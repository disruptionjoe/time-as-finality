# T386: Bidirectional Handshake Origin Screen

## Target Claims

D1, R1, S1, PO1, and the T385 `handshake_origin` open object:

```text
Can the bidirectional handshake premise be derived from compatibility, or only
from a stronger interpretation of compatibility as mutual local attestability?
```

## Setup

Compare protocol semantics:

- one-sided readout,
- broadcast without acknowledgment,
- shared scalar token,
- global reconciler receipt,
- minimal bidirectional handshake,
- three-phase commit handshake,
- signed anti-handshake,
- asymmetric receipt handshake.

## Success Criteria

- Show raw compatibility remains underdetermined.
- Reject one-sided and broadcast semantics as not mutually attestable.
- Reject scalar tokens as lacking signal geometry.
- Reject global reconcilers as hidden ordering/certification layers.
- Reject signed anti-handshakes as source-incompatible.
- Demote overcomplete protocol phases.
- Identify whether mutual local attestability conditionally forces a minimal
  two-leg handshake.

## Failure Criteria

- Claim that raw compatibility alone derives bidirectionality.
- Hide the added mutual-attestability semantics.
- Let global reconciliation count as local compatibility.
- Treat a scalar shared token as a null-signal basis.

## Known Constraints

This is a finite protocol-semantics screen, not a completeness theorem over all
possible distributed protocols.

## Contribution Needed

If the minimal bidirectional handshake survives, the next target is:

```text
derive or falsify why compatibility should mean mutual local attestability.
```
