"""Tests for T87: real-run raw-log contract."""

from __future__ import annotations

import unittest

from models.measured_detector_provenance_posterior import DeploymentEvidence
from models.real_run_raw_log_contract import (
    REQUIRED_CHANNEL_ISOLATION_TESTS,
    REQUIRED_TABLE_COLUMNS,
    REQUIRED_T86_CONTROL_ROLES,
    TABLE_TO_T76_FIELDS,
    audit_raw_log_contract,
    complete_t86_real_run_contract,
    dag_export_without_raw_edges_contract,
    dashboard_only_summary_contract,
    missing_copied_independent_labels_contract,
    posthoc_policy_and_demotion_contract,
    run_t87_analysis,
    unlinked_event_tables_contract,
)


class RealRunRawLogContractTests(unittest.TestCase):
    def test_complete_contract_is_admissible_but_only_as_population_gate(self) -> None:
        audit = audit_raw_log_contract(complete_t86_real_run_contract())

        self.assertEqual(audit.verdict, "admissible_for_t86_real_log_population")
        self.assertEqual(audit.failure_reasons, ())
        self.assertEqual(
            audit.next_allowed_audit,
            "populate_t76_t86_counts_without_schema_changes",
        )

    def test_required_tables_cover_every_t76_evidence_field(self) -> None:
        mapped_fields = {
            field
            for fields in TABLE_TO_T76_FIELDS.values()
            for field in fields
        }
        t76_fields = {
            field
            for field in DeploymentEvidence.__dataclass_fields__
            if field not in {"name", "purpose"}
        }

        self.assertEqual(mapped_fields, t76_fields)
        self.assertIn("perturbation_trial_log", REQUIRED_TABLE_COLUMNS)
        self.assertIn("ancestry_dag_edge_export", REQUIRED_TABLE_COLUMNS)

    def test_dashboard_only_summary_is_rejected_before_scoring(self) -> None:
        audit = audit_raw_log_contract(dashboard_only_summary_contract())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn("no_real_raw_deployment_log", audit.failure_reasons)
        self.assertIn("fixture_counts_only", audit.failure_reasons)
        self.assertIn("missing_required_raw_log_tables", audit.failure_reasons)
        self.assertIn(
            "raw_tables_not_joinable_by_stable_event_id",
            audit.failure_reasons,
        )

    def test_copied_and_independent_witness_labels_are_required(self) -> None:
        audit = audit_raw_log_contract(missing_copied_independent_labels_contract())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn(
            "copied_independent_labels_not_preregistered",
            audit.failure_reasons,
        )
        self.assertEqual(
            audit.missing_t86_control_roles,
            ("copied_record_control_pairs", "independent_record_control_pairs"),
        )

    def test_posthoc_policy_and_demotion_rules_are_rejected(self) -> None:
        audit = audit_raw_log_contract(posthoc_policy_and_demotion_contract())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn("policy_chosen_after_data", audit.failure_reasons)
        self.assertIn("demotion_rules_chosen_after_data", audit.failure_reasons)
        self.assertIn("incomplete_threshold_preregistration", audit.failure_reasons)
        self.assertIn("policy_outside_t77_safe_corridor", audit.failure_reasons)

    def test_dag_summary_without_raw_edges_is_rejected(self) -> None:
        audit = audit_raw_log_contract(dag_export_without_raw_edges_contract())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn("missing_required_raw_log_columns", audit.failure_reasons)
        self.assertIn(
            "ancestry_dag_edge_export.parent_record_id",
            audit.missing_columns,
        )
        self.assertIn(
            "ancestry_dag_edge_export.false_shared_edge_challenge_id",
            audit.missing_columns,
        )

    def test_unlinked_or_mutable_event_tables_are_rejected(self) -> None:
        audit = audit_raw_log_contract(unlinked_event_tables_contract())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn(
            "raw_tables_not_joinable_by_stable_event_id",
            audit.failure_reasons,
        )
        self.assertIn("required_tables_not_immutable_exports", audit.failure_reasons)
        self.assertEqual(
            audit.mutable_tables,
            ("perturbation_trial_log", "ancestry_dag_edge_export"),
        )

    def test_run_result_preserves_no_empirical_upgrade_boundary(self) -> None:
        result = run_t87_analysis()

        self.assertIn("falsifiable admission contract", result.strongest_claim)
        self.assertIn("does not score D1", result.weakened_claim)
        self.assertIn("No actual detector event log is present", result.open_blocker)
        self.assertEqual(
            set(REQUIRED_CHANNEL_ISOLATION_TESTS),
            {"perturbation_response", "signed_ancestry_dag"},
        )
        self.assertIn(
            "copied_record_control_pairs",
            set(REQUIRED_T86_CONTROL_ROLES),
        )


if __name__ == "__main__":
    unittest.main()
