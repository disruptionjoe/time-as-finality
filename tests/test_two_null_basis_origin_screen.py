"""Tests for T385 two-null basis origin-principle screen."""

from __future__ import annotations

import unittest

from models.two_null_basis_origin_screen import run_t385_analysis


class TwoNullBasisOriginScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t385_analysis()
        self.verdicts = {verdict.origin_id: verdict for verdict in self.result.verdicts}

    def test_minimal_handshake_is_unique_survivor(self) -> None:
        verdict = self.verdicts["minimal_handshake_origin"]
        self.assertTrue(verdict.passes)
        self.assertEqual(verdict.status, "minimal_handshake_survivor")
        self.assertEqual(verdict.classification, "survivor")
        self.assertTrue(verdict.imports_acknowledgment_premise)
        self.assertTrue(all(criterion.passes for criterion in verdict.criteria))
        self.assertEqual(self.result.surviving_origin_ids, ("minimal_handshake_origin",))
        self.assertTrue(self.result.minimal_handshake_unique_survivor)

    def test_absolute_clock_origin_is_rejected(self) -> None:
        verdict = self.verdicts["absolute_clock_origin"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "rejected_global_time_import")
        self.assertEqual(verdict.classification, "rejected")
        criteria = {criterion.criterion_id: criterion for criterion in verdict.criteria}
        self.assertFalse(criteria["no_global_time_import"].passes)
        self.assertFalse(criteria["local_substrate_coupling"].passes)
        self.assertTrue(self.result.absolute_clock_rejected)

    def test_scalar_and_one_way_origins_fail_for_missing_signal_closure(self) -> None:
        scalar = self.verdicts["scalar_source_action_origin"]
        one_way = self.verdicts["one_way_signal_origin"]

        self.assertEqual(scalar.status, "rejected_no_signal_geometry")
        self.assertFalse(scalar.passes)
        scalar_criteria = {criterion.criterion_id: criterion for criterion in scalar.criteria}
        self.assertFalse(scalar_criteria["directional_signal_geometry"].passes)

        self.assertEqual(one_way.status, "rejected_undercomplete_one_way")
        self.assertFalse(one_way.passes)
        one_way_criteria = {criterion.criterion_id: criterion for criterion in one_way.criteria}
        self.assertTrue(one_way_criteria["directional_signal_geometry"].passes)
        self.assertFalse(one_way_criteria["round_trip_closure"].passes)
        self.assertFalse(one_way_criteria["exactly_two_primitive_directions"].passes)

        self.assertTrue(self.result.scalar_source_action_rejected)
        self.assertTrue(self.result.one_way_signal_rejected)

    def test_overcomplete_broadcast_is_demoted_not_survivor(self) -> None:
        verdict = self.verdicts["overcomplete_broadcast_origin"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "demoted_overcomplete")
        self.assertEqual(verdict.classification, "demoted")
        criteria = {criterion.criterion_id: criterion for criterion in verdict.criteria}
        self.assertFalse(criteria["exactly_two_primitive_directions"].passes)
        self.assertFalse(criteria["minimal_not_overcomplete"].passes)
        self.assertTrue(self.result.overcomplete_broadcast_demoted)

    def test_signed_cancellation_rejected_as_non_source_compatible(self) -> None:
        verdict = self.verdicts["signed_cancellation_origin"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "rejected_signed_source_counts")
        criteria = {criterion.criterion_id: criterion for criterion in verdict.criteria}
        self.assertTrue(criteria["exactly_two_primitive_directions"].passes)
        self.assertFalse(criteria["nonnegative_source_counts"].passes)
        self.assertTrue(self.result.signed_cancellation_rejected)

    def test_gauge_relabel_is_partial_not_an_origin(self) -> None:
        verdict = self.verdicts["gauge_relabel_origin"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "partial_relabel_not_origin")
        self.assertEqual(verdict.classification, "partial")
        self.assertEqual(self.result.partial_origin_ids, ("gauge_relabel_origin",))
        self.assertTrue(self.result.gauge_relabel_partial)

    def test_comparator_ledger_keeps_derivation_boundary_honest(self) -> None:
        comparators = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertTrue(comparators["compatibility_alone_derivation"].absorbs)
        self.assertFalse(comparators["minimal_handshake_origin"].absorbs)
        self.assertTrue(comparators["handshake_premise_origin"].absorbs)
        self.assertFalse(comparators["scalar_or_clock_shortcut"].absorbs)
        self.assertTrue(comparators["catalog_completeness"].absorbs)

    def test_overall_verdict_moves_gap_to_handshake_origin(self) -> None:
        self.assertFalse(self.result.two_null_basis_derived_from_compatibility_alone)
        self.assertTrue(self.result.two_null_basis_minimally_motivated_by_handshake)
        self.assertTrue(self.result.handshake_premise_still_open)
        self.assertEqual(
            self.result.overall_verdict,
            "two_null_basis_minimally_motivated_by_round_trip_handshake_not_derived_from_compatibility_alone",
        )
        self.assertEqual(
            self.result.next_open_object,
            "derive_or_falsify_bidirectional_handshake_origin",
        )
        self.assertIn("handshake_origin", self.result.claim_ledger_update)
        self.assertIn("not derived from compatibility alone", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
