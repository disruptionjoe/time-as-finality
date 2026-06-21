"""Tests for T119 Future Operation Availability residue audit."""

from __future__ import annotations

import unittest

from models.future_operation_availability_residue import (
    FOARelation,
    PriorArtVerdict,
    run_t119_analysis,
)


class FutureOperationAvailabilityResidueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t119_analysis()
        self.examples = {
            example.example_id: example for example in self.result.finite_examples
        }
        self.branches = {audit.branch: audit for audit in self.result.branch_audits}

    def test_required_branches_are_audited(self) -> None:
        self.assertEqual(
            set(self.branches),
            {
                "Q1A",
                "ASP",
                "Reconstruction debt",
                "Maintenance cost",
                "Provenance",
                "LossKernel",
                "Admissibility",
            },
        )

    def test_q1a_is_only_weakly_foa_while_asp_is_directly_foa(self) -> None:
        self.assertEqual(self.branches["Q1A"].involves_foa, FOARelation.WEAK)
        self.assertTrue(self.branches["Q1A"].expressible_without_foa)
        self.assertEqual(self.branches["ASP"].involves_foa, FOARelation.STRONG)
        self.assertFalse(self.branches["ASP"].expressible_without_foa)

    def test_required_prior_art_targets_are_pressured(self) -> None:
        required = {
            "viability kernels",
            "reachability analysis",
            "affordance landscapes",
            "active inference policy spaces",
            "reinforcement-learning action spaces",
            "opportunity-set economics",
            "capability theory",
            "mechanism design",
            "commons governance",
            "control theory",
        }
        by_target = {item.target: item for item in self.result.prior_art_pressure}
        self.assertEqual(set(by_target), required)
        self.assertEqual(by_target["reachability analysis"].verdict, PriorArtVerdict.ABSORBS)
        self.assertEqual(by_target["opportunity-set economics"].verdict, PriorArtVerdict.ABSORBS)
        self.assertEqual(by_target["capability theory"].verdict, PriorArtVerdict.PARTIAL)

    def test_example_a_foa_differs_while_existing_measures_match(self) -> None:
        example = self.examples["A_foa_differs_existing_measures_do_not"]
        self.assertTrue(example.existing_measures_equal)
        self.assertFalse(example.existing_measures_differ)
        self.assertTrue(example.foa_differs)
        self.assertEqual(example.foa_a, frozenset({"build", "merge", "revert", "bisect"}))
        self.assertEqual(example.foa_b, frozenset({"build"}))

    def test_example_b_existing_measures_differ_while_foa_matches(self) -> None:
        example = self.examples["B_existing_measures_differ_foa_does_not"]
        self.assertFalse(example.existing_measures_equal)
        self.assertTrue(example.existing_measures_differ)
        self.assertFalse(example.foa_differs)
        self.assertEqual(example.foa_a, example.foa_b)

    def test_example_c_absorbs_foa_into_enriched_reachability(self) -> None:
        example = self.examples["C_foa_collapses_into_enriched_reachability"]
        self.assertTrue(example.foa_differs)
        self.assertTrue(example.foa_collapses_into_existing_framework)
        self.assertIn("challenge", example.foa_a)
        self.assertNotIn("challenge", example.foa_b)

    def test_chain_is_supported_but_not_promoted(self) -> None:
        self.assertTrue(self.result.chain_supported)
        self.assertIn("Q1A only joins", self.result.chain_verdict)
        self.assertIn("Preserve and formalize narrowly", self.result.recommendation)
        self.assertIn("Do not promote", self.result.recommendation)
        self.assertIn("No core claim upgrade", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
