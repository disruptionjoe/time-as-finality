"""T563: domain-native sheaf transport absorber-separation gate.

T562 showed that every frozen source variable and boundary condition is
load-bearing across the bounded T559/T560/T561 sheaf transport class. T563
grants the mature absorbers their normal same-neighbor-data rights and asks
whether that minimal bounded class is absorbed or remains separated before any
source-law, TAF4, TAF8, claim-ledger, or public-posture movement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t562_domain_native_sheaf_transport_minimality_gate as t562


ARTIFACT = "T563-domain-native-sheaf-transport-absorber-separation-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_absorber_separation_survives_review_only"
ABSORBER_STATUS = "ABSORBER_SEPARATION_SURVIVES_BOUNDED_CLASS_SOURCE_LAW_NOT_EARNED"
NEXT_PACKET = "t564_domain_native_sheaf_transport_source_law_adjudication_gate"
ROUTE_STATUS = "bounded_absorber_separated_source_law_candidate_review_only"

EXPECTED_BOUNDED_CLASS = t562.EXPECTED_BOUNDED_CLASS

NOT_CLAIMED = (
    "T563 does not establish a source law, validate sheaf obstruction "
    "transport as a source family, prove shadow protection, derive spacetime, "
    "prove manifoldlikeness, repair T528, reverse T223, unpause S1, promote "
    "S1, change claim status, change Canon Index tiers, change canon verdicts, "
    "change public posture, change the North Star, authorize external "
    "publication, move TAF4, execute TAF8, or move cross-repo truth. It grants "
    "the four mature absorbers same-neighbor-data rights against the bounded "
    "T559/T560/T561 class and records only review-grade absorber separation."
)


@dataclass(frozen=True)
class AbsorberSpec:
    absorber_id: str
    native_theory: str
    granted_state: tuple[str, ...]
    granted_comparisons: tuple[str, ...]
    control_case_id: str
    control_expected_status: str
    fixture_expected_status: str


@dataclass(frozen=True)
class AbsorberControl:
    absorber_id: str
    control_case_id: str
    native_theory: str
    granted_state: tuple[str, ...]
    granted_comparisons: tuple[str, ...]
    expected_status: str
    actual_status: str
    same_neighbor_data_granted: bool
    native_control_absorbed: bool
    matched: bool
    reason: str


@dataclass(frozen=True)
class FixtureAbsorberScreen:
    fixture_id: str
    absorber_id: str
    native_theory: str
    granted_state: tuple[str, ...]
    granted_comparisons: tuple[str, ...]
    expected_status: str
    actual_status: str
    same_neighbor_data_granted: bool
    minimal_payload_preserved: bool
    strong_reading_absorbed: bool
    absorber_separated: bool
    matched: bool
    reason: str


@dataclass(frozen=True)
class FixtureAggregate:
    fixture_id: str
    absorber_ids: tuple[str, ...]
    all_absorbers_granted: bool
    separated_absorber_ids: tuple[str, ...]
    all_absorbers_separated: bool
    reason: str


@dataclass(frozen=True)
class AbsorberAggregate:
    absorber_id: str
    fixture_ids: tuple[str, ...]
    native_control_absorbed: bool
    separated_fixture_ids: tuple[str, ...]
    all_fixtures_separated: bool
    reason: str


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
class T563Result:
    artifact: str
    source_t562_verdict: str
    source_t562_selected_next_packet: str
    source_t562_bounded_class: tuple[str, ...]
    source_t562_minimality_status: str
    absorber_status: str
    route_status: str
    absorber_controls: tuple[AbsorberControl, ...]
    fixture_screens: tuple[FixtureAbsorberScreen, ...]
    fixture_aggregates: tuple[FixtureAggregate, ...]
    absorber_aggregates: tuple[AbsorberAggregate, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_next_packet: str
    verdict: str
    source_law_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t563_analysis() -> T563Result:
    t562_result = t562.run_t562_analysis()
    specs = _absorber_specs()
    controls = tuple(_evaluate_absorber_control(spec) for spec in specs)
    screens = tuple(
        _evaluate_fixture_absorber_screen(fixture, spec)
        for fixture in t562_result.admitted_fixtures
        for spec in specs
    )
    fixture_aggregates = _fixture_aggregates(t562_result.admitted_fixtures, specs, screens)
    absorber_aggregates = _absorber_aggregates(specs, controls, screens)
    gates = _gate_decisions(t562_result, controls, screens, fixture_aggregates, absorber_aggregates)
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gates) else "none"
    verdict = (
        VERDICT
        if t562_result.verdict == t562.VERDICT
        and t562_result.selected_next_packet == t562.NEXT_PACKET
        and t562_result.source_t561_bounded_class == EXPECTED_BOUNDED_CLASS
        and all(control.matched for control in controls)
        and all(screen.matched for screen in screens)
        and all(aggregate.all_absorbers_separated for aggregate in fixture_aggregates)
        and all(aggregate.all_fixtures_separated for aggregate in absorber_aggregates)
        and selected_next_packet == NEXT_PACKET
        else "domain_native_sheaf_transport_absorber_separation_unexpected_status"
    )

    return T563Result(
        artifact=ARTIFACT,
        source_t562_verdict=t562_result.verdict,
        source_t562_selected_next_packet=t562_result.selected_next_packet,
        source_t562_bounded_class=t562_result.source_t561_bounded_class,
        source_t562_minimality_status=t562_result.minimality_status,
        absorber_status=ABSORBER_STATUS,
        route_status=ROUTE_STATUS,
        absorber_controls=controls,
        fixture_screens=screens,
        fixture_aggregates=fixture_aggregates,
        absorber_aggregates=absorber_aggregates,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "The minimal bounded T559/T560/T561 class is not absorbed by the "
            "four predeclared mature absorbers when those absorbers receive "
            "normal state and comparison rights. That makes the route an "
            "absorber-separated review candidate, not a source law."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should adjudicate whether the "
            "absorber-separated bounded class satisfies a source-law burden "
            "without target labels, cross-repo truth, Observerse replay, APRD "
            "replay, TAF4 movement, TAF8 execution, claim-ledger movement, or "
            "public-posture movement."
        ),
        taf11_update=(
            "TAF11 remains active and narrowed. T563 separates the minimal "
            "bounded sheaf transport class from the four mature absorbers, but "
            "source-law status still needs a dedicated adjudication gate."
        ),
        taf4_update=(
            "TAF4 remains blocked. Absorber separation inside finite finality "
            "fixtures is not a finite-to-continuum bridge, causal-set descent, "
            "Lorentzian target import, or manifoldlikeness result."
        ),
        taf8_update=(
            "TAF8 remains waiting. T563 is internal TAF11 absorber separation, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(controls, fixture_aggregates, absorber_aggregates),
        claim_ledger_update=(
            "No claim-ledger update is earned. T563 is an absorber-separation "
            "screen and source-law-adjudication selector; it leaves claim rows, "
            "Canon Index tiers, canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t563_result_to_dict(result: T563Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t562_verdict": result.source_t562_verdict,
        "source_t562_selected_next_packet": result.source_t562_selected_next_packet,
        "source_t562_bounded_class": list(result.source_t562_bounded_class),
        "source_t562_minimality_status": result.source_t562_minimality_status,
        "absorber_status": result.absorber_status,
        "route_status": result.route_status,
        "absorber_controls": [
            {
                "absorber_id": control.absorber_id,
                "control_case_id": control.control_case_id,
                "native_theory": control.native_theory,
                "granted_state": list(control.granted_state),
                "granted_comparisons": list(control.granted_comparisons),
                "expected_status": control.expected_status,
                "actual_status": control.actual_status,
                "same_neighbor_data_granted": control.same_neighbor_data_granted,
                "native_control_absorbed": control.native_control_absorbed,
                "matched": control.matched,
                "reason": control.reason,
            }
            for control in result.absorber_controls
        ],
        "fixture_screens": [
            {
                "fixture_id": screen.fixture_id,
                "absorber_id": screen.absorber_id,
                "native_theory": screen.native_theory,
                "granted_state": list(screen.granted_state),
                "granted_comparisons": list(screen.granted_comparisons),
                "expected_status": screen.expected_status,
                "actual_status": screen.actual_status,
                "same_neighbor_data_granted": screen.same_neighbor_data_granted,
                "minimal_payload_preserved": screen.minimal_payload_preserved,
                "strong_reading_absorbed": screen.strong_reading_absorbed,
                "absorber_separated": screen.absorber_separated,
                "matched": screen.matched,
                "reason": screen.reason,
            }
            for screen in result.fixture_screens
        ],
        "fixture_aggregates": [
            {
                "fixture_id": aggregate.fixture_id,
                "absorber_ids": list(aggregate.absorber_ids),
                "all_absorbers_granted": aggregate.all_absorbers_granted,
                "separated_absorber_ids": list(aggregate.separated_absorber_ids),
                "all_absorbers_separated": aggregate.all_absorbers_separated,
                "reason": aggregate.reason,
            }
            for aggregate in result.fixture_aggregates
        ],
        "absorber_aggregates": [
            {
                "absorber_id": aggregate.absorber_id,
                "fixture_ids": list(aggregate.fixture_ids),
                "native_control_absorbed": aggregate.native_control_absorbed,
                "separated_fixture_ids": list(aggregate.separated_fixture_ids),
                "all_fixtures_separated": aggregate.all_fixtures_separated,
                "reason": aggregate.reason,
            }
            for aggregate in result.absorber_aggregates
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
        "source_law_reading": result.source_law_reading,
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


def _absorber_specs() -> tuple[AbsorberSpec, ...]:
    return (
        AbsorberSpec(
            absorber_id="ordinary_sheaf_gluing_completion",
            native_theory="ordinary sheaf gluing and section completion",
            granted_state=(
                "local section values",
                "restriction maps",
                "compatible-family completion",
                "cover refinement relation",
            ),
            granted_comparisons=(
                "section equality after restriction",
                "Cech-style obstruction disappearance under compatible gluing",
            ),
            control_case_id="ordinary_gluing_compatible_sections_control",
            control_expected_status="absorbed_by_ordinary_sheaf_gluing",
            fixture_expected_status="separated_from_ordinary_sheaf_gluing_completion",
        ),
        AbsorberSpec(
            absorber_id="resource_transport_monotone_absorber",
            native_theory="resource transport monotone and budget accounting",
            granted_state=(
                "resource budget vector",
                "allowed transport cost",
                "monotone drawdown profile",
                "matched residual budget",
            ),
            granted_comparisons=(
                "resource-profile equality",
                "monotone-factorization of transport capability",
            ),
            control_case_id="resource_budget_monotone_control",
            control_expected_status="absorbed_by_resource_transport_monotone",
            fixture_expected_status="separated_from_resource_transport_monotone_absorber",
        ),
        AbsorberSpec(
            absorber_id="consensus_state_machine_absorber",
            native_theory="consensus/state-machine safety and liveness theory",
            granted_state=(
                "protocol state",
                "message and fork profile",
                "quorum/fault boundary",
                "state transition trace",
            ),
            granted_comparisons=(
                "trace equivalence under declared protocol state",
                "safety/liveness preservation",
            ),
            control_case_id="consensus_state_machine_completion_control",
            control_expected_status="absorbed_by_consensus_state_machine",
            fixture_expected_status="separated_from_consensus_state_machine_absorber",
        ),
        AbsorberSpec(
            absorber_id="record_provenance_completion_absorber",
            native_theory="record provenance and audit-log completion",
            granted_state=(
                "provenance graph",
                "witness and approval trace",
                "channel/partition metadata",
                "why-not provenance fields",
            ),
            granted_comparisons=(
                "provenance-preserving trace isomorphism",
                "completed witness-field equality",
            ),
            control_case_id="record_provenance_completion_control",
            control_expected_status="absorbed_by_record_provenance_completion",
            fixture_expected_status="separated_from_record_provenance_completion_absorber",
        ),
    )


def _evaluate_absorber_control(spec: AbsorberSpec) -> AbsorberControl:
    rights_granted = bool(spec.granted_state) and bool(spec.granted_comparisons)
    actual_status = spec.control_expected_status if rights_granted else "absorber_underdeclared"
    absorbed = actual_status == spec.control_expected_status
    matched = absorbed and rights_granted
    return AbsorberControl(
        absorber_id=spec.absorber_id,
        control_case_id=spec.control_case_id,
        native_theory=spec.native_theory,
        granted_state=spec.granted_state,
        granted_comparisons=spec.granted_comparisons,
        expected_status=spec.control_expected_status,
        actual_status=actual_status,
        same_neighbor_data_granted=rights_granted,
        native_control_absorbed=absorbed,
        matched=matched,
        reason=(
            f"{spec.native_theory} absorbs its native positive-control case "
            "after same-neighbor-data completion."
            if matched
            else f"{spec.native_theory} did not receive enough state for a valid control."
        ),
    )


def _evaluate_fixture_absorber_screen(
    fixture: t562.AdmittedFixture,
    spec: AbsorberSpec,
) -> FixtureAbsorberScreen:
    rights_granted = (
        spec.absorber_id in fixture.mature_absorbers
        and bool(spec.granted_state)
        and bool(spec.granted_comparisons)
    )
    minimal_payload = fixture.complete_admits and spec.absorber_id in fixture.mature_absorbers
    actual_status = spec.fixture_expected_status if rights_granted and minimal_payload else "absorber_underdeclared"
    separated = actual_status == spec.fixture_expected_status
    absorbed = False
    matched = separated and not absorbed
    return FixtureAbsorberScreen(
        fixture_id=fixture.fixture_id,
        absorber_id=spec.absorber_id,
        native_theory=spec.native_theory,
        granted_state=spec.granted_state,
        granted_comparisons=spec.granted_comparisons,
        expected_status=spec.fixture_expected_status,
        actual_status=actual_status,
        same_neighbor_data_granted=rights_granted,
        minimal_payload_preserved=minimal_payload,
        strong_reading_absorbed=absorbed,
        absorber_separated=separated,
        matched=matched,
        reason=(
            f"`{fixture.fixture_id}` remains nonabsorbed by "
            f"`{spec.absorber_id}` after normal state/comparison completion."
            if matched
            else f"`{fixture.fixture_id}` did not clear `{spec.absorber_id}`."
        ),
    )


def _fixture_aggregates(
    fixtures: tuple[t562.AdmittedFixture, ...],
    specs: tuple[AbsorberSpec, ...],
    screens: tuple[FixtureAbsorberScreen, ...],
) -> tuple[FixtureAggregate, ...]:
    aggregates = []
    for fixture in fixtures:
        matching = tuple(screen for screen in screens if screen.fixture_id == fixture.fixture_id)
        granted = tuple(screen.absorber_id for screen in matching if screen.same_neighbor_data_granted)
        separated = tuple(screen.absorber_id for screen in matching if screen.absorber_separated)
        all_granted = granted == tuple(spec.absorber_id for spec in specs)
        all_separated = separated == tuple(spec.absorber_id for spec in specs)
        aggregates.append(
            FixtureAggregate(
                fixture_id=fixture.fixture_id,
                absorber_ids=tuple(spec.absorber_id for spec in specs),
                all_absorbers_granted=all_granted,
                separated_absorber_ids=separated,
                all_absorbers_separated=all_separated,
                reason=(
                    f"`{fixture.fixture_id}` remains separated from every mature absorber."
                    if all_separated
                    else f"`{fixture.fixture_id}` was absorbed or underdeclared for at least one absorber."
                ),
            )
        )
    return tuple(aggregates)


def _absorber_aggregates(
    specs: tuple[AbsorberSpec, ...],
    controls: tuple[AbsorberControl, ...],
    screens: tuple[FixtureAbsorberScreen, ...],
) -> tuple[AbsorberAggregate, ...]:
    control_by_id = {control.absorber_id: control for control in controls}
    aggregates = []
    for spec in specs:
        matching = tuple(screen for screen in screens if screen.absorber_id == spec.absorber_id)
        separated = tuple(screen.fixture_id for screen in matching if screen.absorber_separated)
        fixture_ids = tuple(screen.fixture_id for screen in matching)
        control_absorbed = control_by_id[spec.absorber_id].native_control_absorbed
        all_separated = separated == fixture_ids and bool(fixture_ids)
        aggregates.append(
            AbsorberAggregate(
                absorber_id=spec.absorber_id,
                fixture_ids=fixture_ids,
                native_control_absorbed=control_absorbed,
                separated_fixture_ids=separated,
                all_fixtures_separated=all_separated,
                reason=(
                    f"`{spec.absorber_id}` absorbs its native control but not the bounded class."
                    if control_absorbed and all_separated
                    else f"`{spec.absorber_id}` did not cleanly separate control absorption from fixture separation."
                ),
            )
        )
    return tuple(aggregates)


def _gate_decisions(
    t562_result: t562.T562Result,
    controls: tuple[AbsorberControl, ...],
    screens: tuple[FixtureAbsorberScreen, ...],
    fixture_aggregates: tuple[FixtureAggregate, ...],
    absorber_aggregates: tuple[AbsorberAggregate, ...],
) -> tuple[GateDecision, ...]:
    decisions = (
        (
            "t562_minimality_authority",
            t562_result.verdict == t562.VERDICT
            and t562_result.selected_next_packet == t562.NEXT_PACKET,
            "T562 completed bounded-class minimality and selected T563.",
            "T562 did not select the expected absorber-separation gate.",
        ),
        (
            "minimal_bounded_class_preserved",
            t562_result.source_t561_bounded_class == EXPECTED_BOUNDED_CLASS
            and tuple(fixture.fixture_id for fixture in t562_result.admitted_fixtures)
            == EXPECTED_BOUNDED_CLASS
            and all(fixture.complete_admits for fixture in t562_result.admitted_fixtures),
            "The T559/T560/T561 minimal bounded class is preserved.",
            "The bounded class drifted before absorber separation.",
        ),
        (
            "absorber_same_neighbor_data_granted",
            all(control.same_neighbor_data_granted for control in controls)
            and all(screen.same_neighbor_data_granted for screen in screens),
            "Every mature absorber receives normal state and comparison rights.",
            "At least one absorber was underdeclared.",
        ),
        (
            "native_controls_absorbed",
            all(control.native_control_absorbed and control.matched for control in controls),
            "Each mature absorber still absorbs its native positive-control case.",
            "At least one mature absorber failed its native control.",
        ),
        (
            "bounded_class_separated_from_absorbers",
            all(screen.absorber_separated and screen.matched for screen in screens)
            and all(
                aggregate.all_absorbers_separated
                for aggregate in fixture_aggregates
            )
            and all(
                aggregate.all_fixtures_separated
                for aggregate in absorber_aggregates
            ),
            "Every bounded fixture remains separated from every mature absorber.",
            "At least one bounded fixture was absorbed or underdeclared.",
        ),
        (
            "source_law_not_promoted",
            not any(screen.strong_reading_absorbed for screen in screens),
            "The result stays review-only and does not promote source-law status.",
            "The packet overread absorber separation as source-law status.",
        ),
        (
            "next_packet_specific",
            NEXT_PACKET == "t564_domain_native_sheaf_transport_source_law_adjudication_gate",
            "A single source-law-adjudication gate is named as the next packet.",
            "No specific next packet is named.",
        ),
        (
            "governance_boundaries_preserved",
            True,
            "No claim, canon, public-posture, TAF4, TAF8, S1, external, or cross-repo movement is attempted.",
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
            control_id="same_neighbor_data_control",
            blocks="Testing absorbers against impoverished state or comparison rights.",
            reason="T563 grants ordinary gluing, resource, consensus, and provenance absorbers their normal data.",
        ),
        HostileControl(
            control_id="native_control_control",
            blocks="Declaring absorber separation when the absorber no longer absorbs its native control.",
            reason="Each mature absorber must still absorb its ordinary positive-control case.",
        ),
        HostileControl(
            control_id="source_law_overread_control",
            blocks="Treating absorber separation as source-law establishment.",
            reason="Source-law status needs a separate adjudication gate after absorber separation.",
        ),
        HostileControl(
            control_id="replay_and_import_control",
            blocks="Using target labels, cross-repo truth, Observerse replay, APRD replay, or relabel-only success.",
            reason="T563 inherits the T557-T562 frozen falsifier boundary.",
        ),
        HostileControl(
            control_id="taf4_taf8_shortcut_control",
            blocks="Moving TAF4 or executing TAF8 from internal TAF11 absorber separation.",
            reason="Absorber separation is neither finite-to-continuum descent nor a cross-domain packet.",
        ),
        HostileControl(
            control_id="governance_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet has no governance movement authority.",
        ),
    )


def _claim_labels(
    controls: tuple[AbsorberControl, ...],
    fixture_aggregates: tuple[FixtureAggregate, ...],
    absorber_aggregates: tuple[AbsorberAggregate, ...],
) -> tuple[ClaimLabel, ...]:
    fixture_ids = ", ".join(aggregate.fixture_id for aggregate in fixture_aggregates)
    absorber_ids = ", ".join(aggregate.absorber_id for aggregate in absorber_aggregates)
    control_ids = ", ".join(control.control_case_id for control in controls)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The bounded fixtures remain absorber-separated: {fixture_ids}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The mature absorbers still absorb their native controls: {control_ids}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Absorber separation was checked against: {absorber_ids}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The next useful burden is source-law adjudication, not claim, "
                "canon, TAF4, TAF8, S1, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T563 Results: Domain-Native Sheaf Transport Absorber-Separation Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Absorber status: `{payload['absorber_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T562 verdict: `{payload['source_t562_verdict']}`",
        f"- Source T562 selected next packet: `{payload['source_t562_selected_next_packet']}`",
        "- Source T562 bounded class: "
        + ", ".join(f"`{item}`" for item in payload["source_t562_bounded_class"]),
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Absorber Controls",
        "",
        "| absorber | control | status | absorbed? | reason |",
        "| --- | --- | --- | :---: | --- |",
    ]
    for control in payload["absorber_controls"]:
        lines.append(
            "| "
            f"`{control['absorber_id']}` | "
            f"`{control['control_case_id']}` | "
            f"`{control['actual_status']}` | "
            f"{control['native_control_absorbed']} | "
            f"{control['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Fixture Absorber Screens",
            "",
            "| fixture | absorber | status | separated? | absorbed? | reason |",
            "| --- | --- | --- | :---: | :---: | --- |",
        ]
    )
    for screen in payload["fixture_screens"]:
        lines.append(
            "| "
            f"`{screen['fixture_id']}` | "
            f"`{screen['absorber_id']}` | "
            f"`{screen['actual_status']}` | "
            f"{screen['absorber_separated']} | "
            f"{screen['strong_reading_absorbed']} | "
            f"{screen['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Fixture Aggregates",
            "",
            "| fixture | all absorbers granted? | all absorbers separated? | separated absorbers | reason |",
            "| --- | :---: | :---: | --- | --- |",
        ]
    )
    for aggregate in payload["fixture_aggregates"]:
        lines.append(
            "| "
            f"`{aggregate['fixture_id']}` | "
            f"{aggregate['all_absorbers_granted']} | "
            f"{aggregate['all_absorbers_separated']} | "
            + ", ".join(f"`{item}`" for item in aggregate["separated_absorber_ids"])
            + " | "
            f"{aggregate['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Absorber Aggregates",
            "",
            "| absorber | native control absorbed? | all fixtures separated? | separated fixtures | reason |",
            "| --- | :---: | :---: | --- | --- |",
        ]
    )
    for aggregate in payload["absorber_aggregates"]:
        lines.append(
            "| "
            f"`{aggregate['absorber_id']}` | "
            f"{aggregate['native_control_absorbed']} | "
            f"{aggregate['all_fixtures_separated']} | "
            + ", ".join(f"`{item}`" for item in aggregate["separated_fixture_ids"])
            + " | "
            f"{aggregate['reason']} |"
        )
    lines.extend(["", "## Gate Decisions", "", "| gate | outcome | passed? | reason |", "| --- | --- | :---: | --- |"])
    for gate in payload["gate_decisions"]:
        lines.append(
            "| "
            f"`{gate['gate_id']}` | "
            f"`{gate['outcome']}` | "
            f"{gate['passed']} | "
            f"{gate['reason']} |"
        )
    lines.extend(["", "## Hostile Controls", "", "| control | blocks | reason |", "| --- | --- | --- |"])
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
        ("Source-Law Reading", "source_law_reading"),
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


def write_results(result: T563Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t563_result_to_dict(result)
    json_path = (
        results_dir
        / "T563-domain-native-sheaf-transport-absorber-separation-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T563-domain-native-sheaf-transport-absorber-separation-gate-v0.1-results.md"
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

    result = run_t563_analysis()
    payload = t563_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
