"""Tests for T223: decisive ordinal-scaling verdict for the T54 colimit tail.

The decisive n=8 enumeration (40320 cases through the full jackknife pipeline)
takes several minutes, so the default test path verifies:

  * the cheap sizes n=5,6,7 reproduce the exact T165/T167 counts (regression
    guard that the decisive model reuses the same screens), and
  * the verdict rubric helpers behave correctly on synthetic trajectories
    (so the advance/no-go decision logic is checked without the slow run).

Set TAF_RUN_T223_N8=1 to additionally run the full n=8 decisive analysis and
assert the issued verdict.
"""

from __future__ import annotations

import os
import unittest
from fractions import Fraction

from models.t54_ordinal_scaling_decisive import (
    DecisiveSizeAudit,
    _audit_size,
    _heights_do_not_grow,
    _monotone_nonincreasing_from,
    run_t223_analysis,
)


class DecisiveSizeReproductionTests(unittest.TestCase):
    """The decisive model must reproduce the established T165/T167 counts."""

    def test_n5_scale_blocked(self) -> None:
        n5 = _audit_size(5)
        self.assertEqual(n5.total_rank_permutation_cases, 120)
        self.assertEqual(n5.t126_pass_count, 0)
        self.assertEqual(n5.stable_labeled_survivor_count, 0)

    def test_n6_reproduces_t165(self) -> None:
        n6 = _audit_size(6)
        self.assertEqual(n6.total_rank_permutation_cases, 720)
        self.assertEqual(n6.t126_pass_count, 578)
        self.assertEqual(n6.t156_pass_count, 305)
        self.assertEqual(n6.parent_interval_pass_count, 156)
        self.assertEqual(n6.stable_labeled_survivor_count, 26)
        self.assertEqual(n6.stable_labeled_survivor_fraction, Fraction(13, 360))
        self.assertEqual(n6.oriented_survivor_class_count, 15)
        self.assertEqual(n6.order_dual_survivor_class_count, 9)
        self.assertEqual(n6.max_survivor_height, 3)
        self.assertTrue(n6.all_survivors_thin_intervals)

    def test_n7_reproduces_t167(self) -> None:
        n7 = _audit_size(7)
        self.assertEqual(n7.total_rank_permutation_cases, 5040)
        self.assertEqual(n7.t126_pass_count, 4456)
        self.assertEqual(n7.t156_pass_count, 2051)
        self.assertEqual(n7.parent_interval_pass_count, 561)
        self.assertEqual(n7.stable_labeled_survivor_count, 174)
        self.assertEqual(n7.stable_labeled_survivor_fraction, Fraction(29, 840))
        self.assertEqual(n7.oriented_survivor_class_count, 86)
        self.assertEqual(n7.order_dual_survivor_class_count, 45)
        self.assertEqual(n7.largest_oriented_class_probability, Fraction(1, 1260))
        self.assertEqual(n7.max_survivor_height, 3)
        self.assertTrue(n7.all_survivors_thin_intervals)

    def test_stable_fraction_decays_from_n6_to_n7(self) -> None:
        n6 = _audit_size(6)
        n7 = _audit_size(7)
        self.assertLess(
            n7.stable_labeled_survivor_fraction,
            n6.stable_labeled_survivor_fraction,
        )


class VerdictRubricHelperTests(unittest.TestCase):
    """The advance/no-go rubric must be correct on synthetic trajectories."""

    def test_monotone_nonincreasing_detects_decay(self) -> None:
        decaying = (
            (5, Fraction(0)),
            (6, Fraction(13, 360)),
            (7, Fraction(29, 840)),
            (8, Fraction(1, 40)),
        )
        self.assertTrue(_monotone_nonincreasing_from(decaying, start=6))

    def test_monotone_nonincreasing_detects_growth(self) -> None:
        growing = (
            (6, Fraction(13, 360)),
            (7, Fraction(29, 840)),
            (8, Fraction(1, 10)),  # grows -> not non-increasing
        )
        self.assertFalse(_monotone_nonincreasing_from(growing, start=6))

    def test_heights_do_not_grow_true_when_bounded(self) -> None:
        audits = [
            _stub_size_audit(event_count=6, max_survivor_height=3),
            _stub_size_audit(event_count=7, max_survivor_height=3),
            _stub_size_audit(event_count=8, max_survivor_height=3),
        ]
        self.assertTrue(_heights_do_not_grow(audits))

    def test_heights_do_not_grow_false_when_taller(self) -> None:
        audits = [
            _stub_size_audit(event_count=7, max_survivor_height=3),
            _stub_size_audit(event_count=8, max_survivor_height=5),
        ]
        self.assertFalse(_heights_do_not_grow(audits))


@unittest.skipUnless(
    os.environ.get("TAF_RUN_T223_N8") == "1",
    "Set TAF_RUN_T223_N8=1 to run the multi-minute n=8 decisive enumeration.",
)
class DecisiveVerdictTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t223_analysis()
        cls.by_size = {a.event_count: a for a in cls.result.size_audits}

    def test_reproduces_prior_counts(self) -> None:
        self.assertTrue(self.result.reproduced_prior_counts)

    def test_n8_decisive_counts(self) -> None:
        n8 = self.by_size[8]
        self.assertEqual(n8.total_rank_permutation_cases, 40320)
        self.assertEqual(n8.t126_pass_count, 34044)
        self.assertEqual(n8.t156_pass_count, 16261)
        self.assertEqual(n8.parent_interval_pass_count, 2057)
        self.assertEqual(n8.stable_labeled_survivor_count, 361)
        self.assertEqual(n8.stable_labeled_survivor_fraction, Fraction(361, 40320))
        self.assertEqual(n8.oriented_survivor_class_count, 174)
        self.assertEqual(n8.order_dual_survivor_class_count, 90)
        self.assertEqual(n8.largest_oriented_class_probability, Fraction(1, 10080))
        self.assertEqual(n8.max_survivor_height, 3)
        self.assertTrue(n8.all_survivors_thin_intervals)

    def test_stable_fraction_strictly_decays_to_n8(self) -> None:
        n6 = self.by_size[6]
        n7 = self.by_size[7]
        n8 = self.by_size[8]
        self.assertGreater(
            n6.stable_labeled_survivor_fraction,
            n7.stable_labeled_survivor_fraction,
        )
        self.assertGreater(
            n7.stable_labeled_survivor_fraction,
            n8.stable_labeled_survivor_fraction,
        )

    def test_issues_finite_no_go_verdict(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "finite_no_go_manifoldlikeness_unreachable_without_added_assumption",
        )
        self.assertTrue(
            self.result.stable_fraction_is_monotone_nonincreasing_from_n6
        )
        self.assertTrue(self.result.survivor_family_stays_thin_height_bounded)
        self.assertTrue(self.result.typical_member_rejected)

    def test_language_guardrails(self) -> None:
        self.assertIn("NOT earned", self.result.not_earned)
        self.assertIn("no spacetime", self.result.not_earned.lower())
        self.assertIn("requires_added_assumption", self.result.s1_update)
        self.assertIn(
            "establishes no continuum limit", self.result.not_claimed
        )


def _stub_size_audit(*, event_count: int, max_survivor_height: int) -> DecisiveSizeAudit:
    return DecisiveSizeAudit(
        event_count=event_count,
        total_rank_permutation_cases=1,
        t126_pass_count=0,
        t156_pass_count=0,
        parent_interval_pass_count=0,
        stable_labeled_survivor_count=0,
        stable_labeled_survivor_fraction=Fraction(0),
        stable_conditional_after_parent_fraction=Fraction(0),
        oriented_survivor_class_count=0,
        order_dual_survivor_class_count=0,
        largest_oriented_class_size=0,
        largest_oriented_class_probability=Fraction(0),
        survivor_height_distribution=(),
        max_survivor_height=max_survivor_height,
        survivor_max_parent_interval_distribution=(),
        all_survivors_thin_intervals=True,
        all_survivors_height_bounded=True,
        modal_t126_classification="passes_filter_only",
        modal_t126_classification_fraction=Fraction(1),
    )


if __name__ == "__main__":
    unittest.main()
