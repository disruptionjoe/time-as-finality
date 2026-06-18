# TS-PERSONA-SPRINT-001: Lena Kowalski Lens (Multiscale Statistics)

**Exploration status:** Heterodox sketch; not promoted to core D1 claims.
**Sprint:** TS-PERSONA-SPRINT-001
**Synthesis:** See `explorations/TS-PERSONA-SPRINT-001-synthesis-v0.1.md`

---

## Lens

Multiscale statistics analysis: cross-level correlations, obstruction
fractions, entropy across scales, cointegration proxy. Key question: do
the three levels move together (cointegrated) or do they diverge? Is there
a dominant level that drives the others?

---

## Canonical Trajectory Results

| Metric                              | Micro  | Meso   | Holonic |
|-------------------------------------|--------|--------|---------|
| Obstruction fraction                | 0.30   | 0.30   | 0.50    |
| Shannon entropy (bits)              | 0.881  | 0.881  | 1.000   |
| Cross-level correlation (lag 0)     |        |        |         |
|   micro-meso                        | 0.524  |        |         |
|   micro-holonic                     |        | 0.655  |         |
|   meso-holonic                      |        |        | 0.655   |
| Dominant level (obstruction frac.)  |        |        | holonic |
| Cointegration detected              | Yes (all |r| > 0.5) |       |

**Finding:** Cointegration detected: all level pairs move together at
lag 0. Holonic has highest obstruction fraction (0.50) and highest entropy
(1.000 bits).

---

## Critical Observation

The finding text says "holonic is the most stable and most obstructed level
simultaneously." This is contradictory: the most obstructed level (fraction
0.50) is not "most stable" -- it is the least finality-accessible. Shannon
entropy is highest for holonic, indicating it is the least predictable by
entropy. The word "stable" here is misleading.

The intended sense is probably: holonic obstructions, once established, last
longer (higher DT). This is captured better by dwell time than by entropy
or obstruction fraction.

---

## Cross-Level Correlation Structure

Micro-holonic correlation (0.655) is higher than micro-meso (0.524), which
is unexpected if meso mediates the micro-to-holonic relationship. The
explanation: holonic is obstructed for a longer window that overlaps both
the micro and meso windows, increasing its lag-0 correlation with both.

The cointegration proxy (|r| > 0.5 for all pairs) is met in all 5 variants.
This reflects that all three levels are obstructed during overlapping periods
-- they are structurally correlated by the shared constraint schedule, not by
any emergent cross-level coupling.

---

## What Cointegration Would Mean

Standard cointegration (e.g., Engle-Granger) tests whether two non-stationary
series share a common stochastic trend. The binary series here are not
non-stationary in the econometric sense (they are bounded and mean-reverting).
The "cointegration" label in this analysis is a proxy: all pairs have |r| > 0.5.

This proxy is weak. For genuinely new multiscale structure, one would want
to test whether holonic dynamics can be predicted from micro dynamics with
less error than from a univariate holonic model. That test is not run here.

---

## Entropy Contradiction

The Aisha Rahman lens reports holonic entropy = 1.000 bits (maximum for a
binary series at 50% obstruction). Lena Kowalski's finding calls holonic
"most stable." These are in tension and reflect that "stability" is used
differently across the two lenses:

- Rahman uses entropy as a proxy for predictability (lower = more stable).
- Kowalski uses obstruction fraction as a proxy for dominance (higher = more
  active / "most present"), and mislabels it stability.

The synthesis must resolve this terminological conflict.

---

## Verdict for This Lens

Cointegration (by the proxy definition used here) is detected in all 5
variants. The cross-level correlation structure is consistent with the
constraint schedule design: levels that overlap in time are correlated.

No new mathematical object is required. The correlations are derivable from
the overlap structure of the constraint windows. The terminological conflict
between "most obstructed" and "most stable" should be flagged in the synthesis.
