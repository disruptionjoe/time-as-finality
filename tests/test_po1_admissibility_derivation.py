import unittest

from models.po1_admissibility_conditions import check_admissibility
from models.po1_admissibility_derivation import (
    AC_IDS,
    ac6_implies_ac4_for_system,
    generate_condition_subsets,
    projection_case_for_conditions,
    run_t32_analysis,
    run_t32_derivation_audit,
)


class T32DependencyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t32_derivation_audit()

    def test_ac6_implies_ac4_edge_exists(self) -> None:
        edges = {(edge.source, edge.target, edge.relation) for edge in self.result.dependency_edges}
        self.assertIn(("AC6", "AC4", "implies"), edges)

    def test_ac4_removed_from_minimal_condition_basis(self) -> None:
        self.assertNotIn("AC4", self.result.minimal_condition_basis)
        self.assertEqual(self.result.minimal_condition_basis, ("AC1", "AC2", "AC3", "AC5", "AC6", "AC7"))

    def test_four_principle_compression(self) -> None:
        self.assertEqual(len(self.result.compressed_principle_basis), 4)
        self.assertIn("P4_informative_forgetting", self.result.compressed_principle_basis)

    def test_best_hypothesis_records_h4_boundary(self) -> None:
        self.assertEqual(self.result.best_supported_hypothesis, "H2 with H4 boundary")
        self.assertIn("AC5", self.result.theorem_verdict)


class T32RemovalAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t32_derivation_audit()

    def test_each_independent_condition_has_false_positive_when_removed(self) -> None:
        audits = {audit.removed_condition: audit for audit in self.result.removal_audits}
        for ac_id in ("AC1", "AC2", "AC3", "AC5", "AC6", "AC7"):
            with self.subTest(ac_id=ac_id):
                self.assertEqual(len(audits[ac_id].newly_admitted_false_positives), 1)

    def test_ac4_removal_admits_no_false_positive(self) -> None:
        audits = {audit.removed_condition: audit for audit in self.result.removal_audits}
        self.assertEqual(audits["AC4"].newly_admitted_false_positives, ())
        self.assertEqual(audits["AC4"].failure_class, "none_under_current_T26_semantics")

    def test_ac5_counterexample_has_all_other_conditions(self) -> None:
        target = {ac_id: True for ac_id in AC_IDS}
        target["AC5"] = False
        check = check_admissibility(projection_case_for_conditions(target, "unit_ac5"))
        self.assertFalse(check.ac5_structure_forgotten)
        self.assertTrue(check.ac1_richer_valid)
        self.assertTrue(check.ac2_restricted_valid)
        self.assertTrue(check.ac3_projection_definable)
        self.assertTrue(check.ac4_local_compat)
        self.assertTrue(check.ac6_restricted_obstructed)
        self.assertTrue(check.ac7_richer_unobstructed)
        self.assertEqual(check.verdict, "non_admissible_no_forgotten_structure")


class T32SubsetGenerationTests(unittest.TestCase):
    def test_generator_covers_all_feasible_condition_vectors(self) -> None:
        generated, impossible = generate_condition_subsets()
        self.assertEqual(len(generated), 96)
        self.assertEqual(len(impossible), 32)
        self.assertTrue(all(item.feasible for item in generated))

    def test_impossible_vectors_are_exactly_ac6_without_ac4(self) -> None:
        _, impossible = generate_condition_subsets()
        self.assertTrue(impossible)
        for item in impossible:
            with self.subTest(subset_id=item.subset_id):
                self.assertTrue(item.target_conditions["AC6"])
                self.assertFalse(item.target_conditions["AC4"])

    def test_generated_cases_match_target_conditions(self) -> None:
        generated, _ = generate_condition_subsets()
        for item in generated:
            with self.subTest(subset_id=item.subset_id):
                self.assertEqual(item.actual_conditions, item.target_conditions)

    def test_ac6_implies_ac4_for_generated_restricted_systems(self) -> None:
        generated, _ = generate_condition_subsets()
        for item in generated:
            if not item.target_conditions["AC6"]:
                continue
            case = projection_case_for_conditions(item.target_conditions, item.subset_id)
            self.assertTrue(ac6_implies_ac4_for_system(case.restricted_system))


class T32AnalysisShapeTests(unittest.TestCase):
    def test_run_t32_analysis_returns_expected_shape(self) -> None:
        result = run_t32_analysis()
        self.assertIn("dependency_edges", result)
        self.assertIn("structural_principles", result)
        self.assertIn("condition_derivations", result)
        self.assertIn("minimal_condition_basis", result)
        self.assertIn("subset_generation", result)
        self.assertEqual(result["subset_generation"]["generated_feasible_vectors"], 96)
        self.assertEqual(result["subset_generation"]["impossible_vectors"], 32)


if __name__ == "__main__":
    unittest.main()
