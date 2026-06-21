"""Tests for T126: finality-colimit causal-set embeddability audit."""

from __future__ import annotations

import unittest

from models.finality_colimit_causal_set_embeddability import (
    audit_finality_colimit_causet,
    audit_poset_axioms,
    canonical_t126_datums,
    complete_bipartite_layer_control,
    cyclic_relation_control,
    degenerate_chain_control,
    grid_filter_pass_control,
    hub_order_control,
    mixed_interval_profile_control,
    non_strict_relation,
    run_t126_analysis,
    t16_positive_poset_control,
)


class FinalityColimitCausalSetEmbeddabilityTests(unittest.TestCase):
    def test_non_strict_relation_adds_reflexive_transitive_closure(self) -> None:
        events = frozenset({"a", "b", "c"})
        relation = non_strict_relation(events, frozenset({("a", "b"), ("b", "c")}))

        self.assertIn(("a", "a"), relation)
        self.assertIn(("a", "c"), relation)
        self.assertTrue(audit_poset_axioms(events, relation).is_poset)

    def test_t16_positive_control_is_causet_candidate_but_too_small(self) -> None:
        audit = audit_finality_colimit_causet(t16_positive_poset_control())

        self.assertTrue(audit.causal_set_candidate)
        self.assertEqual(audit.classification, "insufficient_scale")
        self.assertFalse(audit.manifold_filter_passed)

    def test_descent_and_canonicality_gates_run_before_causet_claims(self) -> None:
        audits = {
            audit.name: audit
            for audit in (
                audit_finality_colimit_causet(datum)
                for datum in canonical_t126_datums()
            )
        }

        self.assertEqual(
            audits["descent_failure_control"].classification,
            "not_descent_datum",
        )
        self.assertEqual(
            audits["noncanonical_boundary_control"].classification,
            "noncanonical_colimit",
        )
        self.assertFalse(audits["descent_failure_control"].causal_set_candidate)

    def test_non_poset_relation_is_rejected(self) -> None:
        audit = audit_finality_colimit_causet(cyclic_relation_control())

        self.assertEqual(audit.classification, "not_poset")
        self.assertFalse(audit.poset_report.antisymmetric)
        self.assertIn("antisymmetry_violation", audit.poset_report.failure_reasons)

    def test_unresolved_phantom_gap_blocks_manifold_filter(self) -> None:
        audits = {
            audit.name: audit
            for audit in (
                audit_finality_colimit_causet(datum)
                for datum in canonical_t126_datums()
            )
        }

        self.assertEqual(
            audits["phantom_gap_control"].classification,
            "phantom_gap_unresolved",
        )
        self.assertFalse(audits["phantom_gap_control"].manifold_filter_passed)

    def test_valid_star_poset_fails_hub_nonlocality_filter(self) -> None:
        audit = audit_finality_colimit_causet(hub_order_control())

        self.assertTrue(audit.poset_report.is_poset)
        self.assertEqual(audit.classification, "hub_nonlocality_obstruction")
        self.assertFalse(audit.manifold_filter_passed)

    def test_complete_bipartite_order_fails_interval_profile_filter(self) -> None:
        audit = audit_finality_colimit_causet(complete_bipartite_layer_control())

        self.assertTrue(audit.poset_report.is_poset)
        self.assertEqual(audit.classification, "interval_profile_obstruction")

    def test_degenerate_chain_fails_rank_width_filter(self) -> None:
        audit = audit_finality_colimit_causet(degenerate_chain_control())

        self.assertTrue(audit.poset_report.is_poset)
        self.assertEqual(audit.classification, "rank_width_obstruction")

    def test_mixed_interval_profiles_fail_dimension_stability_filter(self) -> None:
        audit = audit_finality_colimit_causet(mixed_interval_profile_control())

        self.assertTrue(audit.poset_report.is_poset)
        self.assertEqual(audit.classification, "order_dimension_obstruction")
        assert audit.diagnostics is not None
        self.assertTrue(audit.diagnostics.profile_spread_obstruction)

    def test_grid_control_passes_only_this_necessary_condition_filter(self) -> None:
        audit = audit_finality_colimit_causet(grid_filter_pass_control())

        self.assertTrue(audit.poset_report.is_poset)
        self.assertEqual(audit.classification, "passes_filter_only")
        self.assertTrue(audit.manifold_filter_passed)
        self.assertIn("not a faithful embedding proof", audit.not_claimed)

    def test_t126_aggregate_result(self) -> None:
        result = run_t126_analysis()

        self.assertTrue(result.descent_failures_blocked_before_causet_claims)
        self.assertTrue(result.t16_control_passes_causet_gate)
        self.assertTrue(result.invalid_relations_rejected)
        self.assertTrue(result.valid_posets_can_fail_manifold_filter)
        self.assertTrue(result.passing_filter_does_not_derive_spacetime)
        self.assertIn("not automatically spacetime-like", result.strongest_claim)
        self.assertIn("Add T126 to S1", result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
