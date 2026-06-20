# T68 Results: Intervention-Sensitive Detector Provenance

Strongest claim: In the finite detector witness family, D1 independence classes can be operationally fixed before finality scoring when records carry intervention-sensitive provenance data: origin tags, perturbation response, and signed ancestry.

Weakened claim: TaF's detector-level content is not calibration-free and not recoverable from calibrated outcome statistics or passive correlations. It becomes operational only for detector records with causal/provenance metadata.

## Separation audit

- passive statistics identical: True
- intervention partitions distinct: True
- D1 computed after partition: True
- success: True
- interpretation: The passive observables are intentionally identical; the intervention/provenance observables determine different independence partitions before D1 scoring.

## Scenario verdicts

### dependent_copied_archive_same_passive_stats

- passive agreement: 0.92; phi: 0.84
- inferred same independence class: True
- inferred classes: [('local_log', 'P0'), ('archive', 'P0')]
- D1 profile: [2, 1, 1, 0]
- observer finalized: False

### independent_readout_same_passive_stats

- passive agreement: 0.92; phi: 0.84
- inferred same independence class: False
- inferred classes: [('local_log', 'P0'), ('archive', 'P1')]
- D1 profile: [2, 2, 1, 1]
- observer finalized: True

## Next move

Replace the finite provenance metadata with a physically modeled detector protocol: explicit clock uncertainty, tag failure modes, and intervention back-action limits.
