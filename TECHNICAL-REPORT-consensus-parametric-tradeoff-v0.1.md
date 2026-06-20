# Technical Report: Consensus Parametric Tradeoff v0.1

## Claim Under Test

T17 established a bounded consensus-finality tradeoff at one parameter point:

```text
budget = 10
adversarial_delay = 2
```

At that point no admissible finite protocol configuration jointly maximizes all
four D1 dimensions plus bounded progress.

T71 tests whether that result is parameter-free. It is not. The result is better
stated as a scarcity-regime theorem candidate.

## Model

T71 exposes the finite caps that were implicit in T17:

```text
max_nodes = 6
max_branches = 4
max_confirmations = 4
max_timeout = 4
```

The widened grid is:

```text
budget = 4..32
adversarial_delay = 1..8
```

Each admissible configuration has:

```text
(nodes, quorum, branches, confirmations, timeout)
```

with:

```text
nodes + branches + confirmations + timeout <= budget
```

The D1/progress objective tuple is:

```text
(
  accessible_support,
  holder_redundancy,
  branch_support,
  reversal_cost,
  bounded_progress
)
```

where bounded progress remains outside D1, as in T17.

## Classification Rule

For each budget/delay point, T71 computes the component maxima and checks
whether any configuration reaches every maximum at once.

Regimes:

| Regime | Definition |
| --- | --- |
| `degenerate` | joint maximizer exists and D1 support/branch maxima are all <= 1 |
| `scarcity` | no joint maximizer exists outside the canonical point |
| `canonical_tradeoff` | no joint maximizer exists at `budget=10`, `delay=2` |
| `saturated` | joint maximizer exists because all finite caps are reachable and progress holds |
| `collapse_no_tradeoff` | joint maximizer exists but is neither degenerate nor saturated |

The final class is intentionally included as a safety bucket. No such point was
observed on the v0.1 grid.

## Results

The grid contains 232 parameter points.

Regime counts:

```text
degenerate = 16
scarcity = 130
canonical_tradeoff = 1
saturated = 85
collapse_no_tradeoff = 0
```

The canonical T17 point is preserved:

```text
budget = 10
adversarial_delay = 2
objective maxima = (4, 4, 3, 9, 1)
joint maximizers = none
```

The smallest preserved point on the grid is:

```text
budget = 6
adversarial_delay = 1
```

This is not a claim that the point is physically meaningful. It only marks the
first non-degenerate scarcity point in the finite grid.

## Minimal Failures

### Degenerate low-budget failure

```text
budget = 4
adversarial_delay = 1
joint maximizer = n1-q1-b1-c1-t1
objective maxima = (1, 1, 1, 1, 1)
```

Interpretation: the model is too small to express a real tradeoff. The result
collapses because there is only one admissible one-node configuration.

### Saturated finite-cap failure

```text
budget = 16
adversarial_delay = 4
joint maximizer = n4-q4-b4-c4-t4
objective maxima = (4, 4, 4, 16, 1)
```

Interpretation: every finite cap relevant to the D1/progress objective is
reachable while the delay bound is also loose enough for progress. The tradeoff
collapses because scarcity has been removed inside the capped model.

## Preserved Windows

On the T17 cap surface, preserved tradeoff windows are:

```text
delay = 1: budget 6..32
delay = 2: budget 6..9, budget 10 canonical, budget 11..32
delay = 3: budget 6..32
delay = 4: budget 6..15
delay = 5: budget 6..15
delay = 6: budget 6..15
delay = 7: budget 6..15
delay = 8: budget 6..15
```

The saturated boundary begins at:

```text
budget >= 16
adversarial_delay >= 4
```

for the T17 caps.

## Current Strongest Claim

In the bounded T17-style consensus model, D1/progress finality tradeoffs are
preserved in scarcity regimes but collapse in degenerate low-budget regimes and
saturated finite-cap regimes.

## What This Improves

T71 prevents the T17 result from being overquoted as parameter-free. It converts
the old statement:

```text
no admissible configuration jointly maximizes D1 dimensions and progress
```

into the safer statement:

```text
no joint maximizer exists inside declared scarcity windows of the finite
T17 cap surface
```

That is a better external-facing theorem candidate for distributed-systems
readers because the assumptions are visible.

## What This Weakens

T71 weakens any broad reading of T17 as a general impossibility theorem. The
tradeoff is not universal over all finite resource/delay settings. It fails
when the model is too small to express competing objectives and when the model
is saturated enough to satisfy all capped objectives at once.

## RL-003 Recommendation

Keep RL-003 active and theorem-bearing only in a conditional sense. Do not
promote RL-003 on this result alone.

T17 should be treated as:

```text
bounded theorem candidate with parameter conditions
```

not merely an example, because the scarcity windows are broad and stable on the
tested grid. But it should not be promoted to a canonical theorem until the grid
classification is replaced by symbolic inequalities or an accepted finite-grid
statement.

## Claim Impact

No claim status changes.

The result supports a cleaner future claim shape:

```text
D1/progress finality tradeoffs hold inside bounded scarcity regimes and collapse
under degenerate or saturated resource conditions.
```

This remains a finite consensus-crosswalk result. It does not claim that
physical systems are consensus protocols.

## Reproduction

```bash
python -m unittest tests.test_consensus_parametric_tradeoff -v
python -m models.run_consensus_parametric_tradeoff
```

Machine-readable output:

- `results/consensus-parametric-tradeoff-v0.1.json`

Human-readable result note:

- `results/consensus-parametric-tradeoff-v0.1-results.md`
