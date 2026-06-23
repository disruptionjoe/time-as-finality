# RSPS Robustness Sweep v0.1 Results

## Verdict

Main verdict: `supported_with_boundaries`.

The sweep supports RSPS as a modest flat-QM basis/objectivity selector across finite perturbations, with explicit boundaries. It does not derive Born weights, does not solve measurement, and does not promote a TI or GU physics bridge.

Claim placement: [RSPS](../claims/RSPS-record-stability-pointer-selection.md), bounded by [Q1A](../claims/Q1A-access-boundary-record-accounting.md) and [N10](../literature/N10-q1a-spectrum-broadcast-structure-absorber.md).

## Summary

- Fixture rows: 38
- Verdict counts: `{'pass': 33, 'degenerate': 3, 'absorber_owned_audited_redundancy_required': 2}`
- Failures: `[]`
- Born-weight imports: `[]`

## Result Table

| Fixture | Verdict | Argmax theta | Expected theta | Pointer F | Conjugate F | Redundancy | Audited redundancy | Note |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| R0 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Reproduces pointer-basis selection with no Born-weight output. |
| R1-N1 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 0.881 | 0.881 | Pointer selection persists as N changes; redundancy scales with accessible fragments. |
| R1-N2 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 1.763 | 1.763 | Pointer selection persists as N changes; redundancy scales with accessible fragments. |
| R1-N4 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 3.525 | 3.525 | Pointer selection persists as N changes; redundancy scales with accessible fragments. |
| R1-N8 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Pointer selection persists as N changes; redundancy scales with accessible fragments. |
| R1-N16 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 14.101 | 14.101 | Pointer selection persists as N changes; redundancy scales with accessible fragments. |
| R1-N32 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 28.201 | 28.201 | Pointer selection persists as N changes; redundancy scales with accessible fragments. |
| R2-p0.05 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 2.291 | 2.291 | Score selects the basis while the Born label remains external to F. |
| R2-p0.10 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 3.752 | 3.752 | Score selects the basis while the Born label remains external to F. |
| R2-p0.30 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Score selects the basis while the Born label remains external to F. |
| R2-p0.50 | pass | 0.000000 | 0.000000 | 2.000 | 0.000 | 8.000 | 8.000 | Score selects the basis while the Born label remains external to F. |
| R2-p0.70 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Score selects the basis while the Born label remains external to F. |
| R2-p0.90 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 3.752 | 3.752 | Score selects the basis while the Born label remains external to F. |
| R2-p0.95 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 2.291 | 2.291 | Score selects the basis while the Born label remains external to F. |
| R3-eta0.00 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Noise degrades redundancy; at eta=0.5 record objectivity is absent even if the coupling basis term remains. |
| R3-eta0.10 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 3.647 | 3.647 | Noise degrades redundancy; at eta=0.5 record objectivity is absent even if the coupling basis term remains. |
| R3-eta0.25 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 1.277 | 1.277 | Noise degrades redundancy; at eta=0.5 record objectivity is absent even if the coupling basis term remains. |
| R3-eta0.49 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 0.002 | 0.002 | Noise degrades redundancy; at eta=0.5 record objectivity is absent even if the coupling basis term remains. |
| R3-eta0.50 | degenerate | 0.000000 | 0.000000 | 2.000 | 0.000 | 0.000 | 0.000 | Noise degrades redundancy; at eta=0.5 record objectivity is absent even if the coupling basis term remains. |
| R4-k0 | degenerate | 0.000000 | 0.000000 | 2.000 | 0.000 | 0.000 | 0.000 | Accessible redundancy is observer-indexed; k=0 is basis-only and not an objectivity witness. |
| R4-k1 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 0.881 | 0.881 | Accessible redundancy is observer-indexed; k=0 is basis-only and not an objectivity witness. |
| R4-k2 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 1.763 | 1.763 | Accessible redundancy is observer-indexed; k=0 is basis-only and not an objectivity witness. |
| R4-k4 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 3.525 | 3.525 | Accessible redundancy is observer-indexed; k=0 is basis-only and not an objectivity witness. |
| R4-k8 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Accessible redundancy is observer-indexed; k=0 is basis-only and not an objectivity witness. |
| R5-overlap0.00 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Nonorthogonality degrades distinguishability; full overlap removes record information. |
| R5-overlap0.25 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 6.170 | 6.170 | Nonorthogonality degrades distinguishability; full overlap removes record information. |
| R5-overlap0.50 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 4.456 | 4.456 | Nonorthogonality degrades distinguishability; full overlap removes record information. |
| R5-overlap0.90 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 0.958 | 0.958 | Nonorthogonality degrades distinguishability; full overlap removes record information. |
| R5-overlap1.00 | degenerate | 0.000000 | 0.000000 | 2.000 | 0.000 | 0.000 | 0.000 | Nonorthogonality degrades distinguishability; full overlap removes record information. |
| R6-phi0.0 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | The argmax follows the monitored pointer axis, guarding against a hard-coded z-basis result. |
| R6-phi0.393 | pass | 0.392699 | 0.392699 | 3.000 | 0.000 | 7.050 | 7.050 | The argmax follows the monitored pointer axis, guarding against a hard-coded z-basis result. |
| R6-phi0.785 | pass | 0.785398 | 0.785398 | 3.000 | 0.000 | 7.050 | 7.050 | The argmax follows the monitored pointer axis, guarding against a hard-coded z-basis result. |
| R7-roots8 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Raw redundancy overcounts when fragments share provenance; audited redundancy carries the TaF/Q1A discipline. |
| R7-roots4 | absorber_owned_audited_redundancy_required | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 3.525 | Raw redundancy overcounts when fragments share provenance; audited redundancy carries the TaF/Q1A discipline. |
| R7-roots1 | absorber_owned_audited_redundancy_required | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 0.881 | Raw redundancy overcounts when fragments share provenance; audited redundancy carries the TaF/Q1A discipline. |
| R8-mixture1.00 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Agreement can be weakened or removed without turning F into a Born-weight derivation. |
| R8-mixture0.50 | pass | 0.000000 | 0.000000 | 3.000 | 0.000 | 7.050 | 7.050 | Agreement can be weakened or removed without turning F into a Born-weight derivation. |
| R8-mixture0.00 | pass | 0.000000 | 0.000000 | 2.000 | 0.000 | 7.050 | 7.050 | Agreement can be weakened or removed without turning F into a Born-weight derivation. |

## Interpretation

- R0-R2 preserve pointer-basis selection under baseline, environment-size, and branch-weight sweeps.
- R3-R5 show record objectivity degrades with noise, inaccessible fragments, and nonorthogonal record states.
- R6 shows the score follows the monitored axis, reducing the risk that the result is just a hard-coded z-basis.
- R7 confirms TaF's audited-provenance warning: raw redundancy is not objectivity when fragments share one source.
- R8 shows the agreement term is not load-bearing for Born weights.

## Boundary

RSPS remains a fixed-H null model: record-fidelity terms can select a stable basis/objectivity structure in these fixtures, while probabilities remain trace-rule data. A Temporal Issuance or GU bridge must clear the separate fixed-H and fixed-source gates before receiving source-side credit.
