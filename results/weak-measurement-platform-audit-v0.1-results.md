# T91 Results: Weak-Measurement Platform Audit

## Platform audits

| Platform | Candidate axis | Classification | Blocker |
| --- | --- | --- | --- |
| superconducting homodyne trajectory | branch-live witness from homodyne current plus Bayesian trajectory estimate | `null_same_record_derivation` | candidate axis is reconstructed from the same monitoring record as the standard trajectory |
| superconducting phase-qubit uncollapse | reversal-cost witness from partial-collapse reversal success | `null_postselected_axis` | candidate axis depends on success-conditioned or null-outcome selection |
| three-level superconducting quantum-jump reversal | mid-flight warning and feedback reversal as branch-live or reversal witness | `null_same_record_derivation` | candidate axis is reconstructed from the same monitoring record as the standard trajectory |

## Strongest claim

The concrete superconducting weak-measurement platforms audited here do not yet supply an independent D1 branch-support or reversal-cost observable. They validate quantum trajectory control, but the proposed TaF axes collapse either to the same monitored record or to postselected recovery.

## What this improved

T91 replaces T90's platform placeholder with a concrete negative audit. The repo can now say which named experimental families fail the independent-axis test and why.

## What this weakened

This weakens the idea that currently standard superconducting weak-measurement setups already contain a hidden TaF discriminator waiting to be relabeled.

## Falsification condition

T91 fails if a named weak-measurement platform supplies a pre-registered branch/provenance/reversal observable that is not reconstructible from the same standard monitoring record, does not rely on success-conditioned postselection, and changes the TaF verdict while the standard record is held fixed.

## Q1 update

Keep Q1 partially supported, but narrow the T12 route further: known superconducting homodyne, uncollapse, and quantum-jump-reversal platforms do not yet instantiate the independent D1 axis required by T90.

## Blocker

The missing object is still the same one: a pre-registered branch, provenance, or reversal-cost observable that is operationally distinct from the monitored trajectory record itself.

## Recommended next

Stop treating standard homodyne/jump-reversal platforms as near-ready T12 tests. Search instead for a duplicated-record provenance channel during monitoring or a physically metered undo cost that is fixed before analysis and not success-conditioned.
