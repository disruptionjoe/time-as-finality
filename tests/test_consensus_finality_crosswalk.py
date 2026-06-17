import unittest

from models.consensus_finality_crosswalk import (
    ProtocolConfig,
    evaluate_config,
    generate_protocol_space,
    impossibility_witness,
    run_crosswalk_analysis,
    run_t17_analysis,
)


class ConsensusFinalityCrosswalkTests(unittest.TestCase):
    def test_safety_can_agree_while_branch_finality_differs(self) -> None:
        result = run_crosswalk_analysis()

        kinds = {witness.kind for witness in result.divergence_witnesses}
        self.assertIn("same_safety_different_branch_finality", kinds)

    def test_economic_finality_collapses_d1_dimensions(self) -> None:
        result = run_crosswalk_analysis()

        kinds = {witness.kind for witness in result.divergence_witnesses}
        self.assertIn("same_economic_cost_different_d1_profile", kinds)

    def test_standard_distributed_signature_is_less_expressive_than_d1(self) -> None:
        result = run_crosswalk_analysis()

        kinds = {witness.kind for witness in result.divergence_witnesses}
        self.assertIn("same_distributed_signature_different_d1_profile", kinds)

    def test_liveness_is_not_identical_to_d1_finality(self) -> None:
        fast = evaluate_config(
            ProtocolConfig("fast", 4, 2, 1, 1, 2, budget=10)
        )
        slow = evaluate_config(
            ProtocolConfig("slow", 4, 2, 1, 3, 3, budget=11)
        )

        self.assertTrue(fast.live_under_delay)
        self.assertFalse(slow.live_under_delay)
        self.assertLess(fast.d1.reversal_cost, slow.d1.reversal_cost)

    def test_bounded_search_finds_no_all_dimension_maximizer(self) -> None:
        evaluations = generate_protocol_space(budget=10)
        witness = impossibility_witness(evaluations, budget=10)

        self.assertEqual(
            witness.witness,
            "no admissible configuration reaches all component maxima",
        )
        self.assertGreater(len(witness.pareto_frontier), 1)

    def test_full_analysis_reports_guardrails(self) -> None:
        result = run_t17_analysis()

        self.assertTrue(result["verdict"]["distributed_finality_is_safe_analogy"])
        self.assertTrue(result["verdict"]["bounded_impossibility_witness_found"])
        self.assertTrue(result["verdict"]["physics_not_reduced_to_protocol"])


if __name__ == "__main__":
    unittest.main()
