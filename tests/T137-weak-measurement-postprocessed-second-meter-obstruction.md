# T137: Weak-Measurement Postprocessed Second-Meter Obstruction

## Route

Quantum measurement / classical records.

## Question

When does a simultaneous second meter in a weak-measurement platform still fail
Q1C because it is only a downstream transform of the ordinary monitored record?

## Motivation

T130 and T135 narrowed the weak-measurement loophole from "find any second
meter" to "find a simultaneous dual-meter witness with fixed standard
statistics." That still left one ambiguity: a platform might offer two pieces
of hardware while the second channel carries no branch-sensitive content beyond
the ordinary monitored record.

T137 makes that null class explicit.

## Setup

Let:

- `Y` be the ordinary monitored weak-measurement record;
- `Z` be a proposed simultaneous second meter; and
- `B` be the latent branch-relevant variable that a non-null TaF witness would
  need to separate.

T137 asks whether `Z` is screened off by `Y`. If `P(Z | B, Y) = P(Z | Y)`, then
holding the ordinary monitored record fixed also fixes all admissible second-
meter statistics. In that case `Z` cannot create a pre-registered fixed-record
TaF verdict split.

## Success Criteria

- Exact-copy and noisy-downstream second meters are classified as null.
- A branch-sensitive meter that is not screened off by `Y` is identified as the
  minimal escape class.
- Q1C gains a sharper reinstatement gate than "physically distinct hardware."

## Failure Criteria

- A downstream transform of `Y` is allowed to count as a branch-sensitive
  second meter.
- The artifact implies that all dual-meter routes are impossible, rather than
  only the screened-off class.
- The result is described as a new dynamical law rather than an admissibility
  obstruction.

## Claim Impact

Q1C remains dormant. Add the following sharper null condition:

```text
A simultaneous second meter is null whenever its event-level statistics are
conditionally determined by the ordinary monitored record. Physical distinctness
of the hardware does not matter if the second channel is screened off by the
first.
```

## Contribution Needed

Search only for monitored-qubit protocols where the auxiliary meter couples to
branch-relevant structure that is not recoverable from the ordinary trajectory
record or its downstream transforms.
