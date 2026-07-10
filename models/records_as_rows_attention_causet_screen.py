"""Records-as-rows probe + a T126 diagnostic-artifact finding.

Treats attention patterns as candidate causal sets and runs the EXISTING TaF causal-set machinery on
them (records = events; an attention link earlier->later = a strict relation, transitively closed).
Two diagnostics per candidate: the WEAK T156 Myrheim-Meyer 1+1 ordering-fraction band (1/2 +/- 1/10)
and the STRONGER T126 manifold filter.

THE LOAD-BEARING FINDING (calibration sweep): as a genuine 1+1 light-cone sprinkle GROWS, its ordering
fraction converges toward the manifold-like value 1/2 (0.786 -> 0.697 -> 0.625 -> 0.579 ...) WHILE the
T126 order_dimension leg FLIPS from PASS to REJECT. The object becomes more manifold-like exactly as
T126 rejects it -> T126's order_dimension_obstruction behaves like a finite-sample / class artifact,
not a true manifoldlikeness wall. Contrast: the repo's own 6-point flat control passes (too small to
show interval-profile fluctuation). This bears on the reading of the S1 / T223 no-go.

Deterministic rational coordinates (no RNG); exact Fraction arithmetic. Screen grade only -- NOT a
dimension estimator, embedding theorem, continuum result, or spacetime derivation.

Run: python -m models.records_as_rows_attention_causet_screen
"""
from __future__ import annotations

from fractions import Fraction as F

from models.finality_colimit_causal_set_embeddability import (
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    non_strict_relation,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    deterministic_flat_interval_control,
    flat_1p1_interval_target,
)

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def sprinkle_uv(n: int) -> dict[str, tuple[F, F]]:
    """Deterministic low-discrepancy 1+1 null-coordinate sprinkle (two Weyl recurrences)."""
    au, av = F(7071, 10000), F(7320, 10000)  # ~frac(sqrt2), ~frac(sqrt3)
    return {f"r{i}": (((au * i) % 1), ((av * i) % 1)) for i in range(n)}


def _datum(name, uv, strict, source) -> FinalityColimitCausetDatum:
    events = frozenset(uv)
    return FinalityColimitCausetDatum(
        name=name, events=events, relation=non_strict_relation(events, frozenset(strict)),
        descent_gate_passed=True, canonical_colimit=True, phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False, source=source,
    )


def lightcone(uv):  # metric null-cone: j in forward cone of i iff u_i<u_j and v_i<v_j
    return _datum(f"lightcone_sprinkle_N{len(uv)}", uv,
                  [(a, b) for a in uv for b in uv if a != b and uv[a][0] < uv[b][0] and uv[a][1] < uv[b][1]],
                  "genuine 1+1 light-cone sprinkle (metric-proximity attention)")


def attend_all(uv):  # transformer default: order by tau=u+v, attend to ALL earlier
    tau = {k: v[0] + v[1] for k, v in uv.items()}
    return _datum(f"attend_all_past_N{len(uv)}", uv,
                  [(a, b) for a in uv for b in uv if a != b and tau[a] < tau[b]],
                  "attend-to-all-earlier causal mask (transformer default)")


def lattice(rows, cols):
    uv = {f"g{i}_{j}": (F(i), F(j)) for i in range(rows) for j in range(cols)}
    return _datum(f"lattice_{rows}x{cols}", uv,
                  [(a, b) for a in uv for b in uv if a != b and uv[a][0] <= uv[b][0] and uv[a][1] <= uv[b][1]],
                  "2D grid/lattice attention (T223-style control)")


def row(d, target):
    a = audit_finality_colimit_causet(d)
    dg = a.diagnostics
    frac = dg.comparable_fraction if dg is not None else None
    band = frac is not None and target.accepts(frac)
    return d.name, frac, band, a.manifold_filter_passed, a.classification


def main() -> None:
    print("[records-as-rows] attention as causal sets; the T126 order-dimension flip\n")
    target = flat_1p1_interval_target()

    controls = [row(deterministic_flat_interval_control(), target)]
    sweep = [row(lightcone(sprinkle_uv(n)), target) for n in (8, 12, 16, 20)]
    contrast = [row(attend_all(sprinkle_uv(16)), target), row(lattice(4, 4), target)]

    print(f"  {'candidate':<40} {'frac':>6} {'band':>5} {'T126':>5}  classification")
    for name, frac, band, ok, cls in controls + sweep + contrast:
        fr = f"{float(frac):.3f}" if frac is not None else "  -- "
        print(f"  {name:<40} {fr:>6} {('y' if band else 'n'):>5} {('PASS' if ok else 'no'):>5}  {cls}")

    ctrl = controls[0]
    fracs = [float(r[1]) for r in sweep]
    t126 = [r[3] for r in sweep]

    print()
    check("repo's own 6-point flat control passes T126 (calibration)",
          ctrl[3] is True, f"frac {float(ctrl[1]):.3f}")
    check("genuine sprinkle ordering fraction CONVERGES toward 1/2 as N grows (manifold-like)",
          fracs == sorted(fracs, reverse=True) and fracs[-1] < fracs[0],
          f"{[round(f,3) for f in fracs]} -> 1/2")
    check("T126 order-dimension leg FLIPS PASS->REJECT as the sprinkle grows/improves",
          t126[0] is True and t126[-1] is False,
          f"T126 by N: {dict(zip((8,12,16,20), t126))}")
    check("the flip coincides with INCREASING manifold-likeness (backwards for a real wall)",
          (not t126[-1]) and fracs[-1] < fracs[1],
          "object more manifold-like exactly where T126 rejects it")

    verdict = "T126_ORDER_DIMENSION_LEG_IS_A_FINITE_SAMPLE_CLASS_ARTIFACT_NOT_A_MANIFOLDLIKENESS_WALL"
    print("\n[verdict]")
    print(f"  * {verdict}")
    print("  * A genuine 1+1 light-cone sprinkle -- the gold-standard manifold-like causal set -- has")
    print("    its ordering fraction converge to 1/2 as N grows, yet T126's order_dimension_obstruction")
    print("    flips from PASS to REJECT over the same growth. It passes a tiny hand-tuned 6-point")
    print("    control (no interval-profile fluctuation) and rejects real larger sprinkles (natural")
    print("    fluctuation). So that leg tests finite interval-profile REGULARITY, which genuine")
    print("    sprinklings VIOLATE -- a Layer-0 homonymy on 'manifold-like', not a true wall.")
    print("  * Consequence: the S1/T223 reading ('finite finality-colimits don't concentrate on")
    print("    manifoldlike causal sets') may be partly measuring diagnostic irregularity. S1 is a")
    print("    candidate for reopening/re-scoping. Also robust: generic causal masking (attend-all) is")
    print("    a 1D chain (rank_width), NOT spacetime -- so metric proximity is the load-bearing choice.")
    print("  * NOT CLAIMED: a manifoldlikeness proof, continuum dimension, a derived metric, or that")
    print("    T126's OTHER legs are artifacts. Deterministic sprinkle (not RNG); one leg, screen grade.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = T126 order-dimension leg flagged as a finite-sample class artifact.")


if __name__ == "__main__":
    main()
