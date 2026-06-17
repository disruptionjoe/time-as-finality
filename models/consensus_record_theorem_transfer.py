"""T20: consensus-record theorem transfer lab.

This lab tests a narrow version of the claim that distributed computing and
physical record formation solve the same mathematical problem. It does not
claim that physics literally runs a consensus protocol. It asks whether one
proof pattern, quorum-intersection safety, transfers from distributed
consensus notation into D1-style physical record notation without changing
its proof structure.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product


@dataclass(frozen=True)
class TypedDictionaryEntry:
    source_term: str
    source_type: str
    target_term: str
    target_type: str
    preserves: str
    caveat: str


@dataclass(frozen=True, order=True)
class FinalityProfile:
    accessible_support: int
    holder_redundancy: int
    branch_support: int
    reversal_cost: int

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (
            self.accessible_support,
            self.holder_redundancy,
            self.branch_support,
            self.reversal_cost,
        )


@dataclass(frozen=True)
class Certificate:
    value: str
    holders: frozenset[str]
    confirmation_weight: int = 1
    context: str = "global"

    def d1_profile(self, branch_count: int) -> FinalityProfile:
        support = len(self.holders)
        return FinalityProfile(
            accessible_support=support,
            holder_redundancy=support,
            branch_support=min(branch_count, support),
            reversal_cost=support * self.confirmation_weight,
        )


@dataclass(frozen=True)
class CertificateSystem:
    name: str
    interpretation: str
    holders: frozenset[str]
    quorum_threshold: int
    certificates: tuple[Certificate, ...]
    exclusive_value_pairs: tuple[tuple[str, str], ...]
    local_consistency: bool = True


@dataclass(frozen=True)
class ConflictPair:
    left: Certificate
    right: Certificate
    intersection: frozenset[str]
    blocked_by_intersection: bool


@dataclass(frozen=True)
class CertificateSystemAnalysis:
    system: CertificateSystem
    quorum_intersection_assumption: bool
    all_certificates_meet_quorum: bool
    conflict_pairs: tuple[ConflictPair, ...]
    unsafe_conflicts: tuple[ConflictPair, ...]
    theorem_blocks_all_conflicts: bool


@dataclass(frozen=True)
class TheoremTransferResult:
    source_theorem: str
    target_theorem: str
    proof_steps: tuple[str, ...]
    consensus_analysis: CertificateSystemAnalysis
    record_analysis: CertificateSystemAnalysis
    proof_structure_preserved: bool
    assumptions_preserved: tuple[str, ...]
    assumptions_not_preserved: tuple[str, ...]


@dataclass(frozen=True)
class RelationCertificate:
    left: str
    right: str
    relation: str
    holders: frozenset[str]


@dataclass(frozen=True)
class ContextualRecordCase:
    name: str
    variables: tuple[str, ...]
    holders: frozenset[str]
    quorum_threshold: int
    relation_certificates: tuple[RelationCertificate, ...]


@dataclass(frozen=True)
class ContextualRecordAnalysis:
    case: ContextualRecordCase
    local_certificates_meet_quorum: bool
    pairwise_relations_locally_satisfiable: bool
    global_section_exists: bool
    obstruction_kind: str


@dataclass(frozen=True)
class T20Result:
    dictionary: tuple[TypedDictionaryEntry, ...]
    theorem_transfer: TheoremTransferResult
    weak_quorum_boundary: CertificateSystemAnalysis
    contextual_boundary: ContextualRecordAnalysis
    verdict: dict[str, bool]


def consensus_record_dictionary() -> tuple[TypedDictionaryEntry, ...]:
    return (
        TypedDictionaryEntry(
            source_term="process local state",
            source_type="distributed computation",
            target_term="observer-local finality domain",
            target_type="physical record formation",
            preserves="bounded local view",
            caveat="physical observers are not engineered processes",
        ),
        TypedDictionaryEntry(
            source_term="message or commit certificate",
            source_type="distributed computation",
            target_term="record fragment or environmental witness",
            target_type="physical record formation",
            preserves="portable evidence for a candidate state",
            caveat="physical records need not be symbolic messages",
        ),
        TypedDictionaryEntry(
            source_term="quorum intersection",
            source_type="distributed computation",
            target_term="redundant-holder overlap",
            target_type="D1 finality",
            preserves="shared support that blocks contradictory finalization",
            caveat="holder independence must be justified physically",
        ),
        TypedDictionaryEntry(
            source_term="fork or conflicting commit",
            source_type="distributed computation",
            target_term="incompatible finality sections",
            target_type="T13 sheaf language",
            preserves="local commitments that cannot all be globalized",
            caveat="fork safety is weaker than global-section existence",
        ),
        TypedDictionaryEntry(
            source_term="safety",
            source_type="distributed computation",
            target_term="no contradictory stabilized records",
            target_type="physical record formation",
            preserves="exclusion of incompatible final facts",
            caveat="does not imply liveness or objectivity",
        ),
        TypedDictionaryEntry(
            source_term="liveness",
            source_type="distributed computation",
            target_term="record-amplification progress",
            target_type="physical record formation",
            preserves="eventual availability under bounded conditions",
            caveat="progress is not a D1 dimension",
        ),
        TypedDictionaryEntry(
            source_term="Byzantine fault or adversarial delay",
            source_type="distributed computation",
            target_term="bounded causal access or decoherence lag",
            target_type="physical record formation",
            preserves="limits on reconciliation across local views",
            caveat="physical noise is not adversarial intent",
        ),
    )


def analyze_certificate_system(system: CertificateSystem) -> CertificateSystemAnalysis:
    exclusive_pairs = {tuple(sorted(pair)) for pair in system.exclusive_value_pairs}
    conflict_pairs: list[ConflictPair] = []
    for left, right in combinations(system.certificates, 2):
        if tuple(sorted((left.value, right.value))) not in exclusive_pairs:
            continue
        intersection = left.holders & right.holders
        conflict_pairs.append(
            ConflictPair(
                left=left,
                right=right,
                intersection=intersection,
                blocked_by_intersection=bool(intersection) and system.local_consistency,
            )
        )

    all_meet_quorum = all(
        len(certificate.holders) >= system.quorum_threshold
        for certificate in system.certificates
    )
    quorum_intersection = 2 * system.quorum_threshold > len(system.holders)
    unsafe = tuple(pair for pair in conflict_pairs if not pair.blocked_by_intersection)
    theorem_blocks = (
        all_meet_quorum
        and quorum_intersection
        and system.local_consistency
        and not unsafe
    )
    return CertificateSystemAnalysis(
        system=system,
        quorum_intersection_assumption=quorum_intersection,
        all_certificates_meet_quorum=all_meet_quorum,
        conflict_pairs=tuple(conflict_pairs),
        unsafe_conflicts=unsafe,
        theorem_blocks_all_conflicts=theorem_blocks,
    )


def consensus_majority_safety_system() -> CertificateSystem:
    return CertificateSystem(
        name="consensus_majority_safety",
        interpretation="distributed_consensus",
        holders=frozenset({"n1", "n2", "n3", "n4", "n5"}),
        quorum_threshold=3,
        certificates=(
            Certificate("commit_A", frozenset({"n1", "n2", "n3"})),
            Certificate("commit_B", frozenset({"n3", "n4", "n5"})),
        ),
        exclusive_value_pairs=(("commit_A", "commit_B"),),
    )


def record_majority_safety_system() -> CertificateSystem:
    return CertificateSystem(
        name="record_majority_safety",
        interpretation="physical_record_finality",
        holders=frozenset({"e1", "e2", "e3", "e4", "e5"}),
        quorum_threshold=3,
        certificates=(
            Certificate("spin_up_record", frozenset({"e1", "e2", "e3"})),
            Certificate("spin_down_record", frozenset({"e3", "e4", "e5"})),
        ),
        exclusive_value_pairs=(("spin_up_record", "spin_down_record"),),
    )


def weak_quorum_boundary_system() -> CertificateSystem:
    return CertificateSystem(
        name="weak_quorum_boundary",
        interpretation="physical_record_finality",
        holders=frozenset({"e1", "e2", "e3", "e4"}),
        quorum_threshold=2,
        certificates=(
            Certificate("spin_up_record", frozenset({"e1", "e2"})),
            Certificate("spin_down_record", frozenset({"e3", "e4"})),
        ),
        exclusive_value_pairs=(("spin_up_record", "spin_down_record"),),
    )


def contextual_record_boundary_case() -> ContextualRecordCase:
    return ContextualRecordCase(
        name="contextual_global_section_boundary",
        variables=("A", "B", "C"),
        holders=frozenset({"e1", "e2", "e3", "e4", "e5"}),
        quorum_threshold=3,
        relation_certificates=(
            RelationCertificate("A", "B", "same", frozenset({"e1", "e2", "e3"})),
            RelationCertificate("B", "C", "same", frozenset({"e2", "e3", "e4"})),
            RelationCertificate("A", "C", "different", frozenset({"e3", "e4", "e5"})),
        ),
    )


def analyze_contextual_record_case(
    case: ContextualRecordCase,
) -> ContextualRecordAnalysis:
    all_meet_quorum = all(
        len(certificate.holders) >= case.quorum_threshold
        for certificate in case.relation_certificates
    )
    pairwise_satisfiable = all(
        _relation_is_satisfied(certificate.relation, 0, 0)
        or _relation_is_satisfied(certificate.relation, 0, 1)
        for certificate in case.relation_certificates
    )
    global_exists = _global_section_exists(case)
    obstruction_kind = (
        "local_certificates_no_global_section"
        if all_meet_quorum and pairwise_satisfiable and not global_exists
        else "no_obstruction"
    )
    return ContextualRecordAnalysis(
        case=case,
        local_certificates_meet_quorum=all_meet_quorum,
        pairwise_relations_locally_satisfiable=pairwise_satisfiable,
        global_section_exists=global_exists,
        obstruction_kind=obstruction_kind,
    )


def transfer_quorum_intersection_theorem() -> TheoremTransferResult:
    consensus = analyze_certificate_system(consensus_majority_safety_system())
    record = analyze_certificate_system(record_majority_safety_system())
    proof_steps = (
        "Every final certificate contains at least q holders.",
        "If 2q > n, any two final certificates intersect.",
        "A shared locally consistent holder cannot certify incompatible values.",
        "Therefore incompatible certificates cannot both be final.",
    )
    return TheoremTransferResult(
        source_theorem=(
            "In a quorum system with 2q > n and locally consistent processes, "
            "two conflicting commit certificates cannot both be valid."
        ),
        target_theorem=(
            "In a physical record system with redundant-holder threshold 2q > n "
            "and locally consistent record fragments, two incompatible classical "
            "records cannot both be finalized."
        ),
        proof_steps=proof_steps,
        consensus_analysis=consensus,
        record_analysis=record,
        proof_structure_preserved=(
            consensus.theorem_blocks_all_conflicts
            and record.theorem_blocks_all_conflicts
        ),
        assumptions_preserved=(
            "finite holder set",
            "certificate threshold q",
            "intersection condition 2q > n",
            "local consistency forbids double-certification",
            "incompatible values are explicitly typed",
        ),
        assumptions_not_preserved=(
            "engineered message passing",
            "intentional Byzantine behavior",
            "protocol clock or round structure",
            "proof of global section existence",
        ),
    )


def run_t20_analysis() -> dict[str, object]:
    result = run_theorem_transfer_lab()
    transfer = result.theorem_transfer
    return {
        "dictionary": [
            {
                "source_term": entry.source_term,
                "source_type": entry.source_type,
                "target_term": entry.target_term,
                "target_type": entry.target_type,
                "preserves": entry.preserves,
                "caveat": entry.caveat,
            }
            for entry in result.dictionary
        ],
        "theorem_transfer": {
            "source_theorem": transfer.source_theorem,
            "target_theorem": transfer.target_theorem,
            "proof_steps": list(transfer.proof_steps),
            "proof_structure_preserved": transfer.proof_structure_preserved,
            "assumptions_preserved": list(transfer.assumptions_preserved),
            "assumptions_not_preserved": list(transfer.assumptions_not_preserved),
            "consensus_analysis": _certificate_analysis_to_dict(
                transfer.consensus_analysis
            ),
            "record_analysis": _certificate_analysis_to_dict(
                transfer.record_analysis
            ),
        },
        "boundary_cases": {
            "weak_quorum": _certificate_analysis_to_dict(
                result.weak_quorum_boundary
            ),
            "contextual_record": _contextual_analysis_to_dict(
                result.contextual_boundary
            ),
        },
        "verdict": result.verdict,
    }


def run_theorem_transfer_lab() -> T20Result:
    transfer = transfer_quorum_intersection_theorem()
    weak_boundary = analyze_certificate_system(weak_quorum_boundary_system())
    contextual_boundary = analyze_contextual_record_case(
        contextual_record_boundary_case()
    )
    return T20Result(
        dictionary=consensus_record_dictionary(),
        theorem_transfer=transfer,
        weak_quorum_boundary=weak_boundary,
        contextual_boundary=contextual_boundary,
        verdict={
            "typed_dictionary_complete": len(consensus_record_dictionary()) >= 7,
            "quorum_safety_theorem_transfers": transfer.proof_structure_preserved,
            "weak_quorum_boundary_detected": bool(weak_boundary.unsafe_conflicts),
            "sheaf_style_boundary_detected": (
                contextual_boundary.obstruction_kind
                == "local_certificates_no_global_section"
            ),
            "physics_not_reduced_to_protocol": True,
            "global_section_not_proven_by_quorum_safety": not contextual_boundary.global_section_exists,
        },
    )


def _global_section_exists(case: ContextualRecordCase) -> bool:
    for values in product((0, 1), repeat=len(case.variables)):
        assignment = dict(zip(case.variables, values))
        if all(
            _relation_is_satisfied(
                certificate.relation,
                assignment[certificate.left],
                assignment[certificate.right],
            )
            for certificate in case.relation_certificates
        ):
            return True
    return False


def _relation_is_satisfied(relation: str, left: int, right: int) -> bool:
    if relation == "same":
        return left == right
    if relation == "different":
        return left != right
    raise ValueError(f"unknown relation: {relation}")


def _certificate_to_dict(certificate: Certificate, branch_count: int) -> dict[str, object]:
    return {
        "value": certificate.value,
        "holders": sorted(certificate.holders),
        "confirmation_weight": certificate.confirmation_weight,
        "context": certificate.context,
        "d1_profile": certificate.d1_profile(branch_count).as_tuple(),
    }


def _certificate_analysis_to_dict(
    analysis: CertificateSystemAnalysis,
) -> dict[str, object]:
    branch_count = max(1, len({certificate.context for certificate in analysis.system.certificates}))
    return {
        "system": {
            "name": analysis.system.name,
            "interpretation": analysis.system.interpretation,
            "holders": sorted(analysis.system.holders),
            "quorum_threshold": analysis.system.quorum_threshold,
            "local_consistency": analysis.system.local_consistency,
            "certificates": [
                _certificate_to_dict(certificate, branch_count)
                for certificate in analysis.system.certificates
            ],
        },
        "quorum_intersection_assumption": analysis.quorum_intersection_assumption,
        "all_certificates_meet_quorum": analysis.all_certificates_meet_quorum,
        "conflict_pairs": [
            {
                "left": pair.left.value,
                "right": pair.right.value,
                "intersection": sorted(pair.intersection),
                "blocked_by_intersection": pair.blocked_by_intersection,
            }
            for pair in analysis.conflict_pairs
        ],
        "unsafe_conflicts": [
            {
                "left": pair.left.value,
                "right": pair.right.value,
                "intersection": sorted(pair.intersection),
            }
            for pair in analysis.unsafe_conflicts
        ],
        "theorem_blocks_all_conflicts": analysis.theorem_blocks_all_conflicts,
    }


def _contextual_analysis_to_dict(
    analysis: ContextualRecordAnalysis,
) -> dict[str, object]:
    return {
        "case": {
            "name": analysis.case.name,
            "variables": list(analysis.case.variables),
            "holders": sorted(analysis.case.holders),
            "quorum_threshold": analysis.case.quorum_threshold,
            "relation_certificates": [
                {
                    "left": certificate.left,
                    "right": certificate.right,
                    "relation": certificate.relation,
                    "holders": sorted(certificate.holders),
                }
                for certificate in analysis.case.relation_certificates
            ],
        },
        "local_certificates_meet_quorum": analysis.local_certificates_meet_quorum,
        "pairwise_relations_locally_satisfiable": analysis.pairwise_relations_locally_satisfiable,
        "global_section_exists": analysis.global_section_exists,
        "obstruction_kind": analysis.obstruction_kind,
    }
