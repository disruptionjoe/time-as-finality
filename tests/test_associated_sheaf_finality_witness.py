import unittest

from models.associated_sheaf_finality_witness import (
    EFFECTIVE_DESCENT_SUPPORT,
    TOTAL_FRAGMENTS,
    analyze_sweep,
    fixed_site,
    run_s6_goals,
)


class AssociatedSheafFinalityWitnessTests(unittest.TestCase):
    def test_g1_declares_fixed_finite_site(self) -> None:
        site = fixed_site()

        self.assertEqual(len(site.contexts), TOTAL_FRAGMENTS)
        self.assertEqual(site.cover, site.contexts)
        self.assertEqual(len(site.overlaps), 15)
        self.assertEqual(site.target_category, "finite_record_sets_with_phase_tags")
        self.assertIn("phase_sensitive_branch", site.capability_family)

    def test_g2_finds_first_effective_descent_threshold(self) -> None:
        result = run_s6_goals()

        self.assertEqual(result["threshold"]["first_effective_descent_level"], 3)
        self.assertEqual(
            result["sweep"][3]["sheafified"]["support_count"],
            EFFECTIVE_DESCENT_SUPPORT,
        )
        self.assertTrue(result["sweep"][3]["sheafified"]["stable_global_section"])

    def test_g3_redundancy_rises_and_gluing_error_falls(self) -> None:
        sweep = analyze_sweep()

        redundancies = [item.redundancy for item in sweep]
        gluing_errors = [item.gluing_error for item in sweep]
        self.assertEqual(redundancies, sorted(redundancies))
        self.assertEqual(gluing_errors, sorted(gluing_errors, reverse=True))
        self.assertLessEqual(sweep[3].gluing_error, 2 / TOTAL_FRAGMENTS)

    def test_g4_capability_non_factorization_across_eta(self) -> None:
        threshold = analyze_sweep()[3]

        self.assertIn("phase_sensitive_branch", threshold.cap_presheaf)
        self.assertNotIn("phase_sensitive_branch", threshold.cap_sheaf)
        self.assertIn("phase_sensitive_branch", threshold.loss_kernel)
        self.assertTrue(threshold.non_factorization_across_eta)

    def test_g5_temporal_provenance_reconstruction_improves(self) -> None:
        threshold = analyze_sweep()[3]

        self.assertLess(threshold.presheaf_temporal_score, threshold.sheaf_temporal_score)
        self.assertEqual(threshold.sheaf_temporal_score, 1.0)
        self.assertGreater(threshold.temporal_reconstruction_gain, 0.0)

    def test_effect_verdict_is_project_finalize_lose_not_issue(self) -> None:
        result = run_s6_goals()

        self.assertTrue(result["all_goals_passed"])
        self.assertFalse(result["effect_verdict"]["Issue[S]"])
        self.assertTrue(result["effect_verdict"]["Project[O]"])
        self.assertTrue(result["effect_verdict"]["Finalize[R]"])
        self.assertTrue(result["effect_verdict"]["Lose[K]"])
        self.assertIn("not a quantum dynamics simulation", result["guardrail"])


if __name__ == "__main__":
    unittest.main()
