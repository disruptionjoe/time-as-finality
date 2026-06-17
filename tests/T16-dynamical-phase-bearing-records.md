# T16: Dynamical Phase-Bearing Records

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [C3: Signed Readout Separation](../claims/C3-signed-readout-separation.md)
- [C2: Typed Compositional Finality](../claims/C2-typed-compositional-finality.md)
- [G2: Not A Replacement Theory](../guardrails/G2-not-a-replacement-theory.md)

## Setup

T16 connects the T9 local-dynamics laboratory to T13-T15 signed readout.

Instead of assigning phase/sign weights by hand, it derives them from
counterfactual traces in elementary cellular automata:

```text
terminal 0 -> 1 trace cell gets weight +1
terminal 1 -> 0 trace cell gets weight -1
```

The finality profile remains phase-blind. It counts accessible generated
trace records, holder redundancy, branch support, and reversal count.

## Success Criteria

- Signed weights are generated from local dynamics.
- The same phase-blind finality profile can have different signed readouts.
- Generated traces can cancel to zero readout.
- The generated records can be loaded into the T13 readout graph without
  changing T13 machinery.
- The result is not presented as a derivation of quantum mechanics.

## Failure Criteria

- Signed weights are assigned manually rather than derived from the dynamics.
- No profile/readout separation witness is found.
- No dynamically generated cancellation witness is found.
- The result is used to claim a physical quantum interference experiment.

## Result

Status: implemented. T16 adds 6 focused tests and a deterministic sweep across
`49,152` elementary-cellular-automaton trace cases.

T16 finds dynamically generated signed traces where the same finality profile
maps to readouts `0.0` and `4.0`. It also finds a generated trajectory whose
readout alternates between `0.0` and `1.0`.
