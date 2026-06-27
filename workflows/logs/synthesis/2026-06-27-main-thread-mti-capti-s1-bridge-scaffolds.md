# Main-Thread Synthesis: MTI, Cap_TI, S1, and Bridge Scaffolds

Date: 2026-06-27
Status: completed scaffold batch, not a canonical claim update
Owner: main thread

This artifact completes tasks 6-9 from the 2026-06-27 next-10 queue. It is a
research scaffold only. It does not edit the claim ledger, roadmap, formalism,
or tests, and it does not promote MTI, Cap_TI, S1, H7, TI, or any smooth
physics-facing claim.

## Shared Guardrails

- Do not convert any item here into claim-ledger language without a new
  executable test, external evidence packet where required, and integrator
  review.
- Treat T238/T243 as positive internal witnesses only. They are not landed
  external WBE axioms.
- Treat Cap_TI Candidate C as the live capability target, not as a theorem.
- Treat S1 as requiring an added assumption after T223's uniform finite-colimit
  no-go.
- Treat finite-to-smooth language as bridge design only until a typed source,
  typed target, comparison map, and hostile control all survive.

## Task 6 - MTI External Axiom Evidence Audit Scaffold

### Current Blocker

MTI remains partially_supported. The current promotion blocker is not an
unrun computation; it is an evidence and interpretation blocker. Two internal
sub-objects need independent WBE-native support:

1. Reflectionless / area-preserving branching axiom for the 3/4 exponent.
2. Terminal-reachability / coverage axiom that keeps delivery branches loaded.

The 2026-06-26 integrator review also keeps the capability burden open:
T197/T206-style capability absorption has not been reversed, so a
mu_M-source system performing a task entropy-only systems cannot perform has
not been landed.

### Audit Packet To Build

For each candidate external citation, record:

| Field | Required Content |
| --- | --- |
| citation | Full bibliographic reference and stable locator. |
| domain | WBE, BMR, vascular transport, pulsatile impedance, terminal service, or other. |
| axiom matched | Reflectionless area-preserving, terminal-reachability coverage, or neither. |
| native language | The source's own variables, units, and optimization objective. |
| transfer map | Exact translation into the repo's T238/T243 variables. |
| independence check | Why the source does not cite or depend on TaF/TI/MTI machinery. |
| non-circularity check | Why the source does not assume the 3/4 exponent or coverage floor only because the target result needs it. |
| falsification content | What observation or theorem in the source would make the repo's premise false. |
| verdict | land, partial, reject, or needs reviewer. |

### Acceptance Bar

A citation is landable only if it satisfies all of these:

1. It is external to this repo and not merely a restatement of the project's
   Moses-to-TaF crosswalk.
2. It supports the premise in domain-native terms before the TaF conclusion is
   introduced.
3. It carries units and variables that can be mapped into the existing T238 or
   T243 fixtures without changing the fixture after seeing the result.
4. It survives the relevant absorber:
   - area-preserving evidence must not be a forbidden exponent dial;
   - coverage evidence must not be a restatement of "keep every branch loaded"
     with no biological or transport-native principle.

### Next Executable Artifact

Create a citation-audit test or literature note that emits:

```text
premise_id
citation_id
native_variables
taf_transfer_map
independence_verdict
non_circularity_verdict
landability_verdict
```

No claim promotion is allowed from the scaffold itself.

## Task 7 - Cap_TI Reconciliation Protocol Grounding Scaffold

### Current Blocker

Cap_TI Candidate C has a strong candidate capability: predicted reconciliation
rounds R(beta). T188 supplies the hostile same-neighbor-data split with matched
gluing topology G and different delivery-time metric beta. The missing piece is
a formal reconciliation protocol that makes the continuous formula operational.

### Protocol Target

Define a protocol:

```text
P_rec(Y_TI, O, A, G, beta, n) -> K_TI
```

where:

- `Y_TI` is the source object;
- `O` is the observer family;
- `A` is the access relation;
- `G` is identity, overlap, and gluing topology;
- `beta` is the independently typed delivery exponent;
- `n` is the event or terminal count;
- `K_TI` is the reconciliation cost object.

The native comparison is:

```text
R_K_TI = fewer_or_equal_reconciliation_rounds
```

### Minimal Round Semantics

A round is admissible only if all of these are true:

1. Each observer publishes a frontier-limited signed local order fragment.
2. Overlap witnesses are matched through G without adding timing information
   to G.
3. A conflict is resolved only when at least one newly delivered dependency
   witness or source-order certificate enters the shared frontier.
4. The protocol halts when all observer-local fragments descend to one global
   source-order section on the declared cover.

### Formula Grounding Obligation

The intended formula may stay continuous:

```text
R_continuous(n, beta) = n^(1 - beta)
```

but the protocol test must declare a finite observation map before execution,
for example:

```text
R_rounds(n, beta) = ceil(R_continuous(n, beta))
```

or a bounded interval verdict:

```text
R_rounds in [floor(R_continuous), ceil(R_continuous)]
```

The choice must be frozen before reusing T188's Alpha/Beta pair.

### Controls

Positive control:

- Same G, same access cover, same observer family, beta_Beta > beta_Alpha;
  expected verdict is fewer rounds for Beta.

Hostile controls:

- Same beta but different G: reject as G-owned, not Cap_TI-owned.
- Same G and same beta but different observer cadence: reject as kappa-owned.
- Same G and same beta but different access boundary: reject as A-owned.
- Rounds determined entirely by G topology: demote by the source-spec collapse
  lemma.

### Next Executable Artifact

Implement a small protocol fixture that emits:

```text
case_id
fixed_fields
changed_fields
round_semantics
R_continuous
R_observed_or_bounded
absorber_verdict
cap_ti_verdict
```

Until that exists, Candidate C is a grounded target, not a theorem.

## Task 8 - S1 Natural Non-Uniform Measure Gate Scaffold

### Current Blocker

T223 killed the uniform finite finality-colimit route as a route to
manifoldlike causal sets. The live S1 question is whether a natural
non-uniform measure can be declared independently and tested without selecting
for the desired survivors by hand.

### Candidate Measure Families

Any future measure should name exactly one family before computation:

1. Dynamics-induced measure: generated by a declared local growth or descent
   process.
2. Observer-cover prevalence measure: weighted by physically typed observer
   domains and access overlaps.
3. Sprinkling-compatible measure: matched to Lorentzian causal data rather
   than post hoc finite survivor classes.
4. Cost/action measure: weighted by independently typed transport, access, or
   reconstruction costs.

### Acceptance Conditions

A non-uniform measure is admissible only if:

1. The measure is defined over the whole finite object family before filtering.
2. It is invariant under relabeling and states how order-duals are treated.
3. It does not assign zero mass to failures by construction.
4. It is tested against the T223 n=6, n=7, and n=8 baselines before any larger
   run.
5. It states a predeclared scaling expectation for n=9 or the next feasible
   census.
6. It connects to T153-style Lorentzian causal data, observer world tubes,
   access diamonds, or domains of dependence before claiming S1 relevance.

### Demotion Conditions

Demote the measure if:

- the survivor fraction rises only because failures were excluded from the
  sample space;
- the weights encode Myrheim-Meyer band success directly;
- the measure changes after seeing which isomorphism classes survive;
- the result remains a thin finite-poset tail with no declared continuum
  bridge.

### Next Executable Artifact

Create a measure-gate fixture:

```text
measure_id
support_family
weight_rule
invariance_audit
baseline_uniform_comparison
n6_n7_n8_verdicts
n9_prediction
s1_verdict
```

The only acceptable immediate S1 impact is "candidate added-assumption under
test", not promotion.

## Task 9 - Double-Diagram Finite-To-Smooth Bridge Template

### Purpose

Future bridge proposals should keep two axes separate:

```text
horizontal: observer-domain descent / local-to-global gluing
vertical: source, record, or admissibility filtration
```

This prevents finite TaF colimits, GU/TI filtrations, and smooth geometric
targets from being collapsed into one metaphor.

### Template

```text
Bridge ID:
Date:
Owner:
Status: proposal | executable | refuted | landed-control

Finite source object:
  family:
  fields:
  visible equivalence:
  capability object:
  absorber vector:

Smooth or structured target:
  target category:
  objects:
  morphisms:
  quotient/gauge redundancies:
  native comparison:

Horizontal axis:
  local domains:
  cover:
  restriction maps:
  descent/gluing condition:
  H1 or obstruction object:

Vertical axis:
  filtration index:
  source or record stage:
  admissibility predicate:
  transient class to track:

Bridge type:
  one of discretization, limit, nerve, sheafification, coarse-graining,
  continuum scaling, measurable field, finite cover approximation, or named
  comparison functor.

Preservation claim:
  preserved finite verdict:
  transformed verdict:
  destroyed verdict:
  reason:

Controls:
  positive control:
  hostile control:
  quotient/gauge control:
  refinement control:

Verdict:
  bridge preserves residue | bridge weakens residue | bridge destroys residue
  claim impact:
```

### First Bounded Run Recommendation

Use an accessible-witness gap object or typed transport network as the finite
source and a finite-cover-to-presheaf/sheaf target as the structured target.
The first question should be:

```text
Does the finite capability-spread or witness-obligation verdict survive
restriction, refinement, or sheafification?
```

Do not use this template to claim smooth spacetime. Use it to decide whether a
finite witness has any honest route into a structured target at all.

## Batch Outcome

Tasks 6-9 are now actionable scaffolds with:

- live blocker statement;
- acceptance and demotion conditions;
- executable next-artifact shape;
- explicit no-promotion guardrails.
