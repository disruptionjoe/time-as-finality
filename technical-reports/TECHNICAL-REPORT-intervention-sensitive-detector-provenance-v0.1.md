# Technical Report: Intervention-Sensitive Detector Provenance v0.1

## Claim Under Test

T67 refuted the easy repair to T66: passive detector correlation does not
recover D1 provenance classes. T68 tests the next, stronger repair:
intervention-sensitive detector observables may recover the independence
partition before D1 finality is evaluated.

The question is not whether calibrated outcome statistics are enough. They are
not. The question is whether records that carry causal/provenance metadata can
make the D1 independence partition operational rather than externally supplied.

## Model

T68 starts from the T67 hostile pair:

- copied archive
- independent overlapping readout

Both witnesses have identical passive statistics:

```text
agreement = 0.92
phi       = 0.84
```

The added observables are intervention-sensitive:

- delayed-copy timing plus signed ancestry;
- write-once origin tags;
- active perturbation response;
- signed provenance DAG ancestry, ignoring only the allowed common source
  `latent_spin`.

## Pre-Registered Partition Rule

Before D1 scoring, assign two records to the same independence class if any
of the following are true:

1. perturbing one record changes the other;
2. the records share a write-once origin tag;
3. the signed provenance DAG shows shared ancestry outside allowed common
   sources;
4. timing plus ancestry shows delayed copying.

Otherwise assign distinct independence classes.

The rule is stated before D1 evaluation and does not inspect the desired D1
verdict.

## Result

T68 is a conditional success.

The copied archive and independent readout remain indistinguishable by passive
statistics, but separate under intervention-sensitive provenance data.

### Copied Archive

The copied archive has:

- duplicate origin tag;
- delayed-copy timing plus ancestry;
- perturbation coupling;
- disallowed shared ancestry beyond `latent_spin`.

The rule assigns:

```text
local_log -> P0
archive   -> P0
```

D1 is then computed as:

```text
D1 = (2, 1, 1, 0)
observer_finalized = false
```

### Independent Readout

The independent readout has:

- distinct origin tags;
- no delayed-copy ancestry;
- no perturbation coupling;
- no shared ancestry except `latent_spin`.

The rule assigns:

```text
local_log -> P0
archive   -> P1
```

D1 is then computed as:

```text
D1 = (2, 2, 1, 1)
observer_finalized = true
```

## Current Strongest Claim

In the finite detector witness family, D1 independence classes can be
operationally fixed before finality scoring when detector records carry
intervention-sensitive provenance data: origin tags, perturbation response,
and signed ancestry.

## What This Improved

T68 rescues a narrow detector-level contribution for Q1. The project can now
say something sharper than "declare provenance classes": give detector records
causal/provenance metadata, pre-register a partition rule, and compute D1 only
after that rule runs.

This makes the detector branch more testable. A future physical detector
protocol can attack clock uncertainty, tag failures, perturbation back-action,
and provenance-DAG reliability directly.

## What This Weakened

T68 also weakens Q1 in an important way. TaF's detector-level content is not
calibration-free and is not recoverable from calibrated outcome statistics or
passive correlations. It becomes operational only for detector records with
causal/provenance metadata.

This is a real limitation. Without such metadata, Q1 still reduces to
post-hoc bookkeeping over record fragments.

## Falsification Criterion

T68 fails if copied and independent detector chains can be made identical
under:

- passive statistics;
- timing;
- origin tags;
- active perturbation response;
- signed ancestry;

while still requiring opposite D1 independence partitions.

T68 also fails as a physics-facing repair if real detector protocols cannot
provide the required metadata without arbitrary labels, unphysical
interventions, or outcome-dependent tuning.

## Answer To The Final Question

Yes, in this finite model. TaF's detector-level contribution becomes
operational only when detector records carry causal/provenance metadata, not
merely calibrated outcome statistics.

The result should be read as conditional support, not a finished detector
theory.

## Next Work

Replace the ideal provenance metadata with a physically modeled detector
protocol:

- finite clock uncertainty;
- tag creation and tag failure modes;
- perturbation back-action limits;
- forged or duplicated provenance signatures;
- realistic archive latency.

The next hostile test should ask whether the T68 rule survives those failure
modes without becoming another threshold-tuned rule.

## Reproduction

```bash
python -m unittest tests.test_intervention_sensitive_detector_provenance -v
python -m models.run_t68
```
