"""Tests for T108: loss-relocation prior-art audit."""

from __future__ import annotations

import unittest

from models.loss_relocation_prior_art import run_t108_analysis


class LossRelocationPriorArtTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t108_analysis()
        self.audits = {audit.neighbor: audit for audit in self.result.audits}

    def test_no_strict_separation_is_claimed(self) -> None:
        self.assertFalse(self.result.strict_separation_from_all_neighbors)
        self.assertIn("does not currently separate", self.result.strongest_claim)

    def test_abstract_interpretation_absorbs_source_fiber_rule(self) -> None:
        audit = self.audits["abstract_interpretation"]

        self.assertEqual(audit.verdict, "absorbed")
        self.assertTrue(audit.absorbs_reconstruction_debt)
        self.assertTrue(audit.absorbs_stable_constraint)
        self.assertTrue(audit.absorbs_absorbed_freedom)

    def test_label_only_loss_still_fails_against_rich_effects(self) -> None:
        audit = self.audits["effect_annotations"]

        self.assertTrue(self.result.label_only_loss_refuted_again)
        self.assertEqual(audit.verdict, "absorbed_by_rich_effects_not_label_only")
        self.assertIn("canonical", audit.remaining_delta)

    def test_surviving_delta_is_typed_normal_form_not_new_obstruction(self) -> None:
        self.assertIn("typed normal form", self.result.claim_ledger_update)
        self.assertIn("not a new obstruction mechanism", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
