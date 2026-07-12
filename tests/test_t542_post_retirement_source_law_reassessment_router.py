"""Tests for T542 post-retirement source-law reassessment router."""

from __future__ import annotations

import json
import unittest

from models import t539_resolution_depth_generator_packet as t539
from models import t541_nonidentity_shadow_protection_witness_packet as t541
from models import t542_post_retirement_source_law_reassessment_router as t542


class PostRetirementSourceLawReassessmentRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t542.run_t542_analysis()
        cls.payload = t542.t542_result_to_dict(cls.result)
        cls.decisions = {
            decision.candidate_id: decision
            for decision in cls.result.candidate_decisions
        }

    def test_artifact_identity_and_source_constraints_consumed(self) -> None:
        self.assertEqual(self.result.artifact, t542.ARTIFACT)
        self.assertEqual(self.result.verdict, t542.VERDICT)
        self.assertEqual(self.result.source_t539_verdict, t539.VERDICT)
        self.assertEqual(self.result.source_t539_family_status, t539.FAMILY_STATUS)
        self.assertEqual(self.result.source_t541_verdict, t541.VERDICT)
        self.assertEqual(self.result.source_t541_taf8_status, t541.TAF8_STATUS)

    def test_exactly_one_successor_is_selected(self) -> None:
        self.assertEqual(self.result.selected_family_ids, (t542.SELECTED_FAMILY,))
        selected = self.decisions[t542.SELECTED_FAMILY]

        self.assertEqual(selected.outcome, "SELECTED_FOR_EXECUTION")
        self.assertTrue(selected.selected_for_next_execution)
        self.assertEqual(selected.track_role, "track_1_next_family")
        self.assertEqual(selected.missing_requirements, ())
        self.assertEqual(selected.next_packet, t542.NEXT_PACKET)

    def test_selected_aprd_contract_is_non_rank_and_falsifiable(self) -> None:
        selected = self.decisions[t542.SELECTED_FAMILY]
        text = selected.predeclared_falsifier

        self.assertIn("access_profile", selected.source_variables)
        self.assertIn("reconstruction_boundary", selected.source_variables)
        self.assertIn("descent_gap", selected.source_variables)
        self.assertIn("scalar rank", text)
        self.assertIn("target statistics", text)
        self.assertIn("native absorbers", text)

    def test_taf8_wait_and_t539_retirement_are_respected(self) -> None:
        taf8 = self.decisions["taf8_domain_native_packet_execution"]
        retired = self.decisions["descent_obstruction_resolution_family_replay"]

        self.assertEqual(
            taf8.outcome, "PAUSED_TAF8_WAITING_FOR_DOMAIN_NATIVE_PACKET"
        )
        self.assertIn("domain_native_taf8_packet_in_hand", taf8.missing_requirements)
        self.assertFalse(taf8.selected_for_next_execution)

        self.assertEqual(retired.outcome, "REJECTED_RETIRED_T539_ROUTE")
        self.assertIn("no_retired_t539_family_replay", retired.missing_requirements)
        self.assertFalse(retired.selected_for_next_execution)

    def test_review_only_feeders_are_not_selected(self) -> None:
        stabilization = self.decisions["stabilization_certificate_filtration_family"]
        observerse = self.decisions["observerse_protocol_stack_ablation_family"]

        self.assertEqual(stabilization.outcome, "REVIEW_ONLY")
        self.assertIn("non_rank_source_law_family", stabilization.missing_requirements)
        self.assertEqual(observerse.outcome, "REVIEW_ONLY")
        self.assertIn("executable_next_packet_specific", observerse.missing_requirements)
        self.assertFalse(stabilization.selected_for_next_execution)
        self.assertFalse(observerse.selected_for_next_execution)

    def test_target_track_two_and_governance_shortcuts_block(self) -> None:
        target = self.decisions["ordering_fraction_target_refit_family"]
        track_two = self.decisions["taf12_real_packet_wait_family"]
        governance = self.decisions["s1_claim_or_public_posture_shortcut"]

        self.assertEqual(target.outcome, "BLOCKED_TARGET_IMPORT")
        self.assertEqual(track_two.outcome, "PAUSED_TRACK_2")
        self.assertEqual(governance.outcome, "BLOCKED_GOVERNANCE")
        for decision in (target, track_two, governance):
            self.assertFalse(decision.selected_for_next_execution)

    def test_no_claim_or_posture_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

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
        markdown = t542.render_markdown(self.payload)

        self.assertIn("## Selected Family Contract", markdown)
        self.assertIn(f"`{t542.SELECTED_FAMILY}`", markdown)
        self.assertIn(f"`{t542.NEXT_PACKET}`", markdown)
        self.assertIn("## Not Claimed", markdown)


if __name__ == "__main__":
    unittest.main()
