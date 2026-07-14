"""Tests for T565 domain-native sheaf transport predictive holdout gate."""

from __future__ import annotations

import json
import unittest

from models import t563_domain_native_sheaf_transport_absorber_separation_gate as t563
from models import t564_domain_native_sheaf_transport_source_law_adjudication_gate as t564
from models import t565_domain_native_sheaf_transport_predictive_holdout_gate as t565


class DomainNativeSheafTransportPredictiveHoldoutGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t565.run_t565_analysis()
        cls.payload = t565.t565_result_to_dict(cls.result)
        cls.evaluation = cls.result.holdout_evaluation
        cls.burdens = {
            burden.burden_id: burden for burden in cls.result.remaining_burdens
        }
        cls.routes = {
            decision.decision_id: decision for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t565.ARTIFACT)
        self.assertEqual(self.result.verdict, t565.VERDICT)
        self.assertEqual(self.result.holdout_status, t565.HOLDOUT_STATUS)
        self.assertEqual(self.result.source_law_status, t565.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t565.ROUTE_STATUS)
        self.assertEqual(self.result.source_t564_verdict, t564.VERDICT)
        self.assertEqual(self.result.source_t564_selected_next_packet, t564.NEXT_PACKET)
        self.assertEqual(self.result.source_t564_blocking_burdens, t564.BLOCKING_BURDENS)
        self.assertEqual(self.result.source_t563_absorber_status, t563.ABSORBER_STATUS)
        self.assertEqual(self.result.source_t563_bounded_class, t563.EXPECTED_BOUNDED_CLASS)

    def test_holdout_is_predeclared_independent_and_frozen(self) -> None:
        spec = self.result.holdout_spec

        self.assertTrue(spec.predeclared_before_evaluation)
        self.assertTrue(spec.independent_from_prior_bounded_class)
        self.assertEqual(spec.source_variables, t565.FROZEN_SOURCE_VARIABLES)
        self.assertEqual(spec.absorber_ids, t565.FROZEN_ABSORBER_IDS)
        self.assertEqual(spec.forbidden_shortcuts_used, ())
        self.assertIn("rotating multi-ledger repair", spec.rationale)
        self.assertTrue(self.gates["holdout_predeclared_and_independent"].passed)
        self.assertTrue(self.gates["frozen_contract_used"].passed)

    def test_predictive_holdout_clears_absorber_screen(self) -> None:
        self.assertTrue(self.evaluation.predicted_by_frozen_contract)
        self.assertTrue(self.result.predictive_holdout_cleared)
        self.assertTrue(self.burdens["independent_predictive_holdout"].cleared)
        self.assertFalse(self.burdens["independent_predictive_holdout"].blocking)
        self.assertEqual(
            len(self.evaluation.absorber_screens),
            len(t565.FROZEN_ABSORBER_IDS),
        )
        for screen in self.evaluation.absorber_screens:
            with self.subTest(absorber_id=screen.absorber_id):
                self.assertTrue(screen.absorber_boundary_predicted)
                self.assertEqual(screen.actual_status, screen.expected_status)
                self.assertIn(screen.absorber_id, t565.FROZEN_ABSORBER_IDS)
        self.assertTrue(self.gates["predictive_holdout_cleared"].passed)

    def test_forbidden_shortcuts_are_absent(self) -> None:
        self.assertTrue(self.evaluation.no_forbidden_shortcuts)
        self.assertEqual(self.result.holdout_spec.forbidden_shortcuts_used, ())
        self.assertTrue(self.gates["forbidden_shortcuts_absent"].passed)
        dumped = json.dumps(self.payload, sort_keys=True)
        self.assertIn("No target import, cross-repo, replay", dumped)
        self.assertIn("No claim-ledger update is earned", dumped)
        self.assertEqual(self.payload["holdout_spec"]["forbidden_shortcuts_used"], [])
        self.assertTrue(self.payload["holdout_evaluation"]["no_forbidden_shortcuts"])
        self.assertIn("No claim-ledger update is earned", dumped)

    def test_source_law_is_not_earned_without_typed_generator(self) -> None:
        self.assertFalse(self.result.typed_source_generator_cleared)
        self.assertFalse(self.result.source_law_earned)
        self.assertFalse(self.burdens["typed_source_generator"].cleared)
        self.assertTrue(self.burdens["typed_source_generator"].blocking)
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_GENERATOR_NOT_TYPED",
        )
        self.assertTrue(self.gates["source_law_still_not_promoted"].passed)

    def test_typed_generator_gate_is_selected_next(self) -> None:
        self.assertTrue(self.routes["run_typed_generator_gate"].selected)
        self.assertEqual(
            self.routes["run_typed_generator_gate"].next_packet,
            t565.NEXT_PACKET,
        )
        self.assertEqual(self.result.selected_next_packet, t565.NEXT_PACKET)
        self.assertTrue(self.gates["typed_generator_selected_next"].passed)
        self.assertEqual(
            self.routes["route_reset_after_holdout_failure"].outcome,
            "PAUSED_HOLDOUT_DID_NOT_FAIL",
        )

    def test_taf4_taf8_and_governance_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t565"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t565"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["claim_canon_public_posture_shortcut"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_hostile_controls_name_expected_overreads(self) -> None:
        self.assertIn("Fitting a holdout", self.controls["predeclaration_control"].blocks)
        self.assertIn("T559", self.controls["replay_control"].blocks)
        self.assertIn("target labels", self.controls["target_import_control"].blocks)
        self.assertIn("one holdout", self.controls["generator_underdeclaration_control"].blocks)
        self.assertIn("TAF4", self.controls["taf4_taf8_shortcut_control"].blocks)

    def test_no_claim_canon_public_taf4_taf8_s1_or_cross_repo_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

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

    def test_all_gates_pass_and_markdown_reports_next_packet(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t565.render_markdown(self.payload)

        self.assertIn("T565 Results", markdown)
        self.assertIn("## Holdout Specification", markdown)
        self.assertIn("## Remaining Burdens", markdown)
        self.assertIn("`typed_source_generator`", markdown)
        self.assertIn(t565.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
