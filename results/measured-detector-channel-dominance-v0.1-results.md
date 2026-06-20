# T85 Results: Measured Detector Channel Dominance

Strongest claim: The current measured detector route is narrower than the T76 schema suggests. After trust-boundary and pre-registration gates are fixed, spoof/unique-tag evidence can still independently demote the signed fixture, but perturbation and DAG evidence do not become decisive on their own inside the present witness family.

Weakened claim: This weakens any reading of the detector branch that treats perturbation response or DAG observability as already independent decision channels in the executable audit. At present they are auxiliary to authenticated-tag evidence rather than peer load-bearing axes.

## Baseline

- Verdict: `robust_measured_recovery`
- Robust rate: `1.0`

## Hostile single-category families

| Category | Verdict | Independently decisive | Robust rate | Withhold rate | False-independence rate | False-dependence rate |
| --- | --- | --- | --- | --- | --- | --- |
| spoof_resistance | measured_conservative_withhold | True | 0.455 | 0.545 | 0.0 | 0.0 |
| perturbation | robust_measured_recovery | False | 1.0 | 0.0 | 0.0 | 0.0 |
| dag_observability | robust_measured_recovery | False | 1.0 | 0.0 | 0.0 | 0.0 |

## Falsification condition

T85 fails if a single-category perturbation or DAG stress family, with trust and pre-registration fixed at the signed values, changes the signed fixture's verdict on its own, or if the spoof/unique-tag stress stops changing the verdict.

## Q1 update

Keep Q1 partially supported only as a narrow detector-record admissibility audit. The current executable content is best read as pre-registration gate + trust-boundary gate + authenticated-tag sufficiency, with perturbation and DAG channels not yet independently earned.

## Blocker

The current witness family leaves authenticated tag channels already strong enough to settle provenance in cases where perturbation and DAG evidence degrade. That prevents those channels from being independently decisive.

## Next move

Construct a hostile raw-log family in which authenticated tags are intentionally ambiguous but perturbation response or signed ancestry still separates copied from independent records. If that cannot be done, remove those channels from the detector branch's core schema.
