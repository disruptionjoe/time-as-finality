"""Tests for T146: weak-measurement escape architecture gate."""

from __future__ import annotations

import unittest

from models.weak_measurement_escape_architecture_gate import (
    canonical_architectures,
    classify_architecture,
    current_frontier_case,
    run_t146_analysis,
)


class ArchitectureClassificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = dict(canonical_architectures())

    def test_same_instrument_without_extra_structure_is_null_by_default(self) -> None:
        audit = classify_architecture(
            self.cases["same_instrument_default_null"],
            name="same_instrument_default_null",
        )
        self.assertEqual(audit.classification, "null_same_instrument_default")
        self.assertFalse(audit.active_route)

    def test_extra_environment_structure_is_live_escape_class(self) -> None:
        audit = classify_architecture(
            self.cases["extra_environment_candidate"],
            name="extra_environment_candidate",
        )
        self.assertEqual(audit.classification, "candidate_extra_environment_escape")
        self.assertTrue(audit.active_route)

    def test_instrument_enlargement_needs_declared_comparison_target(self) -> None:
        name, case = current_frontier_case()
        audit = classify_architecture(case, name=name)
        self.assertEqual(audit.classification, "null_same_instrument_default")
        self.assertFalse(audit.active_route)

        enlarged = classify_architecture(
            self.cases["enlarged_instrument_candidate"],
            name="enlarged_instrument_candidate",
        )
        self.assertEqual(enlarged.classification, "candidate_enlarged_instrument_escape")
        self.assertTrue(enlarged.active_route)


class T146ResultTests(unittest.TestCase):
    def test_result_keeps_current_frontier_dormant(self) -> None:
        result = run_t146_analysis()
        classifications = {audit.name: audit.classification for audit in result.audits}
        self.assertEqual(classifications["coarse_record_only"], "null_coarse_standard_record")
        self.assertEqual(
            classifications["screened_off_by_full_record"],
            "null_screened_off_by_full_record",
        )
        self.assertEqual(
            classifications["proxy_or_postselected"],
            "null_proxy_or_postselection",
        )
        self.assertEqual(
            classifications["same_instrument_default_null"],
            "null_same_instrument_default",
        )
        self.assertEqual(
            classifications["extra_environment_candidate"],
            "candidate_extra_environment_escape",
        )
        self.assertEqual(
            classifications["enlarged_instrument_candidate"],
            "candidate_enlarged_instrument_escape",
        )
        self.assertEqual(classifications["current_frontier"], "null_same_instrument_default")
        self.assertIn("only two live Q1C architecture classes remain", result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
