"""Tests for T415: Admissibility-Derivation Probe (bridge obligation #2).

Asserts the predeclared legs of tests/T415-admissibility-derivation-probe.md
(frozen before the model existed). Exploratory; no claim promotion; ledger
untouched. Reuses the registered T412 gate machinery. Cross-domain material is
object of study, not evidence.
"""

from models.admissibility_derivation_probe import run

R = run()


def test_leg1_baseline_reproduces_T412():
    b = R["baseline_reproduces_T412"]
    assert b["max_proper_subset_td"] == 0.0
    assert b["full_joint_td"] == 1.0


def test_leg2_equality_iff_global_parity():
    # the two independently defined predicates induce the SAME partition
    assert R["leg2_equality_iff_global_parity"] is True


def test_leg3_counts():
    c = R["counts"]
    assert c["GL_3_2"] == 168
    assert c["equality_preserving"] == 24          # stabilizer of the parity functional
    assert c["global_parity_preserving"] == 24
    assert c["product_preserving_permutations"] == 6


def test_leg4_teeth_equality_strictly_broader_than_product():
    # THE TEETH: 18 entangling maps preserve the equality -> P1 != product-preservation
    assert R["counts"]["entangling_equality_preserving"] == 18
    ex = R["leg4_teeth_entangling_equality_preserver"]
    assert ex["is_permutation"] is False           # entangling
    assert ex["global_parity_preserving"] is True
    assert ex["equality_preserving"] is True        # preserves the equality
    assert ex["max_proper_subset_td"] == 0.0
    # and the fan-in breaks it (localizes)
    fi = R["leg4_fanin_breaks_equality"]
    assert fi["global_parity_preserving"] is False
    assert fi["max_proper_subset_td"] == 1.0
    assert fi["factor0_td"] == 1.0


def test_leg5_P1_is_circular():
    c = R["leg5_P1_circularity"]
    # full-joint TD invariant under every relabel -> equality-preservation tautological
    assert c["full_joint_td_invariant_under_all_relabels"] is True
    assert c["equality_preservation_is_tautological"] is True


def test_leg6_P2_operational_automorphism_is_the_port():
    p = R["leg6_P2_operational_automorphism"]
    assert p["separator_survives"] is True
    assert p["is_free_declaration"] is False
    assert p["is_operational_commitment"] is True
    assert p["physicality_reduces_to"].startswith("R2")


def test_headline_bridge2_structural_not_physical():
    """Bridge obligation #2: structurally bridged (game symmetry axiom <-> quantum
    operational-automorphism admissibility), P1 refuted as circular (18 entangling
    equality-preservers), physicality still bottomed at R2."""
    assert R["counts"]["entangling_equality_preserving"] == 18
    assert R["leg5_P1_circularity"]["equality_preservation_is_tautological"] is True
    assert R["leg6_P2_operational_automorphism"]["physicality_reduces_to"].startswith("R2")
