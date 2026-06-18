"""Tests for T43: local persistence accumulation mechanism audit."""

from __future__ import annotations

import json
import unittest

from models.local_persistence_mechanisms import (
    EVENT_COUNT,
    T43Result,
    build_propagation_control,
    build_propagation_shadow_counterexample,
    combined_effects_case,
    interaction_density_mechanism_case,
    interaction_density_trace,
    intrinsic_mechanism_case,
    intrinsic_stabilization_trace,
    resource_budget_mechanism_case,
    resource_budget_trace,
    run_t43_analysis,
    search_equivalent_parameterizations,
    t43_result_to_dict,
)


_RESULT: T43Result | None = None


def _r() -> T43Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t43_analysis()
    return _RESULT


class TestMechanismTraceGenerators(unittest.TestCase):
    def test_intrinsic_trace_total(self) -> None:
        trace = intrinsic_stabilization_trace("fast", rate=2)
        self.assertEqual(trace.total_accumulation, 20)
        self.assertEqual(trace.deltas, tuple(2 for _ in range(EVENT_COUNT)))

    def test_intrinsic_trace_independent_of_propagation(self) -> None:
        trace = intrinsic_stabilization_trace("fast", rate=2)
        self.assertFalse(trace.depends_on_propagation)

    def test_resource_budget_caps_delta(self) -> None:
        trace = resource_budget_trace("limited", update_demand=3, stabilization_budget=1)
        self.assertEqual(trace.deltas, tuple(1 for _ in range(EVENT_COUNT)))
        self.assertEqual(trace.total_accumulation, 10)

    def test_resource_budget_full_capacity(self) -> None:
        trace = resource_budget_trace("full", update_demand=2, stabilization_budget=2)
        self.assertEqual(trace.total_accumulation, 20)

    def test_interaction_density_trace(self) -> None:
        trace = interaction_density_trace(
            "dense",
            base_rate=1,
            coupling_strength=2,
            interaction_count=3,
        )
        self.assertEqual(trace.deltas, tuple(7 for _ in range(EVENT_COUNT)))

    def test_interaction_density_independent_of_propagation(self) -> None:
        trace = interaction_density_trace("dense", base_rate=1, coupling_strength=1, interaction_count=1)
        self.assertFalse(trace.depends_on_propagation)


class TestMechanismCases(unittest.TestCase):
    def test_intrinsic_case_produces_difference_without_delay(self) -> None:
        case = intrinsic_mechanism_case()
        self.assertEqual(case.verdict, "supported")
        self.assertEqual(case.observation.reconciliation_lag_events, 0)
        self.assertNotEqual(case.observation.local_accumulation_difference, 0)

    def test_resource_case_produces_difference_without_delay(self) -> None:
        case = resource_budget_mechanism_case()
        self.assertEqual(case.verdict, "supported")
        self.assertEqual(case.observation.reconciliation_lag_events, 0)
        self.assertEqual(case.observation.local_accumulation_difference, 10)

    def test_interaction_case_produces_difference_without_delay(self) -> None:
        case = interaction_density_mechanism_case()
        self.assertEqual(case.verdict, "supported")
        self.assertEqual(case.observation.reconciliation_lag_events, 0)
        self.assertEqual(case.observation.local_accumulation_difference, 10)

    def test_combined_case_has_difference_and_lag(self) -> None:
        case = combined_effects_case()
        self.assertNotEqual(case.observation.local_accumulation_difference, 0)
        self.assertGreater(case.observation.reconciliation_lag_events, 0)

    def test_mechanisms_preserve_t42_split_when_delay_zero(self) -> None:
        cases = (
            intrinsic_mechanism_case(),
            resource_budget_mechanism_case(),
            interaction_density_mechanism_case(),
        )
        self.assertTrue(all(case.preserves_t42_split for case in cases))


class TestPropagationControls(unittest.TestCase):
    def test_varying_propagation_changes_lag_not_accumulation(self) -> None:
        control = build_propagation_control()
        self.assertFalse(control.accumulation_difference_changed)
        self.assertTrue(control.reconciliation_lag_changed)
        self.assertIn("pass", control.verdict)

    def test_zero_delay_control_has_zero_lag(self) -> None:
        control = build_propagation_control()
        self.assertEqual(control.zero_delay_observation.reconciliation_lag_events, 0)

    def test_delayed_control_has_positive_lag(self) -> None:
        control = build_propagation_control()
        self.assertGreater(control.delayed_observation.reconciliation_lag_events, 0)

    def test_propagation_shadow_eliminated(self) -> None:
        shadow = build_propagation_shadow_counterexample()
        self.assertTrue(shadow.eliminated)

    def test_propagation_shadow_no_difference_when_topology_fixed(self) -> None:
        shadow = build_propagation_shadow_counterexample()
        self.assertFalse(shadow.fixed_topology_produces_difference)

    def test_propagation_shadow_difference_only_when_topology_varies(self) -> None:
        shadow = build_propagation_shadow_counterexample()
        self.assertTrue(shadow.varied_topology_produces_difference)


class TestEquivalenceSearch(unittest.TestCase):
    def test_equivalence_classes_found(self) -> None:
        classes = search_equivalent_parameterizations()
        self.assertGreaterEqual(len(classes), 1)

    def test_equivalence_class_has_multiple_members(self) -> None:
        classes = search_equivalent_parameterizations()
        self.assertTrue(any(len(eq.members) >= 3 for eq in classes))

    def test_equivalence_includes_intrinsic_resource_interaction(self) -> None:
        classes = search_equivalent_parameterizations()
        joined = tuple(member for eq in classes for member in eq.members)
        self.assertIn("intrinsic_rate_2", joined)
        self.assertIn("resource_demand_2_budget_2", joined)
        self.assertIn("interaction_base_1_coupling_1_count_1", joined)


class TestT43Analysis(unittest.TestCase):
    def test_run_returns_t43_result(self) -> None:
        self.assertIsInstance(_r(), T43Result)

    def test_has_at_least_three_mechanism_cases(self) -> None:
        self.assertGreaterEqual(len(_r().mechanism_cases), 3)

    def test_hypotheses_cover_h0_to_h5(self) -> None:
        ids = {h.hypothesis_id for h in _r().hypothesis_evaluations}
        self.assertEqual(ids, {"H0", "H1", "H2", "H3", "H4", "H5"})

    def test_best_supported_is_h4(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H4")

    def test_h0_rejected(self) -> None:
        h0 = [h for h in _r().hypothesis_evaluations if h.hypothesis_id == "H0"][0]
        self.assertEqual(h0.status, "rejected")

    def test_h4_best_supported(self) -> None:
        h4 = [h for h in _r().hypothesis_evaluations if h.hypothesis_id == "H4"][0]
        self.assertEqual(h4.status, "best_supported")

    def test_minimal_extension_does_not_modify_d1(self) -> None:
        self.assertIn("Do not modify D1RestrictionSystem", _r().minimal_extension)

    def test_serializes_to_json(self) -> None:
        data = t43_result_to_dict(_r())
        rendered = json.dumps(data)
        self.assertIn("mechanism_cases", rendered)
        self.assertIn("Finite Local Mechanism Equivalence", rendered)


if __name__ == "__main__":
    unittest.main()
