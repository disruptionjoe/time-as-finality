"""Focused tests for T584 capability invariance morphisms."""

from __future__ import annotations

import json
import unittest

from models import t584_capability_invariance_morphism_gate as t584


class CapabilityInvarianceMorphismGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t584.run_t584_analysis()
        cls.payload = t584.result_to_dict(cls.result)
        cls.audits = {item.morphism_id: item for item in cls.result.audits}
        cls.checks = {item.check_id: item for item in cls.result.checks}

    def test_verdict_and_review_boundary(self) -> None:
        self.assertEqual(self.result.verdict, t584.VERDICT)
        self.assertTrue(all(check.passed for check in self.result.checks))
        self.assertEqual(
            self.result.claim_ledger_update,
            "No claim-ledger or Canon Index update is earned.",
        )

    def test_substantive_representation_morphism_preserves_envelope(self) -> None:
        audit = self.audits["unit_and_interface_representation"]
        self.assertTrue(audit.admissible)
        self.assertEqual(audit.relation, "EQUIVALENT")
        self.assertIn("raw tasks", audit.substantive_change)
        self.assertTrue(self.checks["substantive_representation_change"].passed)

    def test_gauge_orbit_factors_through_quotient(self) -> None:
        audit = self.audits["gauge_orbit_phase_shift"]
        self.assertTrue(audit.admissible)
        self.assertEqual(audit.kind, "gauge")
        self.assertEqual(audit.relation, "EQUIVALENT")
        self.assertTrue(self.checks["gauge_factors_through_quotient"].passed)

    def test_irrelevant_coarse_graining_preserves_payload(self) -> None:
        audit = self.audits["telemetry_coarse_graining"]
        self.assertEqual(audit.relation, "EQUIVALENT")
        self.assertTrue(self.checks["irrelevant_coarse_graining_stable"].passed)

    def test_task_vocabulary_merge_is_caught_as_counterexample(self) -> None:
        audit = self.audits["task_vocabulary_merge_counterexample"]
        self.assertFalse(audit.admissible)
        self.assertNotEqual(audit.relation, "EQUIVALENT")
        self.assertTrue(audit.invariant_or_caught)
        self.assertTrue(self.checks["task_merge_counterexample_caught"].passed)

    def test_capability_is_not_full_state_identity(self) -> None:
        self.assertTrue(self.checks["capability_not_state_identity"].passed)

    def test_serialized_results_preserve_nonclaims(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t584.render_markdown(self.payload)
        self.assertIn(t584.VERDICT, dumped)
        self.assertIn("Capability Invariance Morphism Gate", markdown)
        for forbidden in (
            "time derived",
            "issuance proved",
            "source law proved",
            "cross-repo identity proved",
        ):
            self.assertNotIn(forbidden, dumped)


if __name__ == "__main__":
    unittest.main()
