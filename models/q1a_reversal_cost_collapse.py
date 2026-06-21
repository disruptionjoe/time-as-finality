"""T118: reversal-cost collapse audit for the current fixed-data Q1A family.

T105 reduced the surviving fixed-data Q1A branch to audited accessible
provenance support plus partition visibility. T109 then closed branch support
as an escape hatch. T118 tests the last unused D1 dimension in this witness
language: reversal cost.

The current Q1A family has no physical undo dynamics, no calibrated work
meter, and no control protocol. The only admissible reversal-cost proxy left
inside the fixed-data gate is therefore the number of independent accessible
record classes that would have to be erased or overwritten to destroy the
audited record. T118 checks whether even that proxy carries any verdict
content beyond audited accessible support itself.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.q1a_accessible_class_sufficiency import run_t105_analysis
from models.q1a_fixed_data_witness import run_t103_analysis


@dataclass(frozen=True)
class ReversalCostAuditCase:
    case_id: str
    accessible_provenance_support: int | None
    d1_verdict: str
    reversal_cost_proxy: int | None
    proxy_withheld: bool


@dataclass(frozen=True)
class T118Result:
    visible_cases: tuple[ReversalCostAuditCase, ...]
    hidden_partition_case: ReversalCostAuditCase
    proxy_defined_exactly_when_partition_visible: bool
    proxy_equals_support_on_all_visible_cases: bool
    proxy_splits_same_support_class: bool
    branch_history_changes_leave_fixed_data_gate: bool
    any_load_bearing_reversal_cost_witness_in_current_family: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1a_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _reversal_cost_proxy(accessible_provenance_support: int | None) -> int | None:
    if accessible_provenance_support is None:
        return None
    return accessible_provenance_support


def _to_audit_case(case: object) -> ReversalCostAuditCase:
    support = getattr(case, "accessible_provenance_support")
    proxy = _reversal_cost_proxy(support)
    return ReversalCostAuditCase(
        case_id=getattr(case, "case_id"),
        accessible_provenance_support=support,
        d1_verdict=getattr(case, "d1_verdict"),
        reversal_cost_proxy=proxy,
        proxy_withheld=(proxy is None),
    )


def run_t118_analysis() -> T118Result:
    t105 = run_t105_analysis()
    visible_cases = tuple(_to_audit_case(case) for case in t105.visible_cases)
    hidden_case = _to_audit_case(t105.hidden_partition_case)

    proxy_defined_exactly_when_partition_visible = (
        all(case.reversal_cost_proxy is not None for case in visible_cases)
        and hidden_case.reversal_cost_proxy is None
    )
    proxy_equals_support_on_all_visible_cases = all(
        case.reversal_cost_proxy == case.accessible_provenance_support
        for case in visible_cases
    )

    support_to_proxy_values: dict[int, set[int]] = {}
    for case in visible_cases:
        support = case.accessible_provenance_support
        proxy = case.reversal_cost_proxy
        if support is None or proxy is None:
            continue
        support_to_proxy_values.setdefault(support, set()).add(proxy)
    proxy_splits_same_support_class = any(
        len(proxy_values) > 1 for proxy_values in support_to_proxy_values.values()
    )

    t103 = run_t103_analysis()
    branch_history_control = next(
        case for case in t103.cases if case.case_id == "branch_history_changed_control"
    )
    branch_history_changes_leave_fixed_data_gate = (
        branch_history_control.gate_verdict == "reject_standard_data_changed"
    )

    any_load_bearing_reversal_cost_witness_in_current_family = (
        not proxy_defined_exactly_when_partition_visible
        or not proxy_equals_support_on_all_visible_cases
        or proxy_splits_same_support_class
        or not branch_history_changes_leave_fixed_data_gate
    )

    return T118Result(
        visible_cases=visible_cases,
        hidden_partition_case=hidden_case,
        proxy_defined_exactly_when_partition_visible=(
            proxy_defined_exactly_when_partition_visible
        ),
        proxy_equals_support_on_all_visible_cases=(
            proxy_equals_support_on_all_visible_cases
        ),
        proxy_splits_same_support_class=proxy_splits_same_support_class,
        branch_history_changes_leave_fixed_data_gate=(
            branch_history_changes_leave_fixed_data_gate
        ),
        any_load_bearing_reversal_cost_witness_in_current_family=(
            any_load_bearing_reversal_cost_witness_in_current_family
        ),
        strongest_claim=(
            "Reversal cost is not a surviving independent lever in the current "
            "fixed-data Q1A family. Once the witness language is restricted to "
            "already formed records with fixed ordinary quantum-side summaries, "
            "the only admissible reversal-cost proxy is how many audited "
            "accessible provenance classes would need to be erased or "
            "overwritten. That proxy is identical to accessible provenance "
            "support whenever the partition is visible and is withheld when the "
            "partition is hidden. So reversal cost adds no verdict content "
            "beyond the T105 support count in the present family."
        ),
        improved=(
            "T118 closes the last obvious Q1A fixed-data loophole. The repo can "
            "now say explicitly that the current witness family carries no "
            "independent reversal-cost structure, not even at the level of an "
            "admissible proxy."
        ),
        weakened=(
            "This weakens Q1A again. In the present fixed-data regime all live "
            "verdict content is exhausted by audited accessible provenance "
            "support plus partition visibility. Reversal-cost language should "
            "not be presented as extra measurement structure unless it is tied "
            "to a physically calibrated undo observable outside this collapsed "
            "counting regime."
        ),
        falsification_condition=(
            "T118 fails only if an admissible fixed-data witness in the current "
            "Q1A language exhibits different reversal-cost values at the same "
            "audited accessible provenance-support count while ordinary "
            "quantum-side summaries stay fixed, or if a physically calibrated "
            "undo observable becomes available that is neither post hoc nor "
            "equivalent to counting audited accessible record classes."
        ),
        q1a_update=(
            "Q1A should not cite reversal cost as a live independent witness "
            "dimension in the current fixed-data family. At present the only "
            "admissible reversal-cost proxy is the audited accessible "
            "provenance-support count itself, with withholding when the "
            "partition is unavailable."
        ),
        claim_ledger_update=(
            "Add T118 to Q1A: reversal cost does not presently escape the "
            "accessible-class reduction. In the current fixed-data witness "
            "family its only admissible proxy is the number of audited "
            "accessible provenance classes that would need to be erased or "
            "overwritten, so it adds no independent verdict content."
        ),
        open_blocker=(
            "The repo still lacks a finite quantum witness with a physically "
            "calibrated undo or erasure observable that can vary while "
            "decoherence, fragment-information summaries, raw redundancy, "
            "branch/history availability, and audited accessible support stay "
            "fixed."
        ),
        recommended_next=(
            "Either construct a genuinely dynamic witness with a predeclared "
            "undo observable that survives the fixed-data gate, or state "
            "plainly in paper-facing summaries that current Q1A evidence is "
            "fully reduced to audited record-accounting discipline."
        ),
    )


def t118_result_to_dict(result: T118Result) -> dict[str, object]:
    return {
        "visible_cases": [
            {
                "case_id": case.case_id,
                "accessible_provenance_support": case.accessible_provenance_support,
                "d1_verdict": case.d1_verdict,
                "reversal_cost_proxy": case.reversal_cost_proxy,
                "proxy_withheld": case.proxy_withheld,
            }
            for case in result.visible_cases
        ],
        "hidden_partition_case": {
            "case_id": result.hidden_partition_case.case_id,
            "accessible_provenance_support": (
                result.hidden_partition_case.accessible_provenance_support
            ),
            "d1_verdict": result.hidden_partition_case.d1_verdict,
            "reversal_cost_proxy": result.hidden_partition_case.reversal_cost_proxy,
            "proxy_withheld": result.hidden_partition_case.proxy_withheld,
        },
        "proxy_defined_exactly_when_partition_visible": (
            result.proxy_defined_exactly_when_partition_visible
        ),
        "proxy_equals_support_on_all_visible_cases": (
            result.proxy_equals_support_on_all_visible_cases
        ),
        "proxy_splits_same_support_class": result.proxy_splits_same_support_class,
        "branch_history_changes_leave_fixed_data_gate": (
            result.branch_history_changes_leave_fixed_data_gate
        ),
        "any_load_bearing_reversal_cost_witness_in_current_family": (
            result.any_load_bearing_reversal_cost_witness_in_current_family
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1a_update": result.q1a_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t118_result_to_dict(run_t118_analysis()), indent=2))
