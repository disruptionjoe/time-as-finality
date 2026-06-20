"""Tests for T103: Q1A fixed-data witness gate."""

from __future__ import annotations

import unittest

from models.q1a_fixed_data_witness import (
    base_quantum_side,
    run_t103_analysis,
    score_case,
    witness_cases,
)


class Q1AFixedDataWitnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = {case.case_id: case for case in witness_cases()}
        self.baseline = self.cases["independent_records_fixed_data"].quantum_side

    def test_independent_and_copied_cases_keep_standard_quantum_side_data_fixed(
        self,
    ) -> None:
        independent = self.cases["independent_records_fixed_data"]
        copied = self.cases["copied_archive_fixed_data"]

        self.assertEqual(
            independent.quantum_side.fixed_neighbor_signature(),
            copied.quantum_side.fixed_neighbor_signature(),
        )
        self.assertEqual(independent.quantum_side.accessible_raw_redundancy(), 3)
        self.assertEqual(copied.quantum_side.accessible_raw_redundancy(), 3)

    def test_d1_verdict_changes_only_when_independence_partition_changes(self) -> None:
        independent = score_case(
            self.cases["independent_records_fixed_data"],
            self.baseline,
        )
        copied = score_case(self.cases["copied_archive_fixed_data"], self.baseline)

        self.assertTrue(independent.standard_data_matches_baseline)
        self.assertTrue(copied.standard_data_matches_baseline)
        self.assertEqual(independent.independent_accessible_support, 3)
        self.assertEqual(copied.independent_accessible_support, 2)
        self.assertEqual(independent.d1_verdict, "finalized")
        self.assertEqual(copied.d1_verdict, "not_finalized")

    def test_hidden_independence_partition_withholds_d1(self) -> None:
        verdict = score_case(
            self.cases["partition_hidden_fixed_data"],
            self.baseline,
        )

        self.assertTrue(verdict.standard_data_matches_baseline)
        self.assertEqual(verdict.accessible_raw_redundancy, 3)
        self.assertIsNone(verdict.independent_accessible_support)
        self.assertEqual(verdict.d1_verdict, "withhold_partition_unavailable")

    def test_standard_data_negative_controls_are_rejected(self) -> None:
        for case_id in (
            "coherence_changed_control",
            "raw_redundancy_changed_control",
            "branch_history_changed_control",
        ):
            with self.subTest(case_id=case_id):
                verdict = score_case(self.cases[case_id], self.baseline)
                self.assertFalse(verdict.standard_data_matches_baseline)
                self.assertEqual(verdict.d1_verdict, "invalid_fixed_data_gate")
                self.assertEqual(verdict.gate_verdict, "reject_standard_data_changed")

    def test_baseline_signature_tracks_required_neighbor_data(self) -> None:
        signature = base_quantum_side().fixed_neighbor_signature()

        self.assertIn("computational_z", signature)
        self.assertIn(0.0, signature)
        self.assertIn(3, signature)
        self.assertIn(("z0_history", "z1_history"), signature)

    def test_t103_claim_is_internal_not_external_measurement_distinction(self) -> None:
        result = run_t103_analysis()

        self.assertTrue(result.fixed_data_internal_witness_exists)
        self.assertTrue(result.negative_controls_rejected)
        self.assertTrue(result.hidden_partition_withholds)
        self.assertFalse(result.external_measurement_distinction_earned)
        self.assertIn("not yet an external measurement-theory distinction", result.strongest_claim)
        self.assertIn("collapses to bookkeeping", result.weakened)


if __name__ == "__main__":
    unittest.main()
