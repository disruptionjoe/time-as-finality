"""Tests for T510 BRST conserved-ledger compatibility gate."""

from __future__ import annotations

import json
import unittest

from models.brst_conserved_ledger_compatibility_gate import run


class BrstConservedLedgerCompatibilityGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = run()
        self.decisions = {
            item["packet_id"]: item for item in self.payload["decisions"]
        }

    def test_verdict_and_scope_are_review_only(self) -> None:
        self.assertEqual(
            self.payload["verdict"],
            "BRST_CONSERVED_LEDGER_GATE_BUILT_STABILITY_REVIEW_ONLY",
        )
        overall = self.payload["overall"]
        self.assertFalse(overall["claim_movement"])
        self.assertFalse(overall["public_posture_movement"])
        self.assertFalse(overall["external_publication"])
        self.assertFalse(overall["cross_repo_truth_movement"])
        self.assertFalse(overall["sibling_repo_inspection"])
        self.assertFalse(overall["unitarity_theorem_claimed"])
        self.assertFalse(overall["physical_inner_product_chosen"])
        self.assertFalse(overall["hidden_mirror_record_claim_earned"])
        self.assertFalse(overall["physics_claim_earned"])

    def test_fixture_keeps_t509_nontrivial_mirror_class(self) -> None:
        states = self.payload["states"]
        summary = self.payload["constraint_summaries"]["nontrivial_mirror"]

        self.assertTrue(states["share_wplus_before_dynamics"])
        self.assertGreater(states["mirror_delta_before_dynamics"], 0.0)
        self.assertTrue(summary["q_nilpotent"])
        self.assertTrue(summary["mirror_q_closed"])
        self.assertFalse(summary["mirror_q_exact"])
        self.assertTrue(summary["mirror_cohomology_nontrivial"])

    def test_conserved_direct_cohomology_ledger_is_review_only(self) -> None:
        decision = self.decisions["conserved_direct_cohomology_ledger"]

        self.assertTrue(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "ADMITTED_CONSERVED_COHOMOLOGY_LEDGER_REVIEW_TARGET",
        )
        self.assertTrue(decision["dynamics_descends_to_cohomology"])
        self.assertTrue(decision["readout_descends_to_cohomology"])
        self.assertTrue(decision["ledger_conserved"])
        self.assertEqual(decision["ledger_drift_score"], 0.0)
        self.assertGreater(decision["cohomology_readout_delta"], 0.0)
        self.assertFalse(decision["counts_as_claim_evidence"])
        self.assertTrue(
            self.payload["overall"][
                "direct_cohomology_ledger_admitted_review_only"
            ]
        )

    def test_exact_representative_noise_is_absorbed_when_ledger_is_stable(self) -> None:
        decision = self.decisions["exact_representative_noise_control"]

        self.assertTrue(decision["admitted"])
        self.assertTrue(decision["dynamics_descends_to_cohomology"])
        self.assertTrue(decision["readout_descends_to_cohomology"])
        self.assertTrue(decision["ledger_conserved"])
        self.assertGreater(decision["exact_representative_noise_score"], 0.0)
        self.assertTrue(decision["exact_representative_noise_absorbed"])
        self.assertTrue(self.payload["overall"]["exact_representative_noise_absorbed"])

    def test_cohomology_scaling_drift_is_rejected_even_when_dynamics_descends(self) -> None:
        decision = self.decisions["cohomology_scaling_drift_control"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_NONCONSERVED_COHOMOLOGY_LEDGER",
        )
        self.assertTrue(decision["dynamics_descends_to_cohomology"])
        self.assertTrue(decision["readout_descends_to_cohomology"])
        self.assertFalse(decision["ledger_conserved"])
        self.assertGreater(decision["ledger_drift_score"], 0.0)
        self.assertTrue(self.payload["overall"]["cohomology_drift_rejected"])

    def test_full_krein_dynamics_is_rejected_when_it_does_not_descend(self) -> None:
        decision = self.decisions["full_krein_dynamics_shortcut"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_DYNAMICS_NOT_BRST_COMPATIBLE",
        )
        self.assertFalse(decision["dynamics_descends_to_cohomology"])
        self.assertTrue(self.payload["overall"]["nondescending_dynamics_rejected"])

    def test_wplus_ledger_shortcut_is_rejected_by_exact_invariance(self) -> None:
        decision = self.decisions["wplus_ledger_shortcut"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(decision["label"], "REJECTED_NON_DESCENDING_LEDGER_READOUT")
        self.assertTrue(decision["dynamics_descends_to_cohomology"])
        self.assertFalse(decision["readout_descends_to_cohomology"])
        self.assertIn("exact-invariant ledger readout", decision["missing_requirements"])
        self.assertTrue(self.payload["overall"]["non_descending_readout_rejected"])

    def test_exact_mirror_and_non_nilpotent_controls_are_rejected(self) -> None:
        exact = self.decisions["exact_mirror_redundancy_control"]
        non_nilpotent = self.decisions["non_nilpotent_constraint_control"]

        self.assertFalse(exact["admitted"])
        self.assertEqual(exact["label"], "BRST_EXACT_REDUNDANCY_RECORDED")
        self.assertTrue(exact["mirror_q_exact"])
        self.assertFalse(exact["mirror_cohomology_nontrivial"])
        self.assertTrue(self.payload["overall"]["exact_mirror_routes_to_redundancy"])

        self.assertFalse(non_nilpotent["admitted"])
        self.assertEqual(non_nilpotent["label"], "REJECTED_NON_NILPOTENT_CONSTRAINT")
        self.assertFalse(non_nilpotent["q_nilpotent"])
        self.assertIn("nilpotency Q^2 = 0", non_nilpotent["missing_requirements"])

    def test_incomplete_and_claim_shortcuts_are_blocked(self) -> None:
        missing = self.decisions["missing_controls_shortcut"]
        claim = self.decisions["claim_cross_repo_shortcut"]

        self.assertFalse(missing["admitted"])
        self.assertEqual(missing["label"], "REJECTED_INCOMPLETE_LEDGER_PACKET")
        self.assertIn("non-descending dynamics control", missing["missing_requirements"])
        self.assertIn("ledger drift control", missing["missing_requirements"])
        self.assertIn(
            "exact-representative noise control",
            missing["missing_requirements"],
        )

        self.assertFalse(claim["admitted"])
        self.assertEqual(claim["label"], "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT")
        self.assertEqual(claim["action"], "stop")
        self.assertFalse(claim["counts_as_claim_evidence"])

    def test_future_minimum_and_not_earned_are_explicit(self) -> None:
        minimum = self.payload["future_packet_minimum"]
        blocked = self.payload["not_earned"]

        self.assertIn(
            "prove the quotient readout is conserved by the declared dynamics",
            minimum,
        )
        self.assertIn("include non-descending dynamics and ledger-drift controls", minimum)
        self.assertIn(
            "do not treat W+ representative leakage or drifting cohomology as a hidden physical record",
            minimum,
        )
        self.assertIn("unitarity theorem", blocked)
        self.assertIn("physical inner product selection", blocked)
        self.assertIn("hidden mirror record claim", blocked)
        self.assertIn("cross-repo truth movement", blocked)

    def test_payload_is_json_serializable_without_forbidden_overreads(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn(
            "BRST_CONSERVED_LEDGER_GATE_BUILT_STABILITY_REVIEW_ONLY",
            dumped,
        )
        forbidden = (
            "unitarity proven",
            "physical inner product selected",
            "hidden record proven",
            "claim ledger promoted",
            "cross-repo truth established",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
