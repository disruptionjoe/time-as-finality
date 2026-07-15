"""T581: close and park the TAF11 limited review package.

T580 closed the current external absorber panel. This router preserves the
T559-T580 package as limited review material, names evidence-only reopen
conditions, and prevents a new cross-domain packet from reopening the old
route by momentum.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t580_domain_native_sheaf_transport_external_panel_scope_closure_gate as t580,
)


ARTIFACT = "T581-domain-native-sheaf-transport-review-package-closeout-router-v0.1"
VERDICT = "domain_native_sheaf_transport_review_package_closed_parked_limited_review"
PACKAGE_STATUS = "TAF11_REVIEW_PACKAGE_CLOSED_AND_PARKED"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_PACKAGE_CLOSEOUT_IS_NOT_PROMOTION"
OLD_ROUTE_NEXT_PACKET = "none"
SEPARATE_PACKET = "t582_w192_record_conditioned_capability_discriminator_gate"

NOT_CLAIMED = (
    "T581 does not establish a source law, promote TAF11, prove shadow "
    "protection, derive spacetime, move claim status or Canon Index tiers, "
    "change canon verdicts or public posture, authorize publication, move "
    "TAF4 or TAF8, promote S1, or move cross-repo truth. It closes and parks "
    "the TAF11 review package and routes W192 to a separate gate."
)


@dataclass(frozen=True)
class ReopenCondition:
    condition_id: str
    evidence_required: str
    current_evidence_present: bool
    reopens_old_package: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CloseoutDecision:
    decision_id: str
    outcome: str
    selected: bool
    reason: str
    next_packet: str = "none"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class GateDecision:
    gate_id: str
    outcome: str
    passed: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class T581Result:
    artifact: str
    source_t580_verdict: str
    source_t580_selected_next_packet: str
    package_status: str
    source_law_status: str
    reopen_conditions: tuple[ReopenCondition, ...]
    closeout_decisions: tuple[CloseoutDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    package_closed: bool
    package_parked: bool
    source_law_earned: bool
    old_route_next_packet: str
    separate_packet: str
    verdict: str
    recommended_next: str
    taf11_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t581_analysis() -> T581Result:
    source = t580.run_t580_analysis()
    reopen_conditions = _reopen_conditions()
    package_closed = (
        source.verdict == t580.VERDICT
        and source.selected_next_packet == t580.NEXT_PACKET
        and source.current_external_panel_closed
        and not source.source_law_earned
    )
    package_parked = package_closed and not any(
        condition.current_evidence_present and condition.reopens_old_package
        for condition in reopen_conditions
    )
    source_law_earned = False
    decisions = _closeout_decisions(package_closed, package_parked)
    gates = _gate_decisions(
        source=source,
        reopen_conditions=reopen_conditions,
        decisions=decisions,
        package_closed=package_closed,
        package_parked=package_parked,
        source_law_earned=source_law_earned,
    )
    verdict = VERDICT if all(gate.passed for gate in gates) else "taf11_closeout_unexpected_status"

    return T581Result(
        artifact=ARTIFACT,
        source_t580_verdict=source.verdict,
        source_t580_selected_next_packet=source.selected_next_packet,
        package_status=PACKAGE_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        reopen_conditions=reopen_conditions,
        closeout_decisions=decisions,
        gate_decisions=gates,
        package_closed=package_closed,
        package_parked=package_parked,
        source_law_earned=source_law_earned,
        old_route_next_packet=OLD_ROUTE_NEXT_PACKET,
        separate_packet=SEPARATE_PACKET,
        verdict=verdict,
        recommended_next=(
            "Keep the TAF11 package parked. Reopen it only when one named "
            "condition arrives with concrete evidence. Evaluate frozen W192 "
            f"separately through {SEPARATE_PACKET}."
        ),
        taf11_update=(
            "TAF11 is closed and parked as limited review material. No "
            "unattended successor remains on the T559-T581 route."
        ),
        taf8_update=(
            "TAF8 remains open. W192 is a separate candidate packet and does "
            "not inherit support from the parked TAF11 package."
        ),
        claim_labels=_claim_labels(reopen_conditions),
        claim_ledger_update=(
            "No claim-ledger update is earned. Package closeout preserves the "
            "existing review-only status and blocks promotion by momentum."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t581_result_to_dict(result: T581Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t580_verdict": result.source_t580_verdict,
        "source_t580_selected_next_packet": result.source_t580_selected_next_packet,
        "package_status": result.package_status,
        "source_law_status": result.source_law_status,
        "reopen_conditions": [item.to_dict() for item in result.reopen_conditions],
        "closeout_decisions": [item.to_dict() for item in result.closeout_decisions],
        "gate_decisions": [item.to_dict() for item in result.gate_decisions],
        "package_closed": result.package_closed,
        "package_parked": result.package_parked,
        "source_law_earned": result.source_law_earned,
        "old_route_next_packet": result.old_route_next_packet,
        "separate_packet": result.separate_packet,
        "verdict": result.verdict,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [item.to_dict() for item in result.claim_labels],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _reopen_conditions() -> tuple[ReopenCondition, ...]:
    return (
        ReopenCondition(
            condition_id="new_domain_native_source_packet",
            evidence_required=(
                "A new packet with a predeclared native source law, source-role "
                "fields, independent holdout, and completed native absorbers."
            ),
            current_evidence_present=False,
            reopens_old_package=True,
            reason="Only new domain-native evidence can reopen the source-law route.",
        ),
        ReopenCondition(
            condition_id="empirical_detector_manifest",
            evidence_required=(
                "A predeclared data-bearing detector manifest with raw provenance, "
                "controls, and an independent axis."
            ),
            current_evidence_present=False,
            reopens_old_package=True,
            reason="Abstract detector pressure cannot substitute for a real manifest.",
        ),
        ReopenCondition(
            condition_id="finality_native_continuum_bridge",
            evidence_required=(
                "A finality-native finite-to-continuum packet with causal, measure, "
                "covariance, and descent certificates."
            ),
            current_evidence_present=False,
            reopens_old_package=True,
            reason="The causal-set target remains separate until a bridge exists.",
        ),
        ReopenCondition(
            condition_id="cross_domain_shadow_protection_packet",
            evidence_required=(
                "A domain-native nonidentity packet under the frozen T541 spine "
                "with typed transfer, direct preservation, and native absorbers."
            ),
            current_evidence_present=False,
            reopens_old_package=False,
            reason=(
                "A cross-domain packet opens its own gate; it does not retroactively "
                "promote or reopen the TAF11 package."
            ),
        ),
    )


def _closeout_decisions(
    package_closed: bool,
    package_parked: bool,
) -> tuple[CloseoutDecision, ...]:
    return (
        CloseoutDecision(
            decision_id="close_and_park_taf11_review_package",
            outcome="SELECTED_CLOSE_AND_PARK" if package_closed and package_parked else "BLOCKED",
            selected=package_closed and package_parked,
            reason="The scoped package is preserved as limited review material.",
        ),
        CloseoutDecision(
            decision_id="continue_old_route_unattended",
            outcome="BLOCKED_NO_NEW_EVIDENCE",
            selected=False,
            reason="The T559-T581 route has no unattended successor.",
        ),
        CloseoutDecision(
            decision_id="promote_package_by_momentum",
            outcome="BLOCKED_CLOSEOUT_IS_NOT_PROMOTION",
            selected=False,
            reason="Review survival and scope closure do not earn source-law status.",
        ),
        CloseoutDecision(
            decision_id="route_w192_as_separate_packet",
            outcome="SELECTED_SEPARATE_PACKET_GATE",
            selected=True,
            reason="W192 is new cross-domain input, not continuation evidence for TAF11.",
            next_packet=SEPARATE_PACKET,
        ),
        CloseoutDecision(
            decision_id="move_protected_truth",
            outcome="BLOCKED_GOVERNANCE",
            selected=False,
            reason=(
                "Claim, canon, public, publication, TAF4, TAF8, S1, and "
                "cross-repo movements remain blocked."
            ),
        ),
    )


def _gate_decisions(
    source: t580.T580Result,
    reopen_conditions: tuple[ReopenCondition, ...],
    decisions: tuple[CloseoutDecision, ...],
    package_closed: bool,
    package_parked: bool,
    source_law_earned: bool,
) -> tuple[GateDecision, ...]:
    decision_map = {item.decision_id: item for item in decisions}
    checks = (
        (
            "t580_authority",
            source.verdict == t580.VERDICT and source.selected_next_packet == t580.NEXT_PACKET,
            "T580 supplies closeout authority.",
        ),
        (
            "package_closed_and_parked",
            package_closed and package_parked,
            "The TAF11 package is closed and parked as limited review material.",
        ),
        (
            "evidence_only_reopen_conditions_named",
            len(reopen_conditions) == 4
            and all(item.evidence_required for item in reopen_conditions)
            and not any(item.current_evidence_present for item in reopen_conditions),
            "Four concrete evidence-only reopen conditions are named and none is present.",
        ),
        (
            "promotion_by_momentum_blocked",
            not source_law_earned
            and decision_map["promote_package_by_momentum"].outcome
            == "BLOCKED_CLOSEOUT_IS_NOT_PROMOTION",
            "Closeout cannot promote the package by momentum.",
        ),
        (
            "w192_routed_separately",
            decision_map["route_w192_as_separate_packet"].selected
            and decision_map["route_w192_as_separate_packet"].next_packet == SEPARATE_PACKET,
            "W192 is routed to a separate capability gate.",
        ),
        (
            "protected_movements_blocked",
            decision_map["move_protected_truth"].outcome == "BLOCKED_GOVERNANCE",
            "Protected truth and governance movements remain blocked.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=reason if passed else f"Failed: {reason}",
        )
        for gate_id, passed, reason in checks
    )


def _claim_labels(
    reopen_conditions: tuple[ReopenCondition, ...],
) -> tuple[ClaimLabel, ...]:
    condition_ids = ", ".join(item.condition_id for item in reopen_conditions)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="T580 authority closes and parks the TAF11 review package.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Reopen conditions declared: {condition_ids}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="high",
            text="W192 should be evaluated separately rather than reopening TAF11.",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law and protected truth movements remain blocked.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T581 Results: Domain-Native Sheaf Transport Review-Package Closeout Router",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Package status: `{payload['package_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Package closed: {payload['package_closed']}",
        f"- Package parked: {payload['package_parked']}",
        f"- Old-route next packet: `{payload['old_route_next_packet']}`",
        f"- Separate packet: `{payload['separate_packet']}`",
        "",
        "## Reopen Conditions",
        "",
        "| condition | current evidence? | reopens old package? | evidence required | reason |",
        "| --- | :---: | :---: | --- | --- |",
    ]
    for item in payload["reopen_conditions"]:
        lines.append(
            f"| `{item['condition_id']}` | {item['current_evidence_present']} | "
            f"{item['reopens_old_package']} | {item['evidence_required']} | {item['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Closeout Decisions",
            "",
            "| decision | outcome | selected? | next packet | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for item in payload["closeout_decisions"]:
        lines.append(
            f"| `{item['decision_id']}` | `{item['outcome']}` | {item['selected']} | "
            f"`{item['next_packet']}` | {item['reason']} |"
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
    for item in payload["gate_decisions"]:
        lines.append(
            f"| `{item['gate_id']}` | `{item['outcome']}` | {item['passed']} | {item['reason']} |"
        )
    lines.extend(["", "## Claim Labels", ""])
    for item in payload["claim_labels"]:
        lines.append(
            f"- `{item['label']}` confidence `{item['confidence']}`: {item['text']}"
        )
    for heading, key in (
        ("Recommended Next", "recommended_next"),
        ("TAF11 Update", "taf11_update"),
        ("TAF8 Update", "taf8_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def write_results(result: T581Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t581_result_to_dict(result)
    json_path = results_dir / f"{ARTIFACT}.json"
    md_path = results_dir / f"{ARTIFACT}-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)
    result = run_t581_analysis()
    payload = t581_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
