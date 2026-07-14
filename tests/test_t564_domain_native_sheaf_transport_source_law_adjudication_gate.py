"""Tests for T564 domain-native sheaf transport source-law adjudication gate."""

from __future__ import annotations

import json
import unittest

from models import t563_domain_native_sheaf_transport_absorber_separation_gate as t563
from models import t564_domain_native_sheaf_transport_source_law_adjudication_gate as t564


class DomainNativeSheafTransportSourceLawAdjudicationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t564.run_t564_analysis()
        cls.payload = t564.t564_result_to_dict(cls.result)
        cls.burdens = {
            burden.burden_id: burden for burden in cls.result.source_law_burdens
        }
        cls.routes = {
            decision.decision_id: decision for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t564.ARTIFACT)
        self.assertEqual(self.result.verdict, t564.VERDICT)
        self.assertEqual(self.result.source_law_status, t564.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t564.ROUTE_STATUS)
        self.assertEqual(self.result.source_t563_verdict, t563.VERDICT)
        self.assertEqual(self.result.source_t563_selected_next_packet, t563.NEXT_PACKET)
        self.assertEqual(self.result.source_t563_bounded_class, t564.EXPECTED_BOUNDED_CLASS)

    def test_positive_burdens_clear_from_t563(self) -> None:
        for burden_id in (
            "t563_absorber_separation_authority",
            "minimal_bounded_class_preserved",
            "absorber_separation_survives",
            "native_absorber_controls_still_absorb",
            "target_import_and_replay_controls",
            "governance_boundaries_preserved",
        ):
            with self.subTest(burden_id=burden_id):
                self.assertTrue(self.burdens[burden_id].cleared)
                self.assertFalse(self.burdens[burden_id].blocking)
        self.assertTrue(self.gates["positive_burdens_cleared"].passed)

    def test_source_law_is_not_earned_without_holdout_and_generator(self) -> None:
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.blocking_burdens, t564.BLOCKING_BURDENS)
        self.assertFalse(self.burdens["independent_predictive_holdout"].cleared)
        self.assertFalse(self.burdens["typed_source_generator"].cleared)
        self.assertTrue(self.burdens["independent_predictive_holdout"].blocking)
        self.assertTrue(self.burdens["typed_source_generator"].blocking)
        self.assertTrue(self.gates["source_law_rejected_until_holdout"].passed)

    def test_predictive_holdout_is_selected_instead_of_promotion_or_reset(self) -> None:
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_BURDEN_NOT_CLEARED",
        )
        self.assertTrue(self.routes["run_predictive_holdout_gate"].selected)
        self.assertEqual(
            self.routes["run_predictive_holdout_gate"].next_packet,
            t564.NEXT_PACKET,
        )
        self.assertEqual(
            self.routes["route_reset_now"].outcome,
            "PAUSED_CANDIDATE_NOT_ABSORBED",
        )
        self.assertEqual(self.result.selected_next_packet, t564.NEXT_PACKET)
        self.assertTrue(self.gates["predictive_holdout_selected"].passed)

    def test_taf4_taf8_and_governance_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t564"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t564"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["claim_canon_public_posture_shortcut"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_hostile_controls_name_expected_overreads(self) -> None:
        self.assertIn("three admitted fixtures", self.controls["bounded_class_overread_control"].blocks)
        self.assertIn("typed case generator", self.controls["generator_underdeclaration_control"].blocks)
        self.assertIn("target labels", self.controls["target_import_control"].blocks)
        self.assertIn("TAF4", self.controls["taf4_taf8_shortcut_control"].blocks)

    def test_no_claim_canon_public_taf4_taf8_s1_or_cross_repo_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("No claim-ledger update is earned", dumped)
        self.assertIn("TAF4 remains blocked", dumped)
        self.assertIn("TAF8 remains waiting", dumped)
        forbidden = (
            "source law established",
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

    def test_all_gates_pass(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertTrue(self.gates["t563_authority"].passed)

    def test_markdown_reports_blocking_burdens_and_next_packet(self) -> None:
        markdown = t564.render_markdown(self.payload)

        self.assertIn("T564 Results", markdown)
        self.assertIn("## Source-Law Burdens", markdown)
        self.assertIn("`independent_predictive_holdout`", markdown)
        self.assertIn("`typed_source_generator`", markdown)
        self.assertIn(t564.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
