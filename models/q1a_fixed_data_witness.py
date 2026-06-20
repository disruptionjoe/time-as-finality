"""T103: Q1A fixed-data witness gate.

T102 made Q1A's external-neighbor gate concrete: keep the ordinary
quantum-side summaries fixed, then ask whether the D1 verdict can change only
because access-boundary or independence structure changes.

This module builds the smallest finite witness for that gate. It is
intentionally not a new measurement model. The witness uses already-formed
records and asks whether provenance/independence structure changes finality
after decoherence, raw fragment information, and branch/history availability
are held fixed.
"""

from __future__ import annotations

from dataclasses import dataclass


INFO_THRESHOLD_BITS = 0.9
D1_INDEPENDENT_SUPPORT_THRESHOLD = 3


@dataclass(frozen=True)
class FragmentSummary:
    fragment_id: str
    mutual_information_bits: float

    def signature(self) -> tuple[str, float]:
        return (self.fragment_id, round(self.mutual_information_bits, 6))


@dataclass(frozen=True)
class QuantumSideSummary:
    pointer_basis: str
    reduced_pointer_coherence: float
    fragments: tuple[FragmentSummary, ...]
    accessible_fragments: frozenset[str]
    branch_history_availability: tuple[str, ...]

    def informative_fragment_ids(self) -> frozenset[str]:
        return frozenset(
            fragment.fragment_id
            for fragment in self.fragments
            if fragment.mutual_information_bits >= INFO_THRESHOLD_BITS
        )

    def accessible_raw_redundancy(self) -> int:
        return len(self.accessible_fragments & self.informative_fragment_ids())

    def fixed_neighbor_signature(self) -> tuple[object, ...]:
        """Data Q1A must hold fixed against nearby frameworks."""

        return (
            self.pointer_basis,
            round(self.reduced_pointer_coherence, 6),
            tuple(sorted(fragment.signature() for fragment in self.fragments)),
            self.accessible_raw_redundancy(),
            tuple(sorted(self.branch_history_availability)),
        )


@dataclass(frozen=True)
class IndependenceStructure:
    classes: tuple[tuple[str, ...], ...]

    def class_count_for(self, fragment_ids: frozenset[str]) -> int:
        count = 0
        covered: set[str] = set()
        for independence_class in self.classes:
            members = frozenset(independence_class)
            if members & fragment_ids:
                count += 1
                covered.update(members & fragment_ids)
        missing = fragment_ids - covered
        return count + len(missing)

    def signature(self) -> tuple[tuple[str, ...], ...]:
        return tuple(sorted(tuple(sorted(group)) for group in self.classes))


@dataclass(frozen=True)
class WitnessCase:
    case_id: str
    quantum_side: QuantumSideSummary
    independence: IndependenceStructure | None
    access_to_independence_partition: bool
    expected_purpose: str


@dataclass(frozen=True)
class CaseVerdict:
    case_id: str
    standard_data_matches_baseline: bool
    accessible_raw_redundancy: int
    independent_accessible_support: int | None
    d1_verdict: str
    gate_verdict: str
    purpose: str


@dataclass(frozen=True)
class T103Result:
    baseline_case_id: str
    cases: tuple[CaseVerdict, ...]
    fixed_data_internal_witness_exists: bool
    negative_controls_rejected: bool
    hidden_partition_withholds: bool
    external_measurement_distinction_earned: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def base_quantum_side(
    *,
    coherence: float = 0.0,
    accessible_fragments: frozenset[str] = frozenset({"E1", "E2", "E3"}),
    branch_history_availability: tuple[str, ...] = ("z0_history", "z1_history"),
) -> QuantumSideSummary:
    return QuantumSideSummary(
        pointer_basis="computational_z",
        reduced_pointer_coherence=coherence,
        fragments=(
            FragmentSummary("E1", 1.0),
            FragmentSummary("E2", 1.0),
            FragmentSummary("E3", 1.0),
        ),
        accessible_fragments=accessible_fragments,
        branch_history_availability=branch_history_availability,
    )


def witness_cases() -> tuple[WitnessCase, ...]:
    return (
        WitnessCase(
            case_id="independent_records_fixed_data",
            quantum_side=base_quantum_side(),
            independence=IndependenceStructure((("E1",), ("E2",), ("E3",))),
            access_to_independence_partition=True,
            expected_purpose=(
                "Positive side of the fixed-data witness: all three accessible "
                "informative records are independent provenance classes."
            ),
        ),
        WitnessCase(
            case_id="copied_archive_fixed_data",
            quantum_side=base_quantum_side(),
            independence=IndependenceStructure((("E1", "E3"), ("E2",))),
            access_to_independence_partition=True,
            expected_purpose=(
                "Matched quantum-side data, but E3 is a copied archive of E1; "
                "D1 changes only because the independence partition changes."
            ),
        ),
        WitnessCase(
            case_id="partition_hidden_fixed_data",
            quantum_side=base_quantum_side(),
            independence=None,
            access_to_independence_partition=False,
            expected_purpose=(
                "Matched quantum-side data with inaccessible provenance; D1 is "
                "withheld rather than inferred from raw redundancy."
            ),
        ),
        WitnessCase(
            case_id="coherence_changed_control",
            quantum_side=base_quantum_side(coherence=0.2),
            independence=IndependenceStructure((("E1",), ("E2",), ("E3",))),
            access_to_independence_partition=True,
            expected_purpose=(
                "Negative control: a D1 change is inadmissible if reduced "
                "pointer coherence changes."
            ),
        ),
        WitnessCase(
            case_id="raw_redundancy_changed_control",
            quantum_side=base_quantum_side(accessible_fragments=frozenset({"E1", "E2"})),
            independence=IndependenceStructure((("E1",), ("E2",))),
            access_to_independence_partition=True,
            expected_purpose=(
                "Negative control: a D1 change is inadmissible if accessible "
                "raw redundancy changes."
            ),
        ),
        WitnessCase(
            case_id="branch_history_changed_control",
            quantum_side=base_quantum_side(branch_history_availability=("z0_history",)),
            independence=IndependenceStructure((("E1",), ("E2",), ("E3",))),
            access_to_independence_partition=True,
            expected_purpose=(
                "Negative control: a D1 change is inadmissible if ordinary "
                "branch/history availability changes."
            ),
        ),
    )


def score_case(case: WitnessCase, baseline: QuantumSideSummary) -> CaseVerdict:
    standard_matches = (
        case.quantum_side.fixed_neighbor_signature()
        == baseline.fixed_neighbor_signature()
    )
    accessible_informative = (
        case.quantum_side.accessible_fragments
        & case.quantum_side.informative_fragment_ids()
    )

    if not standard_matches:
        return CaseVerdict(
            case_id=case.case_id,
            standard_data_matches_baseline=False,
            accessible_raw_redundancy=case.quantum_side.accessible_raw_redundancy(),
            independent_accessible_support=None,
            d1_verdict="invalid_fixed_data_gate",
            gate_verdict="reject_standard_data_changed",
            purpose=case.expected_purpose,
        )

    if not case.access_to_independence_partition or case.independence is None:
        return CaseVerdict(
            case_id=case.case_id,
            standard_data_matches_baseline=True,
            accessible_raw_redundancy=case.quantum_side.accessible_raw_redundancy(),
            independent_accessible_support=None,
            d1_verdict="withhold_partition_unavailable",
            gate_verdict="passes_fixed_quantum_data_but_withholds_d1",
            purpose=case.expected_purpose,
        )

    independent_support = case.independence.class_count_for(accessible_informative)
    d1_verdict = (
        "finalized"
        if independent_support >= D1_INDEPENDENT_SUPPORT_THRESHOLD
        else "not_finalized"
    )
    return CaseVerdict(
        case_id=case.case_id,
        standard_data_matches_baseline=True,
        accessible_raw_redundancy=case.quantum_side.accessible_raw_redundancy(),
        independent_accessible_support=independent_support,
        d1_verdict=d1_verdict,
        gate_verdict="passes_fixed_data_gate",
        purpose=case.expected_purpose,
    )


def run_t103_analysis() -> T103Result:
    cases = witness_cases()
    baseline = cases[0].quantum_side
    verdicts = tuple(score_case(case, baseline) for case in cases)
    by_id = {verdict.case_id: verdict for verdict in verdicts}

    fixed_data_internal_witness_exists = (
        by_id["independent_records_fixed_data"].standard_data_matches_baseline
        and by_id["copied_archive_fixed_data"].standard_data_matches_baseline
        and by_id["independent_records_fixed_data"].accessible_raw_redundancy
        == by_id["copied_archive_fixed_data"].accessible_raw_redundancy
        and by_id["independent_records_fixed_data"].d1_verdict == "finalized"
        and by_id["copied_archive_fixed_data"].d1_verdict == "not_finalized"
    )
    negative_controls_rejected = all(
        by_id[case_id].gate_verdict == "reject_standard_data_changed"
        for case_id in (
            "coherence_changed_control",
            "raw_redundancy_changed_control",
            "branch_history_changed_control",
        )
    )
    hidden_partition_withholds = (
        by_id["partition_hidden_fixed_data"].d1_verdict
        == "withhold_partition_unavailable"
    )

    return T103Result(
        baseline_case_id="independent_records_fixed_data",
        cases=verdicts,
        fixed_data_internal_witness_exists=fixed_data_internal_witness_exists,
        negative_controls_rejected=negative_controls_rejected,
        hidden_partition_withholds=hidden_partition_withholds,
        external_measurement_distinction_earned=False,
        strongest_claim=(
            "Q1A now has an internal fixed-data witness: decoherence/"
            "pointer-basis evidence, fragment-information summaries, "
            "accessible raw redundancy, and ordinary branch/history "
            "availability can be held fixed while D1 changes from finalized to "
            "not_finalized solely because the independence partition treats a "
            "record as an independent copy versus a copied archive. This is "
            "not yet an external measurement-theory distinction; it is an "
            "access/provenance accounting predicate over already formed "
            "records."
        ),
        improved=(
            "T103 converts the T102 blocker into an executable gate with "
            "positive and negative controls. The repo can now distinguish a "
            "valid fixed-data Q1A witness from invalid cases that changed "
            "coherence, raw redundancy, or branch/history availability."
        ),
        weakened=(
            "The witness also weakens Q1A's physics ambition. The only "
            "surviving delta is carried by an independence/provenance "
            "predicate; if decoherence, Quantum Darwinism, consistent "
            "histories, RQM, QBism, or Everettian accounts admit that same "
            "predicate, Q1A collapses to bookkeeping."
        ),
        falsification_condition=(
            "Demote Q1A if every fixed-data D1 change requires adding a "
            "provenance or independence partition that neighboring frameworks "
            "can adopt without changing their physics, or if no physically "
            "auditable procedure fixes the partition before D1 scoring."
        ),
        q1_update=(
            "Q1A clears the internal fixed-data gate only as record "
            "independence accounting. It still does not earn new measurement "
            "dynamics, collapse content, Born-rule content, or empirical "
            "quantum support."
        ),
        claim_ledger_update=(
            "Add T103 to Q1: a fixed-data witness exists internally because "
            "the same decoherence, fragment-information, raw-redundancy, and "
            "branch/history summaries can yield finalized versus not_finalized "
            "D1 verdicts when only the independence partition changes. This "
            "upgrades Q1A only to conditional record-accounting support; "
            "external distinctness remains unearned if the partition is "
            "ordinary provenance bookkeeping."
        ),
        open_blocker=(
            "The partition is still fixture-declared. The next blocker is a "
            "physically auditable derivation of record independence that is "
            "fixed before D1 scoring and not just imported as TaF vocabulary."
        ),
        recommended_next=(
            "Derive the T103 independence partition from event-level detector "
            "or environment-fragment provenance, then test whether Quantum "
            "Darwinism with provenance-aware fragment partitioning already "
            "absorbs the same verdict."
        ),
    )


def _case_verdict_to_dict(verdict: CaseVerdict) -> dict[str, object]:
    return {
        "case_id": verdict.case_id,
        "standard_data_matches_baseline": verdict.standard_data_matches_baseline,
        "accessible_raw_redundancy": verdict.accessible_raw_redundancy,
        "independent_accessible_support": verdict.independent_accessible_support,
        "d1_verdict": verdict.d1_verdict,
        "gate_verdict": verdict.gate_verdict,
        "purpose": verdict.purpose,
    }


def t103_result_to_dict(result: T103Result) -> dict[str, object]:
    return {
        "baseline_case_id": result.baseline_case_id,
        "cases": [_case_verdict_to_dict(verdict) for verdict in result.cases],
        "fixed_data_internal_witness_exists": result.fixed_data_internal_witness_exists,
        "negative_controls_rejected": result.negative_controls_rejected,
        "hidden_partition_withholds": result.hidden_partition_withholds,
        "external_measurement_distinction_earned": (
            result.external_measurement_distinction_earned
        ),
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

    print(json.dumps(t103_result_to_dict(run_t103_analysis()), indent=2))
