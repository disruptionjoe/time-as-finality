"""Tests for T183: weak-measurement reinstatement stack."""

from __future__ import annotations

import unittest

from models.weak_measurement_reinstatement_stack import (
    canonical_reinstatement_cases,
    classify_reinstatement_stack,
    current_frontier_case,
    run_t183_analysis,
)


class WeakMeasurementReinstatementStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = dict(canonical_reinstatement_cases())
        self.result = run_t183_analysis()
        self.audits = {audit.name: audit for audit in self.result.audits}

    def test_extra_environment_stack_positive_control_is_admitted(self) -> None:
        audit = classify_reinstatement_stack(
            self.cases["positive_control_extra_environment_stack"],
            name="positive_control_extra_environment_stack",
        )

        self.assertEqual(audit.classification, "candidate_q1c_reinstatement_route")
        self.assertTrue(audit.reinstatement_candidate)
        self.assertEqual(audit.verdict_classification, "candidate_typed_verdict_route")

    def test_enlarged_instrument_stack_positive_control_is_admitted(self) -> None:
        audit = self.audits["positive_control_enlarged_instrument_stack"]

        self.assertTrue(audit.reinstatement_candidate)
        self.assertEqual(
            audit.preserved_target_classification,
            "candidate_honest_enlarged_instrument_route",
        )

    def test_packet_only_case_is_not_reinstatement(self) -> None:
        audit = self.audits["packet_only_no_event_data"]

        self.assertEqual(audit.classification, "blocked_missing_event_level_verdict_data")
        self.assertFalse(audit.reinstatement_candidate)

    def test_zero_lift_case_stays_blocked_at_verdict_gate(self) -> None:
        audit = self.audits["zero_lift_extra_environment_packet"]

        self.assertEqual(
            audit.classification,
            "blocked_at_verdict_gate:null_t149_architecture_not_cleared",
        )
        self.assertFalse(audit.reinstatement_candidate)

    def test_auxiliary_defined_verdict_is_rejected(self) -> None:
        audit = self.audits["auxiliary_defined_verdict_packet"]

        self.assertEqual(
            audit.classification,
            "blocked_at_verdict_gate:null_auxiliary_defined_verdict",
        )
        self.assertFalse(audit.reinstatement_candidate)

    def test_enlarged_target_drift_is_rejected_before_verdict_upgrade(self) -> None:
        audit = self.audits["enlarged_instrument_target_drift"]

        self.assertEqual(
            audit.classification,
            "blocked_at_preserved_target_gate:null_target_drift_under_enlargement",
        )
        self.assertFalse(audit.reinstatement_candidate)

    def test_current_frontier_remains_closed(self) -> None:
        name, proposal = current_frontier_case()
        audit = classify_reinstatement_stack(proposal, name=name)

        self.assertTrue(audit.classification.startswith("blocked_at_packet_gate"))
        self.assertFalse(audit.reinstatement_candidate)
        self.assertFalse(self.result.current_frontier_reopened)
        self.assertTrue(self.result.positive_controls_admitted)
        self.assertTrue(self.result.null_controls_rejected)


if __name__ == "__main__":
    unittest.main()
