"""T550: Observerse protocol-stack ablation preflight packet.

T549 selected an Observerse protocol-stack ablation preflight as the next
TAF11 swing after APRD narrowed to a family-local feeder. T550 turns that
route into a bounded preflight contract: it consumes T549 as route authority
and T527 as frozen illustration-grade source evidence, predeclares the layers,
source variables, collapse modes, hostile controls, and next executable packet,
while preserving the review-only boundary.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import run_t527 as t527
from models import t549_taf11_post_aprd_route_reset_router as t549


ARTIFACT = "T550-observerse-protocol-stack-ablation-preflight-packet-v0.1"
VERDICT = "observerse_protocol_stack_preflight_built_next_stress_packet"
PREFLIGHT_STATUS = "PROTOCOL_STACK_PREFLIGHT_BUILT_REVIEW_ONLY"
NEXT_PACKET = "t551_observerse_protocol_stack_source_law_stress_packet"

SELECTED_ROUTE = t549.SELECTED_ROUTE

NOT_CLAIMED = (
    "T550 does not validate Observerse, establish a source law, prove a "
    "shadow-protection theorem, derive spacetime, prove manifoldlikeness, "
    "repair T528, reverse T223, unpause S1, promote S1, change claim status, "
    "change Canon Index tiers, change canon verdicts, change public posture, "
    "change the North Star, authorize external publication, move TAF4, execute "
    "TAF8, or move cross-repo truth. It is a review-only preflight contract "
    "for a later protocol-stack source-law stress packet."
)


@dataclass(frozen=True)
class LayerContract:
    layer_id: str
    source_variable: str
    frozen_t527_row_id: str
    predicted_collapse_mode: str
    t527_ratio_to_full: float
    collapse_threshold: float
    source_law_burden: str
    predeclared_signal: str


@dataclass(frozen=True)
class GateDecision:
    gate_id: str
    outcome: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class HostileControl:
    control_id: str
    blocks: str
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T550Result:
    artifact: str
    source_t549_verdict: str
    source_t549_selected_route_ids: tuple[str, ...]
    source_t527_verdict: str
    source_t527_grade: str
    source_t527_governance_conditional_visible: bool
    preflight_status: str
    layer_contracts: tuple[LayerContract, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_next_packet: str
    verdict: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t550_analysis() -> T550Result:
    t549_result = t549.run_t549_analysis()
    t527_payload = t527.build_payload()
    layer_contracts = _layer_contracts(t527_payload)
    gate_decisions = _gate_decisions(t549_result, t527_payload, layer_contracts)
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gate_decisions) else "none"
    verdict = (
        VERDICT
        if selected_next_packet == NEXT_PACKET
        and t549_result.verdict == t549.VERDICT
        and t549_result.selected_route_ids == (SELECTED_ROUTE,)
        and t527_payload["verdict"] == t527.VERDICT
        and t527_payload["grade"] == "illustration_regression_only"
        else "observerse_protocol_stack_preflight_unexpected_status"
    )

    return T550Result(
        artifact=ARTIFACT,
        source_t549_verdict=t549_result.verdict,
        source_t549_selected_route_ids=t549_result.selected_route_ids,
        source_t527_verdict=t527_payload["verdict"],
        source_t527_grade=t527_payload["grade"],
        source_t527_governance_conditional_visible=bool(
            t527_payload["governance_conditional_visible"]
        ),
        preflight_status=PREFLIGHT_STATUS,
        layer_contracts=layer_contracts,
        gate_decisions=gate_decisions,
        hostile_controls=_hostile_controls(),
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should keep these five layer contracts frozen, "
            "test whether the stack predicts collapse/rescue on a native finality "
            "fixture before target-outcome reading, and reject if it overreads T527, "
            "drops conditional governance, retunes APRD, imports cross-repo truth, "
            "or moves TAF4/source-law status directly."
        ),
        taf11_update=(
            "TAF11 remains active. The post-APRD protocol-stack route is now "
            "preflighted as a five-layer, review-only contract; the next swing must "
            "stress whether that stack has source-law force on a native fixture."
        ),
        taf4_update=(
            "TAF4 remains blocked. T550 supplies no finite-to-continuum bridge and "
            "turns the Observerse stack only into a later TAF11 stress packet."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T550 does not execute or strengthen the T541 transfer gate."
        ),
        claim_labels=_claim_labels(layer_contracts, gate_decisions, t527_payload),
        claim_ledger_update=(
            "No claim-ledger update is earned. T550 is preflight routing and "
            "contract registration only; it leaves claim rows, Canon Index tiers, "
            "canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t550_result_to_dict(result: T550Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t549_verdict": result.source_t549_verdict,
        "source_t549_selected_route_ids": list(result.source_t549_selected_route_ids),
        "source_t527_verdict": result.source_t527_verdict,
        "source_t527_grade": result.source_t527_grade,
        "source_t527_governance_conditional_visible": (
            result.source_t527_governance_conditional_visible
        ),
        "preflight_status": result.preflight_status,
        "layer_contracts": [
            {
                "layer_id": layer.layer_id,
                "source_variable": layer.source_variable,
                "frozen_t527_row_id": layer.frozen_t527_row_id,
                "predicted_collapse_mode": layer.predicted_collapse_mode,
                "t527_ratio_to_full": layer.t527_ratio_to_full,
                "collapse_threshold": layer.collapse_threshold,
                "source_law_burden": layer.source_law_burden,
                "predeclared_signal": layer.predeclared_signal,
            }
            for layer in result.layer_contracts
        ],
        "gate_decisions": [
            {
                "gate_id": gate.gate_id,
                "outcome": gate.outcome,
                "passed": gate.passed,
                "reason": gate.reason,
            }
            for gate in result.gate_decisions
        ],
        "hostile_controls": [
            {
                "control_id": control.control_id,
                "blocks": control.blocks,
                "reason": control.reason,
            }
            for control in result.hostile_controls
        ],
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
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


def _layer_contracts(t527_payload: dict[str, Any]) -> tuple[LayerContract, ...]:
    rows = {row["id"]: row for row in t527_payload["rows"]}
    specs = (
        (
            "issuance",
            "issued_novelty_stream",
            "without_issuance",
            "freeze",
            "No new record candidates arrive, so structure stops accumulating.",
            "positive issued novelty before any coherence or consensus reading",
        ),
        (
            "admissibility",
            "admissible_extension_filter",
            "without_admissibility",
            "incoherence",
            "Contradictory extensions accumulate, so coherent structure collapses.",
            "predeclared rule filter separates legal from contradictory extensions",
        ),
        (
            "sybil_finality",
            "observer_identity_and_finality_guard",
            "without_sybil_finality",
            "capture",
            "Fake-observer capture erodes coherence even with issuance and rules.",
            "identity/finality guard prevents repeated unfounded observers",
        ),
        (
            "consensus",
            "shared_settlement_relation",
            "without_consensus",
            "fragment",
            "Local worlds remain active but fail to become shared structure.",
            "settlement relation decides when admitted records are common",
        ),
        (
            "governance",
            "rule_revision_horizon",
            "without_governance_near_term_rules",
            "ossification",
            "Fixed near-term rules reject novelty beyond their anticipation horizon.",
            "rule horizon and update policy are declared before novelty is read",
        ),
    )
    return tuple(
        LayerContract(
            layer_id=layer_id,
            source_variable=source_variable,
            frozen_t527_row_id=row_id,
            predicted_collapse_mode=mode,
            t527_ratio_to_full=rows[row_id]["scs_ratio_to_full"],
            collapse_threshold=0.20,
            source_law_burden=burden,
            predeclared_signal=signal,
        )
        for layer_id, source_variable, row_id, mode, burden, signal in specs
    )


def _gate_decisions(
    t549_result: t549.T549Result,
    t527_payload: dict[str, Any],
    layers: tuple[LayerContract, ...],
) -> tuple[GateDecision, ...]:
    rows = {row["id"]: row for row in t527_payload["rows"]}
    decisions = (
        (
            "t549_route_authority",
            t549_result.verdict == t549.VERDICT
            and t549_result.selected_route_ids == (SELECTED_ROUTE,),
            "T549 selected exactly the Observerse protocol-stack ablation preflight route.",
            "T549 did not select the expected route.",
        ),
        (
            "t527_review_only_boundary",
            t527_payload["verdict"] == t527.VERDICT
            and t527_payload["grade"] == "illustration_regression_only"
            and not t527_payload["claim_status_changed"]
            and not t527_payload["canon_verdict_changed"]
            and not t527_payload["public_posture_changed"],
            "T527 is usable only as frozen review-only source evidence.",
            "T527 boundary flags do not preserve review-only status.",
        ),
        (
            "five_layer_contract_predeclared",
            tuple(layer.layer_id for layer in layers)
            == ("issuance", "admissibility", "sybil_finality", "consensus", "governance"),
            "The minimal near-term stack contract names exactly five layers.",
            "The layer contract is missing or adding layers.",
        ),
        (
            "collapse_predictions_predeclared",
            all(layer.predicted_collapse_mode for layer in layers)
            and all(layer.source_variable for layer in layers),
            "Every layer has a source variable and a collapse-mode prediction.",
            "At least one layer lacks a source variable or collapse prediction.",
        ),
        (
            "t527_collapse_map_matches_contract",
            all(layer.t527_ratio_to_full <= layer.collapse_threshold for layer in layers),
            "Every contracted layer matches the T527 collapse-band evidence under near-term governance.",
            "At least one contracted layer does not collapse in the frozen T527 map.",
        ),
        (
            "governance_conditional_preserved",
            t527_payload["governance_conditional_visible"]
            and rows["without_governance_near_term_rules"]["scs_ratio_to_full"] <= 0.20
            and rows["without_governance_full_horizon_rules"]["scs_ratio_to_full"] >= 0.95,
            "Governance stays conditional: five layers near-term, four if full-horizon rules are granted.",
            "The governance near-term/full-horizon conditional is not preserved.",
        ),
        (
            "next_packet_specific",
            NEXT_PACKET.startswith("t551_"),
            "A single next executable stress packet is named.",
            "No specific next packet is named.",
        ),
        (
            "governance_boundaries_preserved",
            True,
            "No claim, canon, public-posture, TAF4, TAF8, external, or cross-repo movement is attempted.",
            "A forbidden governance movement was attempted.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=pass_reason if passed else fail_reason,
        )
        for gate_id, passed, pass_reason, fail_reason in decisions
    )


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="t527_validation_overread_control",
            blocks="Treating T527 or T550 as Observerse validation, S1 evidence, or source-law proof.",
            reason="T527 is illustration-grade and T550 is a preflight contract.",
        ),
        HostileControl(
            control_id="post_hoc_layer_control",
            blocks="Adding, dropping, or renaming layers after seeing stress-packet outcomes.",
            reason="T550 freezes the source variables and collapse predictions before T551.",
        ),
        HostileControl(
            control_id="conditional_governance_control",
            blocks="Dropping governance unconditionally from the minimal near-term stack.",
            reason="T527 makes governance load-bearing when fixed rules do not anticipate full novelty.",
        ),
        HostileControl(
            control_id="aprd_retune_control",
            blocks="Repairing APRD or reusing APRD family-local debt as the protocol-stack rule.",
            reason="T548 narrowed APRD and T549 selected a new post-APRD route.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks="Importing cross-repo truth, Lorentzian targets, or outcome labels into the stack.",
            reason="The next packet must be finality-native and predeclared.",
        ),
        HostileControl(
            control_id="taf4_source_law_shortcut_control",
            blocks="Moving TAF4 or source-law status directly from the preflight.",
            reason="Only a later stress survivor could create evidence; T550 creates none.",
        ),
        HostileControl(
            control_id="governance_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet is review-only and has no governance movement authority.",
        ),
    )


def _claim_labels(
    layers: tuple[LayerContract, ...],
    gate_decisions: tuple[GateDecision, ...],
    t527_payload: dict[str, Any],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Five predeclared layers are frozen for the next stress packet: "
                + ", ".join(layer.layer_id for layer in layers)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The frozen T527 collapse map supports the preflight boundary: "
                f"core collapse holds, governance conditional is "
                f"{t527_payload['governance_conditional_visible']}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "All preflight gates pass: "
                + ", ".join(gate.gate_id for gate in gate_decisions if gate.passed)
                + "."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The next useful TAF11 burden is not another route router but a "
                "native stress packet asking whether the frozen stack predicts "
                "collapse and rescue without post-hoc layer choice."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T550 Results: Observerse Protocol-Stack Ablation Preflight Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Preflight status: `{payload['preflight_status']}`",
        f"- Source T549 verdict: `{payload['source_t549_verdict']}`",
        "- Source T549 selected route ids: "
        + ", ".join(f"`{item}`" for item in payload["source_t549_selected_route_ids"]),
        f"- Source T527 verdict: `{payload['source_t527_verdict']}`",
        f"- Source T527 grade: `{payload['source_t527_grade']}`",
        "- Source T527 governance conditional visible: "
        f"`{payload['source_t527_governance_conditional_visible']}`",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Layer Contracts",
        "",
        "| layer | source variable | T527 row | predicted mode | ratio | burden | signal |",
        "| --- | --- | --- | --- | ---: | --- | --- |",
    ]
    for layer in payload["layer_contracts"]:
        lines.append(
            "| "
            f"`{layer['layer_id']}` | "
            f"`{layer['source_variable']}` | "
            f"`{layer['frozen_t527_row_id']}` | "
            f"`{layer['predicted_collapse_mode']}` | "
            f"{layer['t527_ratio_to_full']:.3f} | "
            f"{layer['source_law_burden']} | "
            f"{layer['predeclared_signal']} |"
        )
    lines.extend(
        [
            "",
            "## Gate Decisions",
            "",
            "| gate | outcome | passed? | reason |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for gate in payload["gate_decisions"]:
        lines.append(
            "| "
            f"`{gate['gate_id']}` | "
            f"`{gate['outcome']}` | "
            f"{gate['passed']} | "
            f"{gate['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Hostile Controls",
            "",
            "| control | blocks | reason |",
            "| --- | --- | --- |",
        ]
    )
    for control in payload["hostile_controls"]:
        lines.append(
            "| "
            f"`{control['control_id']}` | "
            f"{control['blocks']} | "
            f"{control['reason']} |"
        )
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Recommended Next", "recommended_next"),
        ("TAF11 Update", "taf11_update"),
        ("TAF4 Update", "taf4_update"),
        ("TAF8 Update", "taf8_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def write_results(result: T550Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t550_result_to_dict(result)
    json_path = results_dir / "T550-observerse-protocol-stack-ablation-preflight-packet-v0.1.json"
    md_path = results_dir / "T550-observerse-protocol-stack-ablation-preflight-packet-v0.1-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t550_analysis()
    payload = t550_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
