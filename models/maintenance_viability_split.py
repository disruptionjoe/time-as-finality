"""T115: maintenance-cost viability split under absorption pressure.

The audit asks whether maintained records can match on ordinary stability,
entropy, control, resilience, viability, and storage metrics while splitting on
future operation capability.  The point is not to prove a new direction.  The
point is to locate the residue after aggressive comparison with existing
frameworks.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Capture(Enum):
    CAPTURES_IF_ENRICHED = "captures_if_enriched"
    PARTIAL = "partial"
    DOES_NOT_CAPTURE_COARSE = "does_not_capture_coarse"


@dataclass(frozen=True)
class StandardMetrics:
    entropy_export: int
    control_effort: int
    stability_window: int
    viability_kernel: str
    resilience_recovery_steps: int
    storage_bits: int
    maintained_record_count: int


@dataclass(frozen=True)
class OperationProfile:
    accessible_witnesses: frozenset[str]
    required_witnesses: frozenset[str]
    operation_rights: frozenset[str]
    required_rights: frozenset[str]
    reconstruction_paths: int
    admissibility_tokens: frozenset[str]
    required_tokens: frozenset[str]


@dataclass(frozen=True)
class MaintainedSystem:
    system_id: str
    domain: str
    description: str
    metrics: StandardMetrics
    profile: OperationProfile


@dataclass(frozen=True)
class FrameworkComparison:
    framework: str
    capture: Capture
    reason: str


@dataclass(frozen=True)
class PairAudit:
    pair_id: str
    domain: str
    system_a: MaintainedSystem
    system_b: MaintainedSystem
    standard_equivalent: bool
    maintained_records_equal: bool
    future_operation_split: bool
    a_future_usable: bool
    b_future_usable: bool
    differing_axis: tuple[str, ...]
    comparisons: tuple[FrameworkComparison, ...]
    strongest_separation: str
    strongest_absorption: str


@dataclass(frozen=True)
class T115Result:
    pair_audits: tuple[PairAudit, ...]
    strongest_separation_case: str
    strongest_absorption_case: str
    closest_existing_theory: str
    missing_mathematical_object: str
    recommendation: str
    current_strongest_claim: str
    weakened_or_falsified: str
    open_blocker: str
    claim_ledger_update: str


def canonical_pairs() -> tuple[tuple[MaintainedSystem, MaintainedSystem], ...]:
    common = StandardMetrics(
        entropy_export=6,
        control_effort=4,
        stability_window=12,
        viability_kernel="stable_archive_kernel_v1",
        resilience_recovery_steps=2,
        storage_bits=128,
        maintained_record_count=3,
    )
    vcs_metrics = StandardMetrics(
        entropy_export=5,
        control_effort=3,
        stability_window=10,
        viability_kernel="same_endpoint_tree_kernel",
        resilience_recovery_steps=1,
        storage_bits=96,
        maintained_record_count=2,
    )
    consensus_metrics = StandardMetrics(
        entropy_export=7,
        control_effort=5,
        stability_window=15,
        viability_kernel="committed_checkpoint_kernel",
        resilience_recovery_steps=2,
        storage_bits=160,
        maintained_record_count=4,
    )
    return (
        (
            MaintainedSystem(
                system_id="record_commons_a_auditable",
                domain="record_commons",
                description=(
                    "Shared archive keeps identical records plus public audit "
                    "witnesses and repair authority."
                ),
                metrics=common,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"record", "checksum", "audit_log"}),
                    required_witnesses=frozenset({"record", "audit_log"}),
                    operation_rights=frozenset({"read", "challenge", "repair"}),
                    required_rights=frozenset({"challenge", "repair"}),
                    reconstruction_paths=2,
                    admissibility_tokens=frozenset({"public_rulebook", "quorum"}),
                    required_tokens=frozenset({"public_rulebook", "quorum"}),
                ),
            ),
            MaintainedSystem(
                system_id="record_commons_b_private_mirror",
                domain="record_commons",
                description=(
                    "Archive keeps the same records with the same ordinary "
                    "maintenance metrics, but audit witnesses and repair "
                    "authority are not available to the commons."
                ),
                metrics=common,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"record", "checksum"}),
                    required_witnesses=frozenset({"record", "audit_log"}),
                    operation_rights=frozenset({"read"}),
                    required_rights=frozenset({"challenge", "repair"}),
                    reconstruction_paths=2,
                    admissibility_tokens=frozenset({"private_policy"}),
                    required_tokens=frozenset({"public_rulebook", "quorum"}),
                ),
            ),
        ),
        (
            MaintainedSystem(
                system_id="provenance_a_signed_lineage",
                domain="provenance",
                description=(
                    "Output artifact is maintained with signed lineage, "
                    "source witness, and admissible attribution token."
                ),
                metrics=common,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"output", "source", "signature"}),
                    required_witnesses=frozenset({"output", "source", "signature"}),
                    operation_rights=frozenset({"use", "attribute", "certify"}),
                    required_rights=frozenset({"attribute", "certify"}),
                    reconstruction_paths=1,
                    admissibility_tokens=frozenset({"chain_of_custody"}),
                    required_tokens=frozenset({"chain_of_custody"}),
                ),
            ),
            MaintainedSystem(
                system_id="provenance_b_content_only",
                domain="provenance",
                description=(
                    "Output artifact is byte-identical and equally maintained, "
                    "but source witness and signature are missing."
                ),
                metrics=common,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"output"}),
                    required_witnesses=frozenset({"output", "source", "signature"}),
                    operation_rights=frozenset({"use"}),
                    required_rights=frozenset({"attribute", "certify"}),
                    reconstruction_paths=0,
                    admissibility_tokens=frozenset(),
                    required_tokens=frozenset({"chain_of_custody"}),
                ),
            ),
        ),
        (
            MaintainedSystem(
                system_id="version_control_a_history_preserved",
                domain="version_control",
                description=(
                    "Endpoint files match the release snapshot, but branch "
                    "history, merge base, and blame witnesses are preserved."
                ),
                metrics=vcs_metrics,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"tree", "merge_base", "branch_history"}),
                    required_witnesses=frozenset({"tree", "merge_base"}),
                    operation_rights=frozenset({"build", "merge", "revert", "bisect"}),
                    required_rights=frozenset({"merge", "revert"}),
                    reconstruction_paths=3,
                    admissibility_tokens=frozenset({"signed_tags"}),
                    required_tokens=frozenset({"signed_tags"}),
                ),
            ),
            MaintainedSystem(
                system_id="version_control_b_squashed_snapshot",
                domain="version_control",
                description=(
                    "Endpoint files, storage, and stability match, but the "
                    "history needed for future merge/revert operations is gone."
                ),
                metrics=vcs_metrics,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"tree"}),
                    required_witnesses=frozenset({"tree", "merge_base"}),
                    operation_rights=frozenset({"build"}),
                    required_rights=frozenset({"merge", "revert"}),
                    reconstruction_paths=0,
                    admissibility_tokens=frozenset({"unsigned_snapshot"}),
                    required_tokens=frozenset({"signed_tags"}),
                ),
            ),
        ),
        (
            MaintainedSystem(
                system_id="governance_a_distributed_authority",
                domain="governance",
                description=(
                    "Same archive and maintenance level, with rulebook, quorum, "
                    "appeal path, and repair authority available."
                ),
                metrics=common,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"archive", "rulebook", "appeal_log"}),
                    required_witnesses=frozenset({"archive", "rulebook"}),
                    operation_rights=frozenset({"read", "challenge", "appeal", "repair"}),
                    required_rights=frozenset({"challenge", "appeal"}),
                    reconstruction_paths=2,
                    admissibility_tokens=frozenset({"quorum", "public_procedure"}),
                    required_tokens=frozenset({"quorum", "public_procedure"}),
                ),
            ),
            MaintainedSystem(
                system_id="governance_b_single_custodian",
                domain="governance",
                description=(
                    "Same archive and maintenance level, but authority is "
                    "centralized and future challenge rights are absent."
                ),
                metrics=common,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"archive", "rulebook"}),
                    required_witnesses=frozenset({"archive", "rulebook"}),
                    operation_rights=frozenset({"read"}),
                    required_rights=frozenset({"challenge", "appeal"}),
                    reconstruction_paths=2,
                    admissibility_tokens=frozenset({"custodian_discretion"}),
                    required_tokens=frozenset({"quorum", "public_procedure"}),
                ),
            ),
        ),
        (
            MaintainedSystem(
                system_id="consensus_a_challenge_window",
                domain="consensus",
                description=(
                    "Same committed checkpoint, but validator signatures and "
                    "challenge window remain available for future dispute."
                ),
                metrics=consensus_metrics,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"checkpoint", "signatures", "slashing_log"}),
                    required_witnesses=frozenset({"checkpoint", "signatures"}),
                    operation_rights=frozenset({"accept", "challenge", "slash", "rollback"}),
                    required_rights=frozenset({"challenge", "slash"}),
                    reconstruction_paths=2,
                    admissibility_tokens=frozenset({"validator_set", "deadline"}),
                    required_tokens=frozenset({"validator_set", "deadline"}),
                ),
            ),
            MaintainedSystem(
                system_id="consensus_b_checkpoint_only",
                domain="consensus",
                description=(
                    "Same committed checkpoint and ordinary maintenance, but "
                    "future challenge evidence and slashing rights are gone."
                ),
                metrics=consensus_metrics,
                profile=OperationProfile(
                    accessible_witnesses=frozenset({"checkpoint"}),
                    required_witnesses=frozenset({"checkpoint", "signatures"}),
                    operation_rights=frozenset({"accept"}),
                    required_rights=frozenset({"challenge", "slash"}),
                    reconstruction_paths=0,
                    admissibility_tokens=frozenset({"expired_window"}),
                    required_tokens=frozenset({"validator_set", "deadline"}),
                ),
            ),
        ),
    )


def future_usable(system: MaintainedSystem) -> bool:
    profile = system.profile
    return (
        profile.required_witnesses <= profile.accessible_witnesses
        and profile.required_rights <= profile.operation_rights
        and profile.required_tokens <= profile.admissibility_tokens
        and profile.reconstruction_paths > 0
    )


def audit_pair(system_a: MaintainedSystem, system_b: MaintainedSystem) -> PairAudit:
    standard_equivalent = system_a.metrics == system_b.metrics
    maintained_records_equal = (
        system_a.metrics.maintained_record_count
        == system_b.metrics.maintained_record_count
    )
    a_usable = future_usable(system_a)
    b_usable = future_usable(system_b)
    differing_axis = _differing_axes(system_a.profile, system_b.profile)
    split = standard_equivalent and maintained_records_equal and a_usable != b_usable
    comparisons = framework_comparisons(system_a.domain)
    return PairAudit(
        pair_id=f"{system_a.domain}_matched_split",
        domain=system_a.domain,
        system_a=system_a,
        system_b=system_b,
        standard_equivalent=standard_equivalent,
        maintained_records_equal=maintained_records_equal,
        future_operation_split=split,
        a_future_usable=a_usable,
        b_future_usable=b_usable,
        differing_axis=differing_axis,
        comparisons=comparisons,
        strongest_separation=_separation_text(system_a.domain),
        strongest_absorption=_absorption_text(system_a.domain),
    )


def run_t115_analysis() -> T115Result:
    audits = tuple(audit_pair(a, b) for a, b in canonical_pairs())
    if not all(audit.standard_equivalent for audit in audits):
        raise AssertionError("canonical pairs must match on standard metrics")
    if not all(audit.future_operation_split for audit in audits):
        raise AssertionError("canonical pairs must split on future operation capability")
    return T115Result(
        pair_audits=audits,
        strongest_separation_case=(
            "Version control is the sharpest finite separation: the endpoint "
            "tree, storage, stability, control effort, and viability label match, "
            "but only the history-preserving system retains future merge, revert, "
            "and bisect rights. Coarse entropy/control/viability metrics cannot "
            "see the split without adding history/provenance to the state."
        ),
        strongest_absorption_case=(
            "The same version-control case is also the strongest absorption "
            "case: ordinary provenance/version-control theory already treats "
            "merge bases, signed tags, and branch history as operational state. "
            "Once those are included, the split is not a new physics object."
        ),
        closest_existing_theory=(
            "Provenance systems plus viability kernels with task-state "
            "enrichment are closest. Commons governance captures authority and "
            "challenge rights; LossKernel/reconstruction debt captures missing "
            "witness obligations. Entropy, control, resilience, and raw "
            "information storage capture only coarse versions unless enriched."
        ),
        missing_mathematical_object=(
            "A task-indexed operation-right state: maintained records plus "
            "accessible witnesses, authority/admissibility tokens, and "
            "reconstruction obligations for a future operation family. It is "
            "not just maintenance cost; it is maintained usability under "
            "declared operations."
        ),
        recommendation=(
            "Preserve and formalize narrowly as operation-right-bearing "
            "provenance/reconstruction debt. Do not promote as independent "
            "physics, and abandon any wording that suggests maintenance cost "
            "replaces entropy production or viability theory."
        ),
        current_strongest_claim=(
            "Finite examples exist where ordinary entropy, control, stability, "
            "resilience, viability, and storage metrics match while future "
            "operation capability differs. The residue is access to witnesses, "
            "authority tokens, reconstruction paths, and operation rights."
        ),
        weakened_or_falsified=(
            "Maintenance-cost accounting does not appear independent of all "
            "existing theory. The strongest cases are absorbed by provenance, "
            "commons governance, version-control semantics, and "
            "LossKernel/reconstruction-debt language once those frameworks "
            "include operation rights in their state."
        ),
        open_blocker=(
            "There is still no non-engineered physical example where this "
            "operation-right residue separates from enriched viability, "
            "free-energy/control, provenance, and information-theoretic side "
            "information."
        ),
        claim_ledger_update=(
            "No core claim upgrade. T115 preserves maintenance-cost viability "
            "only as a narrow operation-right/provenance audit object: matched "
            "standard metrics can split on future usability, but the split is "
            "largely absorbed by existing provenance, commons, and "
            "reconstruction-debt theories when they are given the right state."
        ),
    )


def t115_result_to_dict(result: T115Result) -> dict[str, object]:
    return {
        "pair_audits": [_pair_audit_to_dict(audit) for audit in result.pair_audits],
        "strongest_separation_case": result.strongest_separation_case,
        "strongest_absorption_case": result.strongest_absorption_case,
        "closest_existing_theory": result.closest_existing_theory,
        "missing_mathematical_object": result.missing_mathematical_object,
        "recommendation": result.recommendation,
        "current_strongest_claim": result.current_strongest_claim,
        "weakened_or_falsified": result.weakened_or_falsified,
        "open_blocker": result.open_blocker,
        "claim_ledger_update": result.claim_ledger_update,
    }


def framework_comparisons(domain: str) -> tuple[FrameworkComparison, ...]:
    base = (
        FrameworkComparison(
            "entropy production",
            Capture.DOES_NOT_CAPTURE_COARSE,
            "Entropy/export is matched; it sees cost paid, not who can use the record later.",
        ),
        FrameworkComparison(
            "control-theoretic state maintenance",
            Capture.CAPTURES_IF_ENRICHED,
            "Coarse control effort is matched; a controller with task-state including rights can capture the split.",
        ),
        FrameworkComparison(
            "viability kernels",
            Capture.CAPTURES_IF_ENRICHED,
            "The viability label is matched; viability theory captures the split if the constraint set includes future operation rights.",
        ),
        FrameworkComparison(
            "resilience/adaptive-cycle models",
            Capture.PARTIAL,
            "Recovery and persistence are matched; resilience captures the split only when function is defined as audit/repair/challenge capability.",
        ),
        FrameworkComparison(
            "free-energy formulations",
            Capture.CAPTURES_IF_ENRICHED,
            "Coarse self-maintenance is matched; an active-inference model with witnesses and policies in the generative state could absorb it.",
        ),
        FrameworkComparison(
            "information-theoretic storage",
            Capture.DOES_NOT_CAPTURE_COARSE,
            "Storage bits and record count are matched; raw information quantity misses admissible side information and access rights.",
        ),
        FrameworkComparison(
            "provenance systems",
            Capture.CAPTURES_IF_ENRICHED,
            "Witness availability, lineage, custody, and admissibility tokens are native provenance data.",
        ),
        FrameworkComparison(
            "LossKernel/reconstruction debt",
            Capture.CAPTURES_IF_ENRICHED,
            "Missing witnesses are exactly reconstruction obligations when the operation family is declared.",
        ),
    )
    commons = FrameworkComparison(
        "commons/public-goods models",
        Capture.CAPTURES_IF_ENRICHED if domain in {"record_commons", "governance", "consensus"} else Capture.PARTIAL,
        (
            "Monitoring, sanctioning, repair authority, and challenge rights are "
            "native commons-governance variables for shared records."
        ),
    )
    return base[:5] + (commons,) + base[5:]


def _pair_audit_to_dict(audit: PairAudit) -> dict[str, object]:
    return {
        "pair_id": audit.pair_id,
        "domain": audit.domain,
        "system_a": _system_to_dict(audit.system_a),
        "system_b": _system_to_dict(audit.system_b),
        "standard_equivalent": audit.standard_equivalent,
        "maintained_records_equal": audit.maintained_records_equal,
        "future_operation_split": audit.future_operation_split,
        "a_future_usable": audit.a_future_usable,
        "b_future_usable": audit.b_future_usable,
        "differing_axis": list(audit.differing_axis),
        "comparisons": [
            {
                "framework": comparison.framework,
                "capture": comparison.capture.value,
                "reason": comparison.reason,
            }
            for comparison in audit.comparisons
        ],
        "strongest_separation": audit.strongest_separation,
        "strongest_absorption": audit.strongest_absorption,
    }


def _system_to_dict(system: MaintainedSystem) -> dict[str, object]:
    return {
        "system_id": system.system_id,
        "domain": system.domain,
        "description": system.description,
        "metrics": {
            "entropy_export": system.metrics.entropy_export,
            "control_effort": system.metrics.control_effort,
            "stability_window": system.metrics.stability_window,
            "viability_kernel": system.metrics.viability_kernel,
            "resilience_recovery_steps": system.metrics.resilience_recovery_steps,
            "storage_bits": system.metrics.storage_bits,
            "maintained_record_count": system.metrics.maintained_record_count,
        },
        "profile": {
            "accessible_witnesses": sorted(system.profile.accessible_witnesses),
            "required_witnesses": sorted(system.profile.required_witnesses),
            "operation_rights": sorted(system.profile.operation_rights),
            "required_rights": sorted(system.profile.required_rights),
            "reconstruction_paths": system.profile.reconstruction_paths,
            "admissibility_tokens": sorted(system.profile.admissibility_tokens),
            "required_tokens": sorted(system.profile.required_tokens),
        },
        "future_usable": future_usable(system),
    }


def _differing_axes(left: OperationProfile, right: OperationProfile) -> tuple[str, ...]:
    axes = []
    if left.accessible_witnesses != right.accessible_witnesses:
        axes.append("accessible_witnesses")
    if left.operation_rights != right.operation_rights:
        axes.append("operation_rights")
    if left.reconstruction_paths != right.reconstruction_paths:
        axes.append("reconstruction_paths")
    if left.admissibility_tokens != right.admissibility_tokens:
        axes.append("admissibility_tokens")
    return tuple(axes)


def _separation_text(domain: str) -> str:
    return {
        "record_commons": "Audit and repair rights split while ordinary maintenance metrics match.",
        "provenance": "Attribution and certification split while output storage and stability match.",
        "version_control": "Future merge/revert capability splits while endpoint state and ordinary metrics match.",
        "governance": "Challenge and appeal rights split while archive maintenance metrics match.",
        "consensus": "Future dispute/slashing rights split while committed checkpoint metrics match.",
    }[domain]


def _absorption_text(domain: str) -> str:
    return {
        "record_commons": "Commons governance and provenance absorb the distinction if audit rights are modeled.",
        "provenance": "Provenance theory directly absorbs the distinction as lineage/custody state.",
        "version_control": "Version-control semantics absorb the distinction as history/merge-base state.",
        "governance": "Commons and institutional-governance models absorb the authority-right split.",
        "consensus": "Distributed-systems and provenance models absorb challenge evidence and validator-state rights.",
    }[domain]


if __name__ == "__main__":
    import json

    print(json.dumps(t115_result_to_dict(run_t115_analysis()), indent=2))
