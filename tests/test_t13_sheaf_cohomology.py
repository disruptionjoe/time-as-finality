"""Tests for T13: Finality Sheaf / Cech Cohomology.

These tests verify the FinalitySection, RestrictionMap, and Cech cochain
machinery added to spacetime_aggregation.py as the T16 → T13 upgrade.

Guardrail: finite order-theoretic cohomology checks only. No physics derivation.
"""

import unittest

from models.spacetime_aggregation import (
    FinalitySection,
    LocalFinalityDomain,
    RestrictionMap,
    cech_coboundary_0,
    compatible_chain_domains,
    compute_h1_obstruction,
    h1_obstruction_scenario,
    is_cech_1_coboundary,
    is_cech_1_cocycle,
)


class FinalitySectionTests(unittest.TestCase):

    def test_score_of_returns_assigned_score(self) -> None:
        s = FinalitySection("D", frozenset({("a", 80), ("b", 40)}))
        self.assertEqual(s.score_of("a"), 80)
        self.assertEqual(s.score_of("b"), 40)

    def test_score_of_raises_for_unknown_event(self) -> None:
        s = FinalitySection("D", frozenset({("a", 50)}))
        with self.assertRaises(KeyError):
            s.score_of("z")

    def test_restrict_projects_to_overlap(self) -> None:
        s = FinalitySection("D", frozenset({("a", 80), ("b", 40), ("c", 60)}))
        r = s.restrict(frozenset({"a", "c"}))
        self.assertEqual(r.event_set(), frozenset({"a", "c"}))
        self.assertEqual(r.score_of("a"), 80)
        self.assertEqual(r.score_of("c"), 60)

    def test_restrict_is_idempotent(self) -> None:
        s = FinalitySection("D", frozenset({("a", 10), ("b", 20), ("c", 30)}))
        overlap = frozenset({"a", "b"})
        self.assertEqual(s.restrict(overlap).restrict(overlap), s.restrict(overlap))

    def test_difference_subtracts_scores_on_shared_events(self) -> None:
        s1 = FinalitySection("D1", frozenset({("x", 70), ("y", 50)}))
        s2 = FinalitySection("D2", frozenset({("x", 40), ("y", 60)}))
        diff = s1.difference(s2)
        self.assertEqual(diff.score_of("x"), 30)
        self.assertEqual(diff.score_of("y"), -10)

    def test_is_zero_true_when_all_scores_zero(self) -> None:
        s = FinalitySection("D", frozenset({("a", 0), ("b", 0)}))
        self.assertTrue(s.is_zero())

    def test_is_zero_false_when_any_nonzero(self) -> None:
        s = FinalitySection("D", frozenset({("a", 0), ("b", 1)}))
        self.assertFalse(s.is_zero())


class RestrictionMapTests(unittest.TestCase):

    def _make_map(
        self, src_scores: dict[str, int], tgt_scores: dict[str, int], overlap: set[str]
    ) -> RestrictionMap:
        overlap_fs = frozenset(overlap)
        return RestrictionMap(
            source_id="A",
            target_id="B",
            overlap_events=overlap_fs,
            source_restriction=FinalitySection(
                "A", frozenset((e, src_scores[e]) for e in overlap)
            ),
            target_restriction=FinalitySection(
                "B", frozenset((e, tgt_scores[e]) for e in overlap)
            ),
        )

    def test_agrees_when_scores_match(self) -> None:
        rm = self._make_map({"x": 50, "y": 30}, {"x": 50, "y": 30}, {"x", "y"})
        self.assertTrue(rm.agrees())

    def test_disagrees_when_scores_differ(self) -> None:
        rm = self._make_map({"x": 50}, {"x": 60}, {"x"})
        self.assertFalse(rm.agrees())

    def test_disagreement_is_difference_on_overlap(self) -> None:
        rm = self._make_map({"x": 70}, {"x": 40}, {"x"})
        diff = rm.disagreement()
        self.assertEqual(diff.score_of("x"), 30)


class CechCoboundary0Tests(unittest.TestCase):

    def _domains(self) -> tuple[LocalFinalityDomain, ...]:
        return (
            LocalFinalityDomain("A", frozenset({"a", "x"}), frozenset({("a", "x")})),
            LocalFinalityDomain("B", frozenset({"b", "x"}), frozenset({("b", "x")})),
        )

    def test_zero_coboundary_when_sections_agree_on_overlap(self) -> None:
        domains = self._domains()
        c0 = {
            "A": FinalitySection("A", frozenset({("a", 80), ("x", 50)})),
            "B": FinalitySection("B", frozenset({("b", 60), ("x", 50)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        self.assertIn(("A", "B"), c1)
        self.assertTrue(c1[("A", "B")].is_zero())

    def test_nonzero_coboundary_when_sections_disagree(self) -> None:
        domains = self._domains()
        c0 = {
            "A": FinalitySection("A", frozenset({("a", 80), ("x", 40)})),
            "B": FinalitySection("B", frozenset({("b", 60), ("x", 70)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        # δ⁰_{AB}(x) = f_B(x) - f_A(x) = 70 - 40 = 30
        self.assertEqual(c1[("A", "B")].score_of("x"), 30)


class CechCocycleTests(unittest.TestCase):

    def _three_domains(self) -> tuple[LocalFinalityDomain, ...]:
        return (
            LocalFinalityDomain("A", frozenset({"a", "p", "q"}), frozenset({("a", "p"), ("p", "q")})),
            LocalFinalityDomain("B", frozenset({"b", "p", "q"}), frozenset({("b", "p"), ("p", "q")})),
            LocalFinalityDomain("C", frozenset({"c", "p", "q"}), frozenset({("c", "p"), ("p", "q")})),
        )

    def test_cocycle_from_coboundary_passes(self) -> None:
        domains = self._three_domains()
        c0 = {
            "A": FinalitySection("A", frozenset({("a", 10), ("p", 0), ("q", 0)})),
            "B": FinalitySection("B", frozenset({("b", 20), ("p", 5), ("q", 3)})),
            "C": FinalitySection("C", frozenset({("c", 30), ("p", 2), ("q", 7)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        is_cocycle, violations = is_cech_1_cocycle(c1, domains)
        self.assertTrue(is_cocycle, f"Expected cocycle, got violations: {violations}")

    def test_manually_inconsistent_c1_fails_cocycle_check(self) -> None:
        domains = self._three_domains()
        # Build c1 from a coboundary first, then corrupt one entry
        c0 = {
            "A": FinalitySection("A", frozenset({("a", 0), ("p", 0), ("q", 0)})),
            "B": FinalitySection("B", frozenset({("b", 0), ("p", 1), ("q", 0)})),
            "C": FinalitySection("C", frozenset({("c", 0), ("p", 0), ("q", 1)})),
        }
        c1 = dict(cech_coboundary_0(c0, domains))
        # Corrupt c_{BC} to break the cocycle condition on triple overlap
        original_bc = c1[("B", "C")]
        corrupted_scores = frozenset(
            (e, s + 99 if e == "p" else s) for e, s in original_bc.scores
        )
        c1[("B", "C")] = FinalitySection(original_bc.domain_id, corrupted_scores)
        is_cocycle, violations = is_cech_1_cocycle(c1, tuple(domains))
        self.assertFalse(is_cocycle)
        self.assertTrue(len(violations) > 0)


class CechCoboundaryCheckTests(unittest.TestCase):

    def _domains(self) -> tuple[LocalFinalityDomain, ...]:
        return (
            LocalFinalityDomain("A", frozenset({"a", "x"}), frozenset({("a", "x")})),
            LocalFinalityDomain("B", frozenset({"b", "x"}), frozenset({("b", "x")})),
            LocalFinalityDomain("C", frozenset({"c", "x"}), frozenset({("c", "x")})),
        )

    def test_cocycle_from_sections_is_coboundary(self) -> None:
        domains = self._domains()
        c0 = {
            "A": FinalitySection("A", frozenset({("a", 10), ("x", 20)})),
            "B": FinalitySection("B", frozenset({("b", 30), ("x", 50)})),
            "C": FinalitySection("C", frozenset({("c", 40), ("x", 35)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        is_cob, witness = is_cech_1_coboundary(c1, domains)
        self.assertTrue(is_cob, "Expected coboundary — c1 was built from sections")
        self.assertIsNotNone(witness)

    def test_coboundary_witness_reconstructs_c1(self) -> None:
        domains = self._domains()
        c0 = {
            "A": FinalitySection("A", frozenset({("a", 0), ("x", 10)})),
            "B": FinalitySection("B", frozenset({("b", 0), ("x", 30)})),
            "C": FinalitySection("C", frozenset({("c", 0), ("x", 5)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        is_cob, witness_f = is_cech_1_coboundary(c1, domains)
        self.assertTrue(is_cob)
        # Verify the witness reproduces c1
        reconstructed = cech_coboundary_0(witness_f, domains)
        for key in c1:
            for e, score in c1[key].scores_dict.items():
                self.assertEqual(reconstructed[key].score_of(e), score)


class H1ObstructionTests(unittest.TestCase):

    def test_compatible_chain_has_no_h1_obstruction(self) -> None:
        domains = compatible_chain_domains()
        c0 = {
            "left-diamond": FinalitySection(
                "left-diamond", frozenset({("a", 10), ("b", 30), ("c", 50)})
            ),
            "right-diamond": FinalitySection(
                "right-diamond", frozenset({("b", 30), ("c", 50), ("d", 70)})
            ),
        }
        result = compute_h1_obstruction(c0, domains)
        self.assertTrue(result["is_cocycle"])
        self.assertTrue(result["is_coboundary"])
        self.assertFalse(result["h1_is_nontrivial"])

    def test_h1_scenario_is_cocycle(self) -> None:
        domains, sections = h1_obstruction_scenario()
        result = compute_h1_obstruction(sections, domains)
        self.assertTrue(result["is_cocycle"], f"Expected cocycle: {result}")

    def test_result_includes_guardrail(self) -> None:
        domains = compatible_chain_domains()
        c0 = {
            "left-diamond": FinalitySection(
                "left-diamond", frozenset({("a", 0), ("b", 0), ("c", 0)})
            ),
            "right-diamond": FinalitySection(
                "right-diamond", frozenset({("b", 0), ("c", 0), ("d", 0)})
            ),
        }
        result = compute_h1_obstruction(c0, domains)
        self.assertIn("guardrail", result)
        self.assertIn("geometry", result["guardrail"])

    def test_existing_t16_tests_still_pass(self) -> None:
        from models.spacetime_aggregation import (
            aggregate_domains,
            compatible_chain_domains,
            cycle_obstruction_domains,
            overlap_conflict_domains,
        )
        self.assertTrue(aggregate_domains(compatible_chain_domains()).glues)
        self.assertFalse(aggregate_domains(overlap_conflict_domains()).glues)
        self.assertFalse(aggregate_domains(cycle_obstruction_domains()).glues)


if __name__ == "__main__":
    unittest.main()
