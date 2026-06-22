"""Tests for T172 issuance-to-finality bridge."""

from __future__ import annotations

import unittest

from models.issuance_to_finality_bridge import (
    audit_bridge_fixture,
    bridge_fixture_family,
    run_t172_analysis,
    scenario_readout_edges,
    scenario_source_order,
    source_order_recovered_by_readout,
)


class IssuanceToFinalityBridgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t172_analysis()
        self.audits = {audit.fixture_id: audit for audit in self.result.audits}
        self.fixtures = {fixture.fixture_id: fixture for fixture in bridge_fixture_family()}

    def test_sound_record_generation_reflects_visible_source_order(self) -> None:
        audit = self.audits["sound_record_generation_reflection_control"]
        scenario = self.fixtures["sound_record_generation_reflection_control"].left

        self.assertEqual(scenario_source_order(scenario), (("a", "b"), ("a", "c"), ("b", "c")))
        self.assertEqual(scenario_readout_edges(scenario), scenario_source_order(scenario))
        self.assertTrue(source_order_recovered_by_readout(scenario))
        self.assertTrue(audit.left_source_order_recovered)
        self.assertEqual(audit.verdict, "positive_source_readout_reflection")
        self.assertFalse(audit.h7_source_arrow_upgrade_candidate)

    def test_same_issuance_different_cadence_changes_profile_only(self) -> None:
        audit = self.audits["same_issuance_different_cadence"]

        self.assertTrue(audit.same_source_order)
        self.assertFalse(audit.same_observer_records)
        self.assertTrue(audit.same_taf_readout_edges)
        self.assertTrue(audit.same_mu)
        self.assertTrue(audit.finality_profile_split)
        self.assertFalse(audit.source_capability_split)
        self.assertEqual(audit.verdict, "cadence_boundary_not_source_arrow")

    def test_same_records_can_hide_source_issuance_order(self) -> None:
        audit = self.audits["same_records_different_hidden_issuance"]

        self.assertFalse(audit.same_source_order)
        self.assertTrue(audit.same_observer_records)
        self.assertTrue(audit.same_taf_readout_edges)
        self.assertTrue(audit.same_mu)
        self.assertTrue(audit.source_capability_split)
        self.assertFalse(audit.taf_readout_split)
        self.assertEqual(audit.verdict, "source_capability_lost_by_taf_readout")

    def test_mu_is_invisible_to_plain_taf_readout_when_task_needs_it(self) -> None:
        audit = self.audits["same_issuance_records_different_mu"]

        self.assertTrue(audit.same_source_order)
        self.assertTrue(audit.same_observer_records)
        self.assertTrue(audit.same_taf_readout_edges)
        self.assertFalse(audit.same_mu)
        self.assertTrue(audit.source_capability_split)
        self.assertFalse(audit.taf_readout_split)
        self.assertEqual(audit.verdict, "mu_invisible_to_taf_readout")

    def test_nonmonotone_access_loss_is_observer_boundary(self) -> None:
        audit = self.audits["nonmonotone_access_loss"]

        self.assertTrue(audit.same_source_order)
        self.assertTrue(audit.same_observer_records)
        self.assertTrue(audit.same_mu)
        self.assertTrue(audit.left_access_monotone)
        self.assertFalse(audit.right_access_monotone)
        self.assertEqual(audit.right_access_scores, ((0, 1), (1, 2), (2, 1), (3, 2)))
        self.assertEqual(audit.verdict, "access_boundary_not_source_arrow")

    def test_gluing_failure_does_not_determine_global_order(self) -> None:
        audit = self.audits["gluing_failure_global_order_not_assumed"]

        self.assertFalse(audit.same_source_order)
        self.assertTrue(audit.same_observer_records)
        self.assertTrue(audit.same_taf_readout_edges)
        self.assertTrue(audit.same_mu)
        self.assertTrue(audit.source_capability_split)
        self.assertFalse(audit.taf_readout_split)
        self.assertFalse(audit.left_source_order_recovered)
        self.assertFalse(audit.right_source_order_recovered)
        self.assertEqual(audit.verdict, "gluing_failure_not_global_order")

    def test_fixture_family_has_no_source_arrow_upgrade_candidate(self) -> None:
        for fixture in bridge_fixture_family():
            audit = audit_bridge_fixture(fixture)

            self.assertFalse(audit.h7_source_arrow_upgrade_candidate)

        self.assertEqual(self.result.h7_arrow_candidates, ())
        self.assertIn("Finality can be a sound observer-side reflection", self.result.strongest_claim)
        self.assertIn("does not import Temporal Issuance as true", self.result.not_claimed)


if __name__ == "__main__":
    unittest.main()
