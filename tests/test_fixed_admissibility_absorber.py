"""Tests for T376 fixed-admissibility absorber harness."""

from __future__ import annotations

import unittest

from models.fixed_admissibility_absorber import run_t376_analysis


class FixedAdmissibilityAbsorberTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t376_analysis()
        self.by_fixture = {
            verdict.fixture_name: verdict for verdict in self.result.fixture_verdicts
        }

    def test_required_fixtures_are_present(self) -> None:
        self.assertEqual(
            set(self.by_fixture),
            {
                "parity_clock_free_trace",
                "latent_access_trace",
                "projector_zero_mode_trace",
                "nonfixed_threshold_positive_control",
            },
        )

    def test_fixed_predicate_absorbs_parity_trace(self) -> None:
        verdict = self.by_fixture["parity_clock_free_trace"]

        self.assertFalse(verdict.nonfixed_admissibility_needed)
        self.assertIn("fixed_compatibility_predicate", verdict.absorbing_absorbers)
        self.assertEqual(verdict.residue_label, "fixed_admissibility_absorbed")

    def test_fixed_latent_access_absorbs_latent_trace(self) -> None:
        verdict = self.by_fixture["latent_access_trace"]

        self.assertFalse(verdict.nonfixed_admissibility_needed)
        self.assertIn("fixed_latent_source_changing_access", verdict.absorbing_absorbers)
        self.assertEqual(verdict.residue_label, "fixed_admissibility_absorbed")

    def test_fixed_projector_absorbs_zero_mode_trace(self) -> None:
        verdict = self.by_fixture["projector_zero_mode_trace"]

        self.assertFalse(verdict.nonfixed_admissibility_needed)
        self.assertIn("fixed_projector_state_space", verdict.absorbing_absorbers)
        self.assertEqual(verdict.residue_label, "fixed_admissibility_absorbed")

    def test_nonfixed_positive_control_survives_absorbers(self) -> None:
        verdict = self.by_fixture["nonfixed_threshold_positive_control"]

        self.assertTrue(verdict.nonfixed_admissibility_needed)
        self.assertEqual(verdict.absorbing_absorbers, ())
        self.assertEqual(verdict.residue_label, "nonfixed_admissibility_residue")
        self.assertTrue(self.result.nonfixed_positive_control_survives)

    def test_summary_counts_and_claim_boundary(self) -> None:
        self.assertGreaterEqual(self.result.fixed_predicate_absorbs_count, 3)
        self.assertGreaterEqual(self.result.fixed_latent_access_absorbs_count, 3)
        self.assertGreaterEqual(self.result.fixed_projector_absorbs_count, 3)
        self.assertIn("guardrail harness only", self.result.claim_ledger_update)
        self.assertIn("not source-side residue", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
