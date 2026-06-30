"""Tests for T377 relativistic record-rendering fixture."""

from __future__ import annotations

from fractions import Fraction
import unittest

from models.relativistic_record_rendering import (
    FORBIDDEN_SOURCE_COLUMNS,
    canonical_carrier,
    canonical_observers,
    carrier_interval,
    causal_order_only_sufficient,
    pair_invariants,
    render_record,
    run_t377_analysis,
)


class RelativisticRecordRenderingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t377_analysis()
        self.carrier = canonical_carrier()
        self.observers = canonical_observers()
        self.records = self.carrier.by_id()

    def test_source_rows_have_no_primitive_time_or_space_columns(self) -> None:
        self.assertTrue(self.result.no_primitive_time_column)
        self.assertFalse(set(self.carrier.source_columns) & FORBIDDEN_SOURCE_COLUMNS)

    def test_carrier_is_compatible(self) -> None:
        self.assertTrue(self.result.carrier_valid)
        for record in self.carrier.records:
            for parent_id in record.parents:
                parent = self.records[parent_id]
                self.assertLessEqual(parent.u_rank, record.u_rank)
                self.assertLessEqual(parent.v_rank, record.v_rank)

    def test_rendered_observers_recover_same_interval(self) -> None:
        self.assertTrue(self.result.rendered_interval_invariant)
        for row in self.result.pair_invariants:
            self.assertEqual(row.observer_a_interval, Fraction(row.carrier_interval, 1))
            self.assertEqual(row.observer_b_interval, Fraction(row.carrier_interval, 1))

    def test_observers_disagree_on_simultaneity(self) -> None:
        self.assertTrue(self.result.simultaneity_disagreement)
        self.assertEqual(self.result.simultaneity_pair, ("u_only", "v_only"))

        observer_a, observer_b = self.observers
        u_only = self.records["u_only"]
        v_only = self.records["v_only"]
        self.assertEqual(
            render_record(u_only, observer_a).coord_time,
            render_record(v_only, observer_a).coord_time,
        )
        self.assertNotEqual(
            render_record(u_only, observer_b).coord_time,
            render_record(v_only, observer_b).coord_time,
        )

    def test_causal_order_alone_does_not_determine_interval_magnitude(self) -> None:
        rows = pair_invariants(self.carrier, self.observers)
        self.assertFalse(causal_order_only_sufficient(rows))
        self.assertFalse(self.result.causal_order_only_sufficient)

        near_interval = carrier_interval(self.records["origin"], self.records["near"])
        future_interval = carrier_interval(self.records["origin"], self.records["future"])
        self.assertNotEqual(near_interval, future_interval)

    def test_hostile_comparators_report_absorber_pressure(self) -> None:
        by_id = {verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts}

        self.assertFalse(by_id["minkowski_first"].absorbs)
        self.assertTrue(by_id["fixed_schema_log"].absorbs)
        self.assertTrue(by_id["fixed_completed_table"].absorbs)
        self.assertFalse(by_id["hidden_preferred_foliation"].absorbs)
        self.assertFalse(by_id["causal_order_only"].absorbs)
        self.assertTrue(by_id["t376_fixed_admissibility"].absorbs)

    def test_overall_verdict_is_calibration_not_claim_upgrade(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "rendered_interval_recovered_but_fixed_carrier_absorbed",
        )
        self.assertIn("not a claim upgrade", self.result.claim_ledger_update)
        self.assertIn("fixed carrier schema", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
