# Technical Report: POVM Correlation Provenance Obstruction v0.1

## Claim Under Test

T66 left a repair path open: perhaps the detector independence partition could
be derived from measured channel-correlation data instead of being declared by
hand. T67 tests that repair in the smallest hostile finite family.

The target is narrow. This report does not claim new quantum dynamics, a new
measurement law, or a detector simulation. It only tests whether passive
correlation statistics can decide whether two detector records should count as
the same D1 provenance class.

## Model

There are two observed records:

- `local_log`
- `archive`

and two provenance mechanisms.

### 1. Dependent copy

`archive` is a downstream copy of `local_log`, with optional transport noise:

```text
latent spin -> local_log -> archive
```

Observed agreement is controlled by copy fidelity.

### 2. Independent readout

`local_log` and `archive` are distinct detector chains that both measure the
same latent spin with independent local noise:

```text
            -> local_log
latent spin
            -> archive
```

Observed agreement is controlled by shared-cause alignment, not by copying.

T67 evaluates pairwise agreement and binary phi correlation:

```text
agreement = P(local_log = archive)
phi = 2 * agreement - 1
```

These are exactly the kind of passive channel-correlation observables that a
"recover provenance from data" repair would start from.

## Results

The main result is negative.

`dependent_transport_noisy` and `independent_exact_overlap` have opposite
provenance classes but identical observed pair statistics:

- agreement `= 0.92`
- phi correlation `= 0.84`

Therefore neither agreement nor phi can determine provenance class by
thresholding.

The broader witness family shows the same problem in order-theoretic form:
correlation scores for copied and independent channels overlap. A copied
archive can have *lower* agreement than an independent high-fidelity readout
pair, because copy transport noise and shared-cause accuracy are different
mechanisms.

Threshold search confirms the obstruction. The best scalar threshold over the
canonical witness family still misclassifies two of six scenarios.

## Current Strongest Claim

Pairwise detector correlation can audit similarity of records, but it cannot
by itself determine whether two records belong to the same D1 independence
class.

## What This Improved

T67 sharpens the T66 weakness. The phrase "derive provenance from measured
channel-correlation matrix" is now too optimistic unless extra observables are
added. The problem is not only that provenance was undeclared; it is that
passive similarity statistics do not encode the causal distinction between
copy-descendance and separate readout.

This improves falsifiability. Q1 now carries a clearer burden:

1. specify extra provenance observables before D1 evaluation, or
2. concede that the detector-level independence partition remains post hoc.

## What This Weakened

T67 weakens the detector route under Q1. It rejects the easy repair in which
one infers provenance from passive pairwise detector correlation alone.

It also blocks a common shortcut in the Quantum-Darwinism comparison.
Redundancy-style agreement between fragments is not enough to show that the
fragments are independent record holders rather than descendants of one record
chain.

## Falsification Criterion

T67 is false if a pre-registered provenance-inference rule based only on
passive detector correlation statistics classifies copied versus independent
channels correctly across hostile witness families.

If no such rule survives hostile cases, then Q1 still lacks an operational
detector-side rule for its independence partition.

## Next Work

The next repair must add observables that are sensitive to causal provenance,
not just informational similarity. Candidate additions:

- delayed-copy intervention tests
- write-once or transmission-stage tags
- signed provenance graphs
- causal timing asymmetries between local record and archive appearance

The right next test is whether those additional observables determine the
independence partition before D1 is evaluated.

## Reproduction

```bash
python -m unittest tests.test_povm_correlation_provenance_obstruction -v
python -m models.run_t67
```
