"""Tests for T104: Q1A provenance-aware Darwinism absorption."""

from __future__ import annotations

import unittest

from models.q1a_provenance_absorption import run_t104_analysis, score_t104_case, t104_cases


class Q1AProvenanceAbsorptionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = {case.case_id: case for case in t104_cases()}
        self.baseline = self.cases["independent_records_fixed_data"].quantum_side

    def test_raw_redundancy_stays_fixed_while_partitioned_redundancy_changes(self) -> None:
        independent = score_t104_case(
            self.cases["independent_records_fixed_data"],
            self.baseline,
        )
        copied = score_t104_case(
            self.cases["copied_archive_fixed_data"],
            self.baseline,
        )

        self.assertEqual(independent.raw_accessible_redundancy, 3)
        self.assertEqual(copied.raw_accessible_redundancy, 3)
        self.assertEqual(independent.provenance_aware_redundancy, 3)
        self.assertEqual(copied.provenance_aware_redundancy, 2)

    def test_provenance_aware_qd_matches_d1_on_fixed_data_cases(self) -> None:
        for case_id in (
            "independent_records_fixed_data",
            "copied_archive_fixed_data",
        ):
            with self.subTest(case_id=case_id):
                verdict = score_t104_case(self.cases[case_id], self.baseline)
                self.assertEqual(verdict.absorption_status, "absorbed")
                self.assertEqual(verdict.provenance_qd_verdict, verdict.d1_verdict)

    def test_hidden_partition_withholds_for_both_frameworks(self) -> None:
        verdict = score_t104_case(
            self.cases["partition_hidden_fixed_data"],
            self.baseline,
        )

        self.assertIsNone(verdict.provenance_aware_redundancy)
        self.assertEqual(verdict.d1_verdict, "withhold_partition_unavailable")
        self.assertEqual(
            verdict.provenance_qd_verdict,
            "withhold_partition_unavailable",
        )

    def test_t104_is_a_kill_test_not_a_novelty_upgrade(self) -> None:
        result = run_t104_analysis()

        self.assertTrue(result.exact_absorption_on_fixed_data_cases)
        self.assertTrue(result.hidden_partition_withholds_for_both)
        self.assertFalse(result.external_distinctness_earned)
        self.assertIn("exactly absorbed", result.strongest_claim)
        self.assertIn("bookkeeping or admissibility discipline", result.weakened)


if __name__ == "__main__":
    unittest.main()
