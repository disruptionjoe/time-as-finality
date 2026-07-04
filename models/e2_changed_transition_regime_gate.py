"""T444 - E2 changed-transition / open-regime gate.

T438 admitted only closed public-permutation period-hardness packets for future
D2 computational-finality work. It routed changed-public-transition and
open/nonpermutation packets to a separate spec.

T444 makes that separate-spec boundary executable. Admission here is narrow:
it only says a packet is coherent enough to review as a separate E2 regime. It
does not redesign D2, abandon D2, promote a claim, prove cryptographic hardness,
or make a physics claim.

Run:

    python -m models.e2_changed_transition_regime_gate --write-results
    python -m pytest tests/test_e2_changed_transition_regime_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import e2_period_hardness_admission_gate as t438


ARTIFACT = "T444-e2-changed-transition-regime-gate-v0.1"
SOURCE_D2 = "open-problems/computational-finality-arrow.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"
SOURCE_T438 = "results/T438-e2-period-hardness-admission-gate-v0.1-results.md"

VERDICT = "E2_CHANGED_TRANSITION_REGIME_GATE_BUILT_NO_D2_DECISION"

HONEST_CEILING = (
    "Recorded-tier routing/admission gate only. T444 does not redesign or "
    "abandon D2, does not promote a claim, does not prove cryptographic "
    "hardness, does not turn epistemic ignorance into finality, and does not "
    "authorize public posture."
)


@dataclass(frozen=True)
class RegimePacket:
    packet_id: str
    description: str
    closed_public_permutation_regime: bool = False
    changed_public_transition_knowledge: bool = False
    open_or_nonpermutation_regime: bool = False
    family_level_declared: bool = False
    security_parameter_declared: bool = False
    agent_access_boundary_declared: bool = False
    transition_evidence_frozen: bool = False
    transition_update_law_predeclared: bool = False
    public_verification_or_audit_trail: bool = False
    hardness_or_unpredictability_burden_named: bool = False
    predeclared_reduction_or_theorem_target: bool = False
    distinguishes_capability_from_ignorance: bool = False
    post_hoc_or_pair_specific_policy: bool = False
    hidden_selector_or_private_oracle: bool = False
    thermodynamic_or_erasure_cost_basis: bool = False
    symmetric_complexity_growth_basis: bool = False
    bounded_toy_only: bool = False
    resource_or_environment_completion_absorbs: bool = False
    claims_d2_success: bool = False


def _packet_to_dict(packet: RegimePacket) -> dict[str, Any]:
    return asdict(packet)


def classify_packet(packet: RegimePacket) -> dict[str, Any]:
    admitted = False
    route = "rejected"
    label = "REJECTED_UNCLASSIFIED"
    reason = "No T444 admission rule matched."

    if packet.claims_d2_success:
        label = "BLOCKED_PREMATURE_D2_DECISION"
        reason = "A routing gate cannot redesign, abandon, or discharge D2."
    elif packet.post_hoc_or_pair_specific_policy or packet.hidden_selector_or_private_oracle:
        label = "BLOCKED_POST_HOC_OR_HIDDEN_TRANSITION_POLICY"
        reason = "The packet uses post-hoc policy, pair-specific selection, or a hidden oracle."
    elif packet.thermodynamic_or_erasure_cost_basis:
        label = "NOT_E2_THERMODYNAMIC_OR_ERASURE_E1"
        reason = "The claimed asymmetry is thermodynamic or erasure-cost based, so it is E1/H7 terrain."
    elif packet.symmetric_complexity_growth_basis:
        label = "NOT_E2_SYMMETRIC_COMPLEXITY_GROWTH"
        reason = "The claimed asymmetry is Brown-Susskind-style symmetric complexity growth, not E2 feasible recovery."
    elif packet.closed_public_permutation_regime and not (
        packet.changed_public_transition_knowledge or packet.open_or_nonpermutation_regime
    ):
        route = "route_back_to_t438"
        label = "ROUTE_BACK_TO_T438_CLOSED_PUBLIC_PERMUTATION"
        reason = "Closed public-permutation packets belong to T438's period-hardness gate."
    elif not packet.family_level_declared or not packet.security_parameter_declared:
        label = "REJECTED_NO_FAMILY_LEVEL_SECURITY_PARAMETER"
        reason = "E2 review requires a family and security parameter, not an isolated finite toy."
    elif packet.bounded_toy_only:
        label = "REJECTED_BOUNDED_TOY_NOT_E2"
        reason = "A bounded toy or finite trace is not evidence for an E2 boundary."
    elif packet.resource_or_environment_completion_absorbs:
        label = "REJECTED_RESOURCE_OR_ENVIRONMENT_COMPLETION_ABSORBS"
        reason = "The separator disappears once ordinary resource, environment, or transcript completion is admitted."
    elif packet.changed_public_transition_knowledge:
        if not packet.agent_access_boundary_declared:
            label = "REJECTED_NO_AGENT_ACCESS_BOUNDARY"
            reason = "The packet changes what the agent knows without declaring the agent/access boundary."
        elif not packet.transition_evidence_frozen:
            label = "REJECTED_UNFROZEN_TRANSITION_EVIDENCE"
            reason = "The transition trace, transcript, or update evidence is not frozen before evaluation."
        elif not packet.transition_update_law_predeclared:
            label = "REJECTED_NO_PREDECLARED_TRANSITION_UPDATE_LAW"
            reason = "A changed-transition packet needs a predeclared update law or publication schedule."
        elif not packet.public_verification_or_audit_trail:
            label = "REJECTED_NO_PUBLIC_AUDIT_TRAIL"
            reason = "The transition change cannot be independently audited from the public packet."
        elif not packet.distinguishes_capability_from_ignorance:
            label = "REJECTED_EPISTEMIC_IGNORANCE_NOT_CAPABILITY_BOUNDARY"
            reason = "Mere ignorance of the transition is not a capability/finality boundary."
        elif not packet.hardness_or_unpredictability_burden_named:
            label = "REJECTED_NO_CHANGED_TRANSITION_FORCING_BURDEN"
            reason = "The packet names no hardness, unpredictability, or theorem burden for the access split."
        elif not packet.predeclared_reduction_or_theorem_target:
            label = "REJECTED_STIPULATED_CHANGED_TRANSITION_HARDNESS"
            reason = "Hardness is asserted without a predeclared reduction or theorem target."
        else:
            admitted = True
            route = "admitted_as_separate_spec_target"
            label = "ADMITTED_CHANGED_TRANSITION_SEPARATE_SPEC_NO_D2_DECISION"
            reason = (
                "The packet freezes the family, access boundary, transition evidence, "
                "update law, audit trail, and forcing burden. It is admitted only "
                "as a separate-regime review target."
            )
    elif packet.open_or_nonpermutation_regime:
        if not packet.transition_evidence_frozen:
            label = "REJECTED_UNFROZEN_OPEN_REGIME_TRACE"
            reason = "The open/nonpermutation trace is not frozen before evaluation."
        elif not packet.transition_update_law_predeclared:
            label = "REJECTED_NO_OPEN_DYNAMICS_LAW"
            reason = "An open/nonpermutation packet needs a predeclared dynamics law."
        elif not packet.public_verification_or_audit_trail:
            label = "REJECTED_NO_PUBLIC_OPEN_REGIME_AUDIT_TRAIL"
            reason = "The open dynamics cannot be independently audited from the packet."
        elif not packet.distinguishes_capability_from_ignorance:
            label = "REJECTED_OPEN_REGIME_ONLY_REDESCRIBES_IGNORANCE"
            reason = "The packet does not distinguish physical/open-regime capability from unknown state."
        elif not packet.hardness_or_unpredictability_burden_named:
            label = "REJECTED_NO_OPEN_REGIME_FORCING_BURDEN"
            reason = "The packet names no E2 forcing burden for the open/nonpermutation regime."
        elif not packet.predeclared_reduction_or_theorem_target:
            label = "REJECTED_STIPULATED_OPEN_REGIME_HARDNESS"
            reason = "The open-regime hardness is asserted without a predeclared target."
        else:
            admitted = True
            route = "admitted_as_separate_spec_target"
            label = "ADMITTED_OPEN_NONPERMUTATION_SEPARATE_SPEC_NO_D2_DECISION"
            reason = (
                "The packet freezes the family, dynamics law, evidence, audit trail, "
                "and forcing burden. It is admitted only as a separate-regime review target."
            )

    return {
        "packet": _packet_to_dict(packet),
        "admitted_for_separate_spec_review": admitted,
        "route": route,
        "label": label,
        "reason": reason,
    }


def candidate_packets() -> tuple[RegimePacket, ...]:
    return (
        RegimePacket(
            packet_id="closed_public_permutation_period_packet",
            description="A normal closed public-permutation period-hardness packet.",
            closed_public_permutation_regime=True,
            family_level_declared=True,
            security_parameter_declared=True,
        ),
        RegimePacket(
            packet_id="post_hoc_transition_swap_packet",
            description="The transition schedule is selected after inspecting the witness pair.",
            changed_public_transition_knowledge=True,
            family_level_declared=True,
            security_parameter_declared=True,
            post_hoc_or_pair_specific_policy=True,
        ),
        RegimePacket(
            packet_id="hidden_oracle_transition_packet",
            description="A private oracle chooses which transition is active.",
            changed_public_transition_knowledge=True,
            family_level_declared=True,
            security_parameter_declared=True,
            hidden_selector_or_private_oracle=True,
        ),
        RegimePacket(
            packet_id="thermodynamic_transition_cost_packet",
            description="The transition asymmetry is paid by erasure or heat cost.",
            open_or_nonpermutation_regime=True,
            family_level_declared=True,
            security_parameter_declared=True,
            thermodynamic_or_erasure_cost_basis=True,
        ),
        RegimePacket(
            packet_id="brown_susskind_complexity_packet",
            description="The packet uses symmetric state-complexity growth as the arrow.",
            open_or_nonpermutation_regime=True,
            family_level_declared=True,
            security_parameter_declared=True,
            symmetric_complexity_growth_basis=True,
        ),
        RegimePacket(
            packet_id="pure_unknown_transition_packet",
            description="The agent simply does not know the transition function.",
            changed_public_transition_knowledge=True,
            family_level_declared=True,
            security_parameter_declared=True,
            agent_access_boundary_declared=True,
            transition_evidence_frozen=True,
            transition_update_law_predeclared=True,
            public_verification_or_audit_trail=True,
        ),
        RegimePacket(
            packet_id="unfrozen_transition_evidence_packet",
            description="A changed-transition packet whose update transcript is not frozen.",
            changed_public_transition_knowledge=True,
            family_level_declared=True,
            security_parameter_declared=True,
            agent_access_boundary_declared=True,
            transition_update_law_predeclared=True,
            public_verification_or_audit_trail=True,
            distinguishes_capability_from_ignorance=True,
            hardness_or_unpredictability_burden_named=True,
            predeclared_reduction_or_theorem_target=True,
        ),
        RegimePacket(
            packet_id="predeclared_changed_transition_packet",
            description="Positive control: predeclared changed-transition separate-spec packet.",
            changed_public_transition_knowledge=True,
            family_level_declared=True,
            security_parameter_declared=True,
            agent_access_boundary_declared=True,
            transition_evidence_frozen=True,
            transition_update_law_predeclared=True,
            public_verification_or_audit_trail=True,
            hardness_or_unpredictability_burden_named=True,
            predeclared_reduction_or_theorem_target=True,
            distinguishes_capability_from_ignorance=True,
        ),
        RegimePacket(
            packet_id="open_nonpermutation_no_law_packet",
            description="An open/nonpermutation packet without a dynamics law.",
            open_or_nonpermutation_regime=True,
            family_level_declared=True,
            security_parameter_declared=True,
            transition_evidence_frozen=True,
            public_verification_or_audit_trail=True,
            hardness_or_unpredictability_burden_named=True,
            predeclared_reduction_or_theorem_target=True,
            distinguishes_capability_from_ignorance=True,
        ),
        RegimePacket(
            packet_id="resource_completion_absorbed_open_packet",
            description="An open-regime separator absorbed by ordinary resource completion.",
            open_or_nonpermutation_regime=True,
            family_level_declared=True,
            security_parameter_declared=True,
            transition_evidence_frozen=True,
            transition_update_law_predeclared=True,
            public_verification_or_audit_trail=True,
            hardness_or_unpredictability_burden_named=True,
            predeclared_reduction_or_theorem_target=True,
            distinguishes_capability_from_ignorance=True,
            resource_or_environment_completion_absorbs=True,
        ),
        RegimePacket(
            packet_id="predeclared_open_nonpermutation_packet",
            description="Positive control: predeclared open/nonpermutation separate-spec packet.",
            open_or_nonpermutation_regime=True,
            family_level_declared=True,
            security_parameter_declared=True,
            transition_evidence_frozen=True,
            transition_update_law_predeclared=True,
            public_verification_or_audit_trail=True,
            hardness_or_unpredictability_burden_named=True,
            predeclared_reduction_or_theorem_target=True,
            distinguishes_capability_from_ignorance=True,
        ),
    )


def _t438_routed_packet_ids() -> list[str]:
    result = t438.run()
    return result["overall_verdict"]["routed_packet_ids"]


def run() -> dict[str, Any]:
    t438_routed = _t438_routed_packet_ids()
    classifications = [classify_packet(packet) for packet in candidate_packets()]
    admitted = [
        item
        for item in classifications
        if item["admitted_for_separate_spec_review"]
    ]
    routed_back = [
        item for item in classifications if item["route"] == "route_back_to_t438"
    ]
    rejected = [item for item in classifications if item["route"] == "rejected"]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "d2_open_problem": SOURCE_D2,
            "taxonomy_reference": SOURCE_TAXONOMY,
            "t438": SOURCE_T438,
        },
        "purpose": (
            "Make T438's separate-spec route executable for changed-public-transition "
            "and open/nonpermutation E2 packets."
        ),
        "imported_t438_guardrail": {
            "t438_verdict": t438.VERDICT,
            "routed_packet_ids": t438_routed,
            "requires_separate_spec": [
                "changed_public_transition_packet",
                "open_nonpermutation_packet",
            ],
        },
        "admission_requirements": [
            "family-level packet with security parameter",
            "not a closed public-permutation packet already governed by T438",
            "agent/access boundary declared for changed-transition packets",
            "transition evidence, transcript, or trace frozen before evaluation",
            "predeclared transition-update law, publication schedule, or open-dynamics law",
            "public verification or independent audit trail",
            "explicit distinction between capability boundary and mere ignorance",
            "named hardness, unpredictability, or theorem burden",
            "predeclared reduction or theorem target",
            "no post-hoc policy, hidden oracle, thermodynamic cost, symmetric complexity growth, or resource-completion absorber",
        ],
        "classifications": classifications,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_packet_ids": [item["packet"]["packet_id"] for item in admitted],
            "routed_back_to_t438_packet_ids": [
                item["packet"]["packet_id"] for item in routed_back
            ],
            "rejected_packet_ids": [item["packet"]["packet_id"] for item in rejected],
            "d2_decision": "none; redesign/abandon remains separately gated",
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T444 admits only predeclared changed-transition or open/nonpermutation "
                "packets for separate-spec review. It rejects post-hoc/hidden transition "
                "policies, thermodynamic/E1 packets, Brown-Susskind symmetric-complexity "
                "packets, pure epistemic ignorance, unfrozen transition evidence, "
                "missing open-dynamics law, and resource/environment completion. Closed "
                "public-permutation packets route back to T438."
            ),
        },
        "recommended_next": [
            "Use T438 for closed public-permutation period-hardness packets.",
            "Use T444 before any changed-transition or open/nonpermutation D2 attempt.",
            "Do not treat T444 admission as D2 redesign, D2 success, or claim support.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["admission_requirements"]]
    rows = [
        "| {packet_id} | {label} | {route} | {admitted} |".format(
            packet_id=item["packet"]["packet_id"],
            label=item["label"],
            route=item["route"],
            admitted="yes" if item["admitted_for_separate_spec_review"] else "no",
        )
        for item in result["classifications"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T444 - E2 Changed-Transition Regime Gate - v0.1 results",
            "",
            "> Recorded-tier routing/admission gate. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, "
            "no claim promotion, no public posture.",
            "",
            "- Spec: `tests/T444-e2-changed-transition-regime-gate.md`",
            "- Model: `models/e2_changed_transition_regime_gate.py`",
            "- Tests: `tests/test_e2_changed_transition_regime_gate.py`",
            "- Artifact JSON: `results/T444-e2-changed-transition-regime-gate-v0.1.json`",
            "- Sources: T438, D2 open problem, and adopted taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Imported T438 Guardrail",
            "",
            "- T438 verdict: `{}`".format(
                result["imported_t438_guardrail"]["t438_verdict"]
            ),
            "- T438 routed packet ids: `{}`".format(
                result["imported_t438_guardrail"]["routed_packet_ids"]
            ),
            "",
            "## Admission Requirements",
            "",
            *requirements,
            "",
            "## Packet Classification",
            "",
            "| packet | label | route | admitted? |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable routing/admission classifier for the D2 packets T438 "
            "explicitly routed to a separate spec.",
            "",
            "Does not earn: a D2 redesign, D2 abandonment, a computational arrow, a "
            "crypto theorem, a physics claim, claim-ledger movement, or public posture.",
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
        json_path = results_dir / "T444-e2-changed-transition-regime-gate-v0.1.json"
        md_path = results_dir / "T444-e2-changed-transition-regime-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
