"""Tests for consensus parametric tradeoff classification."""

from __future__ import annotations

import unittest

from models.consensus_parametric_tradeoff import (
    ParameterSurface,
    classify_regime,
    generate_protocol_space,
    run_consensus_parametric_tradeoff_analysis,
    verify_parameter_point,
)
from models.consensus_finality_crosswalk import D1Vector


class ParameterSurfaceTests(unittest.TestCase):
    def test_t17_finite_caps_are_named(self) -> None:
        surface = ParameterSurface()

        self.assertEqual(surface.max_nodes, 6)
        self.assertEqual(surface.max_branches, 4)
        self.assertEqual(surface.max_confirmations, 4)
        self.assertEqual(surface.max_timeout, 4)
        self.assertEqual(surface.canonical_budget, 10)
        self.assertEqual(surface.canonical_adversarial_delay, 2)

    def test_protocol_space_uses_named_caps(self) -> None:
        surface = ParameterSurface()
        evaluations = generate_protocol_space(surface, budget=32, adversarial_delay=8)

        self.assertTrue(evaluations)
        self.assertLessEqual(max(item.config.nodes for item in evaluations), 6)
        self.assertLessEqual(max(item.config.branches for item in evaluations), 4)
        self.assertLessEqual(
            max(item.config.confirmations for item in evaluations),
            4,
        )
        self.assertLessEqual(
            max(item.config.timeout_rounds for item in evaluations),
            4,
        )


class PointClassificationTests(unittest.TestCase):
    def test_canonical_t17_point_is_preserved_tradeoff(self) -> None:
        result = verify_parameter_point(
            ParameterSurface(),
            budget=10,
            adversarial_delay=2,
        )

        self.assertTrue(result.holds)
        self.assertEqual(result.regime, "canonical_tradeoff")
        self.assertEqual(result.objective_maxima(), (4, 4, 3, 9, 1))
        self.assertEqual(result.joint_maximizers, ())

    def test_degenerate_low_budget_failure_is_minimal(self) -> None:
        result = verify_parameter_point(
            ParameterSurface(),
            budget=4,
            adversarial_delay=1,
        )

        self.assertFalse(result.holds)
        self.assertEqual(result.regime, "degenerate")
        self.assertEqual(result.objective_maxima(), (1, 1, 1, 1, 1))
        self.assertEqual(
            [item.config.name for item in result.joint_maximizers],
            ["n1-q1-b1-c1-t1"],
        )

    def test_saturated_failure_matches_scout_boundary(self) -> None:
        result = verify_parameter_point(
            ParameterSurface(),
            budget=16,
            adversarial_delay=4,
        )

        self.assertFalse(result.holds)
        self.assertEqual(result.regime, "saturated")
        self.assertEqual(result.objective_maxima(), (4, 4, 4, 16, 1))
        self.assertIn(
            "n4-q4-b4-c4-t4",
            {item.config.name for item in result.joint_maximizers},
        )

    def test_scarcity_window_preserves_tradeoff_before_saturation(self) -> None:
        result = verify_parameter_point(
            ParameterSurface(),
            budget=15,
            adversarial_delay=4,
        )

        self.assertTrue(result.holds)
        self.assertEqual(result.regime, "scarcity")

    def test_regime_classifier_keeps_unknown_failures_separate(self) -> None:
        regime, reason = classify_regime(
            surface=ParameterSurface(),
            budget=12,
            adversarial_delay=2,
            component_maxima=D1Vector(2, 2, 2, 6),
            progress_maximum=1,
            joint_maximizers=(object(),),  # type: ignore[arg-type]
        )

        self.assertEqual(regime, "collapse_no_tradeoff")
        self.assertIn("outside", reason)


class ConsensusParametricTradeoffResultTests(unittest.TestCase):
    def test_grid_contains_all_required_regimes(self) -> None:
        result = run_consensus_parametric_tradeoff_analysis()

        self.assertGreater(result.regime_counts["degenerate"], 0)
        self.assertGreater(result.regime_counts["scarcity"], 0)
        self.assertEqual(result.regime_counts["canonical_tradeoff"], 1)
        self.assertGreater(result.regime_counts["saturated"], 0)
        self.assertNotIn("collapse_no_tradeoff", result.regime_counts)

    def test_minimal_conditions_record_preserved_and_failure_regions(self) -> None:
        result = run_consensus_parametric_tradeoff_analysis()
        conditions = result.minimal_conditions

        self.assertEqual(conditions.minimal_preserved_point.budget, 6)
        self.assertEqual(conditions.minimal_preserved_point.adversarial_delay, 1)
        self.assertEqual(
            conditions.minimal_degenerate_failure.point.budget,
            4,
        )
        self.assertEqual(
            conditions.minimal_saturated_failure.point.budget,
            16,
        )
        self.assertIsNone(conditions.minimal_collapse_failure)

    def test_preserved_windows_include_canonical_and_scarcity(self) -> None:
        result = run_consensus_parametric_tradeoff_analysis()
        windows = {
            (
                window.adversarial_delay,
                window.start_budget,
                window.end_budget,
                window.regime,
            )
            for window in result.minimal_conditions.preserved_tradeoff_windows
        }

        self.assertIn((2, 10, 10, "canonical_tradeoff"), windows)
        self.assertIn((4, 6, 15, "scarcity"), windows)

    def test_recommendation_keeps_rl003_parameter_conditioned(self) -> None:
        result = run_consensus_parametric_tradeoff_analysis()

        self.assertIn("bounded theorem", result.minimal_conditions.recommendation)
        self.assertIn("parameter conditions", result.minimal_conditions.recommendation)
        self.assertIn("No claim status changes", result.claim_impact)


if __name__ == "__main__":
    unittest.main()
