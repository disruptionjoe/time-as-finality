"""Tests for T90 weak-measurement reparameterization obstruction."""

from __future__ import annotations

import unittest

from models.weak_measurement_reparameterization_obstruction import (
    audit_pair,
    classify_single_protocol,
    compute_finality_times,
    independent_branch_fixture_pair,
    independent_branch_protocol,
    null_protocol,
    null_reparameterization_fixture,
    post_hoc_branch_protocol,
    run_t90_analysis,
)


class WeakMeasurementReparameterizationObstructionTests(unittest.TestCase):
    def test_standard_only_protocol_is_null_reparameterization(self) -> None:
        protocol = null_protocol()
        trajectory = null_reparameterization_fixture()
        times = compute_finality_times(trajectory, protocol)

        self.assertEqual(classify_single_protocol(protocol), "null_reparameterization")
        self.assertEqual(times.decoherence_time, 4.0)
        self.assertEqual(times.redundancy_time, 3.0)
        self.assertEqual(times.access_time, 3.0)
        self.assertEqual(times.taf_finality_time, 3.0)

    def test_independent_branch_pair_is_isolated_non_null_candidate(self) -> None:
        early, late = independent_branch_fixture_pair()
        audit = audit_pair(early, late, independent_branch_protocol())

        self.assertTrue(audit.standard_timelines_equal)
        self.assertTrue(audit.standard_verdict_equal)
        self.assertTrue(audit.taf_verdict_changes)
        self.assertTrue(audit.has_independent_source)
        self.assertFalse(audit.rejected_for_post_hoc_source)
        self.assertEqual(audit.verdict, "candidate_non_null_witness")

    def test_independent_pair_changes_only_taf_time(self) -> None:
        early, late = independent_branch_fixture_pair()
        protocol = independent_branch_protocol()
        early_times = compute_finality_times(early, protocol)
        late_times = compute_finality_times(late, protocol)

        self.assertEqual(early_times.decoherence_time, late_times.decoherence_time)
        self.assertEqual(early_times.redundancy_time, late_times.redundancy_time)
        self.assertEqual(early_times.access_time, late_times.access_time)
        self.assertEqual(early_times.taf_finality_time, 3.0)
        self.assertEqual(late_times.taf_finality_time, 4.0)

    def test_post_hoc_branch_label_is_rejected_even_when_it_separates(self) -> None:
        early, late = independent_branch_fixture_pair()
        audit = audit_pair(early, late, post_hoc_branch_protocol())

        self.assertTrue(audit.taf_verdict_changes)
        self.assertFalse(audit.has_independent_source)
        self.assertTrue(audit.rejected_for_post_hoc_source)
        self.assertEqual(audit.verdict, "null_post_hoc")

    def test_t90_result_reports_claim_boundary(self) -> None:
        result = run_t90_analysis()

        self.assertEqual(result.null_verdict, "null_reparameterization")
        self.assertEqual(result.independent_pair.verdict, "candidate_non_null_witness")
        self.assertEqual(result.post_hoc_pair.verdict, "null_post_hoc")
        self.assertIn("does not yet predict new measurement dynamics", result.weakened_claim)
        self.assertIn("demote T12", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
