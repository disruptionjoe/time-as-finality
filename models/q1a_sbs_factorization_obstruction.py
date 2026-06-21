"""T162: SBS closure-key obstruction for current Q1A verdicts.

N10 says Spectrum Broadcast Structure and strong Quantum Darwinism already own
the objectivity target "many independently accessible records of one pointer
value." T147 says the current Q1A verdict family factors through partition
visibility plus audited accessible provenance-support count.

This module combines those two guardrails. It does not prove a theorem about
quantum measurement. It checks that, once SBS-style objectivity data can import
the same access/provenance support key, the current Q1A verdict family has no
same-SBS-data split left.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.q1a_fixed_data_witness import D1_INDEPENDENT_SUPPORT_THRESHOLD


FRAGMENTS = ("E1", "E2", "E3", "E4")
POINTER_OBSERVABLE = "computational_z"


@dataclass(frozen=True)
class FragmentRecord:
    fragment_id: str
    pointer_value: str
    distinguishable: bool = True


@dataclass(frozen=True)
class SBSCase:
    case_id: str
    fragments: tuple[FragmentRecord, ...]
    accessible_fragments: frozenset[str]
    provenance_partition: tuple[tuple[str, ...], ...] | None
    partition_visible: bool
    strong_independence: bool
    expected_role: str


@dataclass(frozen=True)
class SBSVerdict:
    case_id: str
    sbs_objectivity_verdict: str
    accessible_pointer_value: str | None
    accessible_raw_redundancy: int
    accessible_provenance_support: int | None
    partition_visible: bool
    d1_verdict: str
    sbs_closure_key: tuple[object, ...]
    full_sbs_signature: tuple[object, ...]
    role: str


@dataclass(frozen=True)
class SBSFiber:
    sbs_closure_key: tuple[object, ...]
    case_count: int
    d1_verdicts: tuple[str, ...]
    raw_redundancies: tuple[int, ...]
    partition_signatures: tuple[str, ...]


@dataclass(frozen=True)
class T162Result:
    visible_cases: tuple[SBSVerdict, ...]
    hidden_partition_case: SBSVerdict
    objectivity_failure_controls: tuple[SBSVerdict, ...]
    fibers: tuple[SBSFiber, ...]
    d1_factors_through_sbs_closure_key: bool
    same_full_sbs_data_split_found: bool
    raw_redundancy_is_not_sufficient: bool
    objectivity_failures_withhold: bool
    hidden_partition_withholds: bool
    nontrivial_same_key_variants_exist: bool
    q1a_current_family_has_no_same_sbs_split: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1a_update: str
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


def _partition_signature(partition: tuple[tuple[str, ...], ...] | None) -> str:
    if partition is None:
        return "hidden"
    return "|".join("-".join(group) for group in partition)


def _class_count_for(
    fragment_ids: frozenset[str],
    partition: tuple[tuple[str, ...], ...],
) -> int:
    count = 0
    covered: set[str] = set()
    for group in partition:
        members = frozenset(group)
        if members & fragment_ids:
            count += 1
            covered.update(members & fragment_ids)
    missing = fragment_ids - covered
    return count + len(missing)


def _base_fragments(
    *,
    pointer_value: str = "z0",
    indistinguishable_id: str | None = None,
    disagreement_id: str | None = None,
) -> tuple[FragmentRecord, ...]:
    records: list[FragmentRecord] = []
    for fragment_id in FRAGMENTS:
        value = "z1" if fragment_id == disagreement_id else pointer_value
        records.append(
            FragmentRecord(
                fragment_id=fragment_id,
                pointer_value=value,
                distinguishable=(fragment_id != indistinguishable_id),
            )
        )
    return tuple(records)


def visible_sbs_cases() -> tuple[SBSCase, ...]:
    cases: list[SBSCase] = []
    for accessible in _powerset(FRAGMENTS):
        for partition in _set_partitions(FRAGMENTS):
            access_name = "none" if not accessible else "-".join(sorted(accessible))
            partition_name = _partition_signature(partition)
            cases.append(
                SBSCase(
                    case_id=f"access_{access_name}__partition_{partition_name}",
                    fragments=_base_fragments(),
                    accessible_fragments=accessible,
                    provenance_partition=partition,
                    partition_visible=True,
                    strong_independence=True,
                    expected_role="Finite SBS closure-key enumeration case.",
                )
            )
    return tuple(cases)


def hidden_partition_case() -> SBSCase:
    return SBSCase(
        case_id="access_E1-E2-E3__partition_hidden",
        fragments=_base_fragments(),
        accessible_fragments=frozenset(("E1", "E2", "E3")),
        provenance_partition=None,
        partition_visible=False,
        strong_independence=True,
        expected_role=(
            "Positive SBS objectivity but unavailable provenance partition; "
            "Q1A must withhold rather than infer from raw redundancy."
        ),
    )


def objectivity_failure_controls() -> tuple[SBSCase, ...]:
    return (
        SBSCase(
            case_id="sbs_disagreement_control",
            fragments=_base_fragments(disagreement_id="E3"),
            accessible_fragments=frozenset(("E1", "E2", "E3")),
            provenance_partition=(("E1",), ("E2",), ("E3",), ("E4",)),
            partition_visible=True,
            strong_independence=True,
            expected_role=(
                "SBS negative control: accessible fragments do not all agree "
                "on one pointer value."
            ),
        ),
        SBSCase(
            case_id="sbs_distinguishability_control",
            fragments=_base_fragments(indistinguishable_id="E3"),
            accessible_fragments=frozenset(("E1", "E2", "E3")),
            provenance_partition=(("E1",), ("E2",), ("E3",), ("E4",)),
            partition_visible=True,
            strong_independence=True,
            expected_role=(
                "SBS negative control: one accessible fragment fails the "
                "distinguishability/support-overlap check."
            ),
        ),
        SBSCase(
            case_id="sbs_independence_control",
            fragments=_base_fragments(),
            accessible_fragments=frozenset(("E1", "E2", "E3")),
            provenance_partition=(("E1",), ("E2",), ("E3",), ("E4",)),
            partition_visible=True,
            strong_independence=False,
            expected_role=(
                "SBS negative control: conditional independence/strong "
                "independence is denied."
            ),
        ),
        SBSCase(
            case_id="sbs_no_access_control",
            fragments=_base_fragments(),
            accessible_fragments=frozenset(),
            provenance_partition=(("E1",), ("E2",), ("E3",), ("E4",)),
            partition_visible=True,
            strong_independence=True,
            expected_role=(
                "Access control: no observer-accessible fragment can ground "
                "observer-relative finality."
            ),
        ),
    )


def _accessible_records(case: SBSCase) -> tuple[FragmentRecord, ...]:
    return tuple(
        record
        for record in case.fragments
        if record.fragment_id in case.accessible_fragments
    )


def _sbs_objectivity_verdict(case: SBSCase) -> tuple[str, str | None]:
    accessible = _accessible_records(case)
    if not accessible:
        return ("sbs_no_access", None)
    if not case.strong_independence:
        return ("sbs_failed_strong_independence", None)
    if any(not record.distinguishable for record in accessible):
        return ("sbs_failed_distinguishability", None)

    values = {record.pointer_value for record in accessible}
    if len(values) != 1:
        return ("sbs_failed_agreement", None)

    return ("sbs_objective", next(iter(values)))


def score_sbs_case(case: SBSCase) -> SBSVerdict:
    objectivity_verdict, pointer_value = _sbs_objectivity_verdict(case)
    raw_redundancy = len(_accessible_records(case))

    if objectivity_verdict != "sbs_objective":
        support = None
        d1_verdict = "withhold_sbs_objectivity_failed"
    elif not case.partition_visible or case.provenance_partition is None:
        support = None
        d1_verdict = "withhold_partition_unavailable"
    else:
        support = _class_count_for(case.accessible_fragments, case.provenance_partition)
        d1_verdict = (
            "finalized"
            if support >= D1_INDEPENDENT_SUPPORT_THRESHOLD
            else "not_finalized"
        )

    sbs_closure_key = (
        POINTER_OBSERVABLE,
        objectivity_verdict,
        pointer_value,
        case.partition_visible if objectivity_verdict == "sbs_objective" else None,
        support,
    )
    full_sbs_signature = (
        POINTER_OBSERVABLE,
        tuple(
            (record.fragment_id, record.pointer_value, record.distinguishable)
            for record in case.fragments
        ),
        tuple(sorted(case.accessible_fragments)),
        _partition_signature(case.provenance_partition),
        case.partition_visible,
        case.strong_independence,
    )

    return SBSVerdict(
        case_id=case.case_id,
        sbs_objectivity_verdict=objectivity_verdict,
        accessible_pointer_value=pointer_value,
        accessible_raw_redundancy=raw_redundancy,
        accessible_provenance_support=support,
        partition_visible=case.partition_visible,
        d1_verdict=d1_verdict,
        sbs_closure_key=sbs_closure_key,
        full_sbs_signature=full_sbs_signature,
        role=case.expected_role,
    )


def _unique_sorted(values: list[object]) -> tuple[object, ...]:
    return tuple(sorted(set(values), key=lambda item: str(item)))


def _fibers(verdicts: tuple[SBSVerdict, ...]) -> tuple[SBSFiber, ...]:
    grouped: dict[tuple[object, ...], list[SBSVerdict]] = {}
    for verdict in verdicts:
        grouped.setdefault(verdict.sbs_closure_key, []).append(verdict)

    fibers: list[SBSFiber] = []
    for key in sorted(grouped, key=lambda item: str(item)):
        members = grouped[key]
        fibers.append(
            SBSFiber(
                sbs_closure_key=key,
                case_count=len(members),
                d1_verdicts=_unique_sorted([case.d1_verdict for case in members]),
                raw_redundancies=_unique_sorted(
                    [case.accessible_raw_redundancy for case in members]
                ),
                partition_signatures=_unique_sorted(
                    [
                        str(case.full_sbs_signature[3])
                        for case in members
                    ]
                ),
            )
        )
    return tuple(fibers)


def _same_full_sbs_data_split_found(verdicts: tuple[SBSVerdict, ...]) -> bool:
    by_full_signature: dict[tuple[object, ...], set[str]] = {}
    for verdict in verdicts:
        by_full_signature.setdefault(verdict.full_sbs_signature, set()).add(
            verdict.d1_verdict
        )
    return any(len(d1_verdicts) > 1 for d1_verdicts in by_full_signature.values())


def _raw_redundancy_is_not_sufficient(verdicts: tuple[SBSVerdict, ...]) -> bool:
    by_raw: dict[int, set[str]] = {}
    for verdict in verdicts:
        by_raw.setdefault(verdict.accessible_raw_redundancy, set()).add(
            verdict.d1_verdict
        )
    return any(
        raw_count >= D1_INDEPENDENT_SUPPORT_THRESHOLD and len(d1_verdicts) > 1
        for raw_count, d1_verdicts in by_raw.items()
    )


def run_t162_analysis() -> T162Result:
    visible = tuple(score_sbs_case(case) for case in visible_sbs_cases())
    hidden = score_sbs_case(hidden_partition_case())
    failure_controls = tuple(score_sbs_case(case) for case in objectivity_failure_controls())
    all_verdicts = visible + (hidden,) + failure_controls
    fibers = _fibers(all_verdicts)

    d1_factors_through_sbs_closure_key = all(
        len(fiber.d1_verdicts) == 1 for fiber in fibers
    )
    same_full_sbs_data_split_found = _same_full_sbs_data_split_found(all_verdicts)
    raw_redundancy_is_not_sufficient = _raw_redundancy_is_not_sufficient(all_verdicts)
    objectivity_failures_withhold = all(
        verdict.d1_verdict == "withhold_sbs_objectivity_failed"
        for verdict in failure_controls
    )
    hidden_partition_withholds = hidden.d1_verdict == "withhold_partition_unavailable"
    nontrivial_same_key_variants_exist = any(
        fiber.case_count > 1
        and (len(fiber.raw_redundancies) > 1 or len(fiber.partition_signatures) > 1)
        for fiber in fibers
    )
    q1a_current_family_has_no_same_sbs_split = (
        d1_factors_through_sbs_closure_key
        and not same_full_sbs_data_split_found
        and raw_redundancy_is_not_sufficient
        and objectivity_failures_withhold
        and hidden_partition_withholds
    )

    return T162Result(
        visible_cases=visible,
        hidden_partition_case=hidden,
        objectivity_failure_controls=failure_controls,
        fibers=fibers,
        d1_factors_through_sbs_closure_key=d1_factors_through_sbs_closure_key,
        same_full_sbs_data_split_found=same_full_sbs_data_split_found,
        raw_redundancy_is_not_sufficient=raw_redundancy_is_not_sufficient,
        objectivity_failures_withhold=objectivity_failures_withhold,
        hidden_partition_withholds=hidden_partition_withholds,
        nontrivial_same_key_variants_exist=nontrivial_same_key_variants_exist,
        q1a_current_family_has_no_same_sbs_split=(
            q1a_current_family_has_no_same_sbs_split
        ),
        strongest_claim=(
            "Within the current Q1A already-formed-record verdict family, the "
            "D1 verdict factors through an SBS-importable closure key: pointer "
            "objectivity status, accessible pointer value, partition visibility, "
            "and audited accessible provenance-support count. Therefore the "
            "present Q1A family has no same-SBS-data verdict split; a full SBS "
            "signature refines this key, so fixing full SBS data cannot change "
            "the current D1 verdict."
        ),
        improved=(
            "T162 turns the N10 absorber into an executable obstruction. A "
            "future Q1A proposal now has to say whether it changes the imported "
            "SBS closure key, in which case it is absorbed bookkeeping, or keeps "
            "that key fixed and supplies a genuinely new physical dimension."
        ),
        weakened=(
            "This weakens Q1A as an internal quantum-record route. The current "
            "same-closure-key family cannot produce the same-SBS-data witness "
            "that N10 requires, and raw redundancy remains insufficient once "
            "SBS/objectivity and provenance support are granted."
        ),
        falsification_condition=(
            "T162 fails if an admissible Q1A witness fixes full SBS/strong-QD "
            "objectivity data, observer-accessible fragments, provenance "
            "partition, partition visibility, and audited accessible support "
            "count, but still changes the D1 verdict through a predeclared "
            "physical dimension that SBS or strong Quantum Darwinism cannot "
            "import as ordinary objectivity, access, provenance, or support "
            "data."
        ),
        q1a_update=(
            "Q1A should be treated as SBS-absorbed bookkeeping in the current "
            "family. Reopen it only with a same-SBS-closure-key split or a "
            "physical derivation of the partition/access rule that the SBS "
            "neighbor cannot import without new physics."
        ),
        claim_ledger_update=(
            "Add T162 to Q1A: after N10, current Q1A verdicts factor through "
            "an SBS-importable closure key. No same-full-SBS-data verdict split "
            "exists in the enumerated family; Q1A remains bookkeeping_only."
        ),
        open_blocker=(
            "No named physical dimension currently varies at fixed SBS "
            "objectivity data, access subset, provenance partition, partition "
            "visibility, and audited accessible support count."
        ),
        recommended_next=(
            "Do not spend another autonomous run on Q1A unless a concrete "
            "same-SBS-closure-key split is named. Otherwise route quantum work "
            "to Q1B external packet acquisition, Q1C only if a platform tuple "
            "appears, or leave Q1 for another research line."
        ),
    )


def _verdict_to_dict(verdict: SBSVerdict) -> dict[str, object]:
    return {
        "case_id": verdict.case_id,
        "sbs_objectivity_verdict": verdict.sbs_objectivity_verdict,
        "accessible_pointer_value": verdict.accessible_pointer_value,
        "accessible_raw_redundancy": verdict.accessible_raw_redundancy,
        "accessible_provenance_support": verdict.accessible_provenance_support,
        "partition_visible": verdict.partition_visible,
        "d1_verdict": verdict.d1_verdict,
        "sbs_closure_key": list(verdict.sbs_closure_key),
        "full_sbs_signature": list(verdict.full_sbs_signature),
        "role": verdict.role,
    }


def _fiber_to_dict(fiber: SBSFiber) -> dict[str, object]:
    return {
        "sbs_closure_key": list(fiber.sbs_closure_key),
        "case_count": fiber.case_count,
        "d1_verdicts": list(fiber.d1_verdicts),
        "raw_redundancies": list(fiber.raw_redundancies),
        "partition_signatures": list(fiber.partition_signatures),
    }


def t162_result_to_dict(result: T162Result) -> dict[str, object]:
    return {
        "visible_case_count": len(result.visible_cases),
        "hidden_partition_case": _verdict_to_dict(result.hidden_partition_case),
        "objectivity_failure_controls": [
            _verdict_to_dict(verdict)
            for verdict in result.objectivity_failure_controls
        ],
        "fibers": [_fiber_to_dict(fiber) for fiber in result.fibers],
        "d1_factors_through_sbs_closure_key": (
            result.d1_factors_through_sbs_closure_key
        ),
        "same_full_sbs_data_split_found": result.same_full_sbs_data_split_found,
        "raw_redundancy_is_not_sufficient": result.raw_redundancy_is_not_sufficient,
        "objectivity_failures_withhold": result.objectivity_failures_withhold,
        "hidden_partition_withholds": result.hidden_partition_withholds,
        "nontrivial_same_key_variants_exist": (
            result.nontrivial_same_key_variants_exist
        ),
        "q1a_current_family_has_no_same_sbs_split": (
            result.q1a_current_family_has_no_same_sbs_split
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

    print(json.dumps(t162_result_to_dict(run_t162_analysis()), indent=2))
