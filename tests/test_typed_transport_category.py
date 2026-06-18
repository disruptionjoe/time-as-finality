"""Tests for T41: Typed transport category prototype."""

from __future__ import annotations

import unittest

from models.d1_restriction_system import D1_DIMENSIONS, D1RestrictionMorphism, SiteMap
from models.typed_transport_category import (
    HypothesisCategory,
    MorphismEqualityCheck,
    T41Result,
    _make_aligned_morphism,
    _make_category_system,
    _make_obstructed_system,
    _make_unobstructed_3site_system,
    build_po1_functor_test,
    make_identity,
    morphisms_equal_modulo_name,
    run_t41_analysis,
    t41_result_to_dict,
    verify_associativity,
    verify_left_unit,
    verify_right_unit,
)
from models.transport_network import _compose_morphisms


class TestRunCompletes(unittest.TestCase):
    """Smoke tests: analysis runs and returns expected structure."""

    @classmethod
    def setUpClass(cls):
        cls.result = run_t41_analysis()

    def test_returns_t41_result(self):
        self.assertIsInstance(self.result, T41Result)

    def test_has_category_objects(self):
        self.assertGreater(len(self.result.category_objects), 0)

    def test_has_identity_morphisms(self):
        self.assertGreater(len(self.result.identity_morphisms), 0)

    def test_has_associativity_tests(self):
        self.assertGreater(len(self.result.associativity_tests), 0)

    def test_has_left_unit_tests(self):
        self.assertGreater(len(self.result.left_unit_tests), 0)

    def test_has_right_unit_tests(self):
        self.assertGreater(len(self.result.right_unit_tests), 0)

    def test_has_category_laws(self):
        self.assertEqual(len(self.result.category_laws), 3)

    def test_has_po1_functor_tests(self):
        self.assertGreater(len(self.result.po1_functor_tests), 0)

    def test_has_hypotheses(self):
        self.assertGreater(len(self.result.hypothesis_evaluations), 0)

    def test_serializes_to_dict(self):
        d = t41_result_to_dict(self.result)
        self.assertIsInstance(d, dict)
        self.assertIn("forms_proper_category", d)
        self.assertIn("theorem_category", d)
        self.assertIn("hypotheses", d)


class TestIdentityMorphism(unittest.TestCase):
    """Tests for make_identity()."""

    def setUp(self):
        self.sys_a = _make_category_system("TestA", "ta")

    def test_identity_source_equals_target(self):
        id_a = make_identity(self.sys_a)
        self.assertEqual(id_a.source.name, id_a.target.name)

    def test_identity_source_is_system(self):
        id_a = make_identity(self.sys_a)
        self.assertEqual(id_a.source.name, self.sys_a.name)

    def test_identity_site_map_is_identity_function(self):
        id_a = make_identity(self.sys_a)
        for sm in id_a.site_map:
            self.assertEqual(sm.source_site, sm.target_site)

    def test_identity_covers_all_sites(self):
        id_a = make_identity(self.sys_a)
        system_sites = frozenset(self.sys_a.site_ids())
        identity_sites = frozenset(sm.source_site for sm in id_a.site_map)
        self.assertEqual(system_sites, identity_sites)

    def test_identity_preserves_all_dimensions(self):
        id_a = make_identity(self.sys_a)
        self.assertEqual(frozenset(id_a.preserved_dimensions), frozenset(D1_DIMENSIONS))

    def test_identity_name_convention(self):
        id_a = make_identity(self.sys_a)
        self.assertIn(self.sys_a.name, id_a.name)

    def test_identity_for_3site_system(self):
        sys = _make_obstructed_system("TestObs3", "tobs")
        id_s = make_identity(sys)
        self.assertEqual(len(id_s.site_map), len(sys.site_ids()))
        for sm in id_s.site_map:
            self.assertEqual(sm.source_site, sm.target_site)


class TestMorphismsEqualModuloName(unittest.TestCase):
    """Tests for morphisms_equal_modulo_name()."""

    def setUp(self):
        self.sys_a = _make_category_system("EqA", "eqa")
        self.sys_b = _make_category_system("EqB", "eqb")

    def test_identical_morphisms_equal(self):
        f = _make_aligned_morphism("f", self.sys_a, self.sys_b, D1_DIMENSIONS)
        g = _make_aligned_morphism("g", self.sys_a, self.sys_b, D1_DIMENSIONS)
        check = morphisms_equal_modulo_name(f, g)
        self.assertTrue(check.equal_modulo_name)

    def test_different_dims_not_equal(self):
        f = _make_aligned_morphism("f", self.sys_a, self.sys_b, D1_DIMENSIONS)
        g = _make_aligned_morphism("g", self.sys_a, self.sys_b, ("accessible_support",))
        check = morphisms_equal_modulo_name(f, g)
        self.assertFalse(check.equal_modulo_name)
        self.assertFalse(check.preserved_dims_match)

    def test_different_source_not_equal(self):
        sys_c = _make_category_system("EqC", "eqc")
        f = _make_aligned_morphism("f", self.sys_a, self.sys_b, D1_DIMENSIONS)
        g = _make_aligned_morphism("g", sys_c, self.sys_b, D1_DIMENSIONS)
        check = morphisms_equal_modulo_name(f, g)
        self.assertFalse(check.source_match)
        self.assertFalse(check.equal_modulo_name)

    def test_different_target_not_equal(self):
        sys_c = _make_category_system("EqC2", "eqc2")
        f = _make_aligned_morphism("f", self.sys_a, self.sys_b, D1_DIMENSIONS)
        g = _make_aligned_morphism("g", self.sys_a, sys_c, D1_DIMENSIONS)
        check = morphisms_equal_modulo_name(f, g)
        self.assertFalse(check.target_match)
        self.assertFalse(check.equal_modulo_name)

    def test_same_dims_different_order_equal(self):
        f = _make_aligned_morphism("f", self.sys_a, self.sys_b, D1_DIMENSIONS)
        g = _make_aligned_morphism("g", self.sys_a, self.sys_b, tuple(reversed(D1_DIMENSIONS)))
        check = morphisms_equal_modulo_name(f, g)
        self.assertTrue(check.preserved_dims_match)


class TestAssociativity(unittest.TestCase):
    """Tests for the associativity law."""

    @classmethod
    def setUpClass(cls):
        cls.sys_a = _make_category_system("AssocA", "aa")
        cls.sys_b = _make_category_system("AssocB", "ab")
        cls.sys_c = _make_category_system("AssocC", "ac")
        cls.sys_d = _make_category_system("AssocD", "ad")
        cls.f = _make_aligned_morphism("f_assoc", cls.sys_a, cls.sys_b, D1_DIMENSIONS)
        cls.g = _make_aligned_morphism("g_assoc", cls.sys_b, cls.sys_c, D1_DIMENSIONS)
        cls.h = _make_aligned_morphism("h_assoc", cls.sys_c, cls.sys_d, D1_DIMENSIONS)

    def test_associativity_holds_all_dims(self):
        result = verify_associativity(self.f, self.g, self.h)
        self.assertTrue(result.associativity_holds)

    def test_associativity_site_map_component(self):
        result = verify_associativity(self.f, self.g, self.h)
        self.assertTrue(result.site_map_associative)

    def test_associativity_preserved_dims_component(self):
        result = verify_associativity(self.f, self.g, self.h)
        self.assertTrue(result.preserved_dims_associative)

    def test_associativity_holds_mixed_dims(self):
        f2 = _make_aligned_morphism("f2", self.sys_a, self.sys_b, ("accessible_support", "holder_redundancy"))
        g2 = _make_aligned_morphism("g2", self.sys_b, self.sys_c, ("accessible_support",))
        h2 = _make_aligned_morphism("h2", self.sys_c, self.sys_d, ("accessible_support", "branch_support"))
        result = verify_associativity(f2, g2, h2)
        self.assertTrue(result.associativity_holds)

    def test_associativity_holds_single_dim(self):
        f3 = _make_aligned_morphism("f3", self.sys_a, self.sys_b, ("accessible_support",))
        g3 = _make_aligned_morphism("g3", self.sys_b, self.sys_c, ("accessible_support",))
        h3 = _make_aligned_morphism("h3", self.sys_c, self.sys_d, ("accessible_support",))
        result = verify_associativity(f3, g3, h3)
        self.assertTrue(result.associativity_holds)

    def test_associativity_with_identity_in_triple(self):
        id_a = make_identity(self.sys_a)
        result = verify_associativity(id_a, self.f, self.g)
        self.assertTrue(result.associativity_holds)

    def test_associativity_lhs_rhs_names_differ(self):
        result = verify_associativity(self.f, self.g, self.h)
        self.assertNotEqual(result.lhs_label, result.rhs_label)

    def test_associativity_records_morphism_names(self):
        result = verify_associativity(self.f, self.g, self.h)
        self.assertEqual(result.f_name, self.f.name)
        self.assertEqual(result.g_name, self.g.name)
        self.assertEqual(result.h_name, self.h.name)

    def test_dims_intersection_associative(self):
        # preserved_dims = (f_dims ∩ g_dims) ∩ h_dims = f_dims ∩ (g_dims ∩ h_dims)
        f_dims = frozenset(("accessible_support", "holder_redundancy"))
        g_dims = frozenset(("accessible_support",))
        h_dims = frozenset(("accessible_support", "reversal_cost"))
        lhs = (f_dims & g_dims) & h_dims
        rhs = f_dims & (g_dims & h_dims)
        self.assertEqual(lhs, rhs)


class TestIdentityLaws(unittest.TestCase):
    """Tests for left and right unit laws."""

    @classmethod
    def setUpClass(cls):
        cls.sys_a = _make_category_system("UnitA", "ua")
        cls.sys_b = _make_category_system("UnitB", "ub")
        cls.f_full = _make_aligned_morphism("f_unit_full", cls.sys_a, cls.sys_b, D1_DIMENSIONS)
        cls.f_partial = _make_aligned_morphism(
            "f_unit_partial", cls.sys_a, cls.sys_b, ("accessible_support",)
        )

    def test_left_unit_holds_full_dims(self):
        result = verify_left_unit(self.f_full)
        self.assertTrue(result.law_holds)

    def test_left_unit_holds_partial_dims(self):
        result = verify_left_unit(self.f_partial)
        self.assertTrue(result.law_holds)

    def test_left_unit_site_map_preserved(self):
        result = verify_left_unit(self.f_full)
        self.assertTrue(result.site_map_match)

    def test_left_unit_preserved_dims_preserved(self):
        result = verify_left_unit(self.f_full)
        self.assertTrue(result.preserved_dims_match)

    def test_left_unit_source_preserved(self):
        result = verify_left_unit(self.f_full)
        self.assertTrue(result.source_match)

    def test_left_unit_target_preserved(self):
        result = verify_left_unit(self.f_full)
        self.assertTrue(result.target_match)

    def test_right_unit_holds_full_dims(self):
        result = verify_right_unit(self.f_full)
        self.assertTrue(result.law_holds)

    def test_right_unit_holds_partial_dims(self):
        result = verify_right_unit(self.f_partial)
        self.assertTrue(result.law_holds)

    def test_right_unit_site_map_preserved(self):
        result = verify_right_unit(self.f_full)
        self.assertTrue(result.site_map_match)

    def test_right_unit_preserved_dims_preserved(self):
        result = verify_right_unit(self.f_full)
        self.assertTrue(result.preserved_dims_match)

    def test_left_unit_law_label(self):
        result = verify_left_unit(self.f_full)
        self.assertEqual(result.law, "left_unit")

    def test_right_unit_law_label(self):
        result = verify_right_unit(self.f_full)
        self.assertEqual(result.law, "right_unit")

    def test_identity_composition_left_recovers_morphism_function(self):
        id_a = make_identity(self.sys_a)
        composed = _compose_morphisms(id_a, self.f_full)
        f_pairs = frozenset((sm.source_site, sm.target_site) for sm in self.f_full.site_map)
        c_pairs = frozenset((sm.source_site, sm.target_site) for sm in composed.site_map)
        self.assertEqual(f_pairs, c_pairs)

    def test_identity_composition_right_recovers_morphism_function(self):
        id_b = make_identity(self.sys_b)
        composed = _compose_morphisms(self.f_full, id_b)
        f_pairs = frozenset((sm.source_site, sm.target_site) for sm in self.f_full.site_map)
        c_pairs = frozenset((sm.source_site, sm.target_site) for sm in composed.site_map)
        self.assertEqual(f_pairs, c_pairs)

    def test_identity_composition_left_recovers_dims(self):
        id_a = make_identity(self.sys_a)
        composed = _compose_morphisms(id_a, self.f_partial)
        self.assertEqual(
            frozenset(composed.preserved_dimensions),
            frozenset(self.f_partial.preserved_dimensions),
        )

    def test_identity_composition_right_recovers_dims(self):
        id_b = make_identity(self.sys_b)
        composed = _compose_morphisms(self.f_partial, id_b)
        self.assertEqual(
            frozenset(composed.preserved_dimensions),
            frozenset(self.f_partial.preserved_dimensions),
        )


class TestCategoryLaws(unittest.TestCase):
    """Tests for the full category law summary from run_t41_analysis."""

    @classmethod
    def setUpClass(cls):
        cls.result = run_t41_analysis()

    def test_associativity_law_holds(self):
        law = next(l for l in self.result.category_laws if l.law_name == "associativity")
        self.assertTrue(law.holds)

    def test_left_unit_law_holds(self):
        law = next(l for l in self.result.category_laws if l.law_name == "left_unit")
        self.assertTrue(law.holds)

    def test_right_unit_law_holds(self):
        law = next(l for l in self.result.category_laws if l.law_name == "right_unit")
        self.assertTrue(law.holds)

    def test_all_category_laws_hold(self):
        self.assertTrue(self.result.all_category_laws_hold)

    def test_forms_proper_category(self):
        self.assertTrue(self.result.forms_proper_category)

    def test_associativity_all_tests_pass(self):
        law = next(l for l in self.result.category_laws if l.law_name == "associativity")
        self.assertEqual(law.tests_passed, law.tests_run)

    def test_left_unit_all_tests_pass(self):
        law = next(l for l in self.result.category_laws if l.law_name == "left_unit")
        self.assertEqual(law.tests_passed, law.tests_run)

    def test_right_unit_all_tests_pass(self):
        law = next(l for l in self.result.category_laws if l.law_name == "right_unit")
        self.assertEqual(law.tests_passed, law.tests_run)


class TestPO1FunctorViolation(unittest.TestCase):
    """Tests for the PO1 non-functor theorem."""

    @classmethod
    def setUpClass(cls):
        cls.result = run_t41_analysis()
        cls.po1_test = cls.result.po1_functor_tests[0]

    def test_functor_law_violated(self):
        self.assertTrue(self.po1_test.functor_law_violated)

    def test_composed_is_po1(self):
        self.assertTrue(self.po1_test.fg_po1)

    def test_boolean_and_does_not_predict_po1(self):
        self.assertFalse(self.po1_test.boolean_and_predicts_po1)

    def test_actual_result_contradicts_boolean_and(self):
        self.assertNotEqual(self.po1_test.boolean_and_predicts_po1, self.po1_test.actual_fg_po1)

    def test_po1_not_a_functor(self):
        self.assertFalse(self.result.po1_is_functor)

    def test_has_interpretation(self):
        self.assertGreater(len(self.po1_test.interpretation), 0)

    def test_po1_functor_test_standalone(self):
        test = build_po1_functor_test()
        self.assertIsInstance(test.functor_law_violated, bool)


class TestHypotheses(unittest.TestCase):
    """Tests for hypothesis verdicts."""

    @classmethod
    def setUpClass(cls):
        cls.result = run_t41_analysis()
        cls.hyps = {h.hypothesis_id: h for h in cls.result.hypothesis_evaluations}

    def test_hypothesis_ids_present(self):
        self.assertIn("H_A", self.hyps)
        self.assertIn("H_B", self.hyps)
        self.assertIn("H_C", self.hyps)

    def test_h_a_best_supported_or_supported(self):
        h_a = self.hyps["H_A"]
        self.assertIn(h_a.status, ("best_supported", "supported"))

    def test_h_b_not_best_supported(self):
        h_b = self.hyps["H_B"]
        self.assertNotEqual(h_b.status, "best_supported")

    def test_h_c_supported(self):
        h_c = self.hyps["H_C"]
        self.assertIn(h_c.status, ("best_supported", "supported"))

    def test_best_supported_hypothesis_set(self):
        self.assertIn(self.result.best_supported_hypothesis, ("H_A", "H_C", "undetermined"))

    def test_all_hypotheses_have_verdicts(self):
        for h in self.result.hypothesis_evaluations:
            self.assertGreater(len(h.verdict), 0)


class TestTheoremContent(unittest.TestCase):
    """Tests for theorem and boundary content."""

    @classmethod
    def setUpClass(cls):
        cls.result = run_t41_analysis()

    def test_theorem_category_mentions_category(self):
        self.assertIn("category", self.result.theorem_category.lower())

    def test_theorem_po1_nonfunctor_mentions_nonfunctor(self):
        t = self.result.theorem_po1_nonfunctor.lower()
        self.assertTrue("functor" in t or "t34" in t)

    def test_boundary_mentions_limitation(self):
        b = self.result.boundary.lower()
        self.assertTrue(
            "not" in b or "boundary" in b or "limit" in b or "does not" in b
        )

    def test_recommendation_mentions_next_steps(self):
        r = self.result.recommendation.lower()
        self.assertTrue(
            "next" in r or "further" in r or "explore" in r or "check" in r
        )


if __name__ == "__main__":
    unittest.main()
