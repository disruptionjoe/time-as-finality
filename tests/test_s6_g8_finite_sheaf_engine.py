import unittest

from models.s6_g8_finite_sheaf_engine import (
    DESCENT_SUPPORT,
    FIELDS,
    FieldPolicy,
    finite_associated_record,
    finite_site,
    records_from_sbs_strength,
    run_g8_finite_sheaf_engine,
)


class S6G8FiniteSheafEngineTests(unittest.TestCase):
    def test_site_and_cover_are_declared(self) -> None:
        site = finite_site()

        self.assertEqual(site.cover, site.contexts)
        self.assertEqual(len(site.contexts), 5)
        self.assertEqual(len(site.overlaps), 10)

    def test_prethreshold_records_do_not_stabilize(self) -> None:
        site = finite_site()
        policies = tuple(FieldPolicy(field, DESCENT_SUPPORT) for field in FIELDS)
        record = finite_associated_record(site, records_from_sbs_strength(1.0), policies)

        self.assertFalse(record.stable)
        self.assertLess(record.field_support["measure_record"], DESCENT_SUPPORT)

    def test_threshold_records_stabilize_generically(self) -> None:
        site = finite_site()
        policies = tuple(FieldPolicy(field, DESCENT_SUPPORT) for field in FIELDS)
        record = finite_associated_record(site, records_from_sbs_strength(1.2), policies)

        self.assertTrue(record.stable)
        self.assertEqual(record.values["pointer"], 1)
        self.assertTrue(record.values["prep_measure"])
        self.assertTrue(record.values["measure_record"])

    def test_eta_loss_tracks_phase_sensitive_capability(self) -> None:
        result = run_g8_finite_sheaf_engine()

        self.assertTrue(result["all_checks_passed"])
        self.assertIn("phase_sensitive_branch", result["threshold"]["eta_loss"])
        self.assertNotIn(
            "phase_sensitive_branch",
            result["threshold"]["final_capabilities"],
        )

    def test_effect_verdict_remains_conservative(self) -> None:
        result = run_g8_finite_sheaf_engine()

        self.assertFalse(result["effect_verdict"]["Issue[S]"])
        self.assertTrue(result["effect_verdict"]["Project[O]"])
        self.assertTrue(result["effect_verdict"]["Finalize[R]"])
        self.assertTrue(result["effect_verdict"]["Lose[K]"])
        self.assertIn("not a general sheafification theorem", result["guardrail"])


if __name__ == "__main__":
    unittest.main()
