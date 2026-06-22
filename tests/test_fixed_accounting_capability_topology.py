"""Tests for T179 fixed-accounting capability topology residue."""

from __future__ import annotations

import unittest

from models.fixed_accounting_capability_topology import (
    is_fixed_accounting_capability_residue,
    is_h7_physical_arrow_candidate,
    run_t179_analysis,
)


class FixedAccountingCapabilityTopologyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t179_analysis()
        self.audits = {audit.case_id: audit for audit in self.result.audits}

    def test_branch_topology_split_is_capability_residue_not_arrow(self) -> None:
        audit = self.audits["same_accounting_branch_survival_split"]

        self.assertTrue(audit.absorber_vector_matched)
        self.assertTrue(audit.topology_profile_split)
        self.assertTrue(audit.future_capability_split)
        self.assertTrue(audit.fixed_accounting_capability_residue)
        self.assertFalse(audit.h7_physical_arrow_candidate)
        self.assertEqual(
            audit.verdict, "fixed_accounting_capability_topology_residue"
        )

    def test_same_topology_control_has_no_residue(self) -> None:
        audit = self.audits["same_accounting_same_topology_control"]

        self.assertTrue(audit.absorber_vector_matched)
        self.assertFalse(audit.topology_profile_split)
        self.assertFalse(audit.future_capability_split)
        self.assertFalse(audit.fixed_accounting_capability_residue)
        self.assertEqual(audit.verdict, "no_capability_residue")

    def test_changed_erasure_floor_is_absorber_owned(self) -> None:
        audit = self.audits["changed_erasure_floor_absorber_control"]

        self.assertFalse(audit.absorber_vector_matched)
        self.assertIn("erased_bits", audit.absorber_mismatch_fields)
        self.assertIn("beta_work_floor", audit.absorber_mismatch_fields)
        self.assertEqual(audit.verdict, "absorber_owned_capability_split")

    def test_non_deletion_split_does_not_count_as_fixed_accounting_residue(self) -> None:
        audit = self.audits["provenance_loss_non_deletion_control"]

        self.assertTrue(audit.future_capability_split)
        self.assertFalse(audit.fixed_accounting_capability_residue)
        self.assertEqual(audit.verdict, "non_deletion_capability_split")

    def test_synthetic_positive_control_separates_h7_gate(self) -> None:
        audit = self.audits["constructor_impossible_positive_control"]

        self.assertTrue(audit.absorber_vector_matched)
        self.assertTrue(audit.topology_profile_split)
        self.assertTrue(audit.future_capability_split)
        self.assertFalse(audit.fixed_accounting_capability_residue)
        self.assertTrue(audit.h7_physical_arrow_candidate)
        self.assertEqual(
            audit.verdict, "synthetic_h7_reinstatement_positive_control"
        )

    def test_boolean_gates_have_distinct_outputs(self) -> None:
        common = {
            "absorber_vector_matched": True,
            "topology_profile_split": True,
            "future_capability_split": True,
            "reverse_edge_class": "physical_record_deletion",
        }

        self.assertTrue(
            is_fixed_accounting_capability_residue(
                **common,
                reverse_status="ordinary_erasure_accounted",
            )
        )
        self.assertFalse(
            is_fixed_accounting_capability_residue(
                **common,
                reverse_status="constructor_impossible_after_full_accounting",
            )
        )
        self.assertTrue(
            is_h7_physical_arrow_candidate(
                **common,
                reverse_status="constructor_impossible_after_full_accounting",
            )
        )

    def test_only_current_residue_case_is_t145_survivor(self) -> None:
        self.assertEqual(
            self.result.residue_cases,
            ("same_accounting_branch_survival_split",),
        )
        self.assertEqual(
            self.result.h7_candidates,
            ("constructor_impossible_positive_control",),
        )
        self.assertIn("not a thermodynamic arrow", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
