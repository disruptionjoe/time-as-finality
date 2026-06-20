"""Tests for T92 accessible-witness gap restriction."""

from __future__ import annotations

import unittest

from models.accessible_witness_gap_restriction import (
    audit_monotonicity_control_system,
    audit_system,
    gap,
    non_chain_proposition_gap_system,
    run_t92_analysis,
    semantic_relabeling_control_system,
    t19_proposition_gap_system,
)


class T19PropositionGapTests(unittest.TestCase):
    def setUp(self) -> None:
        self.system = t19_proposition_gap_system()
        self.patches = {patch.name: patch for patch in self.system.patches}

    def test_t19_internal_patch_has_self_finality_gap(self) -> None:
        self.assertEqual(
            gap(self.system, self.patches["U_int"]),
            frozenset({"R_self_finality"}),
        )

    def test_t19_external_patch_closes_self_finality_gap(self) -> None:
        self.assertEqual(gap(self.system, self.patches["U_ext"]), frozenset())

    def test_t19_gap_restriction_closure_holds(self) -> None:
        audit = audit_system(self.system)

        self.assertTrue(audit.ambient_restriction_holds)
        self.assertTrue(audit.audit_monotonicity_holds)
        self.assertTrue(audit.stable_typing_holds)
        self.assertTrue(audit.gap_restriction_holds)
        self.assertEqual(audit.classification, "conditional_theorem_witness")

    def test_t19_smaller_gap_need_not_lift(self) -> None:
        audit = audit_system(self.system)
        examples = {(ex.smaller_patch, ex.prop) for ex in audit.non_lifting_examples}

        self.assertIn(("U_int", "R_self_finality"), examples)


class NonChainWitnessTests(unittest.TestCase):
    def test_non_chain_joint_witness_satisfies_theorem_conditions(self) -> None:
        audit = audit_system(non_chain_proposition_gap_system())

        self.assertEqual(audit.classification, "conditional_theorem_witness")
        self.assertTrue(audit.gap_restriction_holds)
        self.assertGreater(audit.nested_pairs, 3)

    def test_non_chain_has_joint_self_finality_gap_before_both_witnesses(self) -> None:
        system = non_chain_proposition_gap_system()
        patches = {patch.name: patch for patch in system.patches}

        self.assertIn("O_joint_self_finality", gap(system, patches["U_local"]))
        self.assertIn("O_joint_self_finality", gap(system, patches["U_left"]))
        self.assertNotIn("O_joint_self_finality", gap(system, patches["U_joint"]))


class BoundaryControlTests(unittest.TestCase):
    def test_semantic_relabeling_breaks_gap_restriction(self) -> None:
        audit = audit_system(semantic_relabeling_control_system())

        self.assertFalse(audit.stable_typing_holds)
        self.assertFalse(audit.gap_restriction_holds)
        self.assertEqual(audit.classification, "semantic_relabeling_boundary")
        self.assertEqual(audit.violations[0].restricted_prop, "R_obs")

    def test_audit_monotonicity_violation_breaks_gap_restriction(self) -> None:
        audit = audit_system(audit_monotonicity_control_system())

        self.assertFalse(audit.audit_monotonicity_holds)
        self.assertFalse(audit.gap_restriction_holds)
        self.assertEqual(audit.classification, "audit_monotonicity_boundary")
        self.assertEqual(audit.violations[0].restricted_prop, "R_self_finality")


class FullT92AnalysisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t92_analysis()

    def test_theorem_status_supported_with_boundaries(self) -> None:
        self.assertEqual(
            self.result.theorem_status,
            "supported_with_explicit_boundaries",
        )

    def test_positive_witnesses_and_controls_are_both_present(self) -> None:
        classifications = {audit.classification for audit in self.result.audits}

        self.assertIn("conditional_theorem_witness", classifications)
        self.assertIn("semantic_relabeling_boundary", classifications)
        self.assertIn("audit_monotonicity_boundary", classifications)

    def test_claim_update_is_sharpen_not_upgrade(self) -> None:
        self.assertIn("may be sharpened, not upgraded", self.result.claim_update)

    def test_open_blocker_keeps_complexity_claim_open(self) -> None:
        self.assertIn("does not place", self.result.open_blocker)


if __name__ == "__main__":
    unittest.main()
