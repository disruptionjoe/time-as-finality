"""Tests for T387 ten-persona gap audit."""

from __future__ import annotations

import unittest

from models.ten_persona_gap_audit import run_t387_analysis


class TenPersonaGapAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t387_analysis()
        self.gaps = {gap.gap_id: gap for gap in self.result.gap_syntheses}

    def test_exactly_ten_unique_personas_are_present(self) -> None:
        persona_ids = [lens.persona_id for lens in self.result.persona_lenses]
        self.assertEqual(self.result.persona_count, 10)
        self.assertEqual(len(persona_ids), 10)
        self.assertEqual(len(set(persona_ids)), 10)
        self.assertIn("mathematical_formalist", persona_ids)
        self.assertIn("paper_reviewer", persona_ids)

    def test_every_persona_contributes_at_least_one_finding(self) -> None:
        lens_ids = {lens.persona_id for lens in self.result.persona_lenses}
        finding_ids = {finding.persona_id for finding in self.result.persona_findings}
        self.assertEqual(lens_ids, finding_ids)
        self.assertEqual(self.result.finding_count, 20)

    def test_audit_finds_missing_items_but_no_claim_upgrade(self) -> None:
        self.assertTrue(self.result.missing_anything)
        self.assertFalse(self.result.claim_upgrade_allowed)
        self.assertEqual(
            self.result.overall_verdict,
            "ten_persona_audit_finds_no_claim_upgrade_but_prioritizes_mutual_attestability_semantics",
        )

    def test_top_gaps_prioritize_mutuality_nullness_bridge_and_minimality(self) -> None:
        self.assertEqual(
            self.result.top_gap_ids,
            (
                "mutual_attestability_semantics_origin",
                "nullness_bilinearity_origin",
                "two_leg_to_null_signal_bridge",
                "minimality_principle_origin",
                "local_to_global_attestation_descent",
            ),
        )
        self.assertIn("mutual_attestability_semantics_origin", self.gaps)
        self.assertIn("nullness_bilinearity_origin", self.gaps)
        self.assertIn("two_leg_to_null_signal_bridge", self.gaps)

    def test_mutual_attestability_gap_has_multiple_supporting_personas(self) -> None:
        gap = self.gaps["mutual_attestability_semantics_origin"]
        self.assertEqual(gap.status, "top_priority")
        self.assertGreaterEqual(gap.severity_score, 15)
        self.assertEqual(
            set(gap.supporting_personas),
            {
                "mathematical_formalist",
                "distributed_systems_engineer",
                "paper_reviewer",
            },
        )
        self.assertIn("record-finality", gap.recommended_action)

    def test_known_open_gaps_are_not_mistaken_for_new_breaks(self) -> None:
        self.assertIn("nullness_bilinearity_origin", self.result.known_open_gap_ids)
        self.assertIn("higher_dimensional_extension", self.result.known_open_gap_ids)
        self.assertIn("catalog_completeness_boundary", self.result.known_open_gap_ids)
        self.assertEqual(self.gaps["nullness_bilinearity_origin"].status, "known_open_object")
        self.assertEqual(self.gaps["higher_dimensional_extension"].status, "known_open_object")

    def test_security_and_hidden_order_controls_are_explicit(self) -> None:
        self.assertIn("attestation_authenticity", self.gaps)
        self.assertIn("hidden_foliation_and_coordinate_import", self.gaps)
        self.assertIn("spoof", self.gaps["attestation_authenticity"].recommended_action)
        self.assertIn("monotone counters", self.gaps["hidden_foliation_and_coordinate_import"].recommended_action)

    def test_recommended_next_goal_targets_mutual_attestability_semantics(self) -> None:
        self.assertIn("T388", self.result.recommended_next_goal)
        self.assertIn("mutual-attestability semantics", self.result.recommended_next_goal)
        self.assertIn("scalar tokens", self.result.recommended_next_goal)
        self.assertIn("spoofed receipts", self.result.recommended_next_goal)
        self.assertIn("no claim upgrade", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
