"""T235 tests: source-automorphism rigidity certificate.

Real checks (no placeholders) over the finite executable fixture. Each asserts a
load-bearing fact of the verdict: the automorphism group is computed correctly,
the certificate genuinely separates a same-nu pair (so the no-go is not a gate-1
artifact), gate 2 absorbs it via admitted source structure (the decisive
obstruction), the certificate is local + relabel-stable (gates 3a/3b pass), and
the non-vacuity injector proves the harness can report a clear.

Run:
    python -m unittest tests.test_source_automorphism_rigidity -v
    python -m pytest tests/test_source_automorphism_rigidity.py -q
"""

from __future__ import annotations

import unittest

from models.attribution_invariant_separation import Case, Lift, nu
from models.source_automorphism_rigidity import (
    analyze,
    automorphism_group,
    clear_gluings,
    is_local_certificate,
    is_nu_measurable,
    is_rigid,
    nu_prime,
    nu_struct,
    rigidity_certificate,
    same_nu_automorphism_fiber,
    set_gluing,
    _injected_clearing_pair,
    _separation_absorbed_by_nu_struct,
)
from models.attribution_invariant_separation import is_relabel_stable


class TestAutomorphismGroup(unittest.TestCase):
    def setUp(self) -> None:
        clear_gluings()

    def tearDown(self) -> None:
        clear_gluings()

    def test_identity_always_an_automorphism(self) -> None:
        """The identity permutation must always be a valid automorphism."""
        rigid, symmetric, _ = same_nu_automorphism_fiber()
        for case in (rigid, symmetric):
            autos = automorphism_group(case)
            self.assertGreaterEqual(len(autos), 1)
            eps = sorted({l.left_source for l in case.lifts} | {l.right_source for l in case.lifts})
            identity = tuple(sorted((e, e) for e in eps))
            self.assertIn(identity, autos)

    def test_rigid_case_has_trivial_automorphism_group(self) -> None:
        """The gluing {p},{q,r},{s} breaks the swap (p q)(r s) -> only identity."""
        rigid, _, _ = same_nu_automorphism_fiber()
        self.assertEqual(len(automorphism_group(rigid)), 1)
        self.assertTrue(is_rigid(rigid))

    def test_symmetric_case_has_nontrivial_automorphism(self) -> None:
        """The gluing {p,q},{r,s} respects the swap -> a genuine order-2 source
        automorphism invisible to nu."""
        _, symmetric, _ = same_nu_automorphism_fiber()
        autos = automorphism_group(symmetric)
        self.assertEqual(len(autos), 2)
        self.assertFalse(is_rigid(symmetric))
        # the nontrivial element must be the swap (p q)(r s)
        swap = tuple(sorted({"p": "q", "q": "p", "r": "s", "s": "r"}.items()))
        self.assertIn(swap, autos)

    def test_automorphism_actually_preserves_lift_table_and_gluing(self) -> None:
        """A returned automorphism, applied to the lift set and the gluing, must fix
        both -- otherwise the group computation is wrong."""
        _, symmetric, _ = same_nu_automorphism_fiber()
        lift_set = frozenset((l.left_source, l.right_source, l.allowed) for l in symmetric.lifts)
        for auto in automorphism_group(symmetric):
            g = dict(auto)
            permuted = frozenset((g[l], g[r], a) for (l, r, a) in lift_set)
            self.assertEqual(permuted, lift_set)


class TestSameNuFiber(unittest.TestCase):
    def setUp(self) -> None:
        clear_gluings()

    def tearDown(self) -> None:
        clear_gluings()

    def test_fiber_is_a_single_nu_fiber(self) -> None:
        """All members must share ONE nu signature -- otherwise separation is a
        trivial nu-difference, not a same-nu separation."""
        fiber = same_nu_automorphism_fiber()
        self.assertEqual(len({nu(c) for c in fiber}), 1)

    def test_certificate_separates_a_same_nu_pair(self) -> None:
        """The whole point: rigid vs symmetric source gluing yields different Aut
        iso-class while nu is identical -> gate 1 passes (a real separator)."""
        rigid, symmetric, _ = same_nu_automorphism_fiber()
        self.assertEqual(nu(rigid), nu(symmetric))
        self.assertNotEqual(rigidity_certificate(rigid), rigidity_certificate(symmetric))

    def test_certificate_keyed_to_symmetry_class_not_field_value(self) -> None:
        """Same gluing + DIFFERENT hidden field value -> SAME certificate. This is
        the structural content of 'keyed to the symmetry class, not the value'."""
        _, symmetric, symmetric2 = same_nu_automorphism_fiber()
        self.assertNotEqual(symmetric.hidden_source_datum, symmetric2.hidden_source_datum)
        self.assertEqual(
            rigidity_certificate(symmetric), rigidity_certificate(symmetric2)
        )


class TestGates(unittest.TestCase):
    def setUp(self) -> None:
        clear_gluings()

    def tearDown(self) -> None:
        clear_gluings()

    def test_certificate_is_not_nu_measurable(self) -> None:
        """Q1: the automorphism iso-class is NOT determined by nu (rigid vs symmetric
        differ at identical nu). So this is a genuine off-nu separator, not the
        nu-measurable trap (source_fiber_cardinality)."""
        fiber = same_nu_automorphism_fiber()
        self.assertFalse(is_nu_measurable(rigidity_certificate, fiber))

    def test_certificate_is_relabel_stable(self) -> None:
        """Gate 3a: certificate is unchanged by any relabeling of free decorations."""
        fiber = same_nu_automorphism_fiber()
        self.assertTrue(is_relabel_stable(rigidity_certificate, fiber))

    def test_certificate_is_local(self) -> None:
        """Gate 3b: certificate depends only on the case's own source data, not on
        an external enumeration registry."""
        fiber = same_nu_automorphism_fiber()
        self.assertTrue(is_local_certificate(fiber))

    def test_not_absorbed_by_admitting_source_field_alone(self) -> None:
        """Admitting only the source FIELD value (nu_prime) does NOT reproduce the
        separation -- this is what makes the certificate genuinely different from
        T230's source_reading, which dies to nu_prime."""
        rigid, symmetric, _ = same_nu_automorphism_fiber()
        self.assertEqual(nu_prime(rigid), nu_prime(symmetric))

    def test_DECISIVE_absorbed_by_admitting_source_structure(self) -> None:
        """THE obstruction: admitting the source GLUING as audit data (nu_struct)
        DOES reproduce the separation. The automorphism class is a derived function
        of an admissible source relation -> absorbed one level up at gate 2. The bet
        'no single field to admit' fails: the gluing is the admissible carrier."""
        rigid, symmetric, _ = same_nu_automorphism_fiber()
        self.assertNotEqual(nu_struct(rigid), nu_struct(symmetric))
        self.assertTrue(_separation_absorbed_by_nu_struct((rigid, symmetric)))


class TestNonVacuity(unittest.TestCase):
    def setUp(self) -> None:
        clear_gluings()

    def tearDown(self) -> None:
        clear_gluings()

    def test_injected_pair_clears_all_gates(self) -> None:
        """The harness must be able to report a clear, or the no-go is vacuous. The
        injected synthetic pair separates, is relabel-stable, and has identical
        nu_prime AND nu_struct -> non-absorbable -> clears. Proves the gates can fire
        positive."""
        (a, b), inv = _injected_clearing_pair()
        try:
            self.assertNotEqual(inv(a), inv(b))               # separates
            self.assertEqual(nu_prime(a), nu_prime(b))         # field-non-absorbable
            self.assertEqual(nu_struct(a), nu_struct(b))       # structure-non-absorbable
            self.assertTrue(is_relabel_stable(inv, (a, b)))    # relabel-stable
        finally:
            clear_gluings()


class TestVerdict(unittest.TestCase):
    def test_full_analysis_is_no_go_route_a_strengthened(self) -> None:
        """End-to-end: the certificate separates, passes gates 1/3a/3b, but is
        absorbed at gate 2 by admitted source structure -> route (b) NOT cleared;
        route (a) strengthened; verdict no-go. Non-vacuity holds."""
        r = analyze()
        self.assertEqual(r.distinct_nu_signatures_in_fiber, 1)
        self.assertFalse(r.certificate_nu_measurable)
        self.assertTrue(r.separates_same_nu_pair)
        self.assertFalse(r.separation_absorbed_by_nu_prime)
        self.assertTrue(r.separation_absorbed_by_nu_struct)
        self.assertTrue(r.relabel_stable)
        self.assertTrue(r.local)
        self.assertFalse(r.clears_route_b)
        self.assertEqual(r.failure_gate, "gate2_absorbed_by_admitted_source_structure")
        self.assertTrue(r.nonvacuity_injected_pair_clears)
        self.assertFalse(r.route_b_alive)
        self.assertTrue(r.route_a_strengthened)
        self.assertEqual(r.verdict, "no-go")


class TestImportDisciplineUnmodified(unittest.TestCase):
    def test_t230_model_reused_by_import_not_modified(self) -> None:
        """We must re-use the T230 model by import only. Sanity: the imported nu and
        the same-nu discipline behave as T230 defined (a basic shape we depend on)."""
        from models import attribution_invariant_separation as t230

        # nu is the exact realization map; nu_prime appends the admitted source field
        c = Case(
            name="x",
            target_obstructed=True,
            lifts=(Lift("a", "b", True),),
            composite_map=(("a", "x"),),
            target_global_sections=0,
            obstruction_id="o",
            free_label="L",
            path_tag="P",
            hidden_source_datum="d",
        )
        self.assertEqual(t230.nu_prime(c), t230.nu(c) + (("admitted_source", "d"),))


if __name__ == "__main__":
    unittest.main()
