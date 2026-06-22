"""Tests for T170 Q1D correlation-record timing guardrail."""

from __future__ import annotations

import unittest
from math import sqrt

from models.q1d_correlation_record_guardrail import (
    audit_correlation_record_scenario,
    canonical_q1d_guardrail_scenarios,
    run_t170_analysis,
)


class Q1DCorrelationRecordGuardrailTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t170_analysis()
        self.audits = {audit.scenario_id: audit for audit in self.result.audits}
        self.scenarios = {
            scenario.scenario_id: scenario
            for scenario in canonical_q1d_guardrail_scenarios()
        }

    def test_quantum_contextual_record_passes_only_as_guardrail(self) -> None:
        audit = self.audits["quantum_contextual_reconciled_record"]

        self.assertTrue(audit.no_signalling)
        self.assertAlmostEqual(audit.max_chsh_score, 2.0 * sqrt(2.0))
        self.assertTrue(audit.violates_classical_bound)
        self.assertFalse(audit.exceeds_tsirelson_bound)
        self.assertEqual(
            audit.classification,
            "admissible_contextual_reconciliation_record",
        )
        self.assertIn("only after causal reconciliation", audit.allowed_language)

    def test_signalling_marginal_leak_is_null(self) -> None:
        audit = self.audits["signalling_remote_setting_leak"]

        self.assertFalse(audit.no_signalling)
        self.assertGreater(audit.max_marginal_delta, 0.0)
        self.assertEqual(audit.classification, "null_signalling_local_record")
        self.assertIn("remote setting", audit.rejected_language)

    def test_hidden_variable_retrofit_is_null(self) -> None:
        audit = self.audits["hidden_variable_retrofit"]

        self.assertTrue(audit.no_signalling)
        self.assertTrue(audit.claims_prior_local_values)
        self.assertTrue(audit.violates_classical_bound)
        self.assertEqual(audit.classification, "null_hidden_variable_overclaim")

    def test_premature_correlation_export_is_null(self) -> None:
        audit = self.audits["premature_correlation_export"]

        self.assertTrue(audit.no_signalling)
        self.assertEqual(audit.correlation_record_stage, "local_record_stage")
        self.assertEqual(audit.classification, "null_premature_correlation_record")
        self.assertIn("before the parties can compare", audit.rejected_language)

    def test_pr_box_is_guardrail_only_unless_mislabelled_quantum(self) -> None:
        guardrail = self.audits["pr_box_no_signalling_guardrail_only"]
        mislabelled = self.audits["pr_box_mislabelled_quantum_prediction"]

        self.assertTrue(guardrail.no_signalling)
        self.assertEqual(guardrail.max_chsh_score, 4.0)
        self.assertTrue(guardrail.exceeds_tsirelson_bound)
        self.assertEqual(
            guardrail.classification,
            "postquantum_no_signalling_guardrail_only",
        )
        self.assertEqual(
            mislabelled.classification,
            "null_postquantum_as_quantum_prediction",
        )

    def test_classical_global_baseline_does_not_support_q1d_upgrade(self) -> None:
        audit = self.audits["classical_reconciled_baseline"]

        self.assertTrue(audit.no_signalling)
        self.assertFalse(audit.violates_classical_bound)
        self.assertEqual(audit.classification, "classical_reconciliation_baseline")

    def test_direct_and_wrapped_audits_match(self) -> None:
        scenario = self.scenarios["quantum_contextual_reconciled_record"]
        direct = audit_correlation_record_scenario(scenario)
        wrapped = self.audits["quantum_contextual_reconciled_record"]

        self.assertEqual(direct.classification, wrapped.classification)
        self.assertEqual(direct.max_chsh_score, wrapped.max_chsh_score)

    def test_result_language_keeps_q1d_guardrail_only(self) -> None:
        self.assertEqual(
            self.result.admissible_contextual_guardrails,
            ("quantum_contextual_reconciled_record",),
        )
        self.assertIn("Q1D remains guardrail-only", self.result.q1d_update)
        self.assertIn("no new Bell inequality", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
