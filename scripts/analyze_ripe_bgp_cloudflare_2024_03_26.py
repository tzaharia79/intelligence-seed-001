#!/usr/bin/env python3
"""Reproducible RIPEstat BGP snapshot/history retrieval for Cloudflare AS13335.

Run: python3 scripts/analyze_ripe_bgp_cloudflare_2024_03_26.py
Saves raw JSON and a manifest under results/cloudflare-bgp-2024-03-26/.
BGP visibility is not a measurement of HTTP success or customer impact.
"""
import csv, json, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://stat.ripe.net/data"
ASN = "AS13335"
START = "2024-03-26T14:30:00Z"
END = "2024-03-26T15:30:00Z"
CHECKS = ["2024-03-26T14:30:00Z", "2024-03-26T14:58:00Z",
          "2024-03-26T15:05:00Z", "2024-03-26T15:30:00Z"]
OUT = Path("results/cloudflare-bgp-2024-03-26")

def fetch(endpoint, params):
    url = f"{BASE}/{endpoint}/data.json?{urlencode(params)}"
    req = Request(url, headers={"User-Agent":"intelligence-seed-001-research/1.0",
                                "Accept":"application/json"})
    error = None
    for attempt in range(3):
        try:
            with urlopen(req, timeout=45) as response:
                raw = response.read()
            obj = json.loads(raw)
            if obj.get("status") == "error":
                raise RuntimeError(str(obj))
            return url, obj
        except Exception as exc:
            error = repr(exc)
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"Could not retrieve {url}: {error}")

def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "asn": ASN, "window_start_utc": START, "window_end_utc": END,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "incident_reference": "Cloudflare says PDX01 lost power at 2024-03-26T14:58:00Z",
        "caveat": "BGP route visibility does not establish HTTP success, latency, DNS success, or customer impact.",
        "requests": [], "status": "in_progress"
    }
    try:
        url, history = fetch("routing-history", {
            "resource": ASN, "starttime": START, "endtime": END,
            "normalise_visibility": "true", "min_peers": "10"
        })
        write_json(OUT / "routing-history.raw.json", history)
        manifest["requests"].append({"url":url, "file":"routing-history.raw.json"})
        rows = []
        for origin in history.get("data", {}).get("by_origin", []):
            for prefix in origin.get("prefixes", []):
                for segment in prefix.get("timelines", []):
                    rows.append({
                        "origin":origin.get("origin",""),
                        "prefix":prefix.get("prefix",""),
                        "starttime_utc":segment.get("starttime",""),
                        "endtime_utc":segment.get("endtime",""),
                        "full_peers_seeing":segment.get("full_peers_seeing",""),
                        "visibility":segment.get("visibility","")
                    })
        with (OUT / "route-timelines.csv").open("w", newline="", encoding="utf-8") as f:
            writer=csv.DictWriter(f, fieldnames=["origin","prefix","starttime_utc","endtime_utc","full_peers_seeing","visibility"])
            writer.writeheader(); writer.writerows(rows)
        manifest["history_row_count"] = len(rows)
        manifest["state_snapshots"] = []
        for stamp in CHECKS:
            url, state = fetch("bgp-state", {"resource":ASN,"timestamp":stamp})
            filename = "bgp-state-" + stamp.replace(":","").replace("-","") + ".raw.json"
            write_json(OUT / filename, state)
            data = state.get("data", {})
            manifest["requests"].append({"url":url,"file":filename})
            manifest["state_snapshots"].append({
                "requested_timestamp_utc":stamp,
                "query_time":data.get("query_time"),
                "route_record_count":len(data.get("bgp_state",[])),
                "file":filename
            })
        manifest["status"] = "retrieved"
        manifest["interpretation"] = (
            "Compare route visibility and snapshots across the incident window and matched control periods. "
            "Check collector coverage and raw updates before drawing conclusions. No withdrawals does not mean no traffic impact."
        )
        write_json(OUT / "analysis-manifest.json", manifest)
        print(json.dumps(manifest, indent=2))
        return 0
    except Exception as exc:
        manifest["status"] = "retrieval_failed"
        manifest["error"] = str(exc)
        manifest["interpretation"] = "No empirical conclusion: data retrieval did not complete."
        write_json(OUT / "analysis-manifest.json", manifest)
        print(json.dumps(manifest, indent=2))
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
