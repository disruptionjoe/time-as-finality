import unittest

from models.quantum_measurement_finality import (
    POINTER_BASIS,
    run_measurement_finality_lab,
    run_t2_analysis,
)


class QuantumMeasurementFinalityTests(unittest.TestCase):
    def test_pointer_basis_and_unitary_guardrail_are_explicit(self) -> None:
        result = run_measurement_finality_lab()

        self.assertEqual(result.pointer_basis, POINTER_BASIS)
        self.assertEqual(result.pointer_basis, "computational_z")
        self.assertTrue(result.verdict["unitary_dynamics_only_no_collapse"])
        self.assertTrue(result.verdict["pointer_basis_explicit"])

    def test_decoherence_occurs_after_first_environment_copy(self) -> None:
        result = run_measurement_finality_lab()

        self.assertEqual(result.stages[0].name, "measurement_cnot_S_to_A")
        self.assertAlmostEqual(result.stages[0].pointer_coherence_abs, 0.5)
        self.assertEqual(result.stages[1].name, "decoherence_copy_A_to_E1")
        self.assertAlmostEqual(result.stages[1].pointer_coherence_abs, 0.0)
        self.assertTrue(result.verdict["decoherence_occurs_after_environment_copy"])

    def test_environment_redundancy_grows_from_dynamic_copy_steps(self) -> None:
        result = run_measurement_finality_lab()

        self.assertEqual(
            [stage.environment_r_delta_total for stage in result.stages],
            [0, 1, 2, 3],
        )
        final_information = result.stages[-1].fragment_information_bits
        self.assertAlmostEqual(final_information["A"], 1.0)
        self.assertAlmostEqual(final_information["E1"], 1.0)
        self.assertAlmostEqual(final_information["E2"], 1.0)
        self.assertAlmostEqual(final_information["E3"], 1.0)

    def test_observer_access_changes_d1_profiles_after_same_decoherence(self) -> None:
        result = run_measurement_finality_lab()
        final_stage = result.stages[-1]
        profiles = {
            observer.observer.name: observer.d1_profile.as_tuple()
            for observer in final_stage.observers
        }

        self.assertEqual(profiles["apparatus_observer"], (1, 1, 1, 1))
        self.assertEqual(profiles["local_lab_observer"], (2, 2, 1, 1))
        self.assertEqual(profiles["remote_environment_observer"], (2, 2, 1, 1))
        self.assertEqual(profiles["outside_observer"], (0, 0, 0, 0))
        self.assertTrue(result.verdict["d1_profiles_depend_on_observer_access"])

    def test_decohered_but_inaccessible_case_is_detected(self) -> None:
        result = run_measurement_finality_lab()
        final_stage = result.stages[-1]
        outside = next(
            observer
            for observer in final_stage.observers
            if observer.observer.name == "outside_observer"
        )

        self.assertAlmostEqual(final_stage.pointer_coherence_abs, 0.0)
        self.assertEqual(final_stage.environment_r_delta_total, 3)
        self.assertEqual(outside.d1_profile.as_tuple(), (0, 0, 0, 0))
        self.assertTrue(result.verdict["decohered_but_inaccessible_case_detected"])

    def test_redundancy_can_exceed_branch_support(self) -> None:
        result = run_measurement_finality_lab()
        final_stage = result.stages[-1]
        local_lab = next(
            observer
            for observer in final_stage.observers
            if observer.observer.name == "local_lab_observer"
        )

        self.assertEqual(final_stage.environment_r_delta_total, 3)
        self.assertEqual(local_lab.d1_profile.holder_redundancy, 2)
        self.assertEqual(local_lab.d1_profile.branch_support, 1)
        self.assertTrue(result.verdict["redundancy_exceeds_branch_support"])

    def test_full_analysis_reports_claim_recommendation(self) -> None:
        analysis = run_t2_analysis()

        self.assertTrue(analysis["verdict"]["q1_adds_observer_access_distinction"])
        self.assertIn("Keep Q1 partially supported", analysis["interpretation"]["claim_recommendation"])
        self.assertIn("never selects a collapse outcome", analysis["interpretation"]["guardrail"])


if __name__ == "__main__":
    unittest.main()
