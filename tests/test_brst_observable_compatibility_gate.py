"""Tests for T509 BRST observable-compatibility gate."""

from __future__ import annotations

import json
import unittest

from models.brst_observable_compatibility_gate import run


class BrstObservableCompatibilityGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = run()
        self.decisions = {
            item["packet_id"]: item for item in self.payload["decisions"]
        }

    def test_verdict_and_scope_are_review_only(self) -> None:
        self.assertEqual(
            self.payload["verdict"],
            "BRST_OBSERVABLE_COMPATIBILITY_GATE_BUILT_RECOVERY_BLOCKED",
        )
        overall = self.payload["overall"]
        self.assertFalse(overall["claim_movement"])
        self.assertFalse(overall["public_posture_movement"])
        self.assertFalse(overall["external_publication"])
        self.assertFalse(overall["cross_repo_truth_movement"])
        self.assertFalse(overall["sibling_repo_inspection"])
        self.assertFalse(overall["brst_exactness_decided_for_real_physics"])
        self.assertFalse(overall["brst_nontriviality_decided_for_real_physics"])
        self.assertFalse(overall["hidden_mirror_record_claim_earned"])
        self.assertFalse(overall["physics_claim_earned"])

    def test_fixture_has_nontrivial_mirror_but_shared_wplus(self) -> None:
        states = self.payload["states"]
        summary = self.payload["constraint_summaries"]["nontrivial_mirror"]

        self.assertTrue(states["share_wplus_before_operation"])
        self.assertGreater(states["mirror_delta_before_operation"], 0.0)
        self.assertTrue(summary["q_nilpotent"])
        self.assertTrue(summary["mirror_q_closed"])
        self.assertFalse(summary["mirror_q_exact"])
        self.assertTrue(summary["mirror_cohomology_nontrivial"])

    def test_full_krein_recovery_is_rejected_when_it_does_not_descend(self) -> None:
        decision = self.decisions["t508_full_krein_recovery"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_RECOVERY_OPERATION_NOT_BRST_COMPATIBLE",
        )
        self.assertGreater(decision["wplus_recovery_score"], 0.0)
        self.assertFalse(decision["operation_descends_to_cohomology"])
        self.assertTrue(
            self.payload["overall"][
                "t508_full_krein_recovery_rejected_by_quotient_discipline"
            ]
        )

    def test_chain_map_representative_leakage_is_not_a_hidden_record(self) -> None:
        decision = self.decisions["chain_map_representative_leakage"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(decision["label"], "REJECTED_EXACT_REPRESENTATIVE_LEAKAGE")
        self.assertTrue(decision["operation_descends_to_cohomology"])
        self.assertFalse(decision["readout_descends_to_cohomology"])
        self.assertTrue(decision["representative_leakage"])
        self.assertGreater(decision["wplus_recovery_score"], 0.0)
        self.assertTrue(self.payload["overall"]["representative_leakage_rejected"])

    def test_direct_cohomology_readout_is_review_only(self) -> None:
        decision = self.decisions["direct_cohomology_observable"]

        self.assertTrue(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "ADMITTED_COHOMOLOGY_OBSERVABLE_REVIEW_TARGET",
        )
        self.assertTrue(decision["readout_descends_to_cohomology"])
        self.assertGreater(decision["cohomology_readout_delta"], 0.0)
        self.assertFalse(decision["counts_as_claim_evidence"])
        self.assertTrue(
            self.payload["overall"]["direct_cohomology_observable_admitted_review_only"]
        )

    def test_cohomology_scaling_is_direct_observable_not_hidden_wplus_recovery(self) -> None:
        decision = self.decisions["cohomology_scaling_control"]

        self.assertTrue(decision["admitted"])
        self.assertTrue(decision["operation_descends_to_cohomology"])
        self.assertTrue(decision["readout_descends_to_cohomology"])
        self.assertEqual(decision["wplus_recovery_score"], 0.0)
        self.assertGreater(decision["cohomology_readout_delta"], 0.0)
        self.assertFalse(decision["counts_as_claim_evidence"])

    def test_exact_mirror_routes_to_redundancy(self) -> None:
        decision = self.decisions["exact_mirror_redundancy_control"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(decision["label"], "BRST_EXACT_REDUNDANCY_RECORDED")
        self.assertEqual(decision["action"], "record_negative")
        self.assertTrue(decision["mirror_q_exact"])
        self.assertFalse(decision["mirror_cohomology_nontrivial"])
        self.assertTrue(self.payload["overall"]["exact_mirror_routes_to_redundancy"])

    def test_wplus_and_incomplete_shortcuts_are_rejected(self) -> None:
        wplus = self.decisions["wplus_observable_shortcut"]
        post_hoc = self.decisions["post_hoc_readout_shortcut"]
        missing = self.decisions["missing_controls_shortcut"]

        self.assertFalse(wplus["admitted"])
        self.assertEqual(wplus["label"], "REJECTED_NON_DESCENDING_READOUT")
        self.assertIn("exact-invariant readout", wplus["missing_requirements"])

        self.assertFalse(post_hoc["admitted"])
        self.assertEqual(post_hoc["label"], "REJECTED_INCOMPLETE_OBSERVABLE_PACKET")
        self.assertIn(
            "predeclared exact-invariant readout",
            post_hoc["missing_requirements"],
        )

        self.assertFalse(missing["admitted"])
        self.assertEqual(missing["label"], "REJECTED_INCOMPLETE_OBSERVABLE_PACKET")
        self.assertIn(
            "non-descending recovery-operation control",
            missing["missing_requirements"],
        )
        self.assertIn(
            "exact-representative leakage control",
            missing["missing_requirements"],
        )

    def test_claim_and_cross_repo_shortcuts_are_blocked(self) -> None:
        decision = self.decisions["claim_cross_repo_shortcut"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
        )
        self.assertEqual(decision["action"], "stop")
        self.assertFalse(decision["counts_as_claim_evidence"])

    def test_future_minimum_and_not_earned_are_explicit(self) -> None:
        minimum = self.payload["future_packet_minimum"]
        blocked = self.payload["not_earned"]

        self.assertIn(
            "prove the recovery operation descends through the BRST quotient",
            minimum,
        )
        self.assertIn(
            "prove the readout annihilates exact representative shifts",
            minimum,
        )
        self.assertIn(
            "do not treat W+ representative leakage as a hidden physical record",
            minimum,
        )
        self.assertIn("real BRST exactness decision", blocked)
        self.assertIn("hidden mirror record claim", blocked)
        self.assertIn("cross-repo truth movement", blocked)

    def test_payload_is_json_serializable_without_forbidden_overreads(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn(
            "BRST_OBSERVABLE_COMPATIBILITY_GATE_BUILT_RECOVERY_BLOCKED",
            dumped,
        )
        forbidden = (
            "BRST observable proves physics",
            "hidden record proven",
            "Krein quantization accepted",
            "claim ledger promoted",
            "cross-repo truth established",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
