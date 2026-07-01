"""Tests for T388 mutual-attestability semantics origin screen."""

from __future__ import annotations

import unittest

from models.mutual_attestability_semantics_origin_screen import run_t388_analysis


class MutualAttestabilitySemanticsOriginScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t388_analysis()
        self.verdicts = {
            verdict.semantics_id: verdict for verdict in self.result.semantics_verdicts
        }

    def test_finalizable_shared_state_is_unique_survivor(self) -> None:
        verdict = self.verdicts["finalizable_shared_state_compatibility"]
        self.assertTrue(verdict.derives_mutual_attestability)
        self.assertEqual(verdict.status, "record_finality_mutual_attestability_survivor")
        self.assertTrue(all(criterion.passes for criterion in verdict.criteria))
        self.assertEqual(
            self.result.surviving_semantics_ids,
            ("finalizable_shared_state_compatibility",),
        )
        self.assertTrue(self.result.finalizable_shared_state_unique_survivor)

    def test_raw_compatibility_remains_underdetermined(self) -> None:
        verdict = self.verdicts["raw_predicate_compatibility"]
        self.assertFalse(verdict.derives_mutual_attestability)
        self.assertEqual(verdict.status, "underdetermined_raw_predicate")
        criteria = {criterion.criterion_id: criterion for criterion in verdict.criteria}
        self.assertFalse(criteria["shared_record_state"].passes)
        self.assertFalse(criteria["two_endpoint_attestation"].passes)
        self.assertFalse(self.result.raw_compatibility_derives_mutual_attestability)

    def test_symmetric_label_and_scalar_token_do_not_count_as_mutuality(self) -> None:
        label = self.verdicts["symmetric_label_compatibility"]
        scalar = self.verdicts["shared_scalar_token_compatibility"]
        self.assertEqual(label.status, "partial_symmetry_not_attestation")
        self.assertEqual(label.classification, "partial")
        self.assertEqual(scalar.status, "rejected_scalar_token_not_record_state")
        self.assertFalse(scalar.derives_mutual_attestability)

        scalar_criteria = {criterion.criterion_id: criterion for criterion in scalar.criteria}
        self.assertFalse(scalar_criteria["shared_record_state"].passes)
        self.assertFalse(scalar_criteria["not_label_or_scalar_only"].passes)
        self.assertTrue(self.result.symmetric_label_partial)
        self.assertTrue(self.result.scalar_token_rejected)

    def test_one_sided_and_global_reconciled_controls_fail(self) -> None:
        one_sided = self.verdicts["one_sided_readout_compatibility"]
        global_reconciled = self.verdicts["global_reconciled_compatibility"]
        self.assertEqual(one_sided.status, "rejected_one_sided_readout")
        self.assertEqual(global_reconciled.status, "rejected_global_reconciliation")

        global_criteria = {
            criterion.criterion_id: criterion for criterion in global_reconciled.criteria
        }
        self.assertFalse(global_criteria["no_global_reconciler"].passes)
        self.assertFalse(global_criteria["no_hidden_foliation"].passes)
        self.assertTrue(self.result.one_sided_readout_rejected)
        self.assertTrue(self.result.global_reconciler_rejected)

    def test_spoofed_receipts_and_asymmetric_persistence_do_not_pass(self) -> None:
        spoofed = self.verdicts["spoofed_receipt_compatibility"]
        asymmetric = self.verdicts["asymmetric_persistence_compatibility"]
        self.assertEqual(spoofed.status, "rejected_spoofed_or_unowned_receipts")
        self.assertEqual(asymmetric.status, "partial_asymmetric_persistence")
        self.assertEqual(asymmetric.classification, "partial")

        spoofed_criteria = {criterion.criterion_id: criterion for criterion in spoofed.criteria}
        asymmetric_criteria = {
            criterion.criterion_id: criterion for criterion in asymmetric.criteria
        }
        self.assertFalse(spoofed_criteria["source_owned_authentic_receipts"].passes)
        self.assertFalse(asymmetric_criteria["durable_both_sides"].passes)
        self.assertTrue(self.result.spoofed_receipt_rejected)
        self.assertTrue(self.result.asymmetric_persistence_partial)

    def test_derivation_chain_feeds_t386_and_t385(self) -> None:
        step_ids = [step.step_id for step in self.result.derivation_steps]
        self.assertEqual(
            step_ids,
            [
                "raw_compatibility_underdetermined",
                "record_finality_requires_persistent_relation",
                "local_no_global_requires_endpoint_receipts",
                "authentic_two_endpoint_receipts_force_mutuality",
                "mutuality_feeds_t386_t385_chain",
            ],
        )
        self.assertTrue(self.result.record_finality_semantics_derives_mutual_attestability)
        self.assertTrue(self.result.conditional_chain_to_two_null_basis)

    def test_comparators_keep_scope_honest(self) -> None:
        comparators = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertTrue(comparators["raw_compatibility_semantics"].absorbs)
        self.assertFalse(comparators["record_finality_semantics"].absorbs)
        self.assertFalse(comparators["symmetric_label_shortcut"].absorbs)
        self.assertFalse(comparators["receipt_authenticity"].absorbs)
        self.assertTrue(comparators["two_leg_to_null_signal_bridge"].absorbs)
        self.assertTrue(comparators["minimality_principle_origin"].absorbs)

    def test_overall_verdict_moves_next_open_object_to_two_leg_null_bridge(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "mutual_attestability_derived_from_record_finalizable_shared_state_not_raw_compatibility",
        )
        self.assertEqual(self.result.next_open_object, "two_leg_to_null_signal_bridge")
        self.assertIn("record-finalizable shared state", self.result.strongest_claim)
        self.assertIn("raw compatibility remains insufficient", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
