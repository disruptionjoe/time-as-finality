# T527 Results: Observerse Protocol-Stack Ablation

## Verdict

- Verdict: `observerse_stack_ablation_regression_harness_passes_review_only`
- Grade: `illustration_regression_only`
- Core layers each earn slot: `True`
- Governance conditional visible: `True`
- Minimum stack under near-term governance: 5
- Minimum stack when fixed rules anticipate full horizon: 4

## Ablation Rows

| row | SCS | ratio to full | predicted mode |
| --- | ---: | ---: | --- |
| `FULL STACK (all 5)` | 1.218 | 1.000 | `baseline` |
| `- issuance` | 0.000 | 0.000 | `freeze` |
| `- admissibility` | 0.000 | 0.000 | `incoherence` |
| `- sybil/finality` | 0.000 | 0.000 | `capture` |
| `- consensus` | 0.244 | 0.200 | `fragment` |
| `- governance (near-term rules)` | 0.000 | 0.000 | `ossification` |
| `- governance (full-horizon rules)` | 1.218 | 1.000 | `no_collapse_rules_anticipated_all` |

## Strongest Reading

The deterministic ablation model matches its review-only claim: each core layer collapses sustained coherent structure to at most 20% of the full stack, while governance is load-bearing only when fixed rules do not already anticipate the full novelty horizon.

## What This Improved

T527 turns the recent Observerse stack ablation into a repeatable regression harness and frozen result packet, without changing the underlying model or promoting the exploration.

## Falsification Condition

T527 fails if a core-layer removal stays above 20% of full sustained coherent structure, if the governance near-term/full-horizon contrast disappears, or if the result is used as validation rather than illustration-grade compositional accounting.

## Not Claimed

T527 does not validate Observerse, derive S1, prove the Bitcoin analogy, promote any claim, or change canon/public posture. It is only a regression harness for the deterministic illustration model.

## Boundary Checks

- Claim status changed: `False`
- Canon verdict changed: `False`
- Public posture changed: `False`
