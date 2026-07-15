"""Tests for T581 review-package closeout router."""

from __future__ import annotations

import json
import unittest

from models import (
    t580_domain_native_sheaf_transport_external_panel_scope_closure_gate as t580,
)
from models import (
    t581_domain_native_sheaf_transport_review_package_closeout_router as t581,
)


class DomainNativeSheafTransportReviewPackageCloseoutRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t581.run_t581_analysis()
        cls.payload = t581.t581_result_to_dict(cls.result)
        cls.conditions = {item.condition_id: item for item in cls.result.reopen_conditions}
        cls.decisions = {item.decision_id: item for item in cls.result.closeout_decisions}
        cls.gates = {item.gate_id: item for item in cls.result.gate_decisions}

    def test_t580_authority_and_artifact_identity(self) -> None:
        self.assertEqual(self.result.artifact, t581.ARTIFACT)
        self.assertEqual(self.result.verdict, t581.VERDICT)
        self.assertEqual(self.result.source_t580_verdict, t580.VERDICT)
        self.assertEqual(self.result.source_t580_selected_next_packet, t580.NEXT_PACKET)
        self.assertTrue(self.gates["t580_authority"].passed)

    def test_package_is_closed_and_parked_without_promotion(self) -> None:
        self.assertTrue(self.result.package_closed)
        self.assertTrue(self.result.package_parked)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.old_route_next_packet, "none")
        self.assertTrue(self.gates["package_closed_and_parked"].passed)
        self.assertTrue(self.gates["promotion_by_momentum_blocked"].passed)

    def test_four_evidence_only_reopen_conditions_are_named(self) -> None:
        self.assertEqual(
            set(self.conditions),
            {
                "new_domain_native_source_packet",
                "empirical_detector_manifest",
                "finality_native_continuum_bridge",
                "cross_domain_shadow_protection_packet",
            },
        )
        self.assertTrue(all(item.evidence_required for item in self.conditions.values()))
        self.assertFalse(any(item.current_evidence_present for item in self.conditions.values()))
        self.assertFalse(self.conditions["cross_domain_shadow_protection_packet"].reopens_old_package)
        self.assertTrue(self.gates["evidence_only_reopen_conditions_named"].passed)

    def test_w192_is_routed_separately(self) -> None:
        decision = self.decisions["route_w192_as_separate_packet"]
        self.assertTrue(decision.selected)
        self.assertEqual(decision.next_packet, t581.SEPARATE_PACKET)
        self.assertEqual(self.result.separate_packet, t581.SEPARATE_PACKET)
        self.assertTrue(self.gates["w192_routed_separately"].passed)

    def test_old_route_and_protected_movements_are_blocked(self) -> None:
        self.assertFalse(self.decisions["continue_old_route_unattended"].selected)
        self.assertEqual(
            self.decisions["move_protected_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["protected_movements_blocked"].passed)

    def test_all_gates_pass_and_markdown_records_closeout(self) -> None:
        self.assertTrue(all(item.passed for item in self.result.gate_decisions))
        markdown = t581.render_markdown(self.payload)
        self.assertIn("T581 Results", markdown)
        self.assertIn(t581.PACKAGE_STATUS, markdown)
        self.assertIn(t581.SEPARATE_PACKET, markdown)
        self.assertIn("Reopen Conditions", markdown)

    def test_json_serializable_and_no_forbidden_promotion(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        self.assertIn("No claim-ledger update is earned", dumped)
        for phrase in (
            "source law proved",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
        ):
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
