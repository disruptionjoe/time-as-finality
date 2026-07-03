"""T423 - M2 Observer-Game / Judgment-Aggregation Finality Probe (Route B).

Exploratory big-swing for M2 (see explorations/m2-foundation-...-2026-07-02.md and
tests/T423-m2-observer-game.md, frozen first). Route B: exhibit a FINITE observer
/ judgment-aggregation game whose Aumann-Shapley (finite Shapley + non-atomic
trend) value IS the finality/capability separator, using the List-Pettit
discursive dilemma / doctrinal paradox as the finite discrete backbone.

Canonicity is the T422-beating target and is TESTED, not asserted. The honest
predeclared ceiling is a DEMOTION: (a) a genuine finality <-> List-Pettit
cross-application at synthesis tier plus (b) a falsifiable magnitude-decoupling
disanalogy -- NOT the clean triple-coincidence canonicity M2 hoped for.

Cross-domain material (social choice, judgment aggregation, cooperative game
theory) is the OBJECT OF STUDY, never evidence for physics or a sibling repo.
ONE-WAY RULE: ai-epistemology / temporal-issuance / GU are vocabulary and
template only, never imported as support. The ONLY code import is TaF-native
T413 machinery (models.legitimacy_shapley_finality_probe).

Exact rational arithmetic throughout (fractions.Fraction). Deterministic; n=3
fully enumerated (8 coalitions). Run:

    python -m models.m2_observer_game
    python -m pytest tests/test_m2_observer_game.py -q
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from math import factorial
import json

# ONLY import: TaF-native T413 machinery (reused verbatim).
from models.legitimacy_shapley_finality_probe import (
    all_subsets,
    v_of,
    shapley_by_dividends,
    shapley_by_permutations,
    restricted_games_agree,
    minimal_separating_coalition,
    joint_record_completion_verdict,
    symmetry_holds,
)

# ---------------------------------------------------------------------------
# Frozen fixture (predeclared in the spec).
# ---------------------------------------------------------------------------
JUDGES = (1, 2, 3)

# The classic n=3 doctrinal paradox profile.
#   judge 1: p=1 q=1  (r = p&q = 1)
#   judge 2: p=1 q=0  (r = p&q = 0)
#   judge 3: p=0 q=1  (r = p&q = 0)
P = {1: 1, 2: 1, 3: 0}
Q = {1: 1, 2: 0, 3: 1}


def and_doctrine(a, b):
    return 1 if (a and b) else 0


def or_doctrine(a, b):
    return 1 if (a or b) else 0


def dict_doctrine(a, b):
    return 1 if a else 0  # conclusion tracks the first premise (dictator on p)


# r column derived per judge from the AND doctrine (the frozen model).
R = {i: and_doctrine(P[i], Q[i]) for i in JUDGES}  # -> (1, 0, 0)


# ---------------------------------------------------------------------------
# ROUTE-B LOGIC ENGINE (isolated; imports NOTHING from the game side).
# ---------------------------------------------------------------------------
def smaj(col, S):
    """Strict majority of a 0/1 column over members of S; tie -> reject (0)."""
    S = tuple(S)
    ones = sum(col[i] for i in S)
    return 1 if ones * 2 > len(S) else 0


def premise_verdict(S, p=P, q=Q, doctrine=and_doctrine):
    """Premise-based collective verdict of coalition S: apply the doctrine to
    the per-premise majorities."""
    return doctrine(smaj(p, S), smaj(q, S))


def conclusion_verdict(S, r=R):
    """Conclusion-based collective verdict: majority on the r column."""
    return smaj(r, S)


def dilemma_indicator(S, p=P, q=Q, r=R, doctrine=and_doctrine):
    """1 iff premise-based and conclusion-based verdicts DISAGREE on S."""
    return 1 if premise_verdict(S, p, q, doctrine) != conclusion_verdict(S, r) else 0


def judges_consistent(p=P, q=Q, r=R, doctrine=and_doctrine):
    """K2 guard: every individual judgment obeys the doctrine (r_i = f(p_i,q_i))."""
    return all(r[i] == doctrine(p[i], q[i]) for i in JUDGES)


def collective_set(p=P, q=Q, r=R, players=JUDGES):
    """The three per-proposition majority verdicts of the grand coalition."""
    return {"p": smaj(p, players), "q": smaj(q, players), "r": smaj(r, players)}


def collective_inconsistent(p=P, q=Q, r=R, doctrine=and_doctrine, players=JUDGES):
    """The discursive dilemma at the collective level: majority set violates the
    doctrine even though (with judges_consistent) every individual set obeys it."""
    cs = collective_set(p, q, r, players)
    return cs["r"] != doctrine(cs["p"], cs["q"])


def lp_localization(p=P, q=Q, r=R, doctrine=and_doctrine, players=JUDGES):
    """Exhaustive global-no-local scan of the dilemma indicator: it must be 0 on
    every proper subset and 1 only on the grand coalition N."""
    grand = frozenset(players)
    proper_all_zero = True
    proper_carriers = []
    for S in all_subsets(players):
        if frozenset(S) == grand:
            continue
        if dilemma_indicator(S, p, q, r, doctrine) != 0:
            proper_all_zero = False
            proper_carriers.append(sorted(S))
    grand_is_one = dilemma_indicator(grand, p, q, r, doctrine) == 1
    return {
        "dilemma_only_on_grand": bool(proper_all_zero and grand_is_one),
        "proper_carriers": proper_carriers,
        "grand_indicator": dilemma_indicator(grand, p, q, r, doctrine),
    }


def agenda_obstruction(p=P, q=Q, r=R, doctrine=and_doctrine, players=JUDGES):
    """INDEPENDENT judgment-aggregation obstruction measure, computed on the
    PROPOSITION lattice (NOT the coalition lattice).

    omega = number of MINIMALLY-INCONSISTENT subsets of the collective's own
    endorsed literals, where a literal is (proposition, endorsed-truth-value) and
    inconsistency is judged against the doctrine constraint r = f(p, q).

    For the frozen AND profile the collective endorses {p:1, q:1, r:0}; the only
    minimally-inconsistent literal set is the whole {p, q, ~r}, so omega = 1.
    doctrine=None encodes NO-CONNECTION (r unconstrained) -> omega = 0.
    """
    lit = collective_set(p, q, r, players)  # variable -> endorsed truth value

    def satisfiable(constrained_vars):
        for ap in (0, 1):
            for aq in (0, 1):
                for ar in (0, 1):
                    if doctrine is not None and ar != doctrine(ap, aq):
                        continue
                    assign = {"p": ap, "q": aq, "r": ar}
                    if all(assign[v] == lit[v] for v in constrained_vars):
                        return True
        return False

    variables = ("p", "q", "r")
    count = 0
    minimal_sets = []
    for k in range(1, len(variables) + 1):
        for combo in combinations(variables, k):
            Y = set(combo)
            if not satisfiable(Y):
                if all(satisfiable(Y - {v}) for v in Y):
                    count += 1
                    minimal_sets.append(sorted(combo))
    return {"omega": count, "minimal_inconsistent_sets": minimal_sets}


# ---------------------------------------------------------------------------
# ROUTE-A GAME ENGINE.
# ---------------------------------------------------------------------------
def moebius_dividends(v_func, players):
    """Harsanyi dividends d(S) of a game given as a characteristic function
    v_func(S) via Mobius inversion on the coalition lattice."""
    div = {}
    for S in all_subsets(players):
        d = F(0)
        for T in all_subsets(S):
            d += F((-1) ** (len(S) - len(T))) * v_func(T)
        if d != 0:
            div[frozenset(S)] = d
    return div


def gap_value(S, p=P, q=Q, r=R, doctrine=and_doctrine):
    """v_gap(S) = premise_verdict(S) - conclusion_verdict(S)  (in {-1,0,1})."""
    return F(premise_verdict(S, p, q, doctrine) - conclusion_verdict(S, r))


def premise_game_value(S, p=P, q=Q, doctrine=and_doctrine):
    """v_prem(S) = premise-based verdict (the magnitude-decoupling comparison)."""
    return F(premise_verdict(S, p, q, doctrine))


def shapley_marginal(v_func, players):
    """Exact Shapley value by the marginal-contribution weight formula; used for
    the replicated (larger-N) Aumann-Shapley trend where |N|! enumeration is
    avoided.  phi_i = sum_{S !ni i} |S|!(n-|S|-1)!/n! (v(S+i)-v(S))."""
    players = tuple(players)
    n = len(players)
    nfac = factorial(n)
    phi = {i: F(0) for i in players}
    others = {i: [p for p in players if p != i] for i in players}
    for i in players:
        for S in all_subsets(others[i]):
            w = F(factorial(len(S)) * factorial(n - len(S) - 1), nfac)
            phi[i] += w * (v_func(frozenset(S) | {i}) - v_func(frozenset(S)))
    return phi


# ---------------------------------------------------------------------------
# Doctrine family + replication drivers.
# ---------------------------------------------------------------------------
DOCTRINES = {
    "AND": and_doctrine,
    "OR": or_doctrine,
    "DICT": dict_doctrine,
    "NOCONN": None,
}


def doctrine_family_row(name):
    """For one doctrine: build the gap game on the frozen p,q columns (r derived
    per judge from the doctrine), compute d(N), the SURVIVES-R1 separator verdict,
    and the independent agenda obstruction omega."""
    doc = DOCTRINES[name]
    if doc is None:
        # NO-CONNECTION: no premise->conclusion forcing; gap identically 0.
        r_col = {i: 0 for i in JUDGES}
        gv = lambda S: F(0)  # noqa: E731
    else:
        r_col = {i: doc(P[i], Q[i]) for i in JUDGES}
        gv = lambda S, d=doc, rc=r_col: gap_value(S, P, Q, rc, d)  # noqa: E731
    div = moebius_dividends(gv, JUDGES)
    zero = {}
    jrc = joint_record_completion_verdict(div, zero, players=JUDGES)
    separator_present = 1 if jrc.get("verdict") == "SURVIVES-R1" else 0
    dN = div.get(frozenset(JUDGES), F(0))
    obstruction = agenda_obstruction(P, Q, r_col, doc)["omega"] if doc is not None else 0
    return {
        "doctrine": name,
        "r_column": [r_col[i] for i in JUDGES],
        "d_N_moebius": str(dN),
        "gap_grand": str(gv(frozenset(JUDGES))),
        "separator_present": separator_present,
        "jrc_verdict": jrc.get("verdict"),
        "omega": obstruction,
        "separator_equals_omega": separator_present == obstruction,
    }


def replicate_profile(k):
    """Replicate each of the 3 judge-types into k identical copies.  Returns the
    player tuple and the p,q,r columns as dicts keyed by player id."""
    players = []
    p, q, r = {}, {}, {}
    pid = 0
    for t in JUDGES:
        for _ in range(k):
            players.append(pid)
            p[pid], q[pid], r[pid] = P[t], Q[t], R[t]
            pid += 1
    return tuple(players), p, q, r


def aumann_shapley_trend(kmax=3):
    """Replicate judge-types into k copies and report the dilution of individual
    Shapley shares against the preserved collective gap Delta = v_gap(N) = 1, plus
    whether the strict global-no-local (datum in NO proper subset) survives."""
    rows = []
    for k in range(1, kmax + 1):
        players, p, q, r = replicate_profile(k)
        gv = lambda S, p=p, q=q, r=r: gap_value(S, p, q, r, and_doctrine)  # noqa: E731
        vN = gv(frozenset(players))
        phi = shapley_marginal(gv, players)
        # per-type share (players 0..k-1 = type1, etc.); by symmetry equal in type
        type_share = {t: str(phi[(t - 1) * k]) for t in JUDGES}
        # smallest coalition that already exhibits the dilemma (gap == 1)
        min_dilemma_size = None
        for S in all_subsets(players):
            if gv(frozenset(S)) == 1:
                sz = len(S)
                if min_dilemma_size is None or sz < min_dilemma_size:
                    min_dilemma_size = sz
        n = len(players)
        global_no_local = (min_dilemma_size == n)
        rows.append({
            "k": k,
            "n_players": n,
            "v_gap_N_Delta": str(vN),
            "type_share_phi": type_share,
            "share_over_vN": str(phi[0] / vN) if vN != 0 else None,
            "naive_1_over_kn": str(F(1, k * 3)),
            "min_dilemma_coalition_size": min_dilemma_size,
            "global_no_local_survives": global_no_local,
        })
    return rows


def consistency_relaxation_probe():
    """K4 / Candidate-4 guard.  Relax r_i so judges are individually INCONSISTENT
    (r_i != p_i & q_i); show that the collective-inconsistency test then fires
    WITHOUT a genuine List-Pettit dilemma, so the omega<->separator agreement is a
    regime fact (holds only for consistent judges), not an identity."""
    relaxed_r = {1: 0, 2: 0, 3: 0}  # everyone rejects r regardless of p&q
    consistent = judges_consistent(P, Q, relaxed_r, and_doctrine)
    coll_incons = collective_inconsistent(P, Q, relaxed_r, and_doctrine)
    omega = agenda_obstruction(P, Q, relaxed_r, and_doctrine)["omega"]
    gv = lambda S: gap_value(S, P, Q, relaxed_r, and_doctrine)  # noqa: E731
    div = moebius_dividends(gv, JUDGES)
    jrc = joint_record_completion_verdict(div, {}, players=JUDGES)
    return {
        "relaxed_r": [relaxed_r[i] for i in JUDGES],
        "judges_consistent": consistent,          # False -> guard fires
        "collective_inconsistent": coll_incons,    # can still be True
        "omega_relaxed": omega,                    # can be nonzero
        "jrc_verdict": jrc.get("verdict"),
        "genuine_dilemma_requires_consistency": (not consistent) and coll_incons,
    }


# ---------------------------------------------------------------------------
# Assemble the run.
# ---------------------------------------------------------------------------
def run():
    # --- S1 genuine dilemma (K2 guard) --------------------------------------
    cs = collective_set()
    s1 = {
        "profile_p": [P[i] for i in JUDGES],
        "profile_q": [Q[i] for i in JUDGES],
        "profile_r": [R[i] for i in JUDGES],
        "judges_consistent": judges_consistent(),
        "collective_set": cs,
        "premise_based_verdict_grand": premise_verdict(JUDGES),
        "conclusion_based_verdict_grand": conclusion_verdict(JUDGES),
        "collective_inconsistent": collective_inconsistent(),
        "genuine_dilemma": judges_consistent() and collective_inconsistent(),
    }

    # --- Route-A gap game on the frozen AND profile -------------------------
    gv = lambda S: gap_value(S)  # noqa: E731
    gap_div = moebius_dividends(gv, JUDGES)
    coalition_table = {
        str(sorted(S)): {
            "P": premise_verdict(S), "C": conclusion_verdict(S),
            "gap": str(gv(frozenset(S))),
        }
        for S in all_subsets(JUDGES)
    }

    # --- S2 global-no-local -------------------------------------------------
    loc = lp_localization()
    jrc = joint_record_completion_verdict(gap_div, {}, players=JUDGES)
    s2 = {
        "gap_dividends": {str(sorted(S)): str(d) for S, d in gap_div.items()},
        "gap_game_is_unanimity_u_N": (gap_div == {frozenset(JUDGES): F(1)}),
        "lp_localization": loc,
        "joint_record_completion": jrc,
        "survives_R1": jrc.get("verdict") == "SURVIVES-R1",
    }

    # --- S3 Aumann-Shapley IS the separator ---------------------------------
    phi_div = shapley_by_dividends(gap_div, players=JUDGES)
    phi_perm = shapley_by_permutations(gap_div, players=JUDGES)
    s3 = {
        "shapley_by_dividends": {str(i): str(phi_div[i]) for i in JUDGES},
        "shapley_by_permutations": {str(i): str(phi_perm[i]) for i in JUDGES},
        "dividend_eq_permutation": phi_div == phi_perm,
        "d_N": str(gap_div.get(frozenset(JUDGES), F(0))),
        "symmetric": symmetry_holds(phi_div, gap_div, players=JUDGES),
        "efficient": sum(phi_div.values(), F(0)) == v_of(gap_div, JUDGES),
        "ties_to_T413_pair2_grand_dividend": (
            gap_div.get(frozenset(JUDGES), F(0)) == F(1)
            and jrc.get("verdict") == "SURVIVES-R1"
        ),
        "aumann_shapley_trend": aumann_shapley_trend(),
    }

    # --- S4 canonicity, honestly scoped -------------------------------------
    obs = agenda_obstruction()
    # premise game (the magnitude-decoupling teeth)
    pv = lambda S: premise_game_value(S)  # noqa: E731
    prem_div = moebius_dividends(pv, JUDGES)
    phi_prem = shapley_by_dividends(prem_div, players=JUDGES)
    # shared-primitive check: on consistent judges v_gap == dilemma_indicator
    shared_primitive = all(
        gap_value(S) == F(dilemma_indicator(S)) for S in all_subsets(JUDGES)
    )
    s4 = {
        "localization_agreement": {
            "gap_dividend_support": [sorted(S) for S in gap_div],
            "omega": obs["omega"],
            "minimal_inconsistent_sets": obs["minimal_inconsistent_sets"],
            "omega_equals_d_N": obs["omega"] == gap_div.get(frozenset(JUDGES), F(0)),
        },
        "shared_primitive_gap_equals_dilemma_indicator": shared_primitive,
        "K1_partial_localization_is_shared_primitive": shared_primitive,
        "magnitude_decoupling_teeth": {
            "premise_game_dividends": {str(sorted(S)): str(d)
                                       for S, d in prem_div.items()},
            "premise_game_d_N": str(prem_div.get(frozenset(JUDGES), F(0))),
            "premise_game_shapley": {str(i): str(phi_prem[i]) for i in JUDGES},
            "d_N_differs_from_gap": (prem_div.get(frozenset(JUDGES), F(0))
                                     != gap_div.get(frozenset(JUDGES), F(0))),
            "shapley_differs_from_gap": phi_prem != phi_div,
            "not_identical_by_construction": (
                prem_div.get(frozenset(JUDGES), F(0))
                != gap_div.get(frozenset(JUDGES), F(0))
                and phi_prem != phi_div
            ),
        },
        "doctrine_family": [doctrine_family_row(name) for name in DOCTRINES],
    }
    fam = s4["doctrine_family"]
    s4["doctrine_family_all_agree_separator_eq_omega"] = all(
        row["separator_equals_omega"] for row in fam
    )
    s4["doctrine_family_vector_varies"] = len({row["omega"] for row in fam}) > 1

    # --- S5 falsifiers ------------------------------------------------------
    s5 = {
        "consistency_relaxation": consistency_relaxation_probe(),
        "no_proper_subset_reconstructs": loc["dilemma_only_on_grand"],
        "doctrine_family_covaries": s4[
            "doctrine_family_all_agree_separator_eq_omega"],
    }

    return {
        "artifact": "T423-m2-observer-game-v0.1",
        "coalition_table": coalition_table,
        "s1_genuine_dilemma": s1,
        "s2_global_no_local": s2,
        "s3_aumann_shapley_is_separator": s3,
        "s4_canonicity_honestly_scoped": s4,
        "s5_falsifiers": s5,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
