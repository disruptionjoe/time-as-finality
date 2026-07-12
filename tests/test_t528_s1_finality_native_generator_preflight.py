"""Tests for T528: S1 finality-native generator preflight."""

from __future__ import annotations

import unittest

from models.t528_s1_finality_native_generator_preflight import (
    VERDICT,
    run_t528_analysis,
    t528_result_to_dict,
)
from models.run_t528 import _render_markdown


class S1FinalityNativeGeneratorPreflightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t528_analysis()
        cls.decisions = {
            decision.packet_id: decision
            for decision in cls.result.packet_decisions
        }
        cls.summary_by_size = {
            summary.event_count: summary
            for summary in cls.result.pass_summary_by_size
        }

    def test_two_receipt_generator_is_executed_but_incomplete(self) -> None:
        self.assertEqual(self.result.sample_count, 32)
        self.assertEqual(self.result.pass_count, 25)
        self.assertEqual(self.result.pass_rate.numerator, 25)
        self.assertEqual(self.result.pass_rate.denominator, 32)
        self.assertEqual(
            self.result.main_packet_classification,
            "rejected_repaired_suite_incomplete",
        )

    def test_pass_summary_keeps_multi_size_burden_visible(self) -> None:
        expected = {
            8: (7, 8),
            12: (5, 8),
            16: (8, 8),
            20: (5, 8),
        }
        for event_count, (pass_count, sample_count) in expected.items():
            summary = self.summary_by_size[event_count]
            self.assertEqual(summary.pass_count, pass_count)
            self.assertEqual(summary.sample_count, sample_count)

    def test_hostile_controls_are_rejected(self) -> None:
        self.assertTrue(self.result.hostile_controls_rejected)
        self.assertTrue(self.result.hostile_control_audits)
        for audit in self.result.hostile_control_audits:
            self.assertFalse(audit.repaired_suite_passed)

    def test_shortcuts_are_blocked(self) -> None:
        conditioned = self.decisions["screen_conditioned_survivor_law"]
        self.assertEqual(conditioned.classification, "rejected_screen_conditioned_generator")
        self.assertIn(
            "not_conditioned_on_repaired_suite_success",
            conditioned.missing_requirements,
        )

        shortcut = self.decisions["lorentzian_import_promotion_shortcut"]
        self.assertEqual(shortcut.classification, "blocked_s1_promotion_shortcut")
        self.assertFalse(shortcut.counts_as_s1_evidence)

    def test_future_full_burden_packet_is_review_only(self) -> None:
        future = self.decisions["future_full_burden_generator_packet"]
        self.assertEqual(
            future.classification,
            "admitted_future_full_burden_review_target",
        )
        self.assertTrue(future.admitted_as_future_review_target)
        self.assertFalse(future.counts_as_s1_evidence)

    def test_verdict_and_boundary_language(self) -> None:
        self.assertEqual(self.result.verdict, VERDICT)
        self.assertFalse(self.result.main_packet_counts_as_s1_evidence)
        self.assertIn("S1 remains `requires_added_assumption`", self.result.s1_update)
        self.assertIn("No claim-ledger update is earned", self.result.claim_ledger_update)
        self.assertIn("does not derive spacetime", self.result.not_claimed)

    def test_generated_markdown_reports_unreduced_sample_counts(self) -> None:
        markdown = _render_markdown(t528_result_to_dict(self.result))

        self.assertIn(
            "- Repaired-suite samples passing: 25/32 (0.7812)",
            markdown,
        )
        self.assertNotIn("25/32 (25/32", markdown)
        self.assertIn("| 16 | 8 | 8 | 8/8 (1.0000) |", markdown)


if __name__ == "__main__":
    unittest.main()
