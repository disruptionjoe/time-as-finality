"""T462 - H7 physical-deletion overread absorber.

T461 produced a positive E1 locality control: local recovery depth can diverge
across a family. T462 prevents that fact from being overread as H7
physical-record-deletion evidence. It classifies candidate deletion packets
against the existing H7 absorber stack and admits only a synthetic full-burden
review target.

Run:

    python -m models.h7_physical_deletion_overread_absorber --write-results
    python -m pytest tests/test_h7_physical_deletion_overread_absorber.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T462-h7-physical-deletion-overread-absorber-v0.1"
SOURCE_H7 = "open-problems/h7-physical-deletion-substrate-handoff.md"
SOURCE_T145 = "tests/T145-physical-record-deletion-fixed-accounting.md"
SOURCE_T160 = "tests/T160-h7-substrate-family-screen.md"
SOURCE_T168 = "tests/T168-h7-sector-restriction-screen.md"
SOURCE_T439 = "results/T439-finite-time-catalytic-thermo-witness-gate-v0.1-results.md"
SOURCE_T440 = "results/T440-ideal-limit-sector-lock-routing-gate-v0.1-results.md"
SOURCE_T441 = "results/T441-e1-family-limit-packet-gate-v0.1-results.md"
SOURCE_T461 = "results/T461-e1-local-recovery-family-audition-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "H7_PHYSICAL_DELETION_OVERREAD_ABSORBER_BUILT_NO_H7_REOPENING"

HONEST_CEILING = (
    "Recorded-tier absorber audit only. T462 does not promote H7, does not "
    "supply physical-deletion substrate evidence, does not prove a "
    "thermodynamic-arrow theorem, does not prove an E1/E3 theorem, does not "
    "move claim status, and does not authorize public posture."
)

PHYSICAL_RECORD_DELETION = "physical_record_deletion"


@dataclass(frozen=True)
class DeletionPacket:
    packet_id: str
    description: str
    reverse_edge_class: str
    named_physical_substrate: bool = False
    record_encoding_frozen: bool = False
    write_delete_reverse_task_frozen: bool = False
    task_natural_future_operation_split: bool = False
    fixed_absorber_vector_declared: bool = False
    free_energy_floor_matched: bool = False
    blank_capacity_matched: bool = False
    sink_export_history_matched: bool = False
    observer_boundary_matched: bool = False
    provenance_authority_matched: bool = False
    source_copy_status_matched: bool = False
    reversible_control_access_matched: bool = False
    substrate_specific_absorber_data_declared: bool = False
    allowed_control_class_declared: bool = False
    finite_operational_substrate: bool = False
    constructor_impossible_after_full_accounting: bool = False
    future_operation_split_survives_matching: bool = False
    negative_controls_declared: bool = False
    e1_locality_depth_only: bool = False
    access_loss_only: bool = False
    provenance_loss_only: bool = False
    support_copy_removal_only: bool = False
    finite_barrier_or_kinetic_suppression: bool = False
    hidden_sink_or_export: bool = False
    ideal_limit_or_exact_sector_lock: bool = False
    gauge_relabeling: bool = False
    hidden_source_copy_or_reversible_control: bool = False
    thermodynamic_ledger_changes: bool = False
    synthetic_positive_control: bool = False


def _packet_to_dict(packet: DeletionPacket) -> dict[str, Any]:
    return asdict(packet)


def absorber_vector_matched(packet: DeletionPacket) -> bool:
    return (
        packet.fixed_absorber_vector_declared
        and packet.free_energy_floor_matched
        and packet.blank_capacity_matched
        and packet.sink_export_history_matched
        and packet.observer_boundary_matched
        and packet.provenance_authority_matched
        and packet.source_copy_status_matched
        and packet.reversible_control_access_matched
    )


def minimum_h7_commitment_met(packet: DeletionPacket) -> bool:
    return (
        packet.reverse_edge_class == PHYSICAL_RECORD_DELETION
        and packet.named_physical_substrate
        and packet.record_encoding_frozen
        and packet.write_delete_reverse_task_frozen
        and packet.task_natural_future_operation_split
        and absorber_vector_matched(packet)
        and packet.substrate_specific_absorber_data_declared
        and packet.allowed_control_class_declared
        and packet.finite_operational_substrate
    )


def classify_packet(packet: DeletionPacket) -> dict[str, Any]:
    admitted = False
    route = "rejected"
    label = "REJECTED_UNCLASSIFIED"
    reason = "No H7 physical-deletion absorber rule matched."

    if packet.e1_locality_depth_only:
        route = "absorbed_by_e1_locality_control"
        label = "ABSORBED_BY_T461_LOCALITY_DEPTH_NOT_DELETION"
        reason = (
            "Diverging local recovery depth is locality accounting. It is not "
            "a physical-record-deletion reverse edge."
        )
    elif packet.access_loss_only or packet.reverse_edge_class == "access_loss":
        route = "non_deletion_reverse_edge"
        label = "NON_DELETION_ACCESS_LOSS"
        reason = "Observer reachability changed; the record was not physically deleted."
    elif packet.provenance_loss_only or packet.reverse_edge_class == "provenance_loss":
        route = "non_deletion_reverse_edge"
        label = "NON_DELETION_PROVENANCE_LOSS"
        reason = "Authority or provenance changed; that is not physical record deletion."
    elif (
        packet.support_copy_removal_only
        or packet.reverse_edge_class == "support_copy_removal"
    ):
        route = "non_deletion_reverse_edge"
        label = "NON_DELETION_SUPPORT_COPY_REMOVAL"
        reason = "A support copy was removed without showing substrate-native deletion."
    elif packet.gauge_relabeling:
        route = "non_deletion_gauge_or_representation"
        label = "NON_DELETION_GAUGE_RELABELING"
        reason = "Gauge or representative relabeling is not a physical deletion distinction."
    elif packet.finite_barrier_or_kinetic_suppression:
        route = "absorbed_by_finite_kinetics"
        label = "ABSORBED_BY_T439_FINITE_KINETICS"
        reason = "Finite barriers or slow rates are kinetic accounting, not constructor impossibility."
    elif packet.hidden_sink_or_export:
        route = "absorbed_by_hidden_sink_export"
        label = "ABSORBED_BY_T145_HIDDEN_SINK_EXPORT"
        reason = "Sink, reservoir, or exported-history data changed across the comparison."
    elif packet.thermodynamic_ledger_changes:
        route = "absorbed_by_changed_thermodynamic_ledger"
        label = "ABSORBED_BY_CHANGED_LEDGER_ACCOUNTING"
        reason = "Free-energy, blank-capacity, work, or information ledgers are not matched."
    elif packet.hidden_source_copy_or_reversible_control:
        route = "absorbed_by_source_copy_or_reversible_control"
        label = "ABSORBED_BY_SOURCE_COPY_OR_REVERSIBLE_CONTROL"
        reason = "Hidden source copies or reversible controls restore the apparent deletion."
    elif packet.ideal_limit_or_exact_sector_lock:
        route = "route_to_t440_t168_ideal_or_sector_absorber"
        label = "ROUTE_TO_T440_T168_IDEAL_OR_SECTOR_ABSORBER"
        reason = (
            "Exact ideal locks and sector restrictions need finite substrate, "
            "reservoir, gauge-invariance, reference, and allowed-control audits."
        )
    elif packet.reverse_edge_class != PHYSICAL_RECORD_DELETION:
        route = "non_deletion_reverse_edge"
        label = "REJECTED_NOT_PHYSICAL_RECORD_DELETION"
        reason = "The reverse edge is not typed as physical_record_deletion."
    elif not packet.named_physical_substrate:
        label = "REJECTED_NO_NAMED_PHYSICAL_SUBSTRATE"
        reason = "H7 review needs a named substrate, not a generic deletion story."
    elif not packet.record_encoding_frozen:
        label = "REJECTED_RECORD_ENCODING_NOT_FROZEN"
        reason = "The record token and encoding are not frozen before comparison."
    elif not packet.write_delete_reverse_task_frozen:
        label = "REJECTED_TASK_NOT_FROZEN"
        reason = "The write, delete, and reverse tasks are not frozen before scoring."
    elif not packet.task_natural_future_operation_split:
        label = "REJECTED_NO_TASK_NATURAL_SPLIT"
        reason = "No task-natural future-operation split is declared."
    elif not absorber_vector_matched(packet):
        label = "REJECTED_ABSORBER_VECTOR_NOT_MATCHED"
        reason = "The fixed H7 absorber vector is incomplete or unmatched."
    elif not packet.substrate_specific_absorber_data_declared:
        label = "REJECTED_NO_SUBSTRATE_SPECIFIC_ABSORBERS"
        reason = "Substrate-specific absorber data are missing."
    elif not packet.allowed_control_class_declared:
        label = "REJECTED_NO_ALLOWED_CONTROL_CLASS"
        reason = "Possibility versus impossibility is undefined without allowed controls."
    elif not packet.finite_operational_substrate:
        label = "REJECTED_NO_FINITE_OPERATIONAL_SUBSTRATE"
        reason = "The packet relies on an idealization without a finite operational reading."
    elif not packet.constructor_impossible_after_full_accounting:
        label = "REJECTED_DELETION_STILL_CONTROL_POSSIBLE"
        reason = "After matched accounting, the reverse is not constructor-impossible."
    elif not packet.future_operation_split_survives_matching:
        route = "absorbed_by_matched_accounting"
        label = "ABSORBED_SPLIT_VANISHES_AFTER_MATCHING"
        reason = "The future-operation split vanishes after absorber data are matched."
    elif not packet.negative_controls_declared:
        label = "REJECTED_NO_NEGATIVE_CONTROLS"
        reason = "No null controls block idealization, hidden sink, copy, or access overreads."
    else:
        admitted = True
        route = "admitted_as_synthetic_h7_review_target"
        label = "ADMITTED_H7_PHYSICAL_DELETION_REVIEW_TARGET_NO_PROMOTION"
        reason = (
            "The packet freezes the H7 minimum object and passes the absorber "
            "audit shape. Admission is review-target status only, not H7 evidence."
        )

    return {
        "packet": _packet_to_dict(packet),
        "absorber_vector_matched": absorber_vector_matched(packet),
        "minimum_h7_commitment_met": minimum_h7_commitment_met(packet),
        "admitted_for_future_h7_review": admitted,
        "h7_reopened": False,
        "route": route,
        "label": label,
        "reason": reason,
    }


def full_burden_packet(packet_id: str, description: str) -> DeletionPacket:
    return DeletionPacket(
        packet_id=packet_id,
        description=description,
        reverse_edge_class=PHYSICAL_RECORD_DELETION,
        named_physical_substrate=True,
        record_encoding_frozen=True,
        write_delete_reverse_task_frozen=True,
        task_natural_future_operation_split=True,
        fixed_absorber_vector_declared=True,
        free_energy_floor_matched=True,
        blank_capacity_matched=True,
        sink_export_history_matched=True,
        observer_boundary_matched=True,
        provenance_authority_matched=True,
        source_copy_status_matched=True,
        reversible_control_access_matched=True,
        substrate_specific_absorber_data_declared=True,
        allowed_control_class_declared=True,
        finite_operational_substrate=True,
        constructor_impossible_after_full_accounting=True,
        future_operation_split_survives_matching=True,
        negative_controls_declared=True,
        synthetic_positive_control=True,
    )


def candidate_packets() -> tuple[DeletionPacket, ...]:
    return (
        DeletionPacket(
            packet_id="t461_local_recovery_depth_overread",
            description="T461-style local recovery depth divergence read as deletion.",
            reverse_edge_class="local_recovery_depth",
            e1_locality_depth_only=True,
        ),
        DeletionPacket(
            packet_id="observer_access_revocation",
            description="The observer loses access to a record that still exists.",
            reverse_edge_class="access_loss",
            access_loss_only=True,
        ),
        DeletionPacket(
            packet_id="provenance_authority_revocation",
            description="The authority to rely on a record is revoked.",
            reverse_edge_class="provenance_loss",
            provenance_loss_only=True,
        ),
        DeletionPacket(
            packet_id="support_copy_removal",
            description="A redundant support copy is removed while source copies remain.",
            reverse_edge_class="support_copy_removal",
            support_copy_removal_only=True,
        ),
        DeletionPacket(
            packet_id="finite_barrier_metastable_delete",
            description="A finite metastable barrier is treated as deletion impossibility.",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            finite_barrier_or_kinetic_suppression=True,
        ),
        DeletionPacket(
            packet_id="hidden_sink_export_delete",
            description="Deletion appears impossible only because sink/export data are hidden.",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            hidden_sink_or_export=True,
        ),
        DeletionPacket(
            packet_id="changed_blind_reset_ledger",
            description="Blind reset changes free-energy or blank-capacity accounting.",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            thermodynamic_ledger_changes=True,
        ),
        DeletionPacket(
            packet_id="source_copy_reversible_control_missing",
            description="Hidden source copies or reversible controls are withheld.",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            hidden_source_copy_or_reversible_control=True,
        ),
        DeletionPacket(
            packet_id="ideal_sector_lock_delete",
            description="An exact sector or ideal lock is used without finite substrate audit.",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            ideal_limit_or_exact_sector_lock=True,
        ),
        DeletionPacket(
            packet_id="gauge_relabeling_record_loss",
            description="Record loss is only a change of representative.",
            reverse_edge_class="gauge_relabeling",
            gauge_relabeling=True,
        ),
        DeletionPacket(
            packet_id="substrate_incomplete_delete_claim",
            description="The reverse is named deletion but no concrete substrate is frozen.",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
        ),
        DeletionPacket(
            packet_id="control_possible_after_accounting",
            description="Full accounting is declared, but deletion remains control-possible.",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            record_encoding_frozen=True,
            write_delete_reverse_task_frozen=True,
            task_natural_future_operation_split=True,
            fixed_absorber_vector_declared=True,
            free_energy_floor_matched=True,
            blank_capacity_matched=True,
            sink_export_history_matched=True,
            observer_boundary_matched=True,
            provenance_authority_matched=True,
            source_copy_status_matched=True,
            reversible_control_access_matched=True,
            substrate_specific_absorber_data_declared=True,
            allowed_control_class_declared=True,
            finite_operational_substrate=True,
        ),
        DeletionPacket(
            packet_id="matched_split_vanishes",
            description="Deletion impossibility is asserted but the future split vanishes.",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            record_encoding_frozen=True,
            write_delete_reverse_task_frozen=True,
            task_natural_future_operation_split=True,
            fixed_absorber_vector_declared=True,
            free_energy_floor_matched=True,
            blank_capacity_matched=True,
            sink_export_history_matched=True,
            observer_boundary_matched=True,
            provenance_authority_matched=True,
            source_copy_status_matched=True,
            reversible_control_access_matched=True,
            substrate_specific_absorber_data_declared=True,
            allowed_control_class_declared=True,
            finite_operational_substrate=True,
            constructor_impossible_after_full_accounting=True,
        ),
        full_burden_packet(
            "synthetic_full_burden_physical_deletion_packet",
            "Synthetic calibration target with every H7 absorber field frozen.",
        ),
    )


def run() -> dict[str, Any]:
    classifications = [classify_packet(packet) for packet in candidate_packets()]
    admitted = [
        item for item in classifications if item["admitted_for_future_h7_review"]
    ]
    rejected_or_absorbed = [
        item for item in classifications if not item["admitted_for_future_h7_review"]
    ]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "h7_handoff": SOURCE_H7,
            "t145_fixed_accounting": SOURCE_T145,
            "t160_substrate_family_screen": SOURCE_T160,
            "t168_sector_screen": SOURCE_T168,
            "t439_finite_time_catalytic_gate": SOURCE_T439,
            "t440_ideal_sector_gate": SOURCE_T440,
            "t441_e1_family_gate": SOURCE_T441,
            "t461_locality_control": SOURCE_T461,
            "taxonomy_reference": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Convert T461's physical-deletion overread warning into an "
            "executable H7 absorber audit."
        ),
        "minimum_h7_object": [
            "reverse edge typed as physical_record_deletion",
            "named physical substrate and frozen record encoding",
            "write, delete, and reverse task frozen before comparison",
            "task-natural future-operation split declared",
            "full H7 absorber vector declared and matched",
            "substrate-specific absorber data declared",
            "allowed control class declared",
            "finite operational substrate supplied",
            "reverse remains constructor-impossible after full accounting",
            "future-operation split survives matched accounting",
            "negative controls declared",
        ],
        "classifications": classifications,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_review_target_ids": [
                item["packet"]["packet_id"] for item in admitted
            ],
            "rejected_or_absorbed_ids": [
                item["packet"]["packet_id"] for item in rejected_or_absorbed
            ],
            "synthetic_positive_controls_only": all(
                item["packet"]["synthetic_positive_control"] for item in admitted
            ),
            "all_h7_reopened_flags_false": all(
                item["h7_reopened"] is False for item in classifications
            ),
            "h7_promotion": "none; admission is review-target status only",
            "physical_deletion_evidence": "none; no named real substrate clears the audit",
            "claim_ledger_update": "none; no claim promotion or demotion",
            "reading": (
                "T462 absorbs T461-style locality depth, access loss, provenance "
                "loss, support-copy removal, finite kinetic barriers, hidden "
                "sink/export, changed ledger accounting, hidden source-copy or "
                "reversible-control gaps, exact ideal/sector locks, and gauge "
                "relabeling before H7 can reopen. The only admitted packet is a "
                "synthetic full-burden review target."
            ),
        },
        "recommended_next": [
            "Use T462 before treating any E1 locality or ideal-lock packet as H7 physical-deletion evidence.",
            "Do not reopen H7 without a named real substrate that clears the full T462 object.",
            "Keep T461 as a locality control, not a deletion or thermodynamic-arrow result.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["minimum_h7_object"]]
    rows = [
        "| {packet_id} | {label} | {route} | {admitted} | {h7} |".format(
            packet_id=item["packet"]["packet_id"],
            label=item["label"],
            route=item["route"],
            admitted="yes" if item["admitted_for_future_h7_review"] else "no",
            h7="yes" if item["h7_reopened"] else "no",
        )
        for item in result["classifications"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T462 - H7 Physical-Deletion Overread Absorber - v0.1 results",
            "",
            "> Recorded-tier absorber audit only. `CLAIM-LEDGER.md`, "
            "`TESTS.md`, `ROADMAP.md`, README, North Star files, public posture, "
            "hard policy, and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T462-h7-physical-deletion-overread-absorber.md`",
            "- Model: `models/h7_physical_deletion_overread_absorber.py`",
            "- Tests: `tests/test_h7_physical_deletion_overread_absorber.py`",
            "- Artifact JSON: `results/T462-h7-physical-deletion-overread-absorber-v0.1.json`",
            "- Sources: H7 handoff, T145, T160, T168, T439, T440, T441, T461, and the taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Minimum H7 Object",
            "",
            *requirements,
            "",
            "## Packet Classification",
            "",
            "| packet | label | route | admitted? | H7 reopened? |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable absorber audit for future physical-deletion overreads.",
            "",
            "Does not earn: H7 promotion, physical-deletion substrate evidence, "
            "an E1 theorem, an E3 theorem, a thermodynamic-arrow theorem, "
            "stochastic-thermodynamic theorem, claim-ledger movement, public "
            "posture, or cross-repo support.",
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
        json_path = results_dir / "T462-h7-physical-deletion-overread-absorber-v0.1.json"
        md_path = (
            results_dir
            / "T462-h7-physical-deletion-overread-absorber-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
