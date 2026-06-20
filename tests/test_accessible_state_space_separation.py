"""Tests for T117 Accessible State Space separation audit."""

from __future__ import annotations

import unittest

from models.accessible_state_space_separation import Capture, run_t117_analysis


class AccessibleStateSpaceSeparationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t117_analysis()
        self.by_domain = {audit.domain: audit for audit in self.result.audits}

    def test_required_domains_are_present(self) -> None:
        self.assertEqual(
            set(self.by_domain),
            {
                "version_control",
                "provenance",
                "governance",
                "commons",
                "consensus",
                "record_system",
            },
        )

    def test_baseline_metrics_match_for_every_domain(self) -> None:
        for audit in self.result.audits:
            self.assertTrue(audit.entropy_equal, audit.domain)
            self.assertTrue(audit.information_equal, audit.domain)
            self.assertTrue(audit.finality_equal, audit.domain)
            self.assertTrue(audit.viability_equal, audit.domain)
            self.assertTrue(audit.persistence_equal, audit.domain)
            self.assertTrue(audit.coarse_reachability_equal, audit.domain)
            self.assertEqual(audit.system_a.metrics, audit.system_b.metrics)

    def test_asp_splits_when_baseline_metrics_match(self) -> None:
        for audit in self.result.audits:
            self.assertTrue(audit.asp_split, audit.domain)
            self.assertGreater(len(audit.asp_a), len(audit.asp_b))
            self.assertTrue(audit.lost_structure_chain_present)

    def test_version_control_is_strongest_separation(self) -> None:
        audit = self.by_domain["version_control"]

        self.assertEqual(audit.asp_a, frozenset({"build", "merge", "revert", "bisect"}))
        self.assertEqual(audit.asp_b, frozenset({"build"}))
        self.assertIn("Version control", self.result.strongest_separation_case)
        self.assertIn("same endpoint repository state", self.result.strongest_separation_case)

    def test_reachability_and_opportunity_sets_absorb_asp_when_enriched(self) -> None:
        for audit in self.result.audits:
            by_target = {item.target: item for item in audit.prior_art}
            self.assertEqual(
                by_target["reachable-state analysis"].capture,
                Capture.CAPTURES_IF_ENRICHED,
            )
            self.assertEqual(
                by_target["opportunity-set economics"].capture,
                Capture.CAPTURES_DIRECTLY,
            )
            self.assertEqual(
                by_target["mechanism design"].capture,
                Capture.CAPTURES_IF_ENRICHED,
            )

    def test_required_prior_art_targets_are_compared(self) -> None:
        required = {
            "viability kernels",
            "reachable-state analysis",
            "control-theoretic controllability",
            "active inference",
            "free-energy approaches",
            "opportunity-set economics",
            "ecological resilience",
            "adaptive-cycle models",
            "commons governance",
            "niche construction",
            "mechanism design",
        }
        for audit in self.result.audits:
            self.assertEqual({item.target for item in audit.prior_art}, required)

    def test_disposition_preserves_but_does_not_promote(self) -> None:
        self.assertIn("Preserve and formalize", self.result.recommended_disposition)
        self.assertIn("Do not promote", self.result.recommended_disposition)
        self.assertIn("mostly absorbed", self.result.falsification_result)
        self.assertIn("No core claim upgrade", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
