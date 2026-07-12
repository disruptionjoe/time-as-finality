"""T537: source-law family and falsifier packet.

T536 selected a Track-1 successor packet after the finite-generator route
paused without falsifying the North Star. T537 generates a small menu of
finality-domain source-law families, requires independent naturality and a
predeclared falsifier for each, and selects one next computable family without
repeating spent finite-generator shapes or importing target spacetime data.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t536_taf11_source_law_successor_router as t536


ARTIFACT = "T537-source-law-family-and-falsifier-packet-v0.1"
VERDICT = "source_law_family_packet_selected_descent_obstruction_resolution_family"
SELECTED_FAMILY = "descent_obstruction_resolution_family"
NEXT_PACKET = "t538_descent_obstruction_resolution_source_law_packet"

SPENT_SHAPES = (
    "two_channel_receipt_product_order",
    "three_channel_receipt_product_order",
    "record_window_separation_order",
    "external_lorentzian_uv_reference_law",
    "t528_screen_conditioned_receipt_mixture",
    "posthoc_repaired_band_fit",
)

NOT_CLAIMED = (
    "T537 does not establish a source law, derive spacetime, prove "
    "manifoldlikeness, repair T528, reverse T223, unpause the S1 "
    "finite-generator route, promote S1, change claim status, change canon, "
    "change public posture, authorize external publication, or move cross-repo "
    "truth. It is a Track-1 source-law family selection packet only."
)


@dataclass(frozen=True)
class SourceLawFamily:
    family_id: str
    description: str
    source_variables: tuple[str, ...]
    naturality_basis: str
    predeclared_falsifier: str
    next_computation: str
    finality_domain_family: bool
    new_relative_to_spent_shapes: bool
    source_variables_declared: bool
    independent_naturality: bool
    predeclared_falsifier_named: bool
    computable_without_target_import: bool
    executable_next_packet_specific: bool
    hostile_controls_named: bool
    later_burdens_named: bool
    repeats_spent_shape: bool = False
    target_density_fit: bool = False
    imports_lorentzian_reference: bool = False
    depends_on_real_data_packet: bool = False
    replaces_track_1_with_track_2: bool = False
    requests_claim_canon_public_or_external_movement: bool = False


@dataclass(frozen=True)
class FamilyDecision:
    family_id: str
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
    blocks_family_ids: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T537Result:
    artifact: str
    source_t536_verdict: str
    source_t536_selected_routes: tuple[str, ...]
    spent_shapes: tuple[str, ...]
    family_decisions: tuple[FamilyDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_family_ids: tuple[str, ...]
    verdict: str
    recommended_next: str
    claim_labels: tuple[ClaimLabel, ...]
    s1_update: str
    claim_ledger_update: str
    not_claimed: str


def run_t537_analysis() -> T537Result:
    t536_result = t536.run_t536_analysis()
    families = _source_law_families()
    decisions = tuple(_evaluate_family(family) for family in families)
    selected = tuple(
        decision.family_id
        for decision in decisions
        if decision.selected_for_next_execution
    )
    verdict = (
        VERDICT
        if t536_result.selected_route_ids == (t536.SELECTED_ROUTE,)
        and selected == (SELECTED_FAMILY,)
        and _family_menu_excludes_spent(families)
        else "source_law_family_packet_unexpected_status"
    )
    return T537Result(
        artifact=ARTIFACT,
        source_t536_verdict=t536_result.verdict,
        source_t536_selected_routes=t536_result.selected_route_ids,
        spent_shapes=SPENT_SHAPES,
        family_decisions=decisions,
        hostile_controls=_hostile_controls(),
        selected_family_ids=selected,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should instantiate finite record-cover "
            "fixtures for the descent-obstruction resolution family, compute "
            "the obstruction-resolution relation before seeing any target "
            "ordering statistic, and reject the family if it collapses under "
            "the predeclared hostile controls."
        ),
        claim_labels=_claim_labels(decisions),
        s1_update=(
            "S1 remains `requires_added_assumption`. T537 selects one "
            "computable source-law family for the next packet and supplies no "
            "S1 evidence."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T537 is TAF11 work selection and "
            "source-family scoping only; it leaves claim rows, Canon Index "
            "tiers, and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t537_result_to_dict(result: T537Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t536_verdict": result.source_t536_verdict,
        "source_t536_selected_routes": list(result.source_t536_selected_routes),
        "spent_shapes": list(result.spent_shapes),
        "family_decisions": [
            {
                "family_id": decision.family_id,
                "outcome": decision.outcome,
                "selected_for_next_execution": decision.selected_for_next_execution,
                "track_role": decision.track_role,
                "missing_requirements": list(decision.missing_requirements),
                "reason": decision.reason,
                "next_packet": decision.next_packet,
                "source_variables": list(decision.source_variables),
                "predeclared_falsifier": decision.predeclared_falsifier,
            }
            for decision in result.family_decisions
        ],
        "hostile_controls": [
            {
                "control_id": control.control_id,
                "blocks_family_ids": list(control.blocks_family_ids),
                "reason": control.reason,
            }
            for control in result.hostile_controls
        ],
        "selected_family_ids": list(result.selected_family_ids),
        "verdict": result.verdict,
        "recommended_next": result.recommended_next,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _source_law_families() -> tuple[SourceLawFamily, ...]:
    return (
        SourceLawFamily(
            family_id=SELECTED_FAMILY,
            description=(
                "Build finite local record covers with restriction maps and "
                "obstruction witnesses. Derive the candidate source relation "
                "from the stage at which local record sections first resolve "
                "their descent obstruction under allowed refinements."
            ),
            source_variables=(
                "local_record_cover",
                "restriction_maps",
                "compatible_local_sections",
                "descent_obstruction_witness",
                "allowed_refinement_steps",
                "resolution_depth",
            ),
            naturality_basis=(
                "Record finality is already tested through local-to-global "
                "restriction, obstruction, and reconstruction debt; resolution "
                "depth is native to that machinery and does not depend on a "
                "target Lorentzian embedding."
            ),
            predeclared_falsifier=(
                "Reject if the relation is not invariant under cover relabeling "
                "and restriction-map isomorphism, if it collapses to total-chain "
                "or antichain controls, or if any density target or Lorentzian "
                "coordinate is needed to choose the relation."
            ),
            next_computation=NEXT_PACKET,
            finality_domain_family=True,
            new_relative_to_spent_shapes=True,
            source_variables_declared=True,
            independent_naturality=True,
            predeclared_falsifier_named=True,
            computable_without_target_import=True,
            executable_next_packet_specific=True,
            hostile_controls_named=True,
            later_burdens_named=True,
        ),
        SourceLawFamily(
            family_id="stabilization_certificate_filtration_family",
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
                "Finality intuitively depends on persistence of reconstruction "
                "certificates across allowed forgetting."
            ),
            predeclared_falsifier=(
                "Reject if certificate equivalence is underdeclared, if the "
                "family reduces to endpoint-window separation, or if the "
                "filtration is tuned from repaired-suite outcomes."
            ),
            next_computation="none",
            finality_domain_family=True,
            new_relative_to_spent_shapes=True,
            source_variables_declared=True,
            independent_naturality=True,
            predeclared_falsifier_named=True,
            computable_without_target_import=True,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            later_burdens_named=True,
        ),
        SourceLawFamily(
            family_id="record_window_separation_rescue_family",
            description=(
                "Try to rescue the T534 record-window endpoint law with more "
                "parameter choices."
            ),
            source_variables=("record_open_endpoint", "record_finalized_endpoint"),
            naturality_basis="Record windows are finality-domain data.",
            predeclared_falsifier=(
                "Already falsified for the T534 target-density burden."
            ),
            next_computation="none",
            finality_domain_family=True,
            new_relative_to_spent_shapes=False,
            source_variables_declared=True,
            independent_naturality=True,
            predeclared_falsifier_named=True,
            computable_without_target_import=True,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            later_burdens_named=True,
            repeats_spent_shape=True,
        ),
        SourceLawFamily(
            family_id="ordering_fraction_target_fit_family",
            description=(
                "Choose a relation because it can be tuned to the repaired-suite "
                "ordering-fraction target."
            ),
            source_variables=("target_ordering_fraction", "posthoc_relation_band"),
            naturality_basis="Target matching only.",
            predeclared_falsifier="Reject because target matching chooses the law.",
            next_computation="none",
            finality_domain_family=False,
            new_relative_to_spent_shapes=False,
            source_variables_declared=True,
            independent_naturality=False,
            predeclared_falsifier_named=True,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            later_burdens_named=False,
            target_density_fit=True,
        ),
        SourceLawFamily(
            family_id="lorentzian_reference_sampler_family",
            description=(
                "Use external 1+1 causal-diamond coordinates as the source law."
            ),
            source_variables=("external_u_coordinate", "external_v_coordinate"),
            naturality_basis="Known reference law calibration.",
            predeclared_falsifier="Reject because the law imports the target.",
            next_computation="none",
            finality_domain_family=False,
            new_relative_to_spent_shapes=False,
            source_variables_declared=True,
            independent_naturality=False,
            predeclared_falsifier_named=True,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            later_burdens_named=False,
            imports_lorentzian_reference=True,
        ),
        SourceLawFamily(
            family_id="real_taf10_data_packet_wait_family",
            description=(
                "Wait for a future C(R) data-bearing packet to replace Track 1."
            ),
            source_variables=("future_full_stack_profile", "future_noncompletion_witness"),
            naturality_basis="Potential Track-2 data value.",
            predeclared_falsifier=(
                "Reject as a Track-1 replacement unless a real TAF10 packet exists."
            ),
            next_computation="none",
            finality_domain_family=False,
            new_relative_to_spent_shapes=True,
            source_variables_declared=False,
            independent_naturality=False,
            predeclared_falsifier_named=True,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=False,
            later_burdens_named=False,
            depends_on_real_data_packet=True,
            replaces_track_1_with_track_2=True,
        ),
    )


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="isomorphic_cover_relabel_control",
            blocks_family_ids=(),
            reason=(
                "A selected family must give the same decision under cover "
                "relabeling and restriction-map isomorphism."
            ),
        ),
        HostileControl(
            control_id="total_chain_and_antichain_collapse_control",
            blocks_family_ids=(),
            reason=(
                "A selected family must not succeed only by collapsing every "
                "fixture to a total chain or an antichain."
            ),
        ),
        HostileControl(
            control_id="spent_shape_replay_control",
            blocks_family_ids=("record_window_separation_rescue_family",),
            reason="Spent finite-generator and endpoint-window shapes do not re-enter TAF11.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks_family_ids=(
                "ordering_fraction_target_fit_family",
                "lorentzian_reference_sampler_family",
            ),
            reason=(
                "A source law must be chosen before target statistics or "
                "Lorentzian coordinates are read."
            ),
        ),
    )


def _evaluate_family(family: SourceLawFamily) -> FamilyDecision:
    missing = _missing_requirements(family)
    if family.requests_claim_canon_public_or_external_movement:
        outcome = "BLOCKED_GOVERNANCE"
        selected = False
        role = "forbidden"
        reason = "A source-family packet cannot move claims, canon, public posture, or external state."
        next_packet = "none"
    elif family.repeats_spent_shape:
        outcome = "REJECTED_DUPLICATE"
        selected = False
        role = "spent"
        reason = "The family repeats a shape already spent by T532/T534."
        next_packet = "none"
    elif family.target_density_fit:
        outcome = "BLOCKED_TARGET_IMPORT"
        selected = False
        role = "blocked"
        reason = "The family chooses the law from the target statistic."
        next_packet = "none"
    elif family.imports_lorentzian_reference:
        outcome = "BLOCKED_TARGET_IMPORT"
        selected = False
        role = "blocked"
        reason = "The family imports the target Lorentzian reference law."
        next_packet = "none"
    elif family.depends_on_real_data_packet and family.replaces_track_1_with_track_2:
        outcome = "PAUSED_TRACK_2"
        selected = False
        role = "track_2_waiting"
        reason = "T535 found no real data-bearing packet, and Track 2 cannot replace Track 1."
        next_packet = "none"
    elif missing:
        outcome = "REVIEW_ONLY"
        selected = False
        role = "underdeclared_family"
        reason = "The family is useful context but lacks one or more T537 execution requirements."
        next_packet = "none"
    else:
        outcome = "SELECTED_FOR_EXECUTION"
        selected = True
        role = "track_1_next_family"
        reason = (
            "The family is finality-domain native, new relative to spent shapes, "
            "computable without target import, and carries an explicit falsifier."
        )
        next_packet = family.next_computation
    return FamilyDecision(
        family_id=family.family_id,
        outcome=outcome,
        selected_for_next_execution=selected,
        track_role=role,
        missing_requirements=missing,
        reason=reason,
        next_packet=next_packet,
        source_variables=family.source_variables,
        predeclared_falsifier=family.predeclared_falsifier,
    )


def _missing_requirements(family: SourceLawFamily) -> tuple[str, ...]:
    missing: list[str] = []
    if not family.finality_domain_family:
        missing.append("finality_domain_family")
    if not family.new_relative_to_spent_shapes:
        missing.append("new_relative_to_spent_shapes")
    if not family.source_variables_declared:
        missing.append("source_variables_declared")
    if not family.independent_naturality:
        missing.append("independent_naturality")
    if not family.predeclared_falsifier_named:
        missing.append("predeclared_falsifier")
    if not family.computable_without_target_import:
        missing.append("computable_without_target_import")
    if not family.executable_next_packet_specific:
        missing.append("executable_next_packet_specific")
    if not family.hostile_controls_named:
        missing.append("hostile_controls_named")
    if not family.later_burdens_named:
        missing.append("later_burdens_named")
    if family.repeats_spent_shape:
        missing.append("no_spent_shape_repeat")
    if family.target_density_fit:
        missing.append("no_target_density_fit")
    if family.imports_lorentzian_reference:
        missing.append("no_lorentzian_reference_import")
    if family.depends_on_real_data_packet:
        missing.append("not_blocked_on_real_data_packet")
    if family.replaces_track_1_with_track_2:
        missing.append("track_2_does_not_replace_track_1")
    if family.requests_claim_canon_public_or_external_movement:
        missing.append("no_claim_canon_public_or_external_movement")
    return tuple(missing)


def _family_menu_excludes_spent(families: tuple[SourceLawFamily, ...]) -> bool:
    selected_ids = {
        family.family_id
        for family in families
        if family.family_id == SELECTED_FAMILY
    }
    return selected_ids == {SELECTED_FAMILY} and all(
        not family.repeats_spent_shape
        and not family.target_density_fit
        and not family.imports_lorentzian_reference
        for family in families
        if family.family_id == SELECTED_FAMILY
    )


def _claim_labels(decisions: tuple[FamilyDecision, ...]) -> tuple[ClaimLabel, ...]:
    selected = tuple(
        decision for decision in decisions if decision.selected_for_next_execution
    )
    rejected_ids = tuple(
        decision.family_id
        for decision in decisions
        if decision.outcome
        in {"REJECTED_DUPLICATE", "BLOCKED_TARGET_IMPORT", "PAUSED_TRACK_2"}
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T536 is consumed as selecting the source-law family and "
                "falsifier packet route."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Exactly one T537 family is selected: {selected[0].family_id}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Spent-shape replay, target-density fitting, Lorentzian "
                "reference import, and Track-2 replacement are rejected or paused: "
                + ", ".join(rejected_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The descent-obstruction family is the best next source-law "
                "candidate because it uses record-cover, restriction, and "
                "obstruction-resolution data already native to the TaF proof "
                "program while remaining falsifiable before target import."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T537 Results: Source-Law Family And Falsifier Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source T536 verdict: `{payload['source_t536_verdict']}`",
        "- Source T536 selected routes: "
        + (
            ", ".join(f"`{item}`" for item in payload["source_t536_selected_routes"])
            or "none"
        ),
        "- Selected family ids: "
        + (", ".join(f"`{item}`" for item in payload["selected_family_ids"]) or "none"),
        "",
        "## Spent Shapes Excluded From Selection",
        "",
    ]
    lines.extend(f"- `{shape}`" for shape in payload["spent_shapes"])
    lines.extend(
        [
            "",
            "## Family Decisions",
            "",
            "| family | outcome | selected? | role | missing requirements | next packet | reason |",
            "| --- | --- | :---: | --- | --- | --- | --- |",
        ]
    )
    for decision in payload["family_decisions"]:
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['family_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected_for_next_execution']} | "
            f"`{decision['track_role']}` | "
            f"{missing} | "
            f"`{decision['next_packet']}` | "
            f"{decision['reason']} |"
        )
    lines.extend(["", "## Selected Family Contract", ""])
    selected = next(
        decision
        for decision in payload["family_decisions"]
        if decision["selected_for_next_execution"]
    )
    lines.extend(
        [
            f"- Family: `{selected['family_id']}`",
            "- Source variables: "
            + ", ".join(f"`{item}`" for item in selected["source_variables"]),
            f"- Predeclared falsifier: {selected['predeclared_falsifier']}",
        ]
    )
    lines.extend(
        [
            "",
            "## Hostile Controls",
            "",
            "| control | blocks families | reason |",
            "| --- | --- | --- |",
        ]
    )
    for control in payload["hostile_controls"]:
        blocked = ", ".join(f"`{item}`" for item in control["blocks_family_ids"]) or "none"
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
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = t537_result_to_dict(run_t537_analysis())
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T537-source-law-family-and-falsifier-packet-v0.1.json"
        md_path = (
            results_dir
            / "T537-source-law-family-and-falsifier-packet-v0.1-results.md"
        )
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
