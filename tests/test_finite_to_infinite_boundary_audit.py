"""Tests for T59: Finite-to-Infinite Boundary Audit."""

from __future__ import annotations

import unittest

from models.finite_to_infinite_boundary_audit import (
    audit_cover_encoding,
    build_cylinder_orientation_cover,
    build_mobius_orientation_cover,
    coefficient_blind_scalar_constraints,
    run_t59_analysis,
    signed_parity_verdict,
    transition_aware_z2_constraints,
)


class OrientationCoverTests(unittest.TestCase):
    def test_mobius_cover_has_nontrivial_monodromy(self) -> None:
        cover = build_mobius_orientation_cover()
        self.assertEqual(cover.monodromy_sign, -1)
        self.assertFalse(cover.orientation_global_section_exists)
        self.assertTrue(cover.orientation_obstructed)

    def test_cylinder_control_has_trivial_monodromy(self) -> None:
        cover = build_cylinder_orientation_cover()
        self.assertEqual(cover.monodromy_sign, 1)
        self.assertTrue(cover.orientation_global_section_exists)
        self.assertFalse(cover.orientation_obstructed)


class EncodingTests(unittest.TestCase):
    def test_transition_aware_encoding_preserves_mobius_signs(self) -> None:
        constraints = transition_aware_z2_constraints(build_mobius_orientation_cover())
        relations = [constraint.relation for constraint in constraints]
        self.assertEqual(relations, ["same", "different"])

    def test_coefficient_blind_encoding_forgets_mobius_signs(self) -> None:
        constraints = coefficient_blind_scalar_constraints(build_mobius_orientation_cover())
        relations = [constraint.relation for constraint in constraints]
        self.assertEqual(relations, ["same", "same"])


class ParityBoundaryTests(unittest.TestCase):
    def test_transition_aware_parity_detects_mobius_obstruction(self) -> None:
        audit = audit_cover_encoding(build_mobius_orientation_cover(), "transition_aware_z2")
        self.assertTrue(audit.parity_obstruction_detected)
        self.assertFalse(audit.parity_global_section_exists)
        self.assertTrue(audit.parity_matches_orientation)
        self.assertFalse(audit.false_global_section)

    def test_coefficient_blind_parity_misses_mobius_obstruction(self) -> None:
        audit = audit_cover_encoding(build_mobius_orientation_cover(), "coefficient_blind_scalar")
        self.assertFalse(audit.parity_obstruction_detected)
        self.assertTrue(audit.parity_global_section_exists)
        self.assertFalse(audit.parity_matches_orientation)
        self.assertTrue(audit.false_global_section)

    def test_cylinder_control_is_satisfiable_under_both_encodings(self) -> None:
        cover = build_cylinder_orientation_cover()
        for encoding in ("transition_aware_z2", "coefficient_blind_scalar"):
            audit = audit_cover_encoding(cover, encoding)
            self.assertTrue(audit.orientation_global_section_exists)
            self.assertTrue(audit.parity_global_section_exists)
            self.assertTrue(audit.parity_matches_orientation)
            self.assertFalse(audit.false_global_section)

    def test_direct_parity_conflict_is_classified(self) -> None:
        constraints = transition_aware_z2_constraints(build_mobius_orientation_cover())
        verdict = signed_parity_verdict(constraints)
        self.assertTrue(verdict.obstruction_detected)
        self.assertEqual(verdict.obstruction_type, "direct_parity_conflict")


class FullT59AnalysisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t59_analysis()

    def test_transition_aware_detects_mobius(self) -> None:
        self.assertTrue(self.result.transition_aware_detects_mobius)

    def test_coefficient_blind_misses_mobius(self) -> None:
        self.assertTrue(self.result.coefficient_blind_misses_mobius)

    def test_cylinder_controls_pass(self) -> None:
        self.assertTrue(self.result.cylinder_controls_pass)

    def test_h0_universal_continuous_detector_is_refuted(self) -> None:
        h0 = next(h for h in self.result.hypothesis_evaluations if h.hypothesis_id == "H0")
        self.assertEqual(h0.status, "refuted")

    def test_h2_boundary_is_best_supported(self) -> None:
        h2 = next(h for h in self.result.hypothesis_evaluations if h.hypothesis_id == "H2")
        self.assertEqual(h2.status, "best_supported")

    def test_best_supported_keeps_bounded_scope(self) -> None:
        self.assertIn("transition-aware Z2 special case", self.result.best_supported)
        self.assertIn("not licensed", self.result.best_supported)


if __name__ == "__main__":
    unittest.main()
