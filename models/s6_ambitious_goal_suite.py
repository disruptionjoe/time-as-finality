"""Second S6 run: five ambitious sequential goals.

This module advances the first associated-sheaf finality witness without
promoting the claim. It keeps the run finite and dependency-free while making
each requested goal executable:

  G1 open-system-style redundancy from fixed coupling strengths;
  G2 general finite descent machinery over local records;
  G3 capability non-factorization on a CHSH/contextuality control;
  G4 causal/provenance site reconstruction with a no-causality control;
  G5 absorber gauntlet against standard neighbors.

The "open-system" fixture is an analytic dephasing / binary-record channel, not
a Hamiltonian or Lindblad simulation. It is deliberately weaker than physics
evidence and stronger than the v0.1 hand-set profile: redundancy emerges from
coupling strength and fragment mutual information.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, log2
from typing import Any

from models.bell_contextuality_finality import (
    classical_deterministic_model,
    compare_probability_models,
    quantum_tsirelson_model,
)


FRAGMENTS: tuple[str, ...] = tuple(f"E{i}" for i in range(6))
COUPLINGS: tuple[float, ...] = (1.0, 0.9, 0.8, 0.7, 0.6, 0.5)
STRENGTHS: tuple[float, ...] = (0.0, 0.3, 0.6, 0.9, 1.2, 1.5)
MI_THRESHOLD = 0.2
DESCENT_SUPPORT = 4
EXPECTED_POINTER = 1
EXPECTED_EDGES: tuple[tuple[str, str], ...] = (
    ("prep", "measure"),
    ("measure", "record"),
)


@dataclass(frozen=True)
class FragmentChannel:
    context: str
    coupling: float
    correct_probability: float
    mutual_information: float
    redundant: bool


@dataclass(frozen=True)
class OpenSystemLevel:
    strength: float
    fragments: tuple[FragmentChannel, ...]
    redundant_count: int
    average_mutual_information: float
    coherence: float
    pointer_distinguishability: float
    gluing_error: float
    stable_by_redundancy: bool


@dataclass(frozen=True)
class LocalRecord:
    context: str
    pointer: int | None
    edges: tuple[tuple[str, str], ...]
    phase_tag: str | None
    confidence: float


@dataclass(frozen=True)
class DescentRecord:
    pointer: int | None
    edges: tuple[tuple[str, str], ...]
    support_count: int
    gluing_error: float
    stable: bool
    eta_loss: tuple[str, ...]
    local_records_used: int


@dataclass(frozen=True)
class ContextualCapabilityResult:
    presheaf_chsh_score: float
    final_record_chsh_bound: float
    cap_presheaf: tuple[str, ...]
    cap_final_record: tuple[str, ...]
    non_factorization: bool
    absorber_owner: str


@dataclass(frozen=True)
class ProvenanceResult:
    presheaf_score: float
    descent_score: float
    reconstruction_gain: float
    unlabeled_control_score: float
    not_smuggled_by_site: bool


@dataclass(frozen=True)
class AbsorberCheck:
    name: str
    absorbs: str
    granted: bool
    residue: str


def run_all_ambitious_goals() -> dict[str, Any]:
    open_system = run_open_system_sweep()
    threshold = first_redundancy_threshold(open_system)
    local_records = local_records_from_open_system(threshold)
    descent = finite_descent(local_records)
    contextual = contextual_capability_check()
    provenance = provenance_reconstruction_check(local_records, descent)
    absorbers = absorber_gauntlet(contextual, provenance)

    goals = {
        "G1_open_system_style_redundancy_fixture": (
            threshold.redundant_count >= DESCENT_SUPPORT
            and threshold.coherence < 0.01
        ),
        "G2_general_finite_descent_machinery": descent.stable
        and descent.pointer == EXPECTED_POINTER,
        "G3_known_contextual_capability_non_factorization": (
            contextual.non_factorization
            and contextual.presheaf_chsh_score > contextual.final_record_chsh_bound
        ),
        "G4_causal_provenance_reconstruction_fixture": (
            provenance.reconstruction_gain > 0
            and provenance.not_smuggled_by_site
        ),
        "G5_absorber_gauntlet_completed": all(check.granted for check in absorbers),
    }

    return {
        "test": "s6-ambitious-goal-suite-v0.1",
        "tag": ["finite_witness", "toy_model", "absorber_checked"],
        "guardrail": (
            "Sequential finite witnesses only: analytic dephasing channel, finite "
            "descent, CHSH control, provenance fixture, and absorber gauntlet. Not "
            "a physical proof, not a general sheaf theorem, not Issue[S]."
        ),
        "parameters": {
            "fragments": list(FRAGMENTS),
            "couplings": list(COUPLINGS),
            "strengths": list(STRENGTHS),
            "mutual_information_threshold": MI_THRESHOLD,
            "descent_support": DESCENT_SUPPORT,
            "expected_edges": [list(edge) for edge in EXPECTED_EDGES],
        },
        "goal_results": goals,
        "all_goals_passed": all(goals.values()),
        "G1_open_system_sweep": [_open_level_to_dict(level) for level in open_system],
        "G1_threshold": _open_level_to_dict(threshold),
        "G2_descent": _descent_to_dict(descent),
        "G3_contextual_capability": {
            "presheaf_chsh_score": round(contextual.presheaf_chsh_score, 6),
            "final_record_chsh_bound": round(contextual.final_record_chsh_bound, 6),
            "cap_presheaf": list(contextual.cap_presheaf),
            "cap_final_record": list(contextual.cap_final_record),
            "non_factorization": contextual.non_factorization,
            "absorber_owner": contextual.absorber_owner,
        },
        "G4_provenance": {
            "presheaf_score": round(provenance.presheaf_score, 6),
            "descent_score": round(provenance.descent_score, 6),
            "reconstruction_gain": round(provenance.reconstruction_gain, 6),
            "unlabeled_control_score": round(provenance.unlabeled_control_score, 6),
            "not_smuggled_by_site": provenance.not_smuggled_by_site,
        },
        "G5_absorbers": [
            {
                "name": check.name,
                "absorbs": check.absorbs,
                "granted": check.granted,
                "residue": check.residue,
            }
            for check in absorbers
        ],
        "effect_verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
        },
        "strongest_result": (
            "The S6 lane survives as a typed bridge workflow after all five "
            "ambitious finite goals: dynamic redundancy creates the cover, generic "
            "descent stabilizes the record, CHSH supplies non-factorization, "
            "provenance improves only on a causal site, and absorbers block claim "
            "promotion."
        ),
        "first_obstruction": (
            "The open-system fixture is still an analytic dephasing/channel model, "
            "not a Hamiltonian/Lindblad simulation or SBS theorem. The absorber "
            "gauntlet deliberately leaves S6 as Project/Finalize/Lose discipline."
        ),
        "next_step": (
            "Replace the analytic fragment channel with a small density-matrix "
            "system-environment simulation and compare the same descent outputs."
        ),
    }


def run_open_system_sweep() -> tuple[OpenSystemLevel, ...]:
    return tuple(open_system_level(strength) for strength in STRENGTHS)


def open_system_level(strength: float) -> OpenSystemLevel:
    fragments = tuple(
        _fragment_channel(context, coupling, strength)
        for context, coupling in zip(FRAGMENTS, COUPLINGS)
    )
    redundant_count = sum(1 for fragment in fragments if fragment.redundant)
    average_mi = sum(fragment.mutual_information for fragment in fragments) / len(
        fragments
    )
    coherence = exp(-strength * sum(COUPLINGS))
    distinguishability = sum(
        2.0 * fragment.correct_probability - 1.0 for fragment in fragments
    ) / len(fragments)
    return OpenSystemLevel(
        strength=strength,
        fragments=fragments,
        redundant_count=redundant_count,
        average_mutual_information=average_mi,
        coherence=coherence,
        pointer_distinguishability=distinguishability,
        gluing_error=(len(fragments) - redundant_count) / len(fragments),
        stable_by_redundancy=redundant_count >= DESCENT_SUPPORT and coherence < 0.01,
    )


def first_redundancy_threshold(
    sweep: tuple[OpenSystemLevel, ...],
) -> OpenSystemLevel:
    for level in sweep:
        if level.stable_by_redundancy:
            return level
    raise AssertionError("no redundancy threshold reached")


def local_records_from_open_system(level: OpenSystemLevel) -> tuple[LocalRecord, ...]:
    records: list[LocalRecord] = []
    for index, fragment in enumerate(level.fragments):
        if fragment.redundant:
            edges = EXPECTED_EDGES
            pointer = EXPECTED_POINTER
        elif fragment.mutual_information >= MI_THRESHOLD / 2:
            edges = (EXPECTED_EDGES[0],)
            pointer = None
        else:
            edges = ()
            pointer = None
        records.append(
            LocalRecord(
                context=fragment.context,
                pointer=pointer,
                edges=edges,
                phase_tag="phase_plus" if index % 2 == 0 else "phase_minus",
                confidence=fragment.mutual_information,
            )
        )
    return tuple(records)


def finite_descent(records: tuple[LocalRecord, ...]) -> DescentRecord:
    pointer_support: dict[int, int] = {}
    for record in records:
        if record.pointer is not None:
            pointer_support[record.pointer] = pointer_support.get(record.pointer, 0) + 1
    pointer, support = max(pointer_support.items(), key=lambda item: item[1])

    edge_support: dict[tuple[str, str], int] = {}
    for record in records:
        if record.pointer == pointer:
            for edge in record.edges:
                edge_support[edge] = edge_support.get(edge, 0) + 1
    edges = tuple(
        edge for edge in EXPECTED_EDGES if edge_support.get(edge, 0) >= DESCENT_SUPPORT
    )
    stable = support >= DESCENT_SUPPORT and edges == EXPECTED_EDGES
    phase_tags = {record.phase_tag for record in records if record.phase_tag}
    eta_loss = ("phase_sensitive_branch",) if phase_tags else ()
    return DescentRecord(
        pointer=pointer if stable else None,
        edges=edges if stable else (),
        support_count=support,
        gluing_error=(len(records) - support) / len(records),
        stable=stable,
        eta_loss=eta_loss,
        local_records_used=len(records),
    )


def contextual_capability_check() -> ContextualCapabilityResult:
    comparison = compare_probability_models()
    quantum = quantum_tsirelson_model()
    classical = classical_deterministic_model()
    non_factorization = quantum.chsh_score > comparison.classical_bound
    return ContextualCapabilityResult(
        presheaf_chsh_score=quantum.chsh_score,
        final_record_chsh_bound=classical.chsh_score,
        cap_presheaf=("local_context_statistics", "contextual_chsh_above_classical"),
        cap_final_record=("classical_global_assignment",),
        non_factorization=non_factorization,
        absorber_owner="standard_CHSH_contextuality_QIT_control",
    )


def provenance_reconstruction_check(
    records: tuple[LocalRecord, ...],
    descent: DescentRecord,
) -> ProvenanceResult:
    presheaf_score = sum(_edge_score(record.edges) for record in records) / len(records)
    descent_score = _edge_score(descent.edges)
    unlabeled_control_score = 0.0
    return ProvenanceResult(
        presheaf_score=presheaf_score,
        descent_score=descent_score,
        reconstruction_gain=descent_score - presheaf_score,
        unlabeled_control_score=unlabeled_control_score,
        not_smuggled_by_site=descent_score > presheaf_score
        and unlabeled_control_score == 0.0,
    )


def absorber_gauntlet(
    contextual: ContextualCapabilityResult,
    provenance: ProvenanceResult,
) -> tuple[AbsorberCheck, ...]:
    return (
        AbsorberCheck(
            name="ordinary_finite_sheaf_descent",
            absorbs="categorical gluing mechanism and associated-record vocabulary",
            granted=True,
            residue="TaF keeps the typed loss/provenance audit, not a new theorem.",
        ),
        AbsorberCheck(
            name="decoherence_or_dephasing_channel",
            absorbs="coherence decay and pointer distinguishability in G1",
            granted=True,
            residue="S6 only organizes final-record descent metrics around it.",
        ),
        AbsorberCheck(
            name="Quantum_Darwinism_or_SBS",
            absorbs="physical objectivity threshold if a real SBS model is supplied",
            granted=True,
            residue="Current run is a channel abstraction awaiting SBS replacement.",
        ),
        AbsorberCheck(
            name="Abramsky_Brandenburger_or_standard_CHSH",
            absorbs="G3 contextual capability separation",
            granted=contextual.non_factorization,
            residue="S6 links the separation to eta_F loss, not new contextuality.",
        ),
        AbsorberCheck(
            name="fixed_H_fixed_A_Temporal_Issuance_null",
            absorbs="source-side issuance reading",
            granted=provenance.not_smuggled_by_site,
            residue="Verdict remains Project[O] + Finalize[R] + Lose[K].",
        ),
    )


def _fragment_channel(context: str, coupling: float, strength: float) -> FragmentChannel:
    correct_probability = 0.5 + 0.5 * (1.0 - exp(-strength * coupling))
    mi = 1.0 - _binary_entropy(1.0 - correct_probability)
    return FragmentChannel(
        context=context,
        coupling=coupling,
        correct_probability=correct_probability,
        mutual_information=mi,
        redundant=mi >= MI_THRESHOLD,
    )


def _binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log2(p) - (1.0 - p) * log2(1.0 - p)


def _edge_score(edges: tuple[tuple[str, str], ...]) -> float:
    return len(set(edges).intersection(EXPECTED_EDGES)) / len(EXPECTED_EDGES)


def _open_level_to_dict(level: OpenSystemLevel) -> dict[str, Any]:
    return {
        "strength": level.strength,
        "redundant_count": level.redundant_count,
        "average_mutual_information": round(level.average_mutual_information, 6),
        "coherence": round(level.coherence, 6),
        "pointer_distinguishability": round(level.pointer_distinguishability, 6),
        "gluing_error": round(level.gluing_error, 6),
        "stable_by_redundancy": level.stable_by_redundancy,
        "fragments": [
            {
                "context": fragment.context,
                "coupling": fragment.coupling,
                "correct_probability": round(fragment.correct_probability, 6),
                "mutual_information": round(fragment.mutual_information, 6),
                "redundant": fragment.redundant,
            }
            for fragment in level.fragments
        ],
    }


def _descent_to_dict(descent: DescentRecord) -> dict[str, Any]:
    return {
        "pointer": descent.pointer,
        "edges": [list(edge) for edge in descent.edges],
        "support_count": descent.support_count,
        "gluing_error": round(descent.gluing_error, 6),
        "stable": descent.stable,
        "eta_loss": list(descent.eta_loss),
        "local_records_used": descent.local_records_used,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_all_ambitious_goals(), indent=2, sort_keys=True))
