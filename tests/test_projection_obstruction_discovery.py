"""Tests for T35: Projection-Obstruction Discovery Engine."""

import unittest

from models.projection_obstruction_discovery import (
    AdmissibilityEvaluator,
    ObstructionExplorer,
    ProjectionGenerator,
    RestrictionSystemGenerator,
    run_t35_analysis,
    run_t35_discovery,
)


class TestT35Generator(unittest.TestCase):
    def test_generates_bounded_system_family(self) -> None:
        specs = RestrictionSystemGenerator().generate()
        self.assertGreaterEqual(len(specs), 8)
        shapes = {spec.shape for spec in specs}
        self.assertIn("triangle_obstruction", shapes)
        self.assertIn("square_obstruction", shapes)
        self.assertIn("local_failure", shapes)

    def test_enumerates_projection_candidates(self) -> None:
        specs = RestrictionSystemGenerator().generate()
        candidates = ProjectionGenerator().enumerate(specs)
        self.assertGreater(len(candidates), 20)
        self.assertTrue(any(candidate.map_mode == "total" for candidate in candidates))
        self.assertTrue(any(candidate.map_mode == "partial" for candidate in candidates))


class TestT35Discovery(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t35_discovery()

    def test_finds_positive_po1_candidate(self) -> None:
        positives = [
            item for item in self.result.classifications
            if item.classification == "admissible_po1"
        ]
        self.assertTrue(positives)
        self.assertTrue(any(item.po1_evidence for item in positives))

    def test_finds_boundary_case(self) -> None:
        boundaries = [
            item for item in self.result.classifications
            if item.classification == "boundary_non_definable"
        ]
        self.assertTrue(boundaries)
        self.assertTrue(any(not item.ac_vector["AC3"] for item in boundaries))

    def test_finds_minimal_counterexample(self) -> None:
        counterexamples = [
            item for item in self.result.classifications
            if item.classification in {"lossy_non_obstructing", "obstruction_removed"}
        ]
        self.assertTrue(counterexamples)
        self.assertTrue(any(item.minimal_witness.witness_type for item in counterexamples))

    def test_finds_novel_positive_signature(self) -> None:
        novel = [
            item for item in self.result.classifications
            if item.classification == "admissible_po1" and not item.known_signature_match
        ]
        self.assertTrue(novel)
        self.assertTrue(any(item.minimal_witness.patch_count >= 4 for item in novel))

    def test_summary_supports_h2_with_caution(self) -> None:
        self.assertEqual(self.result.summary.best_supported_hypothesis, "H2 with H3 caution")
        self.assertGreater(self.result.summary.rediscovered_known_pattern_count, 0)
        self.assertTrue(self.result.summary.novel_positive_candidates)


class TestT35EvaluationShape(unittest.TestCase):
    def test_evaluator_uses_t31_verdicts(self) -> None:
        specs = RestrictionSystemGenerator().generate()
        candidate = next(
            candidate for candidate in ProjectionGenerator().enumerate(specs)
            if candidate.map_mode == "total"
            and candidate.named_forgetting
            and candidate.richer_spec.shape == "empty"
            and candidate.restricted_spec.shape == "triangle_obstruction"
            and candidate.richer_spec.site_count == candidate.restricted_spec.site_count == 3
        )
        result = AdmissibilityEvaluator().classify(candidate, known_signatures=set())
        self.assertEqual(result.t31_verdict, "fully_admissible")
        self.assertEqual(result.classification, "admissible_po1")
        self.assertTrue(result.ac_vector["AC6"])

    def test_run_t35_analysis_returns_expected_shape(self) -> None:
        result = run_t35_analysis()
        self.assertIn("summary", result)
        self.assertIn("classification_examples", result)
        self.assertIn("positive_candidates", result)
        self.assertIn("boundary_candidates", result)
        self.assertIn("minimal_counterexamples", result)
        self.assertIn("novel_positive_candidates", result)
        self.assertEqual(result["summary"]["best_supported_hypothesis"], "H2 with H3 caution")


if __name__ == "__main__":
    unittest.main()
