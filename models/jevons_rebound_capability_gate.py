"""Pre-T Jevons rebound capability gate.

The Jevons open problem asks whether a lower unit cost is still a net
capability/finality improvement after demand response is modeled. This module
keeps that question executable without registering a new T-number or moving
claim/canon/public posture.

Run: python -m models.jevons_rebound_capability_gate
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Any


ARTIFACT = "jevons-rebound-capability-gate-pre-t-v0.1"
VERDICT = "JEVONS_REBOUND_GATE_BUILT_PRE_T_REVIEW_ONLY"

SOURCE_OPEN_PROBLEM = "open-problems/jevons-rebound-capability-gate.md"

HONEST_CEILING = (
    "Pre-T executable classifier only. This does not add a TESTS.md row, "
    "does not produce a numbered result packet, does not prove TaF-specific "
    "residue over resource-demand accounting, and does not move claim status, "
    "Canon Index tiers, canon verdicts, roadmap, README, North Star, public "
    "posture, hard policy, external publication, or cross-repo truth."
)


@dataclass(frozen=True)
class ReboundPacket:
    packet_id: str
    description: str
    fixed_region_menu: bool
    operation_named: bool
    unit_cost_before: float
    unit_cost_after: float
    demand_before: float
    demand_after: float
    demand_response_predeclared: bool
    burden_predeclared: bool
    burden_before: float
    burden_after: float
    capability_before: float
    capability_after_unit_cost_only: float
    capability_after_demand_response: float
    positive_control_present: bool
    negative_control_present: bool
    resource_accounting_explains_split: bool
    independent_finality_witness: bool
    post_hoc_burden_variable: bool = False
    imports_source_side_growth: bool = False
    claims_claim_or_public_movement: bool = False


@dataclass(frozen=True)
class GateEvaluation:
    packet_id: str
    admitted: bool
    label: str
    action: str
    reason: str
    unit_cost_decreases: bool
    demand_increases: bool
    burden_worsens: bool
    apparent_capability_improves: bool
    net_capability_improves: bool
    packet: ReboundPacket


def example_packets() -> tuple[ReboundPacket, ...]:
    return (
        ReboundPacket(
            packet_id="unit_efficiency_positive_control",
            description=(
                "Lower unit cost does not trigger extra demand; aggregate "
                "burden falls and net capability improves."
            ),
            fixed_region_menu=True,
            operation_named=True,
            unit_cost_before=10.0,
            unit_cost_after=5.0,
            demand_before=10.0,
            demand_after=10.0,
            demand_response_predeclared=True,
            burden_predeclared=True,
            burden_before=100.0,
            burden_after=50.0,
            capability_before=4.0,
            capability_after_unit_cost_only=6.0,
            capability_after_demand_response=6.0,
            positive_control_present=True,
            negative_control_present=True,
            resource_accounting_explains_split=False,
            independent_finality_witness=False,
        ),
        ReboundPacket(
            packet_id="classic_rebound_resource_accounting",
            description=(
                "Lower unit cost increases demand enough that aggregate burden "
                "rises and net capability worsens."
            ),
            fixed_region_menu=True,
            operation_named=True,
            unit_cost_before=10.0,
            unit_cost_after=5.0,
            demand_before=10.0,
            demand_after=30.0,
            demand_response_predeclared=True,
            burden_predeclared=True,
            burden_before=100.0,
            burden_after=150.0,
            capability_before=4.0,
            capability_after_unit_cost_only=6.0,
            capability_after_demand_response=3.0,
            positive_control_present=True,
            negative_control_present=True,
            resource_accounting_explains_split=True,
            independent_finality_witness=False,
        ),
        ReboundPacket(
            packet_id="post_hoc_burden_variable",
            description=(
                "The burden variable is selected only after seeing the pair, "
                "so the apparent split is underdescribed."
            ),
            fixed_region_menu=True,
            operation_named=True,
            unit_cost_before=10.0,
            unit_cost_after=5.0,
            demand_before=10.0,
            demand_after=30.0,
            demand_response_predeclared=True,
            burden_predeclared=False,
            burden_before=100.0,
            burden_after=150.0,
            capability_before=4.0,
            capability_after_unit_cost_only=6.0,
            capability_after_demand_response=3.0,
            positive_control_present=True,
            negative_control_present=True,
            resource_accounting_explains_split=False,
            independent_finality_witness=False,
            post_hoc_burden_variable=True,
        ),
        ReboundPacket(
            packet_id="hidden_demand_response_label",
            description=(
                "Demand response is imported as an unexplained hidden label "
                "rather than a predeclared rule or measured packet."
            ),
            fixed_region_menu=True,
            operation_named=True,
            unit_cost_before=10.0,
            unit_cost_after=5.0,
            demand_before=10.0,
            demand_after=30.0,
            demand_response_predeclared=False,
            burden_predeclared=True,
            burden_before=100.0,
            burden_after=150.0,
            capability_before=4.0,
            capability_after_unit_cost_only=6.0,
            capability_after_demand_response=3.0,
            positive_control_present=True,
            negative_control_present=True,
            resource_accounting_explains_split=False,
            independent_finality_witness=False,
        ),
        ReboundPacket(
            packet_id="source_side_possibility_growth_import",
            description=(
                "The packet tries to explain the split by source-side "
                "possibility growth, which belongs outside TaF."
            ),
            fixed_region_menu=True,
            operation_named=True,
            unit_cost_before=10.0,
            unit_cost_after=5.0,
            demand_before=10.0,
            demand_after=30.0,
            demand_response_predeclared=True,
            burden_predeclared=True,
            burden_before=100.0,
            burden_after=150.0,
            capability_before=4.0,
            capability_after_unit_cost_only=6.0,
            capability_after_demand_response=3.0,
            positive_control_present=True,
            negative_control_present=True,
            resource_accounting_explains_split=False,
            independent_finality_witness=False,
            imports_source_side_growth=True,
        ),
        ReboundPacket(
            packet_id="synthetic_finality_review_target",
            description=(
                "A future-shaped packet where lower unit cost triggers demand "
                "response, ordinary resource accounting does not explain the "
                "net capability split, and a predeclared finality witness is "
                "supplied."
            ),
            fixed_region_menu=True,
            operation_named=True,
            unit_cost_before=10.0,
            unit_cost_after=5.0,
            demand_before=10.0,
            demand_after=30.0,
            demand_response_predeclared=True,
            burden_predeclared=True,
            burden_before=100.0,
            burden_after=150.0,
            capability_before=4.0,
            capability_after_unit_cost_only=6.0,
            capability_after_demand_response=2.0,
            positive_control_present=True,
            negative_control_present=True,
            resource_accounting_explains_split=False,
            independent_finality_witness=True,
        ),
    )


def evaluate_packet(packet: ReboundPacket) -> GateEvaluation:
    unit_cost_decreases = packet.unit_cost_after < packet.unit_cost_before
    demand_increases = packet.demand_after > packet.demand_before
    burden_worsens = packet.burden_after > packet.burden_before
    apparent_capability_improves = (
        packet.capability_after_unit_cost_only > packet.capability_before
    )
    net_capability_improves = (
        packet.capability_after_demand_response > packet.capability_before
    )

    def evaluation(admitted: bool, label: str, action: str, reason: str) -> GateEvaluation:
        return GateEvaluation(
            packet_id=packet.packet_id,
            admitted=admitted,
            label=label,
            action=action,
            reason=reason,
            unit_cost_decreases=unit_cost_decreases,
            demand_increases=demand_increases,
            burden_worsens=burden_worsens,
            apparent_capability_improves=apparent_capability_improves,
            net_capability_improves=net_capability_improves,
            packet=packet,
        )

    if packet.claims_claim_or_public_movement:
        return evaluation(
            False,
            "BLOCKED_GOVERNANCE_OR_PUBLIC_POSTURE_SHORTCUT",
            "block",
            "The Jevons gate cannot move claims, canon, public posture, or publication state.",
        )
    if packet.imports_source_side_growth:
        return evaluation(
            False,
            "REJECTED_SOURCE_SIDE_POSSIBILITY_GROWTH_IMPORT",
            "route_out",
            "TaF owns capability/finality accounting, not source-side possibility growth.",
        )
    if not packet.fixed_region_menu:
        return evaluation(
            False,
            "REJECTED_UNFIXED_REGION_OR_MENU",
            "reject",
            "Region/access profile and operation menu must be fixed before pair selection.",
        )
    if not packet.operation_named:
        return evaluation(
            False,
            "REJECTED_UNNAMED_OPERATION",
            "reject",
            "The operation whose unit cost changes must be named.",
        )
    if not packet.demand_response_predeclared:
        return evaluation(
            False,
            "REJECTED_HIDDEN_DEMAND_RESPONSE",
            "reject",
            "Demand response must be predeclared or measured, not imported as a hidden label.",
        )
    if not packet.burden_predeclared or packet.post_hoc_burden_variable:
        return evaluation(
            False,
            "REJECTED_POST_HOC_BURDEN_VARIABLE",
            "reject",
            "The aggregate burden or reversal-debt quantity must be fixed before pair selection.",
        )
    if not packet.positive_control_present or not packet.negative_control_present:
        return evaluation(
            False,
            "REJECTED_MISSING_CONTROLS",
            "reject",
            "The gate needs both net-improvement and rebound-erasure controls.",
        )
    if not unit_cost_decreases:
        return evaluation(
            False,
            "REJECTED_NO_UNIT_COST_DECREASE",
            "reject",
            "The Jevons gate is only triggered by a lower unit cost.",
        )
    if not apparent_capability_improves:
        return evaluation(
            False,
            "REJECTED_NO_APPARENT_UNIT_EFFICIENCY_IMPROVEMENT",
            "reject",
            "There is no apparent improvement to audit after demand response.",
        )

    rebound_concern = demand_increases and (
        burden_worsens or not net_capability_improves
    )
    if rebound_concern and packet.resource_accounting_explains_split:
        return evaluation(
            False,
            "ABSORBED_BY_RESOURCE_DEMAND_ACCOUNTING",
            "absorb",
            "The apparent capability/finality improvement disappears once total demand and burden are counted.",
        )
    if rebound_concern and packet.independent_finality_witness:
        return evaluation(
            True,
            "ADMITTED_REBOUND_CAPABILITY_REVIEW_TARGET",
            "review_only",
            "The packet has a predeclared finality witness not explained by ordinary resource-demand accounting.",
        )
    if rebound_concern:
        return evaluation(
            False,
            "REJECTED_UNWITNESSED_REBOUND_RESIDUAL",
            "reject",
            "A worsened net packet needs an independent finality witness after resource accounting.",
        )
    if net_capability_improves:
        return evaluation(
            True,
            "NET_IMPROVEMENT_AFTER_DEMAND_RESPONSE",
            "positive_control",
            "Lower unit cost remains a net capability improvement after demand response is modeled.",
        )
    return evaluation(
        False,
        "NO_REBOUND_CAPABILITY_RESIDUE",
        "no_action",
        "Demand response changes usage but does not create a net capability split.",
    )


def run() -> dict[str, Any]:
    evaluations = tuple(evaluate_packet(packet) for packet in example_packets())
    by_id = {item.packet_id: item for item in evaluations}
    admitted = tuple(item.packet_id for item in evaluations if item.admitted)
    absorbed = tuple(
        item.packet_id
        for item in evaluations
        if item.label == "ABSORBED_BY_RESOURCE_DEMAND_ACCOUNTING"
    )
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "packet_evaluations": [
            {
                "packet_id": item.packet_id,
                "admitted": item.admitted,
                "label": item.label,
                "action": item.action,
                "reason": item.reason,
                "unit_cost_decreases": item.unit_cost_decreases,
                "demand_increases": item.demand_increases,
                "burden_worsens": item.burden_worsens,
                "apparent_capability_improves": item.apparent_capability_improves,
                "net_capability_improves": item.net_capability_improves,
                "packet": asdict(item.packet),
            }
            for item in evaluations
        ],
        "overall_verdict": {
            "verdict": VERDICT,
            "net_improvement_control_admitted": by_id[
                "unit_efficiency_positive_control"
            ].admitted,
            "resource_demand_absorber_fired": bool(absorbed),
            "resource_demand_absorbed_packet_ids": absorbed,
            "synthetic_future_review_target_admitted": (
                "synthetic_finality_review_target" in admitted
            ),
            "formal_t_number_created": False,
            "test_registry_movement": False,
            "claim_movement": False,
            "canon_or_public_posture_movement": False,
            "cross_repo_movement": False,
        },
        "recommended_next": [
            "Use this pre-T gate before numbering a Jevons rebound packet.",
            "Number a future test only when a concrete packet needs a recorded result.",
            "Treat ordinary resource-demand accounting as the default absorber.",
            "Route source-side possibility-growth interpretations outside TaF.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def main() -> None:
    print(json.dumps(run(), indent=2))


if __name__ == "__main__":
    main()
