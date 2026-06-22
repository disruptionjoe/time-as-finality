"""Tests for T177: Q1 absorber-owned field intake."""

from __future__ import annotations

import unittest

from models.q1_absorber_owned_field_intake import (
    Q1Proposal,
    classify_q1_proposal,
    run_t177_analysis,
)


class Q1AbsorberOwnedFieldIntakeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t177_analysis()
        self.audits = {audit.proposal_id: audit for audit in self.result.audits}

    def test_absorber_owned_q1a_field_changes_do_not_reopen(self) -> None:
        audit = self.audits["q1a_partition_relabel"]

        self.assertEqual(audit.classification, "absorbed_q1a_changes_sbs_or_qd_data")
        self.assertFalse(audit.should_reopen_branch)

    def test_same_sbs_key_q1a_positive_control_is_admitted(self) -> None:
        audit = self.audits["q1a_same_sbs_key_physical_split_candidate"]

        self.assertEqual(audit.classification, "provisional_q1a_same_sbs_key_split")
        self.assertTrue(audit.should_reopen_branch)

    def test_incomplete_q1b_deployment_stays_scaffold_only(self) -> None:
        audit = self.audits["q1b_nominal_federation"]

        self.assertEqual(audit.classification, "scaffold_only_q1b_incomplete_external_packet")
        self.assertFalse(audit.should_reopen_branch)
        self.assertIn("full reviewable rows", audit.reason)
        self.assertIn("frozen challenge-window policy", audit.reason)

    def test_complete_q1b_packet_positive_control_is_admitted(self) -> None:
        audit = self.audits["q1b_reviewable_packet_candidate"]

        self.assertEqual(audit.classification, "provisional_q1b_reviewable_deployment_packet")
        self.assertTrue(audit.should_reopen_branch)

    def test_q1c_coarse_record_and_no_lift_controls_are_rejected(self) -> None:
        coarse = self.audits["q1c_coarse_record_second_meter"]
        no_lift = self.audits["q1c_packet_without_lift"]

        self.assertEqual(coarse.classification, "null_coarse_ordinary_record")
        self.assertFalse(coarse.should_reopen_branch)
        self.assertEqual(no_lift.classification, "scaffold_only_q1c_packet_without_verdict_lift")
        self.assertFalse(no_lift.should_reopen_branch)

    def test_q1c_packet_plus_typed_lift_positive_control_is_admitted(self) -> None:
        audit = self.audits["q1c_packet_plus_typed_lift_candidate"]

        self.assertEqual(audit.classification, "provisional_q1c_packet_plus_lift")
        self.assertTrue(audit.should_reopen_branch)

    def test_q1d_hidden_variable_story_rejected_and_guardrail_stays_guardrail(self) -> None:
        hidden_variable = self.audits["q1d_hidden_variable_story"]
        guardrail = self.audits["q1d_guardrail_only_language"]

        self.assertEqual(hidden_variable.classification, "null_q1d_hidden_variable_retrofit")
        self.assertFalse(hidden_variable.should_reopen_branch)
        self.assertEqual(guardrail.classification, "guardrail_only_q1d_no_new_theorem_target")
        self.assertFalse(guardrail.should_reopen_branch)

    def test_unknown_branch_is_rejected_before_q1_work(self) -> None:
        audit = classify_q1_proposal(
            Q1Proposal(
                proposal_id="generic_measurement_story",
                branch="Q1X",
                description="Measurement finality without a child branch.",
            )
        )

        self.assertEqual(audit.classification, "null_unknown_q1_branch")
        self.assertFalse(audit.should_reopen_branch)

    def test_aggregate_screen_keeps_q1_as_roadmap_umbrella(self) -> None:
        self.assertTrue(self.result.null_controls_rejected)
        self.assertTrue(self.result.hypothetical_reopen_controls_admitted)
        self.assertTrue(self.result.q1_remains_roadmap_umbrella)
        self.assertIn("absorber-owned fields fixed", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
