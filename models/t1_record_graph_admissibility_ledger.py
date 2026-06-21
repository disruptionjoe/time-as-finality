"""T141: T1 record-graph admissibility ledger for H7.

This grounds the T124 reverse-edge audit on an explicit record substrate rather
than on route-level summaries alone. The question is whether strict D1
increases on the T1-style causal-record graph ever acquire a constructor-
impossible reverse once the full record state and observer boundary are named.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.constructor_admissibility_grounding_audit import (
    CONSTRUCTOR_IMPOSSIBLE,
    REJECTED_REVERSIBLE,
    RESOURCE_ACCOUNTING_ONLY,
    RESOURCE_CONSUMING_POSSIBLE,
    REVERSIBLE_POSSIBLE,
)
from models.t1_record_graph import CausalRecordGraph, Observer, Record


@dataclass(frozen=True)
class RecordGraphLedgerCase:
    case_id: str
    source: str
    graph: CausalRecordGraph
    proposition: str
    value: str
    threshold: int
    before_observer: Observer
    after_observer: Observer
    before_event: str
    after_event: str
    forward_edge: str
    accounting_boundary: str
    forward_status: str
    reverse_edge: str
    reverse_status: str
    reverse_blocker: str
    named_resource_or_condition: str
    verdict: str
    reason: str


@dataclass(frozen=True)
class RecordGraphLedgerAudit:
    case_id: str
    source: str
    before_profile: tuple[int, int, int, int]
    after_profile: tuple[int, int, int, int]
    strict_forward_increase: bool
    forward_status: str
    reverse_status: str
    reverse_classified: bool
    named_resource_or_condition: str
    permits_unqualified_physical_arrow: bool
    verdict: str
    reason: str


@dataclass(frozen=True)
class T141Result:
    audits: tuple[RecordGraphLedgerAudit, ...]
    strict_increase_cases_have_no_constructor_impossible_reverse: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def _base_graph() -> CausalRecordGraph:
    graph = CausalRecordGraph()
    for event in ("a", "a_copy", "observe"):
        graph.add_event(event)
    graph.add_causal_edge("a", "a_copy")
    graph.add_causal_edge("a_copy", "observe")
    graph.add_record(Record("ra1", "A", "true", "a", "ha1", erasure_cost=1.0))
    graph.add_record(Record("ra2", "A", "true", "a_copy", "ha2", erasure_cost=2.0))
    return graph


def _copy_graph() -> CausalRecordGraph:
    graph = CausalRecordGraph()
    for event in ("a", "a_copy", "a_copy2", "observe"):
        graph.add_event(event)
    graph.add_causal_edge("a", "a_copy")
    graph.add_causal_edge("a_copy", "a_copy2")
    graph.add_causal_edge("a_copy2", "observe")
    graph.add_record(Record("ra1", "A", "true", "a", "ha1", erasure_cost=1.0))
    graph.add_record(Record("ra2", "A", "true", "a_copy", "ha2", erasure_cost=2.0))
    graph.add_record(Record("ra3", "A", "true", "a_copy2", "ha3", erasure_cost=3.0))
    return graph


def _branch_graph() -> CausalRecordGraph:
    graph = CausalRecordGraph()
    for event in ("a", "a_copy", "a_branch", "observe"):
        graph.add_event(event)
    graph.add_causal_edge("a", "a_copy")
    graph.add_causal_edge("a_copy", "observe")
    graph.add_causal_edge("a_branch", "observe")
    graph.add_record(Record("ra1", "A", "true", "a", "ha1", erasure_cost=1.0))
    graph.add_record(Record("ra2", "A", "true", "a_copy", "ha2", erasure_cost=2.0))
    graph.add_record(Record("ra3", "A", "true", "a_branch", "ha3", erasure_cost=3.0))
    return graph


def record_graph_cases() -> tuple[RecordGraphLedgerCase, ...]:
    base = _base_graph()
    limited = Observer("O_limited", "observe", frozenset({"ha1"}))
    full = Observer("O_full", "observe", frozenset({"ha1", "ha2"}))

    copy_graph = _copy_graph()
    copy_observer = Observer("O_copy", "observe", frozenset({"ha1", "ha2", "ha3"}))

    branch_graph = _branch_graph()
    branch_observer = Observer("O_branch", "observe", frozenset({"ha1", "ha2", "ha3"}))

    return (
        RecordGraphLedgerCase(
            case_id="access_grant_existing_record",
            source="T1 observer boundary change",
            graph=base,
            proposition="A",
            value="true",
            threshold=2,
            before_observer=limited,
            after_observer=full,
            before_event="observe",
            after_event="observe",
            forward_edge="grant observer access to an already existing record holder",
            accounting_boundary="same record graph, same active records, changed observer boundary",
            forward_status=REVERSIBLE_POSSIBLE,
            reverse_edge="revoke observer access to that holder",
            reverse_status=REVERSIBLE_POSSIBLE,
            reverse_blocker="none when access-control state is included",
            named_resource_or_condition="none",
            verdict=REJECTED_REVERSIBLE,
            reason=(
                "The strict D1 increase is boundary-relative bookkeeping, not a "
                "physical arrow. The reverse is an ordinary access-policy change."
            ),
        ),
        RecordGraphLedgerCase(
            case_id="copy_to_fresh_holder",
            source="T1 independent-holder copy",
            graph=copy_graph,
            proposition="A",
            value="true",
            threshold=3,
            before_observer=copy_observer,
            after_observer=copy_observer,
            before_event="a_copy",
            after_event="observe",
            forward_edge="copy an active record into a fresh accessible holder",
            accounting_boundary="same record graph with blank-holder supply and explicit erasure costs",
            forward_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_edge="erase the fresh copy and return the observer to the pre-copy support level",
            reverse_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_blocker="requires paying the copy's erasure cost and accounting for blank-holder use",
            named_resource_or_condition="fresh holder capacity and erasure work",
            verdict=RESOURCE_ACCOUNTING_ONLY,
            reason=(
                "The D1 increase is real on the substrate, but its reverse is "
                "not constructor-impossible. It is an erase-or-overwrite step "
                "with named resource accounting."
            ),
        ),
        RecordGraphLedgerCase(
            case_id="branch_spread_copy",
            source="T1 branch-robustness spread",
            graph=branch_graph,
            proposition="A",
            value="true",
            threshold=2,
            before_observer=branch_observer,
            after_observer=branch_observer,
            before_event="a_copy",
            after_event="observe",
            forward_edge="copy a record onto an additional incomparable causal branch",
            accounting_boundary="same record graph with explicit branch-support holder and erasure costs",
            forward_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_edge="erase the branch copy and remove the additional branch support",
            reverse_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_blocker="requires deleting the extra branch record under the same erasure ledger",
            named_resource_or_condition="fresh branch-support holder and erasure work",
            verdict=RESOURCE_ACCOUNTING_ONLY,
            reason=(
                "Branch robustness can increase on the T1 graph, but the reverse "
                "is still a named erasure action rather than a constructor "
                "impossibility."
            ),
        ),
        RecordGraphLedgerCase(
            case_id="access_loss_without_erasure_control",
            source="T1 local access-loss control",
            graph=base,
            proposition="A",
            value="true",
            threshold=2,
            before_observer=full,
            after_observer=limited,
            before_event="observe",
            after_event="observe",
            forward_edge="revoke access to one holder while records remain active",
            accounting_boundary="same record graph, same active records, changed observer boundary",
            forward_status=REVERSIBLE_POSSIBLE,
            reverse_edge="restore access to the same holder",
            reverse_status=REVERSIBLE_POSSIBLE,
            reverse_blocker="none when access-control state is included",
            named_resource_or_condition="none",
            verdict=REJECTED_REVERSIBLE,
            reason=(
                "This is the T1 control that separates local access loss from "
                "physical erasure. It is reversible and should not be promoted "
                "as an arrow-bearing edge."
            ),
        ),
    )


def audit_case(case: RecordGraphLedgerCase) -> RecordGraphLedgerAudit:
    before_profile = case.graph.finality_profile(
        case.before_observer,
        case.proposition,
        case.value,
        threshold=case.threshold,
        event=case.before_event,
    )
    after_profile = case.graph.finality_profile(
        case.after_observer,
        case.proposition,
        case.value,
        threshold=case.threshold,
        event=case.after_event,
    )
    strict_forward_increase = (
        before_profile.no_more_final_than(after_profile)
        and before_profile.as_tuple() != after_profile.as_tuple()
    )
    return RecordGraphLedgerAudit(
        case_id=case.case_id,
        source=case.source,
        before_profile=before_profile.as_tuple(),
        after_profile=after_profile.as_tuple(),
        strict_forward_increase=strict_forward_increase,
        forward_status=case.forward_status,
        reverse_status=case.reverse_status,
        reverse_classified=bool(case.reverse_edge and case.reverse_status),
        named_resource_or_condition=case.named_resource_or_condition,
        permits_unqualified_physical_arrow=False,
        verdict=case.verdict,
        reason=case.reason,
    )


def run_t141_analysis() -> T141Result:
    audits = tuple(audit_case(case) for case in record_graph_cases())
    strict_increase_cases = tuple(audit for audit in audits if audit.strict_forward_increase)
    no_constructor_reverse = all(
        audit.reverse_status != CONSTRUCTOR_IMPOSSIBLE for audit in strict_increase_cases
    )
    return T141Result(
        audits=audits,
        strict_increase_cases_have_no_constructor_impossible_reverse=(
            no_constructor_reverse
        ),
        strongest_claim=(
            "On the explicit T1 causal-record graph, the tested strict D1 "
            "increases do not acquire constructor-impossible reverses under full "
            "state accounting. They are either reversible observer-boundary "
            "changes or resource-accounting edges that depend on fresh holders "
            "and erasure work."
        ),
        improved=(
            "T141 grounds the T124 reverse-edge warning on an actual record "
            "substrate. H7 no longer needs to rely only on route-level analogies "
            "to see the problem: even concrete T1 support and branch-robustness "
            "gains remain definalizable once access state, holders, and erasure "
            "actions are named."
        ),
        weakened=(
            "This weakens the current H7 upgrade path again. The T1 substrate "
            "does not supply a constructor-impossible reverse for record "
            "stabilization; it supplies bookkeeping reversals and "
            "resource-accounted definalization moves."
        ),
        falsification_condition=(
            "T141 fails only if a T1-style record-graph transformation produces "
            "a strict D1 increase whose reverse is constructor-impossible under "
            "the same full holder, access, and erasure accounting, rather than "
            "merely resource-consuming or observer-boundary-relative."
        ),
        h7_update=(
            "Add T141 to H7: the explicit T1 record substrate still does not "
            "ground constructor-impossible definalization. Treat current T1/T124 "
            "survivors as reversible-boundary or resource-accounting edges."
        ),
        claim_ledger_update=(
            "T141 grounds the H7 blocker on the T1 record graph. Access grants "
            "are reversible boundary changes; holder and branch-support gains "
            "require fresh-holder/erasure accounting; no tested strict T1 "
            "increase has a constructor-impossible reverse."
        ),
        open_blocker=(
            "The repo still lacks a record substrate where deleting or "
            "definalizing a stabilized record is impossible for substrate-native "
            "reasons rather than costly, omitted, or boundary-relative."
        ),
        suggested_next=(
            "Either formalize a stronger substrate-native impossibility notion "
            "for T1-style records, or calibrate the surviving edges directly "
            "against standard free-energy and erasure accounting."
        ),
    )


def t141_result_to_dict(result: T141Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "case_id": audit.case_id,
                "source": audit.source,
                "before_profile": audit.before_profile,
                "after_profile": audit.after_profile,
                "strict_forward_increase": audit.strict_forward_increase,
                "forward_status": audit.forward_status,
                "reverse_status": audit.reverse_status,
                "reverse_classified": audit.reverse_classified,
                "named_resource_or_condition": audit.named_resource_or_condition,
                "permits_unqualified_physical_arrow": (
                    audit.permits_unqualified_physical_arrow
                ),
                "verdict": audit.verdict,
                "reason": audit.reason,
            }
            for audit in result.audits
        ],
        "strict_increase_cases_have_no_constructor_impossible_reverse": (
            result.strict_increase_cases_have_no_constructor_impossible_reverse
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t141_result_to_dict(run_t141_analysis()), indent=2))
