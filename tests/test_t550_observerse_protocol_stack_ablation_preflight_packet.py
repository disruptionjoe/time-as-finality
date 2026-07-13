"""Tests for T550 Observerse protocol-stack ablation preflight packet."""

from __future__ import annotations

import json
import unittest

from models import run_t527 as t527
from models import t549_taf11_post_aprd_route_reset_router as t549
from models import t550_observerse_protocol_stack_ablation_preflight_packet as t550


class ObserverseProtocolStackAblationPreflightPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t550.run_t550_analysis()
        cls.payload = t550.t550_result_to_dict(cls.result)
        cls.layers = {layer.layer_id: layer for layer in cls.result.layer_contracts}
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t550.ARTIFACT)
        self.assertEqual(self.result.verdict, t550.VERDICT)
        self.assertEqual(self.result.preflight_status, t550.PREFLIGHT_STATUS)
        self.assertEqual(self.result.source_t549_verdict, t549.VERDICT)
        self.assertEqual(
            self.result.source_t549_selected_route_ids,
            (t549.SELECTED_ROUTE,),
        )
        self.assertEqual(self.result.source_t527_verdict, t527.VERDICT)
        self.assertEqual(
            self.result.source_t527_grade,
            "illustration_regression_only",
        )

    def test_five_layer_contract_is_predeclared(self) -> None:
        self.assertEqual(
            tuple(self.layers),
            (
                "issuance",
                "admissibility",
                "sybil_finality",
                "consensus",
                "governance",
            ),
        )
        self.assertEqual(
            self.layers["issuance"].source_variable,
            "issued_novelty_stream",
        )
        self.assertEqual(
            self.layers["admissibility"].predicted_collapse_mode,
            "incoherence",
        )
        self.assertEqual(
            self.layers["sybil_finality"].frozen_t527_row_id,
            "without_sybil_finality",
        )
        self.assertEqual(
            self.layers["consensus"].predicted_collapse_mode,
            "fragment",
        )
        self.assertEqual(
            self.layers["governance"].source_variable,
            "rule_revision_horizon",
        )

    def test_t527_collapse_map_matches_preflight_contract(self) -> None:
        for layer in self.result.layer_contracts:
            with self.subTest(layer=layer.layer_id):
                self.assertLessEqual(
                    layer.t527_ratio_to_full,
                    layer.collapse_threshold,
                )
                self.assertTrue(layer.source_law_burden)
                self.assertTrue(layer.predeclared_signal)

        self.assertTrue(self.result.source_t527_governance_conditional_visible)

    def test_all_preflight_gates_pass_and_select_t551(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertEqual(
            self.gates["t549_route_authority"].outcome,
            "PASS",
        )
        self.assertEqual(
            self.gates["t527_review_only_boundary"].outcome,
            "PASS",
        )
        self.assertEqual(
            self.gates["governance_conditional_preserved"].outcome,
            "PASS",
        )
        self.assertEqual(self.result.selected_next_packet, t550.NEXT_PACKET)

    def test_hostile_controls_block_overreading_and_shortcuts(self) -> None:
        self.assertIn(
            "Observerse validation",
            self.controls["t527_validation_overread_control"].blocks,
        )
        self.assertIn(
            "Adding, dropping, or renaming layers",
            self.controls["post_hoc_layer_control"].blocks,
        )
        self.assertIn(
            "Dropping governance",
            self.controls["conditional_governance_control"].blocks,
        )
        self.assertIn(
            "Repairing APRD",
            self.controls["aprd_retune_control"].blocks,
        )
        self.assertIn(
            "Moving TAF4",
            self.controls["taf4_source_law_shortcut_control"].blocks,
        )

    def test_no_claim_canon_public_or_cross_repo_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("No claim-ledger update is earned", dumped)
        self.assertIn("review-only preflight contract", dumped)
        forbidden = (
            "source law established",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
            "TAF4 unblocked",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)

    def test_markdown_reports_layer_contract_and_next_packet(self) -> None:
        markdown = t550.render_markdown(self.payload)

        self.assertIn("T550 Results", markdown)
        self.assertIn("## Layer Contracts", markdown)
        self.assertIn("`issuance`", markdown)
        self.assertIn("`governance`", markdown)
        self.assertIn(t550.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
