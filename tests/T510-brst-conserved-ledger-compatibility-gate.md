# T510: BRST Conserved Ledger Compatibility Gate

## Target Claims

No claim-ledger target. This is a TaF-side finite record/ledger gate for the
post-T509 BRST/cohomology burden.

## Setup

T509 made the quotient-compatible observable/readout burden executable: the
operation must descend through the BRST quotient and the readout must annihilate
exact representative shifts.

T510 adds the next finite finality precondition named by
`open-problems/unitarity-as-finality-precondition.md`: even a direct cohomology
readout is only usable as review material if the predeclared dynamics conserves
the quotient ledger.

The finite fixture keeps T509's nontrivial mirror class:

```text
Q(auxiliary) = physical_exact
mirror in ker(Q)
mirror not in im(Q)
```

It then checks whether the candidate ledger satisfies:

```text
dynamics descends through the quotient
readout descends through the quotient
readout is conserved by the dynamics
exact representative noise is absorbed
cohomology drift is blocked
```

## Success Criteria

- A direct exact-invariant cohomology readout under identity dynamics is
  admitted only as a review target.
- Exact representative noise is absorbed when it changes only exact
  representatives and leaves the cohomology ledger stable.
- A quotient-descending dynamics that scales the mirror class is rejected as a
  nonconserved ledger.
- A full-Krein boost is rejected when it does not descend through the BRST
  quotient.
- A W+-only ledger shortcut is rejected because the readout is not
  exact-invariant.
- Exact-mirror, non-nilpotent, missing-control, claim/public-posture,
  external-publication, and cross-repo shortcuts are rejected or blocked.

## Failure Criteria

- T510 treats a drifting cohomology readout as a stable finality ledger.
- T510 admits full-Krein dynamics that do not descend through the quotient.
- T510 treats W+ representative leakage as a conserved quotient ledger.
- T510 converts a conserved finite cohomology ledger into claim evidence,
  public posture, source-action truth, mass-gap evidence, unitarity, physical
  inner-product selection, hidden mirror records, or cross-repo truth.

## Known Physics Constraints

This is finite TaF review machinery. It does not establish a physical BRST
complex, physical operation algebra, physical observable algebra, physical inner
product, real unitarity theorem, real ghost cohomology class, or physical
finality substrate.

## Contribution Needed

A future packet that wants more than review status must predeclare `Q`, the
quotient/cohomology object, dynamics, and readout; prove the dynamics descends
through the quotient; prove the readout annihilates exact representatives; prove
the readout is conserved by the dynamics; include non-descending dynamics,
ledger-drift, exact-representative-noise, and exact-mirror controls; and keep
the result in record/ledger language until physics-side constraints are
supplied.
