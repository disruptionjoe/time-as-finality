"""Tests for T155: weak-measurement Blackwell boundary."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.weak_measurement_blackwell_boundary import (
    bayes_risk,
    canonical_cases,
    canonical_loss_tables,
    classify_blackwell_boundary,
    is_screened_off_by_record,
    run_t155_analysis,
)


class WeakMeasurementBlackwellBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = dict(canonical_cases())
        self.loss_tables = canonical_loss_tables()
        self.result = run_t155_analysis()

    def test_screened_off_same_instrument_case_has_equal_risks(self) -> None:
        events = self.cases["garbled_same_instrument_meter"]

        self.assertTrue(is_screened_off_by_record(events))
        for loss_table in self.loss_tables:
            record_risk = bayes_risk(events, features=("record",), loss_table=loss_table)
            record_aux_risk = bayes_risk(
                events,
                features=("record", "auxiliary"),
                loss_table=loss_table,
            )
            self.assertEqual(record_risk, record_aux_risk)
        self.assertEqual(
            bayes_risk(events, features=("record",), loss_table=self.loss_tables[0]),
            Fraction(1, 2),
        )

    def test_independent_noise_case_is_also_null(self) -> None:
        audit = classify_blackwell_boundary(
            self.cases["independent_noise_meter"],
            name="independent_noise_meter",
            loss_tables=self.loss_tables,
        )

        self.assertEqual(audit.classification, "null_blackwell_screened_off")
        self.assertTrue(audit.every_loss_equal)
        self.assertFalse(audit.some_loss_improves)

    def test_extra_environment_case_improves_both_loss_tables(self) -> None:
        audit = classify_blackwell_boundary(
            self.cases["extra_environment_candidate"],
            name="extra_environment_candidate",
            loss_tables=self.loss_tables,
        )

        self.assertEqual(audit.classification, "candidate_extra_structure_or_enlargement")
        self.assertFalse(audit.screened_off_by_record)
        self.assertTrue(audit.some_loss_improves)
        self.assertEqual(audit.record_only_risks["zero_one"], Fraction(1, 2))
        self.assertEqual(audit.record_auxiliary_risks["zero_one"], Fraction(0, 1))
        self.assertEqual(audit.record_only_risks["asymmetric_h1_cost"], Fraction(1, 4))
        self.assertEqual(audit.record_auxiliary_risks["asymmetric_h1_cost"], Fraction(0, 1))

    def test_aggregate_flags_hold(self) -> None:
        self.assertTrue(self.result.null_controls_hold)
        self.assertTrue(self.result.positive_control_improves)
        self.assertIn("screened off by the full ordinary monitored transcript", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
