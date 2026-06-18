# TS-PERSONA-SPRINT-001: Synthesis

**Exploration status:** Heterodox sketch; not promoted to core D1 claims.
**Date:** 2026-06-18
**Trajectories tested:** 5 (canonical + 4 parameter variants)
**Lenses:** Elena Voss (Dynamical Systems), Marcus Hale (Causal Inference),
            Aisha Rahman (Physics-Informed ML), Rafael Cortez (Symbolic Dynamics),
            Lena Kowalski (Multiscale Statistics)

---

## Central Question

> Do explicit time-series dynamics provide genuinely new mathematical structure,
> or are they simply derived observables of the existing TypedTransportNetwork?

---

## Coordinate Classification

The sprint proposed three new finality coordinates. The synthesis classifies
each according to four categories: new invariant, derived observable,
implementation convenience, requires extension.

### DT (obstruction dwell time)

**Classification: derived_observable**

DT is the mean length of obstructed runs in a per-level binary satisfiability
series. This is fully determined by the constraint schedule embedded in the
TTN morphism's forgotten_structure and constraint windows. Given the constraint
schedule, DT is computable without any new mathematical object.

DT is a useful diagnostic shorthand -- it summarizes the satisfiability series
in a single number -- but it is not a new invariant. A static TTN snapshot
plus its time-indexed constraint generator already encodes DT.

### LOD (lag-onset distance)

**Classification: derived_observable**

LOD measures the step difference between micro onset and holonic onset. In the
canonical trajectory and all variants, LOD = 0: both micro and holonic are
triggered at the same step (t=10) because the holonic constraint window is set
to start at micro onset. LOD is a read-off of the constraint schedule, not a
property of TTN topology.

If LOD were non-zero, it would still be derivable from the schedule parameters.
LOD = holonic_start - micro_start, which is a design parameter.

### PG (persistence gap)

**Classification: derived_observable (current implementation)**
**Classification would be potentially new_invariant if MINI-GOAL-TS-002 succeeds**

PG measures holonic obstruction steps beyond micro recovery. In the canonical
case, PG = 10 (micro clears at t=24, holonic clears at t=34). This is set
explicitly by the holonic constraint window (steps 10-34), not by any
consequence of TTN topology or non-empty forgotten_dims.

The persistence gap is real and measurable. What it is not (yet) is emergent:
it does not arise from the structure of D1RestrictionMorphisms. A genuine PG
would require showing that non-empty forgotten_dims in the cross-level morphism
causes the holonic level to remain obstructed after micro recovery, without
any explicit scheduling of that extension.

---

## Four-Outcome Assessment

| Outcome | Assessment |
|---------|-----------|
| (A) TS dynamics strengthen H1 | Partial. The sprint confirms that TTN constraint schedules produce time-series signatures consistent with holonic lock-in. But signatures are read-offs of the schedule, not emergent from forgotten_dims. No new invariant is established. |
| (B) TS dynamics re-interpret H1 | Yes. DT/LOD/PG translate static TTN admissibility into a per-step trajectory vocabulary. This provides a useful interpretive lens without adding new structure. |
| (C) TS dynamics identify H1 boundaries | Yes. H1 (TypedTransportNetwork) provides no mechanism for upward recovery propagation. Once cross-level transport accumulates forgotten_dims, the holonic level has no defined path to detect that micro has recovered. This is a structural gap in H1's current formulation. |
| (D) TS dynamics add little explanatory power | No. All five lenses detect the dwell asymmetry consistently, confirming the phenomenon is real. The caveat is that consistency reflects the constraint schedule design, not independent confirmation of an emergent effect. |

**Best-supported outcomes: (B) and (C).**

---

## What Each Lens Actually Showed

| Lens            | Key result                                   | Verdict                               |
|-----------------|----------------------------------------------|---------------------------------------|
| Elena Voss      | Phase transitions equal; max dwell tied in canonical; holonic dwell > micro dwell only for obstr. period | Dwell asymmetry is schedule-driven, not attractor-like |
| Marcus Hale     | LOD=0 (co-onset); PG=10; offset asymmetry real | Asymmetry real but tautological given constraint design |
| Aisha Rahman    | AR1 tied (0.959 all levels); holonic entropy HIGHER not lower; "more predictable" result is a tie misreported | Holonic is not more predictable or compressible |
| Rafael Cortez   | Permutation entropy identical; irreversibility zero for all levels | No discriminating signal; method under-powered for 2-transition series |
| Lena Kowalski   | Cointegration by proxy; "most stable" language contradicts entropy finding | Correlated by overlapping windows; terminology conflict flagged |

---

## Discrepancy Between Lenses

Two conflicts in the findings:

1. **"Holonic is more predictable" vs holonic entropy = 1.000 bits (maximum).**
   Aisha Rahman's finding is triggered by a tie (AR1 equal); the entropy points
   the other way. The holonic level, obstructed 50% of the time, is the least
   information-efficient level under Shannon entropy. There is no contradiction
   in the mathematics -- only in the narrative label applied to the result.

2. **"Holonic is most stable" vs holonic is most obstructed.**
   Lena Kowalski's "most stable" label refers to holonic dwell time, not to
   entropy or obstruction fraction. The label is misleading. "Most persistently
   obstructed" is accurate; "most stable" is not.

These conflicts are resolved once the labels are replaced by the underlying
measurements. The measurements themselves are consistent.

---

## The Genuine H1 Boundary (Outcome C)

H1 (TypedTransportNetwork) describes how structure propagates downward across
levels via typed morphisms with forgotten_structure. What H1 does not currently
specify is the converse: how does a lower level signal to a higher level that
an earlier obstruction has resolved?

In the current formalism, once a cross-level morphism has forgotten_dims, the
holonic level loses access to the detail that caused the obstruction. If that
detail changes at the micro level (obstruction clears), there is no TTN
operation defined for propagating the recovery upward. The holonic level can
only learn about micro recovery if the cross-level transport is re-run with
the current micro state.

This is a genuine gap. It is not a bug in the formalism; it is an
incompleteness. Whether this gap warrants extending the mathematics (a new
operation for recovery propagation) or is simply a modeling choice (holonic
levels do not auto-update on micro recovery) depends on whether the research
program has a claim that requires upward propagation.

No such claim currently exists in CLAIM-LEDGER.md. The gap should be
documented as an open question in ROADMAP.md.

---

## H1 Evidence Record

H1 (TypedTransportNetwork as a primitive) is consistent with the time-series
findings. The sprint does not strengthen, weaken, or refute H1. It:

- Provides a trajectory vocabulary (DT/LOD/PG) for discussing H1 dynamics.
- Identifies a structural boundary: H1 has no upward recovery propagation.
- Does not establish any new D1 invariant.

H1 status: unchanged. The MATHEMATICAL-INDEPENDENCE-AUDIT.md and CLAIM-LEDGER.md
do not require updates from this sprint.

---

## Recommended Updates

1. **ROADMAP.md:** Add an open question: "Does the holonic persistence gap
   (PG) arise from non-empty forgotten_dims without explicit scheduling?
   (MINI-GOAL-TS-002)"

2. **ROADMAP.md:** Add open question: "Under what TTN topologies does the
   holonic dwell asymmetry vanish? (MINI-GOAL-TS-003)"

3. **HYPOTHESES.md:** Note that H1 has been tested against time-series
   dynamics and confirmed consistent, with the boundary that recovery
   propagation is undefined. Add as a known H1 limitation.

4. **No CLAIM-LEDGER.md update.** No claim has changed status. The sprint
   found derived observables, not new invariants.

---

## Follow-On Goals

**MINI-GOAL-TS-002 (Priority: High)**
Test whether PG emerges from non-empty forgotten_dims WITHOUT explicit
constraint scheduling. Required change: remove the hardcoded holonic
persistence window (steps 30-34) from `_holonic_constraints()`, and instead
let holonic constraints propagate from meso/micro via the TTN structure.
If PG > 0 still appears, it is potentially a new invariant.

**MINI-GOAL-TS-003 (Priority: Medium)**
Systematically test TTN topologies (tree, dense, ring, linear) for whether
holonic dwell asymmetry can be eliminated. If PG=0 is achievable with
non-empty forgotten_dims, the structural and time-series analyses diverge --
which would itself be a significant finding.
