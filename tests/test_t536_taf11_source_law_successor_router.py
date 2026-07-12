"""Tests for T536: TAF11 source-law successor router."""

from __future__ import annotations

import json
import unittest

from models import t536_taf11_source_law_successor_router as t536


class TAF11SourceLawSuccessorRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t536.run_t536_analysis()
        cls.payload = t536.t536_result_to_dict(cls.result)
        cls.decisions = {
            decision.route_id: decision for decision in cls.result.route_decisions
        }

    def test_sources_are_consumed_as_pause_states(self) -> None:
        self.assertEqual(self.result.artifact, t536.ARTIFACT)
        self.assertEqual(self.result.verdict, t536.VERDICT)
        self.assertEqual(self.result.source_t534_route_outcome, "PAUSE")
        self.assertEqual(self.result.source_t534_cleared_laws, ())
        self.assertEqual(self.result.source_t535_verdict, "NO_REAL_TAF10_PACKET_IN_HAND_PAUSE")
        self.assertFalse(self.result.source_t535_real_packet_in_hand)

    def test_exactly_one_successor_route_selected(self) -> None:
        self.assertEqual(self.result.selected_route_ids, (t536.SELECTED_ROUTE,))
        selected = self.decisions[t536.SELECTED_ROUTE]

        self.assertEqual(selected.outcome, "SELECTED")
        self.assertTrue(selected.selected_as_next)
        self.assertEqual(selected.track_role, "track_1_next")
        self.assertEqual(selected.missing_requirements, ())
        self.assertEqual(selected.next_packet, t536.SELECTED_ROUTE)

    def test_spent_and_forbidden_routes_are_not_selected(self) -> None:
        duplicate = self.decisions["repeat_record_window_or_receipt_product"]
        target_drift = self.decisions["changed_target_statistic_first"]
        posture = self.decisions["s1_posture_move_from_pause"]

        self.assertEqual(duplicate.outcome, "REJECTED_DUPLICATE")
        self.assertIn("no_spent_finite_generator_repeat", duplicate.missing_requirements)
        self.assertEqual(target_drift.outcome, "BLOCKED_TARGET_DRIFT")
        self.assertIn(
            "no_target_statistic_change_before_law",
            target_drift.missing_requirements,
        )
        self.assertEqual(posture.outcome, "BLOCKED_GOVERNANCE")
        self.assertIn(
            "no_claim_canon_public_or_external_movement",
            posture.missing_requirements,
        )
        self.assertFalse(duplicate.selected_as_next)
        self.assertFalse(target_drift.selected_as_next)
        self.assertFalse(posture.selected_as_next)

    def test_track_two_data_wait_does_not_replace_track_one(self) -> None:
        decision = self.decisions["taf12_data_packet_wait"]

        self.assertEqual(decision.outcome, "PAUSED_TRACK_2")
        self.assertFalse(decision.selected_as_next)
        self.assertIn("track_2_does_not_replace_track_1", decision.missing_requirements)
        self.assertIn("not_blocked_on_real_data_packet", decision.missing_requirements)

    def test_shadow_protection_is_feeder_not_next_source_law_route(self) -> None:
        decision = self.decisions["taf8_shadow_protection_feeder_packet"]

        self.assertEqual(decision.outcome, "NOT_SELECTED")
        self.assertFalse(decision.selected_as_next)
        self.assertIn("directed_source_law_route", decision.missing_requirements)

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

    def test_markdown_reports_selected_next_packet(self) -> None:
        markdown = t536.render_markdown(self.payload)

        self.assertIn("## Route Decisions", markdown)
        self.assertIn(f"`{t536.SELECTED_ROUTE}`", markdown)
        self.assertIn("## Not Claimed", markdown)
        self.assertIn("source-law family and falsifier packet", markdown)


if __name__ == "__main__":
    unittest.main()
