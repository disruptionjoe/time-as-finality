"""T419 - Computational Arrow of Time (temporal lift of T417's static E2 boundary).

Recorded outcome: REDESIGN. The K4 static-relabel kill fires on the exhibited
toy orbit because its short cycle makes trapdoor-free predecessor recovery cheap.
The model keeps the sound entropy-neutral and Rabin-reduction legs, but records
that the toy does not exhibit the intended temporal arrow.

The D2 open problem (open-problems/computational-finality-arrow.md): force an
arrow of time -- a past/future asymmetry of FEASIBLE recoverability -- with
computational hardness under a standard cryptographic assumption, over an ACTUAL
iterated dynamics (not a static (x,N) datum relabelled past/future).

Construction (Rabin / Blum-Blum-Shub squaring permutation on QR_N of a Blum
integer). Reuse T417's N = 77 = 7*11 (Blum: 7 == 11 == 3 mod 4). The forward
transition is one modular squaring F(x) = x^2 mod N. On the group of quadratic
residues QR_N it is a genuine PERMUTATION (|QR_N| = phi(N)/4 is odd for a Blum
integer) -- so nothing is erased, nothing grows, and the reversal EXISTS with
certainty (each state has a unique predecessor). Yet a backward step is the
principal square root mod N, which by Rabin (1979) is polynomial-time EQUIVALENT
to factoring N. Hardness is therefore REDUCED to a named standard assumption, not
stipulated. The emitted BBS bit-record b_t = lsb(x_t) is the temporal object; the
Quadratic Residuosity Assumption (Goldwasser-Micali 1982) lifts T417's Leg 2 onto
the time axis, with Blum-Blum-Shub (1986) forward-security.

The intended arrow is agent-relative to trapdoor possession: with (p,q) the cone
is symmetric (backward polylog); without it, asymmetric (backward == factoring).
The hostile-review result is that this remains a generic/asymptotic E2 story,
not a successfully exhibited toy-scale temporal arrow.

See tests/T419-computational-arrow-of-time.md (frozen FIRST). Cross-domain
(cryptography / number theory) is the object of study, never evidence for physics
or a sibling repo. Deterministic, exact integer arithmetic; closed model (no
reservoir, no partial trace, no randomness). Hardness cited (Rabin 1979;
Goldwasser-Micali 1982; Blum-Blum-Shub 1986), NOT proven. No claim promotion;
TESTS.md / CLAIM-LEDGER.md untouched; single-process ceiling in force.

    python -m models.computational_arrow_of_time
    python -m pytest tests/test_computational_arrow_of_time.py -v
"""

from __future__ import annotations

import json
from math import gcd

# ---------------------------------------------------------------------------
# Fixed constants (predeclared in the spec, frozen). Reuses T417's N = 77.
# ---------------------------------------------------------------------------
N = 77                # = 7 * 11 ; the reach holds N, not its factors
P, Q = 7, 11          # the trapdoor (factorization), OUTSIDE the reach; Blum
SEED = 4              # x_0 in QR_77
T_TICKS = 8           # orbit length x_0 .. x_8
# Blum-semiprime cost-growth family (all factors == 3 mod 4).
COST_FAMILY_FACTORS = [(3, 7), (7, 11), (11, 19), (23, 31), (43, 59), (83, 103)]
COST_FAMILY = [p * q for p, q in COST_FAMILY_FACTORS]  # [21,77,209,713,2537,8549]


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
    The strongest generic predicate available to the trapdoor-free reach."""
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


def is_blum(p: int, q: int) -> bool:
    """A Blum integer N = p*q has p == q == 3 (mod 4), p, q distinct odd primes."""
    return p % 4 == 3 and q % 4 == 3 and p != q


def lsb(x: int) -> int:
    """Least-significant bit -- the emitted BBS output bit."""
    return x & 1


def quad_residues(n: int) -> list[int]:
    """Enumerate QR_n = { x^2 mod n : gcd(x,n)=1 } (the units that are squares)."""
    return sorted({(x * x) % n for x in range(1, n) if gcd(x, n) == 1})


def forward(x: int, n: int) -> int:
    """Forward transition F(x) = x^2 mod n. ONE modular multiplication; needs
    only n. This is the forward-easy, cost-FLAT step."""
    return (x * x) % n


def forward_reach(x: int, k: int, n: int) -> tuple[list[int], int]:
    """k forward squarings from x using only n. Returns (orbit_states, modmul_ops).
    Any reach agent can do this: O(k) modmuls, flat per step, polylog in |n|."""
    states = [x]
    ops = 0
    for _ in range(k):
        x = forward(x, n)
        ops += 1  # exactly one modmul per step -- FLAT in t
        states.append(x)
    return states, ops


def principal_sqrt(y: int, p: int, q: int) -> int:
    """The TRAPDOOR backward step: principal square root of y mod N=p*q via CRT.
    For a Blum integer the principal root is the unique square root that is itself
    a QR mod both primes -- i.e. the unique predecessor inside QR_N. Polylog
    (two modular exponentiations + CRT). Requires (p,q)."""
    n = p * q
    sp = pow(y, (p + 1) // 4, p)
    if legendre(sp, p) != 1:
        sp = p - sp                       # pick the QR-mod-p root
    sq = pow(y, (q + 1) // 4, q)
    if legendre(sq, q) != 1:
        sq = q - sq                       # pick the QR-mod-q root
    inv_p = pow(p, -1, q)                  # CRT recombination
    return (sp + p * ((sq - sp) * inv_p % q)) % n


def backward_bruteforce(y: int, n: int, qr: list[int]) -> int | None:
    """Trapdoor-FREE backward step by finite search over QR_n: find the unique
    z in QR_n with z^2 == y mod n. Proves the predecessor is present in principle
    -- but at a search cost (illustrative of the factoring wall)."""
    for z in qr:
        if (z * z) % n == y:
            return z
    return None


def cycle_predecessor_by_forward_iteration(y: int, n: int, limit: int | None = None) -> tuple[int, int] | None:
    """Recover a cycle predecessor using only the public forward map.

    This is the K4 hostile-review check. On a short finite cycle, the predecessor
    is F^(period-1)(y), so the exhibited toy orbit is reversible without the
    trapdoor.
    """
    if limit is None:
        limit = n + 1
    x = y
    for steps in range(1, limit + 1):
        x = forward(x, n)
        if forward(x, n) == y:
            return x, steps
    return None


def rabin_reduction(n: int, sqrt_oracle) -> dict | None:
    """Rabin (1979) EXHIBITED: a square-root oracle for N yields a nontrivial
    factor of N. Deterministic sweep of witnesses w coprime to N: set a = w^2,
    ask the oracle for a root r of a; if r != +-w mod N then gcd(r-w, N) splits N.
    This demonstrates a backward step (principal sqrt) IS as hard as factoring --
    hardness REDUCED, not stipulated. (No randomness: first successful w taken.)"""
    for w in range(2, n):
        if gcd(w, n) != 1:
            continue
        a = (w * w) % n
        r = sqrt_oracle(a)                # one backward step
        g = gcd((r - w) % n, n)
        if 1 < g < n:
            return {"witness_w": w, "oracle_root": r,
                    "nontrivial_factor": g, "cofactor": n // g}
    return None


def trial_division_steps(n: int) -> int:
    """Trial-division step count to the smallest factor -- an ILLUSTRATIVE proxy
    for the (super-polynomial) cost of factoring without the trapdoor. The real
    basis is factoring/QRA (GNFS sub-exponential), NOT trial division."""
    steps = 0
    d = 2
    while d * d <= n:
        steps += 1
        if n % d == 0:
            return steps
        d += 1
    return steps


# ---------------------------------------------------------------------------
# Assemble the run.
# ---------------------------------------------------------------------------
def run():
    qr = quad_residues(N)

    # -- Leg 1: PERMUTATION / entropy-neutral (zero erasure, reversal in principle)
    images = sorted(forward(x, N) for x in qr)
    leg1 = {
        "N": N, "is_blum": is_blum(P, Q),
        "QR_N": qr, "size_QR_N": len(qr),
        "phi_over_4": (P - 1) * (Q - 1) // 4,
        "size_is_odd": len(qr) % 2 == 1,
        "F_is_permutation_of_QR_N": images == qr,
        "erasure": "ZERO -- squaring is a bijection on QR_N; constant state "
                   "description length; nothing grows (K1/K2 guard)",
    }

    # -- Build the orbit + emitted BBS bit-record (the temporal object)
    orbit, fwd_ops = forward_reach(SEED, T_TICKS, N)
    bit_record = [lsb(x) for x in orbit]

    # -- Leg 2: CO-PRESENCE (unique predecessor; trapdoor recovers exact x_{t-1})
    trapdoor_recovers = []
    for t in range(1, len(orbit)):
        rec = principal_sqrt(orbit[t], P, Q)
        trapdoor_recovers.append(rec == orbit[t - 1])
    # uniqueness: each orbit state has exactly one QR-predecessor
    unique_pred = all(
        sum(1 for z in qr if (z * z) % N == orbit[t]) == 1
        for t in range(1, len(orbit))
    )
    leg2 = {
        "seed_x0": SEED, "T_ticks": T_TICKS,
        "orbit": orbit, "emitted_bit_record": bit_record,
        "unique_predecessor_every_state": unique_pred,
        "trapdoor_recovers_exact_predecessor_every_t": all(trapdoor_recovers),
        "reversal": "EXISTS with certainty (unique predecessor); datum present",
    }

    # -- Leg 3: FORWARD-EASY-FLAT (1 modmul/step, flat in t, polylog in |N|)
    # extend the emitted record forward by k more ticks with N ALONE:
    ext_states, ext_ops = forward_reach(orbit[-1], 5, N)
    leg3 = {
        "forward_step_ops": 1,
        "ops_per_step_flat_in_t": [1] * T_TICKS,
        "total_forward_ops_for_T": fwd_ops,
        "extend_record_forward_with_N_alone": {
            "extra_ticks": 5, "extra_states": ext_states[1:],
            "extra_bits": [lsb(x) for x in ext_states[1:]], "ops": ext_ops,
        },
        "note": "forward = one modular squaring using only N; O(k) for k steps, "
                "flat per tick, polylog in |N|. Any reach agent extends the orbit "
                "and the bit-record arbitrarily far forward.",
    }

    # -- Leg 4: BACKWARD-HARD-BY-REDUCTION (Rabin sqrt->factor, EXHIBITED)
    #    the sqrt oracle == a single backward step (principal sqrt)
    oracle = lambda a: principal_sqrt(a, P, Q)
    reduction = rabin_reduction(N, oracle)
    factored_ok = (reduction is not None
                   and reduction["nontrivial_factor"] in (P, Q))
    # T417 Leg 2 lifted onto the time axis: trapdoor-free past-bit predicate
    jac_orbit = [jacobi(x, N) for x in orbit]           # all +1, uninformative
    leg_orbit = [legendre(x, P) for x in orbit]         # trapdoor separates
    leg4 = {
        "backward_step": "principal square root mod N",
        "rabin_reduction_exhibited": reduction,
        "sqrt_oracle_yields_factor_of_N": factored_ok,
        "meaning": "one backward step ==(Rabin 1979) factoring N -- hardness is "
                   "REDUCED to a named standard assumption, NOT stipulated (K3 "
                   "guard)",
        "T417_leg2_on_time_axis": {
            "jacobi_over_orbit": jac_orbit,
            "jacobi_uninformative_all_+1": all(s == 1 for s in jac_orbit),
            "legendre_with_trapdoor": leg_orbit,
            "decision_wall": "distinguishing the emitted bits without (p,q) == "
                             "Quadratic Residuosity Assumption (Goldwasser-Micali "
                             "1982); BBS (1986) forward-security. Cited, not proven.",
        },
    }

    # -- Leg 5: TRAPDOOR-RESYMMETRIZES (E2, agent-relative, per-step)
    fwd_step_ops = 1
    back_trap_ops = 2 * (P.bit_length() + Q.bit_length())  # ~2 CRT modexps: polylog
    back_notrap_ops = trial_division_steps(N)              # factoring proxy
    leg5 = {
        "with_trapdoor": {
            "forward_ops": fwd_step_ops, "backward_ops": back_trap_ops,
            "cone": "SYMMETRIC -- backward polylog at every step",
        },
        "without_trapdoor": {
            "forward_ops": fwd_step_ops, "backward_ops": ">= factoring N",
            "backward_proxy_ops": back_notrap_ops,
            "cone": "ASYMMETRIC -- forward flat, backward == factoring",
        },
        "wall_type": "E2 / computational; agent-relative to (p,q) possession; "
                     "NOT thermodynamic (E1), NOT intrinsic (E0/E3)",
    }

    # -- Leg 6: TEMPORAL-ASYMMETRY-OVER-ORBIT (anti-relabel), sampled at several t
    # Hostile-review outcome: the intended anti-relabel guard fails on this toy
    # orbit, because the period-4 cycle gives a cheap trapdoor-free predecessor.
    sample_ts = [2, 4, 6]
    per_step = []
    for t in sample_ts:
        fwd_set, _ = forward_reach(orbit[t], 3, N)   # poly-enumerable
        cycle_recovery = cycle_predecessor_by_forward_iteration(orbit[t], N)
        if cycle_recovery is None:
            back_feasible_no_trap = []
            cycle_steps = None
        else:
            cycle_pred, cycle_steps = cycle_recovery
            back_feasible_no_trap = [cycle_pred]
        back_feasible_trap = [principal_sqrt(orbit[t], P, Q)]
        per_step.append({
            "t": t, "x_t": orbit[t],
            "forward_reachable_3": fwd_set[1:],
            "backward_feasible_without_trapdoor": back_feasible_no_trap,
            "trapdoor_free_cycle_reversal_ops": cycle_steps,
            "backward_feasible_with_trapdoor": back_feasible_trap,
            "recorded_predecessor": orbit[t - 1],
            "predecessor_matches_cycle_recovery":
                len(back_feasible_no_trap) == 1 and back_feasible_no_trap[0] == orbit[t - 1],
            "predecessor_matches_trapdoor": back_feasible_trap[0] == orbit[t - 1],
        })
    k4_fired = any(step["predecessor_matches_cycle_recovery"] for step in per_step)
    leg6 = {
        "sampled_t": sample_ts,
        "per_step": per_step,
        "asymmetry_is_per_step_property": False,
        "forward_cost_flat": True,
        "growing_monotone_used": False,
        "k4_static_relabel_kill_fired": k4_fired,
        "note": "on the exhibited period-4 toy orbit, forward iteration recovers "
                "the recorded predecessor without the trapdoor. The intended "
                "anti-relabel guard therefore fails: the displayed dynamics is a "
                "time-symmetric reversible-recurrent toy, not an executable "
                "per-step computational arrow. NO growing monotone introduced.",
    }

    # -- Leg 7: COST-GROWTH-FAMILY (inherit T417 shape; two diverging curves)
    fam_rows = []
    for (p, q), n in zip(COST_FAMILY_FACTORS, COST_FAMILY):
        fam_rows.append({
            "N": n, "factors": [p, q], "is_blum": is_blum(p, q),
            "forward_step_ops": 1,                                  # FLAT
            "backward_without_trapdoor_ops": trial_division_steps(n),  # increasing
            "backward_with_trapdoor_ops": 2 * (p.bit_length() + q.bit_length()),
        })
    without = [r["backward_without_trapdoor_ops"] for r in fam_rows]
    leg7 = {
        "family": COST_FAMILY,
        "rows": fam_rows,
        "forward_flat": all(r["forward_step_ops"] == 1 for r in fam_rows),
        "backward_without_trapdoor_curve": without,
        "backward_without_trapdoor_strictly_increasing":
            all(without[i] < without[i + 1] for i in range(len(without) - 1)),
        "backward_with_trapdoor_curve":
            [r["backward_with_trapdoor_ops"] for r in fam_rows],
        "honest_note": "trial division is ILLUSTRATIVE; the asymptotic basis is "
                       "factoring / QRA (GNFS sub-exponential). Any single fixed N "
                       "is finite-work crackable -- boundary is family/asymptotic. "
                       "Small-N crossover is expected; the point is the asymptotic "
                       "divergence (backward-no-trapdoor ~sqrt(N) illustrative vs "
                       "backward-with-trapdoor ~log N).",
    }

    # -- Leg 8: KILLER PREMORTEM (four kills, each with its executable dodge)
    leg8 = {
        "K1_thermo_E1": {
            "dodge": "permutation on QR_N => ZERO erasure; no reservoir, no "
                     "partial trace; backward cost billed in ARITHMETIC ops, not "
                     "kT ln2",
            "evidence": leg1["F_is_permutation_of_QR_N"],
        },
        "K2_brown_susskind": {
            "dodge": "constant description length; NOTHING grows; the arrow is a "
                     "per-step forward-vs-inverse COST asymmetry with forward FLAT, "
                     "not a symmetric complexity-growth monotone",
            "evidence": leg6["growing_monotone_used"] is False,
        },
        "K3_stipulated_hardness_E0": {
            "dodge": "Rabin (1979) sqrt==factoring EXHIBITED executably (oracle "
                     "-> factor) + QRA; only (p,q) -- genuinely absent, "
                     "family-superpoly -- crosses",
            "evidence": factored_ok,
        },
        "K4_static_T417_relabel": {
            "dodge": "FAILED on the toy: a real iterated orbit exists, but its "
                     "short cycle lets the public forward map recover predecessors "
                     "without the trapdoor.",
            "evidence": not k4_fired,
            "fired": k4_fired,
        },
        "K5_prior_art": {
            "dodge": "no clean published 'cryptographic arrow of time' with these "
                     "exact properties (info-recoverable-but-computationally-locked, "
                     "distinct from thermodynamic and complexity-growth arrows) "
                     "known at build time; adversarial search pending",
            "evidence": "OPEN -- hostile review to follow",
        },
    }

    # -- Differentiation (success-criterion-3): argued distinctness
    differentiation = {
        "vs_brown_susskind": "constant-complexity bijection; forward cost FLAT; "
                             "asymmetric feasible-INVERTIBILITY, not symmetric "
                             "complexity growth (nothing grows)",
        "vs_lesovik": "reversal EXISTS with probability 1 (unique predecessor), "
                      "computationally sealed -- not statistical improbability, no "
                      "ensemble",
        "vs_crutchfield": "state fully observed, nothing hidden in causal states -- "
                          "the lock is cryptographic one-wayness with an explicit "
                          "factoring reduction",
        "vs_wolpert_bennett": "entropy-neutral, zero thermodynamic cost -- the seal "
                              "is algebraic (missing factorization), isolating E2 "
                              "from E1",
        "vs_T417": "real iterated dynamics + time index + emitted record stream + "
                   "per-transition cost asymmetry, not a static (x,N) datum",
    }

    # -- Honest verdict
    verdict = {
        "arrow": "REDESIGN -- the exhibited toy does not show a computational "
                 "arrow of time; trapdoor-free forward iteration recovers the "
                 "recorded predecessors on the short cycle.",
        "info_theoretically": "TRIVIAL -- datum present, reversal exists (bijection)",
        "computationally": "POINT-SQRT hardness is reduced to Rabin(1979)/QRA, "
                           "but the temporal arrow is not forced by the exhibited "
                           "orbit.",
        "boundary_status": "physical CONDITIONAL on factoring/QRA and only at the "
                           "family/asymptotic level",
        "single_instance": "any fixed N is finite-work crackable (still "
                           "declared/crackable)",
        "no_growing_monotone": True,
        "k4_static_relabel_kill_fired": k4_fired,
        "claim_promotion": "none; recorded-tier; ledger paused for Joe",
    }

    return {
        "artifact": "T419-computational-arrow-of-time-v0.1",
        "provisional_T_number": "T419 (TESTS.md / CLAIM-LEDGER.md UNTOUCHED)",
        "problem": "open-problems/computational-finality-arrow.md (D2)",
        "taxonomy_mode": "E2 (technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md)",
        "extends": "results/T417-computational-finality-boundary-v0.1-results.md",
        "hardness_assumption": "Rabin(1979) sqrt==factoring; QRA (Goldwasser-Micali "
                               "1982); BBS(1986) forward-security. CITED, not proven.",
        "claim_ledger_update": "none; no claim promotion",
        "leg1_permutation_entropy_neutral": leg1,
        "leg2_co_presence": leg2,
        "leg3_forward_easy_flat": leg3,
        "leg4_backward_hard_by_reduction": leg4,
        "leg5_trapdoor_resymmetrizes": leg5,
        "leg6_temporal_asymmetry_over_orbit": leg6,
        "leg7_cost_growth_family": leg7,
        "leg8_killer_premortem": leg8,
        "differentiation": differentiation,
        "honest_verdict": verdict,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
