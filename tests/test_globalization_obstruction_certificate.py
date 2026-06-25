"""T240 test suite: globalization-obstruction certificate (LossKernel route (b) crux).

Real checks, no placeholders. Covers:
  * the Cech H^1 obstruction math (cocycle / coboundary / rank correctness),
  * the same-nu witness fiber (separation; identical nu, gluing, cover; differ
    only in transition cocycle),
  * the full T230/T235 gate harness on the certificate (gate 1, gate 2 against
    nu_struct / nu_piece / nu_cocycle, gates 3a/3b),
  * the decisive route-(b) verdict (no-go via nu_cocycle absorption) AND the
    honest middle finding (survives nu_struct + nu_piece),
  * non-vacuity (the injector clears every gate),
  * HONESTY GUARDS: import-only of the two named siblings, NO import of the d1
    restriction engine (shared-derivation audit), object-identity (compute
    functions are not re-tuned per case), no continuum/general-sheaf assertion.
"""

from __future__ import annotations

import ast
import os
import unittest

from models.attribution_invariant_separation import Case, Lift, nu
import models.globalization_obstruction_certificate as G


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fresh_fiber() -> tuple[Case, Case]:
    G.clear_gluings()
    G.clear_covers()
    G.clear_transitions()
    return G.same_nu_globalization_fiber()


class GlobalizationMathTests(unittest.TestCase):
    """The finite Cech H^1 obstruction is computed correctly."""

    def test_gf2_rank_basic(self) -> None:
        self.assertEqual(G._gf2_rank(((1, 0), (0, 1))), 2)
        self.assertEqual(G._gf2_rank(((1, 1), (1, 1))), 1)
        self.assertEqual(G._gf2_rank(((0, 0), (0, 0))), 0)
        self.assertEqual(G._gf2_rank(()), 0)

    def test_gf2_in_span(self) -> None:
        basis = ((1, 0, 0), (0, 1, 0))
        self.assertTrue(G._gf2_in_span((1, 1, 0), basis))
        self.assertFalse(G._gf2_in_span((0, 0, 1), basis))

    def test_triangle_nerve_h1_rank_is_one(self) -> None:
        """The 3-piece cyclic cover has a triangle nerve with no triple overlap:
        Z^1 = full edge space (rank 3), B^1 = vertex coboundary image (rank 2),
        so H^1 rank = 1 (one independent loop)."""
        patch, _ = _fresh_fiber()
        cover = tuple(frozenset(U) for U in G.cover_of(patch))
        overlaps = G._overlaps(cover)
        triples = G._triple_overlaps(cover)
        self.assertEqual(len(overlaps), 3)
        self.assertEqual(len(triples), 0)
        z1 = G._gf2_rank(G._cocycle_basis(cover, overlaps, triples))
        b1 = G._gf2_rank(G._coboundary_matrix(cover, overlaps))
        self.assertEqual(z1, 3)
        self.assertEqual(b1, 2)
        self.assertEqual(z1 - b1, 1)

    def test_untwisted_is_coboundary_rank_zero(self) -> None:
        patch, _ = _fresh_fiber()
        d = G.globalization_data(patch)
        self.assertEqual(d.transition_signs, (0, 0, 0))
        self.assertTrue(d.is_cocycle)
        self.assertTrue(d.is_coboundary)
        self.assertEqual(d.obstruction_rank, 0)
        self.assertTrue(G.is_globalizable(patch))

    def test_single_twist_is_noncoboundary_rank_one(self) -> None:
        _, obstructed = _fresh_fiber()
        d = G.globalization_data(obstructed)
        self.assertEqual(sum(d.transition_signs), 1)  # exactly one flipped sign
        self.assertTrue(d.is_cocycle)  # no triple overlap => every 1-cochain is a cocycle
        self.assertFalse(d.is_coboundary)  # a single loop sign is not a coboundary
        self.assertEqual(d.obstruction_rank, 1)
        self.assertFalse(G.is_globalizable(obstructed))

    def test_coboundary_twist_is_trivial(self) -> None:
        """A transition cocycle that IS a coboundary (flip the two edges incident
        to one vertex) must give rank 0 -- proving the obstruction quotients by
        coboundaries and is not just 'any nonzero sign'."""
        G.clear_gluings(); G.clear_covers(); G.clear_transitions()
        patch, _ = G.same_nu_globalization_fiber()
        edges = G._overlap_edges()  # ((0,1),(0,2),(1,2))
        # coboundary of vertex 0 = the two edges containing 0: (0,1) and (0,2)
        cob = {edges[0]: 1, edges[1]: 1, edges[2]: 0}
        c = Case(
            name="glob_coboundary_twist",
            target_obstructed=True,
            lifts=patch.lifts,
            composite_map=patch.composite_map,
            target_global_sections=0,
            obstruction_id=patch.obstruction_id,
            free_label="rep",
            path_tag="alpha",
            hidden_source_datum="",
        )
        G.set_gluing(c, G._GLOB_GLUING)
        G.set_cover(c, G._GLOB_COVER)
        G.set_transition(c, cob)
        d = G.globalization_data(c)
        self.assertTrue(d.is_coboundary)
        self.assertEqual(d.obstruction_rank, 0)

    def test_local_automorphisms_are_genuine_finite_groups(self) -> None:
        """Each cover piece carries a nontrivial local nu-fixing automorphism group
        (the swap on the glued overlap pair) -- the obstruction is non-vacuous."""
        patch, _ = _fresh_fiber()
        d = G.globalization_data(patch)
        self.assertTrue(all(o > 1 for o in d.local_group_orders))
        self.assertTrue(all(s == 1 for s in d.overlap_swap_available))


class SameNuFiberTests(unittest.TestCase):
    """The witness pair shares nu, gluing, cover; differs only in the cocycle."""

    def test_pair_shares_nu(self) -> None:
        patch, obstructed = _fresh_fiber()
        self.assertEqual(nu(patch), nu(obstructed))

    def test_pair_shares_gluing_and_cover(self) -> None:
        patch, obstructed = _fresh_fiber()
        self.assertEqual(G._gluing_canonical(patch), G._gluing_canonical(obstructed))
        self.assertEqual(G._cover_canonical(patch), G._cover_canonical(obstructed))

    def test_pair_differs_only_in_transition_cocycle(self) -> None:
        patch, obstructed = _fresh_fiber()
        self.assertNotEqual(
            G.globalization_data(patch).transition_signs,
            G.globalization_data(obstructed).transition_signs,
        )

    def test_certificate_separates_the_pair(self) -> None:
        patch, obstructed = _fresh_fiber()
        self.assertNotEqual(
            G.globalization_obstruction(patch), G.globalization_obstruction(obstructed)
        )


class GateHarnessTests(unittest.TestCase):
    """The full T230/T235 gate harness, run on the globalization certificate."""

    def setUp(self) -> None:
        self.result = G.analyze()

    def test_gate1_separates(self) -> None:
        self.assertTrue(self.result.separates_same_nu_pair)
        self.assertEqual(set(self.result.separating_pair), {"glob_patch", "glob_obstructed"})

    def test_gate2_not_absorbed_by_nu_struct(self) -> None:
        # T235's absorber: field + gluing. Identical on the pair => cannot absorb.
        self.assertFalse(self.result.separation_absorbed_by_nu_struct)

    def test_gate2_not_absorbed_by_nu_piece(self) -> None:
        # the bet's favorable reading: per-vertex local-group iso-classes are
        # identical on the pair => per-piece admission cannot absorb.
        self.assertFalse(self.result.separation_absorbed_by_nu_piece)

    def test_gate2_IS_absorbed_by_nu_cocycle(self) -> None:
        # the binding hostile reading: admitting the transition cocycle (an
        # admissible source relation) reconstructs the obstruction => gate 2 fires.
        self.assertTrue(self.result.separation_absorbed_by_nu_cocycle)

    def test_gate3a_relabel_stable(self) -> None:
        self.assertTrue(self.result.relabel_stable)

    def test_gate3b_local(self) -> None:
        self.assertTrue(self.result.local)

    def test_route_b_does_not_clear(self) -> None:
        self.assertFalse(self.result.clears_route_b)
        self.assertEqual(
            self.result.failure_gate, "gate2_absorbed_by_admitted_transition_cocycle"
        )

    def test_honest_middle_finding_recorded(self) -> None:
        # survives nu_struct AND nu_piece, dies only to nu_cocycle.
        self.assertTrue(self.result.route_b_alive_under_piece_reading_only)

    def test_verdict_is_no_go(self) -> None:
        self.assertEqual(self.result.verdict, "no-go")
        self.assertTrue(self.result.route_a_strengthened)
        self.assertTrue(self.result.losskernel_line_closes_fully)

    def test_obstruction_not_nu_measurable(self) -> None:
        # it DOES separate a same-nu pair, so it is not a function of nu alone.
        self.assertFalse(self.result.obstruction_nu_measurable)


class NonVacuityTests(unittest.TestCase):
    """The injector proves the harness CAN report a clear => the no-go is real."""

    def test_injected_pair_clears_all_gates(self) -> None:
        result = G.analyze()
        self.assertTrue(result.nonvacuity_injected_pair_clears)

    def test_injected_pair_has_identical_enlargements(self) -> None:
        G.clear_gluings(); G.clear_covers(); G.clear_transitions()
        (a, b), inv = G._injected_clearing_pair()
        # the synthetic invariant separates...
        self.assertNotEqual(inv(a), inv(b))
        # ...but every admissible enlargement is identical on the pair.
        self.assertEqual(G.nu_struct(a), G.nu_struct(b))
        self.assertEqual(G.nu_piece(a), G.nu_piece(b))
        self.assertEqual(G.nu_cocycle(a), G.nu_cocycle(b))
        G.clear_gluings(); G.clear_covers(); G.clear_transitions()


class HonestyGuardTests(unittest.TestCase):
    """Falsifiers that would make the result dishonest; confirm none triggers."""

    def _model_source(self) -> str:
        path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "models",
            "globalization_obstruction_certificate.py",
        )
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def _imported_modules(self) -> set[str]:
        tree = ast.parse(self._model_source())
        mods: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                mods.add(node.module)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    mods.add(alias.name)
        return mods

    def test_shared_derivation_audit_no_d1_engine_import(self) -> None:
        """Shared-derivation audit: the obstruction must NOT be built on the d1
        restriction engine (the disqualified transport path). T240 imports only the
        two named LossKernel siblings + stdlib."""
        mods = self._imported_modules()
        forbidden = {m for m in mods if "d1_restriction_system" in m or m.endswith("cap_theorem_bridge")}
        self.assertEqual(forbidden, set(), f"forbidden shared-derivation import(s): {forbidden}")

    def test_imports_only_named_siblings(self) -> None:
        """Import-only discipline: the only non-stdlib model imports are the two
        siblings the lane is permitted to reuse."""
        mods = self._imported_modules()
        model_mods = {m for m in mods if m.startswith("models.")}
        self.assertEqual(
            model_mods,
            {
                "models.attribution_invariant_separation",
                "models.source_automorphism_rigidity",
            },
        )

    def test_object_identity_compute_not_retuned_per_case(self) -> None:
        """The obstruction computer is a SINGLE function applied uniformly; it has
        no per-case branches keyed to case names. Re-running it on a renamed clone
        of each fiber member (same source data) yields the same obstruction -- so
        the certificate is not secretly re-tuned per case."""
        patch, obstructed = _fresh_fiber()
        for case in (patch, obstructed):
            clone = Case(
                name=case.name + "__clone",
                target_obstructed=case.target_obstructed,
                lifts=case.lifts,
                composite_map=case.composite_map,
                target_global_sections=case.target_global_sections,
                obstruction_id=case.obstruction_id,
                free_label=case.free_label,
                path_tag=case.path_tag,
                hidden_source_datum=case.hidden_source_datum,
            )
            G.set_gluing(clone, tuple(tuple(sorted(b)) for b in G.gluing_of(case)))
            G.set_cover(clone, tuple(tuple(sorted(U)) for U in G.cover_of(case)))
            src_edges = G._overlaps(tuple(frozenset(U) for U in G.cover_of(case)))
            tr = G.transition_of(case)
            G.set_transition(clone, {e: tr.get(e, 0) for e in src_edges})
            self.assertEqual(
                G.globalization_obstruction(clone), G.globalization_obstruction(case)
            )
        G.clear_gluings(); G.clear_covers(); G.clear_transitions()

    def test_no_continuum_or_general_sheaf_assertion(self) -> None:
        """The obstruction rank is a finite Z/2 cycle-space rank of a SPECIFIC
        finite cover; nothing in the model asserts a continuum / general
        sheaf-cohomology theorem or sets an is_iso-style flag True from finite
        data. We guard against accidental over-claim by checking the verdict stays
        a test-level no-go, never an unconditional independence/EARNED claim."""
        result = G.analyze()
        self.assertIn(result.verdict, {"no-go", "conditional"})
        # the result must NOT self-promote: it reports route_a_strengthened /
        # losskernel_line_closes_fully as TEST-level facts, and never sets a
        # criterion-6-EARNED boolean (there is no such field by design).
        self.assertFalse(hasattr(result, "criterion_6_earned"))
        self.assertFalse(hasattr(result, "independence_earned"))

    def test_tag_is_finite_witness_poly_decider(self) -> None:
        d = G.result_to_dict(G.analyze())
        self.assertEqual(set(d["tag"]), {"finite_witness", "poly_decider"})


class ImportSiblingGreenTests(unittest.TestCase):
    """Confirm the imported siblings' own analyses still run (no mutation leak)."""

    def test_t230_analysis_runs(self) -> None:
        from models.attribution_invariant_separation import analyze as t230_analyze

        r = t230_analyze()
        self.assertEqual(r.verdict, "no-go")

    def test_t235_analysis_runs(self) -> None:
        from models.source_automorphism_rigidity import analyze as t235_analyze

        r = t235_analyze()
        # T235's own verdict is no-go (route (b) not cleared at its level).
        self.assertEqual(r.verdict, "no-go")


if __name__ == "__main__":
    unittest.main(verbosity=2)
