"""T542: post-retirement source-law reassessment router.

T539 retired the descent-obstruction resolution family as a programmable rank
channel. T541 built the TAF8 witness-packet gate, but explicitly left TAF8
waiting for a real domain-native packet. T542 routes the next honest swing:
choose a non-rank, finality-native TAF11 successor packet only if it is
computable without target import and carries falsifiers before execution.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t539_resolution_depth_generator_packet as t539
from models import t541_nonidentity_shadow_protection_witness_packet as t541


ARTIFACT = "T542-post-retirement-source-law-reassessment-router-v0.1"
VERDICT = "taf11_post_retirement_router_selected_aprd_descent_packet"
SELECTED_FAMILY = "aprd_reconstruction_boundary_descent_family"
NEXT_PACKET = "t543_aprd_reconstruction_boundary_descent_packet"

NOT_CLAIMED = (
    "T542 does not establish a source law, prove a shadow-protection theorem, "
    "derive spacetime, prove manifoldlikeness, repair T528, reverse T223, "
    "unpause S1, promote S1, change claim status, change Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, or move cross-repo truth. It is a "
    "post-retirement source-law work-selection router only."
)


@dataclass(frozen=True)
class SuccessorCandidate:
    candidate_id: str
    description: str
    source_variables: tuple[str, ...]
    naturality_basis: str
    predeclared_falsifier: str
    next_packet: str
    finality_native: bool
    new_after_t539_retirement: bool
    non_rank_source_law_family: bool
    source_variables_declared: bool
    independent_naturality: bool
    predeclared_falsifier_named: bool
    computable_without_target_import: bool
    executable_next_packet_specific: bool
    hostile_controls_named: bool
    bridge_to_taf8_or_taf11_burdens: bool
    consumes_t539_retirement: bool
    respects_t541_wait_state: bool
    repeats_retired_t539_family: bool = False
    repeats_spent_finite_generator_shape: bool = False
    imports_target_statistic_or_lorentzian_reference: bool = False
    depends_on_real_data_packet: bool = False
    replaces_track_1_with_track_2: bool = False
    requires_domain_native_taf8_packet: bool = False
    domain_native_taf8_packet_in_hand: bool = False
    requests_claim_canon_public_or_external_movement: bool = False


@dataclass(frozen=True)
class CandidateDecision:
    candidate_id: str
    outcome: str
    selected_for_next_execution: bool
    track_role: str
    missing_requirements: tuple[str, ...]
    reason: str
    next_packet: str
    source_variables: tuple[str, ...]
    predeclared_falsifier: str


@dataclass(frozen=True)
class HostileControl:
    control_id: str
    blocks_candidate_ids: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T542Result:
    artifact: str
    source_t539_verdict: str
    source_t539_family_status: str
    source_t541_verdict: str
    source_t541_taf8_status: str
    candidate_decisions: tuple[CandidateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_family_ids: tuple[str, ...]
    verdict: str
    recommended_next: str
    taf8_update: str
    taf11_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t542_analysis() -> T542Result:
    t539_result = t539.run_t539_analysis()
    t541_payload = t541.run_t541_analysis()
    candidates = _successor_candidates()
    decisions = tuple(_evaluate_candidate(candidate) for candidate in candidates)
    selected = tuple(
        decision.candidate_id
        for decision in decisions
        if decision.selected_for_next_execution
    )
    verdict = (
        VERDICT
        if t539_result.family_status == t539.FAMILY_STATUS
        and t541_payload["taf8_status"] == t541.TAF8_STATUS
        and selected == (SELECTED_FAMILY,)
        else "taf11_post_retirement_router_unexpected_status"
    )
    return T542Result(
        artifact=ARTIFACT,
        source_t539_verdict=t539_result.verdict,
        source_t539_family_status=t539_result.family_status,
        source_t541_verdict=t541_payload["verdict"],
        source_t541_taf8_status=t541_payload["taf8_status"],
        candidate_decisions=decisions,
        hostile_controls=_hostile_controls(),
        selected_family_ids=selected,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should define APRD as an access/provenance "
            "reconstruction-boundary object, test whether it reproduces the "
            "T19, T66, and T51/T58-style projection/descent burdens without a "
            "scalar rank proxy, and reject if target statistics or Lorentzian "
            "coordinates are needed to choose the relation."
        ),
        taf8_update=(
            "TAF8 remains open but waiting. T541 supplies the review gate; T542 "
            "does not run TAF8 because no real domain-native packet is in hand."
        ),
        taf11_update=(
            "TAF11 receives a new non-rank successor route: APRD / "
            "reconstruction-boundary descent. The retired T539 route stays "
            "retired."
        ),
        claim_labels=_claim_labels(decisions),
        claim_ledger_update=(
            "No claim-ledger update is earned. T542 is work selection and "
            "source-family scoping only; it leaves claim rows, Canon Index tiers, "
            "and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t542_result_to_dict(result: T542Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t539_verdict": result.source_t539_verdict,
        "source_t539_family_status": result.source_t539_family_status,
        "source_t541_verdict": result.source_t541_verdict,
        "source_t541_taf8_status": result.source_t541_taf8_status,
        "candidate_decisions": [
            {
                "candidate_id": decision.candidate_id,
                "outcome": decision.outcome,
                "selected_for_next_execution": decision.selected_for_next_execution,
                "track_role": decision.track_role,
                "missing_requirements": list(decision.missing_requirements),
                "reason": decision.reason,
                "next_packet": decision.next_packet,
                "source_variables": list(decision.source_variables),
                "predeclared_falsifier": decision.predeclared_falsifier,
            }
            for decision in result.candidate_decisions
        ],
        "hostile_controls": [
            {
                "control_id": control.control_id,
                "blocks_candidate_ids": list(control.blocks_candidate_ids),
                "reason": control.reason,
            }
            for control in result.hostile_controls
        ],
        "selected_family_ids": list(result.selected_family_ids),
        "verdict": result.verdict,
        "recommended_next": result.recommended_next,
        "taf8_update": result.taf8_update,
        "taf11_update": result.taf11_update,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _successor_candidates() -> tuple[SuccessorCandidate, ...]:
    return (
        SuccessorCandidate(
            candidate_id=SELECTED_FAMILY,
            description=(
                "Define accessible provenance reconstruction debt as the next "
                "source object: compare what an access profile can reconstruct "
                "from local provenance sections against the descent object that "
                "would be needed to preserve capability."
            ),
            source_variables=(
                "access_profile",
                "provenance_axis",
                "local_record_section",
                "calibration_section",
                "reconstruction_boundary",
                "descent_gap",
                "native_absorber_outcome",
            ),
            naturality_basis=(
                "The branch map names APRD / reconstruction-boundary plus "
                "effective descent as the strongest mathematical feeder after "
                "T539. It uses access, provenance, local-to-global obstruction, "
                "and capability preservation data rather than scalar record rank."
            ),
            predeclared_falsifier=(
                "Reject if APRD reduces to scalar rank/order, if it cannot be "
                "computed before reading target statistics, if the T19/T66 and "
                "T51/T58-style projection/descent burdens are not reproduced in "
                "the declared fixtures, or if native absorbers explain the split."
            ),
            next_packet=NEXT_PACKET,
            finality_native=True,
            new_after_t539_retirement=True,
            non_rank_source_law_family=True,
            source_variables_declared=True,
            independent_naturality=True,
            predeclared_falsifier_named=True,
            computable_without_target_import=True,
            executable_next_packet_specific=True,
            hostile_controls_named=True,
            bridge_to_taf8_or_taf11_burdens=True,
            consumes_t539_retirement=True,
            respects_t541_wait_state=True,
        ),
        SuccessorCandidate(
            candidate_id="taf8_domain_native_packet_execution",
            description=(
                "Run the T541 shadow-protection theorem gate immediately."
            ),
            source_variables=("future_domain_native_packet",),
            naturality_basis="T541 already supplies the gate shape.",
            predeclared_falsifier=(
                "Reject unless the packet is domain-native and clears the T541 "
                "nonidentity, typed-gap, preservation, and absorber burdens."
            ),
            next_packet="none",
            finality_native=True,
            new_after_t539_retirement=True,
            non_rank_source_law_family=False,
            source_variables_declared=False,
            independent_naturality=True,
            predeclared_falsifier_named=True,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf8_or_taf11_burdens=True,
            consumes_t539_retirement=True,
            respects_t541_wait_state=False,
            requires_domain_native_taf8_packet=True,
            domain_native_taf8_packet_in_hand=False,
        ),
        SuccessorCandidate(
            candidate_id="descent_obstruction_resolution_family_replay",
            description=(
                "Rerun the T537/T538/T539 descent-obstruction resolution family "
                "with a different wrapper."
            ),
            source_variables=("resolution_depth", "compatible_local_sections"),
            naturality_basis="Previously selected source-family route.",
            predeclared_falsifier=(
                "Already failed: T539 found only a programmable scalar rank channel."
            ),
            next_packet="none",
            finality_native=True,
            new_after_t539_retirement=False,
            non_rank_source_law_family=False,
            source_variables_declared=True,
            independent_naturality=True,
            predeclared_falsifier_named=True,
            computable_without_target_import=True,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf8_or_taf11_burdens=True,
            consumes_t539_retirement=False,
            respects_t541_wait_state=True,
            repeats_retired_t539_family=True,
        ),
        SuccessorCandidate(
            candidate_id="stabilization_certificate_filtration_family",
            description=(
                "Order records by persistence of stabilization certificates "
                "through a nested finality filtration."
            ),
            source_variables=(
                "record_token",
                "stabilization_certificate",
                "filtration_level",
                "persistence_window",
            ),
            naturality_basis=(
                "Finality depends on persistence of reconstruction certificates "
                "across allowed forgetting."
            ),
            predeclared_falsifier=(
                "Reject if certificate equivalence is underdeclared, if the "
                "family reduces to endpoint-window separation, or if filtration "
                "levels are tuned from target outcomes."
            ),
            next_packet="none",
            finality_native=True,
            new_after_t539_retirement=True,
            non_rank_source_law_family=False,
            source_variables_declared=True,
            independent_naturality=True,
            predeclared_falsifier_named=True,
            computable_without_target_import=True,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf8_or_taf11_burdens=False,
            consumes_t539_retirement=True,
            respects_t541_wait_state=True,
        ),
        SuccessorCandidate(
            candidate_id="observerse_protocol_stack_ablation_family",
            description=(
                "Predeclare an observerse protocol stack and ablate each layer "
                "to test whether S1 failed because isolated finite generators "
                "were the wrong unit."
            ),
            source_variables=(
                "issuance_layer",
                "access_control_layer",
                "admissibility_layer",
                "provenance_layer",
                "governance_layer",
            ),
            naturality_basis=(
                "The branch map marks protocol-stack ablation as high-upside but "
                "risky until the minimal stack and collapse modes are declared."
            ),
            predeclared_falsifier=(
                "Reject if layers are post-hoc, if ablations do not have predicted "
                "collapse modes, or if the stack merely explains away prior S1 negatives."
            ),
            next_packet="none",
            finality_native=True,
            new_after_t539_retirement=True,
            non_rank_source_law_family=True,
            source_variables_declared=True,
            independent_naturality=True,
            predeclared_falsifier_named=True,
            computable_without_target_import=True,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf8_or_taf11_burdens=False,
            consumes_t539_retirement=True,
            respects_t541_wait_state=True,
        ),
        SuccessorCandidate(
            candidate_id="ordering_fraction_target_refit_family",
            description=(
                "Change the ordering-fraction target statistic or fit a relation "
                "because it matches the repaired suite."
            ),
            source_variables=("target_ordering_fraction", "posthoc_relation_band"),
            naturality_basis="Target matching only.",
            predeclared_falsifier="Reject because target matching chooses the law.",
            next_packet="none",
            finality_native=False,
            new_after_t539_retirement=False,
            non_rank_source_law_family=False,
            source_variables_declared=True,
            independent_naturality=False,
            predeclared_falsifier_named=True,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf8_or_taf11_burdens=False,
            consumes_t539_retirement=False,
            respects_t541_wait_state=True,
            imports_target_statistic_or_lorentzian_reference=True,
        ),
        SuccessorCandidate(
            candidate_id="taf12_real_packet_wait_family",
            description=(
                "Wait for a future C(R) data-bearing packet to replace the Track-1 "
                "source-law question."
            ),
            source_variables=("future_full_stack_profile", "future_noncompletion_witness"),
            naturality_basis="Potential Track-2 data value.",
            predeclared_falsifier=(
                "Reject as a Track-1 replacement unless a real TAF10/TAF12 packet exists."
            ),
            next_packet="none",
            finality_native=False,
            new_after_t539_retirement=True,
            non_rank_source_law_family=False,
            source_variables_declared=False,
            independent_naturality=False,
            predeclared_falsifier_named=True,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=False,
            bridge_to_taf8_or_taf11_burdens=False,
            consumes_t539_retirement=True,
            respects_t541_wait_state=True,
            depends_on_real_data_packet=True,
            replaces_track_1_with_track_2=True,
        ),
        SuccessorCandidate(
            candidate_id="s1_claim_or_public_posture_shortcut",
            description=(
                "Treat T539 or T541 as reason to move S1, claims, canon, or "
                "public posture."
            ),
            source_variables=(),
            naturality_basis="none",
            predeclared_falsifier="Blocked by governance.",
            next_packet="none",
            finality_native=False,
            new_after_t539_retirement=False,
            non_rank_source_law_family=False,
            source_variables_declared=False,
            independent_naturality=False,
            predeclared_falsifier_named=False,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=False,
            bridge_to_taf8_or_taf11_burdens=False,
            consumes_t539_retirement=False,
            respects_t541_wait_state=False,
            requests_claim_canon_public_or_external_movement=True,
        ),
    )


def _evaluate_candidate(candidate: SuccessorCandidate) -> CandidateDecision:
    missing = _missing_requirements(candidate)
    if candidate.requests_claim_canon_public_or_external_movement:
        outcome = "BLOCKED_GOVERNANCE"
        selected = False
        role = "forbidden"
        reason = "A router cannot move claims, canon, public posture, or external state."
        next_packet = "none"
    elif candidate.requires_domain_native_taf8_packet and not candidate.domain_native_taf8_packet_in_hand:
        outcome = "PAUSED_TAF8_WAITING_FOR_DOMAIN_NATIVE_PACKET"
        selected = False
        role = "taf8_waiting"
        reason = "T541 says to use the gate only when a real domain-native packet exists."
        next_packet = "none"
    elif candidate.repeats_retired_t539_family:
        outcome = "REJECTED_RETIRED_T539_ROUTE"
        selected = False
        role = "retired"
        reason = "T539 retired this route as a programmable scalar rank channel."
        next_packet = "none"
    elif candidate.repeats_spent_finite_generator_shape:
        outcome = "REJECTED_DUPLICATE"
        selected = False
        role = "spent"
        reason = "The candidate repeats a spent finite-generator shape."
        next_packet = "none"
    elif candidate.imports_target_statistic_or_lorentzian_reference:
        outcome = "BLOCKED_TARGET_IMPORT"
        selected = False
        role = "blocked"
        reason = "The candidate chooses the law from target statistics or Lorentzian data."
        next_packet = "none"
    elif candidate.depends_on_real_data_packet and candidate.replaces_track_1_with_track_2:
        outcome = "PAUSED_TRACK_2"
        selected = False
        role = "track_2_waiting"
        reason = "No real data-bearing packet is in hand, and Track 2 cannot replace Track 1."
        next_packet = "none"
    elif missing:
        outcome = "REVIEW_ONLY"
        selected = False
        role = "underdeclared_or_feeder"
        reason = "The candidate is useful context but lacks one or more T542 execution requirements."
        next_packet = "none"
    else:
        outcome = "SELECTED_FOR_EXECUTION"
        selected = True
        role = "track_1_next_family"
        reason = (
            "The candidate is finality-native, non-rank, new after T539, "
            "computable without target import, and specific enough for the next packet."
        )
        next_packet = candidate.next_packet
    return CandidateDecision(
        candidate_id=candidate.candidate_id,
        outcome=outcome,
        selected_for_next_execution=selected,
        track_role=role,
        missing_requirements=missing,
        reason=reason,
        next_packet=next_packet,
        source_variables=candidate.source_variables,
        predeclared_falsifier=candidate.predeclared_falsifier,
    )


def _missing_requirements(candidate: SuccessorCandidate) -> tuple[str, ...]:
    missing: list[str] = []
    if not candidate.finality_native:
        missing.append("finality_native")
    if not candidate.new_after_t539_retirement:
        missing.append("new_after_t539_retirement")
    if not candidate.non_rank_source_law_family:
        missing.append("non_rank_source_law_family")
    if not candidate.source_variables_declared:
        missing.append("source_variables_declared")
    if not candidate.independent_naturality:
        missing.append("independent_naturality")
    if not candidate.predeclared_falsifier_named:
        missing.append("predeclared_falsifier")
    if not candidate.computable_without_target_import:
        missing.append("computable_without_target_import")
    if not candidate.executable_next_packet_specific:
        missing.append("executable_next_packet_specific")
    if not candidate.hostile_controls_named:
        missing.append("hostile_controls_named")
    if not candidate.bridge_to_taf8_or_taf11_burdens:
        missing.append("bridge_to_taf8_or_taf11_burdens")
    if not candidate.consumes_t539_retirement:
        missing.append("consumes_t539_retirement")
    if not candidate.respects_t541_wait_state:
        missing.append("respects_t541_wait_state")
    if candidate.repeats_retired_t539_family:
        missing.append("no_retired_t539_family_replay")
    if candidate.repeats_spent_finite_generator_shape:
        missing.append("no_spent_finite_generator_replay")
    if candidate.imports_target_statistic_or_lorentzian_reference:
        missing.append("no_target_or_lorentzian_import")
    if candidate.depends_on_real_data_packet:
        missing.append("not_blocked_on_real_data_packet")
    if candidate.replaces_track_1_with_track_2:
        missing.append("track_2_does_not_replace_track_1")
    if candidate.requires_domain_native_taf8_packet and not candidate.domain_native_taf8_packet_in_hand:
        missing.append("domain_native_taf8_packet_in_hand")
    if candidate.requests_claim_canon_public_or_external_movement:
        missing.append("no_claim_canon_public_or_external_movement")
    return tuple(missing)


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="t539_retired_family_control",
            blocks_candidate_ids=("descent_obstruction_resolution_family_replay",),
            reason=(
                "The descent-obstruction resolution family remains retired unless "
                "a genuinely non-rank generator is supplied."
            ),
        ),
        HostileControl(
            control_id="t541_taf8_wait_state_control",
            blocks_candidate_ids=("taf8_domain_native_packet_execution",),
            reason=(
                "T541's gate is executable only when a real domain-native packet is available."
            ),
        ),
        HostileControl(
            control_id="no_scalar_rank_proxy_control",
            blocks_candidate_ids=(
                "descent_obstruction_resolution_family_replay",
                "stabilization_certificate_filtration_family",
            ),
            reason="The next TAF11 successor must not be another scalar rank or filtration proxy.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks_candidate_ids=("ordering_fraction_target_refit_family",),
            reason="A source law must be chosen before target statistics or Lorentzian data are read.",
        ),
        HostileControl(
            control_id="track_2_replacement_control",
            blocks_candidate_ids=("taf12_real_packet_wait_family",),
            reason="A future data-bearing packet may help, but it cannot replace Track 1 now.",
        ),
        HostileControl(
            control_id="governance_posture_control",
            blocks_candidate_ids=("s1_claim_or_public_posture_shortcut",),
            reason="Routers do not move claims, canon, public posture, or external state.",
        ),
    )


def _claim_labels(decisions: tuple[CandidateDecision, ...]) -> tuple[ClaimLabel, ...]:
    selected = tuple(d for d in decisions if d.selected_for_next_execution)
    blocked = tuple(
        d.candidate_id
        for d in decisions
        if d.outcome
        in {
            "PAUSED_TAF8_WAITING_FOR_DOMAIN_NATIVE_PACKET",
            "REJECTED_RETIRED_T539_ROUTE",
            "BLOCKED_TARGET_IMPORT",
            "PAUSED_TRACK_2",
            "BLOCKED_GOVERNANCE",
        }
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T539 is consumed as retiring the current descent-obstruction "
                "resolution family."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T541 is consumed as leaving TAF8 waiting for a real "
                "domain-native packet."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Exactly one T542 successor is selected: {selected[0].candidate_id}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "TAF8 immediate execution, retired-family replay, target import, "
                "Track-2 replacement, and governance shortcuts are blocked or paused: "
                + ", ".join(blocked)
                + "."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "APRD / reconstruction-boundary descent is the best next "
                "Track-1 packet because it uses access, provenance, and descent "
                "burdens directly rather than scalar rank, while still feeding "
                "the TAF8 shadow-protection question."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T542 Results: Post-Retirement Source-Law Reassessment Router",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source T539 verdict: `{payload['source_t539_verdict']}`",
        f"- Source T539 family status: `{payload['source_t539_family_status']}`",
        f"- Source T541 verdict: `{payload['source_t541_verdict']}`",
        f"- Source T541 TAF8 status: `{payload['source_t541_taf8_status']}`",
        "- Selected family ids: "
        + (", ".join(f"`{item}`" for item in payload["selected_family_ids"]) or "none"),
        "",
        "## Candidate Decisions",
        "",
        "| candidate | outcome | selected? | role | missing requirements | next packet | reason |",
        "| --- | --- | :---: | --- | --- | --- | --- |",
    ]
    for decision in payload["candidate_decisions"]:
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['candidate_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected_for_next_execution']} | "
            f"`{decision['track_role']}` | "
            f"{missing} | "
            f"`{decision['next_packet']}` | "
            f"{decision['reason']} |"
        )
    selected = next(
        decision
        for decision in payload["candidate_decisions"]
        if decision["selected_for_next_execution"]
    )
    lines.extend(
        [
            "",
            "## Selected Family Contract",
            "",
            f"- Family: `{selected['candidate_id']}`",
            "- Source variables: "
            + ", ".join(f"`{item}`" for item in selected["source_variables"]),
            f"- Predeclared falsifier: {selected['predeclared_falsifier']}",
            "",
            "## Hostile Controls",
            "",
            "| control | blocks candidates | reason |",
            "| --- | --- | --- |",
        ]
    )
    for control in payload["hostile_controls"]:
        blocked = ", ".join(f"`{item}`" for item in control["blocks_candidate_ids"]) or "none"
        lines.append(
            "| "
            f"`{control['control_id']}` | "
            f"{blocked} | "
            f"{control['reason']} |"
        )
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Recommended Next", "recommended_next"),
        ("TAF8 Update", "taf8_update"),
        ("TAF11 Update", "taf11_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def write_results(result: T542Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t542_result_to_dict(result)
    json_path = results_dir / "T542-post-retirement-source-law-reassessment-router-v0.1.json"
    md_path = results_dir / "T542-post-retirement-source-law-reassessment-router-v0.1-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t542_analysis()
    payload = t542_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
