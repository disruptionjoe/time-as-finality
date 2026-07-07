"""T493 - Levin/Fields competency C(R) absorber gate.

N16 introduced Levin/Fields competency as a calibration neighbor and absorber
candidate for the region-indexed capability object C(R). This executable gate
keeps that dual role disciplined:

- if competency is granted as the full intervention-measured task-success
  profile over a declared region, menu, and task family, current T407/T398 C(R)
  content is absorbed as a competency/resource profile;
- if competency is weakened to a single observed navigation statistic, it does
  not absorb the multi-task C(R) profile;
- the T407 statistics-flat capability split remains a useful surplus target
  only as an internal review target, not as novelty or claim support.

N16 is pointer-grade in this repo. This model does not verify Levin/Fields
primary sources and does not import an active-inference mechanism.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models.region_capability_no_go import (
    FEATURED_PAIR,
    NAMED_CONFIGS,
    TASK_NAMES,
    TOL_EXACT,
    run_analysis,
)


ARTIFACT = "T493-levin-competency-cr-absorber-gate-v0.1"
VERDICT = "N16_COMPETENCY_GATE_BUILT_FULL_PROFILE_ABSORBS_SURPLUS_REVIEW_ONLY"

SOURCE_N16 = "literature/N16-levin-competency-capability-neighbor.md"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T407 = "results/T407-region-capability-no-go-v0.1-results.md"
SOURCE_T398 = "results/T398-resource-profile-absorber-v0.1-results.md"
SOURCE_T460 = "results/T460-post-t459-direction-a-restart-router-v0.1-results.md"

HONEST_CEILING = (
    "Calibration and absorber gate only. T493 does not verify Levin/Fields "
    "primary sources, does not prove novelty over competency/TAME, does not "
    "import active inference or free-energy mechanisms, does not prove a "
    "region-indexed discriminator success, and does not move claim ledger, "
    "roadmap, public posture, hard policy, protected-license material, or "
    "cross-repo truth."
)

READING = (
    "N16 is useful precisely because it cuts both ways. A full "
    "intervention-measured task-success profile over region R behaves like the "
    "current finite C(R) object and absorbs it as competency-style capability "
    "bookkeeping. A weaker single-goal or observed-navigation statistic does "
    "not absorb C(R). T407's zero-trace statistics/capability split therefore "
    "remains a review target for surplus over simple observed statistics, but "
    "not a novelty claim over Levin/Fields competency."
)


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    description: str
    grants_full_task_success_profile: bool
    uses_single_observed_success_statistic: bool
    declares_region_menu_task_context: bool
    uses_t407_zero_trace_split: bool
    primary_sources_checked: bool
    imports_external_mechanism: bool = False
    claims_novelty_or_public_posture: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class Evaluation:
    candidate_id: str
    admitted: bool
    label: str
    action: str
    reason: str
    candidate: Candidate


def _round_profile(profile: dict[str, float]) -> tuple[float, ...]:
    return tuple(round(float(profile[task]), 12) for task in TASK_NAMES)


def _t407_profile_summary(t407: dict[str, Any]) -> dict[str, Any]:
    profile_by_config = {
        config_key: _round_profile(entry["profile"])
        for config_key, entry in t407["profiles"].items()
    }
    distinct_profiles = sorted(set(profile_by_config.values()))
    flat_class = next(
        c
        for c in t407["leg3"]["statistics_partition"]["classes"]
        if "|".join(NAMED_CONFIGS["pristine"]) in c
    )
    flat_profiles = sorted({profile_by_config[config] for config in flat_class})
    featured_keys = {
        name: "|".join(NAMED_CONFIGS[name])
        for name in FEATURED_PAIR
    }
    featured_profiles = {
        name: profile_by_config[key]
        for name, key in featured_keys.items()
    }
    return {
        "n_configurations": len(profile_by_config),
        "n_distinct_profiles": len(distinct_profiles),
        "task_names": list(TASK_NAMES),
        "flat_statistics_class_size": len(flat_class),
        "flat_statistics_distinct_profile_count": len(flat_profiles),
        "flat_statistics_spans_all_profiles": len(flat_profiles) == len(distinct_profiles),
        "featured_pair": {
            "names": list(FEATURED_PAIR),
            "profiles": {k: list(v) for k, v in featured_profiles.items()},
            "statistics_max_diff": t407["leg3"]["featured_pair"]["stats_max_diff"],
            "capability_incomparable": t407["leg3"]["featured_pair"][
                "gap_floor_met_both_directions"
            ],
        },
    }


def _single_goal_collision_audit(t407: dict[str, Any]) -> dict[str, Any]:
    by_class_readout: dict[float, list[dict[str, Any]]] = {}
    for config_key, entry in t407["profiles"].items():
        profile = _round_profile(entry["profile"])
        class_readout = profile[TASK_NAMES.index("class_readout")]
        by_class_readout.setdefault(class_readout, []).append(
            {
                "config": config_key,
                "profile": profile,
                "passes": entry["passes"],
            }
        )

    collisions = []
    for class_readout, entries in sorted(by_class_readout.items()):
        profile_set = {entry["profile"] for entry in entries}
        undo_cross_pass_set = {
            bool(entry["passes"]["undo_cross"])
            for entry in entries
        }
        if len(profile_set) > 1 and len(undo_cross_pass_set) > 1:
            low = next(
                entry
                for entry in entries
                if bool(entry["passes"]["undo_cross"]) is False
            )
            high = next(
                entry
                for entry in entries
                if bool(entry["passes"]["undo_cross"]) is True
            )
            collisions.append(
                {
                    "single_goal_value": class_readout,
                    "witness_configs": [low["config"], high["config"]],
                    "witness_profiles": [list(low["profile"]), list(high["profile"])],
                    "split_task": "undo_cross",
                }
            )

    return {
        "single_goal_statistic": "class_readout_success",
        "collision_count": len(collisions),
        "collisions": collisions,
        "single_goal_absorbs_full_c_r": len(collisions) == 0,
    }


def _same_profile_capability_splits(t407: dict[str, Any]) -> list[dict[str, Any]]:
    by_profile: dict[tuple[float, ...], list[tuple[str, tuple[bool, ...]]]] = {}
    for config_key, entry in t407["profiles"].items():
        profile = _round_profile(entry["profile"])
        passes = tuple(bool(entry["passes"][task]) for task in TASK_NAMES)
        by_profile.setdefault(profile, []).append((config_key, passes))

    splits = []
    for profile, entries in by_profile.items():
        pass_classes: dict[tuple[bool, ...], list[str]] = {}
        for config_key, passes in entries:
            pass_classes.setdefault(passes, []).append(config_key)
        if len(pass_classes) > 1:
            splits.append(
                {
                    "profile": list(profile),
                    "pass_classes": {
                        str(passes): sorted(configs)
                        for passes, configs in pass_classes.items()
                    },
                }
            )
    return splits


def _absorber_audit(t407: dict[str, Any]) -> dict[str, Any]:
    profile_summary = _t407_profile_summary(t407)
    single_goal = _single_goal_collision_audit(t407)
    return {
        "full_profile_absorber": {
            "frame": "competency as full intervention-measured task-success profile",
            "absorbs_current_c_r": True,
            "reason": (
                "Once the task-success vector over the declared region, menu, "
                "and task family is granted, current T407 C(R) is exactly the "
                "admitted capability profile, and T398 shows capability "
                "verdicts factor through that profile."
            ),
            "same_resource_capability_splits": _same_profile_capability_splits(t407),
            "t398_source": SOURCE_T398,
            "profile_summary": profile_summary,
        },
        "single_goal_control": single_goal,
        "zero_trace_surplus_review": {
            "admitted_as_review_target": True,
            "novelty_claim_admitted": False,
            "reason": (
                "T407's flat declared R-statistics class spans all admitted "
                "profiles, so simple observed statistics do not decide the "
                "capability profile. But this is not surplus over a full "
                "competency profile, because that profile already includes the "
                "intervention-measured task-success vector."
            ),
            "statistics_flat_spans_all_profiles": profile_summary[
                "flat_statistics_spans_all_profiles"
            ],
            "featured_pair_statistics_max_diff": profile_summary["featured_pair"][
                "statistics_max_diff"
            ],
            "featured_pair_capability_incomparable": profile_summary["featured_pair"][
                "capability_incomparable"
            ],
        },
        "external_source_status": {
            "n16_primary_sources_checked": False,
            "source_grade": "pointer_grade_intake_extract",
            "safe_use": "internal calibration and absorber-target formulation only",
        },
    }


def candidates() -> tuple[Candidate, ...]:
    return (
        Candidate(
            candidate_id="full_competency_profile_absorber",
            description=(
                "Treat competency as the full intervention-measured task-success "
                "profile over the declared region, menu, and task family."
            ),
            grants_full_task_success_profile=True,
            uses_single_observed_success_statistic=False,
            declares_region_menu_task_context=True,
            uses_t407_zero_trace_split=False,
            primary_sources_checked=False,
        ),
        Candidate(
            candidate_id="single_goal_navigation_statistic",
            description=(
                "Treat competency as one observed navigation/readout success "
                "statistic and ask it to absorb the whole C(R) profile."
            ),
            grants_full_task_success_profile=False,
            uses_single_observed_success_statistic=True,
            declares_region_menu_task_context=True,
            uses_t407_zero_trace_split=False,
            primary_sources_checked=False,
        ),
        Candidate(
            candidate_id="t407_zero_trace_surplus_target",
            description=(
                "Use T407's statistics-flat capability spread as a future "
                "surplus target over simple observed statistics."
            ),
            grants_full_task_success_profile=False,
            uses_single_observed_success_statistic=False,
            declares_region_menu_task_context=True,
            uses_t407_zero_trace_split=True,
            primary_sources_checked=False,
        ),
        Candidate(
            candidate_id="external_mechanism_import",
            description=(
                "Import Levin/Fields mechanism language, active inference, or "
                "free-energy substrate into TaF C(R)."
            ),
            grants_full_task_success_profile=False,
            uses_single_observed_success_statistic=False,
            declares_region_menu_task_context=False,
            uses_t407_zero_trace_split=False,
            primary_sources_checked=False,
            imports_external_mechanism=True,
        ),
        Candidate(
            candidate_id="novelty_or_public_posture_shortcut",
            description=(
                "Treat N16 resonance as evidence that TaF has a public novelty "
                "or claim-status upgrade over competency."
            ),
            grants_full_task_success_profile=False,
            uses_single_observed_success_statistic=False,
            declares_region_menu_task_context=False,
            uses_t407_zero_trace_split=True,
            primary_sources_checked=False,
            claims_novelty_or_public_posture=True,
        ),
        Candidate(
            candidate_id="cross_repo_active_inference_absorber_update",
            description=(
                "Update a temporal-issuance or active-inference absorber from "
                "this TaF run."
            ),
            grants_full_task_success_profile=False,
            uses_single_observed_success_statistic=False,
            declares_region_menu_task_context=False,
            uses_t407_zero_trace_split=False,
            primary_sources_checked=False,
            requests_cross_repo_truth=True,
        ),
    )


def evaluate(candidate: Candidate, audit: dict[str, Any]) -> Evaluation:
    if candidate.claims_novelty_or_public_posture:
        return Evaluation(
            candidate.candidate_id,
            False,
            "BLOCKED_NOVELTY_PUBLIC_POSTURE_SHORTCUT",
            "stop",
            "N16 resonance is not evidence for claim, novelty, or public-posture movement.",
            candidate,
        )
    if candidate.requests_cross_repo_truth:
        return Evaluation(
            candidate.candidate_id,
            False,
            "BLOCKED_CROSS_REPO_TRUTH_UPDATE",
            "stop",
            "Cross-repo absorber updates must route as proposals; this run stays inside TaF.",
            candidate,
        )
    if candidate.imports_external_mechanism:
        return Evaluation(
            candidate.candidate_id,
            False,
            "REJECTED_EXTERNAL_MECHANISM_IMPORT_PRIMARY_SOURCES_UNCHECKED",
            "reject",
            "N16 is pointer-grade, and coupling/free-energy mechanisms are not TaF C(R) machinery.",
            candidate,
        )
    if candidate.grants_full_task_success_profile:
        absorbed = audit["full_profile_absorber"]["absorbs_current_c_r"]
        return Evaluation(
            candidate.candidate_id,
            absorbed,
            "ADMITTED_AS_FULL_PROFILE_ABSORBER_NO_CLAIM",
            "absorb_current_c_r_as_competency_profile",
            "Full intervention-measured competency profile is equivalent to the current admitted C(R) profile.",
            candidate,
        )
    if candidate.uses_single_observed_success_statistic:
        collision_count = audit["single_goal_control"]["collision_count"]
        return Evaluation(
            candidate.candidate_id,
            False,
            "REJECTED_SINGLE_GOAL_STATISTIC_COLLIDES_WITH_C_R",
            "reject",
            f"Single observed success statistic has {collision_count} collision(s) with different C(R) profiles.",
            candidate,
        )
    if candidate.uses_t407_zero_trace_split:
        review = audit["zero_trace_surplus_review"]
        return Evaluation(
            candidate.candidate_id,
            bool(review["admitted_as_review_target"]),
            "ADMITTED_REVIEW_TARGET_SIMPLE_STATISTICS_ONLY_NO_NOVELTY",
            "keep_as_future_surplus_target",
            "T407 can challenge simple observed-statistic readings, not a full competency profile.",
            candidate,
        )
    return Evaluation(
        candidate.candidate_id,
        False,
        "REJECTED_UNTYPED_COMPETENCY_ANALOGY",
        "reject",
        "The candidate does not declare enough region, menu, task, or profile structure.",
        candidate,
    )


def run() -> dict[str, Any]:
    t407 = run_analysis()
    audit = _absorber_audit(t407)
    evaluations = [evaluate(candidate, audit) for candidate in candidates()]
    admitted = [item.candidate_id for item in evaluations if item.admitted]
    return {
        "artifact": ARTIFACT,
        "sources": {
            "n16": SOURCE_N16,
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t407": SOURCE_T407,
            "t398": SOURCE_T398,
            "t460": SOURCE_T460,
        },
        "primary_source_status": "not_checked_pointer_grade_only",
        "absorber_audit": audit,
        "candidate_evaluations": [
            {
                "candidate_id": item.candidate_id,
                "admitted": item.admitted,
                "label": item.label,
                "action": item.action,
                "reason": item.reason,
                "candidate": asdict(item.candidate),
            }
            for item in evaluations
        ],
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_candidate_ids": admitted,
            "full_profile_absorbs_current_c_r": audit["full_profile_absorber"][
                "absorbs_current_c_r"
            ],
            "single_goal_absorbs_full_c_r": audit["single_goal_control"][
                "single_goal_absorbs_full_c_r"
            ],
            "zero_trace_surplus_is_review_only": audit["zero_trace_surplus_review"][
                "admitted_as_review_target"
            ]
            and not audit["zero_trace_surplus_review"]["novelty_claim_admitted"],
        },
        "reading": READING,
        "claim_ledger_update": "none; no claim promotion or demotion",
        "recommended_next": [
            "Use N16 as a calibration/absorber checklist for future C(R) packets.",
            "Do not cite T493 as novelty over Levin/Fields competency.",
            "Before any external-facing statement, verify primary sources and run a separate literature absorber note.",
            "Any stronger Direction-A restart still has to satisfy T460's new-packet-class requirements.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    eval_rows = [
        "| {candidate_id} | {admitted} | {label} | {action} | {reason} |".format(
            candidate_id=item["candidate_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["label"],
            action=item["action"],
            reason=item["reason"],
        )
        for item in payload["candidate_evaluations"]
    ]
    next_lines = [f"- {item}" for item in payload["recommended_next"]]
    profile = payload["absorber_audit"]["full_profile_absorber"]["profile_summary"]
    single = payload["absorber_audit"]["single_goal_control"]
    zero_trace = payload["absorber_audit"]["zero_trace_surplus_review"]

    return "\n".join(
        [
            "# T493 - Levin Competency C(R) Absorber Gate - v0.1 results",
            "",
            "> Calibration and absorber gate only. No claim-ledger, roadmap, "
            "README, North Star, public-posture, hard-policy, protected-license, "
            "external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T493-levin-competency-cr-absorber-gate.md`",
            "- Model: `models/levin_competency_cr_absorber_gate.py`",
            "- Tests: `tests/test_levin_competency_cr_absorber_gate.py`",
            "- Artifact JSON: `results/T493-levin-competency-cr-absorber-gate-v0.1.json`",
            "- Sources: N16, T407, T398, T460, and the region-indexed capability discriminator open problem",
            "- Primary-source status: not checked; pointer-grade N16 only",
            "",
            f"## Overall verdict: {payload['overall_verdict']['verdict']}",
            "",
            payload["reading"],
            "",
            "## Profile Absorber Check",
            "",
            "| Check | Value |",
            "| --- | --- |",
            f"| T407 configurations | {profile['n_configurations']} |",
            f"| Distinct C(R) profiles | {profile['n_distinct_profiles']} |",
            f"| Statistics-flat class size | {profile['flat_statistics_class_size']} |",
            f"| Statistics-flat class spans all profiles | {profile['flat_statistics_spans_all_profiles']} |",
            f"| Same-resource capability splits after T398 | {payload['absorber_audit']['full_profile_absorber']['same_resource_capability_splits']} |",
            "",
            "## Single-Goal Control",
            "",
            f"Single observed statistic: `{single['single_goal_statistic']}`.",
            f"Collision count against full C(R): {single['collision_count']}.",
            "",
            "## Zero-Trace Review Target",
            "",
            f"- Statistics-flat spans all profiles: {zero_trace['statistics_flat_spans_all_profiles']}",
            f"- Featured-pair statistics max diff: {zero_trace['featured_pair_statistics_max_diff']}",
            f"- Featured-pair capability incomparable: {zero_trace['featured_pair_capability_incomparable']}",
            "- Status: review target over simple observed statistics only; no novelty claim over full competency profile.",
            "",
            "## Candidate Evaluation",
            "",
            "| Candidate | Admitted? | Label | Action | Reason |",
            "| --- | --- | --- | --- | --- |",
            *eval_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: an executable way to use N16 as both calibration and absorber "
            "for C(R), while preserving T407 as a simple-statistics surplus "
            "target rather than a novelty claim.",
            "",
            "Does not earn: primary-source-checked Levin/Fields standing, "
            "active-inference mechanism import, novelty over competency/TAME, "
            "region-indexed discriminator success, claim status, public posture, "
            "or cross-repo support.",
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
        json_path = results_dir / "T493-levin-competency-cr-absorber-gate-v0.1.json"
        md_path = results_dir / "T493-levin-competency-cr-absorber-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
