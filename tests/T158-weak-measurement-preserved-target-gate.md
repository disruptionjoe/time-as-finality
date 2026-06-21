# T158: Weak-Measurement Preserved-Target Gate

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)

## Question

T146, T149, and T150 allow one live Q1C architecture class in which the
monitored instrument is enlarged openly. But what counts as an honest
"preserved comparison target" in that class?

## Motivation

Without a sharper gate, an enlarged-instrument proposal can evade the current
null screens by saying:

```text
we changed the instrument, but we still preserve the standard target
```

while only preserving a coarse summary, allowing the target to drift under the
new readout, or never exposing an eventwise map back to the ordinary record at
all. T158 turns that remaining phrase into an executable burden.

## Setup

Declare:

```text
R_std   = full ordinary event-level standard record
R_ext   = enlarged-instrument event record
P       = predeclared eventwise projection from R_ext back to R_std
V       = predeclared Q1C verdict class
```

Audit five finite classes:

1. `honest_enlarged_instrument_candidate`
   The enlargement is explicit, `P(R_ext) = R_std` eventwise, and `R_ext`
   gives positive verdict lift beyond `R_std`.
2. `coarse_preserved_target`
   The proposal preserves only a coarse summary rather than the full standard
   event record.
3. `target_drift_under_enlargement`
   The claimed back-projection changes the standard target on some admissible
   events.
4. `underdeclared_preserved_target`
   The enlargement is declared but the target or projection rule is not frozen
   before analysis.
5. `honest_but_no_lift`
   The target is preserved honestly, but the enlarged record adds no verdict
   value beyond the preserved standard target.

## Success Criteria

- Enlarged-instrument Q1C survives only when the proposal preserves the full
  ordinary event-level record exactly, not approximately or coarsely.
- Target drift under back-projection is null.
- Honest target preservation without extra verdict lift is still null.
- The current Q1C frontier remains inactive.

## Failure Criteria

- A coarse target summary counts as a preserved comparison target.
- Instrument enlargement counts even though the standard target drifts under
  the declared back-projection.
- Positive lift alone is accepted without exact standard-target preservation.

## Claim Impact

Q1C remains dormant.

Add this sharpening:

```text
An enlarged-instrument Q1C route is live only if it predeclares an eventwise
projection back to the full ordinary standard record, preserves that record on
the admissible domain, and still adds positive verdict lift beyond it.
```

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_preserved_target_gate -v
python -m models.run_t158
```
