# TS-PERSONA-SPRINT-001: Marcus Hale Lens (Causal Inference)

**Exploration status:** Heterodox sketch; not promoted to core D1 claims.
**Sprint:** TS-PERSONA-SPRINT-001
**Synthesis:** See `explorations/TS-PERSONA-SPRINT-001-synthesis-v0.1.md`

---

## Lens

Causal inference analysis: lagged correlations, onset lead-lag, offset
persistence. Key question: does micro obstruction precede holonic
obstruction at onset, and does holonic obstruction outlast micro recovery?

---

## Canonical Trajectory Results

| Metric                              | Value |
|-------------------------------------|-------|
| Micro onset step                    | 10    |
| Holonic onset step                  | 10    |
| Lag-onset distance (LOD)            | 0     |
| Micro last-obstructed step          | 24    |
| Holonic last-obstructed step        | 34    |
| Offset lag (persistence gap, PG)    | 10    |
| Micro leads holonic at onset        | True (tie: LOD=0) |
| Holonic leads micro at offset       | True (PG=10)      |

**Best micro-to-holonic correlation lag:** 0

**Finding:** Micro leads holonic by 0 step(s) at onset. Holonic persists
10 step(s) beyond micro recovery. Asymmetric causal structure:
micro->holonic for onset, holonic self-sustains at offset.

---

## Cross-Variant Findings

Across all 5 trajectory variants:

- Micro leads holonic at onset: **True in all variants** (or tied, LOD >= 0)
- Holonic leads micro at offset: **True in all variants** (PG > 0 for all
  except zero_gap which was designed to produce PG=0 but still shows PG=0)

| Variant      | LOD | PG  |
|--------------|-----|-----|
| canonical    | 0   | 10  |
| early_stress | 0   | 5   |
| late_stress  | 0   | 5   |
| large_gap    | 0   | 15  |
| zero_gap     | 0   | 5   |

Note: zero_gap shows PG=5, not PG=0. The zero_gap variant sets the holonic
persistence_gap parameter to 0 in the constraint schedule, but the holonic
window covers 10-29 (20 steps) while micro covers 10-24 (15 steps). The
difference (29-24=5) appears as measured PG because holonic overlaps with
the meso period. PG=0 was not achieved even in the zero_gap variant.

---

## Interpretation

LOD=0 across all variants is structurally forced: the holonic constraint
window starts at the same step as the micro constraint window (both begin
when micro first becomes obstructed). There is no mechanism for holonic to
detect micro obstruction BEFORE micro becomes obstructed. LOD=0 is not a
causal finding; it reflects design.

The persistence gap (PG) is the more substantive signal. PG > 0 in all
variants including zero_gap. However, this is also a consequence of the
constraint schedule: holonic's window always ends at meso_end + pg_parameter,
and meso ends after micro, so holonic always ends after micro.

**The causal asymmetry (micro leads onset, holonic lags recovery) is real
but tautological given the constraint design.** It would become non-trivial
if PG emerged from TTN topology and forgotten_dims without explicit scheduling.

---

## Open Question

Can the causal asymmetry (onset: micro leads; offset: holonic persists) be
derived from the structure of D1RestrictionMorphisms and forgotten_dims alone,
without hardcoding a holonic persistence window? If yes, the lead-lag structure
becomes a genuine causal consequence of information loss. If no, it remains a
scheduling artifact. This is the question MINI-GOAL-TS-002 addresses.

---

## Verdict for This Lens

The onset/offset asymmetry is consistent with H1 (TypedTransportNetwork)
and with outcome (B): a re-interpretation of H1 in causal-inference language.
The persistence gap is a real measured quantity, but its cause is the
constraint schedule, not the network topology. No new mathematical object
is required by this lens.
