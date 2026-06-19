---
document_type: registry
primary_reader: governance
read_pattern: current_state
write_pattern: edit_in_place
authority: canonical
summarizable: false
---

# Research-Line Scorecard

A **portfolio health signal** that governance workflows use when evaluating
research lines. This is **not** a correctness score, and it deliberately does
**not** collapse to a single number. It gives Governance a structured way to
reason about each line's health, maturity, and resource claim.

> **Evolving artifact.** Dimensions and scales below are a starting point and are
> expected to change. It is the **health substrate** that `govern/line-review`
> reads to compute a line's separate, non-canonical standing snapshot (it is not
> itself that snapshot). Distinct from the
> per-persona `templates/scorecard.template.md` (which captures one persona's read
> of one line). This registry holds the *aggregate, per-line* portfolio view.

## Dimensions

| dimension | what it signals |
|---|---|
| Cross-cluster support | breadth of support across *distant* persona clusters |
| Mathematical readiness | how close to rigorous formalization |
| Empirical readiness | how close to executable tests / witnesses |
| Novelty | how new relative to the existing repo |
| Information gain | how much it has changed understanding (incl. via failure) |
| Dependency centrality | how many other lines depend on / are supported by it |
| Overclaim risk | risk of asserting beyond evidence |
| Current trajectory | ↑ improving · → steady · ↓ declining |
| Confidence trend | ↑ rising · → flat · ↓ falling |

Scales: qualitative `low / med / high` for level dimensions; `↑ / → / ↓` for
trajectory and confidence trend. (A finer scale can be adopted later if needed.)

## Current snapshot (provisional — first `line-review` will set real values)

| line | x-cluster | math-ready | emp-ready | novelty | info-gain | dep-centrality | overclaim-risk | trajectory | conf-trend |
|---|---|---|---|---|---|---|---|---|---|
| RL-001 Finite finality descent | high | high | med | high | high | high | med | ↑ | ↑ |
| RL-002 PO1 schema | high | high | med | high | high | high | med | → | → |
| RL-003 Consensus crosswalk | med | med | med | med | med | med | med | → | → |
| RL-004 Typed transport category | med | high | med | med | med | high | low | → | → |
| RL-005 Local persistence | med | med | high | med | med | low | med | ↑ | → |
| RL-006 Compression crosswalk (archived) | low | high | high | med | high | low | low | ↓ | → |

> Values are an initial qualitative read for scaffolding only. They are not the
> output of a scoring run and should not be cited as such until `line-review`
> populates them from persona scorecards and cross-cluster aggregation.

## How this registry is used

`govern/line-review` writes the snapshot from aggregated persona scorecards;
`govern/lifecycle-review` reads it (with the line registry's relationships and the
information portfolio) when applying promotion/demotion and resource allocation.
No dimension is summed into a single rank — Governance reasons over the profile.
