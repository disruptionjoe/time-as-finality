"""Tests for T222: Finite-to-Infinite Boundary Theorem."""

from __future__ import annotations

import unittest

from models.finite_to_infinite_boundary_theorem import (
    csp_po1_verdict,
    d1cat_verdict,
    has_direct_parity_conflict,
    hef_verdict,
    po1_nonfunctor_verdict,
    run_t222_analysis,
    signed_graph_satisfiable,
)


class SignedGraphPrimitiveTests(unittest.TestCase):
    def test_all_same_path_is_satisfiable(self) -> None:
        self.assertTrue(
            signed_graph_satisfiable(["a", "b", "c"], [("a", "b", 1), ("b", "c", 1)])
        )

    def test_negative_triangle_is_unsatisfiable(self) -> None:
        self.assertFalse(
            signed_graph_satisfiable(
                ["a", "b", "c"], [("a", "b", 1), ("b", "c", 1), ("a", "c", -1)]
            )
        )

    def test_direct_conflict_detected(self) -> None:
        self.assertTrue(has_direct_parity_conflict([("a", "b", 1), ("a", "b", -1)]))
        self.assertFalse(has_direct_parity_conflict([("a", "b", 1), ("b", "c", -1)]))


class CSPPO1BoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v = csp_po1_verdict()

    def test_verdict_is_conditional(self) -> None:
        self.assertEqual(self.v.verdict, "conditional")

    def test_countable_survival_witness_holds(self) -> None:
        w = next(x for x in self.v.witnesses if x.side == "infinite_survival")
        self.assertTrue(w.holds)

    def test_continuum_false_section_witness_holds(self) -> None:
        w = next(x for x in self.v.witnesses if x.side == "continuum_obstruction")
        self.assertTrue(w.holds)

    def test_boundary_is_continuum_not_countability(self) -> None:
        self.assertIn("countability", self.v.boundary_line.lower())
        self.assertIn("continu", self.v.boundary_line.lower())

    def test_guardrail_blocks_cohomology_overreach(self) -> None:
        self.assertIn("Cech", self.v.guardrail_note)


class D1CatBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v = d1cat_verdict()

    def test_verdict_is_survives(self) -> None:
        self.assertEqual(self.v.verdict, "survives")

    def test_infinite_site_laws_hold(self) -> None:
        w = next(x for x in self.v.witnesses if x.side == "infinite_survival")
        self.assertTrue(w.holds)

    def test_colimit_obstruction_is_explicit(self) -> None:
        w = next(x for x in self.v.witnesses if x.side == "infinite_obstruction")
        self.assertTrue(w.holds)
        self.assertIn("empt", w.detail.lower())

    def test_guard_blocks_completeness_overread(self) -> None:
        self.assertIn("colimit", self.v.guardrail_note.lower())


class PO1NonFunctorBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v = po1_nonfunctor_verdict()

    def test_verdict_is_survives(self) -> None:
        self.assertEqual(self.v.verdict, "survives")

    def test_existential_persists_in_infinite_ambient(self) -> None:
        w = next(x for x in self.v.witnesses if x.side == "infinite_survival")
        self.assertTrue(w.holds)

    def test_polarity_guard_present(self) -> None:
        # Survival is "obstruction persists", not "functor exists".
        self.assertIn("persist", self.v.guardrail_note.lower())


class HEFBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.v = hef_verdict()

    def test_verdict_is_survives(self) -> None:
        self.assertEqual(self.v.verdict, "survives")

    def test_obstruction_persists_under_infinite_depth(self) -> None:
        w = next(x for x in self.v.witnesses if x.side == "infinite_survival")
        self.assertTrue(w.holds)

    def test_false_dissolution_guard_holds(self) -> None:
        w = next(x for x in self.v.witnesses if x.side == "infinite_obstruction")
        self.assertTrue(w.holds)

    def test_dissolution_requires_dropping_the_sign(self) -> None:
        # Only forgetting the -1 coefficient restores satisfiability.
        self.assertIn("sign", self.v.witnesses[1].detail.lower())


class T222AggregateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t222_analysis()

    def test_all_witnesses_hold(self) -> None:
        self.assertTrue(self.result.all_witnesses_hold)

    def test_four_results_classified(self) -> None:
        self.assertEqual(len(self.result.verdicts), 4)

    def test_verdict_distribution(self) -> None:
        # 3 survives (D1Cat, PO1 non-functor, HEF) + 1 conditional (CSP-PO1).
        self.assertEqual(self.result.survives_count, 3)
        self.assertEqual(self.result.conditional_count, 1)
        self.assertEqual(self.result.strictly_finite_count, 0)

    def test_most_load_bearing_is_csp_po1_continuum(self) -> None:
        self.assertIn("CSP-PO1", self.result.most_load_bearing_finite_restriction)
        self.assertIn("continuum", self.result.most_load_bearing_finite_restriction)

    def test_summary_keeps_countability_non_obstruction(self) -> None:
        self.assertIn("countability is never the obstruction", self.result.summary)


if __name__ == "__main__":
    unittest.main()
