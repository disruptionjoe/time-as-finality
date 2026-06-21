"""Tests for T114 finite viability-filter artifact."""

from __future__ import annotations

import unittest

from models.viability_filter import (
    evaluate_candidate,
    run_t114_analysis,
)


class ViabilityFilterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t114_analysis()
        self.by_name = {
            evaluation.candidate.name: evaluation for evaluation in self.result.evaluations
        }

    def test_geometry_is_not_sufficient_for_experienced_world_membership(self) -> None:
        self.assertTrue(self.result.geometry_not_sufficient)
        candidate = self.by_name["geometric_but_unmaintained_seed"]

        self.assertTrue(candidate.gate_passed("geometry"))
        self.assertTrue(candidate.gate_passed("dynamics"))
        self.assertFalse(candidate.gate_passed("maintenance"))
        self.assertFalse(candidate.observer_experienced)
        self.assertEqual(candidate.first_failed_gate, "maintenance")

    def test_maintenance_is_not_sufficient_without_record_finality(self) -> None:
        self.assertTrue(self.result.maintenance_not_sufficient)
        candidate = self.by_name["maintained_but_unfinalized_wave"]

        self.assertTrue(candidate.gate_passed("maintenance"))
        self.assertFalse(candidate.gate_passed("finality"))
        self.assertFalse(candidate.observer_experienced)
        self.assertIn("accessible records", candidate.gates[3].reason)

    def test_finality_does_not_automatically_make_emergence_platform(self) -> None:
        self.assertTrue(self.result.finality_not_platform)
        candidate = self.by_name["finalized_archive_not_platform"]

        self.assertTrue(candidate.observer_experienced)
        self.assertFalse(candidate.emergence_platform)
        self.assertEqual(candidate.first_failed_gate, "emergence_platform")

    def test_matched_standard_state_pair_is_separated_by_record_access(self) -> None:
        visible = self.by_name["visible_protocol_platform"]
        hidden = self.by_name["hidden_protocol_twin"]

        self.assertEqual(
            visible.candidate.geometry_consistent,
            hidden.candidate.geometry_consistent,
        )
        self.assertEqual(visible.candidate.repair_capacity, hidden.candidate.repair_capacity)
        self.assertEqual(
            visible.candidate.entropy_sink_capacity,
            hidden.candidate.entropy_sink_capacity,
        )
        self.assertEqual(
            visible.candidate.platform_operations,
            hidden.candidate.platform_operations,
        )
        self.assertNotEqual(
            visible.candidate.accessible_records,
            hidden.candidate.accessible_records,
        )
        self.assertTrue(visible.observer_experienced)
        self.assertFalse(hidden.observer_experienced)
        self.assertTrue(self.result.finality_separates_fixed_standard_state)

    def test_impossible_geometry_stops_before_viability_language(self) -> None:
        candidate = self.by_name["impossible_tiling"]

        self.assertFalse(candidate.gate_passed("geometry"))
        self.assertEqual(candidate.first_failed_gate, "geometry")
        self.assertFalse(candidate.observer_experienced)
        self.assertFalse(candidate.emergence_platform)

    def test_result_preserves_no_upgrade_boundary(self) -> None:
        self.assertEqual(self.result.platform_positive_cases, ("visible_protocol_platform",))
        self.assertIn("No core claim is upgraded", self.result.claim_ledger_update)
        self.assertIn("only bookkeeping", self.result.weakened)
        self.assertIn("real domain instantiation", self.result.open_blocker)

    def test_evaluate_candidate_is_pure_for_canonical_cases(self) -> None:
        for evaluation in self.result.evaluations:
            self.assertEqual(evaluate_candidate(evaluation.candidate), evaluation)


if __name__ == "__main__":
    unittest.main()
