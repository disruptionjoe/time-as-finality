"""Tests for T530: T528 generator failure router."""

from __future__ import annotations

import json
import unittest

from models import t530_t528_generator_failure_router as t530
from models.run_t530 import _render_markdown


class T528GeneratorFailureRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t530.run_t530_analysis()
        cls.decisions = {
            decision.packet_id: decision
            for decision in cls.result.packet_decisions
        }
        cls.axes = {
            summary.axis: summary
            for summary in cls.result.failure_axis_summaries
        }
        cls.sizes = {
            summary.event_count: summary
            for summary in cls.result.size_summaries
        }

    def test_t528_counts_are_preserved(self) -> None:
        self.assertEqual(self.result.artifact, t530.ARTIFACT)
        self.assertEqual(self.result.verdict, t530.VERDICT)
        self.assertEqual(self.result.t528_sample_count, 32)
        self.assertEqual(self.result.t528_pass_count, 25)
        self.assertEqual(self.result.t528_failed_count, 7)
        self.assertEqual(self.result.t528_pass_rate.numerator, 25)
        self.assertEqual(self.result.t528_pass_rate.denominator, 32)

    def test_size_failure_distribution_matches_t528(self) -> None:
        expected = {
            8: (7, 1),
            12: (5, 3),
            16: (8, 0),
            20: (5, 3),
        }
        for event_count, (pass_count, failed_count) in expected.items():
            summary = self.sizes[event_count]
            self.assertEqual(summary.pass_count, pass_count)
            self.assertEqual(summary.failed_count, failed_count)

    def test_failure_axis_ranking_names_ordering_fraction_first(self) -> None:
        self.assertEqual(self.result.primary_failure_axis, "ordering_fraction")
        self.assertEqual(self.axes["ordering_fraction"].failed_sample_count, 6)
        self.assertEqual(self.axes["height"].failed_sample_count, 3)
        self.assertEqual(self.axes["largest_interval"].failed_sample_count, 2)
        self.assertEqual(self.axes["width"].failed_sample_count, 1)
        self.assertEqual(self.result.hard_gate_failure_count, 0)
        self.assertIn("height", self.result.secondary_failure_axes)

    def test_shortcuts_and_axis_blind_packets_are_rejected(self) -> None:
        axis_blind = self.decisions["axis_blind_more_receipts"]
        screen_tuned = self.decisions["screen_tuned_receipt_mixture"]
        imported = self.decisions["lorentzian_reference_reuse"]
        height_only = self.decisions["height_only_repair"]

        self.assertEqual(axis_blind.classification, "rejected_primary_axis_not_addressed")
        self.assertEqual(screen_tuned.classification, "rejected_screen_conditioned_repair")
        self.assertEqual(imported.classification, "blocked_s1_or_claim_movement_shortcut")
        self.assertEqual(height_only.classification, "rejected_primary_axis_not_addressed")
        self.assertFalse(imported.counts_as_s1_evidence)

    def test_only_full_future_packet_shape_is_admitted(self) -> None:
        weak = self.decisions["ordering_fraction_repair_without_naturality"]
        admitted = self.decisions["predeclared_ordering_fraction_measure_law"]

        self.assertEqual(weak.classification, "rejected_missing_review_requirements")
        self.assertIn(
            "independent_naturality_or_neighbor_theory",
            weak.missing_requirements,
        )
        self.assertEqual(admitted.classification, "admitted_future_review_target")
        self.assertTrue(admitted.admitted_as_future_review_target)
        self.assertFalse(admitted.counts_as_s1_evidence)

    def test_no_governance_or_posture_movement(self) -> None:
        payload = t530.t530_result_to_dict(self.result)
        dumped = json.dumps(payload, sort_keys=True)

        self.assertIn("S1 remains `requires_added_assumption`", dumped)
        self.assertIn("No claim-ledger update is earned", dumped)
        banned = (
            "S1 promoted",
            "claim status changed",
            "canon movement authorized",
            "public posture changed",
            "external publication authorized",
        )
        for term in banned:
            self.assertNotIn(term, dumped)

    def test_generated_markdown_reports_unreduced_sample_counts(self) -> None:
        markdown = _render_markdown(t530.t530_result_to_dict(self.result))

        self.assertIn(
            "- T528 repaired-suite samples passing: 25/32 (0.7812)",
            markdown,
        )
        self.assertNotIn("25/32 (25/32", markdown)
        self.assertIn("| 16 | 8 | 8 | 0 | 8/8 (1.0000) |", markdown)


if __name__ == "__main__":
    unittest.main()
