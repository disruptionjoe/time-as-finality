"""Tests for T100: detector authority-domain lower bound."""

from __future__ import annotations

import unittest

from models.detector_authority_domain_bound import (
    enumerate_partitions,
    run_t100_analysis,
)
from models.detector_operator_handoff_audit import TABLE_OWNER_BY_DOMAIN


class DetectorAuthorityDomainBoundTests(unittest.TestCase):
    def test_partition_enumeration_covers_all_set_partitions(self) -> None:
        partitions = enumerate_partitions(tuple(TABLE_OWNER_BY_DOMAIN))
        self.assertEqual(len(partitions), 52)

    def test_minimum_admissible_authority_count_is_four(self) -> None:
        result = run_t100_analysis()

        self.assertEqual(result.minimum_admissible_authority_count, 4)
        self.assertTrue(result.no_three_domain_profile_survives)

    def test_exactly_three_minimal_four_domain_profiles_survive(self) -> None:
        result = run_t100_analysis()

        self.assertEqual(
            set(result.admissible_four_domain_profiles),
            {
                "merge_analysis_governor+instrument_operator",
                "merge_archive_custodian+instrument_operator",
                "merge_control_designer+instrument_operator",
            },
        )

    def test_five_domain_profile_also_survives(self) -> None:
        result = run_t100_analysis()
        admissible_profiles = {
            audit.profile_name
            for audit in result.audits
            if audit.admissible
        }

        self.assertIn("fully_separated_five_domain_profile", admissible_profiles)

    def test_all_inadmissible_profiles_fail_for_known_conflict_reasons(self) -> None:
        result = run_t100_analysis()
        reasons = {
            audit.reason
            for audit in result.audits
            if not audit.admissible
        }

        self.assertEqual(
            reasons,
            {
                "trust_auditor_not_independent",
                "governance_control_archive_role_merge",
            },
        )


if __name__ == "__main__":
    unittest.main()
