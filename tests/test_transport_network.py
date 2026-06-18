"""Tests for T37: typed transport network."""

import unittest

from models.transport_network import (
    NetworkAnalysis,
    T37Result,
    TypedTransportNetwork,
    _check_t34_consistency,
    _compose_morphisms,
    _path_accumulated_forgotten,
    all_paths,
    analyze_network,
    check_path_admissibility,
    diamond_network,
    run_t37_analysis,
    spectre_network,
)

_RESULT: T37Result | None = None


def _r() -> T37Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t37_analysis()
    return _RESULT


class TestNetworkConstruction(unittest.TestCase):
    def test_spectre_layer_count(self):
        net = spectre_network()
        self.assertEqual(len(net.layers), 3)

    def test_spectre_transport_count(self):
        net = spectre_network()
        self.assertEqual(len(net.transports), 2)

    def test_spectre_layer_names(self):
        net = spectre_network()
        names = {layer.name for layer in net.layers}
        self.assertEqual(names, {"SRC", "MID", "TGT"})

    def test_diamond_layer_count(self):
        net = diamond_network()
        self.assertEqual(len(net.layers), 4)

    def test_diamond_transport_count(self):
        net = diamond_network()
        self.assertEqual(len(net.transports), 4)

    def test_diamond_layer_names(self):
        net = diamond_network()
        names = {layer.name for layer in net.layers}
        self.assertEqual(names, {"SRC", "L_A", "L_B", "TGT"})

    def test_spectre_tgt_is_obstructed(self):
        net = spectre_network()
        tgt = next(layer for layer in net.layers if layer.name == "TGT")
        self.assertTrue(tgt.system.patches)

    def test_spectre_src_is_unobstructed(self):
        net = spectre_network()
        src = next(layer for layer in net.layers if layer.name == "SRC")
        self.assertFalse(src.system.patches)

    def test_spectre_mid_is_unobstructed(self):
        net = spectre_network()
        mid = next(layer for layer in net.layers if layer.name == "MID")
        self.assertFalse(mid.system.patches)

    def test_diamond_tgt_is_obstructed(self):
        net = diamond_network()
        tgt = next(layer for layer in net.layers if layer.name == "TGT")
        self.assertTrue(tgt.system.patches)

    def test_diamond_la_forgotten_is_type_guarantee(self):
        net = diamond_network()
        t = next(t for t in net.transports if t.name == "SRC_to_L_A")
        self.assertEqual(t.forgotten_structure, ("type_guarantee",))

    def test_diamond_lb_forgotten_is_empty(self):
        net = diamond_network()
        t = next(t for t in net.transports if t.name == "SRC_to_L_B")
        self.assertEqual(t.forgotten_structure, ())


class TestMorphismComposition(unittest.TestCase):
    def test_composed_morphism_source_is_first_source(self):
        net = spectre_network()
        t_sm = next(t for t in net.transports if t.name == "SRC_to_MID")
        t_mt = next(t for t in net.transports if t.name == "MID_to_TGT")
        composed = _compose_morphisms(t_sm.morphism, t_mt.morphism)
        src = next(layer for layer in net.layers if layer.name == "SRC")
        self.assertEqual(composed.source, src.system)

    def test_composed_morphism_target_is_last_target(self):
        net = spectre_network()
        t_sm = next(t for t in net.transports if t.name == "SRC_to_MID")
        t_mt = next(t for t in net.transports if t.name == "MID_to_TGT")
        composed = _compose_morphisms(t_sm.morphism, t_mt.morphism)
        tgt = next(layer for layer in net.layers if layer.name == "TGT")
        self.assertEqual(composed.target, tgt.system)

    def test_composed_preserved_dims_intersection(self):
        from models.d1_restriction_system import D1_DIMENSIONS
        net = diamond_network()
        t_sb = next(t for t in net.transports if t.name == "SRC_to_L_B")
        t_bt = next(t for t in net.transports if t.name == "L_B_to_TGT")
        composed = _compose_morphisms(t_sb.morphism, t_bt.morphism)
        # Both transports declare 3 dims (not accessible_support)
        self.assertNotIn("accessible_support", composed.preserved_dimensions)
        self.assertIn("holder_redundancy", composed.preserved_dimensions)

    def test_composed_all_dims_preserved_when_both_full(self):
        from models.d1_restriction_system import D1_DIMENSIONS
        net = spectre_network()
        t_sm = next(t for t in net.transports if t.name == "SRC_to_MID")
        t_mt = next(t for t in net.transports if t.name == "MID_to_TGT")
        composed = _compose_morphisms(t_sm.morphism, t_mt.morphism)
        self.assertEqual(set(composed.preserved_dimensions), set(D1_DIMENSIONS))

    def test_composed_site_map_has_three_entries(self):
        net = spectre_network()
        t_sm = next(t for t in net.transports if t.name == "SRC_to_MID")
        t_mt = next(t for t in net.transports if t.name == "MID_to_TGT")
        composed = _compose_morphisms(t_sm.morphism, t_mt.morphism)
        self.assertEqual(len(composed.site_map), 3)


class TestPathEnumeration(unittest.TestCase):
    def test_spectre_has_one_path_src_to_tgt(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "TGT")
        self.assertEqual(len(paths), 1)

    def test_spectre_path_layers(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "TGT")
        self.assertEqual(paths[0].layer_names, ("SRC", "MID", "TGT"))

    def test_spectre_has_one_partial_path(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "MID")
        self.assertEqual(len(paths), 1)

    def test_spectre_partial_path_layers(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "MID")
        self.assertEqual(paths[0].layer_names, ("SRC", "MID"))

    def test_diamond_has_two_paths_src_to_tgt(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        self.assertEqual(len(paths), 2)

    def test_diamond_path_layer_names_are_distinct(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        all_names = {path.layer_names for path in paths}
        self.assertIn(("SRC", "L_A", "TGT"), all_names)
        self.assertIn(("SRC", "L_B", "TGT"), all_names)

    def test_no_paths_between_unconnected_layers(self):
        net = spectre_network()
        paths = all_paths(net, "TGT", "SRC")
        self.assertEqual(len(paths), 0)


class TestForgottenAccumulation(unittest.TestCase):
    def test_spectre_full_path_forgotten(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "TGT")
        forgotten = _path_accumulated_forgotten(paths[0])
        self.assertEqual(forgotten, ("type_guarantee",))

    def test_spectre_partial_path_forgotten(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "MID")
        forgotten = _path_accumulated_forgotten(paths[0])
        self.assertEqual(forgotten, ("type_guarantee",))

    def test_diamond_la_path_forgotten(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        la_path = next(p for p in paths if "L_A" in p.layer_names)
        forgotten = _path_accumulated_forgotten(la_path)
        self.assertEqual(forgotten, ("type_guarantee",))

    def test_diamond_lb_path_forgotten(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        lb_path = next(p for p in paths if "L_B" in p.layer_names)
        forgotten = _path_accumulated_forgotten(lb_path)
        self.assertEqual(forgotten, ())


class TestSpectreAdmissibility(unittest.TestCase):
    def test_full_path_is_po1(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "TGT")
        pa = check_path_admissibility(net, paths[0])
        self.assertTrue(pa.is_po1_instance)

    def test_full_path_verdict_fully_admissible(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "TGT")
        pa = check_path_admissibility(net, paths[0])
        self.assertEqual(pa.admissibility.verdict, "fully_admissible")

    def test_partial_path_is_not_po1(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "MID")
        pa = check_path_admissibility(net, paths[0])
        self.assertFalse(pa.is_po1_instance)

    def test_partial_path_fails_ac6(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "MID")
        pa = check_path_admissibility(net, paths[0])
        self.assertIn("AC6", pa.admissibility.failed_conditions)

    def test_partial_path_verdict_no_new_obstruction(self):
        net = spectre_network()
        paths = all_paths(net, "SRC", "MID")
        pa = check_path_admissibility(net, paths[0])
        self.assertEqual(pa.admissibility.verdict, "non_admissible_no_new_obstruction")


class TestDiamondAdmissibility(unittest.TestCase):
    def test_la_path_is_po1(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        la_path = next(p for p in paths if "L_A" in p.layer_names)
        pa = check_path_admissibility(net, la_path)
        self.assertTrue(pa.is_po1_instance)

    def test_lb_path_is_not_po1(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        lb_path = next(p for p in paths if "L_B" in p.layer_names)
        pa = check_path_admissibility(net, lb_path)
        self.assertFalse(pa.is_po1_instance)

    def test_lb_path_fails_ac5(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        lb_path = next(p for p in paths if "L_B" in p.layer_names)
        pa = check_path_admissibility(net, lb_path)
        self.assertIn("AC5", pa.admissibility.failed_conditions)

    def test_lb_path_verdict_no_forgotten_structure(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        lb_path = next(p for p in paths if "L_B" in p.layer_names)
        pa = check_path_admissibility(net, lb_path)
        self.assertEqual(pa.admissibility.verdict, "non_admissible_no_forgotten_structure")

    def test_lb_path_ac1_through_ac4_and_ac6_ac7_pass(self):
        net = diamond_network()
        paths = all_paths(net, "SRC", "TGT")
        lb_path = next(p for p in paths if "L_B" in p.layer_names)
        pa = check_path_admissibility(net, lb_path)
        a = pa.admissibility
        self.assertTrue(a.ac1_richer_valid)
        self.assertTrue(a.ac2_restricted_valid)
        self.assertTrue(a.ac3_projection_definable)
        self.assertTrue(a.ac4_local_compat)
        self.assertTrue(a.ac6_restricted_obstructed)
        self.assertTrue(a.ac7_richer_unobstructed)


class TestNetworkAnalysis(unittest.TestCase):
    def test_spectre_verdict_all_paths_admissible(self):
        net = spectre_network()
        analysis = analyze_network(net, "SRC", "TGT")
        self.assertEqual(analysis.verdict, "all_paths_admissible")

    def test_spectre_not_path_dependent(self):
        net = spectre_network()
        analysis = analyze_network(net, "SRC", "TGT")
        self.assertFalse(analysis.path_dependent)

    def test_spectre_one_po1_path(self):
        net = spectre_network()
        analysis = analyze_network(net, "SRC", "TGT")
        self.assertEqual(len(analysis.po1_paths), 1)

    def test_diamond_verdict_path_dependent(self):
        net = diamond_network()
        analysis = analyze_network(net, "SRC", "TGT")
        self.assertEqual(analysis.verdict, "path_dependent_admissibility_witnessed")

    def test_diamond_is_path_dependent(self):
        net = diamond_network()
        analysis = analyze_network(net, "SRC", "TGT")
        self.assertTrue(analysis.path_dependent)

    def test_diamond_one_po1_and_one_non_po1(self):
        net = diamond_network()
        analysis = analyze_network(net, "SRC", "TGT")
        self.assertEqual(len(analysis.po1_paths), 1)
        self.assertEqual(len(analysis.non_po1_paths), 1)

    def test_diamond_witness_exists(self):
        net = diamond_network()
        analysis = analyze_network(net, "SRC", "TGT")
        self.assertIsNotNone(analysis.path_dependence_witness)

    def test_diamond_witness_source_and_target(self):
        net = diamond_network()
        analysis = analyze_network(net, "SRC", "TGT")
        w = analysis.path_dependence_witness
        self.assertEqual(w.source_name, "SRC")
        self.assertEqual(w.target_name, "TGT")

    def test_diamond_witness_po1_forgotten(self):
        net = diamond_network()
        analysis = analyze_network(net, "SRC", "TGT")
        w = analysis.path_dependence_witness
        self.assertEqual(w.po1_forgotten, ("type_guarantee",))

    def test_diamond_witness_non_po1_forgotten(self):
        net = diamond_network()
        analysis = analyze_network(net, "SRC", "TGT")
        w = analysis.path_dependence_witness
        self.assertEqual(w.non_po1_forgotten, ())

    def test_diamond_witness_failing_conditions_is_ac5(self):
        net = diamond_network()
        analysis = analyze_network(net, "SRC", "TGT")
        w = analysis.path_dependence_witness
        self.assertEqual(w.failing_conditions, ("AC5",))


class TestT34Consistency(unittest.TestCase):
    def test_t34_consistency_true(self):
        net = spectre_network()
        self.assertTrue(_check_t34_consistency(net, "SRC", "MID", "TGT"))


class TestT37Result(unittest.TestCase):
    def test_t34_consistency(self):
        self.assertTrue(_r().t34_consistency)

    def test_path_dependence_witnessed(self):
        self.assertTrue(_r().path_dependence_witnessed)

    def test_spectre_analysis_verdict(self):
        self.assertEqual(
            _r().spectre_network_analysis.verdict, "all_paths_admissible"
        )

    def test_diamond_analysis_verdict(self):
        self.assertEqual(
            _r().diamond_network_analysis.verdict,
            "path_dependent_admissibility_witnessed",
        )

    def test_theorem_mentions_path_dependent(self):
        self.assertIn("path", _r().theorem.lower())

    def test_boundary_mentions_ac5(self):
        self.assertIn("AC5", _r().boundary)

    def test_recommendation_mentions_claim(self):
        self.assertIn("Claim", _r().recommendation)


if __name__ == "__main__":
    unittest.main()
