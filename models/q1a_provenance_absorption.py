"""T104: provenance-aware Quantum Darwinism absorption audit for Q1A.

This module asks whether T103's surviving fixed-data witness still distinguishes
itself from the nearest external neighbor once fragment redundancy is computed
with the same provenance partition D1 requires.

The point is not to promote Quantum Darwinism or TaF. The point is to test
whether the current Q1A delta is genuine physics or only a disciplined
partitioning rule over already formed records.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.q1a_fixed_data_witness import (
    D1_INDEPENDENT_SUPPORT_THRESHOLD,
    QuantumSideSummary,
    WitnessCase,
    base_quantum_side,
    score_case,
)


@dataclass(frozen=True)
class T104Case:
    case_id: str
    quantum_side: QuantumSideSummary
    provenance_partition: tuple[tuple[str, ...], ...] | None
    access_to_partition: bool
    expected_role: str


@dataclass(frozen=True)
class AbsorptionVerdict:
    case_id: str
    raw_accessible_redundancy: int
    provenance_aware_redundancy: int | None
    d1_independent_support: int | None
    d1_verdict: str
    provenance_qd_verdict: str
    absorption_status: str
    expected_role: str


@dataclass(frozen=True)
class T104Result:
    cases: tuple[AbsorptionVerdict, ...]
    exact_absorption_on_fixed_data_cases: bool
    hidden_partition_withholds_for_both: bool
    external_distinctness_earned: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def t104_cases() -> tuple[T104Case, ...]:
    return (
        T104Case(
            case_id="independent_records_fixed_data",
            quantum_side=base_quantum_side(),
            provenance_partition=(("E1",), ("E2",), ("E3",)),
            access_to_partition=True,
            expected_role=(
                "Positive control: three informative fragments are independently "
                "provenanced."
            ),
        ),
        T104Case(
            case_id="copied_archive_fixed_data",
            quantum_side=base_quantum_side(),
            provenance_partition=(("E1", "E3"), ("E2",)),
            access_to_partition=True,
            expected_role=(
                "Duplicate-archive control: raw redundancy stays at three, but "
                "the provenance-aware partition collapses E1 and E3."
            ),
        ),
        T104Case(
            case_id="partition_hidden_fixed_data",
            quantum_side=base_quantum_side(),
            provenance_partition=None,
            access_to_partition=False,
            expected_role=(
                "Audit boundary: raw redundancy is visible but the provenance "
                "partition is unavailable before scoring."
            ),
        ),
    )


def _to_witness_case(case: T104Case) -> WitnessCase:
    from models.q1a_fixed_data_witness import IndependenceStructure

    independence = (
        None
        if case.provenance_partition is None
        else IndependenceStructure(case.provenance_partition)
    )
    return WitnessCase(
        case_id=case.case_id,
        quantum_side=case.quantum_side,
        independence=independence,
        access_to_independence_partition=case.access_to_partition,
        expected_purpose=case.expected_role,
    )


def _provenance_aware_redundancy(case: T104Case) -> int | None:
    if not case.access_to_partition or case.provenance_partition is None:
        return None

    informative_accessible = (
        case.quantum_side.accessible_fragments
        & case.quantum_side.informative_fragment_ids()
    )
    covered: set[str] = set()
    count = 0
    for group in case.provenance_partition:
        members = frozenset(group)
        if members & informative_accessible:
            count += 1
            covered.update(members & informative_accessible)
    missing = informative_accessible - covered
    return count + len(missing)


def score_t104_case(case: T104Case, baseline: QuantumSideSummary) -> AbsorptionVerdict:
    witness_verdict = score_case(_to_witness_case(case), baseline)
    provenance_redundancy = _provenance_aware_redundancy(case)

    if provenance_redundancy is None:
        provenance_qd_verdict = "withhold_partition_unavailable"
    elif provenance_redundancy >= D1_INDEPENDENT_SUPPORT_THRESHOLD:
        provenance_qd_verdict = "finalized"
    else:
        provenance_qd_verdict = "not_finalized"

    absorption_status = (
        "absorbed"
        if provenance_qd_verdict == witness_verdict.d1_verdict
        else "divergent"
    )

    return AbsorptionVerdict(
        case_id=case.case_id,
        raw_accessible_redundancy=case.quantum_side.accessible_raw_redundancy(),
        provenance_aware_redundancy=provenance_redundancy,
        d1_independent_support=witness_verdict.independent_accessible_support,
        d1_verdict=witness_verdict.d1_verdict,
        provenance_qd_verdict=provenance_qd_verdict,
        absorption_status=absorption_status,
        expected_role=case.expected_role,
    )


def run_t104_analysis() -> T104Result:
    cases = t104_cases()
    baseline = cases[0].quantum_side
    verdicts = tuple(score_t104_case(case, baseline) for case in cases)
    by_id = {verdict.case_id: verdict for verdict in verdicts}

    exact_absorption_on_fixed_data_cases = all(
        by_id[case_id].absorption_status == "absorbed"
        for case_id in (
            "independent_records_fixed_data",
            "copied_archive_fixed_data",
        )
    )
    hidden_partition_withholds_for_both = (
        by_id["partition_hidden_fixed_data"].d1_verdict
        == "withhold_partition_unavailable"
        and by_id["partition_hidden_fixed_data"].provenance_qd_verdict
        == "withhold_partition_unavailable"
    )

    return T104Result(
        cases=verdicts,
        exact_absorption_on_fixed_data_cases=exact_absorption_on_fixed_data_cases,
        hidden_partition_withholds_for_both=hidden_partition_withholds_for_both,
        external_distinctness_earned=False,
        strongest_claim=(
            "T104 finds that the surviving T103 Q1A witness is exactly absorbed "
            "by provenance-aware fragment partitioning in the tested family. "
            "Once Quantum-Darwinism-style redundancy is computed over audited "
            "independent fragment classes rather than raw fragment count, it "
            "reproduces the same finalized, not_finalized, and withhold "
            "verdicts as D1 on the fixed-data cases."
        ),
        improved=(
            "T104 converts Q1A's main external comparison threat into an "
            "executable kill test. The repo no longer has to speak vaguely "
            "about possible overlap with Quantum Darwinism; it can now state "
            "that the current fixed-data witness is absorbed once provenance "
            "partitioning is shared."
        ),
        weakened=(
            "This weakens Q1A's external novelty again. In the present witness "
            "family, the live difference from Quantum Darwinism is not new "
            "measurement structure. It is the insistence that fragment "
            "partitioning be provenance-audited before redundancy is treated as "
            "evidence. That is a bookkeeping or admissibility discipline unless "
            "another D1 dimension produces a non-absorbed witness."
        ),
        falsification_condition=(
            "Recover external Q1A distinctness only if one fixed-data witness "
            "keeps provenance-aware fragment partitioning fixed and still "
            "forces a D1 verdict that partitioned Quantum Darwinism cannot "
            "match, or if D1 derives the partition from a physical rule that "
            "cannot be imported into the neighboring framework without adding "
            "new physics."
        ),
        q1_update=(
            "Q1A should now be stated as provenance-disciplined access and "
            "redundancy accounting over already formed records. T103's witness "
            "does not currently separate Q1A from provenance-aware Quantum "
            "Darwinism."
        ),
        claim_ledger_update=(
            "Add T104 to Q1: the T103 fixed-data witness is absorbed by "
            "provenance-aware fragment partitioning. Q1A therefore remains "
            "conditional bookkeeping/admissibility support rather than a "
            "distinct measurement-theory contribution."
        ),
        open_blocker=(
            "The repo lacks any fixed-data witness where D1 diverges from a "
            "neighbor after both sides share the same auditable provenance "
            "partition. Without that, Q1A has no external distinction."
        ),
        recommended_next=(
            "Either find a fixed-data witness where branch support, access "
            "structure, or reversal-cost content survives even after "
            "provenance-aware fragment partitioning is shared, or demote Q1A "
            "explicitly to record-accounting discipline in paper-facing text."
        ),
    )


def _verdict_to_dict(verdict: AbsorptionVerdict) -> dict[str, object]:
    return {
        "case_id": verdict.case_id,
        "raw_accessible_redundancy": verdict.raw_accessible_redundancy,
        "provenance_aware_redundancy": verdict.provenance_aware_redundancy,
        "d1_independent_support": verdict.d1_independent_support,
        "d1_verdict": verdict.d1_verdict,
        "provenance_qd_verdict": verdict.provenance_qd_verdict,
        "absorption_status": verdict.absorption_status,
        "expected_role": verdict.expected_role,
    }


def t104_result_to_dict(result: T104Result) -> dict[str, object]:
    return {
        "cases": [_verdict_to_dict(verdict) for verdict in result.cases],
        "exact_absorption_on_fixed_data_cases": result.exact_absorption_on_fixed_data_cases,
        "hidden_partition_withholds_for_both": result.hidden_partition_withholds_for_both,
        "external_distinctness_earned": result.external_distinctness_earned,
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

    print(json.dumps(t104_result_to_dict(run_t104_analysis()), indent=2))
