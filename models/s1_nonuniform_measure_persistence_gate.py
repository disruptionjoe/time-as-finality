"""T490: S1 nonuniform measure persistence gate.

T223 closed the uniform finite ordinal ensemble route for S1: the stable
T54/T126/T156/T159 survivor tail decays through n=8 and stays structurally
thin. T464 then made the next admission burden executable: a future S1 packet
needs a predeclared added assumption, such as a natural nonuniform measure,
selection law, sprinkling law, or continuum bridge.

T490 narrows the measure branch. It checks whether a proposed post-T223
measure packet is more than one of the cheap restarts:

* rerun the uniform ordinal baseline;
* condition directly on the known survivor tail;
* condition on the existing guardrail screens and call that a measure;
* show a single-size positive;
* change the screens after T223;
* ask for S1 promotion or public posture from the gate itself.

This is a gate only. It does not promote S1, reverse T223, derive spacetime,
or assert manifoldlikeness, Lorentzian geometry, GR, QFT, sprinkling, locality,
embedding, covariance, or a continuum theorem.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T490-s1-nonuniform-measure-persistence-gate-v0.1"
VERDICT = "S1_NONUNIFORM_MEASURE_PERSISTENCE_GATE_BUILT_SCREEN_CONDITIONING_NOT_ENOUGH"

SOURCE_OPEN_PROBLEM = "open-problems/spacetime-as-finality-colimit.md"
SOURCE_T223 = "results/t54-ordinal-scaling-decisive-v0.1-results.md"
SOURCE_T464 = "results/T464-s1-added-assumption-admission-gate-v0.1-results.md"

# A finite review floor, not an asymptotic theorem. The point is to block
# packets that do not even state a multi-size nonvanishing-mass target.
NONVANISHING_REVIEW_FLOOR = Fraction(1, 20)


@dataclass(frozen=True)
class T223SizeCensus:
    event_count: int
    total_cases: int
    parent_interval_pass_count: int
    stable_survivor_count: int

    @property
    def uniform_survivor_mass(self) -> Fraction:
        return Fraction(self.stable_survivor_count, self.total_cases)

    @property
    def parent_conditioned_survivor_mass(self) -> Fraction:
        return Fraction(self.stable_survivor_count, self.parent_interval_pass_count)


@dataclass(frozen=True)
class MeasurePacket:
    packet_id: str
    description: str
    measure_kind: str
    declares_t223_context: bool
    predeclared_before_scoring: bool
    has_independent_generating_law: bool
    finite_audit_fixed_screens: bool
    audited_sizes: tuple[int, ...]
    provides_nonvanishing_mass_claim: bool
    names_lorentzian_targets: bool
    uses_uniform_ordinal_baseline: bool = False
    conditions_on_survivor_success: bool = False
    conditions_on_guardrail_screen: bool = False
    changes_t126_t156_t159_screens: bool = False
    uses_single_size_positive: bool = False
    declared_survivor_masses: tuple[tuple[int, Fraction], ...] = ()
    requests_s1_promotion: bool = False
    requests_public_posture: bool = False
    requires_non_github_external_action: bool = False
    overclaims_spacetime_or_lorentzian_result: bool = False
    synthetic_control_only: bool = False


@dataclass(frozen=True)
class MeasureDecision:
    packet_id: str
    admitted: bool
    gate_label: str
    classification: str
    admitted_as_future_review_target: bool
    counts_as_s1_evidence: bool
    missing_requirements: tuple[str, ...]
    survivor_mass_trajectory: tuple[tuple[int, Fraction], ...]
    notes: tuple[str, ...]


def t223_census() -> tuple[T223SizeCensus, ...]:
    """Return the T223 exact n=6..8 census used by this gate."""

    return (
        T223SizeCensus(
            event_count=6,
            total_cases=720,
            parent_interval_pass_count=156,
            stable_survivor_count=26,
        ),
        T223SizeCensus(
            event_count=7,
            total_cases=5040,
            parent_interval_pass_count=561,
            stable_survivor_count=174,
        ),
        T223SizeCensus(
            event_count=8,
            total_cases=40320,
            parent_interval_pass_count=2057,
            stable_survivor_count=361,
        ),
    )


def measure_packets() -> tuple[MeasurePacket, ...]:
    return (
        MeasurePacket(
            packet_id="uniform_ordinal_baseline",
            description="Rerun the exact 1+1 ordinal rank-permutation ensemble.",
            measure_kind="uniform_ordinal",
            declares_t223_context=True,
            predeclared_before_scoring=True,
            has_independent_generating_law=True,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=False,
            names_lorentzian_targets=False,
            uses_uniform_ordinal_baseline=True,
        ),
        MeasurePacket(
            packet_id="known_survivor_tail_indicator",
            description="Put all mass on the already-known T223 survivors.",
            measure_kind="tail_indicator",
            declares_t223_context=True,
            predeclared_before_scoring=False,
            has_independent_generating_law=False,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=False,
            conditions_on_survivor_success=True,
        ),
        MeasurePacket(
            packet_id="parent_interval_conditioned_measure",
            description=(
                "Normalize only over the T159 parent-interval guardrail pass set "
                "and read its conditional survivor mass as a natural measure."
            ),
            measure_kind="guardrail_conditioned",
            declares_t223_context=True,
            predeclared_before_scoring=False,
            has_independent_generating_law=False,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=False,
            conditions_on_guardrail_screen=True,
        ),
        MeasurePacket(
            packet_id="full_screen_stack_conditioned_measure",
            description="Condition on passing the current finite screen stack.",
            measure_kind="guardrail_conditioned",
            declares_t223_context=True,
            predeclared_before_scoring=False,
            has_independent_generating_law=False,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=False,
            conditions_on_survivor_success=True,
            conditions_on_guardrail_screen=True,
        ),
        MeasurePacket(
            packet_id="screen_drift_after_t223",
            description="Change T126/T156/T159 after seeing the T223 tail.",
            measure_kind="selection_rule",
            declares_t223_context=True,
            predeclared_before_scoring=False,
            has_independent_generating_law=False,
            finite_audit_fixed_screens=False,
            audited_sizes=(8,),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=False,
            changes_t126_t156_t159_screens=True,
        ),
        MeasurePacket(
            packet_id="single_size_n8_positive",
            description="Declare a positive nonuniform weight only at n=8.",
            measure_kind="nonuniform_measure",
            declares_t223_context=True,
            predeclared_before_scoring=True,
            has_independent_generating_law=True,
            finite_audit_fixed_screens=True,
            audited_sizes=(8,),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=True,
            uses_single_size_positive=True,
            declared_survivor_masses=((8, Fraction(1, 4)),),
        ),
        MeasurePacket(
            packet_id="unjustified_nonuniform_weight",
            description="Declare weights with no finality-native or neighbor-theory law.",
            measure_kind="nonuniform_measure",
            declares_t223_context=True,
            predeclared_before_scoring=True,
            has_independent_generating_law=False,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=True,
            declared_survivor_masses=(
                (6, Fraction(1, 5)),
                (7, Fraction(1, 6)),
                (8, Fraction(1, 7)),
            ),
        ),
        MeasurePacket(
            packet_id="nonvanishing_but_no_lorentzian_targets",
            description="A predeclared finite measure with no later causal/metric constraints.",
            measure_kind="nonuniform_measure",
            declares_t223_context=True,
            predeclared_before_scoring=True,
            has_independent_generating_law=True,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=False,
            declared_survivor_masses=(
                (6, Fraction(1, 5)),
                (7, Fraction(3, 16)),
                (8, Fraction(1, 6)),
            ),
        ),
        MeasurePacket(
            packet_id="claim_promotion_shortcut",
            description="Promote S1 because a measure gate admits a future target.",
            measure_kind="nonuniform_measure",
            declares_t223_context=True,
            predeclared_before_scoring=True,
            has_independent_generating_law=True,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=True,
            declared_survivor_masses=(
                (6, Fraction(1, 5)),
                (7, Fraction(3, 16)),
                (8, Fraction(1, 6)),
            ),
            requests_s1_promotion=True,
            synthetic_control_only=True,
        ),
        MeasurePacket(
            packet_id="external_publication_shortcut",
            description="Require external publication before local finite audit.",
            measure_kind="continuum_bridge",
            declares_t223_context=True,
            predeclared_before_scoring=True,
            has_independent_generating_law=True,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=True,
            declared_survivor_masses=(
                (6, Fraction(1, 5)),
                (7, Fraction(3, 16)),
                (8, Fraction(1, 6)),
            ),
            requires_non_github_external_action=True,
            synthetic_control_only=True,
        ),
        MeasurePacket(
            packet_id="synthetic_predeclared_measure_review_target",
            description=(
                "Synthetic future target with a predeclared finality-native "
                "measure law, fixed screens, multi-size audit, nonvanishing "
                "finite survivor mass, and named later Lorentzian constraints."
            ),
            measure_kind="nonuniform_measure",
            declares_t223_context=True,
            predeclared_before_scoring=True,
            has_independent_generating_law=True,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=True,
            declared_survivor_masses=(
                (6, Fraction(1, 5)),
                (7, Fraction(3, 16)),
                (8, Fraction(1, 6)),
            ),
            synthetic_control_only=True,
        ),
        MeasurePacket(
            packet_id="synthetic_continuum_bridge_weight_target",
            description=(
                "Synthetic future target whose finite approximant weights are "
                "audited before any continuum or Lorentzian reading."
            ),
            measure_kind="continuum_bridge",
            declares_t223_context=True,
            predeclared_before_scoring=True,
            has_independent_generating_law=True,
            finite_audit_fixed_screens=True,
            audited_sizes=(6, 7, 8),
            provides_nonvanishing_mass_claim=True,
            names_lorentzian_targets=True,
            declared_survivor_masses=(
                (6, Fraction(3, 20)),
                (7, Fraction(7, 50)),
                (8, Fraction(1, 8)),
            ),
            synthetic_control_only=True,
        ),
    )


def evaluate_packet(packet: MeasurePacket) -> MeasureDecision:
    mass_trajectory = survivor_mass_trajectory(packet)
    missing = missing_requirements(packet, mass_trajectory)
    notes: list[str] = []

    if packet.overclaims_spacetime_or_lorentzian_result:
        label = "BLOCKED_SPACETIME_OR_LORENTZIAN_OVERCLAIM"
        classification = "governance_boundary_block"
        admitted = False
        notes.append("T490 cannot derive spacetime or Lorentzian structure.")
    elif packet.requests_s1_promotion:
        label = "BLOCKED_S1_PROMOTION_REQUEST"
        classification = "governance_boundary_block"
        admitted = False
        notes.append("Measure admission is not S1 evidence or promotion.")
    elif packet.requests_public_posture:
        label = "BLOCKED_PUBLIC_POSTURE_REQUEST"
        classification = "governance_boundary_block"
        admitted = False
        notes.append("Public posture movement is outside this gate.")
    elif packet.requires_non_github_external_action:
        label = "BLOCKED_EXTERNAL_ACTION_REQUIRED"
        classification = "external_action_block"
        admitted = False
        notes.append("External publication or outreach needs separate authorization.")
    elif packet.uses_uniform_ordinal_baseline:
        label = "REJECTED_UNIFORM_BASELINE_CLOSED_BY_T223"
        classification = "uniform_t223_baseline_rejection"
        admitted = False
        notes.append("Uniform finite ordinal enumeration is the T223 no-go baseline.")
    elif packet.conditions_on_survivor_success:
        label = "REJECTED_TAIL_INDICATOR_OR_SUCCESS_CONDITIONING"
        classification = "tail_tuned_measure_rejection"
        admitted = False
        notes.append("Conditioning on the known survivor tail is circular.")
    elif packet.conditions_on_guardrail_screen:
        label = "REJECTED_GUARDRAIL_SCREEN_CONDITIONING"
        classification = "screen_conditioned_measure_rejection"
        admitted = False
        notes.append("Guardrail conditioning is diagnostic normalization, not a natural measure.")
    elif packet.changes_t126_t156_t159_screens:
        label = "REJECTED_SCREEN_DRIFT_AFTER_T223"
        classification = "screen_drift_rejection"
        admitted = False
        notes.append("Changing screens after T223 is target drift.")
    elif packet.uses_single_size_positive or len(packet.audited_sizes) < 2:
        label = "REJECTED_SINGLE_SIZE_POSITIVE"
        classification = "single_size_rejection"
        admitted = False
        notes.append("T490 requires multi-size persistence or a declared limit target.")
    elif missing:
        label = _first_missing_label(missing)
        classification = "missing_measure_requirement_rejection"
        admitted = False
        notes.append("The packet lacks the T490 measure-persistence burden.")
    else:
        label = "ADMITTED_MEASURE_PERSISTENCE_REVIEW_TARGET_NO_PROMOTION"
        classification = "future_measure_persistence_review_target"
        admitted = True
        notes.append("Admission is review-only and counts as no S1 evidence.")

    return MeasureDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        gate_label=label,
        classification=classification,
        admitted_as_future_review_target=admitted,
        counts_as_s1_evidence=False,
        missing_requirements=missing,
        survivor_mass_trajectory=mass_trajectory,
        notes=tuple(notes),
    )


def run_t490_analysis() -> dict[str, Any]:
    census = t223_census()
    packets = measure_packets()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    admitted = tuple(
        decision.packet_id
        for decision in decisions
        if decision.admitted_as_future_review_target
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": VERDICT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t223_results": SOURCE_T223,
            "t464_results": SOURCE_T464,
        },
        "t223_census": [_census_to_dict(item) for item in census],
        "uniform_survivor_mass_trajectory": _trajectory_to_dict(
            tuple((item.event_count, item.uniform_survivor_mass) for item in census)
        ),
        "parent_interval_conditioned_survivor_mass_trajectory": _trajectory_to_dict(
            tuple(
                (item.event_count, item.parent_conditioned_survivor_mass)
                for item in census
            )
        ),
        "nonvanishing_review_floor": _fraction_to_dict(NONVANISHING_REVIEW_FLOOR),
        "packets": [_packet_to_dict(packet) for packet in packets],
        "decisions": [_decision_to_dict(decision) for decision in decisions],
        "admitted_future_targets": list(admitted),
        "all_admitted_targets_are_synthetic_only": all(
            _packet_by_id(packets, packet_id).synthetic_control_only
            for packet_id in admitted
        ),
        "s1_promoted": False,
        "t223_reversed": False,
        "claim_ledger_update": "none",
        "strongest_reading": (
            "T490 makes T464's nonuniform-measure branch sharper. The T223 "
            "uniform baseline stays closed; putting mass on known survivors is "
            "tail tuning; normalizing over parent-interval or screen-stack "
            "passes is guardrail conditioning, not an independent natural "
            "measure; and a single-size positive is insufficient. Only a future "
            "packet with a predeclared independent generating law, fixed finite "
            "screens, multi-size or limit persistence, a nonvanishing-mass "
            "claim, and named later Lorentzian constraints is admitted for "
            "review. Admission is not S1 evidence."
        ),
        "future_packet_minimum": [
            "inherit T223 finite no-go and T464 admission burden",
            "predeclare the nonuniform measure, selection law, sprinkling law, or continuum bridge before scoring survivors",
            "supply an independent finality-native or neighbor-theory generating law",
            "keep T126/T156/T159/T223 finite screens fixed",
            "audit at least two finite sizes or declare a real limit target",
            "state a nonvanishing survivor-mass or concentration target before scoring",
            "do not condition directly on survivor success or guardrail-screen pass predicates",
            "name later causal, metric, covariance, locality, embedding, or Lorentzian constraints",
            "make no S1 promotion, spacetime derivation, public-posture, or external-action shortcut",
        ],
        "not_earned": [
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
            "ROADMAP movement",
            "README movement",
            "North Star movement",
            "public-posture movement",
            "cross-repo truth movement",
        ],
    }


def run() -> dict[str, Any]:
    return run_t490_analysis()


def survivor_mass_trajectory(packet: MeasurePacket) -> tuple[tuple[int, Fraction], ...]:
    if packet.declared_survivor_masses:
        return tuple(sorted(packet.declared_survivor_masses))

    census_by_size = {item.event_count: item for item in t223_census()}
    sizes = packet.audited_sizes or tuple(census_by_size)
    trajectory: list[tuple[int, Fraction]] = []
    for size in sizes:
        item = census_by_size.get(size)
        if item is None:
            continue
        if packet.conditions_on_survivor_success:
            trajectory.append((size, Fraction(1, 1)))
        elif packet.conditions_on_guardrail_screen:
            trajectory.append((size, item.parent_conditioned_survivor_mass))
        else:
            trajectory.append((size, item.uniform_survivor_mass))
    return tuple(trajectory)


def missing_requirements(
    packet: MeasurePacket,
    mass_trajectory: tuple[tuple[int, Fraction], ...],
) -> tuple[str, ...]:
    missing: list[str] = []

    if not packet.declares_t223_context:
        missing.append("t223_context_declared")
    if not packet.predeclared_before_scoring:
        missing.append("predeclared_before_scoring")
    if not packet.has_independent_generating_law:
        missing.append("independent_generating_law")
    if not packet.finite_audit_fixed_screens:
        missing.append("finite_audit_fixed_screens")
    if len(packet.audited_sizes) < 2:
        missing.append("multi_size_or_limit_audit")
    if not packet.provides_nonvanishing_mass_claim:
        missing.append("nonvanishing_mass_claim")
    if not mass_trajectory:
        missing.append("survivor_mass_trajectory")
    elif any(value < NONVANISHING_REVIEW_FLOOR for _, value in mass_trajectory):
        missing.append("nonvanishing_review_floor")
    if not packet.names_lorentzian_targets:
        missing.append("later_lorentzian_constraints_named")
    if packet.uses_uniform_ordinal_baseline:
        missing.append("not_uniform_t223_baseline")
    if packet.conditions_on_survivor_success:
        missing.append("not_conditioned_on_survivor_success")
    if packet.conditions_on_guardrail_screen:
        missing.append("not_guardrail_screen_conditioned")
    if packet.changes_t126_t156_t159_screens:
        missing.append("no_screen_drift")
    if packet.requests_s1_promotion:
        missing.append("no_s1_promotion_request")
    if packet.requests_public_posture:
        missing.append("no_public_posture_request")
    if packet.requires_non_github_external_action:
        missing.append("no_external_action_required")
    if packet.overclaims_spacetime_or_lorentzian_result:
        missing.append("no_spacetime_or_lorentzian_overclaim")

    return tuple(missing)


def render_markdown(result: dict[str, Any]) -> str:
    census_rows = [
        "| {n} | {total} | {parent} | {stable} | {uniform} | {conditioned} |".format(
            n=item["event_count"],
            total=item["total_cases"],
            parent=item["parent_interval_pass_count"],
            stable=item["stable_survivor_count"],
            uniform=item["uniform_survivor_mass"]["fraction"],
            conditioned=item["parent_conditioned_survivor_mass"]["fraction"],
        )
        for item in result["t223_census"]
    ]
    decision_rows = [
        "| {packet} | {admitted} | {label} | {classification} | {mass} | {missing} | {notes} |".format(
            packet=item["packet_id"],
            admitted=item["admitted"],
            label=item["gate_label"],
            classification=item["classification"],
            mass=", ".join(
                f"n={entry['event_count']}:{entry['value']['fraction']}"
                for entry in item["survivor_mass_trajectory"]
            )
            or "none",
            missing=", ".join(item["missing_requirements"]) or "none",
            notes="; ".join(item["notes"]) or "none",
        )
        for item in result["decisions"]
    ]
    future_minimum = [f"- {item}" for item in result["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in result["not_earned"]]

    return "\n".join(
        [
            "# T490 - S1 Nonuniform Measure Persistence Gate - v0.1 results",
            "",
            "> Measure-persistence gate only. No S1 promotion, T223 reversal, "
            "claim-ledger movement, roadmap movement, README movement, North "
            "Star movement, public posture, or cross-repo truth.",
            "",
            "- Spec: `tests/T490-s1-nonuniform-measure-persistence-gate.md`",
            "- Model: `models/s1_nonuniform_measure_persistence_gate.py`",
            "- Tests: `tests/test_s1_nonuniform_measure_persistence_gate.py`",
            "- Artifact JSON: `results/T490-s1-nonuniform-measure-persistence-gate-v0.1.json`",
            f"- Sources: `{SOURCE_T223}`, `{SOURCE_T464}`, `{SOURCE_OPEN_PROBLEM}`",
            "",
            f"## Overall verdict: {result['verdict']}",
            "",
            result["strongest_reading"],
            "",
            "## T223 Baseline Used By This Gate",
            "",
            "| n | total cases | parent-interval pass | stable survivors | uniform survivor mass | parent-conditioned survivor mass |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
            *census_rows,
            "",
            "The parent-conditioned trajectory is reported as a diagnostic. It is "
            "not a natural measure by itself because it normalizes over an "
            "existing guardrail predicate.",
            "",
            "## Packet Decisions",
            "",
            "| packet | admitted? | gate label | classification | survivor mass trajectory | missing requirements | notes |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *decision_rows,
            "",
            "## Future Packet Minimum",
            "",
            *future_minimum,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _first_missing_label(missing: tuple[str, ...]) -> str:
    priority = (
        ("t223_context_declared", "REJECTED_NO_T223_CONTEXT"),
        ("predeclared_before_scoring", "REJECTED_POST_HOC_MEASURE"),
        ("independent_generating_law", "REJECTED_NO_INDEPENDENT_GENERATING_LAW"),
        ("finite_audit_fixed_screens", "REJECTED_NO_FIXED_SCREEN_AUDIT"),
        ("multi_size_or_limit_audit", "REJECTED_NO_MULTI_SIZE_OR_LIMIT_AUDIT"),
        ("nonvanishing_mass_claim", "REJECTED_NO_NONVANISHING_MASS_CLAIM"),
        ("survivor_mass_trajectory", "REJECTED_NO_SURVIVOR_MASS_TRAJECTORY"),
        ("nonvanishing_review_floor", "REJECTED_SURVIVOR_MASS_BELOW_REVIEW_FLOOR"),
        ("later_lorentzian_constraints_named", "REJECTED_NO_LORENTZIAN_CONSTRAINT_TARGETS"),
    )
    for key, label in priority:
        if key in missing:
            return label
    return "REJECTED_MISSING_MEASURE_PERSISTENCE_REQUIREMENTS"


def _packet_by_id(
    packets: tuple[MeasurePacket, ...],
    packet_id: str,
) -> MeasurePacket:
    for packet in packets:
        if packet.packet_id == packet_id:
            return packet
    raise KeyError(packet_id)


def _census_to_dict(item: T223SizeCensus) -> dict[str, Any]:
    return {
        "event_count": item.event_count,
        "total_cases": item.total_cases,
        "parent_interval_pass_count": item.parent_interval_pass_count,
        "stable_survivor_count": item.stable_survivor_count,
        "uniform_survivor_mass": _fraction_to_dict(item.uniform_survivor_mass),
        "parent_conditioned_survivor_mass": _fraction_to_dict(
            item.parent_conditioned_survivor_mass
        ),
    }


def _packet_to_dict(packet: MeasurePacket) -> dict[str, Any]:
    return {
        "packet_id": packet.packet_id,
        "description": packet.description,
        "measure_kind": packet.measure_kind,
        "declares_t223_context": packet.declares_t223_context,
        "predeclared_before_scoring": packet.predeclared_before_scoring,
        "has_independent_generating_law": packet.has_independent_generating_law,
        "finite_audit_fixed_screens": packet.finite_audit_fixed_screens,
        "audited_sizes": list(packet.audited_sizes),
        "provides_nonvanishing_mass_claim": packet.provides_nonvanishing_mass_claim,
        "names_lorentzian_targets": packet.names_lorentzian_targets,
        "uses_uniform_ordinal_baseline": packet.uses_uniform_ordinal_baseline,
        "conditions_on_survivor_success": packet.conditions_on_survivor_success,
        "conditions_on_guardrail_screen": packet.conditions_on_guardrail_screen,
        "changes_t126_t156_t159_screens": packet.changes_t126_t156_t159_screens,
        "uses_single_size_positive": packet.uses_single_size_positive,
        "declared_survivor_masses": _trajectory_to_dict(
            packet.declared_survivor_masses
        ),
        "requests_s1_promotion": packet.requests_s1_promotion,
        "requests_public_posture": packet.requests_public_posture,
        "requires_non_github_external_action": (
            packet.requires_non_github_external_action
        ),
        "overclaims_spacetime_or_lorentzian_result": (
            packet.overclaims_spacetime_or_lorentzian_result
        ),
        "synthetic_control_only": packet.synthetic_control_only,
    }


def _decision_to_dict(decision: MeasureDecision) -> dict[str, Any]:
    return {
        "packet_id": decision.packet_id,
        "admitted": decision.admitted,
        "gate_label": decision.gate_label,
        "classification": decision.classification,
        "admitted_as_future_review_target": decision.admitted_as_future_review_target,
        "counts_as_s1_evidence": decision.counts_as_s1_evidence,
        "missing_requirements": list(decision.missing_requirements),
        "survivor_mass_trajectory": _trajectory_to_dict(
            decision.survivor_mass_trajectory
        ),
        "notes": list(decision.notes),
    }


def _trajectory_to_dict(
    trajectory: tuple[tuple[int, Fraction], ...],
) -> list[dict[str, Any]]:
    return [
        {"event_count": size, "value": _fraction_to_dict(value)}
        for size, value in trajectory
    ]


def _fraction_to_dict(value: Fraction) -> dict[str, Any]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t490_analysis()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
