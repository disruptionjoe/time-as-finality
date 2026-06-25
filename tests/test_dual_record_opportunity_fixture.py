import unittest

from models.dual_record_opportunity_fixture import (
    BUDGET,
    CRITICAL_EDGE,
    TARGET_STATE,
    run_dual_record_opportunity_fixture,
    run_search,
)


class DualRecordOpportunityFixtureTests(unittest.TestCase):
    def test_single_record_and_limited_latent_are_trapped(self) -> None:
        single = run_search("A_single")
        limited = run_search("B0_limited_latent")

        self.assertEqual(single.final_state, 2)
        self.assertEqual(limited.final_state, 2)
        self.assertFalse(single.target_reached)
        self.assertFalse(limited.target_reached)

    def test_growing_adjacency_generates_critical_edge_and_reaches_target(self) -> None:
        growing = run_search("C_growing")

        self.assertEqual(growing.final_state, TARGET_STATE)
        self.assertTrue(growing.target_reached)
        self.assertIn(CRITICAL_EDGE, growing.generated_edges)
        self.assertEqual(growing.proposal_attempts, BUDGET)

    def test_exact_fixed_latent_absorber_reproduces_target_result(self) -> None:
        exact = run_search("B1_exact_latent")
        growing = run_search("C_growing")

        self.assertEqual(exact.final_state, growing.final_state)
        self.assertEqual(exact.best_score, growing.best_score)
        self.assertEqual(exact.proposal_attempts, growing.proposal_attempts)
        self.assertIn(CRITICAL_EDGE, exact.latent_edges_exposed)

    def test_fixture_records_bounded_residue_and_absorber(self) -> None:
        result = run_dual_record_opportunity_fixture()

        self.assertTrue(result["all_checks_passed"])
        self.assertTrue(result["comparisons"]["C_beats_A_and_B0"])
        self.assertTrue(result["comparisons"]["B1_reproduces_C_target_result"])
        self.assertTrue(
            result["absorber_verdict"][
                "exact_fixed_latent_edge_absorbs_source_side_reading"
            ]
        )

    def test_effect_verdict_is_conservative(self) -> None:
        result = run_dual_record_opportunity_fixture()

        self.assertFalse(result["effect_verdict"]["Issue[S]"])
        self.assertTrue(result["effect_verdict"]["Project[O]"])
        self.assertTrue(result["effect_verdict"]["Finalize[R]"])
        self.assertTrue(result["effect_verdict"]["Lose[K]"])
        self.assertEqual(result["absorber_verdict"]["claim_status"], "do_not_promote")


if __name__ == "__main__":
    unittest.main()
