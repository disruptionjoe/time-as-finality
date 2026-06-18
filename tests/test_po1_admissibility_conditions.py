import unittest

from models.po1_admissibility_conditions import (
    ADMISSIBILITY_CONDITIONS,
    check_admissibility,
    run_t31_admissibility_audit,
    run_t31_analysis,
)
from models.cap_theorem_bridge import cap_bridge_case
from models.cross_domain_projection_obstruction_validation import (
    access_control_inheritance_case,
    database_expand_contract_case,
    git_semantic_merge_case,
    type_system_macro_boundary_case,
)
from models.gu_class_relative_bridge import (
    distler_garibaldi_bridge_case,
    nielsen_ninomiya_bridge_case,
    witten_bridge_case,
)
from models.projection_obstruction_schema import (
    projection_case_from_bridge_case,
    synthetic_lossy_no_obstruction_case,
    synthetic_shared_obstruction_case,
)


def _cap_projection_case():
    c = cap_bridge_case()
    from models.projection_obstruction_schema import ProjectionCase
    return ProjectionCase(
        name=c.name,
        source="T28",
        richer_system=c.richer_system,
        restricted_system=c.restricted_system,
        morphism=c.morphism,
        forgotten_structure=c.forgotten_structure,
        preserved_structure=c.preserved_structure,
        intended_reading=c.bridge_verdict,
    )


class AdmissibilityConditionSchemaTests(unittest.TestCase):
    def test_seven_conditions_defined(self) -> None:
        self.assertEqual(len(ADMISSIBILITY_CONDITIONS), 7)

    def test_condition_ids_are_ac1_through_ac7(self) -> None:
        ids = [ac_id for ac_id, _, _ in ADMISSIBILITY_CONDITIONS]
        self.assertEqual(ids, ["AC1", "AC2", "AC3", "AC4", "AC5", "AC6", "AC7"])


class PositiveAdmissibleCasesTests(unittest.TestCase):
    def _check(self, case):
        return check_admissibility(case)

    def test_witten_is_fully_admissible(self) -> None:
        c = self._check(projection_case_from_bridge_case(witten_bridge_case()))
        self.assertEqual(c.verdict, "fully_admissible")
        self.assertTrue(c.po1_evidence)
        self.assertEqual(c.failed_conditions, ())

    def test_nielsen_ninomiya_is_fully_admissible(self) -> None:
        c = self._check(projection_case_from_bridge_case(nielsen_ninomiya_bridge_case()))
        self.assertEqual(c.verdict, "fully_admissible")
        self.assertTrue(c.po1_evidence)
        self.assertEqual(c.failed_conditions, ())

    def test_cap_is_fully_admissible(self) -> None:
        c = self._check(_cap_projection_case())
        self.assertEqual(c.verdict, "fully_admissible")
        self.assertTrue(c.po1_evidence)
        self.assertEqual(c.failed_conditions, ())

    def test_git_merge_is_fully_admissible(self) -> None:
        c = self._check(git_semantic_merge_case().case)
        self.assertEqual(c.verdict, "fully_admissible")
        self.assertTrue(c.po1_evidence)
        self.assertEqual(c.failed_conditions, ())

    def test_all_positive_cases_pass_all_seven_conditions(self) -> None:
        positive_cases = [
            projection_case_from_bridge_case(witten_bridge_case()),
            projection_case_from_bridge_case(nielsen_ninomiya_bridge_case()),
            _cap_projection_case(),
            git_semantic_merge_case().case,
        ]
        for case in positive_cases:
            with self.subTest(name=case.name):
                c = self._check(case)
                self.assertTrue(c.ac1_richer_valid)
                self.assertTrue(c.ac2_restricted_valid)
                self.assertTrue(c.ac3_projection_definable)
                self.assertTrue(c.ac4_local_compat)
                self.assertTrue(c.ac5_structure_forgotten)
                self.assertTrue(c.ac6_restricted_obstructed)
                self.assertTrue(c.ac7_richer_unobstructed)


class BoundaryCasesTests(unittest.TestCase):
    def test_distler_garibaldi_is_boundary_non_definable(self) -> None:
        c = check_admissibility(projection_case_from_bridge_case(distler_garibaldi_bridge_case()))
        self.assertEqual(c.verdict, "boundary_non_definable")
        self.assertFalse(c.po1_evidence)
        self.assertIn("AC3", c.failed_conditions)
        self.assertFalse(c.ac3_projection_definable)

    def test_type_system_macro_is_boundary_non_definable(self) -> None:
        c = check_admissibility(type_system_macro_boundary_case().case)
        self.assertEqual(c.verdict, "boundary_non_definable")
        self.assertFalse(c.po1_evidence)
        self.assertIn("AC3", c.failed_conditions)

    def test_boundary_cases_fail_ac3(self) -> None:
        for case_fn in [
            lambda: projection_case_from_bridge_case(distler_garibaldi_bridge_case()),
            lambda: type_system_macro_boundary_case().case,
        ]:
            with self.subTest():
                c = check_admissibility(case_fn())
                self.assertFalse(c.ac3_projection_definable)


class NonAdmissibleSharedObstructionTests(unittest.TestCase):
    def test_synthetic_shared_obstruction_is_non_admissible(self) -> None:
        c = check_admissibility(synthetic_shared_obstruction_case())
        self.assertEqual(c.verdict, "non_admissible_shared_obstruction")
        self.assertFalse(c.po1_evidence)
        self.assertIn("AC7", c.failed_conditions)
        self.assertFalse(c.ac7_richer_unobstructed)

    def test_access_control_is_non_admissible_shared_obstruction(self) -> None:
        c = check_admissibility(access_control_inheritance_case().case)
        self.assertEqual(c.verdict, "non_admissible_shared_obstruction")
        self.assertFalse(c.po1_evidence)
        self.assertFalse(c.ac7_richer_unobstructed)


class NonAdmissibleNoObstructionTests(unittest.TestCase):
    def test_synthetic_lossy_no_obstruction_is_non_admissible(self) -> None:
        c = check_admissibility(synthetic_lossy_no_obstruction_case())
        self.assertEqual(c.verdict, "non_admissible_no_new_obstruction")
        self.assertFalse(c.po1_evidence)
        self.assertIn("AC6", c.failed_conditions)
        self.assertFalse(c.ac6_restricted_obstructed)

    def test_database_expand_contract_is_non_admissible(self) -> None:
        c = check_admissibility(database_expand_contract_case().case)
        self.assertEqual(c.verdict, "non_admissible_no_new_obstruction")
        self.assertFalse(c.po1_evidence)
        self.assertFalse(c.ac6_restricted_obstructed)


class AuditResultTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t31_admissibility_audit()

    def test_ten_cases_evaluated(self) -> None:
        self.assertEqual(len(self.result.checks), 10)

    def test_four_positive_cases(self) -> None:
        self.assertEqual(len(self.result.positive_cases), 4)

    def test_two_boundary_cases(self) -> None:
        self.assertEqual(len(self.result.boundary_cases), 2)

    def test_four_non_admissible_cases(self) -> None:
        self.assertEqual(len(self.result.non_admissible_cases), 4)

    def test_positive_cases_include_t27_and_t28(self) -> None:
        self.assertIn("witten_1981", self.result.positive_cases)
        self.assertIn("nielsen_ninomiya", self.result.positive_cases)
        self.assertIn("cap_theorem", self.result.positive_cases)

    def test_positive_cases_include_non_physics_instance(self) -> None:
        self.assertIn("git_semantic_merge", self.result.positive_cases)

    def test_boundary_includes_distler_garibaldi(self) -> None:
        self.assertIn("distler_garibaldi", self.result.boundary_cases)

    def test_weakest_po1_has_five_conditions(self) -> None:
        self.assertEqual(len(self.result.weakest_po1_conditions), 5)

    def test_recommended_po1_has_seven_conditions(self) -> None:
        self.assertEqual(len(self.result.recommended_po1_conditions), 7)

    def test_po1_status_reflects_narrowing(self) -> None:
        self.assertIn("partially_supported", self.result.po1_status)

    def test_recommendation_names_all_seven_conditions(self) -> None:
        self.assertIn("AC4", self.result.po1_recommendation)
        self.assertIn("AC5", self.result.po1_recommendation)

    def test_run_t31_analysis_returns_dict(self) -> None:
        result = run_t31_analysis()
        self.assertIsInstance(result, dict)
        self.assertIn("checks", result)
        self.assertIn("positive_cases", result)
        self.assertIn("boundary_cases", result)
        self.assertIn("non_admissible_cases", result)
        self.assertIn("weakest_po1_conditions", result)
        self.assertIn("recommended_po1_conditions", result)

    def test_analysis_case_count(self) -> None:
        result = run_t31_analysis()
        self.assertEqual(result["case_count"], 10)
        self.assertEqual(result["positive_count"], 4)
        self.assertEqual(result["boundary_count"], 2)
        self.assertEqual(result["non_admissible_count"], 4)
