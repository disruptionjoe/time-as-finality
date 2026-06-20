# T79 Results: Dashboard Summary Nonidentifiability

Strongest claim: Coarse deployment dashboards are non-identifying for the detector branch: two completions with the same timing, retention, signature-pass, and threshold-coverage summary can still yield opposite T76-style provenance verdicts.

Weakened claim: T79 weakens the detector branch by ruling out a common shortcut: strong timing, high tag retention, and high signature-pass rates do not by themselves support Q1. Opposite provenance verdicts can hide beneath the same coarse deployment dashboard.

Dashboard projections identical: `True`

## Completion audits

| Completion | Verdict | Robust rate | False independence rate | Withhold rate |
| --- | --- | --- | --- | --- |
| measured_signed_time_tag_stack | robust_measured_recovery | 1.0 | 0.0 | 0.0 |
| dashboard_matched_spoofable_completion | measured_conservative_withhold | 0.0 | 0.0 | 1.0 |

## Shared dashboard summary

- `local_sigma`: [0.003, 0.002]
- `archive_sigma`: [0.025, 0.015]
- `batching_window`: [0.09, 0.04]
- `tag_retention`: [9975, 10000]
- `signature_verification`: [9990, 10000]
- `threshold_coverage`: [20, 20]

## Falsification condition

T79 fails if one can project deployment evidence to a coarse dashboard that omits raw ancestry, replay, spoof, perturbation, and trust-boundary logs while still uniquely determining the T76/T77 verdict for all completions compatible with that summary.

## Q1 update

Keep Q1 partially supported only for event-level raw-log provenance audits. Dashboard summaries are insufficient because they do not identify spoof, trust-boundary, perturbation, or DAG structure.

## Blocker

No real event-level deployment log is present; T79 only proves that dashboard-level evidence cannot close that gap.

## Next move

Demand one real event-level detector log with ancestry, replay, spoof, perturbation, and trust-boundary evidence, then run the locked T76/T77/T78/T79 audit without replacing it by a dashboard summary.
