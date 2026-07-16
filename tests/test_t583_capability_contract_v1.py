"""Focused tests for T583 CapabilityContract v1."""

from __future__ import annotations

import json
import unittest
from dataclasses import replace

from models import t583_capability_contract_v1 as t583


class CapabilityContractV1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t583.run_t583_analysis()
        cls.payload = t583.result_to_dict(cls.result)
        cls.checks = {item.check_id: item for item in cls.result.checks}
        cls.assessments = {item.pair_id: item for item in cls.result.assessments}
        cls.contexts = {item.context_id: item for item in cls.result.contexts}
        cls.envelopes = {
            (item.context_id, item.state_id): item for item in cls.result.envelopes
        }

    def test_contract_verdict_and_review_boundary(self) -> None:
        self.assertEqual(self.result.verdict, t583.VERDICT)
        self.assertTrue(all(item.passed for item in self.result.checks))
        self.assertEqual(
            self.result.claim_ledger_update,
            "No claim-ledger or Canon Index update is earned.",
        )

    def test_capability_is_pareto_envelope_not_scalar(self) -> None:
        base = self.envelopes[("ctx_base", "state_alpha")]
        self.assertEqual(base.native_structure, "task_indexed_pareto_preorder")
        self.assertEqual(len(base.points), 3)
        self.assertNotIn("dominated", {item.protocol_id for item in base.points})
        self.assertFalse(self.result.capability_definition["scalar_default"])
        self.assertTrue(self.checks["pareto_not_scalar_default"].passed)

    def test_cost_and_error_budgets_are_explicit_and_enforced(self) -> None:
        base = self.contexts["ctx_base"]
        low = self.contexts["ctx_low_budget"]
        self.assertEqual(base.budget.energy, 5.0)
        self.assertEqual(base.budget.error, 0.1)
        self.assertEqual(low.budget.energy, 1.0)
        self.assertEqual(len(self.envelopes[("ctx_base", "state_alpha")].points), 3)
        self.assertEqual(len(self.envelopes[("ctx_low_budget", "state_alpha")].points), 1)
        self.assertTrue(self.checks["explicit_cost_error_budget"].passed)

    def test_access_menu_and_resource_provenance_are_typed(self) -> None:
        base = self.contexts["ctx_base"]
        self.assertEqual(base.access_provenance, "declared_local_lab_access")
        self.assertEqual(base.menu_provenance, "law_derived_finite_control")
        self.assertEqual(base.resource_provenance, "fixed_declared_budget")
        self.assertTrue(self.checks["access_menu_resource_provenance"].passed)

    def test_renaming_and_gauge_invariance(self) -> None:
        assessment = self.assessments["renaming_gauge_preservation"]
        base = self.contexts["ctx_base"]
        renamed = self.contexts["ctx_renamed_gauge"]
        self.assertNotEqual(base.gauge_representative, renamed.gauge_representative)
        self.assertEqual(base.semantic_dict(), renamed.semantic_dict())
        self.assertEqual(assessment.capability_relation, "EQUIVALENT")
        self.assertEqual(assessment.verdict, "PRESERVATION_CONTROL_PASS")

    def test_irrelevant_coarse_graining_is_stable(self) -> None:
        context = self.contexts["ctx_base"]
        left = {"physical_payload": "same", "display_label": "left"}
        right = {"physical_payload": "same", "display_label": "right"}
        self.assertEqual(
            t583.project_irrelevant_metadata(left, context),
            t583.project_irrelevant_metadata(right, context),
        )
        self.assertTrue(self.checks["irrelevant_coarse_graining_stability"].passed)

    def test_distinct_states_can_have_equal_capability(self) -> None:
        assessment = self.assessments["distinct_states_equal_capability"]
        self.assertNotEqual("state_alpha", "state_beta_distinct")
        self.assertEqual(assessment.capability_relation, "EQUIVALENT")
        self.assertTrue(self.checks["equal_capability_nontriviality"].passed)

    def test_negative_nonfactorization_detected_then_absorbed(self) -> None:
        assessment = self.assessments["negative_nonfactorization_control"]
        self.assertEqual(assessment.capability_relation, "INCOMPARABLE")
        self.assertEqual(assessment.verdict, "NATIVE_STATE_COMPLETION")
        self.assertFalse(assessment.positive_capability_verdict_allowed)

    def test_budget_mutation_is_completion(self) -> None:
        assessment = self.assessments["budget_mutation_control"]
        self.assertIn("cost_error_budget", assessment.context_differences)
        self.assertEqual(assessment.verdict, "RESOURCE_BUDGET_COMPLETION")
        self.assertFalse(assessment.positive_capability_verdict_allowed)

    def test_w192_remains_explicit_state_resource_completion(self) -> None:
        assessment = self.assessments["w192_explicit_state_resource_absorption"]
        self.assertEqual(assessment.verdict, t583.W192_VERDICT)
        self.assertEqual(self.result.w192_verdict, t583.W192_VERDICT)
        self.assertFalse(assessment.positive_capability_verdict_allowed)

    def test_changed_menu_is_absorbed(self) -> None:
        base = self.contexts["ctx_base"]
        changed = replace(
            base,
            context_id="changed_menu",
            operation_menu=base.operation_menu + ("extra_control",),
        )
        left = t583.attainable_envelope(
            context=base, state_id="menu_left", candidates=t583._base_points()
        )
        right_points = t583._base_points() + (
            t583.PerformancePoint(
                "recover_record", 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, "extra_control"
            ),
        )
        right = t583.attainable_envelope(
            context=changed, state_id="menu_right", candidates=right_points
        )
        assessment = t583.assess_pair(
            pair_id="changed_menu_test",
            left_context=base,
            right_context=changed,
            left_envelope=left,
            right_envelope=right,
            evidence=t583.PairEvidence(),
        )
        self.assertEqual(assessment.verdict, "MENU_COMPLETION")

    def test_synthetic_complete_case_has_review_only_ceiling(self) -> None:
        assessment = self.assessments["synthetic_complete_candidate"]
        self.assertEqual(assessment.verdict, t583.CANDIDATE_CEILING)
        self.assertEqual(self.result.synthetic_candidate_ceiling, t583.CANDIDATE_CEILING)
        self.assertFalse(assessment.positive_capability_verdict_allowed)

    def test_null_and_completion_inventory_is_explicit(self) -> None:
        required = {
            "NO_CAPABILITY_DELTA",
            "RENAMING_OR_GAUGE_EQUIVALENCE",
            "IRRELEVANT_COARSE_GRAINING",
            "TASK_REDEFINITION_COMPLETION",
            "MENU_COMPLETION",
            "ACCESS_COMPLETION",
            "RESOURCE_BUDGET_COMPLETION",
            t583.W192_VERDICT,
            "FIXED_SOURCE_COMPLETION",
            "NATIVE_STATE_COMPLETION",
        }
        self.assertTrue(required.issubset(set(self.result.null_completion_classes)))

    def test_json_and_markdown_preserve_nonclaims(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t583.render_markdown(self.payload)
        self.assertIn(t583.VERDICT, dumped)
        self.assertIn("CapabilityContract v1", markdown)
        self.assertIn("does not establish a universal capability measure", dumped)
        for forbidden in (
            "physical capability proved",
            "time derived",
            "issuance proved",
            "cross-repo identity proved",
        ):
            self.assertNotIn(forbidden, dumped)


if __name__ == "__main__":
    unittest.main()
