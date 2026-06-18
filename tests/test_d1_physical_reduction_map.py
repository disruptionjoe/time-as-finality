import unittest

from models.d1_physical_reduction_map import (
    CONFIDENCE_LEVELS,
    D1_DIMENSIONS,
    compute_d1_profile,
    compute_darwinism_redundancy,
    d1_reduction_map,
    mutual_information_bits,
    quantum_darwinism_toy_scenario,
    run_t22_analysis,
)


class D1PhysicalReductionMapTests(unittest.TestCase):
    def test_reduction_map_covers_all_d1_dimensions(self) -> None:
        entries = d1_reduction_map()

        self.assertEqual({entry.dimension for entry in entries}, set(D1_DIMENSIONS))
        for entry in entries:
            self.assertTrue(entry.candidate_observable)
            self.assertTrue(entry.substrate_assumptions)
            self.assertTrue(entry.lorentz_frame_status)
            self.assertTrue(entry.falsification_conditions)
            self.assertIn(entry.confidence_level, CONFIDENCE_LEVELS)

    def test_toy_model_computes_pointer_fragment_information(self) -> None:
        scenario = quantum_darwinism_toy_scenario()

        self.assertAlmostEqual(mutual_information_bits(scenario, "E1"), 1.0)
        self.assertAlmostEqual(mutual_information_bits(scenario, "E2"), 1.0)
        self.assertAlmostEqual(mutual_information_bits(scenario, "E3"), 1.0)
        self.assertAlmostEqual(mutual_information_bits(scenario, "E4"), 1.0)
        self.assertAlmostEqual(mutual_information_bits(scenario, "N1"), 0.0)

    def test_holder_redundancy_matches_independence_corrected_r_delta(self) -> None:
        scenario = quantum_darwinism_toy_scenario()
        profile = compute_d1_profile(scenario)
        redundancy = compute_darwinism_redundancy(scenario)

        self.assertEqual(profile.holder_redundancy, 2)
        self.assertEqual(redundancy.independence_corrected_r_delta_accessible, 2)
        self.assertTrue(redundancy.agrees_with_d1_holder_redundancy)

    def test_raw_darwinism_fragment_count_can_exceed_d1_holder_redundancy(self) -> None:
        scenario = quantum_darwinism_toy_scenario()
        profile = compute_d1_profile(scenario)
        redundancy = compute_darwinism_redundancy(scenario)

        self.assertEqual(profile.accessible_support, 3)
        self.assertEqual(redundancy.raw_r_delta_accessible, 3)
        self.assertGreater(redundancy.raw_r_delta_accessible, profile.holder_redundancy)
        self.assertTrue(redundancy.raw_count_diverges_from_d1)
        self.assertIn("E3", redundancy.divergence_reason)

    def test_inaccessible_informative_fragment_is_not_accessible_support(self) -> None:
        scenario = quantum_darwinism_toy_scenario()
        profile = compute_d1_profile(scenario)
        redundancy = compute_darwinism_redundancy(scenario)

        self.assertNotIn("E4", scenario.observer_access)
        self.assertEqual(redundancy.raw_r_delta_total, 4)
        self.assertEqual(profile.accessible_support, 3)

    def test_branch_support_and_reversal_cost_stay_conservative(self) -> None:
        scenario = quantum_darwinism_toy_scenario()
        profile = compute_d1_profile(scenario)

        self.assertEqual(profile.branch_support, 2)
        self.assertLess(profile.branch_support, profile.accessible_support)
        self.assertEqual(profile.reversal_cost, 2)

    def test_full_analysis_reports_guardrails_and_recommendation(self) -> None:
        result = run_t22_analysis()

        self.assertTrue(result["verdict"]["all_dimensions_have_reduction_entries"])
        self.assertTrue(result["verdict"]["all_entries_have_falsification_conditions"])
        self.assertTrue(result["verdict"]["holder_redundancy_reduction_supported"])
        self.assertTrue(
            result["verdict"]["raw_fragment_count_diverges_from_holder_redundancy"]
        )
        self.assertTrue(result["verdict"]["branch_support_still_formal"])
        self.assertTrue(result["verdict"]["reversal_cost_still_formal"])
        self.assertTrue(result["verdict"]["no_universal_physical_reduction_claimed"])
        self.assertIn("does not derive D1", result["interpretation"]["guardrail"])
        self.assertIn("candidate observable program", result["interpretation"]["repo_recommendation"])


if __name__ == "__main__":
    unittest.main()
