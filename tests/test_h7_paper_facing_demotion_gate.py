"""Tests for T148: H7 paper-facing demotion gate."""

from __future__ import annotations

import unittest

from models.h7_paper_facing_demotion_gate import (
    H7GateProfile,
    classify_h7_paper_status,
    run_t148_analysis,
)


class H7PaperFacingDemotionGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t148_analysis()

    def test_current_status_is_demoted_to_constructor_resource_audit(self) -> None:
        self.assertEqual(
            self.result.paper_facing_status,
            "demoted_to_constructor_resource_audit",
        )
        self.assertIn(
            "conditional D1-monotone constructor theorem",
            self.result.allowed_claims,
        )
        self.assertIn(
            "derivation of the thermodynamic arrow from finality alone",
            self.result.rejected_claims,
        )

    def test_t145_residue_does_not_promote_physical_arrow(self) -> None:
        self.assertTrue(self.result.profile.fixed_accounting_capability_residue)
        self.assertFalse(self.result.profile.fixed_accounting_deletion_candidate)
        self.assertIn(
            "the surviving fixed-accounting split is future-operation residue, not reverse impossibility",
            self.result.open_blockers,
        )

    def test_current_record_graph_reverse_is_not_grounded(self) -> None:
        self.assertFalse(self.result.profile.record_graph_reverse_grounded)
        self.assertIn(
            "constructor-impossible reverse in the current T1 record graph",
            self.result.rejected_claims,
        )

    def test_positive_control_reopens_only_as_candidate(self) -> None:
        candidate = classify_h7_paper_status(
            H7GateProfile(
                conditional_constructor_theorem=True,
                closed_reversible_obstruction=True,
                open_stochastic_absorbed=True,
                record_graph_reverse_grounded=True,
                fixed_accounting_deletion_candidate=True,
                fixed_accounting_capability_residue=True,
            )
        )

        self.assertEqual(
            candidate.paper_facing_status,
            "physical_arrow_candidate_requires_absorber_review",
        )
        self.assertIn(
            "candidate physical-deletion route pending hostile absorber review",
            candidate.allowed_claims,
        )
        self.assertIn(
            "unreviewed promotion from candidate substrate to physical arrow",
            candidate.rejected_claims,
        )


if __name__ == "__main__":
    unittest.main()
