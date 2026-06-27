---
document_type: synthesis_preflight
batch_item: fourth_batch_task_3
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/first-person-finality-complexity-separation.md
---

# First-Person Finality Complexity Preflight

## Status

This completes fourth-batch task 3 as a synthesis/preflight artifact. It does
not edit `README`, `CLAIM-LEDGER`, `ROADMAP`, tests, models, results, or
open-problem files. It does not claim a complexity-class separation,
consciousness theorem, or hard-problem solution.

## Read Surfaces

- `open-problems/first-person-finality-complexity-separation.md`.
- `open-problems/accessible-witness-gap-restriction-theorem.md`.
- `open-problems/observer-closure-theorem.md`.
- `open-problems/consciousness-as-record-renderer.md`.
- `claims/D2-observer-as-record-bearing-system.md`.
- `tests/T8-observer-renderer-toy-model.md`.
- `tests/T19-phenomenal-bridge-complexity-separation.md`.
- `tests/T60-observer-closure-theorem.md`.
- `tests/T92-accessible-witness-gap-restriction.md`.

## Preflight Verdict

The next work is not a full complexity separation. The next work is a frozen
decision-problem and machine-model specification that separates:

```text
third-person D1 verification over a full record graph
```

from:

```text
first-person finality verification by an observer restricted to its accessible
subgraph, witness relation, and local transition rules.
```

T19 currently supplies a finite causal-access witness: the full graph contains
external `R_self_finality` witnesses, while the observer's internal access set
does not. That is not yet a complexity-class separation. It is a prerequisite
access obstruction that must be encoded precisely before complexity language is
allowed.

## Decision Problem To Freeze First

Input data:

```text
G = finite record graph
O = designated observer or reconciler node
e = observation or evaluation event
Acc_O(e) = O-accessible subgraph at e
D1 = finality preorder/profile and threshold
P = finite typed proposition domain
p in P = proposition queried
W(p) = typed witness requirement for p
encoding = finite binary encoding of all declared data
```

Third-person D1 verification:

```text
TP-D1-FINALITY =
  Given (G, O, e, p, D1, W), does the full graph contain sufficient finalized
  witness structure for p under the declared D1 rule?
```

First-person finality verification:

```text
FP-FINALITY =
  Given only (Acc_O(e), O, e, p, D1, W restricted to Acc_O(e), local rules),
  can O certify that p is finalized?
```

The output convention must be frozen before any class placement:

```text
yes = locally certified finalized
no = locally certified not finalized
unknown = not certifiable from the accessible data
```

If `unknown` is allowed, the problem is not an ordinary decision language until
a promise or two-valued reduction target is declared.

## Required Distinction

Third-person verification asks what a full-graph verifier can decide from all
records. In the finite T19 witness this is a graph inspection problem once the
encoding, D1 rule, and witness predicate are fixed.

First-person verification asks what the observer can certify from its own
accessible records. A missing external witness is not automatically a hard
complexity result. It may be a causal-boundary or information-availability
obstruction.

The preflight distinction is:

| Question | Data available | Current status |
| --- | --- | --- |
| TP-D1-FINALITY | Full graph plus D1 and witness relation | Candidate polynomial graph inspection after encoding is frozen |
| FP-FINALITY | Accessible subgraph plus local rules | Access-bounded certification problem, not yet a named complexity class |
| T19 gap | Full graph says `R_self_finality`; internal patch cannot audit it | Finite causal-access separation witness |
| T92 restriction | Typed proposition gaps restrict under explicit hypotheses | Narrow degree-0 gap structure, not complexity placement |

## Complexity Claim Gate

No complexity claim may be made until these fields are fixed:

```text
encoding_size:
uniform_family_or_single_instance:
machine_model_for_external_verifier:
machine_model_for_access_bounded_observer:
oracle_access_allowed:
whether_unknown_is_an_output:
promise_conditions:
reduction_type:
resource_bounds:
collapse_conditions:
```

Blocked language until then:

```text
FP-FINALITY is outside all classical classes.
FP-FINALITY is BQP-like.
FP-FINALITY proves a phenomenal bridge theorem.
FP-FINALITY is not computable by any third-person graph computation.
```

Allowed language before then:

```text
The T19 witness separates full-graph witness availability from internal
accessible-witness certifiability.
```

## Narrow Target Before Separation

Accessible-witness gap restriction remains the immediate narrow target for this
branch:

```text
A(U) = ambient/full-graph proposition truth
F(U) = locally auditable proposition truth
G(U) = A(U) - F(U)
```

The complexity track may proceed only after the typed proposition object is
frozen enough to say what counts as the queried language. T92-style restriction
closure helps by making the access gap stable under patch restriction, but it
does not by itself define a complexity class.

## Acceptance Criteria

- The decision problem is stated before any class placement.
- The graph encoding, observer boundary, D1 verifier, proposition domain, and
  witness predicate are explicit.
- Third-person D1 verification and first-person finality verification are
  written as separate problems with separate data access.
- `unknown` or non-certification is handled as either an output value or a
  promise-condition boundary.
- The T19 finite witness is described as a causal-access obstruction unless a
  reduction or oracle model is actually supplied.
- D2 is respected: executable observers are record-bearing reconcilers;
  conscious observers are outside the executable model.
- T8 and T60 are used only as observer-renderer and observer-closure scaffolds.
- The final verdict is one of:

```text
decision_problem_ready_no_complexity_claim
machine_model_incomplete
separation_refuted_by_reduction
access_obstruction_only_not_complexity
```

## Null Or Demotion Conditions

Demote the complexity-separation route if any condition holds:

- The first-person query reduces to third-person D1 verification over the
  accessible subgraph with no residue.
- The alleged separation is only that the observer lacks data, with no
  complexity-theoretic formulation.
- The problem depends on an undefined notion of experience or felt present.
- `unknown` is used as a third truth value while still claiming an ordinary
  decision-language separation.
- The proof requires adding or removing meta-nodes after seeing the answer.
- Self-reference is trivially collapsed by stipulating that `R_self_finality`
  equals `R_obs`.
- The external verifier's problem is not actually fixed or is made artificially
  stronger than the internal verifier's problem by changing the proposition.

Demotion language to preserve:

```text
The current result is an accessible-witness or causal-boundary obstruction,
not a complexity-class separation. The phenomenal-bridge route remains an open
problem until a precise language, verifier model, and reduction boundary are
supplied.
```

## No-Promotion Guardrails

- Do not claim a solution to consciousness or the hard problem.
- Do not claim that observer closure is phenomenal experience.
- Do not claim human belief creates matter or physical records.
- Do not claim a complexity-class separation without a formal language and
  reduction or oracle argument.
- Do not claim that T19's finite witness proves undecidability.
- Do not upgrade C1, D2, H6, or any roadmap status.
- Do not edit ledger, roadmap, tests, models, results, README, or open-problem
  files from this preflight.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-first-person-finality-decision-problem-card.md
```

Required fields:

```text
artifact_type: first_person_finality_decision_problem_card
graph_encoding:
observer_node:
evaluation_event:
accessible_subgraph_operator:
d1_verification_rule:
proposition_domain:
witness_relation:
third_person_problem:
  input:
  available_data:
  output:
  expected_resource_bound:
first_person_problem:
  input:
  available_data:
  output:
  unknown_handling:
machine_models:
  external_verifier:
  access_bounded_observer:
promise_conditions:
reduction_or_oracle_plan:
collapse_controls:
  self_witness_loop:
  external_feedback_into_access_boundary:
  semantic_relabeling_R_self_finality_to_R_obs:
relationship_to_T92:
verdict:
claim_effect: none
no_promotion_guardrail_check:
```

Only after that card is accepted should a later worker attempt a reduction,
oracle separation, or executable complexity audit.
