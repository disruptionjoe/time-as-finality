"""Tests for T534: new finality-domain law pause router."""

from __future__ import annotations

import json
import unittest

from models import t534_new_finality_domain_law_pause_router as t534


class NewFinalityDomainLawPauseRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t534.run_t534_analysis()
        cls.payload = t534.t534_result_to_dict(cls.result)
        cls.decisions = {
            decision.law_id: decision for decision in cls.result.candidate_decisions
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t534.ARTIFACT)
        self.assertEqual(self.result.verdict, t534.VERDICT)
        self.assertEqual(self.result.route_outcome, "PAUSE")
        self.assertEqual(self.result.source_t532_cleared_candidate_ids, ())

    def test_candidate_menu_excludes_forbidden_t532_shapes(self) -> None:
        candidate_ids = set(self.result.candidate_menu_ids)

        self.assertEqual(candidate_ids, {"record_window_separation_order"})
        self.assertFalse(candidate_ids & set(t534.EXCLUDED_LAW_IDS))
        self.assertIn("two_channel_receipt_product_order", self.result.excluded_law_ids)
        self.assertIn("three_channel_receipt_product_order", self.result.excluded_law_ids)
        self.assertIn("external_lorentzian_uv_reference_law", self.result.excluded_law_ids)
        self.assertIn("t528_screen_conditioned_receipt_mixture", self.result.excluded_law_ids)
        self.assertIn("posthoc_repaired_band_fit", self.result.excluded_law_ids)

    def test_record_window_law_exact_density_is_narrowed_not_cleared(self) -> None:
        decision = self.decisions["record_window_separation_order"]

        self.assertEqual(decision.outcome, "NARROWED")
        self.assertFalse(decision.clears_source_law_gate)
        self.assertFalse(decision.counts_as_s1_evidence)
        self.assertEqual(decision.expected_comparability_density.numerator, 1)
        self.assertEqual(decision.expected_comparability_density.denominator, 3)
        self.assertEqual(decision.target_comparability_density, t534.TARGET_COMPARABILITY_DENSITY)
        self.assertEqual(decision.missing_requirements, ())

    def test_exact_endpoint_enumeration_supports_density(self) -> None:
        patterns = self.result.endpoint_patterns
        comparable = tuple(pattern for pattern in patterns if pattern.relation != "incomparable")

        self.assertEqual(len(patterns), 6)
        self.assertEqual(len(comparable), 2)
        self.assertEqual(t534.record_window_expected_density().numerator, 1)
        self.assertEqual(t534.record_window_expected_density().denominator, 3)

    def test_outcomes_are_from_allowed_classifier_set(self) -> None:
        self.assertIn(self.result.route_outcome, t534.ALLOWED_OUTCOMES)
        for decision in self.result.candidate_decisions:
            self.assertIn(decision.outcome, t534.ALLOWED_OUTCOMES)

    def test_pause_language_preserves_difficulty_boundary(self) -> None:
        text = json.dumps(self.payload, sort_keys=True)

        self.assertIn("Difficulty alone is not falsification", text)
        self.assertIn("should pause until a new finality-domain source law exists", text)
        self.assertIn("S1 remains `requires_added_assumption`", text)
        self.assertEqual(self.result.cleared_candidate_ids, ())

    def test_claim_labels_include_computed_and_argued_confidence(self) -> None:
        labels = {(claim["label"], claim["confidence"]) for claim in self.payload["claim_labels"]}

        self.assertIn(("COMPUTED", "high"), labels)
        self.assertIn(("ARGUED", "medium"), labels)

    def test_json_markdown_and_forbidden_movement_absent(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t534.render_markdown(self.payload)

        self.assertIn("- Route outcome: `PAUSE`", markdown)
        self.assertIn("`record_window_separation_order`", markdown)
        self.assertIn("## Claim Labels", markdown)
        banned = (
            "S1 promoted",
            "claim status changed",
            "canon movement authorized",
            "public posture changed",
            "external publication authorized",
            "cross-repo truth proved",
        )
        for term in banned:
            self.assertNotIn(term, dumped)


if __name__ == "__main__":
    unittest.main()
