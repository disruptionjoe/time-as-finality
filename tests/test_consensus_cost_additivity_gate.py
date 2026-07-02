"""Tests for T396 consensus-cost additivity gate."""

from __future__ import annotations

import json
import math
import unittest

from models.consensus_cost_additivity_gate import (
    TOL,
    audit_task,
    canonical_tasks,
    run_t396_analysis,
    t396_result_to_dict,
)


class ConsensusCostAdditivityGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t396_analysis()
        self.by_id = {audit.task_id: audit for audit in self.result.audits}

    def test_root_copy_independent_scales_as_k_minus_one(self) -> None:
        for k in range(2, 7):
            audit = self.by_id[f"root_copy_independent_k{k}"]
            self.assertAlmostEqual(audit.input_entropy_bits, float(k), places=12)
            self.assertAlmostEqual(audit.output_entropy_bits, 1.0, places=12)
            self.assertAlmostEqual(audit.min_erasure_bits, float(k - 1), places=12)
            self.assertEqual(audit.verdict, "additive_entropy_bookkeeping_only")

    def test_already_consensus_refutes_holder_count_floor(self) -> None:
        audit = self.by_id["already_consensus_k5"]

        self.assertAlmostEqual(audit.input_entropy_bits, 1.0, places=12)
        self.assertAlmostEqual(audit.output_entropy_bits, 1.0, places=12)
        self.assertAlmostEqual(audit.min_erasure_bits, 0.0, places=12)
        self.assertTrue(audit.holder_count_floor_refuted)
        self.assertEqual(audit.verdict, "holder_count_floor_refuted_by_correlation")

    def test_majority_consensus_is_conditional_entropy_not_edge_term(self) -> None:
        for task_id, expected in (
            ("majority_independent_k3", 2.0),
            ("majority_independent_k5", 4.0),
        ):
            audit = self.by_id[task_id]
            self.assertAlmostEqual(audit.min_erasure_bits, expected, places=12)
            self.assertGreater(audit.conditional_correlation_credit_bits, 0.0)
            self.assertEqual(audit.verdict, "independent_reset_overcounts_joint_entropy")

    def test_single_error_majority_cost_is_error_location_entropy(self) -> None:
        audit = self.by_id["single_error_majority_k5"]

        self.assertAlmostEqual(audit.input_entropy_bits, 1.0 + math.log2(5), places=12)
        self.assertAlmostEqual(audit.output_entropy_bits, 1.0, places=12)
        self.assertAlmostEqual(audit.min_erasure_bits, math.log2(5), places=12)
        self.assertGreater(audit.conditional_correlation_credit_bits, 1.0)

    def test_constant_reset_erases_full_input_entropy(self) -> None:
        audit = self.by_id["constant_reset_independent_k4"]

        self.assertAlmostEqual(audit.input_entropy_bits, 4.0, places=12)
        self.assertAlmostEqual(audit.output_entropy_bits, 0.0, places=12)
        self.assertAlmostEqual(audit.min_erasure_bits, 4.0, places=12)

    def test_full_transcript_control_has_zero_closed_cost(self) -> None:
        self.assertTrue(self.result.full_transcript_control_zero_cost_all)
        for audit in self.result.audits:
            self.assertAlmostEqual(audit.exported_transcript_erasure_bits, 0.0, places=12)

    def test_no_extra_consensus_structure_term_is_found(self) -> None:
        self.assertTrue(self.result.no_extra_consensus_term_found)
        for audit in self.result.audits:
            self.assertAlmostEqual(audit.extra_consensus_structure_term_bits, 0.0, places=12)
            self.assertTrue(audit.ordinary_entropy_bookkeeping_explains)

    def test_task_factory_and_direct_audit_are_stable(self) -> None:
        tasks = canonical_tasks()
        self.assertEqual(len(tasks), len(self.result.audits))
        direct = audit_task(next(task for task in tasks if task.task_id == "parity_consensus_independent_k4"))
        self.assertAlmostEqual(direct.min_erasure_bits, 3.0, places=12)
        self.assertGreater(direct.conditional_correlation_credit_bits, 0.9)

    def test_result_dict_is_json_serializable(self) -> None:
        json.dumps(t396_result_to_dict(self.result))


if __name__ == "__main__":
    unittest.main()
