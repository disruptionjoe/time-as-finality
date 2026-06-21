"""Tests for T129 future capability preservation audit."""

from __future__ import annotations

import unittest

from models.future_capability_preservation_audit import (
    PriorArtVerdict,
    Recommendation,
    branch_witnesses,
    prior_art_pressure,
    run_t129_analysis,
)


class FutureCapabilityPreservationAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t129_analysis()

    def test_required_branches_are_reviewed(self) -> None:
        self.assertEqual(
            {witness.branch for witness in branch_witnesses()},
            {
                "Git history witness",
                "Detector packet witness",
                "Reconstruction debt",
                "Provenance work",
                "Operation-right discussions",
                "ASP",
                "FOA",
                "LossKernel",
                "Admissibility",
                "Maintenance-cost investigations",
            },
        )

    def test_every_branch_has_fixed_state_future_change_and_hidden_cause(self) -> None:
        for witness in self.result.witnesses:
            self.assertTrue(witness.state_held_fixed)
            self.assertTrue(witness.future_capability_changed)
            self.assertTrue(witness.candidate_cause)
            self.assertTrue(witness.capability_structure.components_present())
            self.assertTrue(witness.uniform_representation)
            self.assertFalse(witness.superficial_state_difference)

    def test_candidate_explanations_are_represented(self) -> None:
        components = set().union(
            *(
                witness.capability_structure.components_present()
                for witness in self.result.witnesses
            )
        )

        self.assertTrue(
            {
                "witness_availability",
                "operation_rights",
                "reconstruction_paths",
                "provenance_structure",
                "maintenance_capacity",
                "access_boundaries",
            }
            <= components
        )

    def test_required_prior_art_pressure_is_present(self) -> None:
        self.assertEqual(
            {item.framework for item in prior_art_pressure()},
            {
                "reachability analysis",
                "viability kernels",
                "opportunity-set economics",
                "capability theory",
                "mechanism design",
                "affordance theory",
                "active inference policy spaces",
                "reinforcement-learning action spaces",
                "provenance systems",
                "access-control systems",
                "distributed-systems capability models",
            },
        )

    def test_absorption_is_assumed_until_separation(self) -> None:
        self.assertTrue(self.result.common_structure_exists)
        self.assertTrue(self.result.reducible_to_existing_frameworks)
        self.assertEqual(self.result.recommendation, Recommendation.FORMALIZE)
        self.assertFalse(
            any(item.verdict == PriorArtVerdict.MISSES_ONLY_IF_COARSE for item in self.result.prior_art)
        )

    def test_strongest_witnesses_and_claim_impact_are_conservative(self) -> None:
        self.assertIn("T123", self.result.strongest_separation_witness)
        self.assertIn("Git", self.result.strongest_absorption_witness)
        self.assertIn("No core claim upgrade", self.result.claim_impact_note)
        self.assertNotEqual(self.result.recommendation, Recommendation.PROMOTE)


if __name__ == "__main__":
    unittest.main()
