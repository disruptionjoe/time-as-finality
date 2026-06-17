import unittest

from models.spacetime_aggregation import (
    aggregate_domains,
    compatible_chain_domains,
    cycle_obstruction_domains,
    overlap_conflict_domains,
    partial_spacetime_domains,
    run_t16_analysis,
)


class SpacetimeAggregationTests(unittest.TestCase):
    def test_compatible_domains_glue_to_global_partial_order(self) -> None:
        result = aggregate_domains(compatible_chain_domains())

        self.assertTrue(result.glues)
        self.assertIsNotNone(result.global_structure)
        global_structure = result.global_structure
        assert global_structure is not None
        self.assertTrue(global_structure.precedes("a", "d"))
        self.assertEqual(result.obstructions, ())

    def test_overlap_disagreement_is_obstruction(self) -> None:
        result = aggregate_domains(overlap_conflict_domains())

        self.assertFalse(result.glues)
        self.assertEqual(result.obstructions[0].kind, "overlap_disagreement")
        self.assertEqual(set(result.obstructions[0].events), {"a", "b"})

    def test_global_cycle_is_detected_even_when_pairwise_overlaps_are_small(self) -> None:
        result = aggregate_domains(cycle_obstruction_domains())

        self.assertFalse(result.glues)
        self.assertEqual(result.obstructions[0].kind, "global_cycle")
        self.assertEqual(set(result.obstructions[0].events), {"a", "b", "c"})

    def test_partial_global_structure_need_not_be_total(self) -> None:
        result = aggregate_domains(partial_spacetime_domains())

        self.assertTrue(result.glues)
        global_structure = result.global_structure
        assert global_structure is not None
        self.assertIn(("a", "c"), global_structure.incomparable_pairs())
        self.assertTrue(global_structure.precedes("a", "b"))
        self.assertTrue(global_structure.precedes("c", "d"))

    def test_empty_cover_is_invalid(self) -> None:
        with self.assertRaises(ValueError):
            aggregate_domains(())

    def test_full_analysis_reports_guardrails(self) -> None:
        result = run_t16_analysis()

        self.assertTrue(result["compatible_chain"]["glues"])
        self.assertFalse(result["overlap_conflict"]["glues"])
        self.assertFalse(result["cycle_obstruction"]["glues"])
        self.assertTrue(result["verdict"]["spacetime_not_derived"])


if __name__ == "__main__":
    unittest.main()
