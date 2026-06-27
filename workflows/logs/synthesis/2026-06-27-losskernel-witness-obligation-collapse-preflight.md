---
document_type: synthesis_preflight
primary_reader: governance
read_pattern: current_state
write_pattern: append
authority: non_authoritative
summarizable: true
source_queue_item: fifth_batch_2
claim_status_change: none
---

# LossKernel Witness-Obligation Collapse Preflight

## Status

Non-authoritative preflight artifact for fifth-batch task 2. This file does
not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, code, tests, results, or
open-problem files. It is not TF1 promotion, not a prior-art-separated
LossKernel theorem, and not a reopening of same-neighbor-data separation.

## Read Surfaces

- `open-problems/loss-kernel-witness-obligation-normal-form.md`.
- `open-problems/loss-kernel-formalization.md`.
- `CLAIM-LEDGER.md`: TF1 row and T220 obligation-factorization context.
- Existing synthesis checklist:
  `workflows/logs/synthesis/2026-06-27-losskernel-normal-form-integration-checklist.md`.

## Preflight Verdict

Current classification:

```text
WO(f,J) survives as a neighbor-reconstructible audit checklist only.
```

The canonical witness obligation is not live as same-neighbor-data novelty.
In the canonical regime, it factors through the neighbor-visible data map:

```text
obligation = psi . nu
```

So if two source cases share `nu`, they share the canonical obligation and the
canonical target-settlement duty. The useful surviving object is an audit
normal form that makes source-derived obligations explicit before they are
absorbed by provenance, effects, lenses, abstraction, CSP explanations, or
other neighbor packages.

## Frozen WO Object

Any future executable artifact must freeze `WO(f,J)` with these fields before
evaluating a candidate split:

| Field | Required content |
| --- | --- |
| `f` | Typed projection or morphism from source to target. |
| `J` | Declared target-side judgment family. |
| `target_judgment` | Exact verdict or settlement question under audit. |
| `source_fiber_class` | Source lifts being compared over the same target or `nu` data. |
| `lift_sensitive_distinctions` | Source differences that would change or settle `J` if visible. |
| `obligation_generators` | Minimal source-derived certificates required to settle `J`. |
| `nu_signature` | Neighbor-visible data granted to mature frameworks. |
| `psi_realizer` | Reconstruction map from `nu` data to the obligation object. |
| `absorbed_vs_live` | Classification as absorbed, audit-useful, or live only under a named missing absorber. |
| `neighbor_visible_realization_map` | Where the same obligation appears in provenance, why-not provenance, abstract interpretation, lenses, CSP explanation, effects, audit data, or path/category data. |

## Canonicality Conditions

`WO(f,J)` is admissible only if these conditions are met:

- Same morphism, same source and target structures, and same judgment family
  yield the same witness-obligation normal form.
- Obligations are derived from source fibers and judgment dependence, not
  attached as prose labels.
- Renaming a lost label does not change the object unless it changes the typed
  source, target, `J`, or `nu` data.
- The artifact states whether each generator is reconstructed by `psi(nu)` or
  requires an explicit non-factoring source field.
- The artifact records a collapse verdict when obligations are constant on
  each `nu` fiber.

## Collapse Rule

The default T220 rule is:

```text
nu: source case -> neighbor-visible data
psi: neighbor-visible data -> witness obligation
obligation = psi . nu
```

Operational consequence:

```text
nu(y1) = nu(y2) => WO(y1) = WO(y2)
```

Under this rule, a claimed separation inside one `nu` fiber is a bug in the
packet unless the artifact has named a legitimate non-factoring source field
and then shown that admitting that field to neighbor packages still does not
absorb the split.

## Escape Admission Gate

An escape from collapse is admissible for testing only if the candidate source
field satisfies all items:

- It is declared before the witness pair and before the verdict split.
- It is not readable from the frozen `nu_signature`.
- It is legitimate task data, not a hidden label introduced only to separate
  the pair.
- It changes `WO(f,J)` by a repeatable derivation rule.
- The neighbor packages are allowed to receive the field as enlarged data
  `nu_prime`.
- The split survives after `nu_prime` is available to provenance, effects,
  lenses, abstraction, CSP explanations, audit data, path data, and category
  data.
- A negative control confirms the audit can report collapse when the field is
  absorbable.

## Acceptance Criteria

| Criterion | Preflight handling |
| --- | --- |
| Freezes `WO(f,J)` fields and canonicality conditions. | See Frozen WO Object and Canonicality Conditions. |
| Treats `obligation = psi . nu` as collapse-into-neighbor in the canonical regime. | See Preflight Verdict and Collapse Rule. |
| Preserves the object as an audit checklist only. | The verdict classifies WO as neighbor-reconstructible audit machinery. |
| Requires any escape to name a legitimate non-neighbor-readable source field. | See Escape Admission Gate. |

## Null Or Demotion Conditions

Treat a proposed WO artifact as null or demoted if any condition holds:

- `WO(f,J)` changes when only prose labels or explanations change.
- The target judgment `J` is selected after seeing the desired split.
- The source fiber is not actually matched on the declared `nu_signature`.
- The obligation generators are hand-built annotations instead of derived
  source-fiber duties.
- The obligation factors through `nu`, but the artifact still reports novelty.
- The split disappears when the named source field is admitted as `nu_prime`.
- The object does not improve admissibility review, comparison, or hostile
  audit relative to existing neighbor machinery.
- The result is summarized as "some hidden source distinction matters" with no
  canonical witness object.

## No-Promotion Guardrails

- Do not change TF1 out of `open_formal_target`.
- Do not call WO a prior-art-separated obstruction object.
- Do not reopen same-neighbor-data novelty for the canonical T220 regime.
- Do not claim T220 closes all possible future non-factoring constructions.
- Do not treat an escape as live until a `nu_prime` absorber run fails.
- Do not edit ledger, roadmap, tests, models, results, or open problems from
  this preflight.

## Next Executable Artifact Shape

The next artifact should be a collapse-certificate packet:

```text
artifact_type: witness_obligation_collapse_packet
f:
J:
source_structure:
target_structure:
target_judgment:
nu_signature:
source_fiber_class:
lift_sensitive_distinctions:
obligation_generators:
psi_realizer:
factorization_check: obligation = psi . nu
fiber_constancy_result:
neighbor_visible_realization_map:
non_factoring_source_field:
nu_prime_absorption_attempt:
negative_control:
verdict: collapsed_to_neighbor | audit_checklist_only | admit_for_escape_audit
claim_impact: no_status_change
```

The packet may certify collapse or make later review cleaner. It cannot by
itself promote LossKernel or TF1.
