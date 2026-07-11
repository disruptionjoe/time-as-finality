# A Myrheim-Meyer continuum dimension estimator for S1: the principled statistic the repair suite lacked

2026-07-10. Computed finding, screen grade. Model: `models/myrheim_meyer_dimension_estimator.py`
(exit 0, 6/6 checks, seeded/reproducible). Extends the S1 causal-set lineage
(T126 -> T156 -> T223 -> T524 -> T525 -> T526) with the one object all of them explicitly disclaimed:
a continuum **dimension estimate**. Status impact: **none** -- S1 stays `requires_added_assumption`.

## Why this exists (honest lineage)

The records-as-rows reframe's geometry leg was tested by confronting T223. The chain of prior work:

- **T223** closed the "enumerate finite finality-colimits and hope manifoldlikeness emerges" route,
  and its own disclaimer states it earns "no ... Myrheim-Meyer dimension estimate."
- **T524** found T126's `order_dimension_obstruction` rejects genuine random 1+1 sprinkles as a finite
  interval-profile-regularity artifact. (This exploration's sibling
  `records_as_rows_sprinkle_montecarlo.py` independently reproduced T524's finding from the
  records-as-rows side -- an independent corroboration, not a new discovery; T524 predates it.)
- **T525** built a repaired suite that QUARANTINES the bad leg and replaces it with an EMPIRICAL
  ENVELOPE (is the candidate's ordering fraction / height / width / largest-interval inside the seeded
  1+1 sprinkle band?).
- **T526** showed even that repaired suite is passable only by an external reference law that imports
  Lorentzian u/v coordinates, and named the real missing object: a finality-native generator.

T524 and T525 both explicitly disclaim a *dimension estimate*. This note supplies it.

## What was built and validated

The **Myrheim-Meyer ordering-fraction dimension estimator**. For a Poisson sprinkling into a
d-dimensional Minkowski Alexandrov interval, the expected fraction of causally related pairs is

```
f(d) = Gamma(d+1) * Gamma(d/2) / ( 2 * Gamma(3d/2) )    (strictly decreasing in d)
```

with `f(1)=1` (a chain: all pairs related), `f(2)=1/2`, `f(3)=0.2286...`, `f(4)=1/10`. Inverting `f`
returns a continuum dimension. The ordering fraction uses the SAME convention as the repo audit's
`comparable_fraction` (related pairs / C(N,2)), so it composes with the existing pipeline.

**Validation (formula-independent ground truth).** Direct numerical sprinklings into true d-dim causal
diamonds (N=120, 24 seeds) recover their own dimension:

| input d | measured f | closed-form f(d) | recovered d_hat |
|---|---|---|---|
| 2 | 0.5042 | 0.5000 | **1.99** |
| 3 | 0.2330 | 0.2286 | **2.98** |
| 4 | 0.0994 | 0.1000 | **4.01** |

All within +/-0.25. The estimator is not a fitted curve; the closed form is validated against genuine
sprinklings and recovers the input dimension.

## The application to S1

| candidate | ordering fraction | estimated dimension d_hat |
|---|---|---|
| genuine random 1+1 sprinkle (N=96, 24 seeds) | 0.4995 | **2.00** |
| pure chain (attend-all / 1D control) | 1.0000 | **1.00** |
| T249 grid finality-colimit witness | 0.7500 | **1.44** |
| T252 ordinal finality-colimit witness | 0.5556 | **1.86** |

Two things fall out, both honest:

1. **The artifact is repaired at the principled level.** The genuine random 1+1 sprinkles that T126's
   order-dimension leg wrongly REJECTED read as `d_hat = 2.00` -- they PASS a principled continuum
   statistic. The estimator also discriminates (a chain reads 1.00, not 2), so this is a real screen,
   not a rubber stamp.
2. **The S1 witnesses are positively disqualified at the wrong effective dimension.** The finite
   finality-colimit witnesses S1 hangs on read `d_hat = 1.44` (T249 grid) and `1.86` (T252 ordinal) --
   below manifold-like 2D. T525 already rejected them via its empirical envelope; the MM estimator
   upgrades that to an interpretable statement: they sit at the wrong *dimension*, not merely outside a
   band. (Ordering fraction is ONE statistic -- necessary, not sufficient: a witness near `d_hat = 2` is
   not thereby manifold-like, but one far from 2 is disqualified. T249 at 1.44 is far.)

## Net effect on S1 (status unchanged)

S1 remains `requires_added_assumption`. This **strengthens the diagnostic basis** beyond T525's
empirical envelope: the S1 finite-route conclusion no longer leans on any leg that punishes genuine
sprinkles for fluctuating (T524's artifact), AND the current witnesses now fail a principled,
dimension-valued, validated statistic -- not just an empirical band. It does **not** reopen, promote, or
reverse anything, and it does **not** touch T223's separate n=8 survivor-fraction leg.

## Honest caveat (the T526 gap is untouched)

Like T526's reference law, this estimator is **Lorentzian-calibrated** -- its ground truth is Minkowski
sprinklings, importing exactly the u/v/metric structure T526 flagged. It improves the SCREEN, not the
GENERATOR. The real missing object T526 identified -- a finality-native generator that produces finite
causets without Lorentzian coordinates as primitives and yields `d_hat ~ 2` witnesses -- remains
unbuilt. A better ruler does not supply the thing to be measured.

## Not claimed

Not an embedding theorem, metric reconstruction, locality/covariance result, continuum limit, or
spacetime derivation. A single ordering-fraction dimension match is necessary, not sufficient, for
manifoldlikeness. Screen grade; one continuum statistic; no claim-ledger movement.
