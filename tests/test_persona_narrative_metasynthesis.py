"""Tests for T389 persona narrative metasynthesis."""

from __future__ import annotations

import unittest

from models.persona_narrative_metasynthesis import run_t389_analysis


class PersonaNarrativeMetasynthesisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t389_analysis()

    def test_uses_all_ten_personas(self) -> None:
        self.assertEqual(self.result.persona_count, 10)
        self.assertEqual(len(self.result.persona_passes), 10)
        self.assertEqual(
            {item.persona_id for item in self.result.persona_passes},
            set(self.result.persona_ids),
        )
        self.assertIn("relativity_physicist", self.result.persona_ids)
        self.assertIn("paper_reviewer", self.result.persona_ids)

    def test_persona_passes_have_narrative_science_and_warning(self) -> None:
        for item in self.result.persona_passes:
            self.assertGreater(len(item.narrative_steelman), 40)
            self.assertGreater(len(item.scientific_reverse), 40)
            self.assertGreater(len(item.key_warning), 20)

    def test_plain_english_narrative_names_record_finality_and_observer_rendering(self) -> None:
        narrative = self.result.plain_english_narrative
        self.assertIn("spacetime is not being assumed first", narrative)
        self.assertIn("final records", narrative)
        self.assertIn("durable, authentic local receipts", narrative)
        self.assertIn("relativity-like", narrative)

    def test_scientific_story_preserves_conditional_boundaries(self) -> None:
        by_id = {item.story_id: item for item in self.result.scientific_story}
        self.assertEqual(by_id["relativity_pattern"].status, "conditional_pattern_theorem")
        self.assertEqual(by_id["mutuality_origin"].status, "derived_under_record_finality_semantics")
        self.assertEqual(by_id["live_frontier"].status, "open")
        self.assertIn("nullness", by_id["relativity_pattern"].open_risk)
        self.assertIn("two_leg_to_null_signal_bridge", by_id["live_frontier"].open_risk)

    def test_hegelian_analysis_has_expected_moments(self) -> None:
        moment_ids = [item.moment_id for item in self.result.hegelian_analysis]
        self.assertEqual(
            moment_ids,
            ["thesis", "antithesis", "synthesis", "new_contradiction", "next_movement"],
        )
        synthesis = self.result.hegelian_analysis[2]
        self.assertIn("invariant way", synthesis.statement)
        self.assertIn("conditional", synthesis.pressure)

    def test_metasynthesis_refuses_claim_upgrade_and_selects_next_frontier(self) -> None:
        self.assertFalse(self.result.claim_upgrade_allowed)
        self.assertEqual(self.result.next_open_object, "two_leg_to_null_signal_bridge")
        self.assertIn("conditional scientific program", self.result.metasynthesis)
        self.assertIn("null geometry", self.result.metasynthesis)

    def test_conditional_chain_keeps_null_bridge_explicit(self) -> None:
        self.assertEqual(
            self.result.conditional_chain,
            (
                "record-finalizable shared-state compatibility",
                "mutual local attestability",
                "minimal bidirectional handshake",
                "two primitive signal directions",
                "two-null basis only if nullness/bilinearity bridge holds",
                "Lorentz-pattern observer rendering",
            ),
        )

    def test_recommended_next_goal_targets_two_leg_to_null_screen(self) -> None:
        self.assertIn("T390", self.result.recommended_next_goal)
        self.assertIn("two-leg-to-null signal bridge", self.result.recommended_next_goal)
        self.assertIn("timelike", self.result.recommended_next_goal)
        self.assertIn("no claim upgrade", self.result.claim_ledger_update)
        self.assertEqual(
            self.result.overall_verdict,
            "persona_metasynthesis_supports_conditional_record_finality_narrative_and_prioritizes_two_leg_to_null_bridge",
        )


if __name__ == "__main__":
    unittest.main()
