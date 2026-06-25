import unittest

from models.s6_g9_same_final_record_pair import run_g9_same_final_record_pair


class S6G9SameFinalRecordPairTests(unittest.TestCase):
    def test_same_final_record_is_preserved(self) -> None:
        result = run_g9_same_final_record_pair()

        self.assertTrue(result["checks"]["same_associated_record"])
        self.assertEqual(
            result["phase_final"]["values"],
            result["plain_final"]["values"],
        )
        self.assertEqual(
            result["phase_final"]["final_capabilities"],
            result["plain_final"]["final_capabilities"],
        )

    def test_presheaf_capabilities_differ(self) -> None:
        result = run_g9_same_final_record_pair()

        self.assertTrue(result["checks"]["different_presheaf_capability"])
        self.assertEqual(
            result["capability_equation"]["phase_minus_plain"],
            ["phase_sensitive_branch"],
        )
        self.assertEqual(result["capability_equation"]["plain_minus_phase"], [])

    def test_eta_loss_is_case_specific(self) -> None:
        result = run_g9_same_final_record_pair()

        self.assertTrue(result["checks"]["phase_capability_lost"])
        self.assertTrue(result["checks"]["plain_case_has_no_phase_loss"])
        self.assertIn("phase_sensitive_branch", result["phase_final"]["eta_loss"])
        self.assertNotIn("phase_sensitive_branch", result["plain_final"]["eta_loss"])

    def test_non_factorization_witness_passes(self) -> None:
        result = run_g9_same_final_record_pair()

        self.assertTrue(result["all_checks_passed"])
        self.assertTrue(result["checks"]["non_factorization_witness"])
        self.assertIn("same final record", result["strongest_result"])

    def test_effect_verdict_remains_conservative(self) -> None:
        result = run_g9_same_final_record_pair()

        self.assertFalse(result["effect_verdict"]["Issue[S]"])
        self.assertTrue(result["effect_verdict"]["Project[O]"])
        self.assertTrue(result["effect_verdict"]["Finalize[R]"])
        self.assertTrue(result["effect_verdict"]["Lose[K]"])
        self.assertIn("not a new quantum separation theorem", result["guardrail"])


if __name__ == "__main__":
    unittest.main()
