"""Unit tests for T17: persistent dynamical reconciler."""

from __future__ import annotations

import unittest

from models.t17_persistent_reconciler import (
    evaluate,
    failure_without_persistence,
    finality_profile,
    generated_access_boundary,
    internal_records,
    intervention_profile,
    run_t17_analysis,
    sweep_reconciler,
)


class PersistentDynamicalReconcilerTests(unittest.TestCase):
    def test_memory_records_persist_after_sensor_write(self) -> None:
        run = evaluate(1, 1)
        propositions = {record.proposition for record in run.records}
        self.assertIn("A", propositions)
        self.assertIn("B", propositions)
        self.assertGreaterEqual(
            min(record.persisted_steps for record in run.records if record.proposition in {"A", "B"}),
            3,
        )

    def test_access_boundary_is_generated_by_wiring(self) -> None:
        run = evaluate(1, 1)
        self.assertEqual(
            run.access_boundary,
            frozenset({"memory:A", "memory:B", "comparator"}),
        )
        self.assertEqual(generated_access_boundary(run.history), run.access_boundary)

    def test_reconciler_compares_two_records(self) -> None:
        equal = evaluate(1, 1)
        unequal = evaluate(1, 0)
        self.assertEqual(equal.decision, "true")
        self.assertEqual(unequal.decision, "false")
        self.assertEqual(equal.finality_profiles["A=B"][0], 1)

    def test_finality_profile_uses_internal_records(self) -> None:
        records = internal_records(evaluate(1, 1).history)
        self.assertEqual(finality_profile(records, "A"), (1, 1, 1, 5))
        self.assertEqual(finality_profile(records, "B"), (1, 1, 1, 5))
        self.assertEqual(finality_profile(records, "A=B"), (1, 1, 1, 5))

    def test_interventions_change_internal_decision(self) -> None:
        flip_a = intervention_profile(1, 1, "env_a")
        flip_b = intervention_profile(1, 1, "env_b")
        self.assertTrue(flip_a["decision_changed"])
        self.assertTrue(flip_b["decision_changed"])
        self.assertEqual(flip_a["baseline_boundary"], flip_a["changed_boundary"])

    def test_without_persistence_control_fails_at_final_state(self) -> None:
        control = failure_without_persistence()
        self.assertEqual(control["records_at_final_state"], 0)
        self.assertIsNone(control["decision_at_final_state"])
        self.assertTrue(control["persistent_reconciler_required"])

    def test_sweep_covers_equal_and_unequal_cases(self) -> None:
        summary = sweep_reconciler()
        self.assertEqual(summary["cases"], 4)
        self.assertEqual(summary["comparison_fraction"], 1.0)
        self.assertEqual(summary["true_decision_count"], 2)
        self.assertEqual(summary["false_decision_count"], 2)

    def test_full_analysis_states_guardrails(self) -> None:
        result = run_t17_analysis()
        self.assertTrue(result["verdict"]["storage_arises_inside_dynamics"])
        self.assertTrue(result["verdict"]["access_boundary_is_generated"])
        self.assertTrue(result["verdict"]["consciousness_not_modeled"])


if __name__ == "__main__":
    unittest.main()
