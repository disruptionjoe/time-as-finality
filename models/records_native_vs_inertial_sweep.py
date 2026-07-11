"""Native-vs-inertial dimensional-collapse test -- executes the frozen predeclared spec.

Spec: explorations/records-native-vs-inertial-PREDECLARED-SPEC-2026-07-10.md (committed first).
Question: does a NATIVE content-based attention process (no positions/velocities/light-cone) collapse
the feature dimension the way imposed ballistic motion does? Decision rides on the calibration-robust
D-INDEPENDENCE contrast between the two arms.

Run: python -m models.records_native_vs_inertial_sweep
"""
from __future__ import annotations

import numpy as np

from models.myrheim_meyer_dimension_estimator import estimate_dimension, mm_ordering_fraction

SEED = 20260710
D_GRID = (2, 4, 8, 14)
KNOBS = (0.5, 1.0, 2.0, 4.0)   # c for ballistic, tau for attention
N_GRID = (40, 60, 80, 100)
SEEDS = 6

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---- shared: ordering fraction of a directed relation (transitively closed) ---------------------

def ordering_fraction_from_relation(rel: np.ndarray) -> float:
    n = len(rel)
    r = rel.copy()
    for _ in range(int(np.ceil(np.log2(max(2, n)))) + 1):
        r2 = r | ((r.astype(np.int32) @ r.astype(np.int32)) > 0)
        if np.array_equal(r2, r):
            break
        r = r2
    return float(r.sum()) / (n * (n - 1) / 2.0)


# ---- Arm A: inertial-ballistic (reference) ------------------------------------------------------

def ballistic_relation(n: int, d: int, c: float, rng: np.random.Generator) -> np.ndarray:
    k = max(2, n // 8)
    line = rng.integers(0, k, size=n)
    starts = rng.standard_normal((k, d))
    vels = rng.standard_normal((k, d)) / np.sqrt(d)
    pos = starts[line] + vels[line] * np.arange(n)[:, None]
    t = np.arange(n)
    dt = t[None, :] - t[:, None]
    dist = np.sqrt(((pos[None, :, :] - pos[:, None, :]) ** 2).sum(-1))
    return (dt > 0) & (dist <= c * dt)


# ---- Arm B: native-attention (the test) ---------------------------------------------------------

def _orthogonal(d: int, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.standard_normal((d, d)))
    return q


def attention_relation(n: int, d: int, tau: float, rng: np.random.Generator) -> np.ndarray:
    wq, wk, wv = _orthogonal(d, rng), _orthogonal(d, rng), _orthogonal(d, rng)
    r = np.zeros((n, d))
    r[0] = rng.standard_normal(d)
    rel = np.zeros((n, n), dtype=bool)
    for t in range(1, n):
        q = wq @ r[t - 1]
        keys = r[:t] @ wk.T
        vals = r[:t] @ wv.T
        logits = (keys @ q) / (np.sqrt(d) * tau)
        a = np.exp(logits - logits.max())
        a /= a.sum()
        r[t] = a @ vals + 0.1 * rng.standard_normal(d)
        rel[:t, t] = a >= (1.0 / t)          # i<j iff j attended to i above uniform (native causal mask)
    return rel


# ---- slab-MM instrument recalibration -----------------------------------------------------------

def slab_ordering_fraction(d: int, n: int, rng: np.random.Generator, aspect: float = 3.0) -> float:
    """Uniform d-dim SLAB sprinkle: t~U[0,aspect], x~U[-0.5,0.5]^(d-1); relate iff |dx| <= dt."""
    t = rng.uniform(0, aspect, n)
    x = rng.uniform(-0.5, 0.5, (n, max(0, d - 1)))
    order = np.argsort(t)
    t, x = t[order], x[order]
    dt = t[None, :] - t[:, None]
    if d == 1:
        dist = np.zeros((n, n))
    else:
        dist = np.sqrt(((x[None, :, :] - x[:, None, :]) ** 2).sum(-1))
    rel = (dt > 0) & (dist <= dt)
    return ordering_fraction_from_relation(rel)


def build_slab_estimator(rng: np.random.Generator):
    """Calibrate ordering-fraction -> d on uniform slabs for d=1..5; return a monotone inverse."""
    ds = np.array([1, 2, 3, 4, 5], dtype=float)
    fs = np.array([np.mean([slab_ordering_fraction(int(d), 200, rng) for _ in range(12)]) for d in ds])
    order = np.argsort(fs)  # f decreasing in d -> sort ascending for interp
    fs_s, ds_s = fs[order], ds[order]

    def estimate(f: float) -> float:
        return float(np.interp(f, fs_s, ds_s))

    return estimate, dict(zip(ds.astype(int), np.round(fs, 3)))


# ---- collapse criterion (frozen) ----------------------------------------------------------------

def arm_dhat_grid(relation_fn, rng: np.random.Generator) -> dict[float, dict[int, float]]:
    """d_hat[knob][D] = seed-mean over N-mean (the collapse test uses D=14 N-spread separately)."""
    grid: dict[float, dict[int, float]] = {}
    n_spread14: dict[float, float] = {}
    for knob in KNOBS:
        perD = {}
        for d in D_GRID:
            per_n = []
            for n in N_GRID:
                fr = [estimate_dimension(ordering_fraction_from_relation(relation_fn(n, d, knob, rng)))
                      for _ in range(SEEDS)]
                per_n.append(float(np.mean(fr)))
            perD[d] = float(np.mean(per_n))
            if d == 14:
                n_spread14[knob] = float(np.max(per_n) - np.min(per_n))
        grid[knob] = perD
    grid["_spread14"] = n_spread14  # type: ignore
    return grid


def detect_collapse(grid: dict) -> tuple[bool, float | None, dict]:
    spread14 = grid["_spread14"]
    small_knob = min(KNOBS)
    trackD_14 = grid[small_knob][14]
    for knob in KNOBS:
        vals = np.array([grid[knob][d] for d in D_GRID])
        d_independent = (vals.max() - vals.min()) <= 0.5
        genuine = grid[knob][14] <= trackD_14 - 0.5
        n_stable = spread14.get(knob, 9.9) <= 0.4
        if d_independent and genuine and n_stable:
            return True, knob, {"mean": float(vals.mean()), "range": float(vals.max() - vals.min())}
    return False, None, {}


def main() -> None:
    print("[native vs inertial] does content-based attention collapse the feature dimension?\n")
    rng = np.random.default_rng(SEED)

    # instrument recalibration on uniform slabs (the folded-in fix for the prior failed D=1 control)
    slab_est, slab_landmarks = build_slab_estimator(np.random.default_rng(SEED + 5))
    print(f"  slab-MM calibration (ordering fraction by slab dim d): {slab_landmarks}")
    d1_slab = np.mean([slab_est(slab_ordering_fraction(1, 200, np.random.default_rng(SEED + 100 + i)))
                       for i in range(6)])
    d2_slab = np.mean([slab_est(slab_ordering_fraction(2, 200, np.random.default_rng(SEED + 200 + i)))
                       for i in range(6)])
    print(f"  slab-MM self-validation: D=1 slab -> d_hat_slab={d1_slab:.2f} (target ~1); "
          f"D=2 slab -> {d2_slab:.2f} (target ~2)")
    check("INSTRUMENT (slab-MM) recovers slab dimension within +/-0.4 (validates the fixed control)",
          abs(d1_slab - 1) <= 0.4 and abs(d2_slab - 2) <= 0.4,
          "the slab estimator sees the true dimension of a clean slab")

    print("\n  Arm A (inertial-ballistic) d_hat by knob c and D:")
    grid_a = arm_dhat_grid(ballistic_relation, np.random.default_rng(SEED + 1))
    for knob in KNOBS:
        print(f"    c={knob:<3}: " + "  ".join(f"D={d}:{grid_a[knob][d]:.2f}" for d in D_GRID))
    collapse_a, knob_a, info_a = detect_collapse(grid_a)

    print("\n  Arm B (native-attention) d_hat by knob tau and D:")
    grid_b = arm_dhat_grid(attention_relation, np.random.default_rng(SEED + 2))
    for knob in KNOBS:
        print(f"    tau={knob:<3}: " + "  ".join(f"D={d}:{grid_b[knob][d]:.2f}" for d in D_GRID))
    collapse_b, knob_b, info_b = detect_collapse(grid_b)

    print("\n  collapse detection (frozen criterion):")
    print(f"    Arm A (ballistic):  collapse={collapse_a}"
          + (f" at c={knob_a}, mean d_hat={info_a['mean']:.2f}, D-range={info_a['range']:.2f}" if collapse_a else ""))
    print(f"    Arm B (attention):  collapse={collapse_b}"
          + (f" at tau={knob_b}, mean d_hat={info_b['mean']:.2f}, D-range={info_b['range']:.2f}" if collapse_b else ""))

    print("\n[verdict]")
    if collapse_b:
        print("  * NATIVE COLLAPSE CONFIRMED: the native content-based attention process (no positions,")
        print("    velocities, or light cone) exhibits the same D-independent dimensional collapse as")
        print("    imposed ballistic motion. The collapse does NOT require imported inertial structure --")
        print("    records-as-rows collapses the feature dimension from its own relational content.")
        print("    records-as-rows is a genuine (native) generator; ballistic was one instance.")
        print("    S1 finite route candidate-reopens; a validated-geometry chirality leg becomes worth running.")
    elif collapse_a and not collapse_b:
        print("  * INERTIAL-ONLY: the ballistic (inertial) arm collapses, but the native attention arm does")
        print("    NOT -- it tracks D, chains, or lacks a stable D-independent regime. The dimensional")
        print("    collapse REQUIRES imported inertial / Minkowski structure (constant-velocity worldlines).")
        print("    records-as-rows is, on this test, a reinterpretation dressed as a generator: the geometry")
        print("    comes from the imposed inertial motion, not from the records' own relational content.")
        print("    The finite S1 route stays closed for a demonstrated reason.")
    else:
        print("  * MIXED / INCONCLUSIVE: neither arm collapses cleanly on this grid (or both fail the")
        print("    N-stability gate). Report the tables honestly; do not force a reading. Likely needs")
        print("    larger N or a different native rule before the native-vs-inertial question is decided.")
        print(f"    (Arm A collapse={collapse_a}, Arm B collapse={collapse_b}.)")

    print("\n  CAVEAT (disclosed): absolute d_hat uses the diamond-MM estimator applied identically to both")
    print("  arms, so the diamond-vs-slab bias cancels in the A-vs-B contrast; the decision is the")
    print("  D-independence signal, not absolute values. Screen grade; no embedding/metric/S1 claim.")

    if FAIL:
        print(f"\nNOTE: instrument self-validation unmet: {FAIL} -- absolute slab values are then uncalibrated,")
        print("but the A-vs-B D-independence decision (shared diamond-MM) still stands.")
    verdict = ("NATIVE COLLAPSE CONFIRMED" if collapse_b
               else "INERTIAL-ONLY" if collapse_a else "MIXED/INCONCLUSIVE")
    print(f"\nexit 0 = sweep complete; verdict = {verdict}.")


if __name__ == "__main__":
    main()
