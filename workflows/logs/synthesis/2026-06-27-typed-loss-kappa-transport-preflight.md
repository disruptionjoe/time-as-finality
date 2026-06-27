---
document_type: synthesis_preflight
queue_item: 10
status: complete
authority: non_authoritative
write_scope: workflows/logs/synthesis
claim_effect: none
source_open_problem: open-problems/typed-loss-transport-test.md
---

# Typed-Loss Kappa Transport Preflight

## Scope

This is a preflight artifact for the typed-loss transport test in
`open-problems/typed-loss-transport-test.md`. It prepares a decision-grade run
that tests whether a domain-neutral `kappa` value can be transported from one
mature absorber to another and predict the target's native obstruction value
before that value is computed natively.

This preflight does not compute kappa, construct the transport map, promote a
classification theorem, or update claim surfaces.

## Core Bet Under Test

The test changes the unit of analysis from an object that a mature absorber can
own to a map between absorbers.

Domain-neutral candidate:

```text
kappa(nu) = rank / dimension / information measure of the set of global
            sections that the neighbor-visible data map nu cannot distinguish
```

The run must define this once and use it without per-domain retuning.

## First Instance

Source domain:

```text
A = CSP-PO1 signed-graph frustration, fully specified by the selected fixture
```

Target domain, choose exactly one for the first execution:

```text
B = T21 Bell/CHSH contextuality H1 obstruction
```

or

```text
B = T28 CAP/consensus obstruction
```

The target choice must be recorded before the source kappa is computed. A
second unrelated absorber is required only for any later theorem-shaped
promotion attempt.

## Inputs To Freeze Before Execution

Read surfaces:

- `open-problems/typed-loss-transport-test.md`.
- CSP-PO1/T39 source fixture selected by the executor.
- T21 or T28 target fixture selected by the executor.
- Any T220-style obligation-factoring context used to define `nu`.

Pre-register these fields:

```text
source_fixture_id
target_fixture_id
neighbor_visible_map_nu_A
kappa_definition
structure_preserving_map_A_to_B
target_native_obstruction_definition
prediction_record_format
falsification_condition
```

No target native value may be computed or imported before the prediction record
is written.

## Preflight Protocol

1. Define `nu_A` and the domain-neutral `kappa` formula before selecting
   numerical witnesses.
2. Freeze a CSP-PO1 signed-graph source fixture.
3. Choose one target absorber, either T21 Bell/CHSH or T28 CAP/consensus.
4. Define the structure-preserving map `A -> B`. It must preserve
   neighbor-visible structure, not domain semantics by stipulation.
5. Compute `kappa_A`.
6. Write a sealed prediction for the target native obstruction value or native
   comparison class.
7. Only after the prediction exists, compute the target obstruction natively
   using the target's own definitions.
8. Compare prediction and native result.
9. Classify the outcome without changing the kappa definition.

## Anti-Construction Controls

The executable run must include controls that prevent a pass-by-design result:

| Control | Required behavior |
| --- | --- |
| Independent target native value | Target obstruction is computed from target-native definitions, not copied from `kappa_A`. |
| No shared derivation | The `A -> B` map does not simply re-encode the same construction under new names. |
| Same-visible non-split | At least one same-visible-data pair does not falsely produce a split. |
| Count-all classifier | A naive count of hidden states is tested and distinguished from kappa where possible. |
| Falsifying branch | The harness has an explicit outcome in which the prediction misses. |

## Acceptance Criteria

The first execution is accepted as decision-grade only if all of the following
hold:

- `kappa` is defined once before domain-specific calculation.
- `nu_A` is frozen and the source fixture is fully specified.
- The map `A -> B` preserves the declared neighbor-visible structure.
- The target native obstruction definition is frozen before prediction.
- The target prediction is recorded before native target computation.
- The target native value is computed independently of the source fixture.
- The final verdict is one of:
  `prediction_hit`, `prediction_miss`, `map_not_structure_preserving`,
  `kappa_not_domain_neutral`, or `inconclusive_missing_native_value`.
- A miss is recorded as real evidence against the breakout bet unless the run
  identifies a pre-registered map-typing failure.

The only promotion-relevant success would require later prediction hits across
at least two unrelated absorbers with no shared derivation. This preflight
licenses no such promotion.

## Null Or Demotion Conditions

Demote or kill the transport bet if any of these occur:

- `kappa` cannot be defined domain-neutrally and always needs a per-domain
  choice.
- Every proposed `A -> B` map fails to preserve neighbor-visible structure.
- The target and source secretly share a derivation, making the test a
  re-encoding catalogue rather than a prediction.
- The first prediction misses and no pre-registered structure-preserving map
  repair applies.
- The target native value is known or constructed before the prediction record.
- The result depends on changing units or normalizations after seeing the target
  value.

Null result language to preserve:

```text
The transport test did not support a domain-neutral kappa invariant. The
cross-domain recurrence is currently best treated as a projected template or
multi-domain encoding catalogue, not a transport law.
```

## No-Promotion Guardrails

- Do not promote a cross-domain classification theorem from one target hit.
- Do not promote physics, geometry, curvature, spacetime, quantum-foundational,
  consciousness, or new-object language from this run.
- Do not call kappa a transportable invariant if it was retuned per domain.
- Do not call an encoding catalogue a prediction.
- Do not edit `CLAIM-LEDGER.md`, `ROADMAP.md`, tests, models, results, README,
  or open-problem files from this preflight.
- Do not use source kappa as the target native obstruction definition.

## Next Executable Artifact Shape

Recommended next artifact:

```text
workflows/logs/synthesis/YYYY-MM-DD-typed-loss-kappa-transport-run-card.md
```

If later authorized for implementation, the run-card can be converted into a
test/model/results triplet. That later triplet should preserve this shape:

```text
tests/TXXX-typed-loss-kappa-transport-spec.md
models/run_typed_loss_kappa_transport.py
results/typed-loss-kappa-transport-v0.1-results.md
```

Do not create those implementation surfaces from this preflight.

Required run-card sections:

```text
source_fixture
target_fixture
kappa_definition
nu_freeze
map_A_to_B
prediction_record
target_native_computation_plan
control_results
comparison
verdict
no_promotion_guardrail_check
```

Minimum prediction record:

```text
prediction_timestamp:
source_kappa:
target_native_quantity_predicted:
predicted_value_or_class:
allowed_tolerance_or_native_comparison:
falsification_condition:
sealed_before_native_target_computation: true
```
