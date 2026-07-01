"""Tests for T386 bidirectional-handshake origin screen."""

from __future__ import annotations

import unittest

from models.bidirectional_handshake_origin_screen import run_t386_analysis


class BidirectionalHandshakeOriginScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t386_analysis()
        self.verdicts = {
            verdict.protocol_id: verdict for verdict in self.result.protocol_verdicts
        }

    def test_minimal_bidirectional_handshake_is_unique_survivor(self) -> None:
        verdict = self.verdicts["minimal_bidirectional_handshake"]
        self.assertTrue(verdict.passes)
        self.assertEqual(verdict.status, "minimal_bidirectional_handshake_survivor")
        self.assertTrue(all(criterion.passes for criterion in verdict.criteria))
        self.assertEqual(
            self.result.surviving_protocol_ids,
            ("minimal_bidirectional_handshake",),
        )
        self.assertTrue(self.result.minimal_bidirectional_handshake_unique_survivor)

    def test_one_sided_and_broadcast_protocols_fail_mutual_pairwise_witnessing(self) -> None:
        one_sided = self.verdicts["one_sided_readout"]
        broadcast = self.verdicts["broadcast_without_ack"]
        self.assertEqual(one_sided.status, "rejected_one_sided_attestation")
        self.assertEqual(broadcast.status, "rejected_not_pairwise_local")

        one_sided_criteria = {
            criterion.criterion_id: criterion for criterion in one_sided.criteria
        }
        broadcast_criteria = {
            criterion.criterion_id: criterion for criterion in broadcast.criteria
        }
        self.assertFalse(one_sided_criteria["mutual_attestability"].passes)
        self.assertFalse(one_sided_criteria["round_trip_closure"].passes)
        self.assertFalse(broadcast_criteria["local_pairwise_relation"].passes)
        self.assertFalse(broadcast_criteria["mutual_attestability"].passes)
        self.assertTrue(self.result.one_sided_readout_rejected)
        self.assertTrue(self.result.broadcast_without_ack_rejected)

    def test_shared_scalar_token_fails_signal_geometry(self) -> None:
        verdict = self.verdicts["shared_scalar_token"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "rejected_no_signal_geometry")
        criteria = {criterion.criterion_id: criterion for criterion in verdict.criteria}
        self.assertTrue(criteria["mutual_attestability"].passes)
        self.assertFalse(criteria["directional_signal_geometry"].passes)
        self.assertFalse(criteria["exactly_two_directed_legs"].passes)
        self.assertTrue(self.result.shared_scalar_token_rejected)

    def test_global_reconciler_is_rejected_as_hidden_ordering_layer(self) -> None:
        verdict = self.verdicts["global_reconciler_receipt"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "rejected_global_reconciler")
        criteria = {criterion.criterion_id: criterion for criterion in verdict.criteria}
        self.assertFalse(criteria["no_global_coordinator"].passes)
        self.assertFalse(criteria["no_hidden_foliation"].passes)
        self.assertTrue(self.result.global_reconciler_rejected)

    def test_signed_anti_handshake_rejected_as_source_incompatible(self) -> None:
        verdict = self.verdicts["signed_anti_handshake"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "rejected_signed_counts")
        criteria = {criterion.criterion_id: criterion for criterion in verdict.criteria}
        self.assertTrue(criteria["exactly_two_directed_legs"].passes)
        self.assertFalse(criteria["nonnegative_source_counts"].passes)
        self.assertTrue(self.result.signed_anti_handshake_rejected)

    def test_overcomplete_and_asymmetric_controls_do_not_pass(self) -> None:
        three_phase = self.verdicts["three_phase_commit_handshake"]
        asymmetric = self.verdicts["asymmetric_receipt_handshake"]
        self.assertEqual(three_phase.status, "demoted_overcomplete_protocol")
        self.assertEqual(three_phase.classification, "demoted")
        self.assertEqual(asymmetric.status, "partial_asymmetric_receipt")
        self.assertEqual(asymmetric.classification, "partial")
        self.assertEqual(self.result.demoted_protocol_ids, ("three_phase_commit_handshake",))
        self.assertEqual(self.result.partial_protocol_ids, ("asymmetric_receipt_handshake",))
        self.assertTrue(self.result.three_phase_commit_demoted)
        self.assertTrue(self.result.asymmetric_receipt_partial)

    def test_derivation_chain_names_boundary_and_next_open_object(self) -> None:
        step_ids = [step.step_id for step in self.result.derivation_steps]
        self.assertEqual(
            step_ids,
            [
                "raw_compatibility_insufficient",
                "mutual_attestability_requires_two_receipts",
                "local_pairwise_no_global_reconciler_requires_signal_exchange",
                "minimal_exchange_has_two_directed_legs",
                "two_legs_feed_t385_two_null_basis",
            ],
        )
        self.assertFalse(self.result.raw_compatibility_derives_handshake)
        self.assertTrue(self.result.mutual_attestability_derives_handshake)
        self.assertTrue(self.result.conditional_origin_chain_to_two_null_basis)
        self.assertEqual(
            self.result.next_open_object,
            "derive_or_falsify_mutual_attestability_semantics",
        )

    def test_comparators_keep_conditional_derivation_honest(self) -> None:
        comparators = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertTrue(comparators["raw_compatibility_derivation"].absorbs)
        self.assertFalse(comparators["mutual_attestability_semantics"].absorbs)
        self.assertFalse(comparators["global_reconciler_shortcut"].absorbs)
        self.assertTrue(comparators["protocol_catalog_completeness"].absorbs)
        self.assertTrue(comparators["mutual_attestability_origin"].absorbs)
        self.assertEqual(
            self.result.overall_verdict,
            "bidirectional_handshake_derived_from_mutual_attestability_not_raw_compatibility",
        )
        self.assertIn("mutual_attestability_origin", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
