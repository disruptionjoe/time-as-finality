"""Tests for T46: open causal scarcity and closed synchronization boundary."""

from __future__ import annotations

import json
import unittest

from models.record_access_systems import (
    BoundaryComparison,
    ClosedSynchronizationResult,
    MeasurementProjectionBoundary,
    OpenCausalScarcityResult,
    RecordAccessSystem,
    T46Result,
    compare_boundaries,
    evaluate_closed_synchronization_boundary,
    evaluate_open_causal_scarcity,
    measurement_projection_boundary,
    nyse_style_open_system,
    run_t46_analysis,
    spanner_style_closed_system,
    t46_result_to_dict,
)
from models.run_t46 import render_markdown


_RESULT: T46Result | None = None


def _r() -> T46Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t46_analysis()
    return _RESULT


class TestOpenCausalScarcity(unittest.TestCase):
    def test_nyse_style_system_is_record_access_system(self) -> None:
        system = nyse_style_open_system()
        self.assertIsInstance(system, RecordAccessSystem)
        self.assertIsNone(system.boundary)

    def test_shortest_delays_follow_open_paths(self) -> None:
        system = nyse_style_open_system()
        distances = system.shortest_delays_from("exchange_engine")
        self.assertEqual(distances["colocated_rack"], 1)
        self.assertEqual(distances["metro_pop"], 75)
        self.assertEqual(distances["remote_region"], 750)

    def test_first_access_order_is_proximity_driven(self) -> None:
        result = evaluate_open_causal_scarcity()
        self.assertIsInstance(result, OpenCausalScarcityResult)
        self.assertEqual(
            result.first_access_order,
            ("colocated_rack", "metro_pop", "remote_region"),
        )
        self.assertTrue(result.proximity_driven)

    def test_open_gradient_records_advantage(self) -> None:
        result = evaluate_open_causal_scarcity()
        by_observer = {item.observer_id: item for item in result.gradient}
        self.assertEqual(by_observer["colocated_rack"].advantage_over_slowest, 749)
        self.assertEqual(by_observer["remote_region"].advantage_over_slowest, 0)
        self.assertEqual(result.proximity_advantage, 749)

    def test_open_observations_are_causal_arrivals(self) -> None:
        result = evaluate_open_causal_scarcity()
        self.assertTrue(all(item.access_mode == "causal_arrival" for item in result.observations))
        self.assertTrue(all(not item.inside_boundary for item in result.observations))


class TestClosedSynchronizationBoundary(unittest.TestCase):
    def test_spanner_style_system_has_boundary(self) -> None:
        system, transactions = spanner_style_closed_system()
        self.assertIsNotNone(system.boundary)
        self.assertEqual(len(transactions), 2)
        self.assertIn("west_replica", system.boundary.member_ids)  # type: ignore[union-attr]

    def test_closed_internal_commit_order_uses_timestamps(self) -> None:
        result = evaluate_closed_synchronization_boundary()
        self.assertIsInstance(result, ClosedSynchronizationResult)
        self.assertEqual(result.internal_commit_order, ("tx_west", "tx_east"))

    def test_outside_raw_order_can_differ_from_internal_commit_order(self) -> None:
        result = evaluate_closed_synchronization_boundary()
        self.assertEqual(result.outside_raw_arrival_order, ("tx_east", "tx_west"))
        self.assertTrue(result.raw_order_differs_from_commit_order)

    def test_membership_boundary_is_active(self) -> None:
        result = evaluate_closed_synchronization_boundary()
        self.assertTrue(result.membership_boundary_active)
        self.assertEqual(result.boundary.quorum, 2)
        self.assertEqual(result.boundary.uncertainty_bound, 5)

    def test_propagation_constraints_are_respected(self) -> None:
        result = evaluate_closed_synchronization_boundary()
        self.assertTrue(result.propagation_constraints_respected)
        for item in result.transactions:
            self.assertGreaterEqual(
                item.commit_record_external_arrival_at,
                item.commit_visible_inside_at + item.external_path_delay,
            )

    def test_outside_reconstruction_waits_for_all_commit_records(self) -> None:
        result = evaluate_closed_synchronization_boundary()
        latest_external_commit_record = max(
            item.commit_record_external_arrival_at for item in result.transactions
        )
        self.assertEqual(result.outside_reconstruction_time, latest_external_commit_record)
        self.assertGreater(result.outside_reconstruction_time, max(item.commit_visible_inside_at for item in result.transactions))

    def test_synchronization_has_nonzero_cost(self) -> None:
        result = evaluate_closed_synchronization_boundary()
        self.assertGreater(result.synchronization_cost_total, 0)


class TestBoundaryComparison(unittest.TestCase):
    def test_comparison_identifies_two_scarcity_axes(self) -> None:
        comparison = compare_boundaries(
            evaluate_open_causal_scarcity(),
            evaluate_closed_synchronization_boundary(),
        )
        self.assertIsInstance(comparison, BoundaryComparison)
        self.assertEqual(comparison.open_scarcity_axis, "causal_proximity")
        self.assertEqual(comparison.closed_scarcity_axis, "membership_plus_synchronization_rule")

    def test_synchronization_relocates_scarcity(self) -> None:
        self.assertTrue(_r().comparison.synchronization_relocates_scarcity)
        self.assertTrue(_r().comparison.shared_record_access_frontier)
        self.assertGreater(_r().comparison.outside_observer_lag, 0)


class TestMeasurementProjectionBoundary(unittest.TestCase):
    def test_projection_boundary_is_conservative(self) -> None:
        projection = measurement_projection_boundary()
        self.assertIsInstance(projection, MeasurementProjectionBoundary)
        self.assertFalse(projection.assumes_fourteen_dimensional_y)
        self.assertIn("candidate_projection_boundary_only", projection.po1_status)

    def test_projection_names_preserved_and_forgotten_structure(self) -> None:
        projection = measurement_projection_boundary()
        self.assertIn("stable_pointer_record", projection.preserved_structure)
        self.assertIn("relative_phase_information", projection.forgotten_structure)
        self.assertGreaterEqual(len(projection.preserved_structure), 3)
        self.assertGreaterEqual(len(projection.forgotten_structure), 3)


class TestT46Analysis(unittest.TestCase):
    def test_run_returns_t46_result(self) -> None:
        self.assertIsInstance(_r(), T46Result)

    def test_best_supported_hypothesis_is_h3(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H3")

    def test_hypotheses_cover_h0_to_h5(self) -> None:
        ids = {item.hypothesis_id for item in _r().hypothesis_evaluations}
        self.assertEqual(ids, {"H0", "H1", "H2", "H3", "H4", "H5"})

    def test_h3_best_supported(self) -> None:
        h3 = [item for item in _r().hypothesis_evaluations if item.hypothesis_id == "H3"][0]
        self.assertEqual(h3.status, "best_supported")

    def test_h4_only_partially_supported(self) -> None:
        h4 = [item for item in _r().hypothesis_evaluations if item.hypothesis_id == "H4"][0]
        self.assertEqual(h4.status, "partially_supported")

    def test_named_claim_is_not_promoted_yet(self) -> None:
        self.assertIn("candidate claim", _r().named_claim_recommendation)
        self.assertIn("not a new claim file yet", _r().named_claim_recommendation)

    def test_serializes_to_json(self) -> None:
        data = t46_result_to_dict(_r())
        rendered = json.dumps(data)
        self.assertIn("open_causal", rendered)
        self.assertIn("closed synchronized systems", rendered)

    def test_markdown_renderer_contains_core_sections(self) -> None:
        markdown = render_markdown(t46_result_to_dict(_r()))
        self.assertIn("Open Causal Scarcity", markdown)
        self.assertIn("Closed Synchronization Boundary", markdown)
        self.assertIn("Measurement Projection Boundary", markdown)


if __name__ == "__main__":
    unittest.main()
