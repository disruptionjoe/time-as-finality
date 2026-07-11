"""Tests for T527: Observerse protocol-stack ablation regression harness."""

from __future__ import annotations

import unittest

from models import observerse_stack_ablation as stack
from models.run_t527 import VERDICT, build_payload


class ObserverseStackAblationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = build_payload()
        cls.rows = {row["id"]: row for row in cls.payload["rows"]}

    def test_full_stack_has_positive_sustained_coherent_structure(self) -> None:
        self.assertGreater(self.rows["full_stack"]["scs"], 1.0)

    def test_core_layer_removals_each_collapse_to_at_most_twenty_percent(self) -> None:
        for row_id in (
            "without_issuance",
            "without_admissibility",
            "without_sybil_finality",
            "without_consensus",
        ):
            with self.subTest(row_id=row_id):
                self.assertLessEqual(self.rows[row_id]["scs_ratio_to_full"], 0.20)
        self.assertTrue(self.payload["core_layers_each_earn_slot"])

    def test_governance_is_conditional_on_rule_horizon(self) -> None:
        near = self.rows["without_governance_near_term_rules"]
        full_horizon = self.rows["without_governance_full_horizon_rules"]
        self.assertLessEqual(near["scs_ratio_to_full"], 0.20)
        self.assertGreaterEqual(full_horizon["scs_ratio_to_full"], 0.95)
        self.assertTrue(self.payload["governance_conditional_visible"])
        self.assertEqual(self.payload["minimum_stack_under_near_term_governance"], 5)
        self.assertEqual(self.payload["minimum_stack_when_rules_anticipate_full_horizon"], 4)

    def test_payload_preserves_review_only_boundary(self) -> None:
        self.assertEqual(self.payload["verdict"], VERDICT)
        self.assertEqual(self.payload["grade"], "illustration_regression_only")
        self.assertFalse(self.payload["claim_status_changed"])
        self.assertFalse(self.payload["canon_verdict_changed"])
        self.assertFalse(self.payload["public_posture_changed"])
        self.assertIn("does not validate Observerse", self.payload["not_claimed"])

    def test_runner_matches_source_model_direct_values(self) -> None:
        self.assertAlmostEqual(self.rows["full_stack"]["scs"], stack.run(), places=12)
        self.assertAlmostEqual(
            self.rows["without_governance_full_horizon_rules"]["scs"],
            stack.run(governance=False, rule_fill=stack.T),
            places=12,
        )


if __name__ == "__main__":
    unittest.main()
