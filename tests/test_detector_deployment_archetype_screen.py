"""Tests for T169 detector deployment-archetype screen."""

from __future__ import annotations

import unittest

from models.detector_deployment_archetype_screen import (
    audit_deployment_archetype,
    deployment_archetypes,
    run_t169_analysis,
)


class DetectorDeploymentArchetypeScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t169_analysis()
        self.audits = {audit.archetype_id: audit for audit in self.result.audits}
        self.archetypes = {
            archetype.archetype_id: archetype for archetype in deployment_archetypes()
        }

    def test_single_lab_posthoc_story_is_null_immediately(self) -> None:
        audit = self.audits["single_lab_posthoc_internal_pki"]

        self.assertFalse(audit.manifest_claim_review_ready)
        self.assertEqual(
            audit.classification,
            "null_predata_manifest_or_nominal_authority_failure",
        )
        self.assertFalse(audit.event_rows_reviewable)

    def test_public_archive_repair_is_still_null(self) -> None:
        audit = self.audits["predata_single_lab_public_archive_repair"]

        self.assertEqual(
            audit.classification,
            "null_predata_manifest_or_nominal_authority_failure",
        )
        self.assertIn("pre-data manifest", audit.required_next.lower())

    def test_shared_archive_audit_hsm_kills_nominal_federation(self) -> None:
        audit = self.audits["nominal_federation_shared_archive_audit_hsm"]

        self.assertTrue(audit.manifest_claim_review_ready)
        self.assertFalse(audit.effective_root_partition_admissible)
        self.assertEqual(audit.classification, "null_hidden_control_root_merge")

    def test_shared_release_root_kills_nominal_federation(self) -> None:
        audit = self.audits["nominal_federation_shared_release_root"]

        self.assertTrue(audit.manifest_claim_review_ready)
        self.assertFalse(audit.effective_root_partition_admissible)
        self.assertEqual(audit.classification, "null_hidden_control_root_merge")

    def test_private_escrow_without_reviewable_rows_is_scaffold_only(self) -> None:
        audit = self.audits["federated_independent_roots_private_escrow"]

        self.assertTrue(audit.manifest_claim_review_ready)
        self.assertTrue(audit.effective_root_partition_admissible)
        self.assertFalse(audit.event_rows_reviewable)
        self.assertEqual(audit.classification, "scaffold_only_no_reviewable_event_rows")

    def test_reviewable_row_federation_is_the_only_live_candidate(self) -> None:
        audit = self.audits["federated_independent_roots_reviewable_rows"]

        self.assertTrue(audit.manifest_claim_review_ready)
        self.assertTrue(audit.effective_root_partition_admissible)
        self.assertTrue(audit.event_rows_reviewable)
        self.assertTrue(audit.independently_escrowed)
        self.assertEqual(audit.classification, "live_external_q1b_candidate")
        self.assertEqual(
            self.result.live_external_candidate_archetypes,
            ("federated_independent_roots_reviewable_rows",),
        )

    def test_direct_and_wrapped_audits_match(self) -> None:
        archetype = self.archetypes["federated_independent_roots_reviewable_rows"]
        direct = audit_deployment_archetype(archetype)
        wrapped = self.audits["federated_independent_roots_reviewable_rows"]

        self.assertEqual(direct.classification, wrapped.classification)
        self.assertEqual(direct.required_next, wrapped.required_next)

    def test_result_language_keeps_q1b_blocked(self) -> None:
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)
        self.assertIn("only one surviving deployment archetype family", self.result.strongest_claim)
        self.assertIn("demote Q1B", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
