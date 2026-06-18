"""Tests for T38: minimal multiscale transport formalization."""

import unittest

from models.minimal_multiscale_transport import (
    CompressionRecord,
    EmergenceRecord,
    HypothesisEvaluation,
    LevelSkipTest,
    QuestionCoverage,
    T38Result,
    _make_2site_layer,
    _make_3site_layer_emergence,
    _make_3site_layer_no_patches,
    _make_4site_layer,
    build_compression_scenario,
    build_emergence_scenario,
    build_level_skip_test,
    evaluate_hypotheses,
    run_t38_analysis,
    t38_result_to_dict,
)
from models.d1_restriction_system import global_section, validate_system
from models.transport_network import analyze_network, diamond_network


# ---------------------------------------------------------------------------
# Module-level cached result
# ---------------------------------------------------------------------------

_RESULT: T38Result | None = None


def _r() -> T38Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t38_analysis()
    return _RESULT


# ---------------------------------------------------------------------------
# Layer construction
# ---------------------------------------------------------------------------

class TestLayerConstruction(unittest.TestCase):

    def test_4site_layer_has_four_sites(self) -> None:
        layer = _make_4site_layer("test", "t4")
        self.assertEqual(len(layer.system.local_values), 4)

    def test_4site_layer_valid(self) -> None:
        layer = _make_4site_layer("test", "t4")
        result = validate_system(layer.system)
        self.assertTrue(result.valid)

    def test_4site_layer_no_patches(self) -> None:
        layer = _make_4site_layer("test", "t4")
        self.assertEqual(len(layer.system.patches), 0)

    def test_4site_layer_trust_path(self) -> None:
        from models.d1_restriction_system import analyze_transport
        layer = _make_4site_layer("test", "t4")
        transport = analyze_transport(layer.system)
        self.assertTrue(transport.trust_path_exists)

    def test_2site_layer_not_obstructed_by_default(self) -> None:
        layer = _make_2site_layer("test", "t2", obstructed=False)
        gs = global_section(layer.system)
        self.assertFalse(gs.obstruction_detected)

    def test_2site_layer_obstructed_when_requested(self) -> None:
        layer = _make_2site_layer("test", "t2", obstructed=True)
        gs = global_section(layer.system)
        self.assertTrue(gs.obstruction_detected)

    def test_2site_obstructed_locally_satisfiable(self) -> None:
        layer = _make_2site_layer("test", "t2", obstructed=True)
        gs = global_section(layer.system)
        self.assertEqual(gs.local_witness_count, 2)

    def test_3site_emergence_layer_has_global_section(self) -> None:
        layer = _make_3site_layer_emergence("test", "em")
        gs = global_section(layer.system)
        self.assertTrue(gs.global_assignment_exists)
        self.assertFalse(gs.obstruction_detected)

    def test_3site_emergence_layer_has_patches(self) -> None:
        layer = _make_3site_layer_emergence("test", "em")
        self.assertEqual(len(layer.system.patches), 2)

    def test_3site_no_patches_layer_has_no_patches(self) -> None:
        layer = _make_3site_layer_no_patches("test", "np")
        self.assertEqual(len(layer.system.patches), 0)

    def test_3site_no_patches_layer_valid(self) -> None:
        layer = _make_3site_layer_no_patches("test", "np")
        self.assertTrue(validate_system(layer.system).valid)


# ---------------------------------------------------------------------------
# Compression scenario
# ---------------------------------------------------------------------------

class TestCompressionScenario(unittest.TestCase):

    def setUp(self) -> None:
        self.record, self.admissibility = build_compression_scenario()

    def test_compression_ratio(self) -> None:
        self.assertAlmostEqual(self.record.compression_ratio, 0.5)

    def test_source_site_count(self) -> None:
        self.assertEqual(self.record.source_site_count, 4)

    def test_target_site_count(self) -> None:
        self.assertEqual(self.record.target_site_count, 2)

    def test_po1_admissible(self) -> None:
        self.assertTrue(self.record.po1_admissible)

    def test_retained_invariants_nonempty(self) -> None:
        self.assertGreater(len(self.record.retained_invariants), 0)

    def test_lost_detail_nonempty(self) -> None:
        self.assertGreater(len(self.record.lost_detail), 0)

    def test_admissibility_all_conditions_pass(self) -> None:
        self.assertEqual(self.admissibility.verdict, "fully_admissible")
        self.assertEqual(len(self.admissibility.failed_conditions), 0)

    def test_ac5_fires(self) -> None:
        self.assertTrue(self.admissibility.ac5_structure_forgotten)

    def test_ac6_target_obstructed(self) -> None:
        self.assertTrue(self.admissibility.ac6_restricted_obstructed)

    def test_ac7_source_unobstructed(self) -> None:
        self.assertTrue(self.admissibility.ac7_richer_unobstructed)


# ---------------------------------------------------------------------------
# Emergence scenario
# ---------------------------------------------------------------------------

class TestEmergenceScenario(unittest.TestCase):

    def setUp(self) -> None:
        self.record, self.admissibility = build_emergence_scenario()

    def test_source_has_no_patches(self) -> None:
        self.assertEqual(self.record.source_patch_count, 0)

    def test_target_has_patches(self) -> None:
        self.assertGreater(self.record.target_patch_count, 0)

    def test_is_genuine_emergence(self) -> None:
        self.assertTrue(self.record.is_genuine_emergence)

    def test_source_has_global_section(self) -> None:
        self.assertTrue(self.record.source_has_global_section)

    def test_target_has_global_section(self) -> None:
        self.assertTrue(self.record.target_has_global_section)

    def test_emergence_not_po1(self) -> None:
        # Emergence is orthogonal to PO1: target is unobstructed, AC6 fails.
        self.assertFalse(self.admissibility.po1_evidence)

    def test_ac6_fails_for_emergence(self) -> None:
        self.assertFalse(self.admissibility.ac6_restricted_obstructed)

    def test_emergence_kind(self) -> None:
        self.assertEqual(self.record.emergence_kind, "coherence_emergence")


# ---------------------------------------------------------------------------
# Level-skip test
# ---------------------------------------------------------------------------

class TestLevelSkipTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test = build_level_skip_test()

    def test_stepwise_is_po1(self) -> None:
        self.assertTrue(self.test.stepwise_po1)

    def test_direct_is_po1(self) -> None:
        self.assertTrue(self.test.direct_po1)

    def test_verdict_equivalent(self) -> None:
        self.assertTrue(self.test.verdict_equivalent)

    def test_stepwise_forgotten_nonempty(self) -> None:
        self.assertGreater(len(self.test.stepwise_forgotten), 0)

    def test_direct_forgotten_nonempty(self) -> None:
        self.assertGreater(len(self.test.direct_forgotten), 0)

    def test_finding_nonempty(self) -> None:
        self.assertGreater(len(self.test.finding), 0)

    def test_name_set(self) -> None:
        self.assertEqual(self.test.name, "spectre_stepwise_vs_direct")


# ---------------------------------------------------------------------------
# Simultaneous channels (T37 diamond reuse)
# ---------------------------------------------------------------------------

class TestSimultaneousChannels(unittest.TestCase):

    def test_diamond_path_dependent(self) -> None:
        analysis = analyze_network(diamond_network(), "SRC", "TGT")
        self.assertTrue(analysis.path_dependent)

    def test_diamond_has_po1_and_non_po1_paths(self) -> None:
        analysis = analyze_network(diamond_network(), "SRC", "TGT")
        self.assertGreater(len(analysis.po1_paths), 0)
        self.assertGreater(len(analysis.non_po1_paths), 0)


# ---------------------------------------------------------------------------
# Hypothesis evaluations
# ---------------------------------------------------------------------------

class TestHypothesisEvaluations(unittest.TestCase):

    def setUp(self) -> None:
        self.evaluations = _r().hypothesis_evaluations
        self.by_id = {h.hypothesis_id: h for h in self.evaluations}

    def test_five_hypotheses_evaluated(self) -> None:
        self.assertEqual(len(self.evaluations), 5)

    def test_h0_rejected(self) -> None:
        self.assertEqual(self.by_id["H0"].verdict, "rejected")

    def test_h0_covers_three_questions(self) -> None:
        self.assertAlmostEqual(self.by_id["H0"].coverage.coverage_fraction, 0.3)

    def test_h1_best_supported(self) -> None:
        self.assertIn("best_supported", self.by_id["H1"].verdict)

    def test_h1_covers_eight_questions(self) -> None:
        self.assertAlmostEqual(self.by_id["H1"].coverage.coverage_fraction, 0.8)

    def test_h1_missing_q4_q5(self) -> None:
        not_handled = self.by_id["H1"].coverage.not_handled
        self.assertIn("Q4", not_handled)
        self.assertIn("Q5", not_handled)

    def test_h2_not_required(self) -> None:
        self.assertEqual(self.by_id["H2"].verdict, "not_required")

    def test_h3_premature(self) -> None:
        self.assertEqual(self.by_id["H3"].verdict, "premature")

    def test_h4_rejected(self) -> None:
        self.assertEqual(self.by_id["H4"].verdict, "rejected")

    def test_h4_covers_zero_questions(self) -> None:
        self.assertEqual(self.by_id["H4"].coverage.coverage_fraction, 0.0)


# ---------------------------------------------------------------------------
# T38 result
# ---------------------------------------------------------------------------

class TestT38Result(unittest.TestCase):

    def test_best_supported_hypothesis(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H1_extended")

    def test_two_new_objects_required(self) -> None:
        self.assertEqual(len(_r().new_objects_required), 2)
        self.assertIn("CompressionRecord", _r().new_objects_required)
        self.assertIn("EmergenceRecord", _r().new_objects_required)

    def test_h2_not_required(self) -> None:
        self.assertFalse(_r().h2_required)

    def test_h3_not_required(self) -> None:
        self.assertFalse(_r().h3_required)

    def test_theorem_nonempty(self) -> None:
        self.assertGreater(len(_r().theorem), 0)

    def test_boundary_nonempty(self) -> None:
        self.assertGreater(len(_r().boundary), 0)

    def test_recommendation_nonempty(self) -> None:
        self.assertGreater(len(_r().recommendation), 0)

    def test_serialization_produces_dict(self) -> None:
        d = t38_result_to_dict(_r())
        self.assertIsInstance(d, dict)

    def test_serialization_has_expected_keys(self) -> None:
        d = t38_result_to_dict(_r())
        for key in ("compression_record", "emergence_record", "level_skip_test",
                    "simultaneous_channels", "hypothesis_evaluations",
                    "best_supported_hypothesis", "new_objects_required",
                    "h2_required", "h3_required", "theorem"):
            self.assertIn(key, d, msg=f"Missing key: {key}")

    def test_compression_record_in_result(self) -> None:
        self.assertIsInstance(_r().compression_record, CompressionRecord)

    def test_emergence_record_in_result(self) -> None:
        self.assertIsInstance(_r().emergence_record, EmergenceRecord)

    def test_level_skip_test_in_result(self) -> None:
        self.assertIsInstance(_r().level_skip_test, LevelSkipTest)


if __name__ == "__main__":
    unittest.main()
