"""Myrheim-Meyer continuum dimension estimator: the principled S1 manifoldlikeness statistic
T524/T525 named but did not build.

Context. T524 showed T126's `order_dimension_obstruction` rejects genuine random 1+1 sprinkles as a
finite interval-profile-regularity artifact (independently reproduced by
`records_as_rows_sprinkle_montecarlo.py`). T525 built a *repaired* S1 suite that QUARANTINES that leg
and replaces it with an EMPIRICAL ENVELOPE -- "is the candidate's ordering fraction / height / width /
largest-interval inside the seeded 1+1 sprinkle band?" Both explicitly disclaim a *dimension estimate*.

This module supplies the missing principled object: the Myrheim-Meyer ordering-fraction dimension
estimator. Instead of asking "is the ordering fraction inside the empirical 2D band?" it READS OUT a
continuum Minkowski dimension from the ordering fraction and reports a tolerance -- so a candidate can be
placed at an estimated dimension (a chain reads ~1, a 1+1 sprinkle ~2, a 3+1 sprinkle ~4) rather than
merely inside-or-outside one band.

The Myrheim-Meyer relation. For a Poisson sprinkling into a d-dimensional Alexandrov interval (causal
diamond) of d-dim Minkowski, the expected fraction of RELATED (causally comparable) pairs is

    f(d) = Gamma(d+1) * Gamma(d/2) / ( 2 * Gamma(3d/2) ),

monotone strictly decreasing in d, with f(1)=1 (a chain: all pairs related), f(2)=1/2, f(3)=0.2286...,
f(4)=1/10. Inverting f gives the Myrheim-Meyer dimension. The ordering fraction here uses the SAME
convention as the repo audit's `comparable_fraction` (related unordered pairs / C(N,2)), so estimates
compose directly with the existing causal-set pipeline. The closed form is validated below against
direct numerical sprinklings in d = 2, 3, 4 (measured f must match f(d) and the estimator must recover
the input dimension on held-out seeds).

Screen grade. The ordering fraction is ONE continuum statistic; agreement d_hat ~ 2 is NECESSARY but
not sufficient for manifoldlikeness (distinct posets can share an ordering fraction). This is not an
embedding theorem, metric reconstruction, or spacetime derivation, and it does not by itself promote or
reopen S1.

Run: python -m models.myrheim_meyer_dimension_estimator
"""
from __future__ import annotations

import math
import random
from itertools import combinations

from models.finality_colimit_causal_set_embeddability import audit_finality_colimit_causet
from models.myrheim_meyer_ordering_fraction_screen import deterministic_flat_interval_control
from models.t249_larger_t54_t126_colimit import run_t249_analysis
from models.t252_t255_nine_event_ordinal_controls import run_t252_analysis

SEED = 20260710
FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---- the Myrheim-Meyer relation (closed form) ---------------------------------------------------

def mm_ordering_fraction(d: float) -> float:
    """Expected related-pair fraction for a d-dim Minkowski Alexandrov-interval sprinkling."""
    return math.gamma(d + 1) * math.gamma(d / 2) / (2 * math.gamma(1.5 * d))


def estimate_dimension(f: float, lo: float = 0.5, hi: float = 12.0) -> float:
    """Invert the monotone-decreasing MM relation: solve mm_ordering_fraction(d) = f for d."""
    if f >= mm_ordering_fraction(lo):
        return lo
    if f <= mm_ordering_fraction(hi):
        return hi
    for _ in range(200):  # bisection; mm is strictly decreasing on [lo, hi]
        mid = 0.5 * (lo + hi)
        if mm_ordering_fraction(mid) > f:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---- direct numerical sprinkling (ground-truth validation of the closed form) -------------------

def diamond_sprinkle(d: int, n: int, rng: random.Random) -> list[tuple[float, ...]]:
    """n uniform points in the d-dim causal diamond I(0, e_t): |x_space| < min(t, 1-t), t in (0,1)."""
    pts: list[tuple[float, ...]] = []
    while len(pts) < n:
        t = rng.random()
        space = [rng.uniform(-0.5, 0.5) for _ in range(d - 1)]
        r = math.sqrt(sum(s * s for s in space))
        if r < min(t, 1.0 - t):
            pts.append((t, *space))
    return pts


def measured_ordering_fraction(points: list[tuple[float, ...]]) -> float:
    """Fraction of causally related pairs: y in future of x iff dt > |dx_space| (timelike/null)."""
    related = 0
    total = 0
    for a, b in combinations(points, 2):
        total += 1
        dt = abs(a[0] - b[0])
        dspace = math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(1, len(a))))
        if dt > dspace:
            related += 1
    return related / total if total else 0.0


def calibrate_measured(d: int, n: int, seeds: int, rng: random.Random) -> tuple[float, float]:
    """Mean and half-spread of the measured ordering fraction over `seeds` sprinklings at dim d."""
    vals = [measured_ordering_fraction(diamond_sprinkle(d, n, rng)) for _ in range(seeds)]
    mean = sum(vals) / len(vals)
    return mean, 0.5 * (max(vals) - min(vals))


# ---- main ---------------------------------------------------------------------------------------

def main() -> None:
    print("[MM dimension estimator] the principled continuum statistic T525's envelope lacked\n")
    rng = random.Random(SEED)

    # 1. Closed-form landmarks.
    print("  closed-form MM ordering fraction f(d):")
    for d in (1, 2, 3, 4):
        print(f"    f({d}) = {mm_ordering_fraction(float(d)):.4f}   (estimate_dimension inverts -> "
              f"{estimate_dimension(mm_ordering_fraction(float(d))):.3f})")
    check("closed form hits the known landmarks f(1)=1, f(2)=1/2, f(4)=1/10",
          abs(mm_ordering_fraction(1) - 1.0) < 1e-9
          and abs(mm_ordering_fraction(2) - 0.5) < 1e-9
          and abs(mm_ordering_fraction(4) - 0.1) < 1e-9)
    check("the estimator inverts the closed form (recovers d from f(d)) for d=2,3,4",
          all(abs(estimate_dimension(mm_ordering_fraction(d)) - d) < 1e-3 for d in (2.0, 3.0, 4.0)))

    # 2. Ground-truth validation: direct sprinklings must match the closed form AND be recovered.
    print("\n  direct-sprinkle validation (N=120, 24 seeds/dim); measured f vs closed form; recovered d:")
    ok_recover = True
    for d in (2, 3, 4):
        mean_f, spread = calibrate_measured(d, 120, 24, rng)
        d_hat = estimate_dimension(mean_f)
        d_lo, d_hi = estimate_dimension(mean_f + spread), estimate_dimension(mean_f - spread)
        recovered = abs(d_hat - d) <= 0.25
        ok_recover = ok_recover and recovered
        print(f"    d={d}: measured f={mean_f:.4f} (cf closed {mm_ordering_fraction(d):.4f}); "
              f"d_hat={d_hat:.2f} in [{d_hi:.2f},{d_lo:.2f}]  {'ok' if recovered else 'MISS'}")
    check("direct Minkowski sprinklings recover their own dimension within +/-0.25 (self-validation)",
          ok_recover)

    # 3. Apply to the exact objects the S1 story cares about.
    print("\n  applied to S1-relevant candidates (ordering fraction -> estimated dimension):")
    rng2 = random.Random(SEED + 1)
    # genuine random 1+1 sprinkles: the objects order_dimension wrongly rejected -- must read ~2.
    rand_fs = [measured_ordering_fraction(diamond_sprinkle(2, 96, rng2)) for _ in range(24)]
    rand_mean = sum(rand_fs) / len(rand_fs)
    rand_dhat = estimate_dimension(rand_mean)
    print(f"    genuine random 1+1 sprinkle (N=96, 24 seeds): f={rand_mean:.4f} -> d_hat={rand_dhat:.2f}")

    # the finite finality-colimit witnesses S1 hangs on (deterministic ordering fractions from the repo audit).
    t249 = run_t249_analysis().t126_audit
    t252 = run_t252_analysis().t126_audit
    witnesses = []
    for name, audit in (("t249_grid_colimit", t249), ("t252_ordinal_band", t252)):
        f = float(audit.diagnostics.comparable_fraction)
        witnesses.append((name, f, estimate_dimension(f), audit.classification))
        print(f"    {name}: f={f:.4f} -> d_hat={estimate_dimension(f):.2f}  "
              f"(repo T126 class: {audit.classification})")

    # a pure chain control (attend-to-all masking = 1D): f -> 1 -> d_hat ~ 1.
    chain = [(float(i),) for i in range(40)]
    chain_f = measured_ordering_fraction(chain)
    print(f"    pure chain (attend-all / 1D control, N=40): f={chain_f:.4f} -> "
          f"d_hat={estimate_dimension(chain_f):.2f}")

    check("genuine random 1+1 sprinkles read as manifold-like dimension d_hat in [1.75, 2.25]",
          1.75 <= rand_dhat <= 2.25,
          f"d_hat={rand_dhat:.2f} -- the objects order_dimension wrongly rejected now PASS a principled test")
    check("the pure chain (attend-all 1D control) reads as d_hat ~ 1, not 2 (estimator discriminates)",
          estimate_dimension(chain_f) <= 1.15,
          f"chain d_hat={estimate_dimension(chain_f):.2f}")
    check("the repo flat 6-point control's ordering fraction reads near d=2 (calibration anchor)",
          1.5 <= estimate_dimension(
              float(audit_finality_colimit_causet(deterministic_flat_interval_control())
                    .diagnostics.comparable_fraction)) <= 2.6)

    # 4. The S1 read-out: does the principled estimator support T525's practical conclusion?
    witness_dims = [w[2] for w in witnesses]
    print("\n[verdict]")
    print("  * The Myrheim-Meyer ordering-fraction dimension estimator is validated: it recovers the")
    print("    dimension of true Minkowski sprinklings (d=2,3,4) within +/-0.25, and it reads genuine")
    print(f"    random 1+1 sprinkles as d_hat={rand_dhat:.2f} -- so the manifold-like objects that T126's")
    print("    order_dimension leg wrongly REJECTED now PASS a principled continuum statistic. This is the")
    print("    replacement T524/T525 named (they quarantined the bad leg; this reads out a dimension).")
    print("  * The finite finality-colimit witnesses S1 hangs on read as:")
    for name, f, dh, cls in witnesses:
        print(f"      {name}: d_hat={dh:.2f}")
    print("    (ordering fraction is ONE statistic -- necessary, not sufficient; a witness near d_hat=2")
    print("    is not thereby manifold-like, but a witness FAR from 2 is positively disqualified.)")
    print("  * S1 status: unchanged (requires_added_assumption). This STRENGTHENS the diagnostic basis")
    print("    beyond T525's empirical envelope -- genuine sprinkles pass a principled dimension read-out,")
    print("    so the S1 conclusion no longer leans on any leg that punishes real sprinkles for")
    print("    fluctuating. Does NOT reopen/promote S1 and does NOT touch T223's n=8 survivor leg.")
    print("  * NOT CLAIMED: embedding, metric reconstruction, locality, covariance, continuum limit, or")
    print("    that a single ordering-fraction dimension match establishes manifoldlikeness.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print(f"\nexit 0 = MM dimension estimator validated and applied "
          f"(random sprinkles d_hat={rand_dhat:.2f}; witnesses d_hat={[round(x,2) for x in witness_dims]}).")


if __name__ == "__main__":
    main()
