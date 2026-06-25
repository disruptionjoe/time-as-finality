"""Tests for T226 coefficient-aware Cech-H1 continuum-obstruction object.

Real checks of the two claims:
  (1) coefficient-aware H1 reports NO global section on the Mobius witness
      exactly where the T222 coefficient-blind encoding falsely reports one;
      cylinder control reports a section under both.
  (2) the H1 obstruction class agrees with PO1 AC6 iff the AC5 transition data
      is retained.
Plus structural checks on the cochain machinery (coboundary, cocycle, exhaustive
coboundary search) so the H1 is genuinely computed, not asserted.
"""

from models.coefficient_sheaf_h1 import (
    annular_cover,
    coboundary_d0,
    compare_to_po1,
    h1_verdict,
    is_cocycle,
    mobius_two_set_nerve,
    monodromy_sign,
    run_t226_analysis,
    transition_is_coboundary,
    z2_add,
    z2_to_sign,
    sign_to_z2,
)


# --- Z2 algebra ------------------------------------------------------------


def test_z2_addition_is_xor():
    assert z2_add(0, 0) == 0
    assert z2_add(0, 1) == 1
    assert z2_add(1, 0) == 1
    assert z2_add(1, 1) == 0


def test_z2_sign_isomorphism():
    assert z2_to_sign(0) == 1 and z2_to_sign(1) == -1
    assert sign_to_z2(1) == 0 and sign_to_z2(-1) == 1


# --- Cochain machinery -----------------------------------------------------


def test_coboundary_of_zero_frame_is_zero_cochain():
    nerve = annular_cover(4, reversed_edges=set())
    f = {i: 0 for i in range(4)}
    d0 = coboundary_d0(nerve, f)
    assert all(v == 0 for v in d0.values())


def test_thin_cover_transition_is_always_a_cocycle():
    # no triple overlaps -> cocycle condition vacuous -> always valid
    assert is_cocycle(annular_cover(4, reversed_edges={(3, 0)}))
    assert is_cocycle(annular_cover(5, reversed_edges=set()))


def test_cocycle_check_fires_on_a_bad_triple():
    # construct a nerve WITH a triple overlap violating the cocycle condition
    from models.coefficient_sheaf_h1 import CoverNerve

    bad = CoverNerve(
        opens=("U0", "U1", "U2"),
        overlaps=((0, 1), (1, 2), (0, 2)),
        triples=((0, 1, 2),),
        transition={(0, 1): 1, (1, 2): 0, (0, 2): 0},  # 1+0+0 = 1 != 0
    )
    assert is_cocycle(bad) is False


def test_cocycle_check_passes_on_a_good_triple():
    from models.coefficient_sheaf_h1 import CoverNerve

    good = CoverNerve(
        opens=("U0", "U1", "U2"),
        overlaps=((0, 1), (1, 2), (0, 2)),
        triples=((0, 1, 2),),
        transition={(0, 1): 1, (1, 2): 1, (0, 2): 0},  # 1+1+0 = 0
    )
    assert is_cocycle(good) is True
    # this g IS a coboundary (a consistent global frame exists)
    assert transition_is_coboundary(good) is True


# --- Mobius vs cylinder: the core continuum-obstruction distinction --------


def test_mobius_loop_sign_is_minus_one():
    assert monodromy_sign(annular_cover(4, reversed_edges={(3, 0)})) == -1


def test_cylinder_loop_sign_is_plus_one():
    assert monodromy_sign(annular_cover(4, reversed_edges=set())) == 1


def test_mobius_class_is_nontrivial_no_global_section():
    v = h1_verdict(annular_cover(4, reversed_edges={(3, 0)}), "mobius")
    assert v.coefficient_aware_class_trivial is False  # [g] != 0
    assert v.has_global_section_aware is False
    assert v.is_valid_cocycle is True


def test_cylinder_class_is_trivial_global_section_exists():
    v = h1_verdict(annular_cover(4, reversed_edges=set()), "cylinder")
    assert v.coefficient_aware_class_trivial is True  # [g] == 0
    assert v.has_global_section_aware is True


def test_even_number_of_reversals_is_trivial():
    # two reversals on a 4-cycle -> net +1 -> trivial class (still orientable)
    v = h1_verdict(annular_cover(4, reversed_edges={(0, 1), (3, 0)}), "two_rev")
    assert v.loop_sign == 1
    assert v.coefficient_aware_class_trivial is True


def test_blind_encoding_reports_false_section_on_mobius():
    # this is the T222 false-section trap that T226 closes
    v = h1_verdict(annular_cover(4, reversed_edges={(3, 0)}), "mobius")
    assert v.blind_reports_section is True       # blind: section exists (false)
    assert v.coefficient_aware_class_trivial is False  # aware: no section (true)
    assert v.blind_is_false_section is True


def test_blind_and_aware_agree_on_cylinder():
    v = h1_verdict(annular_cover(4, reversed_edges=set()), "cylinder")
    assert v.blind_reports_section is True
    assert v.coefficient_aware_class_trivial is True
    assert v.blind_is_false_section is False  # not false: both say section


def test_single_overlap_has_trivial_h1_no_cycle():
    # KEY HONEST FINDING: a single overlap (2-set cover, one 1-simplex, NO cycle)
    # can NEVER carry a nontrivial H1 class. g(0,1)=1 is always the coboundary of
    # f=(0,1). Cohomology of an interval/tree nerve is trivial. So the genuine
    # coefficient-aware H1 reports a SECTION on the 2-set form -- even with the
    # reversal -- because there is no cover CYCLE for the twist to obstruct.
    # This exposes that T222's single-overlap "obstruction" was a CSP
    # direct-parity-conflict artifact (two edges on one pair), NOT a real H1
    # class. The real obstruction requires the annular wrap (a cover cycle).
    v = h1_verdict(mobius_two_set_nerve(), "mobius_2set")
    assert v.coefficient_aware_class_trivial is True   # trivial: no cycle
    assert v.loop_sign == -1                            # the twist is present
    assert v.blind_is_false_section is False            # both report a section here


# --- AC1-AC7 comparison ----------------------------------------------------


def test_aware_h1_agrees_with_po1_ac6_when_ac5_retained():
    c = compare_to_po1(annular_cover(4, reversed_edges={(3, 0)}), "mobius", retain_ac5=True)
    assert c.ac5_transition_retained is True
    assert c.ac6_restricted_obstructed is True   # PO1: restricted system obstructed
    assert c.h1_obstructed is True               # aware H1: obstructed
    assert c.agrees_with_po1 is True
    assert c.ac7_source_satisfiable is True       # each patch locally orientable


def test_blind_h1_disagrees_with_po1_when_ac5_forgotten():
    c = compare_to_po1(annular_cover(4, reversed_edges={(3, 0)}), "mobius", retain_ac5=False)
    assert c.ac5_transition_retained is False
    assert c.ac6_restricted_obstructed is True   # PO1 ground truth still flags it
    assert c.h1_obstructed is False              # blind H1 lost it
    assert c.agrees_with_po1 is False            # the false-section trap


def test_cylinder_no_obstruction_under_po1_or_h1():
    c = compare_to_po1(annular_cover(4, reversed_edges=set()), "cylinder", retain_ac5=True)
    assert c.ac6_restricted_obstructed is False
    assert c.h1_obstructed is False
    assert c.agrees_with_po1 is True


# --- Top-level verdict -----------------------------------------------------


def test_t226_closes_false_section_trap():
    res = run_t226_analysis()
    assert res.closes_false_section_trap is True


def test_t226_aware_agrees_blind_loses():
    res = run_t226_analysis()
    assert res.aware_agrees_with_po1_when_ac5_retained is True
    assert res.blind_loses_obstruction_when_ac5_forgotten is True


def test_t226_overall_verdict_conditional():
    res = run_t226_analysis()
    assert res.verdict == "conditional"
