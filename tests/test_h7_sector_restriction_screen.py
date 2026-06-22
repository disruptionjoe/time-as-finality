"""Tests for T168 exact-sector / gauge restriction screen."""

from __future__ import annotations

import unittest

from models.h7_sector_restriction_screen import (
    audit_fixture,
    fixture_family,
    is_sector_h7_upgrade_candidate,
    run_t168_analysis,
)


class H7SectorRestrictionScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t168_analysis()
        self.audits = {audit.fixture_id: audit for audit in self.result.audits}

    def test_local_sector_ban_is_operation_class_stipulation(self) -> None:
        audit = self.audits["local_sector_delete_forbidden_without_reservoir"]

        self.assertTrue(audit.absorber_vector_matched)
        self.assertTrue(audit.finite_operational_substrate)
        self.assertTrue(audit.gauge_invariant_difference)
        self.assertTrue(audit.future_operation_split)
        self.assertFalse(audit.h7_upgrade_candidate)
        self.assertEqual(audit.verdict, "sector_rule_stipulation_not_arrow")

    def test_compensating_reservoir_absorbs_sector_obstruction(self) -> None:
        audit = self.audits["compensating_reservoir_restores_deletion"]

        self.assertFalse(audit.absorber_vector_matched)
        self.assertIn("compensating_reservoir_state", audit.absorber_mismatch_fields)
        self.assertIn("sink_delta", audit.absorber_mismatch_fields)
        self.assertFalse(audit.h7_upgrade_candidate)
        self.assertEqual(
            audit.verdict,
            "absorbed_by_conserved_quantity_or_reservoir_accounting",
        )

    def test_gauge_relabeling_is_not_deletion(self) -> None:
        audit = self.audits["gauge_relabeling_record_loss"]

        self.assertFalse(audit.gauge_invariant_difference)
        self.assertEqual(audit.reverse_edge_class, "gauge_relabeling")
        self.assertEqual(audit.verdict, "pure_gauge_redundancy")
        self.assertFalse(audit.h7_upgrade_candidate)

    def test_exact_superselection_is_ideal_stipulation(self) -> None:
        audit = self.audits["exact_superselection_constructor_lock"]

        self.assertFalse(audit.finite_operational_substrate)
        self.assertFalse(audit.h7_upgrade_candidate)
        self.assertEqual(audit.verdict, "absorbed_by_exact_sector_idealization")

    def test_finite_symmetry_breaking_is_control_accounting(self) -> None:
        audit = self.audits["finite_symmetry_breaking_control"]

        self.assertFalse(audit.absorber_vector_matched)
        self.assertIn("allowed_control_class", audit.absorber_mismatch_fields)
        self.assertIn("reversible_control", audit.absorber_mismatch_fields)
        self.assertEqual(
            audit.verdict,
            "absorbed_by_finite_control_or_enforcement_accounting",
        )

    def test_matched_sector_topology_residue_is_not_arrow(self) -> None:
        audit = self.audits["matched_sector_branch_topology_residue"]

        self.assertTrue(audit.absorber_vector_matched)
        self.assertTrue(audit.finite_operational_substrate)
        self.assertTrue(audit.gauge_invariant_difference)
        self.assertTrue(audit.d1_topology_split)
        self.assertTrue(audit.future_operation_split)
        self.assertFalse(audit.h7_upgrade_candidate)
        self.assertEqual(
            audit.verdict,
            "fixed_accounting_sector_topology_residue_not_arrow",
        )

    def test_no_current_sector_fixture_is_h7_candidate(self) -> None:
        self.assertTrue(self.result.no_sector_fixture_clears_h7)
        self.assertEqual(self.result.h7_arrow_candidates, ())
        self.assertEqual(
            self.result.fixed_accounting_topology_residues,
            ("matched_sector_branch_topology_residue",),
        )

    def test_candidate_gate_has_positive_control(self) -> None:
        self.assertTrue(
            is_sector_h7_upgrade_candidate(
                reverse_edge_class="physical_record_deletion",
                absorber_vector_matched=True,
                finite_operational_substrate=True,
                gauge_invariant_difference=True,
                future_operation_split=True,
                reverse_status="constructor_impossible_after_full_accounting",
            )
        )
        self.assertFalse(
            is_sector_h7_upgrade_candidate(
                reverse_edge_class="physical_record_deletion",
                absorber_vector_matched=True,
                finite_operational_substrate=True,
                gauge_invariant_difference=False,
                future_operation_split=True,
                reverse_status="constructor_impossible_after_full_accounting",
            )
        )

    def test_fixture_family_does_not_implicitly_promote(self) -> None:
        for fixture in fixture_family():
            audit = audit_fixture(fixture)

            self.assertNotEqual(audit.verdict, "h7_physical_arrow_candidate")
        self.assertIn("do not currently reopen H7", self.result.strongest_claim)
        self.assertIn("not a theorem of gauge theory", self.result.not_claimed)


if __name__ == "__main__":
    unittest.main()
