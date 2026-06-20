"""Tests for T79: dashboard summary nonidentifiability."""

from __future__ import annotations

import unittest

from models.dashboard_summary_nonidentifiability import (
    ambiguous_dashboard_spoof_fixture,
    dashboard_projection,
    robust_signed_raw_log_fixture,
    run_t79_analysis,
)


class DashboardSummaryNonidentifiabilityTests(unittest.TestCase):
    def test_dashboard_projection_collapses_distinct_completions(self) -> None:
        signed = robust_signed_raw_log_fixture()
        spoofable = ambiguous_dashboard_spoof_fixture()

        self.assertEqual(dashboard_projection(signed), dashboard_projection(spoofable))

    def test_hidden_provenance_fields_still_differ(self) -> None:
        signed = robust_signed_raw_log_fixture()
        spoofable = ambiguous_dashboard_spoof_fixture()

        self.assertNotEqual(
            signed.accepted_spoofed_independent_tags.observed,
            spoofable.accepted_spoofed_independent_tags.observed,
        )
        self.assertNotEqual(signed.dag_observability.observed, spoofable.dag_observability.observed)
        self.assertNotEqual(
            signed.perturbation_back_action_events.observed,
            spoofable.perturbation_back_action_events.observed,
        )

    def test_result_establishes_nonidentifiability_boundary(self) -> None:
        result = run_t79_analysis()

        self.assertTrue(result.dashboard_equal)
        audits = {audit.name: audit for audit in result.audits}
        self.assertEqual(
            audits["measured_signed_time_tag_stack"].verdict,
            "robust_measured_recovery",
        )
        self.assertEqual(
            audits["dashboard_matched_spoofable_completion"].verdict,
            "measured_conservative_withhold",
        )
        self.assertIn("non-identifying", result.strongest_claim)
        self.assertIn("Dashboard summaries are insufficient", result.q1_update)


if __name__ == "__main__":
    unittest.main()
