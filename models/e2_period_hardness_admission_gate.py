"""T438 - E2 period-hardness admission gate.

T419 failed as a D2 computational-arrow swing because its toy finite public
permutation was a short public cycle. T420 turned that into a reusable guardrail:
finite public cycles absorb the anti-relabel claim once the cycle is traversable.

T438 classifies future D2 packets. The only admitted packet shape is a
family-level period-hardness redesign target. Admission is not a D2 success, not
claim promotion, and not public posture.

Run:

    python -m models.e2_period_hardness_admission_gate --write-results
    python -m pytest tests/test_e2_period_hardness_admission_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import finite_cycle_anti_relabel_gate as t420


ARTIFACT = "T438-e2-period-hardness-admission-gate-v0.1"
SOURCE_D2 = "open-problems/computational-finality-arrow.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"
SOURCE_T419 = "results/T419-computational-arrow-of-time-v0.1-results.md"
SOURCE_T420 = "results/T420-finite-cycle-anti-relabel-gate-v0.1-results.md"

VERDICT = "E2_PERIOD_HARDNESS_ADMISSION_GATE_BUILT_NO_D2_DECISION"

HONEST_CEILING = (
    "Recorded-tier admission gate only. T438 does not redesign or abandon D2, "
    "does not promote a claim, does not prove cryptographic hardness, does not "
    "make a physics claim, and does not authorize public posture."
)


@dataclass(frozen=True)
class CandidatePacket:
    packet_id: str
    description: str
    closed_public_permutation_regime: bool = True
    family_level_declared: bool = False
    security_parameter_declared: bool = False
    public_transition_known: bool = True
    finite_toy_arrow_claim: bool = False
    public_cycle_recovery_within_bound: bool = False
    bounded_nonrecovery_used_as_evidence: bool = False
    period_problem_declared: bool = False
    period_hardness_assumption_named: bool = False
    period_hardness_reduction_predeclared: bool = False
    point_inversion_hardness_only: bool = False
    thermodynamic_or_erasure_cost_basis: bool = False
    symmetric_complexity_growth_basis: bool = False
    single_instance_physical_claim: bool = False
    post_hoc_or_pair_specific_policy: bool = False
    hidden_label_or_private_selector: bool = False
    changed_public_transition_knowledge: bool = False
    open_or_nonpermutation_regime: bool = False


def _packet_to_dict(packet: CandidatePacket) -> dict[str, Any]:
    return asdict(packet)


def classify_packet(packet: CandidatePacket) -> dict[str, Any]:
    admitted = False
    route = "rejected"
    label = "REJECTED_UNCLASSIFIED"
    reason = "No admission rule matched."

    if packet.post_hoc_or_pair_specific_policy or packet.hidden_label_or_private_selector:
        label = "BLOCKED_POST_HOC_OR_HIDDEN_SELECTOR"
        reason = "The packet uses post-hoc policy, pair-specific selection, or hidden labels."
    elif packet.thermodynamic_or_erasure_cost_basis:
        label = "NOT_E2_THERMODYNAMIC_OR_ERASURE_E1"
        reason = "The basis is thermodynamic or erasure cost, so it is not an E2 packet."
    elif packet.symmetric_complexity_growth_basis:
        label = "NOT_E2_SYMMETRIC_COMPLEXITY_GROWTH"
        reason = "The basis is symmetric complexity growth, not asymmetric feasible recovery."
    elif packet.changed_public_transition_knowledge or packet.open_or_nonpermutation_regime:
        route = "separate_spec_required"
        label = "ROUTE_TO_DIFFERENT_REGIME_SPEC"
        reason = (
            "The packet leaves the closed public-permutation regime. It may be "
            "worth a separate spec, but T438 does not admit it as the D2 E2 packet."
        )
    elif packet.public_cycle_recovery_within_bound and packet.finite_toy_arrow_claim:
        label = "REJECTED_T420_PUBLIC_CYCLE_ABSORBS_ARROW"
        reason = (
            "T420 applies: public forward iteration recovers predecessors inside "
            "the declared bound, so the finite toy cycle cannot evidence D2."
        )
    elif packet.bounded_nonrecovery_used_as_evidence and not packet.period_hardness_assumption_named:
        label = "REJECTED_BOUNDED_NONRECOVERY_NOT_EVIDENCE"
        reason = (
            "Bounded search failure is not arrow evidence without a family-level "
            "period-hardness assumption."
        )
    elif packet.point_inversion_hardness_only and not packet.period_problem_declared:
        label = "REJECTED_STATIC_T417_RELABEL"
        reason = (
            "Point inversion or square-root hardness alone is T417's static E2 "
            "boundary relabelled on a time index."
        )
    elif packet.single_instance_physical_claim:
        label = "REJECTED_SINGLE_INSTANCE_FINITE_CRACKABLE"
        reason = (
            "A single fixed finite public instance remains finite-work crackable; "
            "E2 must be family-level and conditional."
        )
    elif not packet.family_level_declared or not packet.security_parameter_declared:
        label = "REJECTED_NO_FAMILY_LEVEL_SECURITY_PARAMETER"
        reason = "The packet does not declare a family and security parameter."
    elif not packet.period_problem_declared:
        label = "REJECTED_NO_PERIOD_REVERSAL_PROBLEM"
        reason = "The packet does not state the period/reversal problem."
    elif not packet.period_hardness_assumption_named:
        label = "REJECTED_NO_NAMED_PERIOD_HARDNESS_ASSUMPTION"
        reason = "The packet lacks a named family-level period-hardness assumption."
    elif not packet.period_hardness_reduction_predeclared:
        label = "REJECTED_STIPULATED_HARDNESS"
        reason = "Hardness is asserted without a predeclared reduction or theorem target."
    elif not packet.closed_public_permutation_regime or not packet.public_transition_known:
        route = "separate_spec_required"
        label = "ROUTE_TO_DIFFERENT_REGIME_SPEC"
        reason = "The packet is not a closed public-permutation family."
    else:
        admitted = True
        route = "admitted_as_future_target"
        label = "ADMITTED_E2_PERIOD_HARDNESS_REDESIGN_PACKET_NO_D2_DECISION"
        reason = (
            "The packet declares the family, security parameter, public transition, "
            "period/reversal problem, named hardness assumption, and predeclared "
            "reduction target. It is admitted only as a future E2 redesign target."
        )

    return {
        "packet": _packet_to_dict(packet),
        "admitted_for_future_d2_work": admitted,
        "route": route,
        "label": label,
        "reason": reason,
    }


def candidate_packets() -> tuple[CandidatePacket, ...]:
    t420_result = t420.run_t420_analysis()
    t419_absorbed = t420_result.t419_qr77_gate.every_predecessor_recovered_within_bound

    return (
        CandidatePacket(
            packet_id="t419_qr77_finite_public_cycle",
            description="The actual T419 toy QR_77 public squaring orbit.",
            finite_toy_arrow_claim=True,
            public_cycle_recovery_within_bound=t419_absorbed,
            point_inversion_hardness_only=True,
        ),
        CandidatePacket(
            packet_id="long_cycle_bounded_nonrecovery_only",
            description=(
                "A finite long public cycle where the chosen bound fails to find "
                "the predecessor, but no family hardness is declared."
            ),
            finite_toy_arrow_claim=True,
            bounded_nonrecovery_used_as_evidence=True,
        ),
        CandidatePacket(
            packet_id="point_sqrt_hardness_static_relabel",
            description="A packet with Rabin point square-root hardness but no period problem.",
            family_level_declared=True,
            security_parameter_declared=True,
            point_inversion_hardness_only=True,
            period_hardness_assumption_named=True,
            period_hardness_reduction_predeclared=True,
        ),
        CandidatePacket(
            packet_id="single_instance_hard_theorem_claim",
            description="A single fixed finite instance claimed as a physical E2 boundary.",
            single_instance_physical_claim=True,
            period_problem_declared=True,
            period_hardness_assumption_named=True,
            period_hardness_reduction_predeclared=True,
        ),
        CandidatePacket(
            packet_id="thermodynamic_reversal_cost_packet",
            description="A packet that bills reversal through erasure or heat cost.",
            thermodynamic_or_erasure_cost_basis=True,
        ),
        CandidatePacket(
            packet_id="brown_susskind_complexity_growth_packet",
            description="A packet whose arrow is symmetric state-complexity growth.",
            symmetric_complexity_growth_basis=True,
        ),
        CandidatePacket(
            packet_id="post_hoc_period_policy_packet",
            description="A period-hardness policy chosen after inspecting the pair.",
            family_level_declared=True,
            security_parameter_declared=True,
            period_problem_declared=True,
            period_hardness_assumption_named=True,
            period_hardness_reduction_predeclared=True,
            post_hoc_or_pair_specific_policy=True,
        ),
        CandidatePacket(
            packet_id="changed_public_transition_packet",
            description=(
                "A packet where the agent does not know the public transition or "
                "the transition changes during the run."
            ),
            closed_public_permutation_regime=False,
            public_transition_known=False,
            changed_public_transition_knowledge=True,
            family_level_declared=True,
            security_parameter_declared=True,
            period_problem_declared=True,
            period_hardness_assumption_named=True,
            period_hardness_reduction_predeclared=True,
        ),
        CandidatePacket(
            packet_id="open_nonpermutation_packet",
            description="An open or non-permutation dynamics packet outside T420's regime.",
            closed_public_permutation_regime=False,
            open_or_nonpermutation_regime=True,
            family_level_declared=True,
            security_parameter_declared=True,
            period_problem_declared=True,
            period_hardness_assumption_named=True,
            period_hardness_reduction_predeclared=True,
        ),
        CandidatePacket(
            packet_id="predeclared_period_hardness_family_packet",
            description=(
                "Positive control: a closed public-permutation family packet that "
                "does not claim toy exhibition and predeclares the period-hardness burden."
            ),
            family_level_declared=True,
            security_parameter_declared=True,
            period_problem_declared=True,
            period_hardness_assumption_named=True,
            period_hardness_reduction_predeclared=True,
        ),
    )


def run() -> dict[str, Any]:
    t420_result = t420.run_t420_analysis()
    classifications = [classify_packet(packet) for packet in candidate_packets()]
    admitted = [
        item for item in classifications if item["admitted_for_future_d2_work"]
    ]
    routed = [item for item in classifications if item["route"] == "separate_spec_required"]
    rejected = [item for item in classifications if item["route"] == "rejected"]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "d2_open_problem": SOURCE_D2,
            "taxonomy_reference": SOURCE_TAXONOMY,
            "t419": SOURCE_T419,
            "t420": SOURCE_T420,
        },
        "purpose": (
            "Convert T420's post-T419 redesign rule into an executable admission "
            "gate for future E2 computational-finality packets."
        ),
        "t420_imported_guardrail": {
            "t419_seed_orbit": list(t420_result.t419_seed_orbit.cycle_labels),
            "public_predecessor_label": t420_result.t419_seed_orbit.public_predecessor_label,
            "max_forward_steps_to_predecessor": (
                t420_result.t419_qr77_gate.max_forward_steps_to_predecessor
            ),
            "every_predecessor_recovered_within_bound": (
                t420_result.t419_qr77_gate.every_predecessor_recovered_within_bound
            ),
        },
        "admission_requirements": [
            "family-level packet, not a single fixed finite instance",
            "security parameter declared",
            "closed public-permutation regime declared, or else routed to a separate spec",
            "public transition knowledge fixed",
            "period/reversal problem stated, not only point inversion",
            "named period-hardness assumption or theorem target",
            "predeclared reduction or proof obligation",
            "bounded non-recovery is not treated as evidence",
            "no post-hoc policy, hidden label, thermodynamic cost, or symmetric complexity-growth basis",
        ],
        "classifications": classifications,
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_packet_ids": [item["packet"]["packet_id"] for item in admitted],
            "routed_packet_ids": [item["packet"]["packet_id"] for item in routed],
            "rejected_packet_ids": [item["packet"]["packet_id"] for item in rejected],
            "d2_decision": "none; redesign/abandon remains separately gated",
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T438 admits only a predeclared family-level period-hardness packet "
                "as a future E2 redesign target. It rejects finite public cycles, "
                "bounded non-recovery, point-inversion-only static relabels, E1 "
                "thermodynamic packets, Brown-Susskind complexity-growth packets, "
                "single-instance claims, and post-hoc selectors. Packets that leave "
                "the closed public-permutation regime require a separate spec."
            ),
        },
        "recommended_next": [
            "Any D2 continuation should first supply the admitted period-hardness packet fields.",
            "If that packet cannot be supplied, demote the temporal story to T417's static E2 boundary.",
            "Changed-transition or open-regime ideas need their own spec before execution.",
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
            admitted="yes" if item["admitted_for_future_d2_work"] else "no",
        )
        for item in result["classifications"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T438 - E2 Period-Hardness Admission Gate - v0.1 results",
            "",
            "> Recorded-tier admission gate. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No D2 redesign/abandon decision, "
            "no claim promotion, no public posture.",
            "",
            "- Spec (frozen first): `tests/T438-e2-period-hardness-admission-gate.md`",
            "- Model: `models/e2_period_hardness_admission_gate.py`",
            "- Tests: `tests/test_e2_period_hardness_admission_gate.py`",
            "- Artifact JSON: `results/T438-e2-period-hardness-admission-gate-v0.1.json`",
            "- Sources: T417, T419, T420, D2 open problem, and the adopted taxonomy reference",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Imported T420 Guardrail",
            "",
            "- T419 seed orbit: `{}`".format(
                result["t420_imported_guardrail"]["t419_seed_orbit"]
            ),
            "- Public predecessor label: `{}`".format(
                result["t420_imported_guardrail"]["public_predecessor_label"]
            ),
            "- Max public forward steps to predecessor: `{}`".format(
                result["t420_imported_guardrail"]["max_forward_steps_to_predecessor"]
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
            "Earns: a reusable admission classifier for future E2 computational-finality "
            "packets after T419/T420.",
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
        json_path = results_dir / "T438-e2-period-hardness-admission-gate-v0.1.json"
        md_path = results_dir / "T438-e2-period-hardness-admission-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
