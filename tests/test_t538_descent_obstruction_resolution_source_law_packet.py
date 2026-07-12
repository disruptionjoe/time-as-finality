"""Tests for T538: descent-obstruction resolution source-law packet."""

from __future__ import annotations

import json
import unittest

from models import t537_source_law_family_and_falsifier_packet as t537
from models import t538_descent_obstruction_resolution_source_law_packet as t538


class DescentObstructionResolutionSourceLawPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t538.run_t538_analysis()
        cls.payload = t538.t538_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.fixture_id: evaluation
            for evaluation in cls.result.fixture_evaluations
        }
        cls.controls = {control.control_id: control for control in cls.result.controls}

    def test_artifact_identity_and_t537_family_consumed(self) -> None:
        self.assertEqual(self.result.artifact, t538.ARTIFACT)
        self.assertEqual(self.result.verdict, t538.VERDICT)
        self.assertEqual(self.result.source_t537_verdict, t537.VERDICT)
        self.assertEqual(self.result.selected_family, t537.SELECTED_FAMILY)
        self.assertFalse(self.result.target_import_used)

    def test_ordered_depth_recipe_programs_multiple_relation_shapes(self) -> None:
        shapes = {
            evaluation.relation_shape
            for evaluation in self.result.fixture_evaluations
        }

        self.assertEqual(shapes, {"antichain", "total_chain", "diamond", "fork"})
        for evaluation in self.result.fixture_evaluations:
            self.assertTrue(evaluation.realizes_intended_relation)
            self.assertTrue(evaluation.is_strict_partial_order)
            self.assertFalse(evaluation.counts_as_source_law_evidence)

    def test_antichain_and_total_chain_controls_are_not_promoted(self) -> None:
        antichain = self.evaluations["antichain_control"]
        chain = self.evaluations["total_chain_control"]

        self.assertEqual(antichain.relation_shape, "antichain")
        self.assertEqual(antichain.comparable_pair_count, 0)
        self.assertFalse(antichain.counts_as_source_law_evidence)
        self.assertEqual(chain.relation_shape, "total_chain")
        self.assertEqual(chain.comparable_pair_count, chain.total_pair_count)
        self.assertFalse(chain.counts_as_source_law_evidence)

    def test_relabel_and_isomorphism_controls_pass_as_diagnostics(self) -> None:
        for control in self.result.controls:
            self.assertTrue(control.passed)

        self.assertIn("underconstraint", self.controls["restriction_map_isomorphism_control"].reason)
        self.assertIn("depth generator", self.controls["free_depth_programmability_control"].reason)

    def test_family_is_narrowed_not_claimed(self) -> None:
        text = json.dumps(self.payload, sort_keys=True)

        self.assertEqual(
            self.result.family_status,
            "NARROWED_REQUIRES_RESOLUTION_DEPTH_GENERATOR",
        )
        self.assertIn("T539", self.result.recommended_next)
        self.assertIn("S1 remains `requires_added_assumption`", text)
        self.assertIn("No claim-ledger update is earned", text)

    def test_claim_labels_include_computed_and_argued_confidence(self) -> None:
        labels = {(claim["label"], claim["confidence"]) for claim in self.payload["claim_labels"]}

        self.assertIn(("COMPUTED", "high"), labels)
        self.assertIn(("ARGUED", "medium"), labels)

    def test_markdown_reports_boundary_and_no_forbidden_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t538.render_markdown(self.payload)

        self.assertIn("## Strongest Reading", markdown)
        self.assertIn("NARROWED_REQUIRES_RESOLUTION_DEPTH_GENERATOR", markdown)
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
