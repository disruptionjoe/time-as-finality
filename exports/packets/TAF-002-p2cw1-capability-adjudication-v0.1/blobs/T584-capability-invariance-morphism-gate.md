# T584: Capability Invariance Morphism Gate

## Target Claims

The TaF-owned region-indexed capability object, T583, TAF3, TAF8, and the
`CAPABILITY-TO-TEMPORAL-ORDER` lane.

## Setup

Use T583 CapabilityContract v1 as the source contract. Define finite
admissible morphism classes for:

- substantive representation changes: raw task interface, measurement units,
  protocol labels, and implementation traces change while physical content is
  preserved;
- gauge changes: representatives and phase labels move inside the declared
  quotient;
- irrelevant coarse-graining: predeclared telemetry and display fields are
  removed.

Then include one deliberately inadmissible morphism: merging certification and
recovery task vocabulary.

## Success Criteria

- Admissible representation morphisms preserve the native Pareto envelope.
- Admissible gauge morphisms factor through the declared quotient.
- Declared irrelevant coarse-graining preserves the physical payload and
  attainable envelope.
- Capability remains nontrivial: distinct controller traces may have the same
  capability.
- The task-vocabulary merge counterexample changes the native envelope and is
  rejected as inadmissible.

## Failure Criteria

- A unit/interface representation change alters capability.
- A gauge representative creates a capability delta.
- Dropping declared irrelevant telemetry changes the physical payload.
- Capability collapses to full state identity.
- A task-vocabulary merge is accepted as a physical-equivalence morphism.

## Run Commands

```text
python -m models.t584_capability_invariance_morphism_gate --write-results
python -m unittest tests.test_t584_capability_invariance_morphism_gate -v
```

## Boundary

T584 is a finite invariance gate only. It does not establish a universal
capability measure, a genuine physical capability model, physical time,
issuance, a source law, public posture movement, or cross-repository identity.
