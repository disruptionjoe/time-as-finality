"""Tests for T417: Computational Finality Boundary (R2, Door C).

Asserts the predeclared legs of tests/T417-computational-finality-boundary.md
(frozen before the model existed). Exploratory; no claim promotion; ledger
untouched. Cross-domain (cryptography/complexity) is object of study, not
evidence.
"""

from models.computational_finality_boundary import (
    run, legendre, jacobi, is_qr_mod_N, N, P, Q, X_A, X_B,
)

R = run()


def test_leg1_co_presence_datum_differs():
    l1 = R["leg1_co_presence"]
    assert l1["A_is_QR"] is True          # x_A is a QR mod 77
    assert l1["B_is_QR"] is False         # x_B is a non-QR mod 77
    assert l1["datum_differs"] is True
    # the datum is a well-defined function of (x, N): recomputes identically
    assert is_qr_mod_N(X_A, P, Q) is True
    assert is_qr_mod_N(X_B, P, Q) is False


def test_leg2_reach_blindness_jacobi_identical():
    l2 = R["leg2_reach_blindness"]
    # the poly-time trapdoor-free predicate is +1 for BOTH -> reach is blind
    assert l2["jacobi_A"] == 1
    assert l2["jacobi_B"] == 1
    assert l2["reach_predicate_identical"] is True
    # cross-check directly
    assert jacobi(X_A, N) == jacobi(X_B, N) == 1


def test_leg3_trapdoor_separates():
    l3 = R["leg3_boundary_is_trapdoor"]
    assert l3["legendre_A_mod_p"] == 1
    assert l3["legendre_B_mod_p"] == -1
    assert l3["trapdoor_separates"] is True


def test_leg4_reservoir_dodged_and_completion_conceded_denied():
    l4 = R["leg4_killer_premortem"]
    assert "closed deterministic" in l4["reservoir_idealization"]
    jrc = l4["joint_record_completion"]
    assert jrc["datum_co_present"] is True
    assert jrc["brute_force_recovers"] is True     # co-presence confirmed executably
    assert jrc["but_at_cost_steps"] >= 1
    assert "denied FEASIBLE recovery" in jrc["verdict"]


def test_leg4_asymptotic_cost_grows():
    wl = R["leg4_killer_premortem"]["wait_longer_asymptotic"]
    assert wl["cost_monotone_increasing"] is True
    # strictly increasing trial-division cost across the semiprime family
    costs = wl["trial_division_steps"]
    assert costs == sorted(costs) and len(set(costs)) == len(costs)


def test_leg5_honest_verdict_conditional_and_family_level():
    l5 = R["leg5_honest_verdict"]
    assert l5["R2_discharged"] is False
    assert "CONDITIONAL" in l5["boundary_status"]
    assert "asymptotic" in l5["boundary_status"]
    assert l5["door"].startswith("C")


def test_headline_closed_model_dodges_reservoir_killer():
    """The headline: the first R2 door the reservoir-idealization killer cannot
    touch (closed deterministic model), which concedes co-presence but denies
    feasible recovery, supplies T416's independent poly-time evidence, and is
    honestly bounded (conditional on QRA, family-level not single-instance)."""
    assert R["leg1_co_presence"]["datum_differs"] is True
    assert R["leg2_reach_blindness"]["reach_predicate_identical"] is True
    assert "dodged" in R["leg4_killer_premortem"]["reservoir_idealization"]
    assert R["leg5_honest_verdict"]["R2_discharged"] is False
