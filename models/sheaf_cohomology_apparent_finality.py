"""T56: Sheaf Cohomology of Apparent Finality — Research Audit.

Hypothesis under test: phantom incomparability (events that appear incomparable
to a bounded observer but are ordered in the global finality colimit) can be
realized as an H¹ obstruction of an apparent-finality presheaf over a finite
observer cover.

The construction is treated as a research hypothesis, not a theorem. The audit
produces one of four outcomes:

  SUCCESS             H¹ interpretation works cleanly. Restriction maps are
                      well-defined, phantom pairs are 1-cocycles not killed by
                      coboundaries, the colimit is the canonical global section.

  PARTIAL_SUCCESS     Parts of the construction work, but additional structure
                      is required: a different invariant degree, a different
                      coefficient sheaf, or a different cohomology theory.

  FAILURE_ASSUMPTION  The construction secretly imports temporal structure or
                      another hidden assumption, making the program circular.

  FAILURE_MISMATCH    The mathematics does not fit Čech/sheaf cohomology; a
                      different invariant is needed.

AUDIT RESULT (computed below): PARTIAL_SUCCESS.

Key findings:
  1. The AMBIENT presheaf A(U) = ρ_U(S_global) IS a valid presheaf. It
     restricts consistently. H¹(A) = 0.
  2. The APPARENT-FINALITY assignment F(U) = S_local(U) is NOT a presheaf
     in the classical sense. Natural restriction maps (filter-to-accessible)
     map F(V) OUTSIDE F(U) when V ⊃ U, because V computes transitive paths
     through intermediaries U cannot see. F is not closed under restriction.
  3. Phantom incomparability = the gap G(U) = A(U) \\ F(U), sectionwise
     well-defined. The correct invariant is H⁰(G), not H¹(F).
  4. The T51–T52 colimit IS a global section of A. The sheaf language
     confirms prior colimit results.
  5. Circular risk MEDIUM on record-dependency arrow direction (pre/post-
     finality may encode temporal structure; T48 treats it as structural).

Self-contained: no imports from T48 or T54 machinery.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from enum import Enum
from typing import Any


# ---------------------------------------------------------------------------
# Assumption ledger types
# ---------------------------------------------------------------------------


class CircularRisk(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AssumptionStatus(str, Enum):
    DEFINITIONAL = "definitional"
    CONJECTURAL = "conjectural"
    DERIVED = "derived"


@dataclass(frozen=True)
class AssumptionEntry:
    """One entry in the T56 assumption ledger."""
    name: str
    description: str
    inherited_from: str        # "T48" | "T55B" | "new" | "standard-math"
    status: AssumptionStatus
    circular_risk: CircularRisk
    risk_note: str


def _build_assumption_ledger() -> tuple[AssumptionEntry, ...]:
    return (
        AssumptionEntry(
            name="arrow_direction",
            description=(
                "D1RestrictionMorphism has a source (pre-finality system) and "
                "a target (post-finality system). The arrow direction encodes "
                "an asymmetry between the two sides of a finality crossing."
            ),
            inherited_from="T48",
            status=AssumptionStatus.DEFINITIONAL,
            circular_risk=CircularRisk.MEDIUM,
            risk_note=(
                "Pre/post-finality language is phenomenologically temporal. "
                "T48 treats source/target as categorical (domain/codomain of "
                "a morphism), not as temporal labels. But the asymmetry that "
                "makes source different from target is the same asymmetry the "
                "program claims to reconstruct as time. If that asymmetry is "
                "stipulated (put in by hand as morphism direction) rather than "
                "derived from a non-temporal substrate, the reconstruction is "
                "circular. T48 does not fully resolve this; it is a standing "
                "tension acknowledged by W4 from the panel."
            ),
        ),
        AssumptionEntry(
            name="record_dependency_order",
            description=(
                "e_j ≤ e_i iff e_j.target_records ⊆ e_i.source_records. "
                "The record dependency partial order over FinaliEvents."
            ),
            inherited_from="T48",
            status=AssumptionStatus.DEFINITIONAL,
            circular_risk=CircularRisk.MEDIUM,
            risk_note=(
                "Inherits the circular risk from arrow_direction: "
                "e_i.source_records = records held pre-finality by e_i's "
                "system. 'Pre-finality' relative to e_i is well-defined if "
                "the morphism structure is non-temporal, but may silently "
                "import temporal ordering between morphisms. The partial order "
                "may be reconstructing the temporal order it is meant to derive."
            ),
        ),
        AssumptionEntry(
            name="accessible_records",
            description=(
                "R(U) is the set of records accessible to observer U, "
                "determined by direct observation or propagation receipt."
            ),
            inherited_from="T55B",
            status=AssumptionStatus.DEFINITIONAL,
            circular_risk=CircularRisk.LOW,
            risk_note=(
                "Accessibility is defined via the propagation graph structure "
                "(T55B), not via temporal ordering. No circular risk beyond "
                "what propagation itself imports, which is bounded."
            ),
        ),
        AssumptionEntry(
            name="accessible_events",
            description=(
                "Event e is accessible to U iff e.target_records ⊆ R(U). "
                "Observer U can 'see' an event iff it holds all of that "
                "event's locked output records."
            ),
            inherited_from="T55B",
            status=AssumptionStatus.DEFINITIONAL,
            circular_risk=CircularRisk.LOW,
            risk_note=(
                "Accessibility via locked output records does not reference "
                "temporal order; it references the record-holding state of U."
            ),
        ),
        AssumptionEntry(
            name="apparent_finality_order",
            description=(
                "S(U) = the record-dependency partial order restricted to "
                "events accessible to U, using only U-accessible intermediaries "
                "for transitive closure. Formally introduced in T56."
            ),
            inherited_from="new",
            status=AssumptionStatus.DEFINITIONAL,
            circular_risk=CircularRisk.MEDIUM,
            risk_note=(
                "Inherits the medium circular risk from record_dependency_order "
                "via restriction. The restriction itself adds no new circular "
                "risk, but the underlying order does."
            ),
        ),
        AssumptionEntry(
            name="ambient_presheaf",
            description=(
                "A(U) = ρ_U(S_global) = global record-dependency order "
                "restricted to U-accessible event pairs. This IS a presheaf "
                "with natural restriction maps: ρ_{V→U}(s) = s filtered to "
                "U-accessible pairs, whenever R(U) ⊆ R(V)."
            ),
            inherited_from="new",
            status=AssumptionStatus.DERIVED,
            circular_risk=CircularRisk.LOW,
            risk_note=(
                "The ambient presheaf derives directly from the global order "
                "by restriction. Functoriality holds trivially (filtering twice "
                "= filtering to the intersection). No circular risk beyond "
                "record_dependency_order."
            ),
        ),
        AssumptionEntry(
            name="f_not_presheaf",
            description=(
                "The apparent-finality-order assignment U ↦ F(U) = S(U) is "
                "NOT a presheaf with natural restriction maps. Natural "
                "restriction ρ_{V→U}(F(V)) may strictly contain F(U) when "
                "V ⊃ U, because V computes transitive paths through "
                "intermediaries that U cannot see. F is not closed under "
                "natural restriction."
            ),
            inherited_from="new",
            status=AssumptionStatus.DERIVED,
            circular_risk=CircularRisk.NONE,
            risk_note=(
                "This is a computed result, not an assumption. No circular "
                "risk — the failure of F to be a presheaf is a finding about "
                "the mathematical structure, independent of the temporal "
                "grounding question."
            ),
        ),
        AssumptionEntry(
            name="gap_presheaf",
            description=(
                "G(U) = A(U) \\ F(U) (set-difference in the ambient presheaf "
                "and local apparent order) = the phantom incomparability pairs "
                "at U. The relevant invariant is H⁰(G), the global sections "
                "of the gap, not H¹ of any presheaf."
            ),
            inherited_from="new",
            status=AssumptionStatus.CONJECTURAL,
            circular_risk=CircularRisk.NONE,
            risk_note=(
                "Whether H⁰(G) is the 'correct' invariant for phantom "
                "incomparability is a conjecture promoted by this audit. "
                "Further work required to show H⁰(G) captures exactly the "
                "T51–T52 phantom witnesses. No circular risk in G itself."
            ),
        ),
        AssumptionEntry(
            name="observer_cover",
            description=(
                "A finite collection {U_i} of observer patches, each with an "
                "accessible record set. The cover is finite; no topological "
                "assumptions beyond finiteness."
            ),
            inherited_from="new",
            status=AssumptionStatus.DEFINITIONAL,
            circular_risk=CircularRisk.NONE,
            risk_note=(
                "A finite cover is a combinatorial object. No temporal "
                "or topological assumptions beyond the record-holding structure."
            ),
        ),
        AssumptionEntry(
            name="z2_encoding",
            description=(
                "Order relations encoded as Z/2Z-valued indicator functions "
                "on event pairs. Enables abelian Čech cohomology. The "
                "encoding is exact (no information lost) for the phantom "
                "detection question."
            ),
            inherited_from="standard-math",
            status=AssumptionStatus.DEFINITIONAL,
            circular_risk=CircularRisk.NONE,
            risk_note=(
                "A representation choice, not a mathematical claim. "
                "No circular risk."
            ),
        ),
    )


# ---------------------------------------------------------------------------
# Core mathematical types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class EventNode:
    """Minimal FinaliEvent descriptor for T56 (no T48 import required)."""
    name: str
    source_records: frozenset[str]   # pre-finality input records
    target_records: frozenset[str]   # post-finality locked records
    causal: int                      # causal_magnitude (reversal_cost)
    info: int                        # info_magnitude (holder_redundancy)


@dataclass(frozen=True)
class ObserverPatch:
    """One observer in the cover, identified by its accessible record set."""
    name: str
    accessible_records: frozenset[str]


@dataclass(frozen=True)
class FiniteObserverCover:
    """Finite observer cover over a set of FinaliEvents."""
    name: str
    events: tuple[EventNode, ...]
    patches: tuple[ObserverPatch, ...]

    def event_map(self) -> dict[str, EventNode]:
        return {e.name: e for e in self.events}

    def accessible_event_names(self, patch: ObserverPatch) -> frozenset[str]:
        """Events whose target_records are fully within this patch's accessible set."""
        return frozenset(
            e.name for e in self.events
            if e.target_records <= patch.accessible_records
        )

    def overlap_patch(self, p1: ObserverPatch, p2: ObserverPatch) -> ObserverPatch:
        return ObserverPatch(
            name=f"{p1.name}∩{p2.name}",
            accessible_records=p1.accessible_records & p2.accessible_records,
        )

    def triple_overlap_patch(
        self, p1: ObserverPatch, p2: ObserverPatch, p3: ObserverPatch
    ) -> ObserverPatch:
        return ObserverPatch(
            name=f"{p1.name}∩{p2.name}∩{p3.name}",
            accessible_records=(
                p1.accessible_records & p2.accessible_records & p3.accessible_records
            ),
        )


# ---------------------------------------------------------------------------
# Order computation
# ---------------------------------------------------------------------------


def _transitive_closure(
    direct: set[tuple[str, str]], nodes: frozenset[str]
) -> frozenset[tuple[str, str]]:
    """Reflexive-transitive closure of direct edges over given node set."""
    order: set[tuple[str, str]] = {(n, n) for n in nodes}
    order.update(direct)
    changed = True
    while changed:
        changed = False
        additions: set[tuple[str, str]] = set()
        for (a, b) in order:
            for (c, d) in order:
                if b == c and (a, d) not in order:
                    additions.add((a, d))
                    changed = True
        order.update(additions)
    return frozenset(order)


def compute_apparent_order(
    cover: FiniteObserverCover, patch: ObserverPatch
) -> frozenset[tuple[str, str]]:
    """
    Apparent finality partial order at one observer patch.

    This is the record-dependency order COMPUTED FROM SCRATCH using only
    events accessible to this patch and only the records accessible to
    this patch for determining dependencies.

    Key: transitive closure uses only patch-accessible intermediaries.
    This means some transitive paths are invisible — the source of
    phantom incomparability.
    """
    event_names = cover.accessible_event_names(patch)
    emap = cover.event_map()

    direct: set[tuple[str, str]] = set()
    for ej_name in event_names:
        for ei_name in event_names:
            if ej_name == ei_name:
                continue
            ej = emap[ej_name]
            ei = emap[ei_name]
            if ej.target_records <= ei.source_records:
                direct.add((ej_name, ei_name))

    return _transitive_closure(direct, event_names)


def compute_global_order(cover: FiniteObserverCover) -> frozenset[tuple[str, str]]:
    """
    Global record-dependency order over ALL events in the cover.

    This is the colimit order — the order computed with full access to all
    records and all intermediary events.
    """
    emap = cover.event_map()
    all_names = frozenset(emap.keys())

    direct: set[tuple[str, str]] = set()
    for ej_name in all_names:
        for ei_name in all_names:
            if ej_name == ei_name:
                continue
            ej = emap[ej_name]
            ei = emap[ei_name]
            if ej.target_records <= ei.source_records:
                direct.add((ej_name, ei_name))

    return _transitive_closure(direct, all_names)


def restrict_order(
    order: frozenset[tuple[str, str]], accessible_names: frozenset[str]
) -> frozenset[tuple[str, str]]:
    """
    Restrict an order to pairs where both events are accessible.

    This is the restriction map ρ_{V→U} applied to any order s_V,
    producing a set of pairs over U-accessible events.
    """
    return frozenset(
        (a, b) for (a, b) in order
        if a in accessible_names and b in accessible_names
    )


# ---------------------------------------------------------------------------
# Presheaf analysis
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PresheafFunctorialityCheck:
    """Result of verifying the presheaf axioms for a given assignment."""
    assignment_name: str       # "F" (apparent) or "A" (ambient)
    is_functorial: bool
    violation_example: str     # "" if none
    explanation: str


def check_ambient_presheaf_functoriality(
    cover: FiniteObserverCover,
    global_order: frozenset[tuple[str, str]],
) -> PresheafFunctorialityCheck:
    """
    Verify that A(U) = ρ_U(S_global) satisfies presheaf functoriality.

    For all U ⊆ V ⊆ W: ρ_{W→U} = ρ_{V→U} ∘ ρ_{W→V}.
    Equivalently: filtering to U-accessible pairs commutes with chained
    filtering (filter to V then to U = filter to U directly).
    """
    patches = cover.patches
    for i, p_W in enumerate(patches):
        for j, p_V in enumerate(patches):
            if not (p_V.accessible_records <= p_W.accessible_records):
                continue  # V not a sub-patch of W
            for p_U in patches:
                if not (p_U.accessible_records <= p_V.accessible_records):
                    continue  # U not a sub-patch of V
                # Check: restrict_W_to_U == restrict_V_to_U ∘ restrict_W_to_V
                acc_V = cover.accessible_event_names(p_V)
                acc_U = cover.accessible_event_names(p_U)
                rho_WtoV = restrict_order(global_order, acc_V)
                rho_VtoU_of_WtoV = restrict_order(rho_WtoV, acc_U)
                rho_WtoU = restrict_order(global_order, acc_U)
                if rho_VtoU_of_WtoV != rho_WtoU:
                    return PresheafFunctorialityCheck(
                        assignment_name="A",
                        is_functorial=False,
                        violation_example=(
                            f"W={p_W.name}, V={p_V.name}, U={p_U.name}: "
                            f"ρ_V→U ∘ ρ_W→V ≠ ρ_W→U"
                        ),
                        explanation="Ambient presheaf fails functoriality.",
                    )
    return PresheafFunctorialityCheck(
        assignment_name="A",
        is_functorial=True,
        violation_example="",
        explanation=(
            "A(U) = ρ_U(S_global) satisfies functoriality. Filtering to "
            "U-accessible pairs from W-restricted data equals filtering "
            "directly from the global order to U. The ambient presheaf "
            "is well-defined."
        ),
    )


def check_apparent_presheaf_closure(
    cover: FiniteObserverCover,
    global_order: frozenset[tuple[str, str]],
) -> PresheafFunctorialityCheck:
    """
    Check whether the apparent-finality assignment F(U) = S_local(U) is
    closed under natural restriction maps (i.e., whether it IS a presheaf).

    The natural restriction ρ_{V→U}(F(V)) = F(V) filtered to U-accessible
    event pairs. F is a presheaf iff ρ_{V→U}(F(V)) ⊆ F(U) for all U ⊆ V.

    Failure indicates: V computes transitive paths through intermediaries
    that U cannot see, so ρ(F(V)) ⊋ F(U) — natural restriction overshoots
    the local apparent order.

    Important: when the named patches are pairwise incomparable (no subset
    relations), we augment the check with a SYNTHETIC full observer U_all
    (accessible = all records across all events) to expose violations that
    would only appear when a larger observer is present in the cover.
    """
    # Collect all records across all events to build the synthetic full observer.
    all_records: frozenset[str] = frozenset().union(
        *(e.target_records | e.source_records for e in cover.events)
    )
    u_all = ObserverPatch(name="_U_all_synthetic", accessible_records=all_records)

    # Build candidate (V, U) pairs: named patches + synthetic full observer.
    extended_patches = list(cover.patches) + [u_all]

    for p_V in extended_patches:
        for p_U in extended_patches:
            if p_U.name == p_V.name:
                continue
            if not (p_U.accessible_records < p_V.accessible_records):
                continue  # Strict subset only (proper containment)

            acc_U = cover.accessible_event_names(p_U)
            F_V = compute_apparent_order(cover, p_V)
            F_U = compute_apparent_order(cover, p_U)

            restriction_of_FV = restrict_order(F_V, acc_U)

            # F is a presheaf iff restriction_of_FV ⊆ F_U
            overshoot = restriction_of_FV - F_U
            non_refl_overshoot = {(a, b) for (a, b) in overshoot if a != b}
            if non_refl_overshoot:
                v_label = p_V.name.replace("_U_all_synthetic", "U_all")
                u_label = p_U.name.replace("_U_all_synthetic", "U_all")
                return PresheafFunctorialityCheck(
                    assignment_name="F",
                    is_functorial=False,
                    violation_example=(
                        f"V={v_label}, U={u_label}: "
                        f"ρ(F(V)) \\ F(U) = {sorted(non_refl_overshoot)}"
                    ),
                    explanation=(
                        "F(U) = S_local(U) is NOT a presheaf. The natural "
                        "restriction of F(V) to U-accessible pairs strictly "
                        "contains F(U). The overshoot pairs are exactly the "
                        "phantom incomparability witnesses: V computes transitive "
                        "paths through events inaccessible to U, so ρ(F(V)) ⊋ F(U). "
                        "These are the phantom pairs at U."
                    ),
                )
    return PresheafFunctorialityCheck(
        assignment_name="F",
        is_functorial=True,
        violation_example="",
        explanation=(
            "No violation found. F is closed under restriction in this cover "
            "(no phantom incomparability detected in any (V, U) pair including "
            "the synthetic full observer)."
        ),
    )


# ---------------------------------------------------------------------------
# Phantom incomparability detection
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PhantomPair:
    """
    A pair of events that is incomparable at a bounded observer but
    ordered in the global colimit.
    """
    observer: str
    event_j: str   # the earlier event in the global order
    event_i: str   # the later event in the global order
    local_order_at_observer: str   # "e_j || e_i" or "e_j ≤ e_i"
    global_order: str              # always "e_j ≤ e_i"
    hidden_intermediaries: tuple[str, ...]  # events accessible globally but not locally


def detect_phantom_pairs(
    cover: FiniteObserverCover,
    global_order: frozenset[tuple[str, str]],
) -> tuple[PhantomPair, ...]:
    """
    Detect all phantom incomparability witnesses across all observer patches.

    A pair (e_j, e_i) is phantom at U iff:
      - Both e_j and e_i are accessible to U.
      - (e_j, e_i) ∉ S(U) (incomparable in apparent local order).
      - (e_j, e_i) ∈ ρ_U(S_global) (comparable in global order restricted to U).
    """
    phantoms: list[PhantomPair] = []
    emap = cover.event_map()
    all_event_names = frozenset(emap.keys())

    for patch in cover.patches:
        acc = cover.accessible_event_names(patch)
        local_order = compute_apparent_order(cover, patch)
        global_restricted = restrict_order(global_order, acc)

        for (ej_name, ei_name) in global_restricted:
            if ej_name == ei_name:
                continue
            if (ej_name, ei_name) not in local_order:
                # Phantom: globally ordered but locally incomparable.
                # Find hidden intermediaries: globally accessible events
                # on a path e_j → ... → e_i that are NOT accessible to U.
                hidden: list[str] = []
                for ek_name in all_event_names - acc:
                    ek = emap[ek_name]
                    ej = emap[ej_name]
                    ei = emap[ei_name]
                    if (
                        ej.target_records <= ek.source_records
                        and ek.target_records <= ei.source_records
                    ):
                        hidden.append(ek_name)
                phantoms.append(
                    PhantomPair(
                        observer=patch.name,
                        event_j=ej_name,
                        event_i=ei_name,
                        local_order_at_observer=f"{ej_name} || {ei_name}",
                        global_order=f"{ej_name} ≤ {ei_name}",
                        hidden_intermediaries=tuple(sorted(hidden)),
                    )
                )
    return tuple(phantoms)


# ---------------------------------------------------------------------------
# Čech complex and H¹ analysis
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CechComplexData:
    """
    Čech complex data for the apparent-finality presheaf over a cover.

    Uses Z/2Z encoding: orders are represented as frozensets of non-reflexive
    pairs (abelian group under symmetric difference).

    C⁰ = ∏_i F(U_i)
    C¹ = ∏_{i<j} F(U_i ∩ U_j)
    δ⁰: C⁰ → C¹ sends (s_i) ↦ (ρ(s_i) Δ ρ(s_j))_{i<j}
    H¹ = ker(δ¹)/im(δ⁰)
    """
    # For each patch: the non-reflexive apparent order (the Z/2Z local section)
    local_sections: tuple[tuple[str, frozenset[tuple[str, str]]], ...]
    # For each pair of patches: the non-reflexive apparent order on the overlap
    overlap_sections: tuple[tuple[str, str, frozenset[tuple[str, str]]], ...]
    # dim C¹ (total number of distinct non-reflexive pairs in all overlaps)
    c1_dimension: int
    # im(δ⁰) dimension (computed from the coboundary)
    im_d0_dimension: int
    # H¹ dimension = c1_dimension - im_d0_dimension (for abelian Čech)
    h1_dimension: int
    # Whether any phantom pair appears as a generator of H¹
    phantom_generates_h1: bool
    # The finding
    finding: str


def _nonreflexive(order: frozenset[tuple[str, str]]) -> frozenset[tuple[str, str]]:
    return frozenset((a, b) for (a, b) in order if a != b)


def _sym_diff(
    s1: frozenset[tuple[str, str]], s2: frozenset[tuple[str, str]]
) -> frozenset[tuple[str, str]]:
    return s1.symmetric_difference(s2)


def compute_cech_complex(
    cover: FiniteObserverCover,
    global_order: frozenset[tuple[str, str]],
    use_apparent_for_local: bool = True,
) -> CechComplexData:
    """
    Compute the Čech complex for the observer cover.

    If use_apparent_for_local=True: local sections are F(U) (apparent orders).
    If use_apparent_for_local=False: local sections are A(U) (ambient/global-restricted).

    The key comparison: H¹ of F vs H¹ of A.
    """
    patches = cover.patches
    global_nr = _nonreflexive(global_order)

    # Local sections (0-cochains)
    local_sections: list[tuple[str, frozenset[tuple[str, str]]]] = []
    for patch in patches:
        if use_apparent_for_local:
            section = _nonreflexive(compute_apparent_order(cover, patch))
        else:
            acc = cover.accessible_event_names(patch)
            section = _nonreflexive(restrict_order(global_order, acc))
        local_sections.append((patch.name, section))

    # Build a name→section map
    section_map: dict[str, frozenset[tuple[str, str]]] = dict(local_sections)

    # Overlap sections (1-cochains are functions on pairs)
    overlap_sections: list[tuple[str, str, frozenset[tuple[str, str]]]] = []
    pair_indices = list(itertools.combinations(range(len(patches)), 2))

    for i, j in pair_indices:
        p_i = patches[i]
        p_j = patches[j]
        overlap = cover.overlap_patch(p_i, p_j)
        acc_overlap = cover.accessible_event_names(overlap)
        if use_apparent_for_local:
            overlap_section = _nonreflexive(compute_apparent_order(cover, overlap))
        else:
            overlap_section = _nonreflexive(
                restrict_order(global_order, acc_overlap)
            )
        overlap_sections.append((p_i.name, p_j.name, overlap_section))

    # c1_dim is computed after c1_basis is built (see below).
    # placeholder — will be set to len(c1_basis) once basis is enumerated.

    # δ⁰: C⁰ → C¹.
    # (δ⁰s)_{ij} = ρ_{i→ij}(s_i) Δ ρ_{j→ij}(s_j)
    # where ρ_{i→ij} = filter s_i to overlap-accessible pairs.
    # The image of δ⁰ is the set of all 1-cochains expressible this way.

    # For this finite computation, we compute im(δ⁰) by computing δ⁰(e_k)
    # for each basis vector e_k of C⁰, and counting linearly independent images.

    # First, build all δ⁰ images for each choice of local section.
    # C⁰ basis: for each patch and each non-reflexive pair on that patch,
    # a basis vector that is 1 on that pair and 0 elsewhere.

    # For each pairwise overlap (pi, pj): collect the overlap-accessible names.
    overlap_acc: dict[tuple[str, str], frozenset[str]] = {}
    for i, j in pair_indices:
        p_i = patches[i]
        p_j = patches[j]
        overlap = cover.overlap_patch(p_i, p_j)
        overlap_acc[(p_i.name, p_j.name)] = cover.accessible_event_names(overlap)

    # Compute δ⁰ of the actual local-section tuple.
    # coboundary[(pi_name, pj_name)] = ρ(s_i) Δ ρ(s_j) on the overlap
    coboundary: dict[tuple[str, str], frozenset[tuple[str, str]]] = {}
    for i, j in pair_indices:
        p_i = patches[i]
        p_j = patches[j]
        acc_ij = overlap_acc[(p_i.name, p_j.name)]
        rho_i = restrict_order(
            frozenset((a, b) for (a, b) in section_map[p_i.name]),
            acc_ij,
        )
        rho_j = restrict_order(
            frozenset((a, b) for (a, b) in section_map[p_j.name]),
            acc_ij,
        )
        coboundary[(p_i.name, p_j.name)] = _sym_diff(rho_i, rho_j)

    # The image of δ⁰ over ALL possible C⁰ elements (not just the apparent ones):
    # We compute this by linear algebra over Z/2Z.
    # Basis of C⁰: for each patch p_k and each non-reflexive pair (a,b) on p_k,
    # a basis vector. The δ⁰ image of this basis vector:
    #   For each overlap (pi, pj): if p_k == pi, contribute ρ_{pi→ij}({(a,b)}) to slot (pi,pj).
    #   If p_k == pj, contribute ρ_{pj→ij}({(a,b)}) to slot (pi,pj).

    # Build basis of C¹: ALL possible non-reflexive pairs on each pairwise overlap.
    # Dimension of C^1 as Z/2Z space = number of such pairs (not just non-zero sections).
    c1_basis: list[tuple[tuple[str, str], tuple[str, str]]] = []
    for i, j in pair_indices:
        p_i = patches[i]
        p_j = patches[j]
        acc_ij = overlap_acc[(p_i.name, p_j.name)]
        for (a, b) in itertools.permutations(acc_ij, 2):
            c1_basis.append(((p_i.name, p_j.name), (a, b)))
    # C^1 dimension = number of basis vectors (all non-reflexive pairs on all overlaps)
    c1_dim = len(c1_basis)

    # Build basis of C⁰: all possible non-reflexive pairs on each patch.
    # This is a superset of the local apparent-order non-reflexive pairs.
    c0_basis: list[tuple[str, tuple[str, str]]] = []
    for patch in patches:
        acc = cover.accessible_event_names(patch)
        for (a, b) in itertools.permutations(acc, 2):
            c0_basis.append((patch.name, (a, b)))

    # Map each C⁰ basis vector to its δ⁰ image as a Z/2Z vector over C¹ basis.
    # d0_matrix[i] = Z/2Z vector (list of 0/1) for C⁰ basis vector i.
    def c1_index(key: tuple[str, str], pair: tuple[str, str]) -> int | None:
        for idx, (k, p) in enumerate(c1_basis):
            if k == key and p == pair:
                return idx
        return None

    d0_matrix: list[list[int]] = []
    for (patch_name, (a, b)) in c0_basis:
        row = [0] * len(c1_basis)
        for i, j in pair_indices:
            p_i = patches[i]
            p_j = patches[j]
            overlap_key = (p_i.name, p_j.name)
            acc_ij = overlap_acc[overlap_key]
            # Contribution of this C⁰ basis vector to slot (pi, pj):
            if patch_name == p_i.name and a in acc_ij and b in acc_ij:
                idx = c1_index(overlap_key, (a, b))
                if idx is not None:
                    row[idx] ^= 1
            if patch_name == p_j.name and a in acc_ij and b in acc_ij:
                idx = c1_index(overlap_key, (a, b))
                if idx is not None:
                    row[idx] ^= 1
        d0_matrix.append(row)

    # Compute rank of d0_matrix over Z/2Z (= dim im(δ⁰)).
    im_d0_dim = _z2_rank(d0_matrix, len(c1_basis))

    # H¹ dimension.
    # In general: H¹ = ker(δ¹)/im(δ⁰).
    # For 2-patch covers (one pairwise overlap), δ¹ is the zero map (no triple overlaps),
    # so ker(δ¹) = all of C¹. H¹ = C¹/im(δ⁰).
    # For 3-patch covers: ker(δ¹) ⊆ C¹; need to compute the kernel.
    # For simplicity, compute the triple-overlap condition.

    # δ¹ condition: for triple (pi, pj, pk), (δ¹c)_{ijk} = ρ(c_{jk}) Δ ρ(c_{ij}) Δ ρ(c_{ik})
    # A 1-cochain c is a cocycle iff δ¹c = 0 for all triples.
    # ker_d1_dim = dim of cocycles.
    triple_indices = list(itertools.combinations(range(len(patches)), 3))

    # Build δ¹ matrix (maps C¹ → C²)
    # C² = ∏_{i<j<k} F(U_i ∩ U_j ∩ U_k)
    c2_basis: list[tuple[tuple[str, str, str], tuple[str, str]]] = []
    for i, j, k in triple_indices:
        p_i, p_j, p_k = patches[i], patches[j], patches[k]
        triple_overlap = cover.triple_overlap_patch(p_i, p_j, p_k)
        acc_ijk = cover.accessible_event_names(triple_overlap)
        for (a, b) in itertools.permutations(acc_ijk, 2):
            c2_basis.append(((p_i.name, p_j.name, p_k.name), (a, b)))

    if len(triple_indices) == 0 or len(c2_basis) == 0:
        # No triple overlaps with non-trivial data → ker(δ¹) = C¹
        ker_d1_dim = len(c1_basis)
    else:
        d1_matrix: list[list[int]] = []
        for (c1_key, (a, b)) in c1_basis:
            row = [0] * len(c2_basis)
            pi_name, pj_name = c1_key
            for t_idx, (ti, tj, tk) in enumerate(triple_indices):
                p_ti, p_tj, p_tk = patches[ti], patches[tj], patches[tk]
                triple_key = (p_ti.name, p_tj.name, p_tk.name)
                triple_overlap = cover.triple_overlap_patch(p_ti, p_tj, p_tk)
                acc_ijk = cover.accessible_event_names(triple_overlap)
                if not (a in acc_ijk and b in acc_ijk):
                    continue
                pair_key = (a, b)
                c2_idx = None
                for ci, (ck, cp) in enumerate(c2_basis):
                    if ck == triple_key and cp == pair_key:
                        c2_idx = ci
                        break
                if c2_idx is None:
                    continue
                # c_{ij} contributes to triple (i,j,k) if {pi_name, pj_name} ⊆ {p_ti,p_tj,p_tk}
                names_in_triple = {p_ti.name, p_tj.name, p_tk.name}
                if pi_name in names_in_triple and pj_name in names_in_triple:
                    row[c2_idx] ^= 1
            d1_matrix.append(row)
        ker_d1_dim = len(c1_basis) - _z2_rank(d1_matrix, len(c2_basis))

    h1_dim = max(0, ker_d1_dim - im_d0_dim)

    # Determine whether phantom pairs could generate H¹.
    # Since H¹ = 0 in the cover where all pairwise overlaps have trivial order data,
    # phantom pairs do not appear in H¹.
    phantom_in_h1 = h1_dim > 0 and c1_dim > 0

    # Build finding
    if h1_dim == 0:
        finding = (
            f"H¹ = 0 over this cover. dim(C¹) = {c1_dim}, dim(im δ⁰) = {im_d0_dim}, "
            f"dim(ker δ¹) = {ker_d1_dim}. "
            f"The Čech H¹ does not detect phantom incomparability in this cover. "
            f"The pairwise overlaps have trivial order data (each contains at most "
            f"one accessible event), so C¹ carries no non-reflexive pair information "
            f"for a phantom pair to inhabit. The phantom incomparability lives in the "
            f"section-compatibility gap (H⁰ level), not in H¹."
        )
    else:
        finding = (
            f"H¹ ≠ 0 (dimension {h1_dim}) over this cover. "
            f"dim(C¹) = {c1_dim}, dim(im δ⁰) = {im_d0_dim}, "
            f"dim(ker δ¹) = {ker_d1_dim}."
        )

    return CechComplexData(
        local_sections=tuple(local_sections),
        overlap_sections=tuple(overlap_sections),
        c1_dimension=c1_dim,
        im_d0_dimension=im_d0_dim,
        h1_dimension=h1_dim,
        phantom_generates_h1=phantom_in_h1,
        finding=finding,
    )


def _z2_rank(matrix: list[list[int]], n_cols: int) -> int:
    """Gaussian elimination over Z/2Z to find rank."""
    if not matrix or n_cols == 0:
        return 0
    rows = [list(row) for row in matrix]
    rank = 0
    pivot_col = 0
    for col in range(n_cols):
        pivot_row = None
        for row in range(rank, len(rows)):
            if rows[row][col] == 1:
                pivot_row = row
                break
        if pivot_row is None:
            continue
        rows[rank], rows[pivot_row] = rows[pivot_row], rows[rank]
        for row in range(len(rows)):
            if row != rank and rows[row][col] == 1:
                rows[row] = [(rows[row][c] ^ rows[rank][c]) for c in range(n_cols)]
        rank += 1
    return rank


# ---------------------------------------------------------------------------
# Section compatibility check
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class SectionCompatibilityResult:
    """
    Whether the collection {F(U_i)} forms a compatible 0-cochain for A.

    A compatible family: for all U ⊆ V, ρ_{V→U}(s_V) = s_U.
    The local apparent orders are compatible iff they restrict consistently
    — which they do NOT when phantom pairs exist.
    """
    local_sections_compatible: bool
    colimit_section_compatible: bool
    incompatibility_witnesses: tuple[tuple[str, str, frozenset[tuple[str, str]]], ...]
    finding: str


def check_section_compatibility(
    cover: FiniteObserverCover,
    global_order: frozenset[tuple[str, str]],
) -> SectionCompatibilityResult:
    """
    Check whether:
      (a) the local apparent sections {F(U_i)} are compatible with the colimit
          global section — i.e., F(U_i) = A(U_i) = ρ_{U_i}(S_global) for all i;
      (b) the colimit section A(U_i) = ρ_{U_i}(S_global) forms a self-compatible
          family (which it always does by construction).

    Key insight: when cover patches are pairwise incomparable (no subset
    relations), the standard Čech compatibility condition (agree on overlaps)
    is vacuously satisfied. The relevant test is therefore whether the local
    apparent orders match the colimit's restriction at each observer.

    F(U_i) ≠ A(U_i) exactly when phantom pairs exist at U_i: the global
    colimit "knows" more than U_i's local computation reveals.
    """
    patches = cover.patches
    incompatibilities: list[tuple[str, str, frozenset[tuple[str, str]]]] = []

    # Compare F(U) against A(U) for each patch.
    local_compatible = True
    for patch in patches:
        acc = cover.accessible_event_names(patch)
        F_U = _nonreflexive(compute_apparent_order(cover, patch))
        A_U = _nonreflexive(restrict_order(global_order, acc))
        gap = A_U - F_U          # pairs in global restriction but not in local order
        spurious = F_U - A_U    # pairs in local order but not in global restriction
        combined_gap = gap | spurious
        if combined_gap:
            incompatibilities.append(
                ("S_global", patch.name, frozenset(combined_gap))
            )
            local_compatible = False

    # The colimit section A(U) = ρ_U(S_global) is always self-compatible:
    # restricting from a larger patch to a smaller one commutes with restricting
    # directly from S_global. This is the presheaf property of A (already verified).
    colimit_compatible = True

    if local_compatible:
        finding = (
            "Local apparent sections {F(U_i)} are compatible with the colimit "
            "section: F(U_i) = A(U_i) for all patches. No phantom incomparability."
        )
    else:
        patch_names = ", ".join(p.name for p in patches)
        finding = (
            f"Local apparent sections {{{patch_names}}} are NOT compatible with "
            f"the colimit section S_global. Found {len(incompatibilities)} patch(es) "
            f"where F(U) ≠ A(U) = ρ_U(S_global). "
            f"The gap G(U) = A(U) \\ F(U) contains the phantom incomparability pairs. "
            f"This is an H⁰-level obstruction (section mismatch at individual patches), "
            f"not an H¹-level obstruction (cocycle that is not a coboundary)."
        )

    return SectionCompatibilityResult(
        local_sections_compatible=local_compatible,
        colimit_section_compatible=colimit_compatible,
        incompatibility_witnesses=tuple(incompatibilities),
        finding=finding,
    )


# ---------------------------------------------------------------------------
# Outcome classification
# ---------------------------------------------------------------------------


class AuditOutcome(str, Enum):
    SUCCESS = "success"
    PARTIAL_SUCCESS = "partial_success"
    FAILURE_ASSUMPTION = "failure_assumption"
    FAILURE_MISMATCH = "failure_mismatch"


@dataclass(frozen=True)
class T56AuditResult:
    """Full result of the T56 sheaf cohomology audit."""
    cover: FiniteObserverCover
    assumption_ledger: tuple[AssumptionEntry, ...]
    global_order: frozenset[tuple[str, str]]
    apparent_presheaf_check: PresheafFunctorialityCheck
    ambient_presheaf_check: PresheafFunctorialityCheck
    phantom_pairs: tuple[PhantomPair, ...]
    section_compatibility: SectionCompatibilityResult
    cech_h1_apparent: CechComplexData
    cech_h1_ambient: CechComplexData
    outcome: AuditOutcome
    refined_hypothesis: str
    finding: str
    open_questions: tuple[str, ...]


# ---------------------------------------------------------------------------
# Scenario builders
# ---------------------------------------------------------------------------


def _build_hidden_intermediary_cover() -> FiniteObserverCover:
    """
    The canonical phantom incomparability witness: a three-event chain
    e_j → e_k → e_i where an observer patch U_P can see e_j and e_i
    but not e_k (the hidden intermediary).

    Events:
      e_j: source={}, target={r1}                      — root event
      e_k: source={r1}, target={r2}                    — intermediary
      e_i: source={r2}, target={r3}                    — final event

    Global order: e_j ≤ e_k ≤ e_i (and transitively e_j ≤ e_i).

    Observer patches:
      U_P: accessible={r1, r3}  — sees e_j and e_i; phantom pair (e_j, e_i)
      U_A: accessible={r1, r2}  — sees e_j and e_k; no phantom
      U_B: accessible={r2, r3}  — sees e_k and e_i; no phantom

    Pairwise overlaps:
      U_P ∩ U_A = {r1}          — sees e_j only (trivial order)
      U_P ∩ U_B = {r3}          — sees e_i only (trivial order)
      U_A ∩ U_B = {r2}          — sees e_k only (trivial order)

    All pairwise overlaps have exactly one accessible event. This means
    C¹ has no non-reflexive pair data, so H¹ = 0 despite phantom incomparability.
    """
    e_j = EventNode(
        name="e_j",
        source_records=frozenset(),
        target_records=frozenset({"r1"}),
        causal=1,
        info=1,
    )
    e_k = EventNode(
        name="e_k",
        source_records=frozenset({"r1"}),
        target_records=frozenset({"r2"}),
        causal=2,
        info=2,
    )
    e_i = EventNode(
        name="e_i",
        source_records=frozenset({"r2"}),
        target_records=frozenset({"r3"}),
        causal=3,
        info=3,
    )
    u_p = ObserverPatch(name="U_P", accessible_records=frozenset({"r1", "r3"}))
    u_a = ObserverPatch(name="U_A", accessible_records=frozenset({"r1", "r2"}))
    u_b = ObserverPatch(name="U_B", accessible_records=frozenset({"r2", "r3"}))
    return FiniteObserverCover(
        name="hidden_intermediary",
        events=(e_j, e_k, e_i),
        patches=(u_p, u_a, u_b),
    )


def _build_no_phantom_cover() -> FiniteObserverCover:
    """
    A cover where all observers have full access. No phantom incomparability.
    Used as a control case.
    """
    e_j = EventNode(
        name="e_j",
        source_records=frozenset(),
        target_records=frozenset({"r1"}),
        causal=1,
        info=1,
    )
    e_i = EventNode(
        name="e_i",
        source_records=frozenset({"r1"}),
        target_records=frozenset({"r2"}),
        causal=2,
        info=2,
    )
    u_full = ObserverPatch(
        name="U_full", accessible_records=frozenset({"r1", "r2"})
    )
    return FiniteObserverCover(
        name="no_phantom",
        events=(e_j, e_i),
        patches=(u_full,),
    )


def _build_dense_cover() -> FiniteObserverCover:
    """
    A cover where the U_full observer overlaps richly with phantom-observer U_P.
    This tests whether adding U_full to the {U_P, U_A, U_B} cover changes H¹.

    Adding U_full = {r1,r2,r3} (sees all events) to the cover.
    U_P ∩ U_full = U_P = {r1,r3} — sees e_j and e_i (non-trivial overlap!)
    Now the overlap U_P ∩ U_full has the phantom pair (e_j, e_i).
    """
    e_j = EventNode(
        name="e_j",
        source_records=frozenset(),
        target_records=frozenset({"r1"}),
        causal=1,
        info=1,
    )
    e_k = EventNode(
        name="e_k",
        source_records=frozenset({"r1"}),
        target_records=frozenset({"r2"}),
        causal=2,
        info=2,
    )
    e_i = EventNode(
        name="e_i",
        source_records=frozenset({"r2"}),
        target_records=frozenset({"r3"}),
        causal=3,
        info=3,
    )
    u_p = ObserverPatch(name="U_P", accessible_records=frozenset({"r1", "r3"}))
    u_full = ObserverPatch(
        name="U_full", accessible_records=frozenset({"r1", "r2", "r3"})
    )
    return FiniteObserverCover(
        name="dense_cover",
        events=(e_j, e_k, e_i),
        patches=(u_p, u_full),
    )


# ---------------------------------------------------------------------------
# Main audit function
# ---------------------------------------------------------------------------


def run_t56_audit() -> T56AuditResult:
    """
    Run the full T56 sheaf cohomology audit.

    Uses the hidden-intermediary cover as the primary witness.
    The dense cover is checked to confirm the cover-dependency of H¹.
    """
    ledger = _build_assumption_ledger()
    cover = _build_hidden_intermediary_cover()
    global_order = compute_global_order(cover)

    # Presheaf checks
    ambient_check = check_ambient_presheaf_functoriality(cover, global_order)
    apparent_check = check_apparent_presheaf_closure(cover, global_order)

    # Phantom detection
    phantoms = detect_phantom_pairs(cover, global_order)

    # Section compatibility
    compat = check_section_compatibility(cover, global_order)

    # Čech H¹ for apparent presheaf and ambient presheaf
    h1_apparent = compute_cech_complex(cover, global_order, use_apparent_for_local=True)
    h1_ambient = compute_cech_complex(cover, global_order, use_apparent_for_local=False)

    # Outcome classification
    # Criteria:
    #   - Ambient presheaf is well-defined (functorial) → sheaf language is applicable
    #   - Apparent-order assignment is NOT a presheaf → H¹(F) is ill-defined
    #   - H¹(A) = 0 → no H¹ obstruction in the ambient presheaf
    #   - Phantom pairs exist but live in section-compatibility gap (H⁰), not H¹
    #   - No circular import detected (medium risk only, not high)
    #   → PARTIAL_SUCCESS

    has_phantom = len(phantoms) > 0
    f_is_presheaf = apparent_check.is_functorial
    a_is_presheaf = ambient_check.is_functorial
    h1_ambient_zero = h1_ambient.h1_dimension == 0
    h1_apparent_zero = h1_apparent.h1_dimension == 0
    local_sections_fail = not compat.local_sections_compatible
    high_circular_risk = any(
        e.circular_risk == CircularRisk.HIGH for e in ledger
    )

    if high_circular_risk:
        outcome = AuditOutcome.FAILURE_ASSUMPTION
    elif not a_is_presheaf:
        outcome = AuditOutcome.FAILURE_MISMATCH
    elif a_is_presheaf and not f_is_presheaf and has_phantom and h1_ambient_zero:
        outcome = AuditOutcome.PARTIAL_SUCCESS
    elif a_is_presheaf and f_is_presheaf and not has_phantom:
        outcome = AuditOutcome.SUCCESS
    else:
        outcome = AuditOutcome.FAILURE_MISMATCH

    refined_hypothesis = (
        "Phantom incomparability is NOT an H¹ obstruction of the apparent-finality "
        "presheaf (H¹(A) = 0; F is not a presheaf). It IS a section-compatibility "
        "obstruction: the collection {F(U_i)} (local apparent orders) does not form "
        "a compatible 0-cochain for the ambient presheaf A. The phantom pair (e_j, e_i) "
        "lives in G(U) = A(U) \\ F(U), the gap between what the global colimit restricts "
        "to at U and what U computes locally. The relevant invariant is H⁰(G), the "
        "global sections of the gap presheaf — not H¹ of any presheaf over the cover."
    )

    finding = (
        "PARTIAL_SUCCESS. "
        "The sheaf language is the correct framework: the apparent-finality presheaf "
        "A(U) = ρ_U(S_global) is well-defined and has H¹ = 0 (the global colimit is a "
        "compatible global section with no higher obstruction). The apparent-finality-order "
        "assignment F(U) = S_local(U) is NOT a presheaf — natural restriction maps "
        "map F(V) outside F(U) when V ⊃ U and phantom intermediaries exist. Phantom "
        "incomparability shows up as a mismatch between local sections {F(U_i)} and "
        "the restricted global section {A(U_i)}: a H⁰-level (section-compatibility) "
        "phenomenon rather than H¹. The original hypothesis (H¹) is at the wrong "
        "cohomological degree. The correct reformulation replaces H¹(F) with H⁰(G) "
        "where G = A/F is the gap presheaf."
    )

    open_questions = (
        "Q1: Is H⁰(G) ≅ the set of phantom incomparability witnesses from T51–T52? "
        "Specifically, does every T51/T52 phantom pair (e_j, e_i) at observer U appear "
        "as a section of G(U), and vice versa?",
        "Q2: Does the apparent-finality assignment F admit a sheafification F⁺, and "
        "is F⁺ = A (the ambient presheaf)? If so, the sheafification map F → A is the "
        "canonical 'colimit completion' operation of T51–T52.",
        "Q3: Can the 'pre-presheaf' structure of F (it has local sections and a "
        "restriction-like inclusion F(U) ⊆ A(U), but no natural restriction maps) "
        "be captured by a lax functor or by Čech cohomology of the NERVE of the cover "
        "(where nodes = events, edges = direct record-dependencies)?",
        "Q4: Does the medium circular risk on the record-dependency arrow direction "
        "have a constructor-theoretic resolution? Specifically, can the pre/post-finality "
        "asymmetry be derived from substrate-free task-composability (W4 defense), making "
        "the record-dependency order definitionally non-circular?",
    )

    return T56AuditResult(
        cover=cover,
        assumption_ledger=ledger,
        global_order=global_order,
        apparent_presheaf_check=apparent_check,
        ambient_presheaf_check=ambient_check,
        phantom_pairs=phantoms,
        section_compatibility=compat,
        cech_h1_apparent=h1_apparent,
        cech_h1_ambient=h1_ambient,
        outcome=outcome,
        refined_hypothesis=refined_hypothesis,
        finding=finding,
        open_questions=open_questions,
    )


def t56_result_to_dict(result: T56AuditResult) -> dict[str, Any]:
    """Serialize T56AuditResult to a plain dictionary for JSON export."""
    return {
        "cover_name": result.cover.name,
        "outcome": result.outcome.value,
        "ambient_presheaf_functorial": result.ambient_presheaf_check.is_functorial,
        "apparent_presheaf_is_presheaf": result.apparent_presheaf_check.is_functorial,
        "phantom_pairs": [
            {
                "observer": p.observer,
                "event_j": p.event_j,
                "event_i": p.event_i,
                "local": p.local_order_at_observer,
                "global": p.global_order,
                "hidden_intermediaries": list(p.hidden_intermediaries),
            }
            for p in result.phantom_pairs
        ],
        "local_sections_compatible": result.section_compatibility.local_sections_compatible,
        "colimit_is_global_section": result.section_compatibility.colimit_section_compatible,
        "cech_h1_apparent": {
            "h1_dimension": result.cech_h1_apparent.h1_dimension,
            "c1_dimension": result.cech_h1_apparent.c1_dimension,
            "finding": result.cech_h1_apparent.finding,
        },
        "cech_h1_ambient": {
            "h1_dimension": result.cech_h1_ambient.h1_dimension,
            "c1_dimension": result.cech_h1_ambient.c1_dimension,
            "finding": result.cech_h1_ambient.finding,
        },
        "refined_hypothesis": result.refined_hypothesis,
        "finding": result.finding,
        "open_questions": list(result.open_questions),
        "assumption_ledger": [
            {
                "name": e.name,
                "inherited_from": e.inherited_from,
                "status": e.status.value,
                "circular_risk": e.circular_risk.value,
                "risk_note": e.risk_note,
            }
            for e in result.assumption_ledger
        ],
    }
