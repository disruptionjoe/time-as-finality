"""Tests for T508 BRST cohomology record-admission gate."""

from __future__ import annotations

import json
import unittest

from models.brst_cohomology_record_admission_gate import run


class BrstCohomologyRecordAdmissionGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = run()
        self.decisions = {
            item["packet_id"]: item for item in self.payload["decisions"]
        }

    def test_verdict_and_scope_are_review_only(self) -> None:
        self.assertEqual(
            self.payload["verdict"],
            "BRST_COHOMOLOGY_RECORD_GATE_BUILT_REVIEW_ONLY",
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

    def test_constraint_summaries_distinguish_exact_and_nontrivial_mirror(self) -> None:
        exact = self.payload["constraint_summaries"]["exact_mirror"]
        nontrivial = self.payload["constraint_summaries"]["nontrivial_mirror"]

        self.assertTrue(exact["q_nilpotent"])
        self.assertTrue(exact["mirror_q_closed"])
        self.assertTrue(exact["mirror_q_exact"])
        self.assertFalse(exact["mirror_cohomology_nontrivial"])
        self.assertTrue(nontrivial["q_nilpotent"])
        self.assertTrue(nontrivial["mirror_q_closed"])
        self.assertFalse(nontrivial["mirror_q_exact"])
        self.assertTrue(nontrivial["mirror_cohomology_nontrivial"])

    def test_invalid_constraint_controls_are_rejected(self) -> None:
        non_nilpotent = self.decisions["non_nilpotent_control"]
        not_closed = self.decisions["mirror_not_closed_control"]

        self.assertFalse(non_nilpotent["admitted"])
        self.assertEqual(non_nilpotent["label"], "REJECTED_NON_NILPOTENT_CONSTRAINT")
        self.assertFalse(non_nilpotent["q_nilpotent"])
        self.assertIn("nilpotency Q^2 = 0", non_nilpotent["missing_requirements"])

        self.assertFalse(not_closed["admitted"])
        self.assertEqual(not_closed["label"], "REJECTED_MIRROR_NOT_Q_CLOSED")
        self.assertFalse(not_closed["mirror_q_closed"])
        self.assertIn("mirror vector in ker(Q)", not_closed["missing_requirements"])

    def test_exact_mirror_routes_to_redundancy(self) -> None:
        decision = self.decisions["exact_mirror_default"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(decision["label"], "BRST_EXACT_REDUNDANCY_RECORDED")
        self.assertEqual(decision["action"], "record_negative")
        self.assertTrue(decision["mirror_q_exact"])
        self.assertFalse(decision["mirror_cohomology_nontrivial"])
        self.assertTrue(self.payload["overall"]["exact_mirror_routes_to_redundancy"])

    def test_nontrivial_mirror_with_t507_double_gate_is_review_only(self) -> None:
        decision = self.decisions["nontrivial_mirror_full_krein_selfnorm"]

        self.assertTrue(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "ADMITTED_NONTRIVIAL_COHOMOLOGY_REVIEW_TARGET",
        )
        self.assertEqual(decision["action"], "review_only")
        self.assertTrue(decision["mirror_cohomology_nontrivial"])
        self.assertTrue(decision["t507_double_gate_paid"])
        self.assertFalse(decision["counts_as_claim_evidence"])
        self.assertTrue(
            self.payload["overall"]["nontrivial_double_gate_admitted_review_only"]
        )

    def test_nontrivial_mirror_still_pays_t507_operation_and_hiddenness_gates(self) -> None:
        full_born = self.decisions["nontrivial_mirror_full_born"]
        no_recovery = self.decisions["nontrivial_mirror_no_recovery"]

        self.assertFalse(full_born["admitted"])
        self.assertEqual(
            full_born["label"],
            "REJECTED_NONTRIVIAL_BUT_FULL_BORN_VISIBLE",
        )
        self.assertFalse(full_born["t507_double_gate_paid"])
        self.assertIn("full-space Born", full_born["strongest_allowed_reading"])

        self.assertFalse(no_recovery["admitted"])
        self.assertEqual(
            no_recovery["label"],
            "REJECTED_NONTRIVIAL_BUT_NO_RECORD_RECOVERY",
        )
        self.assertFalse(no_recovery["t507_double_gate_paid"])
        self.assertIn("operation algebra", no_recovery["strongest_allowed_reading"])

    def test_post_hoc_and_missing_control_packets_are_rejected(self) -> None:
        post_hoc = self.decisions["post_hoc_q_shortcut"]
        missing = self.decisions["missing_controls_shortcut"]

        self.assertFalse(post_hoc["admitted"])
        self.assertEqual(post_hoc["label"], "REJECTED_INCOMPLETE_CONSTRAINT_PACKET")
        self.assertIn(
            "predeclared constraint operator Q",
            post_hoc["missing_requirements"],
        )

        self.assertFalse(missing["admitted"])
        self.assertEqual(missing["label"], "REJECTED_INCOMPLETE_CONSTRAINT_PACKET")
        self.assertIn(
            "declared quotient/cohomology object",
            missing["missing_requirements"],
        )
        self.assertIn("Q-closed observable discipline", missing["missing_requirements"])
        self.assertIn(
            "exact-mirror redundancy control",
            missing["missing_requirements"],
        )

    def test_untyped_brst_and_claim_cross_repo_shortcuts_are_blocked(self) -> None:
        untyped = self.decisions["untyped_brst_shortcut"]
        shortcut = self.decisions["claim_cross_repo_shortcut"]

        self.assertFalse(untyped["admitted"])
        self.assertEqual(untyped["label"], "REJECTED_UNTYPED_BRST_ASSERTION")
        self.assertIn("constraint", untyped["strongest_allowed_reading"])

        self.assertFalse(shortcut["admitted"])
        self.assertEqual(
            shortcut["label"],
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
        )
        self.assertEqual(shortcut["action"], "stop")
        self.assertFalse(shortcut["counts_as_claim_evidence"])

    def test_future_minimum_and_not_earned_are_explicit(self) -> None:
        minimum = self.payload["future_packet_minimum"]
        blocked = self.payload["not_earned"]

        self.assertIn(
            "predeclare the constraint or gauge operator Q before selecting the mirror pair",
            minimum,
        )
        self.assertIn("prove Q is nilpotent with Q^2 = 0", minimum)
        self.assertIn(
            "decide exactness by membership in im(Q), not by assertion",
            minimum,
        )
        self.assertIn("real BRST exactness decision", blocked)
        self.assertIn("real BRST cohomology nontriviality decision", blocked)
        self.assertIn("hidden mirror record claim", blocked)
        self.assertIn("cross-repo truth movement", blocked)

    def test_payload_is_json_serializable_without_forbidden_overreads(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("BRST_COHOMOLOGY_RECORD_GATE_BUILT_REVIEW_ONLY", dumped)
        forbidden = (
            "BRST exactness proven",
            "BRST nontriviality proven",
            "hidden record proven",
            "physics claim earned",
            "claim ledger promoted",
            "cross-repo truth established",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
