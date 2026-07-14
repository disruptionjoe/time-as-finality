"""Tests for T577 source-law firebreak."""

from __future__ import annotations

import json
import unittest

from models import (
    t576_domain_native_sheaf_transport_hostile_search_scope_closure_gate as t576,
)
from models import (
    t577_domain_native_sheaf_transport_source_law_firebreak_gate as t577,
)


class DomainNativeSheafTransportSourceLawFirebreakGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t577.run_t577_analysis()
        cls.payload = t577.t577_result_to_dict(cls.result)
        cls.criteria = {
            item.criterion_id: item for item in cls.result.firebreak_criteria
        }
        cls.boundaries = {
            item.boundary_id: item for item in cls.result.package_boundaries
        }
        cls.decisions = {
            item.decision_id: item for item in cls.result.route_decisions
        }
        cls.gates = {item.gate_id: item for item in cls.result.gate_decisions}

    def test_artifact_identity_and_t576_authority(self) -> None:
        self.assertEqual(self.result.artifact, t577.ARTIFACT)
        self.assertEqual(self.result.verdict, t577.VERDICT)
        self.assertEqual(self.result.firebreak_status, t577.FIREBREAK_STATUS)
        self.assertEqual(self.result.source_law_status, t577.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.source_t576_verdict, t576.VERDICT)
        self.assertEqual(self.result.source_t576_selected_next_packet, t576.NEXT_PACKET)
        self.assertTrue(self.gates["t576_authority"].passed)

    def test_firebreak_criteria_and_boundaries_all_pass(self) -> None:
        expected_criteria = {
            "t576_authority",
            "route_chain_packageable",
            "hostile_pressure_complete_for_declared_scope",
            "promotion_firebreak_needed",
            "protected_boundaries_still_blocked",
        }
        expected_boundaries = {
            "label_firewall",
            "content_firewall",
            "governance_firewall",
            "downstream_firewall",
            "next_burden_firewall",
        }

        self.assertEqual(set(self.criteria), expected_criteria)
        self.assertEqual(set(self.boundaries), expected_boundaries)
        self.assertTrue(all(item.passed for item in self.result.firebreak_criteria))
        self.assertTrue(all(item.satisfied for item in self.result.package_boundaries))
        self.assertTrue(self.gates["firebreak_criteria_pass"].passed)
        self.assertTrue(self.gates["package_boundaries_satisfied"].passed)

    def test_candidate_packaging_allowed_but_source_law_not_earned(self) -> None:
        self.assertTrue(self.result.candidate_packaging_allowed)
        self.assertEqual(self.result.package_label, t577.PACKAGE_LABEL)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(
            self.decisions["allow_internal_candidate_package"].outcome,
            "SELECTED_REVIEW_ONLY_PACKAGE",
        )
        self.assertEqual(
            self.decisions["promote_source_law_now"].outcome,
            "BLOCKED_CANDIDATE_PACKAGE_ONLY",
        )
        self.assertTrue(
            self.gates["candidate_package_allowed_without_promotion"].passed
        )

    def test_limitation_gate_is_selected_as_next_burden(self) -> None:
        selected = self.decisions["run_candidate_package_limitation_gate"]

        self.assertTrue(selected.selected)
        self.assertEqual(selected.next_packet, t577.NEXT_PACKET)
        self.assertEqual(self.result.selected_next_packet, t577.NEXT_PACKET)
        self.assertTrue(self.gates["limitation_gate_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.decisions["move_taf4_from_t577"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.decisions["execute_taf8_from_t577"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.decisions["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["protected_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t578(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t577.render_markdown(self.payload)

        self.assertIn("T577 Results", markdown)
        self.assertIn("## Package Boundaries", markdown)
        self.assertIn(t577.NEXT_PACKET, markdown)
        self.assertIn(t577.PACKAGE_LABEL, markdown)

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
