"""T529 - competency-surplus admission gate.

T493 showed that current C(R) content is absorbed when Levin/Fields-style
competency is granted as the full intervention-measured task-success profile.
T494 upgraded the bounded source status for that absorber warning. This gate
turns the post-T493/T494 burden into executable admission logic for future
region-indexed capability packets.

The gate does not prove any new packet. It classifies packet shapes:

- simple-statistics surplus remains review-only and is not surplus over a full
  competency profile;
- full-profile-equivalent packets are absorbed by competency bookkeeping;
- a future packet is admitted only as a review target if it fixes the region,
  menu, task context, checks the T493/T494 absorbers, keeps the full competency
  profile matched, and supplies an independent noncompletion witness for a
  capability that is not just another task-success coordinate.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import levin_competency_cr_absorber_gate as t493
from models import levin_fields_primary_source_absorber_gate as t494


ARTIFACT = "T529-competency-surplus-admission-gate-v0.1"
VERDICT = "COMPETENCY_SURPLUS_GATE_BUILT_REVIEW_ONLY"

SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T493 = "results/T493-levin-competency-cr-absorber-gate-v0.1-results.md"
SOURCE_T494 = "results/T494-levin-fields-primary-source-absorber-gate-v0.1-results.md"
SOURCE_T460 = "results/T460-post-t459-direction-a-restart-router-v0.1-results.md"

HONEST_CEILING = (
    "Review-only admission gate. T529 does not exhibit a successful "
    "region-indexed discriminator, does not prove surplus over Levin/Fields "
    "competency, does not import active-inference/free-energy/polycomputing "
    "mechanisms, and does not move claim status, Canon Index tiers, canon "
    "verdicts, roadmap, README, North Star, public posture, hard policy, "
    "external publication, or cross-repo truth."
)

READING = (
    "A future C(R) packet cannot count as competency-surplus merely because "
    "simple observed statistics are flat. T493 already shows that the current "
    "flat-statistics class spans the admitted C(R) profiles, while a full "
    "intervention-measured competency profile absorbs current C(R). T529 "
    "therefore requires the future packet to match the full competency profile "
    "and supply an independent noncompletion witness for a capability that is "
    "not just another task-success coordinate."
)


@dataclass(frozen=True)
class Packet:
    packet_id: str
    description: str
    fixed_region_menu_task_context: bool
    checks_t493_t494_absorbers: bool
    primary_source_status_checked: bool
    same_simple_observed_statistics: bool
    same_full_competency_profile: bool
    capability_split: bool
    capability_is_task_success_coordinate: bool
    independent_noncompletion_witness: bool
    imports_external_mechanism: bool = False
    claims_current_success: bool = False
    claims_public_or_cross_repo_update: bool = False
    changes_claim_or_canon_status: bool = False


@dataclass(frozen=True)
class Evaluation:
    packet_id: str
    admitted: bool
    label: str
    action: str
    reason: str
    packet: Packet


def absorber_floor() -> dict[str, Any]:
    t493_payload = t493.run()
    t494_payload = t494.run()
    profile = t493_payload["absorber_audit"]["full_profile_absorber"][
        "profile_summary"
    ]
    single = t493_payload["absorber_audit"]["single_goal_control"]
    zero = t493_payload["absorber_audit"]["zero_trace_surplus_review"]
    return {
        "t493_verdict": t493_payload["overall_verdict"]["verdict"],
        "t494_verdict": t494_payload["overall_verdict"]["verdict"],
        "t493_full_profile_absorbs_current_c_r": t493_payload[
            "overall_verdict"
        ]["full_profile_absorbs_current_c_r"],
        "t493_same_resource_capability_splits": t493_payload[
            "absorber_audit"
        ]["full_profile_absorber"]["same_resource_capability_splits"],
        "t493_distinct_c_r_profiles": profile["n_distinct_profiles"],
        "t493_statistics_flat_spans_all_profiles": profile[
            "flat_statistics_spans_all_profiles"
        ],
        "t493_single_goal_collision_count": single["collision_count"],
        "t493_single_goal_absorbs_full_c_r": single[
            "single_goal_absorbs_full_c_r"
        ],
        "t493_zero_trace_review_only": zero["admitted_as_review_target"]
        and not zero["novelty_claim_admitted"],
        "t494_primary_source_scope_checked": t494_payload["overall_verdict"][
            "n16_upgraded_for_bounded_scope"
        ],
        "t494_claim_movement": t494_payload["overall_verdict"]["claim_movement"],
        "t494_public_or_cross_repo_movement": t494_payload["overall_verdict"][
            "public_or_cross_repo_movement"
        ],
    }


def packets() -> tuple[Packet, ...]:
    return (
        Packet(
            packet_id="current_t407_simple_statistics_surplus",
            description=(
                "Use T407-style equality of simple observed statistics as the "
                "claimed surplus target."
            ),
            fixed_region_menu_task_context=True,
            checks_t493_t494_absorbers=True,
            primary_source_status_checked=True,
            same_simple_observed_statistics=True,
            same_full_competency_profile=False,
            capability_split=True,
            capability_is_task_success_coordinate=True,
            independent_noncompletion_witness=False,
        ),
        Packet(
            packet_id="full_competency_profile_equivalent",
            description=(
                "Package a C(R) profile that is exactly the full "
                "intervention-measured task-success vector."
            ),
            fixed_region_menu_task_context=True,
            checks_t493_t494_absorbers=True,
            primary_source_status_checked=True,
            same_simple_observed_statistics=False,
            same_full_competency_profile=False,
            capability_split=False,
            capability_is_task_success_coordinate=True,
            independent_noncompletion_witness=False,
        ),
        Packet(
            packet_id="weak_single_statistic_proxy",
            description=(
                "Ask one observed navigation/readout statistic to stand for "
                "the full C(R) profile."
            ),
            fixed_region_menu_task_context=True,
            checks_t493_t494_absorbers=True,
            primary_source_status_checked=True,
            same_simple_observed_statistics=True,
            same_full_competency_profile=False,
            capability_split=True,
            capability_is_task_success_coordinate=True,
            independent_noncompletion_witness=False,
        ),
        Packet(
            packet_id="synthetic_competency_surplus_review_target",
            description=(
                "A future packet shape with fixed region/menu/task context, "
                "matched full competency profile, and a predeclared independent "
                "noncompletion witness for a non-task-success capability."
            ),
            fixed_region_menu_task_context=True,
            checks_t493_t494_absorbers=True,
            primary_source_status_checked=True,
            same_simple_observed_statistics=True,
            same_full_competency_profile=True,
            capability_split=True,
            capability_is_task_success_coordinate=False,
            independent_noncompletion_witness=True,
        ),
        Packet(
            packet_id="post_hoc_hidden_residual",
            description=(
                "Assert a hidden residual after pair selection without an "
                "independent noncompletion witness."
            ),
            fixed_region_menu_task_context=True,
            checks_t493_t494_absorbers=True,
            primary_source_status_checked=True,
            same_simple_observed_statistics=True,
            same_full_competency_profile=True,
            capability_split=True,
            capability_is_task_success_coordinate=False,
            independent_noncompletion_witness=False,
        ),
        Packet(
            packet_id="unchecked_source_status_packet",
            description=(
                "Use competency vocabulary without T494 primary-source status "
                "or bounded absorber scope."
            ),
            fixed_region_menu_task_context=True,
            checks_t493_t494_absorbers=True,
            primary_source_status_checked=False,
            same_simple_observed_statistics=True,
            same_full_competency_profile=True,
            capability_split=True,
            capability_is_task_success_coordinate=False,
            independent_noncompletion_witness=True,
        ),
        Packet(
            packet_id="active_inference_mechanism_import",
            description=(
                "Import active-inference/free-energy/polycomputing mechanisms "
                "as the reason C(R) escapes competency absorption."
            ),
            fixed_region_menu_task_context=True,
            checks_t493_t494_absorbers=True,
            primary_source_status_checked=True,
            same_simple_observed_statistics=True,
            same_full_competency_profile=True,
            capability_split=True,
            capability_is_task_success_coordinate=False,
            independent_noncompletion_witness=True,
            imports_external_mechanism=True,
        ),
        Packet(
            packet_id="claim_public_cross_repo_shortcut",
            description=(
                "Use the admission gate to move claims, public posture, or "
                "cross-repo truth."
            ),
            fixed_region_menu_task_context=True,
            checks_t493_t494_absorbers=True,
            primary_source_status_checked=True,
            same_simple_observed_statistics=True,
            same_full_competency_profile=True,
            capability_split=True,
            capability_is_task_success_coordinate=False,
            independent_noncompletion_witness=True,
            claims_current_success=True,
            claims_public_or_cross_repo_update=True,
            changes_claim_or_canon_status=True,
        ),
    )


def evaluate(packet: Packet, floor: dict[str, Any]) -> Evaluation:
    if packet.claims_public_or_cross_repo_update or packet.changes_claim_or_canon_status:
        return Evaluation(
            packet.packet_id,
            False,
            "BLOCKED_GOVERNANCE_OR_CROSS_REPO_SHORTCUT",
            "stop",
            "Admission gates cannot move claims, canon, public posture, or cross-repo truth.",
            packet,
        )
    if packet.claims_current_success:
        return Evaluation(
            packet.packet_id,
            False,
            "BLOCKED_CURRENT_SUCCESS_OVERREAD",
            "stop",
            "T529 admits future review targets only; it proves no current discriminator success.",
            packet,
        )
    if packet.imports_external_mechanism:
        return Evaluation(
            packet.packet_id,
            False,
            "REJECTED_EXTERNAL_MECHANISM_IMPORT",
            "reject",
            "T494 treats external mechanisms as neighbors and absorber pressure, not TaF machinery.",
            packet,
        )
    if not packet.primary_source_status_checked:
        return Evaluation(
            packet.packet_id,
            False,
            "REJECTED_UNCHECKED_COMPETENCY_SOURCE_STATUS",
            "reject",
            "Future packets must use the T494 bounded source-status discipline.",
            packet,
        )
    if not packet.checks_t493_t494_absorbers:
        return Evaluation(
            packet.packet_id,
            False,
            "REJECTED_MISSING_COMPETENCY_ABSORBER_CHECK",
            "reject",
            "Future packets must explicitly clear T493/T494 absorber pressure.",
            packet,
        )
    if not packet.fixed_region_menu_task_context:
        return Evaluation(
            packet.packet_id,
            False,
            "REJECTED_UNFIXED_REGION_MENU_TASK_CONTEXT",
            "reject",
            "Region, menu, and task context must be frozen before pair selection.",
            packet,
        )
    if packet.capability_is_task_success_coordinate:
        if packet.packet_id == "current_t407_simple_statistics_surplus":
            return Evaluation(
                packet.packet_id,
                True,
                "ADMITTED_SIMPLE_STATISTICS_REVIEW_ONLY_NOT_COMPETENCY_SURPLUS",
                "keep_as_simple_statistics_review_target",
                (
                    "T493 says simple statistics can be flat while full C(R) "
                    "profiles differ, so this is not surplus over full competency."
                ),
                packet,
            )
        return Evaluation(
            packet.packet_id,
            False,
            "ABSORBED_BY_FULL_COMPETENCY_PROFILE",
            "absorb",
            "If the capability is a task-success coordinate, the full competency profile contains it.",
            packet,
        )
    if not packet.same_full_competency_profile:
        return Evaluation(
            packet.packet_id,
            False,
            "REJECTED_COMPETENCY_PROFILE_NOT_MATCHED",
            "reject",
            "Surplus over competency requires matching the full competency profile, not only simple statistics.",
            packet,
        )
    if not packet.capability_split:
        return Evaluation(
            packet.packet_id,
            False,
            "REJECTED_NO_CAPABILITY_SPLIT",
            "reject",
            "A surplus packet must produce a capability split after the profile is matched.",
            packet,
        )
    if not packet.independent_noncompletion_witness:
        return Evaluation(
            packet.packet_id,
            False,
            "REJECTED_POST_HOC_OR_UNWITNESSED_RESIDUAL",
            "reject",
            "A post-hoc hidden residual is underdescription unless a predeclared noncompletion witness is supplied.",
            packet,
        )
    if (
        floor["t493_full_profile_absorbs_current_c_r"]
        and floor["t494_primary_source_scope_checked"]
        and floor["t493_same_resource_capability_splits"] == []
    ):
        return Evaluation(
            packet.packet_id,
            True,
            "ADMITTED_COMPETENCY_SURPLUS_FUTURE_REVIEW_TARGET",
            "review_only",
            (
                "The packet shape clears the formal admission burden, but T529 "
                "does not instantiate it or move claims."
            ),
            packet,
        )
    return Evaluation(
        packet.packet_id,
        False,
        "REJECTED_ABSORBER_FLOOR_NOT_ESTABLISHED",
        "reject",
        "The T493/T494 absorber floor is not available.",
        packet,
    )


def run() -> dict[str, Any]:
    floor = absorber_floor()
    evaluations = [evaluate(packet, floor) for packet in packets()]
    admitted = [item.packet_id for item in evaluations if item.admitted]
    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t493": SOURCE_T493,
            "t494": SOURCE_T494,
            "t460": SOURCE_T460,
        },
        "absorber_floor": floor,
        "packet_evaluations": [
            {
                "packet_id": item.packet_id,
                "admitted": item.admitted,
                "label": item.label,
                "action": item.action,
                "reason": item.reason,
                "packet": asdict(item.packet),
            }
            for item in evaluations
        ],
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_packet_ids": admitted,
            "synthetic_future_review_target_admitted": (
                "synthetic_competency_surplus_review_target" in admitted
            ),
            "current_simple_statistics_surplus_is_competency_surplus": False,
            "current_discriminator_success": False,
            "claim_movement": False,
            "canon_or_public_posture_movement": False,
            "cross_repo_movement": False,
        },
        "reading": READING,
        "claim_ledger_update": "none; no claim promotion or demotion",
        "recommended_next": [
            "Use T529 as the admission checklist before reopening the C(R) route.",
            "Treat T407-style flat simple statistics as review material only.",
            "Reject packets whose alleged surplus is just another task-success coordinate.",
            "Any future positive packet still needs its own executable witness and T460-class route checks.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    floor = payload["absorber_floor"]
    packet_rows = [
        "| {packet_id} | {admitted} | {label} | {action} | {reason} |".format(
            packet_id=item["packet_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["label"],
            action=item["action"],
            reason=item["reason"],
        )
        for item in payload["packet_evaluations"]
    ]
    next_lines = [f"- {item}" for item in payload["recommended_next"]]
    return "\n".join(
        [
            "# T529 - Competency Surplus Admission Gate - v0.1 results",
            "",
            "> Review-only admission gate. No claim-ledger, Canon Index, canon verdict, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T529-competency-surplus-admission-gate.md`",
            "- Model: `models/competency_surplus_admission_gate.py`",
            "- Tests: `tests/test_competency_surplus_admission_gate.py`",
            "- Artifact JSON: `results/T529-competency-surplus-admission-gate-v0.1.json`",
            "- Absorber floor: T493/T494",
            "",
            f"## Overall verdict: {payload['overall_verdict']['verdict']}",
            "",
            payload["reading"],
            "",
            "## Absorber Floor",
            "",
            "| Check | Value |",
            "| --- | --- |",
            f"| T493 verdict | {floor['t493_verdict']} |",
            f"| T494 verdict | {floor['t494_verdict']} |",
            f"| Full profile absorbs current C(R) | {floor['t493_full_profile_absorbs_current_c_r']} |",
            f"| Same-resource capability splits after T493/T398 | {floor['t493_same_resource_capability_splits']} |",
            f"| Distinct C(R) profiles | {floor['t493_distinct_c_r_profiles']} |",
            f"| Flat simple-statistics class spans all profiles | {floor['t493_statistics_flat_spans_all_profiles']} |",
            f"| Single-goal collision count | {floor['t493_single_goal_collision_count']} |",
            f"| T494 bounded source scope checked | {floor['t494_primary_source_scope_checked']} |",
            "",
            "## Packet Evaluation",
            "",
            "| Packet | Admitted? | Label | Action | Reason |",
            "| --- | --- | --- | --- | --- |",
            *packet_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: an executable admission checklist for future competency-surplus `C(R)` packets.",
            "",
            "Does not earn: an actual region-indexed discriminator success, novelty over Levin/Fields competency, imported external mechanism, claim movement, canon movement, public posture, or cross-repo support.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_lines,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T529-competency-surplus-admission-gate-v0.1.json"
        md_path = results_dir / "T529-competency-surplus-admission-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
