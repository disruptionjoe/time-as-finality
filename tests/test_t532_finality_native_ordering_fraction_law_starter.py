"""Tests for T532: finality-native ordering-fraction law starter."""

from __future__ import annotations

import json
import unittest

from models import t532_finality_native_ordering_fraction_law_starter as t532
from models.run_t532 import _render_markdown


class FinalityNativeOrderingFractionLawStarterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t532.run_t532_analysis()
        cls.decisions = {
            decision.law_id: decision for decision in cls.result.candidate_decisions
        }

    def test_t531_route_and_t528_negative_evidence_are_preserved(self) -> None:
        self.assertEqual(self.result.artifact, t532.ARTIFACT)
        self.assertEqual(self.result.verdict, t532.VERDICT)
        self.assertEqual(self.result.source_t530_primary_failure_axis, "ordering_fraction")
        self.assertEqual(self.result.source_t528_pass_count, 25)
        self.assertEqual(self.result.source_t528_sample_count, 32)
        self.assertEqual(self.result.source_t528_ordering_failure_count, 6)

    def test_shortcut_classes_are_distinguished(self) -> None:
        self.assertEqual(
            self.decisions["external_lorentzian_uv_reference_law"].classification,
            "rejected_target_import",
        )
        self.assertEqual(
            self.decisions["t528_screen_conditioned_receipt_mixture"].classification,
            "rejected_screen_conditioned_law",
        )
        self.assertEqual(
            self.decisions["posthoc_repaired_band_fit"].classification,
            "rejected_post_hoc_band_fit",
        )

    def test_independent_naturality_candidates_are_negative_not_cleared(self) -> None:
        two_channel = self.decisions["two_channel_receipt_product_order"]
        three_channel = self.decisions["three_channel_receipt_product_order"]

        self.assertTrue(two_channel.independent_naturality_candidate)
        self.assertTrue(three_channel.independent_naturality_candidate)
        self.assertEqual(
            two_channel.classification,
            "negative_independent_naturality_candidate",
        )
        self.assertEqual(
            three_channel.classification,
            "negative_expected_density_mismatch",
        )
        self.assertFalse(two_channel.clears_as_real_candidate)
        self.assertFalse(three_channel.clears_as_real_candidate)

    def test_no_real_candidate_clears_and_no_s1_evidence(self) -> None:
        self.assertEqual(self.result.cleared_candidate_ids, ())
        for decision in self.result.candidate_decisions:
            self.assertFalse(decision.clears_as_real_candidate)
            self.assertFalse(decision.counts_as_s1_evidence)

    def test_missing_requirements_record_import_screen_and_posthoc_failures(self) -> None:
        imported = self.decisions["external_lorentzian_uv_reference_law"]
        screen = self.decisions["t528_screen_conditioned_receipt_mixture"]
        posthoc = self.decisions["posthoc_repaired_band_fit"]
        shortcut = self.decisions["s1_promotion_from_starter_screen"]

        self.assertIn("no_lorentzian_reference_import", imported.missing_requirements)
        self.assertIn("no_t528_screen_conditioning", screen.missing_requirements)
        self.assertIn("no_post_hoc_band_fit", posthoc.missing_requirements)
        self.assertIn(
            "no_s1_claim_canon_public_or_external_movement",
            shortcut.missing_requirements,
        )

    def test_claim_labels_include_computed_and_argued_confidence(self) -> None:
        payload = t532.t532_result_to_dict(self.result)
        labels = {(claim["label"], claim["confidence"]) for claim in payload["claim_labels"]}

        self.assertIn(("COMPUTED", "high"), labels)
        self.assertIn(("ARGUED", "medium"), labels)

    def test_generated_markdown_reports_no_clear_and_boundaries(self) -> None:
        payload = t532.t532_result_to_dict(self.result)
        markdown = _render_markdown(payload)

        self.assertIn("- Cleared real candidate ids: none", markdown)
        self.assertIn("## Claim Labels", markdown)
        self.assertIn("`COMPUTED` confidence `high`", markdown)
        self.assertIn("`ARGUED` confidence `medium`", markdown)
        self.assertIn("T532 does not derive spacetime", markdown)

    def test_json_payload_contains_no_governance_movement_language(self) -> None:
        payload = t532.t532_result_to_dict(self.result)
        dumped = json.dumps(payload, sort_keys=True)

        self.assertIn("S1 remains `requires_added_assumption`", dumped)
        banned = (
            "S1 promoted",
            "claim status changed",
            "canon movement authorized",
            "public posture changed",
            "external publication authorized",
        )
        for term in banned:
            self.assertNotIn(term, dumped)


if __name__ == "__main__":
    unittest.main()
