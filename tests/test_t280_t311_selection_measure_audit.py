"""Tests for T280-T311 finite selection-measure audit."""

from __future__ import annotations

import os
import unittest
from fractions import Fraction

from models.t264_t279_nine_event_ordinal_exact_count import (
    SELECTED_T252_RANK_PERMUTATION,
)
from models.t280_t311_selection_measure_audit import (
    _case_flags,
    _selection_audit,
    run_t280_t311_analyses,
)


class SelectionMeasureFastTests(unittest.TestCase):
    def test_selected_t252_is_target_tail_case(self) -> None:
        flags, deletion_summary = _case_flags(SELECTED_T252_RANK_PERMUTATION)

        self.assertTrue(flags.t126_band_passed)
        self.assertTrue(flags.interval3_parent)
        self.assertTrue(flags.low_cover_parent)
        self.assertTrue(flags.t253_deletion_band_stable)
        self.assertTrue(flags.relaxed_interval3_deletion_stable)
        self.assertTrue(flags.t252_parent_cap)
        self.assertTrue(flags.t252_style_deletion_stable)
        assert deletion_summary is not None
        self.assertEqual(deletion_summary.t252_style_deletion_pass_count, 9)


@unittest.skipUnless(
    os.environ.get("TAF_RUN_T280_N9") == "1",
    "Set TAF_RUN_T280_N9=1 to run the full exact n=9 selection audit.",
)
class FullSelectionMeasureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = _selection_audit()
        cls.features = dict(cls.audit.feature_counts)
        cls.intersections = dict(cls.audit.intersection_counts)
        cls.measures = {summary.name: summary for summary in cls.audit.measure_summaries}

    def test_reproduces_t279_selection_counts(self) -> None:
        self.assertEqual(self.audit.total_cases, 362880)
        self.assertEqual(self.features["t126_band"], 143435)
        self.assertEqual(self.features["t253_deletion_band_stable"], 8339)
        self.assertEqual(self.features["interval3_parent"], 91350)
        self.assertEqual(self.features["low_cover_parent"], 185)
        self.assertEqual(self.features["t252_parent_cap"], 66)
        self.assertEqual(self.features["t252_style_tail"], 10)

    def test_intersection_ablation_counts(self) -> None:
        self.assertEqual(self.intersections["interval3_and_lowcover"], 66)
        self.assertEqual(self.intersections["interval3_and_t253"], 7901)
        self.assertEqual(self.intersections["lowcover_and_t253"], 16)
        self.assertEqual(self.intersections["interval3_lowcover_t253"], 10)

    def test_measure_probabilities(self) -> None:
        self.assertEqual(self.measures["uniform"].tail_probability, Fraction(1, 36288))
        self.assertEqual(self.measures["lowcover"].tail_probability, Fraction(2, 37))
        self.assertEqual(self.measures["parentcap"].tail_probability, Fraction(5, 33))
        self.assertEqual(self.measures["tail"].tail_probability, Fraction(1, 1))
        self.assertTrue(self.measures["tail"].tautological)
        self.assertFalse(self.measures["parentcap"].tautological)

    def test_tail_symmetry_and_task_count(self) -> None:
        self.assertEqual(
            dict(self.audit.tail_symmetry_counts),
            {
                "reverse": 0,
                "complement": 0,
                "reverse_complement": 10,
                "inverse": 10,
            },
        )
        tasks = run_t280_t311_analyses()
        self.assertEqual(len(tasks), 32)
        self.assertEqual(tasks[0].task_id, "T280")
        self.assertEqual(tasks[-1].task_id, "T311")


if __name__ == "__main__":
    unittest.main()
