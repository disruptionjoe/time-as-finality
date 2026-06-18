"""Tests for T42: local persistence and reconciliation split audit."""

from __future__ import annotations

import json
import unittest

from models.local_persistence_reconciliation import (
    ComparisonObservation,
    LocalPersistenceReconciliationSystem,
    T42Result,
    accumulation_until,
    both_effects_system,
    classify_observation,
    delay_without_dilation_system,
    dilation_like_without_delay_system,
    latest_visible_source_index,
    make_node,
    make_uniform_node,
    null_case_system,
    observe_comparison,
    run_t42_analysis,
    t42_result_to_dict,
)


_RESULT: T42Result | None = None


def _r() -> T42Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t42_analysis()
    return _RESULT


class TestNodeConstruction(unittest.TestCase):
    def test_uniform_node_has_requested_event_count(self) -> None:
        node = make_uniform_node("n", 5, 1)
        self.assertEqual(node.event_count, 5)

    def test_uniform_node_accumulates(self) -> None:
        node = make_uniform_node("n", 5, 2)
        self.assertEqual(accumulation_until(node, 5), 10)

    def test_sparse_node_accumulates_deltas(self) -> None:
        node = make_node("n", (1, 0, 1, 0, 1))
        self.assertEqual(accumulation_until(node, 5), 3)

    def test_accumulation_until_zero_is_zero(self) -> None:
        node = make_uniform_node("n", 5, 1)
        self.assertEqual(accumulation_until(node, 0), 0)

    def test_accumulation_rejects_out_of_range_index(self) -> None:
        node = make_uniform_node("n", 5, 1)
        with self.assertRaises(ValueError):
            accumulation_until(node, 6)


class TestVisibilityAndClassification(unittest.TestCase):
    def test_latest_visible_source_index_respects_delay(self) -> None:
        system = delay_without_dilation_system()
        comparison = system.comparisons[0]
        channel = system.channels[0]
        visible = latest_visible_source_index(
            comparison.source_local_index,
            comparison.target_local_index,
            channel,
        )
        self.assertEqual(visible, 6)

    def test_latest_visible_source_index_caps_at_source_index(self) -> None:
        system = null_case_system()
        comparison = system.comparisons[0]
        channel = system.channels[0]
        visible = latest_visible_source_index(
            comparison.source_local_index,
            comparison.target_local_index + 100,
            channel,
        )
        self.assertEqual(visible, comparison.source_local_index)

    def test_classifies_delay_without_dilation(self) -> None:
        self.assertEqual(classify_observation(0, 3), "delay_without_dilation")

    def test_classifies_dilation_like_without_delay(self) -> None:
        self.assertEqual(
            classify_observation(4, 0),
            "dilation_like_accumulation_without_extra_delay",
        )

    def test_classifies_both_effects(self) -> None:
        self.assertEqual(classify_observation(4, 3), "both_effects")

    def test_classifies_null_case(self) -> None:
        self.assertEqual(classify_observation(0, 0), "null_case")


class TestScenarioWitnesses(unittest.TestCase):
    def _observe(self, system: LocalPersistenceReconciliationSystem) -> ComparisonObservation:
        return observe_comparison(system, system.comparisons[0])

    def test_delay_without_dilation_has_lag_but_no_accumulation_difference(self) -> None:
        obs = self._observe(delay_without_dilation_system())
        self.assertEqual(obs.classification, "delay_without_dilation")
        self.assertEqual(obs.local_accumulation_difference, 0)
        self.assertGreater(obs.reconciliation_lag_events, 0)

    def test_delay_without_dilation_same_total_accumulation(self) -> None:
        obs = self._observe(delay_without_dilation_system())
        self.assertEqual(obs.source_total_accumulation, obs.target_total_accumulation)

    def test_dilation_like_without_delay_has_accumulation_difference_but_no_lag(self) -> None:
        obs = self._observe(dilation_like_without_delay_system())
        self.assertEqual(obs.classification, "dilation_like_accumulation_without_extra_delay")
        self.assertNotEqual(obs.local_accumulation_difference, 0)
        self.assertEqual(obs.reconciliation_lag_events, 0)

    def test_dilation_like_without_delay_rates_differ(self) -> None:
        obs = self._observe(dilation_like_without_delay_system())
        self.assertGreater(obs.source_local_rate, obs.target_local_rate)

    def test_both_effects_has_both_axes(self) -> None:
        obs = self._observe(both_effects_system())
        self.assertEqual(obs.classification, "both_effects")
        self.assertNotEqual(obs.local_accumulation_difference, 0)
        self.assertGreater(obs.reconciliation_lag_events, 0)

    def test_null_case_has_neither_axis(self) -> None:
        obs = self._observe(null_case_system())
        self.assertEqual(obs.classification, "null_case")
        self.assertEqual(obs.local_accumulation_difference, 0)
        self.assertEqual(obs.reconciliation_lag_events, 0)

    def test_delay_hides_source_accumulation(self) -> None:
        obs = self._observe(delay_without_dilation_system())
        self.assertEqual(obs.hidden_source_accumulation_due_to_delay, 4)

    def test_no_delay_hides_no_source_accumulation(self) -> None:
        obs = self._observe(dilation_like_without_delay_system())
        self.assertEqual(obs.hidden_source_accumulation_due_to_delay, 0)


class TestT42Analysis(unittest.TestCase):
    def test_run_returns_result(self) -> None:
        self.assertIsInstance(_r(), T42Result)

    def test_four_scenarios_present(self) -> None:
        self.assertEqual(len(_r().scenarios), 4)

    def test_all_witnesses_pass(self) -> None:
        self.assertTrue(_r().all_witnesses_pass)

    def test_independence_witnessed(self) -> None:
        self.assertTrue(_r().independence_witnessed)

    def test_best_supported_hypothesis_is_h2(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H2")

    def test_hypotheses_cover_h0_to_h4(self) -> None:
        ids = {h.hypothesis_id for h in _r().hypothesis_evaluations}
        self.assertEqual(ids, {"H0", "H1", "H2", "H3", "H4"})

    def test_h2_best_supported(self) -> None:
        h2 = [h for h in _r().hypothesis_evaluations if h.hypothesis_id == "H2"][0]
        self.assertEqual(h2.status, "best_supported")

    def test_h3_not_earned(self) -> None:
        h3 = [h for h in _r().hypothesis_evaluations if h.hypothesis_id == "H3"][0]
        self.assertEqual(h3.status, "not_earned")

    def test_serializes_to_json(self) -> None:
        data = t42_result_to_dict(_r())
        rendered = json.dumps(data)
        self.assertIn("scenarios", rendered)
        self.assertIn("Finite Accumulation/Reconciliation Independence", rendered)


if __name__ == "__main__":
    unittest.main()
