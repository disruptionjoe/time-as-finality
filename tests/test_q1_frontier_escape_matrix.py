"""Tests for T140: Q1 frontier escape matrix."""

from __future__ import annotations

import unittest

from models.q1_frontier_escape_matrix import (
    Q1AInput,
    Q1BInput,
    Q1CInput,
    Q1DInput,
    classify_q1a,
    classify_q1b,
    classify_q1c,
    classify_q1d,
    run_t140_analysis,
)


class Q1AEscapeGateTests(unittest.TestCase):
    def test_current_q1a_shape_is_bookkeeping_only(self) -> None:
        audit = classify_q1a(
            Q1AInput(
                fixed_standard_quantum_summaries=True,
                provenance_partition_shared=True,
                same_audited_accessible_support=True,
                verdict_split_at_same_support=False,
                physical_dimension_beyond_support=False,
                partition_rule_nonimportable_by_neighbor=False,
            )
        )
        self.assertEqual(audit.classification, "bookkeeping_only")
        self.assertFalse(audit.active_internal_route)

    def test_same_support_split_needs_physical_dimension_or_nonimportable_rule(self) -> None:
        underjustified = classify_q1a(
            Q1AInput(
                fixed_standard_quantum_summaries=True,
                provenance_partition_shared=True,
                same_audited_accessible_support=True,
                verdict_split_at_same_support=True,
                physical_dimension_beyond_support=False,
                partition_rule_nonimportable_by_neighbor=False,
            )
        )
        candidate = classify_q1a(
            Q1AInput(
                fixed_standard_quantum_summaries=True,
                provenance_partition_shared=True,
                same_audited_accessible_support=True,
                verdict_split_at_same_support=True,
                physical_dimension_beyond_support=True,
                partition_rule_nonimportable_by_neighbor=False,
            )
        )
        self.assertEqual(underjustified.classification, "underjustified_same_support_split")
        self.assertFalse(underjustified.active_internal_route)
        self.assertEqual(candidate.classification, "candidate_nonredundant_q1a_escape")
        self.assertTrue(candidate.active_internal_route)


class Q1BEscapeGateTests(unittest.TestCase):
    def test_manifest_without_real_rows_is_not_live_evidence(self) -> None:
        audit = classify_q1b(
            Q1BInput(
                t138_workflow_fit=True,
                pre_event_manifest_signed=True,
                real_event_rows_published=False,
                packet_schema_unchanged_after_manifest=True,
                passes_packet_and_authority_gates=True,
                survives_t83_null_criterion=True,
            )
        )
        self.assertEqual(audit.classification, "externally_blocked_no_event_rows")
        self.assertFalse(audit.live_evidence)

    def test_complete_packet_is_candidate_live_evidence(self) -> None:
        audit = classify_q1b(
            Q1BInput(
                t138_workflow_fit=True,
                pre_event_manifest_signed=True,
                real_event_rows_published=True,
                packet_schema_unchanged_after_manifest=True,
                passes_packet_and_authority_gates=True,
                survives_t83_null_criterion=True,
            )
        )
        self.assertEqual(audit.classification, "candidate_detector_evidence_packet")
        self.assertTrue(audit.live_evidence)


class Q1CEscapeGateTests(unittest.TestCase):
    def test_coarse_standard_record_is_null(self) -> None:
        audit = classify_q1c(
            Q1CInput(
                full_event_standard_record_fixed=False,
                auxiliary_axis_independent_after_full_record=True,
                verdict_changes=True,
                postselected_or_schedule_proxy=False,
            )
        )
        self.assertEqual(audit.classification, "null_coarse_standard_record")
        self.assertFalse(audit.active_internal_route)

    def test_full_record_escape_is_candidate_route(self) -> None:
        audit = classify_q1c(
            Q1CInput(
                full_event_standard_record_fixed=True,
                auxiliary_axis_independent_after_full_record=True,
                verdict_changes=True,
                postselected_or_schedule_proxy=False,
            )
        )
        self.assertEqual(audit.classification, "candidate_full_record_escape")
        self.assertTrue(audit.active_internal_route)


class Q1DGuardrailTests(unittest.TestCase):
    def test_standard_contextuality_without_new_theorem_is_guardrail_only(self) -> None:
        audit = classify_q1d(
            Q1DInput(
                no_signalling_preserved=True,
                avoids_hidden_variable_reading=True,
                nonredundant_theorem_named=False,
                already_standard_contextuality=True,
            )
        )
        self.assertEqual(audit.classification, "guardrail_only")
        self.assertFalse(audit.active_internal_route)


class T140CurrentFrontierTests(unittest.TestCase):
    def test_current_frontier_has_no_internal_q1_upgrade(self) -> None:
        result = run_t140_analysis()
        classifications = {audit.branch: audit.classification for audit in result.audits}
        self.assertEqual(classifications["Q1A"], "bookkeeping_only")
        self.assertEqual(classifications["Q1B"], "externally_blocked_no_signed_manifest")
        self.assertEqual(classifications["Q1C"], "null_screened_off_by_full_record")
        self.assertEqual(classifications["Q1D"], "guardrail_only")
        self.assertFalse(result.internal_q1_upgrade_available)
        self.assertTrue(result.q1b_is_only_external_experimental_path)
        self.assertIn("Do not spend the next internal research run", result.overall_recommendation)


if __name__ == "__main__":
    unittest.main()
