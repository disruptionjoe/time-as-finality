import unittest

from models.invariant_preserving_transformations import (
    RELATIONSHIP_LEVELS,
    analyze_ipt,
    compose_ipts,
    consensus_record_theorem_transfer_ipt,
    observer_access_transformation,
    quantum_redundancy_reduction_ipt,
    relationship_taxonomy,
    run_t23_analysis,
    weak_quorum_obstruction_ipt,
)


class InvariantPreservingTransformationsTests(unittest.TestCase):
    def test_relationship_taxonomy_has_four_ordered_levels(self) -> None:
        taxonomy = relationship_taxonomy()

        self.assertEqual(set(taxonomy), set(RELATIONSHIP_LEVELS))
        self.assertIn("proof", taxonomy["homology"])
        self.assertIn("inverse", taxonomy["equivalence"])

    def test_observer_access_transformation_preserves_pointer_basis(self) -> None:
        analysis = analyze_ipt(observer_access_transformation())
        checks = {check.invariant: check for check in analysis.invariant_checks}

        self.assertEqual(analysis.transformation.relationship_class, "reduction")
        self.assertTrue(checks["pointer_basis"].preserved)
        self.assertTrue(checks["system_record_correlation"].preserved)
        self.assertTrue(analysis.all_declared_invariants_preserved)
        self.assertIn("inaccessible_records", analysis.transformation.allowed_losses)

    def test_consensus_record_transfer_preserves_quorum_safety(self) -> None:
        analysis = analyze_ipt(consensus_record_theorem_transfer_ipt())
        checks = {check.invariant: check for check in analysis.invariant_checks}

        self.assertEqual(analysis.transformation.relationship_class, "homology")
        self.assertTrue(checks["holder_count"].preserved)
        self.assertTrue(checks["quorum_threshold"].preserved)
        self.assertTrue(checks["quorum_intersection_safety"].preserved)
        self.assertTrue(checks["conflict_exclusion"].preserved)
        self.assertTrue(analysis.all_declared_invariants_preserved)

    def test_quantum_redundancy_reduction_preserves_d1_counts(self) -> None:
        analysis = analyze_ipt(quantum_redundancy_reduction_ipt())
        checks = {check.invariant: check for check in analysis.invariant_checks}

        self.assertEqual(analysis.transformation.source.name, "t2_local_lab_d1_view")
        self.assertEqual(analysis.transformation.target.name, "t22_reduction_schema_view")
        self.assertTrue(checks["holder_redundancy"].preserved)
        self.assertTrue(checks["accessible_support"].preserved)
        self.assertTrue(checks["observer_access_indexed"].preserved)
        self.assertTrue(analysis.all_declared_invariants_preserved)

    def test_weak_quorum_obstruction_blocks_declared_preservation(self) -> None:
        analysis = analyze_ipt(weak_quorum_obstruction_ipt())

        self.assertFalse(analysis.all_declared_invariants_preserved)
        self.assertEqual(len(analysis.triggered_obstructions), 1)
        self.assertEqual(analysis.triggered_obstructions[0].name, "weak_quorum")

    def test_composition_preserves_shared_invariant_without_obstruction(self) -> None:
        first = observer_access_transformation()
        second = quantum_redundancy_reduction_ipt()
        composition = compose_ipts(first, second, ("pointer_basis",))

        self.assertTrue(composition.source_target_match)
        self.assertTrue(composition.composition_preserves_requested_invariants)
        self.assertEqual(
            composition.theorem_status,
            "composition_preserves_requested_invariants",
        )

    def test_composition_reports_obstruction_when_second_map_breaks_condition(self) -> None:
        first = consensus_record_theorem_transfer_ipt()
        second = weak_quorum_obstruction_ipt()
        composition = compose_ipts(first, second, ("quorum_intersection_safety",))

        self.assertTrue(composition.source_target_match)
        self.assertFalse(composition.composition_preserves_requested_invariants)
        self.assertEqual(composition.theorem_status, "composition_blocked_by_obstruction")
        self.assertEqual(composition.triggered_obstructions[0].name, "weak_quorum")

    def test_full_t23_analysis_reports_proto_independence(self) -> None:
        result = run_t23_analysis()

        self.assertTrue(result["verdict"]["typed_ipt_definition_exists"])
        self.assertTrue(result["verdict"]["same_interface_expresses_three_domains"])
        self.assertTrue(result["verdict"]["composition_law_executable"])
        self.assertTrue(result["verdict"]["obstruction_condition_executable"])
        self.assertTrue(result["verdict"]["no_equivalence_claimed"])
        self.assertEqual(result["verdict"]["mathematical_independence"], "proto-independent")
        self.assertIn("Keep incubating", result["recommendation"])


if __name__ == "__main__":
    unittest.main()
