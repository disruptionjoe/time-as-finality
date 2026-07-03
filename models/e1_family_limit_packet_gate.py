"""T441 - E1 family-limit packet gate.

T440 routed family-level ideal-limit packets to future E1 review. T441 makes
that route executable as an admission classifier. It admits only a synthetic
full packet as a future review target. Admission is not an E1 theorem, not H7
promotion, not a thermodynamic-arrow derivation, and not public posture.

Run:

    python -m models.e1_family_limit_packet_gate --write-results
    python -m pytest tests/test_e1_family_limit_packet_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T441-e1-family-limit-packet-gate-v0.1"
SOURCE_T440 = "results/T440-ideal-limit-sector-lock-routing-gate-v0.1-results.md"
SOURCE_T439 = "results/T439-finite-time-catalytic-thermo-witness-gate-v0.1-results.md"
SOURCE_H7 = "open-problems/h7-physical-deletion-substrate-handoff.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "E1_FAMILY_LIMIT_PACKET_GATE_BUILT_NO_PROMOTION"

HONEST_CEILING = (
    "Recorded-tier admission gate only. T441 does not promote H7, does not "
    "prove an E1 limit theorem, does not derive a thermodynamic arrow, does "
    "not make a physics claim, and does not authorize public posture."
)


@dataclass(frozen=True)
class E1LimitPacket:
    packet_id: str
    description: str
    family_declared: bool = False
    scale_parameter_declared: bool = False
    finite_approximants_declared: bool = False
    approximant_map_declared: bool = False
    same_task_across_family: bool = True
    same_operation_class_across_family: bool = True
    observer_boundary_fixed: bool = True
    resource_accounting_fixed: bool = True
    limit_invariant_predeclared: bool = False
    invariant_observable_on_approximants: bool = False
    convergence_or_error_controls_declared: bool = False
    negative_control_declared: bool = False
    recovery_cost_sequence_declared: bool = False
    recovery_cost_diverges_across_family: bool = False
    nonlocality_diverges_across_family: bool = False
    single_instance_claim: bool = False
    infinite_barrier_only: bool = False
    finite_barrier_or_kinetic_suppression: bool = False
    finite_positive_gap_only: bool = False
    post_hoc_limit_selector: bool = False
    family_drift_or_reencoding: bool = False
    hidden_resource_or_boundary_change: bool = False
    thermodynamic_cost_only: bool = False
    e2_hardness_basis: bool = False
    e3_exact_no_go_basis: bool = False
    synthetic_positive_control: bool = False


def _packet_to_dict(packet: E1LimitPacket) -> dict[str, Any]:
    return asdict(packet)


def _has_diverging_family_quantity(packet: E1LimitPacket) -> bool:
    return (
        packet.recovery_cost_sequence_declared
        and (
            packet.recovery_cost_diverges_across_family
            or packet.nonlocality_diverges_across_family
        )
    )


def classify_packet(packet: E1LimitPacket) -> dict[str, Any]:
    admitted = False
    route = "rejected"
    label = "REJECTED_UNCLASSIFIED"
    reason = "No E1 family-limit admission rule matched."

    if packet.post_hoc_limit_selector:
        label = "REJECTED_POST_HOC_LIMIT_SELECTOR"
        reason = "The limit invariant or family selector is chosen after seeing the target pair."
    elif packet.e2_hardness_basis:
        route = "route_to_e2_gate"
        label = "ROUTE_TO_E2_HARDNESS_GATE"
        reason = "A feasible-recovery hardness packet belongs to the E2 gate, not E1."
    elif packet.e3_exact_no_go_basis:
        route = "route_to_e3_gate"
        label = "ROUTE_TO_E3_EXACT_NO_GO_GATE"
        reason = "An exact symmetry or conservation-law no-go belongs to E3 review, not E1."
    elif packet.single_instance_claim or packet.infinite_barrier_only:
        route = "h7_null_or_idealization"
        label = "H7_NULL_SINGLE_INSTANCE_IDEALIZATION"
        reason = "A single ideal lock or infinite barrier is not a family-level E1 packet."
    elif packet.finite_barrier_or_kinetic_suppression:
        route = "absorbed"
        label = "ABSORBED_BY_FINITE_KINETICS"
        reason = "High but finite barriers or slow rates are finite kinetic accounting."
    elif packet.finite_positive_gap_only:
        route = "absorbed"
        label = "ABSORBED_BY_FINITE_GAP_NO_LIMIT_FORCING"
        reason = "A finite positive gap is not asymptotic forcing without a limit invariant."
    elif packet.thermodynamic_cost_only:
        route = "absorbed"
        label = "ABSORBED_BY_ORDINARY_THERMODYNAMIC_COST"
        reason = "Ordinary cost accounting is not E1 unless a declared family quantity diverges."
    elif packet.hidden_resource_or_boundary_change:
        label = "REJECTED_CHANGED_RESOURCE_OR_BOUNDARY"
        reason = "Resource accounting or observer boundary changes across the family."
    elif packet.family_drift_or_reencoding:
        label = "REJECTED_FAMILY_DRIFT_OR_REENCODING"
        reason = "The family changes encoding, target, or substrate faster than the claimed limit can be audited."
    elif not packet.family_declared or not packet.scale_parameter_declared:
        label = "REJECTED_NO_DECLARED_FAMILY_PARAMETER"
        reason = "E1 review needs a named family and scale/security/size parameter."
    elif not packet.finite_approximants_declared or not packet.approximant_map_declared:
        label = "REJECTED_NO_FINITE_APPROXIMANT_MAP"
        reason = "The packet lacks finite approximants or a map relating them to the limit object."
    elif not (
        packet.same_task_across_family
        and packet.same_operation_class_across_family
        and packet.observer_boundary_fixed
        and packet.resource_accounting_fixed
    ):
        label = "REJECTED_UNSTABLE_TASK_OPERATION_OR_ACCOUNTING"
        reason = "Task, operation class, observer boundary, or resource accounting is not fixed across the family."
    elif not packet.limit_invariant_predeclared:
        label = "REJECTED_NO_PREDECLARED_LIMIT_INVARIANT"
        reason = "The limit invariant is not declared before scoring the family."
    elif not packet.invariant_observable_on_approximants:
        label = "REJECTED_INVARIANT_NOT_ANCHORED_TO_APPROXIMANTS"
        reason = "The invariant is not auditable on the finite approximants."
    elif not (
        packet.convergence_or_error_controls_declared
        and packet.negative_control_declared
    ):
        label = "REJECTED_NO_CONVERGENCE_OR_NEGATIVE_CONTROLS"
        reason = "The packet lacks convergence/error controls or a negative control."
    elif not _has_diverging_family_quantity(packet):
        label = "REJECTED_NO_DIVERGING_COST_OR_NONLOCALITY"
        reason = "No recovery cost or nonlocality quantity is declared to diverge across the family."
    else:
        admitted = True
        route = "admitted_as_future_e1_review"
        label = "ADMITTED_E1_FAMILY_LIMIT_REVIEW_NO_PROMOTION"
        reason = (
            "The packet freezes a family-level E1 review shape with finite "
            "approximants, fixed accounting, a predeclared invariant, controls, "
            "and a diverging recovery cost or nonlocality claim. It is admitted "
            "only for future review."
        )

    return {
        "packet": _packet_to_dict(packet),
        "admitted_for_future_e1_review": admitted,
        "route": route,
        "label": label,
        "reason": reason,
    }


def candidate_packets() -> tuple[E1LimitPacket, ...]:
    return (
        E1LimitPacket(
            packet_id="single_instance_infinite_barrier",
            description="A single record protected only by an infinite barrier idealization.",
            single_instance_claim=True,
            infinite_barrier_only=True,
        ),
        E1LimitPacket(
            packet_id="finite_barrier_metastable_family",
            description="A high but finite metastability barrier treated as a limit gap.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_barrier_or_kinetic_suppression=True,
        ),
        E1LimitPacket(
            packet_id="finite_positive_gap_only",
            description="A finite cost gap with no limiting invariant or divergence claim.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_positive_gap_only=True,
        ),
        E1LimitPacket(
            packet_id="post_hoc_limit_selector",
            description="A family or invariant selected after the witness pair is known.",
            post_hoc_limit_selector=True,
        ),
        E1LimitPacket(
            packet_id="hidden_reservoir_boundary_drift",
            description="A family whose reservoir or observer boundary changes with the parameter.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_approximants_declared=True,
            approximant_map_declared=True,
            hidden_resource_or_boundary_change=True,
        ),
        E1LimitPacket(
            packet_id="missing_finite_approximants",
            description="A named limiting object with no finite approximant sequence.",
            family_declared=True,
            scale_parameter_declared=True,
            limit_invariant_predeclared=True,
        ),
        E1LimitPacket(
            packet_id="family_reencoding_drift",
            description="The family changes target encoding while claiming one asymptotic invariant.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_approximants_declared=True,
            approximant_map_declared=True,
            family_drift_or_reencoding=True,
        ),
        E1LimitPacket(
            packet_id="changed_task_operation_class",
            description="The task and operation menu are tightened as n grows.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_approximants_declared=True,
            approximant_map_declared=True,
            same_task_across_family=False,
            same_operation_class_across_family=False,
        ),
        E1LimitPacket(
            packet_id="no_predeclared_limit_invariant",
            description="A finite approximant family with no predeclared invariant.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_approximants_declared=True,
            approximant_map_declared=True,
        ),
        E1LimitPacket(
            packet_id="invariant_not_observable_on_approximants",
            description="A limit invariant named only at infinity, with no finite audit handle.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_approximants_declared=True,
            approximant_map_declared=True,
            limit_invariant_predeclared=True,
        ),
        E1LimitPacket(
            packet_id="missing_convergence_controls",
            description="A family with an invariant and divergence claim but no error controls.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_approximants_declared=True,
            approximant_map_declared=True,
            limit_invariant_predeclared=True,
            invariant_observable_on_approximants=True,
            recovery_cost_sequence_declared=True,
            recovery_cost_diverges_across_family=True,
        ),
        E1LimitPacket(
            packet_id="bounded_cost_sequence",
            description="A fully controlled family whose recovery cost remains bounded.",
            family_declared=True,
            scale_parameter_declared=True,
            finite_approximants_declared=True,
            approximant_map_declared=True,
            limit_invariant_predeclared=True,
            invariant_observable_on_approximants=True,
            convergence_or_error_controls_declared=True,
            negative_control_declared=True,
            recovery_cost_sequence_declared=True,
        ),
        E1LimitPacket(
            packet_id="e2_period_hardness_packet",
            description="A feasible-recovery hardness family with a cryptographic assumption.",
            family_declared=True,
            scale_parameter_declared=True,
            e2_hardness_basis=True,
        ),
        E1LimitPacket(
            packet_id="e3_exact_sector_no_go_packet",
            description="An exact sector/symmetry no-go packet after resource audit.",
            family_declared=True,
            scale_parameter_declared=True,
            e3_exact_no_go_basis=True,
        ),
        E1LimitPacket(
            packet_id="e1_family_limit_synthetic_control",
            description=(
                "Synthetic future target: fixed family, finite approximants, "
                "predeclared invariant, controls, and diverging recovery cost."
            ),
            family_declared=True,
            scale_parameter_declared=True,
            finite_approximants_declared=True,
            approximant_map_declared=True,
            same_task_across_family=True,
            same_operation_class_across_family=True,
            observer_boundary_fixed=True,
            resource_accounting_fixed=True,
            limit_invariant_predeclared=True,
            invariant_observable_on_approximants=True,
            convergence_or_error_controls_declared=True,
            negative_control_declared=True,
            recovery_cost_sequence_declared=True,
            recovery_cost_diverges_across_family=True,
            synthetic_positive_control=True,
        ),
    )


def run() -> dict[str, Any]:
    classifications = [classify_packet(packet) for packet in candidate_packets()]
    admitted = [
        item for item in classifications if item["admitted_for_future_e1_review"]
    ]
    routed = [item for item in classifications if item["route"].startswith("route_to_")]
    absorbed = [item for item in classifications if item["route"] == "absorbed"]
    null = [item for item in classifications if item["route"] == "h7_null_or_idealization"]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "t440_e1_route": SOURCE_T440,
            "t439_thermo_gate": SOURCE_T439,
            "h7_handoff": SOURCE_H7,
            "taxonomy_reference": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Convert T440's E1 family-limit route into an executable admission "
            "gate for future asymptotic/ideal-limit packets."
        ),
        "admission_requirements": [
            "family and scale/security/size parameter declared",
            "finite approximants and approximant-to-limit map declared",
            "task, operation class, observer boundary, and resource accounting fixed across the family",
            "limit invariant declared before scoring",
            "limit invariant auditable on finite approximants",
            "finite convergence/error controls and a negative control declared",
            "recovery cost or nonlocality quantity declared and divergent across the family",
            "no single-instance idealization, post-hoc selector, family drift, hidden resource change, or E2/E3 misroute",
        ],
        "classifications": classifications,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_packet_ids": [item["packet"]["packet_id"] for item in admitted],
            "routed_packet_ids": [item["packet"]["packet_id"] for item in routed],
            "absorbed_packet_ids": [item["packet"]["packet_id"] for item in absorbed],
            "h7_null_packet_ids": [item["packet"]["packet_id"] for item in null],
            "synthetic_positive_controls_only": all(
                item["packet"]["synthetic_positive_control"] for item in admitted
            ),
            "e1_theorem": "none; admission is not proof of a limit theorem",
            "h7_promotion": "none; H7 remains conditional/resource-accounting only",
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T441 admits only a predeclared, family-level E1 packet with "
                "finite approximants, stable task and operation class, fixed "
                "observer/resource accounting, a finite-auditable limit invariant, "
                "convergence/error controls, and a diverging recovery cost or "
                "nonlocality claim. Single-instance idealizations, finite barriers, "
                "finite gaps, post-hoc selectors, drifting families, hidden "
                "resources, and E2/E3 packets do not pass as E1."
            ),
        },
        "recommended_next": [
            "Use T441 before treating T440-admitted E1 packets as live review targets.",
            "A future E1 follow-up should supply the full family packet rather than another ideal barrier.",
            "Do not reopen H7 with an E1 packet until T441, T439, and T440 are all satisfied.",
            "Route hardness assumptions to T438 and exact no-go claims to the T435/T436/T440 E3 gates.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["admission_requirements"]]
    rows = [
        "| {packet_id} | {label} | {route} | {admitted} |".format(
            packet_id=item["packet"]["packet_id"],
            label=item["label"],
            route=item["route"],
            admitted="yes" if item["admitted_for_future_e1_review"] else "no",
        )
        for item in result["classifications"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T441 - E1 Family-Limit Packet Gate - v0.1 results",
            "",
            "> Recorded-tier admission gate. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No H7 promotion, no E1 theorem, "
            "no thermodynamic-arrow derivation, no public posture.",
            "",
            "- Spec: `tests/T441-e1-family-limit-packet-gate.md`",
            "- Model: `models/e1_family_limit_packet_gate.py`",
            "- Tests: `tests/test_e1_family_limit_packet_gate.py`",
            "- Artifact JSON: `results/T441-e1-family-limit-packet-gate-v0.1.json`",
            "- Sources: T440, T439, H7 substrate handoff, and the adopted taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Admission Requirements",
            "",
            *requirements,
            "",
            "## Packet Classification",
            "",
            "| packet | label | route | admitted? |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable admission classifier for future E1 family-limit "
            "packets after T440.",
            "",
            "Does not earn: H7 promotion, an E1 limit theorem, a "
            "thermodynamic-arrow theorem, stochastic-thermodynamic theorem, "
            "claim-ledger movement, public posture, or cross-repo support.",
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
        json_path = results_dir / "T441-e1-family-limit-packet-gate-v0.1.json"
        md_path = results_dir / "T441-e1-family-limit-packet-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
