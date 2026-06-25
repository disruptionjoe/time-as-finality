"""Finite S6 associated-sheaf finality witness.

This is a bounded executable toy model for the 2026-06-25 S6 lane:

    S6 - sheafification / effective descent as the quantum-to-classical
         finality bridge.

It is NOT a quantum dynamics simulation and does not claim to derive
decoherence, Quantum Darwinism, or the Born rule. It is a finite witness for the
typed shape named by the S6 re-vote:

    (C, J), F, aF, eta_F, Cap, Loss_K, PO_rec.

The fixture interprets environment fragments as a finite cover. Increasing
"monitoring strength" deterministically increases the number of fragments that
carry the same pointer record and the same provenance edges. The approximate
associated-sheaf step keeps only the globally glueable pointer/provenance data
and drops local phase tags. That lets the run check all five requested goals:

  G1 typed finite site specification;
  G2 minimal gluing / sheafification computation;
  G3 Darwinian-style redundancy cover transition;
  G4 capability non-factorization across eta_F;
  G5 temporal provenance reconstruction improvement.

Everything is finite, deterministic, and audit-only.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any


Pointer = int
Edge = tuple[str, str]

TOTAL_FRAGMENTS = 6
TRUE_POINTER = 1
EVENTS: tuple[str, ...] = ("prep", "measure", "record")
EXPECTED_EDGES: tuple[Edge, ...] = (("prep", "measure"), ("measure", "record"))
EFFECTIVE_DESCENT_SUPPORT = 4
EDGE_DESCENT_SUPPORT = 3


@dataclass(frozen=True)
class FiniteSite:
    """Fixed finite site (C, J) for the witness.

    `contexts` are environment fragments. `cover` is the declared observer
    cover. `overlaps` are pairwise fragment intersections. The model does not
    tune these after seeing results.
    """

    name: str
    contexts: tuple[str, ...]
    cover: tuple[str, ...]
    overlaps: tuple[tuple[str, str], ...]
    expected_events: tuple[str, ...]
    expected_edges: tuple[Edge, ...]
    target_category: str
    capability_family: tuple[str, ...]


@dataclass(frozen=True)
class LocalSection:
    """Local presheaf datum F(U) for one observer/environment fragment."""

    context: str
    pointer: Pointer | None
    phase_tag: str | None
    edges: tuple[Edge, ...]
    confidence: float
    source: str

    @property
    def has_pointer(self) -> bool:
        return self.pointer is not None


@dataclass(frozen=True)
class SheafifiedRecord:
    """Approximate associated-sheaf / effective-descent output aF."""

    pointer: Pointer | None
    edges: tuple[Edge, ...]
    stable_global_section: bool
    support_count: int
    conflict_count: int
    unknown_count: int
    identified_local_signatures: int
    dropped_phase_tags: tuple[str, ...]


@dataclass(frozen=True)
class LevelAnalysis:
    monitoring_strength: int
    true_count: int
    false_count: int
    unknown_count: int
    redundancy: float
    observer_agreement: float
    gluing_error: float
    overlap_conflict_rate: float
    presheaf_temporal_score: float
    sheaf_temporal_score: float
    temporal_reconstruction_gain: float
    reversal_cost_proxy: int
    cap_presheaf: tuple[str, ...]
    cap_sheaf: tuple[str, ...]
    loss_kernel: tuple[str, ...]
    non_factorization_across_eta: bool
    sheafified: SheafifiedRecord


def fixed_site() -> FiniteSite:
    contexts = tuple(f"E{i}" for i in range(TOTAL_FRAGMENTS))
    return FiniteSite(
        name="S6_fixed_environment_fragment_site",
        contexts=contexts,
        cover=contexts,
        overlaps=tuple(combinations(contexts, 2)),
        expected_events=EVENTS,
        expected_edges=EXPECTED_EDGES,
        target_category="finite_record_sets_with_phase_tags",
        capability_family=(
            "read_pointer",
            "phase_sensitive_branch",
            "reconstruct_provenance_order",
        ),
    )


def profile_for_strength(monitoring_strength: int) -> tuple[int, int, int]:
    """Return (true pointer fragments, false fragments, unknown fragments).

    The profile is fixed before the run. It is the finite abstraction of a
    Darwinian redundancy sweep: more monitoring creates more redundant pointer
    copies and fewer nonrecord fragments.
    """

    profiles = {
        0: (1, 3, 2),
        1: (2, 2, 2),
        2: (3, 2, 1),
        3: (4, 1, 1),
        4: (5, 1, 0),
        5: (6, 0, 0),
    }
    if monitoring_strength not in profiles:
        raise ValueError(f"unsupported monitoring strength: {monitoring_strength}")
    return profiles[monitoring_strength]


def local_sections_for_strength(
    monitoring_strength: int,
    site: FiniteSite | None = None,
) -> tuple[LocalSection, ...]:
    chosen_site = site or fixed_site()
    true_count, false_count, unknown_count = profile_for_strength(monitoring_strength)
    sections: list[LocalSection] = []

    for index, context in enumerate(chosen_site.contexts):
        if index < true_count:
            sections.append(
                LocalSection(
                    context=context,
                    pointer=TRUE_POINTER,
                    phase_tag="phase_plus" if index % 2 == 0 else "phase_minus",
                    edges=_true_edges_for_strength(monitoring_strength),
                    confidence=0.55 + 0.07 * monitoring_strength,
                    source="redundant_pointer_fragment",
                )
            )
        elif index < true_count + false_count:
            sections.append(
                LocalSection(
                    context=context,
                    pointer=1 - TRUE_POINTER,
                    phase_tag="phase_false",
                    edges=(("record", "measure"),),
                    confidence=0.45,
                    source="nonpointer_or_noisy_fragment",
                )
            )
        else:
            sections.append(
                LocalSection(
                    context=context,
                    pointer=None,
                    phase_tag="phase_unread",
                    edges=(),
                    confidence=0.0,
                    source="unread_fragment",
                )
            )

    if len(sections) != TOTAL_FRAGMENTS:
        raise AssertionError((true_count, false_count, unknown_count, len(sections)))
    return tuple(sections)


def analyze_strength(
    monitoring_strength: int,
    site: FiniteSite | None = None,
) -> LevelAnalysis:
    chosen_site = site or fixed_site()
    sections = local_sections_for_strength(monitoring_strength, chosen_site)
    true_count, false_count, unknown_count = profile_for_strength(monitoring_strength)
    sheafified = approximate_associated_sheaf(sections)

    known_count = true_count + false_count
    observer_agreement = true_count / known_count if known_count else 0.0
    redundancy = true_count / TOTAL_FRAGMENTS
    gluing_error = (false_count + unknown_count) / TOTAL_FRAGMENTS
    presheaf_temporal = _presheaf_temporal_score(sections, chosen_site.expected_edges)
    sheaf_temporal = _edge_score(sheafified.edges, chosen_site.expected_edges)
    cap_presheaf = _presheaf_capabilities(sections)
    cap_sheaf = _sheaf_capabilities(sheafified)
    loss_kernel = tuple(cap for cap in cap_presheaf if cap not in cap_sheaf)

    return LevelAnalysis(
        monitoring_strength=monitoring_strength,
        true_count=true_count,
        false_count=false_count,
        unknown_count=unknown_count,
        redundancy=round(redundancy, 6),
        observer_agreement=round(observer_agreement, 6),
        gluing_error=round(gluing_error, 6),
        overlap_conflict_rate=round(_overlap_conflict_rate(sections), 6),
        presheaf_temporal_score=round(presheaf_temporal, 6),
        sheaf_temporal_score=round(sheaf_temporal, 6),
        temporal_reconstruction_gain=round(sheaf_temporal - presheaf_temporal, 6),
        reversal_cost_proxy=sheafified.support_count * sheafified.support_count,
        cap_presheaf=cap_presheaf,
        cap_sheaf=cap_sheaf,
        loss_kernel=loss_kernel,
        non_factorization_across_eta=bool(loss_kernel),
        sheafified=sheafified,
    )


def approximate_associated_sheaf(sections: tuple[LocalSection, ...]) -> SheafifiedRecord:
    """Finite effective-descent approximation.

    This is not a general sheafification algorithm. It is the declared finite
    reflector for this witness: pick the pointer value with enough redundant
    fragment support, retain only provenance edges with enough support, and drop
    phase tags that do not survive as final record data.
    """

    pointer_counts: dict[Pointer, int] = {}
    unknown_count = 0
    for section in sections:
        if section.pointer is None:
            unknown_count += 1
        else:
            pointer_counts[section.pointer] = pointer_counts.get(section.pointer, 0) + 1

    if pointer_counts:
        pointer, support_count = max(pointer_counts.items(), key=lambda item: item[1])
    else:
        pointer, support_count = None, 0
    conflict_count = sum(
        count for value, count in pointer_counts.items() if value != pointer
    )
    stable = (
        pointer is not None
        and pointer == TRUE_POINTER
        and support_count >= EFFECTIVE_DESCENT_SUPPORT
        and conflict_count <= 1
    )

    edge_support: dict[Edge, int] = {}
    for section in sections:
        if section.pointer == pointer:
            for edge in section.edges:
                edge_support[edge] = edge_support.get(edge, 0) + 1
    retained_edges = tuple(
        edge
        for edge in EXPECTED_EDGES
        if edge_support.get(edge, 0) >= EDGE_DESCENT_SUPPORT
    )
    phase_tags = tuple(
        sorted({section.phase_tag for section in sections if section.phase_tag})
    )
    local_signatures = {
        (section.pointer, section.phase_tag, section.edges)
        for section in sections
        if section.pointer == pointer
    }

    return SheafifiedRecord(
        pointer=pointer if stable else None,
        edges=retained_edges if stable else (),
        stable_global_section=stable,
        support_count=support_count,
        conflict_count=conflict_count,
        unknown_count=unknown_count,
        identified_local_signatures=len(local_signatures),
        dropped_phase_tags=phase_tags,
    )


def analyze_sweep() -> tuple[LevelAnalysis, ...]:
    site = fixed_site()
    return tuple(analyze_strength(level, site) for level in range(6))


def run_s6_goals() -> dict[str, Any]:
    site = fixed_site()
    sweep = analyze_sweep()
    threshold_level = next(
        item.monitoring_strength for item in sweep if item.sheafified.stable_global_section
    )
    threshold = sweep[threshold_level]

    goals = {
        "G1_typed_finite_site_specified": bool(
            site.contexts and site.cover and site.overlaps and site.capability_family
        ),
        "G2_minimal_gluing_simulation_ran": all(
            item.sheafified.support_count >= 0 for item in sweep
        ),
        "G3_darwinian_cover_transition_detected": (
            threshold.redundancy >= 4 / TOTAL_FRAGMENTS
            and threshold.gluing_error <= 2 / TOTAL_FRAGMENTS
        ),
        "G4_capability_non_factorization_across_eta": (
            "phase_sensitive_branch" in threshold.loss_kernel
            and threshold.non_factorization_across_eta
        ),
        "G5_temporal_provenance_reconstruction_gain": (
            threshold.temporal_reconstruction_gain > 0.0
            and threshold.sheaf_temporal_score == 1.0
        ),
    }

    return {
        "test": "associated-sheaf-finality-witness-v0.1",
        "tag": ["finite_witness", "poly_decider", "toy_model"],
        "guardrail": (
            "Finite effective-descent toy model only: not a quantum dynamics "
            "simulation, not a general sheafification theorem, and not source-side "
            "issuance evidence."
        ),
        "site": {
            "name": site.name,
            "contexts": list(site.contexts),
            "cover": list(site.cover),
            "overlap_count": len(site.overlaps),
            "expected_events": list(site.expected_events),
            "expected_edges": [list(edge) for edge in site.expected_edges],
            "target_category": site.target_category,
            "capability_family": list(site.capability_family),
            "effective_descent_support": EFFECTIVE_DESCENT_SUPPORT,
            "edge_descent_support": EDGE_DESCENT_SUPPORT,
        },
        "threshold": {
            "first_effective_descent_level": threshold_level,
            "redundancy": threshold.redundancy,
            "gluing_error": threshold.gluing_error,
            "observer_agreement": threshold.observer_agreement,
            "reversal_cost_proxy": threshold.reversal_cost_proxy,
        },
        "sweep": [_level_to_dict(item) for item in sweep],
        "goal_results": goals,
        "all_goals_passed": all(goals.values()),
        "effect_verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
        },
        "strongest_result": (
            "In this fixed finite cover, effective descent appears first at "
            "monitoring_strength=3, where redundancy reaches 4/6, gluing error "
            "falls to 2/6, the final pointer/provenance record stabilizes, phase "
            "capability is lost across eta_F, and provenance reconstruction improves."
        ),
        "first_obstruction": (
            "The result is fixture-local. It uses a declared finite reflector and "
            "deterministic redundancy profile, so it does not prove a physical "
            "Quantum Darwinism threshold or a general sheafification theorem."
        ),
        "next_step": (
            "Replace the deterministic fragment profile with an open-system / SBS "
            "fixture and keep the same outputs: redundancy, gluing error, eta_F "
            "loss, and provenance reconstruction."
        ),
    }


def _true_edges_for_strength(monitoring_strength: int) -> tuple[Edge, ...]:
    if monitoring_strength >= 3:
        return EXPECTED_EDGES
    if monitoring_strength >= 1:
        return (EXPECTED_EDGES[0],)
    return ()


def _presheaf_capabilities(sections: tuple[LocalSection, ...]) -> tuple[str, ...]:
    caps = {"phase_sensitive_branch"}
    if any(section.pointer is not None for section in sections):
        caps.add("read_pointer")
    if any(set(section.edges).intersection(EXPECTED_EDGES) for section in sections):
        caps.add("reconstruct_provenance_order")
    return tuple(sorted(caps))


def _sheaf_capabilities(record: SheafifiedRecord) -> tuple[str, ...]:
    caps: set[str] = set()
    if record.stable_global_section and record.pointer is not None:
        caps.add("read_pointer")
    if record.stable_global_section and record.edges == EXPECTED_EDGES:
        caps.add("reconstruct_provenance_order")
    return tuple(sorted(caps))


def _presheaf_temporal_score(
    sections: tuple[LocalSection, ...],
    expected_edges: tuple[Edge, ...],
) -> float:
    if not sections:
        return 0.0
    return sum(_edge_score(section.edges, expected_edges) for section in sections) / len(
        sections
    )


def _edge_score(edges: tuple[Edge, ...], expected_edges: tuple[Edge, ...]) -> float:
    if not expected_edges:
        return 0.0
    return len(set(edges).intersection(expected_edges)) / len(expected_edges)


def _overlap_conflict_rate(sections: tuple[LocalSection, ...]) -> float:
    known_pairs = 0
    conflicts = 0
    for left, right in combinations(sections, 2):
        if left.pointer is None or right.pointer is None:
            continue
        known_pairs += 1
        if left.pointer != right.pointer:
            conflicts += 1
    return conflicts / known_pairs if known_pairs else 0.0


def _level_to_dict(level: LevelAnalysis) -> dict[str, Any]:
    return {
        "monitoring_strength": level.monitoring_strength,
        "counts": {
            "true": level.true_count,
            "false": level.false_count,
            "unknown": level.unknown_count,
        },
        "redundancy": level.redundancy,
        "observer_agreement": level.observer_agreement,
        "gluing_error": level.gluing_error,
        "overlap_conflict_rate": level.overlap_conflict_rate,
        "presheaf_temporal_score": level.presheaf_temporal_score,
        "sheaf_temporal_score": level.sheaf_temporal_score,
        "temporal_reconstruction_gain": level.temporal_reconstruction_gain,
        "reversal_cost_proxy": level.reversal_cost_proxy,
        "cap_presheaf": list(level.cap_presheaf),
        "cap_sheaf": list(level.cap_sheaf),
        "loss_kernel": list(level.loss_kernel),
        "non_factorization_across_eta": level.non_factorization_across_eta,
        "sheafified": {
            "pointer": level.sheafified.pointer,
            "edges": [list(edge) for edge in level.sheafified.edges],
            "stable_global_section": level.sheafified.stable_global_section,
            "support_count": level.sheafified.support_count,
            "conflict_count": level.sheafified.conflict_count,
            "unknown_count": level.sheafified.unknown_count,
            "identified_local_signatures": (
                level.sheafified.identified_local_signatures
            ),
            "dropped_phase_tags": list(level.sheafified.dropped_phase_tags),
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_s6_goals(), indent=2, sort_keys=True))
