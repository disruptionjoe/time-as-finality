"""Tests for T107: finite loss-relocation audit."""

from __future__ import annotations

import unittest

from models.loss_relocation import analyze_scenario, run_t107_analysis, scenarios


class LossRelocationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scenarios = {scenario.name: scenario for scenario in scenarios()}
        self.result = run_t107_analysis()
        self.verdicts = {verdict.scenario: verdict for verdict in self.result.verdicts}

    def test_charge_loss_derives_reconstruction_debt(self) -> None:
        verdict = analyze_scenario(self.scenarios["charge_neutrality_debt"])

        self.assertEqual(verdict.lost_axis, "charge")
        self.assertEqual(verdict.lift_verdicts, frozenset({True, False}))
        self.assertEqual(verdict.relocation_class, "reconstruction_debt")
        self.assertGreater(len(verdict.derived_witness_pairs), 0)

    def test_gauge_loss_can_be_absorbed(self) -> None:
        verdict = self.verdicts["gauge_representative_absorbed"]

        self.assertEqual(verdict.lost_axis, "gauge")
        self.assertEqual(verdict.lift_verdicts, frozenset({True}))
        self.assertEqual(verdict.relocation_class, "absorbed_freedom")
        self.assertEqual(verdict.derived_witness_pairs, ())

    def test_lorentz_loss_can_stabilize_as_constraint_surface(self) -> None:
        verdict = self.verdicts["lorentz_access_constraint"]

        self.assertEqual(verdict.lost_axis, "lorentz_frame")
        self.assertEqual(verdict.lift_verdicts, frozenset({False}))
        self.assertEqual(verdict.relocation_class, "stable_constraint_surface")

    def test_result_rejects_strong_conservation_language(self) -> None:
        self.assertTrue(self.result.false_conservation_rejected)
        self.assertGreaterEqual(self.result.derived_debt_count, 1)
        self.assertGreaterEqual(self.result.stable_constraint_count, 1)
        self.assertGreaterEqual(self.result.absorbed_freedom_count, 1)
        self.assertIn("there is no conservation law", self.result.strongest_claim)

    def test_debt_is_source_anchored_not_label_declared(self) -> None:
        debt_verdicts = [
            verdict
            for verdict in self.result.verdicts
            if verdict.relocation_class == "reconstruction_debt"
        ]

        self.assertTrue(self.result.source_anchored_derivation)
        self.assertTrue(all(verdict.derived_witness_pairs for verdict in debt_verdicts))


if __name__ == "__main__":
    unittest.main()
