# T14: Integrated Observer-Context Finality

## Target Claims

- [D1: Physical Finality Definition](../claims/D1-physical-finality-definition.md)
- [D2: Observer As Record-Bearing System](../claims/D2-observer-as-record-bearing-system.md)
- [C2: Typed Compositional Finality](../claims/C2-typed-compositional-finality.md)
- [C3: Signed Readout Separation](../claims/C3-signed-readout-separation.md)
- [A1: Distributed Systems Finality Analogy](../claims/A1-distributed-systems-finality-analogy.md)
- [M1: Coupling-Profile Reconstruction](../claims/M1-coupling-profile-reconstruction.md)

## Setup

T14 composes the prior laboratories into one bounded finite witness:

```text
hidden state
  -> record generation
  -> inherited expression
  -> observer coupling
  -> coarse-graining and proof validation
  -> Snowball-style reconciliation
  -> finality profile
  -> signed readout
```

The graph contains three core phase-bearing records, one forged social record,
and one valid-dissent social record. Observers vary by coupling profile,
inherited expression context, and proof-verification requirement.

## Success Criteria

- Coupling profile changes access without changing causal structure.
- Inherited expression can hide a stored record without deleting its identity.
- Proof validation rejects forged records but does not reject valid dissent.
- Snowball-style reconciliation is treated as protocol confidence, not truth.
- Identical finality profiles can still produce different signed readouts.

## Failure Criteria

- T14 treats proof validity as truth.
- T14 treats consensus as a physical law.
- T14 claims finality determines phase-sensitive readout.
- T14 imports a fixed number of fractal or biological layers.
- T14 requires a global clock or universal observer.

## Result

Status: implemented. T14 adds 5 focused tests and a deterministic result file.

The result supports the typed-pipeline reading of Time as Finality. The
framework remains coherent only when finality profile, observer coupling,
inherited expression, proof validity, protocol confidence, and signed readout
are kept separate.
