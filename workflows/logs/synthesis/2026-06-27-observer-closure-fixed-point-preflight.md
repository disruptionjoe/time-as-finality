---
document_type: synthesis_preflight
batch_item: fourth_batch_task_8
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/observer-closure-theorem.md
---

# Observer Closure Fixed-Point Preflight

## Scope

This note completes fourth-batch task 8 as a synthesis/preflight artifact. It
does not prove the observer-closure theorem, change D2, solve the phenomenal
bridge, edit tests or models, or update any canonical claim surface.

The purpose is to turn the existing observer-closure question into a bounded
fixed-point gate: define the access-update operator, check monotonicity,
convergence, least fixed point, uniqueness or non-uniqueness, and self-inclusion
without importing consciousness language.

## Grounding Readout

Read surfaces used:

- `open-problems/observer-closure-theorem.md`.
- `claims/D1-physical-finality-definition.md`.
- `claims/D2-observer-as-record-bearing-system.md`.
- `tests/T60-observer-closure-theorem.md`.
- `guardrails/G1-human-belief-does-not-create-matter.md`.
- `guardrails/G3-observer-rendering-not-mind-created-matter.md`.

Current baseline:

- D2 defines observers as bounded record-processing systems; conscious
  observers are outside the executable model.
- T60 has a finite positive witness: a recorder node `R` converges to a least
  fixed point with self-inclusion in a seven-node fixture.
- T60 does not prove the general theorem and does not prove uniqueness.
- T60 explicitly separates observer closure from phenomenal experience.

## Fixed-Point Object To Freeze

A later executable run must freeze the following object before scoring:

```text
ObserverClosureFixture = (
  graph_class,
  node_set,
  record_edges,
  recorder_node_R,
  base_access_set_A0,
  d1_thresholds,
  finalization_predicate,
  access_update_operator_F_R,
  self_inclusion_predicate,
  record_of_R_predicate,
  hostile_controls
)
```

The central operator is:

```text
F_R : P(nodes) -> P(nodes)
```

where `F_R(S)` returns the updated set of nodes accessible or finalized for
`R` after applying the frozen D1 finalization predicate to the current access
set `S`.

The powerset lattice is ordered by subset inclusion. Knaster-Tarski is
available only if `F_R` is monotone. Uniqueness is a separate question and must
not be inferred from least-fixed-point existence.

## Preflight Protocol

1. Freeze the finite graph class and recorder topology.
2. Freeze `A0`, D1 thresholds, and the exact update rule `F_R`.
3. Check that `F_R` is inflationary or at least that the iteration from `A0`
   is non-decreasing under the declared rule.
4. Check monotonicity:

```text
S subset T implies F_R(S) subset F_R(T)
```

5. Iterate from `A0` until convergence or a bounded failure condition.
6. Enumerate fixed points for the finite fixture class when feasible.
7. Record whether the fixed point reached from `A0` is the least fixed point.
8. Separately record whether the fixed point is unique. If it is not unique,
   narrow the theorem target to least-fixed-point closure.
9. Check whether `R` and at least one record-of-`R` event appear in the least
   fixed-point subgraph.
10. Run hostile controls.

Hostile controls should include:

| Control | Required behavior |
| --- | --- |
| No base record | Pure self-reference without a non-R base should stall or be rejected. |
| No return path | R's own recording events should fail self-inclusion. |
| Access contraction | Any rule that removes previously accessible finalized nodes must block monotonicity. |
| Nonmonotone D1 component | Branch or reversal scoring that decreases under added access must block the theorem claim. |
| Bridge-record ablation | Removing the T60-style bridge record should show whether closure was topology-dependent. |

## Acceptance Criteria

The next run is decision-grade only if all of the following hold:

- `F_R` is explicitly defined as a map on the powerset of finite record nodes.
- The D1 finalization predicate and thresholds are frozen before iteration.
- Monotonicity is proved for the declared class or exhaustively checked for the
  bounded finite family.
- Convergence from `A0` is recorded with step count and terminal set.
- The least-fixed-point claim is justified by monotonicity or by explicit
  finite enumeration.
- Uniqueness is checked separately. If multiple fixed points exist, the run
  states that uniqueness failed and narrows the theorem statement.
- Self-inclusion of `R` and record-of-`R` inclusion are checked separately.
- The bridge-record or base-record requirement is not introduced after seeing
  failure.
- The final verdict is one of:

```text
least_fixed_point_closure_verified
unique_fixed_point_closure_verified
closure_witness_only
monotonicity_failed
self_inclusion_failed
inconclusive_underdeclared_operator
```

## Null Or Demotion Conditions

Demote the theorem target or retain only a fixture-level witness if any of the
following occur:

- `F_R` is not monotone and no narrower monotone class is declared in advance.
- Iteration converges only because the harness silently forbids access removal.
- `R` enters the fixed point only through a circular assumption that `R` was
  already finalized.
- The proof uses the finite T60 witness as if it were a theorem over all finite
  T1 graphs.
- Multiple fixed points exist but the result claims uniqueness.
- The graph class requires hand-picked bridge records for every positive case.
- The update rule changes after observing a stalled or cycling run.
- The result is used as evidence for phenomenal experience, self-awareness, or
  consciousness.

Null result language to preserve:

```text
The fixed-point run did not prove general observer closure. The current safe
status is a finite observer-closure witness plus a narrowed theorem target over
explicitly monotone D1 access-update operators.
```

## No-Promotion Guardrails

- Do not claim observer closure is phenomenal experience.
- Do not claim TaF has solved the hard problem of consciousness.
- Do not claim human belief, self-reference, or observer rendering creates
  matter or record topology.
- Do not promote D2 beyond bounded record-processing systems.
- Do not infer uniqueness from Knaster-Tarski least-fixed-point existence.
- Do not edit `README`, `CLAIM-LEDGER`, `ROADMAP`, tests, models, results, or
  open-problem files from this preflight.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-observer-closure-fixed-point-run-card.md
```

Required sections:

```text
graph_class
recorder_node_R
base_access_set
d1_thresholds
access_update_operator_F_R
monotonicity_check
iteration_trace
fixed_point_enumeration
least_fixed_point_verdict
uniqueness_verdict
self_inclusion_verdict
hostile_controls
allowed_verdict
no_promotion_guardrail_check
```

If later authorized for implementation, the artifact should preserve this
shape:

```text
tests/TXXX-observer-closure-fixed-point-gate.md
models/observer_closure_fixed_point_gate.py
results/observer-closure-fixed-point-gate-v0.1-results.md
```

Do not create those implementation surfaces from this preflight.
