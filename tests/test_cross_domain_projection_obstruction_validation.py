import unittest

from models.cross_domain_projection_obstruction_validation import (
    analyze_hostile_case,
    financial_risk_tail_model_case,
    git_semantic_merge_case,
    run_t30_analysis,
    run_t30_lab,
    t30_hostile_cases,
    translator_poet_boundary_case,
)


class CrossDomainProjectionObstructionValidationTests(unittest.TestCase):
    def test_t30_has_at_least_three_non_physics_cases(self) -> None:
        cases = t30_hostile_cases()

        self.assertGreaterEqual(len(cases), 3)
        domains = {case.domain for case in cases}
        self.assertIn("git merge conflict", domains)
        self.assertIn("financial risk model", domains)
        self.assertIn("translator / poet", domains)

    def test_git_merge_is_positive_po1_instance(self) -> None:
        analysis = analyze_hostile_case(git_semantic_merge_case())

        self.assertEqual(analysis.classification, "projection-created obstruction")
        self.assertTrue(analysis.supports_po1)
        self.assertTrue(analysis.analysis.schema.projection_definable)
        self.assertTrue(analysis.analysis.schema.obstruction_created_by_projection)
        self.assertEqual(analysis.analysis.schema.outcome, "faithful_projection_obstruction")

    def test_financial_risk_is_positive_po1_instance(self) -> None:
        analysis = analyze_hostile_case(financial_risk_tail_model_case())

        self.assertEqual(analysis.classification, "projection-created obstruction")
        self.assertTrue(analysis.supports_po1)
        self.assertTrue(analysis.analysis.schema.projection_definable)
        self.assertTrue(analysis.analysis.schema.obstruction_created_by_projection)
        self.assertEqual(analysis.analysis.schema.outcome, "faithful_projection_obstruction")

    def test_translator_poet_is_no_meaningful_po1_fit(self) -> None:
        analysis = analyze_hostile_case(translator_poet_boundary_case())

        self.assertEqual(analysis.classification, "no meaningful PO1 fit")
        self.assertFalse(analysis.supports_po1)
        self.assertFalse(analysis.meaningful_po1_fit)
        self.assertEqual(analysis.analysis.schema.outcome, "lossy_projection_no_new_obstruction")
        self.assertIn("anti-overclaim", analysis.hypothesis_signal)

    def test_hypothesis_verdict_keeps_po1_constrained(self) -> None:
        result = run_t30_lab()
        evaluations = {item.hypothesis_id: item for item in result.hypothesis_evaluations}

        self.assertEqual(evaluations["H1"].status, "supported")
        self.assertEqual(evaluations["H2"].status, "supported_in_finite_scope")
        self.assertEqual(evaluations["H4"].status, "partially_supported_as_warning")
        self.assertIn("partially_supported", result.po1_recommendation)
        self.assertIn("admissibility", result.po1_recommendation)

    def test_run_t30_analysis_shape(self) -> None:
        result = run_t30_analysis()

        self.assertIn("analyses", result)
        self.assertIn("hypothesis_evaluations", result)
        self.assertIn("po1_recommendation", result)
        self.assertGreaterEqual(len(result["analyses"]), 3)
        self.assertEqual(result["best_supported_hypothesis"], "H2 with H4 admissibility constraints")


if __name__ == "__main__":
    unittest.main()
