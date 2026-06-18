import unittest

from models.projection_obstruction_schema import (
    analyze_projection_case,
    projection_case_from_bridge_case,
    run_t29_analysis,
    run_t29_schema_lab,
    synthetic_lossy_no_obstruction_case,
    synthetic_shared_obstruction_case,
)
from models.gu_class_relative_bridge import (
    distler_garibaldi_bridge_case,
    nielsen_ninomiya_bridge_case,
    witten_bridge_case,
)


class ProjectionObstructionSchemaTests(unittest.TestCase):
    def test_witten_is_positive_schema_instance(self) -> None:
        analysis = analyze_projection_case(projection_case_from_bridge_case(witten_bridge_case()))

        self.assertTrue(analysis.schema.projection_definable)
        self.assertFalse(analysis.schema.richer_obstructed)
        self.assertTrue(analysis.schema.restricted_obstructed)
        self.assertTrue(analysis.schema.obstruction_created_by_projection)
        self.assertTrue(analysis.schema.schema_instance)
        self.assertEqual(analysis.schema.outcome, "faithful_projection_obstruction")

    def test_nielsen_ninomiya_is_positive_schema_instance(self) -> None:
        analysis = analyze_projection_case(projection_case_from_bridge_case(nielsen_ninomiya_bridge_case()))

        self.assertTrue(analysis.schema.projection_definable)
        self.assertTrue(analysis.schema.obstruction_created_by_projection)
        self.assertTrue(analysis.schema.projection_loses_structure)
        self.assertTrue(analysis.schema.schema_instance)

    def test_distler_garibaldi_is_non_definable_boundary(self) -> None:
        analysis = analyze_projection_case(projection_case_from_bridge_case(distler_garibaldi_bridge_case()))

        self.assertFalse(analysis.schema.projection_definable)
        self.assertFalse(analysis.schema.schema_instance)
        self.assertEqual(analysis.schema.outcome, "non_definable_projection")
        self.assertEqual(analysis.morphism_analysis.obstruction, "site_map_incomplete")

    def test_lossy_projection_need_not_create_obstruction(self) -> None:
        analysis = analyze_projection_case(synthetic_lossy_no_obstruction_case())

        self.assertTrue(analysis.schema.projection_definable)
        self.assertTrue(analysis.schema.projection_loses_structure)
        self.assertFalse(analysis.schema.richer_obstructed)
        self.assertFalse(analysis.schema.restricted_obstructed)
        self.assertFalse(analysis.schema.schema_instance)
        self.assertEqual(analysis.schema.outcome, "lossy_projection_no_new_obstruction")

    def test_obstruction_in_both_systems_is_not_projection_created(self) -> None:
        analysis = analyze_projection_case(synthetic_shared_obstruction_case())

        self.assertTrue(analysis.schema.projection_definable)
        self.assertTrue(analysis.schema.richer_obstructed)
        self.assertTrue(analysis.schema.restricted_obstructed)
        self.assertFalse(analysis.schema.obstruction_created_by_projection)
        self.assertFalse(analysis.schema.schema_instance)
        self.assertEqual(analysis.schema.outcome, "shared_obstruction_not_projection_created")

    def test_theorem_ladder_records_positive_and_boundary_cases(self) -> None:
        result = run_t29_schema_lab()
        attempts = {attempt.name: attempt for attempt in result.theorem_attempts}

        self.assertTrue(attempts["Positive Projection-Obstruction Schema"].reached)
        self.assertTrue(attempts["Non-Definable Projection Boundary"].reached)
        self.assertTrue(attempts["Loss Without Obstruction Counterexample"].reached)
        self.assertTrue(attempts["Inherited Obstruction Counterexample"].reached)

    def test_named_claim_decision_is_narrow_and_positive(self) -> None:
        result = run_t29_schema_lab()

        self.assertTrue(result.named_claim_decision.create_named_claim)
        self.assertEqual(result.named_claim_decision.proposed_id, "PO1")
        self.assertEqual(result.named_claim_decision.status, "partially_supported")
        self.assertIn("does not prove any original physics", result.named_claim_decision.non_claims[0])

    def test_run_t29_analysis_returns_expected_shape(self) -> None:
        result = run_t29_analysis()

        self.assertIn("analyses", result)
        self.assertIn("theorem_attempts", result)
        self.assertIn("named_claim_decision", result)
        self.assertEqual(len(result["analyses"]), 5)
        self.assertIn("Projection-Obstruction", result["recommendation"])


if __name__ == "__main__":
    unittest.main()
