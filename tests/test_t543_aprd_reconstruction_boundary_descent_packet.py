"""Tests for T543 APRD reconstruction-boundary descent packet."""

from __future__ import annotations

import json
import unittest

from models import t542_post_retirement_source_law_reassessment_router as t542
from models import t543_aprd_reconstruction_boundary_descent_packet as t543


class APRDReconstructionBoundaryDescentPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t543.run_t543_analysis()
        cls.payload = t543.t543_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.case_id: evaluation for evaluation in cls.result.evaluations
        }

    def test_artifact_identity_and_t542_source_route(self) -> None:
        self.assertEqual(self.result.artifact, t543.ARTIFACT)
        self.assertEqual(self.result.verdict, t543.VERDICT)
        self.assertEqual(self.result.aprd_status, t543.APRD_STATUS)
        self.assertEqual(self.result.source_t542_verdict, t542.VERDICT)
        self.assertEqual(
            self.result.source_t542_selected_family,
            t542.SELECTED_FAMILY,
        )

    def test_aprd_is_set_valued_not_scalar_rank(self) -> None:
        definition = self.payload["aprd_definition"]

        self.assertEqual(definition["kind"], "set_valued_boundary_object")
        self.assertTrue(definition["not_a_scalar"])
        self.assertIn("scalar_rank_proxy", definition["forbidden_shortcuts"])
        self.assertNotIn("rank_score", json.dumps(definition, sort_keys=True))

    def test_reference_burdens_reproduce(self) -> None:
        expected = {
            "t19_internal_self_finality_boundary",
            "t66_threshold_rule_boundary",
            "t66_provenance_partition_boundary",
            "t51_t58_observer_b_phantom_gap",
        }

        self.assertEqual(set(self.result.reproduced_reference_burdens), expected)
        for case_id in expected:
            self.assertTrue(
                self.evaluations[case_id].reproduces_reference_burden,
                case_id,
            )

    def test_t19_and_t51_t58_debts_count_as_feeder_evidence(self) -> None:
        t19 = self.evaluations["t19_internal_self_finality_boundary"]
        t51 = self.evaluations["t51_t58_observer_b_phantom_gap"]

        self.assertEqual(
            t19.debt_ids,
            ("missing:R_self_finality_external_witness",),
        )
        self.assertEqual(t19.classification, "aprd_reconstruction_boundary_detected")
        self.assertTrue(t19.counts_as_source_law_evidence)

        self.assertIn("missing:ambient_pair:e1_A_locking<=e3_composite_locking", t51.debt_ids)
        self.assertIn("missing:provenance_record:r_A_locked", t51.debt_ids)
        self.assertEqual(t51.classification, "aprd_reconstruction_boundary_detected")
        self.assertTrue(t51.counts_as_source_law_evidence)

    def test_t66_debts_are_reproduced_but_absorbed(self) -> None:
        threshold = self.evaluations["t66_threshold_rule_boundary"]
        provenance = self.evaluations["t66_provenance_partition_boundary"]

        self.assertEqual(threshold.classification, "reproduced_but_native_absorbed")
        self.assertIn("underdeclared:threshold_rule", threshold.debt_ids)
        self.assertFalse(threshold.counts_as_source_law_evidence)

        self.assertEqual(provenance.classification, "reproduced_but_native_absorbed")
        self.assertIn("underdeclared:provenance_rule", provenance.debt_ids)
        self.assertFalse(provenance.counts_as_source_law_evidence)
        self.assertTrue(self.result.native_absorber_collapse_found)

    def test_hostile_controls_block_overreads(self) -> None:
        reversal = self.evaluations["t58_local_reversal_control"]
        scalar = self.evaluations["scalar_rank_proxy_control"]
        target = self.evaluations["target_statistic_import_control"]
        lorentzian = self.evaluations["lorentzian_reference_import_control"]

        self.assertEqual(reversal.classification, "invalid_extension_boundary")
        for evaluation in (scalar, target, lorentzian):
            self.assertEqual(
                evaluation.classification,
                "rejected_forbidden_rank_or_import",
            )

    def test_controls_all_pass_and_source_law_not_earned(self) -> None:
        self.assertTrue(all(control.passed for control in self.result.controls))
        source_law_evidence = [
            evaluation
            for evaluation in self.result.evaluations
            if evaluation.counts_as_source_law_evidence
        ]

        self.assertEqual(len(source_law_evidence), 2)
        self.assertIn("source-law status waits", self.result.taf11_update)
        self.assertIn(t543.NEXT_PACKET, self.result.recommended_next)

    def test_payload_and_markdown_do_not_move_governance_surfaces(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t543.render_markdown(self.payload)

        self.assertIn("T543 Results", markdown)
        self.assertIn("APRD Definition", markdown)
        forbidden = (
            "source law established",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
