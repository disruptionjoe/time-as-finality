# T511: Boundary Adapter Finality Gate

## Target Claims

No claim-ledger target. This is a TaF-side finite adapter/finality gate for the
boundary-adapter triangle intake from 2026-07-09.

## Setup

The boundary-adapter intake asks whether a boundary-supplied datum becomes
TaF-final only when the relevant undo or readout handle is inadmissible.

T511 keeps the question local to Time as Finality. It does not assert a GU/TaF/TI
identity, does not import sibling-repo truth, and does not treat boundary supply
or source crossing as finality.

The finite packet must predeclare:

```text
Domain
Boundary adapter B
Region / observer boundary
Admissible operations
Candidate record
Undo or readout handle
Ledger or invariant
Fixed-richer-source absorber
Positive control
Failure control
Verdict
```

## Success Criteria

- A packet is admitted only as review material when the region, operation class,
  record, undo/readout handle, invariant ledger, positive control, failure
  control, and fixed-richer-source absorber are all explicit.
- The undo/readout handle must be inadmissible under the declared operation
  class, not merely absent from prose.
- The ledger must be conserved by the declared adapter dynamics.
- Boundary supply alone, source-crossing language alone, and cross-repo identity
  shortcuts are rejected or blocked.

## Failure Criteria

- T511 treats an admissible undo/readout handle as final.
- T511 treats a missing handle as the same thing as an inadmissible handle.
- T511 admits a drifting ledger.
- T511 converts boundary supply into TaF support for GU or Temporal Issuance.
- T511 moves claim status, canon, North Star, public posture, hard policy,
  external publication, or cross-repo truth.

## Known Physics Constraints

This is finite TaF review machinery. It does not establish a physical boundary
adapter, a conserved universal ledger, BRST physicality, GU support, Temporal
Issuance support, a hidden central server, or a physics-side irreversibility
claim.

## Contribution Needed

A future packet that wants more than review status must supply a domain-native
adapter theorem, counterexample, or executable fixture whose admissible
operation class and finality handle are fixed before the witness pair is chosen.
The packet must still keep cross-repo identity claims gated.
