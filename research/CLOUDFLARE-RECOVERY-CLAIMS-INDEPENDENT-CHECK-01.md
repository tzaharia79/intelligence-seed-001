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

## What would count as stronger independent evidence?

Prioritize, in order:

1. **Third-party synthetic monitoring** with timestamped checks of the Cloudflare dashboard/API during 14:50–15:20 UTC on March 26, 2024, including probe locations, test endpoints, and response codes.
2. **Independent data-plane telemetry** for Cloudflare-hosted or proxied traffic during the same interval: traffic volume, HTTP error rates, latency, BGP reachability, DNS responses, and sampling methodology.
3. **Customer-side incident reports** that separate inability to change configuration from live traffic impact and timestamp each observed symptom. These are useful corroboration but may not generalize to all customers.
4. **Flexential's facility incident report** or a regulator/insurer/commissioning report establishing the power failure mechanism and restoration timeline.
5. **Status history snapshots or archived status API responses** captured contemporaneously. These help reconstruct what was publicly reported, but are not independent measurements of customer experience.

No contact with Cloudflare, Flexential, customers, or researchers was made. The search was limited to public material.

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
