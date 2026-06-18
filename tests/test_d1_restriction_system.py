import unittest

from models.d1_restriction_system import (
    analyze_morphism,
    analyze_transport,
    compare_systems,
    failed_transport_morphism,
    global_section,
    positive_relabel_morphism,
    run_t26_analysis,
    run_t26_lab,
    scalar_projection,
    system_from_scenario,
    validate_system,
    vector_projection,
    vector_sufficient_system,
)
from models.multiscale_observer_field import (
    connected_transport_scenario,
    contextual_gluing_scenario,
    partitioned_transport_scenario,
    uniform_broadcast_scenario,
)


class D1RestrictionSystemTests(unittest.TestCase):
    def test_validation_accepts_t25_scenarios(self) -> None:
        result = run_t26_lab()

        self.assertTrue(all(validation.valid for validation in result.validations))
        self.assertEqual(result.best_supported_hypothesis, "H1")

    def test_scalar_recovery_is_exact_for_uniform_system(self) -> None:
        system = system_from_scenario(uniform_broadcast_scenario())
        projection = scalar_projection(system, "componentwise_min")

        self.assertTrue(validate_system(system).valid)
        self.assertTrue(projection.recovered_without_loss)
        self.assertEqual(projection.profile.as_tuple(), (4, 4, 2, 3))

    def test_vector_projection_is_faithful_for_trusted_chain(self) -> None:
        system = vector_sufficient_system()
        scalar = scalar_projection(system, "componentwise_min")
        vector = vector_projection(system)
        transport = analyze_transport(system)

        self.assertTrue(vector.vector_required)
        self.assertTrue(vector.faithful_without_graph)
        self.assertIn("observer profile distribution", scalar.information_lost)
        self.assertFalse(transport.graph_data_required)

    def test_graph_is_necessary_when_same_vector_has_different_transport(self) -> None:
        connected = system_from_scenario(connected_transport_scenario())
        partitioned = system_from_scenario(partitioned_transport_scenario())
        comparison = compare_systems(connected, partitioned)

        self.assertTrue(comparison.same_vector)
        self.assertFalse(comparison.same_trusted_reachability)
        self.assertTrue(comparison.graph_information_lost_by_vector)

    def test_gluing_obstruction_is_finite_and_executable(self) -> None:
        system = system_from_scenario(contextual_gluing_scenario())
        section = global_section(system)

        self.assertTrue(section.local_patches_satisfiable)
        self.assertFalse(section.global_assignment_exists)
        self.assertTrue(section.obstruction_detected)
        self.assertEqual(section.obstruction_kind, "finite_gluing_obstruction")

    def test_morphism_checks_distinguish_preservation_from_failure(self) -> None:
        positive = analyze_morphism(positive_relabel_morphism())
        failed = analyze_morphism(failed_transport_morphism())

        self.assertTrue(positive.reached)
        self.assertEqual(positive.obstruction, "none")
        self.assertFalse(failed.reached)
        self.assertEqual(failed.obstruction, "trust_path_not_preserved")

    def test_theorem_ladder_stops_before_full_ipt_representation(self) -> None:
        result = run_t26_lab()
        ladder = {attempt.name: attempt for attempt in result.theorem_ladder}

        self.assertTrue(ladder["Minimal Axiom Sufficiency Theorem"].reached)
        self.assertTrue(ladder["Scalar Recovery Theorem"].reached)
        self.assertTrue(ladder["Vector Recovery Theorem"].reached)
        self.assertTrue(ladder["Graph Necessity Theorem"].reached)
        self.assertTrue(ladder["Gluing Obstruction Theorem"].reached)
        self.assertTrue(ladder["Restriction Morphism Theorem"].reached)
        self.assertFalse(ladder["IPT Representation Theorem"].reached)

    def test_full_analysis_is_conservative(self) -> None:
        result = run_t26_analysis()
        evaluations = {item["hypothesis_id"]: item for item in result["hypothesis_evaluations"]}

        self.assertEqual(result["best_supported_hypothesis"], "H1")
        self.assertEqual(evaluations["H1"]["status"], "best_supported")
        self.assertEqual(evaluations["H2"]["status"], "not_required_by_current_evidence")
        self.assertFalse(result["ipt_readiness"]["ready_for_full_representation"])
        self.assertIn("defer full sheaf", result["recommendation"])


if __name__ == "__main__":
    unittest.main()
