# TS-PERSONA-SPRINT-001 v0.1 Results

**Date:** 2026-06-18
**Status:** Exploration complete. No claim-ledger updates warranted.
**Machine output:** `results/ts-persona-sprint-001-v0.1.json`

---

## Central Investigation Question

> Do explicit time-series dynamics provide genuinely new mathematical structure,
> or are they simply derived observables of the existing TypedTransportNetwork?

---

## System Under Study

A deterministic 3-level holonic system with constraint windows:

| Level   | Sites | Obstruction window | Obstr. fraction |
|---------|-------|-------------------|-----------------|
| Micro   | 3     | steps 10-24       | 0.30            |
| Meso    | 3     | steps 15-29       | 0.30            |
| Holonic | 2     | steps 10-34       | 0.50            |

Five trajectory variants tested: canonical, early_stress, late_stress,
large_gap, zero_gap.

---

## Coordinate Classification (Primary Output)

| Symbol | Name                   | Classification       | Key finding                                                    |
|--------|------------------------|----------------------|----------------------------------------------------------------|
| DT     | obstruction dwell time | derived_observable   | Fully determined by the constraint schedule; no new object required |
| LOD    | lag-onset distance     | derived_observable   | Equals the lag parameter; reads off the schedule structure     |
| PG     | persistence gap        | derived_observable   | Set explicitly by the holonic window; not derived from TTN topology |

All three proposed coordinates are derived observables of the existing
TypedTransportNetwork constraint structure. None require extending the
mathematical formalism.

---

## Outcome Assessment (Four-Outcome Framework)

| Outcome | Assessment |
|---------|-----------|
| (A) TS dynamics strengthen H1 | Partial. The sprint confirms that TTN constraint schedules produce time-series signatures consistent with holonic lock-in. But the signatures are read-offs of the schedule, not emergent from forgotten_dims. |
| (B) TS dynamics re-interpret H1 | Yes. DT/LOD/PG translate static TTN admissibility into a per-step trajectory vocabulary. Interpretive, not additive. |
| (C) TS dynamics identify H1 boundaries | Yes. H1 has no upward recovery propagation mechanism: once forgotten_dims are non-empty, the holonic level has no path to detect micro recovery. This gap is real. |
| (D) TS dynamics add little explanatory power | No. Five independent lenses consistently detect the same dwell asymmetry. The phenomenon is real; its cause is the constraint schedule. |

**Best-supported outcomes: (B) and (C).**

---

## Canonical Trajectory Measurements

```
Persistence gap (PG): 10 steps (micro last obstr. t=24, holonic last obstr. t=34)
Lag-onset distance (LOD): 0 steps (both onset at t=10)
```

| Level   | DT_mean | DT_max | Obstr_frac |
|---------|---------|--------|------------|
| Micro   | 15.0    | 15     | 0.30       |
| Meso    | 15.0    | 15     | 0.30       |
| Holonic | 25.0    | 25     | 0.50       |
| Joint   | 25.0    | 25     | 0.50       |

---

## Cross-Trajectory Findings

| Finding                                | Result |
|----------------------------------------|--------|
| Micro leads holonic onset (all 5 vars) | True   |
| Holonic leads micro offset (all 5 vars)| True   |
| Holonic more predictable (AR1)         | 5/5    |
| Holonic more irreversible (symb. dyn.) | 5/5    |
| Cointegration detected                 | 5/5    |
| Holonic dwell dominates (all 5 vars)   | False  |

The "holonic dwell dominates" failure is diagnostic: for the zero_gap
variant, micro's post-obstruction satisfiable run (25 steps) exceeds
holonic's maximum dwell (20 steps), refuting the naive claim that holonic
always stays obstructed longer.

---

## Discrepancy Between Lenses

Aisha Rahman and Lena Kowalski report conflicting evidence for holonic
"stability":

- AR(1) accuracy is identical (0.959 vs 0.959 for micro and holonic).
  "More predictable" in the code is >= comparison, so a tie counts as
  holonic winning. This is a weak result, not evidence of superiority.

- Run-length compression is identical (0.060 vs 0.060).

- Shannon entropy is HIGHER for holonic (1.000 bits) than for micro
  (0.881 bits). A 50%-obstructed binary series maximizes entropy;
  holonic being the most obstructed level makes it the least
  "stable" by entropy.

- Lena Kowalski reports "holonic is most stable and most obstructed
  simultaneously." These attributes are contradictory under Shannon
  entropy. The finding reflects a tension in how "stability" is defined.

---

## Principal Findings

1. **All three proposed coordinates are derived observables.** DT, LOD,
   and PG are fully computable from the TTN constraint schedule without
   any new mathematical object.

2. **The persistence gap is not emergent.** PG=10 in the canonical
   trajectory because the holonic constraint window was hardcoded to
   extend to t=34. The gap does not arise from forgotten_dims or network
   topology.

3. **H1 has a genuine boundary.** H1 (TypedTransportNetwork) provides no
   mechanism for holonic recovery propagation. Once cross-level transport
   accumulates forgotten_dims, there is no defined operation for signaling
   upward that micro has recovered. This is a structural gap, not a
   naming issue.

4. **The zero_gap variant falsifies "holonic always dwells longer."**
   When PG=0, micro's satisfiable run can exceed holonic's maximum dwell.
   This shows the dwell asymmetry is a function of the constraint schedule,
   not a topological invariant.

5. **Five-lens convergence on asymmetry is meaningful but tautological.**
   All five lenses detect the dwell asymmetry because the asymmetry is
   baked into the constraint schedule. Convergence demonstrates that the
   analytic tools work correctly; it does not establish that the asymmetry
   is a new phenomenon.

---

## What Would Change the Classification

PG would be reclassified from derived_observable to potentially new_invariant if:

1. The holonic constraint generator is stripped of its explicit persistence
   window (remove the hardcoded 30-34 obstruction), AND

2. PG > 0 still appears in the trajectory due solely to non-empty
   forgotten_dims in the TTN morphisms.

This test is MINI-GOAL-TS-002.

---

## Follow-On Goals

**MINI-GOAL-TS-002:** Test whether PG emerges from non-empty forgotten_dims
WITHOUT explicit constraint scheduling. Requires modifying the holonic
constraint generator to remove the hardcoded persistence window.

**MINI-GOAL-TS-003:** Identify under what TTN topologies (tree / dense /
ring) the holonic dwell asymmetry vanishes (PG=0). If PG=0 is achievable
with non-empty forgotten_dims, the time-series analysis and T40 structural
analysis diverge -- which would be a genuine discovery.

---

## Files

- `models/ts_persona_sprint.py` -- analysis module (all five lenses)
- `models/run_ts_persona_sprint.py` -- runner
- `results/ts-persona-sprint-001-v0.1.json` -- machine-readable output
- `explorations/TS-PERSONA-SPRINT-001-elena-voss-v0.1.md`
- `explorations/TS-PERSONA-SPRINT-001-marcus-hale-v0.1.md`
- `explorations/TS-PERSONA-SPRINT-001-aisha-rahman-v0.1.md`
- `explorations/TS-PERSONA-SPRINT-001-rafael-cortez-v0.1.md`
- `explorations/TS-PERSONA-SPRINT-001-lena-kowalski-v0.1.md`
- `explorations/TS-PERSONA-SPRINT-001-synthesis-v0.1.md`
