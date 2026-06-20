# T71: Consensus Parametric Tradeoff

## Question

For bounded consensus-finality models, under what resource, delay, and finite-cap
parameters does the T17 D1/progress tradeoff hold?

## Motivation

T17 established a finite witness:

```text
budget = 10
adversarial_delay = 2
```

has no admissible configuration that jointly maximizes:

```text
accessible support
holder redundancy
branch support
reversal cost
bounded progress
```

A follow-up scout showed that this is not parameter-free. Degenerate low-budget
settings and saturated high-budget / relaxed-delay settings can admit joint
maximizers. T71 turns that scout into a parameter classification.

## Named parameter surface

The T17 finite caps are exposed as first-class parameters:

```text
max_nodes = 6
max_branches = 4
max_confirmations = 4
max_timeout = 4
budget = 4..32
adversarial_delay = 1..8
canonical point = (budget=10, adversarial_delay=2)
```

The model keeps the T17 evaluation semantics:

```text
resource_cost = nodes + branches + confirmations + timeout
accessible_support = min(quorum, timeout-reachable nodes)
holder_redundancy = accessible_support
branch_support = min(branches, accessible_support)
reversal_cost = accessible_support * confirmations
bounded_progress = quorum reachable within adversarial_delay
```

## Regimes

T71 classifies each parameter point into:

| Regime | Meaning |
| --- | --- |
| `degenerate` | a joint maximizer exists because the space is too small to express independent objectives |
| `scarcity` | no joint maximizer exists because resources force a real D1/progress tradeoff |
| `canonical_tradeoff` | the original T17 point, `budget=10`, `delay=2` |
| `saturated` | a joint maximizer exists because all finite caps are reachable while progress also holds |
| `collapse_no_tradeoff` | a joint maximizer exists outside the known degenerate or saturated explanations |

## Success criteria

T71 succeeds if:

1. finite caps are explicit;
2. the canonical T17 point remains a preserved tradeoff;
3. at least one scarcity region is found;
4. at least one degenerate failure is found;
5. at least one saturated failure is found;
6. minimal failure witnesses are reported;
7. the recommendation does not promote RL-003 or change claim status.

## Current result

T71 succeeds on the T17 cap surface.

The widened grid produces:

```text
degenerate = 16
scarcity = 130
canonical_tradeoff = 1
saturated = 85
collapse_no_tradeoff = 0
```

Minimal preserved point:

```text
budget = 6
adversarial_delay = 1
```

Canonical preserved point:

```text
budget = 10
adversarial_delay = 2
objective maxima = (4, 4, 3, 9, 1)
```

Minimal degenerate failure:

```text
budget = 4
adversarial_delay = 1
joint maximizer = n1-q1-b1-c1-t1
objective maxima = (1, 1, 1, 1, 1)
```

Minimal saturated failure:

```text
budget = 16
adversarial_delay = 4
joint maximizer = n4-q4-b4-c4-t4
objective maxima = (4, 4, 4, 16, 1)
```

No `collapse_no_tradeoff` point appears on this grid.

## Recommendation

Keep RL-003 active but do not promote it yet. T17 should be upgraded from a
single finite witness to a bounded theorem only with explicit parameter
conditions:

```text
exclude degenerate low-budget points
exclude saturated finite-cap points
state the verified scarcity window
```

The next step is to replace the grid classification with symbolic inequalities
for the scarcity window.

## Artifacts

- Model: `models/consensus_parametric_tradeoff.py`
- Runner: `models/run_consensus_parametric_tradeoff.py`
- Tests: `tests/test_consensus_parametric_tradeoff.py`
- Technical report: `TECHNICAL-REPORT-consensus-parametric-tradeoff-v0.1.md`
- Results JSON: `results/consensus-parametric-tradeoff-v0.1.json`
- Results note: `results/consensus-parametric-tradeoff-v0.1-results.md`
