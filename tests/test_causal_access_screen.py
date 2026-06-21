"""Tests for T151: causal-access screen for finality-boundary claims."""

from __future__ import annotations

import unittest

from models.causal_access_screen import (
    classify_causal_access,
    encoded_indirect_horizon_case,
    horizon_classical_export_case,
    remote_signal_control_case,
    run_t151_analysis,
    soft_boundary_permeability_case,
)


class CausalAccessScreenTests(unittest.TestCase):
    def test_remote_signal_counts_as_record_access_not_participation(self) -> None:
        audit = classify_causal_access(remote_signal_control_case())

        self.assertEqual(audit.classification, "remote_record_access_not_direct_participation")
        self.assertTrue(audit.exterior_classical_access)
        self.assertFalse(audit.exterior_direct_participation)
        self.assertEqual(audit.residue_label, "translation_residue")

    def test_horizon_claim_is_absorbed_by_causal_reachability(self) -> None:
        audit = classify_causal_access(horizon_classical_export_case())

        self.assertEqual(audit.classification, "causal_reachability_absorbs_boundary")
        self.assertTrue(audit.local_classical_access)
        self.assertFalse(audit.exterior_classical_access)
        self.assertEqual(audit.boundary_permeability, "one_way_inward_only")
        self.assertFalse(audit.taf_adds_independent_content)

    def test_encoded_channel_blocks_all_information_overclaim(self) -> None:
        audit = classify_causal_access(encoded_indirect_horizon_case())

        self.assertEqual(audit.classification, "overclaim_classical_screen_only")
        self.assertFalse(audit.exterior_classical_access)
        self.assertTrue(audit.exterior_extended_access)
        self.assertIn("cannot adjudicate total information loss", audit.reason)

    def test_soft_boundary_is_parameterized_not_horizon_like(self) -> None:
        audit = classify_causal_access(soft_boundary_permeability_case())

        self.assertEqual(audit.classification, "permeable_interface_not_horizon")
        self.assertTrue(audit.exterior_classical_access)
        self.assertEqual(audit.boundary_permeability, "bidirectional_classical_exchange")
        self.assertEqual(audit.residue_label, "parameterized_boundary")

    def test_t151_aggregate_checks(self) -> None:
        result = run_t151_analysis()

        self.assertTrue(result.remote_observation_guardrail_passed)
        self.assertTrue(result.horizon_claim_absorbed_by_causal_reachability)
        self.assertTrue(result.encoded_channel_overclaim_rejected)
        self.assertTrue(result.soft_boundary_parameterized)
        self.assertIn("ordinary causal reachability", result.strongest_claim)
        self.assertIn("B1 status should be weakened", result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
