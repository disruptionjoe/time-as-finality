"""Tests for T526: S1 reference-law gap audit."""

from __future__ import annotations

import unittest

from models.t526_s1_reference_law_gap_audit import (
    VERDICT,
    run_t526_analysis,
)


class S1ReferenceLawGapAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t526_analysis()
        cls.decisions = {
            decision.packet_id: decision
            for decision in cls.result.law_packet_decisions
        }

    def test_reference_law_passes_repaired_suite(self) -> None:
        self.assertTrue(self.result.reference_law_passes_repaired_suite)
        self.assertEqual(self.result.reference_sample_count, 32)
        self.assertEqual(self.result.reference_pass_count, 32)
        self.assertEqual(self.result.reference_pass_rate.numerator, 1)
        self.assertEqual(self.result.reference_pass_rate.denominator, 1)

    def test_current_finite_colimits_still_do_not_survive(self) -> None:
        self.assertFalse(self.result.current_finite_colimits_survive_repaired_suite)
        self.assertEqual(self.result.current_finite_colimit_survivor_count, 0)
        current = self.decisions["current_t249_t252_finite_colimit_route"]
        self.assertEqual(current.classification, "rejected_repaired_suite_failure")
        self.assertIn("repaired_suite_pass", current.missing_requirements)

    def test_external_reference_is_calibration_only(self) -> None:
        reference = self.decisions["external_1p1_causal_diamond_reference_law"]
        self.assertEqual(
            reference.classification,
            "calibration_only_external_reference_law",
        )
        self.assertFalse(reference.counts_as_s1_evidence)
        self.assertFalse(self.result.external_reference_counts_as_s1_evidence)
        self.assertIn("finality_colimit_descent", reference.missing_requirements)
        self.assertIn(
            "no_imported_lorentzian_coordinates",
            reference.missing_requirements,
        )

    def test_circular_and_promotion_shortcuts_blocked(self) -> None:
        conditioned = self.decisions["screen_conditioned_survivor_law"]
        self.assertEqual(conditioned.classification, "rejected_screen_conditioned_generator")
        self.assertIn(
            "not_conditioned_on_repaired_suite_success",
            conditioned.missing_requirements,
        )

        shortcut = self.decisions["lorentzian_import_promotion_shortcut"]
        self.assertEqual(shortcut.classification, "blocked_s1_promotion_shortcut")
        self.assertFalse(shortcut.counts_as_s1_evidence)

    def test_future_taf_native_target_is_review_only(self) -> None:
        future = self.decisions["future_taf_native_generator_bridge_target"]
        self.assertEqual(
            future.classification,
            "admitted_future_taf_native_generator_review_target",
        )
        self.assertTrue(future.admitted_as_future_review_target)
        self.assertFalse(future.counts_as_s1_evidence)
        self.assertTrue(self.result.taf_native_future_target_admitted)

    def test_verdict_and_scope_language(self) -> None:
        self.assertEqual(self.result.verdict, VERDICT)
        self.assertIn("S1 remains `requires_added_assumption`", self.result.s1_update)
        self.assertIn("No claim row", self.result.claim_ledger_update)
        self.assertIn("does not derive spacetime", self.result.not_claimed)
        self.assertIn("finality-native generator", self.result.missing_object)


if __name__ == "__main__":
    unittest.main()
