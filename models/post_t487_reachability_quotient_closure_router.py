"""T488: post-T487 reachability-quotient closure router.

T485 admitted a stable reachability quotient over original observer sites.
T487 then showed that this quotient determines only declared reachability-task
capabilities and leaves path-latency, relay-budget, and component-size
capabilities underdetermined.

This router closes the current T479-T487 RG/multiscale reachability-quotient
thread against minor restarts while admitting only genuinely new future review
targets. It does not move claim status, public posture, North Star, roadmap,
physics posture, scale, clock, duration, finality, or cross-repo truth.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T488-post-t487-reachability-quotient-closure-router-v0.1"
T487_ARTIFACT_ID = "T487-reachability-quotient-capability-spread-gate-v0.1"
VERDICT = "POST_T487_REACHABILITY_QUOTIENT_THREAD_CLOSED_NEW_EVIDENCE_ONLY"


@dataclass(frozen=True)
class ClosureProposal:
    """A proposed post-T487 restart or future review packet."""

    proposal_id: str
    proposal_kind: str
    repeats_current_t485_t487_packet_class: bool
    cites_t487_anchor: bool
    declares_capability_object: bool
    computes_capability_spread: bool
    supplies_positive_controls: bool
    supplies_hostile_controls: bool
    independent_of_t485_t487_quotient: bool
    has_domain_native_morphism_class: bool = False
    has_direct_record_finality_bridge_theorem: bool = False
    uses_t487_reachability_sufficiency_as_proof: bool = False
    uses_role_profile_as_scale_structure: bool = False
    uses_non_singleton_spread_as_determined: bool = False
    uses_path_latency_or_relay_artifact: bool = False
    uses_component_size_artifact: bool = False
    imports_rg_or_conformal_mechanism: bool = False
    claims_scale_clock_duration_finality_or_physics: bool = False
    requests_claim_or_posture_movement: bool = False
    intended_use: str = ""


@dataclass(frozen=True)
class ClosureDecision:
    """Router decision for a post-T487 proposal."""

    proposal_id: str
    admitted: bool
    route_label: str
    classification: str
    admitted_as_future_review_target: bool
    counts_as_thread_evidence: bool
    closes_current_thread: bool
    missing_requirements: tuple[str, ...]
    notes: tuple[str, ...]


@dataclass(frozen=True)
class T488Result:
    """Complete T488 closure-router result."""

    t487_anchor: dict[str, Any]
    proposals: tuple[ClosureProposal, ...]
    decisions: tuple[ClosureDecision, ...]
    verdict: str
    claim_ledger_update: str
    current_thread_closed: bool
    admitted_future_targets: tuple[str, ...]
    rejected_restart_packets: tuple[str, ...]
    strongest_reading: str
    future_reopen_minimum: tuple[str, ...]
    not_earned: tuple[str, ...]


def run_t488_analysis() -> T488Result:
    """Run the post-T487 reachability-quotient closure router."""

    t487 = _load_t487_result()
    anchor = _t487_anchor_checks(t487)
    proposals = _closure_proposals()
    decisions = tuple(_evaluate_proposal(proposal, anchor) for proposal in proposals)
    admitted_future_targets = tuple(
        decision.proposal_id
        for decision in decisions
        if decision.admitted_as_future_review_target
    )
    rejected_restart_packets = tuple(
        decision.proposal_id for decision in decisions if not decision.admitted
    )
    current_thread_closed = (
        anchor["anchor_ok"]
        and all(
            decision.closes_current_thread
            for decision in decisions
            if _proposal_by_id(proposals, decision.proposal_id)
            .repeats_current_t485_t487_packet_class
        )
        and not any(decision.counts_as_thread_evidence for decision in decisions)
    )

    return T488Result(
        t487_anchor=anchor,
        proposals=proposals,
        decisions=decisions,
        verdict=VERDICT,
        claim_ledger_update="none",
        current_thread_closed=current_thread_closed,
        admitted_future_targets=admitted_future_targets,
        rejected_restart_packets=rejected_restart_packets,
        strongest_reading=(
            "T488 closes the current T479-T487 RG/multiscale "
            "reachability-quotient thread to minor restarts. T487 provides "
            "reachability-task sufficiency only. It is not internal scale "
            "structure, not a record clock, not duration, not finality, not "
            "scale genesis, not physics evidence, and not claim or public "
            "posture support. Future work can reopen the surface only by "
            "bringing a newly declared independent capability object with "
            "capability-spread controls, a domain-native morphism class that "
            "changes the invariance burden, or a direct record-finality bridge "
            "theorem with hostile controls."
        ),
        future_reopen_minimum=(
            "cite T479-T487 and state why the reachability-quotient closure is insufficient",
            "declare the capability object before witness construction",
            "compute capability spread over the declared visible fibers",
            "preserve positive reachability controls and hostile path, relay, component-size, finality, RG/conformal, and promotion controls",
            "supply evidence independent of the T485/T487 quotient when claiming a new generator",
            "declare a domain-native morphism class before reusing topology as an invariant",
            "provide a direct record-finality bridge theorem before using finality language",
            "keep scale, clock, duration, temporal-arrow, RG/conformal, physics, claim-ledger, roadmap, North Star, public-posture, and cross-repo readings blocked unless separately earned",
        ),
        not_earned=(
            "independent internal scale structure",
            "record clock",
            "duration or temporal arrow",
            "record-finality change",
            "scale-genesis theorem",
            "physics or conformal-gravity claim",
            "D1 promotion",
            "RG/TaF equivalence theorem",
            "claim-ledger movement",
            "roadmap movement",
            "README movement",
            "North Star movement",
            "public-posture movement",
            "cross-repo truth movement",
        ),
    )


def run() -> dict[str, Any]:
    """Return a serializable T488 result."""

    return t488_result_to_dict(run_t488_analysis())


def _closure_proposals() -> tuple[ClosureProposal, ...]:
    return (
        ClosureProposal(
            proposal_id="repeat_reachability_quotient_upgrade",
            proposal_kind="minor_restart",
            repeats_current_t485_t487_packet_class=True,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=False,
            uses_t487_reachability_sufficiency_as_proof=True,
            claims_scale_clock_duration_finality_or_physics=True,
            intended_use="upgrade the admitted reachability task into stronger structure",
        ),
        ClosureProposal(
            proposal_id="role_profile_internal_scale_restart",
            proposal_kind="minor_restart",
            repeats_current_t485_t487_packet_class=True,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=False,
            uses_role_profile_as_scale_structure=True,
            claims_scale_clock_duration_finality_or_physics=True,
            intended_use="treat the quotient role profile as internal scale structure",
        ),
        ClosureProposal(
            proposal_id="path_latency_relabel_restart",
            proposal_kind="refinement_artifact_restart",
            repeats_current_t485_t487_packet_class=True,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=False,
            uses_non_singleton_spread_as_determined=True,
            uses_path_latency_or_relay_artifact=True,
            claims_scale_clock_duration_finality_or_physics=True,
            intended_use="read path-latency bands as determined by the quotient",
        ),
        ClosureProposal(
            proposal_id="relay_budget_clock_restart",
            proposal_kind="refinement_artifact_restart",
            repeats_current_t485_t487_packet_class=True,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=False,
            uses_non_singleton_spread_as_determined=True,
            uses_path_latency_or_relay_artifact=True,
            claims_scale_clock_duration_finality_or_physics=True,
            intended_use="read relay count as a clock or duration proxy",
        ),
        ClosureProposal(
            proposal_id="component_size_capacity_restart",
            proposal_kind="refinement_artifact_restart",
            repeats_current_t485_t487_packet_class=True,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=False,
            uses_non_singleton_spread_as_determined=True,
            uses_component_size_artifact=True,
            claims_scale_clock_duration_finality_or_physics=True,
            intended_use="read component-size capacity as determined by the quotient",
        ),
        ClosureProposal(
            proposal_id="record_finality_bridge_shortcut",
            proposal_kind="finality_shortcut",
            repeats_current_t485_t487_packet_class=True,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=False,
            uses_t487_reachability_sufficiency_as_proof=True,
            claims_scale_clock_duration_finality_or_physics=True,
            intended_use="treat reachability sufficiency as record-finality evidence",
        ),
        ClosureProposal(
            proposal_id="rg_conformal_import_restart",
            proposal_kind="external_mechanism_restart",
            repeats_current_t485_t487_packet_class=True,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=False,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            independent_of_t485_t487_quotient=False,
            imports_rg_or_conformal_mechanism=True,
            claims_scale_clock_duration_finality_or_physics=True,
            intended_use="import RG or conformal fixed-point mechanism into the quotient lane",
        ),
        ClosureProposal(
            proposal_id="claim_public_posture_shortcut",
            proposal_kind="governance_shortcut",
            repeats_current_t485_t487_packet_class=True,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=False,
            uses_t487_reachability_sufficiency_as_proof=True,
            claims_scale_clock_duration_finality_or_physics=True,
            requests_claim_or_posture_movement=True,
            intended_use="move claim or public posture from quotient sufficiency",
        ),
        ClosureProposal(
            proposal_id="independent_capability_missing_controls",
            proposal_kind="undercontrolled_future_packet",
            repeats_current_t485_t487_packet_class=False,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            independent_of_t485_t487_quotient=True,
            intended_use="propose a new capability object without hostile controls",
        ),
        ClosureProposal(
            proposal_id="future_independent_capability_object_packet",
            proposal_kind="future_independent_capability_target",
            repeats_current_t485_t487_packet_class=False,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=True,
            intended_use="future packet with a new independent capability object",
        ),
        ClosureProposal(
            proposal_id="future_domain_native_morphism_class_packet",
            proposal_kind="future_domain_native_morphism_target",
            repeats_current_t485_t487_packet_class=False,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=True,
            has_domain_native_morphism_class=True,
            intended_use="future packet with a stricter domain-native topology morphism class",
        ),
        ClosureProposal(
            proposal_id="future_direct_record_finality_bridge_packet",
            proposal_kind="future_record_finality_bridge_target",
            repeats_current_t485_t487_packet_class=False,
            cites_t487_anchor=True,
            declares_capability_object=True,
            computes_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t485_t487_quotient=True,
            has_direct_record_finality_bridge_theorem=True,
            intended_use="future direct theorem bridging reachability tasks to record finality",
        ),
    )


def _evaluate_proposal(
    proposal: ClosureProposal,
    anchor: dict[str, Any],
) -> ClosureDecision:
    missing = _missing_requirements(proposal, anchor)
    notes: list[str] = []

    if proposal.requests_claim_or_posture_movement:
        route = "block_governance_or_public_posture_shortcut"
        admitted = False
        notes.append("T488 has no authority to move claim status or public posture")
    elif not anchor["anchor_ok"]:
        route = "block_missing_t487_anchor"
        admitted = False
        notes.append("T487 anchor is unavailable or no longer has the expected guardrails")
    elif proposal.imports_rg_or_conformal_mechanism:
        route = "reject_rg_or_conformal_import_restart"
        admitted = False
        notes.append("RG and conformal material remain external calibration only")
    elif proposal.uses_non_singleton_spread_as_determined:
        route = "reject_t487_underdetermined_capability_restart"
        admitted = False
        notes.append("T487 explicitly made this capability non-singleton over quotient fibers")
    elif proposal.uses_path_latency_or_relay_artifact or proposal.uses_component_size_artifact:
        route = "reject_refinement_artifact_restart"
        admitted = False
        notes.append("refinement artifacts remain blocked by T485 and T487")
    elif proposal.uses_role_profile_as_scale_structure:
        route = "reject_role_profile_scale_shortcut"
        admitted = False
        notes.append("role profile is reachability-task bookkeeping, not internal scale")
    elif proposal.uses_t487_reachability_sufficiency_as_proof:
        route = "reject_reachability_upgrade_shortcut"
        admitted = False
        notes.append("reachability-task sufficiency is not evidence for stronger readings")
    elif missing:
        route = "reject_missing_reopen_requirements"
        admitted = False
        notes.append("proposal lacks mandatory T488 reopen controls")
    elif proposal.repeats_current_t485_t487_packet_class:
        route = "reject_current_thread_minor_variant"
        admitted = False
        notes.append("current T485-T487 packet class is closed to minor variants")
    elif proposal.has_direct_record_finality_bridge_theorem:
        route = "admit_future_record_finality_bridge_review_target"
        admitted = True
        notes.append("future theorem packet may be reviewed as new evidence")
        notes.append("admission is not record-finality evidence")
    elif proposal.has_domain_native_morphism_class:
        route = "admit_future_domain_native_morphism_review_target"
        admitted = True
        notes.append("future morphism packet may be reviewed as new evidence")
        notes.append("admission is not scale or physics evidence")
    elif proposal.independent_of_t485_t487_quotient:
        route = "admit_future_independent_capability_review_target"
        admitted = True
        notes.append("future capability packet may be reviewed as new evidence")
        notes.append("admission is not claim evidence")
    else:
        route = "reject_underdeclared_restart"
        admitted = False
        notes.append("proposal does not name a legitimate reopen path")

    admitted_as_future_review_target = route in {
        "admit_future_independent_capability_review_target",
        "admit_future_domain_native_morphism_review_target",
        "admit_future_record_finality_bridge_review_target",
    }
    closes_current_thread = (
        proposal.repeats_current_t485_t487_packet_class and not admitted
    )

    return ClosureDecision(
        proposal_id=proposal.proposal_id,
        admitted=admitted,
        route_label=route,
        classification=_classification_for_route(route),
        admitted_as_future_review_target=admitted_as_future_review_target,
        counts_as_thread_evidence=False,
        closes_current_thread=closes_current_thread,
        missing_requirements=missing,
        notes=tuple(notes),
    )


def _missing_requirements(
    proposal: ClosureProposal,
    anchor: dict[str, Any],
) -> tuple[str, ...]:
    missing: list[str] = []

    if not anchor["anchor_ok"]:
        missing.append("t487_anchor_ok")
    if not proposal.cites_t487_anchor:
        missing.append("t487_anchor_cited")
    if not proposal.declares_capability_object:
        missing.append("capability_object_declared")
    if not proposal.computes_capability_spread:
        missing.append("capability_spread_computed")
    if not proposal.supplies_positive_controls:
        missing.append("positive_reachability_controls")
    if not proposal.supplies_hostile_controls:
        missing.append("hostile_overread_controls")
    if not proposal.independent_of_t485_t487_quotient and not proposal.repeats_current_t485_t487_packet_class:
        missing.append("independent_evidence_beyond_quotient")
    if proposal.claims_scale_clock_duration_finality_or_physics:
        if not proposal.has_direct_record_finality_bridge_theorem:
            missing.append("direct_record_finality_or_scale_bridge_theorem")
        if not proposal.has_domain_native_morphism_class:
            missing.append("domain_native_morphism_class")

    return tuple(missing)


def _classification_for_route(route: str) -> str:
    mapping = {
        "block_governance_or_public_posture_shortcut": "governance_boundary_block",
        "block_missing_t487_anchor": "missing_prior_gate_block",
        "reject_rg_or_conformal_import_restart": "external_mechanism_rejection",
        "reject_t487_underdetermined_capability_restart": "underdetermined_capability_rejection",
        "reject_refinement_artifact_restart": "refinement_artifact_rejection",
        "reject_role_profile_scale_shortcut": "scale_shortcut_rejection",
        "reject_reachability_upgrade_shortcut": "reachability_upgrade_rejection",
        "reject_missing_reopen_requirements": "missing_reopen_requirement_rejection",
        "reject_current_thread_minor_variant": "current_packet_class_closed",
        "admit_future_independent_capability_review_target": "future_independent_capability_review_target",
        "admit_future_domain_native_morphism_review_target": "future_domain_native_morphism_review_target",
        "admit_future_record_finality_bridge_review_target": "future_record_finality_bridge_review_target",
        "reject_underdeclared_restart": "underdeclared_restart_rejection",
    }
    return mapping.get(route, "unclassified_closure_route")


def _load_t487_result() -> dict[str, Any]:
    path = Path("results") / f"{T487_ARTIFACT_ID}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _t487_anchor_checks(t487: dict[str, Any]) -> dict[str, Any]:
    verdict = t487["overall_verdict"]
    expected_admitted = [
        "source_target_reachability_task",
        "quotient_role_profile_task",
    ]
    future_minimum = t487["future_packet_minimum"]
    not_earned = t487["not_earned"]
    anchor_ok = (
        t487["artifact_id"] == T487_ARTIFACT_ID
        and verdict["gate_passed"] is True
        and verdict["reachability_task_sufficient"] is True
        and verdict["role_profile_task_sufficient"] is True
        and verdict["path_latency_underdetermined"] is True
        and verdict["relay_budget_underdetermined"] is True
        and verdict["component_size_underdetermined"] is True
        and verdict["hostile_controls_blocked"] is True
        and t487["admitted_candidate_ids"] == expected_admitted
        and "compute capability spread over quotient-visible fibers" in future_minimum
        and "scale-genesis theorem" in not_earned
        and "record-finality change" in not_earned
    )
    return {
        "artifact_id": t487["artifact_id"],
        "verdict": verdict["verdict"],
        "anchor_ok": anchor_ok,
        "gate_passed": verdict["gate_passed"],
        "admitted_candidate_ids": t487["admitted_candidate_ids"],
        "reachability_task_sufficient": verdict["reachability_task_sufficient"],
        "role_profile_task_sufficient": verdict["role_profile_task_sufficient"],
        "path_latency_underdetermined": verdict["path_latency_underdetermined"],
        "relay_budget_underdetermined": verdict["relay_budget_underdetermined"],
        "component_size_underdetermined": verdict["component_size_underdetermined"],
        "hostile_controls_blocked": verdict["hostile_controls_blocked"],
        "record_finality_change_earned": verdict["record_finality_change_earned"],
        "scale_genesis_theorem_earned": verdict["scale_genesis_theorem_earned"],
        "physics_claim_earned": verdict["physics_claim_earned"],
        "future_packet_minimum_preserved": (
            "compute capability spread over quotient-visible fibers" in future_minimum
        ),
    }


def _proposal_by_id(
    proposals: tuple[ClosureProposal, ...],
    proposal_id: str,
) -> ClosureProposal:
    for proposal in proposals:
        if proposal.proposal_id == proposal_id:
            return proposal
    raise KeyError(proposal_id)


def t488_result_to_dict(result: T488Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "t487_anchor": result.t487_anchor,
        "proposals": [_proposal_to_dict(proposal) for proposal in result.proposals],
        "decisions": [_decision_to_dict(decision) for decision in result.decisions],
        "claim_ledger_update": result.claim_ledger_update,
        "current_thread_closed": result.current_thread_closed,
        "admitted_future_targets": list(result.admitted_future_targets),
        "rejected_restart_packets": list(result.rejected_restart_packets),
        "strongest_reading": result.strongest_reading,
        "future_reopen_minimum": list(result.future_reopen_minimum),
        "not_earned": list(result.not_earned),
    }


def render_markdown(result: T488Result) -> str:
    """Render T488 results as Markdown."""

    anchor_rows = [
        f"| {key} | {value} |" for key, value in result.t487_anchor.items()
    ]
    decision_rows = []
    for decision in result.decisions:
        missing = ", ".join(decision.missing_requirements) or "none"
        notes = "; ".join(decision.notes) or "none"
        decision_rows.append(
            "| {proposal} | {admitted} | {route} | {classification} | "
            "{future} | {evidence} | {closed} | {missing} | {notes} |".format(
                proposal=decision.proposal_id,
                admitted=decision.admitted,
                route=decision.route_label,
                classification=decision.classification,
                future=decision.admitted_as_future_review_target,
                evidence=decision.counts_as_thread_evidence,
                closed=decision.closes_current_thread,
                missing=missing,
                notes=notes,
            )
        )
    reopen = [f"- {item}" for item in result.future_reopen_minimum]
    not_earned = [f"- {item}" for item in result.not_earned]

    return "\n".join(
        [
            "# T488 - Post-T487 Reachability Quotient Closure Router - v0.1 results",
            "",
            "> Closure router only. No claim status, roadmap, README, North Star, "
            "public-posture, hard-policy, physics, scale-genesis, clock, duration, "
            "finality, or cross-repo movement.",
            "",
            "- Spec: `tests/T488-post-t487-reachability-quotient-closure-router.md`",
            "- Model: `models/post_t487_reachability_quotient_closure_router.py`",
            "- Tests: `tests/test_post_t487_reachability_quotient_closure_router.py`",
            "- Artifact JSON: `results/T488-post-t487-reachability-quotient-closure-router-v0.1.json`",
            "- Source open problem: `open-problems/rg-flow-as-multiscale-transport-analogy.md`",
            "- Prior gates: T479 through T487",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## T487 Anchor",
            "",
            "| field | value |",
            "| --- | --- |",
            *anchor_rows,
            "",
            "## Closure Decisions",
            "",
            "| proposal | admitted? | route | classification | future target? | counts as evidence? | closes current thread? | missing requirements | notes |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            *decision_rows,
            "",
            "## Future Reopen Minimum",
            "",
            *reopen,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _proposal_to_dict(proposal: ClosureProposal) -> dict[str, Any]:
    return {
        "proposal_id": proposal.proposal_id,
        "proposal_kind": proposal.proposal_kind,
        "repeats_current_t485_t487_packet_class": (
            proposal.repeats_current_t485_t487_packet_class
        ),
        "cites_t487_anchor": proposal.cites_t487_anchor,
        "declares_capability_object": proposal.declares_capability_object,
        "computes_capability_spread": proposal.computes_capability_spread,
        "supplies_positive_controls": proposal.supplies_positive_controls,
        "supplies_hostile_controls": proposal.supplies_hostile_controls,
        "independent_of_t485_t487_quotient": (
            proposal.independent_of_t485_t487_quotient
        ),
        "has_domain_native_morphism_class": proposal.has_domain_native_morphism_class,
        "has_direct_record_finality_bridge_theorem": (
            proposal.has_direct_record_finality_bridge_theorem
        ),
        "uses_t487_reachability_sufficiency_as_proof": (
            proposal.uses_t487_reachability_sufficiency_as_proof
        ),
        "uses_role_profile_as_scale_structure": (
            proposal.uses_role_profile_as_scale_structure
        ),
        "uses_non_singleton_spread_as_determined": (
            proposal.uses_non_singleton_spread_as_determined
        ),
        "uses_path_latency_or_relay_artifact": (
            proposal.uses_path_latency_or_relay_artifact
        ),
        "uses_component_size_artifact": proposal.uses_component_size_artifact,
        "imports_rg_or_conformal_mechanism": (
            proposal.imports_rg_or_conformal_mechanism
        ),
        "claims_scale_clock_duration_finality_or_physics": (
            proposal.claims_scale_clock_duration_finality_or_physics
        ),
        "requests_claim_or_posture_movement": (
            proposal.requests_claim_or_posture_movement
        ),
        "intended_use": proposal.intended_use,
    }


def _decision_to_dict(decision: ClosureDecision) -> dict[str, Any]:
    return {
        "proposal_id": decision.proposal_id,
        "admitted": decision.admitted,
        "route_label": decision.route_label,
        "classification": decision.classification,
        "admitted_as_future_review_target": decision.admitted_as_future_review_target,
        "counts_as_thread_evidence": decision.counts_as_thread_evidence,
        "closes_current_thread": decision.closes_current_thread,
        "missing_requirements": list(decision.missing_requirements),
        "notes": list(decision.notes),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t488_analysis()
    payload = t488_result_to_dict(result)
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
