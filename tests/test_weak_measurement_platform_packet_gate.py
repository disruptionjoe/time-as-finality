"""Tests for T166: weak-measurement platform-packet gate."""

from __future__ import annotations

import unittest

from models.weak_measurement_platform_packet_gate import (
    canonical_platform_packet_cases,
    classify_platform_packet,
    current_frontier_case,
    run_t166_analysis,
)


class Q1CPlatformPacketGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = dict(canonical_platform_packet_cases())
        self.result = run_t166_analysis()

    def test_extra_environment_packet_can_be_admissible(self) -> None:
        audit = classify_platform_packet(
            self.cases["admissible_extra_environment_packet"],
            name="admissible_extra_environment_packet",
        )

        self.assertEqual(audit.classification, "admissible_external_q1c_packet")
        self.assertTrue(audit.admissible_packet)

    def test_enlarged_instrument_requires_back_projection(self) -> None:
        audit = classify_platform_packet(
            self.cases["enlarged_instrument_missing_back_projection"],
            name="enlarged_instrument_missing_back_projection",
        )

        self.assertEqual(audit.classification, "blocked_missing_back_projection")
        self.assertFalse(audit.admissible_packet)

    def test_same_instrument_packet_is_not_live_architecture(self) -> None:
        audit = classify_platform_packet(
            self.cases["same_instrument_packet"],
            name="same_instrument_packet",
        )

        self.assertEqual(audit.classification, "null_invalid_architecture_class")
        self.assertFalse(audit.admissible_packet)

    def test_event_level_data_is_required(self) -> None:
        audit = classify_platform_packet(
            self.cases["scaffold_only_packet"],
            name="scaffold_only_packet",
        )

        self.assertEqual(audit.classification, "scaffold_only_no_event_level_audit_data")
        self.assertFalse(audit.admissible_packet)

    def test_current_frontier_is_still_inadmissible(self) -> None:
        name, case = current_frontier_case()
        audit = classify_platform_packet(case, name=name)

        self.assertEqual(audit.classification, "blocked_missing_frozen_ordinary_record")
        self.assertFalse(audit.admissible_packet)
        self.assertFalse(self.result.current_frontier_admissible)
        self.assertTrue(self.result.all_null_controls_rejected)
        self.assertIn("two stages", self.result.q1c_update)


if __name__ == "__main__":
    unittest.main()
