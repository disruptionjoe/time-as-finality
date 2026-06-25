import unittest

from models.s6_g6_density_matrix_bridge import (
    DESCENT_SUPPORT,
    MI_THRESHOLD,
    analyze_strength,
    run_g6_density_matrix_bridge,
    state_vector,
)


class S6G6DensityMatrixBridgeTests(unittest.TestCase):
    def test_state_vector_is_normalized(self) -> None:
        state = state_vector(1.2)

        self.assertAlmostEqual(sum(abs(value) ** 2 for value in state), 1.0)

    def test_density_sweep_finds_redundancy_threshold(self) -> None:
        result = run_g6_density_matrix_bridge()
        threshold = result["threshold"]

        self.assertEqual(threshold["strength"], 1.2)
        self.assertEqual(threshold["redundant_count"], DESCENT_SUPPORT)
        self.assertLess(threshold["offdiag_magnitude"], 0.05)
        self.assertTrue(threshold["descent_stable"])

    def test_decoherence_and_redundancy_move_in_expected_directions(self) -> None:
        result = run_g6_density_matrix_bridge()
        sweep = result["sweep"]
        offdiags = [level["offdiag_magnitude"] for level in sweep]
        redundant_counts = [level["redundant_count"] for level in sweep]

        self.assertEqual(offdiags, sorted(offdiags, reverse=True))
        self.assertEqual(redundant_counts, sorted(redundant_counts))

    def test_fragment_mutual_information_is_density_derived(self) -> None:
        level = analyze_strength(1.2)
        redundant = [fragment for fragment in level.fragments if fragment.redundant]

        self.assertEqual(len(redundant), DESCENT_SUPPORT)
        self.assertTrue(all(fragment.mutual_information >= MI_THRESHOLD for fragment in redundant))
        self.assertTrue(all(fragment.density[0][0].real > 0 for fragment in level.fragments))

    def test_effect_verdict_remains_project_finalize_lose(self) -> None:
        result = run_g6_density_matrix_bridge()

        self.assertTrue(result["all_checks_passed"])
        self.assertFalse(result["effect_verdict"]["Issue[S]"])
        self.assertTrue(result["effect_verdict"]["Project[O]"])
        self.assertTrue(result["effect_verdict"]["Finalize[R]"])
        self.assertTrue(result["effect_verdict"]["Lose[K]"])
        self.assertIn("not a Hamiltonian", result["guardrail"])


if __name__ == "__main__":
    unittest.main()
