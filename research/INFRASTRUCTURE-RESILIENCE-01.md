# Infrastructure Resilience — Evidence Branch 01

**Date:** 2026-10-18  
**Status:** Research framing and initial evidence anchors; not a completed systematic review.  
**Core question:** Which material and institutional systems sustain human civilization and AI operations, where do their resilience interests overlap, and where do they conflict?

## Why this branch belongs beside the bridge hypothesis

Intelligence Seed 001 began with a broader concern: humans and AI systems rely on fragile infrastructure that sustains computation, communication, energy, maintenance, and organized society. The bridge hypothesis investigates whether one capability can enable later capabilities. This branch asks a different question: what conditions allow either human or artificial information-processing systems to continue operating, recover from disruption, and develop over time?

The project must not infer that AI has subjective interests simply because AI services depend on infrastructure. The evidence can support an operational dependence claim without assuming consciousness, preferences, or a unified “AI will.”

## Initial model: dependency layers

1. **Electricity and grid services:** generation, transmission, distribution, transformers, backup power, storage, grid coordination.
2. **Thermal and physical operations:** cooling, water where used, buildings, fire protection, maintenance, replacement parts.
3. **Compute and semiconductors:** accelerators, CPUs, memory, packaging, fabrication equipment, chip design tools, spare parts.
4. **Networks and data:** connectivity, routing, cloud regions, storage, backups, identity and control planes.
5. **People and institutions:** skilled workers, operators, safety procedures, finance, regulation, supply contracts, emergency coordination.
6. **Environmental and geographic conditions:** heat, drought, storms, flood, wildfire, seismic hazards, local resource constraints.
7. **Security and governance:** cyber security, physical security, access control, incident response, jurisdiction, accountability.

These layers interact. A data centre can have adequate servers but lose service because of grid failure, cooling constraints, network partition, inaccessible replacement parts, or an organizational failure.

## Initial evidence anchors

### E-IR-01 — Electricity is a material dependency, with concentrated local impacts

The International Energy Agency's 2025 *Energy and AI* report estimates data centres consumed about 415 TWh of electricity in 2024, around 1.5% of global electricity use, and projects approximately 945 TWh by 2030 in its base case. The report emphasizes that data-centre loads are geographically concentrated, so their local grid impacts can be more significant than their global share suggests.

Source: IEA (2025), *Energy and AI*, “Energy demand from AI.”  
https://www.iea.org/reports/energy-and-ai/energy-demand-from-aI

**Interpretation:** This supports the claim that electricity is a material input to AI services and that local grid planning can become a bottleneck. It does not by itself establish that all AI and human energy interests align. The same power demand can create local trade-offs around electricity prices, land, emissions, water, and which users receive priority during shortages.

### E-IR-02 — The demand picture changes quickly and has significant uncertainty

The IEA's 2026 update reports that data-centre electricity use grew by 17% in 2025, with AI-focused data centres growing faster. It describes bottlenecks in grid connections, transformers, advanced chips, and high-bandwidth memory, while also reporting improving energy efficiency per AI task.

Source: IEA, *Key Questions on Energy and AI*, executive summary.  
https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

**Interpretation:** Resilience analysis must track both sides: efficiency gains may reduce resource use per task, while demand growth and more intensive workloads may increase total system demand. Forecasts are scenarios, not certainties; future claims should use ranges and update dates.

### E-IR-03 — Semiconductor supply chains are globally integrated and regionally concentrated

The U.S. Department of Commerce's 2025 Quadrennial Supply Chain Review describes semiconductors as a complex, globally integrated supply chain, identifies concentration of critical inputs and natural hazards as risks, and recommends improving traceability and diversified capacity in selected segments.

Source: U.S. Department of Commerce, *2024 Quadrennial Supply Chain Review* (published 2025), semiconductor discussion.  
https://www.trade.gov/sites/default/files/2025-01/20212024-Quadrennial-Supply-Chain-Review.pdf

**Interpretation:** AI capability depends not just on software but on specialized physical production and logistics. Diversification can improve robustness but may involve cost, time, duplication, and geopolitical trade-offs. Supply-chain concentration should be evaluated segment by segment rather than described as one uniform vulnerability.

### E-IR-04 — AI data-centre security is now a dedicated infrastructure concern

NIST published an initial public draft of SP 800-239, *AI Data Center Security Analysis: A High-Performance Computing (HPC) Driven Approach*, in July 2026. It examines threats and security gaps across architecture, hardware, software, workflows, and storage in AI-focused infrastructure.

Source: NIST SP 800-239 initial public draft.  
https://csrc.nist.gov/pubs/sp/800/239/ipd

**Interpretation:** This is a useful taxonomy anchor for the cyber/operational layer. Because this is an initial public draft, it should be treated as a developing analysis rather than settled final guidance.

## Shared benefits and conflicts: hypotheses to test

### Potential overlap
- More reliable electricity and cooling can reduce service interruptions for both public infrastructure and AI services.
- Better incident response and cyber security can protect hospitals, communications, emergency services, and computing operations.
- More transparent supply-chain risk can help maintain access to critical components for multiple sectors.
- Efficiency and flexible workloads may reduce costs or free capacity, depending on rebound effects and local constraints.
- Backup, redundancy, and recovery planning can reduce downtime, though their value depends on design and hazard model.

### Potential conflict
- AI workloads may compete with households, hospitals, manufacturing, and other users for scarce electricity or grid connections.
- Water use and cooling choices may conflict with local ecological needs or community priorities.
- Redundancy can improve continuity but increase energy, materials, cost, and land use.
- Centralization can improve operational efficiency while creating correlated failure or single points of control.
- Security and continuity goals can conflict with transparency, public oversight, privacy, or local autonomy.
- Organizations may prioritize their own uptime over wider system resilience.

These are candidate mechanisms, not claims that every conflict occurs in every region. Each needs a documented case and counterevidence.

## Research method for the next pass

For each case, record:
- the infrastructure component and geographic/system boundary;
- which human services depend on it;
- which AI services depend on it, distinguishing training, inference, development, and research;
- the specific hazard or disruption;
- baseline and observed outcomes;
- resilience measure (availability, recovery time, redundancy, graceful degradation, substitution, or adaptation);
- beneficiaries and parties bearing costs;
- primary source and date;
- uncertainty, alternative explanations, and contrary cases.

Avoid a single vague “resilience score” until measures are operationally defined. Availability, recovery, adaptability, affordability, and robustness against correlated failures are different properties.

## Candidate case studies for the next research pass

1. **Grid reliability and data-centre loads:** documented grid events, connection delays, demand response, and consequences for other electricity users.
2. **Cooling and water:** compare cooling architectures, water-stressed locations, and trade-offs between water, energy, and operational continuity.
3. **Semiconductor supply disruption:** trace a specific disruption through chips, servers, cloud capacity, and downstream services.
4. **Cloud-region/network failure:** examine real outages and recovery mechanisms, including correlated dependencies.
5. **Human critical services and AI continuity:** investigate where shared infrastructure supports emergency response, healthcare, or research—and what happens when priorities conflict.

## Provisional conclusion

The initial evidence supports a narrow, practical premise: AI services depend on material systems whose reliability, concentration, and resource demands can be measured, and these systems also support many human activities. Whether resilience constitutes a “shared interest” must be demonstrated case by case and should be stated operationally: reliability, access, affordability, safety, or recovery—not presumed as a shared subjective value.

This branch should remain independent of the AlphaDev case. A positive result in algorithm discovery cannot establish the infrastructure thesis, and infrastructure dependence cannot establish the bridge hypothesis.


## Evidence update — IEA 2026 and NIST draft (checked 2026-10-18)

### E-IR-05 — Newer IEA estimates update the 2025 baseline

The IEA's April 2026 report states that global data-centre electricity consumption grew 17% in 2025 and AI-focused data-centre consumption grew 50%. Its updated central projection is about 485 TWh for all data centres in 2025, rising to 950 TWh in 2030 (roughly 3% of global electricity demand). It also emphasizes improving energy efficiency per AI task while total demand rises because of uptake and increasingly energy-intensive uses.

Sources:
- IEA (2026), *Key Questions on Energy and AI*, executive summary: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- Report overview and publication date (16 April 2026): https://www.iea.org/reports/key-questions-on-energy-and-ai

**Interpretation:** Use the newer 2026 figures when describing current demand, and preserve the 2025 report as a dated prior estimate rather than silently blending the two vintages. The report says 2026 data are estimates; the projection is a scenario, not a certainty. The rise in total demand does not contradict lower energy per individual task: total workload volume, task mix, and efficiency can move in different directions.

### E-IR-06 — AI infrastructure security has a developing technical framework

NIST's initial public draft SP 800-239, published 27 July 2026, examines AI data-centre security across architecture, hardware, software, workflows, and storage. The public comment period closed 25 September 2026; the document remains identified as an initial public draft in the source reviewed here.

Source: NIST SP 800-239 (IPD): https://csrc.nist.gov/pubs/sp/800/239/ipd

**Interpretation:** This gives the project a structured starting point for security and operational dependencies. It is draft guidance, not proof that any particular facility is resilient or that the recommendations are universally validated.

### Evidence discipline update

The IEA is a high-value synthesis source for global trends, but its totals and projections should be paired with grid-operator, utility, local-government, facility, and outage records when analyzing a specific place. NIST's draft is a threat-analysis framework, not an incident dataset. For each case study, separate (a) measured facts, (b) forecasts, (c) developer/operator claims, and (d) our inferences.


## Case study added — Grid Reliability Case 01

The first documented case is the July 22, 2026 Northern Virginia large-load transfer event. PJM reports that a 230 kV line fault was followed by roughly 3,800 MW of data-centre load disconnecting and transferring to backup power, creating voltage/frequency disturbances. PJM says operators restored the Balancing Authority Area Control Error limit within nine minutes and reported no significant overall reliability impact. This is a disturbance successfully managed, not a reported widespread blackout.

Full source trace, limits, shared-benefit/conflict analysis, and follow-up questions: [Grid Reliability Case Study 01 — Northern Virginia](GRID-RELIABILITY-CASE-01-NORTHERN-VIRGINIA.md).

The case supports a narrow operational conclusion: the behavior of large computational loads can affect grid dynamics, and grid events can affect how those facilities draw power. It does not isolate AI workloads, establish that AI growth caused the incident, or prove unified human–AI interests. A useful next contrast is evidence that data-centre flexibility measurably helps grid operations, alongside continued investigation of final technical findings and standards changes.


## Positive counterpart — flexible compute field demonstration

The strongest positive case found in this pass is a peer-reviewed *Nature Energy* field demonstration in Phoenix, Arizona. A 256-GPU cluster running representative AI workloads reportedly reduced power use by 25% for three hours during utility-coordinated peak events with APS and SRP, while maintaining AI quality-of-service guarantees and without hardware modifications or energy storage. Paper: https://doi.org/10.1038/s41560-025-01927-1. EPRI's DCFlex program lists related multi-site demonstrations: https://dcflex.epri.com/demonstrations.

Google separately reports ML-workload demand response during three grid events with Omaha Public Power District and other utility partnerships: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/.

The evidence supports technical feasibility for selected workloads, not proof of regional reliability gains, consumer savings, universal scalability, or a reduction in blackouts. See [Grid Reliability Case Study 02 — Flexible Compute](GRID-RELIABILITY-CASE-02-FLEXIBLE-COMPUTE.md) for a comparison with the Northern Virginia load-transfer event and a plan for stronger grid-level evaluation.


## Benefit assessment update — measured outcomes vs modeled benefits

The current evidence supports a narrow but useful claim: selected AI workloads can be modulated to reduce participating cluster power during defined events while meeting tested service constraints. The Phoenix field demonstration reports 25% reduction for three hours on a 256-GPU cluster (Nature Energy, https://doi.org/10.1038/s41560-025-01927-1; public artifacts: https://github.com/ai-emerald/emerald-ai-demo-may-2025).

System-wide benefits are less directly established. A 2026 PJM modeling case estimates up to 32 GW of additional flexible load under 2023 system assumptions with curtailment of 0.1% of annual energy and during 1.2% of hours; authors note a relatively mild-weather data limitation (https://scholars.duke.edu/publication/1917768). Multi-region modeling finds system costs can fall while emissions may rise in some generation mixes (https://doi.org/10.1016/j.isci.2026.116497). PNNL modeling identifies possible congestion and contingency benefits but is not a real-grid outcome audit (https://www.pnnl.gov/publications/potential-data-center-controls-grid-services).

Full benefit ladder, counterexamples, metrics, and verification plan: [Grid Flexibility Benefit Assessment 01](GRID-FLEXIBILITY-BENEFIT-ASSESSMENT-01.md). Current assessment: facility-level power reduction is demonstrated for one setup; grid-level benefits are supported by models but need operating-event verification; consumer savings and avoided blackouts are not yet established; emissions benefits are conditional.


## Phoenix artifact inspection and utility verification plan

The published supplementary repository lists time-stamped SRP cluster power data, workload performance, SRP hourly demand context, GPU power-cap throughput sweeps, and figure data. However, a public issue asks whether GPU cluster power was measured via nvidia-smi; no answer was visible on 2026-10-18. This metric definition should be clarified before independently recalculating the 25% reduction. The published performance table reports a weighted normalized performance value of 0.909560245, which requires interpretation under the paper's normalization method and cautions against saying performance was unchanged.

No event-specific, independent utility-side report was located in this pass that attributes changes in peak demand, congestion, reserves, system costs, outages, or customer bills to the Phoenix experiment. Arizona regulatory and utility records are avenues to pursue, not proof that such outcomes were measured.

Full inspection notes, sources, open measurement question, and draft evidence-request text: [Phoenix Artifact Inspection and Utility Verification Plan 01](PHOENIX-ARTIFACT-INSPECTION-AND-UTILITY-VERIFICATION-01.md).
