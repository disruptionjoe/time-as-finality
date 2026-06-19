"""Tests for T54 finite finality descent theorem."""

from __future__ import annotations

import unittest

from models.finality_descent_theorem import run_t54_analysis


class FiniteFinalityDescentTheoremTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t54_analysis()
        self.by_name = {completion.datum_name: completion for completion in self.result.completions}

    def test_t51_and_t52_are_canonical(self) -> None:
        self.assertEqual(self.by_name["T51_phantom_repair"].classification, "canonical")
        self.assertEqual(self.by_name["T52_symmetric_reconstruction"].classification, "canonical")
        self.assertTrue(self.by_name["T51_phantom_repair"].theorem_applies)
        self.assertTrue(self.by_name["T52_symmetric_reconstruction"].theorem_applies)

    def test_t51_reconstructs_phantom_pair(self) -> None:
        completion = self.by_name["T51_phantom_repair"]
        order = set(completion.partial_order.order_pairs)
        self.assertIn(("e1", "e3"), order)
        self.assertIn(("e2", "e3"), order)
        self.assertTrue(completion.axis_monotonicity.am_holds)

    def test_t52_reconstructs_symmetric_reference_order(self) -> None:
        completion = self.by_name["T52_symmetric_reconstruction"]
        order = set(completion.partial_order.order_pairs)
        self.assertIn(("e1", "e3"), order)
        self.assertIn(("e1", "e4"), order)
        self.assertIn(("e2", "e4"), order)
        self.assertTrue(completion.axis_monotonicity.am_holds)

    def test_t53_is_underdetermined_not_canonical(self) -> None:
        completion = self.by_name["T53_ambiguous_identity"]
        self.assertEqual(completion.classification, "underdetermined")
        self.assertFalse(completion.theorem_applies)
        self.assertTrue(any("missing_event_identity" in f for f in completion.condition_failures))

    def test_counterexamples_cover_required_failure_classes(self) -> None:
        expected = {
            "CE_missing_event_identity": "underdetermined",
            "CE_insufficient_overlap": "underdetermined",
            "CE_source_record_conflict": "conflicting",
            "CE_target_record_conflict": "conflicting",
            "CE_axis_profile_conflict": "conflicting",
            "CE_hidden_record_ambiguity": "underdetermined",
            "CE_nondefinable_map": "nondefinable",
            "CE_am_violation": "am_invalid",
        }
        for name, classification in expected.items():
            with self.subTest(name=name):
                self.assertEqual(self.by_name[name].classification, classification)
                self.assertFalse(self.by_name[name].theorem_applies)

    def test_am_violation_has_valid_partial_order_but_failed_am(self) -> None:
        completion = self.by_name["CE_am_violation"]
        self.assertEqual(completion.classification, "am_invalid")
        self.assertTrue(completion.partial_order.is_partial_order)
        self.assertFalse(completion.axis_monotonicity.am_holds)
        self.assertEqual(completion.axis_monotonicity.missing_count, 1)

    def test_hypothesis_verdicts(self) -> None:
        verdicts = {h.hypothesis_id: h.status for h in self.result.hypothesis_evaluations}
        self.assertEqual(verdicts["H0"], "refuted")
        self.assertEqual(verdicts["H1"], "partially_supported")
        self.assertEqual(verdicts["H2"], "supported")
        self.assertEqual(verdicts["H3"], "supported")
        self.assertEqual(verdicts["H4"], "refuted")
        self.assertEqual(verdicts["H5"], "refuted")

    def test_sheaf_machinery_can_be_postponed(self) -> None:
        self.assertIn("postponed", self.result.sheaf_verdict)
        self.assertIn("quotient-union", self.result.sheaf_verdict)


if __name__ == "__main__":
    unittest.main()
