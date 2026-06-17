import unittest

from models.consensus_record_theorem_transfer import (
    analyze_certificate_system,
    analyze_contextual_record_case,
    consensus_record_dictionary,
    contextual_record_boundary_case,
    record_majority_safety_system,
    run_t20_analysis,
    transfer_quorum_intersection_theorem,
    weak_quorum_boundary_system,
)


class ConsensusRecordTheoremTransferTests(unittest.TestCase):
    def test_dictionary_contains_required_typed_mappings(self) -> None:
        entries = consensus_record_dictionary()
        source_terms = {entry.source_term for entry in entries}

        self.assertIn("process local state", source_terms)
        self.assertIn("message or commit certificate", source_terms)
        self.assertIn("quorum intersection", source_terms)
        self.assertIn("fork or conflicting commit", source_terms)
        self.assertTrue(all(entry.caveat for entry in entries))

    def test_quorum_safety_theorem_transfers_to_record_finality(self) -> None:
        transfer = transfer_quorum_intersection_theorem()

        self.assertTrue(transfer.proof_structure_preserved)
        self.assertTrue(transfer.consensus_analysis.theorem_blocks_all_conflicts)
        self.assertTrue(transfer.record_analysis.theorem_blocks_all_conflicts)
        self.assertEqual(
            transfer.proof_steps[-1],
            "Therefore incompatible certificates cannot both be final.",
        )

    def test_record_certificates_have_d1_profiles(self) -> None:
        analysis = analyze_certificate_system(record_majority_safety_system())

        profiles = [
            certificate.d1_profile(branch_count=1).as_tuple()
            for certificate in analysis.system.certificates
        ]
        self.assertEqual(profiles, [(3, 3, 1, 3), (3, 3, 1, 3)])

    def test_weak_quorum_boundary_allows_disjoint_conflict(self) -> None:
        analysis = analyze_certificate_system(weak_quorum_boundary_system())

        self.assertFalse(analysis.quorum_intersection_assumption)
        self.assertFalse(analysis.theorem_blocks_all_conflicts)
        self.assertEqual(len(analysis.unsafe_conflicts), 1)
        self.assertEqual(analysis.unsafe_conflicts[0].intersection, frozenset())

    def test_contextual_boundary_has_local_certificates_but_no_global_section(self) -> None:
        analysis = analyze_contextual_record_case(contextual_record_boundary_case())

        self.assertTrue(analysis.local_certificates_meet_quorum)
        self.assertTrue(analysis.pairwise_relations_locally_satisfiable)
        self.assertFalse(analysis.global_section_exists)
        self.assertEqual(analysis.obstruction_kind, "local_certificates_no_global_section")

    def test_full_analysis_reports_transfer_and_guardrails(self) -> None:
        result = run_t20_analysis()

        self.assertTrue(result["verdict"]["typed_dictionary_complete"])
        self.assertTrue(result["verdict"]["quorum_safety_theorem_transfers"])
        self.assertTrue(result["verdict"]["weak_quorum_boundary_detected"])
        self.assertTrue(result["verdict"]["sheaf_style_boundary_detected"])
        self.assertTrue(result["verdict"]["physics_not_reduced_to_protocol"])
        self.assertTrue(result["verdict"]["global_section_not_proven_by_quorum_safety"])


if __name__ == "__main__":
    unittest.main()
