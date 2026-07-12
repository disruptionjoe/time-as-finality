"""Tests for T531: ordering-fraction measure-law contract."""

from __future__ import annotations

import json
import unittest

from models import t531_ordering_fraction_measure_law_contract as t531
from models.run_t531 import _render_markdown


class OrderingFractionMeasureLawContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t531.run_t531_analysis()
        cls.decisions = {
            decision.packet_id: decision
            for decision in cls.result.packet_decisions
        }

    def test_t530_route_is_preserved(self) -> None:
        self.assertEqual(self.result.artifact, t531.ARTIFACT)
        self.assertEqual(self.result.verdict, t531.VERDICT)
        self.assertEqual(self.result.source_primary_failure_axis, "ordering_fraction")
        self.assertEqual(
            self.result.source_admitted_packet_id,
            t531.SOURCE_ADMITTED_PACKET_ID,
        )

    def test_contract_terms_include_ordering_law_burdens(self) -> None:
        terms = set(self.result.required_contract_terms)

        self.assertIn("law_declared_before_sampling", terms)
        self.assertIn("finality_native_observable", terms)
        self.assertIn("directly_targets_ordering_fraction", terms)
        self.assertIn("independent_naturality_or_neighbor_theory", terms)
        self.assertIn("hostile_controls_independent_of_screen", terms)
        self.assertIn("no_lorentzian_reference_import", terms)
        self.assertIn("no_t528_screen_conditioning", terms)

    def test_only_full_contract_is_admitted(self) -> None:
        self.assertEqual(
            self.result.admitted_packet_ids,
            (t531.ADMITTED_PACKET_ID,),
        )
        admitted = self.decisions[t531.ADMITTED_PACKET_ID]

        self.assertEqual(
            admitted.classification,
            "admitted_pre_execution_review_contract",
        )
        self.assertTrue(admitted.admitted_as_pre_execution_contract)
        self.assertFalse(admitted.counts_as_s1_evidence)
        self.assertEqual(admitted.missing_requirements, ())

    def test_screen_conditioned_and_imported_packets_are_rejected(self) -> None:
        posthoc = self.decisions["posthoc_ordering_band_fit"]
        imported = self.decisions["lorentzian_ordering_fraction_reference"]

        self.assertEqual(
            posthoc.classification,
            "rejected_screen_conditioned_measure_law",
        )
        self.assertIn("law_declared_before_sampling", posthoc.missing_requirements)
        self.assertIn("no_t528_screen_conditioning", posthoc.missing_requirements)
        self.assertEqual(
            imported.classification,
            "rejected_lorentzian_reference_import",
        )
        self.assertIn("no_lorentzian_reference_import", imported.missing_requirements)

    def test_secondary_axis_and_missing_naturality_packets_are_rejected(self) -> None:
        height = self.decisions["height_first_secondary_repair"]
        no_naturality = self.decisions["ordering_fraction_no_naturality"]

        self.assertEqual(height.classification, "rejected_primary_axis_not_addressed")
        self.assertIn("directly_targets_ordering_fraction", height.missing_requirements)
        self.assertEqual(
            no_naturality.classification,
            "rejected_missing_contract_requirements",
        )
        self.assertIn(
            "independent_naturality_or_neighbor_theory",
            no_naturality.missing_requirements,
        )

    def test_posture_movement_shortcut_is_blocked(self) -> None:
        shortcut = self.decisions["s1_promotion_from_contract"]

        self.assertEqual(
            shortcut.classification,
            "blocked_posture_or_external_movement_shortcut",
        )
        self.assertEqual(shortcut.action, "stop")
        self.assertFalse(shortcut.counts_as_s1_evidence)
        self.assertIn(
            "no_s1_claim_canon_public_or_external_movement",
            shortcut.missing_requirements,
        )

    def test_no_governance_or_posture_movement(self) -> None:
        payload = t531.t531_result_to_dict(self.result)
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

    def test_generated_markdown_reports_review_only_contract(self) -> None:
        markdown = _render_markdown(t531.t531_result_to_dict(self.result))

        self.assertIn(
            "- Source primary failure axis: `ordering_fraction`",
            markdown,
        )
        self.assertIn(
            "`predeclared_finality_native_ordering_measure_law_contract`",
            markdown,
        )
        self.assertIn("## Not Claimed", markdown)
        self.assertIn("does not run a generator", markdown)


if __name__ == "__main__":
    unittest.main()

