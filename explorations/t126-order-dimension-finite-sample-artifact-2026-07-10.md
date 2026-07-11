# T126's order-dimension leg is a finite-sample class artifact, not a manifoldlikeness wall

2026-07-10. Computed finding (Joe's "is T126 a class no-go rather than a wall?" question, run against the
real machinery), **now confirmed by an RNG-ensemble Monte Carlo** (see the CONFIRMED section below).
Screen grade; one diagnostic leg. Models: `models/records_as_rows_attention_causet_screen.py`
(deterministic Weyl probe, exit 0, 4/4) and `models/records_as_rows_sprinkle_montecarlo.py` (seeded
random ensemble, exit 0, 5/5). Bears on the reading of the S1 / T223 no-go: S1's T126-based leg is now a
candidate for a continuum-statistics replacement. Screen grade only -- not a lane/ledger move on its own.

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

## CONFIRMED by the RNG ensemble (2026-07-10 follow-up)

The recommended follow-up below was run: a proper **seeded random-sprinkle Monte Carlo** (50 genuine
random 1+1 Minkowski sprinkles per N, points ~ Uniform in null coordinates, audited with the same
unmodified TaF machinery). Model: `models/records_as_rows_sprinkle_montecarlo.py` (exit 0, 5/5 checks,
reproducible at `SEED=20260710`).

| N | mean ordering fraction | `order_dimension` rejection rate | passes T126 |
|---|---|---|---|
| 8 | 0.479 | 14% | 82% |
| 10 | 0.505 | 38% | 62% |
| 12 | 0.500 | 66% | 34% |
| 14 | 0.518 | 92% | 8% |
| 16 | 0.496 | **94%** | 6% |

The order-dimension rejection rate rises **monotonically 14% -> 38% -> 66% -> 92% -> 94%**, rejecting
**94% of genuine random 1+1 sprinkles at N=16** -- while the ordering fraction stays in the
Myrheim-Meyer 1+1 manifold-like band (1/2 +/- 1/10) at **every** N. So the objects are manifold-like
throughout and the leg rejects **more** of them as they scale. A genuine manifoldlikeness wall would
reject **fewer** manifold-like objects as N grows, not more. This upgrades the deterministic-Weyl
finding to a proper random ensemble and confirms it: the order-dimension leg measures finite
interval-profile REGULARITY, which genuine manifold-like sprinklings statistically violate.

**Pre-registration correction (disclosed).** One of the five pre-registered checks first encoded a
factual error about the statistic -- it expected the ordering fraction to *start away from 1/2 and
converge*. A uniform-square 1+1 sprinkle has `P(comparable) = 1/4 + 1/4 = 1/2` at every N, so it sits in
the manifold-like band throughout rather than converging into it. The check was corrected to the true
manifold-likeness condition (in-band at every N) and disclosed in the script; the three substantive
claims (rising rate, majority at max N, monotonicity) each passed independently and unchanged. Being
manifold-like at *all* N while rejection climbs is a stronger form of the artifact finding, not a
weaker one.

## Honest limits / next step

- ONE diagnostic leg (order_dimension); the others (hub, rank/width, interval-profile-density) are not
  claimed to be artifacts.
- ~~A DETERMINISTIC Weyl sprinkle, not a true RNG ensemble.~~ **Done (above): the RNG-ensemble Monte
  Carlo confirms the artifact.** What it establishes is that S1's T126-based leg needs a
  continuum-statistics replacement (a dimension estimator with a declared tolerance, robust to the
  natural Alexandrov-interval spread) rather than the finite interval-profile-regularity leg.
- Does NOT overturn T223's separate n=8 survivor-fraction leg (a different diagnostic, not addressed
  here). S1 (`requires_added_assumption`) is a candidate for RE-SCOPING, not reversal.
- Screen grade; NOT a manifoldlikeness proof, dimension estimate, derived metric, or spacetime
  derivation.
