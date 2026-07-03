"""Tests for T421: E3 admissibility adapter (GU-adjacent physics <-> TaF).

Exploratory, recorded-tier. Verifies the machine-checkable assertions 1-5 of the
frozen spec plus the shared-signature type-check on BOTH functors and the
grading-preserving control (M1). GU / pseudo-Hermitian QM is the object of study,
never evidence for a TaF statement; the two functors are built independently.
"""

from __future__ import annotations

import unittest

import numpy as np

from models.e3_admissibility_adapter import (
    FPhys,
    FTaF,
    I2,
    K_FORM,
    LINE_GHOST,
    LINE_PHYS,
    P_PARITY,
    U_NULL,
    V_NULL,
    VerdictFunctor,
    Z_GRADE,
    AdmObject,
    AdmMorphism,
    ObsMorphism,
    build_objects,
    commutant_dimension,
    dagger,
    eta_component,
    generated_algebra_basis,
    is_central,
    k_norm,
    metric_space,
    naturality_square_commutes,
    recovery_exists,
    run_adapter,
)

TOL = 1e-9


class Assertion1KreinAmbientTests(unittest.TestCase):
    """Assertion 1: K = K-dagger, K^2 = I, P^2 = I; K-norms +2 / -2."""

    def test_krein_form_selfadjoint_involution(self):
        self.assertTrue(np.allclose(K_FORM, dagger(K_FORM)))
        self.assertTrue(np.allclose(K_FORM @ K_FORM, I2))

    def test_parity_involution(self):
        self.assertTrue(np.allclose(P_PARITY @ P_PARITY, I2))

    def test_null_basis_pairing(self):
        self.assertAlmostEqual(k_norm(U_NULL), 0.0, places=9)
        self.assertAlmostEqual(k_norm(V_NULL), 0.0, places=9)
        cross = complex((dagger(U_NULL.reshape(-1, 1)) @ K_FORM @ V_NULL.reshape(-1, 1))[0, 0])
        self.assertAlmostEqual(cross, 1.0, places=9)

    def test_eigenline_k_norms(self):
        self.assertAlmostEqual(k_norm(LINE_PHYS), 2.0, places=9)   # physical, P-even
        self.assertAlmostEqual(k_norm(LINE_GHOST), -2.0, places=9)  # ghost, P-odd

    def test_eigenlines_are_parity_eigenvectors(self):
        self.assertTrue(np.allclose(P_PARITY @ LINE_PHYS, LINE_PHYS))
        self.assertTrue(np.allclose(P_PARITY @ LINE_GHOST, -LINE_GHOST))


class Assertion2CommutantTests(unittest.TestCase):
    """Assertion 2: reducible menu has 2-dim commutant; irreducible has 1 (Schur)."""

    def test_M0_reducible(self):
        self.assertEqual(commutant_dimension((I2, P_PARITY), 2), 2)

    def test_Mall_irreducible_schur(self):
        self.assertEqual(commutant_dimension((P_PARITY, Z_GRADE), 2), 1)

    def test_Mall_generates_full_matrix_algebra(self):
        self.assertEqual(len(generated_algebra_basis((P_PARITY, Z_GRADE), 2)), 4)
        self.assertEqual(len(generated_algebra_basis((I2, P_PARITY), 2)), 2)


class Assertion3SharedKnobTests(unittest.TestCase):
    """Assertion 3: the shared knob -- P central in <I,P>, NOT central in M2."""

    def test_P_central_in_M0(self):
        self.assertTrue(is_central(P_PARITY, (I2, P_PARITY), 2))

    def test_P_not_central_in_Mall(self):
        self.assertFalse(is_central(P_PARITY, (P_PARITY, Z_GRADE), 2))


class Assertion4GradingBreakingTests(unittest.TestCase):
    """Assertion 4: Z crosses / breaks the grading; recovery needs it."""

    def test_Z_does_not_commute_with_P(self):
        self.assertGreater(np.linalg.norm(Z_GRADE @ P_PARITY - P_PARITY @ Z_GRADE), TOL)

    def test_Z_maps_ghost_line_onto_physical_line(self):
        image = Z_GRADE @ LINE_GHOST  # (1,-1) -> (1,1)
        self.assertTrue(np.allclose(image, LINE_PHYS))

    def test_recovery_requires_irreducible_menu(self):
        # M0 cannot recover the datum; M_all can.
        self.assertFalse(
            recovery_exists(generated_algebra_basis((I2, P_PARITY), 2),
                            LINE_GHOST, LINE_PHYS, 2)
        )
        self.assertTrue(
            recovery_exists(generated_algebra_basis((P_PARITY, Z_GRADE), 2),
                            LINE_GHOST, LINE_PHYS, 2)
        )


class Assertion5VerdictAgreementTests(unittest.TestCase):
    """Assertion 5: the two functors agree at both objects and on the arrow."""

    def setUp(self):
        self.m0, self.m_all, self.m1 = build_objects()
        self.taf, self.phys = FTaF(), FPhys()

    def test_M0_both_forced(self):
        a = self.taf.on_object(self.m0)
        b = self.phys.on_object(self.m0)
        self.assertEqual((a.grading, a.verdict), ("graded", "FORCED"))
        self.assertEqual((b.grading, b.verdict), ("graded", "FORCED"))

    def test_Mall_both_declared(self):
        a = self.taf.on_object(self.m_all)
        b = self.phys.on_object(self.m_all)
        self.assertEqual((a.grading, a.verdict), ("ungraded", "DECLARED"))
        self.assertEqual((b.grading, b.verdict), ("ungraded", "DECLARED"))

    def test_eta_components_are_isos(self):
        self.assertTrue(eta_component(self.m0).is_iso)
        self.assertTrue(eta_component(self.m_all).is_iso)

    def test_naturality_square_commutes_same_direction(self):
        arrow = ObsMorphism("M0 subset M_all", self.m0, self.m_all)
        self.assertTrue(naturality_square_commutes(arrow))

    def test_metric_space_dims(self):
        self.assertEqual(metric_space(self.m0.menu, 2)[0], 2)      # reducible: family
        self.assertEqual(metric_space(self.m_all.menu, 2)[0], 1)   # irreducible: unique


class GradingPreservingControlTests(unittest.TestCase):
    """M1 localizes: a grading-PRESERVING enlargement does NOT flip the verdict.
    The flip requires specifically a grading-breaking (resource-class A2) operator."""

    def setUp(self):
        _, _, self.m1 = build_objects()
        self.taf, self.phys = FTaF(), FPhys()

    def test_M1_stays_forced(self):
        a = self.taf.on_object(self.m1)
        b = self.phys.on_object(self.m1)
        self.assertEqual(a.verdict, "FORCED")
        self.assertEqual(b.verdict, "FORCED")

    def test_M1_keeps_P_central(self):
        self.assertTrue(is_central(self.m1.parity, self.m1.menu, 2))

    def test_M1_algebra_unchanged(self):
        # grading-preserving U stays in <I,P>: algebra dim stays 2.
        self.assertEqual(len(generated_algebra_basis(self.m1.menu, 2)), 2)


class SharedSignatureTypeCheckTests(unittest.TestCase):
    """Both functors instantiate the ONE signature Obs -> Adm, import-free."""

    def test_both_conform_to_verdict_functor_protocol(self):
        self.assertIsInstance(FTaF(), VerdictFunctor)
        self.assertIsInstance(FPhys(), VerdictFunctor)

    def test_on_object_returns_AdmObject_both_sides(self):
        m0, _, _ = build_objects()
        self.assertIsInstance(FTaF().on_object(m0), AdmObject)
        self.assertIsInstance(FPhys().on_object(m0), AdmObject)

    def test_on_morphism_returns_AdmMorphism_both_sides(self):
        m0, m_all, _ = build_objects()
        arrow = ObsMorphism("a", m0, m_all)
        self.assertIsInstance(FTaF().on_morphism(arrow), AdmMorphism)
        self.assertIsInstance(FPhys().on_morphism(arrow), AdmMorphism)

    def test_import_free_flags(self):
        # F_TaF carries ZERO physics input; F_phys carries ZERO TaF input.
        self.assertFalse(FTaF().reads_physics)
        self.assertFalse(FPhys().reads_taf)

    def test_verdict_monotone_one_way_rule(self):
        # Enlargement only ever un-forces: FORCED -> DECLARED is monotone,
        # the reverse is not.
        forced = AdmObject("graded", "FORCED")
        declared = AdmObject("ungraded", "DECLARED")
        self.assertTrue(AdmMorphism(forced, declared).monotone)
        self.assertFalse(AdmMorphism(declared, forced).monotone)


class AdapterIntegrationTests(unittest.TestCase):
    """End-to-end run_adapter() sanity."""

    def test_run_adapter_all_green(self):
        res = run_adapter()
        self.assertTrue(res["both_functors_typecheck"])
        self.assertTrue(res["naturality_M0_to_Mall"])
        self.assertTrue(res["naturality_M0_to_M1"])
        self.assertEqual(res["objects"]["M0"]["F_TaF"], res["objects"]["M0"]["F_phys"])
        self.assertEqual(res["objects"]["M_all"]["F_TaF"], res["objects"]["M_all"]["F_phys"])


if __name__ == "__main__":
    unittest.main()
