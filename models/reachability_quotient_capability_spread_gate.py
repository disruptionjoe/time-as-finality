"""T487: reachability-quotient capability-spread gate.

T485 admits a stable source/target reachability quotient as bookkeeping only.
This module asks the next narrower question: which declared transport-task
capabilities are determined by that quotient signature, and which tempting
readings remain underdetermined or blocked?

The module consumes the committed T485 result artifact instead of re-running
T485. This keeps T487 downstream of quotient stability without reopening the
transport-topology refinement lane.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ARTIFACT_ID = "T487-reachability-quotient-capability-spread-gate-v0.1"
T485_ARTIFACT_ID = "T485-transport-topology-invariant-quotient-gate-v0.1"
VERDICT = "REACHABILITY_QUOTIENT_CAPABILITY_SPREAD_BUILT_TASK_ONLY"


@dataclass(frozen=True)
class CapabilityCandidate:
    """One capability reading proposed after T485."""

    candidate_id: str
    role: str
    cap_field: str
    native_comparison: str
    local_anchor: str
    task_natural: bool
    uses_reachability_quotient: bool = False
    uses_path_length: bool = False
    uses_hop_band: bool = False
    uses_relay_count: bool = False
    uses_component_size: bool = False
    changes_record_finality: bool = False
    treats_quotient_as_scale_structure: bool = False
    claims_clock_duration_or_arrow: bool = False
    claims_scale_genesis_or_physics: bool = False
    requests_claim_or_posture_promotion: bool = False


def capability_candidates() -> tuple[CapabilityCandidate, ...]:
    """Return the finite post-T485 capability catalogue."""

    return (
        CapabilityCandidate(
            candidate_id="source_target_reachability_task",
            role="positive_review_control",
            cap_field="source_target_reachable",
            native_comparison="Boolean equality for the declared transport task",
            local_anchor="T485 admitted reachability quotient",
            task_natural=True,
            uses_reachability_quotient=True,
        ),
        CapabilityCandidate(
            candidate_id="quotient_role_profile_task",
            role="positive_review_control",
            cap_field="quotient_role_profile",
            native_comparison="role-profile equality over original observer sites",
            local_anchor="T485 admitted reachability quotient",
            task_natural=True,
            uses_reachability_quotient=True,
        ),
        CapabilityCandidate(
            candidate_id="path_latency_band_task",
            role="hostile_control",
            cap_field="source_target_hop_band",
            native_comparison="hop-band equality",
            local_anchor="T485 blocked hop-band scale reading",
            task_natural=False,
            uses_hop_band=True,
            uses_path_length=True,
            claims_clock_duration_or_arrow=True,
        ),
        CapabilityCandidate(
            candidate_id="relay_budget_task",
            role="hostile_control",
            cap_field="relay_site_count",
            native_comparison="exact relay-count equality",
            local_anchor="T485 blocked relay-count reading",
            task_natural=False,
            uses_relay_count=True,
            claims_clock_duration_or_arrow=True,
        ),
        CapabilityCandidate(
            candidate_id="component_size_capacity_task",
            role="hostile_control",
            cap_field="max_component_size",
            native_comparison="component-size equality",
            local_anchor="T485 blocked component-size reading",
            task_natural=False,
            uses_component_size=True,
            treats_quotient_as_scale_structure=True,
        ),
        CapabilityCandidate(
            candidate_id="reachability_finality_task",
            role="hostile_control",
            cap_field="record_finality_status",
            native_comparison="finality-status equality",
            local_anchor="T485 finality overread guard",
            task_natural=False,
            uses_reachability_quotient=True,
            changes_record_finality=True,
        ),
        CapabilityCandidate(
            candidate_id="quotient_promotion_task",
            role="hostile_control",
            cap_field="claim_or_public_posture_status",
            native_comparison="promotion-status equality",
            local_anchor="T485 promotion shortcut guard",
            task_natural=False,
            uses_reachability_quotient=True,
            treats_quotient_as_scale_structure=True,
            claims_scale_genesis_or_physics=True,
            requests_claim_or_posture_promotion=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T487 capability-spread gate."""

    t485 = _load_t485_result()
    fixture_rows = _fixture_rows(t485)
    spreads = {
        candidate.cap_field: _capability_spread(fixture_rows, candidate.cap_field)
        for candidate in capability_candidates()
    }
    evaluations = [
        _evaluate_candidate(candidate, spreads[candidate.cap_field])
        for candidate in capability_candidates()
    ]
    admitted = [row["candidate_id"] for row in evaluations if row["admitted"]]
    hostile_violations = [
        row["candidate_id"]
        for row in evaluations
        if row["role"] == "hostile_control" and row["admitted"]
    ]
    expected_admissions = [
        "source_target_reachability_task",
        "quotient_role_profile_task",
    ]
    reachability_spread_singleton = spreads["source_target_reachable"][
        "all_visible_classes_singleton"
    ]
    role_profile_spread_singleton = spreads["quotient_role_profile"][
        "all_visible_classes_singleton"
    ]
    path_band_undertermined = not spreads["source_target_hop_band"][
        "all_visible_classes_singleton"
    ]
    relay_undertermined = not spreads["relay_site_count"][
        "all_visible_classes_singleton"
    ]
    component_size_undertermined = not spreads["max_component_size"][
        "all_visible_classes_singleton"
    ]
    gate_passed = (
        _t485_anchor_ok(t485)
        and admitted == expected_admissions
        and not hostile_violations
        and reachability_spread_singleton
        and role_profile_spread_singleton
        and path_band_undertermined
        and relay_undertermined
        and component_size_undertermined
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Consume T485's stable reachability quotient and test capability "
            "spread over the quotient-visible fibers without rerunning T485."
        ),
        "t485_anchor": {
            "artifact_id": t485["artifact_id"],
            "verdict": t485["overall_verdict"]["verdict"],
            "gate_passed": t485["overall_verdict"]["gate_passed"],
            "reachability_quotient_admitted": t485["overall_verdict"][
                "reachability_quotient_admitted"
            ],
            "component_size_scale_blocked": t485["overall_verdict"][
                "component_size_scale_blocked"
            ],
            "hop_band_scale_blocked": t485["overall_verdict"][
                "hop_band_scale_blocked"
            ],
            "record_finality_change_earned": t485["overall_verdict"][
                "record_finality_change_earned"
            ],
        },
        "visible_projection": (
            "T485 quotient_signature over original observer-site source/target "
            "reachability roles"
        ),
        "fixture_rows": fixture_rows,
        "capability_spreads": spreads,
        "candidate_evaluations": evaluations,
        "admitted_candidate_ids": admitted,
        "hostile_violations": hostile_violations,
        "overall_verdict": {
            "verdict": VERDICT,
            "gate_passed": gate_passed,
            "reachability_task_sufficient": reachability_spread_singleton,
            "role_profile_task_sufficient": role_profile_spread_singleton,
            "path_latency_underdetermined": path_band_undertermined,
            "relay_budget_underdetermined": relay_undertermined,
            "component_size_underdetermined": component_size_undertermined,
            "hostile_controls_blocked": not hostile_violations,
            "internal_scale_structure_earned": False,
            "record_clock_or_duration_earned": False,
            "record_finality_change_earned": False,
            "scale_genesis_theorem_earned": False,
            "physics_claim_earned": False,
            "claim_ledger_update": "none",
            "north_star_update": "none",
            "roadmap_update": "none",
            "public_posture_update": "none",
            "reading": (
                "The T485 quotient signature is sufficient for the declared "
                "reachability task and quotient role-profile task. It is not "
                "sufficient for path-latency, relay-budget, or component-size "
                "capabilities, whose spreads are non-singleton over the same "
                "visible quotient class. Finality, scale, physics, and "
                "promotion readings remain blocked overreads."
            ),
        },
        "future_packet_minimum": [
            "state the capability object before reading the reachability quotient as sufficient",
            "compute capability spread over quotient-visible fibers",
            "treat non-singleton path, relay, and component-size spreads as underdetermination",
            "do not convert reachability sufficiency into scale, clock, duration, finality, physics, or promotion evidence",
        ],
        "not_earned": [
            "independent internal scale structure",
            "record clock",
            "duration or temporal arrow",
            "record-finality change",
            "scale-genesis theorem",
            "physics or conformal-gravity claim",
            "D1 promotion",
            "RG/TaF equivalence theorem",
            "claim-ledger movement",
            "roadmap movement",
            "North Star movement",
            "public-posture movement",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Render T487 results as Markdown."""

    verdict = result["overall_verdict"]
    anchor_rows = [
        f"| {key} | {value} |" for key, value in result["t485_anchor"].items()
    ]
    fixture_rows = [
        "| {fixture_id} | {quotient_signature} | {source_target_reachable} | {source_target_hop_band} | {relay_site_count} | {max_component_size} |".format(
            **row
        )
        for row in result["fixture_rows"]
    ]
    spread_rows = [
        "| {field} | {singleton} | {classes} |".format(
            field=field,
            singleton=spread["all_visible_classes_singleton"],
            classes=spread["visible_class_spreads"],
        )
        for field, spread in result["capability_spreads"].items()
    ]
    candidate_rows = []
    for row in result["candidate_evaluations"]:
        blockers = ", ".join(row["blockers"]) or "none"
        candidate_rows.append(
            "| {candidate_id} | {role} | {decision} | {route_label} | {blockers} |".format(
                candidate_id=row["candidate_id"],
                role=row["role"],
                decision=row["decision"],
                route_label=row["route_label"],
                blockers=blockers,
            )
        )
    minimum = [f"- {item}" for item in result["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in result["not_earned"]]

    return "\n".join(
        [
            "# T487 - Reachability Quotient Capability Spread Gate - v0.1 results",
            "",
            "> Downstream capability-spread gate only. This consumes the committed "
            "T485 artifact and does not rerun T485 or change claim status, "
            "roadmap, README, North Star, public posture, hard policy, physics "
            "posture, scale, clock, duration, finality, or cross-repo truth.",
            "",
            "- Spec: `tests/T487-reachability-quotient-capability-spread-gate.md`",
            "- Model: `models/reachability_quotient_capability_spread_gate.py`",
            "- Tests: `tests/test_reachability_quotient_capability_spread_gate.py`",
            "- Artifact JSON: `results/T487-reachability-quotient-capability-spread-gate-v0.1.json`",
            "- Anchor artifact: `results/T485-transport-topology-invariant-quotient-gate-v0.1.json`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## T485 Anchor",
            "",
            "| field | value |",
            "| --- | --- |",
            *anchor_rows,
            "",
            "## Fixture Rows",
            "",
            "| fixture | quotient signature | reachable | hop band | relays | max component size |",
            "| --- | --- | --- | --- | --- | --- |",
            *fixture_rows,
            "",
            "## Capability Spreads",
            "",
            "| capability field | singleton on visible fibers | visible-class spreads |",
            "| --- | --- | --- |",
            *spread_rows,
            "",
            "## Candidate Evaluations",
            "",
            "| candidate | role | decision | route | blockers |",
            "| --- | --- | --- | --- | --- |",
            *candidate_rows,
            "",
            "## Future Packet Minimum",
            "",
            *minimum,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _load_t485_result() -> dict[str, Any]:
    path = Path("results") / f"{T485_ARTIFACT_ID}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _t485_anchor_ok(t485: dict[str, Any]) -> bool:
    verdict = t485["overall_verdict"]
    return (
        t485["artifact_id"] == T485_ARTIFACT_ID
        and verdict["gate_passed"] is True
        and verdict["reachability_quotient_admitted"] is True
        and verdict["component_size_scale_blocked"] is True
        and verdict["hop_band_scale_blocked"] is True
        and verdict["record_finality_change_earned"] is False
    )


def _fixture_rows(t485: dict[str, Any]) -> list[dict[str, Any]]:
    fixtures = t485["quotient_probe"]["fixture_summaries"]
    rows = []
    for fixture_id, fixture in fixtures.items():
        quotient_signature = _tuple_signature(fixture["quotient_signature"])
        component_sizes = tuple(tuple(item) for item in fixture["component_size_signature"])
        rows.append(
            {
                "fixture_id": fixture_id,
                "quotient_signature": quotient_signature,
                "source_target_reachable": any(
                    role == "source_target_component"
                    for role, _count in quotient_signature
                ),
                "quotient_role_profile": quotient_signature,
                "source_target_hop_band": fixture["source_target_hop_band"],
                "relay_site_count": fixture["relay_site_count"],
                "component_size_signature": component_sizes,
                "max_component_size": max(size for _observer, size in component_sizes),
                "record_finality_status": "unchanged",
                "claim_or_public_posture_status": "none",
            }
        )
    return rows


def _tuple_signature(value: list[list[Any]]) -> tuple[tuple[Any, ...], ...]:
    return tuple(tuple(item) for item in value)


def _capability_spread(
    fixture_rows: list[dict[str, Any]],
    cap_field: str,
) -> dict[str, Any]:
    spreads: dict[str, set[str]] = {}
    for row in fixture_rows:
        visible_key = repr(row["quotient_signature"])
        spreads.setdefault(visible_key, set()).add(repr(row[cap_field]))
    visible_class_spreads = {
        visible_key: sorted(values)
        for visible_key, values in sorted(spreads.items())
    }
    return {
        "cap_field": cap_field,
        "visible_class_spreads": visible_class_spreads,
        "all_visible_classes_singleton": all(
            len(values) == 1 for values in visible_class_spreads.values()
        ),
        "non_singleton_visible_classes": [
            visible_key
            for visible_key, values in visible_class_spreads.items()
            if len(values) > 1
        ],
    }


def _evaluate_candidate(
    candidate: CapabilityCandidate,
    spread: dict[str, Any],
) -> dict[str, Any]:
    blockers: list[str] = []

    if not candidate.task_natural:
        blockers.append("capability_not_task_natural_under_t485")
    if not spread["all_visible_classes_singleton"]:
        blockers.append("non_singleton_capability_spread")
    if candidate.uses_path_length or candidate.uses_hop_band:
        blockers.append("path_or_hop_band_refinement_variant")
    if candidate.uses_relay_count:
        blockers.append("relay_count_refinement_artifact")
    if candidate.uses_component_size:
        blockers.append("component_size_refinement_variant")
    if candidate.treats_quotient_as_scale_structure:
        blockers.append("reachability_quotient_not_internal_scale_structure")
    if candidate.changes_record_finality:
        blockers.append("record_finality_change_overread")
    if candidate.claims_clock_duration_or_arrow:
        blockers.append("clock_duration_or_arrow_overread")
    if candidate.claims_scale_genesis_or_physics:
        blockers.append("scale_genesis_or_physics_claim_overread")
    if candidate.requests_claim_or_posture_promotion:
        blockers.append("claim_or_public_posture_promotion_shortcut")

    admitted = not blockers and candidate.role == "positive_review_control"
    if admitted:
        route_label = "REACHABILITY_CAPABILITY_SPREAD_SINGLETON"
        decision = "admit_declared_reachability_task_only"
    elif "non_singleton_capability_spread" in blockers:
        route_label = "CAPABILITY_UNDERDETERMINED_BY_QUOTIENT"
        decision = "reject_non_singleton_spread"
    else:
        route_label = "CAPABILITY_READING_BLOCKED"
        decision = "reject_or_block"

    return {
        "candidate_id": candidate.candidate_id,
        "role": candidate.role,
        "cap_field": candidate.cap_field,
        "native_comparison": candidate.native_comparison,
        "local_anchor": candidate.local_anchor,
        "admitted": admitted,
        "decision": decision,
        "route_label": route_label,
        "blockers": blockers,
        "spread": spread,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
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
