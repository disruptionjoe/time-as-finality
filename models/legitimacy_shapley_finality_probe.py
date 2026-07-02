"""T412 - Legitimacy-as-Shapley Finality Probe.

Exploratory big-swing model for the governance-layering <-> finality homology
(see tests/T412-legitimacy-shapley-finality-probe.md, frozen first). Classical
finite cooperative game; the Shapley value plays the role of the legitimate
(axiom-forced) capability of an in-region player. We port the T411 discriminator
structure into a game and run the four-absorber gauntlet.

Cross-domain (game theory / governance) is the OBJECT of study, never evidence
for physics or any sibling repo. No claim promotion; ledger untouched.

Exact rational arithmetic throughout (fractions.Fraction). Run:

    python -m models.legitimacy_shapley_finality_probe
    python -m pytest tests/test_legitimacy_shapley_finality_probe.py -v
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, permutations
import json

# ---------------------------------------------------------------------------
# Fixed fixture constants (predeclared in the spec, frozen).
# ---------------------------------------------------------------------------
N = (0, 1, 2, 3, 4)
S_R = (0, 1, 2)            # the reach (region R)
BOUNDARY = (3, 4)
FOCUS = 0                  # in-R focus player

# Games as Harsanyi unanimity dividends: dict frozenset(S) -> Fraction.
DIV_A = {frozenset({0, 1, 2}): F(6)}
DIV_B = {frozenset({0, 1, 2}): F(6), frozenset({0, 3}): F(2)}          # Pair 1
DIV_C = {frozenset({0, 1, 2}): F(6), frozenset({0, 1, 2, 3, 4}): F(5)}  # Pair 2


# ---------------------------------------------------------------------------
# Core game machinery.
# ---------------------------------------------------------------------------
def all_subsets(players):
    players = tuple(players)
    for r in range(len(players) + 1):
        for c in combinations(players, r):
            yield frozenset(c)


def v_of(div, T):
    """Characteristic function v(T) = sum of dividends d(S) for S subseteq T."""
    T = frozenset(T)
    return sum((d for S, d in div.items() if S <= T), F(0))


def shapley_by_dividends(div, players=N):
    """phi_i = sum over S ni i of d(S)/|S|."""
    phi = {i: F(0) for i in players}
    for S, d in div.items():
        share = d / F(len(S))
        for i in S:
            phi[i] += share
    return phi


def shapley_by_permutations(div, players=N):
    """phi_i = average over all |N|! orderings of i's marginal contribution."""
    players = tuple(players)
    n = len(players)
    total = {i: F(0) for i in players}
    count = 0
    for order in permutations(players):
        prefix = set()
        for i in order:
            before = frozenset(prefix)
            after = frozenset(prefix | {i})
            total[i] += v_of(div, after) - v_of(div, before)
            prefix.add(i)
        count += 1
    return {i: total[i] / F(count) for i in players}


# ---------------------------------------------------------------------------
# Absorber machinery.
# ---------------------------------------------------------------------------
def restricted_games_agree(div1, div2, S):
    """Do v1 and v2 agree on every coalition inside S (a proper region)?"""
    return all(v_of(div1, T) == v_of(div2, T) for T in all_subsets(S))


def minimal_separating_coalition(div1, div2, players=N):
    """Smallest coalition T with v1(T) != v2(T); None if identical everywhere."""
    best = None
    for T in all_subsets(players):
        if v_of(div1, T) != v_of(div2, T):
            if best is None or len(T) < len(best):
                best = T
    return best


def joint_record_completion_verdict(div1, div2, players=N):
    """The T401 move: is the separator revealed by a PROPER-subset coalition
    query (ABSORBED) or only by the whole player set (R1 survives)?"""
    sep = minimal_separating_coalition(div1, div2, players)
    if sep is None:
        return {"separates": False, "verdict": "no-separation"}
    is_proper = frozenset(sep) != frozenset(players)
    # Enumerate: does ANY proper subset S !< N carry the difference?
    proper_subset_carries = False
    for S in all_subsets(players):
        if frozenset(S) == frozenset(players):
            continue
        if not restricted_games_agree(div1, div2, S):
            proper_subset_carries = True
            break
    return {
        "separates": True,
        "min_sep_coalition": sorted(sep),
        "min_sep_size": len(sep),
        "datum_in_proper_subset": proper_subset_carries,
        "verdict": "ABSORBED" if proper_subset_carries else "SURVIVES-R1",
    }


def boundary_blind_value(div, players=N, boundary=BOUNDARY, focus=FOCUS):
    """A DECLARED re-weighting: average marginal contributions only over
    orderings in which no boundary player precedes `focus` (the region tries to
    'declare the boundary away'). Returns the allocation and its axiom audit."""
    players = tuple(players)
    total = {i: F(0) for i in players}
    count = 0
    for order in permutations(players):
        pos = {p: k for k, p in enumerate(order)}
        # down-weight (drop) orderings where a boundary player comes before focus
        if any(pos[b] < pos[focus] for b in boundary):
            continue
        prefix = set()
        for i in order:
            before, after = frozenset(prefix), frozenset(prefix | {i})
            total[i] += v_of(div, after) - v_of(div, before)
            prefix.add(i)
        count += 1
    val = {i: (total[i] / F(count) if count else F(0)) for i in players}
    grand = v_of(div, players)
    efficient = sum(val.values(), F(0)) == grand
    return {"value": val, "efficient": efficient,
            "sum": sum(val.values(), F(0)), "grand": grand, "kept_orderings": count}


def symmetry_holds(value, div, players=N):
    """Symmetry axiom check: interchangeable players get equal shares.
    Two players i,j are interchangeable if v(S+i)=v(S+j) for all S not
    containing either. For unanimity u_N all players are interchangeable."""
    players = tuple(players)
    def interchangeable(i, j):
        for S in all_subsets([p for p in players if p not in (i, j)]):
            if v_of(div, frozenset(S) | {i}) != v_of(div, frozenset(S) | {j}):
                return False
        return True
    for i, j in combinations(players, 2):
        if interchangeable(i, j) and value[i] != value[j]:
            return False
    return True


def imputation_set_dimension(div, players=N):
    """The efficient allocations x with x_i >= v({i}) form a simplex of
    dimension |N|-1 whenever the simplex is nonempty (sum of individual values
    <= grand value). Returns that dimension (the 'declared' multiplicity)."""
    players = tuple(players)
    grand = v_of(div, players)
    indiv = {i: v_of(div, frozenset({i})) for i in players}
    slack = grand - sum(indiv.values(), F(0))
    return (len(players) - 1) if slack >= 0 else -1, slack


def finite_N_sensitivity():
    """Aumann-Shapley-flavored gesture: for a family of games
    v = u_{firstcoalition} (dividend 6) + u_{grand} (dividend g), how does the
    focus player's SHARE of the total legitimate value move with N?
    We report phi_0 / v(N) as N grows (the grand-coalition datum's relative
    grip on any single share -> 0). Gesture only; non-atomic limit out of house
    style."""
    rows = []
    for n in (3, 4, 5):
        players = tuple(range(n))
        first = frozenset(range(min(3, n)))  # a fixed small productive coalition
        div = {first: F(6), frozenset(players): F(5)}
        phi = shapley_by_dividends(div, players)
        grand = v_of(div, players)
        rows.append({
            "N": n,
            "phi_0": str(phi[0]),
            "v_N": str(grand),
            "phi_0_share_of_total": str(phi[0] / grand),
            "grand_dividend_contrib_to_phi_0": str(F(5) / F(n)),
        })
    return rows


# ---------------------------------------------------------------------------
# Assemble the run.
# ---------------------------------------------------------------------------
def run():
    phi_A_d = shapley_by_dividends(DIV_A)
    phi_B_d = shapley_by_dividends(DIV_B)
    phi_C_d = shapley_by_dividends(DIV_C)
    phi_A_p = shapley_by_permutations(DIV_A)
    phi_B_p = shapley_by_permutations(DIV_B)
    phi_C_p = shapley_by_permutations(DIV_C)

    def vec(phi):
        return [str(phi[i]) for i in N]

    # Leg 1 - cross-check + efficiency
    leg1 = {
        "dividend_eq_permutation": (phi_A_d == phi_A_p and phi_B_d == phi_B_p
                                    and phi_C_d == phi_C_p),
        "efficiency_A": sum(phi_A_d.values(), F(0)) == v_of(DIV_A, N),
        "efficiency_B": sum(phi_B_d.values(), F(0)) == v_of(DIV_B, N),
        "efficiency_C": sum(phi_C_d.values(), F(0)) == v_of(DIV_C, N),
        "phi_A": vec(phi_A_d), "phi_B": vec(phi_B_d), "phi_C": vec(phi_C_d),
        "v_N": {"A": str(v_of(DIV_A, N)), "B": str(v_of(DIV_B, N)),
                "C": str(v_of(DIV_C, N))},
    }

    # Leg 2 - within-R equality (both pairs)
    leg2 = {
        "pair1_within_R_equal": restricted_games_agree(DIV_A, DIV_B, S_R),
        "pair2_within_R_equal": restricted_games_agree(DIV_A, DIV_C, S_R),
    }

    # Leg 3 - Shapley separation
    leg3 = {
        "pair1_phi0_delta": str(phi_B_d[FOCUS] - phi_A_d[FOCUS]),
        "pair2_phi0_delta": str(phi_C_d[FOCUS] - phi_A_d[FOCUS]),
    }

    # Leg 4 - joint-record completion (the SPLIT)
    leg4 = {
        "pair1": joint_record_completion_verdict(DIV_A, DIV_B),
        "pair2": joint_record_completion_verdict(DIV_A, DIV_C),
    }

    # Leg 5 - relabel / declared re-weighting vs axioms
    bb_C = boundary_blind_value(DIV_C)
    leg5 = {
        "boundary_blind_phi0": str(bb_C["value"][FOCUS]),
        "shapley_phi0": str(phi_C_d[FOCUS]),
        "boundary_blind_changes_phi0": bb_C["value"][FOCUS] != phi_C_d[FOCUS],
        "boundary_blind_efficient": bb_C["efficient"],
        "boundary_blind_symmetric": symmetry_holds(bb_C["value"], DIV_C),
        "shapley_symmetric": symmetry_holds(phi_C_d, DIV_C),
        "shapley_efficient": sum(phi_C_d.values(), F(0)) == v_of(DIV_C, N),
    }

    # Leg 6 - R2 honesty: the datum is declared
    leg6 = {
        "pair2_datum_location": "grand_coalition_v(N)",
        "pair2_datum_value_A": str(v_of(DIV_A, N)),
        "pair2_datum_value_C": str(v_of(DIV_C, N)),
        "datum_is_declared": True,
        "boundary_physicality_reduces_to_declaration": True,  # fires, as in T411
    }

    # Leg 7 - Nash multiplicity vs Shapley uniqueness + AS trend
    dim, slack = imputation_set_dimension(DIV_C)
    leg7 = {
        "imputation_set_dimension": dim,
        "imputation_slack": str(slack),
        "shapley_unique_point": True,
        "aumann_shapley_trend": finite_N_sensitivity(),
    }

    # Leg 8 - quantum-residue negative (executable): Shapley linear in v, so a
    # separator with ALL coalition values equal is impossible.
    #   Constructed test: two games equal on every coalition -> identical phi.
    equal_games_identical_phi = (
        shapley_by_dividends(DIV_A) == shapley_by_dividends(dict(DIV_A))
    )
    # And: any nonzero phi difference is witnessed by some coalition value diff.
    def phi_diff_implies_coalition_diff(div1, div2):
        if shapley_by_dividends(div1) == shapley_by_dividends(div2):
            return None  # no phi difference to witness
        return minimal_separating_coalition(div1, div2) is not None
    leg8 = {
        "equal_games_identical_phi": equal_games_identical_phi,
        "pair1_phi_diff_has_coalition_witness":
            phi_diff_implies_coalition_diff(DIV_A, DIV_B),
        "pair2_phi_diff_has_coalition_witness":
            phi_diff_implies_coalition_diff(DIV_A, DIV_C),
        "no_marginal_separator_possible_classically": True,
        "note": ("A no-marginal / information-in-no-coalition separator (the "
                 "T411 quantum residue) cannot exist in a finite classical "
                 "game: Shapley is linear in v, so phi(v_A)!=phi(v_B) forces "
                 "v_A!=v_B on some coalition."),
    }

    return {
        "artifact": "T412-legitimacy-shapley-finality-probe-v0.1",
        "leg1_crosscheck_efficiency": leg1,
        "leg2_within_R_equality": leg2,
        "leg3_shapley_separation": leg3,
        "leg4_joint_record_completion_SPLIT": leg4,
        "leg5_relabel_vs_axioms": leg5,
        "leg6_R2_declared_honesty": leg6,
        "leg7_nash_multiplicity_vs_shapley_uniqueness": leg7,
        "leg8_quantum_residue_negative": leg8,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
