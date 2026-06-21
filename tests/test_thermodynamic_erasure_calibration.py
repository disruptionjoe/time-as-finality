"""Tests for T142: thermodynamic erasure calibration."""

from __future__ import annotations

import unittest
from math import log

from models.thermodynamic_erasure_calibration import (
    landauer_bound_bits,
    run_t142_analysis,
)


class ThermodynamicErasureCalibrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t142_analysis()
        self.cases = {case.case_id: case for case in self.result.t1_calibrations}

    def test_landauer_bound_is_dimensionless_beta_work(self) -> None:
        self.assertEqual(landauer_bound_bits(0), 0.0)
        self.assertAlmostEqual(landauer_bound_bits(1), log(2.0))
        self.assertAlmostEqual(landauer_bound_bits(3), 3 * log(2.0))

    def test_access_grant_is_boundary_not_thermodynamic_arrow(self) -> None:
        case = self.cases["access_grant_existing_record"]
        self.assertTrue(case.strict_forward_increase)
        self.assertEqual(case.overall_verdict, "boundary_absorbed")
        self.assertEqual(case.reverse_modes[0].mode_id, "boundary_revoke")
        self.assertEqual(case.reverse_modes[0].erased_bits, 0)

    def test_copy_cases_have_uncopy_and_blind_reset_modes(self) -> None:
        for case_id in ("copy_to_fresh_holder", "branch_spread_copy"):
            case = self.cases[case_id]
            modes = {mode.mode_id: mode for mode in case.reverse_modes}

            self.assertTrue(case.strict_forward_increase)
            self.assertEqual(case.overall_verdict, "reversible_or_landauer_absorbed")
            self.assertEqual(modes["correlated_uncopy"].erased_bits, 0)
            self.assertEqual(modes["correlated_uncopy"].beta_work_lower_bound, 0.0)
            self.assertEqual(modes["blind_reset"].erased_bits, 1)
            self.assertAlmostEqual(modes["blind_reset"].beta_work_lower_bound, log(2.0))

    def test_same_erasure_floor_can_have_different_d1_topology(self) -> None:
        same_chain = self.cases["copy_to_fresh_holder"]
        branch = self.cases["branch_spread_copy"]

        self.assertNotEqual(same_chain.d1_delta, branch.d1_delta)
        self.assertTrue(self.result.same_landauer_floor_different_d1_topology)

    def test_resource_drawdown_is_not_physical_until_unit_is_named(self) -> None:
        drawdown = self.result.resource_drawdown_calibration

        self.assertEqual(drawdown.model_id, "test_c_resource_drawdown")
        self.assertEqual(drawdown.resource_units_drawn_down, 3)
        self.assertFalse(drawdown.physical_unit_named)
        self.assertIn("free_energy", drawdown.verdict)

    def test_h7_is_not_upgraded(self) -> None:
        self.assertTrue(self.result.no_t1_strict_increase_has_independent_thermo_arrow)
        self.assertTrue(self.result.copy_reverses_have_zero_heat_uncopy_mode)
        self.assertTrue(self.result.copy_reverses_have_landauer_reset_mode)
        self.assertEqual(self.result.h7_upgrade_status, "thermodynamic_absorption_not_upgrade")
        self.assertIn("not a thermodynamic-arrow derivation", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
