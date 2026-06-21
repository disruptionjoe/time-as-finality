"""T120: ASP typed subpresheaf and absorption audit.

The model narrows ASP to a finite observer/task-indexed admissible future set.
It checks whether the object behaves like a typed subpresheaf under stable
restriction, whether controls fail for the right reasons, and whether the
finite separation from coarse metrics is absorbed by enriched reachability.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping


class Capture(Enum):
    MISSES_COARSE = "misses_coarse"
    CAPTURES_IF_ENRICHED = "captures_if_enriched"
    CAPTURES_DIRECTLY = "captures_directly"
    PARTIAL = "partial"


@dataclass(frozen=True)
class Patch:
    name: str
    subsets: frozenset[str]


@dataclass(frozen=True)
class SectionRequirement:
    name: str
    patch: str
    required_witnesses: frozenset[str]
    required_rights: frozenset[str]
    required_maintenance: int
    required_reconstruction_paths: int
    required_certifications: frozenset[str]
    viable: bool = True
    causally_accessible: bool = True


@dataclass(frozen=True)
class ObserverProfile:
    observer: str
    witnesses_by_patch: Mapping[str, frozenset[str]]
    rights_by_patch: Mapping[str, frozenset[str]]
    maintenance_budget_by_patch: Mapping[str, int]
    reconstruction_paths_by_patch: Mapping[str, int]
    certifications_by_patch: Mapping[str, frozenset[str]]


@dataclass(frozen=True)
class PresheafSystem:
    patches: Mapping[str, Patch]
    sections_by_patch: Mapping[str, tuple[SectionRequirement, ...]]
    restrictions: Mapping[tuple[str, str], Mapping[str, str]]
    observer_profile: ObserverProfile


@dataclass(frozen=True)
class RestrictionAudit:
    name: str
    closure_holds: bool
    violations: tuple[str, ...]
    asp_by_patch: Mapping[str, frozenset[str]]


@dataclass(frozen=True)
class RelabelAudit:
    invariant: bool
    original_signature: tuple[tuple[str, tuple[str, ...]], ...]
    relabeled_signature: tuple[tuple[str, tuple[str, ...]], ...]


@dataclass(frozen=True)
class BoundaryAudit:
    invariant_under_boundary_change: bool
    covariant_change_detected: bool
    coarse_asp: frozenset[str]
    refined_asp: frozenset[str]
    explanation: str


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
class ASPProfile:
    witnesses: frozenset[str]
    rights: frozenset[str]
    maintenance_budget: int
    reconstruction_paths: int
    certifications: frozenset[str]


@dataclass(frozen=True)
class TaskRequirement:
    name: str
    required_witnesses: frozenset[str]
    required_rights: frozenset[str]
    required_maintenance: int
    required_reconstruction_paths: int
    required_certifications: frozenset[str]


@dataclass(frozen=True)
class MatchedSystem:
    name: str
    metrics: MatchedMetrics
    profile: ASPProfile
    task_universe: tuple[TaskRequirement, ...]


@dataclass(frozen=True)
class AbsorptionAudit:
    coarse_metrics_match: bool
    coarse_reachability_separates: bool
    asp_separates: bool
    enriched_reachability_absorbs: bool
    opportunity_set_absorbs: bool
    high_asp_tasks: frozenset[str]
    low_asp_tasks: frozenset[str]
    prior_art: Mapping[str, Capture]


@dataclass(frozen=True)
class T120Result:
    positive_restriction: RestrictionAudit
    negative_restriction: RestrictionAudit
    relabeling: RelabelAudit
    boundary: BoundaryAudit
    absorption: AbsorptionAudit
    strongest_version: str
    weakest_point: str
    verdict: str
    recommendation: str
    claim_impact: str


def accessible_sections(
    sections: tuple[SectionRequirement, ...],
    profile: ObserverProfile,
    patch: str,
) -> frozenset[str]:
    witnesses = profile.witnesses_by_patch[patch]
    rights = profile.rights_by_patch[patch]
    maintenance = profile.maintenance_budget_by_patch[patch]
    reconstruction_paths = profile.reconstruction_paths_by_patch[patch]
    certifications = profile.certifications_by_patch[patch]
    return frozenset(
        section.name
        for section in sections
        if section.causally_accessible
        and section.viable
        and section.required_witnesses <= witnesses
        and section.required_rights <= rights
        and section.required_maintenance <= maintenance
        and section.required_reconstruction_paths <= reconstruction_paths
        and section.required_certifications <= certifications
    )


def audit_restriction(system: PresheafSystem, name: str) -> RestrictionAudit:
    asp_by_patch = {
        patch: accessible_sections(system.sections_by_patch[patch], system.observer_profile, patch)
        for patch in system.sections_by_patch
    }
    violations: list[str] = []
    for (larger, smaller), mapping in system.restrictions.items():
        smaller_asp = asp_by_patch[smaller]
        for section_name in asp_by_patch[larger]:
            restricted = mapping.get(section_name)
            if restricted is None:
                violations.append(f"{section_name}: no restriction {larger}->{smaller}")
            elif restricted not in smaller_asp:
                violations.append(
                    f"{section_name}|{smaller}={restricted} not in ASP({smaller})"
                )
    return RestrictionAudit(
        name=name,
        closure_holds=not violations,
        violations=tuple(violations),
        asp_by_patch=asp_by_patch,
    )


def build_positive_presheaf() -> PresheafSystem:
    patches = {
        "U": Patch("U", frozenset()),
        "V": Patch("V", frozenset({"U"})),
    }
    sections_by_patch = {
        "U": (
            SectionRequirement(
                "build_local",
                "U",
                frozenset({"tree"}),
                frozenset({"read"}),
                1,
                0,
                frozenset(),
            ),
            SectionRequirement(
                "merge_local",
                "U",
                frozenset({"tree", "merge_base"}),
                frozenset({"read", "merge"}),
                1,
                1,
                frozenset({"signed_history"}),
            ),
        ),
        "V": (
            SectionRequirement(
                "build_global",
                "V",
                frozenset({"tree"}),
                frozenset({"read"}),
                1,
                0,
                frozenset(),
            ),
            SectionRequirement(
                "merge_global",
                "V",
                frozenset({"tree", "merge_base"}),
                frozenset({"read", "merge"}),
                1,
                1,
                frozenset({"signed_history"}),
            ),
        ),
    }
    profile = ObserverProfile(
        observer="O",
        witnesses_by_patch={
            "U": frozenset({"tree", "merge_base"}),
            "V": frozenset({"tree", "merge_base", "branch_history"}),
        },
        rights_by_patch={
            "U": frozenset({"read", "merge"}),
            "V": frozenset({"read", "merge", "revert"}),
        },
        maintenance_budget_by_patch={"U": 2, "V": 2},
        reconstruction_paths_by_patch={"U": 1, "V": 2},
        certifications_by_patch={
            "U": frozenset({"signed_history"}),
            "V": frozenset({"signed_history"}),
        },
    )
    return PresheafSystem(
        patches=patches,
        sections_by_patch=sections_by_patch,
        restrictions={
            ("V", "U"): {
                "build_global": "build_local",
                "merge_global": "merge_local",
            }
        },
        observer_profile=profile,
    )


def build_negative_presheaf() -> PresheafSystem:
    system = build_positive_presheaf()
    broken_profile = ObserverProfile(
        observer="O",
        witnesses_by_patch={
            "U": frozenset({"tree"}),
            "V": frozenset({"tree", "merge_base", "branch_history"}),
        },
        rights_by_patch=system.observer_profile.rights_by_patch,
        maintenance_budget_by_patch=system.observer_profile.maintenance_budget_by_patch,
        reconstruction_paths_by_patch={
            "U": 0,
            "V": 2,
        },
        certifications_by_patch={
            "U": frozenset(),
            "V": frozenset({"signed_history"}),
        },
    )
    return PresheafSystem(
        patches=system.patches,
        sections_by_patch=system.sections_by_patch,
        restrictions=system.restrictions,
        observer_profile=broken_profile,
    )


def relabel_system(system: PresheafSystem) -> PresheafSystem:
    section_map = {
        "build_local": "alpha_local",
        "merge_local": "beta_local",
        "build_global": "alpha_global",
        "merge_global": "beta_global",
    }
    witness_map = {
        "tree": "w_tree",
        "merge_base": "w_merge_base",
        "branch_history": "w_branch_history",
    }
    right_map = {
        "read": "r_read",
        "merge": "r_merge",
        "revert": "r_revert",
    }
    cert_map = {
        "signed_history": "c_signed_history",
    }

    def map_set(values: frozenset[str], mapping: Mapping[str, str]) -> frozenset[str]:
        return frozenset(mapping.get(value, value) for value in values)

    sections_by_patch = {
        patch: tuple(
            SectionRequirement(
                name=section_map[section.name],
                patch=section.patch,
                required_witnesses=map_set(section.required_witnesses, witness_map),
                required_rights=map_set(section.required_rights, right_map),
                required_maintenance=section.required_maintenance,
                required_reconstruction_paths=section.required_reconstruction_paths,
                required_certifications=map_set(section.required_certifications, cert_map),
                viable=section.viable,
                causally_accessible=section.causally_accessible,
            )
            for section in sections
        )
        for patch, sections in system.sections_by_patch.items()
    }
    profile = system.observer_profile
    relabeled_profile = ObserverProfile(
        observer="O_prime",
        witnesses_by_patch={
            patch: map_set(values, witness_map)
            for patch, values in profile.witnesses_by_patch.items()
        },
        rights_by_patch={
            patch: map_set(values, right_map)
            for patch, values in profile.rights_by_patch.items()
        },
        maintenance_budget_by_patch=profile.maintenance_budget_by_patch,
        reconstruction_paths_by_patch=profile.reconstruction_paths_by_patch,
        certifications_by_patch={
            patch: map_set(values, cert_map)
            for patch, values in profile.certifications_by_patch.items()
        },
    )
    restrictions = {
        key: {section_map[source]: section_map[target] for source, target in mapping.items()}
        for key, mapping in system.restrictions.items()
    }
    return PresheafSystem(
        patches=system.patches,
        sections_by_patch=sections_by_patch,
        restrictions=restrictions,
        observer_profile=relabeled_profile,
    )


def _signature(audit: RestrictionAudit) -> tuple[tuple[str, tuple[str, ...]], ...]:
    return tuple(
        (patch, tuple(sorted(_normalize_section_name(name) for name in names)))
        for patch, names in sorted(audit.asp_by_patch.items())
    )


def _normalize_section_name(name: str) -> str:
    return (
        name.replace("alpha", "build")
        .replace("beta", "merge")
        .replace("global", "global")
        .replace("local", "local")
    )


def audit_relabeling() -> RelabelAudit:
    original = audit_restriction(build_positive_presheaf(), "original")
    relabeled = audit_restriction(relabel_system(build_positive_presheaf()), "relabeled")
    original_signature = _signature(original)
    relabeled_signature = _signature(relabeled)
    return RelabelAudit(
        invariant=original_signature == relabeled_signature,
        original_signature=original_signature,
        relabeled_signature=relabeled_signature,
    )


def audit_boundary_covariance() -> BoundaryAudit:
    task_universe = version_control_task_universe()
    coarse = MatchedSystem(
        name="coarse_boundary",
        metrics=matched_metrics(),
        profile=ASPProfile(
            witnesses=frozenset({"tree"}),
            rights=frozenset({"read", "write"}),
            maintenance_budget=2,
            reconstruction_paths=0,
            certifications=frozenset({"snapshot_hash"}),
        ),
        task_universe=task_universe,
    )
    refined = MatchedSystem(
        name="refined_boundary",
        metrics=matched_metrics(),
        profile=ASPProfile(
            witnesses=frozenset({"tree", "merge_base", "branch_history"}),
            rights=frozenset({"read", "write", "merge", "revert", "bisect"}),
            maintenance_budget=2,
            reconstruction_paths=2,
            certifications=frozenset({"signed_history"}),
        ),
        task_universe=task_universe,
    )
    coarse_asp = accessible_tasks(coarse)
    refined_asp = accessible_tasks(refined)
    return BoundaryAudit(
        invariant_under_boundary_change=coarse_asp == refined_asp,
        covariant_change_detected=coarse_asp < refined_asp,
        coarse_asp=coarse_asp,
        refined_asp=refined_asp,
        explanation=(
            "Access-boundary refinement changes ASP from snapshot-only tasks to "
            "history-aware tasks. This is a declared boundary change, not gauge."
        ),
    )


def matched_metrics() -> MatchedMetrics:
    return MatchedMetrics(
        entropy_bits=8,
        information_bits=8,
        finality_score=4,
        viability_score=4,
        persistence_horizon=10,
        coarse_reachable_count=4,
        coarse_control_rank=3,
    )


def version_control_task_universe() -> tuple[TaskRequirement, ...]:
    return (
        TaskRequirement("build", frozenset({"tree"}), frozenset({"read"}), 1, 0, frozenset()),
        TaskRequirement(
            "merge",
            frozenset({"tree", "merge_base"}),
            frozenset({"write", "merge"}),
            2,
            1,
            frozenset({"signed_history"}),
        ),
        TaskRequirement(
            "revert",
            frozenset({"tree", "branch_history"}),
            frozenset({"write", "revert"}),
            2,
            1,
            frozenset({"signed_history"}),
        ),
        TaskRequirement(
            "bisect",
            frozenset({"tree", "branch_history"}),
            frozenset({"read", "bisect"}),
            1,
            1,
            frozenset(),
        ),
    )


def accessible_tasks(system: MatchedSystem) -> frozenset[str]:
    profile = system.profile
    return frozenset(
        task.name
        for task in system.task_universe
        if task.required_witnesses <= profile.witnesses
        and task.required_rights <= profile.rights
        and task.required_maintenance <= profile.maintenance_budget
        and task.required_reconstruction_paths <= profile.reconstruction_paths
        and task.required_certifications <= profile.certifications
    )


def enriched_reachable_tasks(system: MatchedSystem) -> frozenset[str]:
    return accessible_tasks(system)


def audit_absorption() -> AbsorptionAudit:
    task_universe = version_control_task_universe()
    high = MatchedSystem(
        name="history_preserving_repo",
        metrics=matched_metrics(),
        profile=ASPProfile(
            witnesses=frozenset({"tree", "merge_base", "branch_history"}),
            rights=frozenset({"read", "write", "merge", "revert", "bisect"}),
            maintenance_budget=2,
            reconstruction_paths=2,
            certifications=frozenset({"signed_history"}),
        ),
        task_universe=task_universe,
    )
    low = MatchedSystem(
        name="squashed_snapshot_repo",
        metrics=matched_metrics(),
        profile=ASPProfile(
            witnesses=frozenset({"tree"}),
            rights=frozenset({"read", "write"}),
            maintenance_budget=2,
            reconstruction_paths=0,
            certifications=frozenset({"snapshot_hash"}),
        ),
        task_universe=task_universe,
    )
    high_asp = accessible_tasks(high)
    low_asp = accessible_tasks(low)
    high_enriched = enriched_reachable_tasks(high)
    low_enriched = enriched_reachable_tasks(low)
    return AbsorptionAudit(
        coarse_metrics_match=high.metrics == low.metrics,
        coarse_reachability_separates=False,
        asp_separates=high_asp != low_asp,
        enriched_reachability_absorbs=(high_enriched == high_asp and low_enriched == low_asp),
        opportunity_set_absorbs=(high_enriched == high_asp and low_enriched == low_asp),
        high_asp_tasks=high_asp,
        low_asp_tasks=low_asp,
        prior_art={
            "reachability analysis": Capture.CAPTURES_IF_ENRICHED,
            "viability kernels": Capture.CAPTURES_IF_ENRICHED,
            "active inference policy spaces": Capture.CAPTURES_IF_ENRICHED,
            "reinforcement-learning action/state spaces": Capture.CAPTURES_IF_ENRICHED,
            "affordance landscapes": Capture.PARTIAL,
            "opportunity sets": Capture.CAPTURES_DIRECTLY,
            "information-theoretic distinguishability": Capture.PARTIAL,
            "finality/reconstruction debt": Capture.PARTIAL,
            "sheaf/section compatibility": Capture.PARTIAL,
            "GU source-shadow projection": Capture.PARTIAL,
        },
    )


def run_t120_analysis() -> T120Result:
    positive = audit_restriction(build_positive_presheaf(), "stable_typed_predicates")
    negative = audit_restriction(build_negative_presheaf(), "audit_monotonicity_violation")
    relabeling = audit_relabeling()
    boundary = audit_boundary_covariance()
    absorption = audit_absorption()
    return T120Result(
        positive_restriction=positive,
        negative_restriction=negative,
        relabeling=relabeling,
        boundary=boundary,
        absorption=absorption,
        strongest_version=(
            "ASP_O^T(U,h) is a typed observer/task-indexed admissible future "
            "set, modeled as a subpresheaf of finite local sections when "
            "admissibility predicates restrict stably."
        ),
        weakest_point=(
            "ASP loses type discipline when restriction, forward transport, "
            "viability dynamics, measures, and goal functionals are collapsed "
            "into one symbol."
        ),
        verdict=(
            "ASP separates from coarse baselines but is absorbed by enriched "
            "reachable-state, opportunity-set, provenance, and task-enriched "
            "viability formalisms."
        ),
        recommendation=(
            "Preserve and formalize narrowly as an audit object. Do not promote "
            "ASP as a primitive, a GU result, or independent physics."
        ),
        claim_impact="No core claim upgrade.",
    )


def t120_result_to_dict(result: T120Result) -> dict[str, object]:
    return {
        "positive_restriction": _restriction_to_dict(result.positive_restriction),
        "negative_restriction": _restriction_to_dict(result.negative_restriction),
        "relabeling": {
            "invariant": result.relabeling.invariant,
            "original_signature": result.relabeling.original_signature,
            "relabeled_signature": result.relabeling.relabeled_signature,
        },
        "boundary": {
            "invariant_under_boundary_change": result.boundary.invariant_under_boundary_change,
            "covariant_change_detected": result.boundary.covariant_change_detected,
            "coarse_asp": sorted(result.boundary.coarse_asp),
            "refined_asp": sorted(result.boundary.refined_asp),
            "explanation": result.boundary.explanation,
        },
        "absorption": {
            "coarse_metrics_match": result.absorption.coarse_metrics_match,
            "coarse_reachability_separates": result.absorption.coarse_reachability_separates,
            "asp_separates": result.absorption.asp_separates,
            "enriched_reachability_absorbs": result.absorption.enriched_reachability_absorbs,
            "opportunity_set_absorbs": result.absorption.opportunity_set_absorbs,
            "high_asp_tasks": sorted(result.absorption.high_asp_tasks),
            "low_asp_tasks": sorted(result.absorption.low_asp_tasks),
            "prior_art": {
                key: value.value for key, value in result.absorption.prior_art.items()
            },
        },
        "strongest_version": result.strongest_version,
        "weakest_point": result.weakest_point,
        "verdict": result.verdict,
        "recommendation": result.recommendation,
        "claim_impact": result.claim_impact,
    }


def _restriction_to_dict(audit: RestrictionAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "closure_holds": audit.closure_holds,
        "violations": list(audit.violations),
        "asp_by_patch": {
            patch: sorted(values) for patch, values in audit.asp_by_patch.items()
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t120_result_to_dict(run_t120_analysis()), indent=2))
