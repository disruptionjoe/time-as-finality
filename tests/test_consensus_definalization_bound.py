"""Unit tests for T442 Consensus Definalization Bound.

Run:
    python -m pytest tests/test_consensus_definalization_bound.py -q
    python -m unittest tests.test_consensus_definalization_bound -v
"""

import unittest

from models import consensus_definalization_bound as m


def _audits():
    return {tid: m.audit_fixture(fx)
            for tid, fx in {f.task_id: f for f in m.build_fixtures()}.items()}


class TestInfoHelpers(unittest.TestCase):
    def test_h2_endpoints_and_peak(self):
        self.assertAlmostEqual(m.h2(0.0), 0.0)
        self.assertAlmostEqual(m.h2(1.0), 0.0)
        self.assertAlmostEqual(m.h2(0.5), 1.0)

    def test_entropy_uniform(self):
        self.assertAlmostEqual(m.entropy(m.iid_uniform(3)), 3.0)

    def test_cond_entropy_root_copy_is_k_minus_1(self):
        for k in (2, 3, 4, 5, 6):
            self.assertAlmostEqual(
                m.cond_entropy_X_given_V(m.iid_uniform(k), m.rule_root_copy),
                k - 1, places=9)


class TestT396Reproduction(unittest.TestCase):
    def setUp(self):
        self.a = _audits()

    def test_root_copy_floor_matches_t396(self):
        for k in (2, 3, 4, 5, 6):
            self.assertAlmostEqual(
                self.a[f"t396_repro_root_copy_k{k}"].single_system_floor_bits,
                k - 1, places=9)

    def test_majority_k3_joint_floor_and_reset(self):
        a = self.a["t396_repro_majority_k3"]
        self.assertAlmostEqual(a.single_system_floor_bits, 2.0, places=9)
        self.assertAlmostEqual(a.per_holder_reset_bits, 2.433834, places=5)
        self.assertGreater(a.per_holder_reset_bits, a.single_system_floor_bits)

    def test_single_error_k5_matches_t396(self):
        self.assertAlmostEqual(
            self.a["dist_single_error_k5_ring"].single_system_floor_bits,
            2.321928, places=5)

    def test_already_consensus_is_zero(self):
        self.assertEqual(
            self.a["t396_repro_already_consensus_k5"].single_system_floor_bits, 0.0)

    def test_export_escape_is_free(self):
        fixtures = {f.task_id: f for f in m.build_fixtures()}
        for tid, a in self.a.items():
            if fixtures[tid].export_available:
                self.assertEqual(a.total_definalization_floor_bits, 0.0)


class TestNewContent(unittest.TestCase):
    def setUp(self):
        self.a = _audits()

    def test_floor_irreducible_under_local_finality(self):
        a = self.a["dist_majority_k5_complete"]
        self.assertTrue(a.surcharge_visible)
        self.assertGreater(a.forced_erasure_bits, 0.0)

    def test_reversal_term_is_topological_at_fixed_k(self):
        lam = {g: self.a[f"dist_majority_k5_{g}"].edge_connectivity
               for g in ("line", "star", "ring", "complete")}
        self.assertEqual(lam["line"], 1)
        self.assertEqual(lam["star"], 1)
        self.assertEqual(lam["ring"], 2)
        self.assertEqual(lam["complete"], 4)
        self.assertNotEqual(lam["ring"], lam["line"])

    def test_total_floor_orders_by_topology(self):
        tot = {g: self.a[f"dist_majority_k5_{g}"].total_definalization_floor_bits
               for g in ("line", "star", "ring", "complete")}
        self.assertLess(tot["line"], tot["ring"])
        self.assertLess(tot["ring"], tot["complete"])

    def test_distributed_exceeds_single_system_escape(self):
        self.assertGreater(
            self.a["dist_majority_k5_complete"].total_definalization_floor_bits, 0.0)
        self.assertEqual(
            self.a["t396_repro_majority_k5"].total_definalization_floor_bits, 0.0)


class TestKillControls(unittest.TestCase):
    def setUp(self):
        self.a = _audits()

    def test_preagreed_vanishes(self):
        self.assertFalse(self.a["kill_preagreed_k5_complete"].surcharge_visible)

    def test_colocated_single_site_vanishes(self):
        self.assertFalse(self.a["kill_colocated_k1"].surcharge_visible)

    def test_not_a_kinetic_barrier_absorber(self):
        self.assertEqual(m.edge_connectivity(5, m.complete_graph(5)), 4)
        self.assertEqual(m.edge_connectivity(5, m.ring_graph(5)), 2)


class TestOverallVerdict(unittest.TestCase):
    def test_run_reports_positive_verdict_and_all_checks_pass(self):
        r = m.run()
        self.assertTrue(r["checks"]["all_passed"])
        self.assertIn("SURCHARGE_IRREDUCIBLE_UNDER_LOCAL_FINALITY", r["overall_verdict"])
        self.assertIn("NO_H7_PROMOTION", r["overall_verdict"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
