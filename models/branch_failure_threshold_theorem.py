"""T181: branch-failure threshold theorem and boundary screen.

T180 showed that exact branch count was too strong for the fixed task
``survive_one_branch_failure``. This module generalizes the narrow survivor:
for unnamed branch-failure tasks, only a support threshold is needed. It also
finds the first natural boundary where thresholds stop being sufficient:
named or correlated branch hazards.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from models.physical_record_deletion_fixed_accounting import (
    AbsorberVector,
    one_bit_blind_reset_vector,
)


BRANCH_IDS = ("A", "B", "C", "D")


@dataclass(frozen=True)
class BranchTopology:
    profile_id: str
    support_branches: frozenset[str]
    provenance_valid: bool
    interpretation: str

    @property
    def branch_support(self) -> int:
        return len(self.support_branches)


@dataclass(frozen=True)
class ProjectionAudit:
    task_name: str
    projection_name: str
    factors_through_capability: bool
    projection_value_count: int
    capability_value_count: int
    witness_pair: tuple[str, str] | None
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T181Result:
    absorber_vector: AbsorberVector
    admissible_profile_count: int
    branch_ids: tuple[str, ...]
    threshold_audits: tuple[ProjectionAudit, ...]
    boundary_audits: tuple[ProjectionAudit, ...]
    theorem_candidate: str
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def topology_family(
    branch_ids: tuple[str, ...] = BRANCH_IDS,
) -> tuple[BranchTopology, ...]:
    profiles: list[BranchTopology] = []
    for size in range(1, len(branch_ids) + 1):
        for support in combinations(branch_ids, size):
            label = "".join(support)
            profiles.append(
                BranchTopology(
                    profile_id=f"support_{label}",
                    support_branches=frozenset(support),
                    provenance_valid=True,
                    interpretation=(
                        "Valid-provenance fixed-accounting record support on "
                        f"branches {label}."
                    ),
                )
            )
    return tuple(profiles)


def branch_support_count(profile: BranchTopology) -> int:
    return profile.branch_support


def support_set(profile: BranchTopology) -> frozenset[str]:
    return profile.support_branches


def survive_k_branch_failures(profile: BranchTopology, k: int) -> bool:
    return profile.provenance_valid and profile.branch_support >= k + 1


def support_threshold(profile: BranchTopology, k: int) -> bool:
    return profile.branch_support >= k + 1


def max_tolerated_branch_failures(profile: BranchTopology) -> int:
    if not profile.provenance_valid:
        return -1
    return profile.branch_support - 1


def survive_named_outage(
    profile: BranchTopology, failed_branches: frozenset[str]
) -> bool:
    return profile.provenance_valid and bool(profile.support_branches - failed_branches)


def audit_projection(
    *,
    task_name: str,
    projection_name: str,
    profiles: tuple[BranchTopology, ...],
    projection,
    capability,
) -> ProjectionAudit:
    witness_pair = _first_nonfactorization_witness(profiles, projection, capability)
    projection_values = {projection(profile) for profile in profiles}
    capability_values = {capability(profile) for profile in profiles}
    factors = witness_pair is None

    if factors:
        verdict = "factors_through_capability"
        interpretation = (
            f"{projection_name} determines {task_name} on the current "
            "valid-provenance fixed-accounting family."
        )
    else:
        verdict = "does_not_factor_through_capability"
        interpretation = (
            f"{projection_name} is insufficient for {task_name}: "
            f"{witness_pair[0]} and {witness_pair[1]} agree on the projection "
            "but disagree on capability."
        )

    return ProjectionAudit(
        task_name=task_name,
        projection_name=projection_name,
        factors_through_capability=factors,
        projection_value_count=len(projection_values),
        capability_value_count=len(capability_values),
        witness_pair=witness_pair,
        verdict=verdict,
        interpretation=interpretation,
    )


def run_t181_analysis() -> T181Result:
    profiles = topology_family()
    threshold_audits = tuple(
        audit_projection(
            task_name=f"survive_{k}_branch_failures",
            projection_name=f"support_threshold_ge_{k + 1}",
            profiles=profiles,
            projection=lambda profile, threshold=k: support_threshold(
                profile, threshold
            ),
            capability=lambda profile, failures=k: survive_k_branch_failures(
                profile, failures
            ),
        )
        for k in range(len(BRANCH_IDS))
    )

    boundary_audits = (
        audit_projection(
            task_name="survive_one_branch_failure",
            projection_name="exact_branch_support_count",
            profiles=profiles,
            projection=branch_support_count,
            capability=lambda profile: survive_k_branch_failures(profile, 1),
        ),
        audit_projection(
            task_name="max_tolerated_branch_failures",
            projection_name="support_threshold_ge_2",
            profiles=profiles,
            projection=lambda profile: support_threshold(profile, 1),
            capability=max_tolerated_branch_failures,
        ),
        audit_projection(
            task_name="max_tolerated_branch_failures",
            projection_name="exact_branch_support_count",
            profiles=profiles,
            projection=branch_support_count,
            capability=max_tolerated_branch_failures,
        ),
        audit_projection(
            task_name="survive_named_outage_A_C",
            projection_name="exact_branch_support_count",
            profiles=profiles,
            projection=branch_support_count,
            capability=lambda profile: survive_named_outage(
                profile, frozenset({"A", "C"})
            ),
        ),
        audit_projection(
            task_name="survive_named_outage_A_C",
            projection_name="support_branch_identity_set",
            profiles=profiles,
            projection=support_set,
            capability=lambda profile: survive_named_outage(
                profile, frozenset({"A", "C"})
            ),
        ),
    )

    return T181Result(
        absorber_vector=one_bit_blind_reset_vector(),
        admissible_profile_count=len(profiles),
        branch_ids=BRANCH_IDS,
        threshold_audits=threshold_audits,
        boundary_audits=boundary_audits,
        theorem_candidate=(
            "For a valid-provenance fixed-accounting record family whose "
            "future task is survival after any unnamed set of at most k branch "
            "failures, capability factors through the threshold predicate "
            "branch_support >= k + 1. Exact branch count is unnecessary for "
            "each fixed k. Exact count becomes load-bearing for the variable "
            "margin task max_tolerated_branch_failures, and branch identity "
            "becomes load-bearing for named or correlated outage tasks."
        ),
        strongest_claim=(
            "The T179/T180 topology residue is narrower than exact branch "
            "multiplicity. For fixed unnamed k-failure survival, the earned "
            "coordinate is the threshold branch_support >= k + 1. Richer "
            "topology is justified only when the future task asks for a "
            "failure margin or names which branches can fail."
        ),
        improved=(
            "T181 turns the open T180 blocker into a finite theorem screen and "
            "adds the first boundary case. It separates threshold sufficiency, "
            "count-valued margin capability, and support-identity capability "
            "instead of treating all topology as one coordinate."
        ),
        weakened=(
            "This further weakens any claim that exact branch multiplicity is "
            "the generic fixed-accounting residue for branch-failure survival. "
            "Exact count is over-specified for every fixed unnamed k tested "
            "here, and branch identity, not count, is the next richer datum for "
            "named hazards."
        ),
        falsification_condition=(
            "The threshold theorem fails if a valid-provenance fixed-accounting "
            "profile pair has the same branch_support >= k + 1 value but "
            "different survival under the declared unnamed k-failure task. The "
            "boundary classification fails if named or correlated hazards can "
            "be reduced to count thresholds under the same admissible family "
            "and task semantics."
        ),
        claim_ledger_update=(
            "Add T181 after T180: for unnamed branch-failure tasks, "
            "branch_support >= k + 1 is sufficient for each fixed k and exact "
            "branch count is nonminimal. Exact count is needed for a margin "
            "capability, while support identity is needed for named/correlated "
            "hazard tasks. This remains fixed-accounting capability residue, "
            "not H7 physical-arrow evidence."
        ),
        open_blocker=(
            "No physically grounded hazard model yet tells which branch "
            "identities are substrate-natural rather than labels, or how these "
            "finite support predicates should be transported into a smooth or "
            "quantum record setting without smuggling in the capability object."
        ),
        suggested_next=(
            "Either attach the branch-identity boundary to a real detector or "
            "memory architecture, or prove a minimal-enrichment statement for "
            "hazard partitions: count thresholds for exchangeable hazards, "
            "support intersections for named hazards, and no H7 upgrade unless "
            "deletion remains constructor-impossible after full accounting."
        ),
    )


def _first_nonfactorization_witness(
    profiles: tuple[BranchTopology, ...], projection, capability
) -> tuple[str, str] | None:
    for left_index, left in enumerate(profiles):
        left_projection = projection(left)
        left_capability = capability(left)
        for right in profiles[left_index + 1 :]:
            if projection(right) != left_projection:
                continue
            if capability(right) != left_capability:
                return (left.profile_id, right.profile_id)
    return None


def t181_result_to_dict(result: T181Result) -> dict[str, object]:
    return {
        "absorber_vector": {
            "erased_bits": result.absorber_vector.erased_bits,
            "beta_work_floor": result.absorber_vector.beta_work_floor,
            "blank_capacity_delta": result.absorber_vector.blank_capacity_delta,
            "sink_delta": result.absorber_vector.sink_delta,
            "boundary_access": result.absorber_vector.boundary_access,
            "provenance_state": result.absorber_vector.provenance_state,
            "reversible_control": result.absorber_vector.reversible_control,
            "source_copy_state": result.absorber_vector.source_copy_state,
        },
        "admissible_profile_count": result.admissible_profile_count,
        "branch_ids": list(result.branch_ids),
        "threshold_audits": [_audit_to_dict(audit) for audit in result.threshold_audits],
        "boundary_audits": [_audit_to_dict(audit) for audit in result.boundary_audits],
        "theorem_candidate": result.theorem_candidate,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


def _audit_to_dict(audit: ProjectionAudit) -> dict[str, object]:
    return {
        "task_name": audit.task_name,
        "projection_name": audit.projection_name,
        "factors_through_capability": audit.factors_through_capability,
        "projection_value_count": audit.projection_value_count,
        "capability_value_count": audit.capability_value_count,
        "witness_pair": list(audit.witness_pair) if audit.witness_pair else None,
        "verdict": audit.verdict,
        "interpretation": audit.interpretation,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t181_result_to_dict(run_t181_analysis()), indent=2))
