"""Tests for T55B: Provenance-Aware Reconstruction Separation Audit."""

from __future__ import annotations

import unittest

from models.provenance_aware_reconstruction import (
    _build_scenario_a1,
    _build_scenario_a2,
    _build_scenario_b1,
    _build_scenario_b2,
    _build_wa_events,
    _compute_event_order,
    compute_accessible_records,
    compute_colimit,
    compute_observer_state,
    run_event_order_ambiguity,
    run_t54_invariance,
    run_t55b_analysis,
    run_wa_separation,
    run_wb_separation,
)


class AccessibleRecordsTests(unittest.TestCase):
    def test_a1_direct_c_sees_both_records(self) -> None:
        s = _build_scenario_a1()
        accessible = compute_accessible_records("C", s)
        self.assertEqual(accessible, frozenset({"r1_locked", "r2_locked"}))

    def test_a1_direct_a_sees_only_own(self) -> None:
        s = _build_scenario_a1()
        accessible = compute_accessible_records("A", s)
        self.assertEqual(accessible, frozenset({"r1_locked"}))

    def test_a2_transitive_c_sees_both_records(self) -> None:
        s = _build_scenario_a2()
        accessible = compute_accessible_records("C", s)
        self.assertEqual(accessible, frozenset({"r1_locked", "r2_locked"}))

    def test_a2_transitive_b_sees_both_after_step1(self) -> None:
        s = _build_scenario_a2()
        # B receives r1_locked from A at step=1 and holds r2_locked natively.
        accessible = compute_accessible_records("B", s)
        self.assertEqual(accessible, frozenset({"r1_locked", "r2_locked"}))

    def test_b1_r_sees_alpha_and_beta(self) -> None:
        s = _build_scenario_b1()
        self.assertEqual(
            compute_accessible_records("R", s),
            frozenset({"r_alpha_locked", "r_beta_locked"}),
        )

    def test_b2_r_sees_gamma_and_delta(self) -> None:
        s = _build_scenario_b2()
        self.assertEqual(
            compute_accessible_records("R", s),
            frozenset({"r_gamma_locked", "r_delta_locked"}),
        )


class ProvenancePathTests(unittest.TestCase):
    def test_wa_a1_r1_is_direct_one_hop(self) -> None:
        s = _build_scenario_a1()
        state = compute_observer_state("C", s)
        r1_paths = [p for p in state.provenance_paths if p.record == "r1_locked"]
        self.assertEqual(len(r1_paths), 1)
        self.assertEqual(r1_paths[0].path, ("A", "C"))
        self.assertFalse(r1_paths[0].is_direct_observation)

    def test_wa_a2_r1_is_two_hop(self) -> None:
        s = _build_scenario_a2()
        state = compute_observer_state("C", s)
        r1_paths = [p for p in state.provenance_paths if p.record == "r1_locked"]
        self.assertEqual(len(r1_paths), 1)
        self.assertEqual(r1_paths[0].path, ("A", "B", "C"))

    def test_wa_r2_same_path_in_both_scenarios(self) -> None:
        s1 = _build_scenario_a1()
        s2 = _build_scenario_a2()
        c1 = compute_observer_state("C", s1)
        c2 = compute_observer_state("C", s2)
        r2_path_1 = next(p.path for p in c1.provenance_paths if p.record == "r2_locked")
        r2_path_2 = next(p.path for p in c2.provenance_paths if p.record == "r2_locked")
        self.assertEqual(r2_path_1, r2_path_2)  # Both: B → C


class WASeparationTests(unittest.TestCase):
    def setUp(self) -> None:
        s1 = _build_scenario_a1()
        s2 = _build_scenario_a2()
        c1 = compute_observer_state("C", s1)
        c2 = compute_observer_state("C", s2)
        self.witness = run_wa_separation(c1, c2)

    def test_same_record_basis(self) -> None:
        self.assertTrue(self.witness.same_record_basis)

    def test_different_provenance_structure(self) -> None:
        self.assertFalse(self.witness.same_provenance_structure)

    def test_separation_confirmed_in_finding(self) -> None:
        self.assertIn("SEPARATION CONFIRMED", self.witness.finding)


class WBSeparationTests(unittest.TestCase):
    def setUp(self) -> None:
        s1 = _build_scenario_b1()
        s2 = _build_scenario_b2()
        r1 = compute_observer_state("R", s1)
        r2 = compute_observer_state("R", s2)
        self.witness = run_wb_separation(r1, r2)

    def test_different_record_bases(self) -> None:
        self.assertFalse(self.witness.same_record_basis)

    def test_topology_content_separation_in_finding(self) -> None:
        self.assertIn("TOPOLOGY-CONTENT SEPARATION", self.witness.finding)


class ColimitComparisonTests(unittest.TestCase):
    def test_a1_a2_produce_identical_colimits(self) -> None:
        s1 = _build_scenario_a1()
        s2 = _build_scenario_a2()
        c1 = compute_observer_state("C", s1)
        c2 = compute_observer_state("C", s2)
        events = _build_wa_events()
        colimit1 = compute_colimit("A1", c1.accessible_records, events)
        colimit2 = compute_colimit("A2", c2.accessible_records, events)
        self.assertEqual(colimit1.event_order, colimit2.event_order)
        self.assertEqual(colimit1.am_holds, colimit2.am_holds)

    def test_wa_events_are_concurrent(self) -> None:
        events = _build_wa_events()
        order = _compute_event_order(events)
        non_refl = {(a, b) for a, b in order if a != b}
        self.assertEqual(non_refl, set())  # e1 || e2 in the wa event structure


class EventOrderAmbiguityTests(unittest.TestCase):
    def setUp(self) -> None:
        s = _build_scenario_a1()
        self.result = run_event_order_ambiguity(s, "C")

    def test_propagation_does_not_determine_event_order(self) -> None:
        self.assertFalse(self.result.propagation_order_determines_event_order)

    def test_concurrent_and_ordered_structures_differ(self) -> None:
        nc = {(a, b) for a, b in self.result.order_concurrent if a != b}
        no = {(a, b) for a, b in self.result.order_ordered if a != b}
        self.assertNotEqual(nc, no)

    def test_concurrent_has_empty_non_refl_order(self) -> None:
        nc = {(a, b) for a, b in self.result.order_concurrent if a != b}
        self.assertEqual(nc, set())

    def test_ordered_has_e1_leq_e2(self) -> None:
        no = {(a, b) for a, b in self.result.order_ordered if a != b}
        self.assertIn(("e1", "e2"), no)


class T54InvarianceTests(unittest.TestCase):
    def setUp(self) -> None:
        s1 = _build_scenario_a1()
        s2 = _build_scenario_a2()
        c1 = compute_observer_state("C", s1)
        c2 = compute_observer_state("C", s2)
        self.result = run_t54_invariance(c1, c2)

    def test_basis_identical(self) -> None:
        self.assertTrue(self.result.basis_identical)

    def test_t54_input_identical(self) -> None:
        self.assertTrue(self.result.t54_input_identical)


class FullAnalysisTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t55b_analysis()
        self.hyps = {h.hypothesis_id: h for h in self.result.hypothesis_verdicts}

    def test_h0_refuted(self) -> None:
        self.assertEqual(self.hyps["H0"].status, "refuted")

    def test_h1_supported(self) -> None:
        self.assertEqual(self.hyps["H1"].status, "supported")

    def test_h4_supported(self) -> None:
        self.assertEqual(self.hyps["H4"].status, "supported")

    def test_recommendation_is_audit_layer(self) -> None:
        self.assertEqual(self.result.recommendation, "optional_audit_layer")

    def test_four_open_questions(self) -> None:
        self.assertEqual(len(self.result.open_questions), 4)

    def test_two_separation_witnesses(self) -> None:
        self.assertEqual(len(self.result.separation_witnesses), 2)

    def test_wa_witness_confirms_separation(self) -> None:
        wa = next(w for w in self.result.separation_witnesses if w.name == "W_A")
        self.assertTrue(wa.same_record_basis)
        self.assertFalse(wa.same_provenance_structure)


if __name__ == "__main__":
    unittest.main()
