"""Tests for T124 constructor-admissibility grounding audit."""

from __future__ import annotations

import unittest

from models.constructor_admissibility_grounding_audit import (
    CONSTRUCTOR_IMPOSSIBLE,
    RESOURCE_ACCOUNTING_ONLY,
    RESOURCE_IMPOSSIBLE,
    REVERSIBLE_POSSIBLE,
    audit_case,
    run_t124_analysis,
    transformation_cases,
)


class ConstructorAdmissibilityGroundingAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t124_analysis()
        self.audits = {audit.case_id: audit for audit in self.result.audits}

    def test_required_sources_are_present(self) -> None:
        self.assertEqual(
            set(self.audits),
            {
                "t18_constructor_rule",
                "t80_reversible_window_definalization",
                "t84_cyclic_export_accounting",
                "t106_bounded_sink_forward_branch",
                "t110_closed_permutation_orbit",
                "t116_open_export_recorder",
                "t122_stationary_markov_upward_move",
                "t128_resource_drawdown",
                "t128_constructor_restricted",
            },
        )

    def test_every_strict_forward_increase_classifies_reverse_edge(self) -> None:
        for audit in self.result.audits:
            if audit.strict_forward_increase:
                self.assertTrue(audit.reverse_classified, audit.case_id)
                self.assertTrue(audit.reverse_edge, audit.case_id)
                self.assertTrue(audit.reverse_status, audit.case_id)

    def test_no_case_promotes_unqualified_physical_arrow(self) -> None:
        for audit in self.result.audits:
            self.assertFalse(audit.permits_unqualified_physical_arrow, audit.case_id)
        self.assertIn("never an unqualified physical arrow", self.result.strongest_claim)

    def test_constructor_survivors_are_marked_stipulative_or_formal(self) -> None:
        t18 = self.audits["t18_constructor_rule"]
        t128 = self.audits["t128_constructor_restricted"]

        for audit in (t18, t128):
            self.assertEqual(audit.reverse_status, CONSTRUCTOR_IMPOSSIBLE)
            self.assertTrue(audit.permits_constructor_reading)
            self.assertFalse(audit.permits_resource_accounting_reading)
        self.assertIn("premise", t18.reason)
        self.assertIn("imported", t128.reason)

    def test_reversible_controls_reject_physical_grounding(self) -> None:
        for case_id in (
            "t80_reversible_window_definalization",
            "t110_closed_permutation_orbit",
        ):
            audit = self.audits[case_id]
            self.assertEqual(audit.reverse_status, REVERSIBLE_POSSIBLE)
            self.assertFalse(audit.permits_constructor_reading)
            self.assertFalse(audit.permits_resource_accounting_reading)
            self.assertIn("reversible", audit.verdict)

    def test_stationary_markov_control_rejects_scalar_arrow(self) -> None:
        audit = self.audits["t122_stationary_markov_upward_move"]

        self.assertFalse(audit.permits_constructor_reading)
        self.assertFalse(audit.permits_resource_accounting_reading)
        self.assertIn("stationary", audit.verdict)
        self.assertIn("zero weighted drift", audit.reason)

    def test_resource_survivors_remain_resource_accounting_only(self) -> None:
        for case_id in (
            "t84_cyclic_export_accounting",
            "t106_bounded_sink_forward_branch",
            "t116_open_export_recorder",
            "t128_resource_drawdown",
        ):
            audit = self.audits[case_id]
            self.assertEqual(audit.verdict, RESOURCE_ACCOUNTING_ONLY)
            self.assertTrue(audit.permits_resource_accounting_reading)
            self.assertNotEqual(audit.named_resource_or_condition, "none")

        self.assertEqual(
            self.audits["t128_resource_drawdown"].reverse_status,
            RESOURCE_IMPOSSIBLE,
        )

    def test_audit_case_reports_required_fields(self) -> None:
        for case in transformation_cases():
            audit = audit_case(case)
            self.assertTrue(audit.case_id)
            self.assertTrue(audit.source)
            self.assertTrue(audit.forward_edge)
            self.assertTrue(audit.accounting_boundary)
            self.assertTrue(audit.reverse_edge)
            self.assertTrue(audit.reason)

    def test_claim_impact_does_not_promote_thermodynamic_arrow(self) -> None:
        self.assertIn("No existing H7 witness", self.result.weakened)
        self.assertIn("does not reduce", self.result.open_blocker)
        self.assertIn("T127", self.result.suggested_next)


if __name__ == "__main__":
    unittest.main()
