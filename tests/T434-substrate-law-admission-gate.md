# T434: Substrate-Law Admission Gate

## Target Claims

- [Region-Indexed Capability Discriminator](../open-problems/region-indexed-capability-discriminator.md)
- T406 transition-system operation-unavailability gate
- T400 boundary-forced task gate
- T403/T405 finality-lock screens

## Setup

T406 showed that operation-unavailability language is absorbed when the only
changed object is the finite transition relation. T434 does not try to supply a
real physical law. It defines the admission gate a future artifact must clear
before a transition-relation split can count as more than transition-system
underdescription.

The gate evaluates a proposed substrate-law or measured-dynamics package for a
future operation-availability split. A package must be fixed before the pair,
shared across both sides, independent of the transition table, independent of
hidden case labels, and able to derive the declared operation availability from
domain-native substrate observables or a measured dynamics protocol.

## Success Criteria

- The current T406 main pair is rejected because it has no independent law or
  measured-dynamics package.
- A transition-table restatement is rejected even if it reproduces the edge set.
- A post hoc law, pair-specific law, hidden-label law, or non-native observable
  package is rejected.
- A measured-dynamics package without enough repeated evidence and a negative
  control is rejected.
- A fixed-accounting mismatch is absorbed before any law verdict is considered.
- Synthetic positive controls show the exact shape that would be admitted:
  a predeclared conservation-style law and a predeclared measured-dynamics
  protocol that derive the transition relation without reading it.
- The result remains admission-only and makes no claim-ledger movement.

## Failure Criteria

The artifact fails if:

- the bare T406 transition split is admitted;
- a transition-table restatement or hidden label is admitted;
- a post hoc or pair-specific law is admitted;
- a package that changes fixed accounting is treated as a law-forced split;
- synthetic positive controls are described as real physics evidence;
- the result claims a physical-arrow theorem, claim promotion, or public posture
  movement.

## Known Physics Constraints

This is a finite admission gate and synthetic positive-control shape. It does
not name or validate any real substrate law, conservation principle,
Hamiltonian, measured platform, or physical finality-lock mechanism.

## Contribution Needed

A future positive Direction-A artifact must bring a concrete domain-native law
or measured substrate dynamics packet that clears this gate, then run the
region-indexed capability discriminator again without changing claim status
unless a separate promotion decision is explicitly authorized.

## Reproduction

```bash
python -m pytest tests/test_substrate_law_admission_gate.py -q
python -m models.substrate_law_admission_gate --write-results
```
