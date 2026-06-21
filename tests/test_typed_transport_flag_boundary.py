"""Tests for the RL-004 preservation-flag boundary audit."""

from __future__ import annotations

import unittest

from models.typed_transport_flag_boundary import (
    FlagBoundaryAudit,
    flag_boundary_audit_to_dict,
    run_flag_boundary_audit,
)


class TestFlagBoundaryAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_flag_boundary_audit()

    def test_returns_audit(self):
        self.assertIsInstance(self.result, FlagBoundaryAudit)

    def test_t41_skeleton_category_still_preserved(self):
        self.assertTrue(self.result.t41_skeleton_category_preserved)

    def test_flagged_category_unproved(self):
        self.assertTrue(self.result.flagged_morphism_category_unproved)

    def test_composition_erases_preservation_flags(self):
        check = self.result.composition_check
        self.assertEqual(check.original_flags, (True, True))
        self.assertEqual(check.composed_flags, (False, False))
        self.assertFalse(check.flag_equal)

    def test_left_unit_erases_preservation_flags(self):
        check = self.result.left_unit_check
        self.assertTrue(check.skeleton_equal_modulo_name)
        self.assertFalse(check.flag_equal)

    def test_right_unit_erases_preservation_flags(self):
        check = self.result.right_unit_check
        self.assertTrue(check.skeleton_equal_modulo_name)
        self.assertFalse(check.flag_equal)

    def test_boundary_mentions_t41(self):
        self.assertIn("T41", self.result.boundary)

    def test_recommendation_does_not_select_semantics(self):
        recommendation = self.result.recommendation.lower()
        self.assertIn("future", recommendation)
        self.assertIn("define", recommendation)

    def test_serializes_to_dict(self):
        data = flag_boundary_audit_to_dict(self.result)
        self.assertIsInstance(data, dict)
        self.assertIn("flagged_morphism_category_unproved", data)


if __name__ == "__main__":
    unittest.main()
