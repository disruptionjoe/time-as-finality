"""Tests for T535: real TAF10 packet screen."""

from __future__ import annotations

import json
import unittest

from models import t535_real_taf10_packet_screen as t535


class RealTAF10PacketScreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t535.run()
        cls.rows = {item["candidate_id"]: item for item in cls.result["classifications"]}

    def test_artifact_identity_and_t533_consumed(self) -> None:
        self.assertEqual(self.result["artifact"], t535.ARTIFACT)
        self.assertEqual(self.result["verdict"], t535.VERDICT)
        self.assertEqual(self.result["t533_criteria_source"], t535.T533_CRITERIA_SOURCE)
        self.assertEqual(
            self.result["source_floor"]["t533_absorber_floor"]["t529_current_success"],
            False,
        )

    def test_evaluates_multiple_existing_source_candidates(self) -> None:
        self.assertGreaterEqual(self.result["overall"]["candidate_count"], 2)
        self.assertIn("t407_t398_t493_t494_current_cr_family", self.rows)
        self.assertIn("t411_t412_departed_record_boundary_family", self.rows)
        self.assertIn("t520_single_use_key_copy_law_packet", self.rows)
        for row in self.rows.values():
            self.assertTrue(row["source_json_present"])

    def test_no_candidate_clears_and_missing_field_is_named(self) -> None:
        self.assertEqual(self.result["overall"]["cleared_candidate_ids"], [])
        self.assertFalse(self.result["overall"]["real_taf10_packet_in_hand"])
        self.assertFalse(self.result["overall"]["current_c_r_success"])
        missing = self.result["exact_missing_field_if_none_clears"]
        self.assertIn("full competency", missing)
        self.assertIn("resource", missing)
        self.assertIn("permission", missing)
        self.assertIn("provenance", missing)
        self.assertIn("non-task-success noncompletion witness", missing)

    def test_current_cr_family_is_review_only_not_success(self) -> None:
        row = self.rows["t407_t398_t493_t494_current_cr_family"]
        self.assertEqual(row["outcome"], "REVIEW_ONLY")
        self.assertFalse(row["full_stack_exact_match"])
        self.assertFalse(row["independent_noncompletion_witness"])
        self.assertIn("full_competency_profile", row["missing_fields"])
        self.assertIn("resource_profile", row["missing_fields"])

    def test_absorbed_real_candidates_are_falsified_for_taf10(self) -> None:
        departed = self.rows["t411_t412_departed_record_boundary_family"]
        key = self.rows["t520_single_use_key_copy_law_packet"]

        self.assertEqual(departed["outcome"], "FALSIFIED")
        self.assertIn("joint-record completion", departed["known_absorber"])
        self.assertFalse(departed["full_stack_exact_match"])
        self.assertEqual(key["outcome"], "FALSIFIED")
        self.assertIn("resource monotone", key["known_absorber"])
        self.assertFalse(key["independent_noncompletion_witness"])

    def test_quantum_and_detector_lanes_do_not_become_taf10_success(self) -> None:
        quantum = self.rows["t516_t517_t519_quantum_access_monogamy_lane"]
        detector = self.rows["t521_detector_manifest_template_lane"]

        self.assertEqual(quantum["outcome"], "NARROWED")
        self.assertEqual(detector["outcome"], "PAUSE")
        self.assertFalse(detector["data_bearing_packet"])
        self.assertIn("no data-bearing packet", detector["known_absorber"])

    def test_claim_table_and_no_movement_boundary(self) -> None:
        statuses = {item["status"] for item in self.result["claim_table"]}

        self.assertIn("COMPUTED", statuses)
        self.assertIn("ARGUED", statuses)
        self.assertTrue(self.result["overall"]["track_2_subordinate"])
        self.assertFalse(self.result["overall"]["claim_movement"])
        self.assertFalse(self.result["overall"]["canon_or_public_posture_movement"])
        self.assertFalse(self.result["overall"]["external_publication"])
        self.assertFalse(self.result["overall"]["cross_repo_truth_movement"])

    def test_json_serializable_and_forbidden_overreads_absent(self) -> None:
        dumped = json.dumps(self.result, sort_keys=True)

        self.assertIn(t535.VERDICT, dumped)
        banned = (
            "claim promotion follows",
            "C(R) success proved",
            "surplus over the full stack proved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
        )
        for term in banned:
            self.assertNotIn(term, dumped)


if __name__ == "__main__":
    unittest.main()
