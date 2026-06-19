"""Tests for T61 MMO reconciliation finality."""

from __future__ import annotations

import json
import unittest

from models.mmo_reconciliation_finality import (
    T61Result,
    failure_record_access_system,
    failure_witness,
    positive_record_access_system,
    positive_witness,
    run_t61_analysis,
    t61_result_to_dict,
)


_RESULT: T61Result | None = None


def _r() -> T61Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t61_analysis()
    return _RESULT


class TestT61PositiveWitness(unittest.TestCase):
    def test_positive_system_has_required_entities(self) -> None:
        system = positive_record_access_system()
        node_ids = {node.node_id for node in system.nodes}
        self.assertEqual(node_ids, {"client_a", "client_b", "edge_cache", "authority_region"})
        self.assertIsNotNone(system.boundary)
        self.assertEqual(system.boundary.member_ids, ("authority_region",))  # type: ignore[union-attr]

    def test_positive_witness_separates_apparent_and_authoritative_finality(self) -> None:
        witness = positive_witness()
        self.assertEqual(witness.classification, "reconciled_without_contradiction")
        self.assertIn("client_a:pred_move_a@1", witness.finality_answer.locally_final)
        self.assertIn("authority_region:commit_move_a@7", witness.finality_answer.authoritatively_final)
        self.assertEqual(witness.finality_answer.rolled_back, ())

    def test_positive_reconciliation_repairs_without_contradiction(self) -> None:
        witness = positive_witness()
        statuses = {(obs.observer_id, obs.event_id): obs.status for obs in witness.observations}
        self.assertEqual(statuses[("client_a", "pred_move_a")], "apparent_local_final")
        self.assertEqual(statuses[("client_a", "commit_move_a")], "reconciled_authoritative_final")
        self.assertIn("without rollback", witness.finality_answer.reconciliation_statement)

    def test_positive_reversal_cost_increases_after_commit(self) -> None:
        trace = positive_witness().finality_answer.reversal_costs[0]
        self.assertLess(trace.before_authoritative_commit, trace.after_authoritative_commit)


class TestT61FailureWitness(unittest.TestCase):
    def test_failure_system_has_conflicting_predictions_and_corrections(self) -> None:
        system = failure_record_access_system()
        event_ids = {event.event_id for event in system.events}
        self.assertTrue({"pred_claim_a", "pred_claim_b", "commit_claim_a", "rollback_claim_b"} <= event_ids)

    def test_failure_witness_requires_rollback(self) -> None:
        witness = failure_witness()
        self.assertEqual(witness.classification, "rollback_required_conflict_handled")
        self.assertIn("pred_claim_b", witness.finality_answer.rolled_back)
        self.assertIn("pred_claim_b until rollback_claim_b arrives at client_b", witness.finality_answer.predicted_only)

    def test_failure_observer_b_is_stale_when_predicting(self) -> None:
        witness = failure_witness()
        times = {
            (observer, event): arrival
            for observer, event, arrival, _status in witness.finality_answer.observer_event_times
        }
        self.assertEqual(times[("client_b", "pred_claim_b")], 2)
        self.assertEqual(times[("client_b", "pred_claim_a")], 3)

    def test_failure_conflict_reuses_t55_completion(self) -> None:
        completion = failure_witness().conflict_completion
        self.assertIsNotNone(completion)
        self.assertEqual(completion.classification, "canonical")
        self.assertTrue(completion.theorem_applies)
        self.assertTrue(completion.conflict_check.valid)  # type: ignore[union-attr]
        self.assertEqual(
            set(completion.conflict_check.conflict_pairs),  # type: ignore[union-attr]
            {("e_claim_a", "e_claim_b")},
        )

    def test_failure_authoritative_commit_makes_winner_expensive_to_reverse(self) -> None:
        traces = {trace.event_id: trace for trace in failure_witness().finality_answer.reversal_costs}
        self.assertGreater(
            traces["commit_claim_a"].after_authoritative_commit,
            traces["commit_claim_a"].before_authoritative_commit,
        )


class TestT61Integration(unittest.TestCase):
    def test_run_returns_t61_result(self) -> None:
        self.assertIsInstance(_r(), T61Result)

    def test_uses_typed_transport_without_promoting_po1(self) -> None:
        positive = _r().positive_witness.transport
        failure = _r().failure_witness.transport
        self.assertEqual(positive.verdict, "no_admissible_paths")
        self.assertEqual(failure.verdict, "no_admissible_paths")
        self.assertTrue(any("cache_freshness" in forgotten for _, forgotten in failure.accumulated_forgotten_by_path))

    def test_axis_mapping_names_required_axes(self) -> None:
        axes = {axis for axis, _meaning in _r().axis_mapping}
        self.assertEqual(
            axes,
            {
                "causal_finality",
                "information_finality",
                "observer_access_finality",
                "branch_conflict_support",
                "reversal_cost",
            },
        )

    def test_claim_classification_is_a1_not_new_claim(self) -> None:
        self.assertIn("Strengthens A1", _r().claim_classification)
        self.assertIn("does not justify a new named claim", _r().claim_classification)

    def test_serializes_to_json(self) -> None:
        data = t61_result_to_dict(_r())
        rendered = json.dumps(data)
        self.assertIn("positive_prediction_confirmed", rendered)
        self.assertIn("failure_stale_conflicting_prediction", rendered)
        self.assertIn("claim_classification", rendered)


if __name__ == "__main__":
    unittest.main()

