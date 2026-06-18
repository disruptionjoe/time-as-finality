# TS-PERSONA-SPRINT-001: Aisha Rahman Lens (Physics-Informed ML)

**Exploration status:** Heterodox sketch; not promoted to core D1 claims.
**Sprint:** TS-PERSONA-SPRINT-001
**Synthesis:** See `explorations/TS-PERSONA-SPRINT-001-synthesis-v0.1.md`

---

## Lens

Physics-informed ML analysis: autoregressive prediction accuracy, run-length
compression, Shannon entropy. Key question: is the holonic trajectory more
predictable or more compressible than the micro trajectory?

---

## Canonical Trajectory Results

| Metric                     | Micro  | Meso   | Holonic |
|----------------------------|--------|--------|---------|
| AR(1) accuracy             | 0.959  | 0.959  | 0.959   |
| Run-length compression     | 0.060  | 0.060  | 0.060   |
| Shannon entropy (bits)     | 0.881  | 0.881  | 1.000   |

**Finding:** Holonic AR(1) accuracy 0.959 vs micro 0.959. Holonic run-length
ratio 0.060 vs micro 0.060 (same). Holonic entropy 1.000 bits vs micro
0.881 bits (holonic is MORE entropic).

---

## Critical Observation

The code's "holonic is more predictable" finding uses a >= comparison: if
holonic AR(1) >= micro AR(1), holonic wins. A tie counts as a holonic win.
In the canonical case, both are 0.959 -- this is a tie, not a holonic advantage.

Run-length compression is also identical (0.060 = 3 runs / 50 steps for
both micro and holonic: each has one obstructed run and two satisfiable runs).

Shannon entropy is higher for holonic (1.000 bits) than for micro (0.881 bits).
A 50%-obstructed binary series maximizes binary entropy; holonic being
obstructed 50% of the time makes it the LEAST predictable level by entropy.

**The "more predictable" and "more compressible" findings are weak: the metric
values are identical. The entropy finding points in the opposite direction.**

---

## Cross-Variant Results

| Variant      | Micro AR1 | Holonic AR1 | Micro H  | Holonic H |
|--------------|-----------|-------------|----------|-----------|
| canonical    | 0.959     | 0.959       | 0.881    | 1.000     |
| early_stress | 0.959     | 0.959       | 0.881    | 1.000     |
| late_stress  | 0.959     | 0.959       | 0.881    | 1.000     |
| large_gap    | 0.959     | 0.959       | 0.881    | 0.971     |
| zero_gap     | 0.959     | 0.959       | 0.881    | 0.971     |

AR(1) accuracy is 0.959 across all variants and levels. The only
meaningful variation is in Shannon entropy, where holonic entropy is
consistently higher than micro entropy.

---

## Interpretation

The uniform AR(1) accuracy (0.959) across all levels reflects that the
binary constraint series has exactly 2 transitions in 50 steps for most
variants. A series with 2 transitions in 50 steps achieves (50-2)/49 =
0.959 AR(1) accuracy regardless of which level it belongs to.

This means AR(1) accuracy is not distinguishing micro from holonic at all.
It is measuring the number of transitions divided by the series length, which
is the same for all three levels in the canonical case.

Shannon entropy is discriminative but points against the holonic stability
hypothesis: the level with higher obstruction fraction has higher entropy.

---

## Verdict for This Lens

This lens does not support the hypothesis that holonic trajectories are more
predictable or more stable. The predictability tie (AR1 = 0.959 for all
levels) and the entropy reversal (holonic entropy > micro entropy) suggest
that if anything, the holonic level is slightly less information-efficient,
though the effect is modest.

No new mathematical object is required. The metrics are derivable from the
constraint schedule statistics.
