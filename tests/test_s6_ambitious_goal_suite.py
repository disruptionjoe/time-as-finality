import unittest

from models.s6_ambitious_goal_suite import (
    DESCENT_SUPPORT,
    MI_THRESHOLD,
    contextual_capability_check,
    finite_descent,
    first_redundancy_threshold,
    local_records_from_open_system,
    provenance_reconstruction_check,
    run_all_ambitious_goals,
    run_open_system_sweep,
)


class S6AmbitiousGoalSuiteTests(unittest.TestCase):
    def test_g1_open_system_style_redundancy_threshold(self) -> None:
        sweep = run_open_system_sweep()
        threshold = first_redundancy_threshold(sweep)

        redundant_counts = [level.redundant_count for level in sweep]
        coherences = [level.coherence for level in sweep]
        self.assertEqual(redundant_counts, sorted(redundant_counts))
        self.assertEqual(coherences, sorted(coherences, reverse=True))
        self.assertEqual(threshold.strength, 1.2)
        self.assertEqual(threshold.redundant_count, DESCENT_SUPPORT)
        self.assertLess(threshold.coherence, 0.01)

    def test_g2_general_descent_stabilizes_record(self) -> None:
        threshold = first_redundancy_threshold(run_open_system_sweep())
        records = local_records_from_open_system(threshold)
        descent = finite_descent(records)

        self.assertTrue(descent.stable)
        self.assertEqual(descent.pointer, 1)
        self.assertEqual(descent.support_count, DESCENT_SUPPORT)
        self.assertIn("phase_sensitive_branch", descent.eta_loss)

    def test_g3_chsh_capability_non_factorization(self) -> None:
        contextual = contextual_capability_check()

        self.assertTrue(contextual.non_factorization)
        self.assertGreater(
            contextual.presheaf_chsh_score,
            contextual.final_record_chsh_bound,
        )
        self.assertIn("contextual_chsh_above_classical", contextual.cap_presheaf)
        self.assertNotIn(
            "contextual_chsh_above_classical",
            contextual.cap_final_record,
        )

    def test_g4_provenance_reconstruction_gain_not_smuggled(self) -> None:
        threshold = first_redundancy_threshold(run_open_system_sweep())
        records = local_records_from_open_system(threshold)
        descent = finite_descent(records)
        provenance = provenance_reconstruction_check(records, descent)

        self.assertGreater(provenance.reconstruction_gain, 0.0)
        self.assertEqual(provenance.descent_score, 1.0)
        self.assertEqual(provenance.unlabeled_control_score, 0.0)
        self.assertTrue(provenance.not_smuggled_by_site)

    def test_g5_absorber_gauntlet_blocks_claim_promotion(self) -> None:
        result = run_all_ambitious_goals()

        self.assertTrue(result["all_goals_passed"])
        self.assertFalse(result["effect_verdict"]["Issue[S]"])
        self.assertTrue(result["effect_verdict"]["Project[O]"])
        self.assertTrue(result["effect_verdict"]["Finalize[R]"])
        self.assertTrue(result["effect_verdict"]["Lose[K]"])
        self.assertTrue(all(check["granted"] for check in result["G5_absorbers"]))
        self.assertEqual(result["parameters"]["mutual_information_threshold"], MI_THRESHOLD)


if __name__ == "__main__":
    unittest.main()
