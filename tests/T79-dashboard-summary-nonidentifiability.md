# T79: Dashboard Summary Nonidentifiability

## Question

Can a coarse detector-deployment dashboard stand in for the T78 raw-log
contract, or do opposite detector-provenance verdicts remain compatible with
the same dashboard summary?

## Motivation

T76 made detector provenance measurable, T77 exposed policy sensitivity, and
T78 required real raw logs before a detector run can count as evidence. T79
tests whether that raw-log requirement is only procedural or genuinely
load-bearing.

## Construction

Project deployment evidence to a dashboard that includes only:

- timing estimates and uncertainties;
- tag-retention rate;
- signature-verification pass rate;
- threshold-coverage count.

Then construct two completions compatible with the same dashboard:

- a signed raw-log completion with strong spoof resistance, trust boundaries,
  perturbation behavior, and ancestry DAG observability;
- a spoofable completion with the same dashboard-visible summary but degraded
  hidden provenance fields.

## Success Criteria

- The dashboard projections are exactly identical.
- The signed completion remains robust under the T76 baseline policy.
- The spoofable completion fails with false-independence risk or conservative
  withhold.

## Failure Criteria

- The dashboard projection differs between the two completions.
- The two completions produce the same T76-style verdict.
- A coarse dashboard uniquely determines the detector-provenance verdict.

## Claim Impact

If T79 passes, Q1 remains `partially_supported` only as an event-level raw-log
provenance claim. Timing, retention, and signature-pass dashboards cannot
upgrade the detector branch because opposite provenance verdicts can hide under
the same summary.

If T79 fails, the T78 raw-log gate would need to be weakened or re-argued.

## Reproduction

```bash
python -m unittest tests.test_dashboard_summary_nonidentifiability -v
python -m models.run_t79
```
