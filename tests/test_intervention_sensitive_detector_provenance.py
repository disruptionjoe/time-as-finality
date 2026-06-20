"""Tests for T68: intervention-sensitive detector provenance."""

from __future__ import annotations

import unittest

from models.intervention_sensitive_detector_provenance import (
    analyze_scenario,
    canonical_scenarios,
    run_t68_analysis,
)


class InterventionSensitiveProvenanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.analyses = {
            scenario.name: analyze_scenario(scenario)
            for scenario in canonical_scenarios()
        }

    def test_hostile_pair_has_identical_passive_statistics(self) -> None:
        dependent = self.analyses["dependent_copied_archive_same_passive_stats"]
        independent = self.analyses["independent_readout_same_passive_stats"]

        self.assertEqual(
            dependent.passive_statistics.agreement_probability,
            independent.passive_statistics.agreement_probability,
        )
        self.assertEqual(
            dependent.passive_statistics.phi_correlation,
            independent.passive_statistics.phi_correlation,
        )
        self.assertEqual(dependent.passive_statistics.agreement_probability, 0.92)
        self.assertEqual(dependent.passive_statistics.phi_correlation, 0.84)

    def test_intervention_observables_separate_dependent_copy(self) -> None:
        analysis = self.analyses["dependent_copied_archive_same_passive_stats"]

        self.assertTrue(analysis.observables.delayed_copy_candidate)
        self.assertTrue(analysis.observables.duplicate_origin_tag)
        self.assertTrue(analysis.observables.perturbation_coupling)
        self.assertTrue(analysis.observables.disallowed_shared_ancestry)
        self.assertTrue(analysis.partition.inferred_same_independence_class)
        self.assertTrue(analysis.correctly_classified)

    def test_intervention_observables_separate_independent_readout(self) -> None:
        analysis = self.analyses["independent_readout_same_passive_stats"]

        self.assertFalse(analysis.observables.delayed_copy_candidate)
        self.assertFalse(analysis.observables.duplicate_origin_tag)
        self.assertFalse(analysis.observables.perturbation_coupling)
        self.assertFalse(analysis.observables.disallowed_shared_ancestry)
        self.assertFalse(analysis.partition.inferred_same_independence_class)
        self.assertTrue(analysis.correctly_classified)

    def test_d1_is_computed_after_preregistered_partition(self) -> None:
        dependent = self.analyses["dependent_copied_archive_same_passive_stats"]
        independent = self.analyses["independent_readout_same_passive_stats"]

        self.assertTrue(dependent.partition.pre_registered)
        self.assertFalse(dependent.partition.depends_on_d1_outcome)
        self.assertTrue(independent.partition.pre_registered)
        self.assertFalse(independent.partition.depends_on_d1_outcome)
        self.assertEqual(dependent.d1_profile.as_tuple(), (2, 1, 1, 0))
        self.assertEqual(independent.d1_profile.as_tuple(), (2, 2, 1, 1))
        self.assertFalse(dependent.observer_finalized)
        self.assertTrue(independent.observer_finalized)


class T68ResultTests(unittest.TestCase):
    def test_result_records_conditional_success(self) -> None:
        result = run_t68_analysis()
        statuses = {
            evaluation.hypothesis_id: evaluation.status
            for evaluation in result.hypothesis_evaluations
        }

        self.assertTrue(result.separation_audit.passive_statistics_identical)
        self.assertTrue(result.separation_audit.intervention_partitions_distinct)
        self.assertTrue(result.separation_audit.d1_computed_after_partition)
        self.assertTrue(result.separation_audit.success)
        self.assertEqual(statuses["H1"], "supported")
        self.assertEqual(statuses["H2"], "supported_with_assumptions")
        self.assertEqual(statuses["H3"], "boundary")
        self.assertEqual(statuses["H4"], "weakened")

    def test_claim_language_preserves_metadata_boundary(self) -> None:
        result = run_t68_analysis()

        self.assertIn("causal/provenance metadata", result.weakened_claim)
        self.assertIn("calibrated outcome statistics", result.weakened_claim)
        self.assertIn("clock uncertainty", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
