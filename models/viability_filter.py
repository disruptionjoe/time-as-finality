"""T114: finite viability filter over geometric possibility.

This model turns the geometry/finality/maintenance/emergence synthesis into a
small falsifiable object.  Geometry supplies candidate structures.  The
viability filter asks which candidates survive reachability, maintenance,
record-finality, and emergence-platform gates.

The result is not a new physics claim.  It is a discipline device: if every
positive verdict is already determined by standard reachability plus
maintenance variables, the filter collapses to ordinary stability/accounting.
If record-finality or platform capacity separates otherwise matched cases,
those are the only TaF-specific residues left to investigate.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StructureCandidate:
    name: str
    geometry_consistent: bool
    dynamically_reachable: bool
    repair_capacity: int
    perturbation_load: int
    entropy_sink_capacity: int
    entropy_export_required: int
    stability_window: int
    required_window: int
    accessible_records: int
    record_threshold: int
    reconstruction_debt: int
    debt_budget: int
    platform_operations: int
    platform_threshold: int
    interpretation: str


@dataclass(frozen=True)
class GateVerdict:
    gate: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class ViabilityEvaluation:
    candidate: StructureCandidate
    gates: tuple[GateVerdict, ...]
    observer_experienced: bool
    emergence_platform: bool
    first_failed_gate: str | None

    def gate_passed(self, gate: str) -> bool:
        return any(verdict.gate == gate and verdict.passed for verdict in self.gates)


@dataclass(frozen=True)
class T114Result:
    evaluations: tuple[ViabilityEvaluation, ...]
    geometry_not_sufficient: bool
    maintenance_not_sufficient: bool
    finality_not_platform: bool
    finality_separates_fixed_standard_state: bool
    platform_positive_cases: tuple[str, ...]
    observer_experienced_cases: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    open_blocker: str
    recommended_next: str
    claim_ledger_update: str


def canonical_candidates() -> tuple[StructureCandidate, ...]:
    return (
        StructureCandidate(
            name="impossible_tiling",
            geometry_consistent=False,
            dynamically_reachable=False,
            repair_capacity=0,
            perturbation_load=0,
            entropy_sink_capacity=0,
            entropy_export_required=0,
            stability_window=0,
            required_window=1,
            accessible_records=0,
            record_threshold=1,
            reconstruction_debt=0,
            debt_budget=0,
            platform_operations=0,
            platform_threshold=1,
            interpretation="Geometry rejects the candidate before viability is meaningful.",
        ),
        StructureCandidate(
            name="geometric_but_unmaintained_seed",
            geometry_consistent=True,
            dynamically_reachable=True,
            repair_capacity=2,
            perturbation_load=4,
            entropy_sink_capacity=2,
            entropy_export_required=3,
            stability_window=5,
            required_window=8,
            accessible_records=4,
            record_threshold=3,
            reconstruction_debt=0,
            debt_budget=1,
            platform_operations=2,
            platform_threshold=2,
            interpretation=(
                "Geometrically admissible and reachable, but the preservation "
                "stack cannot maintain it long enough."
            ),
        ),
        StructureCandidate(
            name="maintained_but_unfinalized_wave",
            geometry_consistent=True,
            dynamically_reachable=True,
            repair_capacity=5,
            perturbation_load=3,
            entropy_sink_capacity=5,
            entropy_export_required=3,
            stability_window=8,
            required_window=8,
            accessible_records=1,
            record_threshold=3,
            reconstruction_debt=3,
            debt_budget=1,
            platform_operations=2,
            platform_threshold=2,
            interpretation=(
                "Maintenance succeeds, but bounded observers lack enough "
                "records to reconstruct it as a settled structure."
            ),
        ),
        StructureCandidate(
            name="finalized_archive_not_platform",
            geometry_consistent=True,
            dynamically_reachable=True,
            repair_capacity=5,
            perturbation_load=3,
            entropy_sink_capacity=5,
            entropy_export_required=3,
            stability_window=8,
            required_window=8,
            accessible_records=3,
            record_threshold=3,
            reconstruction_debt=0,
            debt_budget=1,
            platform_operations=1,
            platform_threshold=2,
            interpretation=(
                "The structure is stable and reconstructable, but it does not "
                "support enough downstream operations to be an emergence platform."
            ),
        ),
        StructureCandidate(
            name="visible_protocol_platform",
            geometry_consistent=True,
            dynamically_reachable=True,
            repair_capacity=5,
            perturbation_load=3,
            entropy_sink_capacity=5,
            entropy_export_required=3,
            stability_window=8,
            required_window=8,
            accessible_records=3,
            record_threshold=3,
            reconstruction_debt=0,
            debt_budget=1,
            platform_operations=3,
            platform_threshold=2,
            interpretation=(
                "Same standard maintenance state as the archive case, but enough "
                "operation rights remain for recursive emergence."
            ),
        ),
        StructureCandidate(
            name="hidden_protocol_twin",
            geometry_consistent=True,
            dynamically_reachable=True,
            repair_capacity=5,
            perturbation_load=3,
            entropy_sink_capacity=5,
            entropy_export_required=3,
            stability_window=8,
            required_window=8,
            accessible_records=2,
            record_threshold=3,
            reconstruction_debt=0,
            debt_budget=1,
            platform_operations=3,
            platform_threshold=2,
            interpretation=(
                "A fixed-standard-state control: geometry, dynamics, maintenance, "
                "and platform operations match the positive protocol case, but "
                "record access is below threshold."
            ),
        ),
    )


def evaluate_candidate(candidate: StructureCandidate) -> ViabilityEvaluation:
    geometry = GateVerdict(
        gate="geometry",
        passed=candidate.geometry_consistent,
        reason=(
            "finite constraints are mutually satisfiable"
            if candidate.geometry_consistent
            else "finite constraints are inconsistent"
        ),
    )
    dynamics = GateVerdict(
        gate="dynamics",
        passed=geometry.passed and candidate.dynamically_reachable,
        reason=(
            "candidate is reachable under the declared transition rule"
            if geometry.passed and candidate.dynamically_reachable
            else "candidate is not reachable from allowed initial states"
        ),
    )

    repair_ok = candidate.repair_capacity >= candidate.perturbation_load
    entropy_ok = candidate.entropy_sink_capacity >= candidate.entropy_export_required
    window_ok = candidate.stability_window >= candidate.required_window
    maintenance = GateVerdict(
        gate="maintenance",
        passed=dynamics.passed and repair_ok and entropy_ok and window_ok,
        reason=_maintenance_reason(candidate, repair_ok, entropy_ok, window_ok),
    )

    records_ok = candidate.accessible_records >= candidate.record_threshold
    debt_ok = candidate.reconstruction_debt <= candidate.debt_budget
    finality = GateVerdict(
        gate="finality",
        passed=maintenance.passed and records_ok and debt_ok,
        reason=_finality_reason(candidate, records_ok, debt_ok),
    )

    platform_ok = candidate.platform_operations >= candidate.platform_threshold
    emergence = GateVerdict(
        gate="emergence_platform",
        passed=finality.passed and platform_ok,
        reason=(
            "structure supports enough downstream operations for platform status"
            if platform_ok
            else "structure is reconstructable but not a platform for further emergence"
        ),
    )

    gates = (geometry, dynamics, maintenance, finality, emergence)
    first_failed = next((verdict.gate for verdict in gates if not verdict.passed), None)
    return ViabilityEvaluation(
        candidate=candidate,
        gates=gates,
        observer_experienced=finality.passed,
        emergence_platform=emergence.passed,
        first_failed_gate=first_failed,
    )


def run_t114_analysis() -> T114Result:
    evaluations = tuple(evaluate_candidate(candidate) for candidate in canonical_candidates())

    geometry_not_sufficient = any(
        evaluation.gate_passed("geometry") and not evaluation.observer_experienced
        for evaluation in evaluations
    )
    maintenance_not_sufficient = any(
        evaluation.gate_passed("maintenance") and not evaluation.observer_experienced
        for evaluation in evaluations
    )
    finality_not_platform = any(
        evaluation.observer_experienced and not evaluation.emergence_platform
        for evaluation in evaluations
    )
    finality_separates_fixed_standard_state = _fixed_standard_state_separation(evaluations)

    return T114Result(
        evaluations=evaluations,
        geometry_not_sufficient=geometry_not_sufficient,
        maintenance_not_sufficient=maintenance_not_sufficient,
        finality_not_platform=finality_not_platform,
        finality_separates_fixed_standard_state=finality_separates_fixed_standard_state,
        platform_positive_cases=tuple(
            evaluation.candidate.name
            for evaluation in evaluations
            if evaluation.emergence_platform
        ),
        observer_experienced_cases=tuple(
            evaluation.candidate.name
            for evaluation in evaluations
            if evaluation.observer_experienced
        ),
        strongest_claim=(
            "In this finite witness family, geometry is a possibility space, "
            "not a viability criterion. Structures become observer-experienced "
            "only after reachability, maintenance, and record-finality gates pass; "
            "emergence-platform status is a stricter downstream gate."
        ),
        improved=(
            "T114 turns the synthesis into a falsifiable filter with negative "
            "controls. It shows exactly where geometry, maintenance, finality, "
            "and emergence-platform capacity can separate without claiming a new "
            "law of physics."
        ),
        weakened=(
            "The artifact weakens any broad reading of the slogan. If all future "
            "positive cases are already fixed by standard maintenance and "
            "thermodynamic accounting, the viability filter is only bookkeeping. "
            "The only non-collapse signal here is the fixed-standard-state pair "
            "where record accessibility changes the observer-experienced verdict."
        ),
        falsification_condition=(
            "The viability-filter thesis loses independent content if every "
            "observer-experienced or platform verdict is determined by geometry, "
            "dynamics, and standard maintenance variables alone, with no "
            "pre-registered record-finality or operation-right separation."
        ),
        open_blocker=(
            "The current filter is a finite schema, not a derived theorem. It "
            "needs a real domain instantiation where the gates are measured or "
            "canonically derived rather than assigned."
        ),
        recommended_next=(
            "Instantiate the filter on one serious domain, preferably cellular "
            "automata or a D1RestrictionSystem transport case, and test whether "
            "the finality/emergence gates survive after matching standard "
            "stability and entropy variables."
        ),
        claim_ledger_update=(
            "Add T114 as a North-Star/viability-filter artifact only: geometry "
            "can be treated as a finite possibility space, while maintenance, "
            "record-finality, and emergence-platform gates classify which "
            "candidates become observer-experienced. No core claim is upgraded."
        ),
    )


def t114_result_to_dict(result: T114Result) -> dict[str, object]:
    return {
        "evaluations": [_evaluation_to_dict(evaluation) for evaluation in result.evaluations],
        "geometry_not_sufficient": result.geometry_not_sufficient,
        "maintenance_not_sufficient": result.maintenance_not_sufficient,
        "finality_not_platform": result.finality_not_platform,
        "finality_separates_fixed_standard_state": (
            result.finality_separates_fixed_standard_state
        ),
        "platform_positive_cases": list(result.platform_positive_cases),
        "observer_experienced_cases": list(result.observer_experienced_cases),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
        "claim_ledger_update": result.claim_ledger_update,
    }


def _evaluation_to_dict(evaluation: ViabilityEvaluation) -> dict[str, object]:
    candidate = evaluation.candidate
    return {
        "name": candidate.name,
        "interpretation": candidate.interpretation,
        "observer_experienced": evaluation.observer_experienced,
        "emergence_platform": evaluation.emergence_platform,
        "first_failed_gate": evaluation.first_failed_gate,
        "standard_state_signature": _standard_state_signature(candidate),
        "gates": [
            {
                "gate": gate.gate,
                "passed": gate.passed,
                "reason": gate.reason,
            }
            for gate in evaluation.gates
        ],
    }


def _fixed_standard_state_separation(
    evaluations: tuple[ViabilityEvaluation, ...],
) -> bool:
    by_signature: dict[tuple[object, ...], set[bool]] = {}
    for evaluation in evaluations:
        signature = _standard_state_signature(evaluation.candidate)
        by_signature.setdefault(signature, set()).add(evaluation.observer_experienced)
    return any(len(verdicts) > 1 for verdicts in by_signature.values())


def _standard_state_signature(candidate: StructureCandidate) -> tuple[object, ...]:
    return (
        candidate.geometry_consistent,
        candidate.dynamically_reachable,
        candidate.repair_capacity,
        candidate.perturbation_load,
        candidate.entropy_sink_capacity,
        candidate.entropy_export_required,
        candidate.stability_window,
        candidate.required_window,
        candidate.platform_operations,
        candidate.platform_threshold,
    )


def _maintenance_reason(
    candidate: StructureCandidate,
    repair_ok: bool,
    entropy_ok: bool,
    window_ok: bool,
) -> str:
    failures = []
    if not repair_ok:
        failures.append(
            f"repair capacity {candidate.repair_capacity} < load {candidate.perturbation_load}"
        )
    if not entropy_ok:
        failures.append(
            "entropy sink capacity "
            f"{candidate.entropy_sink_capacity} < required {candidate.entropy_export_required}"
        )
    if not window_ok:
        failures.append(
            f"stability window {candidate.stability_window} < required {candidate.required_window}"
        )
    if failures:
        return "; ".join(failures)
    return "repair, entropy export, and stability-window constraints all pass"


def _finality_reason(
    candidate: StructureCandidate,
    records_ok: bool,
    debt_ok: bool,
) -> str:
    failures = []
    if not records_ok:
        failures.append(
            f"accessible records {candidate.accessible_records} < threshold {candidate.record_threshold}"
        )
    if not debt_ok:
        failures.append(
            f"reconstruction debt {candidate.reconstruction_debt} > budget {candidate.debt_budget}"
        )
    if failures:
        return "; ".join(failures)
    return "record threshold and reconstruction-debt budget both pass"


if __name__ == "__main__":
    import json

    print(json.dumps(t114_result_to_dict(run_t114_analysis()), indent=2))
