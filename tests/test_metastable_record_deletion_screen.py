"""Tests for T152 metastable-record deletion screen."""

from __future__ import annotations

import unittest

from models.metastable_record_deletion_screen import (
    audit_fixture,
    escape_rate,
    fixture_family,
    is_metastable_h7_upgrade_candidate,
    run_t152_analysis,
    survival_probability,
)


class MetastableRecordDeletionScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t152_analysis()
        self.audits = {audit.fixture_id: audit for audit in self.result.audits}

    def test_finite_barrier_lifetime_is_kinetic_not_arrow(self) -> None:
        audit = self.audits["finite_barrier_lifetime_split"]

        self.assertFalse(audit.absorber_vector_matched)
        self.assertIn("beta_barrier", audit.absorber_mismatch_fields)
        self.assertTrue(audit.finite_barriers)
        self.assertTrue(audit.future_operation_split)
        self.assertFalse(audit.h7_upgrade_candidate)
        self.assertEqual(audit.verdict, "absorbed_by_kinetic_barrier_accounting")
        self.assertGreater(audit.left_survival_probability, 0.99)
        self.assertLess(audit.right_survival_probability, 0.99)

    def test_same_barrier_topology_split_is_not_arrow(self) -> None:
        audit = self.audits["same_barrier_branch_topology_split"]

        self.assertTrue(audit.absorber_vector_matched)
        self.assertTrue(audit.finite_barriers)
        self.assertTrue(audit.d1_topology_split)
        self.assertTrue(audit.future_operation_split)
        self.assertFalse(audit.h7_upgrade_candidate)
        self.assertEqual(
            audit.verdict,
            "fixed_accounting_metastable_topology_residue_not_arrow",
        )

    def test_infinite_barrier_is_constructor_stipulation(self) -> None:
        audit = self.audits["infinite_barrier_constructor_lock"]

        self.assertFalse(audit.finite_barriers)
        self.assertFalse(audit.h7_upgrade_candidate)
        self.assertEqual(audit.verdict, "absorbed_by_infinite_barrier_stipulation")

    def test_control_denial_is_boundary_accounting(self) -> None:
        audit = self.audits["control_window_denial"]

        self.assertFalse(audit.absorber_vector_matched)
        self.assertIn("control_window", audit.absorber_mismatch_fields)
        self.assertIn("reversible_control", audit.absorber_mismatch_fields)
        self.assertEqual(audit.verdict, "absorbed_by_control_boundary")

    def test_reservoir_change_is_absorber_data(self) -> None:
        audit = self.audits["hidden_cold_reservoir_or_engineered_barrier"]

        self.assertFalse(audit.absorber_vector_matched)
        self.assertIn("reservoir_state", audit.absorber_mismatch_fields)
        self.assertEqual(
            audit.verdict,
            "absorbed_by_reservoir_or_temperature_accounting",
        )

    def test_no_current_metastable_fixture_is_h7_candidate(self) -> None:
        self.assertTrue(self.result.no_finite_metastable_substrate_clears_h7)
        self.assertEqual(self.result.h7_arrow_candidates, ())
        self.assertEqual(
            self.result.fixed_accounting_topology_residues,
            ("same_barrier_branch_topology_split",),
        )

    def test_candidate_gate_has_positive_control(self) -> None:
        self.assertTrue(
            is_metastable_h7_upgrade_candidate(
                reverse_edge_class="physical_record_deletion",
                absorber_vector_matched=True,
                finite_barriers=True,
                future_operation_split=True,
                reverse_status="constructor_impossible_after_full_accounting",
            )
        )
        self.assertFalse(
            is_metastable_h7_upgrade_candidate(
                reverse_edge_class="physical_record_deletion",
                absorber_vector_matched=True,
                finite_barriers=True,
                future_operation_split=True,
                reverse_status="finite_rate_or_control_deletion_possible",
            )
        )

    def test_escape_rate_boundary(self) -> None:
        self.assertEqual(escape_rate(None), 0.0)
        self.assertGreater(escape_rate(5.0), escape_rate(30.0))
        self.assertEqual(survival_probability(None, horizon=1000.0), 1.0)

    def test_fixture_family_does_not_implicitly_promote(self) -> None:
        for fixture in fixture_family():
            audit = audit_fixture(fixture)

            self.assertNotEqual(audit.verdict, "h7_physical_arrow_candidate")
        self.assertIn("Metastability does not reopen H7", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
