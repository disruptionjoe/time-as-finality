"""T461 - E1 local-recovery family audition.

T441 admits only family-level E1 packets with finite approximants, fixed task
and operation class, a predeclared finite-auditable invariant, controls, and a
diverging recovery cost or nonlocality quantity. T461 turns that synthetic shape
into a concrete local-recovery family control.

The result is intentionally narrow: a nearest-neighbor recovery depth can
diverge across a finite family, but the split factors through ordinary locality
and endpoint distance. This is useful E1 calibration, not H7 physical-deletion
evidence and not claim support.

Run:

    python -m models.e1_local_recovery_family_audition --write-results
    python -m pytest tests/test_e1_local_recovery_family_audition.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import ceil
from pathlib import Path
from typing import Any

from models import e1_family_limit_packet_gate as t441


ARTIFACT = "T461-e1-local-recovery-family-audition-v0.1"
SOURCE_T441 = "results/T441-e1-family-limit-packet-gate-v0.1-results.md"
SOURCE_T440 = "results/T440-ideal-limit-sector-lock-routing-gate-v0.1-results.md"
SOURCE_H7 = "open-problems/h7-physical-deletion-substrate-handoff.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "E1_LOCAL_RECOVERY_FAMILY_AUDITION_BUILT_LOCALITY_ONLY_NO_H7_REOPENING"

HONEST_CEILING = (
    "Recorded-tier E1 calibration only. T461 does not promote H7, does not "
    "prove an E1 limit theorem, does not derive a thermodynamic arrow, does "
    "not supply physical-deletion evidence, does not move claim status, and "
    "does not authorize public posture."
)


@dataclass(frozen=True)
class LocalRecoveryFamily:
    family_id: str
    description: str
    scale_values: tuple[int, ...]
    operation_radius: int = 1
    fixed_depth_budget: int = 2
    family_declared: bool = True
    scale_parameter_declared: bool = True
    approximant_map_declared: bool = True
    same_task_across_family: bool = True
    same_operation_class_across_family: bool = True
    observer_boundary_fixed: bool = True
    resource_accounting_fixed: bool = True
    limit_invariant_predeclared: bool = True
    invariant_observable_on_approximants: bool = True
    convergence_or_error_controls_declared: bool = True
    negative_control_declared: bool = True
    physical_record_deletion_reverse_edge: bool = False
    post_hoc_limit_selector: bool = False
    family_drift_or_reencoding: bool = False
    hidden_resource_or_boundary_change: bool = False
    finite_barrier_or_kinetic_suppression: bool = False
    finite_positive_gap_only: bool = False
    e2_hardness_basis: bool = False
    e3_exact_no_go_basis: bool = False


def _family_to_dict(family: LocalRecoveryFamily) -> dict[str, Any]:
    data = asdict(family)
    data["scale_values"] = list(family.scale_values)
    return data


def finite_approximant_profiles(family: LocalRecoveryFamily) -> list[dict[str, Any]]:
    """Return finite local-chain profiles for the declared family.

    Scale n means a chain with observer/control endpoint at 0 and the target
    record at n. Nearest-neighbor local recovery with radius r needs ceil(n/r)
    sequential local steps.
    """

    if family.operation_radius <= 0:
        raise ValueError("operation_radius must be positive")

    profiles: list[dict[str, Any]] = []
    for scale in family.scale_values:
        if scale <= 0:
            raise ValueError("scale values must be positive")
        min_depth = ceil(scale / family.operation_radius)
        profiles.append(
            {
                "scale": scale,
                "chain_sites": scale + 1,
                "observer_site": 0,
                "record_site": scale,
                "endpoint_distance": scale,
                "operation_radius": family.operation_radius,
                "minimum_local_recovery_depth": min_depth,
                "fixed_depth_budget": family.fixed_depth_budget,
                "recoverable_with_fixed_depth_budget": (
                    min_depth <= family.fixed_depth_budget
                ),
                "region_shadow": "same observer endpoint and local radius",
                "boundary_completion": "admit path to endpoint record",
            }
        )
    return profiles


def recovery_depth_sequence(family: LocalRecoveryFamily) -> list[int]:
    return [
        int(item["minimum_local_recovery_depth"])
        for item in finite_approximant_profiles(family)
    ]


def sequence_is_strictly_increasing(values: list[int]) -> bool:
    return all(left < right for left, right in zip(values, values[1:]))


def has_diverging_locality_witness(family: LocalRecoveryFamily) -> bool:
    """Finite audit predicate for the declared linear-depth formula."""

    values = recovery_depth_sequence(family)
    return (
        len(values) >= 3
        and sequence_is_strictly_increasing(values)
        and family.operation_radius > 0
        and max(values) > family.fixed_depth_budget
    )


def t441_packet_for_family(family: LocalRecoveryFamily) -> t441.E1LimitPacket:
    profiles = finite_approximant_profiles(family)
    return t441.E1LimitPacket(
        packet_id=family.family_id,
        description=family.description,
        family_declared=family.family_declared,
        scale_parameter_declared=family.scale_parameter_declared,
        finite_approximants_declared=len(profiles) >= 3,
        approximant_map_declared=family.approximant_map_declared,
        same_task_across_family=family.same_task_across_family,
        same_operation_class_across_family=(
            family.same_operation_class_across_family
        ),
        observer_boundary_fixed=family.observer_boundary_fixed,
        resource_accounting_fixed=family.resource_accounting_fixed,
        limit_invariant_predeclared=family.limit_invariant_predeclared,
        invariant_observable_on_approximants=(
            family.invariant_observable_on_approximants
        ),
        convergence_or_error_controls_declared=(
            family.convergence_or_error_controls_declared
        ),
        negative_control_declared=family.negative_control_declared,
        recovery_cost_sequence_declared=True,
        recovery_cost_diverges_across_family=(
            has_diverging_locality_witness(family)
            and not family.finite_barrier_or_kinetic_suppression
            and not family.finite_positive_gap_only
        ),
        nonlocality_diverges_across_family=has_diverging_locality_witness(family),
        finite_barrier_or_kinetic_suppression=(
            family.finite_barrier_or_kinetic_suppression
        ),
        finite_positive_gap_only=family.finite_positive_gap_only,
        post_hoc_limit_selector=family.post_hoc_limit_selector,
        family_drift_or_reencoding=family.family_drift_or_reencoding,
        hidden_resource_or_boundary_change=(
            family.hidden_resource_or_boundary_change
        ),
        e2_hardness_basis=family.e2_hardness_basis,
        e3_exact_no_go_basis=family.e3_exact_no_go_basis,
        synthetic_positive_control=False,
    )


def classify_family(family: LocalRecoveryFamily) -> dict[str, Any]:
    t441_packet = t441_packet_for_family(family)
    t441_classification = t441.classify_packet(t441_packet)
    profiles = finite_approximant_profiles(family)
    depth_sequence = recovery_depth_sequence(family)

    admitted_by_t441 = t441_classification["admitted_for_future_e1_review"]
    if not admitted_by_t441:
        label = "NOT_E1_ADMITTED_BY_T441"
        route = "reject_or_route_by_t441"
        h7_reopened = False
        reason = "The family fails or routes away under the existing T441 gate."
    elif family.physical_record_deletion_reverse_edge:
        label = "E1_ADMITTED_BUT_H7_REQUIRES_DELETION_ABSORBER_AUDIT"
        route = "separate_h7_physical_deletion_review_required"
        h7_reopened = False
        reason = (
            "T441 admission is not H7 evidence. A physical-deletion reading "
            "would need the H7 substrate absorber stack, not just locality depth."
        )
    else:
        label = "E1_LOCALITY_CONTROL_ADMITTED_NO_H7_REOPENING"
        route = "admitted_as_e1_locality_control"
        h7_reopened = False
        reason = (
            "The family clears the structural E1 packet shape, but the "
            "divergence factors through ordinary endpoint distance and local "
            "operation radius."
        )

    return {
        "family": _family_to_dict(family),
        "finite_profiles": profiles,
        "recovery_depth_sequence": depth_sequence,
        "strictly_increasing_depth": sequence_is_strictly_increasing(depth_sequence),
        "has_diverging_locality_witness": has_diverging_locality_witness(family),
        "t441_packet": asdict(t441_packet),
        "t441_label": t441_classification["label"],
        "t441_route": t441_classification["route"],
        "t441_admitted_for_future_e1_review": admitted_by_t441,
        "label": label,
        "route": route,
        "h7_reopened": h7_reopened,
        "reason": reason,
    }


def candidate_families() -> tuple[LocalRecoveryFamily, ...]:
    return (
        LocalRecoveryFamily(
            family_id="nearest_neighbor_endpoint_recovery_chain",
            description=(
                "Finite chain family with observer at one endpoint and record at "
                "distance n; nearest-neighbor recovery depth grows as n."
            ),
            scale_values=(2, 4, 8, 16),
            fixed_depth_budget=2,
        ),
        LocalRecoveryFamily(
            family_id="single_window_endpoint_recovery",
            description="A single finite recovery instance, not an E1 family.",
            scale_values=(4,),
        ),
        LocalRecoveryFamily(
            family_id="finite_barrier_metastable_recovery",
            description="A finite kinetic barrier relabeled as an E1 family.",
            scale_values=(2, 4, 8),
            finite_barrier_or_kinetic_suppression=True,
        ),
        LocalRecoveryFamily(
            family_id="post_hoc_distance_selector",
            description="A distance cutoff selected after seeing the separator.",
            scale_values=(2, 4, 8),
            post_hoc_limit_selector=True,
        ),
        LocalRecoveryFamily(
            family_id="drifting_task_operation_family",
            description="The task and operation menu change with n.",
            scale_values=(2, 4, 8),
            same_task_across_family=False,
            same_operation_class_across_family=False,
        ),
        LocalRecoveryFamily(
            family_id="hidden_relay_resource_family",
            description="A relay resource appears at larger n and changes the boundary.",
            scale_values=(2, 4, 8),
            hidden_resource_or_boundary_change=True,
        ),
        LocalRecoveryFamily(
            family_id="e2_hardness_labeled_recovery",
            description="A hardness-assumption recovery family mislabeled as E1.",
            scale_values=(2, 4, 8),
            e2_hardness_basis=True,
        ),
        LocalRecoveryFamily(
            family_id="locality_family_claimed_as_deletion",
            description=(
                "The same local-depth family overread as physical record deletion."
            ),
            scale_values=(2, 4, 8, 16),
            physical_record_deletion_reverse_edge=True,
        ),
    )


def run() -> dict[str, Any]:
    classifications = [classify_family(family) for family in candidate_families()]
    admitted_locality = [
        item
        for item in classifications
        if item["route"] == "admitted_as_e1_locality_control"
    ]
    deletion_overreads = [
        item
        for item in classifications
        if item["route"] == "separate_h7_physical_deletion_review_required"
    ]
    t441_rejected_or_routed = [
        item for item in classifications if item["route"] == "reject_or_route_by_t441"
    ]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "t441_e1_family_gate": SOURCE_T441,
            "t440_e1_route": SOURCE_T440,
            "h7_handoff": SOURCE_H7,
            "taxonomy_reference": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Audition a concrete finite local-recovery family against the T441 "
            "E1 packet gate while preserving the H7 physical-deletion boundary."
        ),
        "family_model": {
            "finite_approximant": "path graph with observer/control endpoint 0 and record endpoint n",
            "approximant_map": "n maps to the finite path of length n with nearest-neighbor local operations",
            "predeclared_limit_invariant": "minimum local recovery depth grows with endpoint distance",
            "capability_question": (
                "can a fixed-depth local operation recover the endpoint record?"
            ),
            "absorber_reading": (
                "the split is ordinary distance/locality accounting once endpoint "
                "position and operation radius are admitted"
            ),
        },
        "classifications": classifications,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_locality_control_ids": [
                item["family"]["family_id"] for item in admitted_locality
            ],
            "deletion_overread_ids": [
                item["family"]["family_id"] for item in deletion_overreads
            ],
            "rejected_or_routed_ids": [
                item["family"]["family_id"] for item in t441_rejected_or_routed
            ],
            "all_h7_reopened_flags_false": all(
                item["h7_reopened"] is False for item in classifications
            ),
            "e1_theorem": "none; finite family control and admission audit only",
            "h7_promotion": "none; locality depth is not physical-record-deletion evidence",
            "claim_ledger_update": "none; no claim promotion or demotion",
            "reading": (
                "T461 provides a concrete T441-positive E1 family control: "
                "nearest-neighbor endpoint recovery has finite approximants, a "
                "stable task and operation class, fixed observer/resource "
                "accounting, and recovery depth that grows with endpoint distance. "
                "The result is not H7 evidence because the capability split factors "
                "through ordinary locality data once endpoint distance and local "
                "operation radius are admitted."
            ),
        },
        "recommended_next": [
            "Use T461 as the positive locality control for future E1 family-limit packets.",
            "Do not cite local recovery-depth divergence as physical deletion or H7 support.",
            "A non-null H7 follow-up still needs a named physical-deletion substrate that survives T439, T440, T441, and the H7 absorber stack.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    rows = [
        "| {family_id} | {t441_label} | {label} | {route} | {h7} |".format(
            family_id=item["family"]["family_id"],
            t441_label=item["t441_label"],
            label=item["label"],
            route=item["route"],
            h7="yes" if item["h7_reopened"] else "no",
        )
        for item in result["classifications"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T461 - E1 Local-Recovery Family Audition - v0.1 results",
            "",
            "> Recorded-tier E1 calibration only. `CLAIM-LEDGER.md`, "
            "`TESTS.md`, `ROADMAP.md`, README, North Star files, public posture, "
            "hard policy, and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T461-e1-local-recovery-family-audition.md`",
            "- Model: `models/e1_local_recovery_family_audition.py`",
            "- Tests: `tests/test_e1_local_recovery_family_audition.py`",
            "- Artifact JSON: `results/T461-e1-local-recovery-family-audition-v0.1.json`",
            "- Sources: T441, T440, H7 substrate handoff, and the taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Family Model",
            "",
            f"- Finite approximant: {result['family_model']['finite_approximant']}.",
            f"- Approximant map: {result['family_model']['approximant_map']}.",
            f"- Predeclared invariant: {result['family_model']['predeclared_limit_invariant']}.",
            f"- Capability question: {result['family_model']['capability_question']}",
            f"- Absorber reading: {result['family_model']['absorber_reading']}.",
            "",
            "## Candidate Classification",
            "",
            "| family | T441 label | T461 label | route | H7 reopened? |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a concrete T441-positive local-recovery family control for "
            "future E1 packet review.",
            "",
            "Does not earn: H7 promotion, physical-deletion evidence, an E1 "
            "limit theorem, a thermodynamic-arrow theorem, stochastic-"
            "thermodynamic theorem, claim-ledger movement, public posture, or "
            "cross-repo support.",
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
        json_path = results_dir / "T461-e1-local-recovery-family-audition-v0.1.json"
        md_path = results_dir / "T461-e1-local-recovery-family-audition-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
