"""Tests for T56: Sheaf Cohomology of Apparent Finality — Research Audit."""

from __future__ import annotations

import unittest

from models.sheaf_cohomology_apparent_finality import (
    AuditOutcome,
    CircularRisk,
    _build_dense_cover,
    _build_hidden_intermediary_cover,
    _build_no_phantom_cover,
    check_ambient_presheaf_functoriality,
    check_apparent_presheaf_closure,
    check_section_compatibility,
    compute_apparent_order,
    compute_cech_complex,
    compute_global_order,
    detect_phantom_pairs,
    restrict_order,
    run_t56_audit,
)


class GlobalOrderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cover = _build_hidden_intermediary_cover()
        self.order = compute_global_order(self.cover)
        self.nr = {(a, b) for (a, b) in self.order if a != b}

    def test_ej_leq_ek(self) -> None:
        self.assertIn(("e_j", "e_k"), self.nr)

    def test_ek_leq_ei(self) -> None:
        self.assertIn(("e_k", "e_i"), self.nr)

    def test_ej_leq_ei_transitive(self) -> None:
        self.assertIn(("e_j", "e_i"), self.nr)

    def test_no_spurious_edges(self) -> None:
        # No upward edges
        self.assertNotIn(("e_k", "e_j"), self.nr)
        self.assertNotIn(("e_i", "e_j"), self.nr)
        self.assertNotIn(("e_i", "e_k"), self.nr)


class ApparentOrderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cover = _build_hidden_intermediary_cover()
        patches = {p.name: p for p in self.cover.patches}
        self.u_p = patches["U_P"]
        self.u_a = patches["U_A"]
        self.u_b = patches["U_B"]

    def test_up_sees_ej_and_ei(self) -> None:
        acc = self.cover.accessible_event_names(self.u_p)
        self.assertIn("e_j", acc)
        self.assertIn("e_i", acc)
        self.assertNotIn("e_k", acc)

    def test_up_apparent_order_has_no_nonrefl_pairs(self) -> None:
        # e_j || e_i at U_P: no direct record dependency visible
        order = compute_apparent_order(self.cover, self.u_p)
        nr = {(a, b) for (a, b) in order if a != b}
        self.assertEqual(nr, set())

    def test_ua_sees_ej_leq_ek(self) -> None:
        order = compute_apparent_order(self.cover, self.u_a)
        nr = {(a, b) for (a, b) in order if a != b}
        self.assertIn(("e_j", "e_k"), nr)

    def test_ub_sees_ek_leq_ei(self) -> None:
        order = compute_apparent_order(self.cover, self.u_b)
        nr = {(a, b) for (a, b) in order if a != b}
        self.assertIn(("e_k", "e_i"), nr)

    def test_ua_does_not_see_ei(self) -> None:
        acc = self.cover.accessible_event_names(self.u_a)
        self.assertNotIn("e_i", acc)

    def test_ub_does_not_see_ej(self) -> None:
        acc = self.cover.accessible_event_names(self.u_b)
        self.assertNotIn("e_j", acc)


class AmbientPresheafTests(unittest.TestCase):
    def test_ambient_is_functorial(self) -> None:
        cover = _build_hidden_intermediary_cover()
        global_order = compute_global_order(cover)
        check = check_ambient_presheaf_functoriality(cover, global_order)
        self.assertTrue(check.is_functorial)

    def test_ambient_functorial_no_violation(self) -> None:
        cover = _build_hidden_intermediary_cover()
        global_order = compute_global_order(cover)
        check = check_ambient_presheaf_functoriality(cover, global_order)
        self.assertEqual(check.violation_example, "")

    def test_ambient_also_functorial_for_no_phantom_cover(self) -> None:
        cover = _build_no_phantom_cover()
        global_order = compute_global_order(cover)
        check = check_ambient_presheaf_functoriality(cover, global_order)
        self.assertTrue(check.is_functorial)


class ApparentPresheafClosureTests(unittest.TestCase):
    def test_apparent_is_not_presheaf_for_phantom_cover(self) -> None:
        cover = _build_hidden_intermediary_cover()
        global_order = compute_global_order(cover)
        check = check_apparent_presheaf_closure(cover, global_order)
        self.assertFalse(check.is_functorial)

    def test_apparent_violation_involves_phantom_pair(self) -> None:
        cover = _build_hidden_intermediary_cover()
        global_order = compute_global_order(cover)
        check = check_apparent_presheaf_closure(cover, global_order)
        self.assertIn("phantom", check.explanation.lower())

    def test_apparent_is_presheaf_when_no_phantom(self) -> None:
        cover = _build_no_phantom_cover()
        global_order = compute_global_order(cover)
        check = check_apparent_presheaf_closure(cover, global_order)
        self.assertTrue(check.is_functorial)


class PhantomPairTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cover = _build_hidden_intermediary_cover()
        self.global_order = compute_global_order(self.cover)
        self.phantoms = detect_phantom_pairs(self.cover, self.global_order)

    def test_phantom_detected_at_up(self) -> None:
        observers = [p.observer for p in self.phantoms]
        self.assertIn("U_P", observers)

    def test_phantom_pair_is_ej_ei(self) -> None:
        up_phantoms = [p for p in self.phantoms if p.observer == "U_P"]
        pairs = {(p.event_j, p.event_i) for p in up_phantoms}
        self.assertIn(("e_j", "e_i"), pairs)

    def test_hidden_intermediary_is_ek(self) -> None:
        p = next(
            ph for ph in self.phantoms
            if ph.observer == "U_P" and ph.event_j == "e_j" and ph.event_i == "e_i"
        )
        self.assertIn("e_k", p.hidden_intermediaries)

    def test_no_phantom_at_ua(self) -> None:
        observers = [p.observer for p in self.phantoms]
        self.assertNotIn("U_A", observers)

    def test_no_phantom_at_ub(self) -> None:
        observers = [p.observer for p in self.phantoms]
        self.assertNotIn("U_B", observers)

    def test_no_phantom_in_no_phantom_cover(self) -> None:
        cover = _build_no_phantom_cover()
        global_order = compute_global_order(cover)
        phantoms = detect_phantom_pairs(cover, global_order)
        self.assertEqual(len(phantoms), 0)


class SectionCompatibilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cover = _build_hidden_intermediary_cover()
        self.global_order = compute_global_order(self.cover)
        self.result = check_section_compatibility(self.cover, self.global_order)

    def test_local_sections_not_compatible(self) -> None:
        self.assertFalse(self.result.local_sections_compatible)

    def test_colimit_is_global_section(self) -> None:
        self.assertTrue(self.result.colimit_section_compatible)

    def test_incompatibility_witnesses_exist(self) -> None:
        self.assertGreater(len(self.result.incompatibility_witnesses), 0)

    def test_finding_mentions_h0(self) -> None:
        self.assertIn("H⁰", self.result.finding)

    def test_no_incompatibility_in_no_phantom_cover(self) -> None:
        cover = _build_no_phantom_cover()
        global_order = compute_global_order(cover)
        result = check_section_compatibility(cover, global_order)
        self.assertTrue(result.local_sections_compatible)


class CechH1Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.cover = _build_hidden_intermediary_cover()
        self.global_order = compute_global_order(self.cover)

    def test_apparent_h1_is_zero_in_sparse_cover(self) -> None:
        h1 = compute_cech_complex(self.cover, self.global_order, use_apparent_for_local=True)
        self.assertEqual(h1.h1_dimension, 0)

    def test_ambient_h1_is_zero(self) -> None:
        h1 = compute_cech_complex(self.cover, self.global_order, use_apparent_for_local=False)
        self.assertEqual(h1.h1_dimension, 0)

    def test_apparent_c1_is_zero_in_sparse_cover(self) -> None:
        # All pairwise overlaps have at most one accessible event → no non-reflexive pairs
        h1 = compute_cech_complex(self.cover, self.global_order, use_apparent_for_local=True)
        self.assertEqual(h1.c1_dimension, 0)

    def test_phantom_does_not_generate_h1_in_sparse_cover(self) -> None:
        h1 = compute_cech_complex(self.cover, self.global_order, use_apparent_for_local=True)
        self.assertFalse(h1.phantom_generates_h1)

    def test_h1_finding_mentions_section_compatibility(self) -> None:
        h1 = compute_cech_complex(self.cover, self.global_order, use_apparent_for_local=True)
        self.assertIn("H⁰", h1.finding)


class DenseCoverTests(unittest.TestCase):
    """
    The dense cover {U_P, U_full} has a non-trivial overlap U_P ∩ U_full = U_P.
    This tests whether the phantom pair (e_j, e_i) can appear in H¹ with a richer cover.
    """

    def setUp(self) -> None:
        self.cover = _build_dense_cover()
        self.global_order = compute_global_order(self.cover)

    def test_dense_cover_has_two_patches(self) -> None:
        self.assertEqual(len(self.cover.patches), 2)

    def test_up_still_has_phantom_in_dense_cover(self) -> None:
        phantoms = detect_phantom_pairs(self.cover, self.global_order)
        up_phantoms = [p for p in phantoms if p.observer == "U_P"]
        self.assertTrue(len(up_phantoms) > 0)

    def test_dense_cover_overlap_has_two_accessible_events(self) -> None:
        patches = {p.name: p for p in self.cover.patches}
        overlap = self.cover.overlap_patch(patches["U_P"], patches["U_full"])
        acc = self.cover.accessible_event_names(overlap)
        self.assertEqual(len(acc), 2)  # e_j and e_i (not e_k, which needs r2)


class AssumptionLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t56_audit()
        self.ledger = {e.name: e for e in self.result.assumption_ledger}

    def test_arrow_direction_has_medium_risk(self) -> None:
        self.assertEqual(
            self.ledger["arrow_direction"].circular_risk, CircularRisk.MEDIUM
        )

    def test_record_dependency_has_medium_risk(self) -> None:
        self.assertEqual(
            self.ledger["record_dependency_order"].circular_risk, CircularRisk.MEDIUM
        )

    def test_accessible_records_has_low_risk(self) -> None:
        self.assertEqual(
            self.ledger["accessible_records"].circular_risk, CircularRisk.LOW
        )

    def test_observer_cover_has_no_risk(self) -> None:
        self.assertEqual(
            self.ledger["observer_cover"].circular_risk, CircularRisk.NONE
        )

    def test_z2_encoding_has_no_risk(self) -> None:
        self.assertEqual(
            self.ledger["z2_encoding"].circular_risk, CircularRisk.NONE
        )

    def test_no_high_risk_entries(self) -> None:
        high_risk = [e for e in self.result.assumption_ledger
                     if e.circular_risk == CircularRisk.HIGH]
        self.assertEqual(len(high_risk), 0)

    def test_f_not_presheaf_is_derived(self) -> None:
        from models.sheaf_cohomology_apparent_finality import AssumptionStatus
        self.assertEqual(
            self.ledger["f_not_presheaf"].status, AssumptionStatus.DERIVED
        )

    def test_gap_presheaf_is_conjectural(self) -> None:
        from models.sheaf_cohomology_apparent_finality import AssumptionStatus
        self.assertEqual(
            self.ledger["gap_presheaf"].status, AssumptionStatus.CONJECTURAL
        )


class FullAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t56_audit()

    def test_outcome_is_partial_success(self) -> None:
        self.assertEqual(self.result.outcome, AuditOutcome.PARTIAL_SUCCESS)

    def test_ambient_presheaf_is_functorial(self) -> None:
        self.assertTrue(self.result.ambient_presheaf_check.is_functorial)

    def test_apparent_assignment_is_not_presheaf(self) -> None:
        self.assertFalse(self.result.apparent_presheaf_check.is_functorial)

    def test_phantom_pairs_detected(self) -> None:
        self.assertGreater(len(self.result.phantom_pairs), 0)

    def test_local_sections_not_compatible(self) -> None:
        self.assertFalse(self.result.section_compatibility.local_sections_compatible)

    def test_colimit_is_global_section(self) -> None:
        self.assertTrue(self.result.section_compatibility.colimit_section_compatible)

    def test_h1_ambient_is_zero(self) -> None:
        self.assertEqual(self.result.cech_h1_ambient.h1_dimension, 0)

    def test_h1_apparent_is_zero_in_sparse_cover(self) -> None:
        self.assertEqual(self.result.cech_h1_apparent.h1_dimension, 0)

    def test_refined_hypothesis_mentions_h0_gap(self) -> None:
        self.assertIn("H⁰", self.result.refined_hypothesis)
        self.assertIn("gap", self.result.refined_hypothesis.lower())

    def test_finding_mentions_partial_success(self) -> None:
        self.assertIn("PARTIAL_SUCCESS", self.result.finding)

    def test_four_open_questions(self) -> None:
        self.assertEqual(len(self.result.open_questions), 4)

    def test_finding_mentions_h0_level(self) -> None:
        self.assertIn("H⁰", self.result.finding)

    def test_assumption_ledger_has_ten_entries(self) -> None:
        self.assertEqual(len(self.result.assumption_ledger), 10)


if __name__ == "__main__":
    unittest.main()
