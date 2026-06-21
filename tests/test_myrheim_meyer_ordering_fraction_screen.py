"""Tests for T156: Myrheim-Meyer ordering-fraction screen."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.finality_colimit_causal_set_embeddability import (
    audit_finality_colimit_causet,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    audit_ordering_fraction_target,
    deterministic_flat_interval_control,
    flat_1p1_interval_target,
    product_grid_colimit_control,
    run_t156_analysis,
)


class MyrheimMeyerOrderingFractionScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = flat_1p1_interval_target()
        self.result = run_t156_analysis()
        self.by_name = {audit.name: audit for audit in self.result.audits}

    def test_flat_1p1_target_control_passes_declared_band(self) -> None:
        audit = audit_ordering_fraction_target(
            deterministic_flat_interval_control(),
            target=self.target,
        )

        self.assertTrue(audit.t126_filter_passed)
        self.assertEqual(audit.ordering_fraction, Fraction(7, 15))
        self.assertEqual(audit.absolute_gap, Fraction(1, 30))
        self.assertEqual(audit.verdict, "passes_ordering_fraction_control_only")

    def test_minimum_scale_product_grid_passes_t126_but_fails_target(self) -> None:
        datum = product_grid_colimit_control(2, 3)
        t126_audit = audit_finality_colimit_causet(datum)
        target_audit = audit_ordering_fraction_target(datum, target=self.target)

        self.assertEqual(t126_audit.classification, "passes_filter_only")
        self.assertTrue(t126_audit.manifold_filter_passed)
        self.assertEqual(target_audit.ordering_fraction, Fraction(4, 5))
        self.assertEqual(target_audit.verdict, "t126_pass_but_ordering_fraction_fail")

    def test_existing_t126_grid_survivor_fails_ordering_fraction_target(self) -> None:
        audit = self.by_name["grid_filter_pass_control"]

        self.assertTrue(audit.t126_filter_passed)
        self.assertEqual(audit.ordering_fraction, Fraction(3, 4))
        self.assertEqual(audit.absolute_gap, Fraction(1, 4))
        self.assertEqual(audit.verdict, "t126_pass_but_ordering_fraction_fail")

    def test_aggregate_flags_record_weakening(self) -> None:
        self.assertTrue(self.result.positive_target_control_passes)
        self.assertTrue(self.result.t126_pass_can_fail_ordering_fraction_target)
        self.assertTrue(self.result.all_product_grid_survivors_fail_target)
        self.assertIn("T126 `passes_filter_only` result", self.result.strongest_claim)
        self.assertIn("not even a 1+1", self.result.strongest_claim)
        self.assertIn("T126 passing is only a pre-diagnostic filter", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
