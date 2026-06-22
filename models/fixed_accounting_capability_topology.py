"""T179: fixed-accounting capability topology residue.

T145 found one survivor after thermodynamic absorber matching: branch topology
can change a future operation while free-energy, capacity, sink, boundary,
provenance, source-copy, and reversible-control data are held fixed. This
module turns that survivor into a narrow theorem target without promoting it
to H7 arrow evidence.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

from models.physical_record_deletion_fixed_accounting import (
    AbsorberVector,
    one_bit_blind_reset_vector,
)


@dataclass(frozen=True)
class TopologyProfile:
    holder_count: int
    causal_chain_count: int
    branch_support: int
    provenance_valid: bool


@dataclass(frozen=True)
class CapabilityCase:
    case_id: str
    left_profile: TopologyProfile
    right_profile: TopologyProfile
    left_absorber: AbsorberVector
    right_absorber: AbsorberVector
    reverse_edge_class: str
    reverse_status: str
    future_task: str
    left_task_available: bool
    right_task_available: bool
    interpretation: str


@dataclass(frozen=True)
class CapabilityTopologyAudit:
    case_id: str
    absorber_vector_matched: bool
    absorber_mismatch_fields: tuple[str, ...]
    topology_profile_split: bool
    future_task: str
    future_capability_split: bool
    reverse_edge_class: str
    reverse_status: str
    fixed_accounting_capability_residue: bool
    h7_physical_arrow_candidate: bool
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T179Result:
    audits: tuple[CapabilityTopologyAudit, ...]
    residue_cases: tuple[str, ...]
    h7_candidates: tuple[str, ...]
    theorem_candidate: str
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def case_family() -> tuple[CapabilityCase, ...]:
    one_bit = one_bit_blind_reset_vector()
    two_bit = AbsorberVector(
        erased_bits=2,
        beta_work_floor=2 * one_bit.beta_work_floor,
        blank_capacity_delta=2,
        sink_delta=0,
        boundary_access="matched_observer_boundary",
        provenance_state="matched_valid_provenance",
        reversible_control="blind_reset_only",
        source_copy_state="authoritative_source_remains",
    )

    same_chain = TopologyProfile(
        holder_count=2,
        causal_chain_count=1,
        branch_support=1,
        provenance_valid=True,
    )
    branch_spread = TopologyProfile(
        holder_count=2,
        causal_chain_count=2,
        branch_support=2,
        provenance_valid=True,
    )
    provenance_loss = TopologyProfile(
        holder_count=2,
        causal_chain_count=2,
        branch_support=2,
        provenance_valid=False,
    )

    return (
        CapabilityCase(
            case_id="same_accounting_branch_survival_split",
            left_profile=same_chain,
            right_profile=branch_spread,
            left_absorber=one_bit,
            right_absorber=one_bit,
            reverse_edge_class="physical_record_deletion",
            reverse_status="ordinary_erasure_accounted",
            future_task="survive_one_branch_failure",
            left_task_available=False,
            right_task_available=True,
            interpretation=(
                "Branch support changes a future survival task while the "
                "thermodynamic and control accounting vector is fixed."
            ),
        ),
        CapabilityCase(
            case_id="same_accounting_same_topology_control",
            left_profile=same_chain,
            right_profile=same_chain,
            left_absorber=one_bit,
            right_absorber=one_bit,
            reverse_edge_class="physical_record_deletion",
            reverse_status="ordinary_erasure_accounted",
            future_task="survive_one_branch_failure",
            left_task_available=False,
            right_task_available=False,
            interpretation=(
                "Holding both accounting and topology fixed removes the "
                "future-operation split."
            ),
        ),
        CapabilityCase(
            case_id="changed_erasure_floor_absorber_control",
            left_profile=same_chain,
            right_profile=branch_spread,
            left_absorber=one_bit,
            right_absorber=two_bit,
            reverse_edge_class="physical_record_deletion",
            reverse_status="absorbed_by_erasure_cost",
            future_task="pay_same_blind_reset_floor",
            left_task_available=True,
            right_task_available=False,
            interpretation=(
                "A task split with changed erased bits is thermodynamic "
                "accounting, not fixed-accounting topology residue."
            ),
        ),
        CapabilityCase(
            case_id="provenance_loss_non_deletion_control",
            left_profile=branch_spread,
            right_profile=provenance_loss,
            left_absorber=one_bit,
            right_absorber=one_bit,
            reverse_edge_class="authority_or_provenance_loss",
            reverse_status="governance_not_thermodynamic",
            future_task="use_record_for_claim_review",
            left_task_available=True,
            right_task_available=False,
            interpretation=(
                "The future task changes, but the reverse edge is provenance "
                "loss rather than physical record deletion."
            ),
        ),
        CapabilityCase(
            case_id="constructor_impossible_positive_control",
            left_profile=same_chain,
            right_profile=branch_spread,
            left_absorber=one_bit,
            right_absorber=one_bit,
            reverse_edge_class="physical_record_deletion",
            reverse_status="constructor_impossible_after_full_accounting",
            future_task="survive_one_branch_failure",
            left_task_available=False,
            right_task_available=True,
            interpretation=(
                "This is a synthetic positive control for the stricter H7 "
                "reinstatement gate; no current substrate supplies it."
            ),
        ),
    )


def audit_case(case: CapabilityCase) -> CapabilityTopologyAudit:
    mismatches = absorber_mismatch_fields(case.left_absorber, case.right_absorber)
    absorber_matched = not mismatches
    topology_split = case.left_profile != case.right_profile
    capability_split = case.left_task_available != case.right_task_available
    h7_candidate = is_h7_physical_arrow_candidate(
        absorber_vector_matched=absorber_matched,
        topology_profile_split=topology_split,
        future_capability_split=capability_split,
        reverse_edge_class=case.reverse_edge_class,
        reverse_status=case.reverse_status,
    )
    residue = is_fixed_accounting_capability_residue(
        absorber_vector_matched=absorber_matched,
        topology_profile_split=topology_split,
        future_capability_split=capability_split,
        reverse_edge_class=case.reverse_edge_class,
        reverse_status=case.reverse_status,
    )

    return CapabilityTopologyAudit(
        case_id=case.case_id,
        absorber_vector_matched=absorber_matched,
        absorber_mismatch_fields=mismatches,
        topology_profile_split=topology_split,
        future_task=case.future_task,
        future_capability_split=capability_split,
        reverse_edge_class=case.reverse_edge_class,
        reverse_status=case.reverse_status,
        fixed_accounting_capability_residue=residue,
        h7_physical_arrow_candidate=h7_candidate,
        verdict=_verdict(case, mismatches, residue, h7_candidate),
        interpretation=case.interpretation,
    )


def absorber_mismatch_fields(
    left: AbsorberVector, right: AbsorberVector
) -> tuple[str, ...]:
    left_values = asdict(left)
    right_values = asdict(right)
    return tuple(
        field for field, value in left_values.items() if value != right_values[field]
    )


def is_fixed_accounting_capability_residue(
    *,
    absorber_vector_matched: bool,
    topology_profile_split: bool,
    future_capability_split: bool,
    reverse_edge_class: str,
    reverse_status: str,
) -> bool:
    return (
        absorber_vector_matched
        and topology_profile_split
        and future_capability_split
        and reverse_edge_class == "physical_record_deletion"
        and reverse_status != "constructor_impossible_after_full_accounting"
    )


def is_h7_physical_arrow_candidate(
    *,
    absorber_vector_matched: bool,
    topology_profile_split: bool,
    future_capability_split: bool,
    reverse_edge_class: str,
    reverse_status: str,
) -> bool:
    return (
        absorber_vector_matched
        and topology_profile_split
        and future_capability_split
        and reverse_edge_class == "physical_record_deletion"
        and reverse_status == "constructor_impossible_after_full_accounting"
    )


def run_t179_analysis() -> T179Result:
    audits = tuple(audit_case(case) for case in case_family())
    residue_cases = tuple(
        audit.case_id for audit in audits if audit.fixed_accounting_capability_residue
    )
    h7_candidates = tuple(
        audit.case_id for audit in audits if audit.h7_physical_arrow_candidate
    )

    return T179Result(
        audits=audits,
        residue_cases=residue_cases,
        h7_candidates=h7_candidates,
        theorem_candidate=(
            "For a fixed absorber vector A and a fixed future task F, a "
            "record-topology profile tau carries fixed-accounting capability "
            "residue exactly when two admissible states have the same A, "
            "different tau, and different F-availability. This residue is H7 "
            "physical-arrow evidence only under the stricter added condition "
            "that the reverse edge is physical_record_deletion with status "
            "constructor_impossible_after_full_accounting."
        ),
        strongest_claim=(
            "The T145 survivor is not a thermodynamic arrow, but it is a "
            "legitimate capability-kernel target: branch topology can matter "
            "for a future operation even when ordinary deletion accounting is "
            "matched. The useful next theorem is about minimal topology data "
            "needed for future capability, not about time's arrow."
        ),
        improved=(
            "T179 preserves the negative H7 verdict while extracting a precise "
            "positive object from it: fixed-accounting capability topology. "
            "It separates three gates that were easy to blur: absorber "
            "matching, future-capability split, and constructor-impossible "
            "physical deletion."
        ),
        weakened=(
            "This weakens any attempt to cite the T145 branch-topology split "
            "as physical-arrow evidence. The same finite pattern becomes "
            "formal capability residue unless the stricter reverse-status "
            "gate is cleared."
        ),
        falsification_condition=(
            "The theorem target fails if fixed absorber vector plus topology "
            "profile is insufficient to determine the declared future task, "
            "or if a mature absorber shows that the topology profile is just "
            "a disguised thermodynamic, boundary, provenance, or control "
            "variable under the same comparison."
        ),
        claim_ledger_update=(
            "Add T179 to H7/T129: the T145 fixed-accounting branch-topology "
            "split should be preserved as capability/topology residue and "
            "formalized as a minimal future-capability kernel target, while "
            "remaining explicitly non-evidence for H7 physical-arrow promotion."
        ),
        open_blocker=(
            "No minimality theorem yet proves which record-topology fields "
            "are necessary and sufficient for a class of future tasks under "
            "matched thermodynamic and control accounting."
        ),
        suggested_next=(
            "Prove or refute the finite minimality theorem: for branch-failure "
            "tasks, branch_support is the minimal topology coordinate that "
            "restores capability sufficiency at fixed absorber vector."
        ),
    )


def _verdict(
    case: CapabilityCase,
    mismatches: tuple[str, ...],
    residue: bool,
    h7_candidate: bool,
) -> str:
    if h7_candidate:
        return "synthetic_h7_reinstatement_positive_control"
    if residue:
        return "fixed_accounting_capability_topology_residue"
    if case.reverse_edge_class != "physical_record_deletion":
        return "non_deletion_capability_split"
    if mismatches:
        return "absorber_owned_capability_split"
    return "no_capability_residue"


def t179_result_to_dict(result: T179Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "case_id": audit.case_id,
                "absorber_vector_matched": audit.absorber_vector_matched,
                "absorber_mismatch_fields": list(audit.absorber_mismatch_fields),
                "topology_profile_split": audit.topology_profile_split,
                "future_task": audit.future_task,
                "future_capability_split": audit.future_capability_split,
                "reverse_edge_class": audit.reverse_edge_class,
                "reverse_status": audit.reverse_status,
                "fixed_accounting_capability_residue": (
                    audit.fixed_accounting_capability_residue
                ),
                "h7_physical_arrow_candidate": audit.h7_physical_arrow_candidate,
                "verdict": audit.verdict,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "residue_cases": list(result.residue_cases),
        "h7_candidates": list(result.h7_candidates),
        "theorem_candidate": result.theorem_candidate,
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

    print(json.dumps(t179_result_to_dict(run_t179_analysis()), indent=2))
