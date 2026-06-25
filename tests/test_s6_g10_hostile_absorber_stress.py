import unittest

from models.s6_g10_hostile_absorber_stress import (
    run_g10_hostile_absorber_stress,
)


class S6G10HostileAbsorberStressTests(unittest.TestCase):
    def test_source_witnesses_are_imported_and_passing(self) -> None:
        result = run_g10_hostile_absorber_stress()

        self.assertTrue(result["checks"]["source_witnesses_pass"])
        self.assertTrue(result["source_summary"]["G6"]["all_checks_passed"])
        self.assertTrue(result["source_summary"]["G7"]["all_checks_passed"])
        self.assertTrue(result["source_summary"]["G8"]["all_checks_passed"])
        self.assertTrue(result["source_summary"]["G9"]["all_checks_passed"])

    def test_all_standard_absorbers_are_granted(self) -> None:
        result = run_g10_hostile_absorber_stress()

        self.assertTrue(result["checks"]["all_absorbers_granted"])
        statuses = {
            challenge["absorber"]: challenge["status"]
            for challenge in result["absorber_challenges"]
        }
        self.assertEqual(
            statuses,
            {
                "density_matrix_open_system": "granted",
                "quantum_darwinism_sbs": "granted",
                "finite_sheaf_descent": "granted",
                "resource_contextuality_task_theory": "granted",
                "distributed_provenance_event_dag": "granted",
                "fixed_source_issuance_null": "granted",
            },
        )

    def test_claim_is_not_promoted(self) -> None:
        result = run_g10_hostile_absorber_stress()

        self.assertTrue(result["checks"]["no_s6_claim_promotion"])
        self.assertEqual(result["stress_verdict"]["claim_status"], "do_not_promote")
        self.assertFalse(result["stress_verdict"]["same_neighbor_data_escape_found"])

    def test_surviving_residue_is_only_typed_bridge_workflow(self) -> None:
        result = run_g10_hostile_absorber_stress()

        self.assertTrue(result["checks"]["residue_is_bridge_workflow_only"])
        self.assertEqual(
            result["surviving_residue"]["classification"],
            "typed_bridge_workflow_only",
        )
        self.assertIn("same-SBS-data", result["surviving_residue"]["minimum_reopen_packet"])

    def test_verdict_remains_project_finalize_lose(self) -> None:
        result = run_g10_hostile_absorber_stress()

        self.assertTrue(result["all_checks_passed"])
        self.assertFalse(result["effect_verdict"]["Issue[S]"])
        self.assertTrue(result["effect_verdict"]["Project[O]"])
        self.assertTrue(result["effect_verdict"]["Finalize[R]"])
        self.assertTrue(result["effect_verdict"]["Lose[K]"])
        self.assertIn("same-neighbor-data physical capability split", result["guardrail"])


if __name__ == "__main__":
    unittest.main()
