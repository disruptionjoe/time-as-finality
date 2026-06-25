"""Tests for T224: Typed-Loss Transport Test (kappa cross-domain prediction).

Real checks, not placeholders. They verify:
  1. kappa is computed by ONE formula and is correct on hand-checkable graphs.
  2. kappa_A on T39 signed-graph instances has the expected frustrated-cycle ranks.
  3. The structure-preserving A -> B map does NOT share a derivation (T21 does not
     import the T39 engine; T28/CAP would).
  4. The transported prediction matches B's native obstruction for the decisive
     trial and both controls.
  5. The verdict logic fires correctly.
"""

from __future__ import annotations

import unittest

from models.typed_loss_transport import (
    NeighborVisibleCover,
    compute_kappa,
    nu_from_binary_csp,
    nu_from_chsh,
    transport_kappa_A_to_B,
    native_B_obstruction,
    shared_derivation_audit,
    run_transport_test,
    _all_same_chsh_scenario,
)
from models.csp_satisfiability_reframing import (
    build_minimum_direct_obstruction,
    build_minimum_transitive_obstruction,
    build_tree_structured_csp,
    build_satisfiable_csp,
)
from models.bell_contextuality_finality import canonical_chsh_finality_scenario


class TestKappaFormula(unittest.TestCase):
    def test_single_odd_triangle_has_kappa_1(self):
        # A=B (same), B=C (same), A!=C (different): one frustrated 3-cycle.
        cover = NeighborVisibleCover(
            name="triangle",
            variables=("A", "B", "C"),
            signed_edges=(("A", "B", 1), ("B", "C", 1), ("A", "C", -1)),
        )
        k = compute_kappa(cover)
        self.assertEqual(k.kappa, 1)
        self.assertTrue(k.frustrated)
        self.assertFalse(k.global_section_exists)

    def test_balanced_triangle_has_kappa_0(self):
        # A=B, B=C, A=C: consistent, no frustration.
        cover = NeighborVisibleCover(
            name="balanced_triangle",
            variables=("A", "B", "C"),
            signed_edges=(("A", "B", 1), ("B", "C", 1), ("A", "C", 1)),
        )
        k = compute_kappa(cover)
        self.assertEqual(k.kappa, 0)
        self.assertTrue(k.global_section_exists)

    def test_direct_conflict_pair_has_kappa_1(self):
        # A=B and A!=B on the same pair: a frustrated 2-cycle.
        cover = NeighborVisibleCover(
            name="direct",
            variables=("A", "B"),
            signed_edges=(("A", "B", 1), ("A", "B", -1)),
        )
        k = compute_kappa(cover)
        self.assertEqual(k.kappa, 1)

    def test_tree_has_kappa_0(self):
        cover = NeighborVisibleCover(
            name="tree",
            variables=("A", "B", "C", "D"),
            signed_edges=(("A", "B", 1), ("B", "C", 1), ("B", "D", -1)),
        )
        k = compute_kappa(cover)
        self.assertEqual(k.kappa, 0)
        self.assertTrue(k.global_section_exists)

    def test_two_independent_odd_cycles_has_kappa_2(self):
        # Two disjoint frustrated triangles share no edges: kappa = 2.
        cover = NeighborVisibleCover(
            name="two_triangles",
            variables=("A", "B", "C", "D", "E", "F"),
            signed_edges=(
                ("A", "B", 1), ("B", "C", 1), ("A", "C", -1),
                ("D", "E", 1), ("E", "F", 1), ("D", "F", -1),
            ),
        )
        k = compute_kappa(cover)
        self.assertEqual(k.kappa, 2)


class TestKappaOnDomainA(unittest.TestCase):
    def test_min_transitive_kappa_1(self):
        csp, _ = build_minimum_transitive_obstruction()
        k = compute_kappa(nu_from_binary_csp(csp))
        self.assertEqual(k.kappa, 1)

    def test_min_direct_kappa_1(self):
        csp, _ = build_minimum_direct_obstruction()
        k = compute_kappa(nu_from_binary_csp(csp))
        self.assertEqual(k.kappa, 1)

    def test_tree_kappa_0(self):
        csp, _ = build_tree_structured_csp()
        k = compute_kappa(nu_from_binary_csp(csp))
        self.assertEqual(k.kappa, 0)

    def test_satisfiable_kappa_0(self):
        csp, _ = build_satisfiable_csp()
        k = compute_kappa(nu_from_binary_csp(csp))
        self.assertEqual(k.kappa, 0)


class TestNoSharedDerivation(unittest.TestCase):
    def test_T21_does_not_import_T39_engine(self):
        audit = shared_derivation_audit()
        self.assertFalse(audit["T21_imports_d1_restriction_system"])
        self.assertFalse(audit["T21_shares_derivation_with_T39"])

    def test_T28_CAP_would_share_derivation(self):
        # The disqualified alternative B IS built from the T39 engine.
        audit = shared_derivation_audit()
        self.assertTrue(audit["T28_CAP_imports_d1_restriction_system"])
        self.assertTrue(audit["T28_would_share_derivation_with_T39"])


class TestDomainBNative(unittest.TestCase):
    def test_canonical_chsh_native_rank_1(self):
        native = native_B_obstruction(canonical_chsh_finality_scenario())
        self.assertEqual(native["native_frustrated_cycle_rank"], 1)
        self.assertEqual(native["parity_product"], -1)
        self.assertTrue(native["no_global_assignment"])

    def test_noncontextual_control_native_rank_0(self):
        native = native_B_obstruction(_all_same_chsh_scenario())
        self.assertEqual(native["native_frustrated_cycle_rank"], 0)

    def test_chsh_nu_kappa_matches_native(self):
        scenario = canonical_chsh_finality_scenario()
        k_nu = compute_kappa(nu_from_chsh(scenario))
        native = native_B_obstruction(scenario)
        self.assertEqual(k_nu.kappa, native["native_frustrated_cycle_rank"])


class TestTransportPrediction(unittest.TestCase):
    def test_transported_prediction_matches_native(self):
        csp, _ = build_minimum_transitive_obstruction()
        k_A = compute_kappa(nu_from_binary_csp(csp))
        tm = transport_kappa_A_to_B(k_A, "B:canonical")
        native = native_B_obstruction(canonical_chsh_finality_scenario())
        # PREDICTION (before measuring B) == B's native obstruction rank.
        self.assertEqual(tm.predicted_target_kappa, native["native_frustrated_cycle_rank"])
        self.assertFalse(tm.shares_derivation)


class TestFullProtocol(unittest.TestCase):
    def test_all_trials_match_and_verdict(self):
        result = run_transport_test()
        self.assertTrue(result["all_predictions_match"])
        self.assertTrue(result["kappa_single_formula"])
        self.assertTrue(result["no_shared_derivation"])
        self.assertEqual(result["verdict"], "PASS")
        # Honesty caveat present: only one absorber cleared this cycle.
        self.assertFalse(result["two_absorber_confirmation"])
        self.assertIn("finite_witness", result["complexity_tags"])
        self.assertIn("poly_decider", result["complexity_tags"])

    def test_each_trial_internally_consistent(self):
        result = run_transport_test()
        for trial in result["trials"]:
            # predicted == native == nu-side, all three agree.
            self.assertEqual(trial["predicted_kappa_B"], trial["measured_native_B_rank"])
            self.assertEqual(trial["measured_native_B_rank"], trial["measured_kappa_B_via_nu"])
            self.assertTrue(trial["prediction_matches_native"])


if __name__ == "__main__":
    unittest.main()
