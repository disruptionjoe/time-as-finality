"""Tests for T507 finality record-redundancy double gate."""

from __future__ import annotations

import json
import unittest

from models.finality_record_redundancy_double_gate import run


class FinalityRecordRedundancyDoubleGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = run()
        self.decisions = {
            item["packet_id"]: item for item in self.payload["decisions"]
        }

    def test_verdict_and_scope_are_review_only(self) -> None:
        self.assertEqual(
            self.payload["verdict"],
            "FINALITY_RECORD_REDUNDANCY_DOUBLE_GATE_BUILT_DEFAULT_REDUNDANCY",
        )
        self.assertFalse(self.payload["overall"]["claim_movement"])
        self.assertFalse(self.payload["overall"]["public_posture_movement"])
        self.assertFalse(self.payload["overall"]["external_publication"])
        self.assertFalse(self.payload["overall"]["cross_repo_truth_movement"])
        self.assertFalse(self.payload["overall"]["sibling_repo_inspection"])
        self.assertFalse(self.payload["overall"]["brst_exactness_decided"])
        self.assertFalse(self.payload["overall"]["krein_quantization_decided"])
        self.assertFalse(self.payload["overall"]["physics_claim_earned"])

    def test_carrier_reproduces_the_two_underlying_exploratory_findings(self) -> None:
        carrier = self.payload["carrier"]

        self.assertTrue(carrier["states_share_wplus"])
        self.assertTrue(carrier["states_differ_in_wminus"])
        self.assertTrue(carrier["mirror_negative_under_krein_form"])
        self.assertTrue(carrier["mirror_positive_under_standard_inner_product"])
        self.assertLess(carrier["individual_recovery_score"], 1e-9)
        self.assertGreater(carrier["collective_recovery_score"], 0.1)
        self.assertGreater(carrier["full_born_max_delta"], 1e-6)
        self.assertLess(carrier["selfnorm_max_delta"], 1e-9)
        self.assertGreater(carrier["full_space_observer_mirror_number_delta"], 0.01)

    def test_standard_positivity_default_records_redundancy(self) -> None:
        decision = self.decisions["standard_positivity_default"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REDUNDANCY_UNDER_STANDARD_POSITIVITY",
        )
        self.assertEqual(decision["action"], "record_negative")
        self.assertFalse(decision["mirror_recoverable_by_declared_algebra"])
        self.assertTrue(self.payload["overall"]["standard_default_redundancy"])
        self.assertEqual(self.payload["overall"]["default_corner"], "redundancy")

    def test_full_krein_full_born_is_visible_not_hidden_record(self) -> None:
        decision = self.decisions["krein_retention_full_born"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_AS_HIDDEN_RECORD_FULL_BORN_LEAKAGE",
        )
        self.assertEqual(decision["action"], "demote_to_visible_physical_dof")
        self.assertTrue(decision["mirror_recoverable_by_declared_algebra"])
        self.assertFalse(decision["hidden_under_declared_normalization"])
        self.assertTrue(decision["full_born_leakage_present"])

    def test_krein_selfnorm_corner_is_the_only_hidden_record_review_target(self) -> None:
        decision = self.decisions["krein_retention_selfnorm_corner"]

        self.assertTrue(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "ADMITTED_HIDDEN_RECORD_REVIEW_TARGET_DOUBLE_GATED",
        )
        self.assertEqual(decision["action"], "review_only")
        self.assertTrue(decision["mirror_recoverable_by_declared_algebra"])
        self.assertTrue(decision["hidden_under_declared_normalization"])
        self.assertTrue(decision["double_special_corner"])
        self.assertFalse(decision["counts_as_claim_evidence"])
        self.assertTrue(
            self.payload["overall"]["hidden_record_corner_admitted_review_only"]
        )
        self.assertTrue(
            self.payload["overall"]["record_reading_requires_two_special_bets"]
        )

    def test_self_normalization_alone_does_not_create_record_recovery(self) -> None:
        decision = self.decisions["positivity_selfnorm_no_recovery"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REDUNDANCY_UNDER_STANDARD_POSITIVITY",
        )
        self.assertTrue(decision["hidden_under_declared_normalization"])
        self.assertFalse(decision["mirror_recoverable_by_declared_algebra"])

    def test_degenerate_no_mirror_spread_control_is_rejected(self) -> None:
        decision = self.decisions["degenerate_no_mirror_spread_control"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_DEGENERATE_NO_MIRROR_SPREAD",
        )
        self.assertFalse(decision["mirror_recoverable_by_declared_algebra"])
        self.assertTrue(decision["hidden_under_declared_normalization"])

    def test_untyped_brst_assertion_is_rejected(self) -> None:
        decision = self.decisions["untyped_brst_assertion_shortcut"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_UNTYPED_BRST_STATUS_ASSERTION",
        )
        self.assertIn("constraint/gauge structure", decision["strongest_allowed_reading"])

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
            "declare the admissible operation algebra before the record/redundancy verdict",
            minimum,
        )
        self.assertIn(
            "declare the observer normalization rule before checking hiddenness",
            minimum,
        )
        self.assertIn("BRST exactness decision", blocked)
        self.assertIn("Krein-retention quantization accepted as physical", blocked)
        self.assertIn("hidden mirror record claim", blocked)
        self.assertIn("cross-repo truth movement", blocked)

    def test_payload_is_json_serializable_without_forbidden_overreads(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn(
            "FINALITY_RECORD_REDUNDANCY_DOUBLE_GATE_BUILT_DEFAULT_REDUNDANCY",
            dumped,
        )
        forbidden = (
            "BRST exactness proven",
            "Krein quantization accepted",
            "hidden record proven",
            "physics claim earned",
            "claim ledger promoted",
            "cross-repo truth established",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
