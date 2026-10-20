# Network Resilience Case Study 03 — Cloudflare's March 2024 Contained Data-Center Outage

**Research date:** 2026-10-19  
**Incident date:** 2024-03-26  
**Status:** Operator-documented repeat failure at the same facility after a resilience programme; strong before/after operational evidence, with independent verification limits.  
**Purpose:** Add a positive/partial-success case where recovery paths were improved after an earlier outage and then exercised by a similar real-world failure. Uses [GLOSSARY.md](GLOSSARY.md).

## Executive summary

On March 26, 2024, Cloudflare's PDX01 data centre in Portland lost power after failures in four facility-owned switchboards. The loss disabled both primary and redundant power paths serving Cloudflare's equipment in that facility. Cloudflare reported that its control-plane APIs and dashboard returned to normal operation by 15:05 UTC—seven minutes after the power loss—without human intervention. Its global data plane, which handles customer traffic, was not impacted. Some individual services still needed human intervention, and the analytics platform remained impaired until later that day. [1]

The importance of this incident is the comparison with the same provider's November 2023 outage at the same facility. That earlier outage had caused hours of control-plane downtime and prolonged degradation of some services. In response, Cloudflare launched a “Code Orange” reliability programme, moved configuration databases to a highly available topology, provisioned additional capacity across the remaining facilities, improved failover behavior, and performed an internal cut test in February 2024. The March outage then exercised that work under real conditions. [1][2]

This is the strongest candidate so far for a **documented containment and remediation case** in this project: a similar class of facility failure recurred, but a critical recovery outcome improved dramatically. It is not a controlled experiment, and the postmortem is written by the operator. Still, the before/after contrast is stronger than a generic claim that redundancy ought to work. It shows the sequence of failure, targeted changes, a rehearsal, and improved outcome during a subsequent real event.

## Why this is a useful comparison

The November 2023 outage was already recorded as part of [Network Resilience Case Study 02 context](NETWORK-RESILIENCE-CASE-02-AWS-S3-OUTAGE.md) and in the earlier Cloudflare case analysis. In that event, Cloudflare's control plane and analytics were impaired from November 2 to November 4. Cloudflare moved supported control-plane services to a disaster-recovery facility, but that failover encountered a thundering herd of retrying API requests, some services were not supported at the recovery site, and analytics/log processing had gaps. Its network and security data plane nevertheless continued passing traffic. [2]

Cloudflare said the November outage prompted it to prioritize control-plane reliability, including:
- moving configuration databases to a highly available topology;
- pre-provisioning sufficient capacity to absorb a facility loss;
- expanding services' ability to run across the remaining Portland facilities and, where necessary, Europe;
- improving automatic failover;
- requiring more reliable disaster-recovery plans and testing; and
- running an internal cut test before the next incident. [1][2]

This study treats the March 2024 event as the test case for that remediation. It does not treat every element of the broader programme as independently verified or proven effective.

## Incident reconstruction

### 1. The facility failed again

Cloudflare reported that PDX01 lost power at 14:58 UTC on March 26, 2024. Four switchboards serving Cloudflare's equipment reportedly failed simultaneously, disabling both primary and redundant power paths. Cloudflare's postmortem relays an initial assessment that incorrectly set breaker-coordination settings may have contributed to the switchboard failures. That root-cause description is attributed to the operator's account of its provider's investigation, not an independent electrical engineering investigation in this research. [1]

The relevant trigger was at the physical facility/power distribution layer, not a software deployment or an operator command. This made the incident a meaningful test of whether software and service architecture could tolerate loss of an entire facility.

### 2. Automatic failover restored the control plane rapidly

Cloudflare reported that its APIs and dashboards were operating normally by 15:05 UTC—seven minutes after the facility lost power—and that this occurred without human intervention. It attributed the result to work completed after November 2023, including highly available configuration databases and enough pre-provisioned capacity to absorb the loss. The company said services that had experienced at least six hours of control-plane downtime in November were running within minutes during the March incident, with many seeing no impact. [1]

This is evidence for the narrow claim that a prepared, automatic failover path can contain the impact of a repeated facility failure. It is not proof that every service failed over identically or that every customer's experience was uninterrupted.

### 3. The data plane remained operational; analytics did not fully share that resilience

Cloudflare said its global data plane—the network handling customer traffic—was not impacted. Its analytics platform was impacted and was not fully restored until later that day, because analytics remained dependent on PDX01. The company had started building additional analytics capacity after the November outage, but described that work as incomplete at the time of the March event. [1]

This partial result is analytically valuable. The architecture preserved core traffic handling and restored configuration APIs quickly, while a related but distinct observability function remained degraded. Resilience was service-specific, not an all-or-nothing property.

### 4. Rebuilding the failed facility was also faster

Cloudflare reported that cold-starting the large data centre had taken roughly 72 hours in November 2023, whereas in March 2024 it completed the corresponding process in roughly 10 hours. It said more work remained to make the process faster. [1]

This is an operator-reported improvement in a separate recovery metric. It should not be conflated with the seven-minute control-plane recovery: the control plane resumed through failover while the failed facility itself still needed to be rebuilt.

## Before/after comparison

| Outcome | November 2, 2023 | March 26, 2024 | What the comparison suggests |
|---|---|---|---|
| Trigger class | Catastrophic power failure at Cloudflare's Portland facility | Another major power failure at the same facility | Similar class of failure recurred, making this a useful practical comparison |
| API/dashboard recovery | Most control-plane services restored at a disaster-recovery site by 17:57 UTC; outage began around 11:43 UTC | APIs and dashboards normal by 15:05 UTC, seven minutes after 14:58 UTC power loss | Large improvement in the critical management path |
| Human intervention | Failover and restoration required extensive operational work; some services were unsupported at the DR site | Primary API/dashboard recovery happened automatically; a few services still needed human intervention | More failure handling was automated, but not every service was fully independent |
| Global traffic handling | Cloudflare reported network/security traffic continued | Cloudflare reported data plane was not impacted | Core data-plane continuity is a repeated positive outcome, not unique to March |
| Analytics/logging | Significant analytics/logging disruption and persistent gaps for some non-replicated datasets | Analytics remained impaired until later that day | Important recovery gap remained |
| Facility rebuild | Roughly 72 hours to cold-start | Roughly 10 hours | Reported improvement in facility restoration |
| Preparation | Earlier design did not prevent lengthy control-plane outage | Internal cut test in February and Code Orange work preceded the event | Rehearsal and architectural changes plausibly contributed to improved behavior |
| Evidence source | Cloudflare's postmortem | Cloudflare's postmortem | Strong internal timeline, but not an independent causal experiment |

The comparison is more persuasive than comparing two unrelated providers because the same operator and facility were involved. However, the failures may not have been identical in all details, the architecture and service mix may have changed, and this is not a randomized or controlled trial. The before/after difference is consistent with the remediation explanation, but does not isolate the causal contribution of each individual change.

## What worked, what remained weak

### Reported successes

- Automatic control-plane failover restored APIs and dashboards within seven minutes.
- Pre-provisioned capacity in remaining facilities absorbed the loss of PDX01 for the principal management path.
- The global data plane continued to handle customer traffic.
- The February internal cut test had exercised the intended automatic failover before the real event.
- Facility cold-start time reportedly fell from roughly 72 hours to roughly 10 hours.

### Residual gaps and cautions

- Analytics remained dependent on PDX01 and was impaired until later that day.
- A few services still required human intervention.
- The physical switchboard failure demonstrates that nominally redundant power paths can share a common failure mode at a downstream distribution component.
- Cloudflare's postmortem is an operator account. This desk review did not independently inspect telemetry, customer-level impact records, or the provider's electrical forensic report.
- One successful event cannot prove that the design will handle every correlated regional, software, identity, control-plane, or multi-facility failure.

## Applying Tieg's glossary

### Baseline and counterfactual

- **Baseline:** November 2023 provides the earlier observed outcome: long control-plane recovery and prolonged service/analytics effects after facility loss. March 2024 provides the later observed outcome following changes and a cut test.
- **Counterfactual:** We cannot directly observe what would have happened in March without Code Orange changes, nor isolate how much each intervention contributed.
- **System boundary:** Include facility power distribution, service placement, highly available configuration databases, capacity in remaining sites, automatic failover, test procedures, analytics/logging, and human intervention for exceptional services.

### Capability extension, recombination, possibility-space change, system-level organization

- **Capability extension:** The improved architecture extended the ability to keep APIs and dashboards available during loss of a core facility, according to the operator's reported outcome.
- **Capability recombination:** Highly available databases, pre-provisioned capacity, automatic failover, and rehearsed cut tests worked together to preserve the management path.
- **Possibility-space change:** **Not established.** The evidence shows improved reliability of an existing capability, not a new class of future information-processing capability.
- **System-level organization:** The service architecture distributed control-plane work across remaining facilities while keeping the global data plane operating. The analytics result shows that this organization was not uniformly resilient across all functions.

### Does this count as a bridge?

This is a stronger candidate for a resilience-enabling bridge than the outage cases alone: it documents an infrastructure arrangement and tested recovery mechanism preserving a critical capability under a real failure. Still, the claim must remain narrow. The case supports “architectural changes plus rehearsed failover improved continuity for the control plane in this event.” It does not establish a universal bridge law, a change in future possibility-space, or that all architecture coupling is beneficial.

## Qualitative B/M/D/A/F/T desk assessment

The rubric from the glossary is qualitative and unvalidated. These scores apply only to the claim that remediation and rehearsed failover improved containment of a repeated facility failure.

| Dimension | Score | Reason |
|---|---:|---|
| **B — Baseline clarity** | 2 | The November incident provides a documented before-state and the March postmortem describes the changed architecture. |
| **M — Mechanism** | 2 | Cloudflare describes HA configuration databases, provisioned capacity, automatic failover, and prior cut testing. |
| **D — Demonstrated difference** | 2 | Reported control-plane recovery improved from hours to seven minutes; the facility cold-start also shortened. Operator-reported, not independently replicated here. |
| **A — Architectural change** | 2 | Concrete service placement and database availability changes are described. |
| **F — Future capability space** | 0 | No new future capability class is established. |
| **T — Trade-offs** | 2 | Control-plane resilience improved while analytics still depended on the failed facility; resilience investment and capacity costs remain relevant. |

Do not sum these values or treat them as a validated metric. Independent blinded inter-rater validation remains open.

## What the case supports—and does not support

| Claim | Assessment | Boundary |
|---|---|---|
| Recovery architecture can improve after a documented outage and then work during a later similar failure | **Strongly supported for this case** | Operator-reported; not a controlled experiment |
| Automatic failover can restore a critical management path quickly after a facility loss | **Demonstrated by the operator's reported timeline** | Applies to APIs/dashboard, not every service |
| Rehearsal is useful evidence of recovery readiness | **Supported** | February cut test preceded the event; exact causal contribution cannot be isolated |
| Redundancy guarantees all services survive a facility loss | **Not established** | Analytics remained impaired and some services needed manual intervention |
| Data-plane continuity proves all customers were unaffected | **Not established** | The company reports data-plane continuity; control-plane and analytics users still had impacts |
| The March outcome proves each Code Orange intervention was necessary and sufficient | **Not established** | Multiple changes occurred together, with no controlled comparison |
| The case validates a universal bridge hypothesis or unified human–AI goal | **Not established** | It is a specific operational resilience case |

## Practical questions for further study

1. Can published cut-test results show which dependencies are deliberately removed and which service-level recovery objectives are verified?
2. What metrics should be published to distinguish data-plane continuity, control-plane recovery, analytics recovery, and full facility restoration?
3. Which remaining services required human intervention, and what dependencies made automation incomplete?
4. How does resilience change when an entire region, rather than one facility, fails?
5. How are capacity costs, redundancy investments, and service prioritization distributed among the provider and customers?
6. What evidence would independently corroborate the seven-minute API/dashboard recovery and the absence of data-plane impact?

## Sources

**[1] Primary operator postmortem for the March 2024 event**  
Cloudflare, “Major data center power failure (again): Cloudflare Code Orange tested,” 27 March 2024.  
https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/

**[2] Primary operator postmortem for the November 2023 event**  
Cloudflare, “Post mortem on the Cloudflare Control Plane and Analytics Outage,” 4 November 2023.  
https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/

**[3] Independent technical news coverage**  
Data Center Dynamics, “Cloudflare suffers second power outage at Flexential data center in Oregon in six months,” March 2024.  
https://www.datacenterdynamics.com/en/news/cloudflare-suffers-second-power-outage-at-flexential-data-center-in-oregon-in-six-months/

## Provisional conclusion

Cloudflare's March 26, 2024 outage is a compelling positive/partial-containment case because the same facility suffered another major power failure less than five months after a much more damaging event. Following a focused resilience programme and an internal cut test, the operator reported automatic API/dashboard recovery in seven minutes, continued data-plane operation, and a much faster facility rebuild.

The result was not perfect: analytics remained impaired until later that day, and some services still needed human intervention. The evidence is mainly the operator's own postmortem, so causal claims should remain calibrated. Even with those limitations, this case provides a useful concrete contrast with the AWS and Meta failures: **redundancy becomes evidence of resilience when the relevant failure mode is rehearsed and the subsequent real event shows that critical capabilities survive within an explicit recovery boundary.**
