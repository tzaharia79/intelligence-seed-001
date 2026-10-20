# Cloudflare Recovery Claims — Independent Evidence Check 01

**Reviewed:** 2026-10-19  
**Incident:** PDX01 power loss, 2024-03-26  
**Question:** Can sources independent of Cloudflare corroborate the reported seven-minute control-plane recovery and uninterrupted global data-plane operation?

## Bottom line

**The central seven-minute recovery claim remains operator-reported, not independently verified in the public material found during this review.** We found external reporting that repeats Cloudflare's account, a corporate regulatory filing that acknowledges the March outage and describes customer impact at a broader level, and public status-history/API infrastructure. We did not find a public third-party measurement report, customer-level incident dataset, independent network-telemetry analysis, or published Flexential root-cause report that directly validates the exact API/dashboard recovery time or the claim that the global data plane was unaffected.

This does not mean the claim is false. It means the public evidence supports a narrower confidence statement: Cloudflare made a specific, internally detailed claim; external sources establish that the incident was publicly reported and affected some services, but do not independently verify the most important recovery metrics.

## Claims and evidence status

| Claim | Evidence found | Independence and limits | Status |
|---|---|---|---|
| PDX01 lost power on March 26, 2024 | Cloudflare's postmortem describes the event and the facility-level power failure; Data Center Dynamics separately reported the incident, largely repeating Cloudflare's statements | External article is editorially independent but relies heavily on Cloudflare's account; no independent facility telemetry located | Corroborated as a publicly reported incident; physical details not independently reconstructed |
| APIs and dashboards returned to normal in seven minutes, without human intervention | Cloudflare postmortem gives times 14:58 and 15:05 UTC; Data Center Dynamics repeats those figures | No independent API probe series, customer traces, or third-party monitoring report found | Operator-reported; not independently verified |
| Global data plane was not impacted | Cloudflare states this directly; external reporting repeats it | No independent global traffic/error-rate analysis tied to the exact incident window found in this pass | Operator-reported; not independently verified |
| Analytics remained impaired for hours | Cloudflare postmortem; Cloudflare's 2024 annual financial filing says the March power failure affected certain customers' access to products for minutes and analytics for several hours | The annual filing is a formal corporate disclosure, but it is not an independent technical measurement or a customer-by-customer dataset | Broad duration/impact corroborated by a second corporate publication, not independent of Cloudflare |
| Facility restoration was faster than in November 2023 | Cloudflare reports cold-start duration fell from roughly 72 hours to roughly 10 hours | No independent facility restoration log or Flexential postmortem found | Operator-reported; not independently verified |
| Electrical switchboard failure and breaker settings caused the facility loss | Cloudflare relays preliminary information from Flexential's investigation | No public Flexential root-cause report found in this review; the account remains second-hand through Cloudflare | Preliminary operator-relayed explanation; do not state as independently established fact |

## Source review

### 1. Cloudflare's March 2024 postmortem — primary source, not independent

Cloudflare, “Major data center power failure (again): Cloudflare Code Orange tested,” March 27, 2024.  
https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/

This is the source for the exact timeline, automatic failover, continued data-plane operation, analytics degradation, Code Orange work, and facility cold-start comparison. It gives a detailed first-party account, but Cloudflare is also the operator whose resilience claims are being evaluated.

### 2. Data Center Dynamics — independent publication, mostly secondary evidence

“Cloudflare suffers second power outage at Flexential data center in Oregon in six months,” March 2024.  
https://www.datacenterdynamics.com/en/news/cloudflare-suffers-second-power-outage-at-flexential-data-center-in-oregon-in-six-months/

This is a separately published industry report and establishes that the incident and Cloudflare's recovery claim were reported externally. For the seven-minute timeline and no-data-plane-impact statement, it quotes or paraphrases Cloudflare. It is **not** independent telemetry validating the claim.

### 3. Cloudflare 2024 annual financial filing — formal disclosure, not independent technical verification

Cloudflare's 2024 annual filing says the November 2023 outage affected certain customers' access to products for several days and resulted in loss of some customer logs; the March 2024 power failure affected certain customers' access to some products for minutes and analytics for several hours.  
https://cloudflare.net/files/doc_financials/2024/q4/2c5ce18c-bb02-4031-89cb-59ff64f22eaf.pdf

This is useful because the company describes the incidents in a formal corporate risk disclosure, using broader language about customer impact. However, it is another Cloudflare-authored source and does not validate the exact seven-minute figure or uninterrupted data-plane operation independently.

### 4. Cloudflare Status API and incident history — potential research route, not yet confirmation

Status API documentation: https://www.cloudflarestatus.com/api  
Dashboard incident history: https://www.cloudflarestatus.com/history?service=Dashboard

Cloudflare publishes a status API and historical incident page. In this review, we did not retrieve a preserved, incident-specific independent monitoring record that could establish API availability minute-by-minute on March 26, 2024. The status page is also operator-managed, so even a historical status entry would corroborate published status, not substitute for external probes.

### 5. Flexential root-cause report — unresolved

The public material reviewed did not yield a published Flexential post-incident root-cause analysis for the March 2024 PDX01 event. Cloudflare's account attributes the initial electrical explanation to Flexential engineers, but this research should not treat the breaker-setting explanation as independently confirmed.


### 6. Contemporaneous public status notice — useful for impact scope, not independent measurement

A community support forum preserved the March 26 Cloudflare status notice at 15:13 UTC: Cloudflare was investigating dashboard/API issues, and the notice said the problem did not affect cached-file delivery through the CDN or security features at the Cloudflare edge. The forum entry is here: https://community.centminmod.com/threads/cloudflare-dashboard-and-cloudflare-api-service-issues.24824/ . A corresponding Cloudflare status incident identifier appears as https://www.cloudflarestatus.com/incidents/b31dxdz60366 .

This is useful evidence that, near the event, the publicly reported failure was scoped to dashboard/API access rather than described as a general CDN/security-edge outage. But the underlying status notice was authored by Cloudflare; a community repost is not independent telemetry. It corroborates the **contemporaneous declared scope**, not the actual availability of every data-plane route or the exact seven-minute recovery interval.

## What would count as stronger independent evidence?

Prioritize, in order:

1. **Third-party synthetic monitoring** with timestamped checks of the Cloudflare dashboard/API during 14:50–15:20 UTC on March 26, 2024, including probe locations, test endpoints, and response codes.
2. **Independent data-plane telemetry** for Cloudflare-hosted or proxied traffic during the same interval: traffic volume, HTTP error rates, latency, BGP reachability, DNS responses, and sampling methodology.
3. **Customer-side incident reports** that separate inability to change configuration from live traffic impact and timestamp each observed symptom. These are useful corroboration but may not generalize to all customers.
4. **Flexential's facility incident report** or a regulator/insurer/commissioning report establishing the power failure mechanism and restoration timeline.
5. **Status history snapshots or archived status API responses** captured contemporaneously. These help reconstruct what was publicly reported, but are not independent measurements of customer experience.

No contact with Cloudflare, Flexential, customers, or researchers was made. The search was limited to public material.


## Follow-up search — archived monitoring, network measurements, customer reports, facility documentation

**Follow-up date:** 2026-10-19  
**Scope:** Public-source search for archived synthetic checks, network/routing observations, customer-side reports, and Flexential facility documentation. No operator contact was made.

### A. Synthetic monitoring and status archives

- Cloudflare's public status API documents incident endpoints and historical status access: https://www.cloudflarestatus.com/api . Its history is useful for reconstructing what the operator declared, but the status data itself is operator-authored.
- The March incident was preserved under status incident identifier `b31dxdz60366`: https://www.cloudflarestatus.com/incidents/b31dxdz60366 . Search results identify a contemporaneous status notice scoped to dashboard/API issues and state that cached-file delivery via the CDN and edge security features were not affected. A community support forum also preserved the notice: https://community.centminmod.com/threads/cloudflare-dashboard-and-cloudflare-api-service-issues.24824/ . These are evidence of contemporaneous reported scope, not independent synthetic checks.
- IsDown says it has monitored Cloudflare since April 2020, but its stated method includes monitoring Cloudflare's official status page and user reports: https://isdown.app/status/cloudflare . StatusGator similarly combines official status data, user reports, and other signals: https://statusgator.com/services/cloudflare . Public pages surfaced during this pass did not expose timestamped third-party probe results for the March 26, 2024 14:50–15:20 UTC window.
- One contemporaneous WordPress.org support thread says a site's analytics data stopped during the dashboard/API issue and later resumed: https://wordpress.org/support/topic/site-kit-connected-correctly-and-no-data-in-analytics/ . This is a customer-side report consistent with an analytics/control-plane effect, but it is anecdotal and does not test data-plane availability.

**Finding:** A historical synthetic monitoring run cannot be performed now against the 2024 event. We would need archived probes or retained monitoring logs from a provider such as Catchpoint, ThousandEyes, Pingdom, Datadog Synthetics, or a customer-operated monitor. None was found publicly in this pass. A new live test today could validate present-day endpoints, not reconstruct the incident.

### B. Network and routing measurements

- RIPE RIS collects BGP routing announcements and withdrawals from distributed route collectors and publishes historical MRT data: https://www.ripe.net/analyse/internet-measurements/routing-information-service-ris/ .
- RIPEstat documents BGPlay for examining BGP route updates over a selected historical window: https://data.stat.ripe.net/docs/data-api/api-endpoints/bgplay and routing history: https://data.stat.ripe.net/docs/data-api/api-endpoints/routing-history .
- The public web retrieval available for this pass did not yield a successful, reproducible raw-data query for AS13335 in the March 26 2024 incident window. Therefore **no BGP result is asserted here**. The next measurement step is to query RIS/RV collectors for Cloudflare-announced prefixes and AS13335 around 14:30–15:30 UTC, archive the query parameters and raw result, and compare route visibility/update rates with matched control windows before and after the event.
- Important interpretation limit: absence of a global BGP withdrawal would not prove the data plane was unaffected. Cloudflare uses a distributed anycast network; losing one facility or location can be masked by other locations continuing to announce/serve the same prefixes. BGP data can test for routing withdrawal or instability, but cannot by itself establish HTTP success, latency, error rates, or customer impact at the edge. Ideally pair routing observations with independent HTTP/DNS/TLS probes and customer-side traffic/error data.

**Finding:** Historical BGP archives are a viable independent measurement source, but this pass has identified the method rather than completed and verified the raw-data analysis. Treat network measurement as **open**, not as a negative finding.

### C. Customer-side incident reports

The WordPress support thread above is the clearest contemporaneous third-party report found in this pass. It links the disappearance of a site's analytics data to the dashboard/API issue and says data later returned. It supports the claim that some users experienced an analytics effect, but:
- it does not identify the site's plan, region, or exact test method;
- the author inferred the relationship from timing;
- it does not measure Cloudflare-proxied traffic availability;
- it cannot establish how broadly the effect was distributed.

No sufficiently detailed customer postmortem with independently timestamped HTTP error rates or data-plane traffic measurements was located. Search absence should not be interpreted as proof none exists.

### D. Facility documentation and root-cause evidence

No public Flexential-authored incident report, electrical forensic report, regulator filing, or facility restoration log specific to the March 26, 2024 PDX01 event was located. Cloudflare's account relays Flexential engineers' investigation of four circuit switchboards and says incorrectly configured breaker-coordination settings were an initial suspected contributor. Data Center Dynamics' coverage repeats this account rather than presenting a separate facility investigation: https://www.datacenterdynamics.com/en/news/cloudflare-suffers-second-power-outage-at-flexential-data-center-in-oregon-in-six-months/ .

Flexential's current public Portland/Hillsboro facility page is general marketing/service information, not an incident report: https://www.flexential.com/data-centers/portland-hillsboro-5 .

**Finding:** Facility mechanism, precise restoration sequence, and the reported breaker-setting contribution remain unverified by an independent public facility document in this search.


## Reproducible BGP analysis package — 2026-10-19

A standard-library Python script has been added at [`scripts/analyze_ripe_bgp_cloudflare_2024_03_26.py`](../scripts/analyze_ripe_bgp_cloudflare_2024_03_26.py). It queries RIPEstat's documented `routing-history` endpoint for AS13335 over 2024-03-26 14:30–15:30 UTC and requests BGP-state snapshots at 14:30, 14:58, 15:05, and 15:30 UTC. It saves raw JSON responses, a CSV of route timelines, and a JSON manifest containing retrieval timestamps and exact request URLs.

**Important execution status:** The script is committed, but it has **not yet completed a successful data retrieval in this environment**. Direct network access from the execution container failed, and the web retrieval interface could not open the parameterized RIPEstat API URLs. No raw response files or empirical route findings are claimed. The script is a reproducible analysis path, not a completed analysis. Run it in an environment with outbound HTTPS access:
```bash
python3 scripts/analyze_ripe_bgp_cloudflare_2024_03_26.py
```
Default outputs go to `results/cloudflare-bgp-2024-03-26/`. Preserve the raw responses and manifest alongside any interpretation. Review route counts/visibility at each timestamp, inspect route changes against a matched control period, and document collector coverage. The script's state snapshots use RIPEstat's documented reconstruction from an earlier RIB snapshot plus subsequent observed updates; they are not direct packet or HTTP measurements.

**Interpretation boundary:** The RIPEstat routing-history endpoint documents route announcement timelines, visibility, and peer counts; the BGP-state endpoint reconstructs route state at a timestamp. These can detect visible routing changes or instability, but cannot prove that HTTP requests succeeded, that latency was normal, or that no customer traffic was affected. A stable global route view is compatible with a local facility failure in a distributed anycast network.

API documentation:
- Routing history: https://data.stat.ripe.net/docs/data-api/api-endpoints/routing-history
- BGP state: https://stat.ripe.net/docs/data-api/api-endpoints/bgp-state
- Raw RIS MRT files for deeper collector-level work: https://www.ris.ripe.net/docs/mrt/

**Next pairing step:** Once the script is run and raw data reviewed, search for independent archived HTTP/DNS/TLS probes in the same UTC window and record probe location, target, interval, error codes, and retention/source details. Do not merge BGP visibility with application monitoring into a single claim unless timestamps and measurement scope align.

## Updated evidence disposition

| Evidence path | Result of this pass | Confidence consequence |
|---|---|---|
| Archived synthetic monitoring | No timestamped independent probe dataset found | Exact seven-minute recovery remains operator-reported |
| Status page/archive | Contemporaneous status notice found, but operator-authored | Supports declared incident scope only |
| Network measurements | RIPE RIS/BGPlay method identified; raw query not successfully retrieved/verified here | No BGP conclusion; follow-up remains open |
| Customer reports | One anecdotal analytics-impact report found | Limited corroboration of analytics symptoms, not data-plane continuity |
| Facility documentation | No public Flexential root-cause or restoration report found | Physical root-cause explanation remains second-hand |
| Independent news coverage | DCD reports event, largely citing Cloudflare | Confirms external reporting, not independent technical validation |

The appropriate overall label remains: **“Detailed operator-reported recovery, externally reported and partly consistent with anecdotal customer evidence; exact recovery and data-plane claims not independently measured in this review.”**

## Glossary application

- **Baseline/counterfactual:** The November 2023 incident is the observed earlier outcome; March 2024 is the later outcome after multiple changes. The counterfactual—March without remediation—is unobservable.
- **Capability extension:** The operator reports improved continuity of an existing control-plane function. Independent measurement of the size and distribution of that improvement is still missing.
- **Capability recombination:** High-availability configuration databases, pre-provisioned capacity, automatic failover, and cut testing are described as interacting. Their separate causal contributions are not isolated.
- **Possibility-space change:** Not established.
- **System-level organization:** The case concerns architecture across facility, control plane, data plane, analytics, and recovery procedures.
- **B/M/D/A/F/T rubric:** Keep prior scores provisional and operator-source-dependent. Do not raise confidence merely because the same claim appears in a news article that quotes the postmortem.

## Provisional conclusion

The best honest label is **“detailed operator-reported recovery, externally reported but not independently measured.”** Cloudflare's 2024 annual filing broadly corroborates that the March outage had minutes-scale product impacts and hours-scale analytics impacts, but it is not an independent source. The exact seven-minute API/dashboard recovery and uninterrupted global data-plane claims remain unverified by independent public telemetry in this pass.

For the project, retain the case as a useful remediation/containment example with a clearly marked source limitation. Do not upgrade it to independently verified evidence unless new data is found. This distinction is itself important to the research method: multiple publications repeating one source do not constitute multiple independent observations.
