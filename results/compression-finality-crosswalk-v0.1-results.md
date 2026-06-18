# T36: Compression-Finality Crosswalk — v0.1 Results

## Verdict

**Divergence confirmed. Compressibility is a downstream observable of stable
record structure, not a constituent of finality.**

The strongest hypothesis (finality = compressibility) is falsified by two
classes of counterexample. The weaker and more defensible relationship is:

```
restriction system
    → projection
    → stable records
    → predictive structure
    → compression opportunities
```

## Key Counterexamples

| Rule | Survival | Compressibility | What this shows |
| --- | --- | --- | --- |
| Rule 30 | 1.000 | 0.065 | Durable records do NOT imply compressibility |
| Rule 0 | 0.000 | 1.000 | Compressibility does NOT imply durable records |

**Rule 30** (chaotic, high survival, 30/32 unique trace patterns): every
intervention leaves a trace, but the trace patterns are highly diverse and
unpredictable. Compressibility is near minimum (0.065). High finality does not
imply high compressibility.

**Rule 0** (all-zeros attractor, no surviving records): every state collapses
to all-zeros after a few steps. No intervention leaves any trace. The "trace
distribution" is degenerate — only one pattern (all-zeros) is ever observed.
This gives trivially perfect compressibility (1.000). Zero finality does not
imply low compressibility; it implies trivial compressibility.

These counterexamples show the two quantities measure different things.

## Divergence Witnesses

| Witness type | Rules | Shared value | Compression gap |
| --- | --- | --- | --- |
| Same survival, different compression | 15 & 166 | survival ≈ 1.000 | 0.496 (0.536 vs 0.040) |
| Same loss, different compression | 2 & 8 | lost_bits ≈ 2.594 | 0.597 (0.403 vs 1.000) |

These witnesses confirm that compressibility is not a function of either D1
finality (trace_survival) or thermodynamic information loss (lost_bits) alone.

## Correlation Structure

| Relationship | Pearson r | Interpretation |
| --- | --- | --- |
| Compression vs. survival | −0.745 | Correlated but not identical; high survival tends toward more diverse traces |
| Compression vs. lost_bits | +0.631 | Correlated but not identical; higher loss collapses trace variety |

Both correlations are substantial but well below ±1.0. This is informative:
compressibility and finality both appear to reflect latent structure of the
restriction system, but neither is reducible to the other. They are
co-varying observables, not synonyms.

## Notable Rule Profiles

| Rule | Injective | Lost bits | Survival | Compressibility | Unique patterns |
| --- | --- | --- | --- | --- | --- |
| 0 | No | 5.000 | 0.000 | 1.000 | 1 |
| 1 | No | 2.882 | 0.500 | 0.438 | 16 |
| 30 | No | 0.375 | 1.000 | 0.065 | 30 |
| 90 | No | 1.000 | 1.000 | 0.536 | 5 |
| 110 | No | 0.738 | 1.000 | 0.393 | 21 |
| 128 | No | 2.882 | 0.062 | 0.933 | 2 |
| 150 | Yes | 0.000 | 1.000 | 0.536 | 5 |
| 255 | No | 5.000 | 0.000 | 1.000 | 1 |

Reversible rules (injective=True) have mean compressibility 0.336 vs 0.293 for
irreversible rules — slightly higher, but the difference is small and the
variation within each class is large.

## What This Does Not Support

- Compressibility as a new D1 dimension. The current evidence does not justify
  adding compressibility to the D1 profile. It is a derived observable, not an
  independent finality axis.
- The identity finality = compressibility. Rule 30 and Rule 0 refute this.
- Compressibility as a proxy for information loss. Same-loss pairs with
  different compressibility (Rules 2 and 8) refute this.

## Test Suite

37 tests, 37 passed (with 1280 subtests across 256-rule bounds checks).

```
python -m pytest tests/test_compression_finality_lab.py -v
```

## Reproducible Run

```
python -m models.run_t36
```

Output: `results/compression-finality-crosswalk-v0.1.json`
