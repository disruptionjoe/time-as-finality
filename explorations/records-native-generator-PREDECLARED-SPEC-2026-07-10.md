# PREDECLARED SPEC: does a finality-native record generator collapse to a manifold-like dimension?

2026-07-10, predeclared BEFORE building or running the experiment (committed alone as the
anti-p-hacking receipt; results land in a separate follow-up). Screen/toy grade. Targets the T526 open
object: a finality-native generator that produces finite causal sets WITHOUT importing Lorentzian u/v
coordinates, scored by the validated Myrheim-Meyer dimension estimator
(`models/myrheim_meyer_dimension_estimator.py`).

## The question (fixed in advance)

Read records-as-rows literally: records issued in sequence, each a point in a D-dim column space, with a
causal mask = a finite-propagation constraint. **Is there any finality-native parameter regime in which
the emergent causal set reads a STABLE, scale-invariant, manifold-like dimension `d_hat ~ 2` -- a genuine
dimensional COLLAPSE from the D-dim column space -- without importing Minkowski coordinates?** If yes,
records-as-rows is a GENERATOR (S1 finite-route candidate-reopen). If no across the whole predeclared
grid, records-as-rows is a REINTERPRETATION, not a generator (the T526 gap is real and principled).

## The generator family (fixed)

- N records issued at ticks `t = 1..N` (the row index = time; native).
- Each record carries a position `r_t` in R^D (the column space; D = 14 is the Y14 target).
- **Native issuance dynamics** (three families, all swept -- the experiment does not prejudge which, if
  any, works):
  - `iid`: `r_t ~ N(0, I_D)` independent (feature distance ~ const in dt);
  - `diffusive`: random walk `r_t = r_{t-1} + eta_t`, `eta_t ~ N(0, I_D/D)` (distance ~ sqrt(dt));
  - `ballistic`: persistent velocity `r_t = r_{t-1} + v`, one `v ~ N(0, I_D/D)` per record-worldline
    seeded at issuance (distance ~ dt) -- realized as K independent worldlines sampled at staggered
    ticks so pairs have a genuine velocity spread.
- **Causal mask = finite propagation (the ONLY imported structure -- one scalar `c`):**
  `i < j` iff `t_i < t_j` AND `||r_j - r_i|| <= c * (t_j - t_i)`. Uses only issuance order (native) +
  the records' own feature distances (native) + the propagation speed `c`. No u/v/Minkowski coordinates.
- Transitively close -> the causal order -> ordering fraction `= (#related pairs)/C(N,2)` ->
  `estimate_dimension` (the validated MM estimator).

## The grid (fixed)

- dynamics in {iid, diffusive, ballistic}
- D in {2, 4, 8, 14}
- c in {0.5, 1.0, 2.0, 4.0} (per-step feature scale normalized to ~1)
- N in {40, 60, 80, 120} (for the plateau / scale-invariance test)
- 8 seeds per cell; report the seed-mean `d_hat(N)` per cell.

## The manifold-like criterion (fixed, predeclared)

A cell `(dynamics, c, D)` is a **manifold-like generator** iff, over `N in {40,60,80,120}`:
1. **stable plateau**: all four seed-mean `d_hat(N)` lie within `+/- 0.3` of their across-N mean
   (scale-invariant, not a finite-size accident);
2. **genuine collapse**: the across-N mean `d_hat <= D - 0.5` (the emergent dimension is strictly below
   the column dimension -- a real collapse, not just reading D back);
3. **not a chain**: across-N mean `d_hat >= 1.5`.
- **PRIMARY TARGET (2D):** additionally the across-N mean `d_hat in [1.7, 2.3]`.
- **SECONDARY:** a stable plateau at any other fixed value (report the value).

## Predeclared outcomes

- **GENERATOR FOUND** (some cell meets the PRIMARY target): records-as-rows generates 1+1 manifold-like
  geometry from finality-native data. S1 finite route candidate-reopens; proceed to the chirality leg
  (discrete Dirac operator on the survivor's causal graph with a frontier boundary; net chiral edge
  mode?).
- **COLLAPSE-TO-CHAIN** (small c): `d_hat -> 1`. Expected boundary; not a generator.
- **FEATURE-DIMENSION / NO PLATEAU** (large c or iid): `d_hat` tracks D or fails stability. Expected
  boundary; not a generator.
- **FALSIFIED** (no cell meets the PRIMARY target): records-as-rows does NOT generate 2D geometry in the
  predeclared grid. Report any SECONDARY plateau honestly. S1 finite route stays closed for a
  demonstrated reason; the frame is a reinterpretation, not a mechanism.

## Honest caveats (fixed in advance)

- **The interpretive crux:** the propagation speed `c` is the one imported structure. Whether "native
  record process + one scalar `c`" counts as finality-native or as a smuggled metric is itself something
  the result sharpens -- if ONLY `ballistic` (constant-velocity) issuance yields `d_hat ~ 2`, that is
  either "the frame recovers inertial/SR structure as the condition for emergent geometry" (positive) or
  "ballistic = Minkowski smuggled in" (deflationary); the `d_hat` value and the dynamics dependence
  discriminate, and BOTH readings will be reported.
- **The load-bearing risk:** collapsing `d_hat` from D=14 down to ~2 is the literal "GR emerges from
  finite-speed resolution" claim; failure is a clean, honest negative on the frame.
- Screen/toy grade; ordering fraction is ONE necessary-not-sufficient statistic; no embedding, metric,
  locality, or continuum claim; no S1 promotion by this alone.

## Discipline

The generator family, grid, and criterion above are FROZEN by this commit. The experiment
(`models/records_native_generator_sweep.py`) and its results will be committed separately; the verdict
is whatever the frozen criterion returns, positive or negative.
