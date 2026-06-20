"""Tests for T13/T16 Cech cohomology extension.

Covers FinalitySection, RestrictionMap, coboundary_0, cocycle check,
coboundary check, H^1 obstruction, and canonical scenarios.
"""

import unittest

from models.spacetime_aggregation import (
    # Existing T16 fixtures — re-tested to confirm no regressions
    aggregate_domains,
    compatible_chain_domains,
    cycle_obstruction_domains,
    overlap_conflict_domains,
    # New sheaf/cohomology API
    CechC0,
    CechC1,
    FinalitySection,
    LocalFinalityDomain,
    RestrictionMap,
    SHEAF_UPGRADE_GUARDRAIL,
    cech_coboundary_0,
    compute_h1_obstruction,
    cyclic_cover_domains,
    h1_nontrivial_c1,
    h1_nontrivial_c1_coboundary_fail,
    h1_obstruction_scenario,
    is_cech_1_coboundary,
    is_cech_1_cocycle,
)


# ---------------------------------------------------------------------------
# 1. FinalitySection
# ---------------------------------------------------------------------------


class TestFinalitySection(unittest.TestCase):
    def _make(self) -> FinalitySection:
        return FinalitySection(
            domain_id="test",
            scores=frozenset({("e1", 10), ("e2", 30), ("e3", 50)}),
        )

    def test_score_of_returns_correct_value(self) -> None:
        sec = self._make()
        self.assertEqual(sec.score_of("e1"), 10)
        self.assertEqual(sec.score_of("e3"), 50)

    def test_score_of_raises_for_unknown_event(self) -> None:
        sec = self._make()
        with self.assertRaises(KeyError):
            sec.score_of("eX")

    def test_event_set(self) -> None:
        sec = self._make()
        self.assertEqual(sec.event_set(), frozenset({"e1", "e2", "e3"}))

    def test_events_alias(self) -> None:
        sec = self._make()
        self.assertEqual(sec.events(), sec.event_set())

    def test_restrict_returns_subset(self) -> None:
        sec = self._make()
        restricted = sec.restrict(frozenset({"e1", "e3"}))
        self.assertEqual(restricted.event_set(), frozenset({"e1", "e3"}))
        self.assertEqual(restricted.score_of("e1"), 10)
        self.assertEqual(restricted.score_of("e3"), 50)

    def test_restrict_to_empty_set(self) -> None:
        sec = self._make()
        restricted = sec.restrict(frozenset())
        self.assertEqual(restricted.event_set(), frozenset())

    def test_restrict_raises_for_unknown_events(self) -> None:
        sec = self._make()
        with self.assertRaises(ValueError):
            sec.restrict(frozenset({"e1", "eUnknown"}))

    def test_restrict_presheaf_commutativity(self) -> None:
        """restrict is a presheaf morphism: restrict(A).restrict(B) == restrict(B) for B <= A."""
        sec = self._make()
        A = frozenset({"e1", "e2"})
        B = frozenset({"e1"})
        self.assertEqual(sec.restrict(A).restrict(B), sec.restrict(B))

    def test_difference_on_shared_events(self) -> None:
        sec_a = FinalitySection("A", frozenset({("e1", 40), ("e2", 60)}))
        sec_b = FinalitySection("B", frozenset({("e1", 10), ("e2", 20)}))
        diff = sec_a.difference(sec_b)
        self.assertEqual(diff.score_of("e1"), 30)
        self.assertEqual(diff.score_of("e2"), 40)

    def test_difference_only_on_shared_events(self) -> None:
        sec_a = FinalitySection("A", frozenset({("e1", 40), ("e2", 60)}))
        sec_b = FinalitySection("B", frozenset({("e1", 10), ("e3", 20)}))
        diff = sec_a.difference(sec_b)
        self.assertEqual(diff.event_set(), frozenset({"e1"}))

    def test_is_zero_true(self) -> None:
        sec = FinalitySection("zero", frozenset({("e1", 0), ("e2", 0)}))
        self.assertTrue(sec.is_zero())

    def test_is_zero_false(self) -> None:
        sec = FinalitySection("nonzero", frozenset({("e1", 0), ("e2", 5)}))
        self.assertFalse(sec.is_zero())

    def test_is_zero_empty_section(self) -> None:
        sec = FinalitySection("empty", frozenset())
        self.assertTrue(sec.is_zero())

    def test_scores_dict_property(self) -> None:
        sec = self._make()
        d = sec.scores_dict
        self.assertIsInstance(d, dict)
        self.assertEqual(d["e1"], 10)

    def test_hashable_and_frozen(self) -> None:
        sec = self._make()
        # Should be usable as a dict key
        d = {sec: "value"}
        self.assertEqual(d[sec], "value")


# ---------------------------------------------------------------------------
# 2. RestrictionMap
# ---------------------------------------------------------------------------


class TestRestrictionMap(unittest.TestCase):
    def _make_agreeing(self) -> RestrictionMap:
        overlap = frozenset({"e1", "e2"})
        shared = FinalitySection("shared", frozenset({("e1", 10), ("e2", 30)}))
        return RestrictionMap(
            source_id="A",
            target_id="B",
            overlap_events=overlap,
            source_restriction=shared,
            target_restriction=shared,
        )

    def _make_disagreeing(self) -> RestrictionMap:
        overlap = frozenset({"e1", "e2"})
        src = FinalitySection("A_overlap", frozenset({("e1", 10), ("e2", 30)}))
        tgt = FinalitySection("B_overlap", frozenset({("e1", 10), ("e2", 99)}))
        return RestrictionMap(
            source_id="A",
            target_id="B",
            overlap_events=overlap,
            source_restriction=src,
            target_restriction=tgt,
        )

    def test_agrees_when_sections_identical(self) -> None:
        rm = self._make_agreeing()
        self.assertTrue(rm.agrees())

    def test_disagrees_when_sections_differ(self) -> None:
        rm = self._make_disagreeing()
        self.assertFalse(rm.agrees())

    def test_disagreement_is_zero_when_agreeing(self) -> None:
        rm = self._make_agreeing()
        self.assertTrue(rm.disagreement().is_zero())

    def test_disagreement_shows_difference(self) -> None:
        rm = self._make_disagreeing()
        diff = rm.disagreement()
        # source(e2)=30, target(e2)=99 -> diff = 30-99 = -69
        self.assertEqual(diff.score_of("e2"), -69)
        # e1 is same -> diff = 0
        self.assertEqual(diff.score_of("e1"), 0)


# ---------------------------------------------------------------------------
# 3. cech_coboundary_0
# ---------------------------------------------------------------------------


class TestCechCoboundary0(unittest.TestCase):
    def test_zero_on_compatible_sections(self) -> None:
        """delta^0(f) = 0 when all sections agree on overlaps."""
        domains = (
            LocalFinalityDomain("A", frozenset({"e1", "e2"}), frozenset()),
            LocalFinalityDomain("B", frozenset({"e2", "e3"}), frozenset()),
        )
        # e2 appears in both; give it the same score
        c0: CechC0 = {
            "A": FinalitySection("A", frozenset({("e1", 10), ("e2", 30)})),
            "B": FinalitySection("B", frozenset({("e2", 30), ("e3", 50)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        self.assertIn(("A", "B"), c1)
        section_ab = c1[("A", "B")]
        # delta^0(f)_{AB}(e2) = f_B(e2) - f_A(e2) = 30 - 30 = 0
        self.assertEqual(section_ab.score_of("e2"), 0)
        self.assertTrue(section_ab.is_zero())

    def test_nonzero_on_differing_sections(self) -> None:
        domains = (
            LocalFinalityDomain("A", frozenset({"e1", "e2"}), frozenset()),
            LocalFinalityDomain("B", frozenset({"e2", "e3"}), frozenset()),
        )
        c0: CechC0 = {
            "A": FinalitySection("A", frozenset({("e1", 10), ("e2", 30)})),
            "B": FinalitySection("B", frozenset({("e2", 70), ("e3", 50)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        # delta^0(f)_{AB}(e2) = f_B(e2) - f_A(e2) = 70 - 30 = 40
        self.assertEqual(c1[("A", "B")].score_of("e2"), 40)

    def test_keys_use_canonical_ordering(self) -> None:
        """Keys in C^1 must be (i,j) with i < j lexicographically."""
        domains = (
            LocalFinalityDomain("Z", frozenset({"e1", "e2"}), frozenset()),
            LocalFinalityDomain("A", frozenset({"e2", "e3"}), frozenset()),
        )
        c0: CechC0 = {
            "Z": FinalitySection("Z", frozenset({("e1", 10), ("e2", 30)})),
            "A": FinalitySection("A", frozenset({("e2", 30), ("e3", 50)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        # "A" < "Z" lexicographically, so key must be ("A", "Z")
        self.assertIn(("A", "Z"), c1)
        self.assertNotIn(("Z", "A"), c1)

    def test_empty_overlap_not_in_c1(self) -> None:
        """Pairs with no overlap should not appear in C^1."""
        domains = (
            LocalFinalityDomain("A", frozenset({"e1"}), frozenset()),
            LocalFinalityDomain("B", frozenset({"e2"}), frozenset()),
        )
        c0: CechC0 = {
            "A": FinalitySection("A", frozenset({("e1", 10)})),
            "B": FinalitySection("B", frozenset({("e2", 20)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        self.assertEqual(len(c1), 0)

    def test_three_domains_all_pairs_covered(self) -> None:
        domains, sections = h1_obstruction_scenario()
        c1 = cech_coboundary_0(sections, domains)
        # A∩B={eX,e2}, A∩C={eX,e1}, B∩C={eX,e3} -> 3 pairs
        self.assertEqual(len(c1), 3)
        self.assertIn(("A", "B"), c1)
        self.assertIn(("A", "C"), c1)
        self.assertIn(("B", "C"), c1)


# ---------------------------------------------------------------------------
# 4. is_cech_1_cocycle
# ---------------------------------------------------------------------------


class TestIsCech1Cocycle(unittest.TestCase):
    def test_coboundary_is_always_a_cocycle(self) -> None:
        """Any c1 = delta^0(f) must satisfy the cocycle condition."""
        domains, sections = h1_obstruction_scenario()
        c1 = cech_coboundary_0(sections, domains)
        is_cocycle, witness = is_cech_1_cocycle(c1, domains)
        self.assertTrue(is_cocycle)
        self.assertIsNone(witness)

    def test_non_cocycle_detected_with_witness(self) -> None:
        """A C^1 cochain violating the triple overlap condition is flagged."""
        domains, _ = h1_obstruction_scenario()
        # Manually build a c1 with nonzero holonomy on the triple overlap {eX}
        # c_{BC}(eX) - c_{AC}(eX) + c_{AB}(eX) = 10 - 0 + 0 = 10 != 0
        bad_c1: CechC1 = {
            ("A", "B"): FinalitySection("A__B", frozenset({("eX", 0), ("e2", 0)})),
            ("A", "C"): FinalitySection("A__C", frozenset({("eX", 0), ("e1", 0)})),
            ("B", "C"): FinalitySection("B__C", frozenset({("eX", 10), ("e3", 0)})),
        }
        is_cocycle, witness = is_cech_1_cocycle(bad_c1, domains)
        self.assertFalse(is_cocycle)
        self.assertIsNotNone(witness)
        triple, violation_section = witness  # type: ignore[misc]
        self.assertEqual(set(triple), {"A", "B", "C"})
        # The violation magnitude at eX should be 10
        self.assertEqual(violation_section.score_of("eX"), 10)

    def test_valid_cocycle_passes(self) -> None:
        """A c1 satisfying the cocycle condition returns True."""
        domains, _ = h1_obstruction_scenario()
        # c_{BC}(eX) - c_{AC}(eX) + c_{AB}(eX) = 10 - 20 + 10 = 0
        good_c1: CechC1 = {
            ("A", "B"): FinalitySection("A__B", frozenset({("eX", 10), ("e2", 0)})),
            ("A", "C"): FinalitySection("A__C", frozenset({("eX", 20), ("e1", 0)})),
            ("B", "C"): FinalitySection("B__C", frozenset({("eX", 10), ("e3", 0)})),
        }
        is_cocycle, witness = is_cech_1_cocycle(good_c1, domains)
        self.assertTrue(is_cocycle)
        self.assertIsNone(witness)

    def test_consistent_c1_on_cyclic_cover_is_cocycle(self) -> None:
        """A c1 satisfying c_{BC} - c_{AC} + c_{AB} = 0 on the triple overlap is a cocycle."""
        domains = cyclic_cover_domains()
        # c_{BC}(eShared) - c_{AC}(eShared) + c_{AB}(eShared) = 10 - 20 + 10 = 0
        consistent_c1: CechC1 = {
            ("A", "B"): FinalitySection("A__B", frozenset({("eShared", 10)})),
            ("B", "C"): FinalitySection("B__C", frozenset({("eShared", 10)})),
            ("A", "C"): FinalitySection("A__C", frozenset({("eShared", 20)})),
        }
        is_cocycle, witness = is_cech_1_cocycle(consistent_c1, domains)
        self.assertTrue(is_cocycle)
        self.assertIsNone(witness)


# ---------------------------------------------------------------------------
# 5. is_cech_1_coboundary
# ---------------------------------------------------------------------------


class TestIsCech1Coboundary(unittest.TestCase):
    def test_zero_c1_is_coboundary(self) -> None:
        """The zero cochain is always a coboundary (f = 0 works)."""
        domains = (
            LocalFinalityDomain("A", frozenset({"e1", "e2"}), frozenset()),
            LocalFinalityDomain("B", frozenset({"e2", "e3"}), frozenset()),
        )
        c0: CechC0 = {
            "A": FinalitySection("A", frozenset({("e1", 10), ("e2", 30)})),
            "B": FinalitySection("B", frozenset({("e2", 30), ("e3", 50)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        is_cob, witness_f = is_cech_1_coboundary(c1, domains)
        self.assertTrue(is_cob)
        self.assertIsNotNone(witness_f)

    def test_coboundary_check_returns_witness_f(self) -> None:
        """When coboundary exists, verify delta^0(witness_f) matches c1."""
        domains = (
            LocalFinalityDomain("A", frozenset({"e1", "e2"}), frozenset()),
            LocalFinalityDomain("B", frozenset({"e2", "e3"}), frozenset()),
        )
        c0: CechC0 = {
            "A": FinalitySection("A", frozenset({("e1", 10), ("e2", 30)})),
            "B": FinalitySection("B", frozenset({("e2", 50), ("e3", 70)})),
        }
        c1 = cech_coboundary_0(c0, domains)
        is_cob, witness_f = is_cech_1_coboundary(c1, domains)
        self.assertTrue(is_cob)
        assert witness_f is not None
        # Recompute delta^0 from witness_f and compare with c1
        recomputed = cech_coboundary_0(witness_f, domains)
        for key in c1:
            for e in c1[key].event_set():
                self.assertEqual(c1[key].score_of(e), recomputed[key].score_of(e))

    def test_nontrivial_c1_is_not_coboundary(self) -> None:
        """The cyclic cover c1 with contradictory constraint is not a coboundary."""
        domains = cyclic_cover_domains()
        c1 = h1_nontrivial_c1_coboundary_fail(domains)
        is_cob, witness_f = is_cech_1_coboundary(c1, domains)
        self.assertFalse(is_cob)
        self.assertIsNone(witness_f)

    def test_three_domain_consistent_sections_is_coboundary(self) -> None:
        """Sections from h1_obstruction_scenario are globally consistent -> coboundary."""
        domains, sections = h1_obstruction_scenario()
        c1 = cech_coboundary_0(sections, domains)
        is_cob, witness_f = is_cech_1_coboundary(c1, domains)
        self.assertTrue(is_cob)
        self.assertIsNotNone(witness_f)


# ---------------------------------------------------------------------------
# 6. compute_h1_obstruction — h1_obstruction_scenario (pairwise agree, H^1=0)
# ---------------------------------------------------------------------------


class TestComputeH1Obstruction(unittest.TestCase):
    def test_consistent_three_domain_scenario_h1_trivial(self) -> None:
        """The canonical three-domain scenario has H^1 = 0 (globally consistent)."""
        domains, sections = h1_obstruction_scenario()
        result = compute_h1_obstruction(sections, domains)
        self.assertTrue(result["is_cocycle"])
        self.assertTrue(result["is_coboundary"])
        self.assertFalse(result["h1_is_nontrivial"])

    def test_result_contains_c1(self) -> None:
        domains, sections = h1_obstruction_scenario()
        result = compute_h1_obstruction(sections, domains)
        c1 = result["c1"]
        self.assertIsInstance(c1, dict)
        self.assertIn(("A", "B"), c1)

    def test_result_keys_present(self) -> None:
        domains, sections = h1_obstruction_scenario()
        result = compute_h1_obstruction(sections, domains)
        for key in ("c1", "is_cocycle", "is_coboundary", "h1_is_nontrivial", "obstruction_witness"):
            self.assertIn(key, result)


# ---------------------------------------------------------------------------
# 7. compute_h1_obstruction — compatible_chain_domains (T16 fixture)
# ---------------------------------------------------------------------------


class TestH1OnT16CompatibleChain(unittest.TestCase):
    def test_compatible_chain_h1_trivial(self) -> None:
        """The T16 compatible chain domains have H^1 = 0."""
        domains = compatible_chain_domains()
        # Build simple finality sections consistent with the chain a<b<c<d
        sections: CechC0 = {
            "left-diamond": FinalitySection(
                "left-diamond", frozenset({("a", 10), ("b", 30), ("c", 50)})
            ),
            "right-diamond": FinalitySection(
                "right-diamond", frozenset({("b", 30), ("c", 50), ("d", 70)})
            ),
        }
        result = compute_h1_obstruction(sections, domains)
        self.assertTrue(result["is_cocycle"])
        self.assertTrue(result["is_coboundary"])
        self.assertFalse(result["h1_is_nontrivial"])


# ---------------------------------------------------------------------------
# 8. Nontrivial H^1 via cyclic cover
# ---------------------------------------------------------------------------


class TestNontrivialH1CyclicCover(unittest.TestCase):
    def test_cyclic_cover_nontrivial_c1_is_not_coboundary(self) -> None:
        """Contradictory constraint on eShared is not a coboundary.

        h1_nontrivial_c1_coboundary_fail defines:
            c_{AB}(eShared) = 10, c_{BC}(eShared) = 10, c_{AC}(eShared) = 30
        BFS assigns f_A=0, f_B=10, f_C=20 (via B), then checks f_C from A direct: 0+30=30 != 20.

        All three domains share eShared, so there IS a triple overlap and the cocycle
        condition also fails (c_{BC} - c_{AC} + c_{AB} = 10 - 30 + 10 = -10 != 0).
        Both conditions detect the inconsistency; the coboundary check is the primary one.
        """
        domains = cyclic_cover_domains()
        c1 = h1_nontrivial_c1_coboundary_fail(domains)
        # This c1 also fails the cocycle check (triple overlap exists)
        is_cocycle, _ = is_cech_1_cocycle(c1, domains)
        self.assertFalse(is_cocycle)
        # And NOT a coboundary (contradictory constraint detected by BFS)
        is_cob, _ = is_cech_1_coboundary(c1, domains)
        self.assertFalse(is_cob)

    def test_consistent_c1_on_cyclic_cover_is_coboundary(self) -> None:
        """A c1 where constraints are mutually consistent IS a coboundary."""
        domains = cyclic_cover_domains()
        # c_{AC}(eShared) = 20 = 10 + 10 -> consistent: f_A=0, f_B=10, f_C=20
        consistent_c1: CechC1 = {
            ("A", "B"): FinalitySection("A__B", frozenset({("eShared", 10)})),
            ("B", "C"): FinalitySection("B__C", frozenset({("eShared", 10)})),
            ("A", "C"): FinalitySection("A__C", frozenset({("eShared", 20)})),
        }
        is_cob, witness_f = is_cech_1_coboundary(consistent_c1, domains)
        self.assertTrue(is_cob)
        self.assertIsNotNone(witness_f)

    def test_h1_nontrivial_c1_also_fails_cocycle(self) -> None:
        """The h1_nontrivial_c1 cochain (with triple overlap) also fails the cocycle check."""
        domains = cyclic_cover_domains()
        c1 = h1_nontrivial_c1(domains)
        # Triple overlap = {eShared} for (A,B,C)
        # c_{BC} - c_{AC} + c_{AB} = 10 - 30 + 10 = -10 != 0
        is_cocycle, witness = is_cech_1_cocycle(c1, domains)
        self.assertFalse(is_cocycle)
        self.assertIsNotNone(witness)


# ---------------------------------------------------------------------------
# 9. SHEAF_UPGRADE_GUARDRAIL string
# ---------------------------------------------------------------------------


class TestGuardrail(unittest.TestCase):
    def test_guardrail_string_present(self) -> None:
        self.assertIsInstance(SHEAF_UPGRADE_GUARDRAIL, str)
        self.assertIn("finite order-theoretic cohomology", SHEAF_UPGRADE_GUARDRAIL)
        self.assertIn("spacetime geometry", SHEAF_UPGRADE_GUARDRAIL)

    def test_guardrail_denies_physical_derivation(self) -> None:
        self.assertIn("does not derive", SHEAF_UPGRADE_GUARDRAIL)


# ---------------------------------------------------------------------------
# 10. Regression: existing T16 tests
# ---------------------------------------------------------------------------


class TestT16Regression(unittest.TestCase):
    def test_compatible_domains_glue(self) -> None:
        result = aggregate_domains(compatible_chain_domains())
        self.assertTrue(result.glues)

    def test_overlap_conflict_is_obstruction(self) -> None:
        result = aggregate_domains(overlap_conflict_domains())
        self.assertFalse(result.glues)
        self.assertEqual(result.obstructions[0].kind, "overlap_disagreement")

    def test_cycle_obstruction_detected(self) -> None:
        result = aggregate_domains(cycle_obstruction_domains())
        self.assertFalse(result.glues)
        self.assertEqual(result.obstructions[0].kind, "global_cycle")

    def test_empty_cover_invalid(self) -> None:
        with self.assertRaises(ValueError):
            aggregate_domains(())


if __name__ == "__main__":
    unittest.main()
