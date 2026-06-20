"""Tests for T120 ASP typed subpresheaf and absorption audit."""

from __future__ import annotations

import unittest

from models.asp_typed_subpresheaf_absorption import (
    Capture,
    run_t120_analysis,
)


class ASPTypedSubpresheafAbsorptionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t120_analysis()

    def test_positive_system_is_typed_subpresheaf(self) -> None:
        self.assertTrue(self.result.positive_restriction.closure_holds)
        self.assertEqual(self.result.positive_restriction.violations, ())
        self.assertEqual(
            self.result.positive_restriction.asp_by_patch["V"],
            frozenset({"build_global", "merge_global"}),
        )
        self.assertEqual(
            self.result.positive_restriction.asp_by_patch["U"],
            frozenset({"build_local", "merge_local"}),
        )

    def test_negative_control_breaks_restriction_closure(self) -> None:
        self.assertFalse(self.result.negative_restriction.closure_holds)
        self.assertTrue(self.result.negative_restriction.violations)
        self.assertIn(
            "merge_global|U=merge_local not in ASP(U)",
            self.result.negative_restriction.violations,
        )

    def test_relabeling_is_invariant(self) -> None:
        self.assertTrue(self.result.relabeling.invariant)
        self.assertEqual(
            self.result.relabeling.original_signature,
            self.result.relabeling.relabeled_signature,
        )

    def test_boundary_changes_are_covariant_not_gauge(self) -> None:
        self.assertFalse(self.result.boundary.invariant_under_boundary_change)
        self.assertTrue(self.result.boundary.covariant_change_detected)
        self.assertEqual(self.result.boundary.coarse_asp, frozenset({"build"}))
        self.assertEqual(
            self.result.boundary.refined_asp,
            frozenset({"build", "merge", "revert", "bisect"}),
        )

    def test_absorption_rerun_matches_expected_verdict(self) -> None:
        absorption = self.result.absorption

        self.assertTrue(absorption.coarse_metrics_match)
        self.assertFalse(absorption.coarse_reachability_separates)
        self.assertTrue(absorption.asp_separates)
        self.assertTrue(absorption.enriched_reachability_absorbs)
        self.assertTrue(absorption.opportunity_set_absorbs)
        self.assertEqual(absorption.low_asp_tasks, frozenset({"build"}))
        self.assertEqual(
            absorption.high_asp_tasks,
            frozenset({"build", "merge", "revert", "bisect"}),
        )

    def test_required_prior_art_targets_are_compared(self) -> None:
        required = {
            "reachability analysis",
            "viability kernels",
            "active inference policy spaces",
            "reinforcement-learning action/state spaces",
            "affordance landscapes",
            "opportunity sets",
            "information-theoretic distinguishability",
            "finality/reconstruction debt",
            "sheaf/section compatibility",
            "GU source-shadow projection",
        }
        self.assertEqual(set(self.result.absorption.prior_art), required)
        self.assertEqual(
            self.result.absorption.prior_art["opportunity sets"],
            Capture.CAPTURES_DIRECTLY,
        )
        self.assertEqual(
            self.result.absorption.prior_art["reachability analysis"],
            Capture.CAPTURES_IF_ENRICHED,
        )

    def test_recommendation_preserves_but_does_not_promote(self) -> None:
        self.assertIn("Preserve and formalize", self.result.recommendation)
        self.assertIn("Do not promote", self.result.recommendation)
        self.assertIn("absorbed by enriched", self.result.verdict)
        self.assertEqual(self.result.claim_impact, "No core claim upgrade.")


if __name__ == "__main__":
    unittest.main()
