"""Tests for T34: Chained Projection Analysis."""

import unittest

from models.po1_chained_projection import (
    T34Result,
    run_t34_analysis,
)

_RESULT: T34Result | None = None


def _r() -> T34Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t34_analysis()
    return _RESULT


class TestT34ResultStructure(unittest.TestCase):
    def test_result_has_three_chains(self):
        r = _r()
        self.assertIsNotNone(r.spectre_chain)
        self.assertIsNotNone(r.stepwise_chain)
        self.assertIsNotNone(r.absorbed_chain)

    def test_top_level_flags_present(self):
        r = _r()
        self.assertIsInstance(r.emergent_obstruction_confirmed, bool)
        self.assertIsInstance(r.stepwise_propagation_confirmed, bool)
        self.assertIsInstance(r.absorbed_obstruction_confirmed, bool)

    def test_theorem_string_non_empty(self):
        self.assertTrue(len(_r().po1_chain_theorem) > 0)

    def test_boundary_string_non_empty(self):
        self.assertTrue(len(_r().boundary) > 0)

    def test_recommendation_string_non_empty(self):
        self.assertTrue(len(_r().recommendation) > 0)


class TestSpectreChain(unittest.TestCase):
    def _sc(self):
        return _r().spectre_chain

    def test_emergent_obstruction_confirmed(self):
        self.assertTrue(_r().emergent_obstruction_confirmed)

    def test_spectre_emergent_flag(self):
        self.assertTrue(self._sc().emergent_obstruction)

    def test_spectre_not_stepwise(self):
        self.assertFalse(self._sc().stepwise_propagation)

    def test_spectre_not_absorbed(self):
        self.assertFalse(self._sc().absorbed_obstruction)

    def test_spectre_endpoint_fully_admissible(self):
        self.assertEqual(self._sc().endpoint_verdict, "fully_admissible")

    def test_spectre_no_admissible_checkpoints(self):
        self.assertEqual(self._sc().admissible_checkpoint_pairs, ())

    def test_spectre_four_links(self):
        self.assertEqual(self._sc().step_count, 4)

    def test_spectre_five_levels(self):
        self.assertEqual(len(self._sc().chain.abstraction_levels), 5)

    def test_spectre_three_checkpoints(self):
        self.assertEqual(len(self._sc().chain.checkpoint_pairs), 3)

    def test_spectre_obstruction_first_at_microarch(self):
        self.assertEqual(self._sc().obstruction_first_appears_at, "microarchitecture")

    def test_spectre_endpoint_all_acs_true(self):
        ea = self._sc().chain.endpoint_admissibility
        for attr in ("ac1_richer_valid", "ac2_restricted_valid",
                     "ac3_projection_definable", "ac4_local_compat",
                     "ac5_structure_forgotten", "ac6_restricted_obstructed",
                     "ac7_richer_unobstructed"):
            with self.subTest(ac=attr):
                self.assertTrue(getattr(ea, attr))

    def test_spectre_checkpoint_ir_not_po1(self):
        cp = self._sc().chain.checkpoint_pairs[0]
        self.assertEqual(cp.intermediate_level, "compiler_IR")
        self.assertFalse(cp.admissibility.po1_evidence)

    def test_spectre_checkpoint_assembly_not_po1(self):
        cp = self._sc().chain.checkpoint_pairs[1]
        self.assertEqual(cp.intermediate_level, "assembly")
        self.assertFalse(cp.admissibility.po1_evidence)

    def test_spectre_checkpoint_machine_not_po1(self):
        cp = self._sc().chain.checkpoint_pairs[2]
        self.assertEqual(cp.intermediate_level, "machine_code")
        self.assertFalse(cp.admissibility.po1_evidence)

    def test_spectre_conclusion_contains_emergent(self):
        self.assertIn("EMERGENT", self._sc().chain_po1_conclusion)


class TestStepwiseChain(unittest.TestCase):
    def _sc(self):
        return _r().stepwise_chain

    def test_stepwise_propagation_confirmed(self):
        self.assertTrue(_r().stepwise_propagation_confirmed)

    def test_stepwise_flag(self):
        self.assertTrue(self._sc().stepwise_propagation)

    def test_stepwise_not_emergent(self):
        self.assertFalse(self._sc().emergent_obstruction)

    def test_stepwise_not_absorbed(self):
        self.assertFalse(self._sc().absorbed_obstruction)

    def test_stepwise_endpoint_fully_admissible(self):
        self.assertEqual(self._sc().endpoint_verdict, "fully_admissible")

    def test_stepwise_assembly_checkpoint_is_po1(self):
        self.assertIn("assembly", self._sc().admissible_checkpoint_pairs)

    def test_stepwise_ir_checkpoint_not_po1(self):
        cp = self._sc().chain.checkpoint_pairs[0]
        self.assertEqual(cp.intermediate_level, "compiler_IR")
        self.assertFalse(cp.admissibility.po1_evidence)

    def test_stepwise_three_links(self):
        self.assertEqual(self._sc().step_count, 3)

    def test_stepwise_obstruction_first_at_assembly(self):
        self.assertEqual(self._sc().obstruction_first_appears_at, "assembly")

    def test_stepwise_conclusion_contains_propagation(self):
        self.assertIn("STEPWISE PROPAGATION", self._sc().chain_po1_conclusion)


class TestAbsorbedChain(unittest.TestCase):
    def _ac(self):
        return _r().absorbed_chain

    def test_absorbed_obstruction_confirmed(self):
        self.assertTrue(_r().absorbed_obstruction_confirmed)

    def test_absorbed_flag(self):
        self.assertTrue(self._ac().absorbed_obstruction)

    def test_absorbed_not_emergent(self):
        self.assertFalse(self._ac().emergent_obstruction)

    def test_absorbed_not_stepwise(self):
        self.assertFalse(self._ac().stepwise_propagation)

    def test_absorbed_endpoint_not_po1(self):
        self.assertNotEqual(self._ac().endpoint_verdict, "fully_admissible")

    def test_absorbed_endpoint_verdict_no_new_obstruction(self):
        self.assertEqual(self._ac().endpoint_verdict, "non_admissible_no_new_obstruction")

    def test_absorbed_unoptimized_ir_checkpoint_is_po1(self):
        self.assertIn("unoptimized_IR", self._ac().admissible_checkpoint_pairs)

    def test_absorbed_optimized_ir_checkpoint_not_po1(self):
        cp = self._ac().chain.checkpoint_pairs[1]
        self.assertEqual(cp.intermediate_level, "optimized_IR")
        self.assertFalse(cp.admissibility.po1_evidence)

    def test_absorbed_three_links(self):
        self.assertEqual(self._ac().step_count, 3)

    def test_absorbed_obstruction_first_at_unoptimized_ir(self):
        self.assertEqual(self._ac().obstruction_first_appears_at, "unoptimized_IR")

    def test_absorbed_conclusion_contains_absorbed(self):
        self.assertIn("ABSORBED", self._ac().chain_po1_conclusion)


if __name__ == "__main__":
    unittest.main()
