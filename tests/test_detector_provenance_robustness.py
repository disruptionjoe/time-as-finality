"""Tests for T70: detector provenance robustness."""

from __future__ import annotations

import unittest

from models.detector_provenance_robustness import (
    analyze_witness,
    canonical_regimes,
    canonical_witnesses,
    run_t70_analysis,
)


class DetectorProvenanceRobustnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.regimes = {regime.name: regime for regime in canonical_regimes()}
        self.witnesses = {witness.name: witness for witness in canonical_witnesses()}

    def analysis(self, witness_name: str, regime_name: str):
        return analyze_witness(
            self.witnesses[witness_name],
            self.regimes[regime_name],
        )

    def test_ideal_t68_metadata_still_separates_hostile_pair(self) -> None:
        copied = self.analysis("dependent_copied_archive", "ideal_t68_metadata")
        independent = self.analysis(
            "independent_overlapping_readout",
            "ideal_t68_metadata",
        )

        self.assertTrue(copied.partition.inferred_same_class)
        self.assertFalse(independent.partition.inferred_same_class)
        self.assertEqual(copied.d1_profile.as_tuple(), (2, 1, 1, 0))
        self.assertEqual(independent.d1_profile.as_tuple(), (2, 2, 1, 1))
        self.assertFalse(copied.observer_finalized)
        self.assertTrue(independent.observer_finalized)

    def test_clock_uncertainty_alone_does_not_break_rule(self) -> None:
        copied = self.analysis("dependent_copied_archive", "clock_uncertainty_only")
        independent = self.analysis(
            "independent_overlapping_readout",
            "clock_uncertainty_only",
        )

        self.assertIn("clock_or_latency_timing", copied.evidence.ambiguous_channels)
        self.assertTrue(copied.partition.inferred_same_class)
        self.assertFalse(independent.partition.inferred_same_class)
        self.assertTrue(copied.correctly_classified)
        self.assertTrue(independent.correctly_classified)

    def test_tag_loss_survives_when_intervention_and_dag_remain(self) -> None:
        copied = self.analysis("dependent_copied_archive", "tag_loss_only")
        independent = self.analysis(
            "independent_overlapping_readout",
            "tag_loss_only",
        )

        self.assertIn("tag_loss", copied.evidence.ambiguous_channels)
        self.assertTrue(copied.evidence.perturbation_dependence)
        self.assertTrue(copied.evidence.dag_dependence)
        self.assertTrue(independent.evidence.perturbation_independence)
        self.assertTrue(independent.evidence.dag_independence)
        self.assertTrue(copied.correctly_classified)
        self.assertTrue(independent.correctly_classified)

    def test_forgeable_tags_are_not_used_as_provenance_evidence(self) -> None:
        copied = self.analysis(
            "dependent_copied_archive",
            "tag_spoofing_caught_by_dag_and_intervention",
        )

        self.assertIn(
            "unauthenticated_or_forgeable_tags",
            copied.evidence.ambiguous_channels,
        )
        self.assertFalse(copied.evidence.duplicate_tag_dependence)
        self.assertTrue(copied.evidence.perturbation_dependence)
        self.assertTrue(copied.evidence.dag_dependence)
        self.assertTrue(copied.partition.inferred_same_class)

    def test_missing_strong_channels_abstains_and_withholds_d1(self) -> None:
        copied = self.analysis(
            "dependent_copied_archive",
            "dag_incomplete_tags_lost_back_action",
        )
        independent = self.analysis(
            "independent_overlapping_readout",
            "dag_incomplete_tags_lost_back_action",
        )

        self.assertEqual(copied.partition.status, "undetermined_clean_abstention")
        self.assertEqual(
            independent.partition.status,
            "undetermined_clean_abstention",
        )
        self.assertIsNone(copied.partition.inferred_same_class)
        self.assertIsNone(independent.partition.inferred_same_class)
        self.assertIsNone(copied.d1_profile)
        self.assertIsNone(independent.d1_profile)

    def test_partial_dag_threshold_only_is_marked_not_used(self) -> None:
        copied = self.analysis("dependent_copied_archive", "partial_dag_threshold_only")
        independent = self.analysis(
            "independent_overlapping_readout",
            "partial_dag_threshold_only",
        )

        self.assertTrue(copied.partition.threshold_or_label_dependent)
        self.assertTrue(independent.partition.threshold_or_label_dependent)
        self.assertEqual(
            copied.partition.status,
            "undetermined_threshold_or_label_dependent",
        )
        self.assertIsNone(copied.d1_profile)
        self.assertIsNone(independent.d1_profile)


class T70ResultTests(unittest.TestCase):
    def test_result_contains_survival_clean_failure_and_threshold_failure(self) -> None:
        result = run_t70_analysis()
        verdicts = {summary.verdict for summary in result.robustness_table}

        self.assertIn("survives", verdicts)
        self.assertIn("fails_clean_abstention", verdicts)
        self.assertIn("fails_threshold_or_label_dependent", verdicts)

    def test_minimal_metadata_requirement_rejects_passive_similarity(self) -> None:
        result = run_t70_analysis()

        self.assertIn("authenticated dependence channel", result.minimal_metadata_requirement)
        self.assertIn("Passive similarity", result.minimal_metadata_requirement)
        self.assertIn("withheld", result.weakened_claim + result.q1_recommendation)
        self.assertIn("Do not claim", result.q1_recommendation)

    def test_d1_is_computed_only_after_determined_partition(self) -> None:
        result = run_t70_analysis()

        for analysis in result.witness_analyses:
            if analysis.partition.inferred_same_class is None:
                self.assertIsNone(analysis.d1_profile)
            else:
                self.assertIsNotNone(analysis.d1_profile)
                self.assertTrue(analysis.partition.pre_registered)
                self.assertFalse(analysis.partition.depends_on_d1_outcome)


if __name__ == "__main__":
    unittest.main()


