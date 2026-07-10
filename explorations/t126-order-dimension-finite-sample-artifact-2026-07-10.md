# T126's order-dimension leg is a finite-sample class artifact, not a manifoldlikeness wall

2026-07-10. Computed finding (Joe's "is T126 a class no-go rather than a wall?" question, run against the
real machinery). Screen grade; one diagnostic leg; deterministic sprinkle. Model:
`models/records_as_rows_attention_causet_screen.py` (exit 0, 4/4 checks). Bears on the reading of the
S1 / T223 no-go. No claim, lane, or ledger movement without a genuine-sprinkle (RNG-ensemble) follow-up.

## What was tested

Treat attention patterns as candidate causal sets (records = events; earlier->later attention link =
strict relation, transitively closed) and run the existing T126 manifold filter + T156 Myrheim-Meyer
1+1 ordering-fraction band on them. Include a **calibration sweep**: a genuine 1+1 light-cone sprinkle
(the gold-standard manifold-like causal set) at growing N, alongside the repo's OWN known-passing
6-point flat control.

## The finding (the calibration sweep)

| candidate | ordering fraction | T126 |
|---|---|---|
| repo 6-point flat control (known pass) | 0.467 | PASS |
| light-cone sprinkle N=8 | 0.786 | PASS |
| light-cone sprinkle N=12 | 0.697 | PASS |
| light-cone sprinkle N=16 | 0.625 | **REJECT** (order_dimension) |
| light-cone sprinkle N=20 | 0.579 -> 1/2 | **REJECT** (order_dimension) |

**As the sprinkle grows, its ordering fraction converges toward the manifold-like 1+1 value (1/2) --
correct behavior -- while T126's `order_dimension_obstruction` flips from PASS to REJECT.** The object
becomes MORE manifold-like exactly where T126 starts rejecting it. That is backwards for a genuine
manifoldlikeness wall.

## Diagnosis (a Layer-0 homonymy on "manifold-like")

`order_dimension_obstruction` fires when "equal-size intervals have incompatible internal height/width
profiles." A genuine random/quasi-random sprinkle of 1+1 Minkowski HAS such fluctuation -- it is the
expected statistical spread of Alexandrov intervals, not a defect. The tiny hand-tuned 6-point control
passes only because it is too small to show the spread. So the leg tests finite interval-profile
**REGULARITY**, and genuine manifold-like sprinklings **violate** it. "Manifold-like" as this leg means
it (finite-profile-regular) is a DIFFERENT object than "manifold-like" in the continuum / ordering-
fraction sense -- exactly the Layer-0 semantic-alignment failure the GU protocol now names (a
same-name-different-object homonymy applied to TaF's own screen).

## Consequence for S1 / T223 (candidate reopening, not a claim)

T223 concluded the uniform finite finality-colimit ensemble does NOT concentrate on manifoldlike
causal sets, using these finite diagnostics. If the `order_dimension` leg rejects genuine 1+1
sprinklings, then part of that negative may be measuring **diagnostic irregularity rather than
non-manifoldness**. This does NOT overturn T223 -- but it means S1 (`requires_added_assumption`) is a
candidate for RE-SCOPING: the honest question is whether the finality colimits fail a *robust*
manifoldlikeness test (dimension estimator with continuum-limit statistics) or merely the
finite-profile-regularity leg that genuine sprinkles also fail. The n=8 survivor-fraction decay of
T223 is a separate leg and is not addressed here.

## Also robust (independent of the artifact finding)

Generic causal masking -- the transformer default of attending to ALL earlier records -- is a **1D
chain** (`rank_width_obstruction`, ordering fraction 1.0), NOT spacetime at all. So "spacetime from
attention" is FALSE for generic masking; the load-bearing requirement is METRIC (bounded, light-cone)
proximity with genuine spacelike antichains. Lattice attention fails like T223's grids.

## Honest limits / next step

- ONE diagnostic leg (order_dimension); the others (hub, rank/width, interval-profile-density) are not
  claimed to be artifacts.
- A DETERMINISTIC Weyl sprinkle, not a true RNG ensemble. The decisive confirmation is a proper
  random-sprinkle Monte Carlo at several N: does `order_dimension_obstruction` reject a rising fraction
  of genuine 1+1 sprinkles as N grows? If yes, the artifact is confirmed and S1's T126-based leg needs
  a continuum-statistics replacement. That is the recommended follow-up (bounded, cheap).
- Screen grade; NOT a manifoldlikeness proof, dimension estimate, derived metric, or spacetime
  derivation.
