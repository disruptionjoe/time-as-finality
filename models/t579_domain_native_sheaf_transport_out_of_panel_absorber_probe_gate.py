"""T579: out-of-panel absorber probe for the TAF11 candidate package.

T578 kept the T559-T577 route as a limited review-only candidate package and
selected an out-of-panel absorber probe. This gate asks whether external
absorber families outside the route's internal panel break the package, absorb
it as source-law overread, or leave it only as bounded review material.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t578_domain_native_sheaf_transport_candidate_package_limitation_gate as t578,
)


ARTIFACT = (
    "T579-domain-native-sheaf-transport-out-of-panel-absorber-probe-gate-v0.1"
)
VERDICT = "domain_native_sheaf_transport_out_of_panel_probe_survives_limited_review_only"
PANEL_STATUS = "OUT_OF_PANEL_PRESSURE_APPLIED_REVIEW_ONLY"
PACKAGE_STATUS = "PACKAGE_SURVIVES_EXTERNAL_PRESSURE_ONLY_AS_LIMITED_REVIEW_TARGET"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_EXTERNAL_ABSORBERS_LOAD_BEARING"
NEXT_PACKET = "t580_domain_native_sheaf_transport_external_panel_scope_closure_gate"

NOT_CLAIMED = (
    "T579 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It applies out-of-panel "
    "absorber pressure and keeps the T559-T578 candidate package limited to "
    "review material."
)


@dataclass(frozen=True)
class ExternalProbe:
    probe_id: str
    prior_panel_member: bool
    pressure_family: str
    pressure_question: str
    package_response: str
    breaks_package: bool
    absorbs_source_law_reading: bool
    surviving_review_value: str
    next_pressure: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PackageDecision:
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
class T579Result:
    artifact: str
    source_t578_verdict: str
    source_t578_selected_next_packet: str
    panel_status: str
    package_status: str
    source_law_status: str
    external_probes: tuple[ExternalProbe, ...]
    package_decisions: tuple[PackageDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    panel_is_out_of_prior_scope: bool
    package_broken_by_external_panel: bool
    package_survives_as_limited_review: bool
    source_law_earned: bool
    selected_next_packet: str
    verdict: str
    panel_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t579_analysis() -> T579Result:
    source = t578.run_t578_analysis()
    probes = _external_probes(source)
    panel_is_out_of_prior_scope = all(not probe.prior_panel_member for probe in probes)
    package_broken_by_external_panel = any(probe.breaks_package for probe in probes)
    source_law_earned = False
    package_survives_as_limited_review = (
        panel_is_out_of_prior_scope
        and not package_broken_by_external_panel
        and all(probe.absorbs_source_law_reading for probe in probes)
    )
    decisions = _package_decisions(
        package_broken_by_external_panel=package_broken_by_external_panel,
        package_survives_as_limited_review=package_survives_as_limited_review,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(decisions)
    gates = _gate_decisions(
        source=source,
        probes=probes,
        panel_is_out_of_prior_scope=panel_is_out_of_prior_scope,
        package_broken_by_external_panel=package_broken_by_external_panel,
        package_survives_as_limited_review=package_survives_as_limited_review,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        decisions=decisions,
    )
    verdict = (
        VERDICT
        if all(gate.passed for gate in gates)
        and selected_next_packet == NEXT_PACKET
        else "domain_native_sheaf_transport_out_of_panel_probe_unexpected_status"
    )

    return T579Result(
        artifact=ARTIFACT,
        source_t578_verdict=source.verdict,
        source_t578_selected_next_packet=source.selected_next_packet,
        panel_status=PANEL_STATUS,
        package_status=PACKAGE_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        external_probes=probes,
        package_decisions=decisions,
        gate_decisions=gates,
        panel_is_out_of_prior_scope=panel_is_out_of_prior_scope,
        package_broken_by_external_panel=package_broken_by_external_panel,
        package_survives_as_limited_review=package_survives_as_limited_review,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        panel_reading=(
            "T579 adds external absorber pressure from stochastic thermodynamics, "
            "detector metrology, causal-set measure-law calibration, and quantum "
            "access-structure monogamy. The panel does not break the candidate "
            "package as a bounded review object, but every probe absorbs any "
            "source-law or downstream-overread interpretation."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should close or expand the "
            "external-panel scope before any stronger reading of the TAF11 "
            "candidate package."
        ),
        taf11_update=(
            "TAF11 remains open, but only as a limited review target. T579 "
            "shows the package can face out-of-panel pressure without becoming "
            "a public source law."
        ),
        taf4_update=(
            "TAF4 remains blocked. The causal-set measure-law probe absorbs "
            "continuum or manifoldlikeness overreads and supplies no finite-to-"
            "continuum bridge."
        ),
        taf8_update=(
            "TAF8 remains waiting. The quantum access-structure probe blocks "
            "cross-domain shadow-protection overread without a domain-native "
            "cross-domain packet."
        ),
        claim_labels=_claim_labels(probes, package_survives_as_limited_review),
        claim_ledger_update=(
            "No claim-ledger update is earned. T579 is external absorber "
            "pressure on a review-only package; claim rows, Canon Index tiers, "
            "canon verdicts, and public posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t579_result_to_dict(result: T579Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t578_verdict": result.source_t578_verdict,
        "source_t578_selected_next_packet": result.source_t578_selected_next_packet,
        "panel_status": result.panel_status,
        "package_status": result.package_status,
        "source_law_status": result.source_law_status,
        "external_probes": [probe.to_dict() for probe in result.external_probes],
        "package_decisions": [
            decision.to_dict() for decision in result.package_decisions
        ],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "panel_is_out_of_prior_scope": result.panel_is_out_of_prior_scope,
        "package_broken_by_external_panel": result.package_broken_by_external_panel,
        "package_survives_as_limited_review": result.package_survives_as_limited_review,
        "source_law_earned": result.source_law_earned,
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "panel_reading": result.panel_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [claim.to_dict() for claim in result.claim_labels],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _external_probes(source: t578.T578Result) -> tuple[ExternalProbe, ...]:
    return (
        ExternalProbe(
            probe_id="stochastic_thermodynamic_maintenance_absorber",
            prior_panel_member=False,
            pressure_family="stochastic thermodynamics and maintenance accounting",
            pressure_question=(
                "Does the package reduce to energy, erasure, maintenance, or "
                "resource-accounting costs once thermodynamic state is granted?"
            ),
            package_response=(
                "Thermodynamic accounting absorbs source-law readings, but does "
                "not erase the review question about finality-native transport "
                "squares and repair payloads."
            ),
            breaks_package=False,
            absorbs_source_law_reading=True,
            surviving_review_value=(
                "limited review pressure on whether record-finality transport "
                "adds anything after thermodynamic state completion"
            ),
            next_pressure="scope whether more external absorber families are required",
        ),
        ExternalProbe(
            probe_id="detector_metrology_calibration_absorber",
            prior_panel_member=False,
            pressure_family="detector metrology, calibration, and provenance",
            pressure_question=(
                "Does the package smuggle instrument state, calibration drift, "
                "or provenance fields that a detector-native absorber would own?"
            ),
            package_response=(
                "Detector completion blocks public or empirical readings because "
                "the package has no raw manifest or calibration packet, but the "
                "abstract review object survives as non-empirical pressure."
            ),
            breaks_package=False,
            absorbs_source_law_reading=True,
            surviving_review_value="abstract non-empirical review target only",
            next_pressure="keep detector-data claims gated on real manifests",
        ),
        ExternalProbe(
            probe_id="causal_set_measure_law_absorber",
            prior_panel_member=False,
            pressure_family="causal-set measure law and Lorentzian calibration",
            pressure_question=(
                "Does the package provide a finality-native measure law, "
                "sprinkling analogue, or continuum bridge rather than importing "
                "target spacetime structure?"
            ),
            package_response=(
                "The package supplies no measure law or continuum bridge, so "
                "TAF4, S1, T223 reversal, and manifoldlikeness overreads remain "
                "blocked."
            ),
            breaks_package=False,
            absorbs_source_law_reading=True,
            surviving_review_value="negative pressure against continuum overread",
            next_pressure="close whether the external panel needs a separate TAF4 gate",
        ),
        ExternalProbe(
            probe_id="quantum_access_structure_monogamy_absorber",
            prior_panel_member=False,
            pressure_family="quantum access structures, shareability, and monogamy",
            pressure_question=(
                "Does the package establish a domain-native cross-domain shadow-"
                "protection theorem or only resemble access-structure limits?"
            ),
            package_response=(
                "Known quantum access-structure and monogamy machinery absorbs "
                "cross-domain theorem overread; TAF8 still needs its own "
                "domain-native packet."
            ),
            breaks_package=False,
            absorbs_source_law_reading=True,
            surviving_review_value="review-only comparison to access-structure absorbers",
            next_pressure="keep TAF8 waiting for an actual cross-domain packet",
        ),
    )


def _package_decisions(
    package_broken_by_external_panel: bool,
    package_survives_as_limited_review: bool,
    source_law_earned: bool,
) -> tuple[PackageDecision, ...]:
    return (
        PackageDecision(
            decision_id="promote_source_law_after_external_probe",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "BLOCKED_EXTERNAL_ABSORBERS_LOAD_BEARING"
            ),
            selected=source_law_earned,
            reason=(
                "Source-law promotion was earned."
                if source_law_earned
                else "Every external probe absorbs source-law or downstream-overread interpretations."
            ),
        ),
        PackageDecision(
            decision_id="retire_package_as_broken",
            outcome=(
                "SELECTED_RETIREMENT"
                if package_broken_by_external_panel
                else "BLOCKED_PACKAGE_NOT_BROKEN"
            ),
            selected=package_broken_by_external_panel,
            reason=(
                "An external absorber broke the package as review material."
                if package_broken_by_external_panel
                else "The external panel did not break the package as bounded review material."
            ),
        ),
        PackageDecision(
            decision_id="retain_limited_review_package",
            outcome=(
                "SELECTED_LIMITED_REVIEW_RETENTION"
                if package_survives_as_limited_review
                else "BLOCKED_LIMITED_REVIEW_NOT_STABLE"
            ),
            selected=package_survives_as_limited_review,
            reason=(
                "The package survives external pressure only as a limited review target."
                if package_survives_as_limited_review
                else "The package did not stabilize as limited review material."
            ),
        ),
        PackageDecision(
            decision_id="run_external_panel_scope_closure",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if package_survives_as_limited_review and not source_law_earned
                else "PAUSED_UNTIL_EXTERNAL_PANEL_STATUS_CLEAR"
            ),
            selected=package_survives_as_limited_review and not source_law_earned,
            reason=(
                "The external panel applied pressure, but its scope should be closed or expanded before stronger readings."
                if package_survives_as_limited_review
                else "No scope closure until the package's external-panel status is stable."
            ),
            next_packet=NEXT_PACKET,
        ),
        PackageDecision(
            decision_id="move_taf4_from_t579",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            reason="The causal-set probe supplies no finality-native continuum bridge.",
        ),
        PackageDecision(
            decision_id="execute_taf8_from_t579",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            reason="The quantum probe is absorber pressure, not a cross-domain theorem packet.",
        ),
        PackageDecision(
            decision_id="move_s1_or_cross_repo_truth",
            outcome="BLOCKED_GOVERNANCE",
            selected=False,
            reason="No S1, cross-repo, publication, claim, canon, or public-posture movement is authorized.",
        ),
    )


def _selected_next_packet(decisions: tuple[PackageDecision, ...]) -> str:
    next_packets = tuple(
        decision.next_packet
        for decision in decisions
        if decision.selected and decision.next_packet != "none"
    )
    if len(next_packets) != 1:
        return "none"
    return next_packets[0]


def _gate_decisions(
    source: t578.T578Result,
    probes: tuple[ExternalProbe, ...],
    panel_is_out_of_prior_scope: bool,
    package_broken_by_external_panel: bool,
    package_survives_as_limited_review: bool,
    source_law_earned: bool,
    selected_next_packet: str,
    decisions: tuple[PackageDecision, ...],
) -> tuple[GateDecision, ...]:
    decision_map = {decision.decision_id: decision for decision in decisions}
    all_source_law_absorbed = all(probe.absorbs_source_law_reading for probe in probes)
    gates = (
        (
            "t578_authority",
            source.verdict == t578.VERDICT
            and source.selected_next_packet == t578.NEXT_PACKET
            and source.package_remains_review_only,
            "T578 supplies out-of-panel probe authority.",
            "T578 did not supply the expected probe authority.",
        ),
        (
            "panel_out_of_prior_scope",
            panel_is_out_of_prior_scope and len(probes) == 4,
            "Every probe is outside the prior internal T559-T578 panel.",
            "One or more probes are not outside the prior panel.",
        ),
        (
            "source_law_absorbed_not_earned",
            all_source_law_absorbed and not source_law_earned,
            "Every external probe blocks source-law overread.",
            "A source-law reading escaped external absorber pressure.",
        ),
        (
            "package_survives_limited_review",
            package_survives_as_limited_review
            and not package_broken_by_external_panel
            and decision_map["retain_limited_review_package"].selected,
            "The package survives only as a limited review target.",
            "The package either broke or moved too far.",
        ),
        (
            "external_scope_closure_selected",
            selected_next_packet == NEXT_PACKET
            and decision_map["run_external_panel_scope_closure"].selected,
            "External-panel scope closure is selected as the next burden.",
            "The expected external-panel scope closure was not selected.",
        ),
        (
            "protected_boundaries_preserved",
            decision_map["move_taf4_from_t579"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decision_map["execute_taf8_from_t579"].outcome
            == "BLOCKED_TAF8_OVERREAD"
            and decision_map["move_s1_or_cross_repo_truth"].outcome
            == "BLOCKED_GOVERNANCE",
            "TAF4, TAF8, S1, cross-repo, publication, claim, canon, and public-posture shortcuts are blocked.",
            "A protected movement was allowed.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=pass_reason if passed else fail_reason,
        )
        for gate_id, passed, pass_reason, fail_reason in gates
    )


def _claim_labels(
    probes: tuple[ExternalProbe, ...],
    package_survives_as_limited_review: bool,
) -> tuple[ClaimLabel, ...]:
    probe_ids = ", ".join(probe.probe_id for probe in probes)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Out-of-panel probes applied: {probe_ids}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Every external probe absorbs source-law or downstream-overread readings.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The package survives only as limited review material."
                if package_survives_as_limited_review
                else "The package does not survive as limited review material."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Claim, canon, public-posture, TAF4, TAF8, S1, publication, and cross-repo movement remain blocked.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T579 Results: Domain-Native Sheaf Transport Out-Of-Panel Absorber Probe Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Panel status: `{payload['panel_status']}`",
        f"- Package status: `{payload['package_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Source T578 verdict: `{payload['source_t578_verdict']}`",
        f"- Source T578 selected next packet: `{payload['source_t578_selected_next_packet']}`",
        f"- Panel is out of prior scope: {payload['panel_is_out_of_prior_scope']}",
        f"- Package broken by external panel: {payload['package_broken_by_external_panel']}",
        f"- Package survives as limited review: {payload['package_survives_as_limited_review']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## External Probes",
        "",
        "| probe | prior panel? | pressure family | breaks package? | absorbs source-law reading? | surviving review value | next pressure |",
        "| --- | :---: | --- | :---: | :---: | --- | --- |",
    ]
    for probe in payload["external_probes"]:
        lines.append(
            "| "
            f"`{probe['probe_id']}` | "
            f"{probe['prior_panel_member']} | "
            f"{probe['pressure_family']} | "
            f"{probe['breaks_package']} | "
            f"{probe['absorbs_source_law_reading']} | "
            f"{probe['surviving_review_value']} | "
            f"{probe['next_pressure']} |"
        )
    lines.extend(
        [
            "",
            "## Package Decisions",
            "",
            "| decision | outcome | selected? | next packet | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for decision in payload["package_decisions"]:
        lines.append(
            "| "
            f"`{decision['decision_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected']} | "
            f"`{decision['next_packet']}` | "
            f"{decision['reason']} |"
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
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Panel Reading", "panel_reading"),
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


def write_results(result: T579Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t579_result_to_dict(result)
    json_path = (
        results_dir
        / "T579-domain-native-sheaf-transport-out-of-panel-absorber-probe-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T579-domain-native-sheaf-transport-out-of-panel-absorber-probe-gate-v0.1-results.md"
    )
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t579_analysis()
    payload = t579_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
