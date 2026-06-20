"""Tests for T112 spin-observerse holonomy Step 2."""

from __future__ import annotations

import unittest
from math import pi, sqrt

from models.t112_spin_observerse_holonomy import (
    audit_causal_controls,
    audit_phase_proxy,
    default_angle_convention,
    holonomy,
    is_locally_causal,
    run_t112_audit,
)


class SpinObserverseHolonomyStep2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t112_audit()

    def test_naive_y_is_negative_control_and_spin_lift_is_only_candidate(self) -> None:
        topology = self.result.topology

        self.assertEqual(topology.naive_y_pi1_order, 1)
        self.assertFalse(topology.naive_y_nontrivial_z2_holonomy_available)
        self.assertEqual(topology.spin_lift_pi1_order, 2)
        self.assertTrue(topology.spin_lift_z2_candidate_available)

    def test_declared_spin_lift_phase_matches_cech_sign(self) -> None:
        phase = self.result.phase
        chsh = self.result.chsh

        self.assertAlmostEqual(phase.positive_generator_total_angle, 2.0 * pi)
        self.assertEqual(phase.positive_generator_z2_sign, -1)
        self.assertEqual(chsh.canonical_holonomy, -1)
        self.assertEqual(
            phase.positive_generator_z2_sign,
            chsh.canonical_holonomy,
        )

    def test_signed_closed_angle_control_blocks_unqualified_berry_claim(self) -> None:
        phase = audit_phase_proxy(default_angle_convention())

        self.assertAlmostEqual(phase.signed_closed_total_angle, 0.0)
        self.assertEqual(phase.signed_closed_z2_sign, +1)
        self.assertTrue(phase.convention_is_load_bearing)
        self.assertIn("load-bearing", phase.verdict)

    def test_chsh_sign_and_majority_representatives_under_declared_angles(self) -> None:
        chsh = self.result.chsh

        self.assertAlmostEqual(chsh.chsh_value, -2.0 * sqrt(2.0))
        self.assertTrue(chsh.abs_chsh_matches_tsirelson)
        self.assertEqual(chsh.majority_section_count, 16)
        self.assertEqual(chsh.majority_holonomies, (-1,))
        self.assertEqual(chsh.canonical_transition_pattern.count(-1), 1)

    def test_t65_controls_are_preserved_without_restoring_biconditional(self) -> None:
        causal = audit_causal_controls()

        self.assertEqual(causal.total_sections, 256)
        self.assertEqual(causal.locally_causal_sections, 16)
        self.assertTrue(causal.locally_causal_all_holonomy_plus_one)
        self.assertEqual(causal.holonomy_plus_one_sections, 128)
        self.assertEqual(causal.non_lc_holonomy_plus_one_sections, 112)
        self.assertFalse(causal.biconditional_restored)
        self.assertFalse(is_locally_causal(causal.example_non_lc_holonomy_plus_one))
        self.assertEqual(holonomy(causal.example_non_lc_holonomy_plus_one), +1)

    def test_representative_dependence_is_explicit(self) -> None:
        control = self.result.representative_control

        self.assertEqual(control.all_support_sections, 256)
        self.assertEqual(control.all_support_holonomy_counts[-1], 128)
        self.assertEqual(control.all_support_holonomy_counts[+1], 128)
        self.assertTrue(control.majority_representatives_all_holonomy_minus_one)
        self.assertTrue(control.arbitrary_support_has_holonomy_plus_one)
        self.assertTrue(control.arbitrary_support_has_holonomy_minus_one)
        self.assertTrue(control.representative_dependence_present)

    def test_result_is_conditional_and_does_not_claim_gu_validation(self) -> None:
        self.assertTrue(self.result.finite_proxy_passed)
        self.assertIn("conditional", self.result.h3_status)
        self.assertIn("GU physics is validated", self.result.not_claimed)
        self.assertTrue(
            any(
                "holonomy +1 is equivalent" in claim
                for claim in self.result.not_claimed
            )
        )
        self.assertIn("continuous bipartite Berry", self.result.open_blocker)


if __name__ == "__main__":
    unittest.main()
