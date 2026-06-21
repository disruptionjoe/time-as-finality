"""Tests for T154: direct T54/T58-to-T126 bridge."""

from __future__ import annotations

import unittest

from models.t54_t58_t126_bridge import run_t154_analysis


class T54T58T126BridgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t154_analysis()
        self.by_source = {
            audit.source_completion: audit for audit in self.result.audits
        }

    def test_actual_t54_canonical_completions_are_audited(self) -> None:
        self.assertTrue(self.result.canonical_completions_audited)
        self.assertIn("T51_phantom_repair", self.by_source)
        self.assertIn("T52_symmetric_reconstruction", self.by_source)

    def test_t58_gate_passes_before_phantom_gap_resolution(self) -> None:
        self.assertTrue(self.result.t58_gate_required)
        self.assertTrue(self.by_source["T51_phantom_repair"].t58_gap_gate_passed)
        self.assertTrue(
            self.by_source["T52_symmetric_reconstruction"].t58_gap_gate_passed
        )

    def test_canonical_colimits_reach_only_the_causet_gate(self) -> None:
        for name in ("T51_phantom_repair", "T52_symmetric_reconstruction"):
            with self.subTest(name=name):
                audit = self.by_source[name]
                self.assertTrue(audit.t54_theorem_applies)
                self.assertTrue(audit.causal_set_candidate)
                self.assertEqual(audit.t126_classification, "insufficient_scale")
                self.assertFalse(audit.manifold_filter_passed)
                self.assertEqual(audit.verdict, "causet_candidate_only")

    def test_t53_boundary_is_not_embeddability_evidence(self) -> None:
        audit = self.by_source["T53_ambiguous_identity"]

        self.assertFalse(audit.t54_theorem_applies)
        self.assertFalse(audit.causal_set_candidate)
        self.assertEqual(audit.t126_classification, "not_descent_datum")
        self.assertEqual(audit.verdict, "blocked_before_spacetime_claim")

    def test_named_dimension_estimator_is_not_applied_below_scale(self) -> None:
        self.assertTrue(self.result.no_named_dimension_estimator_applied)
        for name in ("T51_phantom_repair", "T52_symmetric_reconstruction"):
            self.assertEqual(
                self.by_source[name].dimension_diagnostic,
                "myrheim_meyer_ordering_fraction_not_applied_below_minimum_scale",
            )

    def test_claim_language_is_weakening_not_upgrade(self) -> None:
        self.assertTrue(
            self.result.all_actual_canonical_colimits_blocked_before_manifold_claims
        )
        self.assertIn("not current spacetime-reconstruction", self.result.weakened)
        self.assertIn("insufficient_scale", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
