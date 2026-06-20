# T64 Results: Stern-Gerlach Detector Access-Window Discriminator

## Strongest Claim

In the T64 Stern-Gerlach toy detector, TaF adds at most an observer-access and independence-filter predicate over already formed detector records; it does not add collapse or new noisy measurement dynamics.

## Weakened Claim

Q1 is weakened because detector finality can flip under plausible information-threshold choices. Without a physically justified threshold and independence partition, the D1 verdict is bookkeeping.

## Scenario Matrix

| Scenario | t | threshold | coherence | Total R_delta | Accessible raw | Independent | D1 profile | Classification |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| local_lab_after_readout | 2.5 | 0.75 | 0.000288 | 3 | 3 | 3 | (3, 3, 1, 2) | detector_record_finalized |
| redundant_but_before_access | 2.5 | 0.75 | 0.000288 | 3 | 0 | 0 | (0, 0, 0, 0) | redundant_but_inaccessible |
| single_channel_early_window | 1.25 | 0.75 | 0.012 | 1 | 1 | 1 | (1, 1, 1, 0) | single_channel_underfinalized |
| duplicate_archive_boundary | 4.5 | 0.75 | 0.000144 | 3 | 3 | 2 | (3, 2, 1, 0) | raw_redundancy_overcounts_independence |
| high_threshold_fragility | 2.5 | 0.9 | 0.000288 | 1 | 1 | 1 | (1, 1, 1, 0) | single_channel_underfinalized |

## Threshold Sweep

| threshold | t | Total R_delta | Independent accessible | Finalized | Classification |
| ---: | ---: | ---: | ---: | --- | --- |
| 0.6 | 1.25 | 1 | 1 | False | single_channel_underfinalized |
| 0.6 | 2.5 | 3 | 3 | True | detector_record_finalized |
| 0.6 | 4.5 | 3 | 2 | True | detector_record_finalized |
| 0.75 | 1.25 | 1 | 1 | False | single_channel_underfinalized |
| 0.75 | 2.5 | 3 | 3 | True | detector_record_finalized |
| 0.75 | 4.5 | 3 | 2 | True | detector_record_finalized |
| 0.9 | 1.25 | 0 | 0 | False | unclassified_boundary |
| 0.9 | 2.5 | 1 | 1 | False | single_channel_underfinalized |
| 0.9 | 4.5 | 2 | 1 | False | raw_redundancy_overcounts_independence |

Threshold-sensitive time slices: 2

## No-Signalling Audit

| Local setting | Local readout marginals by remote setting | Max delta | Passed |
| --- | --- | ---: | --- |
| local_z | remote_z: 0.5, remote_x: 0.5, remote_diag: 0.5 | 0.0 | True |
| local_x | remote_z: 0.5, remote_x: 0.5, remote_diag: 0.5 | 0.0 | True |

## Hypothesis Results

### H1: supported

A detector-level access window can separate total detector redundancy from observer-relative D1 finality.

Evidence: redundant_but_before_access has total R_delta=3 but D1 profile (0, 0, 0, 0).

### H2: supported

Raw fragment redundancy can overcount independent detector holders.

Evidence: duplicate_archive_boundary has accessible raw R_delta=3 but independent R_delta=2.

### H3: weakened

The detector-level D1 predicate is threshold-sensitive, so Q1 does not yet produce a calibration-free prediction.

Evidence: The threshold sweep contains 2 observer-time slices whose finalized/not-finalized verdict changes across thresholds.

### H4: supported

The access-window finality rule does not create signalling in the finite entangled-pair audit.

Evidence: All local readout marginals are invariant under remote setting changes to numerical precision.

### H5: open

The access windows, thresholds, and independence partition still need derivation from real detector physics.

Evidence: T64 declares these inputs rather than deriving them from a Hamiltonian, POVM, or measured detector response curve.

## Falsification Condition

If detector physics fixes admissible access windows and independence classes such that D1 always equals standard fragment redundancy R_delta, or if those inputs cannot be physically specified at all, Q1 adds no independent measurement content.

## Recommended Next

Replace the declared binary channels with a calibrated detector model: a POVM or scattering response curve that fixes fragment reliabilities, access windows, and independence classes before the D1 predicate is evaluated.
