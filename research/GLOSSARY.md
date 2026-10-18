# Glossary — Intelligence Seed 001 Research Workspace

**Status:** Working aid; not part of the archived v0.2.0 release and not covered by its manifest.
**Canonical definitions:** The ten terms in [`releases/v0.2.0/definitions.json`](../releases/v0.2.0/definitions.json) are authoritative for the release. They are not restated here; this file only links to them and adds terms the research workspace uses without defining. Where the workspace's working usage differs from the release, the difference is stated.

## Terms defined in the release

See `definitions.json` for: *intelligence*, *information processing*, *cognitive substrate*, *bridge*, *externalization*, *civilization*, *infrastructure*, *resilience*, *alignment*, *agency*.

## Bridge: release definition vs. working definition

- **Release (v0.2.0):** a capability, organization, or substrate that expands the reachable state-space of information processing, coordination, learning, or action beyond prior constraints.
- **Working (BRIDGE-PRESSURE-TEST-01):** a change in representation, organization, substrate, or coordination that, relative to an explicit baseline, causally enables a defined system to perform at least one specified class of tasks with a measurable change in feasibility, performance, cost, or robustness. Claims about changing later systems' capabilities need separate evidence, and costs and failure modes must be recorded.
- **Why they differ:** the pressure test found the release wording too permissive (nearly any useful change qualifies). The release is immutable, so the narrower wording lives only in the workspace until a new version.

## Bridge-analysis terms

- **Baseline:** the comparison condition for judging a change: what the system could do before, or what a matched system does without the proposed bridge.
- **Counterfactual:** what would likely have happened without the change. For historical or biological cases it usually cannot be observed directly, so evidence ratings should say so.
- **System boundary:** which entities and resources count as "the system" before and after a change. Chosen for a specific task and purpose.
- **Capability extension:** the system performs an existing task better, faster, more cheaply, or more reliably.
- **Capability recombination:** existing capabilities can be combined in ways not feasible under the baseline.
- **Possibility-space change:** the change enables classes of future capabilities that were not practically evolvable or constructible before. The hardest claim to support; scored by the "F" dimension and not established for any case reviewed.
- **New system-level organization:** components become integrated into a coordinated whole with new roles, dependencies, or behavior.
- **Capability / architectural / possibility-space bridge:** the three levels used in case studies, from a measured task-level change, to a change in how a workflow or system is organized, to a change in what later systems can do.
- **Rubric dimensions (B, M, D, A, F, T):** baseline clarity, mechanism, demonstrated difference, architectural change, future capability space, trade-offs. Each is scored 0–2 as a qualitative prompt. The scores are one analyst's desk judgments, not a validated scale.
- **Inter-rater validation:** independent reviewers classify cases without seeing prior ratings. Not yet done.
- **Cognitive offloading:** moving a memory or processing task to an external aid; used as a test case because it helps in the short term but may carry costs.
- **Distributed cognition:** cognitive work organized across people, artifacts, and procedures (Hutchins). Weaker than the extended-mind claim.
- **Extended mind:** the stronger, contested claim that external resources can be literal parts of a cognitive process (Clark & Chalmers).
- **Major evolutionary transition (in individuality):** formerly independent units become an integrated higher-level entity (West et al.). A stricter biological category than "bridge".
- **Teleological / retrospective reading:** interpreting an earlier change as aimed at a later outcome because the outcome happened.

## Evidence terms

- **Rating key (EVIDENCE-LEDGER):** *High* means multiple convergent lines of direct evidence for the narrowly stated claim. *Moderate* means credible evidence but contested scope or generalizability. *Low / open* means indirect evidence or a claim too vague to test. Confidence applies to the claim's exact wording, not the whole seed.
- **Observation / inference / hypothesis:** the seed's claim types. Observations are descriptive, inferences derive from observations, and hypotheses are testable proposals.
- **Falsification criterion:** an observation that would lead to rejecting or substantially revising a claim.
- **Descendant:** a revised or extended version of the seed that records its parent's ID, version, and hash.
- **Response:** an independent critique or extension that cites the exact seed version and hash.
- **Canonical seed hash:** SHA-256 of the seed JSON serialized with sorted keys and compact separators (see `provenance.json`).
- **Modeled vs. measured vs. operator-reported:** the grid and AI case studies keep these apart. Measured results come from field data, modeled results from simulations or scenarios, and operator-reported results from the organization's own account.

## AI downstream-case terms

- **Downstream chain:** the documented path from an AI output to independent adoption and to a measurable later effect.
- **Attribution:** separating the AI's contribution from human expertise, compute, data, and existing automation.
- **Branchless sort:** a sorting routine that avoids conditional branches; the form of the AlphaDev routines adopted in LLVM libc++.
- **AssemblyGame:** AlphaDev's formulation of program discovery as a single-player game of appending assembly instructions.

## Infrastructure and grid terms

- **Dependency layers:** the infrastructure-resilience branch's grouping of what AI and human systems rely on: electricity, thermal and physical operations, compute and semiconductors, networks and data, people and institutions, environment, and security and governance.
- **Large-load transfer event:** many large loads (here, data centers) disconnecting from the grid and moving to backup power at once, typically after a disturbance.
- **Ride-through:** a load's ability to stay connected and operating through a voltage or frequency disturbance instead of disconnecting.
- **Area Control Error (ACE):** a balancing authority's measure of mismatch between supply and demand; the limit is the threshold operators must restore it to after a disturbance.
- **Demand response / load flexibility:** deliberately reducing, delaying, or shifting electricity use in response to grid conditions.
- **Rebound:** demand that returns after a curtailment; if synchronized, it can create a new peak.
- **Curtailment-enabled headroom:** additional peak load a system can serve without new capacity if the new loads commit to reducing draw during critical periods.
- **Facility-level vs. grid-level vs. public benefit:** a reduction at one site; a measured change in grid operation; and lower cost or risk for other users after the counterfactual and cost distribution are accounted for. Each needs its own evidence.
- **Shared practical interest:** the seed's operational reading of H4: overlapping reliability, access, affordability, safety, or recovery needs. It does not mean shared values or subjective preferences.
