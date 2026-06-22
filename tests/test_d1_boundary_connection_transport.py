"""Tests for T125 D1 boundary-connection transport."""

from __future__ import annotations

import unittest

from models.d1_boundary_connection_transport import (
    audit_composition,
    audit_loop,
    audit_transport,
    boundary_objects,
    run_t125_analysis,
    transport_arrows,
)


class D1BoundaryConnectionTransportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.objects = boundary_objects()
        self.arrows = transport_arrows()
        self.result = run_t125_analysis()
        self.transport_audits = {
            audit.arrow_id: audit for audit in self.result.transport_audits
        }
        self.loop_audits = {
            audit.loop_id: audit for audit in self.result.loop_audits
        }

    def test_boundary_objects_reuse_t111_profile_values(self) -> None:
        self.assertEqual(self.objects["B0"].profile.as_tuple(), (4, 2, 2, 2))
        self.assertEqual(self.objects["B_refined"].profile.as_tuple(), (2, 2, 2, 0))
        self.assertEqual(self.objects["B_coarsened"].profile.as_tuple(), (5, 3, 3, 3))

    def test_identity_transport_preserves_every_fixture_profile(self) -> None:
        self.assertTrue(self.result.identity_passes)
        for arrow_id, arrow in self.arrows.items():
            if not arrow_id.startswith("id_"):
                continue
            audit = audit_transport(arrow, self.objects)
            self.assertEqual(audit.admissibility_verdict, "identity")
            self.assertEqual(audit.transported_profile, self.objects[arrow.source].profile)
            self.assertEqual(audit.boundary_delta.profile_before, audit.boundary_delta.profile_after)

    def test_pure_gauge_transport_preserves_profile_and_carries_provenance(self) -> None:
        for arrow_id in ("gauge_observer", "gauge_record", "gauge_holder", "gauge_causal"):
            audit = self.transport_audits[arrow_id]
            self.assertEqual(audit.admissibility_verdict, "pure_gauge_identity_delta")
            self.assertEqual(audit.transported_profile, self.objects["B0"].profile)
            self.assertTrue(audit.provenance_trace)
            self.assertTrue(audit.boundary_delta.reversible)

    def test_access_boundary_transports_are_deltas_not_gauge(self) -> None:
        refine = self.transport_audits["refine_access"]
        coarsen = self.transport_audits["coarsen_access"]

        self.assertEqual(refine.admissibility_verdict, "boundary_delta")
        self.assertEqual(coarsen.admissibility_verdict, "boundary_delta")
        self.assertIn("accessible_holders", refine.boundary_delta.changed_access_boundary)
        self.assertIn("accessible_holders", coarsen.boundary_delta.changed_access_boundary)
        self.assertFalse(self.arrows["refine_access"].pure_gauge)
        self.assertFalse(self.arrows["coarsen_access"].pure_gauge)

    def test_hostile_and_scalarized_maps_are_undefined(self) -> None:
        self.assertTrue(self.result.hostile_maps_undefined)
        for arrow_id in (
            "missing_boundary_provenance",
            "bad_record_incidence",
            "bad_holder_partition",
            "bad_causal_reachability",
            "scalarized_profile",
        ):
            audit = self.transport_audits[arrow_id]
            self.assertEqual(audit.admissibility_verdict, "undefined")
            self.assertIsNone(audit.transported_profile)
            self.assertIsNone(audit.boundary_delta)

    def test_composition_preserves_ordered_boundary_provenance(self) -> None:
        composition = audit_composition(
            "refine_restore",
            ("refine_access", "restore_from_refined_trace"),
            "id_B0",
            self.objects,
            self.arrows,
        )

        self.assertEqual(
            composition.admissibility_verdict,
            "composes_with_declared_direct_effect",
        )
        self.assertEqual(composition.composite_profile, self.objects["B0"].profile)
        self.assertTrue(composition.deltas_preserved)
        self.assertIn("drop_access_to_archive_holders", composition.provenance_trace)
        self.assertIn("restore_access_using_retained_boundary_trace", composition.provenance_trace)

    def test_undefined_intermediate_blocks_composition(self) -> None:
        composition = audit_composition(
            "undefined_middle",
            ("missing_boundary_provenance", "restore_from_refined_trace"),
            None,
            self.objects,
            self.arrows,
        )

        self.assertEqual(composition.admissibility_verdict, "undefined_intermediate")
        self.assertIsNone(composition.composite_profile)
        self.assertFalse(composition.deltas_preserved)

    def test_closed_loop_classifications_are_conservative(self) -> None:
        pure = self.loop_audits["pure_observer_relabeling_loop"]
        restore = self.loop_audits["refinement_restore_with_trace_loop"]
        lossy = self.loop_audits["coarsen_restrict_lossy_boundary_loop"]
        hostile = self.loop_audits["hostile_missing_provenance_loop"]

        self.assertEqual(pure.classification, "identity_loop")
        self.assertFalse(pure.residual_boundary_delta)
        self.assertEqual(restore.classification, "closed_with_residual_boundary_delta")
        self.assertTrue(restore.residual_boundary_delta)
        self.assertEqual(lossy.classification, "closed_with_residual_boundary_delta")
        self.assertTrue(lossy.residual_boundary_delta)
        self.assertEqual(hostile.classification, "undefined")

    def test_full_result_rejects_curvature_upgrade(self) -> None:
        self.assertTrue(self.result.identity_passes)
        self.assertTrue(self.result.pure_gauge_loops_close)
        self.assertTrue(self.result.lossy_loops_report_residual_delta)
        self.assertIn("curvature", self.result.weakened)
        self.assertIn("no curvature", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
