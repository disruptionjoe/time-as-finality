# PREDECLARED SPEC: is the dimensional collapse NATIVE, or does it require imported inertial motion?

2026-07-10, predeclared BEFORE building or running (committed alone as the anti-p-hack receipt; results
land separately). Screen/toy grade. Follows the PARTIAL result of
`records-native-generator-RESULTS-2026-07-10.md`: only `ballistic` (constant-velocity) issuance produced
the D-independent dimensional collapse, which is the "smuggled-metric" crux -- constant-velocity
worldlines are most of Minkowski. This experiment tests whether a NON-inertial, genuinely native rule
produces the same collapse.

## The question (fixed)

**Does a native content-based autoregressive ATTENTION process -- with no imposed positions, velocities,
or light cone -- exhibit the same D-independent dimensional collapse that imposed ballistic motion does?**
If yes, the collapse is native and records-as-rows is a real generator (ballistic was one instance). If
only the ballistic arm collapses, the collapse requires imported inertial structure and the frame
imports special relativity.

## The two arms (fixed)

- **Arm A -- inertial-ballistic (reference).** K worldlines, `r_t = start_k + v_k * t`
  (`start_k ~ N(0,I_D)`, `v_k ~ N(0,I_D/D)`); each record an event on a worldline. Causal relation:
  `i < j` iff `t_i < t_j` and `||r_j - r_i|| <= c*(t_j - t_i)`. Knob `c in {0.5, 1.0, 2.0, 4.0}`.
  (Reproduces the established collapse as the positive reference.)
- **Arm B -- native-attention (the test).** A single-layer causal self-attention autoregressive process,
  NO positions/velocities/light-cone: fixed random `W_q, W_k, W_v` (seeded, orthogonalized); `r_0` random;
  for `t>=1`, `q = W_q r_{t-1}`, keys `k_s = W_k r_s` and values `val_s = W_v r_s` over `s<t`, logits
  `(k_s . q)/(sqrt(D)*tau)`, softmax weights `a_{ts}`, `r_t = sum_s a_{ts} val_s + eps*noise`
  (`eps=0.1`). **Causal relation is the ATTENTION pattern itself**: `i < j` iff `a_{ji} >= 1/(#prior)`
  (j attended to i above uniform). Knob `tau in {0.5, 1.0, 2.0, 4.0}` (attention sharpness -- the native
  analog of cone width). Genuinely native: the causal structure comes from content similarity, not an
  imposed geometry.

Both arms: `D in {2, 4, 8, 14}`, `N in {40, 60, 80, 100}`, 6 seeds/cell; transitively close the relation;
ordering fraction -> dimension estimate.

## Estimators (fixed)

- **Primary (decision): diamond-MM** `estimate_dimension` (the validated
  `models/myrheim_meyer_dimension_estimator.py`), applied identically to BOTH arms so the shared
  diamond-vs-slab bias cancels in the comparison. The decision rides on D-INDEPENDENCE, not absolute d_hat.
- **Instrument validation (folded-in slab recalibration): slab-MM.** Calibrate ordering-fraction -> d on
  uniform d-dim SLAB sprinklings (`t ~ U[0,T]`, `x ~ U[box]^{d-1}`, relation `|dx| <= dt`, fixed aspect
  ratio) for `d in {1,2,3,4}`; self-validate it recovers d within +/-0.4 on held-out slabs. In particular
  a genuine D=1 (1-space+1-time) slab must read `d_hat_slab ~ 2` -- fixing the failed control of the prior
  sweep. If slab-MM self-validates, absolute collapse values become interpretable; if not, absolute
  values stay uncalibrated and only the D-independence decision stands.

## The collapse criterion (fixed, per arm)

An arm exhibits **collapse** iff there is a knob value where, over `D in {2,4,8,14}`:
1. **D-independent**: `max_D d_hat - min_D d_hat <= 0.5` (the emergent dimension stops tracking D);
2. **genuine collapse**: that D-independent value is `>= 0.5` below the arm's small-knob (tracks-D)
   regime at `D=14` (a real reduction, not trivially flat);
3. **N-stable**: at the collapse knob, the across-N spread at `D=14` is `<= 0.4`.

## Predeclared outcomes

- **NATIVE COLLAPSE CONFIRMED** (Arm B exhibits collapse): the collapse does not require imposed inertial
  motion -- a content-based attention process collapses the feature dimension too. records-as-rows is a
  genuine (native) generator; ballistic was one instance. Strong positive; S1 finite route
  candidate-reopens; proceed to a validated-geometry chirality leg.
- **INERTIAL-ONLY** (Arm A collapses, Arm B does NOT -- always tracks D, or chains, or no stable
  structure): the collapse REQUIRES imported inertial/Minkowski structure. records-as-rows is a
  reinterpretation dressed as a generator; the finite S1 route stays closed for a demonstrated reason.
- **NEITHER / MIXED**: report honestly (e.g. Arm B collapses only under an attention regime that itself
  encodes a geometry; or neither arm is stable at this N). No forced reading.

## Honest caveats (fixed)

- The emergent geometry of content-based attention is genuinely UNKNOWN a priori -- that is why this is a
  real test, not a rigged one. Arm B may degenerate (chain at sharp attention, dense at flat attention)
  with no collapse; that is an informative INERTIAL-ONLY outcome.
- Absolute d_hat is bias-limited (processes are non-uniform causets, not clean sprinkles); the DECISION
  is the calibration-robust D-independence contrast between the two arms.
- Screen/toy grade; ordering fraction is one necessary-not-sufficient statistic; no embedding, metric,
  continuum, or S1-promotion claim.

## Discipline

Arms, knobs, grid, estimators, and the collapse criterion above are FROZEN by this commit. The
experiment (`models/records_native_vs_inertial_sweep.py`) and results are committed separately; the
verdict is whatever the frozen criterion returns.
