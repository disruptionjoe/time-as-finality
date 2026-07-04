import unittest

from models import dolev_redundancy_feasibility_gate as gate


class DolevRedundancyFeasibilityGateTests(unittest.TestCase):
    def test_vertex_connectivity_base_graphs(self):
        self.assertEqual(gate.vertex_connectivity(5, gate.line_graph(5)), 1)
        self.assertEqual(gate.vertex_connectivity(5, gate.star_graph(5)), 1)
        self.assertEqual(gate.vertex_connectivity(5, gate.cycle_graph(5)), 2)
        self.assertEqual(gate.vertex_connectivity(5, gate.complete_graph(5)), 4)

    def test_complete_bipartite_k33_has_three_connectivity(self):
        n, graph = gate.complete_bipartite_graph(3, 3)
        self.assertEqual(n, 6)
        self.assertEqual(gate.vertex_connectivity(n, graph), 3)

    def test_f_one_gate_requires_three_vertex_connectivity(self):
        result = gate.run()
        audits = result["audits"]
        self.assertTrue(audits["complete_k4_f1_minimal_pass"]["admitted"])
        self.assertTrue(audits["k33_f1_pass"]["admitted"])
        self.assertFalse(audits["cycle_k4_f1_connectivity_fail"]["admitted"])
        self.assertIn(
            "vertex_connectivity_below_2f_plus_1",
            audits["cycle_k4_f1_connectivity_fail"]["blockers"],
        )

    def test_f_two_gate_requires_node_count_and_connectivity(self):
        result = gate.run()
        audits = result["audits"]
        self.assertFalse(audits["complete_k6_f2_node_count_fail"]["admitted"])
        self.assertIn(
            "node_count_below_3f_plus_1",
            audits["complete_k6_f2_node_count_fail"]["blockers"],
        )
        self.assertFalse(audits["cycle_k7_f2_connectivity_fail"]["admitted"])
        self.assertIn(
            "vertex_connectivity_below_2f_plus_1",
            audits["cycle_k7_f2_connectivity_fail"]["blockers"],
        )
        self.assertTrue(audits["complete_k7_f2_minimal_pass"]["admitted"])

    def test_t442_graph_family_is_feasibility_not_cost(self):
        result = gate.run()
        audits = result["audits"]
        self.assertFalse(audits["t442_line_k5_f1"]["admitted"])
        self.assertFalse(audits["t442_star_k5_f1"]["admitted"])
        self.assertFalse(audits["t442_cycle_k5_f1"]["admitted"])
        self.assertTrue(audits["t442_complete_k5_f1"]["admitted"])
        self.assertTrue(all(not item["cost_claim_made"] for item in audits.values()))

    def test_zero_fault_gate_reduces_to_connectivity(self):
        result = gate.run()
        audits = result["audits"]
        self.assertTrue(audits["t442_line_k5_f0"]["admitted"])
        self.assertFalse(audits["disconnected_f0_fail"]["admitted"])

    def test_all_model_checks_pass(self):
        result = gate.run()
        self.assertEqual(
            result["overall_verdict"],
            "DOLEV_REDUNDANCY_FEASIBILITY_GATE_BUILT_NO_COST_CLAIM",
        )
        self.assertTrue(result["checks"]["all_passed"])


if __name__ == "__main__":
    unittest.main()
