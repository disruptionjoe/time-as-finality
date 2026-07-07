"""T489: post-T478 valid-coarse-graining closure router.

T467-T478 built and stress-tested bounded-observer valid-coarse-graining
admission gates. The latest T478 result makes the repaired packet coherent
across a finite observer-budget lattice, while keeping it observer-indexed and
non-promotional.

This router closes the current valid-coarse-graining thread against minor
restarts while admitting only genuinely new future review targets. It does not
move claim status, public posture, North Star, roadmap, D1/T10/T29, Observer
Theory, physics, consciousness, or cross-repo truth.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T489-post-t478-valid-coarse-graining-closure-router-v0.1"
T478_ARTIFACT_ID = "T478-coarse-graining-budget-lattice-gate-v0.1"
VERDICT = "POST_T478_VALID_COARSE_GRAINING_THREAD_CLOSED_NEW_EVIDENCE_ONLY"


@dataclass(frozen=True)
class ClosureProposal:
    """A proposed post-T478 restart or future review packet."""

    proposal_id: str
    proposal_kind: str
    repeats_current_t467_t478_packet_class: bool
    cites_t478_anchor: bool
    declares_observer_budget_poset: bool
    declares_certified_record_capability: bool
    reports_budget_monotonicity_and_join_checks: bool
    supplies_positive_controls: bool
    supplies_hostile_controls: bool
    independent_of_t467_t478_fixture: bool
    has_domain_native_cost_certifiability_theorem: bool = False
    has_direct_observer_theory_taf_equivalence_theorem: bool = False
    uses_t467_binary_controls_as_independent: bool = False
    uses_task_label_as_certified_record: bool = False
    uses_budget_lattice_as_global_criterion: bool = False
    uses_boundary_pair_as_global_admission: bool = False
    uses_lattice_coherence_as_promotion_proof: bool = False
    uses_cheap_arithmetic_or_xor: bool = False
    uses_microstate_or_label_restatement: bool = False
    uses_observer_creates_truth_overread: bool = False
    claims_d1_t10_t29_observer_theory_or_physics: bool = False
    requests_claim_or_posture_movement: bool = False
    intended_use: str = ""


@dataclass(frozen=True)
class ClosureDecision:
    """Router decision for a post-T478 proposal."""

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
class T489Result:
    """Complete T489 closure-router result."""

    t478_anchor: dict[str, Any]
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


def run_t489_analysis() -> T489Result:
    """Run the post-T478 valid-coarse-graining closure router."""

    t478 = _load_t478_result()
    anchor = _t478_anchor_checks(t478)
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
            if _proposal_by_id(
                proposals, decision.proposal_id
            ).repeats_current_t467_t478_packet_class
        )
        and not any(decision.counts_as_thread_evidence for decision in decisions)
    )

    return T489Result(
        t478_anchor=anchor,
        proposals=proposals,
        decisions=decisions,
        verdict=VERDICT,
        claim_ledger_update="none",
        current_thread_closed=current_thread_closed,
        admitted_future_targets=admitted_future_targets,
        rejected_restart_packets=rejected_restart_packets,
        strongest_reading=(
            "T489 closes the current T467-T478 valid-coarse-graining thread "
            "to minor restarts. T478 supplies a finite observer-budget lattice "
            "intake guardrail only: admissions are budget-indexed review "
            "targets, not a global valid-coarse-graining criterion, not an "
            "Observer Theory equivalence theorem, not D1/T10/T29 promotion, "
            "not physics or consciousness evidence, and not claim or public "
            "posture support. Future work can reopen the surface only by "
            "bringing a newly declared certified-record capability object with "
            "hostile controls, a domain-native cost/certifiability theorem, or "
            "a direct Observer Theory/TaF equivalence theorem with explicit "
            "limits and controls."
        ),
        future_reopen_minimum=(
            "cite T467-T478 and state why the budget-lattice closure is insufficient",
            "declare the observer-budget poset before relation selection",
            "declare a certified-record capability object before witness construction",
            "report budget-edge monotonicity and join/path checks",
            "explain every new admission by newly accessible certified record fields",
            "preserve independent positive controls across at least one non-binary or multi-holder fixture",
            "preserve hostile cheap arithmetic, xor, label-restatement, microstate, and observer-creates-truth controls",
            "supply evidence independent of the T467-T478 finite fixture before claiming a new criterion",
            "provide a domain-native cost/certifiability theorem before importing computation-cost language",
            "provide a direct Observer Theory/TaF equivalence theorem before using identity language",
            "keep D1/T10/T29, Observer Theory, global-criterion, physics, consciousness, claim-ledger, roadmap, North Star, public-posture, and cross-repo readings blocked unless separately earned",
        ),
        not_earned=(
            "D1 promotion",
            "T10 superselection result",
            "T29 projection-obstruction promotion",
            "Observer Theory equivalence theorem",
            "global valid-coarse-graining criterion",
            "cost/certifiability theorem",
            "physics or consciousness claim",
            "observer-creates-truth claim",
            "claim-ledger movement",
            "roadmap movement",
            "README movement",
            "North Star movement",
            "public-posture movement",
            "hard-policy movement",
            "protected-license movement",
            "cross-repo truth movement",
        ),
    )


def run() -> dict[str, Any]:
    """Return a serializable T489 result."""

    return t489_result_to_dict(run_t489_analysis())


def _closure_proposals() -> tuple[ClosureProposal, ...]:
    return (
        ClosureProposal(
            proposal_id="t467_binary_positive_control_upgrade",
            proposal_kind="minor_restart",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=False,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=False,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=False,
            uses_t467_binary_controls_as_independent=True,
            intended_use="reuse T467's binary positives as independent support",
        ),
        ClosureProposal(
            proposal_id="task_label_certification_shortcut",
            proposal_kind="minor_restart",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=False,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            independent_of_t467_t478_fixture=False,
            uses_task_label_as_certified_record=True,
            intended_use="treat an asserted finality-task label as certification",
        ),
        ClosureProposal(
            proposal_id="budget_lattice_global_criterion_upgrade",
            proposal_kind="global_criterion_shortcut",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=False,
            uses_budget_lattice_as_global_criterion=True,
            claims_d1_t10_t29_observer_theory_or_physics=True,
            intended_use="upgrade lattice coherence into a global criterion",
        ),
        ClosureProposal(
            proposal_id="boundary_pair_global_admission_overread",
            proposal_kind="observer_index_overread",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=False,
            uses_boundary_pair_as_global_admission=True,
            intended_use="read boundary-pair admission as budget-free validity",
        ),
        ClosureProposal(
            proposal_id="lattice_path_independence_promotion_shortcut",
            proposal_kind="promotion_shortcut",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=False,
            uses_lattice_coherence_as_promotion_proof=True,
            claims_d1_t10_t29_observer_theory_or_physics=True,
            intended_use="treat path independence as D1/T10/T29 or Observer Theory evidence",
        ),
        ClosureProposal(
            proposal_id="cheap_arithmetic_xor_restart",
            proposal_kind="hostile_control_restart",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=False,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            independent_of_t467_t478_fixture=False,
            uses_cheap_arithmetic_or_xor=True,
            intended_use="reopen with accessible arithmetic or xor partitions",
        ),
        ClosureProposal(
            proposal_id="microstate_label_restatement_restart",
            proposal_kind="hostile_control_restart",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=False,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            independent_of_t467_t478_fixture=False,
            uses_microstate_or_label_restatement=True,
            intended_use="reopen with microstate identity or label restatement",
        ),
        ClosureProposal(
            proposal_id="observer_creates_truth_restart",
            proposal_kind="forbidden_posture_restart",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=False,
            uses_observer_creates_truth_overread=True,
            claims_d1_t10_t29_observer_theory_or_physics=True,
            intended_use="treat coarse-graining as observer-created truth",
        ),
        ClosureProposal(
            proposal_id="observer_theory_identity_shortcut",
            proposal_kind="identity_shortcut",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=False,
            has_direct_observer_theory_taf_equivalence_theorem=False,
            claims_d1_t10_t29_observer_theory_or_physics=True,
            intended_use="assert TaF criterion exactly fills Observer Theory's open slot",
        ),
        ClosureProposal(
            proposal_id="claim_public_posture_shortcut",
            proposal_kind="governance_shortcut",
            repeats_current_t467_t478_packet_class=True,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=False,
            uses_budget_lattice_as_global_criterion=True,
            requests_claim_or_posture_movement=True,
            intended_use="move claim status or public posture from T478",
        ),
        ClosureProposal(
            proposal_id="independent_capability_missing_hostile_controls",
            proposal_kind="undercontrolled_future_packet",
            repeats_current_t467_t478_packet_class=False,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            independent_of_t467_t478_fixture=True,
            intended_use="propose a new certified-record capability without hostile controls",
        ),
        ClosureProposal(
            proposal_id="future_independent_certified_record_capability_packet",
            proposal_kind="future_independent_capability_target",
            repeats_current_t467_t478_packet_class=False,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=True,
            intended_use="future packet with a new certified-record capability object",
        ),
        ClosureProposal(
            proposal_id="future_domain_native_cost_certifiability_theorem_packet",
            proposal_kind="future_cost_certifiability_target",
            repeats_current_t467_t478_packet_class=False,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=True,
            has_domain_native_cost_certifiability_theorem=True,
            intended_use="future packet with a domain-native cost/certifiability theorem",
        ),
        ClosureProposal(
            proposal_id="future_direct_observer_theory_taf_equivalence_packet",
            proposal_kind="future_equivalence_theorem_target",
            repeats_current_t467_t478_packet_class=False,
            cites_t478_anchor=True,
            declares_observer_budget_poset=True,
            declares_certified_record_capability=True,
            reports_budget_monotonicity_and_join_checks=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t467_t478_fixture=True,
            has_direct_observer_theory_taf_equivalence_theorem=True,
            intended_use="future direct theorem comparing Observer Theory validity to TaF finality-admissibility",
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
        notes.append("T489 has no authority to move claim status or public posture")
    elif not anchor["anchor_ok"]:
        route = "block_missing_t478_anchor"
        admitted = False
        notes.append("T478 anchor is unavailable or no longer has expected guardrails")
    elif proposal.uses_observer_creates_truth_overread:
        route = "reject_observer_creates_truth_restart"
        admitted = False
        notes.append("observer-creates-truth readings remain forbidden posture")
    elif proposal.uses_t467_binary_controls_as_independent:
        route = "reject_t467_binary_positive_control_upgrade"
        admitted = False
        notes.append("T468 already made the binary positives collapse")
    elif proposal.uses_task_label_as_certified_record:
        route = "reject_task_label_certification_shortcut"
        admitted = False
        notes.append("task labels do not substitute for certified record objects")
    elif proposal.uses_cheap_arithmetic_or_xor:
        route = "reject_cheap_arithmetic_or_xor_restart"
        admitted = False
        notes.append("cheap arithmetic and xor controls remain hostile controls")
    elif proposal.uses_microstate_or_label_restatement:
        route = "reject_microstate_or_label_restatement_restart"
        admitted = False
        notes.append("microstate identity and label restatement remain blocked")
    elif proposal.uses_boundary_pair_as_global_admission:
        route = "reject_observer_index_overread"
        admitted = False
        notes.append("boundary-pair admission is observer-budget indexed only")
    elif proposal.uses_budget_lattice_as_global_criterion:
        route = "reject_global_criterion_shortcut"
        admitted = False
        notes.append("T478 is a finite guardrail, not a global criterion")
    elif proposal.uses_lattice_coherence_as_promotion_proof:
        route = "reject_lattice_coherence_promotion_shortcut"
        admitted = False
        notes.append("lattice coherence is not D1/T10/T29 or Observer Theory evidence")
    elif (
        proposal.claims_d1_t10_t29_observer_theory_or_physics
        and not proposal.has_direct_observer_theory_taf_equivalence_theorem
    ):
        route = "reject_observer_theory_or_physics_shortcut"
        admitted = False
        notes.append("strong readings need a direct theorem beyond T478")
    elif missing:
        route = "reject_missing_reopen_requirements"
        admitted = False
        notes.append("proposal lacks mandatory T489 reopen controls")
    elif proposal.repeats_current_t467_t478_packet_class:
        route = "reject_current_thread_minor_variant"
        admitted = False
        notes.append("current T467-T478 packet class is closed to minor variants")
    elif proposal.has_direct_observer_theory_taf_equivalence_theorem:
        route = "admit_future_equivalence_theorem_review_target"
        admitted = True
        notes.append("future equivalence theorem packet may be reviewed as new evidence")
        notes.append("admission is not Observer Theory or TaF evidence")
    elif proposal.has_domain_native_cost_certifiability_theorem:
        route = "admit_future_cost_certifiability_review_target"
        admitted = True
        notes.append("future cost/certifiability packet may be reviewed as new evidence")
        notes.append("admission is not a global criterion")
    elif proposal.independent_of_t467_t478_fixture:
        route = "admit_future_independent_capability_review_target"
        admitted = True
        notes.append("future certified-record capability packet may be reviewed")
        notes.append("admission is not claim evidence")
    else:
        route = "reject_underdeclared_restart"
        admitted = False
        notes.append("proposal does not name a legitimate reopen path")

    admitted_as_future_review_target = route in {
        "admit_future_independent_capability_review_target",
        "admit_future_cost_certifiability_review_target",
        "admit_future_equivalence_theorem_review_target",
    }
    closes_current_thread = (
        proposal.repeats_current_t467_t478_packet_class and not admitted
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
        missing.append("t478_anchor_ok")
    if not proposal.cites_t478_anchor:
        missing.append("t478_anchor_cited")
    if not proposal.declares_observer_budget_poset:
        missing.append("observer_budget_poset_declared")
    if not proposal.declares_certified_record_capability:
        missing.append("certified_record_capability_declared")
    if not proposal.reports_budget_monotonicity_and_join_checks:
        missing.append("budget_monotonicity_and_join_checks_reported")
    if not proposal.supplies_positive_controls:
        missing.append("positive_finality_controls")
    if not proposal.supplies_hostile_controls:
        missing.append("hostile_overread_controls")
    if (
        not proposal.independent_of_t467_t478_fixture
        and not proposal.repeats_current_t467_t478_packet_class
    ):
        missing.append("independent_evidence_beyond_t467_t478_fixture")
    if proposal.claims_d1_t10_t29_observer_theory_or_physics:
        if not proposal.has_direct_observer_theory_taf_equivalence_theorem:
            missing.append("direct_observer_theory_taf_equivalence_theorem")
        if not proposal.has_domain_native_cost_certifiability_theorem:
            missing.append("domain_native_cost_certifiability_theorem")

    return tuple(missing)


def _classification_for_route(route: str) -> str:
    mapping = {
        "block_governance_or_public_posture_shortcut": "governance_boundary_block",
        "block_missing_t478_anchor": "missing_prior_gate_block",
        "reject_observer_creates_truth_restart": "forbidden_posture_rejection",
        "reject_t467_binary_positive_control_upgrade": "collapsed_positive_control_rejection",
        "reject_task_label_certification_shortcut": "task_label_shortcut_rejection",
        "reject_cheap_arithmetic_or_xor_restart": "hostile_arithmetic_rejection",
        "reject_microstate_or_label_restatement_restart": "hostile_identity_or_label_restatement_rejection",
        "reject_observer_index_overread": "observer_index_overread_rejection",
        "reject_global_criterion_shortcut": "global_criterion_shortcut_rejection",
        "reject_lattice_coherence_promotion_shortcut": "promotion_shortcut_rejection",
        "reject_observer_theory_or_physics_shortcut": "strong_reading_shortcut_rejection",
        "reject_missing_reopen_requirements": "missing_reopen_requirement_rejection",
        "reject_current_thread_minor_variant": "current_packet_class_closed",
        "admit_future_independent_capability_review_target": "future_independent_capability_review_target",
        "admit_future_cost_certifiability_review_target": "future_cost_certifiability_review_target",
        "admit_future_equivalence_theorem_review_target": "future_equivalence_theorem_review_target",
        "reject_underdeclared_restart": "underdeclared_restart_rejection",
    }
    return mapping.get(route, "unclassified_closure_route")


def _load_t478_result() -> dict[str, Any]:
    path = Path("results") / f"{T478_ARTIFACT_ID}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _t478_anchor_checks(t478: dict[str, Any]) -> dict[str, Any]:
    verdict = t478["overall_verdict"]
    future_minimum = t478["future_packet_minimum"]
    not_earned = t478["not_earned"]
    expected_top_ids = [
        "boundary_pair_status",
        "pair_01_finality_band",
        "pair_02_finality_band",
        "three_holder_finality_band",
        "three_holder_support_count",
    ]
    anchor_ok = (
        t478["artifact_id"] == T478_ARTIFACT_ID
        and verdict["gate_passed"] is True
        and verdict["edge_monotonicity_passed"] is True
        and verdict["join_path_independence_passed"] is True
        and verdict["top_path_independence_passed"] is True
        and verdict["hostile_controls_blocked_when_accessible"] is True
        and verdict["top_budget_positive_controls_independent"] is True
        and verdict["d1_promotion_earned"] is False
        and verdict["t10_promotion_earned"] is False
        and verdict["t29_promotion_earned"] is False
        and verdict["observer_theory_identification_earned"] is False
        and verdict["global_valid_coarse_graining_criterion_earned"] is False
        and verdict["physics_claim_earned"] is False
        and t478["top_budget_admitted_positive_ids"] == expected_top_ids
        and "declare a finite observer-budget poset, not only one chain" in future_minimum
        and "global valid-coarse-graining criterion" in not_earned
    )
    return {
        "artifact_id": t478["artifact_id"],
        "verdict": verdict["verdict"],
        "anchor_ok": anchor_ok,
        "gate_passed": verdict["gate_passed"],
        "edge_monotonicity_passed": verdict["edge_monotonicity_passed"],
        "join_path_independence_passed": verdict["join_path_independence_passed"],
        "top_path_independence_passed": verdict["top_path_independence_passed"],
        "hostile_controls_blocked_when_accessible": (
            verdict["hostile_controls_blocked_when_accessible"]
        ),
        "top_budget_positive_controls_independent": (
            verdict["top_budget_positive_controls_independent"]
        ),
        "d1_promotion_earned": verdict["d1_promotion_earned"],
        "t10_promotion_earned": verdict["t10_promotion_earned"],
        "t29_promotion_earned": verdict["t29_promotion_earned"],
        "observer_theory_identification_earned": (
            verdict["observer_theory_identification_earned"]
        ),
        "global_valid_coarse_graining_criterion_earned": (
            verdict["global_valid_coarse_graining_criterion_earned"]
        ),
        "physics_claim_earned": verdict["physics_claim_earned"],
        "top_budget_admitted_positive_ids": t478["top_budget_admitted_positive_ids"],
        "future_packet_minimum_preserved": (
            "declare a finite observer-budget poset, not only one chain"
            in future_minimum
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


def t489_result_to_dict(result: T489Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "t478_anchor": result.t478_anchor,
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


def render_markdown(result: T489Result) -> str:
    """Render T489 results as Markdown."""

    anchor_rows = [
        f"| {key} | {value} |" for key, value in result.t478_anchor.items()
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
            "# T489 - Post-T478 Valid Coarse-Graining Closure Router - v0.1 results",
            "",
            "> Closure router only. No claim status, roadmap, README, North Star, "
            "public-posture, hard-policy, D1/T10/T29, Observer Theory, physics, "
            "consciousness, or cross-repo movement.",
            "",
            "- Spec: `tests/T489-post-t478-valid-coarse-graining-closure-router.md`",
            "- Model: `models/post_t478_valid_coarse_graining_closure_router.py`",
            "- Tests: `tests/test_post_t478_valid_coarse_graining_closure_router.py`",
            "- Artifact JSON: `results/T489-post-t478-valid-coarse-graining-closure-router-v0.1.json`",
            "- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`",
            "- Prior gates: T467, T468, T469, T471, T477, and T478",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## T478 Anchor",
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
        "repeats_current_t467_t478_packet_class": (
            proposal.repeats_current_t467_t478_packet_class
        ),
        "cites_t478_anchor": proposal.cites_t478_anchor,
        "declares_observer_budget_poset": proposal.declares_observer_budget_poset,
        "declares_certified_record_capability": (
            proposal.declares_certified_record_capability
        ),
        "reports_budget_monotonicity_and_join_checks": (
            proposal.reports_budget_monotonicity_and_join_checks
        ),
        "supplies_positive_controls": proposal.supplies_positive_controls,
        "supplies_hostile_controls": proposal.supplies_hostile_controls,
        "independent_of_t467_t478_fixture": (
            proposal.independent_of_t467_t478_fixture
        ),
        "has_domain_native_cost_certifiability_theorem": (
            proposal.has_domain_native_cost_certifiability_theorem
        ),
        "has_direct_observer_theory_taf_equivalence_theorem": (
            proposal.has_direct_observer_theory_taf_equivalence_theorem
        ),
        "uses_t467_binary_controls_as_independent": (
            proposal.uses_t467_binary_controls_as_independent
        ),
        "uses_task_label_as_certified_record": (
            proposal.uses_task_label_as_certified_record
        ),
        "uses_budget_lattice_as_global_criterion": (
            proposal.uses_budget_lattice_as_global_criterion
        ),
        "uses_boundary_pair_as_global_admission": (
            proposal.uses_boundary_pair_as_global_admission
        ),
        "uses_lattice_coherence_as_promotion_proof": (
            proposal.uses_lattice_coherence_as_promotion_proof
        ),
        "uses_cheap_arithmetic_or_xor": proposal.uses_cheap_arithmetic_or_xor,
        "uses_microstate_or_label_restatement": (
            proposal.uses_microstate_or_label_restatement
        ),
        "uses_observer_creates_truth_overread": (
            proposal.uses_observer_creates_truth_overread
        ),
        "claims_d1_t10_t29_observer_theory_or_physics": (
            proposal.claims_d1_t10_t29_observer_theory_or_physics
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

    result = run_t489_analysis()
    payload = t489_result_to_dict(result)
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
