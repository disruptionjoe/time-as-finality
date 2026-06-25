"""Tests for T220: LossKernel witness-obligation factorization certificate."""

from __future__ import annotations

import unittest

from models.losskernel_obligation_factorization import (
    canonical_cases,
    derived_obligation,
    hidden_source_escape_pair,
    neighbor_derived_obligation,
    neighbor_signature,
    probe_pair,
    run_t220_analysis,
)


class LossKernelObligationFactorizationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t220_analysis()
        self.cases = {case.name: case for case in canonical_cases()}
        self.probes = {probe.pair_id: probe for probe in self.result.pair_probes}

    def test_canonical_factorization_holds(self) -> None:
        # Every fiber of nu has a constant obligation and verdict: this is the
        # exhaustive finite proof that obligation factors through nu.
        self.assertTrue(self.result.canonical_factorization_holds)
        for report in self.result.fiber_reports:
            self.assertTrue(report.obligations_agree)
            self.assertTrue(report.verdicts_agree)

    def test_neighbor_can_reconstruct_obligation_from_signature(self) -> None:
        # The neighbor, handed only nu(case), recomputes the obligation exactly.
        self.assertTrue(self.result.neighbor_reconstruction_matches)
        for case in canonical_cases():
            self.assertEqual(
                neighbor_derived_obligation(case), derived_obligation(case)
            )

    def test_relabel_pair_collapses_under_same_neighbor_data(self) -> None:
        # mixed_a and mixed_b_relabelled differ only in free label and path tag.
        left = self.cases["mixed_a"]
        right = self.cases["mixed_b_relabelled"]
        self.assertEqual(neighbor_signature(left), neighbor_signature(right))
        self.assertEqual(derived_obligation(left), derived_obligation(right))
        probe = probe_pair("relabel", left, right)
        self.assertTrue(probe.same_neighbor_data)
        self.assertFalse(probe.obligation_diverges)
        self.assertEqual(probe.classification, "collapse")

    def test_no_impossible_separation_witness_in_canonical_regime(self) -> None:
        self.assertTrue(
            self.result.same_neighbor_separation_impossible_in_canonical_regime
        )
        self.assertFalse(self.result.strict_separation_found)
        for probe in self.result.pair_probes:
            self.assertNotEqual(probe.classification, "impossible_separation_witness")

    def test_hidden_source_escape_separates_only_by_non_factoring(self) -> None:
        # The lone loophole: same neighbor data, diverging obligation, but only
        # because a hidden source datum (outside nu) is read.
        left, right = hidden_source_escape_pair()
        self.assertEqual(neighbor_signature(left), neighbor_signature(right))
        self.assertNotEqual(derived_obligation(left), derived_obligation(right))
        probe = self.probes["hidden_source_escape"]
        self.assertTrue(probe.same_neighbor_data)
        self.assertTrue(probe.obligation_diverges)
        self.assertFalse(probe.obligation_factors_through_neighbor)
        self.assertEqual(probe.classification, "non_factoring_escape")

    def test_hidden_escape_is_not_prior_art_separation(self) -> None:
        # Separating + factoring would be a prior-art separation. It never both
        # separates same-neighbor cases AND factors through nu.
        self.assertTrue(self.result.hidden_escape_separates)
        self.assertFalse(self.result.hidden_escape_factors_through_neighbor)
        self.assertFalse(self.result.hidden_escape_is_prior_art_separation)

    def test_verdict_is_narrowed(self) -> None:
        self.assertEqual(self.result.verdict, "narrowed")
        self.assertIn("factors through", self.result.strongest_claim)
        self.assertIn("normal form", self.result.tf1_update)
        self.assertIn("open_formal_target", self.result.tf1_update)


if __name__ == "__main__":
    unittest.main()
