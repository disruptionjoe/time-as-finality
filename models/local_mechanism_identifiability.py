"""T44: Local mechanism identifiability audit.

T43 showed that multiple finite mechanisms can generate identical local
accumulation traces. T44 probes those equivalent mechanisms to ask whether the
equivalence is removable by finite perturbation observables.

This module stays inside the finite toy framework. It does not derive proper
time and does not add spacetime dynamics.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import combinations
from typing import Any

from models.local_persistence_mechanisms import (
    EVENT_COUNT,
    MechanismTrace,
    interaction_density_trace,
    intrinsic_stabilization_trace,
    resource_budget_trace,
)


MECHANISMS = ("intrinsic_rate", "resource_budget", "interaction_density")
BASELINE_EVENT_COUNT = EVENT_COUNT


@dataclass(frozen=True)
class ProbeResponse:
    """One mechanism's finite response to one probe."""

    mechanism_id: str
    probe_name: str
    trace: MechanismTrace
    observable_signature: tuple[int, ...]
    total_accumulation: int
    mean_rate: float
    changed_from_baseline: bool


@dataclass(frozen=True)
class PairSeparation:
    """Whether a pair of mechanisms is separated by a probe set."""

    pair: tuple[str, str]
    separating_probes: tuple[str, ...]
    separated: bool


@dataclass(frozen=True)
class ProbeProtocolResult:
    """Result for one finite probe protocol."""

    probe_name: str
    description: str
    responses: tuple[ProbeResponse, ...]
    separated_pairs: tuple[tuple[str, str], ...]
    unresolved_pairs: tuple[tuple[str, str], ...]
    separates_all: bool
    finding: str


@dataclass(frozen=True)
class MinimalObservableBasis:
    """Smallest probe set found that separates all mechanism IDs."""

    probe_names: tuple[str, ...]
    separates_all: bool
    separated_pairs: tuple[PairSeparation, ...]
    unresolved_pairs: tuple[tuple[str, str], ...]
    reason: str


@dataclass(frozen=True)
class UnresolvedEquivalence:
    """A finite equivalence that remains under a named probe set."""

    name: str
    probe_names: tuple[str, ...]
    unresolved_pairs: tuple[tuple[str, str], ...]
    reason: str


@dataclass(frozen=True)
class HypothesisEvaluation:
    """T44 hypothesis verdict."""

    hypothesis_id: str
    claim: str
    status: str
    evidence_for: tuple[str, ...]
    evidence_against: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class T44Result:
    """Full T44 result."""

    probe_results: tuple[ProbeProtocolResult, ...]
    minimal_basis: MinimalObservableBasis
    unresolved_equivalences: tuple[UnresolvedEquivalence, ...]
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    best_supported_hypothesis: str
    theorem: str
    boundary: str
    recommendation: str


def baseline_trace(mechanism_id: str, event_count: int = BASELINE_EVENT_COUNT) -> MechanismTrace:
    """Return the T43-equivalent baseline trace for a mechanism."""

    if mechanism_id == "intrinsic_rate":
        return intrinsic_stabilization_trace("intrinsic_rate_baseline", rate=2, event_count=event_count)
    if mechanism_id == "resource_budget":
        return resource_budget_trace(
            "resource_budget_baseline",
            update_demand=2,
            stabilization_budget=2,
            event_count=event_count,
        )
    if mechanism_id == "interaction_density":
        return interaction_density_trace(
            "interaction_density_baseline",
            base_rate=1,
            coupling_strength=1,
            interaction_count=1,
            event_count=event_count,
        )
    raise ValueError(f"unknown mechanism_id: {mechanism_id}")


def trace_for_probe(mechanism_id: str, probe_name: str) -> MechanismTrace:
    """Generate a mechanism trace under a finite probe."""

    if probe_name == "baseline":
        return baseline_trace(mechanism_id)

    if probe_name == "event_count_scaling":
        return baseline_trace(mechanism_id, event_count=20)

    if probe_name == "demand_drop":
        if mechanism_id == "resource_budget":
            return resource_budget_trace(
                "resource_budget_demand_drop",
                update_demand=1,
                stabilization_budget=2,
            )
        return baseline_trace(mechanism_id)

    if probe_name == "resource_shock":
        if mechanism_id == "resource_budget":
            return resource_budget_trace(
                "resource_budget_resource_shock",
                update_demand=2,
                stabilization_budget=1,
            )
        return baseline_trace(mechanism_id)

    if probe_name == "coupling_rewire":
        if mechanism_id == "interaction_density":
            return interaction_density_trace(
                "interaction_density_coupling_rewire",
                base_rate=1,
                coupling_strength=1,
                interaction_count=0,
            )
        return baseline_trace(mechanism_id)

    if probe_name == "load_recovery":
        if mechanism_id == "resource_budget":
            return MechanismTrace(
                name="resource_budget_load_recovery",
                mechanism_type="finite_resource_budget",
                parameters={
                    "phase_1_demand": 3,
                    "phase_2_demand": 2,
                    "stabilization_budget": 2,
                    "event_count": BASELINE_EVENT_COUNT,
                },
                deltas=(2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
                total_accumulation=20,
                mean_rate=2.0,
                depends_on_propagation=False,
            )
        return baseline_trace(mechanism_id)

    raise ValueError(f"unknown probe_name: {probe_name}")


def _all_pairs() -> tuple[tuple[str, str], ...]:
    return tuple(combinations(MECHANISMS, 2))


def response_for_probe(mechanism_id: str, probe_name: str) -> ProbeResponse:
    """Compute one finite probe response."""

    trace = trace_for_probe(mechanism_id, probe_name)
    baseline = baseline_trace(mechanism_id, event_count=len(trace.deltas))
    signature = trace.deltas
    return ProbeResponse(
        mechanism_id=mechanism_id,
        probe_name=probe_name,
        trace=trace,
        observable_signature=signature,
        total_accumulation=trace.total_accumulation,
        mean_rate=trace.mean_rate,
        changed_from_baseline=trace.deltas != baseline.deltas,
    )


def evaluate_probe(probe_name: str, description: str) -> ProbeProtocolResult:
    """Evaluate which mechanism pairs one probe separates."""

    responses = tuple(response_for_probe(mechanism_id, probe_name) for mechanism_id in MECHANISMS)
    by_mechanism = {response.mechanism_id: response for response in responses}
    separated: list[tuple[str, str]] = []
    unresolved: list[tuple[str, str]] = []
    for a, b in _all_pairs():
        if by_mechanism[a].observable_signature != by_mechanism[b].observable_signature:
            separated.append((a, b))
        else:
            unresolved.append((a, b))
    separates_all = len(unresolved) == 0
    finding = (
        f"{probe_name}: separates {len(separated)} of {len(_all_pairs())} pairs; "
        f"unresolved={tuple(unresolved)}"
    )
    return ProbeProtocolResult(
        probe_name=probe_name,
        description=description,
        responses=responses,
        separated_pairs=tuple(separated),
        unresolved_pairs=tuple(unresolved),
        separates_all=separates_all,
        finding=finding,
    )


def evaluate_probe_suite(probe_names: tuple[str, ...]) -> tuple[PairSeparation, ...]:
    """Evaluate pair separation under a set of probes."""

    responses_by_probe = {
        probe: {mechanism: response_for_probe(mechanism, probe) for mechanism in MECHANISMS}
        for probe in probe_names
    }
    result: list[PairSeparation] = []
    for a, b in _all_pairs():
        separating = tuple(
            probe
            for probe in probe_names
            if responses_by_probe[probe][a].observable_signature
            != responses_by_probe[probe][b].observable_signature
        )
        result.append(
            PairSeparation(
                pair=(a, b),
                separating_probes=separating,
                separated=bool(separating),
            )
        )
    return tuple(result)


def find_minimal_basis(candidate_probes: tuple[str, ...]) -> MinimalObservableBasis:
    """Find the smallest probe subset that separates all mechanism pairs."""

    for size in range(1, len(candidate_probes) + 1):
        for subset in combinations(candidate_probes, size):
            pair_results = evaluate_probe_suite(tuple(subset))
            unresolved = tuple(item.pair for item in pair_results if not item.separated)
            if not unresolved:
                return MinimalObservableBasis(
                    probe_names=tuple(subset),
                    separates_all=True,
                    separated_pairs=pair_results,
                    unresolved_pairs=(),
                    reason=(
                        "This is the first smallest subset, in declared probe order, "
                        "that separates all T43 baseline mechanism families."
                    ),
                )
    all_results = evaluate_probe_suite(candidate_probes)
    unresolved = tuple(item.pair for item in all_results if not item.separated)
    return MinimalObservableBasis(
        probe_names=candidate_probes,
        separates_all=False,
        separated_pairs=all_results,
        unresolved_pairs=unresolved,
        reason="No finite probe subset in the candidate set separates all pairs.",
    )


def build_probe_results() -> tuple[ProbeProtocolResult, ...]:
    """Run all T44 probe protocols."""

    probe_specs = (
        (
            "baseline",
            "No perturbation. Confirms the T43 equivalence class.",
        ),
        (
            "event_count_scaling",
            "Increase local event count while preserving per-event mechanism parameters.",
        ),
        (
            "demand_drop",
            "Lower update demand. Resource-budget mechanisms respond; others do not.",
        ),
        (
            "resource_shock",
            "Lower stabilization budget. Resource-budget mechanisms respond; others do not.",
        ),
        (
            "coupling_rewire",
            "Reduce local interaction count. Interaction-density mechanisms respond; others do not.",
        ),
        (
            "load_recovery",
            "Apply finite load then recovery. In this simple trace model it does not separate mechanisms.",
        ),
    )
    return tuple(evaluate_probe(name, description) for name, description in probe_specs)


def build_unresolved_equivalences(
    probe_results: tuple[ProbeProtocolResult, ...],
) -> tuple[UnresolvedEquivalence, ...]:
    """Record informative unresolved equivalences."""

    by_name = {result.probe_name: result for result in probe_results}
    unresolved: list[UnresolvedEquivalence] = []
    for probe_name in ("baseline", "event_count_scaling", "load_recovery"):
        result = by_name[probe_name]
        if result.unresolved_pairs:
            unresolved.append(
                UnresolvedEquivalence(
                    name=f"{probe_name}_equivalence",
                    probe_names=(probe_name,),
                    unresolved_pairs=result.unresolved_pairs,
                    reason=(
                        f"{probe_name} leaves mechanisms trace-equivalent under "
                        "the current observable signature."
                    ),
                )
            )
    return tuple(unresolved)


def evaluate_hypotheses(
    probe_results: tuple[ProbeProtocolResult, ...],
    minimal_basis: MinimalObservableBasis,
    unresolved: tuple[UnresolvedEquivalence, ...],
) -> tuple[HypothesisEvaluation, ...]:
    """Evaluate H0-H5 from T44 evidence."""

    by_name = {result.probe_name: result for result in probe_results}

    return (
        HypothesisEvaluation(
            hypothesis_id="H0",
            claim="The mechanisms remain indistinguishable in the current finite framework.",
            status="rejected",
            evidence_for=(
                "Baseline and event-count scaling leave mechanisms indistinguishable.",
            ),
            evidence_against=(
                "Demand-drop separates resource budget from the other mechanisms.",
                "Coupling-rewire separates interaction density from the other mechanisms.",
                "The minimal basis separates all T43 baseline mechanism families.",
            ),
            verdict="Rejected for the T43 mechanism family set.",
        ),
        HypothesisEvaluation(
            hypothesis_id="H1",
            claim="Intrinsic rate is distinguishable by stability under perturbation.",
            status="partially_supported",
            evidence_for=(
                "Intrinsic-rate response is stable under demand-drop and coupling-rewire probes.",
                "The combined probe vector distinguishes intrinsic rate from resource budget and interaction density.",
            ),
            evidence_against=(
                "Stability under any single irrelevant probe is not unique.",
                "Baseline and event-count scaling do not distinguish intrinsic rate.",
            ),
            verdict="Supported only as a probe-vector property, not as a single-probe marker.",
        ),
        HypothesisEvaluation(
            hypothesis_id="H2",
            claim="Resource budget is distinguishable by saturation under changed demand or resource shock.",
            status="supported",
            evidence_for=(
                f"Demand-drop unresolved pairs: {by_name['demand_drop'].unresolved_pairs}.",
                f"Resource-shock unresolved pairs: {by_name['resource_shock'].unresolved_pairs}.",
                "Both probes separate resource budget from intrinsic rate and interaction density.",
            ),
            evidence_against=(
                "Demand-drop and resource-shock are redundant in this simple trace model.",
            ),
            verdict="Supported for finite T43 mechanisms.",
        ),
        HypothesisEvaluation(
            hypothesis_id="H3",
            claim="Interaction density is distinguishable by sensitivity to local coupling changes.",
            status="supported",
            evidence_for=(
                "Coupling-rewire separates interaction density from intrinsic rate and resource budget.",
            ),
            evidence_against=(
                "Coupling-rewire alone leaves intrinsic rate and resource budget unresolved.",
            ),
            verdict="Supported for finite T43 mechanisms.",
        ),
        HypothesisEvaluation(
            hypothesis_id="H4",
            claim="A small observable basis separates all T43 mechanisms.",
            status="best_supported" if minimal_basis.separates_all else "not_supported",
            evidence_for=(
                f"Minimal basis found: {minimal_basis.probe_names}.",
                "Demand-drop plus coupling-rewire separates all three baseline mechanisms.",
            ),
            evidence_against=(
                "The basis is only for the finite T43 mechanism family set.",
                "Unresolved equivalences remain under weaker probe sets.",
            ),
            verdict=(
                "Best supported. A two-probe observable basis separates the T43 mechanisms."
                if minimal_basis.separates_all
                else "Not supported by the candidate probes."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H5",
            claim="No finite observable basis separates them without richer dynamics.",
            status="rejected_for_t43_family",
            evidence_for=(
                f"Unresolved weaker probe sets remain: {tuple(item.name for item in unresolved)}.",
            ),
            evidence_against=(
                "The minimal finite probe basis separates all T43 baseline mechanisms.",
            ),
            verdict="Rejected for the T43 mechanism family set, but open for richer mechanisms.",
        ),
    )


def run_t44_analysis() -> T44Result:
    """Run the T44 identifiability audit."""

    probe_results = build_probe_results()
    candidate_basis_probes = (
        "demand_drop",
        "coupling_rewire",
        "resource_shock",
        "event_count_scaling",
        "load_recovery",
    )
    minimal_basis = find_minimal_basis(candidate_basis_probes)
    unresolved = build_unresolved_equivalences(probe_results)
    hypotheses = evaluate_hypotheses(probe_results, minimal_basis, unresolved)
    return T44Result(
        probe_results=probe_results,
        minimal_basis=minimal_basis,
        unresolved_equivalences=unresolved,
        hypothesis_evaluations=hypotheses,
        best_supported_hypothesis="H4",
        theorem=(
            "Finite Probe Identifiability Theorem: the T43 trace-equivalent "
            "mechanisms are not identifiable from baseline local accumulation "
            "alone, but a two-probe finite observable basis, demand_drop plus "
            "coupling_rewire, separates intrinsic rate, resource budget, and "
            "interaction density."
        ),
        boundary=(
            "The theorem is limited to the finite T43 mechanism families and "
            "the declared probe set. It does not identify a physical proper-time "
            "mechanism and does not rule out new mechanisms with identical probe "
            "response vectors."
        ),
        recommendation=(
            "Promote demand sensitivity and coupling sensitivity as the minimal "
            "next observable basis for local accumulation studies. Keep baseline "
            "trace equivalence as a live warning against overinterpreting local "
            "accumulation curves."
        ),
    )


def t44_result_to_dict(result: T44Result) -> dict[str, Any]:
    """Serialize T44 result for JSON output."""

    return asdict(result)
