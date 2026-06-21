"""Tests for T128 minimal living arrow finite models."""

from __future__ import annotations

import unittest

from models.minimal_living_arrow import audit_model, all_models, run_t128_analysis


class MinimalLivingArrowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t128_analysis()
        self.audits = {audit.model_id: audit for audit in self.result.audits}

    def test_required_models_are_present(self) -> None:
        self.assertEqual(
            {model.model_id for model in all_models()},
            {
                "control_a_closed_reversible",
                "control_b_stationary_markov",
                "test_c_resource_drawdown",
                "test_d_maintenance_cost",
                "test_e_open_boundary",
                "test_f_constructor_restricted",
            },
        )

    def test_closed_reversible_control_has_no_arrow(self) -> None:
        audit = self.audits["control_a_closed_reversible"]

        self.assertTrue(audit.has_directed_cycle)
        self.assertFalse(audit.direction_survives)
        self.assertFalse(audit.t122_assumptions_violated)
        self.assertIn("T110", audit.obstruction_status)

    def test_stationary_markov_control_has_no_arrow(self) -> None:
        audit = self.audits["control_b_stationary_markov"]

        self.assertTrue(audit.has_directed_cycle)
        self.assertFalse(audit.direction_survives)
        self.assertFalse(audit.t122_assumptions_violated)
        self.assertIn("T122", audit.obstruction_status)

    def test_resource_drawdown_is_smallest_nonstipulative_survivor(self) -> None:
        audit = self.audits["test_c_resource_drawdown"]

        self.assertFalse(audit.has_directed_cycle)
        self.assertTrue(audit.every_edge_strictly_increases)
        self.assertTrue(audit.direction_survives)
        self.assertIn("nonstationary resource drawdown", audit.t122_assumptions_violated)
        self.assertEqual(
            self.result.strongest_surviving_minimal_model,
            "test_c_resource_drawdown",
        )

    def test_maintenance_survives_only_as_resource_drawdown(self) -> None:
        audit = self.audits["test_d_maintenance_cost"]

        self.assertTrue(audit.direction_survives)
        self.assertIn("finite repair budget", audit.resource_accounting)
        self.assertIn("Equivalent to resource drawdown", audit.equivalence_note)

    def test_open_boundary_survives_only_with_sink_accounting(self) -> None:
        audit = self.audits["test_e_open_boundary"]

        self.assertTrue(audit.direction_survives)
        self.assertIn("open boundary", audit.t122_assumptions_violated)
        self.assertIn("sink capacity", audit.equivalence_note)

    def test_constructor_restriction_is_formal_but_stipulative(self) -> None:
        audit = self.audits["test_f_constructor_restricted"]

        self.assertTrue(audit.direction_survives)
        self.assertIn("excluded reverse channel", audit.t122_assumptions_violated)
        self.assertIn("stipulated", audit.verdict)
        self.assertIn("constructor restriction alone", self.result.smallest_formal_ingredient_set)

    def test_every_model_reports_required_deliverable_fields(self) -> None:
        for model in all_models():
            audit = audit_model(model)
            self.assertTrue(audit.state_names)
            self.assertTrue(audit.transition_rules)
            self.assertTrue(audit.resource_accounting)
            self.assertTrue(audit.direction_candidate)
            self.assertTrue(audit.obstruction_status)
            self.assertIsInstance(audit.direction_survives, bool)

    def test_claim_impact_does_not_promote_thermodynamic_arrow(self) -> None:
        self.assertIn("Do not promote", self.result.claim_impact_recommendation)
        self.assertIn("ordinary free-energy", self.result.suggested_next)


if __name__ == "__main__":
    unittest.main()
