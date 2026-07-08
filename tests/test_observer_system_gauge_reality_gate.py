"""Tests for T505 observer/system gauge reality gate."""

from __future__ import annotations

import json
import unittest

from models.observer_system_gauge_reality_gate import run


class ObserverSystemGaugeRealityGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = run()
        self.decisions = {
            item["packet_id"]: item for item in self.payload["decisions"]
        }

    def test_verdict_and_scope_are_review_only(self) -> None:
        self.assertEqual(
            self.payload["verdict"],
            "OBSERVER_SYSTEM_GAUGE_REALITY_GATE_BUILT_DINOSAUR_GUARD_REVIEW_ONLY",
        )
        self.assertTrue(self.payload["overall"]["review_target_only"])
        self.assertFalse(self.payload["overall"]["claim_movement"])
        self.assertFalse(self.payload["overall"]["public_posture_movement"])
        self.assertFalse(self.payload["overall"]["external_publication"])
        self.assertFalse(self.payload["overall"]["cross_repo_truth_movement"])
        self.assertFalse(self.payload["overall"]["sibling_repo_inspection"])

    def test_proven_equivalence_routes_to_invariant_only(self) -> None:
        decision = self.decisions["coordinate_relabeling_equivalence"]

        self.assertFalse(decision["admitted"])
        self.assertTrue(decision["genuine_gauge"])
        self.assertEqual(
            decision["label"],
            "GENUINE_GAUGE_EQUIVALENCE_INVARIANT_ONLY",
        )
        self.assertEqual(decision["action"], "treat_as_invariant")
        self.assertFalse(decision["counts_as_claim_evidence"])

    def test_no_difference_only_shortcut_is_rejected(self) -> None:
        decision = self.decisions["no_difference_only_gauge_shortcut"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(decision["label"], "REJECTED_VERIFICATIONIST_GAUGE_SHORTCUT")
        self.assertFalse(decision["genuine_gauge"])
        self.assertTrue(
            self.payload["overall"]["verificationist_gauge_shortcut_rejected"]
        )

    def test_unobservable_hard_to_vary_structure_is_not_demoted_to_gauge(self) -> None:
        decision = self.decisions["dinosaur_hidden_cause_calibration"]

        self.assertTrue(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "ADMITTED_UNOBSERVABLE_BUT_HARD_TO_VARY_REVIEW_TARGET",
        )
        self.assertTrue(decision["unobservable_but_real_candidate"])
        self.assertFalse(decision["genuine_gauge"])
        self.assertFalse(decision["counts_as_claim_evidence"])

    def test_current_two_adapter_state_is_review_only_and_decorrelation_pending(self) -> None:
        decision = self.decisions["current_two_adapter_single_process"]

        self.assertTrue(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "ADMITTED_SINGLE_PROCESS_INDEPENDENT_FORCING_DECORRELATION_PENDING",
        )
        self.assertTrue(decision["current_adapter_state"])
        self.assertTrue(decision["de_correlation_pending"])
        self.assertFalse(decision["de_correlation_requirement_met"])
        self.assertFalse(self.payload["overall"]["current_two_adapter_gate_closed"])

    def test_future_decorrelated_packet_is_admitted_as_review_target_only(self) -> None:
        decision = self.decisions["future_decorrelated_two_adapter_packet"]

        self.assertTrue(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "ADMITTED_DECORRELATED_HARD_TO_VARY_REVIEW_TARGET",
        )
        self.assertTrue(decision["de_correlation_requirement_met"])
        self.assertFalse(decision["de_correlation_pending"])
        self.assertFalse(decision["counts_as_claim_evidence"])
        self.assertTrue(
            self.payload["overall"]["future_decorrelated_packet_admitted_for_review"]
        )

    def test_trivial_and_shared_knob_convergence_are_rejected(self) -> None:
        constant = self.decisions["constant_functor_convergence"]
        shared = self.decisions["shared_knob_manufactured_convergence"]

        self.assertFalse(constant["admitted"])
        self.assertEqual(constant["label"], "REJECTED_TRIVIAL_OR_CONSTANT_CONVERGENCE")
        self.assertFalse(shared["admitted"])
        self.assertEqual(shared["label"], "REJECTED_MANUFACTURED_CONVERGENCE_RISK")
        self.assertTrue(self.payload["overall"]["manufactured_convergence_rejected"])

    def test_missing_hard_to_vary_burden_is_rejected(self) -> None:
        decision = self.decisions["missing_hard_to_vary_burden"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(decision["label"], "REJECTED_MISSING_HARD_TO_VARY_BURDEN")
        self.assertIn("hard_to_vary_explanation", decision["missing_requirements"])
        self.assertIn(
            "falsifiable_disagreement_control",
            decision["missing_requirements"],
        )

    def test_external_and_cross_repo_shortcuts_are_blocked(self) -> None:
        decision = self.decisions["external_cross_repo_shortcut"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(decision["label"], "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT")
        self.assertEqual(decision["action"], "stop")
        self.assertFalse(decision["counts_as_claim_evidence"])

    def test_future_minimum_and_not_earned_are_explicit(self) -> None:
        minimum = self.payload["future_decorrelation_minimum"]
        blocked = self.payload["not_earned"]

        self.assertIn("do not infer gauge from lack of direct observability", minimum)
        self.assertIn("fix the observer/system split independently on each adapter", minimum)
        self.assertIn("GU/TI/TaF adapter identity", blocked)
        self.assertIn(
            "two-adapter gate closure for the current single-process build",
            blocked,
        )
        self.assertIn("cross-repo truth movement", blocked)

    def test_payload_is_json_serializable_without_forbidden_overreads(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn(
            "OBSERVER_SYSTEM_GAUGE_REALITY_GATE_BUILT_DINOSAUR_GUARD_REVIEW_ONLY",
            dumped,
        )
        forbidden = (
            "adapter identity proven",
            "cross-repo truth established",
            "public posture authorized",
            "therefore observer/system split is gauge",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
