# T150: Weak-Measurement Verdict-Admissibility Gate

## Route

Quantum measurement / classical records.

## Target Claims

- [Q1C: Weak-Measurement Discriminator Gate](../claims/Q1C-weak-measurement-discriminator-gate.md)
- [Q1: Quantum Under-Finalization](../claims/Q1-quantum-under-finalization.md)

## Question

After T149, can a proposal still manufacture a positive Q1C decision lift by
choosing a verdict target that is really just an auxiliary-meter label or a
vanishingly rare event class?

## Motivation

T149 made "survives full-record conditioning" operational, but it left one
obvious loophole. A proposal could still say:

```text
my auxiliary meter improves prediction of verdict V
```

without showing that `V` is an honest TaF target rather than a label chosen to
favor that meter. T150 turns verdict honesty into a finite gate.

## Setup

Start from a T149-cleared candidate and add:

```text
H = independently typed TaF-relevant hidden axis
V = predeclared verdict class, fixed as a map V = g(H)
s = minimum allowed support for every verdict class
```

Audit five finite classes:

1. `typed_extra_environment_candidate`
   Positive lift, extra-environment architecture, verdict induced from a typed
   hidden axis, balanced support.
2. `typed_enlarged_instrument_candidate`
   Positive lift, explicit instrument enlargement, verdict induced from a typed
   hidden axis, balanced support.
3. `auxiliary_echo_gerrymander`
   Positive lift, but the verdict is really just the auxiliary label.
4. `rare_target_gerrymander`
   Positive lift, but only because the verdict isolates a tiny rare class.
5. `posthoc_target_choice`
   Positive lift, but the verdict target is chosen after analysis.

## Success Criteria

- T149-cleared proposals still fail when the verdict is auxiliary-defined,
  post hoc, or support-gerrymandered.
- Typed verdict candidates survive only when the verdict is a fixed map from an
  independently declared TaF axis.
- The current frontier remains inactive.

## Failure Criteria

- Positive lift alone is allowed to count without a typed target axis.
- Rare-event verdict partitions count as Q1C evidence.
- Auxiliary-meter labels are accepted as if they were independent TaF targets.

## Claim Impact

Q1C remains dormant.

Add this sharpening:

```text
Positive conditional lift is not enough. A non-null Q1C proposal must target a
predeclared TaF verdict map V = g(H) from an independently typed axis H, with
nontrivial support in every verdict class.
```

## Reproduction

```bash
python -m unittest tests.test_weak_measurement_verdict_admissibility_gate -v
python -m models.run_t150
```
