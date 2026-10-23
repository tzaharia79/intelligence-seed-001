# Combined Research Map — Draft 01

**Status:** Working synthesis plan; not a new thesis or release.
**Purpose:** Show how each research sample is intended to contribute to the overall Intelligence Seed 001 project, which framework it belongs to, how directly it bears on the thesis, and what it can and cannot establish.
**Versioning note:** This is a working-tree document. It does not modify or supersede the immutable v0.2.0 release.

## 1. Overall question and claim structure

Intelligence Seed 001 explores four connected but separable propositions:

1. **Life and information processing:** Living systems acquire, preserve, use, and sometimes transmit information in ways relevant to behavior and cognition.
2. **Cognitive externalization and organization:** Human cognition and coordination can be extended or reorganized through language, records, tools, institutions, and technology.
3. **Bridges and later capabilities:** Some physical, organizational, or technological changes may enable new classes of information processing or coordination. This is a proposed synthesis, not yet a validated general theory.
4. **AI and shared infrastructure:** AI may contribute to building later cognitive infrastructure, while human societies and AI systems can have overlapping practical dependencies on reliable infrastructure. Shared dependency does not imply consciousness, identical values, or a unified goal.

The motivating phrase “life as an intelligence generator” is a broad hypothesis/metaphor, **not an established empirical law or a claim that evolution has a purpose**. Each sample should test a bounded proposition, not be counted as generic support for the whole thesis.

## 2. Classification rules

### Framework labels
A sample may have more than one label:
- **Technical:** engineered systems, software, networks, energy, compute, infrastructure, operational performance.
- **Biological:** organisms, inheritance, evolution, natural information processing, development, ecology.
- **Philosophical/conceptual:** definitions of intelligence, cognition, externalization, agency, system boundaries, teleology, and interpretation.
- **Mathematical/formal:** explicit models, measurable variables, causal identification, information theory, graph/network models, probability, optimization, population genetics, or formal logic.
- **Methodological/governance:** evidence quality, reproducibility, who benefits or bears costs, reliability practice, evaluation and publication integrity. This is a cross-cutting label, not a replacement for the four main frameworks.

### Relevance to the overall thesis
- **Direct:** directly tests a named proposition or an important mechanism in the thesis.
- **Supporting/indirect:** establishes a prerequisite, mechanism, analogy, or boundary condition but cannot by itself establish the overall thesis.
- **Tangential/contextual:** improves definitions, measurement, reliability, discoverability, or project governance; necessary for good research but not substantive evidence for the thesis.
- **Counter-test:** deliberately searches for failure, trade-offs, contradictions, or alternative explanations. This can be direct or supporting depending on the claim tested.

These labels describe the *logical relationship* to the thesis, not evidence strength. A direct test may be weak or inconclusive; a tangential task can still be important.

## 3. Research inventory

| ID | Sample / workstream | Framework | Intended to show or test | Thesis relationship | Current status and key limit |
|---|---|---|---|---|---|
| R-01 | Seed artifact, companion essay, definitions and release schemas | Philosophical/conceptual; methodological | Make the claims inspectable, separable, machine-readable, and open to independent evaluation | Tangential/contextual | v0.2.0 published. Publication quality is not evidence that the claims are true. |
| R-02 | Evidence review on biological cognition, learning and information use | Biological; philosophical | Establish bounded examples of organisms acquiring, retaining, and using information | Supporting/indirect | Literature map and ledger anchors exist; scope across taxa and definitions of “intelligence” remain open. |
| R-03 | Major transitions in individuality and cognitive evolution | Biological; philosophical | Test whether particular evolutionary transitions reorganize cooperation, inheritance, or the kinds of cognition that can evolve | Direct to the life/transition proposition; supporting to the full thesis | Literature anchors exist; transition criteria differ and examples are debated. Not evidence of a universal direction or purpose. |
| R-04 | Biological sampling branch: inheritance, variation, immune memory, cellular regulation, nervous systems, multicellularity, symbiosis, eusociality, development, niche construction | Biological; potentially mathematical | Compare mechanisms that preserve, transform, or coordinate information across organisms and generations; include failures and trade-offs | Direct to the biological strand; supporting to the cross-domain thesis | Planned future branch, intentionally parked while technical resilience work proceeds. No single example should be called an “intelligence bridge” by default. |
| R-05 | Extended mind and distributed cognition (Clark & Chalmers; Hutchins and critiques) | Philosophical/conceptual; social/technical | Clarify when tasks are distributed across people, artifacts, and practices, and whether external resources are part of a cognitive process | Direct to cognitive externalization; supporting to the whole thesis | Established literature anchors exist. Stronger claims about where a mind begins and ends remain contested. |
| R-06 | Human externalization through language, records, tools, institutions and technology | Philosophical; historical/social; technical | Track how memory, calculation, coordination and knowledge can persist beyond one brain or lifetime | Direct to cognitive externalization | Broad claim is well supported, but examples must specify which function changes and avoid treating tools as mere passive containers. |
| R-07 | Bridge hypothesis, operational definition, rubric and counterexamples | Philosophical/conceptual; methodological; potentially mathematical | Determine whether “bridge” adds explanatory value beyond existing terms; require baselines, causal enablement, defined task classes, costs and failure modes | Direct to the proposed bridge proposition | Working definition narrowed after pressure tests; B/M/D/A/F/T prompts are qualitative and unvalidated. No case yet establishes possibility-space change. |
| R-08 | AlphaDev paper-to-artifact-to-LLVM implementation chain | Technical; mathematical/computational | Show that AI-assisted search can produce a concrete algorithmic improvement that survives evaluation and enters a real software implementation chain | Direct to AI contribution; supporting to bridge hypothesis | Source chain substantially traced. This is bounded capability evidence, not proof of system-wide downstream impact or a new future capability class. |
| R-09 | AI-assisted software development randomized studies | Technical; mathematical/statistical | Estimate when AI assistance changes task speed, output, quality or performance under specific study conditions | Direct to AI contribution, narrowly | Evidence scan exists. Results vary by task and context; productivity is not equivalent to expanded possibility-space. |
| R-10 | Downstream AI cases: AlphaFold2, AlphaChip, AlphaTensor and experimentally validated AI protein design | Technical; biological; mathematical | Test whether AI outputs feed into later scientific, engineering or biological capabilities beyond a demonstration | Direct to AI contribution; supporting to bridge hypothesis | Evidence chain scan exists. Attribution, independent validation, adoption, and actual downstream effect differ by case; keep each chain separate. |
| R-11 | Northern Virginia large-load transfer disturbance | Technical; methodological/governance | Examine how concentrated computational load and transfer/contingency conditions affect grid reliability, and how impacts are distributed | Direct to infrastructure-resilience proposition; supporting to shared-interest proposition | Documented public case. Does not by itself establish AI-specific intent or a general rule about data centers. |
| R-12 | Phoenix/SRP flexible-compute field demonstration and artifact inspection | Technical; mathematical/statistical; governance | Test whether computational demand can be shifted or curtailed in ways that support grid operations, and distinguish measured facility behavior from modeled system benefits | Direct to conditional resilience/co-benefit claim | Public demonstration and CSV inspection exist. Units, boundaries and event windows remain unresolved; exploratory averages do not reproduce the paper’s headline claim. |
| R-13 | Grid flexibility benefit assessment, including emissions and rebound caveats | Technical; mathematical; governance | Identify conditions under which flexibility helps, and cases where rebound, dispatch, emissions, costs or resource allocation may offset benefits | Counter-test; supporting to shared-interest proposition | Working assessment exists. Utility-scale and net public benefits remain unverified for the examined demonstration. |
| R-14 | Meta global outage (2021) | Technical; network systems; governance | Show how common dependencies can turn a local operational fault into broad failure, including impairment of DNS, remote access and diagnosis | Counter-test to optimistic bridge framing; direct to resilience | Operator postmortem plus independent external network observations. Desk analysis, not independent internal forensic audit. |
| R-15 | AWS S3 outage and recovery-path coupling (2017) | Technical; systems engineering; governance | Test whether recovery, integrity-check, or incident-communication paths depend on the failed service itself | Counter-test; direct to resilience | Operator postmortem documents the incident. It illustrates coupling and recovery delays, not that all redundancy fails. |
| R-16 | Cloudflare PDX01 power loss and post-remediation recovery (2024), compared with 2023 outage | Technical; systems engineering; governance | Test whether prior remediation and automatic failover improved containment in a repeated class of facility failure, while tracking functions that remained degraded | Direct to resilience; supporting to the claim that organized infrastructure can change feasible recovery | Strong before/after operator account, but the seven-minute recovery and uninterrupted data-plane claims remain operator-reported, not independently verified. |
| R-17 | Cloudflare independent-claims check and RIPEstat BGP retrieval workflow | Technical; mathematical/measurement; methodological | Seek independent observable traces and determine what routing data can actually corroborate about reachability during an outage | Tangential to the broad thesis; direct to the validity of R-16's empirical claims | Reproducible script and resilient retrieval workflow exist. BGP routes do not prove HTTP success, latency, DNS success or customer impact; current workflow run was still being retrieved at last check. |
| R-18 | Infrastructure dependency model: electricity, cooling/water, compute/semiconductors, networks/data, people/institutions, environment, security/governance | Technical; systems engineering; governance | Map physical and organizational dependencies, common-cause failure paths, and competing resource demands | Supporting/indirect to shared-infrastructure proposition | Initial branch exists. Avoid opening all sub-branches simultaneously; select cases with good primary evidence. |
| R-19 | Future cooling/water, semiconductor supply-chain, institutional, cyber/physical security and distributional cases | Technical; governance; potentially mathematical | Test whether resilience constraints and benefits vary across infrastructure layers and affected groups | Supporting/indirect; selected cases may directly test resilience | Planned, not yet systematically sampled. Prioritize one well-documented case at a time; direct company/utility outreach remains paused. |
| R-20 | Shared human–AI infrastructure dependence | Technical; philosophical; governance | Establish practical overlap in dependencies and identify when reliability benefits both humans and AI operations, as well as conflicts over control, resource allocation and acceptable risk | Direct to the fourth proposition, conditionally | Infrastructure dependence is well supported; “shared interest” is a conditional interpretation, not proof of subjective preference, aligned values or unified goals. |
| R-21 | Teleology and the phrase “life as an intelligence generator” | Philosophical; biological | Separate a useful motivating question from claims that evolution has a purpose, direction, or inevitable endpoint | Direct to scope and interpretation; counter-test to overclaiming | Explicitly provisional. No current evidence establishes a universal direction or purpose of existence. |
| R-22 | Mathematical/formal framework — causal models, information theory, network reliability, evolutionary models and explicit uncertainty | Mathematical/formal; cross-domain | Convert selected concepts into variables, measurable outcomes, baselines, causal diagrams or models; test whether cross-domain comparisons are valid | Supporting/indirect now; potentially direct once specified | **Not yet a unified formal framework.** Treat these as candidate tools, not as an existing validated model. Do not invent a single “intelligence score” without defensible operationalization. |
| R-23 | Evidence ledger, source provenance, counterevidence and mission reviews | Methodological; all frameworks | Keep observation, source interpretation, project inference, confidence, uncertainty, beneficiaries/cost-bearers and next tests distinct | Tangential/contextual but essential to validity | Active. Working ledger is not the empty evidence schema in the immutable release. |
| R-24 | Zenodo archive, hashes, discovery metadata, independent review invitations and future outreach | Methodological; technical | Preserve provenance, enable reproduction and invite criticism; verify what is actually discoverable or reviewed | Tangential/contextual | Archive/alignment audit and independent-response tracking remain open. Publication or silence is not evidence of endorsement. |

## 4. How the samples fit together

The intended research architecture is not “collect many examples that support the thesis.” It is a chain of bounded questions:

1. **Define the claims and terms** — R-01, R-07, R-21.
2. **Establish biological and cognitive background** — R-02 through R-06, with R-04 as a later dedicated branch.
3. **Test AI’s actual contribution to downstream capability** — R-08 through R-10.
4. **Test infrastructure dependence and resilience with both failure and containment cases** — R-11 through R-20.
5. **Improve measurement and causal discipline** — R-13, R-17, R-22, R-23.
6. **Enable independent checking and preserve version integrity** — R-01 and R-24.

The cross-domain thesis should be evaluated only after the individual samples have been assessed on their own terms. Similar words across biology, cognition, and technology do not guarantee that the mechanisms are equivalent.

## 5. Missing work and next priorities

### Priority 1 — finish the current technical measurement loop
- Retrieve and inspect the resilient RIPEstat run output.
- State exactly what the BGP data supports, including partial retrieval or a null result.
- Do not promote route stability to proof of customer-facing service availability.

### Priority 2 — consolidate the resilience comparison
- Compare grid load/flexibility with Meta, AWS and Cloudflare using the same template: trigger, dependency path, baseline, intervention, measured outcome, counterevidence, recovery path, distribution of costs/benefits.
- Keep “reliability of infrastructure” separate from “AI-specific benefit” unless evidence links them.

### Priority 3 — create a small explicit mathematical-methods plan
- For each chosen case, specify variables, unit, boundary, time window, baseline/counterfactual and uncertainty before computing summary metrics.
- Use causal diagrams or reliability/network models only where inputs can be defended.
- Do not aggregate heterogeneous cases into one numeric score.

### Priority 4 — return to biological sampling after the technical casework
- Select a small, contrasting set: one natural information-processing mechanism, one evolutionary transition, one inheritance/development case, and one counterexample/trade-off.
- For each, record mechanism, inheritance pathway, selection context, system boundary, alternative explanation and what would falsify the proposed analogy.
- Keep biological sampling visible in the mission map without letting it silently take over the active resilience branch.

### Priority 5 — synthesis and independent review
- Update the evidence ledger from the completed samples.
- Identify which thesis clauses have direct evidence, indirect support, unresolved status or counterevidence.
- Only then revise the companion essay or consider a future seed release. v0.2.0 remains immutable.

## 6. Minimum record required for any new sample

Every new case should answer:
1. **Question:** Which named claim or uncertainty is this case meant to test?
2. **Framework:** Technical, biological, philosophical, mathematical/formal, and/or governance-methodological?
3. **Relevance:** Direct, supporting/indirect, tangential/contextual, or counter-test?
4. **Baseline:** What is the comparison condition or plausible counterfactual?
5. **Observation:** What do the sources or measurements directly show?
6. **Inference:** What is the project's interpretation, clearly separated from the source's claim?
7. **Alternatives/counterevidence:** What else could explain the result? What would weaken it?
8. **Boundary and distribution:** Which system and time window are included; who benefits, pays, or bears risk?
9. **Confidence and next test:** What is unresolved and what evidence would change the assessment?
10. **Bridge rubric:** Only if applicable, distinguish extension, recombination, possibility-space change, and system-level organization. Do not force every case into the bridge category.

## 7. Synthesis guardrail

A sample is not a vote for the thesis. A sample is a bounded test with a stated purpose. The combined research is successful if it clarifies which propositions survive, which need narrower wording, which remain unsupported, and which should be rejected.
