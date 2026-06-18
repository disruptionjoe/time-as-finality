"""Tests for T36: Compression-Finality Crosswalk."""

import unittest

from models.compression_finality_lab import (
    CompressionFinalitySummary,
    run_compression_finality_analysis,
)

_RESULT: CompressionFinalitySummary | None = None


def _r() -> CompressionFinalitySummary:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_compression_finality_analysis()
    return _RESULT


def _rule(n: int):
    return _r().rules[n]


class TestResultStructure(unittest.TestCase):
    def test_rule_count(self):
        self.assertEqual(_r().rule_count, 256)

    def test_rules_tuple_length(self):
        self.assertEqual(len(_r().rules), 256)

    def test_rule_indices_match(self):
        for i, p in enumerate(_r().rules):
            self.assertEqual(p.rule, i)

    def test_verdict_non_empty(self):
        self.assertTrue(len(_r().verdict) > 0)

    def test_recommendation_non_empty(self):
        self.assertTrue(len(_r().recommendation) > 0)


class TestDivergenceConfirmed(unittest.TestCase):
    def test_divergence_exists(self):
        self.assertTrue(_r().divergence_exists)

    def test_same_survival_different_compression_witness_exists(self):
        self.assertIsNotNone(_r().same_survival_different_compression)

    def test_same_loss_different_compression_witness_exists(self):
        self.assertIsNotNone(_r().same_loss_different_compression)

    def test_same_survival_witness_gap_substantial(self):
        w = _r().same_survival_different_compression
        self.assertIsNotNone(w)
        self.assertGreater(w.gap, 0.2)

    def test_same_loss_witness_gap_substantial(self):
        w = _r().same_loss_different_compression
        self.assertIsNotNone(w)
        self.assertGreater(w.gap, 0.2)

    def test_same_survival_witness_shared_survival_high(self):
        # The best witness should be two rules both with full survival
        w = _r().same_survival_different_compression
        self.assertIsNotNone(w)
        self.assertGreater(w.value_equal, 0.8)


class TestCorrelations(unittest.TestCase):
    def test_compression_survival_correlation_negative(self):
        # High survival → lower compressibility on average (more diverse traces)
        self.assertLess(_r().compression_survival_correlation, 0.0)

    def test_compression_loss_correlation_positive(self):
        # Higher information loss → higher compressibility (attractor collapse)
        self.assertGreater(_r().compression_loss_correlation, 0.0)

    def test_compression_survival_correlation_in_range(self):
        c = _r().compression_survival_correlation
        self.assertGreater(c, -1.0)
        self.assertLess(c, 0.0)

    def test_neither_correlation_is_one(self):
        # Compressibility is not identical to either metric
        self.assertNotAlmostEqual(abs(_r().compression_survival_correlation), 1.0, places=1)
        self.assertNotAlmostEqual(abs(_r().compression_loss_correlation), 1.0, places=1)


class TestRuleZero(unittest.TestCase):
    """Rule 0 (all-zeros attractor): no traces survive → trivially compressible."""
    def test_rule0_zero_survival(self):
        self.assertAlmostEqual(_rule(0).trace_survival_fraction, 0.0, places=3)

    def test_rule0_perfect_compressibility(self):
        self.assertAlmostEqual(_rule(0).trace_compressibility, 1.0, places=2)

    def test_rule0_unique_patterns_is_one(self):
        self.assertEqual(_rule(0).unique_trace_patterns, 1)


class TestRule255(unittest.TestCase):
    """Rule 255 (all-ones attractor): same as Rule 0 structure."""
    def test_rule255_zero_survival(self):
        self.assertAlmostEqual(_rule(255).trace_survival_fraction, 0.0, places=3)

    def test_rule255_perfect_compressibility(self):
        self.assertAlmostEqual(_rule(255).trace_compressibility, 1.0, places=2)


class TestRule30(unittest.TestCase):
    """Rule 30: chaotic, high survival, near-minimum compressibility."""
    def test_rule30_high_survival(self):
        self.assertGreater(_rule(30).trace_survival_fraction, 0.9)

    def test_rule30_low_compressibility(self):
        # Rule 30 should have very low compressibility (diverse trace patterns)
        self.assertLess(_rule(30).trace_compressibility, 0.15)

    def test_rule30_many_unique_patterns(self):
        self.assertGreater(_rule(30).unique_trace_patterns, 20)


class TestRule150(unittest.TestCase):
    """Rule 150: reversible, full survival, moderate compressibility."""
    def test_rule150_injective(self):
        self.assertTrue(_rule(150).injective)

    def test_rule150_zero_lost_bits(self):
        self.assertAlmostEqual(_rule(150).lost_bits, 0.0, places=3)

    def test_rule150_full_survival(self):
        self.assertAlmostEqual(_rule(150).trace_survival_fraction, 1.0, places=3)

    def test_rule150_moderate_compressibility(self):
        # Reversible rule with structured traces — moderate, not zero or one
        comp = _rule(150).trace_compressibility
        self.assertGreater(comp, 0.1)
        self.assertLess(comp, 0.9)


class TestInjectiveVsIrreversible(unittest.TestCase):
    def test_injective_mean_compressibility_positive(self):
        self.assertGreater(_r().injective_mean_compressibility, 0.0)

    def test_irreversible_mean_compressibility_positive(self):
        self.assertGreater(_r().irreversible_mean_compressibility, 0.0)

    def test_all_rules_compressibility_in_unit_interval(self):
        for p in _r().rules:
            with self.subTest(rule=p.rule):
                self.assertGreaterEqual(p.trace_compressibility, 0.0)
                self.assertLessEqual(p.trace_compressibility, 1.0)

    def test_all_rules_entropy_non_negative(self):
        for p in _r().rules:
            with self.subTest(rule=p.rule):
                self.assertGreaterEqual(p.trace_shannon_entropy, 0.0)

    def test_all_rules_total_traces_correct(self):
        # 2^5 = 32 initials × 5 seed indices = 160 traces per rule
        for p in _r().rules:
            self.assertEqual(p.total_traces, 160)


class TestProfileBounds(unittest.TestCase):
    def test_survival_in_unit_interval(self):
        for p in _r().rules:
            with self.subTest(rule=p.rule):
                self.assertGreaterEqual(p.trace_survival_fraction, 0.0)
                self.assertLessEqual(p.trace_survival_fraction, 1.0)

    def test_zlib_ratio_positive(self):
        for p in _r().rules:
            with self.subTest(rule=p.rule):
                self.assertGreater(p.zlib_ratio, 0.0)

    def test_entropy_bounded_by_max(self):
        for p in _r().rules:
            with self.subTest(rule=p.rule):
                self.assertLessEqual(p.trace_shannon_entropy, p.max_possible_entropy + 1e-9)

    def test_unique_patterns_at_least_one(self):
        for p in _r().rules:
            self.assertGreaterEqual(p.unique_trace_patterns, 1)

    def test_lost_bits_non_negative(self):
        for p in _r().rules:
            self.assertGreaterEqual(p.lost_bits, 0.0)


if __name__ == "__main__":
    unittest.main()
