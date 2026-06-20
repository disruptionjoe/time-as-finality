"""Tests for T74: provenance protocol Monte Carlo audit."""

from __future__ import annotations

import unittest

from models.provenance_protocol_monte_carlo import (
    SAMPLE_COUNT,
    SEED,
    prior_families,
    run_t74_analysis,
)


class ProvenanceProtocolMonteCarloTests(unittest.TestCase):
    def test_prior_family_count_is_stable(self) -> None:
        self.assertEqual(len(prior_families()), 3)

    def test_monte_carlo_uses_fixed_seed_and_sample_count(self) -> None:
        result = run_t74_analysis()

        self.assertEqual(result.seed, SEED)
        self.assertEqual(result.sample_count, SAMPLE_COUNT)
        for outcome in result.family_outcomes.values():
            self.assertEqual(outcome.sample_count, SAMPLE_COUNT)

    def test_engineered_prior_has_highest_robust_recovery_rate(self) -> None:
        result = run_t74_analysis()
        engineered = result.family_outcomes["engineered_lab"]
        mixed = result.family_outcomes["mixed_lab"]
        degraded = result.family_outcomes["field_degraded"]

        self.assertGreater(engineered.robust_rate, mixed.robust_rate)
        self.assertGreater(engineered.robust_rate, degraded.robust_rate)
        self.assertEqual(mixed.robust_rate, 0.0)
        self.assertEqual(degraded.robust_rate, 0.0)

    def test_mixed_and_degraded_priors_are_not_robust_majority_regimes(self) -> None:
        result = run_t74_analysis()
        mixed = result.family_outcomes["mixed_lab"]
        degraded = result.family_outcomes["field_degraded"]

        self.assertLess(mixed.robust_rate, 0.5)
        self.assertLess(degraded.robust_rate, 0.2)
        self.assertGreater(
            mixed.withhold_rate + mixed.false_independence_rate + mixed.false_dependence_rate,
            mixed.robust_rate,
        )
        self.assertGreater(
            degraded.withhold_rate + degraded.threshold_dependent_rate,
            0.5,
        )

    def test_engineered_prior_d1_is_usually_computable(self) -> None:
        result = run_t74_analysis()
        engineered = result.family_outcomes["engineered_lab"]

        self.assertGreater(engineered.computable_d1_rate, 0.7)
        self.assertGreater(engineered.robust_rate, 0.6)


if __name__ == "__main__":
    unittest.main()
