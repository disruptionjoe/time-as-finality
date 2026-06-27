"""Tests for T312-T375 finite measure stress tests."""

from __future__ import annotations

import os
import unittest
from fractions import Fraction

from models.t264_t279_nine_event_ordinal_exact_count import (
    SELECTED_T252_RANK_PERMUTATION,
)
from models.t312_t375_principled_measure_stress import (
    _case_flags,
    _measure_stress_audit,
    run_t312_t375_analyses,
)


class MeasureStressFastTests(unittest.TestCase):
    def test_selected_t252_has_full_tail_flags(self) -> None:
        flags, deletion_summary = _case_flags(SELECTED_T252_RANK_PERMUTATION)

        self.assertTrue(flags.band)
        self.assertTrue(flags.interval3)
        self.assertTrue(flags.lowcover)
        self.assertTrue(flags.parentcap)
        self.assertTrue(flags.t253_stable)
        self.assertTrue(flags.relaxed_interval3_stable)
        self.assertTrue(flags.tail)
        self.assertEqual(deletion_summary.t252_style_deletion_pass_count, 9)


@unittest.skipUnless(
    os.environ.get("TAF_RUN_T312_N9") == "1",
    "Set TAF_RUN_T312_N9=1 to run the full exact n=9 measure stress audit.",
)
class FullMeasureStressTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = _measure_stress_audit()
        cls.features = dict(cls.audit.feature_counts)
        cls.intersections = dict(cls.audit.intersection_counts)
        cls.measures = {summary.name: summary for summary in cls.audit.measure_summaries}

    def test_reproduces_feature_and_intersection_counts(self) -> None:
        self.assertEqual(self.audit.total_cases, 362880)
        self.assertEqual(self.features["band"], 143435)
        self.assertEqual(self.features["lowcover"], 185)
        self.assertEqual(self.features["parentcap"], 66)
        self.assertEqual(self.features["tail"], 10)
        self.assertEqual(self.intersections["cover_deletion"], 16)
        self.assertEqual(self.intersections["interval_cover_deletion"], 10)

    def test_strong_candidate_probabilities(self) -> None:
        self.assertEqual(
            self.measures["hard_cover_deletion"].tail_probability,
            Fraction(5, 8),
        )
        self.assertEqual(
            self.measures["hard_parentcap"].tail_probability,
            Fraction(5, 33),
        )
        self.assertEqual(
            self.measures["soft_s_count_squared"].tail_probability,
            Fraction(2621440, 4627863),
        )
        self.assertEqual(
            self.measures["soft_s_count_cubed"].tail_probability,
            Fraction(1342177280, 1705336003),
        )
        self.assertFalse(self.measures["hard_cover_deletion"].uses_tail_label)
        self.assertFalse(self.measures["soft_s_count_cubed"].uses_tail_label)

    def test_task_count_and_synthesis(self) -> None:
        tasks = run_t312_t375_analyses()

        self.assertEqual(len(tasks), 64)
        self.assertEqual(tasks[0].task_id, "T312")
        self.assertEqual(tasks[-1].task_id, "T375")
        self.assertEqual(
            tasks[-1].verdict,
            "finite_candidate_measures_concentrate_tail_but_remain_underived",
        )


if __name__ == "__main__":
    unittest.main()
