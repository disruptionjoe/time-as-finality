"""Tests for T582 W192 record-conditioned capability discriminator gate."""

from __future__ import annotations

import json
import unittest

from models import t581_domain_native_sheaf_transport_review_package_closeout_router as t581
from models import t582_w192_record_conditioned_capability_discriminator_gate as t582


class W192RecordConditionedCapabilityDiscriminatorGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t582.run_t582_analysis()
        cls.payload = t582.t582_result_to_dict(cls.result)
        cls.tasks = {item.task_id: item for item in cls.result.task_results}
        cls.certificates = {
            item.certificate_id: item for item in cls.result.equality_certificates
        }
        cls.controls = {item.control_id: item for item in cls.result.control_results}
        cls.stages = {item.stage_id: item for item in cls.result.response_stages}
        cls.gates = {item.gate_id: item for item in cls.result.gate_decisions}

    def test_t581_authority_and_current_verdict(self) -> None:
        self.assertEqual(self.result.source_t581_verdict, t581.VERDICT)
        self.assertTrue(self.result.source_t581_package_parked)
        self.assertEqual(self.result.verdict, t582.VERDICT)
        self.assertFalse(self.result.positive_capability_verdict_allowed)
        self.assertTrue(self.gates["t581_separate_route_authority"].passed)

    def test_exact_one_task_state_resource_delta(self) -> None:
        self.assertEqual(self.result.capability_delta, (t582.TASK_RECORD_CONDITIONED,))
        self.assertEqual(self.result.deciding_fields, ("psi_access", "psi_identifier"))
        self.assertTrue(self.tasks[t582.TASK_RECORD_CONDITIONED].capability_changes)
        for task_id, task in self.tasks.items():
            if task_id != t582.TASK_RECORD_CONDITIONED:
                self.assertFalse(task.capability_changes)
        self.assertTrue(self.gates["exact_one_task_delta"].passed)

    def test_proxy_failure_does_not_decide_native_adjoint_task(self) -> None:
        self.assertEqual(
            self.tasks[t582.TASK_STATE_INDEPENDENT].before_outcome,
            "EXACT_FAIL_CENTRAL_PARITY",
        )
        self.assertEqual(
            self.tasks[t582.TASK_TYPED_CURRENT].before_outcome,
            "UNAVAILABLE_NATIVE_OBJECT_ABSENT",
        )
        self.assertTrue(self.gates["proxy_native_constructions_separated"].passed)

    def test_arbitrary_v_and_operator_shell_controls_do_not_add_delta(self) -> None:
        arbitrary_v = self.tasks[t582.TASK_ARBITRARY_V]
        shell = self.tasks[t582.TASK_OPERATOR_SHELL]
        self.assertEqual(arbitrary_v.before_outcome, "SURJECTIVE_PASS_FIBER_DIM_256")
        self.assertEqual(arbitrary_v.before_outcome, arbitrary_v.after_outcome)
        self.assertEqual(shell.before_outcome, shell.after_outcome)
        self.assertFalse(arbitrary_v.capability_changes)
        self.assertFalse(shell.capability_changes)

    def test_access_complete_and_intervention_equality_fail_closed(self) -> None:
        self.assertTrue(self.certificates["structural_observation_equality"].passed)
        self.assertFalse(self.certificates["access_complete_observation_equality"].passed)
        self.assertFalse(
            self.certificates["all_region_supported_intervention_equality"].passed
        )
        self.assertTrue(self.gates["equality_certificates_fail_closed"].passed)

    def test_completion_and_dependency_controls(self) -> None:
        self.assertEqual(
            self.controls["fixed_richer_source_delayed_access"].outcome,
            "FIXED_SOURCE_COMPLETION_FIRES",
        )
        self.assertEqual(self.controls["action2_only"].outcome, "WAITING_ACTION_3")
        self.assertEqual(self.controls["action3_only"].outcome, "WAITING_ACTION_2")
        self.assertEqual(
            self.controls["synthetic_complete"].outcome,
            t582.REVIEW_CANDIDATE_VERDICT,
        )
        self.assertTrue(all(item.passed for item in self.result.control_results))
        self.assertTrue(self.gates["completion_controls_pass"].passed)

    def test_response_stages_are_ordered_and_currently_not_ready(self) -> None:
        self.assertFalse(self.stages["TYPE_ADMISSIBLE"].ready)
        self.assertFalse(self.stages["QUOTIENT_RESPONSE_READY"].ready)
        self.assertFalse(self.stages["RETARDED_PHYSICS_READY"].ready)
        self.assertEqual(self.stages["TYPE_ADMISSIBLE"].gauge_scope, "proxy")
        self.assertTrue(self.gates["response_stages_ordered"].passed)

    def test_embedded_subalgebra_scope_is_not_relabeled_full_native(self) -> None:
        evidence = t582.EvidencePacket(
            state_resource_completion_fires=False,
            shadow_equality_earned=True,
            physical_boundary_forced=True,
            action2_evidence_present=True,
            action3_evidence_present=True,
            gauge_scope="embedded_subalgebra",
            type_fields_ready=True,
            quotient_fields_ready=True,
            retarded_fields_ready=False,
        )
        result = t582.run_t582_analysis(evidence)
        stages = {item.stage_id: item for item in result.response_stages}
        self.assertTrue(stages["TYPE_ADMISSIBLE"].ready)
        self.assertTrue(stages["QUOTIENT_RESPONSE_READY"].ready)
        self.assertFalse(stages["RETARDED_PHYSICS_READY"].ready)
        self.assertEqual(stages["TYPE_ADMISSIBLE"].gauge_scope, "embedded_subalgebra")
        self.assertEqual(result.verdict, "FORMAL_CANDIDATE_MISSING_NATIVE_RESPONSE")

    def test_absorber_precedence_blocks_otherwise_complete_packet(self) -> None:
        verdict, _ = t582.classify_verdict(
            schema_valid=True,
            capability_delta_count=1,
            state_resource_completion_fires=False,
            shadow_equality_earned=True,
            physical_boundary_forced=True,
            action2_ready=True,
            action3_ready=True,
            named_absorber="law_sector",
            retarded_physics_ready=True,
        )
        self.assertEqual(verdict, "ABSORBED_LAW_SECTOR")

    def test_json_and_markdown_are_bounded(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t582.render_markdown(self.payload)
        self.assertIn(t582.VERDICT, dumped)
        self.assertIn("T582 Results", markdown)
        self.assertIn("Response Stages", markdown)
        self.assertIn("No claim-ledger update is earned", dumped)
        for phrase in (
            "physical capability proved",
            "source law proved",
            "TAF8 theorem proved",
            "cross-repo identity proved",
        ):
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
