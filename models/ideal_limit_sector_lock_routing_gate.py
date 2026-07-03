"""T440 - ideal-limit / sector-lock routing gate.

T439 routed exact ideal-limit and sector-lock packets to a separate
E1/E3/idealization spec. T440 implements that spec as a recorded-tier routing
gate. It admits only synthetic future-review shapes and does not promote H7,
E1, E3, or any public claim.

Run:

    python -m models.ideal_limit_sector_lock_routing_gate --write-results
    python -m pytest tests/test_ideal_limit_sector_lock_routing_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T440-ideal-limit-sector-lock-routing-gate-v0.1"
SOURCE_T439 = "results/T439-finite-time-catalytic-thermo-witness-gate-v0.1-results.md"
SOURCE_T168 = "results/h7-sector-restriction-screen-v0.1-results.md"
SOURCE_N14 = "literature/N14-h7-sector-gauge-absorber.md"
SOURCE_T436 = "results/T436-quantum-e3-resource-lift-classifier-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "IDEAL_LIMIT_SECTOR_LOCK_ROUTING_GATE_BUILT_NO_PROMOTION"
HONEST_CEILING = (
    "Recorded-tier routing gate only. T440 does not promote H7, prove an E1 "
    "limit theorem, prove an E3 no-go theorem, prove WAY, authorize public "
    "posture, or move the claim ledger."
)


@dataclass(frozen=True)
class IdealizationPacket:
    packet_id: str
    description: str
    infinite_barrier_idealization: bool = False
    exact_sector_rule: bool = False
    finite_operational_substrate: bool = False
    family_limit_declared: bool = False
    finite_approximants_declared: bool = False
    limit_invariant_declared: bool = False
    recovery_cost_diverges_across_family: bool = False
    single_instance_claim: bool = False
    gauge_invariant_record_distinction: bool = False
    physical_record_deletion_reverse_edge: bool = False
    task_natural_future_operation_split: bool = False
    absorbers_matched: bool = False
    reservoirs_boundaries_references_accounted: bool = False
    allowed_controls_declared: bool = False
    a2_resource_lift_audited: bool = False
    exact_no_go_after_resource_lift: bool = False
    reference_frame_or_reservoir_restores: bool = False
    compensating_reservoir_available: bool = False
    pure_gauge_relabel: bool = False
    finite_enforcement_or_leakage_path: bool = False
    finite_barrier_only: bool = False
    post_hoc_selector: bool = False
    changed_resource_boundary: bool = False
    synthetic_e1_control: bool = False
    synthetic_e3_control: bool = False


def _packet_to_dict(packet: IdealizationPacket) -> dict[str, Any]:
    return asdict(packet)


def classify_packet(packet: IdealizationPacket) -> dict[str, Any]:
    admitted = False
    route = "rejected"
    label = "REJECTED_UNCLASSIFIED"
    reason = "No ideal-limit or sector-lock routing rule matched."

    if packet.post_hoc_selector:
        label = "REJECTED_POST_HOC_IDEALIZATION_SELECTOR"
        reason = "The idealization or sector rule is chosen after seeing the target pair."
    elif packet.pure_gauge_relabel:
        route = "h7_null_or_nonphysical"
        label = "H7_NULL_GAUGE_REPRESENTATIVE_CHANGE"
        reason = "A gauge representative change is not gauge-invariant physical record deletion."
    elif packet.finite_barrier_only or packet.finite_enforcement_or_leakage_path:
        route = "absorbed"
        label = "ABSORBED_BY_FINITE_CONTROL_OR_KINETICS"
        reason = "Finite barriers, enforcement hardware, or leakage paths are control/kinetic accounting."
    elif packet.changed_resource_boundary:
        label = "REJECTED_CHANGED_RESOURCE_BOUNDARY"
        reason = "The comparison changes reservoirs, reference resources, controls, or boundary data."
    elif packet.compensating_reservoir_available or packet.reference_frame_or_reservoir_restores:
        route = "e0_resource_completion"
        label = "E0_DECLARED_BY_RESERVOIR_OR_REFERENCE_COMPLETION"
        reason = "A compensating reservoir, boundary mode, or reference resource restores the distinction."
    elif packet.infinite_barrier_idealization and not packet.family_limit_declared:
        route = "h7_null_or_nonphysical"
        label = "H7_NULL_INFINITE_BARRIER_IDEALIZATION"
        reason = "An infinite barrier is an ideal constructor restriction, not a finite substrate result."
    elif packet.exact_sector_rule and not packet.finite_operational_substrate:
        route = "h7_null_or_nonphysical"
        label = "H7_NULL_EXACT_SECTOR_STIPULATION"
        reason = "An exact sector ban without finite operational substrate is an ideal operation-class ban."
    elif packet.family_limit_declared:
        if packet.single_instance_claim:
            label = "REJECTED_E1_CANNOT_BE_SINGLE_INSTANCE"
            reason = "E1 ideal-limit routing is family-level, not a single-instance boundary."
        elif not (
            packet.finite_approximants_declared
            and packet.limit_invariant_declared
            and packet.recovery_cost_diverges_across_family
        ):
            label = "REJECTED_INCOMPLETE_E1_LIMIT_PACKET"
            reason = (
                "E1 review needs finite approximants, a declared limit invariant, "
                "and diverging recovery cost or nonlocality across the family."
            )
        else:
            admitted = True
            route = "e1_family_limit_review"
            label = "ADMITTED_E1_IDEAL_LIMIT_REVIEW_NO_PROMOTION"
            reason = (
                "The packet freezes a family-level ideal-limit shape. It is admitted "
                "only for future E1 review, not as H7 evidence or a theorem."
            )
    elif packet.exact_sector_rule:
        if not packet.gauge_invariant_record_distinction:
            label = "REJECTED_NO_GAUGE_INVARIANT_RECORD_DISTINCTION"
            reason = "A sector-lock packet must name a gauge-invariant record distinction."
        elif not (
            packet.absorbers_matched
            and packet.reservoirs_boundaries_references_accounted
            and packet.allowed_controls_declared
        ):
            label = "REJECTED_INCOMPLETE_SECTOR_ACCOUNTING"
            reason = "Conserved quantities, reservoirs, boundary modes, references, and controls are not fixed."
        elif not packet.a2_resource_lift_audited:
            label = "BLOCKED_MISSING_A2_RESOURCE_LIFT_AUDIT"
            reason = "T436 requires an A2 resource/reference audit before reading A1 obstruction as E3."
        elif not packet.exact_no_go_after_resource_lift:
            route = "e0_resource_completion"
            label = "E0_DECLARED_AFTER_A2_RESOURCE_LIFT"
            reason = "The obstruction is A1-relative and becomes declared once A2 resources are admitted."
        elif not packet.task_natural_future_operation_split:
            label = "REJECTED_NO_TASK_NATURAL_CAPABILITY_SPLIT"
            reason = "No task-natural future-operation split is declared."
        else:
            admitted = True
            route = "e3_exact_no_go_review"
            label = "ADMITTED_E3_EXACT_NO_GO_REVIEW_NO_PROMOTION"
            reason = (
                "The packet freezes an exact no-go shape after absorber and A2 "
                "resource-lift audit. It is admitted only for future E3 review."
            )

    return {
        "packet": _packet_to_dict(packet),
        "admitted_for_future_review": admitted,
        "route": route,
        "label": label,
        "reason": reason,
    }


def candidate_packets() -> tuple[IdealizationPacket, ...]:
    return (
        IdealizationPacket(
            packet_id="infinite_barrier_single_instance",
            description="A single record protected only by an infinite barrier idealization.",
            infinite_barrier_idealization=True,
            single_instance_claim=True,
        ),
        IdealizationPacket(
            packet_id="exact_sector_local_ban",
            description="A local exact-sector operation ban with no finite substrate reading.",
            exact_sector_rule=True,
        ),
        IdealizationPacket(
            packet_id="gauge_relabel_lock",
            description="A claimed deletion event that only changes gauge representative.",
            exact_sector_rule=True,
            pure_gauge_relabel=True,
        ),
        IdealizationPacket(
            packet_id="compensating_reservoir_sector",
            description="A conserved-sector lock lifted by a compensating reservoir.",
            exact_sector_rule=True,
            finite_operational_substrate=True,
            compensating_reservoir_available=True,
        ),
        IdealizationPacket(
            packet_id="reference_frame_lifted_phase_lock",
            description="An A1 phase/sector lock restored by an admitted reference resource.",
            exact_sector_rule=True,
            finite_operational_substrate=True,
            reference_frame_or_reservoir_restores=True,
        ),
        IdealizationPacket(
            packet_id="finite_symmetry_enforcement",
            description="A finite enforcement or leakage-path implementation of a sector lock.",
            exact_sector_rule=True,
            finite_operational_substrate=True,
            finite_enforcement_or_leakage_path=True,
        ),
        IdealizationPacket(
            packet_id="post_hoc_idealization_selector",
            description="A selector that chooses an idealization after seeing the failure pair.",
            post_hoc_selector=True,
        ),
        IdealizationPacket(
            packet_id="incomplete_e1_limit_packet",
            description="A family-limit packet missing approximants and a limit invariant.",
            family_limit_declared=True,
        ),
        IdealizationPacket(
            packet_id="single_instance_e1_overread",
            description="A single-instance packet incorrectly framed as E1.",
            family_limit_declared=True,
            finite_approximants_declared=True,
            limit_invariant_declared=True,
            recovery_cost_diverges_across_family=True,
            single_instance_claim=True,
        ),
        IdealizationPacket(
            packet_id="e1_family_limit_synthetic_control",
            description="Synthetic E1 control with finite approximants and a declared diverging limit invariant.",
            family_limit_declared=True,
            finite_approximants_declared=True,
            limit_invariant_declared=True,
            recovery_cost_diverges_across_family=True,
            synthetic_e1_control=True,
        ),
        IdealizationPacket(
            packet_id="a2_lift_absorbs_sector_lock",
            description="A T435/T436-style A1 obstruction that becomes declared after A2 resource lift.",
            exact_sector_rule=True,
            finite_operational_substrate=True,
            gauge_invariant_record_distinction=True,
            absorbers_matched=True,
            reservoirs_boundaries_references_accounted=True,
            allowed_controls_declared=True,
            a2_resource_lift_audited=True,
            exact_no_go_after_resource_lift=False,
            task_natural_future_operation_split=True,
        ),
        IdealizationPacket(
            packet_id="e3_exact_no_go_synthetic_control",
            description="Synthetic exact no-go control after A2 resource-lift and absorber audits.",
            exact_sector_rule=True,
            finite_operational_substrate=True,
            gauge_invariant_record_distinction=True,
            physical_record_deletion_reverse_edge=True,
            task_natural_future_operation_split=True,
            absorbers_matched=True,
            reservoirs_boundaries_references_accounted=True,
            allowed_controls_declared=True,
            a2_resource_lift_audited=True,
            exact_no_go_after_resource_lift=True,
            synthetic_e3_control=True,
        ),
    )


def run() -> dict[str, Any]:
    classifications = [classify_packet(packet) for packet in candidate_packets()]
    admitted = [item for item in classifications if item["admitted_for_future_review"]]
    e1 = [item for item in admitted if item["route"] == "e1_family_limit_review"]
    e3 = [item for item in admitted if item["route"] == "e3_exact_no_go_review"]
    e0 = [item for item in classifications if item["route"] == "e0_resource_completion"]
    null = [item for item in classifications if item["route"] == "h7_null_or_nonphysical"]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "t439_routing_obligation": SOURCE_T439,
            "t168_sector_screen": SOURCE_T168,
            "n14_sector_gauge_absorber": SOURCE_N14,
            "t436_resource_lift_classifier": SOURCE_T436,
            "taxonomy_reference": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Route exact ideal-limit and sector-lock packets before they can be "
            "used in H7, E1, or E3 work."
        ),
        "routing_requirements": {
            "e1_family_limit_review": [
                "family, not single-instance, packet",
                "finite approximants declared",
                "limit invariant declared before scoring",
                "recovery cost or nonlocality diverges across the family",
                "no H7 or claim promotion from admission",
            ],
            "e3_exact_no_go_review": [
                "exact sector/symmetry rule on physical states",
                "gauge-invariant record distinction",
                "conserved quantities, reservoirs, boundary modes, references, and controls fixed",
                "A2 resource/reference lift audited",
                "exact no-go remains after the A2 audit",
                "task-natural future-operation split declared",
                "no WAY, quantum, H7, or claim promotion from admission",
            ],
            "h7_null_or_absorbed": [
                "infinite barriers and exact sector axioms without finite substrate are idealizations",
                "gauge representative changes are not physical record deletion",
                "finite barriers, enforcement hardware, and leakage paths are control/kinetic accounting",
                "reservoir or reference completion routes to E0/resource completion",
            ],
        },
        "classifications": classifications,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_packet_ids": [item["packet"]["packet_id"] for item in admitted],
            "e1_review_packet_ids": [item["packet"]["packet_id"] for item in e1],
            "e3_review_packet_ids": [item["packet"]["packet_id"] for item in e3],
            "e0_completion_packet_ids": [item["packet"]["packet_id"] for item in e0],
            "h7_null_packet_ids": [item["packet"]["packet_id"] for item in null],
            "synthetic_controls_only": all(
                item["packet"]["synthetic_e1_control"]
                or item["packet"]["synthetic_e3_control"]
                for item in admitted
            ),
            "h7_promotion": "none; exact idealization and sector lock are routing inputs only",
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T440 separates T439's routed packets. Infinite barriers and "
                "exact sector bans without finite substrate are H7-null "
                "idealizations; gauge relabeling is not deletion; finite "
                "enforcement, leakage, reservoirs, and reference frames are "
                "absorbers or E0 completions. E1 requires a family-level limit "
                "packet, while E3 requires an exact no-go that survives absorber "
                "and A2 resource-lift audit. Only synthetic controls are admitted."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "recommended_next": [
            "Use T440 before treating T439-routed ideal-limit or sector-lock packets as live.",
            "E1 follow-up needs a predeclared family-limit packet, not a single instance.",
            "E3 follow-up needs an independently typed exact no-go after A2 resource-lift audit.",
            "Do not reopen H7 with infinite barriers, exact sector axioms, gauge relabeling, or missing reservoirs.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    req_lines = []
    for route, requirements in result["routing_requirements"].items():
        req_lines.append(f"### {route}")
        req_lines.append("")
        req_lines.extend(f"- {item}" for item in requirements)
        req_lines.append("")

    rows = [
        "| {packet_id} | {label} | {route} | {admitted} |".format(
            packet_id=item["packet"]["packet_id"],
            label=item["label"],
            route=item["route"],
            admitted="yes" if item["admitted_for_future_review"] else "no",
        )
        for item in result["classifications"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T440 - Ideal-Limit Sector-Lock Routing Gate - v0.1 results",
            "",
            "> Recorded-tier routing gate. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No H7 promotion, no E1 theorem, "
            "no E3 theorem, no WAY claim, no public posture.",
            "",
            "- Spec: `tests/T440-ideal-limit-sector-lock-routing-gate.md`",
            "- Model: `models/ideal_limit_sector_lock_routing_gate.py`",
            "- Tests: `tests/test_ideal_limit_sector_lock_routing_gate.py`",
            "- Artifact JSON: `results/T440-ideal-limit-sector-lock-routing-gate-v0.1.json`",
            "- Sources: T439, T168, N14, T436, and the adopted taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Routing Requirements",
            "",
            *req_lines,
            "## Packet Classification",
            "",
            "| packet | label | route | admitted? |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable routing classifier for exact ideal-limit and "
            "sector-lock packets deferred by T439.",
            "",
            "Does not earn: H7 promotion, an E1 limit theorem, an E3 exact no-go "
            "theorem, a WAY theorem, quantum physics claim, claim-ledger movement, "
            "public posture, or cross-repo support.",
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_steps,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T440-ideal-limit-sector-lock-routing-gate-v0.1.json"
        md_path = results_dir / "T440-ideal-limit-sector-lock-routing-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
