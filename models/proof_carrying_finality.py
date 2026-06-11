"""Proof-carrying, coarse-grained, metastable finality laboratory.

The proof system in this module is an ideal functionality. It models
completeness, sound verification, bounded disclosure, and recursive evidence
aggregation. It is not a production zero-knowledge construction.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from hashlib import sha256
import hmac
from itertools import product
from math import log, log2
from random import Random
from statistics import mean
from typing import Iterable, Literal


Bits = tuple[int, ...]
AdversaryMode = Literal["forged", "valid_dissent"]


def hamming_distance(left: Bits, right: Bits) -> int:
    return sum(a != b for a, b in zip(left, right))


def block_majorities(microstate: Bits, block_size: int = 3) -> Bits:
    if block_size < 1 or block_size % 2 == 0:
        raise ValueError("block size must be positive and odd")
    if len(microstate) == 0 or len(microstate) % block_size:
        raise ValueError("microstate width must be a positive multiple of block size")
    threshold = block_size // 2 + 1
    return tuple(
        int(sum(microstate[start : start + block_size]) >= threshold)
        for start in range(0, len(microstate), block_size)
    )


def coarse_claim(microstate: Bits, block_size: int = 3) -> int:
    macrostate = block_majorities(microstate, block_size)
    if len(macrostate) % 2 == 0:
        raise ValueError("the number of blocks must be odd")
    return int(sum(macrostate) >= len(macrostate) // 2 + 1)


def corrupt_microstate(microstate: Bits, bit_error_rate: float, rng: Random) -> Bits:
    if not 0.0 <= bit_error_rate <= 1.0:
        raise ValueError("bit error rate must be in [0, 1]")
    return tuple(bit ^ int(rng.random() < bit_error_rate) for bit in microstate)


def opposite_claim_state(width: int = 9, claim: int = 0) -> Bits:
    if width < 1 or width % 3:
        raise ValueError("width must be a positive multiple of three")
    state = (claim,) * width
    if coarse_claim(state) != claim:
        raise AssertionError("constructed state has the wrong coarse claim")
    return state


@dataclass(frozen=True)
class ProofCertificate:
    proof_id: str
    epoch: int
    claim: int
    support_count: int
    commitment: str
    tag: str


@dataclass(frozen=True)
class _ProofWitness:
    source_ids: frozenset[str]
    claim: int
    epoch: int
    relation_valid: bool


class IdealProofSystem:
    """Trusted ideal functionality for a coarse-graining relation.

    Public certificates reveal only an epoch, a binary claim, a support count,
    and opaque commitment/proof strings. The registry represents the hidden
    witness relation that a real ZK or proof-carrying-data construction would
    need to implement cryptographically.
    """

    def __init__(self, key: bytes = b"time-as-finality-t10") -> None:
        self._key = key
        self._registry: dict[str, _ProofWitness] = {}
        self._counter = 0

    def _tag(
        self,
        proof_id: str,
        epoch: int,
        claim: int,
        support_count: int,
        commitment: str,
    ) -> str:
        payload = f"{proof_id}|{epoch}|{claim}|{support_count}|{commitment}".encode()
        return hmac.new(self._key, payload, sha256).hexdigest()

    def _register(
        self,
        witness: _ProofWitness,
        commitment_material: str,
    ) -> ProofCertificate:
        self._counter += 1
        proof_id = sha256(
            f"{self._counter}|{commitment_material}|{witness.epoch}|{witness.claim}".encode()
        ).hexdigest()
        commitment = sha256(commitment_material.encode()).hexdigest()
        self._registry[proof_id] = witness
        support_count = len(witness.source_ids)
        return ProofCertificate(
            proof_id=proof_id,
            epoch=witness.epoch,
            claim=witness.claim,
            support_count=support_count,
            commitment=commitment,
            tag=self._tag(
                proof_id,
                witness.epoch,
                witness.claim,
                support_count,
                commitment,
            ),
        )

    def issue_leaf(
        self,
        source_id: str,
        microstate: Bits,
        epoch: int,
        nonce: str,
    ) -> ProofCertificate:
        claim = coarse_claim(microstate)
        witness = _ProofWitness(
            source_ids=frozenset({source_id}),
            claim=claim,
            epoch=epoch,
            relation_valid=coarse_claim(microstate) == claim,
        )
        hidden_state = "".join(str(bit) for bit in microstate)
        return self._register(witness, f"{source_id}|{nonce}|{hidden_state}")

    def merge(
        self,
        certificates: Iterable[ProofCertificate],
        claim: int,
        epoch: int,
    ) -> ProofCertificate:
        certificates = tuple(certificates)
        if not certificates:
            raise ValueError("at least one certificate is required")
        if any(
            not self.verify(certificate)
            or certificate.claim != claim
            or certificate.epoch != epoch
            for certificate in certificates
        ):
            raise ValueError("cannot merge invalid or incompatible certificates")
        witnesses = tuple(self._registry[certificate.proof_id] for certificate in certificates)
        source_ids = frozenset().union(*(witness.source_ids for witness in witnesses))
        merged = _ProofWitness(
            source_ids=source_ids,
            claim=claim,
            epoch=epoch,
            relation_valid=all(witness.relation_valid for witness in witnesses),
        )
        material = "|".join(sorted(certificate.proof_id for certificate in certificates))
        return self._register(merged, material)

    def forge(
        self,
        source_id: str,
        claim: int,
        epoch: int,
    ) -> ProofCertificate:
        proof_id = sha256(f"forged|{source_id}|{claim}|{epoch}".encode()).hexdigest()
        commitment = sha256(f"forged-commitment|{source_id}".encode()).hexdigest()
        return ProofCertificate(
            proof_id=proof_id,
            epoch=epoch,
            claim=claim,
            support_count=1,
            commitment=commitment,
            tag="0" * 64,
        )

    def verify(self, certificate: ProofCertificate) -> bool:
        expected_tag = self._tag(
            certificate.proof_id,
            certificate.epoch,
            certificate.claim,
            certificate.support_count,
            certificate.commitment,
        )
        witness = self._registry.get(certificate.proof_id)
        return (
            hmac.compare_digest(certificate.tag, expected_tag)
            and witness is not None
            and witness.claim == certificate.claim
            and witness.epoch == certificate.epoch
            and len(witness.source_ids) == certificate.support_count
            and witness.relation_valid
        )

    def hidden_source_ids(self, certificate: ProofCertificate) -> frozenset[str]:
        if not self.verify(certificate):
            return frozenset()
        return self._registry[certificate.proof_id].source_ids


@dataclass
class Agent:
    agent_id: str
    certificate: ProofCertificate
    byzantine: bool = False
    preference: int = field(init=False)
    confidence: list[int] = field(default_factory=lambda: [0, 0])
    consecutive_claim: int | None = None
    consecutive_successes: int = 0
    decided: bool = False

    def __post_init__(self) -> None:
        self.preference = self.certificate.claim


@dataclass(frozen=True)
class SnowballParameters:
    sample_size: int = 7
    quorum: int = 5
    decision_threshold: int = 4
    max_rounds: int = 80

    def validate(self, population_size: int) -> None:
        if not 1 <= self.sample_size < population_size:
            raise ValueError("sample size must be between one and population size - 1")
        if not 1 <= self.quorum <= self.sample_size:
            raise ValueError("quorum must be in [1, sample size]")
        if self.decision_threshold < 1 or self.max_rounds < 1:
            raise ValueError("threshold and max rounds must be positive")


@dataclass(frozen=True)
class ConsensusRun:
    rounds: int
    honest_count: int
    decided_count: int
    final_preferences: tuple[int, ...]
    decision_claims: tuple[int, ...]
    consensus_claim: int | None
    messages_sampled: int
    rejected_messages: int
    mean_public_support_count: float

    @property
    def decision_fraction(self) -> float:
        return self.decided_count / self.honest_count


@dataclass(frozen=True)
class TrialOutcome:
    truth: int
    static_trace_claim: int | None
    static_truth_support_fraction: float
    verified_majority: int | None
    bayesian_map: int | None
    proof_snowball: ConsensusRun
    raw_snowball: ConsensusRun
    proofless_majority_dynamics: ConsensusRun


@dataclass(frozen=True)
class MethodSummary:
    trials: int
    accuracy: float
    false_finality_rate: float
    consensus_rate: float
    mean_decision_fraction: float
    mean_rounds: float
    mean_messages: float
    mean_rejected_messages: float
    mean_public_support_count: float


@dataclass(frozen=True)
class ExperimentSummary:
    configuration: dict[str, object]
    proof_snowball: MethodSummary
    raw_snowball: MethodSummary
    proofless_majority_dynamics: MethodSummary
    trace_persistence_consensus_rate: float
    trace_persistence_accuracy: float
    mean_static_truth_support_fraction: float
    verified_majority_accuracy: float
    bayesian_map_accuracy: float


@dataclass(frozen=True)
class CoarseGrainingSummary:
    width: int
    block_size: int
    microstate_count: int
    claim_counts: tuple[tuple[int, int], ...]
    claim_entropy_bits: float
    hidden_information_bits: float
    mean_single_bit_stability: float
    mean_reversal_radius: float
    minimum_reversal_radius: int
    maximum_reversal_radius: int


def build_population(
    proof_system: IdealProofSystem,
    global_microstate: Bits,
    population_size: int,
    bit_error_rate: float,
    adversary_fraction: float,
    adversary_mode: AdversaryMode,
    rng: Random,
    epoch: int = 0,
) -> list[Agent]:
    if population_size < 3:
        raise ValueError("population must contain at least three agents")
    if not 0.0 <= adversary_fraction < 1.0:
        raise ValueError("adversary fraction must be in [0, 1)")
    truth = coarse_claim(global_microstate)
    adversary_count = round(population_size * adversary_fraction)
    agents: list[Agent] = []
    for index in range(population_size):
        source_id = f"agent-{index}"
        if index < adversary_count:
            false_claim = 1 - truth
            if adversary_mode == "forged":
                certificate = proof_system.forge(source_id, false_claim, epoch)
            else:
                certificate = proof_system.issue_leaf(
                    source_id,
                    opposite_claim_state(len(global_microstate), false_claim),
                    epoch,
                    nonce=f"valid-dissent-{index}",
                )
            agents.append(Agent(source_id, certificate, byzantine=True))
            continue
        local_state = corrupt_microstate(global_microstate, bit_error_rate, rng)
        certificate = proof_system.issue_leaf(
            source_id,
            local_state,
            epoch,
            nonce=f"honest-{index}-{rng.getrandbits(64)}",
        )
        agents.append(Agent(source_id, certificate))
    return agents


def clone_agents(agents: Iterable[Agent]) -> list[Agent]:
    return [
        Agent(agent.agent_id, agent.certificate, byzantine=agent.byzantine)
        for agent in agents
    ]


def _consensus_result(
    agents: list[Agent],
    rounds: int,
    messages_sampled: int,
    rejected_messages: int,
) -> ConsensusRun:
    honest = [agent for agent in agents if not agent.byzantine]
    decision_claims = tuple(agent.preference for agent in honest if agent.decided)
    consensus_claim = (
        decision_claims[0]
        if len(decision_claims) == len(honest)
        and len(set(decision_claims)) == 1
        else None
    )
    return ConsensusRun(
        rounds=rounds,
        honest_count=len(honest),
        decided_count=len(decision_claims),
        final_preferences=tuple(agent.preference for agent in honest),
        decision_claims=decision_claims,
        consensus_claim=consensus_claim,
        messages_sampled=messages_sampled,
        rejected_messages=rejected_messages,
        mean_public_support_count=mean(
            agent.certificate.support_count for agent in honest
        ),
    )


def run_snowball(
    agents: list[Agent],
    proof_system: IdealProofSystem,
    parameters: SnowballParameters,
    seed: int,
    verify_proofs: bool,
) -> ConsensusRun:
    parameters.validate(len(agents))
    rng = Random(seed)
    messages_sampled = 0
    rejected_messages = 0
    rounds = 0
    for round_number in range(1, parameters.max_rounds + 1):
        rounds = round_number
        order = [agent for agent in agents if not agent.byzantine and not agent.decided]
        rng.shuffle(order)
        if not order:
            break
        for agent in order:
            peers = [peer for peer in agents if peer.agent_id != agent.agent_id]
            sampled = rng.sample(peers, parameters.sample_size)
            messages_sampled += len(sampled)
            accepted: list[Agent] = []
            for peer in sampled:
                if verify_proofs and not proof_system.verify(peer.certificate):
                    rejected_messages += 1
                    continue
                accepted.append(peer)
            counts = Counter(peer.preference for peer in accepted)
            winners = [
                claim for claim, count in counts.items() if count >= parameters.quorum
            ]
            if len(winners) != 1:
                agent.consecutive_claim = None
                agent.consecutive_successes = 0
                continue
            candidate = winners[0]
            agent.confidence[candidate] += 1
            if agent.confidence[candidate] > agent.confidence[agent.preference]:
                agent.preference = candidate
            if candidate == agent.consecutive_claim:
                agent.consecutive_successes += 1
            else:
                agent.consecutive_claim = candidate
                agent.consecutive_successes = 1
            if verify_proofs and agent.preference == candidate:
                candidate_certificates = [
                    peer.certificate
                    for peer in accepted
                    if peer.preference == candidate
                ]
                agent.certificate = proof_system.merge(
                    candidate_certificates,
                    candidate,
                    agent.certificate.epoch,
                )
            if (
                agent.consecutive_successes >= parameters.decision_threshold
                and agent.preference == candidate
            ):
                agent.decided = True
        honest = [agent for agent in agents if not agent.byzantine]
        if all(agent.decided for agent in honest):
            break
    return _consensus_result(
        agents,
        rounds,
        messages_sampled,
        rejected_messages,
    )


def run_majority_dynamics(
    agents: list[Agent],
    parameters: SnowballParameters,
    seed: int,
) -> ConsensusRun:
    """Matched local-majority process without certificates or confidence."""

    parameters.validate(len(agents))
    rng = Random(seed)
    messages_sampled = 0
    rounds = 0
    stable_rounds = 0
    previous_preferences: tuple[int, ...] | None = None
    for round_number in range(1, parameters.max_rounds + 1):
        rounds = round_number
        updates: dict[str, int] = {}
        for agent in agents:
            if agent.byzantine:
                continue
            peers = [peer for peer in agents if peer.agent_id != agent.agent_id]
            sampled = rng.sample(peers, parameters.sample_size)
            messages_sampled += len(sampled)
            counts = Counter(peer.preference for peer in sampled)
            winners = [
                claim for claim, count in counts.items() if count >= parameters.quorum
            ]
            if len(winners) == 1:
                updates[agent.agent_id] = winners[0]
        for agent in agents:
            if agent.agent_id in updates:
                agent.preference = updates[agent.agent_id]
        honest = [agent for agent in agents if not agent.byzantine]
        preferences = tuple(agent.preference for agent in honest)
        if len(set(preferences)) == 1 and preferences == previous_preferences:
            stable_rounds += 1
        else:
            stable_rounds = 0
        previous_preferences = preferences
        if stable_rounds >= parameters.decision_threshold:
            for agent in honest:
                agent.decided = True
            break
    return _consensus_result(agents, rounds, messages_sampled, 0)


def verified_leaf_claims(
    agents: Iterable[Agent],
    proof_system: IdealProofSystem,
) -> tuple[int, ...]:
    return tuple(
        agent.certificate.claim
        for agent in agents
        if proof_system.verify(agent.certificate)
        and agent.certificate.support_count == 1
    )


def majority_decision(claims: Iterable[int]) -> int | None:
    counts = Counter(claims)
    if counts[0] == counts[1]:
        return None
    return int(counts[1] > counts[0])


def bayesian_map_decision(
    claims: Iterable[int],
    claim_accuracy: float,
    prior_true: float = 0.5,
) -> int | None:
    """MAP decision for independent, equally reliable binary reports."""

    if not 0.5 < claim_accuracy < 1.0:
        raise ValueError("claim accuracy must be in (0.5, 1)")
    if not 0.0 < prior_true < 1.0:
        raise ValueError("prior must be in (0, 1)")
    log_odds = log(prior_true / (1.0 - prior_true))
    weight = log(claim_accuracy / (1.0 - claim_accuracy))
    for claim in claims:
        log_odds += weight if claim else -weight
    if abs(log_odds) < 1e-12:
        return None
    return int(log_odds > 0)


def exact_claim_accuracy(global_microstate: Bits, bit_error_rate: float) -> float:
    truth = coarse_claim(global_microstate)
    accuracy = 0.0
    width = len(global_microstate)
    for flips in product((0, 1), repeat=width):
        changed = tuple(bit ^ flip for bit, flip in zip(global_microstate, flips))
        probability = 1.0
        for flip in flips:
            probability *= bit_error_rate if flip else 1.0 - bit_error_rate
        if coarse_claim(changed) == truth:
            accuracy += probability
    return accuracy


def run_trial(
    seed: int,
    global_microstate: Bits,
    population_size: int,
    bit_error_rate: float,
    adversary_fraction: float,
    adversary_mode: AdversaryMode,
    parameters: SnowballParameters,
) -> TrialOutcome:
    proof_system = IdealProofSystem(key=f"trial-{seed}".encode())
    agents = build_population(
        proof_system,
        global_microstate,
        population_size,
        bit_error_rate,
        adversary_fraction,
        adversary_mode,
        Random(seed),
    )
    claims = verified_leaf_claims(agents, proof_system)
    claim_accuracy = exact_claim_accuracy(global_microstate, bit_error_rate)
    truth = coarse_claim(global_microstate)
    static_claim = claims[0] if claims and len(set(claims)) == 1 else None
    poll_seed = seed * 7919 + 17
    return TrialOutcome(
        truth=truth,
        static_trace_claim=static_claim,
        static_truth_support_fraction=mean(claim == truth for claim in claims),
        verified_majority=majority_decision(claims),
        bayesian_map=bayesian_map_decision(claims, claim_accuracy),
        proof_snowball=run_snowball(
            clone_agents(agents),
            proof_system,
            parameters,
            poll_seed,
            verify_proofs=True,
        ),
        raw_snowball=run_snowball(
            clone_agents(agents),
            proof_system,
            parameters,
            poll_seed,
            verify_proofs=False,
        ),
        proofless_majority_dynamics=run_majority_dynamics(
            clone_agents(agents),
            parameters,
            poll_seed,
        ),
    )


def summarize_method(
    outcomes: Iterable[TrialOutcome],
    attribute: str,
) -> MethodSummary:
    outcomes = tuple(outcomes)
    runs: tuple[ConsensusRun, ...] = tuple(
        getattr(outcome, attribute) for outcome in outcomes
    )
    truths = tuple(outcome.truth for outcome in outcomes)
    return MethodSummary(
        trials=len(outcomes),
        accuracy=mean(
            run.consensus_claim == truth
            for run, truth in zip(runs, truths)
        ),
        false_finality_rate=mean(
            run.consensus_claim is not None and run.consensus_claim != truth
            for run, truth in zip(runs, truths)
        ),
        consensus_rate=mean(run.consensus_claim is not None for run in runs),
        mean_decision_fraction=mean(run.decision_fraction for run in runs),
        mean_rounds=mean(run.rounds for run in runs),
        mean_messages=mean(run.messages_sampled for run in runs),
        mean_rejected_messages=mean(run.rejected_messages for run in runs),
        mean_public_support_count=mean(
            run.mean_public_support_count for run in runs
        ),
    )


def run_experiment(
    trials: int,
    global_microstate: Bits,
    population_size: int,
    bit_error_rate: float,
    adversary_fraction: float,
    adversary_mode: AdversaryMode,
    parameters: SnowballParameters,
    seed: int = 1,
) -> ExperimentSummary:
    outcomes = tuple(
        run_trial(
            seed + index,
            global_microstate,
            population_size,
            bit_error_rate,
            adversary_fraction,
            adversary_mode,
            parameters,
        )
        for index in range(trials)
    )
    truth = coarse_claim(global_microstate)
    return ExperimentSummary(
        configuration={
            "trials": trials,
            "global_microstate": "".join(str(bit) for bit in global_microstate),
            "truth": truth,
            "population_size": population_size,
            "bit_error_rate": bit_error_rate,
            "adversary_fraction": adversary_fraction,
            "adversary_mode": adversary_mode,
            "sample_size": parameters.sample_size,
            "quorum": parameters.quorum,
            "decision_threshold": parameters.decision_threshold,
            "max_rounds": parameters.max_rounds,
            "single_report_accuracy": exact_claim_accuracy(
                global_microstate, bit_error_rate
            ),
        },
        proof_snowball=summarize_method(outcomes, "proof_snowball"),
        raw_snowball=summarize_method(outcomes, "raw_snowball"),
        proofless_majority_dynamics=summarize_method(
            outcomes, "proofless_majority_dynamics"
        ),
        trace_persistence_consensus_rate=mean(
            outcome.static_trace_claim is not None for outcome in outcomes
        ),
        trace_persistence_accuracy=mean(
            outcome.static_trace_claim == truth for outcome in outcomes
        ),
        mean_static_truth_support_fraction=mean(
            outcome.static_truth_support_fraction for outcome in outcomes
        ),
        verified_majority_accuracy=mean(
            outcome.verified_majority == truth for outcome in outcomes
        ),
        bayesian_map_accuracy=mean(
            outcome.bayesian_map == truth for outcome in outcomes
        ),
    )


def coarse_graining_summary(width: int = 9, block_size: int = 3) -> CoarseGrainingSummary:
    states = tuple(product((0, 1), repeat=width))
    claims = tuple(coarse_claim(state, block_size) for state in states)
    counts = Counter(claims)
    probabilities = tuple(count / len(states) for count in counts.values())
    claim_entropy = -sum(p * log2(p) for p in probabilities)
    single_bit_stabilities = []
    reversal_radii = []
    for state, claim in zip(states, claims):
        neighbors = [
            state[:index] + (1 - state[index],) + state[index + 1 :]
            for index in range(width)
        ]
        single_bit_stabilities.append(
            mean(coarse_claim(neighbor, block_size) == claim for neighbor in neighbors)
        )
        reversal_radii.append(
            min(
                hamming_distance(state, candidate)
                for candidate, candidate_claim in zip(states, claims)
                if candidate_claim != claim
            )
        )
    return CoarseGrainingSummary(
        width=width,
        block_size=block_size,
        microstate_count=len(states),
        claim_counts=tuple(sorted(counts.items())),
        claim_entropy_bits=claim_entropy,
        hidden_information_bits=log2(len(states)) - claim_entropy,
        mean_single_bit_stability=mean(single_bit_stabilities),
        mean_reversal_radius=mean(reversal_radii),
        minimum_reversal_radius=min(reversal_radii),
        maximum_reversal_radius=max(reversal_radii),
    )


def adversary_sweep(
    fractions: Iterable[float],
    adversary_mode: AdversaryMode,
    trials: int = 100,
    seed: int = 1000,
) -> tuple[ExperimentSummary, ...]:
    global_microstate = (1, 1, 1, 1, 1, 0, 0, 0, 0)
    parameters = SnowballParameters()
    return tuple(
        run_experiment(
            trials=trials,
            global_microstate=global_microstate,
            population_size=21,
            bit_error_rate=0.20,
            adversary_fraction=fraction,
            adversary_mode=adversary_mode,
            parameters=parameters,
            seed=seed + index * trials,
        )
        for index, fraction in enumerate(fractions)
    )
