"""Tests for the pre-T Jevons rebound capability gate."""

from __future__ import annotations

import json
import unittest

from models import jevons_rebound_capability_gate as gate


class JevonsReboundCapabilityGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = gate.run()
        cls.evaluations = {
            item["packet_id"]: item for item in cls.result["packet_evaluations"]
        }

    def test_artifact_identity_and_no_movement_boundary(self) -> None:
        verdict = self.result["overall_verdict"]

        self.assertEqual(self.result["artifact"], gate.ARTIFACT)
        self.assertEqual(verdict["verdict"], gate.VERDICT)
        self.assertFalse(verdict["formal_t_number_created"])
        self.assertFalse(verdict["test_registry_movement"])
        self.assertFalse(verdict["claim_movement"])
        self.assertFalse(verdict["canon_or_public_posture_movement"])
        self.assertFalse(verdict["cross_repo_movement"])

    def test_net_improvement_control_survives_demand_response(self) -> None:
        control = self.evaluations["unit_efficiency_positive_control"]

        self.assertTrue(control["admitted"])
        self.assertEqual(control["label"], "NET_IMPROVEMENT_AFTER_DEMAND_RESPONSE")
        self.assertEqual(control["action"], "positive_control")
        self.assertTrue(control["unit_cost_decreases"])
        self.assertFalse(control["demand_increases"])
        self.assertFalse(control["burden_worsens"])
        self.assertTrue(control["net_capability_improves"])

    def test_classic_rebound_is_absorbed_by_resource_demand_accounting(self) -> None:
        rebound = self.evaluations["classic_rebound_resource_accounting"]

        self.assertFalse(rebound["admitted"])
        self.assertEqual(rebound["label"], "ABSORBED_BY_RESOURCE_DEMAND_ACCOUNTING")
        self.assertEqual(rebound["action"], "absorb")
        self.assertTrue(rebound["unit_cost_decreases"])
        self.assertTrue(rebound["demand_increases"])
        self.assertTrue(rebound["burden_worsens"])
        self.assertFalse(rebound["net_capability_improves"])
        self.assertTrue(self.result["overall_verdict"]["resource_demand_absorber_fired"])

    def test_hidden_or_post_hoc_inputs_are_rejected(self) -> None:
        post_hoc = self.evaluations["post_hoc_burden_variable"]
        hidden = self.evaluations["hidden_demand_response_label"]

        self.assertFalse(post_hoc["admitted"])
        self.assertEqual(post_hoc["label"], "REJECTED_POST_HOC_BURDEN_VARIABLE")
        self.assertFalse(hidden["admitted"])
        self.assertEqual(hidden["label"], "REJECTED_HIDDEN_DEMAND_RESPONSE")

    def test_source_side_import_routes_out(self) -> None:
        packet = self.evaluations["source_side_possibility_growth_import"]

        self.assertFalse(packet["admitted"])
        self.assertEqual(packet["label"], "REJECTED_SOURCE_SIDE_POSSIBILITY_GROWTH_IMPORT")
        self.assertEqual(packet["action"], "route_out")

    def test_synthetic_future_target_requires_independent_finality_witness(self) -> None:
        target = self.evaluations["synthetic_finality_review_target"]

        self.assertTrue(target["admitted"])
        self.assertEqual(target["label"], "ADMITTED_REBOUND_CAPABILITY_REVIEW_TARGET")
        self.assertEqual(target["action"], "review_only")
        self.assertTrue(target["packet"]["independent_finality_witness"])
        self.assertFalse(target["packet"]["resource_accounting_explains_split"])
        self.assertTrue(
            self.result["overall_verdict"]["synthetic_future_review_target_admitted"]
        )

    def test_json_serializable_and_banned_claims_absent(self) -> None:
        dumped = json.dumps(self.result, sort_keys=True)

        self.assertIn(gate.VERDICT, dumped)
        banned = (
            "claim promotion follows",
            "public posture authorized",
            "external publication authorized",
            "source-side truth imported",
            "Jevons residue proved",
        )
        for phrase in banned:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
