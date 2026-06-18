import unittest

from models.cross_domain_projection_obstruction_validation import (
    access_control_inheritance_case,
    analyze_hostile_case,
    database_expand_contract_case,
    git_semantic_merge_case,
    run_t30_analysis,
    run_t30_lab,
    t30_hostile_cases,
    type_system_macro_boundary_case,
)


class CrossDomainProjectionObstructionValidationTests(unittest.TestCase):
    def test_t30_has_at_least_three_non_physics_cases(self) -> None:
        cases = t30_hostile_cases()

        self.assertGreaterEqual(len(cases), 3)
        domains = {case.domain for case in cases}
        self.assertIn("git merge conflict", domains)
        self.assertIn("database schema migration", domains)
        self.assertIn("access-control policy inheritance", domains)

    def test_git_merge_is_positive_po1_instance(self) -> None:
        analysis = analyze_hostile_case(git_semantic_merge_case())

        self.assertEqual(analysis.classification, "projection-created obstruction")
        self.assertTrue(analysis.supports_po1)
        self.assertTrue(analysis.analysis.schema.projection_definable)
        self.assertTrue(analysis.analysis.schema.obstruction_created_by_projection)
        self.assertEqual(analysis.analysis.schema.outcome, "faithful_projection_obstruction")

    def test_database_migration_is_lossy_without_obstruction(self) -> None:
        analysis = analyze_hostile_case(database_expand_contract_case())

        self.assertEqual(analysis.classification, "lossy projection without obstruction")
        self.assertFalse(analysis.supports_po1)
        self.assertFalse(analysis.analysis.schema.restricted_obstructed)
        self.assertEqual(analysis.analysis.schema.outcome, "lossy_projection_no_new_obstruction")

    def test_access_control_is_shared_obstruction(self) -> None:
        analysis = analyze_hostile_case(access_control_inheritance_case())

        self.assertEqual(analysis.classification, "shared obstruction")
        self.assertFalse(analysis.supports_po1)
        self.assertTrue(analysis.analysis.schema.richer_obstructed)
        self.assertTrue(analysis.analysis.schema.restricted_obstructed)
        self.assertFalse(analysis.analysis.schema.obstruction_created_by_projection)

    def test_type_system_case_is_non_definable_boundary(self) -> None:
        analysis = analyze_hostile_case(type_system_macro_boundary_case())

        self.assertEqual(analysis.classification, "non-definable projection")
        self.assertFalse(analysis.supports_po1)
        self.assertFalse(analysis.meaningful_po1_fit)
        self.assertFalse(analysis.analysis.schema.projection_definable)
        self.assertEqual(analysis.analysis.morphism_analysis.obstruction, "site_map_incomplete")

    def test_hypothesis_verdict_keeps_po1_constrained(self) -> None:
        result = run_t30_lab()
        evaluations = {item.hypothesis_id: item for item in result.hypothesis_evaluations}

        self.assertEqual(evaluations["H1"].status, "supported")
        self.assertEqual(evaluations["H2"].status, "not_yet_supported")
        self.assertEqual(evaluations["H4"].status, "partially_supported_as_warning")
        self.assertIn("partially_supported", result.po1_recommendation)
        self.assertIn("admissibility", result.po1_recommendation)

    def test_run_t30_analysis_shape(self) -> None:
        result = run_t30_analysis()

        self.assertIn("analyses", result)
        self.assertIn("hypothesis_evaluations", result)
        self.assertIn("po1_recommendation", result)
        self.assertGreaterEqual(len(result["analyses"]), 3)
        self.assertEqual(result["best_supported_hypothesis"], "H1 with H3/H4 constraints")


if __name__ == "__main__":
    unittest.main()
