"""Observerse issuance dynamics -- executes the frozen predeclared spec (P1-P4).

Spec: explorations/observerse-issuance-dynamics-PREDECLARED-SPEC-2026-07-10.md (committed first).

HONEST GRADE: this is a COMPOSITIONALITY / ILLUSTRATION test, not evidence that reality or GU works this
way. A hand-built dynamical model of the lambda*-curve (which is DEFINED to have an interior optimum)
will tend to exhibit one. The genuine content is: (a) it forces each of Joe's ingredients -- goals,
holonomy, deflation -- to be made mechanistically PRECISE; (b) it checks they COMPOSE without
contradiction into a single self-consistent infinite-game dynamics; (c) any ingredient with no honest
mechanism (or that fails to matter when built) is a real finding. Parameters are fixed once and NOT
tuned; the model is run once; whatever P1-P4 return is reported.

Run: python -m models.observerse_issuance_dynamics
"""
from __future__ import annotations

import numpy as np

# fixed implementation constants (set once, not tuned)
D = 8
K = 6
T = 150
SEEDS = 6
ALPHA = 1.0        # goal pull
BETA0 = 1.0        # base novelty
TAU = 30.0         # deflation timescale
RHO = 0.3          # reconciliation rate (coupled)
KAPPA = 0.6        # how much issuance disturbs a frame
ETA_DIRECTED = 0.35  # directed issuance disturbs the frame LESS (coherent exploration is easier to reconcile)
LAMBDAS = (0.05, 0.15, 0.4, 1.0, 2.5)
SEED = 20260710

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def _orthonormal(m: np.ndarray) -> np.ndarray:
    q, r = np.linalg.qr(m)
    return q * np.sign(np.diag(r))  # fix QR sign ambiguity for stability


def run_arm(lam: float, coupled: bool, directed: bool, deflationary: bool, seed: int):
    rng = np.random.default_rng(seed)
    goals = rng.standard_normal((K, D))
    goals /= np.linalg.norm(goals, axis=1, keepdims=True)
    frames = np.stack([_orthonormal(np.eye(D) + 0.05 * rng.standard_normal((D, D))) for _ in range(K)])
    pos = 0.1 * rng.standard_normal((K, D))

    def pairwise_C(fr):
        return float(np.mean([np.linalg.norm(fr[a] - fr[b]) for a in range(K) for b in range(a + 1, K)]))

    C0 = pairwise_C(frames)
    N_series, C_series = [], []
    for t in range(1, T + 1):
        beta_t = BETA0 / (1 + t / TAU) if deflationary else BETA0
        step_novelty = 0.0
        for k in range(K):
            g = goals[k] if directed else (lambda v: v / np.linalg.norm(v))(rng.standard_normal(D))
            fresh = rng.standard_normal(D)
            fresh /= np.linalg.norm(fresh)
            # the genuinely-novel (non-goal-predictable) component
            novel = fresh - (fresh @ g) * g
            direction = ALPHA * g + beta_t * fresh
            pos[k] = pos[k] + lam * direction
            step_novelty += lam * beta_t * np.linalg.norm(novel)
            # issuance disturbs this observer's frame; goal-directed issuance is more coherent (disturbs less)
            disturb = KAPPA * lam * beta_t * (ETA_DIRECTED if directed else 1.0)
            frames[k] = _orthonormal(frames[k] + disturb * rng.standard_normal((D, D)))
        if coupled:  # reconcile frames toward consensus (holonomy)
            consensus = _orthonormal(frames.mean(axis=0))
            for k in range(K):
                frames[k] = _orthonormal((1 - RHO) * frames[k] + RHO * consensus)
        C_t = pairwise_C(frames)
        # coherent novelty: novelty counts only while the shared structure is not fragmented
        coherent = step_novelty if C_t < 2.0 * C0 else 0.0
        N_series.append(coherent)
        C_series.append(C_t)
    return np.array(N_series), np.array(C_series), C0


def scn(N_series: np.ndarray) -> float:
    """Sustained Coherent Novelty = mean coherent novelty over the last third."""
    return float(np.mean(N_series[-(T // 3):]))


def arm_mean(lam, coupled, directed, deflationary):
    runs = [run_arm(lam, coupled, directed, deflationary, SEED + s) for s in range(SEEDS)]
    scn_v = float(np.mean([scn(n) for n, c, c0 in runs]))
    cfin = float(np.mean([c[-(T // 3):].mean() for n, c, c0 in runs]))
    c0 = float(np.mean([c0 for n, c, c0 in runs]))
    return scn_v, cfin, c0


def main() -> None:
    print("[observerse issuance dynamics] compositionality/illustration test of the lambda*-curve\n")

    # P1: interior optimum in lambda (coupled, directed, deflationary).
    print("  P1 -- SCN vs issuance rate lambda (coupled, directed, deflationary):")
    scn_by_lam = {}
    for lam in LAMBDAS:
        s, cf, c0 = arm_mean(lam, True, True, True)
        scn_by_lam[lam] = s
        print(f"    lambda={lam:<5}: SCN={s:.3f}  (mean late-C={cf:.2f}, C0={c0:.2f})")
    best_lam = max(scn_by_lam, key=scn_by_lam.get)
    interior = best_lam not in (LAMBDAS[0], LAMBDAS[-1])
    exceeds = scn_by_lam[best_lam] >= 1.25 * max(scn_by_lam[LAMBDAS[0]], scn_by_lam[LAMBDAS[-1]])
    check("P1 interior optimum: a finite lambda* beats both endpoints by >=25%",
          interior and exceeds, f"lambda*={best_lam}, SCN*={scn_by_lam[best_lam]:.3f}")

    lam_star = best_lam if interior else 0.4

    # P2: holonomy necessity (coupled vs independent) at lambda*.
    _, c_coupled, c0c = arm_mean(lam_star, True, True, True)
    _, c_indep, c0i = arm_mean(lam_star, False, True, True)
    print(f"\n  P2 -- coherence cost C at lambda*={lam_star}: coupled late-C={c_coupled:.2f} (C0={c0c:.2f}); "
          f"independent late-C={c_indep:.2f} (C0={c0i:.2f})")
    check("P2 holonomy necessity: coupled C stays bounded (<2x C0) while independent C grows (>2x C0)",
          c_coupled < 2.0 * c0c and c_indep > 2.0 * c0i,
          f"coupled {c_coupled/c0c:.1f}x, independent {c_indep/c0i:.1f}x")

    # P3: goal necessity (directed vs random) at lambda*, coupled deflationary.
    scn_dir, _, _ = arm_mean(lam_star, True, True, True)
    scn_rnd, _, _ = arm_mean(lam_star, True, False, True)
    print(f"\n  P3 -- SCN at lambda*={lam_star}: directed={scn_dir:.3f}; random={scn_rnd:.3f}")
    check("P3 goal necessity: directed SCN >= 1.25x random SCN",
          scn_dir >= 1.25 * scn_rnd if scn_rnd > 0 else scn_dir > 0,
          f"directed/random = {scn_dir/scn_rnd:.2f}x" if scn_rnd > 0 else "random collapsed to 0")

    # P4: deflationary vs constant at lambda*, coupled directed.
    scn_def, c_def, c0d = arm_mean(lam_star, True, True, True)
    scn_con, c_con, c0k = arm_mean(lam_star, True, True, False)
    print(f"\n  P4 -- at lambda*={lam_star}: deflationary SCN={scn_def:.3f} (late-C={c_def:.2f}); "
          f"constant SCN={scn_con:.3f} (late-C={c_con:.2f})")
    check("P4 deflationary sustains coherent novelty better than constant (higher SCN and/or bounded C)",
          scn_def > scn_con or (c_def < 2 * c0d <= c_con),
          f"SCN def/con = {scn_def/scn_con:.2f}x" if scn_con > 0 else "constant collapsed to 0")

    held = 4 - len(FAIL)
    print("\n[verdict]")
    print(f"  * {held}/4 predictions hold. This is a COMPOSITIONALITY/ILLUSTRATION result: it shows the")
    print("    four ingredients of Joe's reframe (issuance rate, holonomy reconciliation, goal-direction,")
    print("    deflation), each made mechanistically precise, COMPOSE into a single self-consistent")
    print("    interior-optimum infinite-game dynamics -- the lambda*-curve realized with the full nuance.")
    print("    It is NOT evidence that the observerse/GU is this way; a curve defined to have an interior")
    print("    optimum exhibits one. The honest content is that the ingredients cohere and each has a")
    print("    non-vacuous role (or, where a prediction FAILS, that that ingredient is decoration here).")
    if FAIL:
        print(f"  * Predictions that did NOT hold: {FAIL} -- reported as the honest finding, not tuned away.")
    print("  * Holography (Y14->X4) and chirality are the sequenced follow-on, not tested here.")

    print(f"\nexit 0 = compositionality test complete ({held}/4 predictions hold).")


if __name__ == "__main__":
    main()
