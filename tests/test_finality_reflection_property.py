"""Tests for T57: Finality Reflection Property."""

from __future__ import annotations

import unittest

from models.finality_reflection_property import (
    build_branching_dependency_lattice_cover,
    build_generic_complement_counterexample,
    build_hidden_intermediary_lattice_cover,
    check_finality_reflection,
    check_gap_restriction_closure,
    gap_pairs,
    run_t57_analysis,
)
from models.sheaf_cohomology_apparent_finality import (
    compute_global_order,
)


class FinalityReflectionTests(unittest.TestCase):
    def test_hidden_intermediary_lattice_has_nested_patch_pairs(self) -> None:
        cover = build_hidden_intermediary_lattice_cover()
        check = check_finality_reflection(cover)
        self.assertGreater(check.comparable_patch_pairs, 0)
        self.assertGreater(check.checked_event_pairs, 0)

    def test_frp_holds_for_hidden_intermediary_lattice(self) -> None:
        cover = build_hidden_intermediary_lattice_cover()
        check = check_finality_reflection(cover)
        self.assertTrue(check.holds)
        self.assertEqual(check.violations, ())

    def test_frp_holds_for_branching_dependency_lattice(self) -> None:
        cover = build_branching_dependency_lattice_cover()
        check = check_finality_reflection(cover)
        self.assertTrue(check.holds)
        self.assertEqual(check.violations, ())

    def test_frp_is_not_vacuous_for_branching_dependency_lattice(self) -> None:
        cover = build_branching_dependency_lattice_cover()
        check = check_finality_reflection(cover)
        self.assertGreater(check.checked_event_pairs, 10)


class GapRestrictionTests(unittest.TestCase):
    def test_gap_restriction_closure_holds_for_hidden_intermediary(self) -> None:
        cover = build_hidden_intermediary_lattice_cover()
        check = check_gap_restriction_closure(cover)
        self.assertTrue(check.holds)
        self.assertEqual(check.violations, ())

    def test_gap_restriction_closure_holds_for_branching_dependency(self) -> None:
        cover = build_branching_dependency_lattice_cover()
        check = check_gap_restriction_closure(cover)
        self.assertTrue(check.holds)
        self.assertEqual(check.violations, ())

    def test_smaller_gap_need_not_lift_to_larger_patch(self) -> None:
        cover = build_hidden_intermediary_lattice_cover()
        global_order = compute_global_order(cover)
        patches = {p.name: p for p in cover.patches}
        smaller_gap = gap_pairs(cover, patches["U_r1_r3"], global_order)
        larger_gap = gap_pairs(cover, patches["U_r1_r2_r3"], global_order)

        self.assertIn(("e_j", "e_i"), smaller_gap)
        self.assertNotIn(("e_j", "e_i"), larger_gap)

    def test_non_lifting_example_is_recorded(self) -> None:
        cover = build_hidden_intermediary_lattice_cover()
        check = check_gap_restriction_closure(cover)
        pairs = {ex.pair for ex in check.non_lifting_examples}
        self.assertIn(("e_j", "e_i"), pairs)


class ComplementCounterexampleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.counterexample = build_generic_complement_counterexample()

    def test_generic_complement_counterexample_violates_frp(self) -> None:
        self.assertFalse(self.counterexample.frp_holds)

    def test_generic_complement_counterexample_not_closed(self) -> None:
        self.assertFalse(self.counterexample.complement_restriction_closed)
        self.assertIn(
            self.counterexample.witness_pair,
            self.counterexample.complement_larger,
        )
        self.assertNotIn(
            self.counterexample.witness_pair,
            self.counterexample.complement_smaller,
        )


class FullT57AnalysisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t57_analysis()

    def test_all_reflection_checks_hold(self) -> None:
        self.assertTrue(all(check.holds for check in self.result.reflection_checks))

    def test_all_gap_checks_hold(self) -> None:
        self.assertTrue(all(check.holds for check in self.result.gap_checks))

    def test_h3_refutes_automatic_complement_closure(self) -> None:
        h3 = next(
            h for h in self.result.hypothesis_evaluations
            if h.hypothesis_id == "H3"
        )
        self.assertEqual(h3.status, "refuted")

    def test_arrow_direction_risk_left_open(self) -> None:
        h4 = next(
            h for h in self.result.hypothesis_evaluations
            if h.hypothesis_id == "H4"
        )
        self.assertEqual(h4.status, "left_open")

    def test_best_supported_mentions_gap_presheaf(self) -> None:
        self.assertIn("gap-presheaf", self.result.best_supported)


if __name__ == "__main__":
    unittest.main()
