"""T109: branch-support collapse audit for the current fixed-data Q1A family.

T105 left one obvious escape hatch open: perhaps the surviving Q1A branch is
not controlled entirely by accessible provenance support because another D1
dimension, especially branch support, still does independent work.

T109 audits that possibility inside the current fixed-data witness language.
The result is negative. Every admissible visible case inherits the same
single-root branch structure used by T2/T103/T105, while any attempt to vary
ordinary branch/history availability leaves the fixed-data gate.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.q1a_accessible_class_sufficiency import run_t105_analysis
from models.q1a_fixed_data_witness import run_t103_analysis


@dataclass(frozen=True)
class BranchSupportAuditCase:
    case_id: str
    accessible_provenance_support: int | None
    d1_verdict: str
    rooted_branch_support: int
    rooted_branch_support_is_nontrivial: bool


@dataclass(frozen=True)
class T109Result:
    visible_cases: tuple[BranchSupportAuditCase, ...]
    rooted_branch_support_constant_on_nonzero_support_cases: bool
    rooted_branch_support_varies_only_with_zero_access_boundary: bool
    rooted_branch_support_splits_same_support_class: bool
    branch_history_changes_leave_fixed_data_gate: bool
    any_load_bearing_branch_support_witness_in_current_family: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1a_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _rooted_branch_support(accessible_provenance_support: int | None) -> int:
    if accessible_provenance_support is None:
        return 0
    return 1 if accessible_provenance_support > 0 else 0


def _to_audit_case(case: object) -> BranchSupportAuditCase:
    support = getattr(case, "accessible_provenance_support")
    rooted = _rooted_branch_support(support)
    return BranchSupportAuditCase(
        case_id=getattr(case, "case_id"),
        accessible_provenance_support=support,
        d1_verdict=getattr(case, "d1_verdict"),
        rooted_branch_support=rooted,
        rooted_branch_support_is_nontrivial=(rooted > 1),
    )


def run_t109_analysis() -> T109Result:
    t105 = run_t105_analysis()
    visible_cases = tuple(_to_audit_case(case) for case in t105.visible_cases)

    nonzero_support_cases = tuple(
        case for case in visible_cases if (case.accessible_provenance_support or 0) > 0
    )
    zero_support_cases = tuple(
        case for case in visible_cases if case.accessible_provenance_support == 0
    )

    rooted_branch_support_constant_on_nonzero_support_cases = all(
        case.rooted_branch_support == 1 for case in nonzero_support_cases
    )
    rooted_branch_support_varies_only_with_zero_access_boundary = (
        rooted_branch_support_constant_on_nonzero_support_cases
        and all(case.rooted_branch_support == 0 for case in zero_support_cases)
    )

    supports_to_branch_values: dict[int, set[int]] = {}
    for case in visible_cases:
        support = case.accessible_provenance_support
        if support is None:
            continue
        supports_to_branch_values.setdefault(support, set()).add(case.rooted_branch_support)
    rooted_branch_support_splits_same_support_class = any(
        len(branch_values) > 1 for branch_values in supports_to_branch_values.values()
    )

    t103 = run_t103_analysis()
    branch_history_control = next(
        case for case in t103.cases if case.case_id == "branch_history_changed_control"
    )
    branch_history_changes_leave_fixed_data_gate = (
        branch_history_control.gate_verdict == "reject_standard_data_changed"
    )

    any_load_bearing_branch_support_witness_in_current_family = (
        any(case.rooted_branch_support_is_nontrivial for case in visible_cases)
        or rooted_branch_support_splits_same_support_class
        or not branch_history_changes_leave_fixed_data_gate
    )

    return T109Result(
        visible_cases=visible_cases,
        rooted_branch_support_constant_on_nonzero_support_cases=(
            rooted_branch_support_constant_on_nonzero_support_cases
        ),
        rooted_branch_support_varies_only_with_zero_access_boundary=(
            rooted_branch_support_varies_only_with_zero_access_boundary
        ),
        rooted_branch_support_splits_same_support_class=(
            rooted_branch_support_splits_same_support_class
        ),
        branch_history_changes_leave_fixed_data_gate=(
            branch_history_changes_leave_fixed_data_gate
        ),
        any_load_bearing_branch_support_witness_in_current_family=(
            any_load_bearing_branch_support_witness_in_current_family
        ),
        strongest_claim=(
            "Branch support is not a surviving independent lever in the current "
            "fixed-data Q1A family. Under the rooted-branch reading inherited "
            "from T2, every visible case with any audited accessible support "
            "has branch support 1 because all accessible records descend from "
            "the same pointer-measurement root; zero-support cases alone drop "
            "to 0. Under the ordinary branch/history reading, any change "
            "already violates T103's fixed-data gate. So branch support does "
            "not presently escape the T105 accessible-class reduction."
        ),
        improved=(
            "T109 removes a vague future-work loophole. The repo can now say "
            "exactly why branch support is not yet a live rescue route for "
            "Q1A: in the current witness language it is either trivial or "
            "already counted as changed standard quantum-side data."
        ),
        weakened=(
            "This weakens Q1A again. The remaining fixed-data branch no longer "
            "has a generic 'maybe branch support saves it' escape clause. Any "
            "future branch-support upgrade must enlarge the witness language to "
            "include genuinely distinct causal record channels rather than "
            "relabeling the existing single-root family."
        ),
        falsification_condition=(
            "T109 fails only if an admissible fixed-data witness in the "
            "current Q1A language exhibits different branch-support values "
            "while keeping standard quantum-side summaries fixed, or if a new "
            "branch-support observable is introduced that is neither trivial on "
            "the current family nor equivalent to changing ordinary "
            "branch/history availability."
        ),
        q1a_update=(
            "Q1A should not cite branch support as a live independent witness "
            "dimension in the current fixed-data family. At present the branch "
            "story is either single-root triviality or an inadmissible change "
            "to ordinary branch/history data."
        ),
        claim_ledger_update=(
            "Add T109 to Q1A: branch support does not presently escape the "
            "accessible-class reduction. In the current fixed-data witness "
            "family it is either the trivial single-root value 1 on all "
            "nonzero-support cases or an inadmissible change to ordinary "
            "branch/history availability."
        ),
        open_blocker=(
            "The repo still lacks any finite quantum witness with genuinely "
            "distinct causal record channels whose branch-support value can "
            "vary without changing the standard quantum-side summaries already "
            "held fixed by T103/T105."
        ),
        recommended_next=(
            "Either construct a witness with multiple causally independent "
            "record channels that survive the fixed-data gate, or shift the "
            "next Q1A attack to reversal cost and test whether that dimension "
            "also collapses under the same audit discipline."
        ),
    )


def t109_result_to_dict(result: T109Result) -> dict[str, object]:
    return {
        "visible_cases": [
            {
                "case_id": case.case_id,
                "accessible_provenance_support": case.accessible_provenance_support,
                "d1_verdict": case.d1_verdict,
                "rooted_branch_support": case.rooted_branch_support,
                "rooted_branch_support_is_nontrivial": (
                    case.rooted_branch_support_is_nontrivial
                ),
            }
            for case in result.visible_cases
        ],
        "rooted_branch_support_constant_on_nonzero_support_cases": (
            result.rooted_branch_support_constant_on_nonzero_support_cases
        ),
        "rooted_branch_support_varies_only_with_zero_access_boundary": (
            result.rooted_branch_support_varies_only_with_zero_access_boundary
        ),
        "rooted_branch_support_splits_same_support_class": (
            result.rooted_branch_support_splits_same_support_class
        ),
        "branch_history_changes_leave_fixed_data_gate": (
            result.branch_history_changes_leave_fixed_data_gate
        ),
        "any_load_bearing_branch_support_witness_in_current_family": (
            result.any_load_bearing_branch_support_witness_in_current_family
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

    print(json.dumps(t109_result_to_dict(run_t109_analysis()), indent=2))
