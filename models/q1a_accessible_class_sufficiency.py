"""T105: sufficient-statistic audit for the surviving fixed-data Q1A branch.

T103 showed that Q1A can change verdicts while the ordinary quantum-side
summaries stay fixed. T104 then showed that the strongest witness is absorbed
by provenance-aware Quantum Darwinism once the same audited partition is
shared.

T105 asks the next high-value question: after that absorption, how much
structure is really left in the current fixed-data Q1A branch? The answer
matters because if the verdict collapses to a single thresholded statistic,
then the remaining branch is narrower than "observer-relative measurement
theory" language suggests.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.q1a_fixed_data_witness import (
    D1_INDEPENDENT_SUPPORT_THRESHOLD,
    IndependenceStructure,
    WitnessCase,
    base_quantum_side,
    score_case,
)


FRAGMENTS = ("E1", "E2", "E3")


@dataclass(frozen=True)
class SupportCase:
    case_id: str
    accessible_fragments: frozenset[str]
    provenance_partition: tuple[tuple[str, ...], ...] | None
    access_to_partition: bool


@dataclass(frozen=True)
class SupportVerdict:
    case_id: str
    accessible_fragments: tuple[str, ...]
    raw_accessible_redundancy: int
    accessible_provenance_support: int | None
    d1_verdict: str
    support_classifier_verdict: str
    classifier_matches_d1: bool


@dataclass(frozen=True)
class T105Result:
    visible_cases: tuple[SupportVerdict, ...]
    hidden_partition_case: SupportVerdict
    classifier_matches_all_visible_cases: bool
    same_support_always_same_verdict: bool
    raw_redundancy_is_not_sufficient: bool
    external_distinctness_earned: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _set_partitions(items: tuple[str, ...]) -> tuple[tuple[tuple[str, ...], ...], ...]:
    if not items:
        return ((),)

    first = items[0]
    tail_partitions = _set_partitions(items[1:])
    seen: set[tuple[tuple[str, ...], ...]] = set()
    results: list[tuple[tuple[str, ...], ...]] = []

    for partition in tail_partitions:
        new_group_partition = tuple(
            sorted(tuple(sorted(group)) for group in partition + ((first,),))
        )
        if new_group_partition not in seen:
            seen.add(new_group_partition)
            results.append(new_group_partition)

        for index, group in enumerate(partition):
            expanded = list(partition)
            expanded[index] = tuple(sorted(group + (first,)))
            normalized = tuple(sorted(tuple(sorted(entry)) for entry in expanded))
            if normalized not in seen:
                seen.add(normalized)
                results.append(normalized)

    return tuple(results)


def _powerset(items: tuple[str, ...]) -> tuple[frozenset[str], ...]:
    subsets: list[frozenset[str]] = []
    for mask in range(1 << len(items)):
        subset = frozenset(
            item for bit_index, item in enumerate(items) if mask & (1 << bit_index)
        )
        subsets.append(subset)
    return tuple(subsets)


def _to_witness_case(case: SupportCase) -> WitnessCase:
    independence = (
        None
        if case.provenance_partition is None
        else IndependenceStructure(case.provenance_partition)
    )
    return WitnessCase(
        case_id=case.case_id,
        quantum_side=base_quantum_side(accessible_fragments=case.accessible_fragments),
        independence=independence,
        access_to_independence_partition=case.access_to_partition,
        expected_purpose="T105 support sufficiency audit case.",
    )


def _support_classifier_verdict(support: int | None, partition_visible: bool) -> str:
    if not partition_visible or support is None:
        return "withhold_partition_unavailable"
    if support >= D1_INDEPENDENT_SUPPORT_THRESHOLD:
        return "finalized"
    return "not_finalized"


def _score_case(case: SupportCase) -> SupportVerdict:
    baseline = base_quantum_side(accessible_fragments=case.accessible_fragments)
    witness_verdict = score_case(_to_witness_case(case), baseline)
    support = witness_verdict.independent_accessible_support
    classifier_verdict = _support_classifier_verdict(support, case.access_to_partition)
    return SupportVerdict(
        case_id=case.case_id,
        accessible_fragments=tuple(sorted(case.accessible_fragments)),
        raw_accessible_redundancy=baseline.accessible_raw_redundancy(),
        accessible_provenance_support=support,
        d1_verdict=witness_verdict.d1_verdict,
        support_classifier_verdict=classifier_verdict,
        classifier_matches_d1=(classifier_verdict == witness_verdict.d1_verdict),
    )


def visible_support_cases() -> tuple[SupportCase, ...]:
    cases: list[SupportCase] = []
    for subset in _powerset(FRAGMENTS):
        for partition in _set_partitions(FRAGMENTS):
            subset_name = "none" if not subset else "-".join(sorted(subset))
            partition_name = "__".join("-".join(group) for group in partition)
            cases.append(
                SupportCase(
                    case_id=f"access_{subset_name}__partition_{partition_name}",
                    accessible_fragments=subset,
                    provenance_partition=partition,
                    access_to_partition=True,
                )
            )
    return tuple(cases)


def hidden_partition_case() -> SupportCase:
    return SupportCase(
        case_id="access_E1-E2-E3__partition_hidden",
        accessible_fragments=frozenset(FRAGMENTS),
        provenance_partition=None,
        access_to_partition=False,
    )


def _same_support_always_same_verdict(verdicts: tuple[SupportVerdict, ...]) -> bool:
    seen: dict[int, str] = {}
    for verdict in verdicts:
        support = verdict.accessible_provenance_support
        if support is None:
            continue
        prior = seen.get(support)
        if prior is None:
            seen[support] = verdict.d1_verdict
        elif prior != verdict.d1_verdict:
            return False
    return True


def _raw_redundancy_is_not_sufficient(verdicts: tuple[SupportVerdict, ...]) -> bool:
    by_raw: dict[int, set[str]] = {}
    for verdict in verdicts:
        bucket = by_raw.setdefault(verdict.raw_accessible_redundancy, set())
        bucket.add(verdict.d1_verdict)
    return any(
        raw_redundancy >= D1_INDEPENDENT_SUPPORT_THRESHOLD and len(verdicts_for_raw) >= 2
        for raw_redundancy, verdicts_for_raw in by_raw.items()
    )


def run_t105_analysis() -> T105Result:
    visible = tuple(_score_case(case) for case in visible_support_cases())
    hidden = _score_case(hidden_partition_case())

    classifier_matches_all_visible_cases = all(
        verdict.classifier_matches_d1 for verdict in visible
    )
    same_support_always_same_verdict = _same_support_always_same_verdict(visible)
    raw_redundancy_is_not_sufficient = _raw_redundancy_is_not_sufficient(visible)

    return T105Result(
        visible_cases=visible,
        hidden_partition_case=hidden,
        classifier_matches_all_visible_cases=classifier_matches_all_visible_cases,
        same_support_always_same_verdict=same_support_always_same_verdict,
        raw_redundancy_is_not_sufficient=raw_redundancy_is_not_sufficient,
        external_distinctness_earned=False,
        strongest_claim=(
            "Within the current fixed-data Q1A family, the D1 verdict collapses "
            "to one auditable statistic plus one audit flag: the number of "
            "informative accessible provenance classes, together with whether "
            "that partition is available before scoring. Once ordinary "
            "quantum-side summaries are fixed, partition geometry, fragment "
            "labels, and raw accessible redundancy carry no extra verdict "
            "content beyond that thresholded accessible-class count."
        ),
        improved=(
            "T105 sharpens the surviving Q1A branch into an explicit reduction "
            "target. A serious reader no longer has to guess what structure is "
            "doing work in the current fixed-data regime: it is the audited "
            "accessible provenance-class count, not richer measurement "
            "dynamics."
        ),
        weakened=(
            "This weakens Q1A further. In the current regime it is not even a "
            "rich partition-sensitive theory; it is a thresholded classifier "
            "over audited accessible record classes. Any future paper-facing "
            "novelty claim must therefore show verdict content that survives "
            "after this reduction."
        ),
        falsification_condition=(
            "T105 stands unless a future fixed-data witness keeps the ordinary "
            "quantum-side summaries fixed and forces different D1 verdicts for "
            "two cases with the same audited accessible provenance-class count, "
            "or unless a physically justified D1 dimension beyond that count "
            "becomes load-bearing."
        ),
        q1_update=(
            "Q1A should currently be read as audited accessible-class "
            "bookkeeping over already formed records. Raw fragment redundancy "
            "is insufficient, but the surviving fixed-data branch still "
            "collapses to a thresholded accessible provenance-support count "
            "once the partition is shared."
        ),
        claim_ledger_update=(
            "Add T105 to Q1A: in the current fixed-data witness family, D1 "
            "verdicts are completely determined by the audited accessible "
            "provenance-class count plus partition visibility. This narrows "
            "Q1A from a general observer-relative measurement claim to a "
            "thresholded record-accounting classifier."
        ),
        open_blocker=(
            "No current Q1A witness uses branch support, reversal cost, or "
            "another physically justified D1 dimension to escape the "
            "accessible-class reduction after provenance auditing is shared."
        ),
        recommended_next=(
            "Try to construct or kill a witness where branch support or "
            "reversal-cost content remains nontrivial after matching "
            "provenance-aware access support, or else demote Q1A again in "
            "paper-facing summaries."
        ),
    )


def _verdict_to_dict(verdict: SupportVerdict) -> dict[str, object]:
    return {
        "case_id": verdict.case_id,
        "accessible_fragments": list(verdict.accessible_fragments),
        "raw_accessible_redundancy": verdict.raw_accessible_redundancy,
        "accessible_provenance_support": verdict.accessible_provenance_support,
        "d1_verdict": verdict.d1_verdict,
        "support_classifier_verdict": verdict.support_classifier_verdict,
        "classifier_matches_d1": verdict.classifier_matches_d1,
    }


def t105_result_to_dict(result: T105Result) -> dict[str, object]:
    verdict_histogram: dict[str, int] = {}
    support_histogram: dict[str, int] = {}
    for verdict in result.visible_cases:
        verdict_histogram[verdict.d1_verdict] = verdict_histogram.get(verdict.d1_verdict, 0) + 1
        support_key = str(verdict.accessible_provenance_support)
        support_histogram[support_key] = support_histogram.get(support_key, 0) + 1

    return {
        "visible_cases": [_verdict_to_dict(verdict) for verdict in result.visible_cases],
        "hidden_partition_case": _verdict_to_dict(result.hidden_partition_case),
        "classifier_matches_all_visible_cases": result.classifier_matches_all_visible_cases,
        "same_support_always_same_verdict": result.same_support_always_same_verdict,
        "raw_redundancy_is_not_sufficient": result.raw_redundancy_is_not_sufficient,
        "external_distinctness_earned": result.external_distinctness_earned,
        "verdict_histogram": verdict_histogram,
        "support_histogram": support_histogram,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t105_result_to_dict(run_t105_analysis()), indent=2))
