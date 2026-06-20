"""Tests for T115 maintenance-cost viability split."""

from __future__ import annotations

import unittest

from models.maintenance_viability_split import Capture, run_t115_analysis


class MaintenanceViabilitySplitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t115_analysis()
        self.by_domain = {audit.domain: audit for audit in self.result.pair_audits}

    def test_required_toy_domains_are_present(self) -> None:
        self.assertEqual(
            set(self.by_domain),
            {
                "record_commons",
                "provenance",
                "version_control",
                "governance",
                "consensus",
            },
        )

    def test_all_pairs_match_standard_metrics(self) -> None:
        for audit in self.result.pair_audits:
            self.assertTrue(audit.standard_equivalent, audit.domain)
            self.assertTrue(audit.maintained_records_equal, audit.domain)
            self.assertEqual(audit.system_a.metrics, audit.system_b.metrics)

    def test_all_pairs_split_future_operation_capability(self) -> None:
        for audit in self.result.pair_audits:
            self.assertTrue(audit.future_operation_split, audit.domain)
            self.assertTrue(audit.a_future_usable)
            self.assertFalse(audit.b_future_usable)
            self.assertTrue(audit.differing_axis)

    def test_version_control_is_both_separation_and_absorption_case(self) -> None:
        audit = self.by_domain["version_control"]

        self.assertIn("merge", audit.system_a.profile.operation_rights)
        self.assertNotIn("merge", audit.system_b.profile.operation_rights)
        self.assertIn("merge_base", audit.system_a.profile.accessible_witnesses)
        self.assertNotIn("merge_base", audit.system_b.profile.accessible_witnesses)
        self.assertIn("Version control", self.result.strongest_separation_case)
        self.assertIn("provenance/version-control", self.result.strongest_absorption_case)

    def test_entropy_control_and_storage_do_not_capture_coarse_split(self) -> None:
        for audit in self.result.pair_audits:
            by_framework = {comparison.framework: comparison for comparison in audit.comparisons}
            self.assertEqual(
                by_framework["entropy production"].capture,
                Capture.DOES_NOT_CAPTURE_COARSE,
            )
            self.assertEqual(
                by_framework["information-theoretic storage"].capture,
                Capture.DOES_NOT_CAPTURE_COARSE,
            )
            self.assertEqual(
                by_framework["control-theoretic state maintenance"].capture,
                Capture.CAPTURES_IF_ENRICHED,
            )

    def test_required_comparison_targets_are_all_present(self) -> None:
        expected = {
            "entropy production",
            "control-theoretic state maintenance",
            "viability kernels",
            "resilience/adaptive-cycle models",
            "free-energy formulations",
            "commons/public-goods models",
            "information-theoretic storage",
            "provenance systems",
            "LossKernel/reconstruction debt",
        }
        for audit in self.result.pair_audits:
            self.assertEqual({comparison.framework for comparison in audit.comparisons}, expected)

    def test_recommendation_is_preserve_and_formalize_not_promote(self) -> None:
        self.assertIn("Preserve and formalize narrowly", self.result.recommendation)
        self.assertIn("Do not promote", self.result.recommendation)
        self.assertIn("No core claim upgrade", self.result.claim_ledger_update)
        self.assertIn("absorbed", self.result.weakened_or_falsified)


if __name__ == "__main__":
    unittest.main()
