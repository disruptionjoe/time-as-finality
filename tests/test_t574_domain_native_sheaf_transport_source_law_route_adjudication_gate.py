"""Tests for T574 source-law route adjudication."""

from __future__ import annotations

import json
import unittest

from models import (
    t573_domain_native_sheaf_transport_adversarial_blind_family_holdout_gate
    as t573,
)
from models import (
    t574_domain_native_sheaf_transport_source_law_route_adjudication_gate
    as t574,
)


class DomainNativeSheafTransportRouteAdjudicationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t574.run_t574_analysis()
        cls.payload = t574.t574_result_to_dict(cls.result)
        cls.criteria = {
            criterion.criterion_id: criterion for criterion in cls.result.route_criteria
        }
        cls.blockers = {
            blocker.blocker_id: blocker for blocker in cls.result.promotion_blockers
        }
        cls.decisions = {
            decision.decision_id: decision for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t574.ARTIFACT)
        self.assertEqual(self.result.verdict, t574.VERDICT)
        self.assertEqual(self.result.adjudication_status, t574.ADJUDICATION_STATUS)
        self.assertEqual(self.result.source_law_status, t574.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.source_t573_verdict, t573.VERDICT)
        self.assertEqual(self.result.source_t573_selected_next_packet, t573.NEXT_PACKET)
        self.assertTrue(self.result.source_t573_adversarial_holdout_cleared)

    def test_required_route_criteria_keep_route_open(self) -> None:
        required = [
            criterion for criterion in self.result.route_criteria if criterion.weight == "required"
        ]

        self.assertTrue(required)
        self.assertTrue(all(criterion.passed for criterion in required))
        self.assertTrue(self.result.route_kept_open)
        self.assertTrue(self.gates["route_evidence_keeps_route_open"].passed)
        self.assertIn("t573_authority", self.criteria)
        self.assertIn(
            "rotation_blind_and_adversarial_holdouts_cleared",
            self.criteria,
        )

    def test_promotion_is_blocked_and_source_law_not_earned(self) -> None:
        self.assertFalse(self.result.source_law_earned)
        self.assertTrue(all(blocker.active for blocker in self.result.promotion_blockers))
        self.assertIn("hostile_counterfamily_search_missing", self.blockers)
        self.assertEqual(
            self.decisions["promote_source_law_now"].outcome,
            "BLOCKED_PROMOTION_BAR_NOT_MET",
        )
        self.assertTrue(self.gates["promotion_blockers_active"].passed)
        self.assertTrue(self.gates["source_law_not_promoted"].passed)

    def test_counterfamily_search_is_selected_as_next_non_promotion_burden(self) -> None:
        selected = self.decisions["run_hostile_counterfamily_search_gate"]

        self.assertTrue(selected.selected)
        self.assertEqual(selected.next_packet, t574.NEXT_PACKET)
        self.assertEqual(self.result.selected_next_packet, t574.NEXT_PACKET)
        self.assertTrue(self.gates["hostile_counterfamily_search_selected_next"].passed)
        self.assertFalse(self.decisions["retire_semantic_generator_route"].selected)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.decisions["move_taf4_from_t574"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.decisions["execute_taf8_from_t574"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.decisions["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t575(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t574.render_markdown(self.payload)

        self.assertIn("T574 Results", markdown)
        self.assertIn("## Route Criteria", markdown)
        self.assertIn(t574.NEXT_PACKET, markdown)

    def test_json_serializable_and_avoids_forbidden_promotions(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        json.dumps(self.payload, sort_keys=True)
        self.assertIn("No claim-ledger update is earned", dumped)
        forbidden = (
            "source law proved",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
            "TAF4 unblocked",
            "TAF8 theorem proved",
            "S1 promoted",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
