"""Records-as-rows: the RNG-ensemble Monte Carlo confirmation of the T126 finite-sample-artifact finding.

The deterministic-Weyl probe (`records_as_rows_attention_causet_screen.py`) found that T126's
`order_dimension_obstruction` flips PASS->REJECT as a single low-discrepancy 1+1 light-cone sprinkle
grows, WHILE its ordering fraction converges toward the manifold-like 1/2 -- backwards for a genuine
manifoldlikeness wall. That probe's own stated limit: it used a DETERMINISTIC sprinkle, not a true RNG
ensemble, so the flip could in principle be a lattice/quasirandom artifact rather than a property of
genuine sprinklings.

THIS script closes that gap. It runs a proper seeded random-sprinkle Monte Carlo: for each N, draw many
GENUINE random 1+1 Minkowski sprinkles (points ~ Uniform in null coordinates; i<j iff u_i<u_j and
v_i<v_j -- the gold-standard manifold-like causal set), audit each with the EXISTING TaF causal-set
machinery, and measure the fraction that T126 rejects SPECIFICALLY via `order_dimension_obstruction`
(the precedence-first classification, so the rejection is attributed to that leg and not another).

THE QUESTION (pre-registered): as N grows, genuine 1+1 sprinkles become MORE manifold-like (mean
ordering fraction -> 1/2). If T126's order-dimension leg were a true manifoldlikeness wall, its
rejection rate on genuine sprinkles should FALL (or stay ~0). If it is a finite-sample REGULARITY
artifact, its rejection rate should RISE toward 1 -- because natural interval-profile fluctuation (the
expected statistical spread of Alexandrov intervals) grows with N. A rising rejection rate on
increasingly-manifold-like input CONFIRMS the artifact reading and means TaF's S1 / T223 T126-leg needs
a continuum-statistics replacement.

Seeded (reproducible) yet genuinely random ensemble -- distinct from the deterministic Weyl probe.
Screen grade only: NOT a dimension estimator, embedding theorem, continuum result, or spacetime
derivation. Uses the repo audit unmodified.

Run: python -m models.records_as_rows_sprinkle_montecarlo
"""
from __future__ import annotations

import random

from models.finality_colimit_causal_set_embeddability import (
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    non_strict_relation,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    deterministic_flat_interval_control,
)

SEED = 20260710
SAMPLES = 50
NS = (8, 10, 12, 14, 16)

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def random_sprinkle(rng: random.Random, n: int) -> dict[str, tuple[float, float]]:
    """A genuine random 1+1 Minkowski sprinkle in null coordinates (u, v) ~ Uniform(0,1)^2.

    Distinct u and v values (ties have measure zero; we resample the rare collision) so the induced
    order is a clean 2D poset. This is the standard sprinkling of the causal-set literature.
    """
    while True:
        pts = {f"r{i}": (rng.random(), rng.random()) for i in range(n)}
        us = [u for u, _ in pts.values()]
        vs = [v for _, v in pts.values()]
        if len(set(us)) == n and len(set(vs)) == n:
            return pts


def lightcone_datum(pts: dict[str, tuple[float, float]]) -> FinalityColimitCausetDatum:
    strict = [
        (a, b)
        for a in pts
        for b in pts
        if a != b and pts[a][0] < pts[b][0] and pts[a][1] < pts[b][1]
    ]
    events = frozenset(pts)
    return FinalityColimitCausetDatum(
        name=f"rng_lightcone_N{len(pts)}",
        events=events,
        relation=non_strict_relation(events, frozenset(strict)),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="genuine random 1+1 Minkowski sprinkle",
    )


def audit_one(pts) -> tuple[float, str, bool]:
    a = audit_finality_colimit_causet(lightcone_datum(pts))
    frac = float(a.diagnostics.comparable_fraction) if a.diagnostics is not None else float("nan")
    return frac, a.classification, a.manifold_filter_passed


def main() -> None:
    print("[records-as-rows MC] genuine random 1+1 sprinkles vs the T126 order-dimension leg\n")
    rng = random.Random(SEED)

    rows = []
    for n in NS:
        fracs, od_reject, passed, other = [], 0, 0, 0
        for _ in range(SAMPLES):
            frac, cls, ok = audit_one(random_sprinkle(rng, n))
            fracs.append(frac)
            if ok:
                passed += 1
            elif cls == "order_dimension_obstruction":
                od_reject += 1
            else:
                other += 1
        mean_frac = sum(fracs) / len(fracs)
        rows.append((n, mean_frac, od_reject / SAMPLES, passed / SAMPLES, other / SAMPLES))

    print(f"  {'N':>3}  {'mean_frac':>9}  {'OD_reject':>9}  {'pass':>6}  {'other_rej':>9}")
    for n, mf, odr, pr, orj in rows:
        print(f"  {n:>3}  {mf:>9.3f}  {odr:>9.2%}  {pr:>6.2%}  {orj:>9.2%}")

    mean_fracs = [r[1] for r in rows]
    od_rates = [r[2] for r in rows]

    # Control: the repo's own hand-tuned flat control still passes T126 (small-N, no profile spread).
    ctrl = audit_finality_colimit_causet(deterministic_flat_interval_control())
    print()
    check("repo 6-point flat control still PASSES T126 (calibration anchor)",
          ctrl.manifold_filter_passed is True,
          f"class={ctrl.classification}")
    # DISCLOSURE (pre-registration correction, 2026-07-10): the first-run version of this check expected
    # the mean ordering fraction to START away from 1/2 and CONVERGE to it. That misjudged the statistic:
    # a uniform-square 1+1 sprinkle has P(comparable) = P(i<j both coords) + P(i>j both) = 1/4 + 1/4 = 1/2
    # at EVERY N, so it sits in the manifold-like band throughout, not "converging" from elsewhere. The
    # correct manifold-likeness condition -- and the relevant one -- is that every N sits in the repo's
    # Myrheim-Meyer 1+1 band (1/2 +/- 1/10). That the sprinkles are manifold-like at ALL N while
    # order-dimension rejection still climbs is a STRONGER form of the artifact finding, not a weaker one.
    check("genuine random sprinkles are manifold-like at EVERY N (mean ordering fraction in the 1+1 band 1/2 +/- 1/10)",
          all(abs(mf - 0.5) <= 0.1 for mf in mean_fracs),
          f"mean_frac by N: {[round(mf, 3) for mf in mean_fracs]} (all within 1/2 +/- 1/10)")
    check("order_dimension rejection rate RISES with N on genuine sprinkles",
          od_rates[-1] > od_rates[0],
          f"OD_reject {od_rates[0]:.2%} (N={NS[0]}) -> {od_rates[-1]:.2%} (N={NS[-1]})")
    check("at the largest N, order_dimension rejects a MAJORITY of genuine 1+1 sprinkles",
          od_rates[-1] >= 0.5,
          f"OD_reject at N={NS[-1]}: {od_rates[-1]:.2%}")
    check("the rise is MONOTONE non-decreasing across the sweep (not a single-N fluke)",
          all(od_rates[i] <= od_rates[i + 1] + 1e-9 for i in range(len(od_rates) - 1)),
          f"OD rates: {[round(r, 3) for r in od_rates]}")

    print("\n[verdict]")
    if not FAIL:
        print("  * CONFIRMED (RNG ensemble): T126's order_dimension_obstruction rejects a RISING fraction")
        print("    of GENUINE random 1+1 sprinkles as N grows -- while those sprinkles are manifold-like at")
        print("    EVERY N (mean ordering fraction in the 1+1 band 1/2 +/- 1/10 throughout). A true")
        print("    manifoldlikeness wall would reject FEWER manifold-like objects as they scale, not more.")
        print("    This upgrades the deterministic-Weyl finding to a proper random ensemble: the")
        print("    order-dimension leg measures finite interval-profile REGULARITY, which genuine")
        print("    manifold-like sprinklings statistically VIOLATE.")
        print("  * Consequence for TaF: the S1 / T223 reading that leans on this leg is measuring, in part,")
        print("    diagnostic irregularity rather than non-manifoldness. S1's T126-based leg is a candidate")
        print("    for a continuum-statistics replacement (a dimension estimator with declared tolerance).")
        print("    Does NOT overturn T223's separate n=8 survivor-fraction leg.")
        print("  * Screen grade; one leg; NOT a manifoldlikeness proof, dimension estimate, or metric.")
    else:
        print(f"  * NOT confirmed by the RNG ensemble on this sweep: {FAIL}")
        print("  * The deterministic-Weyl flip did NOT reproduce as a rising rejection rate on genuine")
        print("    random sprinkles -- so the artifact reading is weakened, and T126's order-dimension leg")
        print("    behaves more like a genuine (if noisy) screen than a pure finite-sample artifact.")
        print("    Report the observed rates honestly; do NOT re-scope S1 on this evidence.")

    if FAIL:
        print(f"\nNOTE: {len(FAIL)} pre-registered expectation(s) unmet -- the honest outcome is printed above.")
        # A pre-registered expectation being unmet is a real (informative) result, not a script error.
    print("\nexit 0 (ensemble complete; verdict above reflects the data either way).")


if __name__ == "__main__":
    main()
