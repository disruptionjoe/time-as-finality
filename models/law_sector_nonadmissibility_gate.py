"""T452 - law-sector nonadmissibility gate.

T445 showed that a finite substrate-law packet can clear T434 without merely
restating a transition table, but it still factors through explicit law-sector
completion. T452 turns the next burden into an executable gate: a stronger
region-indexed capability packet must make the law-sector completion physically
non-admissible, not merely hidden from R.

Recorded-tier admission gate only. This is not a discriminator success, not a
physics theorem, not a WAY theorem, and not claim support.

Run:

    python -m models.law_sector_nonadmissibility_gate --write-results
    python -m pytest tests/test_law_sector_nonadmissibility_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import region_capability_substrate_law_big_swing as t445


ARTIFACT = "T452-law-sector-nonadmissibility-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T434 = "results/T434-substrate-law-admission-gate-v0.1-results.md"
SOURCE_T445 = "results/T445-region-capability-substrate-law-big-swing-v0.1-results.md"
SOURCE_T436 = "results/T436-quantum-e3-resource-lift-classifier-v0.1-results.md"
SOURCE_T447 = "results/T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md"

VERDICT = "LAW_SECTOR_NONADMISSIBILITY_GATE_BUILT_CURRENT_T445_NOT_ADMITTED"

HONEST_CEILING = (
    "Recorded-tier admission gate only. T452 blocks the current T445 law-sector "
    "packet from being read as a discriminator success because explicit "
    "law-sector completion remains admissible. It admits only a synthetic future "
    "review target with a predeclared exact nonadmissibility witness, A2 "
    "resource-lift audit, frozen operations, and negative control. It is not a "
    "physics theorem, not a WAY theorem, not claim-ledger movement, and not "
    "public posture."
)


@dataclass(frozen=True)
class LawSectorPacket:
    packet_id: str
    description: str
    source: str
    clears_t434_law_admission: bool
    r_statistics_and_interventions_matched: bool
    boundary_menu_splits_capability: bool
    law_sector_completion_named: bool
    completion_merely_hidden_from_r: bool
    transition_table_restatement: bool = False
    post_hoc_policy: bool = False
    hidden_label_or_case_id: bool = False
    allowed_operations_frozen: bool = True
    a2_resource_lift_audited: bool = True
    a2_reference_restores_completion: bool = False
    consumed_or_cyclic_resource_restores_completion: bool = False
    cost_or_limit_only: bool = False
    exact_nonadmissibility_witness_predeclared: bool = False
    negative_control_present: bool = True
    synthetic_control_only: bool = False


def _packet_to_dict(packet: LawSectorPacket) -> dict[str, Any]:
    return asdict(packet)


def _base_packet_ok(packet: LawSectorPacket) -> bool:
    return (
        packet.clears_t434_law_admission
        and packet.r_statistics_and_interventions_matched
        and packet.boundary_menu_splits_capability
        and packet.law_sector_completion_named
    )


def evaluate_packet(packet: LawSectorPacket) -> dict[str, Any]:
    admitted = False

    if packet.transition_table_restatement:
        label = "NOT_ADMITTED_TRANSITION_TABLE_RESTATEMENT"
        reason = "The packet reuses the T434 failure mode instead of supplying a law."
    elif packet.post_hoc_policy:
        label = "NOT_ADMITTED_POST_HOC_NONADMISSIBILITY_POLICY"
        reason = "The completion policy is selected after seeing the pair."
    elif packet.hidden_label_or_case_id:
        label = "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
        reason = "The completion policy reads a hidden label or case id."
    elif not _base_packet_ok(packet):
        label = "NOT_ADMITTED_BASE_PACKET_INCOMPLETE"
        reason = (
            "A law-sector nonadmissibility packet must first clear T434, match "
            "R-supported statistics and interventions, split under the boundary "
            "menu, and name the completion it blocks."
        )
    elif packet.completion_merely_hidden_from_r:
        label = "NOT_ADMITTED_COMPLETION_MERELY_OUTSIDE_R"
        reason = (
            "The law-sector completion is outside R but still admissible once the "
            "boundary/law sector is included. This is the T445 absorber."
        )
    elif packet.cost_or_limit_only:
        label = "ROUTES_TO_E1_E2_NOT_SINGLE_PACKET_NONADMISSIBILITY"
        reason = (
            "A large cost or family limit may be a separate E1/E2 packet, but it "
            "does not make law-sector completion physically non-admissible in "
            "this single-packet gate."
        )
    elif not packet.allowed_operations_frozen:
        label = "NOT_ADMITTED_ALLOWED_OPERATIONS_UNFROZEN"
        reason = "The allowed operation class must be frozen before scoring completion."
    elif not packet.a2_resource_lift_audited:
        label = "NOT_ADMITTED_A2_RESOURCE_LIFT_UNTESTED"
        reason = "The packet must audit reference/resource completions before claiming nonadmissibility."
    elif packet.a2_reference_restores_completion:
        label = "RESOURCE_LIFT_ABSORBS_LAW_SECTOR_SPLIT"
        reason = "A2 reference or compensator resources restore the completion."
    elif packet.consumed_or_cyclic_resource_restores_completion:
        label = "RESOURCE_COMPLETION_CONTROL_RESTORES_OR_ROUTES_AWAY"
        reason = "Consumed or cyclic resources restore the task or route it away from exact nonadmissibility."
    elif not packet.exact_nonadmissibility_witness_predeclared:
        label = "NOT_ADMITTED_NO_EXACT_NONADMISSIBILITY_WITNESS"
        reason = "The packet lacks a predeclared exact witness that forbids the completion."
    elif not packet.negative_control_present:
        label = "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
        reason = "A negative control is required to show the gate can reject a nearby completion."
    else:
        admitted = True
        label = "ADMITTED_LAW_SECTOR_NONADMISSIBILITY_REVIEW_TARGET_NO_PROMOTION"
        reason = (
            "The packet clears the law-admission base gate, freezes operations, "
            "audits A2 resources, supplies a predeclared exact nonadmissibility "
            "witness, and includes a negative control. This is admitted only as "
            "a future review target."
        )

    return {
        "packet_id": packet.packet_id,
        "description": packet.description,
        "source": packet.source,
        "packet": _packet_to_dict(packet),
        "admitted": admitted,
        "residue_label": label,
        "reason": reason,
    }


def _current_t445_packet() -> LawSectorPacket:
    snapshot = t445.run()["overall_verdict"]
    return LawSectorPacket(
        packet_id="current_t445_z2_law_packet",
        description=(
            "The current T445 Z2 law packet clears T434 and splits under a "
            "boundary compensator, but law-sector completion still absorbs it."
        ),
        source=SOURCE_T445,
        clears_t434_law_admission=bool(snapshot["t434_main_packet_admitted"]),
        r_statistics_and_interventions_matched=bool(
            snapshot["main_pair_r_statistics_equal"]
            and snapshot["main_pair_r_interventions_equal"]
        ),
        boundary_menu_splits_capability=bool(snapshot["boundary_pair_splits"]),
        law_sector_completion_named=True,
        completion_merely_hidden_from_r=bool(snapshot["law_sector_completion_absorbs"]),
        a2_resource_lift_audited=True,
        a2_reference_restores_completion=not bool(
            snapshot["reference_resource_pair_splits"]
        ),
        exact_nonadmissibility_witness_predeclared=False,
    )


def packets() -> tuple[LawSectorPacket, ...]:
    return (
        _current_t445_packet(),
        LawSectorPacket(
            packet_id="t445_reference_resource_lift_control",
            description="A2 reference/compensator resources restore revision capability.",
            source=SOURCE_T445,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            a2_reference_restores_completion=True,
        ),
        LawSectorPacket(
            packet_id="transition_table_restatement_control",
            description="A transition-table restatement cannot be promoted to nonadmissibility.",
            source=SOURCE_T434,
            clears_t434_law_admission=False,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            transition_table_restatement=True,
        ),
        LawSectorPacket(
            packet_id="post_hoc_completion_policy_control",
            description="A completion ban chosen after pair selection is not admitted.",
            source=ARTIFACT,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            post_hoc_policy=True,
        ),
        LawSectorPacket(
            packet_id="hidden_label_completion_policy_control",
            description="A completion policy keyed to a hidden label is blocked.",
            source=ARTIFACT,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            hidden_label_or_case_id=True,
        ),
        LawSectorPacket(
            packet_id="family_cost_only_packet",
            description="A diverging cost claim routes to E1/E2 review, not this single-packet gate.",
            source=SOURCE_T447,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            cost_or_limit_only=True,
        ),
        LawSectorPacket(
            packet_id="missing_a2_resource_lift_audit",
            description="An A1-only packet cannot claim completion nonadmissibility.",
            source=SOURCE_T436,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            a2_resource_lift_audited=False,
            exact_nonadmissibility_witness_predeclared=True,
        ),
        LawSectorPacket(
            packet_id="no_exact_nonadmissibility_witness",
            description="A packet that audits A2 but lacks an exact witness remains incomplete.",
            source=ARTIFACT,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            exact_nonadmissibility_witness_predeclared=False,
        ),
        LawSectorPacket(
            packet_id="synthetic_exact_nonadmissibility_packet",
            description=(
                "Synthetic calibration: a frozen operation class plus an exact "
                "no-go witness forbids the named law-sector completion after A2 audit."
            ),
            source=ARTIFACT,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            exact_nonadmissibility_witness_predeclared=True,
            synthetic_control_only=True,
        ),
        LawSectorPacket(
            packet_id="synthetic_missing_negative_control",
            description="A nearby synthetic packet with no negative control is rejected.",
            source=ARTIFACT,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            completion_merely_hidden_from_r=False,
            exact_nonadmissibility_witness_predeclared=True,
            negative_control_present=False,
            synthetic_control_only=True,
        ),
    )


def run() -> dict[str, Any]:
    evaluations = [evaluate_packet(packet) for packet in packets()]
    current = next(
        item for item in evaluations if item["packet_id"] == "current_t445_z2_law_packet"
    )
    admitted = [item for item in evaluations if item["admitted"]]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t434": SOURCE_T434,
            "t445": SOURCE_T445,
            "t436": SOURCE_T436,
            "t447": SOURCE_T447,
        },
        "purpose": (
            "Turn T445's next burden into an executable gate: future "
            "region-indexed law packets must show law-sector completion is "
            "physically non-admissible, not merely outside R."
        ),
        "admission_requirements": [
            "clear T434 law admission first",
            "match all declared R-supported statistics and interventions",
            "split capability only under the boundary/law menu",
            "name the law-sector completion being blocked",
            "freeze the allowed operation/resource class before pair selection",
            "audit A2 reference/resource completion",
            "supply a predeclared exact nonadmissibility witness",
            "include a negative control",
            "avoid hidden labels, post-hoc policies, and transition-table restatements",
        ],
        "packet_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "current_t445_admitted": current["admitted"],
            "current_t445_label": current["residue_label"],
            "admitted_packet_ids": [item["packet_id"] for item in admitted],
            "admitted_packets_are_synthetic_only": all(
                item["packet"]["synthetic_control_only"] for item in admitted
            ),
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T452 builds the missing gate after T445. The current T445 packet "
                "does not pass because law-sector completion is only outside R, "
                "not physically non-admissible. The gate admits only a synthetic "
                "future target with a predeclared exact witness and A2 audit."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Do not treat T445-style hidden law-sector packets as discriminator successes.",
            "A future positive packet must forbid the completion under a frozen operation/resource class.",
            "Pair any stronger attempt with T434 admission and T436/T447-style resource-lift controls.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["admission_requirements"]]
    rows = [
        "| {packet_id} | {admitted} | {label} |".format(
            packet_id=item["packet_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["residue_label"],
        )
        for item in result["packet_evaluations"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T452 - Law-Sector Nonadmissibility Gate - v0.1 results",
            "",
            "> Recorded-tier admission gate. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T452-law-sector-nonadmissibility-gate.md`",
            "- Model: `models/law_sector_nonadmissibility_gate.py`",
            "- Tests: `tests/test_law_sector_nonadmissibility_gate.py`",
            "- Artifact JSON: `results/T452-law-sector-nonadmissibility-gate-v0.1.json`",
            "- Sources: T434, T445, T436/T447, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Admission Requirements",
            "",
            *requirements,
            "",
            "## Packet Evaluation",
            "",
            "| packet | admitted? | residue label |",
            "| --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: an executable gate for the next region-indexed substrate-law burden. "
            "It records that the current T445-style packet remains absorbed by "
            "law-sector completion.",
            "",
            "Does not earn: a region-indexed discriminator success, a real substrate "
            "law, a physics theorem, a WAY theorem, a claim-ledger update, public "
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
        json_path = results_dir / "T452-law-sector-nonadmissibility-gate-v0.1.json"
        md_path = results_dir / "T452-law-sector-nonadmissibility-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
