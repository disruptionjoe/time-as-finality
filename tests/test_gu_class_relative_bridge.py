import unittest

from models.gu_class_relative_bridge import (
    distler_garibaldi_bridge_case,
    nielsen_ninomiya_bridge_case,
    run_t27_bridge_audit,
    run_t27_analysis,
    witten_bridge_case,
)
from models.d1_restriction_system import (
    global_section,
    validate_system,
)


class WittenBridgeCaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.case = witten_bridge_case()

    def test_both_systems_validate(self) -> None:
        self.assertTrue(self.case.richer_validation.valid)
        self.assertTrue(self.case.restricted_validation.valid)

    def test_richer_system_has_global_section(self) -> None:
        gs = self.case.richer_global_section
        self.assertTrue(gs.global_assignment_exists)
        self.assertFalse(gs.obstruction_detected)
        self.assertGreater(gs.global_witness_count, 0)

    def test_restricted_system_is_obstructed(self) -> None:
        gs = self.case.restricted_global_section
        self.assertFalse(gs.global_assignment_exists)
        self.assertTrue(gs.obstruction_detected)
        self.assertEqual(gs.global_witness_count, 0)

    def test_restricted_system_is_locally_satisfiable(self) -> None:
        gs = self.case.restricted_global_section
        self.assertEqual(gs.local_witness_count, len(self.case.restricted_system.patches))

    def test_morphism_site_map_is_total(self) -> None:
        self.assertTrue(self.case.morphism_analysis.site_map_total)

    def test_morphism_loses_profiles_and_obstruction(self) -> None:
        a = self.case.morphism_analysis
        self.assertFalse(a.local_profiles_preserved)
        self.assertFalse(a.obstruction_status_preserved)
        self.assertFalse(a.reached)

    def test_morphism_preserves_trust_path(self) -> None:
        self.assertTrue(self.case.morphism_analysis.trust_path_preserved)

    def test_hypothesis_is_h1(self) -> None:
        self.assertEqual(self.case.hypothesis, "H1")

    def test_morphism_failure_is_profile_mismatch(self) -> None:
        self.assertEqual(self.case.morphism_failure_kind, "local_profile_mismatch")


class NielsenNinomiyaBridgeCaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.case = nielsen_ninomiya_bridge_case()

    def test_both_systems_validate(self) -> None:
        self.assertTrue(self.case.richer_validation.valid)
        self.assertTrue(self.case.restricted_validation.valid)

    def test_richer_system_has_global_section(self) -> None:
        gs = self.case.richer_global_section
        self.assertTrue(gs.global_assignment_exists)
        self.assertFalse(gs.obstruction_detected)
        self.assertGreater(gs.global_witness_count, 0)

    def test_restricted_system_is_obstructed(self) -> None:
        gs = self.case.restricted_global_section
        self.assertFalse(gs.global_assignment_exists)
        self.assertTrue(gs.obstruction_detected)
        self.assertEqual(gs.global_witness_count, 0)

    def test_restricted_system_all_patches_locally_satisfiable(self) -> None:
        gs = self.case.restricted_global_section
        self.assertEqual(gs.local_witness_count, len(self.case.restricted_system.patches))

    def test_morphism_site_map_is_total(self) -> None:
        self.assertTrue(self.case.morphism_analysis.site_map_total)

    def test_morphism_loses_profiles_and_obstruction(self) -> None:
        a = self.case.morphism_analysis
        self.assertFalse(a.local_profiles_preserved)
        self.assertFalse(a.obstruction_status_preserved)
        self.assertFalse(a.reached)

    def test_hypothesis_is_h1(self) -> None:
        self.assertEqual(self.case.hypothesis, "H1")

    def test_three_sites_encode_three_distinct_nn_assumptions(self) -> None:
        site_ids = self.case.restricted_system.site_ids()
        self.assertEqual(len(site_ids), 3)
        patch_ids = {p.patch_id for p in self.case.restricted_system.patches}
        self.assertIn("locality_hermitian", patch_ids)
        self.assertIn("translation_invariance", patch_ids)
        self.assertIn("exact_onsit_ua", patch_ids)


class DistlerGaribaldiCaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.case = distler_garibaldi_bridge_case()

    def test_both_systems_validate(self) -> None:
        self.assertTrue(self.case.richer_validation.valid)
        self.assertTrue(self.case.restricted_validation.valid)

    def test_richer_system_has_global_section(self) -> None:
        gs = self.case.richer_global_section
        self.assertTrue(gs.global_assignment_exists)
        self.assertFalse(gs.obstruction_detected)

    def test_restricted_system_is_obstructed(self) -> None:
        gs = self.case.restricted_global_section
        self.assertFalse(gs.global_assignment_exists)
        self.assertTrue(gs.obstruction_detected)

    def test_morphism_site_map_is_incomplete(self) -> None:
        self.assertFalse(self.case.morphism_analysis.site_map_total)

    def test_morphism_failure_is_site_map_incomplete(self) -> None:
        self.assertEqual(self.case.morphism_failure_kind, "site_map_incomplete")

    def test_hypothesis_is_h3(self) -> None:
        self.assertEqual(self.case.hypothesis, "H3")

    def test_richer_has_four_sites(self) -> None:
        self.assertEqual(len(self.case.richer_system.site_ids()), 4)

    def test_restricted_has_three_sites(self) -> None:
        self.assertEqual(len(self.case.restricted_system.site_ids()), 3)


class BridgeAuditResultTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t27_bridge_audit()

    def test_three_cases_produced(self) -> None:
        self.assertEqual(len(self.result.cases), 3)

    def test_projection_obstruction_pattern_detected(self) -> None:
        self.assertTrue(self.result.common_pattern.applies)

    def test_pattern_applies_to_witten_and_nn(self) -> None:
        self.assertIn("witten_1981", self.result.common_pattern.cases)
        self.assertIn("nielsen_ninomiya", self.result.common_pattern.cases)

    def test_dg_not_in_pattern(self) -> None:
        self.assertNotIn("distler_garibaldi", self.result.common_pattern.cases)

    def test_stretch_goal_reached(self) -> None:
        self.assertEqual(self.result.stretch_goal_status, "REACHED")

    def test_recommendation_names_h2(self) -> None:
        self.assertIn("H2", self.result.recommendation)

    def test_run_t27_analysis_returns_dict(self) -> None:
        result = run_t27_analysis()
        self.assertIsInstance(result, dict)
        self.assertIn("cases", result)
        self.assertIn("common_pattern", result)
        self.assertIn("recommendation", result)
        self.assertEqual(len(result["cases"]), 3)
