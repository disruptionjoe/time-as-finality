"""T417 - Computational Finality Boundary (R2, Door C).

Forces the capability boundary with COMPUTATION instead of energy or a partial
trace. The model is closed and deterministic (number theory), so the
reservoir-idealization killer that killed every prior R2 attempt structurally
cannot apply. The datum (quadratic-residuosity of x mod N) is information-
theoretically co-present in (x, N) but recovery is computationally hard
(Quadratic Residuosity Assumption; reduces to factoring N). Reach = feasible
(poly-time) operations -- the independent operational bound T416 says R2 needs.

Goldwasser-Micali construction. See tests/T417-computational-finality-boundary.md
(frozen first). Cross-domain (cryptography/complexity) is the object of study,
never evidence. No claim promotion; ledger untouched.

    python -m models.computational_finality_boundary
    python -m pytest tests/test_computational_finality_boundary.py -v
"""

from __future__ import annotations

import json

# ---------------------------------------------------------------------------
# Fixed constants (predeclared in the spec, frozen).
# ---------------------------------------------------------------------------
N = 77            # = 7 * 11 ; the reach holds N, not its factors
P, Q = 7, 11      # the trapdoor (boundary-crossing menu), OUTSIDE the reach
X_A = 58          # QR mod 77 (58 = 2 mod 7, 3 mod 11: QR both)
X_B = 24          # non-QR mod 77 with Jacobi +1 (24 = 3 mod 7, 2 mod 11: non-QR both)
COST_FAMILY = [15, 77, 143, 899, 3599]   # 3*5, 7*11, 11*13, 29*31, 59*61


# ---------------------------------------------------------------------------
# Number-theory primitives (poly-time; Jacobi needs no factorization).
# ---------------------------------------------------------------------------
def legendre(a: int, p: int) -> int:
    """Legendre symbol (a/p) via Euler's criterion. Needs the prime p (trapdoor)."""
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return -1 if r == p - 1 else r  # r is 1 or p-1


def jacobi(a: int, n: int) -> int:
    """Jacobi symbol (a/n), n odd positive. Poly-time; needs NO factorization.
    This is the strongest generic predicate available to the trapdoor-free reach."""
    assert n > 0 and n % 2 == 1
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def is_qr_mod_N(x: int, p: int, q: int) -> bool:
    """QR-ness of x mod N=pq. Needs the factorization (the trapdoor)."""
    return legendre(x, p) == 1 and legendre(x, q) == 1


def trial_division_cost(n: int) -> dict:
    """Brute-force factoring by trial division; returns the smallest factor and
    the number of trial steps taken to reach it (an executable cost proxy)."""
    steps = 0
    d = 2
    while d * d <= n:
        steps += 1
        if n % d == 0:
            return {"smallest_factor": d, "steps": steps}
        d += 1
    return {"smallest_factor": n, "steps": steps}  # prime


# ---------------------------------------------------------------------------
# Assemble the run.
# ---------------------------------------------------------------------------
def run():
    # Leg 1 - co-presence (needs the trapdoor)
    a_is_qr = is_qr_mod_N(X_A, P, Q)
    b_is_qr = is_qr_mod_N(X_B, P, Q)
    leg1 = {
        "x_A": X_A, "x_B": X_B, "N": N,
        "A_is_QR": a_is_qr, "B_is_QR": b_is_qr,
        "datum_differs": a_is_qr != b_is_qr,
        "datum_is_function_of_x_N": True,   # QR-ness is determined by (x, N)
    }

    # Leg 2 - reach-blindness: the poly-time predicate (Jacobi) is identical
    jac_a, jac_b = jacobi(X_A, N), jacobi(X_B, N)
    leg2 = {
        "jacobi_A": jac_a, "jacobi_B": jac_b,
        "reach_predicate_identical": jac_a == jac_b == 1,
        "distinguishing_equiv_to": "Quadratic Residuosity Assumption (QRA); "
                                    "reduces to factoring N (cited, not proven)",
    }

    # Leg 3 - boundary crossing = the trapdoor (Legendre mod p)
    leg3 = {
        "legendre_A_mod_p": legendre(X_A, P),
        "legendre_B_mod_p": legendre(X_B, P),
        "trapdoor_separates": legendre(X_A, P) != legendre(X_B, P),
        "trapdoor_location": "the factorization p,q -- OUTSIDE the reach",
    }

    # Leg 4 - killer premortem
    # joint-record completion: brute force DOES recover (co-present) but at a cost
    fac = trial_division_cost(N)
    recovered_datum = None
    if fac["smallest_factor"] not in (1, N):
        p_found = fac["smallest_factor"]
        q_found = N // p_found
        recovered_datum = is_qr_mod_N(X_A, p_found, q_found)  # == A_is_QR
    # wait-longer / asymptotic gap: trial-division cost across the family
    costs = [trial_division_cost(n)["steps"] for n in COST_FAMILY]
    cost_monotone_increasing = all(costs[i] < costs[i + 1] for i in range(len(costs) - 1))
    leg4 = {
        "reservoir_idealization": "dodged structurally: closed deterministic "
                                  "model, no partial trace, nothing adopted",
        "joint_record_completion": {
            "datum_co_present": True,
            "brute_force_recovers": recovered_datum == a_is_qr,
            "but_at_cost_steps": fac["steps"],
            "verdict": "conceded co-presence, denied FEASIBLE recovery",
        },
        "wait_longer_asymptotic": {
            "family": COST_FAMILY,
            "trial_division_steps": costs,
            "cost_monotone_increasing": cost_monotone_increasing,
            "note": "boundary is a GROWING cost; physical only at the "
                    "family/asymptotic level, conditional on factoring hardness. "
                    "Trial division is illustrative; the actual basis is QRA.",
        },
        "lieb_robinson": "N/A (no spatial/light-cone structure)",
    }

    # Leg 5 - honest verdict
    leg5 = {
        "door": "C (complexity-forced recovery)",
        "relation_to_door_B": "a refinement of Door B (asymptotic gap) with "
                              "computation as the scaling resource",
        "supplies_T416_independent_evidence": "yes: reach = poly-time feasibility, "
                                              "an external bound not chosen to "
                                              "protect the separator",
        "boundary_status": "physical CONDITIONAL on QRA/factoring hardness and "
                           "only at the family/asymptotic level",
        "single_instance": "brute-force recoverable (finite work) -> a single "
                           "fixed instance is still declared/crackable",
        "R2_discharged": False,
    }

    return {
        "artifact": "T417-computational-finality-boundary-v0.1",
        "source": [
            "steward/runs/2026-07-02-coupling-graph-forcing-gate.md (T416)",
            "results/T415-admissibility-derivation-probe-v0.1-results.md",
            "explorations/physical-boundary-hegelian-persona-pass-2026-07-02.md",
        ],
        "claim_ledger_update": "none; no claim promotion",
        "leg1_co_presence": leg1,
        "leg2_reach_blindness": leg2,
        "leg3_boundary_is_trapdoor": leg3,
        "leg4_killer_premortem": leg4,
        "leg5_honest_verdict": leg5,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
