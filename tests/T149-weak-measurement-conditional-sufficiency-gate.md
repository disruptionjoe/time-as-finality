# T149: Weak-Measurement Conditional-Sufficiency Gate

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)

## Question

Can the T146 phrase "survives full-record conditioning" be turned into a
finite operational gate, so future Q1C weak-measurement proposals can be
accepted or rejected before more platform prose is written?

## Setup

Declare a finite decision problem:

```text
R = full ordinary event-level monitored record
A = auxiliary channel or meter output
V = predeclared Q1C verdict class
L = declared 0-1 verdict loss in the finite model
```

Compute the Bayes risk for predicting `V` from `R` alone and from `(R,A)`.
The conditional lift is:

```text
risk(V | R) - risk(V | R,A)
```

A non-null Q1C proposal must have positive lift at fixed full ordinary record
and must also type the physical source of the lift as either:

1. extra environment or detector structure not included in the ordinary
   transcript; or
2. an explicit instrument enlargement with a predeclared preserved comparison
   target.

## Success Criteria

- Screened-off and independent-noise auxiliary meters have zero lift.
- Coarse-record refinements and postselected lifts are null.
- Same-instrument positive lift without an extra-structure or enlargement
  declaration is underdeclared, not a live route.
- Extra-environment and declared enlarged-instrument cases are the only live
  candidate classes.
- The current Q1C frontier remains inactive.

## Failure Criteria

- A zero-lift auxiliary channel is treated as verdict-changing.
- Positive lift from a coarse record is allowed to count.
- Same-instrument positive lift is promoted without naming extra physical
  structure or declaring instrument enlargement.
- Instrument enlargement counts without a preserved comparison target.

## Claim Impact

Q1C remains dormant, but its reinstatement condition is now sharper:

```text
positive predeclared decision-risk lift at fixed full ordinary event record
+ typed extra-environment or enlarged-instrument architecture
```

This does not upgrade weak measurement. It prevents future Q1C work from
treating "not screened off" as an undefined phrase.

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_conditional_sufficiency_gate -v
python -m models.run_t149
```
