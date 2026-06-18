"""Tests for T44: local mechanism identifiability audit."""

from __future__ import annotations

import json
import unittest

from models.local_mechanism_identifiability import (
    MECHANISMS,
    T44Result,
    baseline_trace,
    build_probe_results,
    evaluate_probe,
    evaluate_probe_suite,
    find_minimal_basis,
    response_for_probe,
    run_t44_analysis,
    t44_result_to_dict,
    trace_for_probe,
)


_RESULT: T44Result | None = None


def _r() -> T44Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t44_analysis()
    return _RESULT


class TestTraceGeneration(unittest.TestCase):
    def test_baseline_traces_are_equivalent(self) -> None:
        signatures = {baseline_trace(mechanism).deltas for mechanism in MECHANISMS}
        self.assertEqual(len(signatures), 1)

    def test_event_count_scaling_preserves_equivalence(self) -> None:
        signatures = {trace_for_probe(mechanism, "event_count_scaling").deltas for mechanism in MECHANISMS}
        self.assertEqual(len(signatures), 1)

    def test_demand_drop_changes_resource_only(self) -> None:
        intrinsic = trace_for_probe("intrinsic_rate", "demand_drop")
        resource = trace_for_probe("resource_budget", "demand_drop")
        interaction = trace_for_probe("interaction_density", "demand_drop")
        self.assertNotEqual(resource.deltas, intrinsic.deltas)
        self.assertEqual(intrinsic.deltas, interaction.deltas)

    def test_resource_shock_changes_resource_only(self) -> None:
        intrinsic = trace_for_probe("intrinsic_rate", "resource_shock")
        resource = trace_for_probe("resource_budget", "resource_shock")
        interaction = trace_for_probe("interaction_density", "resource_shock")
        self.assertNotEqual(resource.deltas, intrinsic.deltas)
        self.assertEqual(intrinsic.deltas, interaction.deltas)

    def test_coupling_rewire_changes_interaction_only(self) -> None:
        intrinsic = trace_for_probe("intrinsic_rate", "coupling_rewire")
        resource = trace_for_probe("resource_budget", "coupling_rewire")
        interaction = trace_for_probe("interaction_density", "coupling_rewire")
        self.assertNotEqual(interaction.deltas, intrinsic.deltas)
        self.assertEqual(intrinsic.deltas, resource.deltas)

    def test_response_changed_from_baseline(self) -> None:
        response = response_for_probe("resource_budget", "demand_drop")
        self.assertTrue(response.changed_from_baseline)

    def test_intrinsic_response_stable_under_demand_drop(self) -> None:
        response = response_for_probe("intrinsic_rate", "demand_drop")
        self.assertFalse(response.changed_from_baseline)


class TestProbeProtocolResults(unittest.TestCase):
    def test_baseline_separates_no_pairs(self) -> None:
        result = evaluate_probe("baseline", "baseline")
        self.assertFalse(result.separates_all)
        self.assertEqual(len(result.separated_pairs), 0)
        self.assertEqual(len(result.unresolved_pairs), 3)

    def test_demand_drop_separates_resource_from_two_pairs(self) -> None:
        result = evaluate_probe("demand_drop", "demand drop")
        self.assertIn(("intrinsic_rate", "resource_budget"), result.separated_pairs)
        self.assertIn(("resource_budget", "interaction_density"), result.separated_pairs)
        self.assertIn(("intrinsic_rate", "interaction_density"), result.unresolved_pairs)

    def test_coupling_rewire_separates_interaction_from_two_pairs(self) -> None:
        result = evaluate_probe("coupling_rewire", "coupling rewire")
        self.assertIn(("intrinsic_rate", "interaction_density"), result.separated_pairs)
        self.assertIn(("resource_budget", "interaction_density"), result.separated_pairs)
        self.assertIn(("intrinsic_rate", "resource_budget"), result.unresolved_pairs)

    def test_resource_shock_redundant_with_demand_drop_for_pair_structure(self) -> None:
        demand = evaluate_probe("demand_drop", "demand drop")
        shock = evaluate_probe("resource_shock", "resource shock")
        self.assertEqual(demand.separated_pairs, shock.separated_pairs)

    def test_probe_results_include_six_protocols(self) -> None:
        results = build_probe_results()
        self.assertEqual(len(results), 6)


class TestMinimalBasis(unittest.TestCase):
    def test_demand_drop_plus_coupling_rewire_separates_all(self) -> None:
        basis = find_minimal_basis(("demand_drop", "coupling_rewire", "resource_shock"))
        self.assertTrue(basis.separates_all)
        self.assertEqual(basis.probe_names, ("demand_drop", "coupling_rewire"))

    def test_single_demand_probe_does_not_separate_all(self) -> None:
        pair_results = evaluate_probe_suite(("demand_drop",))
        unresolved = tuple(item.pair for item in pair_results if not item.separated)
        self.assertIn(("intrinsic_rate", "interaction_density"), unresolved)

    def test_single_coupling_probe_does_not_separate_all(self) -> None:
        pair_results = evaluate_probe_suite(("coupling_rewire",))
        unresolved = tuple(item.pair for item in pair_results if not item.separated)
        self.assertIn(("intrinsic_rate", "resource_budget"), unresolved)

    def test_event_count_scaling_basis_fails(self) -> None:
        basis = find_minimal_basis(("event_count_scaling",))
        self.assertFalse(basis.separates_all)
        self.assertEqual(len(basis.unresolved_pairs), 3)


class TestT44Analysis(unittest.TestCase):
    def test_run_returns_t44_result(self) -> None:
        self.assertIsInstance(_r(), T44Result)

    def test_best_supported_hypothesis_is_h4(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H4")

    def test_hypotheses_cover_h0_to_h5(self) -> None:
        ids = {h.hypothesis_id for h in _r().hypothesis_evaluations}
        self.assertEqual(ids, {"H0", "H1", "H2", "H3", "H4", "H5"})

    def test_h0_rejected(self) -> None:
        h0 = [h for h in _r().hypothesis_evaluations if h.hypothesis_id == "H0"][0]
        self.assertEqual(h0.status, "rejected")

    def test_h4_best_supported(self) -> None:
        h4 = [h for h in _r().hypothesis_evaluations if h.hypothesis_id == "H4"][0]
        self.assertEqual(h4.status, "best_supported")

    def test_unresolved_equivalences_preserved(self) -> None:
        self.assertGreaterEqual(len(_r().unresolved_equivalences), 1)

    def test_theorem_mentions_two_probe_basis(self) -> None:
        self.assertIn("two-probe", _r().theorem)

    def test_serializes_to_json(self) -> None:
        data = t44_result_to_dict(_r())
        rendered = json.dumps(data)
        self.assertIn("probe_results", rendered)
        self.assertIn("Finite Probe Identifiability", rendered)


if __name__ == "__main__":
    unittest.main()
