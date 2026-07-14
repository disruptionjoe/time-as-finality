"""Tests for T571 multi-family falsifier rotation."""

from __future__ import annotations

import json
import unittest

from models import (
    t570_domain_native_sheaf_transport_fresh_family_stress_gate as t570,
)
from models import (
    t571_domain_native_sheaf_transport_multi_family_falsifier_rotation_gate as t571,
)


class DomainNativeSheafTransportMultiFamilyFalsifierRotationGateTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t571.run_t571_analysis()
        cls.payload = t571.t571_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.probe_id: evaluation for evaluation in cls.result.evaluations
        }
        cls.summaries = {
            summary.family_id: summary for summary in cls.result.family_summaries
        }
        cls.checks = {
            check.check_id: check for check in cls.result.closure_checks
        }
        cls.routes = {
            decision.decision_id: decision for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t571.ARTIFACT)
        self.assertEqual(self.result.verdict, t571.VERDICT)
        self.assertEqual(self.result.rotation_status, t571.ROTATION_STATUS)
        self.assertEqual(self.result.source_law_status, t571.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t571.ROUTE_STATUS)
        self.assertEqual(self.result.source_t570_verdict, t570.VERDICT)
        self.assertEqual(self.result.source_t570_selected_next_packet, t570.NEXT_PACKET)
        self.assertTrue(self.result.source_t570_fresh_family_stress_cleared)

    def test_contract_rotates_all_t570_families(self) -> None:
        contract = self.result.rotation_contract

        self.assertEqual(contract.contract_id, "multi_family_falsifier_rotation_v1")
        self.assertEqual(
            contract.source_t570_projection_id,
            "fresh_role_recoding_projection_v1",
        )
        self.assertEqual(
            contract.admitted_family_ids,
            (
                "calibration_chain_role_recoding_family",
                "archive_manifest_handoff_role_recoding_family",
            ),
        )
        self.assertIn("cross_family_alias_replay", contract.rotated_falsifier_axes)
        self.assertTrue(self.checks["all_t570_families_rotated"].passed)

    def test_family_survivors_admit(self) -> None:
        expected = (
            "calibration_chain_rotated_survivor",
            "archive_manifest_rotated_survivor",
        )

        self.assertEqual(self.result.admitted_probe_ids, expected)
        for probe_id in expected:
            with self.subTest(probe_id=probe_id):
                evaluation = self.evaluations[probe_id]
                self.assertTrue(evaluation.rotation_admissible)
                self.assertTrue(evaluation.expectation_matched)
                self.assertEqual(evaluation.failed_checks, ())
        self.assertTrue(self.checks["expected_survivors_admitted"].passed)

    def test_rotated_falsifiers_reject(self) -> None:
        expected = (
            "calibration_missing_scope_restriction_falsifier",
            "calibration_single_panel_completion_falsifier",
            "archive_payload_optional_falsifier",
            "archive_target_geometry_import_falsifier",
            "cross_family_alias_replay_falsifier",
        )

        self.assertEqual(self.result.rejected_probe_ids, expected)
        for probe_id in expected:
            with self.subTest(probe_id=probe_id):
                evaluation = self.evaluations[probe_id]
                self.assertFalse(evaluation.rotation_admissible)
                self.assertTrue(evaluation.expectation_matched)
        self.assertIn(
            "source_roles_complete",
            self.evaluations[
                "calibration_missing_scope_restriction_falsifier"
            ].failed_checks,
        )
        self.assertIn(
            "native_payload_forced",
            self.evaluations["archive_payload_optional_falsifier"].failed_checks,
        )
        self.assertIn(
            "target_blind_language",
            self.evaluations["archive_target_geometry_import_falsifier"].failed_checks,
        )
        self.assertIn(
            "no_cross_family_alias_replay",
            self.evaluations["cross_family_alias_replay_falsifier"].failed_checks,
        )
        self.assertTrue(self.checks["rotated_falsifiers_rejected"].passed)
        self.assertTrue(self.checks["all_rotated_axes_exercised"].passed)

    def test_family_summaries_have_survivor_and_falsifiers(self) -> None:
        for family_id, summary in self.summaries.items():
            with self.subTest(family_id=family_id):
                self.assertTrue(summary.passed)
                self.assertTrue(summary.admitted_probe_ids)
                self.assertGreaterEqual(len(summary.rejected_probe_ids), 2)

    def test_source_law_not_earned_and_t572_selected(self) -> None:
        self.assertTrue(self.result.multi_family_rotation_cleared)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.selected_next_packet, t571.NEXT_PACKET)
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_REVIEW_ONLY_BLIND_FAMILY_HOLDOUT_REQUIRED",
        )
        self.assertTrue(self.routes["run_blind_family_holdout_gate"].selected)
        self.assertTrue(self.gates["source_law_not_promoted"].passed)
        self.assertTrue(self.gates["blind_family_holdout_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t571"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t571"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t572(self) -> None:
        self.assertTrue(all(check.passed for check in self.result.closure_checks))
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t571.render_markdown(self.payload)

        self.assertIn("T571 Results", markdown)
        self.assertIn("## Probe Evaluations", markdown)
        self.assertIn(t571.NEXT_PACKET, markdown)

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
