import unittest
from random import Random

from models.proof_carrying_finality import (
    IdealProofSystem,
    SnowballParameters,
    bayesian_map_decision,
    block_majorities,
    build_population,
    coarse_claim,
    coarse_graining_summary,
    exact_claim_accuracy,
    majority_decision,
    run_experiment,
)


class ProofCarryingFinalityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.global_state = (1, 1, 1, 1, 1, 0, 0, 0, 0)

    def test_coarse_graining_maps_many_microstates_to_one_claim(self) -> None:
        self.assertEqual(block_majorities(self.global_state), (1, 1, 0))
        self.assertEqual(coarse_claim(self.global_state), 1)
        summary = coarse_graining_summary()
        self.assertEqual(summary.microstate_count, 512)
        self.assertEqual(summary.claim_counts, ((0, 256), (1, 256)))
        self.assertAlmostEqual(summary.hidden_information_bits, 8.0)

    def test_coarse_claim_has_nontrivial_perturbation_robustness(self) -> None:
        summary = coarse_graining_summary()
        self.assertGreater(summary.mean_single_bit_stability, 0.5)
        self.assertGreater(summary.maximum_reversal_radius, 1)
        self.assertEqual(summary.minimum_reversal_radius, 1)

    def test_ideal_proof_verifies_relation_without_public_microstate(self) -> None:
        proof_system = IdealProofSystem()
        certificate = proof_system.issue_leaf(
            "source", self.global_state, epoch=0, nonce="secret"
        )
        self.assertTrue(proof_system.verify(certificate))
        self.assertFalse(hasattr(certificate, "microstate"))
        self.assertEqual(certificate.claim, coarse_claim(self.global_state))

    def test_forged_certificate_is_rejected(self) -> None:
        proof_system = IdealProofSystem()
        forged = proof_system.forge("source", claim=0, epoch=0)
        self.assertFalse(proof_system.verify(forged))

    def test_recursive_merge_counts_unique_hidden_sources(self) -> None:
        proof_system = IdealProofSystem()
        first = proof_system.issue_leaf(
            "a", self.global_state, epoch=0, nonce="a"
        )
        second = proof_system.issue_leaf(
            "b", self.global_state, epoch=0, nonce="b"
        )
        duplicate_merge = proof_system.merge((first, first), claim=1, epoch=0)
        full_merge = proof_system.merge((first, second), claim=1, epoch=0)
        self.assertEqual(duplicate_merge.support_count, 1)
        self.assertEqual(full_merge.support_count, 2)
        self.assertTrue(proof_system.verify(full_merge))

    def test_proof_does_not_reject_valid_conflicting_records(self) -> None:
        proof_system = IdealProofSystem()
        agents = build_population(
            proof_system,
            self.global_state,
            population_size=9,
            bit_error_rate=0.0,
            adversary_fraction=1 / 3,
            adversary_mode="valid_dissent",
            rng=Random(1),
        )
        dissent = [agent for agent in agents if agent.byzantine]
        self.assertTrue(all(proof_system.verify(agent.certificate) for agent in dissent))
        self.assertTrue(all(agent.certificate.claim == 0 for agent in dissent))

    def test_bayesian_map_equals_majority_for_equal_reliability(self) -> None:
        claims = (1, 1, 0, 1, 0)
        self.assertEqual(majority_decision(claims), 1)
        self.assertEqual(bayesian_map_decision(claims, 0.8), 1)

    def test_exact_report_accuracy_is_better_than_chance(self) -> None:
        accuracy = exact_claim_accuracy(self.global_state, 0.2)
        self.assertGreater(accuracy, 0.5)
        self.assertLess(accuracy, 1.0)

    def test_proofs_help_against_forgery_but_not_valid_dissent(self) -> None:
        parameters = SnowballParameters(max_rounds=60)
        forged = run_experiment(
            trials=40,
            global_microstate=self.global_state,
            population_size=21,
            bit_error_rate=0.15,
            adversary_fraction=0.33,
            adversary_mode="forged",
            parameters=parameters,
            seed=100,
        )
        valid_dissent = run_experiment(
            trials=40,
            global_microstate=self.global_state,
            population_size=21,
            bit_error_rate=0.15,
            adversary_fraction=0.33,
            adversary_mode="valid_dissent",
            parameters=parameters,
            seed=200,
        )
        self.assertGreater(
            forged.proof_snowball.accuracy,
            forged.raw_snowball.accuracy,
        )
        self.assertLessEqual(
            valid_dissent.proof_snowball.accuracy,
            forged.proof_snowball.accuracy,
        )

    def test_snowball_is_not_assumed_to_outperform_bayesian_baseline(self) -> None:
        summary = run_experiment(
            trials=50,
            global_microstate=self.global_state,
            population_size=21,
            bit_error_rate=0.2,
            adversary_fraction=0.2,
            adversary_mode="forged",
            parameters=SnowballParameters(max_rounds=60),
            seed=500,
        )
        self.assertLessEqual(
            summary.proof_snowball.accuracy,
            summary.bayesian_map_accuracy,
        )


if __name__ == "__main__":
    unittest.main()
