# T68: Intervention-Sensitive Detector Provenance

## Question

Can the D1 independence partition be recovered from intervention-sensitive
detector observables rather than passive detector correlations?

## Motivation

T66 showed that calibrated POVM response matrices do not make D1 finality
calibration-free. T67 then showed that passive detector correlations do not
recover provenance classes: a copied archive and an independent readout pair
can have identical agreement and phi correlation.

T68 tests the next repair. It asks whether provenance becomes operational if
detector records carry causal metadata or can be tested under intervention.

## Witness Family

T68 uses two hostile witnesses with identical passive statistics:

- `dependent_copied_archive_same_passive_stats`
- `independent_readout_same_passive_stats`

Both have:

- agreement `0.92`
- phi correlation `0.84`

They differ only in intervention-sensitive provenance observables.

## Intervention Observables

T68 evaluates four observables before D1 scoring:

- delayed-copy evidence: `archive.created_at > local_log.created_at` plus
  `local_log` in the archive's signed ancestry;
- write-once origin tags: duplicate origin tags indicate copied provenance;
- perturbation coupling: `do(local_log := perturbed)` changes the archive only
  in the copied case;
- signed provenance DAG: shared ancestry outside the allowed common source
  `latent_spin` indicates dependence.

## Pre-Registered Rule

Before D1 scoring, place two records in the same independence class if any of
the following hold:

- active perturbation of one record changes the other;
- they share a write-once origin tag;
- a signed provenance DAG shows non-common ancestry;
- timing plus ancestry shows delayed copying.

Otherwise assign distinct independence classes. The only allowed common
ancestor in this witness family is the latent spin source.

## Success Conditions

T68 succeeds if:

- passive statistics are identical across the copied and independent witness;
- intervention-sensitive observables infer distinct provenance partitions;
- the rule is pre-registered before D1 scoring;
- the rule does not inspect or tune to the desired D1 verdict;
- D1 finality is computed only after the partition is fixed.

## Current Result

T68 succeeds conditionally.

The copied archive is assigned one independence class:

```text
local_log -> P0
archive   -> P0
D1 = (2, 1, 1, 0)
finalized = false
```

The independent readout is assigned two independence classes:

```text
local_log -> P0
archive   -> P1
D1 = (2, 2, 1, 1)
finalized = true
```

The result is not calibration-free. It depends on detector records carrying
causal/provenance metadata or supporting active interventions.

## Artifacts

- Model: `models/intervention_sensitive_detector_provenance.py`
- Runner: `models/run_t68.py`
- Test: `tests/test_intervention_sensitive_detector_provenance.py`
- Technical report: `TECHNICAL-REPORT-intervention-sensitive-detector-provenance-v0.1.md`
- Results: `results/intervention-sensitive-detector-provenance-v0.1.json`
- Result note: `results/intervention-sensitive-detector-provenance-v0.1-results.md`
