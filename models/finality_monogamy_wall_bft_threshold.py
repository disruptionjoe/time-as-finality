"""FINALITY -- the monogamy wall vs the BFT 2/3 threshold: a falsification check (T517).

Resolves prospecting corner 4 of
explorations/lane-status-and-adjacent-space-prospecting-2026-07-09.md
("worth one check"): the qubit 2-shareability wall is 2/3, and classical
Byzantine fault tolerance needs > 2/3 honest nodes. Is this a shared monogamy
structure, or a parametrization coincidence?

The stated correspondence, made precise and tested:
  H(structural): the 2-shareability wall equals the BFT honest-fraction
                 threshold 2/3 because monogamy of entanglement *is* the
                 structural cause of fault-tolerance bounds. If so, the wall
                 should track the BFT constant, not drift.

We use the certified closed form (T516) F_share(d) = (d+1)/(2d), and its
visibility form v_share(d) = (d+2)/(2(d+1)) [derived below], both confirmed by
POCS. Then we confront H(structural) with what the wall actually does.

Verdict preview: SHUT as stated. The 2/3 is a d=2 single-parametrization
coincidence; the wall drifts to 1/2 while the BFT threshold is pinned at 2/3,
and the two 2/3's are functions of different variables (local dimension d at
fixed 2 shares, vs party count n at fixed local structure).

Run: python -m models.finality_monogamy_wall_bft_threshold   (exit 0)
"""
from __future__ import annotations

from fractions import Fraction

from models.finality_ladder_qudit import is_2_shareable, isotropic

FAIL: list[str] = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def F_share(d):
    """Certified isotropic 2-shareability wall in singlet fraction (T516)."""
    return Fraction(d + 1, 2 * d)


def v_share(d):
    """Same wall in visibility v, with rho = v|Phi><Phi| + (1-v) I/d^2.

    v = (d^2 F - 1)/(d^2 - 1). Substituting F = (d+1)/2d gives (d+2)/(2(d+1))."""
    F = F_share(d)
    return (d * d * F - 1) / Fraction(d * d - 1)


def main():
    print("#" * 100)
    print("# FINALITY -- monogamy wall vs BFT 2/3 threshold (falsification check, T517)")
    print("#" * 100)

    # ---- [0] confirm the two closed forms agree, and v_share(d) reduces as claimed ----
    print("\n[0] closed forms")
    for d in range(2, 7):
        check(f"v_share(d) = (d+2)/(2(d+1)) at d={d}", v_share(d) == Fraction(d + 2, 2 * (d + 1)),
              f"{v_share(d)} vs {Fraction(d + 2, 2 * (d + 1))}")

    # ---- [1] the coincidence, stated precisely ----
    print("\n[1] the datum FOR the coincidence")
    check("qubit shareability wall in visibility is EXACTLY 2/3 (v_share(2) = 2/3)",
          v_share(2) == Fraction(2, 3), f"v_share(2)={v_share(2)}")
    print(f"      v_share(2) = {v_share(2)} = 2/3, and classical BFT needs > 2/3 honest nodes. So at d=2,")
    print("      in the visibility parametrization, the numbers coincide.")

    # ---- [2] the data AGAINST: the wall drifts, BFT does not ----
    print("\n[2] the data AGAINST a STRUCTURAL correspondence")
    walls_v = [(d, v_share(d)) for d in range(2, 9)]
    print("      d : v_share(d) = (d+2)/2(d+1)")
    for d, v in walls_v:
        print(f"      {d} : {float(v):.4f} = {v}")
    check("the wall DRIFTS with d (monotone decreasing), while BFT 2/3 is d-independent",
          all(walls_v[i + 1][1] < walls_v[i][1] for i in range(len(walls_v) - 1)))
    check("the wall -> 1/2 as d -> infinity, NOT 2/3 (so it does not track the BFT constant)",
          abs(float(v_share(100_000)) - 0.5) < 1e-4 and float(v_share(100_000)) < 2.0 / 3.0)
    check("the QUTRIT wall does not land on 2/3 (matches the note's datum): v_share(3)=5/8=0.625",
          v_share(3) == Fraction(5, 8), f"v_share(3)={v_share(3)}")
    check("in the OTHER natural parametrization the coincidence lands at a DIFFERENT d "
          "(F_share(3)=2/3, not F_share(2)) -- parametrization-dependent, a coincidence signature",
          F_share(3) == Fraction(2, 3) and F_share(2) != Fraction(2, 3),
          f"F_share(2)={F_share(2)}, F_share(3)={F_share(3)}")

    # ---- [3] independent POCS confirmation that the walls are where the closed form says ----
    print("\n[3] independent POCS confirmation of the walls (so the falsification rests on real walls)")
    for d in (2, 3, 4):
        cf = float(F_share(d))
        below = is_2_shareable(isotropic(cf - 0.03, d), d)
        above = is_2_shareable(isotropic(cf + 0.03, d), d)
        check(f"d={d}: isotropic is shareable just below (d+1)/2d and un-shareable just above",
              below and not above, f"F_share={cf:.3f}")

    print("\n[4] axis mismatch (the structural kill)")
    print("      2-shareability fixes the number of shares at 2 and varies the LOCAL DIMENSION d.")
    print("      BFT fixes the local structure and varies the PARTY COUNT n (threshold n > 3f).")
    print("      The two '2/3's are values of functions of DIFFERENT variables; equating them at d=2")
    print("      is not a shared structure. The genuine monogamy<->secret-sharing bridge (access")
    print("      structures) survives elsewhere; THIS specific numerical bridge does not.")

    print("\n[verdict]  SHUT as stated (falsified as a structural correspondence).")
    print("  * The qubit wall really is 2/3 (in visibility), but that is a d=2, single-parametrization")
    print("    coincidence: the wall drifts as (d+2)/2(d+1) -> 1/2, the qutrit wall is 5/8 not 2/3, and")
    print("    the coincidence even moves to a different d under the fidelity parametrization.")
    print("  * The BFT 2/3 is a party-count/fault ratio (n>3f); the shareability 2/3 is a fixed-2-share")
    print("    local-dimension value. Different objects -- no shared monogamy structure is earned.")
    print("  * Preserved as a labeled negative result. The monogamy<->access-structure bridge is untouched.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = monogamy-wall <-> BFT-2/3 correspondence falsified as structural; kept as coincidence.")


if __name__ == "__main__":
    main()
