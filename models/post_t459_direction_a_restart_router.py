"""T460 - post-T459 Direction-A restart router.

T459 closes the current integrated E3-region packet class as a route-level
negative guardrail. This router keeps that closure executable: future Direction-A
work must not reopen the T454-T459 class by minor variation. It must either
bring a genuinely new region packet class with a predeclared independent theorem
that clears T457, T458, and T459 together, or route through another existing mode
gate before returning to Direction A.

Run:

    python -m models.post_t459_direction_a_restart_router --write-results
    python -m pytest tests/test_post_t459_direction_a_restart_router.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import policy_independent_theorem_supply_gate as t459


ARTIFACT = "T460-post-t459-direction-a-restart-router-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T457 = "results/T457-description-completion-squeeze-gate-v0.1-results.md"
SOURCE_T458 = "results/T458-reference-policy-invariance-gate-v0.1-results.md"
SOURCE_T459 = "results/T459-policy-independent-theorem-supply-gate-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "POST_T459_DIRECTION_A_RESTART_ROUTER_BUILT_CURRENT_ROUTE_CLOSED_NEW_CLASS_ONLY"

HONEST_CEILING = (
    "Routing/admission gate only. T460 does not prove a region-indexed "
    "discriminator, substrate law, quantum physics theorem, WAY theorem, "
    "GU/TaF adapter, claim support, public posture, hard-policy move, or "
    "cross-repo support. It preserves T459's route-level closure of the "
    "current integrated E3-region packet class and admits only synthetic "
    "future restart targets."
)


@dataclass(frozen=True)
class RestartCandidate:
    candidate_id: str
    description: str
    source: str
    route_family: str
    region_packet_present: bool
    new_packet_class_declared: bool
    uses_current_t454_t459_class: bool
    independent_theorem_supplied: bool
    theorem_declared_before_pair: bool
    theorem_targets_named_completion: bool
    theorem_makes_completion_nonadmissible: bool
    clears_description_completion_blocker: bool
    handles_reference_policy_variants: bool
    clears_t457_t458_t459_together: bool
    operation_resource_class_frozen: bool = True
    a2_resource_lift_audited: bool = True
    negative_control_present: bool = True
    requests_cross_repo_truth: bool = False
    requests_public_posture: bool = False
    existing_mode_gate: str = ""
    synthetic_control_only: bool = False


def _candidate_to_dict(candidate: RestartCandidate) -> dict[str, Any]:
    return asdict(candidate)


def _t459_summary() -> dict[str, Any]:
    result = t459.run()
    verdict = result["overall_verdict"]
    return {
        "verdict": verdict["verdict"],
        "current_route_label": verdict["current_route_label"],
        "current_route_demoted_to_negative_guardrail": verdict[
            "current_route_demoted_to_negative_guardrail"
        ],
        "route_demotion_scope": verdict["route_demotion_scope"],
        "current_artifacts_admitted_for_stronger_posture": verdict[
            "current_artifacts_admitted_for_stronger_posture"
        ],
    }


def requirement_audit(candidate: RestartCandidate) -> dict[str, bool]:
    return {
        "region_packet_present": candidate.region_packet_present,
        "new_packet_class_declared": candidate.new_packet_class_declared,
        "does_not_use_current_t454_t459_class": (
            not candidate.uses_current_t454_t459_class
        ),
        "independent_theorem_supplied": candidate.independent_theorem_supplied,
        "theorem_declared_before_pair": candidate.theorem_declared_before_pair,
        "theorem_targets_named_completion": (
            candidate.theorem_targets_named_completion
        ),
        "theorem_makes_completion_nonadmissible": (
            candidate.theorem_makes_completion_nonadmissible
        ),
        "clears_description_completion_blocker": (
            candidate.clears_description_completion_blocker
        ),
        "handles_reference_policy_variants": (
            candidate.handles_reference_policy_variants
        ),
        "clears_t457_t458_t459_together": (
            candidate.clears_t457_t458_t459_together
        ),
        "operation_resource_class_frozen": (
            candidate.operation_resource_class_frozen
        ),
        "a2_resource_lift_audited": candidate.a2_resource_lift_audited,
        "negative_control_present": candidate.negative_control_present,
        "no_cross_repo_truth_request": not candidate.requests_cross_repo_truth,
        "no_public_posture_request": not candidate.requests_public_posture,
    }


def evaluate_candidate(candidate: RestartCandidate) -> dict[str, Any]:
    requirements = requirement_audit(candidate)
    missing = [key for key, value in requirements.items() if value is False]
    admitted = False

    if candidate.requests_public_posture:
        label = "BLOCKED_PUBLIC_POSTURE_REQUEST"
        action = "stop"
        reason = "Public posture movement is outside this repo-local router."
    elif candidate.requests_cross_repo_truth:
        label = "BLOCKED_CROSS_REPO_TRUTH_REQUEST"
        action = "stop"
        reason = "Cross-repo truth cannot be imported or asserted by this repo-local run."
    elif candidate.route_family == "current_integrated_e3_region":
        label = "CLOSED_CURRENT_T454_T459_CLASS_NEGATIVE_GUARDRAIL"
        action = "do_not_reopen"
        reason = "T459 already demoted this packet class to route-level negative guardrail."
    elif candidate.route_family == "existing_mode_gate":
        label = "ROUTE_TO_EXISTING_MODE_GATE_NOT_DIRECTION_A_RESTART"
        action = f"route_to_{candidate.existing_mode_gate}"
        reason = "The candidate belongs under an existing E1/E2/E3 mode gate before any Direction-A restart."
    elif not candidate.region_packet_present:
        label = "NOT_ADMITTED_NO_REGION_PACKET"
        action = "reject"
        reason = "A theorem or method note without a region-indexed packet cannot restart Direction A."
    elif not candidate.new_packet_class_declared:
        label = "NOT_ADMITTED_NO_NEW_PACKET_CLASS"
        action = "reject"
        reason = "Minor variations of the closed class do not restart the route."
    elif candidate.uses_current_t454_t459_class:
        label = "NOT_ADMITTED_CURRENT_CLASS_VARIATION"
        action = "reject"
        reason = "The candidate still uses the current T454-T459 packet class."
    elif not candidate.independent_theorem_supplied:
        label = "NOT_ADMITTED_T459_NO_INDEPENDENT_THEOREM"
        action = "reject"
        reason = "The candidate does not supply the independent theorem T459 requires."
    elif not candidate.theorem_declared_before_pair:
        label = "NOT_ADMITTED_POST_HOC_THEOREM"
        action = "reject"
        reason = "The theorem or theorem scope is selected after pair construction."
    elif not candidate.theorem_targets_named_completion:
        label = "NOT_ADMITTED_THEOREM_NOT_TIED_TO_COMPLETION"
        action = "reject"
        reason = "The theorem does not target the completion that restores factorization."
    elif not candidate.theorem_makes_completion_nonadmissible:
        label = "NOT_ADMITTED_COMPLETION_NOT_PRECLUDED"
        action = "reject"
        reason = "The theorem does not make the named completion physically non-admissible."
    elif not candidate.clears_description_completion_blocker:
        label = "NOT_ADMITTED_T457_DESCRIPTION_COMPLETION_BLOCKER"
        action = "reject"
        reason = "The candidate still factors through admitted description."
    elif not candidate.handles_reference_policy_variants:
        label = "NOT_ADMITTED_T458_REFERENCE_POLICY_FRAGILITY"
        action = "reject"
        reason = "Reference variants still restore completion or route away."
    elif not candidate.clears_t457_t458_t459_together:
        label = "NOT_ADMITTED_T456_BLOCKER_SET_UNCLEARED"
        action = "reject"
        reason = "The candidate does not clear the T457/T458/T459 blocker set together."
    elif not candidate.operation_resource_class_frozen:
        label = "NOT_ADMITTED_OPERATION_RESOURCE_CLASS_UNFROZEN"
        action = "reject"
        reason = "The operation/resource class must be frozen before scoring."
    elif not candidate.a2_resource_lift_audited:
        label = "NOT_ADMITTED_A2_RESOURCE_LIFT_UNAUDITED"
        action = "reject"
        reason = "A2 reference/resource completion must be audited."
    elif not candidate.negative_control_present:
        label = "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
        action = "reject"
        reason = "The candidate lacks a negative control."
    else:
        admitted = True
        label = "ADMITTED_NEW_DIRECTION_A_RESTART_TARGET_NO_PROMOTION"
        action = "admit_future_review_target"
        reason = "Synthetic new packet class clears the restart router without claim promotion."

    return {
        "candidate_id": candidate.candidate_id,
        "candidate": _candidate_to_dict(candidate),
        "requirement_audit": requirements,
        "missing_requirements": missing,
        "gate_label": label,
        "router_action": action,
        "admitted_future_target": admitted,
        "reason": reason,
    }


def candidates() -> tuple[RestartCandidate, ...]:
    current_sources = "; ".join((SOURCE_T457, SOURCE_T458, SOURCE_T459))
    return (
        RestartCandidate(
            candidate_id="current_t454_t459_integrated_route",
            description="The route class closed by T459.",
            source=current_sources,
            route_family="current_integrated_e3_region",
            region_packet_present=True,
            new_packet_class_declared=False,
            uses_current_t454_t459_class=True,
            independent_theorem_supplied=False,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=False,
            theorem_makes_completion_nonadmissible=False,
            clears_description_completion_blocker=False,
            handles_reference_policy_variants=False,
            clears_t457_t458_t459_together=False,
        ),
        RestartCandidate(
            candidate_id="minor_boundary_resource_variation",
            description="A renamed boundary-resource packet inside the same T454-T459 class.",
            source=SOURCE_T459,
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=False,
            uses_current_t454_t459_class=True,
            independent_theorem_supplied=False,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=False,
            theorem_makes_completion_nonadmissible=False,
            clears_description_completion_blocker=False,
            handles_reference_policy_variants=False,
            clears_t457_t458_t459_together=False,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="theorem_without_region_packet",
            description="A theorem-shaped note with no region-indexed packet.",
            source=ARTIFACT,
            route_family="direction_a_restart",
            region_packet_present=False,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            clears_description_completion_blocker=True,
            handles_reference_policy_variants=True,
            clears_t457_t458_t459_together=True,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="new_packet_without_independent_theorem",
            description="A new packet fixture that lacks an independent theorem.",
            source=ARTIFACT,
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=False,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=False,
            theorem_makes_completion_nonadmissible=False,
            clears_description_completion_blocker=False,
            handles_reference_policy_variants=False,
            clears_t457_t458_t459_together=False,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="post_hoc_new_packet_theorem",
            description="A new packet whose theorem is selected after the witness pair.",
            source=ARTIFACT,
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=True,
            theorem_declared_before_pair=False,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            clears_description_completion_blocker=True,
            handles_reference_policy_variants=True,
            clears_t457_t458_t459_together=True,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="new_packet_description_factorizes",
            description="A new packet that still factors through admitted description.",
            source=SOURCE_T457,
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            clears_description_completion_blocker=False,
            handles_reference_policy_variants=True,
            clears_t457_t458_t459_together=False,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="new_packet_reference_policy_fragile",
            description="A new packet that leaves cyclic/consumed/ideal references unhandled.",
            source=SOURCE_T458,
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            clears_description_completion_blocker=True,
            handles_reference_policy_variants=False,
            clears_t457_t458_t459_together=False,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="untargeted_independent_theorem_packet",
            description="A new theorem packet not tied to the completion that restores factorization.",
            source=SOURCE_T459,
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=False,
            theorem_makes_completion_nonadmissible=True,
            clears_description_completion_blocker=True,
            handles_reference_policy_variants=True,
            clears_t457_t458_t459_together=False,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="e1_family_limit_packet",
            description="An E1 family-limit packet candidate, routed to the T441 gate first.",
            source="results/T441-e1-family-limit-packet-gate-v0.1-results.md",
            route_family="existing_mode_gate",
            region_packet_present=False,
            new_packet_class_declared=False,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=False,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=False,
            theorem_makes_completion_nonadmissible=False,
            clears_description_completion_blocker=False,
            handles_reference_policy_variants=False,
            clears_t457_t458_t459_together=False,
            existing_mode_gate="T441_E1_family_limit_packet_gate",
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="e2_changed_transition_packet",
            description="An E2 changed-transition packet candidate, routed to T438/T444 first.",
            source="results/T444-e2-changed-transition-regime-gate-v0.1-results.md",
            route_family="existing_mode_gate",
            region_packet_present=False,
            new_packet_class_declared=False,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=False,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=False,
            theorem_makes_completion_nonadmissible=False,
            clears_description_completion_blocker=False,
            handles_reference_policy_variants=False,
            clears_t457_t458_t459_together=False,
            existing_mode_gate="T438_T444_E2_packet_gates",
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="cross_repo_adapter_shortcut",
            description="A shortcut that asks GU/TaF cross-repo support to stand in for theorem supply.",
            source="open-problems/e3-admissibility-adapter-gu-taf.md",
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            clears_description_completion_blocker=True,
            handles_reference_policy_variants=True,
            clears_t457_t458_t459_together=True,
            requests_cross_repo_truth=True,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="synthetic_new_independent_theorem_packet",
            description="A future-shaped new Direction-A packet class clearing T457, T458, and T459 together.",
            source=ARTIFACT,
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            clears_description_completion_blocker=True,
            handles_reference_policy_variants=True,
            clears_t457_t458_t459_together=True,
            synthetic_control_only=True,
        ),
        RestartCandidate(
            candidate_id="synthetic_missing_negative_control",
            description="A future-shaped new packet missing its negative control.",
            source=ARTIFACT,
            route_family="direction_a_restart",
            region_packet_present=True,
            new_packet_class_declared=True,
            uses_current_t454_t459_class=False,
            independent_theorem_supplied=True,
            theorem_declared_before_pair=True,
            theorem_targets_named_completion=True,
            theorem_makes_completion_nonadmissible=True,
            clears_description_completion_blocker=True,
            handles_reference_policy_variants=True,
            clears_t457_t458_t459_together=True,
            negative_control_present=False,
            synthetic_control_only=True,
        ),
    )


def run() -> dict[str, Any]:
    evaluations = [evaluate_candidate(candidate) for candidate in candidates()]
    admitted = [item for item in evaluations if item["admitted_future_target"]]
    current = next(
        item
        for item in evaluations
        if item["candidate_id"] == "current_t454_t459_integrated_route"
    )
    routed = [
        item
        for item in evaluations
        if item["gate_label"] == "ROUTE_TO_EXISTING_MODE_GATE_NOT_DIRECTION_A_RESTART"
    ]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t457": SOURCE_T457,
            "t458": SOURCE_T458,
            "t459": SOURCE_T459,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Convert T459's route-level demotion into an executable restart "
            "router for future Direction-A work."
        ),
        "t459_import_summary": _t459_summary(),
        "candidate_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "current_route_label": current["gate_label"],
            "current_route_closed": True,
            "current_route_action": current["router_action"],
            "admitted_candidate_ids": [item["candidate_id"] for item in admitted],
            "admitted_candidates_are_synthetic_only": all(
                item["candidate"]["synthetic_control_only"] for item in admitted
            ),
            "routed_candidate_ids": [
                {
                    "candidate_id": item["candidate_id"],
                    "action": item["router_action"],
                }
                for item in routed
            ],
            "current_artifacts_admitted_for_stronger_posture": False,
            "route_closure_scope": "current integrated E3-region packet class only",
            "region_discriminator_success": False,
            "claim_ledger_update": "none; no claim promotion or claim demotion",
            "reading": (
                "T460 makes the post-T459 route decision executable. The current "
                "T454-T459 integrated E3-region packet class and minor variations "
                "are closed as Direction-A restart candidates. E1/E2-style "
                "alternatives route to their existing mode gates first. Only a "
                "new region packet class with a predeclared independent theorem "
                "that targets the named completion, precludes it, clears "
                "description completion, and handles or precludes reference "
                "variants is admitted, and only as a synthetic future review target."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion or claim demotion",
        "recommended_next": [
            "Use T460 before reopening Direction A after T459.",
            "Do not rebuild the T454-T459 integrated E3-region packet class by minor variation.",
            "Choose a different lane unless a new packet class brings an independent theorem clearing T457, T458, and T459 together.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    rows = [
        "| {candidate_id} | {action} | {admitted} | {label} | {missing} |".format(
            candidate_id=item["candidate_id"],
            action=item["router_action"],
            admitted="yes" if item["admitted_future_target"] else "no",
            label=item["gate_label"],
            missing=", ".join(item["missing_requirements"]) or "none",
        )
        for item in result["candidate_evaluations"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T460 - Post-T459 Direction-A Restart Router - v0.1 results",
            "",
            "> Routing/admission gate only. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T460-post-t459-direction-a-restart-router.md`",
            "- Model: `models/post_t459_direction_a_restart_router.py`",
            "- Tests: `tests/test_post_t459_direction_a_restart_router.py`",
            "- Artifact JSON: `results/T460-post-t459-direction-a-restart-router-v0.1.json`",
            "- Sources: T457, T458, T459, the region-indexed capability discriminator, and the taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Candidate Evaluation",
            "",
            "| candidate | router action | admitted? | gate label | missing requirements |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Route Disposition",
            "",
            "- Current route status: `closed_current_class_negative_guardrail`.",
            f"- Scope: `{verdict['route_closure_scope']}`.",
            "- Claim ledger movement: none.",
            "- Public posture movement: none.",
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable router for post-T459 Direction-A work. It blocks "
            "minor variations of the closed packet class and separates true "
            "Direction-A restarts from adjacent E1/E2 mode-gate work.",
            "",
            "Does not earn: a region-indexed discriminator success, real "
            "substrate law, quantum physics theorem, WAY theorem, GU/TaF adapter, "
            "claim-ledger movement, TESTS or roadmap movement, public posture, "
            "hard-policy movement, or cross-repo support.",
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
        json_path = results_dir / "T460-post-t459-direction-a-restart-router-v0.1.json"
        md_path = results_dir / "T460-post-t459-direction-a-restart-router-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
