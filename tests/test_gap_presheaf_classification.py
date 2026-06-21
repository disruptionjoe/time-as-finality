"""Tests for T113: Gap Presheaf Classification."""

from __future__ import annotations

import unittest

from models.gap_presheaf_classification import run_t113_analysis


class GapPresheafClassificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t113_analysis()
        self.audits = {
            (audit.source_pattern, audit.case_name, audit.observer): audit
            for audit in self.result.section_audits
        }

    def test_raw_h0_is_refuted_by_diagnostic_extra_gaps(self) -> None:
        self.assertFalse(self.result.raw_h0_equals_phantoms)
        extra = self.result.raw_h0_gap_sections - self.result.phantom_sections
        self.assertIn(
            (
                "T53",
                "hidden_record_repair:hidden_record_repair_completion",
                "Observer_A",
                "e1->e2",
            ),
            extra,
        )
        self.assertIn(
            ("T58_CONTROL", "local_reversal", "local_reversal", "a->b"),
            extra,
        )

    def test_typed_gap_sections_exactly_match_phantom_sections(self) -> None:
        self.assertTrue(self.result.typed_gap_sections_equal_phantoms)
        self.assertEqual(self.result.typed_gap_sections, self.result.phantom_sections)

    def test_t51_t52_well_formed_sections_remain_exact(self) -> None:
        t51_b = self.audits[("T51", "t51", "Observer_B")]
        self.assertEqual(
            t51_b.typed_gap_pairs,
            frozenset({("e1_A_locking", "e3_composite_locking")}),
        )
        self.assertEqual(t51_b.typed_gap_pairs, t51_b.phantom_pairs)

        t52_a = self.audits[("T52", "t52", "Observer_A")]
        self.assertEqual(
            t52_a.typed_gap_pairs,
            frozenset({("e1_alpha_locking", "e4_delta_locking")}),
        )
        self.assertEqual(t52_a.typed_gap_pairs, t52_a.phantom_pairs)

    def test_t56_hidden_intermediary_classified_as_typed_gap(self) -> None:
        audit = self.audits[("T56", "hidden_intermediary", "U_P")]
        self.assertEqual(audit.gap_pairs, frozenset({("e_j", "e_i")}))
        self.assertEqual(audit.typed_gap_pairs, audit.phantom_pairs)
        self.assertEqual(audit.classification, "typed_exact_match")

    def test_t57_gap_restriction_closure_preserved(self) -> None:
        self.assertTrue(self.result.frp_restriction_closure_preserved)
        self.assertTrue(all(check.holds for check in self.result.frp_gap_checks))
        self.assertTrue(
            any(check.non_lifting_examples for check in self.result.frp_gap_checks)
        )

    def test_t53_noncanonical_repair_is_diagnostic_not_typed(self) -> None:
        audit = self.audits[
            (
                "T53",
                "hidden_record_repair:hidden_record_repair_completion",
                "Observer_A",
            )
        ]
        self.assertEqual(audit.gap_pairs, frozenset({("e1", "e2")}))
        self.assertEqual(audit.typed_gap_pairs, frozenset())
        self.assertEqual(audit.phantom_pairs, frozenset())
        self.assertEqual(audit.classification, "noncanonical_ambient_diagnostic")

    def test_malformed_and_local_reversal_controls_rejected(self) -> None:
        self.assertTrue(self.result.malformed_controls_rejected)
        reversal = self.audits[("T58_CONTROL", "local_reversal", "local_reversal")]
        self.assertFalse(reversal.local_is_suborder)
        self.assertEqual(reversal.spurious_apparent_pairs, frozenset({("b", "a")}))
        self.assertEqual(reversal.typed_gap_pairs, frozenset())

        malformed = self.audits[
            (
                "T113_CONTROL",
                "malformed_extra_local_order",
                "malformed_extra_local_order",
            )
        ]
        self.assertFalse(malformed.local_is_suborder)
        self.assertEqual(malformed.classification, "invalid_local_order_control")
        self.assertEqual(malformed.typed_gap_pairs, frozenset())

    def test_best_supported_is_typed_subobject_not_torsion_claim(self) -> None:
        self.assertIn("typed subobject", self.result.best_supported)
        self.assertIn("not raw H0(G)", self.result.best_supported)
        self.assertTrue(
            any("physical torsion" in guardrail for guardrail in self.result.guardrails)
        )


if __name__ == "__main__":
    unittest.main()
