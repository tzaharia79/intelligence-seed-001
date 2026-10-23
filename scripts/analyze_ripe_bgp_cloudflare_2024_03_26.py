#!/usr/bin/env python3
"""Resilient RIPEstat BGP retrieval for the Cloudflare AS13335 incident window.

Writes raw responses, per-request errors, CSV timelines, and a manifest under
results/cloudflare-bgp-2024-03-26/. Read analysis-manifest.json's status before
interpreting results. BGP visibility does not measure HTTP success, latency,
DNS success, or customer impact.
"""
import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://stat.ripe.net/data"
ASN = "AS13335"
START = "2024-03-26T14:30:00Z"
END = "2024-03-26T15:30:00Z"
CHECKS = [
    "2024-03-26T14:30:00Z",
    "2024-03-26T14:58:00Z",
    "2024-03-26T15:05:00Z",
    "2024-03-26T15:30:00Z",
]
OUT = Path("results/cloudflare-bgp-2024-03-26")
MAX_ATTEMPTS = 4
TIMEOUT_SECONDS = 75
BACKOFF_SECONDS = (2, 5, 12)


def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class RetrievalError(RuntimeError):
    def __init__(self, url, label, attempts):
        self.url = url
        self.label = label
        self.attempts = attempts
        super().__init__(
            f"{label} failed after {len(attempts)} attempts: "
            f"{attempts[-1].get('error', 'unknown error')}"
        )


def fetch(endpoint, params, label):
    """Return URL, parsed JSON, and attempt log; retry transient errors boundedly."""
    url = f"{BASE}/{endpoint}/data.json?{urlencode(params)}"
    attempts = []
    for attempt in range(1, MAX_ATTEMPTS + 1):
        started = datetime.now(timezone.utc).isoformat()
        req = Request(url, headers={
            "User-Agent": "intelligence-seed-001-research/1.1",
            "Accept": "application/json",
        })
        try:
            with urlopen(req, timeout=TIMEOUT_SECONDS) as response:
                raw = response.read()
                http_status = getattr(response, "status", 200)
            obj = json.loads(raw)
            if obj.get("status") == "error":
                raise RuntimeError(f"RIPEstat API returned status=error: {obj}")
            attempts.append({
                "attempt": attempt, "started_at_utc": started,
                "result": "success", "http_status": http_status,
                "response_bytes": len(raw),
            })
            return url, obj, attempts
        except (TimeoutError, URLError, HTTPError, json.JSONDecodeError, RuntimeError, OSError) as exc:
            attempts.append({
                "attempt": attempt, "started_at_utc": started,
                "result": "error", "error": repr(exc),
            })
            if attempt < MAX_ATTEMPTS:
                delay = BACKOFF_SECONDS[min(attempt - 1, len(BACKOFF_SECONDS) - 1)]
                attempts[-1]["retry_delay_seconds"] = delay
                time.sleep(delay)
    raise RetrievalError(url, label, attempts)


def record_request(manifest, label, url, filename, attempts, status):
    manifest["requests"].append({
        "label": label, "url": url, "file": filename,
        "status": status, "attempts": attempts,
    })


def save_error(manifest, label, error):
    filename = label + ".error.json"
    write_json(OUT / filename, {
        "label": label, "url": error.url, "error": str(error),
        "attempts": error.attempts,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
    })
    record_request(manifest, label, error.url, filename, error.attempts, "failed")
    manifest["errors"].append({
        "label": label, "error_file": filename, "message": str(error),
    })


def write_route_csv(rows):
    fields = [
        "origin", "prefix", "starttime_utc", "endtime_utc",
        "full_peers_seeing", "visibility",
    ]
    with (OUT / "route-timelines.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "asn": ASN,
        "window_start_utc": START,
        "window_end_utc": END,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "incident_reference": "Cloudflare says PDX01 lost power at 2024-03-26T14:58:00Z",
        "caveat": "BGP route visibility does not establish HTTP success, latency, DNS success, or customer impact.",
        "retrieval_policy": {
            "max_attempts_per_request": MAX_ATTEMPTS,
            "timeout_seconds_per_attempt": TIMEOUT_SECONDS,
            "backoff_seconds": list(BACKOFF_SECONDS),
            "partial_results_preserved": True,
        },
        "requests": [],
        "errors": [],
        "history_row_count": None,
        "state_snapshots": [],
        "status": "in_progress",
    }
    successful_datasets = 0
    history_label = "routing-history"
    history_file = "routing-history.raw.json"
    try:
        url, history, attempts = fetch("routing-history", {
            "resource": ASN, "starttime": START, "endtime": END,
            "normalise_visibility": "true", "min_peers": "10",
        }, history_label)
        write_json(OUT / history_file, history)
        record_request(manifest, history_label, url, history_file, attempts, "success")
        rows = []
        for origin in history.get("data", {}).get("by_origin", []):
            for prefix in origin.get("prefixes", []):
                for segment in prefix.get("timelines", []):
                    rows.append({
                        "origin": origin.get("origin", ""),
                        "prefix": prefix.get("prefix", ""),
                        "starttime_utc": segment.get("starttime", ""),
                        "endtime_utc": segment.get("endtime", ""),
                        "full_peers_seeing": segment.get("full_peers_seeing", ""),
                        "visibility": segment.get("visibility", ""),
                    })
        manifest["history_row_count"] = len(rows)
        successful_datasets += 1
    except RetrievalError as exc:
        save_error(manifest, history_label, exc)
        rows = []
    # A predictable CSV exists even if history failed; consult the manifest
    # before interpreting a header-only CSV as a genuine empty result.
    write_route_csv(rows)
    manifest["route_csv"] = "route-timelines.csv"

    # Each snapshot is independent: one failure cannot discard other results.
    for stamp in CHECKS:
        label = "bgp-state-" + stamp.replace(":", "").replace("-", "")
        filename = label + ".raw.json"
        try:
            url, state, attempts = fetch(
                "bgp-state", {"resource": ASN, "timestamp": stamp}, label
            )
            write_json(OUT / filename, state)
            record_request(manifest, label, url, filename, attempts, "success")
            data = state.get("data", {})
            manifest["state_snapshots"].append({
                "requested_timestamp_utc": stamp,
                "status": "retrieved",
                "query_time": data.get("query_time"),
                "route_record_count": len(data.get("bgp_state", [])),
                "file": filename,
            })
            successful_datasets += 1
        except RetrievalError as exc:
            save_error(manifest, label, exc)
            manifest["state_snapshots"].append({
                "requested_timestamp_utc": stamp,
                "status": "failed",
                "error_file": label + ".error.json",
            })

    if successful_datasets == 0:
        manifest["status"] = "retrieval_failed"
        manifest["interpretation"] = (
            "No empirical conclusion: all requested data retrievals failed. "
            "Inspect per-request error files and retry later."
        )
        exit_code = 2
    elif manifest["errors"]:
        manifest["status"] = "partial"
        manifest["interpretation"] = (
            "Partial data retrieval. Inspect each request status and error file; "
            "do not treat missing snapshots or empty route history as evidence of no route change. "
            "Compare available results with matched control periods and collector coverage. "
            "BGP does not establish HTTP success or customer impact."
        )
        # Exit zero when the script completed and preserved partial outputs;
        # the manifest status, not the process exit code, indicates completeness.
        exit_code = 0
    else:
        manifest["status"] = "retrieved"
        manifest["interpretation"] = (
            "All requested data retrieved. Compare route visibility and snapshots across the "
            "incident window and matched control periods. Check collector coverage and raw updates "
            "before drawing conclusions. No withdrawals does not mean no traffic impact."
        )
        exit_code = 0

    manifest["successful_dataset_count"] = successful_datasets
    manifest["expected_dataset_count"] = 1 + len(CHECKS)
    manifest["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
    write_json(OUT / "analysis-manifest.json", manifest)
    print(json.dumps(manifest, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
