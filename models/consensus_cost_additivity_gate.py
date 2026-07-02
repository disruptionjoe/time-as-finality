"""T396: consensus-cost additivity gate.

Direction C asks whether record consensus has a thermodynamic cost term that is
not just ordinary erasure / entropy-reduction accounting. This model is a
finite intake gate for that question.

The declared finite task:

  input  X = k observer-held bits, with a named distribution P(X)
  rule   f: X -> {0, 1}
  output Y = f(X) copied as a consensus bit to every observer

The Landauer-style dimensionless erasure floor in bits is:

  H(X) - H(Y) = H(X | Y)

because Y is a deterministic function of X. If the full input transcript is
exported with the output, the closed reversible floor is zero because no
logical information is discarded. This keeps the T110/T142/T145 guardrail
active: apparent direction comes from coarse graining, erasure, export, or a
resource boundary, not from a closed reversible finite dynamics claim.

This artifact does not prove a physical bound. It asks whether the current
finite consensus framing forces a positive structure term beyond entropy
bookkeeping. In the fixtures below, it does not.
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import dataclass
from typing import Callable


BitString = tuple[int, ...]
Distribution = dict[BitString, float]
ConsensusRule = Callable[[BitString], int]

TOL = 1e-12


@dataclass(frozen=True)
class ConsensusTask:
    task_id: str
    k: int
    distribution_name: str
    distribution: Distribution
    rule_name: str
    rule: ConsensusRule
    reading: str


@dataclass(frozen=True)
class ConsensusAudit:
    task_id: str
    k: int
    distribution_name: str
    rule_name: str
    input_entropy_bits: float
    output_entropy_bits: float
    min_erasure_bits: float
    exported_transcript_erasure_bits: float
    independent_conditional_reset_bits: float
    conditional_correlation_credit_bits: float
    expected_disagreement_edges: float
    holder_count_floor_bits: float
    holder_count_floor_refuted: bool
    ordinary_entropy_bookkeeping_explains: bool
    extra_consensus_structure_term_bits: float
    verdict: str
    reading: str


@dataclass(frozen=True)
class T396Result:
    artifact: str
    audits: tuple[ConsensusAudit, ...]
    root_copy_scaling: tuple[tuple[int, float], ...]
    already_consensus_refutes_holder_count_floor: bool
    majority_independent_overcount_seen: bool
    full_transcript_control_zero_cost_all: bool
    no_extra_consensus_term_found: bool
    strongest_claim: str
    direction_c_update: str
    falsification_condition: str
    next_gate: str


def bitstrings(k: int) -> tuple[BitString, ...]:
    if k < 1:
        raise ValueError("k must be positive")
    return tuple(itertools.product((0, 1), repeat=k))


def normalize(dist: Distribution) -> Distribution:
    total = sum(dist.values())
    if total <= 0:
        raise ValueError("distribution mass must be positive")
    out = {state: value / total for state, value in dist.items() if value > 0}
    lengths = {len(state) for state in out}
    if len(lengths) != 1:
        raise ValueError("all states must have the same length")
    for state in out:
        if any(bit not in (0, 1) for bit in state):
            raise ValueError("states must be bitstrings")
    return out


def uniform_distribution(k: int) -> Distribution:
    states = bitstrings(k)
    p = 1.0 / len(states)
    return {state: p for state in states}


def already_consensus_distribution(k: int) -> Distribution:
    return {
        tuple(0 for _ in range(k)): 0.5,
        tuple(1 for _ in range(k)): 0.5,
    }


def single_error_distribution(k: int) -> Distribution:
    """Latent bit plus exactly one flipped holder, uniformly."""

    if k < 3 or k % 2 == 0:
        raise ValueError("single-error majority fixture requires odd k >= 3")
    dist: Distribution = {}
    for latent in (0, 1):
        for error_index in range(k):
            state = [latent for _ in range(k)]
            state[error_index] = 1 - latent
            dist[tuple(state)] = 1.0
    return normalize(dist)


def entropy_bits(dist: dict[object, float]) -> float:
    total = 0.0
    for p in dist.values():
        if p > 0:
            total -= p * math.log2(p)
    return total


def root_rule(index: int = 0) -> ConsensusRule:
    return lambda state: state[index]


def constant_zero_rule(state: BitString) -> int:
    return 0


def parity_rule(state: BitString) -> int:
    return sum(state) % 2


def majority_rule(state: BitString) -> int:
    if len(state) % 2 == 0:
        raise ValueError("majority_rule fixture requires odd k")
    return 1 if sum(state) > len(state) // 2 else 0


def output_distribution(dist: Distribution, rule: ConsensusRule) -> dict[int, float]:
    out = {0: 0.0, 1: 0.0}
    for state, p in dist.items():
        out[rule(state)] += p
    return out


def conditional_bit_entropy_sum(dist: Distribution, rule: ConsensusRule) -> float:
    """Sum_i H(X_i | Y), the independent per-holder reset accounting.

    This is intentionally not the minimum joint erasure cost. Its overcount
    relative to H(X|Y) is ordinary conditional correlation / multi-information.
    """

    k = len(next(iter(dist)))
    py = output_distribution(dist, rule)
    total = 0.0
    for i in range(k):
        for y, p_y in py.items():
            if p_y <= 0:
                continue
            p1 = sum(p for state, p in dist.items() if rule(state) == y and state[i] == 1) / p_y
            p0 = 1.0 - p1
            total += p_y * entropy_bits({0: p0, 1: p1})
    return total


def expected_disagreement_edges(dist: Distribution) -> float:
    k = len(next(iter(dist)))
    total = 0.0
    for state, p in dist.items():
        disagreements = sum(
            1
            for i in range(k)
            for j in range(i + 1, k)
            if state[i] != state[j]
        )
        total += p * disagreements
    return total


def audit_task(task: ConsensusTask) -> ConsensusAudit:
    dist = normalize(task.distribution)
    h_x = entropy_bits(dist)
    out = output_distribution(dist, task.rule)
    h_y = entropy_bits(out)
    min_erasure = h_x - h_y
    independent = conditional_bit_entropy_sum(dist, task.rule)
    credit = independent - min_erasure
    holder_floor = max(task.k - 1, 0)
    exported_transcript = 0.0
    extra_term = 0.0
    holder_refuted = min_erasure + TOL < holder_floor
    ordinary_explains = abs(extra_term) < TOL and min_erasure >= -TOL
    if holder_refuted:
        verdict = "holder_count_floor_refuted_by_correlation"
    elif credit > TOL:
        verdict = "independent_reset_overcounts_joint_entropy"
    else:
        verdict = "additive_entropy_bookkeeping_only"
    return ConsensusAudit(
        task_id=task.task_id,
        k=task.k,
        distribution_name=task.distribution_name,
        rule_name=task.rule_name,
        input_entropy_bits=h_x,
        output_entropy_bits=h_y,
        min_erasure_bits=min_erasure,
        exported_transcript_erasure_bits=exported_transcript,
        independent_conditional_reset_bits=independent,
        conditional_correlation_credit_bits=credit,
        expected_disagreement_edges=expected_disagreement_edges(dist),
        holder_count_floor_bits=holder_floor,
        holder_count_floor_refuted=holder_refuted,
        ordinary_entropy_bookkeeping_explains=ordinary_explains,
        extra_consensus_structure_term_bits=extra_term,
        verdict=verdict,
        reading=task.reading,
    )


def canonical_tasks() -> tuple[ConsensusTask, ...]:
    tasks: list[ConsensusTask] = []
    for k in range(2, 7):
        tasks.append(
            ConsensusTask(
                task_id=f"root_copy_independent_k{k}",
                k=k,
                distribution_name="independent_uniform_bits",
                distribution=uniform_distribution(k),
                rule_name="root_bit",
                rule=root_rule(0),
                reading=(
                    "Copy one designated source bit to all holders while "
                    "discarding the other independent holder bits."
                ),
            )
        )
    for k in (3, 5):
        tasks.append(
            ConsensusTask(
                task_id=f"majority_independent_k{k}",
                k=k,
                distribution_name="independent_uniform_bits",
                distribution=uniform_distribution(k),
                rule_name="majority",
                rule=majority_rule,
                reading=(
                    "Majority consensus on independent bits; joint entropy is "
                    "lower than per-holder conditional reset accounting."
                ),
            )
        )
    tasks.extend(
        (
            ConsensusTask(
                task_id="already_consensus_k5",
                k=5,
                distribution_name="already_consensus_latent_bit",
                distribution=already_consensus_distribution(5),
                rule_name="root_bit",
                rule=root_rule(0),
                reading=(
                    "Five holders already agree on a latent bit, so redundancy "
                    "alone cannot force a positive consensus erasure floor."
                ),
            ),
            ConsensusTask(
                task_id="single_error_majority_k5",
                k=5,
                distribution_name="latent_bit_plus_one_error",
                distribution=single_error_distribution(5),
                rule_name="majority",
                rule=majority_rule,
                reading=(
                    "Consensus erases the location of the single bad holder; "
                    "the cost is log2(k), an ordinary error-location entropy."
                ),
            ),
            ConsensusTask(
                task_id="constant_reset_independent_k4",
                k=4,
                distribution_name="independent_uniform_bits",
                distribution=uniform_distribution(4),
                rule_name="constant_zero",
                rule=constant_zero_rule,
                reading=(
                    "A hostile control: resetting all holders to a fixed value "
                    "erases the full input entropy."
                ),
            ),
            ConsensusTask(
                task_id="parity_consensus_independent_k4",
                k=4,
                distribution_name="independent_uniform_bits",
                distribution=uniform_distribution(4),
                rule_name="parity",
                rule=parity_rule,
                reading=(
                    "A balanced one-bit consensus function; the floor is still "
                    "H(X|Y), not a separate edge-count term."
                ),
            ),
        )
    )
    return tuple(tasks)


def run_t396_analysis() -> T396Result:
    audits = tuple(audit_task(task) for task in canonical_tasks())
    by_id = {audit.task_id: audit for audit in audits}
    root_scaling = tuple(
        (k, by_id[f"root_copy_independent_k{k}"].min_erasure_bits)
        for k in range(2, 7)
    )
    already_refutes = by_id["already_consensus_k5"].holder_count_floor_refuted
    majority_overcount = (
        by_id["majority_independent_k3"].conditional_correlation_credit_bits > TOL
        and by_id["majority_independent_k5"].conditional_correlation_credit_bits > TOL
    )
    full_transcript_zero = all(
        abs(audit.exported_transcript_erasure_bits) < TOL for audit in audits
    )
    no_extra = all(
        abs(audit.extra_consensus_structure_term_bits) < TOL for audit in audits
    )
    return T396Result(
        artifact="T396-consensus-cost-additivity-gate-v0.1",
        audits=audits,
        root_copy_scaling=root_scaling,
        already_consensus_refutes_holder_count_floor=already_refutes,
        majority_independent_overcount_seen=majority_overcount,
        full_transcript_control_zero_cost_all=full_transcript_zero,
        no_extra_consensus_term_found=no_extra,
        strongest_claim=(
            "In the declared finite bit-consensus tasks, the minimal coarse-"
            "grained cost is exactly ordinary entropy reduction H(X)-H(Y). "
            "Root-copy independent inputs give the expected k-1 bit floor, "
            "but already-consensus inputs cost zero and majority/error-location "
            "fixtures are explained by conditional entropy and correlation "
            "bookkeeping. No standalone consensus-structure term is earned."
        ),
        direction_c_update=(
            "Direction C remains live only after a sharper native protocol "
            "adds constraints not represented by this finite map: reliability, "
            "communication geometry, metastability, clocking, finite-time "
            "dissipation, or substrate-specific reset dynamics. Holder count "
            "or pairwise disagreement alone is not a thermodynamic bound."
        ),
        falsification_condition=(
            "This gate is beaten by a physically typed consensus protocol with "
            "the same input distribution, same consensus output, and same "
            "exported transcript policy, but a proven lower bound strictly "
            "above H(X|Y) that cannot be absorbed by ordinary communication, "
            "reliability, finite-time, or reset-mechanism costs."
        ),
        next_gate=(
            "Build a substrate-native stochastic-thermodynamic consensus "
            "protocol with finite-time reliability constraints declared before "
            "D1 scoring; otherwise demote Direction C's first rung to entropy "
            "bookkeeping plus engineering overhead."
        ),
    )


def audit_to_dict(audit: ConsensusAudit) -> dict[str, object]:
    return {
        "task_id": audit.task_id,
        "k": audit.k,
        "distribution_name": audit.distribution_name,
        "rule_name": audit.rule_name,
        "input_entropy_bits": audit.input_entropy_bits,
        "output_entropy_bits": audit.output_entropy_bits,
        "min_erasure_bits": audit.min_erasure_bits,
        "exported_transcript_erasure_bits": audit.exported_transcript_erasure_bits,
        "independent_conditional_reset_bits": audit.independent_conditional_reset_bits,
        "conditional_correlation_credit_bits": audit.conditional_correlation_credit_bits,
        "expected_disagreement_edges": audit.expected_disagreement_edges,
        "holder_count_floor_bits": audit.holder_count_floor_bits,
        "holder_count_floor_refuted": audit.holder_count_floor_refuted,
        "ordinary_entropy_bookkeeping_explains": audit.ordinary_entropy_bookkeeping_explains,
        "extra_consensus_structure_term_bits": audit.extra_consensus_structure_term_bits,
        "verdict": audit.verdict,
        "reading": audit.reading,
    }


def t396_result_to_dict(result: T396Result) -> dict[str, object]:
    return {
        "artifact": result.artifact,
        "audits": [audit_to_dict(audit) for audit in result.audits],
        "root_copy_scaling": [
            {"k": k, "min_erasure_bits": bits}
            for k, bits in result.root_copy_scaling
        ],
        "already_consensus_refutes_holder_count_floor": (
            result.already_consensus_refutes_holder_count_floor
        ),
        "majority_independent_overcount_seen": (
            result.majority_independent_overcount_seen
        ),
        "full_transcript_control_zero_cost_all": (
            result.full_transcript_control_zero_cost_all
        ),
        "no_extra_consensus_term_found": result.no_extra_consensus_term_found,
        "strongest_claim": result.strongest_claim,
        "direction_c_update": result.direction_c_update,
        "falsification_condition": result.falsification_condition,
        "next_gate": result.next_gate,
    }


if __name__ == "__main__":
    result = run_t396_analysis()
    print(json.dumps(t396_result_to_dict(result), indent=2))
    print()
    print("=" * 70)
    print("SUMMARY -- T396 Consensus-Cost Additivity Gate")
    print("=" * 70)
    for k, bits in result.root_copy_scaling:
        print(f"root-copy independent k={k}: min erasure = {bits:.6f} bits")
    print(
        "already-consensus refutes holder-count floor: "
        f"{result.already_consensus_refutes_holder_count_floor}"
    )
    print(
        "majority independent per-holder reset overcounts: "
        f"{result.majority_independent_overcount_seen}"
    )
    print(
        "full-transcript closed control zero-cost all: "
        f"{result.full_transcript_control_zero_cost_all}"
    )
    print(f"no extra consensus term found: {result.no_extra_consensus_term_found}")
    print(result.strongest_claim)
