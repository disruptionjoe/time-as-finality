import unittest

from models.cap_theorem_bridge import (
    cap_bridge_case,
    nn_cap_structural_comparison,
    run_cap_bridge_audit,
    run_cap_analysis,
)
from models.d1_restriction_system import (
    global_section,
    validate_system,
)


class CAPRestrictedSystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.case = cap_bridge_case()

    def test_both_systems_validate(self) -> None:
        self.assertTrue(self.case.richer_validation.valid)
        self.assertTrue(self.case.restricted_validation.valid)

    def test_restricted_has_three_sites(self) -> None:
        self.assertEqual(len(self.case.restricted_system.site_ids()), 3)

    def test_restricted_three_cap_patches_present(self) -> None:
        patch_ids = {p.patch_id for p in self.case.restricted_system.patches}
        self.assertIn("consistency", patch_ids)
        self.assertIn("availability", patch_ids)
        self.assertIn("partition_tolerance", patch_ids)

    def test_restricted_system_is_obstructed(self) -> None:
        gs = self.case.restricted_global_section
        self.assertFalse(gs.global_assignment_exists)
        self.assertTrue(gs.obstruction_detected)
        self.assertEqual(gs.global_witness_count, 0)

    def test_restricted_all_patches_locally_satisfiable(self) -> None:
        gs = self.case.restricted_global_section
        self.assertEqual(gs.local_witness_count, len(self.case.restricted_system.patches))


class CAPRicherSystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.case = cap_bridge_case()

    def test_richer_system_has_global_section(self) -> None:
        gs = self.case.richer_global_section
        self.assertTrue(gs.global_assignment_exists)
        self.assertFalse(gs.obstruction_detected)
        self.assertGreater(gs.global_witness_count, 0)

    def test_richer_has_three_sites(self) -> None:
        self.assertEqual(len(self.case.richer_system.site_ids()), 3)

    def test_richer_contains_partition_diverge_patch(self) -> None:
        patch_ids = {p.patch_id for p in self.case.richer_system.patches}
        self.assertIn("partition_diverge", patch_ids)

    def test_richer_contains_sync_reconcile_patch(self) -> None:
        patch_ids = {p.patch_id for p in self.case.richer_system.patches}
        self.assertIn("sync_reconcile", patch_ids)


class CAPMorphismTests(unittest.TestCase):
    def setUp(self) -> None:
        self.case = cap_bridge_case()

    def test_morphism_site_map_is_total(self) -> None:
        self.assertTrue(self.case.morphism_analysis.site_map_total)

    def test_morphism_loses_profiles(self) -> None:
        self.assertFalse(self.case.morphism_analysis.local_profiles_preserved)

    def test_morphism_obstruction_not_preserved(self) -> None:
        self.assertFalse(self.case.morphism_analysis.obstruction_status_preserved)

    def test_morphism_not_reached(self) -> None:
        self.assertFalse(self.case.morphism_analysis.reached)

    def test_morphism_trust_path_preserved(self) -> None:
        self.assertTrue(self.case.morphism_analysis.trust_path_preserved)

    def test_morphism_failure_is_profile_mismatch(self) -> None:
        self.assertEqual(self.case.morphism_failure_kind, "local_profile_mismatch")

    def test_hypothesis_is_h1(self) -> None:
        self.assertEqual(self.case.hypothesis, "H1")


class NNCAPComparisonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.comparison = nn_cap_structural_comparison()

    def test_structural_identity(self) -> None:
        self.assertTrue(self.comparison.structural_identity)

    def test_same_patch_count(self) -> None:
        self.assertEqual(self.comparison.nn_patch_count, self.comparison.cap_patch_count)
        self.assertEqual(self.comparison.cap_patch_count, 3)

    def test_same_local_witness_count(self) -> None:
        self.assertEqual(
            self.comparison.nn_local_witness_count,
            self.comparison.cap_local_witness_count,
        )
        self.assertEqual(self.comparison.cap_local_witness_count, 3)

    def test_same_global_witness_count(self) -> None:
        self.assertEqual(
            self.comparison.nn_global_witness_count,
            self.comparison.cap_global_witness_count,
        )
        self.assertEqual(self.comparison.cap_global_witness_count, 0)

    def test_both_obstructed(self) -> None:
        self.assertTrue(self.comparison.nn_obstruction_detected)
        self.assertTrue(self.comparison.cap_obstruction_detected)


class CAPBridgeAuditResultTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_cap_bridge_audit()

    def test_recommendation_names_h1(self) -> None:
        self.assertIn("H1", self.result.recommendation)

    def test_recommendation_names_nn(self) -> None:
        self.assertIn("Nielsen", self.result.recommendation)

    def test_run_cap_analysis_returns_dict(self) -> None:
        result = run_cap_analysis()
        self.assertIsInstance(result, dict)
        self.assertIn("case", result)
        self.assertIn("nn_cap_comparison", result)
        self.assertIn("recommendation", result)

    def test_run_cap_analysis_case_is_h1(self) -> None:
        result = run_cap_analysis()
        self.assertEqual(result["case"]["hypothesis"], "H1")

    def test_run_cap_analysis_structural_identity(self) -> None:
        result = run_cap_analysis()
        self.assertTrue(result["nn_cap_comparison"]["structural_identity"])
