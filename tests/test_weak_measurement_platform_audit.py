"""Tests for T91 weak-measurement platform audit."""

from __future__ import annotations

import unittest

from models.weak_measurement_platform_audit import (
    classify_candidate,
    platform_candidates,
    run_t91_analysis,
)


class WeakMeasurementPlatformAuditTests(unittest.TestCase):
    def test_homodyne_candidate_is_same_record_derivation(self) -> None:
        homodyne = platform_candidates()[0]
        audit = classify_candidate(homodyne)

        self.assertEqual(audit.classification, "null_same_record_derivation")
        self.assertIn("same monitoring record", audit.blocker)

    def test_uncollapse_candidate_is_rejected_for_postselection(self) -> None:
        uncollapse = platform_candidates()[1]
        audit = classify_candidate(uncollapse)

        self.assertEqual(audit.classification, "null_postselected_axis")
        self.assertIn("success-conditioned", audit.blocker)

    def test_quantum_jump_candidate_is_same_record_derivation(self) -> None:
        jump = platform_candidates()[2]
        audit = classify_candidate(jump)

        self.assertEqual(audit.classification, "null_same_record_derivation")
        self.assertIn("same monitoring record", audit.blocker)

    def test_t91_result_reports_no_current_platform_escape(self) -> None:
        result = run_t91_analysis()

        self.assertEqual(len(result.audits), 3)
        self.assertTrue(all(audit.classification != "candidate_non_null_platform" for audit in result.audits))
        self.assertIn("do not yet supply an independent D1", result.strongest_claim)
        self.assertIn("Stop treating standard homodyne/jump-reversal platforms", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
