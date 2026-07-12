"""Tests for T537: source-law family and falsifier packet."""

from __future__ import annotations

import json
import unittest

from models import t536_taf11_source_law_successor_router as t536
from models import t537_source_law_family_and_falsifier_packet as t537


class SourceLawFamilyAndFalsifierPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t537.run_t537_analysis()
        cls.payload = t537.t537_result_to_dict(cls.result)
        cls.decisions = {
            decision.family_id: decision for decision in cls.result.family_decisions
        }

    def test_t536_route_is_consumed(self) -> None:
        self.assertEqual(self.result.artifact, t537.ARTIFACT)
        self.assertEqual(self.result.verdict, t537.VERDICT)
        self.assertEqual(self.result.source_t536_selected_routes, (t536.SELECTED_ROUTE,))
        self.assertEqual(self.result.source_t536_verdict, t536.VERDICT)

    def test_exactly_one_source_law_family_selected(self) -> None:
        self.assertEqual(self.result.selected_family_ids, (t537.SELECTED_FAMILY,))
        selected = self.decisions[t537.SELECTED_FAMILY]

        self.assertEqual(selected.outcome, "SELECTED_FOR_EXECUTION")
        self.assertTrue(selected.selected_for_next_execution)
        self.assertEqual(selected.track_role, "track_1_next_family")
        self.assertEqual(selected.missing_requirements, ())
        self.assertEqual(selected.next_packet, t537.NEXT_PACKET)

    def test_selected_family_has_source_variables_and_falsifier(self) -> None:
        selected = self.decisions[t537.SELECTED_FAMILY]

        self.assertIn("local_record_cover", selected.source_variables)
        self.assertIn("descent_obstruction_witness", selected.source_variables)
        self.assertIn("target", selected.predeclared_falsifier)
        self.assertIn("Lorentzian", selected.predeclared_falsifier)

    def test_spent_target_import_and_track_two_routes_are_not_selected(self) -> None:
        duplicate = self.decisions["record_window_separation_rescue_family"]
        target_fit = self.decisions["ordering_fraction_target_fit_family"]
        lorentzian = self.decisions["lorentzian_reference_sampler_family"]
        track_two = self.decisions["real_taf10_data_packet_wait_family"]

        self.assertEqual(duplicate.outcome, "REJECTED_DUPLICATE")
        self.assertIn("no_spent_shape_repeat", duplicate.missing_requirements)
        self.assertEqual(target_fit.outcome, "BLOCKED_TARGET_IMPORT")
        self.assertIn("no_target_density_fit", target_fit.missing_requirements)
        self.assertEqual(lorentzian.outcome, "BLOCKED_TARGET_IMPORT")
        self.assertIn("no_lorentzian_reference_import", lorentzian.missing_requirements)
        self.assertEqual(track_two.outcome, "PAUSED_TRACK_2")
        self.assertIn("track_2_does_not_replace_track_1", track_two.missing_requirements)
        for decision in (duplicate, target_fit, lorentzian, track_two):
            self.assertFalse(decision.selected_for_next_execution)

    def test_underdeclared_feeder_is_review_only(self) -> None:
        feeder = self.decisions["stabilization_certificate_filtration_family"]

        self.assertEqual(feeder.outcome, "REVIEW_ONLY")
        self.assertFalse(feeder.selected_for_next_execution)
        self.assertIn("executable_next_packet_specific", feeder.missing_requirements)

    def test_no_governance_or_posture_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("S1 remains `requires_added_assumption`", dumped)
        self.assertIn("No claim-ledger update is earned", dumped)
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

    def test_markdown_reports_selected_contract(self) -> None:
        markdown = t537.render_markdown(self.payload)

        self.assertIn("## Selected Family Contract", markdown)
        self.assertIn(f"`{t537.SELECTED_FAMILY}`", markdown)
        self.assertIn(f"`{t537.NEXT_PACKET}`", markdown)
        self.assertIn("## Not Claimed", markdown)


if __name__ == "__main__":
    unittest.main()
