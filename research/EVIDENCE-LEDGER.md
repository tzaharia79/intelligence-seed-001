# Evidence Ledger — Intelligence Seed 001

**Working version:** 0.1  
**Started:** 2026-10-17  
**Purpose:** Track claims, supporting and conflicting evidence, confidence, and revision decisions.  
**Status:** Initial ledger; entries are preliminary and should be updated after full-text review.

## Rating key

- **High:** multiple convergent lines of direct evidence or a mature empirical/technical literature support the narrowly stated claim.
- **Moderate:** credible evidence supports the claim, but scope, interpretation, or generalizability remains contested.
- **Low / open:** evidence is indirect, incomplete, or the claim is currently too vague to test.
- Confidence applies only to the specific wording of the claim, not to the whole seed.

## Ledger

| ID | Claim | Current assessment | Evidence supporting it | Limitations / counterevidence | Next action |
|---|---|---|---|---|---|
| E-01 | Biological organisms acquire, retain, and use information in ways relevant to behavior. | High for narrowly defined learning/cognition in studied organisms. | Dukas (2004), review of evolutionary biology of animal cognition: https://doi.org/10.1146/annurev.ecolsys.35.112202.130152 | "Information processing" is broader than "intelligence"; taxa and methods vary. Does not establish a universal intelligence scale or evolutionary goal. | Add newer reviews across microbial, plant, and animal systems; define terms separately. |
| E-02 | Some cognitive tasks are distributed across people, artifacts, and coordinated practices. | High as a descriptive claim in studied systems. | Hutchins (1995), *Cognition in the Wild*: https://doi.org/10.7551/mitpress/1881.001.0001 | Does not imply every network is a mind or that system boundaries are settled. | Identify operational criteria for distributed task performance versus stronger extended-mind claims. |
| E-03 | External resources can, under some theories and conditions, count as parts of cognitive processes. | Moderate; influential, contested theoretical claim. | Clark & Chalmers (1998), "The Extended Mind": https://doi.org/10.1111/1467-8284.00096 | Philosophical and conceptual debate over coupling, access, reliability, and boundaries. | Include major critiques and clarify that the seed need not endorse a literal extended-mind ontology. |
| E-04 | Some evolutionary transitions alter the organization of information, cooperation, or what cognitive capabilities can evolve. | Moderate-to-high for specific documented biological transitions; not a universal law of progress. | West et al. (2015), major transitions in individuality: https://doi.org/10.1073/pnas.1421402112; Barron, Halina & Klein (2023), transitions in cognitive evolution: https://doi.org/10.1098/rspb.2023.0671; Ginsburg & Jablonka (2021): https://doi.org/10.1098/rstb.2019.0766 | Different authors define transitions differently; retrospective selection and disputed examples matter. Evolution is not prospective. | Compare criteria and distinguish "transition" from a vague claim of increased complexity. |
| E-05 | A useful bridge concept could describe changes that expand the reachable range of information processing, coordination, learning, or action. | Low / open; proposed synthesis, not yet validated as a distinct explanatory construct. | Related ideas exist in evolutionary transitions, computational architecture, distributed cognition, and infrastructure studies. | Risk of being a catch-all metaphor that labels successful changes after the fact. | Operationalize before adding more examples; test on positive, negative, and ambiguous cases. |
| E-06 | A transition can matter because it changes what future cognitive capacities become possible, not only because it adds an immediate skill. | Moderate as a theoretical claim in evolutionary cognitive research. | Barron, Halina & Klein (2023): https://doi.org/10.1098/rspb.2023.0671 | Must separate changed possibility space from downstream benefits that evolution could not foresee. | Use this as a candidate criterion for "bridge effect"; seek measurable proxies and critiques. |
| E-07 | Human cognition and coordination are materially extended through language, records, tools, institutions, and technical systems. | High as a broad descriptive claim; individual examples differ. | Hutchins (1995); Clark & Chalmers (1998); research on cultural and informational transitions. | "Externalization" may obscure how tools reshape practices rather than merely move a pre-existing function outside the brain. | Add historical/empirical case studies and clarify which cognitive function changes. |
| E-08 | AI may materially participate in designing or building systems that expand subsequent information-processing capabilities. | Low / open as a broad claim; case-specific evidence required. | No direct evidence established in this initial ledger. Potential domains: software engineering, scientific workflows, chip design, AI-assisted research. | Attribution problems: human expertise, existing automation, compute, data, and organizational inputs may explain outcomes. | Build case-study table with baselines, measured contribution, reproducibility, and negative results. |
| E-09 | AI systems depend on physical infrastructure such as compute hardware, energy, cooling, networks, and supply chains. | High. | IEA (2025), *Energy and AI*: https://www.iea.org/reports/energy-and-ai | Demand and architecture vary; infrastructure dependence alone does not imply goals or moral interests. | Add supply-chain and water/cooling sources; distinguish system-specific requirements. |
| E-10 | Infrastructure interdependence can create both efficiency/cooperation and cascading or common-cause failures. | High as a systems-engineering and governance concern. | OECD (2019), *Good Governance for Critical Infrastructure Resilience*: https://doi.org/10.1787/02f0e5a0-en; NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework | It does not establish that resilience is inherently a shared goal of AI and humans. | Collect concrete cases and assess distribution of benefits, control, and risk. |
| E-11 | Resilience can sometimes support human welfare and reliable AI operations simultaneously, without identical values. | Moderate as a conditional systems hypothesis; case-dependent. | OECD infrastructure resilience guidance; NIST AI RMF. | A shared dependency can also create conflict over resource allocation, control, or acceptable risk. | Identify cases where goals align and conflict; define "shared practical interest" narrowly. |
| E-12 | Life as a whole is best described as an intelligence generator, or intelligence is a direction of existence. | Not established; not treated as an empirical conclusion. | No evidence in this ledger establishes a universal direction or purpose. | Teleological interpretation, survivorship bias, ambiguity in "intelligence," and evolutionary counterexamples. | Keep as a motivating metaphor or reject as an empirical claim unless separately operationalized. |

| E-13 | Reinforcement learning can discover low-level sorting routines that outperform selected human baselines in specified benchmarks, and some were adapted and integrated into LLVM libc++. | High for this narrow, scoped claim. | Mankowitz et al. (2023); AlphaDev source/tests; LLVM review D118029 and commit 194d196; current LLVM source retains branchless small-sort logic. | Performance is type-, comparator-, workload-, compiler-, and architecture-dependent. Neri (2023) challenges a narrow shortest-program claim for Sort3; no downstream possibility-space effect established. | Trace real-world usage and end-to-end effects; keep global optimality and future-capability claims open. |

## Evidence quality notes

1. A source may support only one component of a claim. Do not cite it as proof of the seed's complete thesis.
2. Reviews and theoretical papers are useful for mapping debates; they are not substitutes for primary evidence where empirical claims are made.
3. Record contradictory results and failed cases. The ledger must not become a collection of supportive citations only.
4. Distinguish observed evidence, an author's interpretation, and the seed's own inference.
5. Keep value judgments (what should be protected or optimized) separate from descriptive claims (what depends on what).
6. Confidence should change when evidence changes; it is not a score for how attractive the thesis feels.

## Immediate priorities

1. Operationalize the bridge hypothesis.
2. Compare it with major evolutionary transitions, transitions in cognitive evolution, distributed cognition, and extended-mind theory.
3. Build a case matrix that includes examples, counterexamples, and borderline cases.
4. Research AI-assisted creation of future cognitive infrastructure with explicit attribution standards.
5. Review the sources in full and add counterarguments before treating this as a mature evidence review.

## AlphaDev source-trace update (2026-10-18)

See [AlphaDev Primary-Source Trace — Round 1](ALPHADEV-PRIMARY-SOURCE-TRACE-01.md). The evidence supports a bounded algorithmic capability improvement and adoption into shared software infrastructure. It does not establish a general cognitive transition or altered future possibility space. A 2023 note by Cassio Neri challenges a narrow optimality claim about Sort3; this should remain recorded as counterevidence to “globally best” framing, not as blanket refutation of integration or benchmark results.


## AlphaDev chain closure review (2026-10-18)

See [AlphaDev Evidence Chain — Closure Review 01](ALPHADEV-CHAIN-CLOSURE-01.md). Conclusion: strong evidence for bounded algorithmic discovery, human-reviewed integration, and reusable infrastructure adoption; no established causal downstream capability-space effect. The LLVM review also documents why eligibility had to be constrained and why benchmark input distributions matter. A historical libc++ benchmark pipeline announced in 2026 may enable future retrospective analysis, but it is not itself a remeasurement of the AlphaDev commit.


## Grid reliability case — Northern Virginia load-transfer event (2026-07-22)

**Claim:** Large computational loads can disconnect in response to a grid disturbance in ways that materially affect grid voltage and frequency; grid operators may successfully contain the disturbance.

**Assessment:** Strong for this specific event, based on PJM's operational account; not a general frequency estimate. PJM reports approximately 3,800 MW transferred to backup power after a 230 kV line failure and recovery of the balancing-area control-error limit within nine minutes, with no significant overall reliability impact.

**Primary record:** https://insidelines.pjm.com/pjm-dominion-review-large-load-transfer-event/

**Regulatory context:** FERC large-load integration orders (https://www.ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration); Reuters reporting on PJM registry/curtailment proposal (https://www.reuters.com/business/energy/us-panel-approves-pjms-registry-data-centers-rejects-plan-curtail-power-them-2026-10-12/).

**Counterevidence/limits:** No significant overall reliability impact was reported; the public account is preliminary; affected loads are described as data centres/computational loads, not exclusively AI; one event cannot establish prevalence or prove AI demand caused the event. Shared infrastructure dependence does not establish unified interests or subjective preferences.

**Follow-up:** Seek final technical findings and standards status; examine evidence of data-centre flexibility improving grid operations; trace cost allocation and affected human services in a documented jurisdiction.

See [full case study](GRID-RELIABILITY-CASE-01-NORTHERN-VIRGINIA.md).


## Grid reliability case 02 — flexible compute field demonstration (Phoenix)

**Claim:** Software-managed scheduling of selected AI workloads can reduce a participating cluster's power draw during utility-coordinated peak events while meeting stated service constraints.

**Assessment:** Strong for technical feasibility in the tested setup. A peer-reviewed *Nature Energy* field demonstration reports 25% power reduction for three hours on a 256-GPU cluster at an Oracle Cloud Infrastructure facility in Phoenix, coordinated with APS and SRP, while maintaining AI quality-of-service guarantees. No hardware modifications or energy storage were required for the demonstrated software approach.

**Primary source:** “AI data centres as grid-interactive assets,” *Nature Energy* (2025), https://doi.org/10.1038/s41560-025-01927-1. Accessible abstract/experiment summary: https://www.alphaxiv.org/abs/2507.00909.

**Corroborating operator account:** Google reports ML-workload demand response during three grid events with Omaha Public Power District and additional utility partnerships: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/.

**Limits:** Single site/cluster in the peer-reviewed demonstration; not evidence of 25% whole-facility or grid-wide reduction. The public abstract does not establish avoided outages, lower bills, reduced infrastructure investment, or scale across all workloads. Google accounts are operator-reported. Flexible demand can shift or rebound later and may transfer load to another grid.

**Comparison:** See [Grid Reliability Case Study 02 — Flexible Compute](GRID-RELIABILITY-CASE-02-FLEXIBLE-COMPUTE.md), compared with Case 01 (Northern Virginia load-transfer event).


## Grid flexibility benefits — evidence synthesis (2026-10-18)

**Facility-level claim:** Selected AI workloads can be modulated to reduce a participating cluster's power during defined events while meeting specified service constraints. Evidence: peer-reviewed Phoenix field demonstration on 256-GPU cluster; reported 25% reduction for three hours. https://doi.org/10.1038/s41560-025-01927-1 ; artifacts: https://github.com/ai-emerald/emerald-ai-demo-may-2025.

**Grid-level claim:** Flexibility may make additional large loads compatible with existing system headroom and may ease congestion/contingency operations. Evidence: modeled PJM case estimates up to 32 GW of flexible new load for the 2023 system with curtailment of 0.1% annual energy during 1.2% of hours; limited by relatively mild weather year and model assumptions. https://scholars.duke.edu/publication/1917768. PNNL models potential congestion and contingency services: https://www.pnnl.gov/publications/potential-data-center-controls-grid-services.

**Cost/emissions counterweight:** 2026 multi-region modeling finds system costs fall under modeled flexibility scenarios but emissions may increase up to 3% in Mid-Atlantic/WECC cases and fall up to 40% in Texas scenarios with higher renewable availability. https://doi.org/10.1016/j.isci.2026.116497. Thus, lower costs do not imply lower emissions.

**Status:** Facility power reduction = demonstrated in one setup. Grid-wide benefits = modeled/plausible, not yet verified as realized benefits in an operational outcome audit. Consumer bill savings, avoided blackouts, and universal net benefit = not established. Emissions = conditional and region-dependent.

Full synthesis and evaluation protocol: [Grid Flexibility Benefit Assessment 01](GRID-FLEXIBILITY-BENEFIT-ASSESSMENT-01.md).


## Phoenix artifact inspection — reproducibility and utility-level verification (2026-10-18)

**Facility-level data:** Public supplementary repository lists the SRP total-power time series, workload performance table, utility-demand context, DVFS throughput sweep, and figure source data: https://github.com/ai-emerald/emerald-ai-demo-may-2025. Paper reports 25% cluster power reduction for three hours: https://doi.org/10.1038/s41560-025-01927-1.

**Measurement uncertainty:** Open public issue asks whether the cluster power metric was measured through nvidia-smi; no public response visible on 2026-10-18: https://github.com/ai-emerald/emerald-ai-demo-may-2025/issues/1. The performance table lists weighted normalized performance of 0.909560245, requiring interpretation from the paper's method; this prevents assuming zero performance trade-off.

**Utility-level evidence:** No event-specific independent utility-side evaluation was located in this research pass showing a causal effect on grid peak, congestion, reserves, prices, outages, customer bills, or avoided capacity. Arizona Corporation Commission records are a path for tariff/program context and potential filings, not evidence that this particular test produced grid-level savings.

**Status:** Facility demand flexibility = supported by published field demonstration, pending metric clarification and independent recalculation. Grid/public benefits = not yet verified by event-specific independent utility records.

Full report and draft records-request text: [Phoenix Artifact Inspection and Utility Verification Plan 01](PHOENIX-ARTIFACT-INSPECTION-AND-UTILITY-VERIFICATION-01.md).


## Phoenix CSV direct inspection and utility-record search update (2026-10-18)

**Direct data inspection:** `SRP_total_power.csv` contains 400 one-minute rows from 14:40–21:19 local time on May 4, 2025. The `total` column has no unit in the header. Exploratory means: 14:40–15:13 = 94,035.76; 17:00–18:59 = 63,666.97; 19:00–19:59 = 73,694.51; 20:00–21:19 = 89,525.88. These hand-selected clock windows imply a descriptive 32.3% difference between the first and lower-power windows, but are **not** a reproduction of the paper's 25% result because official event/baseline windows, units, measurement boundary and exclusions are unverified. The series rises again after the lower-power window; causation/rebound cannot yet be determined.

**Performance data:** six workload rows range from normalized 0.666923 to 1.0; weighted value 0.909560245. This requires method context before assigning a precise service-degradation interpretation. Public measurement question remains open with zero comments when checked: https://github.com/ai-emerald/emerald-ai-demo-may-2025/issues/1.

**Public utility/regulatory records:** ACC reports Arizona utility record peaks in August 2025 (context only): https://azcc.gov/news/home/2025/08/09/arizona-electric-utilities-set-record-high-demand--again. SRP says data centres represented 5.1% of its summer 2025 peak and describes minimum-billing rules for new large loads: https://www.srpnet.com/about/data-center-facts. APS describes proposed large-customer cost-allocation/formula rates: https://www.aps.com/en/Utility/Regulatory-and-Legal/Rate-case. FERC directed NERC to submit initial computational-load reliability standards by December 31, 2026: https://www.ferc.gov/news-events/news/summaries-july-2026-commission-meeting. These sources contextualize peak demand, costs, and reliability but do not independently verify benefits from the Phoenix experiment.

**Status:** No public event-specific utility-side measurement-and-verification report was found in this pass that attributes changes in grid peak, congestion, reserves, dispatch cost, reliability, customer bills or avoided infrastructure to the Phoenix demonstration. Do not promote those outcomes as established. See the full inspection report for records pathways and request text.
