# Technical Report: Thermodynamic Erasure Calibration v0.1

## Claim Under Test

T141 left H7 with copy/erase and branch-support edges on an explicit T1 record
graph. T142 asks whether those edges survive standard thermodynamic absorption.

## Artifact

T142 adds an executable calibration that distinguishes:

- reversible observer-boundary changes;
- correlated uncopy when source-copy correlations and reversible control are
  retained;
- blind reset or overwrite, which is absorbed by ordinary erasure/free-energy
  accounting;
- formal resource drawdown whose physical status is withheld until the
  resource unit is typed.

## Result

No tested strict T1 D1 increase carries an independent thermodynamic arrow.

Access grants are boundary changes. Same-chain copy and branch-spread copy
each have two ordinary reverse descriptions:

- with full correlation/control access, the added copy can be uncomputed with
  no blind erasure;
- without that handle, resetting the copy is a one-bit erasure/free-energy
  ledger item.

T142 also preserves a non-arrow residue: same-chain copy and branch-spread copy
have the same one-bit blind-reset floor but different D1 deltas. That shows D1
topology is not identical to thermodynamic erasure cost, but the difference is
not a thermodynamic arrow by itself.

## Current Strongest Claim

H7 survives only as a resource-accounting or constructor lemma. T1 record
copying and branch spreading do not supply independent physical-arrow evidence.
They are reversible under full microstate/control access or absorbed by
ordinary erasure/free-energy accounting under blind reset.

## What This Improved

The calibration blocks two opposite mistakes:

- overclaiming that every record-copy deletion is thermodynamic erasure;
- underclaiming the cost of blind reset when reversible uncopy handles are not
  available.

It also cleanly separates D1 topology from thermodynamic cost.

## What This Weakened Or Falsified

T142 weakens any H7 reading that treats increased support, redundancy, or
branch robustness as physical-arrow evidence. Those increases may still matter
for access, provenance, or future operations, but thermodynamic irreversibility
has to come from named free-energy, heat-bath, blank-capacity, sink, boundary,
or excluded-control data.

## Falsification Condition

T142 fails in H7's favor only if a physically typed record substrate gives a
strict D1 increase whose reverse remains inadmissible after full reversible
correlation access, heat-bath erasure cost, blank-capacity use, sink state,
boundary conditions, and provenance/control data are all included and matched.

## Claim Ledger Update

Add T142 to H7:

```text
T142 calibrates the T141/T128 survivor against thermodynamic absorbers. Access
grants are boundary changes; copied records can be reversed by correlated
uncopy when the full handle remains, or by ordinary one-bit erasure/free-energy
accounting when blindly reset. H7 remains a resource-accounting/constructor
lemma, not a thermodynamic-arrow derivation.
```

## Open Blocker

Find a physically typed record substrate where D1 topology changes future
operation availability at fixed free-energy, capacity, sink, boundary,
provenance, and reversible-control data.

## Next Work

Either demote H7's paper-facing label to resource-accounting lemma, or attempt
a non-equilibrium physical model with named free-energy and capacity variables
fixed before D1 scoring.

## Reproduction

```bash
python -m unittest tests.test_thermodynamic_erasure_calibration -v
python -m models.run_t142
```
