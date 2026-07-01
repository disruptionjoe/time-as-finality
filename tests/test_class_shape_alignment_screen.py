"""Tests for T390 class-shape alignment screen."""

from __future__ import annotations

import unittest

from models.class_shape_alignment_screen import run_t390_analysis


class ClassShapeAlignmentScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t390_analysis()
        self.verdicts = {
            verdict.alignment_id: verdict for verdict in self.result.alignment_verdicts
        }
        self.facts = {fact.fact_id: fact for fact in self.result.source_facts}
        self.cautions = {
            caution.caution_id: caution
            for caution in self.result.temporal_issuance_cautions
        }

    def test_uses_class_material_not_gu_vindication(self) -> None:
        self.assertTrue(self.result.uses_class_not_gu_specific)
        self.assertIn("class_not_gu_specific", self.facts)
        self.assertIn("GU-independent", self.facts["class_not_gu_specific"].statement)
        comparators = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertEqual(comparators["gu_specific_vindication"].status, "rejected_scope")

    def test_source_facts_include_class_boundary_source_action_and_forgetful_map(self) -> None:
        expected = {
            "class_not_gu_specific",
            "observer_universe_external_boundary",
            "class_structural_law_external_count",
            "missing_source_action_spec",
            "source_action_observer_slice_killed",
            "forgetful_image_relation_side",
            "riemannian_ehresmannian_shadow",
            "truth_seeking_posture",
        }
        self.assertEqual(set(self.facts), expected)
        self.assertIn("source action", self.facts["missing_source_action_spec"].statement)
        self.assertIn("forced analogy", self.facts["source_action_observer_slice_killed"].statement)
        self.assertIn("forgetful shadows", self.facts["forgetful_image_relation_side"].statement)

    def test_temporal_issuance_cautions_demote_shadow_definiteness(self) -> None:
        expected = {
            "record_table_demoted_to_interface",
            "external_completion_absorbs_lc_witness",
            "projection_access_negative_rejected",
            "candidate_scout_not_evidence",
        }
        self.assertEqual(set(self.cautions), expected)
        self.assertTrue(self.result.temporal_issuance_demotes_shadow_definiteness)
        self.assertTrue(self.result.shadow_projection_definiteness_rejected)
        self.assertIn(
            "interface vocabulary",
            self.cautions["record_table_demoted_to_interface"].statement,
        )
        self.assertIn(
            "fixed-source",
            self.cautions["projection_access_negative_rejected"].consequence_for_taf,
        )

    def test_shadow_projection_is_cautionary_heuristic_not_direct_null_derivation(self) -> None:
        self.assertFalse(self.result.class_material_resolves_two_leg_to_null_bridge)
        self.assertTrue(self.result.class_material_supplies_testable_bridge_hypothesis)
        self.assertNotIn("taf_finality_to_class_forgetful_shadow", self.result.strongest_fit_ids)
        self.assertEqual(
            self.verdicts["taf_finality_to_class_forgetful_shadow"].classification,
            "cautionary_bridge_heuristic",
        )
        self.assertIn(
            "absorbed by fixed",
            self.verdicts["taf_finality_to_class_forgetful_shadow"].reason,
        )
        self.assertFalse(
            self.verdicts[
                "taf_two_leg_to_ehresmannian_hidden_mechanism"
            ].resolves_two_leg_to_null_bridge
        )
        self.assertIn(
            "controls",
            self.verdicts["taf_two_leg_to_ehresmannian_hidden_mechanism"].reason,
        )

    def test_source_action_observer_slice_mapping_is_rejected(self) -> None:
        verdict = self.verdicts["taf_handshake_as_source_action_observer_slice"]
        self.assertEqual(verdict.classification, "rejected_overfit")
        self.assertEqual(verdict.fit_strength, "none")
        self.assertIn("forced analogy", verdict.reason)
        self.assertTrue(self.result.source_action_observer_slice_rejected)

    def test_generation_chirality_and_direct_14d_mappings_are_rejected(self) -> None:
        generation = self.verdicts["taf_two_null_basis_to_generation_chirality"]
        direct_14d = self.verdicts["taf_two_legs_as_14d_class_identity"]
        self.assertEqual(generation.classification, "rejected_overfit")
        self.assertEqual(direct_14d.classification, "rejected_overfit")
        self.assertTrue(self.result.generation_chirality_mapping_rejected)
        self.assertTrue(self.result.direct_14d_to_two_leg_identity_rejected)
        self.assertIn("not the same object", generation.reason)
        self.assertIn("not identical", direct_14d.reason)

    def test_nullness_remains_open_after_alignment(self) -> None:
        verdict = self.verdicts["taf_nullness_from_class_material"]
        self.assertEqual(verdict.classification, "open_not_resolved")
        self.assertFalse(verdict.resolves_two_leg_to_null_bridge)
        self.assertIn("does not by itself derive", verdict.reason)
        comparators = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertTrue(comparators["two_leg_to_null_bridge"].absorbs)
        self.assertTrue(comparators["forgetful_shadow_hypothesis"].absorbs)
        self.assertEqual(
            comparators["forgetful_shadow_hypothesis"].status,
            "demoted_to_cautionary_heuristic",
        )
        self.assertEqual(
            comparators["temporal_issuance_projection_absorber"].status,
            "active_caution",
        )

    def test_overall_verdict_and_claim_ledger_are_honest(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "class_material_suggests_shadow_heuristic_but_temporal_issuance_rejects_definite_projection_metaphor",
        )
        self.assertIn("does not solve", self.result.strongest_claim)
        self.assertIn("cannot be treated as definitely correct", self.result.strongest_claim)
        self.assertIn("overfits", self.result.strongest_claim)
        self.assertIn("hypothesis generator", self.result.claim_ledger_update)
        self.assertIn("definitive shadow metaphor", self.result.claim_ledger_update)

    def test_recommended_next_goal_is_projection_metaphor_absorber_screen(self) -> None:
        self.assertIn("T391", self.result.recommended_next_goal)
        self.assertIn("projection-metaphor absorber screen", self.result.recommended_next_goal)
        self.assertIn("fixed-source", self.result.recommended_next_goal)
        self.assertIn("bounded-access", self.result.recommended_next_goal)
        self.assertIn("source-action", self.result.recommended_next_goal)
        self.assertIn("generation/chirality", self.result.recommended_next_goal)


if __name__ == "__main__":
    unittest.main()
