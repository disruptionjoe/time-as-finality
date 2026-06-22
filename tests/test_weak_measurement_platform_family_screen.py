"""Tests for T182: weak-measurement platform-family screen."""

from __future__ import annotations

import unittest

from models.weak_measurement_platform_family_screen import (
    canonical_platform_family_cases,
    classify_platform_family,
    run_t182_analysis,
)


class WeakMeasurementPlatformFamilyScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = {
            case.family_id: case for case in canonical_platform_family_cases()
        }
        self.result = run_t182_analysis()
        self.audits = {audit.family_id: audit for audit in self.result.audits}

    def test_homodyne_trajectory_family_is_ordinary_record_baseline(self) -> None:
        audit = classify_platform_family(self.cases["murch_koolstra_homodyne_trajectory"])

        self.assertEqual(audit.classification, "null_ordinary_record_baseline")
        self.assertFalse(audit.q1c_live)

    def test_jump_reversal_family_is_same_instrument_postselected_control(self) -> None:
        audit = self.audits["minev_jump_reversal"]

        self.assertEqual(
            audit.classification, "null_same_instrument_postselected_control"
        )
        self.assertFalse(audit.q1c_live)

    def test_replacement_readout_families_need_preserved_target(self) -> None:
        photon_counter = self.audits["opremcak_photon_counter_replacement"]
        thermal = self.audits["gunyho_thermal_detector_replacement"]

        self.assertEqual(
            photon_counter.classification,
            "blocked_honest_enlargement_without_preserved_target",
        )
        self.assertEqual(
            thermal.classification,
            "blocked_honest_enlargement_without_preserved_target",
        )
        self.assertFalse(photon_counter.q1c_live)
        self.assertFalse(thermal.q1c_live)

    def test_nanocalorimetric_route_is_alternate_ordinary_record(self) -> None:
        audit = self.audits["karimi_nanocalorimetric_trajectory"]

        self.assertEqual(audit.classification, "null_alternate_ordinary_record")
        self.assertFalse(audit.q1c_live)

    def test_calorimeter_assisted_quadrature_changes_task(self) -> None:
        audit = self.audits["shojaee_calorimeter_assisted_quadrature"]

        self.assertEqual(audit.classification, "null_task_changed_non_monitored_qubit")
        self.assertFalse(audit.q1c_live)

    def test_positive_controls_for_both_live_classes_are_admitted(self) -> None:
        extra_environment = self.audits["positive_control_extra_environment"]
        enlarged = self.audits["positive_control_enlarged_instrument"]

        self.assertEqual(
            extra_environment.classification,
            "provisional_live_extra_environment_route",
        )
        self.assertTrue(extra_environment.q1c_live)
        self.assertEqual(
            enlarged.classification,
            "provisional_live_enlarged_instrument_route",
        )
        self.assertTrue(enlarged.q1c_live)

    def test_aggregate_result_keeps_named_families_out_of_live_frontier(self) -> None:
        self.assertEqual(self.result.named_platforms_screened, 6)
        self.assertEqual(self.result.named_platforms_live, 0)
        self.assertTrue(self.result.positive_controls_admitted)
        self.assertIn("executable screen", self.result.improved)


if __name__ == "__main__":
    unittest.main()
