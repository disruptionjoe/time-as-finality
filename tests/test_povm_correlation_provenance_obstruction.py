"""Tests for T67: correlation-threshold provenance obstruction."""

from __future__ import annotations

import unittest

from models.povm_correlation_provenance_obstruction import (
    analyze_scenario,
    best_threshold_audit,
    canonical_scenarios,
    run_t67_analysis,
)


class ScenarioAnalysisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.analyses = {
            scenario.name: analyze_scenario(scenario)
            for scenario in canonical_scenarios()
        }

    def test_dependent_and_independent_overlap_exactly_on_agreement(self) -> None:
        dependent = self.analyses["dependent_transport_noisy"]
        independent = self.analyses["independent_exact_overlap"]

        self.assertEqual(dependent.agreement_probability, 0.92)
        self.assertEqual(independent.agreement_probability, 0.92)
        self.assertEqual(dependent.phi_correlation, 0.84)
        self.assertEqual(independent.phi_correlation, 0.84)
        self.assertNotEqual(
            dependent.scenario.provenance_class,
            independent.scenario.provenance_class,
        )

    def test_independent_high_fidelity_can_exceed_noisy_copy_correlation(self) -> None:
        dependent = self.analyses["dependent_transport_very_noisy"]
        independent = self.analyses["independent_high_fidelity"]

        self.assertGreater(
            independent.agreement_probability,
            dependent.agreement_probability,
        )
        self.assertEqual(dependent.scenario.provenance_class, "dependent_copy")
        self.assertEqual(
            independent.scenario.provenance_class,
            "independent_readout",
        )


class ThresholdAuditTests(unittest.TestCase):
    def test_best_agreement_threshold_still_misclassifies(self) -> None:
        analyses = tuple(self.analyses())
        audit = best_threshold_audit(
            analyses=analyses,
            score_name="agreement_probability",
        )

        self.assertGreaterEqual(audit.error_count, 2)

    def test_best_phi_threshold_still_misclassifies(self) -> None:
        analyses = tuple(self.analyses())
        audit = best_threshold_audit(
            analyses=analyses,
            score_name="phi_correlation",
        )

        self.assertGreaterEqual(audit.error_count, 2)

    @staticmethod
    def analyses():
        return (
            analyze_scenario(scenario)
            for scenario in canonical_scenarios()
        )


class T67ResultTests(unittest.TestCase):
    def test_result_marks_correlation_repair_as_weakened(self) -> None:
        result = run_t67_analysis()
        statuses = {
            evaluation.hypothesis_id: evaluation.status
            for evaluation in result.hypothesis_evaluations
        }

        self.assertEqual(statuses["H1"], "refuted")
        self.assertEqual(statuses["H2"], "refuted")
        self.assertEqual(statuses["H3"], "supported")
        self.assertEqual(statuses["H4"], "supported")
        self.assertEqual(result.overlap_witness.agreement_gap, 0.0)
        self.assertEqual(result.overlap_witness.phi_gap, 0.0)
        self.assertGreaterEqual(
            result.best_agreement_threshold_audit.error_count,
            2,
        )

    def test_recommended_next_mentions_interventions(self) -> None:
        result = run_t67_analysis()

        self.assertIn("intervention", result.recommended_next)
        self.assertIn("provenance", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
