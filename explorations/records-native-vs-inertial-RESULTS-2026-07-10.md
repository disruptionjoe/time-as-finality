# RESULTS: native-vs-inertial collapse test -- INERTIAL-ONLY. The geometry needs imposed inertial motion.

2026-07-10. Executes the frozen spec `records-native-vs-inertial-PREDECLARED-SPEC-2026-07-10.md`
(committed first). Model: `models/records_native_vs_inertial_sweep.py` (exit 0, deterministic seed
20260710). Screen grade. **Verdict: INERTIAL-ONLY** -- the dimensional collapse requires imported
inertial / Minkowski structure; a genuinely native content-based attention process does not produce it.
This settles the geometry lane of records-as-rows with a clean negative. No S1 status change.

## Instrument control now PASSES (the folded-in slab recalibration worked)

The prior sweep's failure was a diamond-vs-slab calibration mismatch. Recalibrating the MM estimator on
uniform SLAB sprinklings fixed it: a genuine D=1 (1-space+1-time) slab reads `d_hat_slab = 1.00`, a D=2
slab reads `1.98`. The instrument now sees the true dimension of a clean slab, so the verdict is
trustworthy (and the decision rides on the calibration-robust D-independence contrast anyway).

## The two arms, side by side

**Arm A -- inertial-ballistic (reference): collapses, as before.**

| c | D=2 | D=4 | D=8 | D=14 | |
|---|---|---|---|---|---|
| 0.5 | 4.41 | 8.33 | 11.47 | 11.82 | tracks D (resolves the full feature space) |
| 2.0 | 1.82 | 1.84 | 1.87 | 1.92 | **D-independent collapse** (mean 1.86, range 0.10) |

**Arm B -- native-attention (the test): no collapse; near-chain at every setting.**

| tau | D=2 | D=4 | D=8 | D=14 |
|---|---|---|---|---|
| 0.5 | 1.64 | 1.80 | 1.74 | 1.85 |
| 1.0 | 1.61 | 1.46 | 1.50 | 1.53 |
| 2.0 | 1.58 | 1.56 | 1.56 | 1.47 |
| 4.0 | 1.65 | 1.46 | 1.49 | 1.63 |

The native attention arm is stuck at `d_hat ~ 1.5-1.85` for **every** D and **every** tau. It never
resolves a D-dimensional spatial spread (no "tracks-D" regime at any knob), and there is no collapse
*transition* -- so the frozen collapse criterion is not met. Content-based attention with the "above-
uniform-attention" causal relation produces a **near-chain temporal order**, not a tunable manifold-like
geometry: each record attends to a few recent records, giving a mostly-timelike (chain-leaning) causet
with no spacelike structure to resolve or collapse.

## What this settles

The collapse that looked like "geometry emerging from records" in the prior sweep came from the imposed
**constant-velocity (inertial) worldlines** -- most of Minkowski's structure -- not from the records'
own relational content. When that inertial scaffolding is removed and the causal structure is taken from
a genuinely native process (content-based attention), the geometry does not appear: the causet is
near-chain, D-independent only in the trivial sense of being degenerate at all D.

**So records-as-rows, in its genuinely-native (attention) form, does NOT generate spacetime geometry.**
The geometry lane of the frame is a reinterpretation, not a generator. The finite S1 route stays closed
for a demonstrated, principled reason: the one native rule tested (autoregressive content attention) is
not a finality-native geometry generator -- it yields temporal order, not spacelike structure.

## Honest scope of the negative

- This falsifies the tested native rule (content-attention + above-uniform-threshold causal mask), not
  every conceivable native rule. A different native construction that manufactures genuine spacelike
  (spatial-spread) structure from record content -- not just temporal order -- could in principle
  collapse; this one does not. The honest missing object (T526) is now sharper still: a native rule that
  produces *spacelike* structure, which content attention does not.
- The ballistic collapse is real but inertial; its value (~1.86) is a crossover, and (per the prior
  results) importing inertial motion is importing Minkowski. So the ballistic arm is not an independent
  generator either.
- Screen grade; ordering fraction is one necessary-not-sufficient statistic; the diamond-MM decision
  rides on D-independence (bias-cancelling across arms), with slab-MM validating the instrument.

## Net (the geometry lane, concluded)

- **records-as-rows is a reinterpretation, not a generator, for the geometry lane.** The dimensional
  collapse requires imported inertial structure; native content-attention gives near-chain temporal
  order, no manifold-like geometry. Clean, decisive negative.
- S1 stays `requires_added_assumption`; the finite route stays closed, now for a demonstrated reason.
- The T526 generator gap is sharpened, not closed: a *spacelike-structure-producing* native rule is the
  named missing object.
- The chirality (Nielsen-Ninomiya) lane is unaffected but now sits without a validated native geometry
  to stand on -- the domain-wall reading remains an analogy, as flagged.

## Not claimed

Not a proof that no native rule can generate geometry -- only that the tested content-attention rule does
not, and that the prior collapse was inertial. Not a spacetime derivation, metric, or S1 movement. A
decisive screen-grade negative with a validated instrument and a predeclared criterion.
