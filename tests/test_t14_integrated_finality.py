"""Unit tests for T14: integrated observer-context finality."""

from __future__ import annotations

import unittest

from models.t14_integrated_finality import (
    build_integrated_scenario,
    run_t14_analysis,
)


class IntegratedObserverContextTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph, self.observers, self.hidden_state = build_integrated_scenario()

    def test_coupling_profile_changes_finality_and_readout(self) -> None:
        core = self.graph.profile_for(self.observers["core"], "X", "true", 1)
        grav_only = self.graph.profile_for(self.observers["grav_only"], "X", "true", 1)
        self.assertEqual(core, (3, 3, 1, 3))
        self.assertEqual(grav_only, (2, 2, 1, 2))
        self.assertEqual(self.graph.readout_for(self.observers["core"], "X", "true"), 1.0)
        self.assertEqual(
            self.graph.readout_for(self.observers["grav_only"], "X", "true"),
            4.0,
        )

    def test_inherited_expression_changes_visibility_not_stored_identity(self) -> None:
        silenced = self.observers["phase_silenced"]
        self.assertEqual(self.graph.stored_record_count(), 5)
        self.assertEqual(
            [record.record_id for record in self.graph.visible_records(silenced)],
            ["r1", "r3"],
        )
        self.assertEqual(self.graph.profile_for(silenced, "X", "true", 1), (2, 2, 1, 2))
        self.assertEqual(self.graph.readout_for(silenced, "X", "true"), 4.0)

    def test_proofs_reject_forgery_but_not_valid_dissent(self) -> None:
        verified = self.observers["verified_social"]
        raw = self.observers["raw_social"]
        self.assertIn("r4-forged", self.graph.rejected_forged_record_ids(verified))
        self.assertIn("r5-valid-dissent", self.graph.valid_dissent_record_ids(verified))
        self.assertIn("r4-forged", [record.record_id for record in self.graph.visible_records(raw)])
        self.assertNotIn(
            "r4-forged",
            [record.record_id for record in self.graph.visible_records(verified)],
        )

    def test_same_profile_can_have_different_signed_readout(self) -> None:
        destructive, destructive_observers, _ = build_integrated_scenario(
            destructive_phase=True
        )
        constructive, constructive_observers, _ = build_integrated_scenario(
            destructive_phase=False
        )
        destructive_profile = destructive.profile_for(
            destructive_observers["core"], "X", "true", 1
        )
        constructive_profile = constructive.profile_for(
            constructive_observers["core"], "X", "true", 1
        )
        self.assertEqual(destructive_profile, constructive_profile)
        self.assertEqual(destructive_profile, (3, 3, 1, 3))
        self.assertEqual(
            destructive.readout_for(destructive_observers["core"], "X", "true"),
            1.0,
        )
        self.assertEqual(
            constructive.readout_for(constructive_observers["core"], "X", "true"),
            9.0,
        )

    def test_full_analysis_reports_consensus_limit(self) -> None:
        result = run_t14_analysis()
        forged = result["consensus_probe"]["forged"]
        valid_dissent = result["consensus_probe"]["valid_dissent"]
        self.assertLess(
            forged["proof_snowball"]["false_finality_rate"],
            forged["raw_snowball"]["false_finality_rate"],
        )
        self.assertGreater(
            valid_dissent["proof_snowball"]["false_finality_rate"],
            0.0,
        )
        self.assertTrue(result["verdict"]["consensus_confidence_is_not_truth"])


if __name__ == "__main__":
    unittest.main()
