import unittest

from models.bell_contextuality_finality import (
    analyze_chsh_finality,
    canonical_chsh_finality_scenario,
    classical_deterministic_model,
    compare_probability_models,
    local_section_for_context,
    pr_box_model,
    quantum_tsirelson_model,
    run_t21_analysis,
)


class BellContextualityFinalityTests(unittest.TestCase):
    def test_each_context_has_local_finality_section(self) -> None:
        scenario = canonical_chsh_finality_scenario()

        for context in scenario.contexts:
            section = local_section_for_context(context)
            self.assertEqual(len(section.assignments), 2)
            self.assertTrue(
                all(left * right == context.parity for left, right in section.assignments)
            )

    def test_canonical_chsh_has_no_global_assignment(self) -> None:
        result = analyze_chsh_finality()

        self.assertTrue(result.all_local_sections_exist)
        self.assertTrue(result.compatible_on_named_overlaps)
        self.assertTrue(result.no_global_assignment)
        self.assertTrue(result.h1_style_obstruction)

    def test_contextuality_witness_has_chsh_parity_contradiction(self) -> None:
        result = analyze_chsh_finality()

        self.assertEqual(result.contextuality_witness.parity_product, -1)
        self.assertEqual(result.contextuality_witness.expected_noncontextual_product, 1)
        self.assertIn("global assignment", result.contextuality_witness.contradiction)

    def test_contexts_encode_three_same_one_different_pattern(self) -> None:
        result = analyze_chsh_finality()

        relations = [section.relation for section in result.local_sections]
        self.assertEqual(relations.count("same"), 3)
        self.assertEqual(relations.count("different"), 1)

    def test_full_analysis_reports_guardrails(self) -> None:
        result = run_t21_analysis()

        self.assertTrue(result["verdict"]["bell_chsh_mapping_constructed"])
        self.assertTrue(result["verdict"]["local_finality_without_global_section"])
        self.assertTrue(result["verdict"]["contextuality_certificate_detected"])
        self.assertTrue(
            result["verdict"]["physical_referent_is_structural_not_probabilistic"]
        )
        self.assertIn("not a simulation", result["interpretation"]["guardrail"])

    def test_classical_model_respects_chsh_bound(self) -> None:
        model = classical_deterministic_model()

        self.assertEqual(model.chsh_score, 2.0)
        self.assertTrue(model.global_assignment_available)
        self.assertEqual(model.finality_status, "global_noncontextual_section_available")

    def test_quantum_model_reaches_tsirelson_target(self) -> None:
        comparison = compare_probability_models()
        model = quantum_tsirelson_model()

        self.assertAlmostEqual(model.chsh_score, comparison.tsirelson_bound)
        self.assertGreater(model.chsh_score, comparison.classical_bound)
        self.assertFalse(model.global_assignment_available)
        self.assertEqual(model.finality_status, "local_sections_without_global_assignment")

    def test_pr_box_reaches_no_signalling_extreme(self) -> None:
        comparison = compare_probability_models()
        model = pr_box_model()

        self.assertEqual(model.chsh_score, comparison.no_signalling_bound)
        self.assertGreater(model.chsh_score, comparison.tsirelson_bound)
        self.assertTrue(model.no_signalling)

    def test_probability_comparison_reports_three_way_separation(self) -> None:
        comparison = compare_probability_models()

        self.assertTrue(comparison.quantum_exceeds_classical)
        self.assertTrue(comparison.quantum_respects_tsirelson)
        self.assertTrue(comparison.pr_box_exceeds_tsirelson)

    def test_full_analysis_includes_probability_bearing_result(self) -> None:
        result = run_t21_analysis()

        self.assertTrue(result["verdict"]["probability_bearing_chsh_model_added"])
        self.assertTrue(result["verdict"]["classical_quantum_pr_separation_detected"])
        self.assertEqual(len(result["probability_models"]["models"]), 3)


if __name__ == "__main__":
    unittest.main()
