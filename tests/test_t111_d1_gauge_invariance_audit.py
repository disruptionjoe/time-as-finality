"""Tests for T111 D1 gauge-invariance audit."""

from __future__ import annotations

import unittest

from models.t111_d1_gauge_invariance_audit import (
    BOUNDARY_KINDS,
    D1_DIMENSIONS,
    access_boundary_coarsening,
    access_boundary_refinement,
    audit_transformation,
    compute_profile,
    reference_system,
    run_t111_analysis,
    run_t111_audit,
    transformation_specs,
)


class T111D1GaugeInvarianceAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.system = reference_system()
        self.result = run_t111_audit()

    def test_reference_profile_has_distinct_axes(self) -> None:
        profile = compute_profile(self.system)

        self.assertEqual(profile.as_tuple(), (4, 2, 2, 2))
        self.assertEqual(set(D1_DIMENSIONS), set(profile.__dataclass_fields__))

    def test_pure_gauge_transformations_preserve_all_d1_dimensions(self) -> None:
        for audit in self.result.audits:
            if not (audit.admissible and audit.gauge_pure):
                continue

            self.assertEqual(audit.before_profile, audit.after_profile, audit.name)
            self.assertEqual(audit.invariant_failure_dimensions, (), audit.name)
            self.assertTrue(
                all(
                    item.classification == "invariant"
                    for item in audit.classifications
                ),
                audit.name,
            )

    def test_access_boundary_refinement_and_coarsening_are_covariant_not_gauge(self) -> None:
        refined = compute_profile(access_boundary_refinement(self.system))
        coarsened = compute_profile(access_boundary_coarsening(self.system))

        self.assertEqual(refined.as_tuple(), (2, 2, 2, 0))
        self.assertEqual(coarsened.as_tuple(), (5, 3, 3, 3))
        for audit in self.result.audits:
            if audit.kind not in BOUNDARY_KINDS:
                continue
            self.assertFalse(audit.gauge_pure)
            self.assertTrue(audit.invariant_failure_dimensions)
            self.assertTrue(
                all(
                    item.classification == "covariant"
                    and "not gauge" in item.reason
                    for item in audit.classifications
                ),
                audit.name,
            )

    def test_negative_controls_are_undefined_and_break_claimed_invariants(self) -> None:
        negative_audits = [audit for audit in self.result.audits if not audit.admissible]

        self.assertGreaterEqual(len(negative_audits), 3)
        self.assertTrue(
            any("distinct_holder_redundancy" in audit.invariant_failure_dimensions for audit in negative_audits)
        )
        self.assertTrue(
            any("causal_branch_support" in audit.invariant_failure_dimensions for audit in negative_audits)
        )
        for audit in negative_audits:
            self.assertTrue(audit.invariant_failure_dimensions, audit.name)
            self.assertTrue(
                all(item.classification == "undefined" for item in audit.classifications),
                audit.name,
            )

    def test_classification_summary_keeps_observables_boundary_indexed(self) -> None:
        summaries = {summary.dimension: summary for summary in self.result.dimension_summaries}

        for dimension in D1_DIMENSIONS:
            self.assertEqual(summaries[dimension].pure_gauge_classification, "invariant")
            self.assertEqual(summaries[dimension].boundary_classification, "covariant")
            self.assertIn("boundary-indexed", summaries[dimension].future_connection_status)
        self.assertEqual(
            summaries["causal_branch_support"].observable_status,
            "formal-only in current physical claims",
        )
        self.assertEqual(
            summaries["graph_reversal_count"].observable_status,
            "formal-only in current physical claims",
        )

    def test_individual_transformation_audit_reports_expected_failure_dimensions(self) -> None:
        specs = {spec.name: spec for spec in transformation_specs(self.system)}

        holder_merge = audit_transformation(
            self.system,
            specs["negative_holder_partition_merge"],
        )
        graph_break = audit_transformation(
            self.system,
            specs["negative_causal_graph_nonisomorphism"],
        )

        self.assertEqual(holder_merge.invariant_failure_dimensions, ("distinct_holder_redundancy",))
        self.assertEqual(graph_break.invariant_failure_dimensions, ("causal_branch_support",))

    def test_full_analysis_is_conservative(self) -> None:
        payload = run_t111_analysis()
        verdict = payload["verdict"]

        self.assertTrue(verdict["pure_gauge_maps_preserve_all_d1_dimensions"])
        self.assertTrue(verdict["boundary_maps_are_not_treated_as_gauge"])
        self.assertTrue(verdict["negative_controls_change_alleged_invariants"])
        self.assertTrue(verdict["no_curvature_gravity_or_anomaly_claim"])
        self.assertIn("Boundary changes are observer-frame data", payload["strongest_claim"])
        self.assertIn("no curvature", payload["guardrail"])


if __name__ == "__main__":
    unittest.main()
