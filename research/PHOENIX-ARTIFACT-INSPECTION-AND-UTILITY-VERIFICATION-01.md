# Artifact Inspection and Utility Verification Plan 01 — Phoenix Grid-Interactive AI Demonstration

**Research date:** 2026-10-18  
**Status:** Public artifact inspection completed at repository/document level; detailed numerical reproduction and independent grid-outcome verification remain incomplete.  
**Research question:** What can the published Phoenix field demonstration actually establish, and what utility/system records would verify broader grid benefits?

## 1. Executive finding

The published study and public supplementary repository provide a meaningful, inspectable evidence trail for the facility-level result. The supplementary repository lists one-minute time-stamped total-power measurements for the SRP experiment, per-workload performance data, utility demand context, GPU power-cap throughput sweeps, and Excel data behind the paper's figures.

The data support inspection of the reported cluster response, but the artifact alone does not prove a utility-scale reliability or cost benefit. Publicly accessible materials reviewed in this pass do not supply an independent utility-side evaluation showing changes in system peak, congestion, reserve deployment, wholesale prices, avoided curtailment, or customer bills attributable to the demonstration.

A material reproducibility question is already open in the artifact repository: a user asked which metric underlies the plotted GPU-cluster power values and whether it was measured via nvidia-smi. No answer was visible in the public issue when checked. That question should be resolved before we independently recalculate the reported percentage.

## 2. Sources inspected

### S-01 — Peer-reviewed paper

Colangelo et al., “AI data centres as grid-interactive assets,” *Nature Energy* 11, 254–261 (2026; published online 5 December 2025).  
https://doi.org/10.1038/s41560-025-01927-1

The abstract reports a software-based field demonstration on a 256-GPU cluster at a hyperscale cloud facility in Phoenix. It reports 25% lower cluster power for three hours during peak demand while maintaining AI quality-of-service guarantees, without hardware modifications or energy storage.

**Evidence type:** Peer-reviewed paper with a real-world field demonstration. Authors include participants from Emerald AI, Oracle, NVIDIA, SRP, and EPRI. This partner involvement is relevant context for independence; it does not invalidate the result, but makes independent replication and transparent measurements especially valuable.

### S-02 — Supplementary artifact repository

https://github.com/ai-emerald/emerald-ai-demo-may-2025

The README lists:
- data/SRP_total_power.csv — total power time series for the SRP experiment (401 lines including header).
- data/SRP_exp_performance.csv — scaled performance of workloads in the SRP experiment.
- data/SRP_0503.csv — hourly SRP power-demand data for May 3, 2025.
- data/dvfs_sweep.csv — throughput of power-capped AI workloads on the 256-GPU cluster.
- data/Fig2_data.xlsx and data/Fig345_data.xlsx — data used for figures in the paper.
- Pseudocode and implementation excerpts for the workload orchestration system.

Repository README: https://github.com/ai-emerald/emerald-ai-demo-may-2025  
SRP total-power series: https://github.com/ai-emerald/emerald-ai-demo-may-2025/blob/main/data/SRP_total_power.csv  
Performance data: https://github.com/ai-emerald/emerald-ai-demo-may-2025/blob/main/data/SRP_exp_performance.csv  
Utility-demand context: https://github.com/ai-emerald/emerald-ai-demo-may-2025/blob/main/data/SRP_0503.csv  
Figure data: https://github.com/ai-emerald/emerald-ai-demo-may-2025/tree/main/data

### S-03 — Unresolved measurement-metric question

Public issue: “Could you clarify which metric was used to measure GPU Cluster Power?”  
https://github.com/ai-emerald/emerald-ai-demo-may-2025/issues/1

The issue asks whether the GPU-cluster-power curves were measured through nvidia-smi, as the paper's Measurement section reportedly says. No public answer was visible in the issue when checked on 18 October 2026.

**Implication:** The existence of a time series is not enough. Before reproducing a power-reduction percentage, establish the measurement source, units, sampling/aggregation method, whether readings represent GPU board power or total cluster draw, how non-GPU overhead is treated, and how the baseline window was chosen.

### S-04 — Independent regulator context: Arizona peak demand

The Arizona Corporation Commission reported that APS and SRP set record peak demand in August 2025 and again in 2026.  
2025 report: https://azcc.gov/news/home/2025/08/09/arizona-electric-utilities-set-record-high-demand--again--demand-soars-above-original-forecasts-for-2025  
2026 report: https://www.azcc.gov/news/home/2026/09/23/arizona-power-grid-holds-steady-amid-all-time-high-demand--electric-utilities-break-records--again

This confirms the broader regional importance of peak demand. It does not show that the May 2025 AI workload experiment reduced utility peak demand or changed grid operations.

### S-05 — Arizona Corporation Commission public records

Potentially useful public regulatory records include APS demand-side-management implementation-plan filings and large-load/data-centre workshop materials:
- APS 2026 Demand Side Management Implementation Plan docket E-01345A-25-0106: https://edocket.azcc.gov/search/docket-search/item-detail/29552
- ACC large-load/data-centre workshop summary (April 2026): https://azcc.gov/kevin-thompson/news/2026/04/20/acc-large-load-data-center-workshop-highlights
- ACC electric utility annual reports: https://www.azcc.gov/utilities/industry-types/electric/annual-reports

These are relevant avenues for program design, demand-response definitions, peak forecasts, cost allocation, and utility reporting. They are not, based on the materials located in this pass, event-specific validation of the Emerald AI test.

### S-06 — Federal reliability context

FERC's July 16, 2026 order directs NERC to submit initial reliability standards for computational-load integration by December 31, 2026, with a later workplan for additional standards.  
Order RD26-7-000: https://www.ferc.gov/sites/default/files/2026-07/RD26-7-000.pdf

PJM's September 2026 proposal following the Northern Virginia load-transfer event concerns large-load ride-through behavior and interconnection requirements:  
https://insidelines.pjm.com/reliability-standards-to-manage-large-load-disconnection-events-proposed-by-pjm/

These sources can help assess the counterexample/mitigation branch, but they do not verify positive benefits from the Phoenix demonstration.

## 3. What artifact inspection can and cannot establish

### What it can establish, subject to reproducible recalculation
- A time-series dataset was published for the SRP cluster experiment.
- A workload-performance table was published alongside it.
- The repository provides power-cap throughput sweeps and data used in the paper's figures.
- The paper reports a 25% cluster-power reduction for three hours under utility-coordinated peak events.
- The public performance table lists a weighted performance value of 0.909560245. This should be interpreted only after confirming the authors' normalization and aggregation method; it is not proof of identical throughput or zero performance cost.
- The orchestration pseudocode describes power-cap changes, workload pausing, GPU allocation changes, and restoration to default power after the event.

### What it cannot establish on its own
- That the participating utility's system peak fell by the same percentage.
- That local congestion, reserve deployment, system operating costs, or outage risk changed measurably.
- That customer bills fell or infrastructure investment was avoided.
- That demand did not rebound later or shift to another grid.
- That the result generalizes to other data centres, GPU clusters, workloads, seasons, or utilities.
- That a system-level benefit occurred merely because the experiment was coordinated with a utility.

## 4. Utility records to seek

The most valuable next evidence is an event-level, utility-side record for the APS and SRP demonstrations, ideally corroborated by the participating utility and an independent evaluator.

### Priority A — Ask the study authors / artifact maintainers
Request:
1. A direct answer to the open question about the exact power measurement source and metric.
2. The units and interpretation of the total column in SRP_total_power.csv.
3. Definition of baseline and event windows and calculation of the 25% reduction.
4. Raw or minimally processed per-minute power measurements and any excluded intervals.
5. Whether the series includes only GPU/compute power or also servers, networking, cooling, power conversion, and other facility loads.
6. The detailed meaning of “quality-of-service guarantees,” including workload-specific throughput, latency, job-completion and SLA outcomes.
7. A complete post-event series sufficient to quantify rebound and total energy shifted or avoided.
8. Event signal timestamps and confirmation of what utility/grid condition triggered the test.
9. Whether any utility-side outcomes were measured and, if so, where they are published.

### Priority B — Arizona Public Service and Salt River Project
Ask for public or releasable records associated with the 2025 demonstration:
1. Date, start/end time, and nature of each utility-coordinated event; whether it was a real operational peak event, a utility test, or a scenario replay.
2. Requested MW reduction and delivered MW reduction at the point of interconnection.
3. Baseline method, telemetry interval, response latency, ramp rates, and return-to-baseline behavior.
4. Utility-side system demand and relevant local feeder/substation/constraint data at appropriately aggregated, non-sensitive resolution.
5. Whether the load reduction affected peak demand, congestion, reserve deployment, dispatch, emergency procedures, or wholesale purchases.
6. Any independent verification, settlement, demand-response payment, or measurement-and-verification report.
7. Whether the event was counted in utility demand-response capacity, resource adequacy, or peak planning.
8. Any identified service impacts, exceptions, rebound, or operational limits.

Public contact route / docket pathway:
- APS-related records can be pursued through the Arizona Corporation Commission's eDocket, including the demand-side-management docket above.
- SRP is a community-based, not-for-profit utility and not regulated by the ACC in the same way as APS; ask SRP directly for public technical reports and published board/utility records rather than assuming the ACC docket contains SRP's operational files.

### Priority C — Arizona Corporation Commission
Search the APS rate case and demand-side-management dockets for:
- large-load and data-centre tariff treatment;
- demand-response measurement and verification;
- peak forecasting and load-shape assumptions;
- system benefits, program costs, and who receives any savings;
- treatment of flexible loads in planning and resource-adequacy filings.

The ACC's public docket is a route to regulatory records, not a guarantee that operational telemetry or commercially sensitive facility data will be public.

### Priority D — Independent grid validation
For any event where utility-level benefit is claimed, seek a utility/ISO or independent evaluator's comparison of:
- observed system and local demand against a disclosed baseline;
- relevant local constraint or peak conditions;
- dispatch, reserve, congestion, voltage/frequency, and market-price indicators;
- rebound and load shifting;
- system cost and emissions impacts;
- counterfactual outcome without the intervention.

## 5. Suggested evidence-request text

**Subject:** Request for public technical records on 2025 AI data-centre demand-flexibility demonstration

I am conducting an independent research review of the published Phoenix AI data-centre grid-flexibility demonstration, described in “AI data centres as grid-interactive assets,” *Nature Energy* (2026), DOI 10.1038/s41560-025-01927-1.

I am seeking any publicly releasable technical summary, measurement-and-verification report, or operational record relating to the APS- and/or SRP-coordinated 2025 demonstration. In particular, I would appreciate clarification of the event date and trigger, the requested and delivered MW reduction at the relevant electrical boundary, the baseline and telemetry method, any post-event rebound, and whether utility-side indicators (peak demand, congestion, reserves, dispatch costs, reliability metrics, or customer costs) were measured.

I am not requesting customer-identifying information, security-sensitive grid details, or proprietary facility data. Aggregated or redacted information sufficient to evaluate the claimed system benefits would be valuable. If no utility-side outcome evaluation was conducted, confirmation of that fact would also help prevent overstatement of the evidence.

Thank you for considering this request.

## 6. Next analysis protocol

Before upgrading the evidence grade:
1. Obtain clarification on the power metric and unit.
2. Reproduce the cluster-level reduction from the published series using a documented baseline/event window.
3. Compare the power series with the workload-performance series and quantify service trade-offs.
4. Quantify rebound and total energy over a longer window, not just event-period power.
5. Obtain utility-side records or explicitly mark them unavailable.
6. Keep the benefit categories separate: facility performance, grid operation, customer cost, emissions, and public reliability.
7. Record source independence and uncertainty.

## Provisional conclusion

The Phoenix study's public artifacts make its facility-level claim more inspectable than a press release alone. The data repository is a useful resource, but one key measurement-definition question is publicly unresolved, and the public material located so far does not independently verify utility-scale benefits.

The most defensible present conclusion is therefore: **the demonstration provides credible evidence of technical demand flexibility at the participating cluster, while the broader grid and public benefits remain unverified by event-specific independent utility records.** The next step is to obtain measurement clarification and utility-side evidence before assigning stronger benefit claims.
