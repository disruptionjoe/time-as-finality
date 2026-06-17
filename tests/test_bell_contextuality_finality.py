import unittest

from models.bell_contextuality_finality import (
    analyze_chsh_finality,
    canonical_chsh_finality_scenario,
    local_section_for_context,
    run_t21_analysis,
)


class BellContextualityFinalityTests(unittest.TestCase):
    def test_each_context_has_local_finality_section(self) -> None:
        scenario = canonical_chsh_finality_scenario()

        for context in scenario.contexts:
            section = local_section_for_context(context)
            self.assertEqual(len(section.assignments), 2)
            self.assertTrue(
                all(left * right == context.parity for left, right in section.assignments)
            )

    def test_canonical_chsh_has_no_global_assignment(self) -> None:
        result = analyze_chsh_finality()

        self.assertTrue(result.all_local_sections_exist)
        self.assertTrue(result.compatible_on_named_overlaps)
        self.assertTrue(result.no_global_assignment)
        self.assertTrue(result.h1_style_obstruction)

    def test_contextuality_witness_has_chsh_parity_contradiction(self) -> None:
        result = analyze_chsh_finality()

        self.assertEqual(result.contextuality_witness.parity_product, -1)
        self.assertEqual(result.contextuality_witness.expected_noncontextual_product, 1)
        self.assertIn("global assignment", result.contextuality_witness.contradiction)

    def test_contexts_encode_three_same_one_different_pattern(self) -> None:
        result = analyze_chsh_finality()

        relations = [section.relation for section in result.local_sections]
        self.assertEqual(relations.count("same"), 3)
        self.assertEqual(relations.count("different"), 1)

    def test_full_analysis_reports_guardrails(self) -> None:
        result = run_t21_analysis()

        self.assertTrue(result["verdict"]["bell_chsh_mapping_constructed"])
        self.assertTrue(result["verdict"]["local_finality_without_global_section"])
        self.assertTrue(result["verdict"]["contextuality_certificate_detected"])
        self.assertTrue(
            result["verdict"]["physical_referent_is_structural_not_probabilistic"]
        )
        self.assertIn("not a simulation", result["interpretation"]["guardrail"])


if __name__ == "__main__":
    unittest.main()
