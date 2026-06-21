# Technical Report: Compression-Finality Crosswalk (T36) — v0.1

## Summary

T36 tests whether compressibility and D1 finality (trace_survival) are the
same observable, or whether they diverge empirically on the T9 emergence
laboratory substrate. The strongest hypothesis — finality = compressibility —
is falsified. Compressibility is a downstream observable of stable record
structure, not a constituent of finality.

The correct working relationship is:

```
restriction system
    → projection
    → stable records
    → predictive structure
    → compression opportunities
```

## Model

All 256 elementary CA rules are run on the same substrate as T9 (width=5 cells,
layers=3, periodic boundary). For each rule, 160 seed-intervention traces are
computed (32 initial states × 5 seed positions). Two independent metric columns
are computed per rule:

**D1 finality column**
- `trace_survival_fraction`: fraction of 160 traces with nonzero trace_mask.
- `mean_accessible_support`: mean Hamming weight of surviving traces.

**Compression column**
- `trace_shannon_entropy`: Shannon entropy H(trace distribution) in bits, where
  the distribution is over 2^5=32 possible trace_mask patterns.
- `trace_compressibility`: 1 − entropy/log₂(32); 0=uniform, 1=deterministic.
- `zlib_ratio`: zlib-compressed / raw length for all traces concatenated.
- `unique_trace_patterns`: distinct trace_mask values observed across 160 runs.

## Key Counterexamples

Two counterexamples falsify the identity claim:

**Rule 30 — durable records do not imply compressibility.**
Rule 30 is chaotic: every intervention produces a trace (survival=1.000), but
the traces cover 30 of the 32 possible patterns (unique_patterns=30). The
trace distribution is nearly uniform. Compressibility=0.065 — near minimum.
High finality does not imply high compressibility.

**Rule 0 — compressibility does not imply durable records.**
Rule 0 maps all states to the all-zeros state. After 3 layers, every initial
state collapses to all-zeros. No intervention leaves any trace (survival=0.000).
The trace distribution is degenerate: only the all-zeros pattern appears.
Compressibility=1.000 — trivially perfect. Zero finality does not imply low
compressibility; it implies trivial compressibility (a degenerate distribution).

## Divergence Witnesses

| Witness type | Rules | Shared metric | Gap |
| --- | --- | --- | --- |
| Same survival (≈1.000), different compression | 15 & 166 | survival ≈ 1.000 | comp gap 0.496 |
| Same info loss (≈2.594 bits), different compression | 2 & 8 | lost_bits ≈ 2.594 | comp gap 0.597 |
| Same compression (≈1.000), different info loss | 0 & 32 | compressibility ≈ 1.000 | loss gap 2.516 bits |

These witnesses show that compressibility is determined by neither trace_survival
nor lost_bits alone.

## Correlation Structure

| Relationship | Pearson r |
| --- | --- |
| Compressibility vs. trace_survival | −0.745 |
| Compressibility vs. lost_bits | +0.631 |

The negative compression-survival correlation reflects a structural fact: rules
where many diverse traces survive (high survival, many patterns) have low
compressibility, while rules where few or no traces survive (low survival, few
patterns) have high compressibility. The correlation is substantial (−0.745) but
well below −1. The positive compression-loss correlation reflects the attractor
structure of high-loss rules: many-to-one maps concentrate states, reducing
trace pattern variety.

Both correlations are informative rather than damning: compressibility and
finality co-vary because both reflect the underlying structure of the restriction
system, but they are not synonyms.

## What This Result Changes

1. **Compressibility is not a D1 dimension.** The current evidence does not
   justify extending the D1 profile with a compressibility axis.

2. **The exploration note hypothesis is refined.** The strongest form
   (finality → compressibility as a monotone or near-monotone relationship) is
   falsified by Rule 30. The correct frame is:

   ```
   stable records → predictive structure → compression opportunities
   ```

   This is a conditional downstream relationship, not a definitional one.
   Compressibility is a diagnostic observable of record architecture, not a
   measure of record stability.

3. **Both Rule 30 and Rule 0 should become long-term reference cases.** They
   mark the boundaries of the compressibility-finality relationship and should
   be cited whenever the connection is discussed.

## Relation to Prior Tests

| Test | Connection |
| --- | --- |
| T9 | Same substrate; same 256-rule sweep; finality metrics reused directly |
| T5 | Thermodynamic crosswalk; lost_bits is the T9 analog of Landauer cost |
| explorations/compression-finality-crosswalk.md | Prototype stage; T36 delivers the promised experiment |

## Boundary

- Width=5 is a small lattice. Divergence witnesses should be reproduced at
  width=7 or width=9 before strong conclusions about the general relationship.
- zlib ratio is an empirical proxy for description length, not Kolmogorov
  complexity. The Shannon entropy measure is cleaner but only approximates the
  true algorithmic complexity of each rule family.
- The experiment measures the compressibility of the *trace distribution*, not
  the compressibility of individual records. These are related but not identical.

## Evidence

37 unit tests, all passing. 1280 rule-level subtest assertions.

```
python -m pytest tests/test_compression_finality_lab.py -v
# 37 passed, 1280 subtests passed in 0.90s
```

Reproducible output: `results/compression-finality-crosswalk-v0.1.json`
