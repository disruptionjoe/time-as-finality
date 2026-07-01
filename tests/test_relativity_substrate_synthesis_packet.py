"""Tests for T384 relativity-substrate synthesis packet."""

from __future__ import annotations

import unittest

from models.relativity_substrate_synthesis_packet import run_t384_analysis


class RelativitySubstrateSynthesisPacketTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t384_analysis()

    def test_claim_level_is_conditional_not_physical_derivation(self) -> None:
        self.assertEqual(
            self.result.claim_level,
            "conditional_pattern_theorem_not_physical_derivation",
        )
        self.assertIn("Given", self.result.theorem_like_statement)
        self.assertIn("finite screen forces Lorentz-pattern", self.result.theorem_like_statement)

    def test_premise_bundle_names_exact_dependency_set(self) -> None:
        premise_ids = {premise.premise_id for premise in self.result.premise_bundle}
        self.assertEqual(
            premise_ids,
            {
                "shared_generated_substrate",
                "two_independent_null_channels",
                "bilinear_interval",
                "round_trip_calibration",
                "invariant_signal_unit",
                "exact_access_minimality",
            },
        )

    def test_forced_outputs_include_relativity_pattern(self) -> None:
        outputs = set(self.result.forced_outputs)
        self.assertIn("observer simultaneity disagreement", outputs)
        self.assertIn("gamma/beta Lorentz-pattern coefficients", outputs)
        self.assertIn("time dilation from round-trip calibration", outputs)
        self.assertIn("shared interval recovery without source time/space columns", outputs)

    def test_open_objects_keep_boundary_honest(self) -> None:
        open_ids = {item.object_id for item in self.result.open_objects}
        self.assertIn("basis_origin", open_ids)
        self.assertIn("bilinear_null_premise", open_ids)
        self.assertIn("nonfinite_nonfixed_extension", open_ids)
        self.assertIn("physical_interpretation", open_ids)
        self.assertIn("basis_origin", self.result.next_goal)

    def test_ladder_findings_cover_t377_through_t383(self) -> None:
        test_ids = [finding.test_id for finding in self.result.ladder_findings]
        self.assertEqual(test_ids, ["T377", "T378", "T379", "T380", "T381", "T382", "T383"])

    def test_external_adapter_reading_names_two_null_interface(self) -> None:
        self.assertIn("minimal two-null-channel", self.result.external_adapter_reading)
        self.assertIn("without importing global time", self.result.external_adapter_reading)

    def test_overall_verdict_names_open_object(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "conditional_lorentz_pattern_forced_open_object_is_two_null_basis_origin",
        )
        self.assertIn("remaining hard problem", self.result.plain_english_summary)


if __name__ == "__main__":
    unittest.main()
