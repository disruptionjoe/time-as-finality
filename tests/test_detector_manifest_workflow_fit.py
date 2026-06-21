"""Tests for T138 detector manifest workflow fit."""

from __future__ import annotations

import unittest

from models.detector_manifest_workflow_fit import (
    audit_workflow_fit,
    manifest_from_workflow,
    run_t138_analysis,
    t136_human_fillable_template,
    workflow_fixtures,
)
from models.detector_preregistration_manifest import audit_preregistration_manifest


class T138TemplateTests(unittest.TestCase):
    def test_template_names_export_rule_not_preknown_payload(self) -> None:
        template = t136_human_fillable_template()
        payload_lines = [
            line for line in template if line.item == "raw_measurement_payload"
        ]

        self.assertEqual(len(payload_lines), 1)
        self.assertIn("Export-rule commitment", payload_lines[0].acceptable_fill)
        self.assertIn("Pre-known detector outcomes", payload_lines[0].null_if_missing)

    def test_template_includes_authority_and_claim_review_extension(self) -> None:
        items = {line.item for line in t136_human_fillable_template()}

        self.assertIn("authority_partition", items)
        self.assertIn("claim_review_fields", items)
        self.assertIn("manifest_hash", items)


class T138WorkflowFitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t138_analysis()
        self.audits = {audit.workflow_name: audit for audit in self.result.audits}
        self.workflows = {workflow.name: workflow for workflow in workflow_fixtures()}

    def test_common_single_lab_photonic_workflow_is_null(self) -> None:
        audit = self.audits["common_single_lab_photonic_coincidence_workflow"]

        self.assertFalse(audit.claimed_tier_admissible)
        self.assertEqual(audit.verdict, "workflow_null_for_q1b")
        self.assertFalse(audit.predata_boundary_respected)
        self.assertFalse(audit.authority_partition_admissible)
        self.assertIn("authority:authority_partition", audit.missing_template_items)
        self.assertIn("wrapper:authority_domains", audit.missing_template_items)

    def test_public_archive_repair_still_fails_authority_split(self) -> None:
        audit = self.audits["predata_single_lab_with_public_archive_workflow"]

        self.assertFalse(audit.claimed_tier_admissible)
        self.assertTrue(audit.predata_boundary_respected)
        self.assertTrue(audit.wrapper_commitments_valid)
        self.assertFalse(audit.authority_partition_admissible)
        self.assertIn("authority_partition_below_t100_lower_bound", audit.t136_failure_reasons)
        self.assertNotIn("wrapper:witness_references", audit.missing_template_items)

    def test_federated_predata_scaffold_clears_manifest_only(self) -> None:
        audit = self.audits["federated_predata_claim_review_workflow"]

        self.assertTrue(audit.claimed_tier_admissible)
        self.assertEqual(audit.max_certifiable_tier, "claim_review")
        self.assertEqual(audit.verdict, "claim_review_scaffold_fit")
        self.assertEqual(audit.t136_failure_reasons, ())
        self.assertIn("scaffold only", audit.interpretation)

    def test_preknown_payload_control_fails_boundary(self) -> None:
        audit = self.audits["federated_but_preknown_payload_workflow"]

        self.assertFalse(audit.claimed_tier_admissible)
        self.assertIn(
            "predata_manifest_claims_observed_payload_values",
            audit.t136_failure_reasons,
        )
        self.assertIn(
            "payload_boundary:raw_measurement_payload_export_rule",
            audit.missing_template_items,
        )

    def test_workflow_manifest_uses_t136_auditor(self) -> None:
        workflow = self.workflows["federated_predata_claim_review_workflow"]
        direct = audit_preregistration_manifest(manifest_from_workflow(workflow))
        wrapped = audit_workflow_fit(workflow)

        self.assertEqual(direct.claimed_tier_admissible, wrapped.claimed_tier_admissible)
        self.assertEqual(direct.failure_reasons, wrapped.t136_failure_reasons)

    def test_result_language_keeps_q1b_blocked(self) -> None:
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)
        self.assertIn("not as detector support", self.result.strongest_claim)
        self.assertIn("demote Q1B", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
