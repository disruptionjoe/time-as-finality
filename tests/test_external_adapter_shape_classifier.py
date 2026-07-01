"""Tests for T382 external adapter shape classifier."""

from __future__ import annotations

import unittest

from models.external_adapter_shape_classifier import evaluate_adapters, run_t382_analysis


class ExternalAdapterShapeClassifierTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t382_analysis()
        self.verdicts = {verdict.adapter_id: verdict for verdict in evaluate_adapters()}

    def test_two_null_channel_adapter_is_uniquely_clean(self) -> None:
        self.assertTrue(self.result.two_null_adapter_uniquely_clean)
        self.assertEqual(self.result.uniquely_clean_adapter, "two_null_channel")
        verdict = self.verdicts["two_null_channel"]
        self.assertTrue(verdict.passes)
        self.assertEqual(verdict.status, "uniquely_clean")
        self.assertTrue(all(criterion.passes for criterion in verdict.criteria))

    def test_absolute_clock_is_rejected_for_global_time_import(self) -> None:
        self.assertTrue(self.result.absolute_clock_rejected)
        verdict = self.verdicts["absolute_clock"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "rejected_global_clock")
        failed = {criterion.criterion_id for criterion in verdict.criteria if not criterion.passes}
        self.assertIn("no_global_time_import", failed)

    def test_scalar_source_action_has_no_signal_geometry(self) -> None:
        self.assertTrue(self.result.scalar_source_action_rejected)
        verdict = self.verdicts["scalar_source_action"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "rejected_no_signal_geometry")
        failed = {criterion.criterion_id for criterion in verdict.criteria if not criterion.passes}
        self.assertIn("two_independent_null_directions", failed)

    def test_one_channel_is_undercomplete(self) -> None:
        self.assertTrue(self.result.one_channel_rejected)
        verdict = self.verdicts["one_signal_channel"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "rejected_undercomplete")

    def test_overcomplete_adapter_is_demoted(self) -> None:
        self.assertTrue(self.result.overcomplete_adapter_demoted)
        verdict = self.verdicts["overcomplete_multi_channel"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "demoted_overcomplete")
        failed = {criterion.criterion_id for criterion in verdict.criteria if not criterion.passes}
        self.assertIn("two_independent_null_directions", failed)
        self.assertIn("minimal_not_overcomplete", failed)

    def test_gauge_like_adapter_is_partial_without_observer_calibration(self) -> None:
        self.assertTrue(self.result.gauge_like_adapter_partial)
        verdict = self.verdicts["gauge_like_local_adapter"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "partial_gauge_relabel_only")
        failed = {criterion.criterion_id for criterion in verdict.criteria if not criterion.passes}
        self.assertIn("reciprocal_scaling_support", failed)

    def test_hostile_comparators_keep_catalog_boundary_honest(self) -> None:
        by_id = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertFalse(by_id["adapter_uniqueness"].absorbs)
        self.assertTrue(by_id["shape_catalog_completeness"].absorbs)
        self.assertTrue(by_id["external_origin"].absorbs)
        self.assertFalse(by_id["global_clock_shortcut"].absorbs)

    def test_overall_verdict_is_adapter_shape_evidence(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "two_null_channel_adapter_uniquely_clean_within_catalog",
        )
        self.assertIn("cleanest external interface candidate", self.result.claim_ledger_update)
        self.assertIn("Among the declared external-adapter shapes", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
