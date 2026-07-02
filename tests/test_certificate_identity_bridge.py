"""Tests for T413: Certificate-Identity Bridge (bridge obligation #1).

Asserts the predeclared legs of tests/T413-certificate-identity-bridge.md
(frozen before the model existed). Exploratory; no claim promotion; ledger
untouched. Built falsifiable: Pair 1 must be REJECTED; T411 invariance reported
honestly as partial.
"""

from models.certificate_identity_bridge import run, SIGNATURE_FIELDS

R = run()


def test_leg1_both_instantiate_signature_and_verdict():
    assert R["game_pair2_instantiates"] is True
    assert R["t411_instantiates"] is True
    assert R["cert_game_pair2"]["verdict"] == "final-relative-to-R"
    assert R["cert_t411"]["verdict"] == "final-relative-to-R"


def test_leg2_stability_match():
    assert R["cert_game_pair2"]["stability_witness"]["no_in_R_overturn"] is True
    assert R["cert_t411"]["stability_witness"]["no_in_R_overturn"] is True


def test_leg3_datum_locus_match_pair2():
    assert R["cert_game_pair2"]["datum_locus"] == "whole"
    assert R["cert_t411"]["datum_locus"] == "whole"


def test_leg4_invariance_divergence_is_the_honest_asymmetry():
    # game: complete (proven); T411: incomplete (LR only, full class open)
    assert R["cert_game_pair2"]["invariance_witness"]["complete"] is True
    assert R["cert_t411"]["invariance_witness"]["complete"] is False
    # T411 IS invariant on the irrelevant (LR) class, just not the full class
    assert R["cert_t411"]["invariance_witness"]["irrelevant_class"] is True
    assert R["cert_t411"]["invariance_witness"]["full_admissible_class"] is False


def test_leg5_bridge_verdict_partial_homology():
    b = R["bridge_pair2_vs_t411"]
    assert b["bridge_verdict"] == "PARTIAL-HOMOLOGY (invariance owed by T411)"
    # exactly one divergent field, and it is the invariance completeness
    assert b["divergent_fields"] == ["invariance_witness.complete"]
    # 4 of 5 conceptual fields identical (region+menu counted separately -> 5)
    assert b["n_identical"] >= 4


def test_leg6_falsifiability_pair1_rejected():
    # Pair 1's datum is in a proper subset -> NOT the same certificate as T411
    assert R["cert_game_pair1"]["datum_locus"] == "proper-subset"
    assert R["bridge_pair1_vs_t411"]["bridge_verdict"] == "REJECT"


def test_leg7_game_invariance_sweep_executable():
    sweep = R["cert_game_pair2"]["_sweep"]
    assert sweep["base_delta"] == "1"
    assert sweep["checks"]["boundary_permutation"] is True
    assert sweep["checks"]["irrelevant_coalition_dividend"] is True
    assert sweep["checks"]["in_R_dividend_both"] is True
    assert sweep["irrelevant_class_invariant"] is True
    # the localizer moves phi_0 but breaks symmetry -> full class is axiom-forced
    assert sweep["localizer_changes_phi"] is True
    assert sweep["localizer_breaks_symmetry"] is True
    assert sweep["full_admissible_class_forced"] is True


def test_headline_bridge_holds_on_4of5_invariance_owed():
    """The stab: the shared signature is genuinely instantiated by both, the
    verdict derives identically, 4/5 fields match, and the ONE gap is exactly
    the relabel-invariance the persona pass already flagged T411 owes."""
    b = R["bridge_pair2_vs_t411"]
    assert b["bridge_verdict"].startswith("PARTIAL-HOMOLOGY")
    assert b["divergent_fields"] == ["invariance_witness.complete"]
    assert R["bridge_pair1_vs_t411"]["bridge_verdict"] == "REJECT"
