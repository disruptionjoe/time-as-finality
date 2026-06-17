# T15: Generated Integrated Finality Stress Lab

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D2: Observer As Record-Bearing System](../claims/D2-observer-as-record-bearing-system.md)
- [C2: Typed Compositional Finality](../claims/C2-typed-compositional-finality.md)
- [C3: Signed Readout Separation](../claims/C3-signed-readout-separation.md)
- [A1: Distributed Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [M1: Coupling-Profile Reconstruction](../claims/M1-coupling-profile-reconstruction.md)

## Setup

T15 replaces T14's single witness with a deterministic generated family. It
sweeps:

- core record sizes `2..5`;
- every non-all-positive signed weight pattern;
- inherited expression masking on or off;
- adversary modes: none, forged, valid dissent, both.

Each generated case is evaluated through the T14 integrated pipeline:

```text
record generation
  -> inherited expression
  -> observer coupling
  -> proof validation
  -> finality profile
  -> signed readout
```

## Success Criteria

- The generator is deterministic.
- The generated family contains T14-style successes.
- The generated family finds minimal profile/readout separation witnesses.
- Proof filtering rejects forged records when required.
- Valid dissent remains visible under proof filtering.
- Results include both robust regions and breakpoints.

## Failure Criteria

- T14 works only as one hand-built special case.
- Signed readout separation disappears across generated cases.
- Proof validation is reported as truth.
- Valid dissent is incorrectly filtered as if it were forgery.
- Expression masking is confused with ordinary channel inaccessibility.

## Result

Status: implemented. T15 adds 5 focused tests and a deterministic 448-case
sweep.

The sweep supports T14 as a family-level pattern rather than a single special
case, but it preserves the hard limit: proof filtering rejects forgery, not
valid disagreement, and signed phase weights are still assigned rather than
dynamically generated.
