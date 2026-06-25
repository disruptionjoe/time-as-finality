"""Tests for T229: Rank-2 second unrelated absorber (the breakout's promotion gate).

Real checks, not placeholders. They verify:
  1. The domain-A kappa_A = 2 instance (two disjoint T39 odd cycles) really has
     kappa = 2 under the UNCHANGED T224 compute_kappa.
  2. The native two-box CHSH witness counts independent frustrated boxes via T21's
     OWN parity-product per box, and separates rank 0 / 1 / 2 (NOT a binary present/
     absent classifier).
  3. The transported prediction kappa_B' = 2 matches BOTH the native two-box rank
     AND the nu-side kappa, with the off-by-one guard (kappa_A=1 -> native 1, NOT 2).
  4. No shared derivation: neither T21 nor this module imports the T39 engine; T28/
     CAP would (the disqualified alternative).
  5. The native witness does NOT secretly call compute_kappa (independence of the
     two measurements).
  6. The verdict logic fires PASS_RANK2 only when BOTH T224 conditions clear.
"""

from __future__ import annotations

import inspect
import unittest

from models.typed_loss_transport import compute_kappa, nu_from_chsh
import models.kappa_rank2_transport as r2
from models.kappa_rank2_transport import (
    build_two_cell_transitive_obstruction,
    build_one_cell_transitive_cover,
    build_zero_cell_cover,
    build_two_box_chsh,
    native_two_box_obstruction,
    shared_derivation_audit_rank2,
    run_rank2_transport_test,
)


class TestDomainAKappa2(unittest.TestCase):
    def test_two_cell_transitive_has_kappa_2(self):
        cover = build_two_cell_transitive_obstruction()
        k = compute_kappa(cover)
        self.assertEqual(k.kappa, 2)
        self.assertTrue(k.frustrated)
        self.assertFalse(k.global_section_exists)

    def test_one_cell_transitive_has_kappa_1(self):
        cover = build_one_cell_transitive_cover()
        self.assertEqual(compute_kappa(cover).kappa, 1)

    def test_zero_cell_has_kappa_0(self):
        cover = build_zero_cell_cover()
        self.assertEqual(compute_kappa(cover).kappa, 0)

    def test_two_cells_are_vertex_disjoint(self):
        # The two odd cycles must share NO variable, else they are not independent.
        cover = build_two_cell_transitive_obstruction()
        cell1_vars = {v for v in cover.variables if not v.endswith("__cell2")}
        cell2_vars = {v for v in cover.variables if v.endswith("__cell2")}
        self.assertTrue(cell1_vars)
        self.assertTrue(cell2_vars)
        self.assertEqual(cell1_vars & cell2_vars, set())


class TestNativeTwoBoxWitness(unittest.TestCase):
    def test_two_boxes_frustrated_native_rank_2(self):
        native = native_two_box_obstruction(build_two_box_chsh(2))
        self.assertEqual(native["native_frustrated_box_rank"], 2)
        self.assertEqual(native["num_boxes"], 2)
        self.assertTrue(all(b["box_frustrated"] for b in native["per_box"]))
        self.assertTrue(all(b["parity_product"] == -1 for b in native["per_box"]))

    def test_one_box_frustrated_native_rank_1(self):
        native = native_two_box_obstruction(build_two_box_chsh(1))
        self.assertEqual(native["native_frustrated_box_rank"], 1)
        frustrated = [b for b in native["per_box"] if b["box_frustrated"]]
        self.assertEqual(len(frustrated), 1)

    def test_zero_boxes_frustrated_native_rank_0(self):
        native = native_two_box_obstruction(build_two_box_chsh(0))
        self.assertEqual(native["native_frustrated_box_rank"], 0)
        self.assertTrue(all(not b["box_frustrated"] for b in native["per_box"]))

    def test_native_rank_separates_presence_classifier(self):
        # The decisive distinction a binary present/absent classifier CANNOT make:
        # one-box-frustrated and two-box-frustrated are BOTH "obstructed" but have
        # native rank 1 vs 2. The native witness must separate them.
        r1 = native_two_box_obstruction(build_two_box_chsh(1))["native_frustrated_box_rank"]
        r2_ = native_two_box_obstruction(build_two_box_chsh(2))["native_frustrated_box_rank"]
        self.assertNotEqual(r1, r2_)
        self.assertEqual((r1, r2_), (1, 2))


class TestNativeWitnessIndependence(unittest.TestCase):
    def test_native_witness_does_not_call_compute_kappa(self):
        # Independence guard: the native two-box rank must be measured by T21's own
        # parity witness, NOT by the kappa machinery. If it CALLED compute_kappa the
        # two measurements would not be independent corroboration. We inspect the
        # compiled names the function actually references (co_names), not the
        # docstring -- the docstring legitimately states "does not call compute_kappa".
        referenced = set(native_two_box_obstruction.__code__.co_names)
        self.assertNotIn("compute_kappa", referenced)
        self.assertIn("analyze_chsh_finality", referenced)


class TestNuSideKappaMatchesNative(unittest.TestCase):
    def test_nu_kappa_equals_native_rank_each_rung(self):
        for n in (0, 1, 2):
            scenario = build_two_box_chsh(n)
            k_nu = compute_kappa(nu_from_chsh(scenario)).kappa
            native = native_two_box_obstruction(scenario)["native_frustrated_box_rank"]
            self.assertEqual(k_nu, n, f"nu-side kappa wrong for {n} frustrated boxes")
            self.assertEqual(native, n, f"native rank wrong for {n} frustrated boxes")
            self.assertEqual(k_nu, native)


class TestNoSharedDerivation(unittest.TestCase):
    def test_T21_and_module_do_not_import_T39_engine(self):
        audit = shared_derivation_audit_rank2()
        self.assertFalse(audit["T21_imports_d1_restriction_system"])
        self.assertFalse(audit["rank2_module_imports_d1_restriction_system"])
        self.assertFalse(audit["Bprime_shares_derivation_with_T39"])

    def test_T28_CAP_would_share_derivation(self):
        audit = shared_derivation_audit_rank2()
        self.assertTrue(audit["T28_CAP_imports_d1_restriction_system"])


class TestFullProtocol(unittest.TestCase):
    def test_verdict_pass_rank2(self):
        result = run_rank2_transport_test()
        self.assertTrue(result["all_predictions_match"])
        self.assertTrue(result["rank_load_bearing"])
        self.assertTrue(result["rank_separates_1_from_2"])
        self.assertTrue(result["no_shared_derivation"])
        self.assertTrue(result["kappa_single_formula"])
        self.assertTrue(result["second_absorber_cleared"])
        self.assertTrue(result["both_T224_conditions_cleared"])
        self.assertEqual(result["verdict"], "PASS_RANK2")
        self.assertIn("finite_witness", result["complexity_tags"])
        self.assertIn("poly_decider", result["complexity_tags"])

    def test_decisive_trial_predicts_rank_2(self):
        result = run_rank2_transport_test()
        decisive = result["trials"][0]
        self.assertEqual(decisive["a_instance"], "two_cell_transitive_kappa2")
        self.assertEqual(decisive["kappa_A"], 2)
        self.assertEqual(decisive["predicted_kappa_B"], 2)
        self.assertEqual(decisive["measured_native_B_rank"], 2)
        self.assertEqual(decisive["measured_kappa_B_via_nu"], 2)
        self.assertTrue(decisive["prediction_matches_native"])
        self.assertTrue(decisive["rank_is_load_bearing"])

    def test_off_by_one_guard_holds(self):
        # kappa_A = 1 must transport to native rank 1, NOT 2.
        result = run_rank2_transport_test()
        guard = result["trials"][1]
        self.assertEqual(guard["kappa_A"], 1)
        self.assertEqual(guard["predicted_kappa_B"], 1)
        self.assertEqual(guard["measured_native_B_rank"], 1)
        self.assertNotEqual(guard["measured_native_B_rank"], 2)

    def test_each_trial_three_way_agreement(self):
        result = run_rank2_transport_test()
        for trial in result["trials"]:
            self.assertEqual(trial["predicted_kappa_B"], trial["measured_native_B_rank"])
            self.assertEqual(trial["measured_native_B_rank"], trial["measured_kappa_B_via_nu"])
            self.assertTrue(trial["prediction_matches_native"])

    def test_module_does_not_import_d1_engine(self):
        # Hard structural guard at the module level, mirroring T224's audit.
        # The module mentions 'd1_restriction_system' only inside the audit's
        # disqualifier check (string literals); it never IMPORTS the T39 engine.
        # We parse the AST and inspect actual import statements, not raw text, so a
        # string literal naming the engine does not trip the guard.
        import ast
        tree = ast.parse(inspect.getsource(r2))
        imported_modules: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                imported_modules.add(node.module)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imported_modules.add(alias.name)
        self.assertNotIn("models.d1_restriction_system", imported_modules)
        # B' construction must come only from the T21 bell module:
        self.assertIn("models.bell_contextuality_finality", imported_modules)


if __name__ == "__main__":
    unittest.main()
