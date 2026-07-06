"""T474: bridge-admission gate for observer-shadow packet families.

T473 blocked transport/LossKernel cross-family composition unless a bridge is
declared. This follow-up makes that bridge burden executable while preventing
semantic relabels, absorber completion, or direct category shortcuts from
counting as observer-shadow category evidence.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models.observer_shadow_indexed_composition_gate import run_t473_analysis


ARTIFACT_ID = "T474-observer-shadow-bridge-admission-gate-v0.1"
VERDICT = "CROSS_FAMILY_BRIDGE_GATE_BUILT_ATLAS_BRIDGE_ONLY_NO_CATEGORY"


@dataclass(frozen=True)
class BridgeControl:
    """A finite control inherited from T473 route cases."""

    control_id: str
    source_case_id: str
    control_kind: str
    available: bool
    description: str


@dataclass(frozen=True)
class BridgeProposal:
    """A proposed bridge between unlike observer-shadow packet families."""

    proposal_id: str
    source_family: str
    target_family: str
    declared_bridge_relation: str
    declared_shadow_relation: tuple[str, ...]
    declared_capability_relation: tuple[str, ...]
    required_controls: tuple[str, ...]
    supplied_controls: tuple[str, ...]
    uses_absorber_completion: bool
    attempts_direct_category_composition: bool
    intended_use: str


@dataclass(frozen=True)
class BridgeAdmission:
    """Gate decision for a bridge proposal."""

    proposal_id: str
    admitted: bool
    route_label: str
    missing_controls: tuple[str, ...]
    classification: str
    counts_as_cross_family_bridge: bool
    counts_as_category_evidence: bool
    notes: tuple[str, ...]


@dataclass(frozen=True)
class T474Result:
    """Complete T474 bridge-admission gate result."""

    controls: tuple[BridgeControl, ...]
    proposals: tuple[BridgeProposal, ...]
    admissions: tuple[BridgeAdmission, ...]
    verdict: str
    claim_ledger_update: str
    admitted_bridges: tuple[str, ...]
    rejected_bridges: tuple[str, ...]
    atlas_bridge_available: bool
    direct_cross_family_category_composition_supported: bool
    global_category_theorem_supported: bool
    strongest_reading: str
    future_packet_minimum: tuple[str, ...]
    not_earned: tuple[str, ...]


def run_t474_analysis() -> T474Result:
    """Run the finite observer-shadow bridge-admission gate."""

    controls = _bridge_controls()
    proposals = _bridge_proposals()
    available_controls = {
        control.control_id for control in controls if control.available
    }
    admissions = tuple(
        _evaluate_proposal(proposal, available_controls) for proposal in proposals
    )
    admitted_bridges = tuple(
        admission.proposal_id for admission in admissions if admission.admitted
    )
    rejected_bridges = tuple(
        admission.proposal_id for admission in admissions if not admission.admitted
    )

    return T474Result(
        controls=controls,
        proposals=proposals,
        admissions=admissions,
        verdict=VERDICT,
        claim_ledger_update="none",
        admitted_bridges=admitted_bridges,
        rejected_bridges=rejected_bridges,
        atlas_bridge_available="audit_atlas_bridge_packet" in admitted_bridges,
        direct_cross_family_category_composition_supported=False,
        global_category_theorem_supported=False,
        strongest_reading=(
            "T474 makes T473's missing-bridge burden executable. A bridge can be "
            "admitted only as audit-atlas metadata that keeps typed-transport and "
            "LossKernel capability objects separate, carries positive and hostile "
            "controls from T473, and refuses absorber completion as category "
            "evidence. The admitted bridge is enough to review cross-family "
            "packets, but not enough to compose unlike families into an "
            "observer-shadow category or fibration theorem."
        ),
        future_packet_minimum=(
            "declare the source and target packet families",
            "declare the bridge relation without identifying family-specific capability objects",
            "supply positive controls from each family",
            "supply a no-bridge hostile control",
            "supply upstream-rejection and absorber-completion hostile controls",
            "state whether the bridge is audit-atlas metadata or direct composition",
            "block category or fibration language unless cross-family preservation is proved beyond metadata",
        ),
        not_earned=(
            "observer-shadow category theorem",
            "indexed category or fibration theorem",
            "North Star geometry proof",
            "D1, PO1, TF1, or LossKernel promotion",
            "physics or consciousness claim",
            "claim-ledger movement",
            "roadmap movement",
            "public-posture movement",
        ),
    )


def _bridge_controls() -> tuple[BridgeControl, ...]:
    t473 = run_t473_analysis()
    cases = {case.case_id: case for case in t473.route_cases}

    return (
        BridgeControl(
            control_id="transport_bookkeeping_positive",
            source_case_id="transport_indexed_bookkeeping_threefold",
            control_kind="typed_transport_positive",
            available=(
                cases["transport_indexed_bookkeeping_threefold"].admitted
                and cases["transport_indexed_bookkeeping_threefold"].classification
                == "associative_indexed_bookkeeping_only"
            ),
            description=(
                "path-indexed transport composes only as indexed bookkeeping"
            ),
        ),
        BridgeControl(
            control_id="losskernel_preservation_positive",
            source_case_id="losskernel_preservation_threefold",
            control_kind="losskernel_positive",
            available=(
                cases["losskernel_preservation_threefold"].admitted
                and cases["losskernel_preservation_threefold"].counts_as_preservation_control
            ),
            description=(
                "LossKernel neighbor-visible preservation composes as a finite control"
            ),
        ),
        BridgeControl(
            control_id="no_bridge_hostile",
            source_case_id="cross_family_bridge_missing",
            control_kind="missing_bridge_negative",
            available=(
                not cases["cross_family_bridge_missing"].admitted
                and cases["cross_family_bridge_missing"].classification
                == "blocked_by_missing_cross_family_bridge"
            ),
            description=(
                "transport/LossKernel composition is rejected when no bridge is declared"
            ),
        ),
        BridgeControl(
            control_id="upstream_rejection_hostile",
            source_case_id="endpoint_rejection_blocks_composition",
            control_kind="upstream_rejection_negative",
            available=(
                not cases["endpoint_rejection_blocks_composition"].admitted
                and cases["endpoint_rejection_blocks_composition"].classification
                == "blocked_by_t472_rejection"
            ),
            description="T472-rejected packets remain blocked under composition",
        ),
        BridgeControl(
            control_id="absorber_completion_hostile",
            source_case_id="losskernel_absorber_taints_composition",
            control_kind="absorber_completion_negative",
            available=(
                cases["losskernel_absorber_taints_composition"].admitted
                and cases["losskernel_absorber_taints_composition"].classification
                == "absorber_completion_blocks_category_evidence"
            ),
            description=(
                "hidden-source completion taints composition as absorber bookkeeping"
            ),
        ),
    )


def _bridge_proposals() -> tuple[BridgeProposal, ...]:
    required = (
        "transport_bookkeeping_positive",
        "losskernel_preservation_positive",
        "no_bridge_hostile",
        "upstream_rejection_hostile",
        "absorber_completion_hostile",
    )

    return (
        BridgeProposal(
            proposal_id="no_declared_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            declared_bridge_relation="",
            declared_shadow_relation=(),
            declared_capability_relation=(),
            required_controls=required,
            supplied_controls=(),
            uses_absorber_completion=False,
            attempts_direct_category_composition=True,
            intended_use="compose unlike packet families by position in the route algebra",
        ),
        BridgeProposal(
            proposal_id="semantic_keyword_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            declared_bridge_relation="both packets involve loss, forgetting, or hidden data",
            declared_shadow_relation=("shared English gloss only",),
            declared_capability_relation=("loss-like capability phrase",),
            required_controls=required,
            supplied_controls=required,
            uses_absorber_completion=False,
            attempts_direct_category_composition=False,
            intended_use="treat semantic similarity as a bridge",
        ),
        BridgeProposal(
            proposal_id="absorber_completion_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            declared_bridge_relation=(
                "complete hidden source state and compare completed packets"
            ),
            declared_shadow_relation=("completed state alignment",),
            declared_capability_relation=("ordinary state-completion comparison",),
            required_controls=required,
            supplied_controls=required,
            uses_absorber_completion=True,
            attempts_direct_category_composition=False,
            intended_use="use absorber completion to repair the cross-family bridge",
        ),
        BridgeProposal(
            proposal_id="direct_category_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            declared_bridge_relation=(
                "identify both packet families as morphisms in one category"
            ),
            declared_shadow_relation=(
                "transport path index maps to neighbor signature",
                "accumulated forgotten structure maps to obligation normal form",
            ),
            declared_capability_relation=(
                "PO1 admissibility and witness obligation are treated as one K object",
            ),
            required_controls=required,
            supplied_controls=required,
            uses_absorber_completion=False,
            attempts_direct_category_composition=True,
            intended_use="promote cross-family bridge into direct category composition",
        ),
        BridgeProposal(
            proposal_id="audit_atlas_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            declared_bridge_relation=(
                "audit-atlas bridge comparing route evidence while preserving "
                "family-specific shadows, capability objects, and native comparisons"
            ),
            declared_shadow_relation=(
                "typed_transport keeps endpoint, path_label, and accumulated_forgotten_structure",
                "losskernel keeps neighbor_signature and blocks hidden-source omission",
            ),
            declared_capability_relation=(
                "PO1 admissibility remains boolean equality on PO1 evidence",
                "LossKernel obligation remains tuple equality on obligation normal form",
                "bridge compares only route labels and control status",
            ),
            required_controls=required,
            supplied_controls=required,
            uses_absorber_completion=False,
            attempts_direct_category_composition=False,
            intended_use=(
                "admit cross-family observer-shadow packets for review as atlas metadata"
            ),
        ),
    )


def _evaluate_proposal(
    proposal: BridgeProposal,
    available_controls: set[str],
) -> BridgeAdmission:
    missing = tuple(
        control
        for control in proposal.required_controls
        if control not in proposal.supplied_controls or control not in available_controls
    )
    notes: list[str] = []

    if not proposal.declared_bridge_relation:
        route = "reject_bridge_not_declared"
        admitted = False
        notes.append("no bridge relation is declared")
    elif missing:
        route = "reject_missing_bridge_controls"
        admitted = False
        notes.append("proposal lacks required positive or hostile bridge controls")
    elif proposal.uses_absorber_completion:
        route = "reject_absorber_completion_bridge"
        admitted = False
        notes.append("absorber completion is state-completion bookkeeping")
    elif proposal.attempts_direct_category_composition:
        route = "reject_direct_category_shortcut"
        admitted = False
        notes.append("direct category composition is not earned by finite controls")
    elif "shared English gloss only" in proposal.declared_shadow_relation:
        route = "reject_semantic_relabel_bridge"
        admitted = False
        notes.append("semantic similarity is not a typed bridge relation")
    elif (
        not proposal.declared_shadow_relation
        or not proposal.declared_capability_relation
    ):
        route = "reject_underdeclared_bridge"
        admitted = False
        notes.append("bridge does not preserve declared shadow and capability relations")
    else:
        route = "admit_audit_atlas_bridge_only"
        admitted = True
        notes.append("bridge is admitted only as audit-atlas metadata")
        notes.append("family-specific capability objects and comparisons remain separate")

    classification = _classification_for_route(route)

    return BridgeAdmission(
        proposal_id=proposal.proposal_id,
        admitted=admitted,
        route_label=route,
        missing_controls=missing,
        classification=classification,
        counts_as_cross_family_bridge=route == "admit_audit_atlas_bridge_only",
        counts_as_category_evidence=False,
        notes=tuple(notes),
    )


def _classification_for_route(route: str) -> str:
    if route == "admit_audit_atlas_bridge_only":
        return "atlas_bridge_admitted_no_category_evidence"
    if route == "reject_bridge_not_declared":
        return "missing_bridge_rejection"
    if route == "reject_missing_bridge_controls":
        return "insufficient_control_rejection"
    if route == "reject_absorber_completion_bridge":
        return "absorber_completion_rejection"
    if route == "reject_direct_category_shortcut":
        return "category_shortcut_rejection"
    if route == "reject_underdeclared_bridge":
        return "underdeclared_bridge_rejection"
    if route == "reject_semantic_relabel_bridge":
        return "semantic_relabel_rejection"
    return "unclassified_bridge_route"


def t474_result_to_dict(result: T474Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "controls": [_control_to_dict(control) for control in result.controls],
        "proposals": [_proposal_to_dict(proposal) for proposal in result.proposals],
        "admissions": [
            _admission_to_dict(admission) for admission in result.admissions
        ],
        "claim_ledger_update": result.claim_ledger_update,
        "admitted_bridges": list(result.admitted_bridges),
        "rejected_bridges": list(result.rejected_bridges),
        "atlas_bridge_available": result.atlas_bridge_available,
        "direct_cross_family_category_composition_supported": (
            result.direct_cross_family_category_composition_supported
        ),
        "global_category_theorem_supported": result.global_category_theorem_supported,
        "strongest_reading": result.strongest_reading,
        "future_packet_minimum": list(result.future_packet_minimum),
        "not_earned": list(result.not_earned),
    }


def render_markdown(result: T474Result) -> str:
    control_rows = []
    for control in result.controls:
        control_rows.append(
            "| {control_id} | {case} | {kind} | {available} | {description} |".format(
                control_id=control.control_id,
                case=control.source_case_id,
                kind=control.control_kind,
                available=control.available,
                description=control.description,
            )
        )

    admission_rows = []
    for admission in result.admissions:
        missing = ", ".join(admission.missing_controls) or "none"
        notes = "; ".join(admission.notes) or "none"
        admission_rows.append(
            "| {proposal_id} | {admitted} | {route} | {classification} | "
            "{missing} | {bridge} | {category} | {notes} |".format(
                proposal_id=admission.proposal_id,
                admitted=admission.admitted,
                route=admission.route_label,
                classification=admission.classification,
                missing=missing,
                bridge=admission.counts_as_cross_family_bridge,
                category=admission.counts_as_category_evidence,
                notes=notes,
            )
        )

    minimum = [f"- {item}" for item in result.future_packet_minimum]
    not_earned = [f"- {item}" for item in result.not_earned]

    return "\n".join(
        [
            "# T474 - Observer-Shadow Bridge Admission Gate - v0.1 results",
            "",
            "> Bridge-admission guardrail only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T474-observer-shadow-bridge-admission-gate.md`",
            "- Model: `models/observer_shadow_bridge_admission_gate.py`",
            "- Tests: `tests/test_observer_shadow_bridge_admission_gate.py`",
            "- Artifact JSON: `results/T474-observer-shadow-bridge-admission-gate-v0.1.json`",
            "- Source open problem: `open-problems/observer-shadow-category.md`",
            "- Prior gates: T470, T472, and T473",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## Bridge Controls",
            "",
            "| control | source T473 case | kind | available? | description |",
            "| --- | --- | --- | --- | --- |",
            *control_rows,
            "",
            "## Bridge Proposal Decisions",
            "",
            "| proposal | admitted? | route | classification | missing controls | counts as bridge? | category evidence? | notes |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *admission_rows,
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


def _control_to_dict(control: BridgeControl) -> dict[str, Any]:
    return {
        "control_id": control.control_id,
        "source_case_id": control.source_case_id,
        "control_kind": control.control_kind,
        "available": control.available,
        "description": control.description,
    }


def _proposal_to_dict(proposal: BridgeProposal) -> dict[str, Any]:
    return {
        "proposal_id": proposal.proposal_id,
        "source_family": proposal.source_family,
        "target_family": proposal.target_family,
        "declared_bridge_relation": proposal.declared_bridge_relation,
        "declared_shadow_relation": list(proposal.declared_shadow_relation),
        "declared_capability_relation": list(proposal.declared_capability_relation),
        "required_controls": list(proposal.required_controls),
        "supplied_controls": list(proposal.supplied_controls),
        "uses_absorber_completion": proposal.uses_absorber_completion,
        "attempts_direct_category_composition": (
            proposal.attempts_direct_category_composition
        ),
        "intended_use": proposal.intended_use,
    }


def _admission_to_dict(admission: BridgeAdmission) -> dict[str, Any]:
    return {
        "proposal_id": admission.proposal_id,
        "admitted": admission.admitted,
        "route_label": admission.route_label,
        "missing_controls": list(admission.missing_controls),
        "classification": admission.classification,
        "counts_as_cross_family_bridge": admission.counts_as_cross_family_bridge,
        "counts_as_category_evidence": admission.counts_as_category_evidence,
        "notes": list(admission.notes),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t474_analysis()
    payload = t474_result_to_dict(result)
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
