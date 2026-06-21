"""T117: Accessible State Space separation and absorption audit.

ASP is tested as a finite observer/task-indexed future opportunity set.  The
model deliberately matches ordinary entropy, information, finality, viability,
and persistence metrics, then checks whether admissible future operations still
split.  It also records the strongest absorption route for each domain.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Capture(Enum):
    MISSES_COARSE = "misses_coarse"
    CAPTURES_IF_ENRICHED = "captures_if_enriched"
    CAPTURES_DIRECTLY = "captures_directly"
    PARTIAL = "partial"


@dataclass(frozen=True)
class MatchedMetrics:
    entropy_bits: int
    information_bits: int
    finality_score: int
    viability_score: int
    persistence_horizon: int
    coarse_reachable_count: int
    coarse_control_rank: int


@dataclass(frozen=True)
class TaskRequirement:
    name: str
    required_witnesses: frozenset[str]
    required_rights: frozenset[str]
    required_maintenance: int
    required_reconstruction_paths: int
    required_certifications: frozenset[str]


@dataclass(frozen=True)
class ASPProfile:
    witnesses: frozenset[str]
    rights: frozenset[str]
    maintenance_budget: int
    reconstruction_paths: int
    certifications: frozenset[str]


@dataclass(frozen=True)
class ASPSystem:
    system_id: str
    domain: str
    description: str
    metrics: MatchedMetrics
    profile: ASPProfile
    task_universe: tuple[TaskRequirement, ...]


@dataclass(frozen=True)
class PriorArtExplanation:
    target: str
    capture: Capture
    explanation: str


@dataclass(frozen=True)
class DomainAudit:
    domain: str
    system_a: ASPSystem
    system_b: ASPSystem
    entropy_equal: bool
    information_equal: bool
    finality_equal: bool
    viability_equal: bool
    persistence_equal: bool
    coarse_reachability_equal: bool
    asp_a: frozenset[str]
    asp_b: frozenset[str]
    asp_split: bool
    lost_structure_chain_present: bool
    prior_art: tuple[PriorArtExplanation, ...]
    separation_verdict: str


@dataclass(frozen=True)
class T117Result:
    audits: tuple[DomainAudit, ...]
    strongest_separation_case: str
    strongest_absorption_case: str
    recommended_disposition: str
    current_strongest_claim: str
    falsification_result: str
    missing_object: str
    claim_ledger_update: str


def canonical_task_universe(domain: str) -> tuple[TaskRequirement, ...]:
    common = {
        "version_control": (
            ("build", {"tree"}, {"read"}, 1, 0, set()),
            ("merge", {"tree", "merge_base"}, {"write", "merge"}, 2, 1, {"signed_history"}),
            ("revert", {"tree", "branch_history"}, {"write", "revert"}, 2, 1, {"signed_history"}),
            ("bisect", {"tree", "branch_history"}, {"read", "bisect"}, 1, 1, set()),
        ),
        "provenance": (
            ("use", {"data"}, {"read"}, 1, 0, set()),
            ("attribute", {"data", "source_witness"}, {"attribute"}, 1, 1, {"signature"}),
            ("certify", {"data", "source_witness", "custody_log"}, {"certify"}, 2, 1, {"signature"}),
            ("repair_lineage", {"custody_log"}, {"repair"}, 2, 1, {"signature"}),
        ),
        "governance": (
            ("read_archive", {"archive"}, {"read"}, 1, 0, set()),
            ("challenge", {"archive", "rulebook"}, {"challenge"}, 1, 1, {"quorum"}),
            ("appeal", {"archive", "appeal_log"}, {"appeal"}, 2, 1, {"quorum"}),
            ("repair_rule", {"rulebook", "audit_log"}, {"repair"}, 2, 1, {"quorum"}),
        ),
        "commons": (
            ("consume", {"resource_state"}, {"use"}, 1, 0, set()),
            ("audit", {"resource_state", "audit_log"}, {"audit"}, 1, 1, {"public_rule"}),
            ("sanction", {"audit_log"}, {"sanction"}, 2, 1, {"public_rule"}),
            ("repair", {"resource_state", "repair_log"}, {"repair"}, 2, 1, {"public_rule"}),
        ),
        "consensus": (
            ("accept", {"checkpoint"}, {"accept"}, 1, 0, set()),
            ("challenge", {"checkpoint", "validator_signatures"}, {"challenge"}, 1, 1, {"challenge_window"}),
            ("slash", {"validator_signatures", "slashing_log"}, {"slash"}, 2, 1, {"challenge_window"}),
            ("rollback", {"checkpoint", "fraud_proof"}, {"rollback"}, 3, 1, {"challenge_window"}),
        ),
        "record_system": (
            ("read", {"record"}, {"read"}, 1, 0, set()),
            ("reconstruct", {"record", "index", "schema"}, {"reconstruct"}, 2, 1, {"schema_version"}),
            ("certify", {"record", "audit_log"}, {"certify"}, 2, 1, {"schema_version"}),
            ("repair", {"record", "checksum"}, {"repair"}, 2, 1, set()),
        ),
    }[domain]
    return tuple(
        TaskRequirement(
            name=name,
            required_witnesses=frozenset(witnesses),
            required_rights=frozenset(rights),
            required_maintenance=maintenance,
            required_reconstruction_paths=reconstruction,
            required_certifications=frozenset(certifications),
        )
        for name, witnesses, rights, maintenance, reconstruction, certifications in common
    )


def canonical_pairs() -> tuple[tuple[ASPSystem, ASPSystem], ...]:
    base = MatchedMetrics(
        entropy_bits=8,
        information_bits=8,
        finality_score=4,
        viability_score=4,
        persistence_horizon=10,
        coarse_reachable_count=4,
        coarse_control_rank=3,
    )
    return tuple(
        _pair_for_domain(domain, base)
        for domain in (
            "version_control",
            "provenance",
            "governance",
            "commons",
            "consensus",
            "record_system",
        )
    )


def accessible_tasks(system: ASPSystem) -> frozenset[str]:
    return frozenset(
        task.name
        for task in system.task_universe
        if task.required_witnesses <= system.profile.witnesses
        and task.required_rights <= system.profile.rights
        and task.required_maintenance <= system.profile.maintenance_budget
        and task.required_reconstruction_paths <= system.profile.reconstruction_paths
        and task.required_certifications <= system.profile.certifications
    )


def audit_domain(system_a: ASPSystem, system_b: ASPSystem) -> DomainAudit:
    asp_a = accessible_tasks(system_a)
    asp_b = accessible_tasks(system_b)
    metrics = system_a.metrics
    prior_art = prior_art_explanations(system_a.domain)
    return DomainAudit(
        domain=system_a.domain,
        system_a=system_a,
        system_b=system_b,
        entropy_equal=metrics.entropy_bits == system_b.metrics.entropy_bits,
        information_equal=metrics.information_bits == system_b.metrics.information_bits,
        finality_equal=metrics.finality_score == system_b.metrics.finality_score,
        viability_equal=metrics.viability_score == system_b.metrics.viability_score,
        persistence_equal=metrics.persistence_horizon == system_b.metrics.persistence_horizon,
        coarse_reachability_equal=(
            metrics.coarse_reachable_count == system_b.metrics.coarse_reachable_count
            and metrics.coarse_control_rank == system_b.metrics.coarse_control_rank
        ),
        asp_a=asp_a,
        asp_b=asp_b,
        asp_split=asp_a != asp_b,
        lost_structure_chain_present=_lost_structure_chain(system_a, system_b),
        prior_art=prior_art,
        separation_verdict=_separation_verdict(system_a.domain),
    )


def run_t117_analysis() -> T117Result:
    audits = tuple(audit_domain(a, b) for a, b in canonical_pairs())
    if not all(
        audit.entropy_equal
        and audit.information_equal
        and audit.finality_equal
        and audit.viability_equal
        and audit.persistence_equal
        and audit.coarse_reachability_equal
        for audit in audits
    ):
        raise AssertionError("canonical ASP pairs must match baseline metrics")
    if not all(audit.asp_split for audit in audits):
        raise AssertionError("canonical ASP pairs must split on accessible tasks")
    return T117Result(
        audits=audits,
        strongest_separation_case=(
            "Version control is the strongest finite separation: same endpoint "
            "repository state, entropy, information, finality, viability, "
            "persistence, and coarse reachable count, but branch history and "
            "merge-base witnesses change the accessible future task set from "
            "{build} to {build, merge, revert, bisect}."
        ),
        strongest_absorption_case=(
            "Reachable-state analysis or opportunity-set economics absorbs ASP "
            "once the state includes witness availability, rights, certifications, "
            "maintenance budgets, and reconstruction paths. Under that enriched "
            "state, ASP is the feasible action/opportunity set, not a new "
            "primitive."
        ),
        recommended_disposition=(
            "Preserve and formalize only as an observer/task-indexed set-valued "
            "audit object. Do not promote ASP as independent physics. Reject any "
            "scalar or global 'future opportunity' reading."
        ),
        current_strongest_claim=(
            "ASP separates finite systems that coarse entropy, information, "
            "finality, viability, persistence, and coarse reachability classify "
            "identically, but only by adding task requirements, witnesses, rights, "
            "certifications, and reconstruction paths."
        ),
        falsification_result=(
            "ASP is not killed by coarse metrics, but it is mostly absorbed by "
            "enriched reachability, controllability, opportunity-set economics, "
            "commons governance, provenance, and reconstruction-debt formalisms."
        ),
        missing_object=(
            "A prespecified observer-task admissibility structure: task universe, "
            "witness requirements, operation rights, certification tokens, "
            "maintenance budget, reconstruction paths, horizon, and observer "
            "access. Without these, ASP is post hoc."
        ),
        claim_ledger_update=(
            "No core claim upgrade. T117 preserves ASP only as a set-valued "
            "observer/task-indexed audit object. It separates from coarse "
            "entropy/information/finality/viability metrics, but collapses into "
            "enriched reachable-state/opportunity/provenance analysis when those "
            "frameworks include witnesses and operation rights."
        ),
    )


def t117_result_to_dict(result: T117Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "strongest_separation_case": result.strongest_separation_case,
        "strongest_absorption_case": result.strongest_absorption_case,
        "recommended_disposition": result.recommended_disposition,
        "current_strongest_claim": result.current_strongest_claim,
        "falsification_result": result.falsification_result,
        "missing_object": result.missing_object,
        "claim_ledger_update": result.claim_ledger_update,
    }


def prior_art_explanations(domain: str) -> tuple[PriorArtExplanation, ...]:
    return (
        PriorArtExplanation(
            "viability kernels",
            Capture.CAPTURES_IF_ENRICHED,
            "Coarse viability is matched; viability theory absorbs ASP if the viability set is future-task availability.",
        ),
        PriorArtExplanation(
            "reachable-state analysis",
            Capture.CAPTURES_IF_ENRICHED,
            "Coarse reachable count is matched; enriched reachable sets over rights and witnesses are essentially ASP.",
        ),
        PriorArtExplanation(
            "control-theoretic controllability",
            Capture.CAPTURES_IF_ENRICHED,
            "Coarse control rank is matched; controllability over certified operation states captures the split.",
        ),
        PriorArtExplanation(
            "active inference",
            Capture.CAPTURES_IF_ENRICHED,
            "Policies over future usable states absorb ASP when witnesses and rights are part of the generative state.",
        ),
        PriorArtExplanation(
            "free-energy approaches",
            Capture.PARTIAL,
            "Free-energy style maintenance can absorb expected opportunity preservation, but coarse free-energy does not encode legal/admissible rights.",
        ),
        PriorArtExplanation(
            "opportunity-set economics",
            Capture.CAPTURES_DIRECTLY,
            "ASP is very close to a feasible opportunity set under constraints and rights.",
        ),
        PriorArtExplanation(
            "ecological resilience",
            Capture.PARTIAL,
            "Resilience captures persistence of function if function is defined as future task availability.",
        ),
        PriorArtExplanation(
            "adaptive-cycle models",
            Capture.PARTIAL,
            "Adaptive-cycle language can describe changing opportunity sets, but does not by itself encode witness admissibility.",
        ),
        PriorArtExplanation(
            "commons governance",
            Capture.CAPTURES_IF_ENRICHED if domain in {"commons", "governance", "consensus"} else Capture.PARTIAL,
            "Monitoring, sanctioning, repair, authority, and challenge rights absorb shared-resource ASP cases.",
        ),
        PriorArtExplanation(
            "niche construction",
            Capture.PARTIAL,
            "Niche construction captures modified future option spaces for lineages, but not all record-witness cases.",
        ),
        PriorArtExplanation(
            "mechanism design",
            Capture.CAPTURES_IF_ENRICHED,
            "Rights, incentives, challenge rules, and admissible moves are mechanism-design variables.",
        ),
    )


def _pair_for_domain(domain: str, metrics: MatchedMetrics) -> tuple[ASPSystem, ASPSystem]:
    tasks = canonical_task_universe(domain)
    rich, poor, rich_description, poor_description = {
        "version_control": (
            ASPProfile(
                witnesses=frozenset({"tree", "merge_base", "branch_history"}),
                rights=frozenset({"read", "write", "merge", "revert", "bisect"}),
                maintenance_budget=2,
                reconstruction_paths=2,
                certifications=frozenset({"signed_history"}),
            ),
            ASPProfile(
                witnesses=frozenset({"tree"}),
                rights=frozenset({"read", "write"}),
                maintenance_budget=2,
                reconstruction_paths=0,
                certifications=frozenset({"snapshot_hash"}),
            ),
            "Same endpoint repo with retained history and merge witnesses.",
            "Same endpoint repo as squashed snapshot without future merge witnesses.",
        ),
        "provenance": (
            ASPProfile(
                witnesses=frozenset({"data", "source_witness", "custody_log"}),
                rights=frozenset({"read", "attribute", "certify", "repair"}),
                maintenance_budget=2,
                reconstruction_paths=1,
                certifications=frozenset({"signature"}),
            ),
            ASPProfile(
                witnesses=frozenset({"data"}),
                rights=frozenset({"read"}),
                maintenance_budget=2,
                reconstruction_paths=0,
                certifications=frozenset(),
            ),
            "Same data with source and custody witnesses.",
            "Same data content without witness availability.",
        ),
        "governance": (
            ASPProfile(
                witnesses=frozenset({"archive", "rulebook", "appeal_log", "audit_log"}),
                rights=frozenset({"read", "challenge", "appeal", "repair"}),
                maintenance_budget=2,
                reconstruction_paths=1,
                certifications=frozenset({"quorum"}),
            ),
            ASPProfile(
                witnesses=frozenset({"archive", "rulebook"}),
                rights=frozenset({"read"}),
                maintenance_budget=2,
                reconstruction_paths=0,
                certifications=frozenset({"custodian"}),
            ),
            "Same archive with public authority and appeal path.",
            "Same archive under single-custodian authority.",
        ),
        "commons": (
            ASPProfile(
                witnesses=frozenset({"resource_state", "audit_log", "repair_log"}),
                rights=frozenset({"use", "audit", "sanction", "repair"}),
                maintenance_budget=2,
                reconstruction_paths=1,
                certifications=frozenset({"public_rule"}),
            ),
            ASPProfile(
                witnesses=frozenset({"resource_state"}),
                rights=frozenset({"use"}),
                maintenance_budget=2,
                reconstruction_paths=0,
                certifications=frozenset(),
            ),
            "Same resource with audit, sanction, and repair rights.",
            "Same resource without public maintenance rights.",
        ),
        "consensus": (
            ASPProfile(
                witnesses=frozenset({"checkpoint", "validator_signatures", "slashing_log", "fraud_proof"}),
                rights=frozenset({"accept", "challenge", "slash", "rollback"}),
                maintenance_budget=3,
                reconstruction_paths=1,
                certifications=frozenset({"challenge_window"}),
            ),
            ASPProfile(
                witnesses=frozenset({"checkpoint"}),
                rights=frozenset({"accept"}),
                maintenance_budget=3,
                reconstruction_paths=0,
                certifications=frozenset({"expired_window"}),
            ),
            "Same committed state with future challenge evidence.",
            "Same committed state after challenge witnesses expire.",
        ),
        "record_system": (
            ASPProfile(
                witnesses=frozenset({"record", "index", "schema", "audit_log", "checksum"}),
                rights=frozenset({"read", "reconstruct", "certify", "repair"}),
                maintenance_budget=2,
                reconstruction_paths=1,
                certifications=frozenset({"schema_version"}),
            ),
            ASPProfile(
                witnesses=frozenset({"record", "checksum"}),
                rights=frozenset({"read", "repair"}),
                maintenance_budget=2,
                reconstruction_paths=0,
                certifications=frozenset(),
            ),
            "Same stored records with schema and audit reconstruction witnesses.",
            "Same stored records without schema/index reconstruction witnesses.",
        ),
    }[domain]
    return (
        ASPSystem(
            system_id=f"{domain}_a_high_asp",
            domain=domain,
            description=rich_description,
            metrics=metrics,
            profile=rich,
            task_universe=tasks,
        ),
        ASPSystem(
            system_id=f"{domain}_b_low_asp",
            domain=domain,
            description=poor_description,
            metrics=metrics,
            profile=poor,
            task_universe=tasks,
        ),
    )


def _lost_structure_chain(system_a: ASPSystem, system_b: ASPSystem) -> bool:
    lost_witnesses = system_a.profile.witnesses - system_b.profile.witnesses
    lost_rights = system_a.profile.rights - system_b.profile.rights
    debt_increases = system_a.profile.reconstruction_paths > system_b.profile.reconstruction_paths
    asp_reduces = len(accessible_tasks(system_a)) > len(accessible_tasks(system_b))
    return bool(lost_witnesses and lost_rights and debt_increases and asp_reduces)


def _separation_verdict(domain: str) -> str:
    return {
        "version_control": "Separates from coarse metrics; absorbed by history-aware reachability/provenance.",
        "provenance": "Separates from data equality; absorbed by provenance and side-information formalisms.",
        "governance": "Separates from archive equality; absorbed by authority-aware mechanism/commons models.",
        "commons": "Separates from resource equality; absorbed by commons governance if maintenance rights are state.",
        "consensus": "Separates from committed-state equality; absorbed by challenge-window and validator-state models.",
        "record_system": "Separates from stored-record equality; absorbed by schema/provenance/reconstruction-debt state.",
    }[domain]


def _audit_to_dict(audit: DomainAudit) -> dict[str, object]:
    return {
        "domain": audit.domain,
        "system_a": _system_to_dict(audit.system_a),
        "system_b": _system_to_dict(audit.system_b),
        "entropy_comparison": audit.entropy_equal,
        "information_comparison": audit.information_equal,
        "finality_comparison": audit.finality_equal,
        "viability_comparison": audit.viability_equal,
        "persistence_comparison": audit.persistence_equal,
        "coarse_reachability_comparison": audit.coarse_reachability_equal,
        "asp_a": sorted(audit.asp_a),
        "asp_b": sorted(audit.asp_b),
        "asp_comparison": audit.asp_split,
        "lost_structure_chain_present": audit.lost_structure_chain_present,
        "prior_art": [
            {
                "target": item.target,
                "capture": item.capture.value,
                "explanation": item.explanation,
            }
            for item in audit.prior_art
        ],
        "separation_verdict": audit.separation_verdict,
    }


def _system_to_dict(system: ASPSystem) -> dict[str, object]:
    return {
        "system_id": system.system_id,
        "description": system.description,
        "metrics": {
            "entropy_bits": system.metrics.entropy_bits,
            "information_bits": system.metrics.information_bits,
            "finality_score": system.metrics.finality_score,
            "viability_score": system.metrics.viability_score,
            "persistence_horizon": system.metrics.persistence_horizon,
            "coarse_reachable_count": system.metrics.coarse_reachable_count,
            "coarse_control_rank": system.metrics.coarse_control_rank,
        },
        "profile": {
            "witnesses": sorted(system.profile.witnesses),
            "rights": sorted(system.profile.rights),
            "maintenance_budget": system.profile.maintenance_budget,
            "reconstruction_paths": system.profile.reconstruction_paths,
            "certifications": sorted(system.profile.certifications),
        },
        "accessible_tasks": sorted(accessible_tasks(system)),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t117_result_to_dict(run_t117_analysis()), indent=2))
