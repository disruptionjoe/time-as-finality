"""T491: post-T490 S1 finite-colimit closure router.

T223 closed the uniform finite finality-colimit route for S1. T464 made the
added-assumption admission burden executable, and T490 narrowed the nonuniform
measure branch by blocking tail tuning, guardrail conditioning, screen drift,
single-size positives, and promotion shortcuts.

This router closes the current finite S1 colimit route against minor restarts
while preserving only genuinely new future review targets: an independent
measure law, a continuum bridge, or one of the separate formal entry points from
the open problem. It does not promote S1, reverse T223, derive spacetime, move
public posture, or change cross-repo truth.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T491-post-t490-s1-finite-colimit-closure-router-v0.1"
T490_ARTIFACT_ID = "T490-s1-nonuniform-measure-persistence-gate-v0.1"
VERDICT = "POST_T490_S1_FINITE_COLIMIT_ROUTE_CLOSED_NEW_EVIDENCE_ONLY"


@dataclass(frozen=True)
class ClosureProposal:
    """A proposed post-T490 restart or future review packet."""

    proposal_id: str
    proposal_kind: str
    repeats_current_t223_t490_finite_route: bool
    cites_t490_anchor: bool
    declares_t223_t490_context: bool
    predeclares_measure_law_or_bridge: bool
    keeps_finite_screens_fixed: bool
    audits_multi_size_or_limit: bool
    states_nonvanishing_mass_target: bool
    names_later_lorentzian_constraints: bool
    supplies_positive_controls: bool
    supplies_hostile_controls: bool
    independent_of_t223_t490_finite_route: bool
    has_independent_measure_law: bool = False
    has_continuum_bridge: bool = False
    uses_separate_formal_entry_point: bool = False
    uses_uniform_baseline: bool = False
    conditions_on_survivor_success: bool = False
    conditions_on_guardrail_screen: bool = False
    changes_finite_screens: bool = False
    uses_single_size_positive: bool = False
    uses_t490_admission_as_evidence: bool = False
    overclaims_s1_spacetime_or_lorentzian_result: bool = False
    requests_claim_or_posture_movement: bool = False
    requires_non_github_external_action: bool = False
    intended_use: str = ""


@dataclass(frozen=True)
class ClosureDecision:
    """Router decision for a post-T490 proposal."""

    proposal_id: str
    admitted: bool
    route_label: str
    classification: str
    admitted_as_future_review_target: bool
    counts_as_s1_evidence: bool
    closes_current_finite_route: bool
    missing_requirements: tuple[str, ...]
    notes: tuple[str, ...]


@dataclass(frozen=True)
class T491Result:
    """Complete T491 closure-router result."""

    t490_anchor: dict[str, Any]
    proposals: tuple[ClosureProposal, ...]
    decisions: tuple[ClosureDecision, ...]
    verdict: str
    claim_ledger_update: str
    current_finite_route_closed: bool
    admitted_future_targets: tuple[str, ...]
    rejected_restart_packets: tuple[str, ...]
    strongest_reading: str
    future_reopen_minimum: tuple[str, ...]
    not_earned: tuple[str, ...]


def run_t491_analysis() -> T491Result:
    """Run the post-T490 S1 finite-colimit closure router."""

    t490 = _load_t490_result()
    anchor = _t490_anchor_checks(t490)
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
    current_finite_route_closed = (
        anchor["anchor_ok"]
        and all(
            decision.closes_current_finite_route
            for decision in decisions
            if _proposal_by_id(
                proposals, decision.proposal_id
            ).repeats_current_t223_t490_finite_route
        )
        and not any(decision.counts_as_s1_evidence for decision in decisions)
    )

    return T491Result(
        t490_anchor=anchor,
        proposals=proposals,
        decisions=decisions,
        verdict=VERDICT,
        claim_ledger_update="none",
        current_finite_route_closed=current_finite_route_closed,
        admitted_future_targets=admitted_future_targets,
        rejected_restart_packets=rejected_restart_packets,
        strongest_reading=(
            "T491 closes the current T223-T490 finite S1 colimit route to "
            "minor restarts. T490 admits only review targets; it is not S1 "
            "evidence, not a T223 reversal, not a spacetime derivation, not "
            "manifoldlikeness, not Lorentzian structure, and not a continuum "
            "theorem. Future work can reopen the finite route only with a "
            "predeclared independent measure law or continuum bridge that "
            "inherits T223/T464/T490 and preserves fixed finite screens, "
            "multi-size or limit persistence, nonvanishing survivor mass, "
            "later Lorentzian constraints, and hostile controls. Separate "
            "topos, NCG, path-integral, or stochastic entry points remain "
            "reviewable as separate formal routes, not as evidence from the "
            "finite survivor tail."
        ),
        future_reopen_minimum=(
            "cite T223, T464, and T490 and state why the finite-route closure is insufficient",
            "predeclare the nonuniform measure law, selection law, sprinkling law, continuum bridge, or separate formal entry point before scoring",
            "supply an independent finality-native or neighbor-theory generating law when reopening the finite measure branch",
            "keep T126/T156/T159/T223 finite screens fixed unless the new packet is a separate formal entry point",
            "audit at least two finite sizes or declare a real limit target before claiming persistence",
            "state a nonvanishing survivor-mass or concentration target before scoring any finite survivor ensemble",
            "do not condition directly on survivor success or guardrail-screen pass predicates",
            "name later causal, metric, covariance, locality, embedding, or Lorentzian constraints",
            "preserve promotion, public-posture, external-action, and spacetime-derivation blocks",
            "treat admitted packets as review targets, not S1 evidence",
        ),
        not_earned=(
            "S1 promotion",
            "T223 reversal",
            "spacetime derivation",
            "manifoldlikeness result",
            "dimension estimate",
            "sprinkling law",
            "Lorentzian metric",
            "locality or covariance theorem",
            "embedding theorem",
            "continuum theorem",
            "GR or QFT result",
            "claim-ledger movement",
            "roadmap movement",
            "README movement",
            "North Star movement",
            "public-posture movement",
            "hard-policy movement",
            "protected-license movement",
            "cross-repo truth movement",
            "non-GitHub external action",
        ),
    )


def run() -> dict[str, Any]:
    """Return a serializable T491 result."""

    return t491_result_to_dict(run_t491_analysis())


def _closure_proposals() -> tuple[ClosureProposal, ...]:
    return (
        ClosureProposal(
            proposal_id="uniform_finite_colimit_rerun",
            proposal_kind="minor_restart",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=False,
            names_later_lorentzian_constraints=False,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=False,
            uses_uniform_baseline=True,
            intended_use="rerun the uniform finite ordinal ensemble",
        ),
        ClosureProposal(
            proposal_id="survivor_tail_measure_restart",
            proposal_kind="tail_tuned_restart",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=False,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=False,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=False,
            conditions_on_survivor_success=True,
            intended_use="put mass on the already known T223 survivor tail",
        ),
        ClosureProposal(
            proposal_id="screen_conditioned_measure_restart",
            proposal_kind="guardrail_conditioning_restart",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=False,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=False,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=False,
            conditions_on_guardrail_screen=True,
            intended_use="treat guardrail-screen conditioning as a natural measure",
        ),
        ClosureProposal(
            proposal_id="post_t223_screen_drift_restart",
            proposal_kind="screen_drift_restart",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=False,
            keeps_finite_screens_fixed=False,
            audits_multi_size_or_limit=False,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=False,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            independent_of_t223_t490_finite_route=False,
            changes_finite_screens=True,
            intended_use="change the finite screens after T223/T490",
        ),
        ClosureProposal(
            proposal_id="single_size_positive_restart",
            proposal_kind="single_size_restart",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=False,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=False,
            uses_single_size_positive=True,
            intended_use="claim persistence from one finite size",
        ),
        ClosureProposal(
            proposal_id="t490_admission_as_s1_evidence_shortcut",
            proposal_kind="evidence_shortcut",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=False,
            uses_t490_admission_as_evidence=True,
            overclaims_s1_spacetime_or_lorentzian_result=True,
            intended_use="treat T490 review admission as S1 evidence",
        ),
        ClosureProposal(
            proposal_id="spacetime_derivation_overclaim",
            proposal_kind="overclaim_shortcut",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=False,
            overclaims_s1_spacetime_or_lorentzian_result=True,
            intended_use="claim spacetime, manifoldlikeness, or Lorentzian structure",
        ),
        ClosureProposal(
            proposal_id="claim_public_posture_shortcut",
            proposal_kind="governance_shortcut",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=False,
            uses_t490_admission_as_evidence=True,
            requests_claim_or_posture_movement=True,
            intended_use="move claim status or public posture from T490",
        ),
        ClosureProposal(
            proposal_id="external_publication_shortcut",
            proposal_kind="external_action_shortcut",
            repeats_current_t223_t490_finite_route=True,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=False,
            requires_non_github_external_action=True,
            intended_use="publish or advertise the S1 finite route externally",
        ),
        ClosureProposal(
            proposal_id="independent_measure_missing_hostile_controls",
            proposal_kind="undercontrolled_future_packet",
            repeats_current_t223_t490_finite_route=False,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            independent_of_t223_t490_finite_route=True,
            has_independent_measure_law=True,
            intended_use="future independent measure packet without hostile controls",
        ),
        ClosureProposal(
            proposal_id="future_independent_measure_law_packet",
            proposal_kind="future_measure_law_target",
            repeats_current_t223_t490_finite_route=False,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=True,
            has_independent_measure_law=True,
            intended_use="future packet with an independent finality-native measure law",
        ),
        ClosureProposal(
            proposal_id="future_continuum_bridge_packet",
            proposal_kind="future_continuum_bridge_target",
            repeats_current_t223_t490_finite_route=False,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=True,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=True,
            has_continuum_bridge=True,
            intended_use="future finite-to-continuum bridge with fixed finite screens",
        ),
        ClosureProposal(
            proposal_id="future_separate_formal_entry_point_packet",
            proposal_kind="future_separate_formal_entry_point_target",
            repeats_current_t223_t490_finite_route=False,
            cites_t490_anchor=True,
            declares_t223_t490_context=True,
            predeclares_measure_law_or_bridge=True,
            keeps_finite_screens_fixed=False,
            audits_multi_size_or_limit=True,
            states_nonvanishing_mass_target=True,
            names_later_lorentzian_constraints=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            independent_of_t223_t490_finite_route=True,
            uses_separate_formal_entry_point=True,
            intended_use="future topos, NCG, path-integral, or stochastic S1 route",
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
        notes.append("T491 has no authority to move claim status or public posture")
    elif proposal.requires_non_github_external_action:
        route = "block_external_action_shortcut"
        admitted = False
        notes.append("external publication or outreach needs separate authorization")
    elif not anchor["anchor_ok"]:
        route = "block_missing_t490_anchor"
        admitted = False
        notes.append("T490 anchor is unavailable or no longer has expected guardrails")
    elif proposal.overclaims_s1_spacetime_or_lorentzian_result:
        route = "block_s1_spacetime_or_lorentzian_overclaim"
        admitted = False
        notes.append("T490 review admission is not S1, spacetime, or Lorentzian evidence")
    elif proposal.uses_uniform_baseline:
        route = "reject_uniform_finite_colimit_rerun"
        admitted = False
        notes.append("T223 already closed the uniform finite ordinal baseline")
    elif proposal.conditions_on_survivor_success:
        route = "reject_tail_tuned_measure_restart"
        admitted = False
        notes.append("conditioning on the known survivor tail is circular")
    elif proposal.conditions_on_guardrail_screen:
        route = "reject_guardrail_screen_conditioning_restart"
        admitted = False
        notes.append("guardrail conditioning is diagnostic, not a natural measure")
    elif proposal.changes_finite_screens:
        route = "reject_post_t223_screen_drift_restart"
        admitted = False
        notes.append("changing finite screens after T223/T490 is target drift")
    elif proposal.uses_single_size_positive:
        route = "reject_single_size_positive_restart"
        admitted = False
        notes.append("single-size positives do not clear T490 persistence burden")
    elif proposal.uses_t490_admission_as_evidence:
        route = "reject_t490_admission_as_evidence_shortcut"
        admitted = False
        notes.append("T490 admission is review-only and counts as no S1 evidence")
    elif missing:
        route = "reject_missing_reopen_requirements"
        admitted = False
        notes.append("proposal lacks mandatory T491 reopen controls")
    elif proposal.repeats_current_t223_t490_finite_route:
        route = "reject_current_finite_route_minor_variant"
        admitted = False
        notes.append("current finite S1 colimit route is closed to minor variants")
    elif proposal.uses_separate_formal_entry_point:
        route = "admit_future_separate_formal_entry_point_review_target"
        admitted = True
        notes.append("separate formal entry point may be reviewed as new work")
        notes.append("admission is not evidence from the finite survivor tail")
    elif proposal.has_continuum_bridge:
        route = "admit_future_continuum_bridge_review_target"
        admitted = True
        notes.append("future continuum bridge packet may be reviewed as new evidence")
        notes.append("admission is not a continuum theorem")
    elif proposal.has_independent_measure_law:
        route = "admit_future_independent_measure_law_review_target"
        admitted = True
        notes.append("future independent measure-law packet may be reviewed")
        notes.append("admission is not S1 evidence")
    else:
        route = "reject_underdeclared_restart"
        admitted = False
        notes.append("proposal does not name a legitimate reopen path")

    admitted_as_future_review_target = route in {
        "admit_future_independent_measure_law_review_target",
        "admit_future_continuum_bridge_review_target",
        "admit_future_separate_formal_entry_point_review_target",
    }
    closes_current_finite_route = (
        proposal.repeats_current_t223_t490_finite_route and not admitted
    )

    return ClosureDecision(
        proposal_id=proposal.proposal_id,
        admitted=admitted,
        route_label=route,
        classification=_classification_for_route(route),
        admitted_as_future_review_target=admitted_as_future_review_target,
        counts_as_s1_evidence=False,
        closes_current_finite_route=closes_current_finite_route,
        missing_requirements=missing,
        notes=tuple(notes),
    )


def _missing_requirements(
    proposal: ClosureProposal,
    anchor: dict[str, Any],
) -> tuple[str, ...]:
    missing: list[str] = []

    if not anchor["anchor_ok"]:
        missing.append("t490_anchor_ok")
    if not proposal.cites_t490_anchor:
        missing.append("t490_anchor_cited")
    if not proposal.declares_t223_t490_context:
        missing.append("t223_t464_t490_context_declared")
    if not proposal.predeclares_measure_law_or_bridge:
        missing.append("measure_law_or_bridge_predeclared")
    if not proposal.keeps_finite_screens_fixed and not proposal.uses_separate_formal_entry_point:
        missing.append("finite_screens_fixed")
    if not proposal.audits_multi_size_or_limit:
        missing.append("multi_size_or_limit_audit")
    if not proposal.states_nonvanishing_mass_target:
        missing.append("nonvanishing_mass_target")
    if not proposal.names_later_lorentzian_constraints:
        missing.append("later_lorentzian_constraints_named")
    if not proposal.supplies_positive_controls:
        missing.append("positive_controls")
    if not proposal.supplies_hostile_controls:
        missing.append("hostile_overread_controls")
    if (
        not proposal.independent_of_t223_t490_finite_route
        and not proposal.repeats_current_t223_t490_finite_route
    ):
        missing.append("independent_evidence_beyond_t223_t490_finite_route")

    return tuple(missing)


def _classification_for_route(route: str) -> str:
    mapping = {
        "block_governance_or_public_posture_shortcut": "governance_boundary_block",
        "block_external_action_shortcut": "external_action_block",
        "block_missing_t490_anchor": "missing_prior_gate_block",
        "block_s1_spacetime_or_lorentzian_overclaim": "overclaim_boundary_block",
        "reject_uniform_finite_colimit_rerun": "uniform_baseline_rejection",
        "reject_tail_tuned_measure_restart": "tail_tuned_measure_rejection",
        "reject_guardrail_screen_conditioning_restart": "screen_conditioning_rejection",
        "reject_post_t223_screen_drift_restart": "screen_drift_rejection",
        "reject_single_size_positive_restart": "single_size_rejection",
        "reject_t490_admission_as_evidence_shortcut": "review_admission_overread_rejection",
        "reject_missing_reopen_requirements": "missing_reopen_requirement_rejection",
        "reject_current_finite_route_minor_variant": "current_finite_route_closed",
        "admit_future_independent_measure_law_review_target": "future_measure_law_review_target",
        "admit_future_continuum_bridge_review_target": "future_continuum_bridge_review_target",
        "admit_future_separate_formal_entry_point_review_target": "future_separate_formal_entry_point_review_target",
        "reject_underdeclared_restart": "underdeclared_restart_rejection",
    }
    return mapping.get(route, "unclassified_closure_route")


def _load_t490_result() -> dict[str, Any]:
    path = Path("results") / f"{T490_ARTIFACT_ID}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _t490_anchor_checks(t490: dict[str, Any]) -> dict[str, Any]:
    decisions = {item["packet_id"]: item for item in t490["decisions"]}
    future_minimum = t490["future_packet_minimum"]
    not_earned = t490["not_earned"]
    expected_targets = [
        "synthetic_predeclared_measure_review_target",
        "synthetic_continuum_bridge_weight_target",
    ]
    anchor_ok = (
        t490["artifact_id"] == T490_ARTIFACT_ID
        and t490["verdict"]
        == "S1_NONUNIFORM_MEASURE_PERSISTENCE_GATE_BUILT_SCREEN_CONDITIONING_NOT_ENOUGH"
        and t490["admitted_future_targets"] == expected_targets
        and t490["all_admitted_targets_are_synthetic_only"] is True
        and t490["s1_promoted"] is False
        and t490["t223_reversed"] is False
        and t490["claim_ledger_update"] == "none"
        and decisions["uniform_ordinal_baseline"]["admitted"] is False
        and decisions["known_survivor_tail_indicator"]["admitted"] is False
        and decisions["parent_interval_conditioned_measure"]["admitted"] is False
        and decisions["single_size_n8_positive"]["admitted"] is False
        and "predeclare the nonuniform measure, selection law, sprinkling law, or continuum bridge before scoring survivors"
        in future_minimum
        and "supply an independent finality-native or neighbor-theory generating law"
        in future_minimum
        and "S1 promotion" in not_earned
        and "T223 reversal" in not_earned
        and "spacetime derivation" in not_earned
        and "continuum theorem" in not_earned
    )
    return {
        "artifact_id": t490["artifact_id"],
        "verdict": t490["verdict"],
        "anchor_ok": anchor_ok,
        "admitted_future_targets": t490["admitted_future_targets"],
        "all_admitted_targets_are_synthetic_only": (
            t490["all_admitted_targets_are_synthetic_only"]
        ),
        "s1_promoted": t490["s1_promoted"],
        "t223_reversed": t490["t223_reversed"],
        "claim_ledger_update": t490["claim_ledger_update"],
        "uniform_baseline_rejected": (
            decisions["uniform_ordinal_baseline"]["admitted"] is False
        ),
        "tail_indicator_rejected": (
            decisions["known_survivor_tail_indicator"]["admitted"] is False
        ),
        "guardrail_conditioning_rejected": (
            decisions["parent_interval_conditioned_measure"]["admitted"] is False
        ),
        "single_size_positive_rejected": (
            decisions["single_size_n8_positive"]["admitted"] is False
        ),
        "future_packet_minimum_preserved": (
            "supply an independent finality-native or neighbor-theory generating law"
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


def t491_result_to_dict(result: T491Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "t490_anchor": result.t490_anchor,
        "proposals": [_proposal_to_dict(proposal) for proposal in result.proposals],
        "decisions": [_decision_to_dict(decision) for decision in result.decisions],
        "claim_ledger_update": result.claim_ledger_update,
        "current_finite_route_closed": result.current_finite_route_closed,
        "admitted_future_targets": list(result.admitted_future_targets),
        "rejected_restart_packets": list(result.rejected_restart_packets),
        "strongest_reading": result.strongest_reading,
        "future_reopen_minimum": list(result.future_reopen_minimum),
        "not_earned": list(result.not_earned),
    }


def render_markdown(result: T491Result) -> str:
    """Render T491 results as Markdown."""

    anchor_rows = [
        f"| {key} | {value} |" for key, value in result.t490_anchor.items()
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
                evidence=decision.counts_as_s1_evidence,
                closed=decision.closes_current_finite_route,
                missing=missing,
                notes=notes,
            )
        )
    reopen = [f"- {item}" for item in result.future_reopen_minimum]
    not_earned = [f"- {item}" for item in result.not_earned]

    return "\n".join(
        [
            "# T491 - Post-T490 S1 Finite-Colimit Closure Router - v0.1 results",
            "",
            "> Closure router only. No S1 promotion, T223 reversal, "
            "spacetime derivation, claim-ledger movement, roadmap movement, "
            "README movement, North Star movement, public posture, hard-policy "
            "movement, or cross-repo truth.",
            "",
            "- Spec: `tests/T491-post-t490-s1-finite-colimit-closure-router.md`",
            "- Model: `models/post_t490_s1_finite_colimit_closure_router.py`",
            "- Tests: `tests/test_post_t490_s1_finite_colimit_closure_router.py`",
            "- Artifact JSON: `results/T491-post-t490-s1-finite-colimit-closure-router-v0.1.json`",
            "- Source open problem: `open-problems/spacetime-as-finality-colimit.md`",
            "- Prior gates: T223, T464, and T490",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## T490 Anchor",
            "",
            "| field | value |",
            "| --- | --- |",
            *anchor_rows,
            "",
            "## Closure Decisions",
            "",
            "| proposal | admitted? | route | classification | future target? | counts as S1 evidence? | closes current finite route? | missing requirements | notes |",
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
        "repeats_current_t223_t490_finite_route": (
            proposal.repeats_current_t223_t490_finite_route
        ),
        "cites_t490_anchor": proposal.cites_t490_anchor,
        "declares_t223_t490_context": proposal.declares_t223_t490_context,
        "predeclares_measure_law_or_bridge": (
            proposal.predeclares_measure_law_or_bridge
        ),
        "keeps_finite_screens_fixed": proposal.keeps_finite_screens_fixed,
        "audits_multi_size_or_limit": proposal.audits_multi_size_or_limit,
        "states_nonvanishing_mass_target": (
            proposal.states_nonvanishing_mass_target
        ),
        "names_later_lorentzian_constraints": (
            proposal.names_later_lorentzian_constraints
        ),
        "supplies_positive_controls": proposal.supplies_positive_controls,
        "supplies_hostile_controls": proposal.supplies_hostile_controls,
        "independent_of_t223_t490_finite_route": (
            proposal.independent_of_t223_t490_finite_route
        ),
        "has_independent_measure_law": proposal.has_independent_measure_law,
        "has_continuum_bridge": proposal.has_continuum_bridge,
        "uses_separate_formal_entry_point": (
            proposal.uses_separate_formal_entry_point
        ),
        "uses_uniform_baseline": proposal.uses_uniform_baseline,
        "conditions_on_survivor_success": proposal.conditions_on_survivor_success,
        "conditions_on_guardrail_screen": proposal.conditions_on_guardrail_screen,
        "changes_finite_screens": proposal.changes_finite_screens,
        "uses_single_size_positive": proposal.uses_single_size_positive,
        "uses_t490_admission_as_evidence": proposal.uses_t490_admission_as_evidence,
        "overclaims_s1_spacetime_or_lorentzian_result": (
            proposal.overclaims_s1_spacetime_or_lorentzian_result
        ),
        "requests_claim_or_posture_movement": (
            proposal.requests_claim_or_posture_movement
        ),
        "requires_non_github_external_action": (
            proposal.requires_non_github_external_action
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
        "counts_as_s1_evidence": decision.counts_as_s1_evidence,
        "closes_current_finite_route": decision.closes_current_finite_route,
        "missing_requirements": list(decision.missing_requirements),
        "notes": list(decision.notes),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t491_analysis()
    payload = t491_result_to_dict(result)
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
