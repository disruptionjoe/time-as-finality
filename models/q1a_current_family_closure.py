"""T144: closure audit for the current fixed-data Q1A family.

T105 showed that current Q1A verdicts collapse to audited accessible
provenance support plus partition visibility. T109 and T118 then killed the
obvious branch-support and reversal-cost escape hatches. T144 packages those
separate negative results into one executable closure check.

This is not a no-go theorem for quantum measurement. It is only a current-family
audit: within the present already-formed-record witness language, no declared
D1 dimension carries verdict content beyond the T105 closure key.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.q1a_accessible_class_sufficiency import run_t105_analysis
from models.q1a_branch_support_collapse import run_t109_analysis
from models.q1a_fixed_data_witness import D1_INDEPENDENT_SUPPORT_THRESHOLD
from models.q1a_reversal_cost_collapse import run_t118_analysis


@dataclass(frozen=True)
class ClosureCase:
    case_id: str
    partition_visible: bool
    accessible_provenance_support: int | None
    raw_accessible_redundancy: int
    d1_verdict: str
    closure_verdict: str
    rooted_branch_support: int | None
    reversal_cost_proxy: int | None
    classifier_matches_d1: bool

    def closure_key(self) -> tuple[bool, int | None]:
        return (self.partition_visible, self.accessible_provenance_support)


@dataclass(frozen=True)
class ClosureFiber:
    partition_visible: bool
    accessible_provenance_support: int | None
    case_count: int
    d1_verdicts: tuple[str, ...]
    raw_accessible_redundancies: tuple[int, ...]
    rooted_branch_support_values: tuple[int, ...]
    reversal_cost_proxy_values: tuple[int, ...]


@dataclass(frozen=True)
class T144Result:
    visible_cases: tuple[ClosureCase, ...]
    hidden_partition_case: ClosureCase
    fibers: tuple[ClosureFiber, ...]
    closure_classifier_matches_d1: bool
    d1_factors_through_closure_key: bool
    branch_support_factors_through_closure_key: bool
    reversal_cost_factors_through_closure_key: bool
    raw_redundancy_is_not_sufficient: bool
    branch_support_load_bearing: bool
    reversal_cost_load_bearing: bool
    current_family_closed_under_declared_dimensions: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1a_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _closure_verdict(partition_visible: bool, support: int | None) -> str:
    if not partition_visible or support is None:
        return "withhold_partition_unavailable"
    if support >= D1_INDEPENDENT_SUPPORT_THRESHOLD:
        return "finalized"
    return "not_finalized"


def _unique_sorted(values: list[object]) -> tuple[object, ...]:
    return tuple(sorted(set(values), key=lambda item: str(item)))


def _make_visible_cases() -> tuple[ClosureCase, ...]:
    t105 = run_t105_analysis()
    t109_by_id = {case.case_id: case for case in run_t109_analysis().visible_cases}
    t118_by_id = {case.case_id: case for case in run_t118_analysis().visible_cases}

    cases: list[ClosureCase] = []
    for case in t105.visible_cases:
        branch_case = t109_by_id[case.case_id]
        reversal_case = t118_by_id[case.case_id]
        closure_verdict = _closure_verdict(True, case.accessible_provenance_support)
        cases.append(
            ClosureCase(
                case_id=case.case_id,
                partition_visible=True,
                accessible_provenance_support=case.accessible_provenance_support,
                raw_accessible_redundancy=case.raw_accessible_redundancy,
                d1_verdict=case.d1_verdict,
                closure_verdict=closure_verdict,
                rooted_branch_support=branch_case.rooted_branch_support,
                reversal_cost_proxy=reversal_case.reversal_cost_proxy,
                classifier_matches_d1=(closure_verdict == case.d1_verdict),
            )
        )
    return tuple(cases)


def _make_hidden_case() -> ClosureCase:
    t105_hidden = run_t105_analysis().hidden_partition_case
    t118_hidden = run_t118_analysis().hidden_partition_case
    closure_verdict = _closure_verdict(False, t105_hidden.accessible_provenance_support)
    return ClosureCase(
        case_id=t105_hidden.case_id,
        partition_visible=False,
        accessible_provenance_support=t105_hidden.accessible_provenance_support,
        raw_accessible_redundancy=t105_hidden.raw_accessible_redundancy,
        d1_verdict=t105_hidden.d1_verdict,
        closure_verdict=closure_verdict,
        rooted_branch_support=None,
        reversal_cost_proxy=t118_hidden.reversal_cost_proxy,
        classifier_matches_d1=(closure_verdict == t105_hidden.d1_verdict),
    )


def _fibers(cases: tuple[ClosureCase, ...]) -> tuple[ClosureFiber, ...]:
    grouped: dict[tuple[bool, int | None], list[ClosureCase]] = {}
    for case in cases:
        grouped.setdefault(case.closure_key(), []).append(case)

    fibers: list[ClosureFiber] = []
    for key in sorted(grouped, key=lambda item: (item[0], -1 if item[1] is None else item[1])):
        members = grouped[key]
        branch_values = [
            case.rooted_branch_support
            for case in members
            if case.rooted_branch_support is not None
        ]
        reversal_values = [
            case.reversal_cost_proxy
            for case in members
            if case.reversal_cost_proxy is not None
        ]
        fibers.append(
            ClosureFiber(
                partition_visible=key[0],
                accessible_provenance_support=key[1],
                case_count=len(members),
                d1_verdicts=_unique_sorted([case.d1_verdict for case in members]),
                raw_accessible_redundancies=_unique_sorted(
                    [case.raw_accessible_redundancy for case in members]
                ),
                rooted_branch_support_values=_unique_sorted(branch_values),
                reversal_cost_proxy_values=_unique_sorted(reversal_values),
            )
        )
    return tuple(fibers)


def _all_fibers_singleton(
    fibers: tuple[ClosureFiber, ...],
    attribute: str,
) -> bool:
    return all(len(getattr(fiber, attribute)) <= 1 for fiber in fibers)


def run_t144_analysis() -> T144Result:
    visible_cases = _make_visible_cases()
    hidden_case = _make_hidden_case()
    all_cases = visible_cases + (hidden_case,)
    fibers = _fibers(all_cases)

    t105 = run_t105_analysis()
    t109 = run_t109_analysis()
    t118 = run_t118_analysis()

    closure_classifier_matches_d1 = all(case.classifier_matches_d1 for case in all_cases)
    d1_factors_through_closure_key = _all_fibers_singleton(fibers, "d1_verdicts")
    branch_support_factors_through_closure_key = _all_fibers_singleton(
        fibers, "rooted_branch_support_values"
    )
    reversal_cost_factors_through_closure_key = _all_fibers_singleton(
        fibers, "reversal_cost_proxy_values"
    )
    branch_support_load_bearing = t109.any_load_bearing_branch_support_witness_in_current_family
    reversal_cost_load_bearing = (
        t118.any_load_bearing_reversal_cost_witness_in_current_family
    )
    current_family_closed_under_declared_dimensions = (
        closure_classifier_matches_d1
        and d1_factors_through_closure_key
        and branch_support_factors_through_closure_key
        and reversal_cost_factors_through_closure_key
        and t105.raw_redundancy_is_not_sufficient
        and not branch_support_load_bearing
        and not reversal_cost_load_bearing
    )

    return T144Result(
        visible_cases=visible_cases,
        hidden_partition_case=hidden_case,
        fibers=fibers,
        closure_classifier_matches_d1=closure_classifier_matches_d1,
        d1_factors_through_closure_key=d1_factors_through_closure_key,
        branch_support_factors_through_closure_key=(
            branch_support_factors_through_closure_key
        ),
        reversal_cost_factors_through_closure_key=(
            reversal_cost_factors_through_closure_key
        ),
        raw_redundancy_is_not_sufficient=t105.raw_redundancy_is_not_sufficient,
        branch_support_load_bearing=branch_support_load_bearing,
        reversal_cost_load_bearing=reversal_cost_load_bearing,
        current_family_closed_under_declared_dimensions=(
            current_family_closed_under_declared_dimensions
        ),
        strongest_claim=(
            "The current enumerated Q1A fixed-data family is closed under the "
            "declared D1 dimensions: the D1 verdict factors through exactly "
            "the T105 closure key, namely partition visibility plus audited "
            "accessible provenance-support count. Raw accessible redundancy "
            "cannot replace that key, but branch support and reversal-cost "
            "proxies add no independent verdict content in this family."
        ),
        improved=(
            "T144 converts the scattered T105/T109/T118 demotions into one "
            "reusable closure test. A reviewer can now see the exact quotient "
            "that preserves all current Q1A verdict content and the exact "
            "condition a future Q1A witness must violate."
        ),
        weakened=(
            "This weakens Q1A by removing the last internal ambiguity in the "
            "current family. Q1A is not presently a measurement-dynamics claim; "
            "it is an access/provenance bookkeeping rule over already formed "
            "records unless a future witness splits the closure key."
        ),
        falsification_condition=(
            "T144 fails if an admissible Q1A witness keeps ordinary "
            "quantum-side summaries fixed, shares the same access cut and "
            "provenance-aware partition, matches the audited accessible "
            "support count, and still changes the D1 verdict through a "
            "predeclared physical dimension. It also fails if branch support "
            "or a calibrated undo/erasure observable varies at fixed closure "
            "key without changing standard data."
        ),
        q1a_update=(
            "Q1A should be stated as current-family closed: all present "
            "verdict content is captured by partition visibility plus audited "
            "accessible provenance support. Reopen Q1A only with a same-closure "
            "key verdict split or with a physical partition rule that cannot be "
            "imported by the neighboring framework without adding new physics."
        ),
        claim_ledger_update=(
            "Add T144 to Q1A: the current fixed-data family is closed under "
            "accessible support, branch support, and reversal-cost audits. The "
            "surviving quotient is partition visibility plus audited "
            "accessible provenance-support count; no current internal Q1A "
            "dimension escapes that quotient."
        ),
        open_blocker=(
            "The repo still lacks a physically grounded same-support Q1A "
            "witness: fixed standard quantum summaries, shared audited "
            "partition, same accessible provenance support, and a nonabsorbed "
            "D1 verdict split."
        ),
        recommended_next=(
            "Do not add another Q1A finite record toy model unless it targets "
            "the same-closure-key escape gate. If no such target is available, "
            "spend quantum effort on an external Q1B packet or leave Q1 for a "
            "different route."
        ),
    )


def _case_to_dict(case: ClosureCase) -> dict[str, object]:
    return {
        "case_id": case.case_id,
        "partition_visible": case.partition_visible,
        "accessible_provenance_support": case.accessible_provenance_support,
        "raw_accessible_redundancy": case.raw_accessible_redundancy,
        "d1_verdict": case.d1_verdict,
        "closure_verdict": case.closure_verdict,
        "rooted_branch_support": case.rooted_branch_support,
        "reversal_cost_proxy": case.reversal_cost_proxy,
        "classifier_matches_d1": case.classifier_matches_d1,
    }


def _fiber_to_dict(fiber: ClosureFiber) -> dict[str, object]:
    return {
        "partition_visible": fiber.partition_visible,
        "accessible_provenance_support": fiber.accessible_provenance_support,
        "case_count": fiber.case_count,
        "d1_verdicts": list(fiber.d1_verdicts),
        "raw_accessible_redundancies": list(fiber.raw_accessible_redundancies),
        "rooted_branch_support_values": list(fiber.rooted_branch_support_values),
        "reversal_cost_proxy_values": list(fiber.reversal_cost_proxy_values),
    }


def t144_result_to_dict(result: T144Result) -> dict[str, object]:
    return {
        "visible_cases": [_case_to_dict(case) for case in result.visible_cases],
        "hidden_partition_case": _case_to_dict(result.hidden_partition_case),
        "fibers": [_fiber_to_dict(fiber) for fiber in result.fibers],
        "closure_classifier_matches_d1": result.closure_classifier_matches_d1,
        "d1_factors_through_closure_key": result.d1_factors_through_closure_key,
        "branch_support_factors_through_closure_key": (
            result.branch_support_factors_through_closure_key
        ),
        "reversal_cost_factors_through_closure_key": (
            result.reversal_cost_factors_through_closure_key
        ),
        "raw_redundancy_is_not_sufficient": result.raw_redundancy_is_not_sufficient,
        "branch_support_load_bearing": result.branch_support_load_bearing,
        "reversal_cost_load_bearing": result.reversal_cost_load_bearing,
        "current_family_closed_under_declared_dimensions": (
            result.current_family_closed_under_declared_dimensions
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

    print(json.dumps(t144_result_to_dict(run_t144_analysis()), indent=2))
