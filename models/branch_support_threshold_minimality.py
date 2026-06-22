"""T180: branch-support threshold minimality screen.

T179 preserved a useful formal residue from H7's demotion: at fixed absorber
accounting, record topology can matter for future capability. The tempting next
guess was that exact ``branch_support`` is the minimal topology coordinate for
the surviving branch-failure task.

This module tries to break that guess. For the declared task
``survive_one_branch_failure`` it tests whether capability already factors
through the weaker threshold predicate ``branch_support >= 2``.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.physical_record_deletion_fixed_accounting import (
    AbsorberVector,
    one_bit_blind_reset_vector,
)


@dataclass(frozen=True)
class TopologyProfile:
    profile_id: str
    holder_count: int
    causal_chain_count: int
    branch_support: int
    provenance_valid: bool
    interpretation: str


@dataclass(frozen=True)
class ProjectionAudit:
    projection_name: str
    factors_through_capability: bool
    value_count: int
    witness_pair: tuple[str, str] | None
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T180Result:
    absorber_vector: AbsorberVector
    future_task: str
    profiles: tuple[TopologyProfile, ...]
    audits: tuple[ProjectionAudit, ...]
    exact_branch_support_nonminimal: bool
    threshold_projection_name: str
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def topology_family() -> tuple[TopologyProfile, ...]:
    return (
        TopologyProfile(
            profile_id="single_branch_triplicate",
            holder_count=3,
            causal_chain_count=3,
            branch_support=1,
            provenance_valid=True,
            interpretation=(
                "Three holders and three causal chains still collapse to one "
                "surviving branch root after a branch failure."
            ),
        ),
        TopologyProfile(
            profile_id="dual_branch_triplicate",
            holder_count=3,
            causal_chain_count=3,
            branch_support=2,
            provenance_valid=True,
            interpretation=(
                "Three holders are spread across two independent surviving "
                "branch roots."
            ),
        ),
        TopologyProfile(
            profile_id="triple_branch_triplicate",
            holder_count=3,
            causal_chain_count=3,
            branch_support=3,
            provenance_valid=True,
            interpretation=(
                "Three holders are spread across three independent surviving "
                "branch roots."
            ),
        ),
        TopologyProfile(
            profile_id="dual_chain_single_branch",
            holder_count=2,
            causal_chain_count=2,
            branch_support=1,
            provenance_valid=True,
            interpretation=(
                "Two causal chains can still live on the same branch root, so "
                "chain count alone does not guarantee failure robustness."
            ),
        ),
        TopologyProfile(
            profile_id="dual_chain_two_branch",
            holder_count=2,
            causal_chain_count=2,
            branch_support=2,
            provenance_valid=True,
            interpretation=(
                "Two causal chains can also occupy two independent branch "
                "roots, restoring one-failure survival."
            ),
        ),
    )


def survive_one_branch_failure(profile: TopologyProfile) -> bool:
    return profile.provenance_valid and profile.branch_support >= 2


def exact_branch_support(profile: TopologyProfile) -> int:
    return profile.branch_support


def backup_branch_threshold(profile: TopologyProfile) -> bool:
    return profile.branch_support >= 2


def holder_count_only(profile: TopologyProfile) -> int:
    return profile.holder_count


def causal_chain_count_only(profile: TopologyProfile) -> int:
    return profile.causal_chain_count


def provenance_only(profile: TopologyProfile) -> bool:
    return profile.provenance_valid


def nonsupport_topology_signature(profile: TopologyProfile) -> tuple[int, int, bool]:
    return (
        profile.holder_count,
        profile.causal_chain_count,
        profile.provenance_valid,
    )


def audit_projection(
    *,
    projection_name: str,
    profiles: tuple[TopologyProfile, ...],
    projection,
) -> ProjectionAudit:
    witness_pair = _first_nonfactorization_witness(profiles, projection)
    factors = witness_pair is None
    values = {projection(profile) for profile in profiles}

    if factors:
        verdict = "factors_through_capability"
        interpretation = (
            f"{projection_name} determines the declared future task on the "
            "current admissible family."
        )
    else:
        verdict = "does_not_factor_through_capability"
        interpretation = (
            f"{projection_name} is insufficient: the witness pair "
            f"{witness_pair[0]} vs {witness_pair[1]} agrees on the projection "
            "but disagrees on future capability."
        )

    return ProjectionAudit(
        projection_name=projection_name,
        factors_through_capability=factors,
        value_count=len(values),
        witness_pair=witness_pair,
        verdict=verdict,
        interpretation=interpretation,
    )


def run_t180_analysis() -> T180Result:
    profiles = topology_family()
    audits = (
        audit_projection(
            projection_name="exact_branch_support",
            profiles=profiles,
            projection=exact_branch_support,
        ),
        audit_projection(
            projection_name="backup_branch_threshold",
            profiles=profiles,
            projection=backup_branch_threshold,
        ),
        audit_projection(
            projection_name="holder_count_only",
            profiles=profiles,
            projection=holder_count_only,
        ),
        audit_projection(
            projection_name="causal_chain_count_only",
            profiles=profiles,
            projection=causal_chain_count_only,
        ),
        audit_projection(
            projection_name="provenance_only",
            profiles=profiles,
            projection=provenance_only,
        ),
        audit_projection(
            projection_name="nonsupport_topology_signature",
            profiles=profiles,
            projection=nonsupport_topology_signature,
        ),
    )
    audit_by_name = {audit.projection_name: audit for audit in audits}
    exact_audit = audit_by_name["exact_branch_support"]
    threshold_audit = audit_by_name["backup_branch_threshold"]

    exact_nonminimal = (
        exact_audit.factors_through_capability
        and threshold_audit.factors_through_capability
        and threshold_audit.value_count < exact_audit.value_count
    )

    return T180Result(
        absorber_vector=one_bit_blind_reset_vector(),
        future_task="survive_one_branch_failure",
        profiles=profiles,
        audits=audits,
        exact_branch_support_nonminimal=exact_nonminimal,
        threshold_projection_name="backup_branch_threshold",
        strongest_claim=(
            "For the current fixed-accounting branch-failure family, exact "
            "branch_support is not the minimal topology coordinate for the "
            "task survive_one_branch_failure. Capability already factors "
            "through the weaker threshold predicate backup_branch_threshold := "
            "[branch_support >= 2]."
        ),
        improved=(
            "T180 sharpens T179's positive residue instead of inflating it. "
            "The surviving object is now task-relative and smaller: one-backup "
            "branch availability, not exact branch count."
        ),
        weakened=(
            "This weakens the stronger T179 guess that exact numeric "
            "branch_support is the minimal coordinate for the current "
            "branch-failure task. Profiles with branch_support 2 and 3 remain "
            "capability-equivalent in the tested family."
        ),
        falsification_condition=(
            "The threshold claim fails if an admissible fixed-accounting "
            "profile pair with the same backup-branch threshold but different "
            "survive_one_branch_failure capability is found, or if the task is "
            "changed so that exact branch multiplicity beyond the threshold "
            "becomes operationally relevant."
        ),
        claim_ledger_update=(
            "Add T180 to H7/T179: for the current fixed-accounting "
            "branch-failure survivor, exact branch_support is not the minimal "
            "future-capability coordinate. The current task factors through the "
            "coarser threshold backup_branch_threshold = [branch_support >= 2], "
            "while non-support topology signatures fail."
        ),
        open_blocker=(
            "No theorem yet characterizes the full task family where threshold "
            "predicates branch_support >= k+1 are necessary and sufficient, or "
            "when richer topology data beyond thresholds becomes genuinely "
            "load-bearing under matched accounting."
        ),
        suggested_next=(
            "Generalize or kill the pattern: test whether survive_k_branch_"
            "failures factors through branch_support >= k+1, and identify the "
            "first natural task that needs richer topology than a threshold."
        ),
    )


def _first_nonfactorization_witness(
    profiles: tuple[TopologyProfile, ...], projection
) -> tuple[str, str] | None:
    for left_index, left in enumerate(profiles):
        left_value = projection(left)
        left_capability = survive_one_branch_failure(left)
        for right in profiles[left_index + 1 :]:
            if projection(right) != left_value:
                continue
            if survive_one_branch_failure(right) != left_capability:
                return (left.profile_id, right.profile_id)
    return None


def t180_result_to_dict(result: T180Result) -> dict[str, object]:
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
        "future_task": result.future_task,
        "profiles": [
            {
                "profile_id": profile.profile_id,
                "holder_count": profile.holder_count,
                "causal_chain_count": profile.causal_chain_count,
                "branch_support": profile.branch_support,
                "provenance_valid": profile.provenance_valid,
                "future_capability": survive_one_branch_failure(profile),
                "interpretation": profile.interpretation,
            }
            for profile in result.profiles
        ],
        "audits": [
            {
                "projection_name": audit.projection_name,
                "factors_through_capability": audit.factors_through_capability,
                "value_count": audit.value_count,
                "witness_pair": list(audit.witness_pair) if audit.witness_pair else None,
                "verdict": audit.verdict,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "exact_branch_support_nonminimal": result.exact_branch_support_nonminimal,
        "threshold_projection_name": result.threshold_projection_name,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t180_result_to_dict(run_t180_analysis()), indent=2))
