"""Tests for T55 conflict-enriched FinaliEvent descent."""

from __future__ import annotations

import unittest

from models.conflict_finalievent_descent import run_t55_analysis


class ConflictFinaliEventDescentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t55_analysis()
        self.by_name = {completion.datum_name: completion for completion in self.result.completions}

    def test_empty_conflict_special_case_is_preserved(self) -> None:
        completion = self.by_name["T48_empty_conflict_special_case"]
        self.assertEqual(completion.classification, "canonical")
        self.assertTrue(completion.theorem_applies)
        self.assertEqual(completion.conflict_check.conflict_pairs, ())
        self.assertTrue(completion.axis_monotonicity.am_holds)

    def test_canonical_conflict_descent_has_valid_conflict(self) -> None:
        completion = self.by_name["canonical_conflict_descent"]
        self.assertEqual(completion.classification, "canonical")
        self.assertTrue(completion.theorem_applies)
        self.assertTrue(completion.partial_order.is_partial_order)
        self.assertTrue(completion.axis_monotonicity.am_holds)
        self.assertTrue(completion.conflict_check.valid)
        self.assertEqual(
            set(completion.conflict_check.conflict_pairs),
            {("e1", "e2"), ("e2", "e3")},
        )

    def test_conflict_is_not_reconstructed_from_order_or_am(self) -> None:
        conflict = self.by_name["canonical_conflict_descent"]
        no_conflict = self.by_name["same_order_no_conflict_control"]
        self.assertEqual(
            set(conflict.partial_order.order_pairs),
            set(no_conflict.partial_order.order_pairs),
        )
        self.assertTrue(conflict.axis_monotonicity.am_holds)
        self.assertTrue(no_conflict.axis_monotonicity.am_holds)
        self.assertNotEqual(
            set(conflict.conflict_check.conflict_pairs),
            set(no_conflict.conflict_check.conflict_pairs),
        )

    def test_hidden_conflict_is_repaired_by_colimit(self) -> None:
        completion = self.by_name["hidden_conflict_repaired_by_colimit"]
        self.assertEqual(completion.classification, "canonical")
        self.assertTrue(completion.theorem_applies)
        self.assertTrue(completion.conflict_check.valid)
        self.assertEqual(
            set(completion.conflict_check.conflict_pairs),
            {("e1", "e2"), ("e2", "e3")},
        )

    def test_explicit_conflict_disagreement_fails(self) -> None:
        completion = self.by_name["explicit_conflict_disagreement"]
        self.assertEqual(completion.classification, "conflict_invalid")
        self.assertFalse(completion.theorem_applies)
        self.assertTrue(any("explicit_conflict_disagreement" in f for f in completion.condition_failures))

    def test_upward_inheritance_failure_is_conflict_only(self) -> None:
        completion = self.by_name["upward_inheritance_failure"]
        self.assertEqual(completion.classification, "conflict_invalid")
        self.assertTrue(completion.partial_order.is_partial_order)
        self.assertTrue(completion.axis_monotonicity.am_holds)
        self.assertFalse(completion.conflict_check.valid)
        self.assertTrue(any("missing_inherited_conflict" in f for f in completion.condition_failures))

    def test_self_conflict_after_identity_collapse_fails(self) -> None:
        completion = self.by_name["self_conflict_after_identity_collapse"]
        self.assertEqual(completion.classification, "conflict_invalid")
        self.assertFalse(completion.theorem_applies)
        self.assertTrue(any("self_conflict" in f for f in completion.condition_failures))

    def test_hypothesis_verdicts(self) -> None:
        verdicts = {h.hypothesis_id: h.status for h in self.result.hypothesis_evaluations}
        self.assertEqual(verdicts["H0"], "refuted")
        self.assertEqual(verdicts["H1"], "partially_supported")
        self.assertEqual(verdicts["H2"], "supported")
        self.assertEqual(verdicts["H3"], "refuted")
        self.assertEqual(verdicts["H4"], "supported")

    def test_event_structure_machinery_can_still_be_postponed(self) -> None:
        self.assertIn("postponed", self.result.event_structure_verdict)
        self.assertIn("finite conflict checks", self.result.event_structure_verdict)


if __name__ == "__main__":
    unittest.main()
