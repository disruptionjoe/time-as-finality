"""Tests for T264-T279 exact n=9 ordinal count tasks."""

from __future__ import annotations

import os
import unittest
from fractions import Fraction

from models.t264_t279_nine_event_ordinal_exact_count import (
    SELECTED_T252_RANK_PERMUTATION,
    _audit_size,
    _deletion_summary,
    _diagnostics_for_permutation,
    run_t264_analysis,
)


class OptimizedOrdinalCounterTests(unittest.TestCase):
    def test_t264_reproduces_published_t223_counts(self) -> None:
        result = run_t264_analysis()

        self.assertEqual(
            result.verdict,
            "optimized_counter_reproduces_t223_n6_to_n8_counts",
        )
        metrics = {metric.name: metric.value for metric in result.metrics}
        self.assertEqual(metrics["n6_t126_t156_stable"], (578, 305, 26))
        self.assertEqual(metrics["n7_t126_t156_stable"], (4456, 2051, 174))
        self.assertEqual(metrics["n8_t126_t156_stable"], (34044, 16261, 361))
        self.assertTrue(metrics["reproduces_t223_counts"])

    def test_selected_t252_diagnostics_match_prior_round(self) -> None:
        diagnostics = _diagnostics_for_permutation(SELECTED_T252_RANK_PERMUTATION)
        deletion_summary = _deletion_summary(SELECTED_T252_RANK_PERMUTATION)

        self.assertEqual(diagnostics.classification, "passes_filter_only")
        self.assertTrue(diagnostics.t126_filter_passed)
        self.assertEqual(diagnostics.strict_pair_count, 20)
        self.assertEqual(diagnostics.cover_relation_count, 8)
        self.assertEqual(diagnostics.height, 5)
        self.assertEqual(diagnostics.width, 2)
        self.assertEqual(diagnostics.rank_profile, (1, 2, 2, 2, 2))
        self.assertEqual(diagnostics.largest_interval_size, 3)
        self.assertEqual(diagnostics.largest_cover_hub_fraction, Fraction(1, 4))
        self.assertEqual(deletion_summary.t253_t126_band_deletion_pass_count, 9)
        self.assertEqual(deletion_summary.t159_thin_deletion_pass_count, 0)
        self.assertEqual(deletion_summary.t252_style_deletion_pass_count, 9)


@unittest.skipUnless(
    os.environ.get("TAF_RUN_T264_N9") == "1",
    "Set TAF_RUN_T264_N9=1 to run the full exact n=9 sweep.",
)
class ExactN9OrdinalCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = _audit_size(9)

    def test_n9_t126_and_t156_counts(self) -> None:
        self.assertEqual(self.audit.total_rank_permutation_cases, 362880)
        self.assertEqual(self.audit.t126_pass_count, 263047)
        self.assertEqual(self.audit.t156_pass_count, 143435)
        self.assertEqual(
            dict(self.audit.t126_classification_counts),
            {
                "hub_nonlocality_obstruction": 7341,
                "interval_profile_obstruction": 2050,
                "order_dimension_obstruction": 90440,
                "passes_filter_only": 263047,
                "rank_width_obstruction": 2,
            },
        )

    def test_n9_thin_and_t252_style_tail_counts(self) -> None:
        self.assertEqual(self.audit.parent_interval_cap1_count, 7813)
        self.assertEqual(self.audit.t159_thin_deletion_stable_count, 1583)
        self.assertEqual(self.audit.parent_interval_cap3_count, 91350)
        self.assertEqual(self.audit.relaxed_interval3_deletion_stable_count, 9176)
        self.assertEqual(self.audit.t252_parent_cap_count, 66)
        self.assertEqual(self.audit.t252_deletion_stable_count, 10)
        self.assertEqual(self.audit.t253_all_deletions_t126_band_stable_count, 8339)

    def test_selected_t252_is_in_global_t252_style_tail(self) -> None:
        assert self.audit.selected_t252_deletion_summary is not None
        self.assertEqual(
            self.audit.selected_t252_deletion_summary.t252_style_deletion_pass_count,
            9,
        )
        self.assertIn(
            SELECTED_T252_RANK_PERMUTATION,
            self.audit.representative_t252_deletion_stable_permutations,
        )


if __name__ == "__main__":
    unittest.main()
