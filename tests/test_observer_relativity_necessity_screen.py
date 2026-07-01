"""Tests for T381 observer-relativity necessity screen."""

from __future__ import annotations

import unittest

from models.compatibility_signal_basis_screen import canonical_form
from models.observer_relativity_necessity_screen import (
    evaluate_candidates,
    necessity_candidates,
    primitive_ray_count,
    run_t381_analysis,
)


class ObserverRelativityNecessityScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t381_analysis()
        self.verdicts = {verdict.candidate_id: verdict for verdict in evaluate_candidates()}

    def test_minimal_two_null_adapter_is_unique_survivor(self) -> None:
        self.assertTrue(self.result.minimal_two_null_adapter_unique_survivor)
        self.assertEqual(self.result.surviving_candidate_ids, ("minimal_two_null_channel",))
        verdict = self.verdicts["minimal_two_null_channel"]
        self.assertTrue(verdict.passes_all)
        self.assertEqual(verdict.status, "minimal_survivor")
        self.assertEqual(verdict.forced_form, canonical_form())
        self.assertTrue(all(check.passes for check in verdict.checks))

    def test_one_channel_and_collinear_controls_fail_directionality(self) -> None:
        self.assertTrue(self.result.one_channel_fails)
        self.assertTrue(self.result.collinear_channels_fail)
        self.assertEqual(self.verdicts["single_channel"].status, "insufficient_directionality")
        self.assertEqual(
            self.verdicts["collinear_two_channel"].status,
            "insufficient_directionality",
        )

    def test_overcomplete_three_channel_fails_minimality(self) -> None:
        self.assertTrue(self.result.three_channel_overcomplete_fails_minimality)
        verdict = self.verdicts["overcomplete_three_channel"]
        self.assertFalse(verdict.passes_all)
        self.assertEqual(verdict.status, "overcomplete_not_minimal")
        failed = {check.requirement_id for check in verdict.checks if not check.passes}
        self.assertIn("minimal_two_primitive_rays", failed)
        self.assertIn("nondegenerate_forced_interval", failed)

    def test_asymmetric_unit_adapter_is_redundant_basis_variant(self) -> None:
        self.assertTrue(self.result.asymmetric_unit_adapter_reduces_to_two_null_basis)
        verdict = self.verdicts["asymmetric_unit_two_channel"]
        self.assertFalse(verdict.passes_all)
        self.assertEqual(verdict.status, "isomorphic_to_two_null_basis_but_unit_redundant")
        self.assertEqual(verdict.forced_form, canonical_form())

    def test_signed_diagonal_adapter_rejected_as_non_source_compatible(self) -> None:
        self.assertTrue(self.result.signed_diagonal_adapter_rejected_as_non_source_compatible)
        verdict = self.verdicts["signed_diagonal_two_channel"]
        self.assertFalse(verdict.passes_all)
        self.assertEqual(verdict.status, "rejected_signed_source_direction")
        failed = {check.requirement_id for check in verdict.checks if not check.passes}
        self.assertIn("source_compatible_nonnegative_counts", failed)

    def test_primitive_ray_count_collapses_collinear_labels(self) -> None:
        candidates = {
            candidate.candidate_id: candidate for candidate in necessity_candidates()
        }
        self.assertEqual(primitive_ray_count(candidates["minimal_two_null_channel"].channels), 2)
        self.assertEqual(primitive_ray_count(candidates["collinear_two_channel"].channels), 1)
        self.assertEqual(primitive_ray_count(candidates["overcomplete_three_channel"].channels), 3)

    def test_hostile_comparators_keep_necessity_boundary_honest(self) -> None:
        by_id = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertTrue(by_id["finite_candidate_scope"].absorbs)
        self.assertFalse(by_id["two_null_basis_necessity"].absorbs)
        self.assertTrue(by_id["compatibility_alone_derivation"].absorbs)
        self.assertTrue(by_id["external_adapter_reading"].absorbs)

    def test_overall_verdict_is_conditional_necessity(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "minimal_two_null_adapter_necessary_within_declared_screen",
        )
        self.assertIn("conditional necessity evidence", self.result.claim_ledger_update)
        self.assertIn("not a compatibility-alone derivation", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
