# T71 Results: Consensus Parametric Tradeoff

Strongest claim: In the bounded T17-style consensus model, D1/progress finality tradeoffs are preserved in scarcity regimes but collapse in degenerate low-budget regimes and saturated finite-cap regimes.

Weakened claim: The original T17 result should not be treated as parameter-free. It is a bounded theorem candidate only when its resource, delay, and cap conditions are stated.

## Parameter surface

- caps: nodes <= 6, branches <= 4, confirmations <= 4, timeout <= 4
- grid: budget 4..32; adversarial_delay 1..8

## Regime counts

- degenerate: 16
- scarcity: 130
- canonical_tradeoff: 1
- saturated: 85

## Canonical point

budget=10, delay=2, regime=canonical_tradeoff, holds=True, maxima=(4, 4, 3, 9, 1)

## Minimal failures

- degenerate: budget=4, delay=1, regime=degenerate, holds=False, maxima=(1, 1, 1, 1, 1)
- saturated: budget=16, delay=4, regime=saturated, holds=False, maxima=(4, 4, 4, 16, 1)
- collapse / no-tradeoff: none observed

## Preserved tradeoff windows

- delay=1: budget 6..32 (scarcity)
- delay=2: budget 6..9 (scarcity)
- delay=2: budget 10..10 (canonical_tradeoff)
- delay=2: budget 11..32 (scarcity)
- delay=3: budget 6..32 (scarcity)
- delay=4: budget 6..15 (scarcity)
- delay=5: budget 6..15 (scarcity)
- delay=6: budget 6..15 (scarcity)
- delay=7: budget 6..15 (scarcity)
- delay=8: budget 6..15 (scarcity)

## Recommendation

Upgrade T17 from a single finite witness to a bounded theorem with explicit parameter conditions: exclude degenerate low-budget points, exclude saturated finite-cap points, and state the verified scarcity window. Do not promote RL-003 until those inequalities are proved or the grid classification is accepted as the intended finite theorem.

## Next move

Derive symbolic inequalities for the scarcity window instead of relying on grid enumeration, then test whether richer protocol features shift the boundaries.
