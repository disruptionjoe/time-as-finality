"""Tests for T58: Gap-Phantom Equivalence Audit."""

from __future__ import annotations

import unittest

from models.gap_phantom_equivalence import (
    audit_t51,
    audit_t52,
    build_conflicting_order_control,
    run_t58_audit,
)


class T51GapPhantomTests(unittest.TestCase):
    def setUp(self) -> None:
        self.audits = {a.observer: a for a in audit_t51()}

    def test_observer_a_has_empty_gap_and_no_phantom(self) -> None:
        audit = self.audits["Observer_A"]
        self.assertEqual(audit.gap_pairs, frozenset())
        self.assertEqual(audit.phantom_pairs, frozenset())
        self.assertTrue(audit.gap_equals_phantoms)

    def test_observer_b_gap_is_exact_phantom_pair(self) -> None:
        audit = self.audits["Observer_B"]
        expected = frozenset({("e1_A_locking", "e3_composite_locking")})
        self.assertEqual(audit.gap_pairs, expected)
        self.assertEqual(audit.phantom_pairs, expected)
        self.assertTrue(audit.local_is_suborder)
        self.assertEqual(audit.classification, "exact_match")


class T52GapPhantomTests(unittest.TestCase):
    def setUp(self) -> None:
        self.audits = {a.observer: a for a in audit_t52()}

    def test_observer_a_gap_is_exact_phantom_pair(self) -> None:
        audit = self.audits["Observer_A"]
        expected = frozenset({("e1_alpha_locking", "e4_delta_locking")})
        self.assertEqual(audit.gap_pairs, expected)
        self.assertEqual(audit.phantom_pairs, expected)
        self.assertTrue(audit.local_is_suborder)

    def test_observer_b_gap_is_exact_phantom_pair(self) -> None:
        audit = self.audits["Observer_B"]
        expected = frozenset({("e1_alpha_locking", "e3_gamma_locking")})
        self.assertEqual(audit.gap_pairs, expected)
        self.assertEqual(audit.phantom_pairs, expected)
        self.assertTrue(audit.local_is_suborder)


class BoundaryControlTests(unittest.TestCase):
    def test_reversed_local_order_is_not_phantom_incomparability(self) -> None:
        audit = build_conflicting_order_control()
        self.assertFalse(audit.local_is_suborder)
        self.assertFalse(audit.gap_equals_phantoms)
        self.assertEqual(audit.gap_pairs, frozenset({("a", "b")}))
        self.assertEqual(audit.phantom_pairs, frozenset())
        self.assertEqual(audit.spurious_apparent_pairs, frozenset({("b", "a")}))
        self.assertEqual(audit.classification, "invalid_extension_boundary")


class FullT58AuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t58_audit()

    def test_t51_equivalence_supported(self) -> None:
        self.assertTrue(self.result.t51_gap_equals_phantoms)

    def test_t52_equivalence_supported(self) -> None:
        self.assertTrue(self.result.t52_gap_equals_phantoms)

    def test_extension_boundary_supported(self) -> None:
        self.assertTrue(self.result.extension_condition_necessary)

    def test_all_hypotheses_supported(self) -> None:
        self.assertTrue(
            all(h.status == "supported" for h in self.result.hypothesis_evaluations)
        )

    def test_finding_keeps_bounded_scope(self) -> None:
        self.assertIn("bounded witness class", self.result.finding)
        self.assertIn("blocks a universal reading", self.result.finding)


if __name__ == "__main__":
    unittest.main()
