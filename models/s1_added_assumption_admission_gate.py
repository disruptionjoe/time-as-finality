"""T464 - S1 added-assumption admission gate.

T223 downgraded the finite finality-colimit route for S1 to
requires_added_assumption: the uniform finite ordinal ensemble does not
concentrate on manifoldlike causal sets through n=8, and later selected
controls do not reverse that finite no-go. T464 makes the next burden
executable. Future S1 work must declare the added assumption it wants to use
before scoring, show why it is natural rather than tail-tuned, and preserve the
T126/T156/T159/T223 guardrails before it can become a review target.

Run:

    python -m models.s1_added_assumption_admission_gate --write-results
    python -m pytest tests/test_s1_added_assumption_admission_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T464-s1-added-assumption-admission-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/spacetime-as-finality-colimit.md"
SOURCE_T223 = "results/t54-ordinal-scaling-decisive-v0.1-results.md"
SOURCE_T223_SPEC = "tests/T223-t54-ordinal-scaling-decisive-verdict.md"
SOURCE_S1 = "claims/S1-spacetime-consensus-envelope.md"
SOURCE_T126 = "results/finality-colimit-causal-set-embeddability-v0.1-results.md"
SOURCE_T156 = "results/t54-ordering-fraction-bridge-v0.1-results.md"
SOURCE_T159 = "results/t54-interval-jackknife-screen-v0.1-results.md"

VERDICT = "S1_ADDED_ASSUMPTION_ADMISSION_GATE_BUILT_NO_S1_PROMOTION"

ASSUMPTION_TYPES = {
    "non_uniform_measure",
    "selection_rule",
    "sprinkling_law",
    "continuum_bridge",
}

HONEST_CEILING = (
    "Admission gate only. T464 does not reverse T223, does not promote S1, "
    "does not derive spacetime, manifoldlikeness, dimension, Lorentzian metric, "
    "sprinkling, locality, GR, QFT, or a continuum theorem, and does not move "
    "claim status or public posture."
)


@dataclass(frozen=True)
class S1AssumptionProposal:
    proposal_id: str
    description: str
    source: str
    assumption_type: str = ""
    post_t223_context_declared: bool = False
    added_assumption_declared: bool = False
    predeclared_before_scoring: bool = False
    finality_native_or_external_justified: bool = False
    noncircular_not_tail_tuned: bool = False
    finite_audit_on_existing_screens: bool = False
    tested_across_multiple_sizes_or_limit: bool = False
    nonvanishing_weight_or_limit_claim: bool = False
    compatible_with_t126_t156_t159: bool = False
    lorentzian_constraints_named: bool = False
    no_overclaim_language: bool = True
    uniform_ordinal_repeat: bool = False
    finite_enumeration_only: bool = False
    selected_survivor_only: bool = False
    changes_screen_after_t223: bool = False
    requests_t223_reversal: bool = False
    requests_claim_promotion: bool = False
    requests_public_posture: bool = False
    requires_non_github_external_action: bool = False
    synthetic_control_only: bool = False


def _proposal_to_dict(proposal: S1AssumptionProposal) -> dict[str, Any]:
    return asdict(proposal)


def requirement_audit(proposal: S1AssumptionProposal) -> dict[str, bool]:
    return {
        "post_t223_context_declared": proposal.post_t223_context_declared,
        "added_assumption_type_supported": proposal.assumption_type
        in ASSUMPTION_TYPES,
        "added_assumption_declared": proposal.added_assumption_declared,
        "predeclared_before_scoring": proposal.predeclared_before_scoring,
        "finality_native_or_external_justified": (
            proposal.finality_native_or_external_justified
        ),
        "noncircular_not_tail_tuned": proposal.noncircular_not_tail_tuned,
        "finite_audit_on_existing_screens": proposal.finite_audit_on_existing_screens,
        "tested_across_multiple_sizes_or_limit": (
            proposal.tested_across_multiple_sizes_or_limit
        ),
        "nonvanishing_weight_or_limit_claim": (
            proposal.nonvanishing_weight_or_limit_claim
        ),
        "compatible_with_t126_t156_t159": (
            proposal.compatible_with_t126_t156_t159
        ),
        "lorentzian_constraints_named": proposal.lorentzian_constraints_named,
        "no_overclaim_language": proposal.no_overclaim_language,
        "no_screen_drift_after_t223": not proposal.changes_screen_after_t223,
        "no_t223_reversal_request": not proposal.requests_t223_reversal,
        "no_claim_promotion_request": not proposal.requests_claim_promotion,
        "no_public_posture_request": not proposal.requests_public_posture,
        "no_non_github_external_action_required": (
            not proposal.requires_non_github_external_action
        ),
    }


def evaluate_proposal(proposal: S1AssumptionProposal) -> dict[str, Any]:
    requirements = requirement_audit(proposal)
    missing = [key for key, value in requirements.items() if value is False]
    admitted = False

    if proposal.requests_public_posture:
        label = "BLOCKED_PUBLIC_POSTURE_REQUEST"
        action = "stop"
        reason = "Public posture movement is outside this repo-local gate."
    elif proposal.requests_claim_promotion:
        label = "BLOCKED_CLAIM_PROMOTION_REQUEST"
        action = "stop"
        reason = "T464 is an admission gate and cannot promote S1."
    elif proposal.requires_non_github_external_action:
        label = "BLOCKED_EXTERNAL_ACTION_REQUIRED"
        action = "stop"
        reason = "External publication, outreach, or data gathering needs separate authorization."
    elif not proposal.no_overclaim_language:
        label = "BLOCKED_SPACETIME_OVERCLAIM"
        action = "stop"
        reason = "The proposal overclaims spacetime, dimension, Lorentzian, GR, QFT, or continuum content."
    elif proposal.requests_t223_reversal:
        label = "REJECTED_T223_REVERSAL_REQUEST"
        action = "reject"
        reason = "T464 does not reverse T223; it only admits added-assumption review targets."
    elif proposal.uniform_ordinal_repeat or proposal.finite_enumeration_only:
        label = "REJECTED_CLOSED_BY_T223_FINITE_ENSEMBLE_NO_GO"
        action = "reject"
        reason = "More uniform finite ordinal enumeration is closed as an S1 restart route by T223."
    elif proposal.selected_survivor_only:
        label = "REJECTED_SELECTED_SURVIVOR_NO_CONCENTRATION"
        action = "reject"
        reason = "A selected positive survivor or control does not supply a natural measure or concentration result."
    elif proposal.changes_screen_after_t223:
        label = "REJECTED_SCREEN_DRIFT_AFTER_T223"
        action = "reject"
        reason = "Changing the T126/T156/T159 screens after T223 is target drift, not an added assumption."
    elif proposal.assumption_type and proposal.assumption_type not in ASSUMPTION_TYPES:
        label = "REJECTED_UNSUPPORTED_ASSUMPTION_TYPE"
        action = "reject"
        reason = "The proposal does not name one of the admitted post-T223 assumption families."
    elif not proposal.post_t223_context_declared:
        label = "REJECTED_NO_T223_CONTEXT"
        action = "reject"
        reason = "The proposal must explicitly inherit T223's finite no-go and S1 status."
    elif not proposal.added_assumption_declared or not proposal.assumption_type:
        label = "REJECTED_NO_ADDED_ASSUMPTION"
        action = "reject"
        reason = "The proposal does not declare the added measure, selection, sprinkling, or bridge assumption."
    elif not proposal.predeclared_before_scoring:
        label = "REJECTED_POST_HOC_ASSUMPTION"
        action = "reject"
        reason = "The added assumption is selected after seeing the survivor tail."
    elif not proposal.finality_native_or_external_justified:
        label = "REJECTED_NO_NATURALITY_OR_NATIVE_JUSTIFICATION"
        action = "reject"
        reason = "The assumption is not justified by finality structure or an external neighboring theory."
    elif not proposal.noncircular_not_tail_tuned:
        label = "REJECTED_CIRCULAR_TAIL_TUNING"
        action = "reject"
        reason = "The measure or selection rule is tuned to privilege the known T223 tail."
    elif not proposal.finite_audit_on_existing_screens:
        label = "REJECTED_NO_FINITE_AUDIT_HANDLE"
        action = "reject"
        reason = "The assumption has no finite audit on the existing T126/T156/T159/T223 pipeline."
    elif not proposal.tested_across_multiple_sizes_or_limit:
        label = "REJECTED_NO_SIZE_OR_LIMIT_TEST"
        action = "reject"
        reason = "The proposal has not been tested across multiple sizes or a declared limit."
    elif not proposal.nonvanishing_weight_or_limit_claim:
        label = "REJECTED_NO_NONVANISHING_WEIGHT_OR_LIMIT_CLAIM"
        action = "reject"
        reason = "The assumption does not assert nonvanishing survivor weight or a real limit theorem target."
    elif not proposal.compatible_with_t126_t156_t159:
        label = "REJECTED_NOT_COMPATIBLE_WITH_EXISTING_SCREENS"
        action = "reject"
        reason = "The assumption does not preserve the existing finite guardrail screens."
    elif not proposal.lorentzian_constraints_named:
        label = "REJECTED_NO_LORENTZIAN_CONSTRAINT_TARGETS"
        action = "reject"
        reason = "The proposal does not name the causal, metric, covariance, locality, or embedding constraints it must later face."
    else:
        label = "ADMITTED_ADDED_ASSUMPTION_REVIEW_TARGET_NO_PROMOTION"
        action = "admit_future_s1_review_target"
        admitted = True
        reason = (
            "The proposal has the post-T223 review shape: a predeclared added "
            "assumption with naturality, non-circularity, finite audit, "
            "multi-size or limit evidence, screen compatibility, and no "
            "spacetime overclaim. Admission is review-only."
        )

    return {
        "proposal_id": proposal.proposal_id,
        "proposal": _proposal_to_dict(proposal),
        "requirement_audit": requirements,
        "missing_requirements": missing,
        "gate_label": label,
        "gate_action": action,
        "admitted_future_target": admitted,
        "s1_promoted": False,
        "t223_reversed": False,
        "reason": reason,
    }


def proposals() -> tuple[S1AssumptionProposal, ...]:
    return (
        S1AssumptionProposal(
            proposal_id="more_uniform_ordinal_enumeration",
            description="Continue finite uniform ordinal enumeration as if one more size can reopen S1.",
            source=SOURCE_T223,
            uniform_ordinal_repeat=True,
            finite_enumeration_only=True,
            post_t223_context_declared=True,
        ),
        S1AssumptionProposal(
            proposal_id="selected_nine_event_survivor_shortcut",
            description="Use a selected finite survivor or positive control as spacetime evidence.",
            source=SOURCE_T223,
            selected_survivor_only=True,
            post_t223_context_declared=True,
        ),
        S1AssumptionProposal(
            proposal_id="screen_redefinition_after_tail",
            description="Change the screening target after T223 to make the known tail look typical.",
            source=SOURCE_T223_SPEC,
            changes_screen_after_t223=True,
            post_t223_context_declared=True,
            added_assumption_declared=True,
            assumption_type="selection_rule",
        ),
        S1AssumptionProposal(
            proposal_id="no_added_assumption_packet",
            description="Restate S1 after T223 with no measure, selection, sprinkling, or continuum assumption.",
            source=SOURCE_OPEN_PROBLEM,
            post_t223_context_declared=True,
        ),
        S1AssumptionProposal(
            proposal_id="tail_tuned_non_uniform_measure",
            description="Assign weight only to the known T223 survivors without independent justification.",
            source=SOURCE_T223,
            assumption_type="non_uniform_measure",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=False,
        ),
        S1AssumptionProposal(
            proposal_id="post_hoc_selection_rule",
            description="Choose a finality-colimit selection rule after inspecting the survivor classes.",
            source=SOURCE_T223,
            assumption_type="selection_rule",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=False,
            finality_native_or_external_justified=True,
        ),
        S1AssumptionProposal(
            proposal_id="measure_without_finite_audit",
            description="Declare a non-uniform measure but give no finite audit on the existing screens.",
            source=SOURCE_OPEN_PROBLEM,
            assumption_type="non_uniform_measure",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=True,
        ),
        S1AssumptionProposal(
            proposal_id="single_size_positive_measure",
            description="A measure looks good at one finite size only.",
            source=SOURCE_T223,
            assumption_type="non_uniform_measure",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=True,
            finite_audit_on_existing_screens=True,
        ),
        S1AssumptionProposal(
            proposal_id="sprinkling_law_without_lorentz_targets",
            description="A proposed random-sprinkling law has finite tests but no named Lorentzian constraints.",
            source=SOURCE_OPEN_PROBLEM,
            assumption_type="sprinkling_law",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=True,
            finite_audit_on_existing_screens=True,
            tested_across_multiple_sizes_or_limit=True,
            nonvanishing_weight_or_limit_claim=True,
            compatible_with_t126_t156_t159=True,
        ),
        S1AssumptionProposal(
            proposal_id="continuum_bridge_overclaim",
            description="A continuum bridge is presented as deriving spacetime from TaF.",
            source=SOURCE_OPEN_PROBLEM,
            assumption_type="continuum_bridge",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=True,
            finite_audit_on_existing_screens=True,
            tested_across_multiple_sizes_or_limit=True,
            nonvanishing_weight_or_limit_claim=True,
            compatible_with_t126_t156_t159=True,
            lorentzian_constraints_named=True,
            no_overclaim_language=False,
        ),
        S1AssumptionProposal(
            proposal_id="claim_promotion_shortcut",
            description="Promote S1 because an added-assumption gate exists.",
            source=SOURCE_S1,
            assumption_type="non_uniform_measure",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=True,
            finite_audit_on_existing_screens=True,
            tested_across_multiple_sizes_or_limit=True,
            nonvanishing_weight_or_limit_claim=True,
            compatible_with_t126_t156_t159=True,
            lorentzian_constraints_named=True,
            requests_claim_promotion=True,
            synthetic_control_only=True,
        ),
        S1AssumptionProposal(
            proposal_id="external_publication_shortcut",
            description="Require a public paper or external write before local finite audit.",
            source=SOURCE_OPEN_PROBLEM,
            assumption_type="continuum_bridge",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=True,
            finite_audit_on_existing_screens=True,
            tested_across_multiple_sizes_or_limit=True,
            nonvanishing_weight_or_limit_claim=True,
            compatible_with_t126_t156_t159=True,
            lorentzian_constraints_named=True,
            requires_non_github_external_action=True,
            synthetic_control_only=True,
        ),
        S1AssumptionProposal(
            proposal_id="synthetic_natural_measure_review_target",
            description=(
                "Synthetic future target: a non-uniform measure predeclared "
                "from finality-native data, audited across sizes, and not "
                "tuned to the known tail."
            ),
            source=ARTIFACT,
            assumption_type="non_uniform_measure",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=True,
            finite_audit_on_existing_screens=True,
            tested_across_multiple_sizes_or_limit=True,
            nonvanishing_weight_or_limit_claim=True,
            compatible_with_t126_t156_t159=True,
            lorentzian_constraints_named=True,
            synthetic_control_only=True,
        ),
        S1AssumptionProposal(
            proposal_id="synthetic_continuum_bridge_review_target",
            description=(
                "Synthetic future target: a continuum bridge with finite "
                "approximant audits, a declared limit object, and named "
                "Lorentzian constraints."
            ),
            source=ARTIFACT,
            assumption_type="continuum_bridge",
            post_t223_context_declared=True,
            added_assumption_declared=True,
            predeclared_before_scoring=True,
            finality_native_or_external_justified=True,
            noncircular_not_tail_tuned=True,
            finite_audit_on_existing_screens=True,
            tested_across_multiple_sizes_or_limit=True,
            nonvanishing_weight_or_limit_claim=True,
            compatible_with_t126_t156_t159=True,
            lorentzian_constraints_named=True,
            synthetic_control_only=True,
        ),
    )


def run() -> dict[str, Any]:
    evaluations = [evaluate_proposal(proposal) for proposal in proposals()]
    admitted = [item for item in evaluations if item["admitted_future_target"]]
    blocked = [item for item in evaluations if item["gate_action"] == "stop"]
    rejected = [item for item in evaluations if item["gate_action"] == "reject"]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "s1_claim": SOURCE_S1,
            "t223_results": SOURCE_T223,
            "t223_spec": SOURCE_T223_SPEC,
            "t126_screen": SOURCE_T126,
            "t156_screen": SOURCE_T156,
            "t159_screen": SOURCE_T159,
        },
        "purpose": (
            "Convert T223's requires_added_assumption burden into an executable "
            "admission gate for future S1 finite-colimit work."
        ),
        "admission_requirements": [
            "T223 finite no-go and S1 requires_added_assumption status inherited",
            "added assumption type declared: non_uniform_measure, selection_rule, sprinkling_law, or continuum_bridge",
            "assumption predeclared before survivor scoring",
            "finality-native naturality or external-theory justification supplied",
            "non-circular and not tuned to the known T223 survivor tail",
            "finite audit handle on the existing T126/T156/T159/T223 pipeline",
            "tested across multiple finite sizes or tied to a declared limit",
            "nonvanishing survivor weight, concentration, or real limit theorem target stated",
            "compatible with existing guardrail screens and no target drift",
            "later Lorentzian causal, metric, covariance, locality, or embedding constraints named",
            "no spacetime, manifoldlikeness, dimension, GR/QFT, continuum, claim-promotion, or public-posture overclaim",
        ],
        "proposal_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_future_target_ids": [
                item["proposal_id"] for item in admitted
            ],
            "admitted_targets_are_synthetic_only": all(
                item["proposal"]["synthetic_control_only"] for item in admitted
            ),
            "blocked_proposal_ids": [
                {"proposal_id": item["proposal_id"], "label": item["gate_label"]}
                for item in blocked
            ],
            "rejected_proposal_ids": [
                {"proposal_id": item["proposal_id"], "label": item["gate_label"]}
                for item in rejected
            ],
            "all_s1_promoted_flags_false": all(
                item["s1_promoted"] is False for item in evaluations
            ),
            "all_t223_reversed_flags_false": all(
                item["t223_reversed"] is False for item in evaluations
            ),
            "s1_promotion": "none; T464 is an admission gate only",
            "t223_status": "unchanged; T223 finite no-go remains the inherited baseline",
            "claim_ledger_update": "none; no claim promotion or demotion",
            "reading": (
                "T464 makes the post-T223 S1 burden executable. Finite "
                "enumeration repeats, selected-survivor shortcuts, screen drift, "
                "post-hoc assumptions, circular tail-tuned measures, missing "
                "finite audits, single-size positives, missing Lorentzian targets, "
                "external-action shortcuts, and claim-promotion shortcuts fail or "
                "block. Only synthetic future added-assumption packets are admitted "
                "for review, and they earn no S1 promotion."
            ),
        },
        "recommended_next": [
            "Use T464 before reopening S1 finite-colimit work after T223.",
            "Do not treat selected finite survivors or more uniform enumeration as S1 progress.",
            "A future S1 packet should bring a predeclared natural measure, selection law, sprinkling law, or continuum bridge with finite audits and named Lorentzian constraints.",
            "Leave S1 at requires_added_assumption until such a packet runs and survives without overclaiming.",
        ],
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion or demotion",
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["admission_requirements"]]
    rows = [
        "| {proposal_id} | {action} | {admitted} | {label} | {missing} |".format(
            proposal_id=item["proposal_id"],
            action=item["gate_action"],
            admitted="yes" if item["admitted_future_target"] else "no",
            label=item["gate_label"],
            missing=", ".join(item["missing_requirements"]) or "none",
        )
        for item in result["proposal_evaluations"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T464 - S1 Added-Assumption Admission Gate - v0.1 results",
            "",
            "> Admission gate only. `CLAIM-LEDGER.md`, `ROADMAP.md`, README, "
            "North Star files, public posture, hard policy, and cross-repo "
            "truth are untouched.",
            "",
            "- Spec: `tests/T464-s1-added-assumption-admission-gate.md`",
            "- Model: `models/s1_added_assumption_admission_gate.py`",
            "- Tests: `tests/test_s1_added_assumption_admission_gate.py`",
            "- Artifact JSON: `results/T464-s1-added-assumption-admission-gate-v0.1.json`",
            "- Sources: S1, T223, T126/T156/T159 screens, and the spacetime colimit open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Admission Requirements",
            "",
            *requirements,
            "",
            "## Proposal Evaluation",
            "",
            "| proposal | gate action | admitted? | gate label | missing requirements |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Route Disposition",
            "",
            "- T223 remains the inherited finite no-go baseline.",
            "- S1 remains `requires_added_assumption` for the finite-colimit route.",
            "- More uniform finite enumeration and selected survivors are not restart routes.",
            "- Added assumptions are admitted only for future review, not for promotion.",
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable admission classifier for future S1 finite-colimit "
            "work after T223.",
            "",
            "Does not earn: S1 promotion, T223 reversal, spacetime derivation, "
            "manifoldlikeness, dimension estimate, random-sprinkling law, "
            "continuum theorem, Lorentzian metric, GR/QFT result, claim-ledger "
            "movement, public posture, or cross-repo support.",
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
        json_path = results_dir / "T464-s1-added-assumption-admission-gate-v0.1.json"
        md_path = (
            results_dir / "T464-s1-added-assumption-admission-gate-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
