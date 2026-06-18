"""Tests for T39: CSP / Satisfiability Reframing.

Tests verify four theorems:
  1. Arc-Consistency Triviality: every binary same/different constraint is arc-consistent.
  2. Signed-Graph Parity: globally satisfiable iff no negative cycle.
  3. D1-CSP Equivalence: D1 obstruction iff CSP parity conflict.
  4. PO1-as-CSP: PO1 = CSP obstruction + typed projection + admissibility classification.
"""

import unittest
from models.csp_satisfiability_reframing import (
    T39Result,
    run_t39_analysis,
    build_minimum_direct_obstruction,
    build_minimum_transitive_obstruction,
    build_tree_structured_csp,
    build_satisfiable_csp,
    _check_arc_consistency,
    _csp_from_system,
    _parity_analysis,
    _analyze_csp,
)

_RESULT: T39Result | None = None


def _r() -> T39Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t39_analysis()
    return _RESULT


class TestRunCompletes(unittest.TestCase):
    def test_run_returns_result(self) -> None:
        r = _r()
        self.assertIsInstance(r, T39Result)

    def test_best_hypothesis_is_h_b(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H_B")

    def test_four_d1_analyses(self) -> None:
        self.assertEqual(len(_r().d1_to_csp_analyses), 4)

    def test_four_po1_bridges(self) -> None:
        self.assertEqual(len(_r().po1_as_csp_bridges), 4)

    def test_three_hypotheses(self) -> None:
        self.assertEqual(len(_r().hypothesis_evaluations), 3)

    def test_theorems_populated(self) -> None:
        r = _r()
        self.assertTrue(r.theorem_arc_consistency)
        self.assertTrue(r.theorem_parity)
        self.assertTrue(r.theorem_d1_csp_equivalence)
        self.assertTrue(r.theorem_po1_as_csp)

    def test_boundary_populated(self) -> None:
        self.assertTrue(_r().boundary)

    def test_recommendation_populated(self) -> None:
        self.assertTrue(_r().recommendation)


class TestArcConsistencyTriviality(unittest.TestCase):
    """Theorem 1: every binary same/different constraint over {-1,1} is arc-consistent."""

    def _check_all_arc_consistent(self, name: str) -> None:
        r = _r()
        for a in r.d1_to_csp_analyses:
            if a.csp.name == name:
                self.assertTrue(a.arc_consistency.all_arc_consistent,
                                f"{name} should be arc-consistent")
                return
        self.fail(f"analysis {name!r} not found")

    def test_direct_conflict_arc_consistent(self) -> None:
        self._check_all_arc_consistent("min_direct_conflict")

    def test_transitive_conflict_arc_consistent(self) -> None:
        self._check_all_arc_consistent("min_transitive_conflict")

    def test_tree_structured_arc_consistent(self) -> None:
        self._check_all_arc_consistent("tree_structured")

    def test_satisfiable_arc_consistent(self) -> None:
        self._check_all_arc_consistent("satisfiable_all_same")

    def test_arc_consistency_adds_no_information(self) -> None:
        r = _r()
        for a in r.d1_to_csp_analyses:
            # arc consistent even when globally UN-satisfiable
            self.assertTrue(a.arc_consistency.all_arc_consistent,
                            f"{a.csp.name} not arc-consistent")

    def test_arc_consistency_count_matches_constraints(self) -> None:
        r = _r()
        for a in r.d1_to_csp_analyses:
            ac = a.arc_consistency
            self.assertEqual(ac.arc_consistent_count, ac.total_constraints)


class TestSignedGraphParity(unittest.TestCase):
    """Theorem 2: globally satisfiable iff no negative cycle."""

    def test_direct_conflict_is_not_globally_satisfiable(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        p = _parity_analysis(csp)
        self.assertFalse(p.globally_satisfiable)
        self.assertEqual(p.global_witness_count, 0)

    def test_transitive_conflict_is_not_globally_satisfiable(self) -> None:
        csp, _ = build_minimum_transitive_obstruction()
        p = _parity_analysis(csp)
        self.assertFalse(p.globally_satisfiable)
        self.assertEqual(p.global_witness_count, 0)

    def test_tree_structured_is_globally_satisfiable(self) -> None:
        csp, _ = build_tree_structured_csp()
        p = _parity_analysis(csp)
        self.assertTrue(p.globally_satisfiable)
        self.assertGreater(p.global_witness_count, 0)

    def test_satisfiable_all_same_is_globally_satisfiable(self) -> None:
        csp, _ = build_satisfiable_csp()
        p = _parity_analysis(csp)
        self.assertTrue(p.globally_satisfiable)
        self.assertGreater(p.global_witness_count, 0)

    def test_direct_conflict_is_locally_satisfiable(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        p = _parity_analysis(csp)
        self.assertTrue(p.locally_satisfiable)

    def test_transitive_conflict_is_locally_satisfiable(self) -> None:
        csp, _ = build_minimum_transitive_obstruction()
        p = _parity_analysis(csp)
        self.assertTrue(p.locally_satisfiable)

    def test_direct_obstruction_type(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        p = _parity_analysis(csp)
        self.assertEqual(p.obstruction_type, "direct_parity_conflict")

    def test_transitive_obstruction_type(self) -> None:
        csp, _ = build_minimum_transitive_obstruction()
        p = _parity_analysis(csp)
        self.assertEqual(p.obstruction_type, "transitive_parity_conflict")

    def test_tree_no_obstruction(self) -> None:
        csp, _ = build_tree_structured_csp()
        p = _parity_analysis(csp)
        self.assertEqual(p.obstruction_type, "none")

    def test_satisfiable_no_obstruction(self) -> None:
        csp, _ = build_satisfiable_csp()
        p = _parity_analysis(csp)
        self.assertEqual(p.obstruction_type, "none")

    def test_direct_minimum_conflict_size_is_2(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        p = _parity_analysis(csp)
        self.assertEqual(p.minimum_conflict_size, 2)

    def test_transitive_minimum_conflict_size_is_3(self) -> None:
        csp, _ = build_minimum_transitive_obstruction()
        p = _parity_analysis(csp)
        self.assertEqual(p.minimum_conflict_size, 3)

    def test_direct_has_2_variables(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        self.assertEqual(len(csp.variables), 2)

    def test_transitive_has_3_variables(self) -> None:
        csp, _ = build_minimum_transitive_obstruction()
        self.assertEqual(len(csp.variables), 3)

    def test_tree_has_4_variables(self) -> None:
        csp, _ = build_tree_structured_csp()
        self.assertEqual(len(csp.variables), 4)


class TestD1CSPEquivalence(unittest.TestCase):
    """Theorem 3: D1 obstruction iff parity conflict."""

    def test_direct_d1_equivalence_verified(self) -> None:
        _, sys = build_minimum_direct_obstruction()
        csp, _ = build_minimum_direct_obstruction()
        a = _analyze_csp(csp, sys)
        self.assertTrue(a.d1_equivalence_verified)

    def test_transitive_d1_equivalence_verified(self) -> None:
        _, sys = build_minimum_transitive_obstruction()
        csp, _ = build_minimum_transitive_obstruction()
        a = _analyze_csp(csp, sys)
        self.assertTrue(a.d1_equivalence_verified)

    def test_tree_d1_equivalence_verified(self) -> None:
        _, sys = build_tree_structured_csp()
        csp, _ = build_tree_structured_csp()
        a = _analyze_csp(csp, sys)
        self.assertTrue(a.d1_equivalence_verified)

    def test_satisfiable_d1_equivalence_verified(self) -> None:
        _, sys = build_satisfiable_csp()
        csp, _ = build_satisfiable_csp()
        a = _analyze_csp(csp, sys)
        self.assertTrue(a.d1_equivalence_verified)

    def test_all_analyses_d1_equivalence_verified(self) -> None:
        r = _r()
        for a in r.d1_to_csp_analyses:
            self.assertTrue(a.d1_equivalence_verified,
                            f"{a.csp.name} D1 equivalence failed")

    def test_minimum_direct_obstruction_equivalence(self) -> None:
        self.assertTrue(_r().minimum_direct_obstruction.d1_equivalence_verified)

    def test_minimum_transitive_obstruction_equivalence(self) -> None:
        self.assertTrue(_r().minimum_transitive_obstruction.d1_equivalence_verified)


class TestPO1AsCSP(unittest.TestCase):
    """Theorem 4: PO1 = CSP obstruction + typed projection + admissibility."""

    def _bridge(self, name: str):  # type: ignore[return]
        for b in _r().po1_as_csp_bridges:
            if b.case_name == name:
                return b
        self.fail(f"bridge {name!r} not found")

    def test_witten_po1_true(self) -> None:
        self.assertTrue(self._bridge("witten_1981").po1_verdict)

    def test_witten_csp_detects_obstruction(self) -> None:
        self.assertTrue(self._bridge("witten_1981").csp_detects_obstruction)

    def test_witten_source_satisfiable(self) -> None:
        self.assertTrue(self._bridge("witten_1981").source_globally_satisfiable)

    def test_nielsen_ninomiya_po1_true(self) -> None:
        self.assertTrue(self._bridge("nielsen_ninomiya").po1_verdict)

    def test_nielsen_ninomiya_csp_detects(self) -> None:
        self.assertTrue(self._bridge("nielsen_ninomiya").csp_detects_obstruction)

    def test_lossy_no_obstruction_po1_false(self) -> None:
        self.assertFalse(self._bridge("synthetic_lossy_no_obstruction").po1_verdict)

    def test_lossy_no_obstruction_target_unobstructed(self) -> None:
        self.assertEqual(
            self._bridge("synthetic_lossy_no_obstruction").target_obstruction_type, "none")

    def test_shared_obstruction_po1_false(self) -> None:
        self.assertFalse(self._bridge("synthetic_shared_obstruction").po1_verdict)

    def test_ac5_not_expressible_in_csp(self) -> None:
        for b in _r().po1_as_csp_bridges:
            self.assertFalse(b.ac5_expressible_in_csp,
                             f"AC5 should not be CSP-expressible in {b.case_name}")

    def test_ac7_not_expressible_in_csp(self) -> None:
        for b in _r().po1_as_csp_bridges:
            self.assertFalse(b.ac7_expressible_in_csp,
                             f"AC7 should not be CSP-expressible in {b.case_name}")

    def test_all_bridges_have_gap_conditions(self) -> None:
        for b in _r().po1_as_csp_bridges:
            self.assertGreater(len(b.csp_gap_conditions), 0,
                               f"{b.case_name} has no gap conditions")

    def test_shared_obstruction_source_not_satisfiable(self) -> None:
        b = self._bridge("synthetic_shared_obstruction")
        self.assertFalse(b.source_globally_satisfiable)


class TestHypotheses(unittest.TestCase):

    def _hyp(self, hid: str):  # type: ignore[return]
        for h in _r().hypothesis_evaluations:
            if h.hypothesis_id == hid:
                return h
        self.fail(f"hypothesis {hid!r} not found")

    def test_h_a_rejected(self) -> None:
        self.assertEqual(self._hyp("H_A").verdict, "rejected")

    def test_h_b_best_supported(self) -> None:
        self.assertEqual(self._hyp("H_B").verdict, "best_supported")

    def test_h_c_partially_supported(self) -> None:
        self.assertEqual(self._hyp("H_C").verdict, "partially_supported")

    def test_h_a_has_evidence_against(self) -> None:
        self.assertGreater(len(self._hyp("H_A").evidence_against), 0)

    def test_h_b_has_evidence_for(self) -> None:
        self.assertGreater(len(self._hyp("H_B").evidence_for), 0)

    def test_best_supported_matches_field(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H_B")

    def test_h_b_claim_mentions_csp(self) -> None:
        self.assertIn("CSP", self._hyp("H_B").claim)

    def test_h_b_claim_mentions_typed_projection(self) -> None:
        self.assertIn("Typed projection", self._hyp("H_B").claim)


class TestCSPConstruction(unittest.TestCase):

    def test_csp_from_direct_system_has_2_vars(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        self.assertEqual(len(csp.variables), 2)

    def test_csp_from_direct_system_has_2_constraints(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        self.assertEqual(len(csp.all_constraints), 2)

    def test_csp_from_transitive_system_has_3_constraints(self) -> None:
        csp, _ = build_minimum_transitive_obstruction()
        self.assertEqual(len(csp.all_constraints), 3)

    def test_csp_patch_groups_match_patches(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        self.assertEqual(len(csp.patch_groups), 2)

    def test_csp_transitive_patch_groups(self) -> None:
        csp, _ = build_minimum_transitive_obstruction()
        self.assertEqual(len(csp.patch_groups), 3)

    def test_direct_csp_name(self) -> None:
        csp, _ = build_minimum_direct_obstruction()
        self.assertEqual(csp.name, "min_direct_conflict")

    def test_transitive_csp_name(self) -> None:
        csp, _ = build_minimum_transitive_obstruction()
        self.assertEqual(csp.name, "min_transitive_conflict")

    def test_tree_csp_has_3_constraints(self) -> None:
        csp, _ = build_tree_structured_csp()
        self.assertEqual(len(csp.all_constraints), 3)

    def test_satisfiable_csp_has_2_constraints(self) -> None:
        csp, _ = build_satisfiable_csp()
        self.assertEqual(len(csp.all_constraints), 2)


if __name__ == "__main__":
    unittest.main()
