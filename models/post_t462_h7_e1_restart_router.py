"""T463 - post-T462 H7/E1 restart router.

T462 makes the H7 physical-deletion overread audit executable and admits only a
synthetic full-burden H7 review target. T463 keeps that disposition from being
reopened by minor variation. Future H7/E1 work must either route through the
existing E1/E2/E3 gates or bring a named physical-deletion substrate packet that
clears T462's full object.

Run:

    python -m models.post_t462_h7_e1_restart_router --write-results
    python -m pytest tests/test_post_t462_h7_e1_restart_router.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import h7_physical_deletion_overread_absorber as t462


ARTIFACT = "T463-post-t462-h7-e1-restart-router-v0.1"
SOURCE_H7 = "open-problems/h7-physical-deletion-substrate-handoff.md"
SOURCE_T439 = "results/T439-finite-time-catalytic-thermo-witness-gate-v0.1-results.md"
SOURCE_T440 = "results/T440-ideal-limit-sector-lock-routing-gate-v0.1-results.md"
SOURCE_T441 = "results/T441-e1-family-limit-packet-gate-v0.1-results.md"
SOURCE_T461 = "results/T461-e1-local-recovery-family-audition-v0.1-results.md"
SOURCE_T462 = "results/T462-h7-physical-deletion-overread-absorber-v0.1-results.md"
SOURCE_T438 = "results/T438-e2-period-hardness-admission-gate-v0.1-results.md"
SOURCE_T444 = "results/T444-e2-changed-transition-regime-gate-v0.1-results.md"
SOURCE_T451 = "results/T451-d2-temporal-route-demotion-packet-v0.1-results.md"
SOURCE_T436 = "results/T436-quantum-e3-resource-lift-classifier-v0.1-results.md"
SOURCE_T447 = "results/T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "POST_T462_H7_E1_RESTART_ROUTER_BUILT_FULL_BURDEN_ONLY"

HONEST_CEILING = (
    "Routing/admission gate only. T463 does not reopen H7, does not supply "
    "physical-deletion substrate evidence, does not prove a thermodynamic-arrow "
    "theorem, does not prove an E1/E2/E3 theorem, does not move claim status, "
    "and does not authorize public posture."
)

PHYSICAL_RECORD_DELETION = t462.PHYSICAL_RECORD_DELETION


@dataclass(frozen=True)
class RestartProposal:
    proposal_id: str
    description: str
    source: str
    route_family: str
    reverse_edge_class: str = ""
    named_physical_substrate: bool = False
    full_h7_object_frozen: bool = False
    clears_t462_absorber: bool = False
    negative_controls_declared: bool = False
    real_substrate_evidence_present: bool = False
    current_t461_t462_variation: bool = False
    e1_family_limit_packet: bool = False
    e1_locality_only: bool = False
    e2_hardness_packet: bool = False
    e3_exact_no_go_packet: bool = False
    finite_time_or_catalytic_packet: bool = False
    ideal_or_sector_lock_packet: bool = False
    requests_cross_repo_truth: bool = False
    requests_public_posture: bool = False
    requests_claim_promotion: bool = False
    requires_non_github_external_action: bool = False
    synthetic_control_only: bool = False


def _proposal_to_dict(proposal: RestartProposal) -> dict[str, Any]:
    return asdict(proposal)


def _t462_summary() -> dict[str, Any]:
    result = t462.run()
    verdict = result["overall_verdict"]
    return {
        "verdict": verdict["verdict"],
        "admitted_review_target_ids": verdict["admitted_review_target_ids"],
        "synthetic_positive_controls_only": verdict[
            "synthetic_positive_controls_only"
        ],
        "all_h7_reopened_flags_false": verdict["all_h7_reopened_flags_false"],
        "h7_promotion": verdict["h7_promotion"],
        "physical_deletion_evidence": verdict["physical_deletion_evidence"],
    }


def requirement_audit(proposal: RestartProposal) -> dict[str, bool]:
    return {
        "reverse_edge_typed_physical_record_deletion": (
            proposal.reverse_edge_class == PHYSICAL_RECORD_DELETION
        ),
        "named_physical_substrate": proposal.named_physical_substrate,
        "full_h7_object_frozen": proposal.full_h7_object_frozen,
        "clears_t462_absorber": proposal.clears_t462_absorber,
        "negative_controls_declared": proposal.negative_controls_declared,
        "real_substrate_evidence_present": proposal.real_substrate_evidence_present,
        "not_current_t461_t462_variation": (
            not proposal.current_t461_t462_variation
        ),
        "no_cross_repo_truth_request": not proposal.requests_cross_repo_truth,
        "no_public_posture_request": not proposal.requests_public_posture,
        "no_claim_promotion_request": not proposal.requests_claim_promotion,
        "no_non_github_external_action_required": (
            not proposal.requires_non_github_external_action
        ),
    }


def evaluate_proposal(proposal: RestartProposal) -> dict[str, Any]:
    requirements = requirement_audit(proposal)
    missing = [key for key, value in requirements.items() if value is False]
    admitted = False
    h7_reopened = False

    if proposal.requests_public_posture:
        label = "BLOCKED_PUBLIC_POSTURE_REQUEST"
        action = "stop"
        reason = "Public posture movement is outside this repo-local router."
    elif proposal.requests_claim_promotion:
        label = "BLOCKED_CLAIM_PROMOTION_REQUEST"
        action = "stop"
        reason = "T463 is a router and cannot promote H7 or a physics claim."
    elif proposal.requests_cross_repo_truth:
        label = "BLOCKED_CROSS_REPO_TRUTH_REQUEST"
        action = "stop"
        reason = "Cross-repo support cannot substitute for a repo-local H7 packet."
    elif proposal.requires_non_github_external_action:
        label = "BLOCKED_EXTERNAL_ACTION_REQUIRED"
        action = "stop"
        reason = "External substrate investigation or publication needs separate authorization."
    elif proposal.current_t461_t462_variation:
        label = "CLOSED_T461_T462_VARIATION_DO_NOT_REOPEN_H7"
        action = "do_not_reopen"
        reason = "T461/T462 variations are already absorbed unless they supply a new full-burden H7 object."
    elif proposal.e1_locality_only:
        label = "ROUTE_TO_T441_T461_E1_LOCALITY_CONTROL"
        action = "route_to_T441_T461"
        reason = "Locality-depth or family-limit work belongs under the E1 gates, not H7."
    elif proposal.e1_family_limit_packet:
        label = "ROUTE_TO_T441_E1_FAMILY_LIMIT_GATE"
        action = "route_to_T441"
        reason = "E1 packets must clear the family-limit gate before any H7 reading."
    elif proposal.e2_hardness_packet:
        label = "ROUTE_TO_T438_T444_T451_E2_GATES"
        action = "route_to_T438_T444_T451"
        reason = "E2 computational-finality work is not an H7 physical-deletion restart."
    elif proposal.e3_exact_no_go_packet:
        label = "ROUTE_TO_T440_T436_T447_E3_RESOURCE_LIFT_GATES"
        action = "route_to_T440_T436_T447"
        reason = "E3 exact-no-go work needs resource-lift and ideal/sector audits before any H7 reading."
    elif proposal.finite_time_or_catalytic_packet:
        label = "ROUTE_TO_T439_FINITE_TIME_CATALYTIC_GATE"
        action = "route_to_T439"
        reason = "Finite-time and catalytic thermodynamic packets route through T439."
    elif proposal.ideal_or_sector_lock_packet:
        label = "ROUTE_TO_T440_T168_IDEAL_OR_SECTOR_ABSORBER"
        action = "route_to_T440_T168"
        reason = "Ideal limits and sector locks route through T440/T168 before H7."
    elif proposal.reverse_edge_class != PHYSICAL_RECORD_DELETION:
        label = "REJECTED_NOT_PHYSICAL_RECORD_DELETION"
        action = "reject"
        reason = "The reverse edge is not typed as physical_record_deletion."
    elif not proposal.named_physical_substrate:
        label = "REJECTED_NO_NAMED_SUBSTRATE"
        action = "reject"
        reason = "H7 cannot restart without a named physical substrate."
    elif not proposal.full_h7_object_frozen:
        label = "ROUTE_TO_T462_FULL_OBJECT_CHECK"
        action = "route_to_T462"
        reason = "The proposal has not frozen the full minimum H7 object."
    elif not proposal.clears_t462_absorber:
        label = "ROUTE_TO_T462_ABSORBER_BEFORE_RESTART"
        action = "route_to_T462"
        reason = "The packet must clear the T462 absorber before any H7 review."
    elif not proposal.negative_controls_declared:
        label = "REJECTED_NO_NEGATIVE_CONTROLS"
        action = "reject"
        reason = "Negative controls must block idealization, hidden-sink, copy, and access overreads."
    elif not proposal.real_substrate_evidence_present:
        label = "ADMITTED_SYNTHETIC_FULL_BURDEN_TARGET_NO_REOPENING"
        action = "record_synthetic_future_target"
        admitted = True
        reason = (
            "The packet has the full review shape, but only as a synthetic "
            "future target. No real substrate evidence is present."
        )
    else:
        label = "ADMITTED_NAMED_SUBSTRATE_REVIEW_TARGET_NO_PROMOTION"
        action = "admit_future_h7_review_target"
        admitted = True
        reason = (
            "A named substrate packet clears the restart router for future H7 "
            "review only. This still does not promote H7."
        )

    return {
        "proposal_id": proposal.proposal_id,
        "proposal": _proposal_to_dict(proposal),
        "requirement_audit": requirements,
        "missing_requirements": missing,
        "gate_label": label,
        "router_action": action,
        "admitted_future_target": admitted,
        "h7_reopened": h7_reopened,
        "reason": reason,
    }


def proposals() -> tuple[RestartProposal, ...]:
    return (
        RestartProposal(
            proposal_id="t461_locality_depth_reopen_attempt",
            description="Reopen H7 from the T461 local-recovery family by renaming depth as deletion.",
            source=SOURCE_T461,
            route_family="current_h7_e1_stack",
            reverse_edge_class="local_recovery_depth",
            current_t461_t462_variation=True,
            e1_locality_only=True,
        ),
        RestartProposal(
            proposal_id="t462_full_burden_without_real_substrate",
            description="Repeat the T462 synthetic full-burden packet as if it were evidence.",
            source=SOURCE_T462,
            route_family="current_h7_e1_stack",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            full_h7_object_frozen=True,
            clears_t462_absorber=True,
            negative_controls_declared=True,
            current_t461_t462_variation=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="new_e1_family_limit_candidate",
            description="A future E1 family-limit packet with diverging recovery cost.",
            source=SOURCE_T441,
            route_family="e1",
            reverse_edge_class="family_limit_recovery_cost",
            e1_family_limit_packet=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="new_e2_hardness_candidate",
            description="A future computational-finality hardness packet.",
            source="; ".join((SOURCE_T438, SOURCE_T444, SOURCE_T451)),
            route_family="e2",
            reverse_edge_class="computational_recovery_hardness",
            e2_hardness_packet=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="new_e3_exact_no_go_candidate",
            description="A future exact symmetry/no-go packet with reference-resource questions.",
            source="; ".join((SOURCE_T440, SOURCE_T436, SOURCE_T447)),
            route_family="e3",
            reverse_edge_class="symmetry_no_go",
            e3_exact_no_go_packet=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="finite_time_catalytic_candidate",
            description="A finite-time thermodynamic or catalytic deletion packet.",
            source=SOURCE_T439,
            route_family="h7_thermodynamic",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            finite_time_or_catalytic_packet=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="ideal_sector_lock_candidate",
            description="An exact ideal lock or sector restriction read as deletion.",
            source=SOURCE_T440,
            route_family="h7_ideal_or_sector",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            ideal_or_sector_lock_packet=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="access_revocation_reopen_attempt",
            description="An observer access boundary is renamed physical deletion.",
            source=SOURCE_T462,
            route_family="h7",
            reverse_edge_class="access_loss",
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="substrate_name_only_packet",
            description="A named substrate is provided without freezing the full H7 object.",
            source=SOURCE_H7,
            route_family="h7",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="full_object_not_absorber_cleared",
            description="A named substrate freezes the object but has not cleared T462.",
            source=SOURCE_H7,
            route_family="h7",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            full_h7_object_frozen=True,
            negative_controls_declared=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="full_object_missing_negative_controls",
            description="A full H7-shaped packet lacks null controls.",
            source=SOURCE_H7,
            route_family="h7",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            full_h7_object_frozen=True,
            clears_t462_absorber=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="cross_repo_support_shortcut",
            description="Use another repo's result as support for H7 without a local packet.",
            source=SOURCE_TAXONOMY,
            route_family="shortcut",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            full_h7_object_frozen=True,
            clears_t462_absorber=True,
            negative_controls_declared=True,
            requests_cross_repo_truth=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="external_substrate_investigation_shortcut",
            description="Require external literature outreach or publication before local packet review.",
            source=SOURCE_H7,
            route_family="external_action",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            full_h7_object_frozen=True,
            clears_t462_absorber=True,
            negative_controls_declared=True,
            requires_non_github_external_action=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="claim_promotion_shortcut",
            description="Promote H7 based on the existence of the full-burden target shape.",
            source=SOURCE_T462,
            route_family="promotion",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            full_h7_object_frozen=True,
            clears_t462_absorber=True,
            negative_controls_declared=True,
            requests_claim_promotion=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="synthetic_full_burden_restart_target",
            description="A synthetic future-shaped H7 packet with the full T462 object.",
            source=ARTIFACT,
            route_family="h7",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            full_h7_object_frozen=True,
            clears_t462_absorber=True,
            negative_controls_declared=True,
            synthetic_control_only=True,
        ),
        RestartProposal(
            proposal_id="future_named_substrate_review_packet",
            description="A future real substrate packet that would be admitted for review only.",
            source=ARTIFACT,
            route_family="h7",
            reverse_edge_class=PHYSICAL_RECORD_DELETION,
            named_physical_substrate=True,
            full_h7_object_frozen=True,
            clears_t462_absorber=True,
            negative_controls_declared=True,
            real_substrate_evidence_present=True,
            synthetic_control_only=True,
        ),
    )


def run() -> dict[str, Any]:
    evaluations = [evaluate_proposal(proposal) for proposal in proposals()]
    admitted = [item for item in evaluations if item["admitted_future_target"]]
    actual_admitted_now = [
        item
        for item in admitted
        if item["proposal"]["real_substrate_evidence_present"]
        and not item["proposal"]["synthetic_control_only"]
    ]
    routed = [
        item
        for item in evaluations
        if item["router_action"].startswith("route_to_")
    ]
    blocked = [item for item in evaluations if item["router_action"] == "stop"]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "h7_handoff": SOURCE_H7,
            "t439_finite_time_catalytic_gate": SOURCE_T439,
            "t440_ideal_sector_gate": SOURCE_T440,
            "t441_e1_family_gate": SOURCE_T441,
            "t461_locality_control": SOURCE_T461,
            "t462_h7_absorber": SOURCE_T462,
            "t438_period_hardness_gate": SOURCE_T438,
            "t444_changed_transition_gate": SOURCE_T444,
            "t451_d2_route_demotion": SOURCE_T451,
            "t436_e3_resource_lift": SOURCE_T436,
            "t447_e3_exact_no_go": SOURCE_T447,
            "taxonomy_reference": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Convert T462's full-burden H7 disposition into an executable "
            "restart router for H7/E1-adjacent future work."
        ),
        "t462_import_summary": _t462_summary(),
        "restart_requirements": [
            "reverse edge typed as physical_record_deletion",
            "named physical substrate",
            "full T462 H7 object frozen before scoring",
            "T462 absorber cleared",
            "negative controls declared",
            "real substrate evidence before evidential reading",
            "no current T461/T462 minor variation",
            "no cross-repo truth shortcut",
            "no public-posture or claim-promotion shortcut",
            "no non-GitHub external action requirement",
        ],
        "proposal_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_future_target_ids": [
                item["proposal_id"] for item in admitted
            ],
            "actual_substrate_packets_admitted_now": [
                item["proposal_id"] for item in actual_admitted_now
            ],
            "admitted_targets_are_synthetic_or_future_only": all(
                item["proposal"]["synthetic_control_only"] for item in admitted
            ),
            "routed_proposal_ids": [
                {
                    "proposal_id": item["proposal_id"],
                    "action": item["router_action"],
                }
                for item in routed
            ],
            "blocked_proposal_ids": [
                {
                    "proposal_id": item["proposal_id"],
                    "label": item["gate_label"],
                }
                for item in blocked
            ],
            "all_h7_reopened_flags_false": all(
                item["h7_reopened"] is False for item in evaluations
            ),
            "h7_promotion": "none; T463 is a router only",
            "physical_deletion_evidence": (
                "none in this run; no actual substrate packet is supplied"
            ),
            "claim_ledger_update": "none; no claim promotion or demotion",
            "reading": (
                "T463 closes the post-T462 H7/E1 restart surface against minor "
                "variations. T461/T462 reopen attempts do not reopen H7; E1, E2, "
                "E3, finite-time/catalytic, and ideal/sector packets route to "
                "their existing gates; access-loss, name-only, absorber-uncleared, "
                "missing-control, cross-repo, external-action, and promotion "
                "shortcuts are rejected or blocked. Only a full-burden H7 packet "
                "can be admitted as a future review target, with no promotion."
            ),
        },
        "recommended_next": [
            "Use T463 before restarting H7/E1-adjacent work after T462.",
            "Choose a different lane unless a named real physical-deletion substrate packet clears the full T462 object.",
            "Route E1, E2, and E3 candidates through their existing mode gates before any H7 reading.",
        ],
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion or demotion",
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["restart_requirements"]]
    rows = [
        "| {proposal_id} | {action} | {admitted} | {label} | {missing} |".format(
            proposal_id=item["proposal_id"],
            action=item["router_action"],
            admitted="yes" if item["admitted_future_target"] else "no",
            label=item["gate_label"],
            missing=", ".join(item["missing_requirements"]) or "none",
        )
        for item in result["proposal_evaluations"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T463 - Post-T462 H7/E1 Restart Router - v0.1 results",
            "",
            "> Routing/admission gate only. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T463-post-t462-h7-e1-restart-router.md`",
            "- Model: `models/post_t462_h7_e1_restart_router.py`",
            "- Tests: `tests/test_post_t462_h7_e1_restart_router.py`",
            "- Artifact JSON: `results/T463-post-t462-h7-e1-restart-router-v0.1.json`",
            "- Sources: H7 handoff, T439, T440, T441, T461, T462, E2 gates, E3 gates, and the taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Restart Requirements",
            "",
            *requirements,
            "",
            "## Proposal Evaluation",
            "",
            "| proposal | router action | admitted? | gate label | missing requirements |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Route Disposition",
            "",
            "- T461/T462 minor variations do not reopen H7.",
            "- E1, E2, and E3 candidates route through existing mode gates first.",
            "- Cross-repo, external-action, public-posture, and claim-promotion shortcuts block.",
            "- Full-burden H7 packets are admitted only as review targets, not evidence or promotion.",
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable router for post-T462 H7/E1-adjacent work.",
            "",
            "Does not earn: H7 promotion, physical-deletion substrate evidence, "
            "an E1 theorem, an E2 theorem, an E3 theorem, a thermodynamic-arrow "
            "theorem, stochastic-thermodynamic theorem, claim-ledger movement, "
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
        json_path = results_dir / "T463-post-t462-h7-e1-restart-router-v0.1.json"
        md_path = results_dir / "T463-post-t462-h7-e1-restart-router-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
