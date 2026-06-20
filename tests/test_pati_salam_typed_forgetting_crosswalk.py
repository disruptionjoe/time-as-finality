"""Tests for T88: Pati-Salam typed-forgetting crosswalk."""

from __future__ import annotations

import unittest

from models.pati_salam_typed_forgetting_crosswalk import (
    PAPER_TABLE,
    Multiplet,
    bl_only_projection_audit,
    run_t88_analysis,
    spinor16_weights,
    standard_pati_salam_audit,
    t88_result_to_dict,
)


class PatiSalamTypedForgettingCrosswalkTests(unittest.TestCase):
    def test_spinor16_weight_count_is_exact(self) -> None:
        weights = spinor16_weights()

        self.assertEqual(len(weights), 16)
        for weight in weights:
            minus_count = sum(1 for component in weight if component < 0)
            self.assertEqual(minus_count % 2, 0)

    def test_standard_pati_salam_map_reconstructs_paper_table(self) -> None:
        audit = standard_pati_salam_audit()

        self.assertTrue(audit.exact_table_match)
        self.assertTrue(audit.dimension_preserved)
        self.assertEqual(audit.total_dimension, 16)
        self.assertEqual({m.as_tuple() for m in audit.multiplets}, {m.as_tuple() for m in PAPER_TABLE})
        self.assertEqual(audit.n_values, (-4, -3, 0, 1, 2, 6))
        self.assertEqual(audit.losskernel, frozenset())

    def test_standard_map_has_sm_charge_set(self) -> None:
        audit = standard_pati_salam_audit()

        self.assertEqual(
            set(audit.charge_values),
            {"-1", "-2/3", "-1/3", "0", "1/3", "2/3", "1"},
        )

    def test_b_minus_l_only_projection_preserves_dimension_but_fails_table(self) -> None:
        audit = bl_only_projection_audit()

        self.assertFalse(audit.exact_table_match)
        self.assertTrue(audit.dimension_preserved)
        self.assertEqual(audit.total_dimension, 16)
        self.assertEqual(audit.n_values, (-3, -1, 1, 3))
        self.assertIn("SU2R_cartan_T3R", audit.losskernel)
        self.assertIn("right_isospin_splitting", audit.losskernel)

    def test_b_minus_l_only_projection_merges_right_singlets(self) -> None:
        audit = bl_only_projection_audit()

        self.assertIn(Multiplet("3bar", 1, -1, 6), audit.extra_multiplets)
        self.assertIn(Multiplet("1", 1, 3, 2), audit.extra_multiplets)
        self.assertIn(Multiplet("3bar", 1, 2, 3), audit.missing_paper_multiplets)
        self.assertIn(Multiplet("3bar", 1, -4, 3), audit.missing_paper_multiplets)
        self.assertIn(Multiplet("1", 1, 6, 1), audit.missing_paper_multiplets)
        self.assertIn(Multiplet("1", 1, 0, 1), audit.missing_paper_multiplets)

    def test_result_classifies_as_typed_forgetting_not_po1_or_physics_support(self) -> None:
        result = run_t88_analysis()

        self.assertIn("SU2R_cartan_T3R", result.loss_attribution)
        self.assertIn("not_a_po1_instance", result.po1_status)
        self.assertIn("does not validate GU physics", result.weakened_claim)
        self.assertIn("No current TaF physics claim is upgraded", result.taf_update)

    def test_result_serializes_for_runner(self) -> None:
        payload = t88_result_to_dict(run_t88_analysis())

        self.assertTrue(payload["standard_audit"]["exact_table_match"])
        self.assertFalse(payload["bl_only_audit"]["exact_table_match"])
        self.assertIn("falsification_condition", payload)
        self.assertIn("recommended_next", payload)


if __name__ == "__main__":
    unittest.main()
