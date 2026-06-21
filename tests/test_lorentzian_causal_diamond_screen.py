"""Tests for T153: Lorentzian causal-diamond screen."""

from __future__ import annotations

import unittest

from models.lorentzian_causal_diamond_screen import (
    CausalDiamond,
    InitialDataInterval,
    MinkowskiEvent,
    causally_precedes,
    changed_diamond_boundary_control,
    domain_dependence_control,
    fixed_lorentzian_data_control,
    interval_squared,
    remote_signal_control,
    run_t153_analysis,
    spacelike_reconciliation_control,
    spacelike_separated,
)


class LorentzianCausalDiamondScreenTests(unittest.TestCase):
    def test_minkowski_causal_relations(self) -> None:
        origin = MinkowskiEvent("origin", 0.0, 0.0)
        timelike_future = MinkowskiEvent("future", 3.0, 1.0)
        spacelike = MinkowskiEvent("spacelike", 1.0, 3.0)

        self.assertGreater(interval_squared(origin, timelike_future), 0.0)
        self.assertTrue(causally_precedes(origin, timelike_future))
        self.assertFalse(causally_precedes(origin, spacelike))
        self.assertTrue(spacelike_separated(origin, spacelike))

    def test_causal_diamond_membership(self) -> None:
        diamond = CausalDiamond(
            "diamond",
            MinkowskiEvent("past", -1.0, 0.0),
            MinkowskiEvent("future", 3.0, 0.0),
        )

        self.assertTrue(diamond.contains(MinkowskiEvent("inside", 1.0, 0.0)))
        self.assertFalse(diamond.contains(MinkowskiEvent("outside", 1.0, 3.0)))

    def test_future_domain_of_dependence_interval(self) -> None:
        interval = InitialDataInterval("slice", 0.0, -2.0, 2.0)

        self.assertTrue(
            interval.future_domain_contains(MinkowskiEvent("inside", 1.0, 0.0))
        )
        self.assertFalse(
            interval.future_domain_contains(MinkowskiEvent("outside", 1.5, 1.0))
        )

    def test_remote_signal_is_causal_record_access(self) -> None:
        audit = remote_signal_control()

        self.assertEqual(audit.classification, "remote_signal_is_causal_record_access")
        self.assertEqual(audit.residue_label, "translation_residue")
        self.assertFalse(audit.taf_adds_independent_content)

    def test_spacelike_events_have_later_common_future(self) -> None:
        audit = spacelike_reconciliation_control()

        self.assertEqual(
            audit.classification,
            "spacelike_no_invariant_order_later_reconciles",
        )
        self.assertEqual(audit.causal_relation, "spacelike_pair_with_common_future")

    def test_domain_dependence_absorbs_reconstructability(self) -> None:
        audit = domain_dependence_control()

        self.assertEqual(
            audit.classification,
            "domain_of_dependence_absorbs_reconstructability",
        )
        self.assertTrue(audit.capability_split)
        self.assertFalse(audit.lorentzian_data_matched)
        self.assertFalse(audit.taf_adds_independent_content)

    def test_changed_access_diamond_absorbs_verdict_split(self) -> None:
        audit = changed_diamond_boundary_control()

        self.assertEqual(
            audit.classification,
            "verdict_split_absorbed_by_changed_access_diamond",
        )
        self.assertTrue(audit.capability_split)
        self.assertFalse(audit.lorentzian_data_matched)

    def test_fixed_lorentzian_data_has_no_residue(self) -> None:
        audit = fixed_lorentzian_data_control()

        self.assertEqual(
            audit.classification,
            "fixed_lorentzian_data_no_finality_split",
        )
        self.assertTrue(audit.lorentzian_data_matched)
        self.assertFalse(audit.capability_split)

    def test_t153_aggregate_result(self) -> None:
        result = run_t153_analysis()

        self.assertTrue(result.remote_signal_guardrail_passed)
        self.assertTrue(result.spacelike_reconciliation_guardrail_passed)
        self.assertTrue(result.domain_dependence_absorbs_reconstructability)
        self.assertTrue(result.changed_diamond_absorbed)
        self.assertTrue(result.fixed_lorentzian_data_no_residue)
        self.assertIn("ordinary causal pasts", result.strongest_claim)
        self.assertIn("No same-Lorentzian-data TaF residue", result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
