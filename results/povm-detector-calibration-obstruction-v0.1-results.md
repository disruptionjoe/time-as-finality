# T66 Results: POVM Detector Calibration Obstruction

## Strongest Claim

A calibrated binary POVM response lets TaF compute detector fragment information and re-run the access-window discriminator, but it does not determine finality without independent threshold and provenance assumptions.

## Weakened Claim

Q1 cannot claim a calibration-free Stern-Gerlach prediction from POVM data alone.  The same calibrated response can support different D1 verdicts under different threshold or independence rules.

## Scenario Matrix

| Scenario | t | threshold | Total R_delta | Accessible raw | Independent | D1 profile | Classification |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| povm_local_lab_after_readout | 2.5 | 0.75 | 3 | 3 | 3 | (3, 3, 1, 1) | povm_record_finalized |
| same_povm_high_threshold | 2.5 | 0.9 | 2 | 2 | 2 | (2, 2, 1, 0) | povm_below_redundancy_threshold |
| povm_redundant_but_inaccessible | 2.5 | 0.75 | 3 | 0 | 0 | (0, 0, 0, 0) | povm_redundant_but_inaccessible |
| archive_copy_partition | 4.5 | 0.75 | 3 | 3 | 2 | (3, 2, 1, 0) | povm_independence_obstruction |
| archive_independent_partition | 4.5 | 0.75 | 3 | 3 | 3 | (3, 3, 1, 1) | povm_record_finalized |

## Threshold Obstruction

| Low threshold | High threshold | Same POVM response | Low finalized | High finalized | Verdict flips |
| ---: | ---: | --- | --- | --- | --- |
| 0.75 | 0.9 | True | True | False | True |

POVM calibration supplies response probabilities, but does not select the information threshold that turns response into finality.

## Independence Obstruction

| Same POVM response | Same access window | Copy partition finalized | Independent partition finalized | Verdict flips |
| --- | --- | --- | --- | --- |
| True | True | False | True | True |

The archive copy and independent archive have identical calibrated response data.  The D1 verdict changes only because the provenance partition changes.

## No-Signalling Audit

| Local setting | Fragment | Local readout marginals by remote setting | Max delta | Passed |
| --- | --- | --- | ---: | --- |
| local_z | screen_spot | remote_z: 0.505, remote_x: 0.505, remote_diag: 0.505 | 0.0 | True |
| local_x | screen_spot | remote_z: 0.505, remote_x: 0.505, remote_diag: 0.505 | 0.0 | True |

## Hypothesis Results

### H1: supported

Declared scalar reliabilities can be replaced by explicit binary POVM response matrices for this detector proxy.

Evidence: Fragment information is computed from P(readout=+|spin=+) and P(readout=+|spin=-), not assigned as a reliability.

### H2: weakened

A calibrated POVM response does not by itself determine observer-relative D1 finality.

Evidence: The archive-copy and archive-independent scenarios have the same response data and access window but opposite D1 finalization verdicts.

### H3: weakened

The information threshold remains an external input unless a physical calibration rule fixes it before evaluation.

Evidence: The same local detector response finalizes at threshold 0.75 and does not finalize at threshold 0.9.

### H4: supported_guardrail

The calibrated-response predicate preserves no-signalling in the finite singlet audit.

Evidence: All local POVM readout marginals are invariant under the tested remote settings.

### H5: open

Q1 needs a detector provenance rule and threshold rule that are specified before the D1 predicate is evaluated.

Evidence: Without those rules, D1 can be changed while leaving the calibrated POVM response matrices unchanged.

## Falsification Condition

If detector physics cannot non-arbitrarily fix the information threshold and provenance/independence partition before D1 is evaluated, Q1 reduces to post hoc bookkeeping.  If those rules are fixed and D1 always equals standard R_delta, Q1 adds no independent measurement content.

## Recommended Next

Derive the independence partition from a detector provenance graph or measured channel-correlation matrix, then pre-register the information threshold before comparing D1 with standard R_delta.
