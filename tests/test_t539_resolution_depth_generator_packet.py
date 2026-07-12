"""Tests for T539: resolution-depth generator packet."""

from __future__ import annotations

import json
import unittest

from models import t538_descent_obstruction_resolution_source_law_packet as t538
from models import t539_resolution_depth_generator_packet as t539


class ResolutionDepthGeneratorPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t539.run_t539_analysis()
        cls.payload = t539.t539_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.fixture_id: evaluation
            for evaluation in cls.result.fixture_evaluations
        }
        cls.controls = {control.control_id: control for control in cls.result.controls}

    def test_artifact_identity_and_t538_route_consumed(self) -> None:
        self.assertEqual(self.result.artifact, t539.ARTIFACT)
        self.assertEqual(self.result.verdict, t539.VERDICT)
        self.assertEqual(self.result.source_t538_verdict, t538.VERDICT)
        self.assertEqual(self.result.selected_family, t538.SELECTED_FAMILY)
        self.assertFalse(self.result.target_import_used)

    def test_depths_are_generated_not_pairwise_inputs(self) -> None:
        for evaluation in self.result.fixture_evaluations:
            self.assertFalse(evaluation.uses_pairwise_depth_table)
            self.assertEqual(
                len(evaluation.generated_depths),
                len(evaluation.activation_ranks) * (len(evaluation.activation_ranks) - 1),
            )

        self.assertTrue(self.controls["no_pairwise_depth_table_control"].passed)

    def test_generated_rank_channel_realizes_hostile_shapes(self) -> None:
        shapes = {
            evaluation.relation_shape
            for evaluation in self.result.fixture_evaluations
        }

        self.assertEqual(shapes, {"antichain", "total_chain", "diamond", "fork"})
        for evaluation in self.result.fixture_evaluations:
            self.assertTrue(evaluation.realizes_expected_rank_relation)
            self.assertTrue(evaluation.is_strict_partial_order)
            self.assertEqual(evaluation.failure_mode, "programmable_scalar_rank_channel")
            self.assertFalse(evaluation.counts_as_source_law_evidence)

    def test_relabel_control_passes_as_diagnostic(self) -> None:
        self.assertTrue(self.controls["record_and_cover_relabel_control"].passed)
        self.assertIn(
            "diagnostic programmability",
            self.controls["scalar_rank_programmability_control"].reason,
        )

    def test_family_route_is_retired_not_promoted(self) -> None:
        text = json.dumps(self.payload, sort_keys=True)

        self.assertEqual(
            self.result.family_status,
            "RETIRED_CURRENT_ROUTE_REQUIRES_NEW_SOURCE_LAW_FAMILY",
        )
        self.assertIn("TAF8", self.result.recommended_next)
        self.assertIn("S1 remains `requires_added_assumption`", text)
        self.assertIn("No claim-ledger update is earned", text)

    def test_claim_labels_include_computed_and_argued_confidence(self) -> None:
        labels = {(claim["label"], claim["confidence"]) for claim in self.payload["claim_labels"]}

        self.assertIn(("COMPUTED", "high"), labels)
        self.assertIn(("ARGUED", "medium"), labels)

    def test_markdown_reports_boundary_and_no_forbidden_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t539.render_markdown(self.payload)

        self.assertIn("## Strongest Reading", markdown)
        self.assertIn("RETIRED_CURRENT_ROUTE_REQUIRES_NEW_SOURCE_LAW_FAMILY", markdown)
        banned = (
            "S1 promoted",
            "claim status changed",
            "canon movement authorized",
            "public posture changed",
            "external publication authorized",
            "cross-repo truth proved",
        )
        for term in banned:
            self.assertNotIn(term, dumped)


if __name__ == "__main__":
    unittest.main()
