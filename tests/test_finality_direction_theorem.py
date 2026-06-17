import unittest

from models.finality_direction_theorem import (
    FinalityState,
    FinalityVector,
    classify_transformation,
    run_t18_analysis,
    verify_arrow_theorem,
)


class FinalityDirectionTheoremTests(unittest.TestCase):
    def test_strict_finalization_reverse_is_impossible(self) -> None:
        before = FinalityState("before", FinalityVector(1, 1, 1, 1), 1)
        after = FinalityState("after", FinalityVector(2, 2, 1, 3), 1)

        forward = classify_transformation(before, after)
        reverse = classify_transformation(after, before)

        self.assertEqual(forward.kind, "strict_finalization")
        self.assertTrue(forward.possible)
        self.assertEqual(reverse.kind, "strict_definalization")
        self.assertFalse(reverse.possible)

    def test_arrow_graph_is_acyclic(self) -> None:
        result = verify_arrow_theorem()

        self.assertTrue(result.holds)
        self.assertTrue(result.arrow_graph_acyclic)
        self.assertGreater(result.strict_finalization_edges, 0)

    def test_impossible_transformations_are_not_closed_under_reversal(self) -> None:
        result = verify_arrow_theorem()

        self.assertTrue(result.impossible_set_not_closed_under_reversal)
        self.assertIsNotNone(result.impossible_reversal_witness)
        self.assertFalse(result.impossible_reversal_witness.possible)
        self.assertTrue(result.impossible_reversal_witness.reverse.possible)

    def test_finality_direction_can_diverge_from_thermodynamic_proxy(self) -> None:
        result = verify_arrow_theorem()

        witness = result.thermodynamic_divergence_witness
        self.assertIsNotNone(witness)
        self.assertTrue(witness.possible)
        self.assertEqual(witness.kind, "strict_finalization")
        self.assertLessEqual(
            witness.after.thermodynamic_cost_proxy,
            witness.before.thermodynamic_cost_proxy,
        )

    def test_finality_arrow_is_partial_not_total(self) -> None:
        result = verify_arrow_theorem()

        self.assertTrue(result.partial_order_not_total)
        self.assertIsNotNone(result.incomparable_witness)
        left, right = result.incomparable_witness
        self.assertTrue(left.d1.incomparable_with(right.d1))

    def test_full_analysis_reports_guardrails(self) -> None:
        result = run_t18_analysis()

        self.assertTrue(result["verdict"]["conditional_finality_arrow_derived"])
        self.assertTrue(result["verdict"]["does_not_derive_thermodynamic_arrow"])
        self.assertTrue(result["verdict"]["does_not_replace_proper_time"])
        self.assertTrue(result["verdict"]["arrow_is_partial_not_total"])


if __name__ == "__main__":
    unittest.main()
