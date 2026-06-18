import unittest

from models.minimal_d1_generalization import (
    run_t25_analysis,
    run_t25_lab,
    vector_sufficient_scenario,
)
from models.multiscale_observer_field import analyze_scenario


class MinimalD1GeneralizationTests(unittest.TestCase):
    def test_question_zero_selects_minimal_graph_restriction_system(self) -> None:
        result = run_t25_lab()

        self.assertIn("finite graph-indexed", result.question_zero_answer)
        self.assertEqual(result.best_supported_hypothesis, "H3")

    def test_vector_sufficient_case_is_not_forced_to_field(self) -> None:
        analysis = analyze_scenario(vector_sufficient_scenario())

        self.assertTrue(analysis.vector.vector_required)
        self.assertFalse(analysis.transport.field_required)
        self.assertFalse(analysis.gluing.obstruction_detected)
        self.assertEqual(analysis.representation_needed, "vector")

    def test_theorem_ladder_stops_before_full_representation(self) -> None:
        result = run_t25_lab()
        ladder = {attempt.name: attempt for attempt in result.theorem_ladder}

        self.assertTrue(ladder["Scalar Recovery Theorem"].reached)
        self.assertTrue(ladder["Vector Sufficiency Theorem"].reached)
        self.assertTrue(ladder["Transport Necessity Theorem"].reached)
        self.assertTrue(ladder["Gluing Obstruction Theorem"].reached)
        self.assertTrue(ladder["Morphism Theorem"].reached)
        self.assertFalse(ladder["IPT Representation Theorem"].reached)

    def test_hypothesis_evaluation_compares_h0_through_h4(self) -> None:
        result = run_t25_lab()
        evaluations = {item.hypothesis_id: item for item in result.hypothesis_evaluations}

        self.assertEqual(set(evaluations), {"H0", "H1", "H2", "H3", "H4"})
        self.assertEqual(evaluations["H0"].status, "rejected_for_multiscale_claims")
        self.assertEqual(evaluations["H1"].status, "partially_supported_but_insufficient")
        self.assertEqual(evaluations["H3"].status, "best_supported")

    def test_informative_failures_are_recorded(self) -> None:
        result = run_t25_lab()
        failures = {item.attempted_structure: item for item in result.negative_results}

        self.assertIn("scalar D1", failures)
        self.assertIn("vector D1", failures)
        self.assertIn("full IPT representation", failures)
        self.assertIn("boundary", failures["full IPT representation"].framework_boundary)

    def test_factorization_attempts_include_success_failure_and_defer(self) -> None:
        result = run_t25_lab()
        attempts = {item.name: item for item in result.factorization_attempts}

        self.assertTrue(attempts["local_quantum_redundancy_reduction"].reached)
        self.assertFalse(attempts["weak_quorum_boundary"].reached)
        self.assertEqual(attempts["weak_quorum_boundary"].obstruction, "weak_quorum")
        self.assertFalse(attempts["full_ipt_representation"].reached)

    def test_full_analysis_recommendation_is_conservative(self) -> None:
        result = run_t25_analysis()

        self.assertEqual(result["best_supported_hypothesis"], "H3")
        self.assertIn("defer full sheaf", result["recommendation"])
        self.assertIn("Retain scalar D1", result["recommendation"])


if __name__ == "__main__":
    unittest.main()
