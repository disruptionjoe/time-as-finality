import unittest

from models.s6_g7_sbs_approximation import (
    DESCENT_SUPPORT,
    DISTINGUISHABILITY_THRESHOLD,
    SBS_CLOSURE_THRESHOLD,
    run_g7_sbs_approximation,
    sbs_level,
)


class S6G7SBSApproximationTests(unittest.TestCase):
    def test_sbs_threshold_matches_density_descent_threshold(self) -> None:
        result = run_g7_sbs_approximation()

        self.assertTrue(result["all_checks_passed"])
        self.assertEqual(result["sbs_threshold"]["strength"], 1.2)
        self.assertEqual(
            result["sbs_threshold"]["strength"],
            result["descent_threshold"]["strength"],
        )

    def test_threshold_has_enough_objective_fragments(self) -> None:
        threshold = sbs_level(1.2)

        self.assertEqual(threshold.objective_fragment_count, DESCENT_SUPPORT)
        self.assertGreaterEqual(threshold.sbs_closure_score, SBS_CLOSURE_THRESHOLD)
        self.assertTrue(threshold.sbs_objective)

    def test_objective_fragments_are_distinguishable_and_redundant(self) -> None:
        threshold = sbs_level(1.2)
        objective = [
            fragment for fragment in threshold.fragment_scores if fragment.objective_fragment
        ]

        self.assertEqual(len(objective), DESCENT_SUPPORT)
        self.assertTrue(
            all(
                fragment.conditional_distinguishability
                >= DISTINGUISHABILITY_THRESHOLD
                for fragment in objective
            )
        )
        self.assertTrue(all(fragment.redundant for fragment in objective))

    def test_pre_threshold_does_not_pass_sbs_closure(self) -> None:
        pre = sbs_level(1.0)

        self.assertFalse(pre.sbs_objective)
        self.assertLess(pre.objective_fragment_count, DESCENT_SUPPORT)

    def test_absorber_verdict_keeps_s6_as_bridge_metric(self) -> None:
        result = run_g7_sbs_approximation()

        self.assertFalse(result["effect_verdict"]["Issue[S]"])
        self.assertEqual(
            result["absorber_verdict"]["Quantum_Darwinism_or_SBS"],
            "granted_as_neighbor_absorber",
        )
        self.assertIn("does not own SBS", result["absorber_verdict"]["S6_residue"])


if __name__ == "__main__":
    unittest.main()
