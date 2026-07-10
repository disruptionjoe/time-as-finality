"""FINALITY -- QD redundancy / replication invariant gate (T519).

T518 confirmed a structural bridge between quantum-Darwinism redundancy and
distributed replication, but left the quantitative bridge open. Its wake
condition named one possible dimensionless invariant:

    information deficit 1 - f_delta / N

where f_delta is the smallest environment fragment carrying enough pointer
information. T519 tests that candidate against two distributed-systems readings.

Verdict preview: the invariant matches a crash-quorum survival fraction only by
choosing quorum size q = f_delta. It fails the Byzantine quorum-intersection
reading that made the distributed-systems side interesting. So this is a useful
crash-model translation, not the discovery-level invariant T518 needed.

Run: python -m models.quantum_darwinism_replication_invariant_gate
"""
from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path

import numpy as np

from models.quantum_darwinism_replication_bridge import (
    global_state,
    partial_info,
    reduced_dm,
    vn_entropy,
)

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def exact_redundancy(N: int, theta: float, delta: float) -> dict:
    """Compute f_delta by exact averaging over all same-size fragments."""
    psi = global_state(N, theta)
    hs = vn_entropy(reduced_dm(psi, N + 1, [0]))
    target = (1 - delta) * hs
    env = list(range(1, N + 1))
    curve: list[dict] = []
    f_delta = None
    for f in range(1, N + 1):
        infos = [partial_info(psi, N, frag) for frag in combinations(env, f)]
        avg = float(np.mean(infos))
        curve.append({"f": f, "avg_info": avg})
        if f_delta is None and avg >= target:
            f_delta = f
    if f_delta is None:
        f_delta = N
    return {
        "N": N,
        "theta_pi": theta / np.pi,
        "delta": delta,
        "H_S": hs,
        "f_delta": f_delta,
        "R_delta": N / f_delta,
        "info_deficit": 1 - f_delta / N,
        "curve": curve,
    }


def crash_survival_fraction(N: int, quorum_size: int) -> float:
    """Largest crash fraction that still leaves at least one read quorum."""
    return (N - quorum_size) / N


def byzantine_intersection_safe(N: int, quorum_size: int, faulty: int) -> bool:
    """Every pair of quorums intersects in more than faulty nodes iff 2q > N+f."""
    return 2 * quorum_size > N + faulty


def min_byzantine_quorum(N: int, faulty: int) -> int:
    """Smallest quorum satisfying pairwise honest intersection under f faults."""
    for q in range(1, N + 1):
        if byzantine_intersection_safe(N, q, faulty):
            return q
    return N


def main() -> None:
    print("#" * 100)
    print("# FINALITY -- QD redundancy / replication invariant gate (T519)")
    print("#" * 100)

    N = 8
    rows = [
        exact_redundancy(N, np.pi, 0.10),
        exact_redundancy(N, 0.6 * np.pi, 0.10),
        exact_redundancy(N, 0.6 * np.pi, 0.05),
        exact_redundancy(N, 0.6 * np.pi, 0.20),
    ]

    print("\n[1] QD candidate invariant D = 1 - f_delta/N")
    for row in rows:
        print(
            "      theta={theta_pi:.2f}pi delta={delta:.2f}: f={f_delta}, "
            "R={R_delta:.2f}, D={info_deficit:.3f}".format(**row)
        )
    check(
        "candidate varies with delta for fixed physics, so it is not a state-only invariant",
        abs(rows[2]["info_deficit"] - rows[3]["info_deficit"]) > 1e-9,
        f"D(0.05)={rows[2]['info_deficit']:.3f}, D(0.20)={rows[3]['info_deficit']:.3f}",
    )

    print("\n[2] crash-quorum reading")
    crash_matches = []
    for row in rows:
        q = int(row["f_delta"])
        ds = crash_survival_fraction(N, q)
        crash_matches.append(abs(ds - row["info_deficit"]) < 1e-12)
        print(f"      q=f_delta={q}: crash survival=(N-q)/N={ds:.3f}")
    check(
        "D matches crash survival exactly when the DS quorum size is stipulated as f_delta",
        all(crash_matches),
        "translation identity, not independent prediction",
    )

    print("\n[3] Byzantine quorum-intersection reading")
    # Classical n > 3f quorum intuition: with N=8, f=2 is the natural floor to test.
    faulty = 2
    q_bft = min_byzantine_quorum(N, faulty)
    bft_survival = crash_survival_fraction(N, q_bft)
    print(f"      N={N}, faulty={faulty}: minimum Byzantine-safe quorum q={q_bft}, survival={bft_survival:.3f}")
    bft_matches = [abs(row["info_deficit"] - bft_survival) < 1e-12 for row in rows]
    check(
        "D does NOT match the Byzantine quorum-intersection invariant across the QD rows",
        not all(bft_matches),
        f"D rows={[round(r['info_deficit'], 3) for r in rows]}, BFT={bft_survival:.3f}",
    )
    check(
        "the high-quality QD case would overstate Byzantine tolerance if read as the same invariant",
        rows[0]["info_deficit"] > bft_survival,
        f"perfect-copy D={rows[0]['info_deficit']:.3f} > BFT survival={bft_survival:.3f}",
    )

    verdict = "CRASH_TRANSLATION_ONLY_BYZANTINE_INVARIANT_FAILS"
    payload = {
        "artifact_id": "T519-quantum-darwinism-replication-invariant-gate-v0.1",
        "verdict": verdict,
        "model": "models/quantum_darwinism_replication_invariant_gate.py",
        "N": N,
        "candidate_invariant": "D_delta = 1 - f_delta/N",
        "rows": rows,
        "crash_quorum_reading": "D_delta equals crash survival only when q is set to f_delta.",
        "byzantine_reading": {
            "faulty": faulty,
            "minimum_safe_quorum": q_bft,
            "survival_fraction": bft_survival,
            "matches_all_rows": all(bft_matches),
        },
        "checks_passed": None,
        "checks_failed": None,
    }

    print("\n[verdict]")
    print(f"  * {verdict}")
    print("  * The proposed information-deficit invariant is a crash-quorum translation")
    print("    after importing q=f_delta from the QD side.")
    print("  * It is not a shared DS/QD quantitative discovery: it is delta-sensitive and")
    print("    fails the Byzantine quorum-intersection reading.")
    print("  * T518 remains structural correspondence only; the quantitative bridge stays open")
    print("    only for a new invariant that survives a predeclared DS failure model.")

    payload["checks_passed"] = 5 - len(FAIL)
    payload["checks_failed"] = len(FAIL)
    out = Path("results/T519-quantum-darwinism-replication-invariant-gate-v0.1.json")
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = candidate invariant tested; crash translation only, Byzantine invariant fails.")


if __name__ == "__main__":
    main()
