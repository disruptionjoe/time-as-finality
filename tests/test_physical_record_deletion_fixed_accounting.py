"""Tests for T145 physical record deletion fixed-accounting screen."""

from __future__ import annotations

import unittest

from models.physical_record_deletion_fixed_accounting import (
    audit_fixture,
    fixture_family,
    is_h7_upgrade_candidate,
    run_t145_analysis,
)


class PhysicalRecordDeletionFixedAccountingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t145_analysis()
        self.audits = {audit.fixture_id: audit for audit in self.result.audits}

    def test_fixed_erasure_floor_split_is_capability_not_arrow(self) -> None:
        audit = self.audits["same_floor_branch_topology_split"]

        self.assertTrue(audit.absorber_vector_matched)
        self.assertTrue(audit.d1_topology_split)
        self.assertTrue(audit.future_operation_split)
        self.assertFalse(audit.h7_upgrade_candidate)
        self.assertEqual(audit.verdict, "fixed_accounting_capability_split_not_arrow")

    def test_uncopy_vs_blind_reset_is_absorbed_by_accounting(self) -> None:
        audit = self.audits["correlated_uncopy_vs_blind_reset"]

        self.assertFalse(audit.absorber_vector_matched)
        self.assertIn("erased_bits", audit.absorber_mismatch_fields)
        self.assertIn("beta_work_floor", audit.absorber_mismatch_fields)
        self.assertIn("reversible_control", audit.absorber_mismatch_fields)
        self.assertEqual(audit.verdict, "absorbed_by_erasure_work_accounting")

    def test_hidden_sink_export_is_not_fixed_accounting(self) -> None:
        audit = self.audits["hidden_sink_export_control"]

        self.assertFalse(audit.absorber_vector_matched)
        self.assertIn("sink_delta", audit.absorber_mismatch_fields)
        self.assertEqual(audit.verdict, "absorbed_by_sink_accounting")

    def test_non_deletion_reverse_classes_do_not_count_for_h7(self) -> None:
        for fixture_id in (
            "observer_access_revocation",
            "authority_provenance_revocation",
        ):
            audit = self.audits[fixture_id]

            self.assertTrue(audit.future_operation_split)
            self.assertFalse(audit.h7_upgrade_candidate)
            self.assertEqual(audit.verdict, "non_deletion_reverse_class")

    def test_no_current_fixture_is_h7_arrow_candidate(self) -> None:
        self.assertTrue(self.result.no_current_fixed_accounting_deletion_arrow)
        self.assertEqual(self.result.h7_arrow_candidates, ())
        self.assertEqual(
            self.result.fixed_accounting_capability_splits,
            ("same_floor_branch_topology_split",),
        )

    def test_h7_candidate_gate_has_positive_control(self) -> None:
        self.assertTrue(
            is_h7_upgrade_candidate(
                reverse_edge_class="physical_record_deletion",
                absorber_vector_matched=True,
                future_operation_split=True,
                reverse_status="constructor_impossible_after_full_accounting",
            )
        )
        self.assertFalse(
            is_h7_upgrade_candidate(
                reverse_edge_class="physical_record_deletion",
                absorber_vector_matched=True,
                future_operation_split=True,
                reverse_status="ordinary_erasure_accounted",
            )
        )

    def test_fixture_family_audits_without_implicit_promotion(self) -> None:
        for fixture in fixture_family():
            audit = audit_fixture(fixture)

            self.assertNotEqual(audit.verdict, "h7_physical_arrow_candidate")
        self.assertIn("not enough for a physical arrow", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
