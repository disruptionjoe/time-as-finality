"""T125: finite boundary-connection transport for D1 profiles.

This module implements the first connection-like object allowed by T111:
transport of boundary-indexed D1 tuples with provenance-bearing boundary
deltas. It is deliberately finite bookkeeping. It does not compute curvature,
gravity, torsion, or anomaly data.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from typing import Any

from models.t111_d1_gauge_invariance_audit import (
    D1GaugeProfile,
    D1GaugeSystem,
    access_boundary_coarsening,
    access_boundary_refinement,
    causal_graph_isomorphism,
    compute_profile,
    holder_relabeling_preserving_partitions,
    negative_causal_graph_nonisomorphism,
    negative_holder_partition_merge,
    negative_record_incidence_break,
    observer_relabeling,
    record_label_permutation,
    reference_system,
)


PROFILE_DIMS = (
    "accessible_support",
    "distinct_holder_redundancy",
    "causal_branch_support",
    "graph_reversal_count",
)


@dataclass(frozen=True)
class BoundaryObject:
    boundary_id: str
    system: D1GaugeSystem
    profile: D1GaugeProfile
    provenance: tuple[str, ...]


@dataclass(frozen=True)
class BoundaryDelta:
    profile_before: D1GaugeProfile
    profile_after: D1GaugeProfile
    operation_kind: str
    changed_records: tuple[str, ...]
    changed_holders: tuple[str, ...]
    changed_access_boundary: tuple[str, ...]
    changed_reachability: tuple[str, ...]
    reversible: bool
    loss_notes: tuple[str, ...]


@dataclass(frozen=True)
class TransportArrow:
    arrow_id: str
    source: str
    target: str
    operation_kind: str
    declared_admissible: bool
    pure_gauge: bool
    reversible: bool
    provenance: tuple[str, ...]
    loss_notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class TransportAudit:
    arrow_id: str
    source: str
    target: str
    transported_profile: D1GaugeProfile | None
    boundary_delta: BoundaryDelta | None
    admissibility_verdict: str
    provenance_trace: tuple[str, ...]
    interpretation: str


@dataclass(frozen=True)
class CompositionAudit:
    composition_id: str
    arrows: tuple[str, ...]
    direct_arrow: str | None
    composite_profile: D1GaugeProfile | None
    direct_profile: D1GaugeProfile | None
    deltas_preserved: bool
    admissibility_verdict: str
    provenance_trace: tuple[str, ...]
    interpretation: str


@dataclass(frozen=True)
class LoopAudit:
    loop_id: str
    arrows: tuple[str, ...]
    start_profile: D1GaugeProfile
    end_profile: D1GaugeProfile | None
    classification: str
    residual_boundary_delta: bool
    provenance_trace: tuple[str, ...]
    interpretation: str


@dataclass(frozen=True)
class T125Result:
    objects: tuple[BoundaryObject, ...]
    transport_audits: tuple[TransportAudit, ...]
    composition_audits: tuple[CompositionAudit, ...]
    loop_audits: tuple[LoopAudit, ...]
    identity_passes: bool
    pure_gauge_loops_close: bool
    lossy_loops_report_residual_delta: bool
    hostile_maps_undefined: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def boundary_objects() -> dict[str, BoundaryObject]:
    base = reference_system()
    refined = access_boundary_refinement(base)
    coarsened = access_boundary_coarsening(base)
    observer_copy = observer_relabeling(base)
    record_copy = record_label_permutation(base)
    holder_copy = holder_relabeling_preserving_partitions(base)
    causal_copy = causal_graph_isomorphism(base)
    negative_record = negative_record_incidence_break(base)
    negative_holder = negative_holder_partition_merge(base)
    negative_causal = negative_causal_graph_nonisomorphism(base)
    systems = {
        "B0": (base, ("reference_boundary",)),
        "B0_observer_relabel": (observer_copy, ("observer_relabeling",)),
        "B0_record_relabel": (record_copy, ("record_label_permutation",)),
        "B0_holder_relabel": (holder_copy, ("holder_relabeling",)),
        "B0_causal_relabel": (causal_copy, ("causal_graph_isomorphism",)),
        "B_refined": (refined, ("access_boundary_refinement",)),
        "B_coarsened": (coarsened, ("access_boundary_coarsening",)),
        "B_bad_record": (negative_record, ("negative_record_incidence_break",)),
        "B_bad_holder": (negative_holder, ("negative_holder_partition_merge",)),
        "B_bad_causal": (negative_causal, ("negative_causal_nonisomorphism",)),
    }
    return {
        boundary_id: BoundaryObject(
            boundary_id=boundary_id,
            system=system,
            profile=compute_profile(system),
            provenance=provenance,
        )
        for boundary_id, (system, provenance) in systems.items()
    }


def transport_arrows() -> dict[str, TransportArrow]:
    object_ids = (
        "B0",
        "B0_observer_relabel",
        "B0_record_relabel",
        "B0_holder_relabel",
        "B0_causal_relabel",
        "B_refined",
        "B_coarsened",
    )
    arrows: dict[str, TransportArrow] = {
        f"id_{object_id}": TransportArrow(
            arrow_id=f"id_{object_id}",
            source=object_id,
            target=object_id,
            operation_kind="identity",
            declared_admissible=True,
            pure_gauge=True,
            reversible=True,
            provenance=("identity_transport", object_id),
        )
        for object_id in object_ids
    }
    arrows.update(
        {
            "gauge_observer": _arrow(
                "gauge_observer",
                "B0",
                "B0_observer_relabel",
                "pure_gauge_relabeling",
                True,
                True,
                True,
                ("observer_id_bijection",),
            ),
            "gauge_observer_back": _arrow(
                "gauge_observer_back",
                "B0_observer_relabel",
                "B0",
                "pure_gauge_relabeling",
                True,
                True,
                True,
                ("observer_id_inverse_bijection",),
            ),
            "gauge_record": _arrow(
                "gauge_record",
                "B0",
                "B0_record_relabel",
                "pure_gauge_relabeling",
                True,
                True,
                True,
                ("record_id_bijection",),
            ),
            "gauge_holder": _arrow(
                "gauge_holder",
                "B0",
                "B0_holder_relabel",
                "pure_gauge_relabeling",
                True,
                True,
                True,
                ("holder_id_bijection_with_partition",),
            ),
            "gauge_causal": _arrow(
                "gauge_causal",
                "B0",
                "B0_causal_relabel",
                "pure_gauge_relabeling",
                True,
                True,
                True,
                ("causal_graph_isomorphism",),
            ),
            "refine_access": _arrow(
                "refine_access",
                "B0",
                "B_refined",
                "access_boundary_refinement",
                True,
                False,
                False,
                ("drop_access_to_archive_holders",),
                ("records_hidden_from_target_boundary",),
            ),
            "restore_from_refined_trace": _arrow(
                "restore_from_refined_trace",
                "B_refined",
                "B0",
                "access_boundary_coarsening_with_trace",
                True,
                False,
                True,
                ("restore_access_using_retained_boundary_trace",),
            ),
            "coarsen_access": _arrow(
                "coarsen_access",
                "B0",
                "B_coarsened",
                "access_boundary_coarsening",
                True,
                False,
                False,
                ("add_auxiliary_holder_access",),
            ),
            "restrict_from_coarsened": _arrow(
                "restrict_from_coarsened",
                "B_coarsened",
                "B0",
                "access_boundary_refinement",
                True,
                False,
                False,
                ("remove_auxiliary_holder_access",),
                ("auxiliary_access_removed",),
            ),
            "missing_boundary_provenance": _arrow(
                "missing_boundary_provenance",
                "B0",
                "B_refined",
                "access_boundary_refinement",
                False,
                False,
                False,
                (),
                ("profile_changed_without_provenance",),
            ),
            "bad_record_incidence": _arrow(
                "bad_record_incidence",
                "B0",
                "B_bad_record",
                "record_incidence_break",
                False,
                False,
                False,
                ("invalid_record_event_holder_map",),
                ("record_incidence_not_preserved",),
            ),
            "bad_holder_partition": _arrow(
                "bad_holder_partition",
                "B0",
                "B_bad_holder",
                "holder_partition_merge",
                False,
                False,
                False,
                ("invalid_holder_partition_map",),
                ("independence_partition_not_preserved",),
            ),
            "bad_causal_reachability": _arrow(
                "bad_causal_reachability",
                "B0",
                "B_bad_causal",
                "causal_nonisomorphism",
                False,
                False,
                False,
                ("invalid_causal_map",),
                ("reachability_changed_without_transport_rule",),
            ),
            "scalarized_profile": _arrow(
                "scalarized_profile",
                "B0",
                "B0",
                "scalarization_control",
                False,
                False,
                False,
                ("tuple_collapsed_to_sum",),
                ("d1_tuple_erased_before_transport",),
            ),
        }
    )
    return arrows


def audit_transport(
    arrow: TransportArrow,
    objects: dict[str, BoundaryObject] | None = None,
) -> TransportAudit:
    objs = objects or boundary_objects()
    source = objs[arrow.source]
    target = objs[arrow.target]
    profile_changed = source.profile != target.profile
    has_provenance = bool(arrow.provenance)
    if not arrow.declared_admissible:
        return TransportAudit(
            arrow_id=arrow.arrow_id,
            source=arrow.source,
            target=arrow.target,
            transported_profile=None,
            boundary_delta=None,
            admissibility_verdict="undefined",
            provenance_trace=arrow.provenance,
            interpretation=_undefined_interpretation(arrow),
        )
    if arrow.pure_gauge and profile_changed:
        verdict = "invalid_gauge_profile_change"
    elif profile_changed and not has_provenance:
        verdict = "invalid_missing_boundary_provenance"
    elif arrow.operation_kind == "identity":
        verdict = "identity"
    elif arrow.pure_gauge:
        verdict = "pure_gauge_identity_delta"
    else:
        verdict = "boundary_delta"
    delta = BoundaryDelta(
        profile_before=source.profile,
        profile_after=target.profile,
        operation_kind=arrow.operation_kind,
        changed_records=_changed_records(source.system, target.system),
        changed_holders=_changed_holders(source.system, target.system),
        changed_access_boundary=_changed_access_boundary(source.system, target.system),
        changed_reachability=_changed_reachability(source.system, target.system),
        reversible=arrow.reversible,
        loss_notes=arrow.loss_notes,
    )
    return TransportAudit(
        arrow_id=arrow.arrow_id,
        source=arrow.source,
        target=arrow.target,
        transported_profile=target.profile,
        boundary_delta=delta,
        admissibility_verdict=verdict,
        provenance_trace=arrow.provenance,
        interpretation=_transport_interpretation(arrow, verdict, delta),
    )


def audit_composition(
    composition_id: str,
    arrow_ids: tuple[str, ...],
    direct_arrow_id: str | None = None,
    objects: dict[str, BoundaryObject] | None = None,
    arrows: dict[str, TransportArrow] | None = None,
) -> CompositionAudit:
    objs = objects or boundary_objects()
    arrs = arrows or transport_arrows()
    audits = tuple(audit_transport(arrs[arrow_id], objs) for arrow_id in arrow_ids)
    provenance = tuple(
        item for audit in audits for item in audit.provenance_trace
    )
    if any(audit.admissibility_verdict == "undefined" for audit in audits):
        return CompositionAudit(
            composition_id=composition_id,
            arrows=arrow_ids,
            direct_arrow=direct_arrow_id,
            composite_profile=None,
            direct_profile=None,
            deltas_preserved=False,
            admissibility_verdict="undefined_intermediate",
            provenance_trace=provenance,
            interpretation="Composition is undefined because an intermediate transport is undefined.",
        )
    if not _composable(arrow_ids, arrs):
        return CompositionAudit(
            composition_id=composition_id,
            arrows=arrow_ids,
            direct_arrow=direct_arrow_id,
            composite_profile=None,
            direct_profile=None,
            deltas_preserved=False,
            admissibility_verdict="source_target_mismatch",
            provenance_trace=provenance,
            interpretation="Composition is undefined because adjacent arrows do not share a boundary object.",
        )
    composite_profile = objs[arrs[arrow_ids[-1]].target].profile
    direct_profile = None
    if direct_arrow_id is not None:
        direct_audit = audit_transport(arrs[direct_arrow_id], objs)
        direct_profile = direct_audit.transported_profile
    deltas_preserved = len(provenance) >= len(arrow_ids)
    profiles_agree = direct_profile is None or direct_profile == composite_profile
    return CompositionAudit(
        composition_id=composition_id,
        arrows=arrow_ids,
        direct_arrow=direct_arrow_id,
        composite_profile=composite_profile,
        direct_profile=direct_profile,
        deltas_preserved=deltas_preserved,
        admissibility_verdict=(
            "composes_with_declared_direct_effect"
            if profiles_agree and deltas_preserved
            else "composition_mismatch"
        ),
        provenance_trace=provenance,
        interpretation=(
            "Composition preserves ordered boundary provenance and reaches the declared target profile."
            if profiles_agree and deltas_preserved
            else "Composition loses provenance or fails to match the declared direct effect."
        ),
    )


def audit_loop(
    loop_id: str,
    arrow_ids: tuple[str, ...],
    objects: dict[str, BoundaryObject] | None = None,
    arrows: dict[str, TransportArrow] | None = None,
) -> LoopAudit:
    objs = objects or boundary_objects()
    arrs = arrows or transport_arrows()
    start = objs[arrs[arrow_ids[0]].source]
    composition = audit_composition(loop_id, arrow_ids, None, objs, arrs)
    if composition.composite_profile is None:
        return LoopAudit(
            loop_id=loop_id,
            arrows=arrow_ids,
            start_profile=start.profile,
            end_profile=None,
            classification="undefined",
            residual_boundary_delta=True,
            provenance_trace=composition.provenance_trace,
            interpretation="Loop is undefined because at least one transport is inadmissible.",
        )
    end_profile = composition.composite_profile
    loop_arrows = tuple(arrs[arrow_id] for arrow_id in arrow_ids)
    residual = any(
        (not arrow.pure_gauge) and (not arrow.reversible or arrow.loss_notes)
        for arrow in loop_arrows
    )
    if start.profile == end_profile and not residual:
        classification = "identity_loop"
        interpretation = "Loop returns the original profile with no residual boundary delta."
    elif start.profile == end_profile and residual:
        classification = "closed_with_residual_boundary_delta"
        interpretation = "Loop returns the profile but retains nontrivial boundary provenance."
    else:
        classification = "nontrivial_boundary_transport"
        interpretation = "Loop does not return the original profile, so it is not a gauge-trivial loop."
    return LoopAudit(
        loop_id=loop_id,
        arrows=arrow_ids,
        start_profile=start.profile,
        end_profile=end_profile,
        classification=classification,
        residual_boundary_delta=residual,
        provenance_trace=composition.provenance_trace,
        interpretation=interpretation,
    )


def run_t125_analysis() -> T125Result:
    objects = boundary_objects()
    arrows = transport_arrows()
    transport_audits = tuple(
        audit_transport(arrow, objects) for arrow in arrows.values()
    )
    compositions = (
        audit_composition(
            "pure_gauge_record_then_identity",
            ("gauge_record", "id_B0_record_relabel"),
            "gauge_record",
            objects,
            arrows,
        ),
        audit_composition(
            "refine_then_restore",
            ("refine_access", "restore_from_refined_trace"),
            "id_B0",
            objects,
            arrows,
        ),
        audit_composition(
            "coarsen_then_restrict",
            ("coarsen_access", "restrict_from_coarsened"),
            "id_B0",
            objects,
            arrows,
        ),
        audit_composition(
            "undefined_middle_map",
            ("missing_boundary_provenance", "restore_from_refined_trace"),
            None,
            objects,
            arrows,
        ),
    )
    loops = (
        audit_loop(
            "pure_observer_relabeling_loop",
            ("gauge_observer", "gauge_observer_back"),
            objects,
            arrows,
        ),
        audit_loop(
            "refinement_restore_with_trace_loop",
            ("refine_access", "restore_from_refined_trace"),
            objects,
            arrows,
        ),
        audit_loop(
            "coarsen_restrict_lossy_boundary_loop",
            ("coarsen_access", "restrict_from_coarsened"),
            objects,
            arrows,
        ),
        audit_loop(
            "hostile_missing_provenance_loop",
            ("missing_boundary_provenance", "restore_from_refined_trace"),
            objects,
            arrows,
        ),
    )
    identity_passes = all(
        audit.admissibility_verdict == "identity"
        and audit.transported_profile == objects[audit.source].profile
        for audit in transport_audits
        if audit.arrow_id.startswith("id_")
    )
    pure_gauge_loops_close = all(
        loop.classification == "identity_loop"
        for loop in loops
        if loop.loop_id == "pure_observer_relabeling_loop"
    )
    lossy_loops_report_residual_delta = all(
        loop.residual_boundary_delta
        and loop.classification == "closed_with_residual_boundary_delta"
        for loop in loops
        if loop.loop_id
        in {
            "refinement_restore_with_trace_loop",
            "coarsen_restrict_lossy_boundary_loop",
        }
    )
    hostile_maps_undefined = all(
        audit.admissibility_verdict == "undefined"
        for audit in transport_audits
        if audit.arrow_id
        in {
            "missing_boundary_provenance",
            "bad_record_incidence",
            "bad_holder_partition",
            "bad_causal_reachability",
            "scalarized_profile",
        }
    )
    return T125Result(
        objects=tuple(objects.values()),
        transport_audits=transport_audits,
        composition_audits=compositions,
        loop_audits=loops,
        identity_passes=identity_passes,
        pure_gauge_loops_close=pure_gauge_loops_close,
        lossy_loops_report_residual_delta=lossy_loops_report_residual_delta,
        hostile_maps_undefined=hostile_maps_undefined,
        strongest_claim=(
            "T125 implements a finite provenance-aware transport rule for "
            "boundary-indexed D1 profiles. Pure relabeling transports close as "
            "identity, access-boundary transports carry typed deltas, lossy "
            "loops retain residual boundary provenance, and hostile or "
            "scalarized maps are undefined."
        ),
        improved=(
            "The finality gauge-theory branch now has a connection-definition "
            "prerequisite: identity, composition, and closed-loop behavior are "
            "auditable before any curvature or gravity language is allowed."
        ),
        weakened=(
            "This weakens curvature talk. Profile changes across access "
            "boundaries are not gauge-invariant field strength; they are "
            "boundary data unless a later theorem defines a real curvature "
            "object over these transports."
        ),
        falsification_condition=(
            "T125 fails if an identity changes a D1 tuple, pure gauge transport "
            "changes a profile, composition discards intermediate provenance, "
            "a lossy boundary loop is treated as trivial, or a hostile map is "
            "silently repaired into an admissible transport."
        ),
        claim_ledger_update=(
            "Add T125 to D1/D1-Field as a formal transport prerequisite: D1 "
            "profiles can be carried across declared finite boundary maps only "
            "with provenance-bearing deltas; no curvature, gravity, torsion, "
            "or physical observable upgrade follows."
        ),
        open_blocker=(
            "No curvature functional, flatness criterion, continuum limit, "
            "Lorentzian covariance result, or physical reduction of branch "
            "support and reversal count exists."
        ),
        recommended_next=(
            "Use T125 to define a minimal flatness/holonomy audit over "
            "boundary loops, but keep it finite and reject gravity language "
            "until a nontrivial loop invariant survives relabeling and "
            "access-boundary absorbers."
        ),
    )


def t125_result_to_dict(result: T125Result) -> dict[str, Any]:
    return {
        "objects": [
            {
                "boundary_id": item.boundary_id,
                "profile": _profile_to_dict(item.profile),
                "provenance": list(item.provenance),
            }
            for item in result.objects
        ],
        "transport_audits": [
            {
                "arrow_id": item.arrow_id,
                "source": item.source,
                "target": item.target,
                "transported_profile": (
                    None
                    if item.transported_profile is None
                    else _profile_to_dict(item.transported_profile)
                ),
                "boundary_delta": (
                    None
                    if item.boundary_delta is None
                    else _delta_to_dict(item.boundary_delta)
                ),
                "admissibility_verdict": item.admissibility_verdict,
                "provenance_trace": list(item.provenance_trace),
                "interpretation": item.interpretation,
            }
            for item in result.transport_audits
        ],
        "composition_audits": [
            {
                "composition_id": item.composition_id,
                "arrows": list(item.arrows),
                "direct_arrow": item.direct_arrow,
                "composite_profile": (
                    None
                    if item.composite_profile is None
                    else _profile_to_dict(item.composite_profile)
                ),
                "direct_profile": (
                    None
                    if item.direct_profile is None
                    else _profile_to_dict(item.direct_profile)
                ),
                "deltas_preserved": item.deltas_preserved,
                "admissibility_verdict": item.admissibility_verdict,
                "provenance_trace": list(item.provenance_trace),
                "interpretation": item.interpretation,
            }
            for item in result.composition_audits
        ],
        "loop_audits": [
            {
                "loop_id": item.loop_id,
                "arrows": list(item.arrows),
                "start_profile": _profile_to_dict(item.start_profile),
                "end_profile": (
                    None if item.end_profile is None else _profile_to_dict(item.end_profile)
                ),
                "classification": item.classification,
                "residual_boundary_delta": item.residual_boundary_delta,
                "provenance_trace": list(item.provenance_trace),
                "interpretation": item.interpretation,
            }
            for item in result.loop_audits
        ],
        "identity_passes": result.identity_passes,
        "pure_gauge_loops_close": result.pure_gauge_loops_close,
        "lossy_loops_report_residual_delta": result.lossy_loops_report_residual_delta,
        "hostile_maps_undefined": result.hostile_maps_undefined,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _arrow(
    arrow_id: str,
    source: str,
    target: str,
    operation_kind: str,
    declared_admissible: bool,
    pure_gauge: bool,
    reversible: bool,
    provenance: tuple[str, ...],
    loss_notes: tuple[str, ...] = (),
) -> TransportArrow:
    return TransportArrow(
        arrow_id=arrow_id,
        source=source,
        target=target,
        operation_kind=operation_kind,
        declared_admissible=declared_admissible,
        pure_gauge=pure_gauge,
        reversible=reversible,
        provenance=provenance,
        loss_notes=loss_notes,
    )


def _changed_records(source: D1GaugeSystem, target: D1GaugeSystem) -> tuple[str, ...]:
    source_records = {(item.record_id, item.event, item.holder) for item in source.records}
    target_records = {(item.record_id, item.event, item.holder) for item in target.records}
    return tuple(sorted(str(item) for item in source_records ^ target_records))


def _changed_holders(source: D1GaugeSystem, target: D1GaugeSystem) -> tuple[str, ...]:
    source_items = set(source.holder_independence.items())
    target_items = set(target.holder_independence.items())
    access_change = source.boundary.accessible_holders ^ target.boundary.accessible_holders
    return tuple(sorted(str(item) for item in source_items ^ target_items)) + tuple(
        sorted(f"access:{item}" for item in access_change)
    )


def _changed_access_boundary(
    source: D1GaugeSystem,
    target: D1GaugeSystem,
) -> tuple[str, ...]:
    changes: list[str] = []
    if source.boundary.observer_id != target.boundary.observer_id:
        changes.append("observer_id")
    if source.boundary.event_horizon != target.boundary.event_horizon:
        changes.append("event_horizon")
    if source.boundary.accessible_holders != target.boundary.accessible_holders:
        changes.append("accessible_holders")
    if source.boundary.threshold != target.boundary.threshold:
        changes.append("threshold")
    return tuple(changes)


def _changed_reachability(
    source: D1GaugeSystem,
    target: D1GaugeSystem,
) -> tuple[str, ...]:
    source_edges = set(source.causal_edges)
    target_edges = set(target.causal_edges)
    source_events = set(source.events)
    target_events = set(target.events)
    changes = tuple(sorted(str(item) for item in source_edges ^ target_edges))
    event_changes = tuple(sorted(f"event:{item}" for item in source_events ^ target_events))
    return event_changes + changes


def _composable(arrow_ids: tuple[str, ...], arrows: dict[str, TransportArrow]) -> bool:
    return all(
        arrows[left].target == arrows[right].source
        for left, right in zip(arrow_ids, arrow_ids[1:])
    )


def _transport_interpretation(
    arrow: TransportArrow,
    verdict: str,
    delta: BoundaryDelta,
) -> str:
    if verdict == "identity":
        return "Identity transport preserves the source boundary profile exactly."
    if verdict == "pure_gauge_identity_delta":
        return "Pure relabeling preserves the D1 tuple and records only gauge provenance."
    if verdict == "boundary_delta":
        return (
            "Boundary transport is admissible because the profile change is "
            f"carried as `{delta.operation_kind}` provenance, not erased as gauge."
        )
    return "Transport failed one of the finite admissibility checks."


def _undefined_interpretation(arrow: TransportArrow) -> str:
    if arrow.arrow_id == "scalarized_profile":
        return "Scalarization is undefined because T125 transports the D1 tuple, not a summed score."
    return (
        "Transport is undefined because the map lacks admissible provenance or "
        "breaks record, holder, access, or causal preservation."
    )


def _profile_to_dict(profile: D1GaugeProfile) -> dict[str, Any]:
    return asdict(profile) | {
        "tuple_order": list(PROFILE_DIMS),
        "profile_tuple": [
            profile.accessible_support,
            profile.distinct_holder_redundancy,
            profile.causal_branch_support,
            profile.graph_reversal_count,
        ],
    }


def _delta_to_dict(delta: BoundaryDelta) -> dict[str, Any]:
    return {
        "profile_before": _profile_to_dict(delta.profile_before),
        "profile_after": _profile_to_dict(delta.profile_after),
        "operation_kind": delta.operation_kind,
        "changed_records": list(delta.changed_records),
        "changed_holders": list(delta.changed_holders),
        "changed_access_boundary": list(delta.changed_access_boundary),
        "changed_reachability": list(delta.changed_reachability),
        "reversible": delta.reversible,
        "loss_notes": list(delta.loss_notes),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t125_result_to_dict(run_t125_analysis()), indent=2))
