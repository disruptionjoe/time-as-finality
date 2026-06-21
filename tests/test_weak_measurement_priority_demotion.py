"""Tests for T94 weak-measurement priority demotion."""

from __future__ import annotations

import unittest

from models.weak_measurement_priority_demotion import (
    audit_priority,
    detector_provenance_state,
    run_t94_analysis,
    weak_measurement_state,
)


class WeakMeasurementPriorityDemotionTests(unittest.TestCase):
    def test_detector_route_currently_dominates(self) -> None:
        detector = detector_provenance_state()
        weak = weak_measurement_state()

        audit = audit_priority(detector, weak)

        self.assertEqual(audit.preferred_route, "detector_provenance")
        self.assertEqual(
            audit.weak_measurement_status,
            "demoted_below_detector_provenance",
        )
        self.assertEqual(audit.detector_status, "active_but_not_empirically_upgraded")

    def test_t94_result_requires_reinstatement_gate(self) -> None:
        result = run_t94_analysis()

        self.assertIn("demote T12 below detector provenance", result.q1_update)
        self.assertIn("independent branch, provenance, or undo-cost axis", result.strongest_claim)
        self.assertIn("real T78-style deployment", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
