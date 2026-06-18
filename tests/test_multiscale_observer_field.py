import unittest

from models.multiscale_observer_field import (
    analyze_gluing,
    analyze_scenario,
    analyze_vector,
    compare_vector_to_field,
    connected_transport_scenario,
    contextual_gluing_scenario,
    partitioned_transport_scenario,
    reduce_to_scalar,
    run_t24_analysis,
    stratified_access_scenario,
    uniform_broadcast_scenario,
)


class MultiscaleObserverFieldTests(unittest.TestCase):
    def test_uniform_broadcast_reduces_to_scalar_without_loss(self) -> None:
        scenario = uniform_broadcast_scenario()
        analysis = analyze_scenario(scenario)

        self.assertEqual(analysis.representation_needed, "scalar")
        self.assertTrue(analysis.scalar_min.recovered_without_loss)
        self.assertEqual(analysis.scalar_min.profile.as_tuple(), (4, 4, 2, 3))
        self.assertFalse(analysis.vector.vector_required)

    def test_stratified_access_requires_vector_over_observers(self) -> None:
        scenario = stratified_access_scenario()
        vector = analyze_vector(scenario)
        scalar_min = reduce_to_scalar(scenario, "componentwise_min")
        scalar_max = reduce_to_scalar(scenario, "componentwise_max")

        self.assertTrue(vector.vector_required)
        self.assertEqual(vector.distinct_profile_count, 4)
        self.assertEqual(scalar_min.profile.as_tuple(), (0, 0, 0, 0))
        self.assertEqual(scalar_max.profile.as_tuple(), (4, 3, 2, 2))
        self.assertIn("observer profile distribution", scalar_min.information_lost)

    def test_same_vector_can_have_different_field_transport(self) -> None:
        connected = connected_transport_scenario()
        partitioned = partitioned_transport_scenario()
        comparison = compare_vector_to_field(connected, partitioned)

        self.assertTrue(comparison.same_vector)
        self.assertFalse(comparison.same_transport_result)
        self.assertTrue(comparison.field_information_lost_by_vector)
        self.assertTrue(analyze_scenario(connected).transport.trust_path_exists)
        self.assertFalse(analyze_scenario(partitioned).transport.trust_path_exists)

    def test_contextual_local_patches_need_not_glue_globally(self) -> None:
        scenario = contextual_gluing_scenario()
        gluing = analyze_gluing(scenario)

        self.assertTrue(gluing.local_patches_satisfiable)
        self.assertFalse(gluing.global_assignment_exists)
        self.assertTrue(gluing.obstruction_detected)
        self.assertEqual(gluing.obstruction_kind, "contextual_finality_obstruction")

    def test_chosen_observer_scalar_declares_information_loss(self) -> None:
        scenario = stratified_access_scenario()
        scalar = reduce_to_scalar(scenario, "chosen_observer", "lab")

        self.assertEqual(scalar.profile.as_tuple(), (4, 3, 2, 2))
        self.assertFalse(scalar.recovered_without_loss)
        self.assertIn("all other observer profiles", scalar.information_lost)

    def test_full_t24_analysis_recommends_field_extension_not_replacement(self) -> None:
        result = run_t24_analysis()

        self.assertFalse(result["verdict"]["single_global_scalar_sufficient"])
        self.assertTrue(result["verdict"]["vector_d1_required_for_multiscale_snapshots"])
        self.assertTrue(result["verdict"]["field_d1_required_for_transport_and_gluing_claims"])
        self.assertTrue(result["verdict"]["scalar_d1_recoverable_as_special_case"])
        self.assertFalse(result["verdict"]["replace_existing_d1"])
        self.assertEqual(result["verdict"]["recommendation_class"], "introduce_field_extension")
        self.assertIn("Retain the existing observer-indexed D1 profile", result["recommendation"])


if __name__ == "__main__":
    unittest.main()
