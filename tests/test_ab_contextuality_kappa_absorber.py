"""Tests for T465: AB contextuality kappa absorber."""

from __future__ import annotations

import unittest

from models.ab_contextuality_kappa_absorber import (
    VERDICT,
    audit_claimed_transport,
    build_ab_empirical_model,
    native_ab_obstruction,
    nu_from_ab_empirical_model,
    run,
)
from models.typed_loss_transport import compute_kappa


class TestABNativeObstruction(unittest.TestCase):
    def test_single_contextual_block_has_native_rank_one(self):
        model = build_ab_empirical_model(1, model_id="single")
        native = native_ab_obstruction(model)

        self.assertTrue(native["all_local_sections_exist"])
        self.assertFalse(native["global_section_exists"])
        self.assertEqual(native["native_contextuality_rank"], 1)
        self.assertEqual(native["blocks"][0]["parity_product"], -1)

    def test_balanced_control_has_native_rank_zero(self):
        model = build_ab_empirical_model(0, balanced_blocks=1, model_id="balanced")
        native = native_ab_obstruction(model)

        self.assertTrue(native["all_local_sections_exist"])
        self.assertTrue(native["global_section_exists"])
        self.assertEqual(native["native_contextuality_rank"], 0)
        self.assertEqual(native["blocks"][0]["parity_product"], 1)

    def test_mixed_blocks_count_only_contextual_components(self):
        model = build_ab_empirical_model(
            2,
            balanced_blocks=1,
            model_id="mixed",
        )
        native = native_ab_obstruction(model)

        self.assertEqual(native["native_contextuality_rank"], 2)
        self.assertEqual(len(native["blocks"]), 3)


class TestKappaAbsorption(unittest.TestCase):
    def test_kappa_on_same_support_matches_native_ab_rank(self):
        for k in (1, 2, 3):
            with self.subTest(k=k):
                model = build_ab_empirical_model(k, model_id=f"k{k}")
                native = native_ab_obstruction(model)
                kappa = compute_kappa(nu_from_ab_empirical_model(model))

                self.assertEqual(kappa.kappa, k)
                self.assertEqual(kappa.kappa, native["native_contextuality_rank"])

    def test_balanced_control_kappa_zero(self):
        model = build_ab_empirical_model(0, balanced_blocks=1, model_id="balanced")
        kappa = compute_kappa(nu_from_ab_empirical_model(model))

        self.assertEqual(kappa.kappa, 0)
        self.assertTrue(kappa.global_section_exists)

    def test_native_obstruction_does_not_call_compute_kappa(self):
        self.assertNotIn("compute_kappa", native_ab_obstruction.__code__.co_names)

    def test_audit_labels_paired_fixture_as_reencoding_not_prediction(self):
        model = build_ab_empirical_model(2, model_id="paired")
        audit = audit_claimed_transport(model)

        self.assertTrue(audit.pairing_passes)
        self.assertTrue(audit.transport_map_is_identity_on_integer_k)
        self.assertFalse(audit.independent_prediction_branch)
        self.assertTrue(audit.native_and_kappa_read_same_support_table)
        self.assertEqual(audit.gate_label, "NATIVE_H1_REENCODING_NOT_PREDICTION")

    def test_mismatch_control_fails(self):
        model = build_ab_empirical_model(1, model_id="mismatch")
        audit = audit_claimed_transport(model, claimed_source_kappa=2)

        self.assertFalse(audit.pairing_passes)
        self.assertFalse(audit.transport_map_is_identity_on_integer_k)
        self.assertEqual(audit.native_ab_rank, 1)
        self.assertEqual(audit.kappa_from_same_support_cover, 1)
        self.assertEqual(audit.gate_label, "MISMATCH_CONTROL_FAILS_AS_EXPECTED")


class TestT465Protocol(unittest.TestCase):
    def test_overall_verdict_and_boundaries(self):
        result = run()
        findings = result["absorber_findings"]

        self.assertEqual(result["overall_verdict"]["verdict"], VERDICT)
        self.assertTrue(findings["paired_fixtures_pass"])
        self.assertTrue(findings["paired_fixtures_are_identity_on_integer_k"])
        self.assertTrue(findings["native_and_kappa_read_same_support_table"])
        self.assertFalse(findings["independent_prediction_branch_present"])
        self.assertTrue(findings["mismatch_control_fails"])
        self.assertFalse(findings["t224_promotion_earned"])
        self.assertFalse(findings["genre_agnostic_theorem_earned"])
        self.assertEqual(result["overall_verdict"]["claim_movement"], "none")

    def test_no_overclaim_items_are_explicit(self):
        result = run()
        not_earned = set(result["not_earned"])

        self.assertIn("T224 promotion", not_earned)
        self.assertIn("genre-agnostic kappa theorem", not_earned)
        self.assertIn("physics or quantum prediction", not_earned)
        self.assertIn("claim-ledger movement", not_earned)


if __name__ == "__main__":
    unittest.main()
