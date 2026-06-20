# T66: POVM Detector Calibration Obstruction

## Purpose

T64 showed that the Stern-Gerlach access-window discriminator is threshold
sensitive when detector channels are declared as binary reliabilities. T66
replaces those declared reliabilities with calibrated two-outcome POVM response
matrices:

```text
P(readout = + | spin = +)
P(readout = + | spin = -)
```

The test asks whether this calibration is enough to make Q1 a detector-level
prediction rather than a bookkeeping predicate.

## Result

The result is mostly negative.

A calibrated POVM response is enough to compute fragment mutual information and
run the access-boundary comparison:

```text
I(S;R) = H(R) - H(R|S)
```

But the calibrated response does not determine:

- the information threshold at which a response counts as a record,
- the observer access window,
- the independence/provenance partition that decides whether an archive is a
  copied log or an independent detector record.

## Witnesses

`povm_local_lab_after_readout` is the positive control. At threshold `0.75`,
three independent local detector fragments are above threshold and accessible:

```text
D1 = (3, 3, 1, 1)
```

`same_povm_high_threshold` uses the same calibrated response matrices at the
same observer time but raises the information threshold to `0.9`. The verdict
flips: only two fragments remain above threshold, so the record is not
finalized.

`archive_copy_partition` and `archive_independent_partition` use the same POVM
response data and same access window. The only difference is the provenance
partition. Treating the archive as a copy of the local log gives independent
redundancy `2` and no D1 finality. Treating it as an independent archive gives
independent redundancy `3` and D1 finality.

The no-signalling guardrail still passes: remote setting changes alter joint
correlations but not the local POVM readout marginal.

## Current Strongest Claim

TaF can express an observer-access and provenance-sensitive predicate over
calibrated detector records. It still does not produce a calibration-free
Stern-Gerlach prediction from POVM data alone.

## Falsification Criterion

Q1 loses independent measurement content if either condition holds:

1. Detector physics cannot non-arbitrarily fix the information threshold and
   provenance/independence partition before D1 is evaluated.
2. Once those rules are fixed, D1 always equals standard fragment redundancy
   `R_delta`.

## Reproduction

```bash
python -m unittest tests.test_povm_detector_calibration_obstruction -v
python -m models.run_t66
```
