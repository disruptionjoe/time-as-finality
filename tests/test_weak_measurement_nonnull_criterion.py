"""Tests for T132 weak-measurement non-null criterion."""

from __future__ import annotations

import unittest

from models.weak_measurement_nonnull_criterion import (
    classify_protocol,
    protocol_shapes,
    run_t132_analysis,
)


class WeakMeasurementNonnullCriterionTests(unittest.TestCase):
    def test_threshold_only_protocol_is_same_record_null(self) -> None:
        audit = classify_protocol(protocol_shapes()[0])
        self.assertEqual(audit.classification, "null_same_record_derivation")
        self.assertIn("same monitoring record", audit.blocker)

    def test_post_hoc_semantic_protocol_is_rejected(self) -> None:
        audit = classify_protocol(protocol_shapes()[1])
        self.assertEqual(audit.classification, "null_unpreregistered_or_post_hoc")
        self.assertIn("not fixed before analysis", audit.blocker)

    def test_monotone_proxy_reversal_cost_is_null(self) -> None:
        audit = classify_protocol(protocol_shapes()[4])
        self.assertEqual(audit.classification, "null_monotone_proxy_cost")
        self.assertIn("monotone proxy", audit.blocker)

    def test_independent_meter_must_change_verdict(self) -> None:
        audit = classify_protocol(protocol_shapes()[5])
        self.assertEqual(audit.classification, "independent_but_not_decisive")
        self.assertFalse(audit.passes_nonnull_gate)

    def test_one_minimal_candidate_survives(self) -> None:
        audit = classify_protocol(protocol_shapes()[6])
        self.assertEqual(audit.classification, "candidate_non_null_protocol")
        self.assertTrue(audit.passes_nonnull_gate)
        self.assertEqual(audit.independent_axes, ("holder_redundancy",))

    def test_t132_result_reports_single_candidate_shape(self) -> None:
        result = run_t132_analysis()
        self.assertEqual(result.candidate_count, 1)
        self.assertEqual(result.null_count, 6)
        self.assertIn("non-null only in a narrow shape", result.strongest_claim)
        self.assertIn("demote T12", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
