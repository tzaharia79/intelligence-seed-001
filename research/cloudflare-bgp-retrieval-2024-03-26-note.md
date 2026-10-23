# Cloudflare PDX01 BGP Cross-Check — Retrieval Result

**Status:** Closed for now; no further Cloudflare retrieval runs planned.
**Incident window examined:** 2024-03-26 14:30–15:30 UTC
**Target:** Cloudflare AS13335
**Workflow run:** [Cloudflare historical BGP analysis, run 2](https://github.com/tzaharia79/intelligence-seed-001/actions/runs/39959418232)
**Artifact:** [cloudflare-bgp-2024-03-26](https://github.com/tzaharia79/intelligence-seed-001/actions/runs/39959418232/artifacts/12504827451)
**Incident reference:** Cloudflare's postmortem says its PDX01 facility lost power at 14:58 UTC on 2024-03-26.

## What was actually retrieved

The artifact contains seven files: one analysis manifest, four per-timestamp BGP-state error records, one routing-history response, and one route CSV.

- **Routing-history request:** HTTP 200 / API status `ok`; response was valid JSON. Its `data.by_origin` array was empty, so the generated route CSV contains only its header and zero route rows.
- **Important measurement limitation:** the response reports `time_granularity: 28800` seconds (8 hours) even though the requested window was one hour. The endpoint response therefore does not provide a useful minute-scale view of this incident window. The query also excluded routes seen by fewer than 10 RIS full-feed peers.
- **Four BGP-state snapshots:** requests for 14:30, 14:58, 15:05 and 15:30 UTC each failed after four attempts. The recorded failures were read timeouts and HTTP 502 Bad Gateway responses.
- **Workflow:** the GitHub Actions job concluded successfully because it completed the bounded retrieval procedure and preserved the outputs. The manifest correctly marks the evidence as `partial`, with 1 of 5 requested datasets retrieved and zero history rows.

## Conclusions supported by this artifact

1. The selected RIPEstat routing-history request returned a successful but empty result for the query and visibility filter used.
2. The historical BGP-state endpoint was not retrievable at any of the four requested timestamps during this run.
3. The current RIPEstat query/response combination is inadequate to test minute-scale route changes around this incident: the response advertises eight-hour time granularity, and all four timestamp snapshots are missing.
4. The retrieval workflow now preserves failures and partial results, making the limitation auditable rather than silently treating missing data as a negative finding.

## Conclusions not supported

- We **cannot** conclude that Cloudflare's routes remained stable, changed, or were unaffected by the power loss.
- We **cannot** infer HTTP reachability, DNS success, latency, customer impact, or data-plane availability from this artifact.
- We **cannot** independently verify Cloudflare's reported recovery times or service-impact claims with this BGP sample.
- The empty history array is not evidence that no route change occurred; it may reflect query granularity, visibility filtering, source coverage, or the behavior of the endpoint.

## Decision

Close this BGP cross-check as **inconclusive due to measurement/source limitations**. Do not schedule another Cloudflare-specific run for this project branch. Preserve the artifact and this interpretation as the final result of the current sample.

Continue the Cloudflare case using the operator postmortem and existing external records with clear attribution, and move research effort to a different sample that can be evaluated from already available sources. Any future reopening should require a materially different source or a clearly improved measurement design—not merely another retry of the same RIPEstat requests.

## Source links

- [Cloudflare postmortem: Major data center power failure again](https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/)
- [Cloudflare status incident](https://www.cloudflarestatus.com/incidents/b31dxdz60366)
- [RIPEstat routing-history API documentation](https://stat.ripe.net/docs/data-api/api-endpoints/routing-history)
- [RIPEstat BGP-state API documentation](https://stat.ripe.net/docs/data-api/api-endpoints/bgp-state)

**Interpretation boundary:** this is a record of what the saved artifact can establish, not a claim about the underlying outage's network behavior.
