"""Tests for T72: physical provenance protocol."""

from __future__ import annotations

import unittest

from models.physical_provenance_protocol import (
    analyze_witness,
    canonical_regimes,
    canonical_witnesses,
    run_t72_analysis,
)


class PhysicalProvenanceProtocolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.regimes = {regime.name: regime for regime in canonical_regimes()}
        self.witnesses = {witness.name: witness for witness in canonical_witnesses()}

    def analysis(self, witness_name: str, regime_name: str):
        return analyze_witness(
            self.witnesses[witness_name],
            self.regimes[regime_name],
        )

    def test_robust_protocol_recovers_both_partitions_before_d1(self) -> None:
        copied = self.analysis("dependent_copied_archive", "robust_recovery_protocol")
        independent = self.analysis(
            "independent_overlapping_readout",
            "robust_recovery_protocol",
        )

        self.assertEqual(copied.partition.status, "accepted_same_class")
        self.assertEqual(independent.partition.status, "accepted_distinct_classes")
        self.assertEqual(copied.d1_profile.as_tuple(), (2, 1, 1, 0))
        self.assertEqual(independent.d1_profile.as_tuple(), (2, 2, 1, 1))
        self.assertFalse(copied.observer_finalized)
        self.assertTrue(independent.observer_finalized)

    def test_batched_clock_recovery_does_not_require_timing(self) -> None:
        copied = self.analysis(
            "dependent_copied_archive",
            "batched_clock_crypto_dag_recovery",
        )
        accepted = set(copied.partition.accepted_channels)

        self.assertEqual(copied.partition.status, "accepted_same_class")
        self.assertIn("signed_shared_ancestry", accepted)
        self.assertNotIn("clock_latency_interval", accepted)

    def test_ambiguous_low_trust_withholds_d1(self) -> None:
        copied = self.analysis("dependent_copied_archive", "ambiguous_withhold_low_trust")
        independent = self.analysis(
            "independent_overlapping_readout",
            "ambiguous_withhold_low_trust",
        )

        self.assertEqual(copied.partition.status, "withhold_ambiguous")
        self.assertEqual(independent.partition.status, "withhold_ambiguous")
        self.assertIsNone(copied.d1_profile)
        self.assertIsNone(independent.d1_profile)

    def test_ad_hoc_partial_dag_threshold_withholds_d1(self) -> None:
        copied = self.analysis("dependent_copied_archive", "partial_dag_ad_hoc_threshold")

        self.assertEqual(copied.partition.status, "withhold_threshold_dependent")
        self.assertEqual(copied.partition.threshold_source, "ad_hoc_partial_dag_threshold")
        self.assertIsNone(copied.d1_profile)

    def test_forged_tags_can_create_false_independence_risk(self) -> None:
        copied = self.analysis(
            "dependent_copied_archive",
            "forged_tags_false_independence_risk",
        )

        self.assertEqual(copied.partition.status, "false_independence_risk")
        self.assertFalse(copied.partition.inferred_same_class)
        self.assertFalse(copied.correctly_classified)
        self.assertIn(
            "authenticated_distinct_origin_tags",
            copied.partition.accepted_channels,
        )

    def test_backaction_can_create_false_dependence_risk(self) -> None:
        independent = self.analysis(
            "independent_overlapping_readout",
            "backaction_false_dependence_risk",
        )

        self.assertEqual(independent.partition.status, "false_dependence_risk")
        self.assertTrue(independent.partition.inferred_same_class)
        self.assertFalse(independent.correctly_classified)
        self.assertIn(
            "perturbation_change_response",
            independent.partition.accepted_channels,
        )


class T72ResultTests(unittest.TestCase):
    def test_regime_table_contains_required_outcomes(self) -> None:
        result = run_t72_analysis()
        verdicts = {summary.verdict for summary in result.regime_table}

        self.assertIn("robust_provenance_recovery", verdicts)
        self.assertIn("ambiguous_withhold_region", verdicts)
        self.assertIn("ambiguous_withhold_threshold_dependent", verdicts)
        self.assertIn("false_independence_risk", verdicts)
        self.assertIn("false_dependence_risk", verdicts)

    def test_d1_is_withheld_when_partition_is_not_fixed(self) -> None:
        result = run_t72_analysis()

        for analysis in result.analyses:
            if analysis.partition.inferred_same_class is None:
                self.assertIsNone(analysis.d1_profile)
            else:
                self.assertIsNotNone(analysis.d1_profile)
                self.assertTrue(analysis.partition.pre_registered)
                self.assertFalse(analysis.partition.depends_on_d1_outcome)

    def test_claim_language_rejects_outcome_only_recovery(self) -> None:
        result = run_t72_analysis()

        self.assertIn("protocol-relative", result.weakened_claim)
        self.assertIn("explicit physical protocol assumptions", result.q1_recommendation)
        self.assertIn("cannot be justified independently", result.falsification_condition)


if __name__ == "__main__":
    unittest.main()
