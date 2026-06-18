# TS-PERSONA-SPRINT-001: Rafael Cortez Lens (Symbolic Dynamics)

**Exploration status:** Heterodox sketch; not promoted to core D1 claims.
**Sprint:** TS-PERSONA-SPRINT-001
**Synthesis:** See `explorations/TS-PERSONA-SPRINT-001-synthesis-v0.1.md`

---

## Lens

Symbolic dynamics analysis: ordinal patterns, permutation entropy,
time-reversal asymmetry (irreversibility). Key question: is the holonic
trajectory less random (lower permutation entropy) and more time-irreversible
than the micro trajectory?

Ordinal patterns of order 2 (consecutive pairs):
- "up": x_{t+1} > x_t
- "down": x_{t+1} < x_t
- "same": x_{t+1} = x_t

Permutation entropy H over ordinal pattern distribution.
Irreversibility = sum(|p_forward(i) - p_reverse(i)|) / 2.

---

## Canonical Trajectory Results

| Metric                          | Micro  | Holonic |
|---------------------------------|--------|---------|
| Ordinal patterns (up/down/same) | 2/2/45 | 2/2/45  |
| Permutation entropy (bits)      | 0.287  | 0.287   |
| Irreversibility score           | 0.000  | 0.000   |

**Finding:** Permutation entropy and irreversibility are identical for micro
and holonic in the canonical configuration. Zero irreversibility.

---

## Critical Observation

All three levels have the same ordinal pattern distribution: 2 "up" transitions,
2 "down" transitions, and 45 "same" steps, in 49 consecutive pairs. The forward
and reversed distributions are identical (same counts), producing zero
irreversibility.

Zero irreversibility is expected: a binary series with only two 0->1 and two
1->0 transitions has a perfectly symmetric transition structure. The forward
trajectory enters and exits obstruction exactly once; the reversed trajectory
also enters and exits exactly once. They are mirror images.

This means time-reversal asymmetry cannot be detected by ordinal patterns on
these trajectories. The series is too simple (2 transitions in 50 steps) for
ordinal pattern analysis to be discriminative.

---

## Cross-Variant Results

All five variants produce the same result: permutation entropy 0.287 and
irreversibility 0.000 for all levels. This is a structural feature of any
binary series with exactly 2 transitions, regardless of the window sizes.

The "holonic is less random and more irreversible" finding in the code is
triggered by the condition `h_pe <= m_pe AND h_irr >= m_irr`. With equal
values, both conditions are True (via <=, >= comparisons), so the finding
fires. This is another tie misreported as a holonic advantage.

---

## Interpretation

Symbolic dynamics analysis of order-2 ordinal patterns is not the right tool
for binary series with only 2 transitions in 50 steps. The method needs
higher-entropy series (more transitions) to be informative.

A more informative application would compare ordinal patterns across different
CA rules (as in T36), where entropy and irreversibility vary substantially
across rules. Applied to the current holonic trajectories, the method is
under-powered.

---

## What This Lens Would Need to Be Informative

1. Trajectories with more transitions (e.g., a micro system that alternates
   between obstruction and satisfaction multiple times per trajectory).

2. Higher-order ordinal patterns (length 3 or 4) to capture sub-block structure.

3. A comparison between trajectories that genuinely differ in reversibility --
   for example, comparing a trajectory where micro drives holonic (causal) against
   one where holonic is independently obstructed (non-causal).

---

## Verdict for This Lens

The lens produces no discriminating signal for these trajectories. Permutation
entropy and irreversibility are identical across all levels and all variants.
The "more irreversible" finding in the code is a tie misclassified as a holonic
advantage.

No new mathematical object is required. The null result here is informative:
ordinal pattern analysis of simple binary series with few transitions is not a
useful finality diagnostic.
