"""Tests for T99: LossKernel quotient-separation audit."""

from __future__ import annotations

import unittest

from models.losskernel_quotient_separation import (
    attribution_verdict,
    naive_quotient_key,
    path_fixtures,
    run_t99_analysis,
    typed_signature,
)


class LossKernelQuotientSeparationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = {case.name: case for case in path_fixtures()}

    def test_collision_cases_share_naive_quotient_key(self) -> None:
        relevant = self.cases["collision_path_relevant_witness"]
        decorative = self.cases["collision_path_decorative_label"]

        self.assertEqual(naive_quotient_key(relevant), naive_quotient_key(decorative))
        self.assertEqual(relevant.naive_loss_labels, decorative.naive_loss_labels)
        self.assertEqual(relevant.ordinary_composite_map, decorative.ordinary_composite_map)
        self.assertEqual(
            relevant.endpoint_behavior.signature(),
            decorative.endpoint_behavior.signature(),
        )

    def test_collision_cases_receive_different_attribution_verdicts(self) -> None:
        relevant = self.cases["collision_path_relevant_witness"]
        decorative = self.cases["collision_path_decorative_label"]

        self.assertEqual(attribution_verdict(relevant), "admissible_typed_attribution")
        self.assertEqual(attribution_verdict(decorative), "inadmissible_label_only_metadata")
        self.assertNotEqual(typed_signature(relevant), typed_signature(decorative))

    def test_naive_label_kernel_fails_quotient_gate(self) -> None:
        result = run_t99_analysis()

        self.assertTrue(result.naive_label_kernel_fails_quotient_gate)
        collision_groups = [group for group in result.quotient_groups if group.naive_collision]
        self.assertEqual(len(collision_groups), 1)
        self.assertIn(
            "collision_path_relevant_witness",
            collision_groups[0].case_names,
        )

    def test_typed_witness_kernel_separates_collision(self) -> None:
        result = run_t99_analysis()

        self.assertTrue(result.typed_witness_kernel_separates_collision)
        self.assertIn("source-anchored witness obligations", result.strongest_claim)

    def test_same_typed_control_collapses(self) -> None:
        alias_a = self.cases["same_typed_alias_a"]
        alias_b = self.cases["same_typed_alias_b"]

        self.assertEqual(naive_quotient_key(alias_a), naive_quotient_key(alias_b))
        self.assertEqual(typed_signature(alias_a), typed_signature(alias_b))
        self.assertEqual(attribution_verdict(alias_a), attribution_verdict(alias_b))
        self.assertTrue(run_t99_analysis().same_typed_control_collapses)

    def test_endpoint_difference_control_is_not_quotient_evidence(self) -> None:
        control = self.cases["endpoint_difference_control"]

        self.assertEqual(
            attribution_verdict(control),
            "inadmissible_no_target_obstruction",
        )
        self.assertTrue(run_t99_analysis().endpoint_difference_control_excluded)

    def test_tf1_is_weakened_not_promoted(self) -> None:
        result = run_t99_analysis()

        self.assertIn("open formal target", result.tf1_update)
        self.assertIn("Label-only loss is refuted", result.tf1_update)
        self.assertIn("cannot be promoted from T73", result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
