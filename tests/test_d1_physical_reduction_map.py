import unittest

from models.d1_physical_reduction_map import (
    D1_DIMENSIONS,
    compute_d1_profile,
    compute_darwinism_redundancy,
    d1_reduction_map,
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
            self.assertTrue(entry.frame_status)
            self.assertTrue(entry.falsification_condition)

    def test_holder_redundancy_matches_independent_darwinism_fragments(self) -> None:
        scenario = quantum_darwinism_toy_scenario()
        profile = compute_d1_profile(scenario)
        redundancy = compute_darwinism_redundancy(scenario)

        self.assertEqual(profile.holder_redundancy, 2)
        self.assertEqual(redundancy.independent_informative_fragments, 2)
        self.assertTrue(redundancy.agrees_with_d1_holder_redundancy)

    def test_raw_informative_fragments_can_exceed_holder_redundancy(self) -> None:
        scenario = quantum_darwinism_toy_scenario()
        profile = compute_d1_profile(scenario)
        redundancy = compute_darwinism_redundancy(scenario)

        self.assertEqual(profile.accessible_support, 3)
        self.assertEqual(redundancy.raw_informative_fragment_count, 3)
        self.assertGreater(
            redundancy.raw_informative_fragment_count,
            profile.holder_redundancy,
        )
        self.assertTrue(redundancy.raw_count_diverges_from_d1)
        self.assertIn("correlated", redundancy.divergence_reason)

    def test_inaccessible_informative_fragment_is_not_accessible_support(self) -> None:
        scenario = quantum_darwinism_toy_scenario()
        profile = compute_d1_profile(scenario)
        total_informative = sum(
            1 for fragment in scenario.fragments if fragment.encodes_system
        )

        self.assertNotIn("E4", scenario.observer_access)
        self.assertEqual(total_informative, 4)
        self.assertEqual(profile.accessible_support, 3)
        self.assertEqual(profile.reversal_cost, 4)

    def test_branch_support_counts_independent_channels_not_raw_holders(self) -> None:
        scenario = quantum_darwinism_toy_scenario()
        profile = compute_d1_profile(scenario)

        self.assertEqual(profile.branch_support, 2)
        self.assertLess(profile.branch_support, profile.accessible_support)

    def test_full_analysis_reports_guardrails(self) -> None:
        result = run_t22_analysis()

        self.assertTrue(result["verdict"]["all_dimensions_have_reduction_entries"])
        self.assertTrue(result["verdict"]["holder_redundancy_reduction_supported"])
        self.assertTrue(
            result["verdict"]["raw_fragment_count_diverges_from_holder_redundancy"]
        )
        self.assertTrue(result["verdict"]["reversal_cost_still_open"])
        self.assertTrue(result["verdict"]["no_universal_physical_reduction_claimed"])
        self.assertIn("does not derive D1", result["interpretation"]["guardrail"])


if __name__ == "__main__":
    unittest.main()
