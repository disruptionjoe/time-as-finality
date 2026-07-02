"""Tests for T397 multipath class-marker absorber audit."""

from __future__ import annotations

import json
import math
import unittest

from models.multipath_class_marker_absorber import (
    GAMMA_SWEEP,
    TOL,
    generic_three_path_classes,
    generic_three_path_labels,
    marker_overlap,
    path_postdiction_success,
    run_t397_analysis,
    scalarizations_fail_binary_at_perfect_record,
    signature,
    signatures_match,
    t395_three_order_classes,
    t395_three_order_labels,
    t397_result_to_dict,
)


class MultipathClassMarkerAbsorberTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t397_analysis()

    def test_canonical_three_order_matches_generic_three_path_signature(self) -> None:
        self.assertTrue(self.result.canonical_equivalence)
        for generic_sig, order_sig in zip(
            self.result.generic_three_path, self.result.canonical_three_order
        ):
            self.assertTrue(signatures_match(generic_sig, order_sig))

    def test_signature_comparison_drops_label_names_only(self) -> None:
        generic = signature(
            "generic",
            generic_three_path_labels(),
            generic_three_path_classes(),
            math.pi / 2.0,
        )
        order = signature(
            "order",
            t395_three_order_labels(),
            t395_three_order_classes(),
            math.pi / 2.0,
        )

        self.assertNotEqual(
            generic.normalized_pairwise_factors[0][0],
            order.normalized_pairwise_factors[0][0],
        )
        self.assertTrue(signatures_match(generic, order))

    def test_same_class_flat_and_cross_class_cosine(self) -> None:
        for sig in self.result.canonical_three_order:
            self.assertAlmostEqual(sig.within_class_factor, 1.0, places=12)
            self.assertAlmostEqual(sig.cross_class_factor, marker_overlap(sig.gamma), places=12)

    def test_path_postdiction_formula(self) -> None:
        for sig in self.result.canonical_three_order:
            expected = (1.0 + math.sin(sig.gamma / 2.0)) / sig.k
            self.assertAlmostEqual(sig.path_postdiction_success, expected, places=12)
            self.assertAlmostEqual(sig.path_postdiction_success, path_postdiction_success(sig.k, sig.gamma), places=12)

    def test_perfect_class_record_ceiling_is_two_over_k(self) -> None:
        self.assertAlmostEqual(
            self.result.canonical_three_order[-1].path_postdiction_success,
            2.0 / 3.0,
            places=12,
        )
        self.assertAlmostEqual(
            self.result.six_path_parity[-1].path_postdiction_success,
            1.0 / 3.0,
            places=12,
        )

    def test_scalarization_failures_are_generic(self) -> None:
        canonical_pi = self.result.canonical_three_order[-1]
        six_pi = self.result.six_path_parity[-1]

        self.assertTrue(scalarizations_fail_binary_at_perfect_record(canonical_pi))
        self.assertTrue(scalarizations_fail_binary_at_perfect_record(six_pi))
        self.assertAlmostEqual(canonical_pi.scalarization_residuals.mean, -23.0 / 36.0, places=12)
        self.assertAlmostEqual(canonical_pi.scalarization_residuals.minimum, -3.0 / 4.0, places=12)
        self.assertAlmostEqual(canonical_pi.scalarization_residuals.maximum, 1.0 / 4.0, places=12)

    def test_exhaustive_bipartition_sweeps_pass(self) -> None:
        expected_counts = {3: 3, 4: 7, 5: 15, 6: 31}
        for sweep in self.result.exhaustive_bipartition_sweeps:
            self.assertEqual(sweep.bipartitions_checked, expected_counts[sweep.k])
            self.assertEqual(sweep.gamma_values_checked, len(GAMMA_SWEEP))
            self.assertTrue(sweep.within_class_flat_all)
            self.assertTrue(sweep.cross_class_duality_all)
            self.assertTrue(sweep.postdiction_formula_all)
            self.assertTrue(sweep.scalarizations_fail_binary_at_perfect_record_all)

    def test_full_resolution_positive_control(self) -> None:
        self.assertAlmostEqual(
            self.result.full_resolution_path_postdiction_at_perfect_record,
            1.0,
            places=12,
        )
        self.assertAlmostEqual(
            self.result.full_resolution_max_pairwise_coherence_at_perfect_record,
            0.0,
            places=12,
        )

    def test_absorber_verdict_is_restrained(self) -> None:
        self.assertIn("absorbed", self.result.absorber_verdict)
        self.assertIn("generic multipath class-marker algebra", self.result.absorber_verdict)
        self.assertNotIn("proves", self.result.absorber_verdict.lower())
        self.assertNotIn("new physics", self.result.strongest_safe_claim.lower())

    def test_gamma_sweep_has_expected_endpoints(self) -> None:
        self.assertLess(abs(GAMMA_SWEEP[0]), TOL)
        self.assertLess(abs(GAMMA_SWEEP[-1] - math.pi), TOL)

    def test_result_dict_is_json_serializable(self) -> None:
        json.dumps(t397_result_to_dict(self.result))


if __name__ == "__main__":
    unittest.main()
