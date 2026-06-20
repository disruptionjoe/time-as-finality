"""Tests for T102: Q1A neighbor comparison gate."""

from __future__ import annotations

import unittest

from models.q1a_neighbor_comparison import run_t102_analysis


class Q1ANeighborComparisonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t102_analysis()
        self.by_neighbor = {
            audit.neighbor_id: audit for audit in self.result.neighbors
        }

    def test_all_required_neighbors_are_present(self) -> None:
        self.assertEqual(
            set(self.by_neighbor),
            {
                "decoherence",
                "quantum_darwinism",
                "consistent_histories",
                "relational_quantum_mechanics",
                "qbism",
                "many_worlds",
            },
        )

    def test_no_neighbor_comparison_currently_earns_paper_facing_distinction(self) -> None:
        self.assertTrue(
            self.result.no_neighbor_comparison_yet_earns_paper_facing_distinction
        )
        for audit in self.result.neighbors:
            self.assertFalse(audit.earns_paper_facing_distinction_now)

    def test_only_decoherence_and_darwinism_have_partial_current_delta(self) -> None:
        partial_neighbors = {
            audit.neighbor_id
            for audit in self.result.neighbors
            if audit.current_verdict == "narrow_partial_delta"
        }
        self.assertEqual(partial_neighbors, {"decoherence", "quantum_darwinism"})

    def test_fixed_data_gate_requires_standard_quantum_side_data_to_stay_fixed(self) -> None:
        gate = self.result.fixed_data_distinction_gate

        self.assertIn("decoherence/pointer-basis evidence", gate)
        self.assertIn("fragment-information summaries", gate)
        self.assertIn("branch/history availability", gate)
        self.assertIn("access-boundary or independence structure", gate)

    def test_strongest_claim_names_q1a_as_accounting_not_interpretation(self) -> None:
        strongest = self.result.strongest_claim

        self.assertIn("access-boundary and independence accounting", strongest)
        self.assertIn("does not yet earn a paper-facing distinction", strongest)
        self.assertIn("fixed-data witness", strongest)

    def test_recommended_next_move_builds_independence_or_access_cut_witness(self) -> None:
        recommended = self.result.recommended_next

        self.assertIn("independence partition", recommended)
        self.assertIn("access cut", recommended)
        self.assertIn("D1 verdict", recommended)


if __name__ == "__main__":
    unittest.main()
