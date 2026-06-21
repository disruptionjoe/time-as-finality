"""Tests for T93 weak-measurement undo-cost independence."""

from __future__ import annotations

import unittest

from models.weak_measurement_undo_cost_independence import (
    audit_pair,
    control_energy_proxy_pair,
    independent_but_nondecisive_pair,
    independent_meter_pair,
    independent_meter_protocol,
    postselected_cost_pair,
    postselected_protocol,
    proxy_protocol,
    run_t93_analysis,
)


class WeakMeasurementUndoCostIndependenceTests(unittest.TestCase):
    def test_control_energy_proxy_is_null(self) -> None:
        left, right = control_energy_proxy_pair()
        audit = audit_pair("control_energy_proxy", left, right, proxy_protocol())

        self.assertEqual(audit.classification, "null_proxy_cost")
        self.assertTrue(audit.standard_timelines_equal)
        self.assertFalse(audit.undo_cost_differs)

    def test_postselected_reversal_success_is_null(self) -> None:
        left, right = postselected_cost_pair()
        audit = audit_pair("postselected_reversal_success", left, right, postselected_protocol())

        self.assertEqual(audit.classification, "null_postselected_cost")
        self.assertTrue(audit.undo_cost_differs)
        self.assertTrue(audit.taf_verdict_changes)

    def test_independent_meter_can_be_candidate_shape(self) -> None:
        left, right = independent_meter_pair()
        audit = audit_pair("independent_meter_candidate", left, right, independent_meter_protocol())

        self.assertEqual(audit.classification, "candidate_non_null_undo_cost_axis")
        self.assertTrue(audit.standard_timelines_equal)
        self.assertTrue(audit.undo_cost_differs)
        self.assertTrue(audit.taf_verdict_changes)

    def test_independent_meter_without_verdict_change_is_not_decisive(self) -> None:
        left, right = independent_but_nondecisive_pair()
        audit = audit_pair("independent_meter_nondecisive", left, right, independent_meter_protocol())

        self.assertEqual(audit.classification, "independent_but_not_decisive")
        self.assertTrue(audit.standard_timelines_equal)
        self.assertTrue(audit.undo_cost_differs)
        self.assertFalse(audit.taf_verdict_changes)

    def test_t93_result_keeps_route_blocked_without_real_meter(self) -> None:
        result = run_t93_analysis()

        classifications = {audit.case: audit.classification for audit in result.audits}
        self.assertEqual(classifications["control_energy_proxy"], "null_proxy_cost")
        self.assertEqual(classifications["postselected_reversal_success"], "null_postselected_cost")
        self.assertEqual(
            classifications["independent_meter_candidate"],
            "candidate_non_null_undo_cost_axis",
        )
        self.assertIn("No real platform", result.blocker)
        self.assertIn("demote weak measurement", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
