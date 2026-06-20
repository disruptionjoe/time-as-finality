# T67: POVM Correlation Provenance Obstruction

## Question

Can the detector independence partition in T66 be recovered from measured
channel-correlation data alone, without separately declared provenance labels?

## Why This Matters

T66 showed that Q1 still depends on a provenance / independence partition.
One natural repair is to infer that partition from measured detector
correlations. If that inference fails even in a finite hostile witness family,
the detector route remains underdetermined.

## Minimal Model

Use two observed detector records:

- `local_log`
- `archive`

Compare two provenance mechanisms:

1. `dependent_copy`
   `archive` is a downstream copy of `local_log`, possibly degraded by
   transport noise.
2. `independent_readout`
   `local_log` and `archive` are distinct detector chains measuring the same
   latent spin variable with independent local noise.

For each scenario compute:

- pairwise agreement `P(local_log = archive)`
- binary phi correlation `phi = 2 * agreement - 1`
- local and archive accuracies

## Hypotheses

- `H1`: a threshold on pairwise agreement can recover provenance class.
- `H2`: a threshold on phi correlation can recover provenance class.
- `H3`: correlation can rank record similarity but cannot recover provenance
  dependence on its own.
- `H4`: intervention or signed provenance metadata are needed to fix the
  independence partition before D1 evaluation.

## Pass / Fail Criteria

- `H1` is refuted if there exists a copied-archive witness and an independent
  witness with identical agreement but opposite provenance class.
- `H2` is refuted if the same happens for phi correlation.
- `H3` is supported if the best scalar-threshold classifier still
  misclassifies at least one hostile witness.
- `H4` is supported if the obstruction persists after explicit finite
  calibration of the detector channels.

## Current Result

- `H1`: refuted.
- `H2`: refuted.
- `H3`: supported.
- `H4`: supported.

Exact overlap witness:

- `dependent_transport_noisy` has agreement `0.92`, phi `0.84`.
- `independent_exact_overlap` has agreement `0.92`, phi `0.84`.
- Their provenance classes are opposite.

Therefore passive pairwise detector correlation does not determine D1
independence class in the finite witness family.

## Artifacts

- Model: `models/povm_correlation_provenance_obstruction.py`
- Test: `tests/test_povm_correlation_provenance_obstruction.py`
- Results: `results/povm-correlation-provenance-obstruction-v0.1.json`
- Result note: `results/povm-correlation-provenance-obstruction-v0.1-results.md`
