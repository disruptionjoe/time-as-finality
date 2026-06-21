"""Tests for T116 open Markov record-entropy comparison."""

from __future__ import annotations

import unittest

from models.open_markov_record_entropy import (
    detailed_balance_shuffle_control,
    nonequilibrium_cycle_control,
    open_export_recorder,
    reversible_append_only_control,
    run_t116_analysis,
)


class OpenMarkovRecordEntropyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t116_analysis()

    def test_detailed_balance_control_has_no_strict_record_arrow(self) -> None:
        audit = detailed_balance_shuffle_control()

        self.assertEqual(audit.total_irreversibility_nats, 0.0)
        self.assertFalse(audit.accounted_nondecreasing)
        self.assertFalse(audit.candidate_independent_h7_arrow)
        self.assertEqual(audit.classification, "no_strict_h7_arrow")

    def test_entropy_current_alone_is_not_scalar_finality_monotone(self) -> None:
        audit = nonequilibrium_cycle_control()

        self.assertGreater(audit.total_irreversibility_nats, 0.0)
        self.assertFalse(audit.accounted_nondecreasing)
        self.assertEqual(audit.accounted_score_sequence, (0, 1, 2, 0))
        self.assertEqual(audit.classification, "no_strict_h7_arrow")

    def test_open_export_recorder_is_absorbed_by_entropy_export(self) -> None:
        audit = open_export_recorder()

        self.assertFalse(audit.local_nondecreasing)
        self.assertTrue(audit.accounted_nondecreasing)
        self.assertEqual(audit.accounted_score_sequence, (0, 1, 2, 2, 3, 4, 4))
        self.assertGreater(audit.total_irreversibility_nats, 0.0)
        self.assertEqual(audit.exported_records_added, 4)
        self.assertFalse(audit.candidate_independent_h7_arrow)
        self.assertEqual(audit.classification, "absorbed_by_entropy_export")

    def test_reversible_append_only_uses_fresh_capacity(self) -> None:
        audit = reversible_append_only_control()

        self.assertTrue(audit.accounted_nondecreasing)
        self.assertEqual(audit.total_irreversibility_nats, 0.0)
        self.assertEqual(audit.fresh_capacity_consumed, 3)
        self.assertFalse(audit.candidate_independent_h7_arrow)
        self.assertEqual(audit.classification, "absorbed_by_fresh_capacity")

    def test_no_t116_fixture_produces_independent_h7_arrow(self) -> None:
        audits = (
            self.result.detailed_balance_control,
            self.result.nonequilibrium_cycle_control,
            self.result.open_export_recorder,
            self.result.reversible_append_only_control,
        )

        self.assertFalse(any(audit.candidate_independent_h7_arrow for audit in audits))
        self.assertIn("no independent open Markov arrow", self.result.h7_update)
        self.assertIn("standard stochastic thermodynamics", self.result.open_blocker)


if __name__ == "__main__":
    unittest.main()
