# TS-PERSONA-SPRINT-001: Elena Voss Lens (Dynamical Systems)

**Exploration status:** Heterodox sketch; not promoted to core D1 claims.
**Sprint:** TS-PERSONA-SPRINT-001
**Synthesis:** See `explorations/TS-PERSONA-SPRINT-001-synthesis-v0.1.md`

---

## Lens

Dynamical systems analysis: attractor-like behavior, dwell times, state
recurrence, phase transitions.

**Key question for this lens:** Do finality trajectories show attractor-like
behavior at the holonic level, specifically: fewer phase transitions and
longer dwell times, consistent with holonic lock-in?

---

## Canonical Trajectory Results

| Metric                     | Micro | Meso  | Holonic |
|----------------------------|-------|-------|---------|
| Phase transitions          | 2     | 2     | 2       |
| Max dwell time (steps)     | 25    | 25    | 25      |
| Recurrence fraction        | 0.959 |  -    | 0.959   |

**Finding:** Holonic dynamics are not demonstrably simpler than micro in
the canonical configuration.

The phase transition count is identical (2 for all levels: one entry into
obstruction, one exit). The maximum dwell time is also identical at 25 steps
for both micro and holonic -- because both levels have a 25-step satisfiable
run, just at different positions in the trajectory.

The "attractor-like" hypothesis requires that holonic has fewer transitions
or longer maximum dwell. Neither criterion is met in the canonical case.

---

## Cross-Variant Results

| Variant       | Holonic max dwell | Micro max dwell | Holonic dominates? |
|---------------|-------------------|-----------------|--------------------|
| canonical     | 25                | 25              | No (tie)           |
| early_stress  | 25                | 25              | No (tie)           |
| late_stress   | 25                | 20              | Yes                |
| large_gap     | 30                | 25              | Yes                |
| zero_gap      | 20                | 25              | No (reversed)      |

Holonic dwell dominates in 2 of 5 variants, is tied in 2, and is reversed
in 1 (zero_gap).

---

## Interpretation

The dwell-time comparison is confounded by the satisfiable periods. Both
micro and holonic have a pre-obstruction satisfiable run at the start of
the trajectory. The maximum dwell often belongs to that pre- or
post-obstruction satisfiable period, not to the obstructed period itself.

If the question is restricted to obstructed dwell times only:

| Variant       | Holonic obstr. dwell | Micro obstr. dwell |
|---------------|---------------------|-------------------|
| canonical     | 25                  | 15                |
| early_stress  | 25                  | 15                |
| late_stress   | 25                  | 15                |
| large_gap     | 30                  | 15                |
| zero_gap      | 20                  | 15                |

In all 5 variants, the holonic obstructed dwell time exceeds the micro
obstructed dwell time. This is consistent with holonic lock-in. However,
it is a direct consequence of the constraint schedule design: the holonic
window is always set >= the micro window by construction.

---

## Verdict for This Lens

The attractor hypothesis (holonic has fewer transitions) is not supported.
The dwell-time asymmetry (holonic stays obstructed longer) is confirmed
across all variants, but it is not an emergent property -- it reflects
the hardcoded constraint window.

This lens does not provide evidence that holonic dynamics require new
mathematical machinery beyond what the constraint schedule already encodes.

---

## Notation

This report uses the same binary satisfiability series as the synthesis.
1 = satisfiable (finality accessible); 0 = obstructed (finality blocked).
