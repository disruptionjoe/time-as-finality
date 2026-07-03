"""T439 - finite-time catalytic thermodynamic witness gate.

T142 separated reversible uncopy from blind Landauer-style reset. N8 then
records the stochastic-thermodynamic absorbers that any future H7 physical-arrow
proposal must grant before claiming thermodynamic residue.

T439 is an admission gate for finite-time or catalytic thermodynamic-resource
packets. It admits only a full-accounting future target. Admission is not H7
promotion, not a thermodynamic-arrow derivation, and not public posture.

Run:

    python -m models.finite_time_catalytic_thermo_witness_gate --write-results
    python -m pytest tests/test_finite_time_catalytic_thermo_witness_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models.thermodynamic_erasure_calibration import (
    landauer_bound_bits,
    run_t142_analysis,
)


ARTIFACT = "T439-finite-time-catalytic-thermo-witness-gate-v0.1"
SOURCE_H7 = "open-problems/h7-physical-deletion-substrate-handoff.md"
SOURCE_N8 = "literature/N8-h7-stochastic-thermodynamic-absorbers.md"
SOURCE_T142 = "results/thermodynamic-erasure-calibration-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

MIN_TRAJECTORY_REPLICATES = 8
VERDICT = "FINITE_TIME_CATALYTIC_THERMO_GATE_BUILT_NO_H7_PROMOTION"

HONEST_CEILING = (
    "Recorded-tier admission gate only. T439 does not promote H7, does not "
    "derive a thermodynamic arrow, does not prove a stochastic-thermodynamic or "
    "catalytic resource theorem, and does not authorize public posture."
)


@dataclass(frozen=True)
class ThermoPacket:
    packet_id: str
    description: str
    named_record_substrate: bool = False
    finite_time_protocol_declared: bool = False
    physical_record_deletion_reverse_edge: bool = False
    stochastic_thermo_ledgers_fixed: bool = False
    information_ledgers_fixed: bool = False
    source_copy_access_accounted: bool = False
    reversible_control_access_accounted: bool = False
    catalyst_policy_declared: bool = False
    catalyst_returned_exactly: bool = False
    catalyst_state_changed: bool = False
    catalyst_hidden_or_untracked: bool = False
    task_natural_future_operation_split: bool = False
    split_persists_after_matched_ledgers: bool = False
    constructor_impossible_after_full_accounting: bool = False
    evidence_replicates: int = 0
    negative_control_declared: bool = False
    reversible_uncopy_available: bool = False
    landauer_erasure_only: bool = False
    finite_barrier_or_kinetic_suppression: bool = False
    nonequilibrium_current_only: bool = False
    feedback_controller_memory_omitted: bool = False
    hidden_sink_or_export_history: bool = False
    untyped_resource_unit: bool = False
    ideal_limit_or_exact_sector_lock: bool = False
    synthetic_positive_control: bool = False


def _packet_to_dict(packet: ThermoPacket) -> dict[str, Any]:
    return asdict(packet)


def classify_packet(packet: ThermoPacket) -> dict[str, Any]:
    admitted = False
    route = "rejected"
    label = "REJECTED_UNCLASSIFIED"
    reason = "No thermodynamic admission rule matched."

    if packet.reversible_uncopy_available:
        label = "ABSORBED_BY_REVERSIBLE_UNCOPY"
        reason = "Full source-copy correlation and reversible control absorb deletion."
    elif packet.landauer_erasure_only:
        label = "ABSORBED_BY_LANDAUER_BENNETT_ERASURE"
        reason = "Blind reset is ordinary erasure/free-energy accounting."
    elif packet.finite_barrier_or_kinetic_suppression:
        label = "ABSORBED_BY_KINETICS_NOT_CONSTRUCTOR_IMPOSSIBILITY"
        reason = "A finite barrier or slow rate is not constructor impossibility."
    elif packet.nonequilibrium_current_only:
        label = "ABSORBED_BY_STOCHASTIC_THERMO_CURRENT"
        reason = "A steady current or entropy-production ledger is standard stochastic thermodynamics."
    elif packet.feedback_controller_memory_omitted:
        label = "BLOCKED_OMITTED_FEEDBACK_MEMORY_LEDGER"
        reason = "Feedback or measurement packets must account for controller memory and information flow."
    elif packet.hidden_sink_or_export_history:
        label = "BLOCKED_HIDDEN_SINK_OR_EXPORT_HISTORY"
        reason = "Sink, export history, or reservoir boundary changes must be in the accounting vector."
    elif packet.untyped_resource_unit:
        label = "REJECTED_UNTYPED_RESOURCE_UNIT"
        reason = "Resource drawdown is formal until mapped to named thermodynamic or capacity units."
    elif packet.ideal_limit_or_exact_sector_lock:
        route = "separate_spec_required"
        label = "ROUTE_TO_IDEAL_LIMIT_OR_E3_SPEC"
        reason = "Exact ideal-limit or sector-lock packets require a separate E1/E3/idealization spec."
    elif packet.catalyst_hidden_or_untracked or not packet.catalyst_policy_declared:
        label = "BLOCKED_UNDECLARED_CATALYST_POLICY"
        reason = "Catalyst availability, return state, and accounting boundary are not declared."
    elif packet.catalyst_state_changed or not packet.catalyst_returned_exactly:
        label = "ABSORBED_BY_CHANGED_CATALYST_RESOURCE_BOUNDARY"
        reason = "A consumed or changed catalyst is a changed resource boundary, not matched accounting."
    elif not packet.named_record_substrate or not packet.finite_time_protocol_declared:
        label = "REJECTED_NO_NAMED_FINITE_PROTOCOL_SUBSTRATE"
        reason = "The packet does not name a finite record substrate and finite-time protocol."
    elif not packet.physical_record_deletion_reverse_edge:
        label = "REJECTED_NOT_PHYSICAL_RECORD_DELETION"
        reason = "The reverse edge is not typed as physical_record_deletion."
    elif not packet.stochastic_thermo_ledgers_fixed:
        label = "REJECTED_STOCHASTIC_THERMO_LEDGER_INCOMPLETE"
        reason = "Work, heat, entropy production, free energy, reservoir, and protocol ledgers are incomplete."
    elif not (
        packet.information_ledgers_fixed
        and packet.source_copy_access_accounted
        and packet.reversible_control_access_accounted
    ):
        label = "REJECTED_INFORMATION_CONTROL_LEDGER_INCOMPLETE"
        reason = "Source-copy, controller-memory, feedback, or reversible-control access is underaccounted."
    elif (
        packet.evidence_replicates < MIN_TRAJECTORY_REPLICATES
        or not packet.negative_control_declared
    ):
        label = "REJECTED_UNDERPOWERED_FINITE_TIME_PROTOCOL"
        reason = "Finite-time dynamics needs enough trajectory evidence and a negative control."
    elif not packet.task_natural_future_operation_split:
        label = "REJECTED_NO_TASK_NATURAL_CAPABILITY_SPLIT"
        reason = "No task-natural future-operation split is declared."
    elif not packet.split_persists_after_matched_ledgers:
        label = "REJECTED_SPLIT_ABSORBED_AFTER_LEDGER_MATCH"
        reason = "The capability split vanishes after thermodynamic and information ledgers are matched."
    elif not packet.constructor_impossible_after_full_accounting:
        label = "REJECTED_HIGH_COST_NOT_IMPOSSIBILITY"
        reason = "The packet shows high cost or low probability, not constructor impossibility after full accounting."
    else:
        admitted = True
        route = "admitted_as_future_target"
        label = "ADMITTED_THERMO_RESOURCE_WITNESS_TARGET_NO_H7_PROMOTION"
        reason = (
            "The packet freezes finite-time substrate, thermodynamic ledgers, "
            "information ledgers, catalyst return, controls, and a persistent "
            "future-operation split. It is admitted only as a future review target."
        )

    return {
        "packet": _packet_to_dict(packet),
        "admitted_for_future_h7_work": admitted,
        "route": route,
        "label": label,
        "reason": reason,
    }


def candidate_packets() -> tuple[ThermoPacket, ...]:
    return (
        ThermoPacket(
            packet_id="t142_correlated_uncopy_copy",
            description="T142 copy reversal with full source-copy correlation and reversible control.",
            reversible_uncopy_available=True,
            source_copy_access_accounted=True,
            reversible_control_access_accounted=True,
        ),
        ThermoPacket(
            packet_id="t142_blind_reset_only",
            description="T142 blind reset: one-bit erasure/free-energy bookkeeping.",
            landauer_erasure_only=True,
            physical_record_deletion_reverse_edge=True,
        ),
        ThermoPacket(
            packet_id="finite_barrier_metastable_memory",
            description="A metastable record with a high but finite deletion barrier.",
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            finite_barrier_or_kinetic_suppression=True,
        ),
        ThermoPacket(
            packet_id="nonequilibrium_current_only",
            description="A nonequilibrium steady current with no separate finality capability split.",
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            nonequilibrium_current_only=True,
        ),
        ThermoPacket(
            packet_id="feedback_demon_missing_memory",
            description="A feedback-control packet that omits controller memory and erasure ledgers.",
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            feedback_controller_memory_omitted=True,
        ),
        ThermoPacket(
            packet_id="hidden_sink_export_history",
            description="A deletion packet that exports history or changes a sink without accounting for it.",
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            hidden_sink_or_export_history=True,
        ),
        ThermoPacket(
            packet_id="untyped_resource_drawdown",
            description="A finite drawdown coordinate with no named free-energy, fuel, or capacity unit.",
            untyped_resource_unit=True,
        ),
        ThermoPacket(
            packet_id="ideal_infinite_barrier_or_sector_lock",
            description="An exact ideal lock or sector rule without a finite operational substrate reading.",
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            ideal_limit_or_exact_sector_lock=True,
        ),
        ThermoPacket(
            packet_id="hidden_catalyst_packet",
            description="A catalytic-looking packet whose catalyst boundary is not declared.",
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            catalyst_hidden_or_untracked=True,
        ),
        ThermoPacket(
            packet_id="consumed_catalyst_packet",
            description="A catalytic packet where the catalyst state changes across the pair.",
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            catalyst_policy_declared=True,
            catalyst_state_changed=True,
        ),
        ThermoPacket(
            packet_id="ledger_matched_split_vanishes",
            description="A full-ledger packet whose claimed capability split disappears after matching.",
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            physical_record_deletion_reverse_edge=True,
            stochastic_thermo_ledgers_fixed=True,
            information_ledgers_fixed=True,
            source_copy_access_accounted=True,
            reversible_control_access_accounted=True,
            catalyst_policy_declared=True,
            catalyst_returned_exactly=True,
            evidence_replicates=MIN_TRAJECTORY_REPLICATES,
            negative_control_declared=True,
            task_natural_future_operation_split=True,
            split_persists_after_matched_ledgers=False,
        ),
        ThermoPacket(
            packet_id="full_accounting_synthetic_positive_control",
            description=(
                "Synthetic future-target packet: full finite-time, catalytic, "
                "thermodynamic, information, and task accounting is frozen."
            ),
            named_record_substrate=True,
            finite_time_protocol_declared=True,
            physical_record_deletion_reverse_edge=True,
            stochastic_thermo_ledgers_fixed=True,
            information_ledgers_fixed=True,
            source_copy_access_accounted=True,
            reversible_control_access_accounted=True,
            catalyst_policy_declared=True,
            catalyst_returned_exactly=True,
            task_natural_future_operation_split=True,
            split_persists_after_matched_ledgers=True,
            constructor_impossible_after_full_accounting=True,
            evidence_replicates=12,
            negative_control_declared=True,
            synthetic_positive_control=True,
        ),
    )


def run() -> dict[str, Any]:
    t142 = run_t142_analysis()
    classifications = [classify_packet(packet) for packet in candidate_packets()]
    admitted = [
        item for item in classifications if item["admitted_for_future_h7_work"]
    ]
    routed = [item for item in classifications if item["route"] == "separate_spec_required"]
    rejected = [item for item in classifications if item["route"] == "rejected"]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "h7_handoff": SOURCE_H7,
            "n8_absorber_map": SOURCE_N8,
            "t142": SOURCE_T142,
            "taxonomy_reference": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Turn the thermodynamic-resource next action into an admission gate "
            "for finite-time or catalytic record-finality packets."
        ),
        "t142_imported_guardrail": {
            "one_bit_blind_reset_beta_work_floor": landauer_bound_bits(1),
            "copy_reverses_have_zero_heat_uncopy_mode": (
                t142.copy_reverses_have_zero_heat_uncopy_mode
            ),
            "copy_reverses_have_landauer_reset_mode": (
                t142.copy_reverses_have_landauer_reset_mode
            ),
            "h7_upgrade_status": t142.h7_upgrade_status,
        },
        "admission_requirements": [
            "named finite record substrate and finite-time protocol",
            "reverse edge typed as physical_record_deletion",
            "work, heat, entropy-production, free-energy, reservoir, and protocol ledgers fixed",
            "source-copy, controller-memory, feedback, and reversible-control access fixed",
            "catalyst policy declared and catalyst returned exactly",
            "enough repeated trajectory evidence and a negative control",
            "task-natural future-operation split persists after all ledgers are matched",
            "constructor impossibility remains after full accounting",
        ],
        "minimum_trajectory_replicates": MIN_TRAJECTORY_REPLICATES,
        "classifications": classifications,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_packet_ids": [item["packet"]["packet_id"] for item in admitted],
            "routed_packet_ids": [item["packet"]["packet_id"] for item in routed],
            "rejected_packet_ids": [item["packet"]["packet_id"] for item in rejected],
            "synthetic_positive_controls_only": all(
                item["packet"]["synthetic_positive_control"] for item in admitted
            ),
            "h7_promotion": "none; H7 remains conditional/resource-accounting only",
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T439 rejects ordinary thermodynamic absorbers and accounting gaps: "
                "reversible uncopy, blind erasure, finite barriers, stochastic "
                "currents, omitted feedback memory, hidden sinks, untyped resources, "
                "and changed catalysts. It routes exact ideal-limit or sector-lock "
                "packets to a separate spec. Only a full-accounting synthetic packet "
                "is admitted as a future review target, not as evidence."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "recommended_next": [
            "Do not reopen H7 with Landauer cost, finite barriers, or currents alone.",
            "A future thermodynamic packet must freeze the full ledger and catalyst boundary before scoring finality.",
            "Ideal-limit or exact sector-lock proposals need a separate E1/E3/idealization spec.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["admission_requirements"]]
    rows = [
        "| {packet_id} | {label} | {route} | {admitted} |".format(
            packet_id=item["packet"]["packet_id"],
            label=item["label"],
            route=item["route"],
            admitted="yes" if item["admitted_for_future_h7_work"] else "no",
        )
        for item in result["classifications"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T439 - Finite-Time Catalytic Thermodynamic Witness Gate - v0.1 results",
            "",
            "> Recorded-tier admission gate. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No H7 promotion, no "
            "thermodynamic-arrow derivation, no public posture.",
            "",
            "- Spec (frozen first): `tests/T439-finite-time-catalytic-thermo-witness-gate.md`",
            "- Model: `models/finite_time_catalytic_thermo_witness_gate.py`",
            "- Tests: `tests/test_finite_time_catalytic_thermo_witness_gate.py`",
            "- Artifact JSON: `results/T439-finite-time-catalytic-thermo-witness-gate-v0.1.json`",
            "- Sources: T142, N8 absorber map, H7 substrate handoff, and the adopted taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Imported T142 Guardrail",
            "",
            "- One-bit blind reset beta*W floor: `{}`".format(
                result["t142_imported_guardrail"]["one_bit_blind_reset_beta_work_floor"]
            ),
            "- Correlated uncopy zero-heat mode present: `{}`".format(
                result["t142_imported_guardrail"]["copy_reverses_have_zero_heat_uncopy_mode"]
            ),
            "- Blind reset mode present: `{}`".format(
                result["t142_imported_guardrail"]["copy_reverses_have_landauer_reset_mode"]
            ),
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
            "Earns: a reusable admission classifier for future finite-time or "
            "catalytic thermodynamic-resource packets after T142 and N8.",
            "",
            "Does not earn: H7 promotion, a physical-arrow theorem, a "
            "stochastic-thermodynamic theorem, a catalytic resource theorem, "
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
        json_path = results_dir / "T439-finite-time-catalytic-thermo-witness-gate-v0.1.json"
        md_path = results_dir / "T439-finite-time-catalytic-thermo-witness-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
