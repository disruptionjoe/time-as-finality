---
document_type: synthesis_preflight
batch_item: fourth_batch_task_1
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/accessible-witness-gap-restriction-theorem.md
---

# Accessible Witness Gap Restriction Preflight

## Status

This completes fourth-batch task 1 as a synthesis/preflight artifact. It does
not edit `README`, `CLAIM-LEDGER`, `ROADMAP`, tests, models, results, or
open-problem files. It is not theorem promotion and not a C1 status change.

## Read Surfaces

- `open-problems/accessible-witness-gap-restriction-theorem.md`.
- `tests/T19-phenomenal-bridge-complexity-separation.md`.
- `tests/T58-gap-phantom-equivalence.md`.
- `tests/T92-accessible-witness-gap-restriction.md`.
- `results/accessible-witness-gap-restriction-v0.1-results.md`.
- `technical-reports/TECHNICAL-REPORT-accessible-witness-gap-restriction-v0.1.md`.
- `workflows/logs/synthesis/2026-06-27-t19-t58-common-typed-gap-category-decision.md`.

## Preflight Verdict

The next artifact should be a lemma-card or run-card that freezes the typed
proposition-domain object before any further theorem language is used:

```text
For finite typed proposition-domain accessible-witness systems satisfying
ambient restriction, audit monotonicity, and stable proposition typing,
G(U)=A(U)-F(U) restricts contravariantly:
rho_{U,V}(G(U)) subset G(V).
```

The T92 context supports this as a finite conditional audit with explicit
boundaries. This preflight does not upgrade that audit into an arbitrary-cover
presheaf theorem.

## Frozen Objects

Patch:

```text
U = (events_U, holders_U, causal_past_U, witness_access_U)
```

Patches form a finite inclusion poset. For `V subset U`, every event, holder,
and causal-past witness available in `V` must be interpreted through the
restriction of the larger patch `U`.

Proposition domain:

```text
P_O = finite typed propositions about observer O
```

The first theorem instance should keep the T19 two-proposition domain unless a
proof obligation requires a larger domain:

```text
P_R = {R_obs, R_self_finality}
```

Ambient object:

```text
A(U) = propositions in P_O whose truth is fixed by the full record graph
       and remains expressible at U.
```

`A(U)` is third-person/ambient. It must not import first-person access.

Auditable object:

```text
F(U) = propositions in P_O auditable using only U-accessible holders and
       causal-past witnesses.
```

`F(U)` is local to the patch. External full-graph knowledge is not allowed in
the audit.

Gap object:

```text
G(U) = A(U) - F(U)
```

Restriction map:

```text
rho_{U,V}: P_O(U) -> P_O(V)
```

`rho_{U,V}` is defined only for propositions that remain expressible at `V`.
It must preserve proposition type and witness requirement. Semantic relabeling
is not an admissible restriction map.

## Conditions To Freeze

Ambient restriction:

```text
p in A(U) and rho_{U,V}(p) defined
  implies rho_{U,V}(p) in A(V).
```

Audit monotonicity:

```text
rho_{U,V}(p) in F(V) implies p in F(U).
```

Equivalently, a smaller patch cannot gain a witness that the larger patch lacks
unless the example is being marked as an audit-monotonicity boundary control.

Stable proposition typing:

```text
type(rho_{U,V}(p)) = type(p)
```

In particular, `R_self_finality` may not be identified with `R_obs` unless that
identification is declared as a collapse condition and excluded from evidence.

Witness locality:

```text
F(U) depends only on U-accessible holders and U causal-past witnesses.
```

Non-circular construction:

```text
A and F are defined before G is computed.
G is not obtained by removing the desired counterexample after inspection.
```

Closure target:

```text
p in G(U) and rho_{U,V}(p) defined
  implies rho_{U,V}(p) in G(V).
```

Closure is not surjectivity. A gap at `V` need not lift to a gap at `U`.

## Required Controls

The next executable or proof-shaped artifact must include these controls:

| Control | Purpose | Expected verdict |
| --- | --- | --- |
| T19 unary witness | Checks the original proposition-domain gap | Closure holds if the three conditions hold |
| Non-chain joint witness | Prevents restating only the T19 chain | Closure holds if the three conditions hold |
| Semantic relabeling | Tests whether `R_self_finality` is collapsed into `R_obs` | Stable typing fails; closure evidence rejected |
| Audit-monotonicity violation | Tests a smaller patch gaining audit power absent in the larger patch | Audit monotonicity fails; closure evidence rejected |
| Ambient restriction violation | Tests non-functorial ambient truth | Ambient condition fails; no theorem evidence |
| Circular gap construction | Tests defining `F` or `G` by desired outcome | Invalid construction |

At least one failing control is required. A theorem-shaped pass with no hostile
counterexample does not satisfy this preflight.

## Acceptance Criteria

- Patch, proposition domain, `A`, `F`, `G`, and `rho` are frozen before examples
  are evaluated.
- The T19 two-proposition domain is used as the first instance, or any
  expansion beyond it is justified as a proof obligation.
- Ambient restriction, audit monotonicity, and stable proposition typing are
  named as hypotheses, not discovered after the pass.
- Semantic relabeling is rejected as a collapse condition, not counted as a
  legitimate bridge.
- At least one non-chain positive witness and at least one necessary-condition
  counterexample are included.
- The final verdict is one of:

```text
conditional_finite_restriction_supported
restriction_refuted_by_well_typed_counterexample
conditions_insufficient_or_circular
not_executed
```

- Any success is stated as a finite typed proposition-domain result only.

## Null Or Demotion Conditions

Demote the theorem target to an isolated finite lemma if any condition holds:

- A well-typed, audit-monotone witness has `rho(G(U))` outside `G(V)`.
- Proposition restriction cannot be defined without semantic choices.
- `A(U)` is not ambiently functorial under restriction.
- A smaller patch can audit a proposition whose larger patch cannot audit.
- `R_self_finality` has to be identified with `R_obs` to make closure hold.
- The proof depends on defining `F` as `A - desired_gap`.
- The only positive example is the original T19 chain witness.

Demotion language to preserve:

```text
T19 remains a finite Accessible Witness Gap Lemma. It shares degree-0
ambient/local failure shape with T58, but it is not licensed as a
gap-presheaf-style restriction theorem under the tested maps.
```

## No-Promotion Guardrails

- Do not upgrade C1 or any phenomenal-bridge claim.
- Do not claim a consciousness theorem or hard-problem solution.
- Do not place `FIRST-PERSON-FINALITY` in a complexity class.
- Do not claim a general H1/cohomology result.
- Do not identify T19 proposition gaps with T58 order-pair phantom gaps.
- Do not call raw `G=A-F` a presheaf without the typed restriction hypotheses.
- Do not edit ledger, roadmap, tests, models, results, README, or open-problem
  files from this preflight.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-accessible-witness-gap-restriction-lemma-card.md
```

Required fields:

```text
artifact_type: accessible_witness_gap_restriction_lemma_card
patch_poset:
proposition_domain:
type_system:
restriction_maps:
ambient_object_A:
auditable_object_F:
gap_object_G:
hypotheses:
  ambient_restriction:
  audit_monotonicity:
  stable_typing:
  witness_locality:
positive_witnesses:
  t19_unary:
  non_chain:
necessary_condition_controls:
  semantic_relabeling:
  audit_monotonicity_violation:
  ambient_restriction_violation:
closure_check:
non_lifting_check:
verdict:
claim_effect: none
no_promotion_guardrail_check:
```

If later authorized for implementation, the executable surface should preserve
the same shape in a test/model/results triplet. This preflight does not create
or modify those implementation surfaces.
