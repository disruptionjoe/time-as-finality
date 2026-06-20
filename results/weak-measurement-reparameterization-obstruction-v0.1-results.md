# T90 Results: Weak-Measurement Reparameterization Obstruction

## Null fixture

Verdict: `null_reparameterization`

| Time | Value |
| --- | ---: |
| `t_decohere` | 4.0 |
| `t_redundancy` | 3.0 |
| `t_access` | 3.0 |
| `t_finality` | 3.0 |

## Identical-standard-statistics pair

| Audit field | Independent branch | Post hoc branch |
| --- | --- | --- |
| `standard_timelines_equal` | True | True |
| `standard_verdict_equal` | True | True |
| `taf_verdict_changes` | True | True |
| `has_independent_source` | True | False |
| `rejected_for_post_hoc_source` | False | True |
| `verdict` | candidate_non_null_witness | null_post_hoc |

## Strongest claim

A weak-measurement finalization time is null when every D1 coordinate is fixed by coherence, redundancy, access windows, or post hoc threshold choices. It becomes only a candidate discriminator when an independent pre-registered observable changes the TaF verdict while the standard monitored-record statistics are unchanged.

## Weakened claim

The current TaF weak-measurement route does not yet predict new measurement dynamics. At most, T90 gives a required separation test for any future monitored-qubit or detector-trajectory proposal.

## Falsification condition

T90 fails if a protocol with only standard coherence/redundancy/access statistics yields a TaF verdict that cannot be expressed as a thresholded standard-statistic rule, or if a post hoc branch label is accepted as an independent observable.

## Q1 update

Keep Q1 partially supported, but state the weak-measurement branch as an obstruction result: T12 is non-null only after a pre-registered branch, provenance, or reversal-cost observable produces a verdict change between trajectories with identical standard monitored-record statistics.

## Blocker

No concrete platform currently supplies a pre-registered branch-live or reversal-cost observable that is independent of coherence decay, fragment redundancy, and access thresholds.

## Recommended next

Instantiate the independent-axis test on a superconducting-qubit homodyne trajectory or a trapped-ion/cavity-QED undo protocol; if no independent axis can be named before data analysis, demote T12.
