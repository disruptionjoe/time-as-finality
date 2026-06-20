"""T111: finite D1 gauge-invariance audit.

This module audits the four D1 profile dimensions under a finite list of
admissible transformations.  It deliberately stops at invariance and
covariance bookkeeping; it does not introduce curvature, gravity, or anomaly
claims.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from itertools import combinations
from typing import Any, Callable


D1_DIMENSIONS = (
    "accessible_support",
    "distinct_holder_redundancy",
    "causal_branch_support",
    "graph_reversal_count",
)

CLASSIFICATIONS = (
    "invariant",
    "covariant",
    "gauge-dependent",
    "undefined",
)

PURE_GAUGE_KINDS = (
    "observer_relabeling",
    "record_label_permutation",
    "holder_relabeling",
    "causal_graph_isomorphism",
)

BOUNDARY_KINDS = (
    "access_boundary_refinement",
    "access_boundary_coarsening",
)


@dataclass(frozen=True)
class D1GaugeProfile:
    accessible_support: int
    distinct_holder_redundancy: int
    causal_branch_support: int
    graph_reversal_count: int

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (
            self.accessible_support,
            self.distinct_holder_redundancy,
            self.causal_branch_support,
            self.graph_reversal_count,
        )


@dataclass(frozen=True)
class GaugeRecord:
    record_id: str
    proposition: str
    value: str
    event: str
    holder: str
    active: bool = True


@dataclass(frozen=True)
class AccessBoundary:
    observer_id: str
    event_horizon: str
    accessible_holders: frozenset[str]
    threshold: int


@dataclass(frozen=True)
class D1GaugeSystem:
    name: str
    events: tuple[str, ...]
    causal_edges: tuple[tuple[str, str], ...]
    records: tuple[GaugeRecord, ...]
    holder_independence: dict[str, str]
    boundary: AccessBoundary
    proposition: str = "R"
    value: str = "true"


@dataclass(frozen=True)
class TransformationSpec:
    name: str
    kind: str
    admissible: bool
    gauge_pure: bool
    description: str
    transformed_system: D1GaugeSystem
    transport_rule: str
    negative_control_reason: str = ""


@dataclass(frozen=True)
class DimensionClassification:
    transformation: str
    dimension: str
    classification: str
    before_value: int
    after_value: int
    transport_rule: str
    reason: str


@dataclass(frozen=True)
class TransformationAudit:
    name: str
    kind: str
    admissible: bool
    gauge_pure: bool
    before_profile: D1GaugeProfile
    after_profile: D1GaugeProfile
    classifications: tuple[DimensionClassification, ...]
    invariant_failure_dimensions: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class DimensionSummary:
    dimension: str
    pure_gauge_classification: str
    boundary_classification: str
    negative_control_failures: tuple[str, ...]
    future_connection_status: str
    observable_status: str


@dataclass(frozen=True)
class T111GaugeAuditResult:
    allowed_transformations: tuple[str, ...]
    negative_controls: tuple[str, ...]
    reference_profile: D1GaugeProfile
    audits: tuple[TransformationAudit, ...]
    dimension_summaries: tuple[DimensionSummary, ...]
    strongest_claim: str
    guardrail: str
    recommendation: str


def reference_system() -> D1GaugeSystem:
    events = (
        "source",
        "left",
        "right",
        "aux",
        "left_archive",
        "right_archive",
        "observe",
    )
    edges = (
        ("source", "left"),
        ("source", "right"),
        ("source", "aux"),
        ("left", "left_archive"),
        ("right", "right_archive"),
        ("left_archive", "observe"),
        ("right_archive", "observe"),
        ("aux", "observe"),
    )
    records = (
        GaugeRecord("r_left_1", "R", "true", "left", "h_left_1"),
        GaugeRecord("r_left_2", "R", "true", "left_archive", "h_left_2"),
        GaugeRecord("r_right_1", "R", "true", "right", "h_right_1"),
        GaugeRecord("r_right_2", "R", "true", "right_archive", "h_right_2"),
        GaugeRecord("r_aux", "R", "true", "aux", "h_aux"),
    )
    holder_independence = {
        "h_left_1": "left_family",
        "h_left_2": "left_family",
        "h_right_1": "right_family",
        "h_right_2": "right_family",
        "h_aux": "aux_family",
    }
    return D1GaugeSystem(
        name="t111_reference_d1_system",
        events=events,
        causal_edges=edges,
        records=records,
        holder_independence=holder_independence,
        boundary=AccessBoundary(
            observer_id="observer_A",
            event_horizon="observe",
            accessible_holders=frozenset(
                {"h_left_1", "h_left_2", "h_right_1", "h_right_2"}
            ),
            threshold=3,
        ),
    )


def validate_system(system: D1GaugeSystem) -> tuple[str, ...]:
    errors: list[str] = []
    event_set = set(system.events)
    if len(event_set) != len(system.events):
        errors.append("duplicate_events")
    if system.boundary.event_horizon not in event_set:
        errors.append("boundary_event_missing")
    for earlier, later in system.causal_edges:
        if earlier not in event_set or later not in event_set:
            errors.append(f"unknown_edge_endpoint:{earlier}->{later}")
    for record in system.records:
        if record.event not in event_set:
            errors.append(f"unknown_record_event:{record.record_id}")
        if record.holder not in system.holder_independence:
            errors.append(f"unknown_record_holder:{record.record_id}")
    missing_access_holders = system.boundary.accessible_holders - set(
        system.holder_independence
    )
    if missing_access_holders:
        errors.append(f"unknown_access_holders:{sorted(missing_access_holders)}")
    if system.boundary.threshold < 1:
        errors.append("threshold_less_than_one")
    if _has_cycle(system):
        errors.append("causal_cycle")
    return tuple(errors)


def compute_profile(system: D1GaugeSystem) -> D1GaugeProfile:
    errors = validate_system(system)
    if errors:
        raise ValueError(f"invalid D1 gauge system {system.name}: {errors}")
    records = accessible_supporting_records(system)
    support = len(records)
    independent_holders = {
        system.holder_independence[record.holder] for record in records
    }
    branch_support = _antichain_width(system, tuple(record.event for record in records))
    return D1GaugeProfile(
        accessible_support=support,
        distinct_holder_redundancy=len(independent_holders),
        causal_branch_support=branch_support,
        graph_reversal_count=max(0, support - system.boundary.threshold + 1),
    )


def accessible_supporting_records(system: D1GaugeSystem) -> tuple[GaugeRecord, ...]:
    return tuple(
        record
        for record in system.records
        if record.active
        and record.proposition == system.proposition
        and record.value == system.value
        and record.holder in system.boundary.accessible_holders
        and is_ancestor(system, record.event, system.boundary.event_horizon)
    )


def observer_relabeling(system: D1GaugeSystem) -> D1GaugeSystem:
    return replace(
        system,
        name="observer_relabeling_copy",
        boundary=replace(system.boundary, observer_id="observer_B"),
    )


def record_label_permutation(system: D1GaugeSystem) -> D1GaugeSystem:
    label_map = {
        "r_left_1": "rho_30",
        "r_left_2": "rho_10",
        "r_right_1": "rho_40",
        "r_right_2": "rho_20",
        "r_aux": "rho_50",
    }
    return replace(
        system,
        name="record_label_permutation_copy",
        records=tuple(
            replace(record, record_id=label_map[record.record_id])
            for record in system.records
        ),
    )


def holder_relabeling_preserving_partitions(system: D1GaugeSystem) -> D1GaugeSystem:
    holder_map = {
        "h_left_1": "H_La",
        "h_left_2": "H_Lb",
        "h_right_1": "H_Ra",
        "h_right_2": "H_Rb",
        "h_aux": "H_Aux",
    }
    return replace(
        system,
        name="holder_relabeling_partition_preserving_copy",
        records=tuple(
            replace(record, holder=holder_map[record.holder])
            for record in system.records
        ),
        holder_independence={
            holder_map[holder]: independence
            for holder, independence in system.holder_independence.items()
        },
        boundary=replace(
            system.boundary,
            accessible_holders=frozenset(
                holder_map[holder] for holder in system.boundary.accessible_holders
            ),
        ),
    )


def causal_graph_isomorphism(system: D1GaugeSystem) -> D1GaugeSystem:
    event_map = {
        "source": "sigma_0",
        "left": "sigma_L",
        "right": "sigma_R",
        "aux": "sigma_A",
        "left_archive": "sigma_L2",
        "right_archive": "sigma_R2",
        "observe": "sigma_obs",
    }
    return replace(
        system,
        name="causal_graph_isomorphic_copy",
        events=tuple(event_map[event] for event in system.events),
        causal_edges=tuple(
            (event_map[earlier], event_map[later])
            for earlier, later in system.causal_edges
        ),
        records=tuple(
            replace(record, event=event_map[record.event])
            for record in system.records
        ),
        boundary=replace(
            system.boundary,
            event_horizon=event_map[system.boundary.event_horizon],
        ),
    )


def access_boundary_refinement(system: D1GaugeSystem) -> D1GaugeSystem:
    return replace(
        system,
        name="access_boundary_refined_copy",
        boundary=replace(
            system.boundary,
            accessible_holders=frozenset({"h_left_1", "h_right_1"}),
        ),
    )


def access_boundary_coarsening(system: D1GaugeSystem) -> D1GaugeSystem:
    return replace(
        system,
        name="access_boundary_coarsened_copy",
        boundary=replace(
            system.boundary,
            accessible_holders=frozenset(
                {
                    "h_left_1",
                    "h_left_2",
                    "h_right_1",
                    "h_right_2",
                    "h_aux",
                }
            ),
        ),
    )


def negative_record_incidence_break(system: D1GaugeSystem) -> D1GaugeSystem:
    return replace(
        system,
        name="negative_record_incidence_break",
        records=tuple(
            replace(record, event="left_archive", holder="h_left_1")
            if record.record_id in {"r_right_1", "r_right_2"}
            else record
            for record in system.records
        ),
    )


def negative_holder_partition_merge(system: D1GaugeSystem) -> D1GaugeSystem:
    return replace(
        system,
        name="negative_holder_partition_merge",
        holder_independence={
            holder: "merged_family" for holder in system.holder_independence
        },
    )


def negative_causal_graph_nonisomorphism(system: D1GaugeSystem) -> D1GaugeSystem:
    return replace(
        system,
        name="negative_causal_graph_nonisomorphism",
        causal_edges=system.causal_edges + (("left_archive", "right"),),
    )


def transformation_specs(system: D1GaugeSystem | None = None) -> tuple[TransformationSpec, ...]:
    base = system or reference_system()
    return (
        _spec(
            base,
            "observer_relabeling",
            observer_relabeling,
            "observer_relabeling",
            True,
            True,
            "Rename only the observer index attached to the same access boundary.",
            "Transport the observer index by bijection; D1 numeric components are unchanged.",
        ),
        _spec(
            base,
            "record_label_permutation",
            record_label_permutation,
            "record_label_permutation",
            True,
            True,
            "Permute record identifiers while preserving record-event and record-holder incidence.",
            "Transport record ids by bijection; incidence and accessibility predicates are unchanged.",
        ),
        _spec(
            base,
            "holder_relabeling_preserving_independence_partitions",
            holder_relabeling_preserving_partitions,
            "holder_relabeling",
            True,
            True,
            "Rename holder identifiers while preserving the independence partition and observer access set.",
            "Transport holder ids by bijection and carry the same independence classes.",
        ),
        _spec(
            base,
            "causal_graph_isomorphism",
            causal_graph_isomorphism,
            "causal_graph_isomorphism",
            True,
            True,
            "Rename causal events through a graph isomorphism preserving reachability.",
            "Transport events by graph isomorphism; antichain width is computed after pushforward.",
        ),
        _spec(
            base,
            "access_boundary_refinement",
            access_boundary_refinement,
            "access_boundary_refinement",
            True,
            False,
            "Restrict the observer access boundary to one holder from each visible branch.",
            "Recompute D1 on the refined access boundary. Value changes are boundary data, not gauge.",
        ),
        _spec(
            base,
            "access_boundary_coarsening",
            access_boundary_coarsening,
            "access_boundary_coarsening",
            True,
            False,
            "Expand the observer access boundary to include an auxiliary independent branch.",
            "Recompute D1 on the coarsened access boundary. Value changes are boundary data, not gauge.",
        ),
        _spec(
            base,
            "negative_record_incidence_break",
            negative_record_incidence_break,
            "negative_control",
            False,
            False,
            "Move a right-branch record onto the left branch without an incidence-preserving map.",
            "No transport rule: the transformation is outside the admissible action.",
            "Breaks record-event and record-holder incidence, so relabeling invariance is not applicable.",
        ),
        _spec(
            base,
            "negative_holder_partition_merge",
            negative_holder_partition_merge,
            "negative_control",
            False,
            False,
            "Merge all holder independence classes without an admissible partition map.",
            "No transport rule: the transformation is outside the admissible action.",
            "Breaks the independence partition required by holder relabeling.",
        ),
        _spec(
            base,
            "negative_causal_graph_nonisomorphism",
            negative_causal_graph_nonisomorphism,
            "negative_control",
            False,
            False,
            "Add a causal edge that serializes the left and right branches.",
            "No transport rule: the transformation is outside the admissible action.",
            "Breaks causal-graph isomorphism and reachability preservation.",
        ),
    )


def audit_transformation(
    reference: D1GaugeSystem,
    spec: TransformationSpec,
) -> TransformationAudit:
    before = compute_profile(reference)
    after = compute_profile(spec.transformed_system)
    classifications = tuple(
        _classify_dimension(spec, before, after, dimension)
        for dimension in D1_DIMENSIONS
    )
    invariant_failures = tuple(
        dimension
        for dimension in D1_DIMENSIONS
        if getattr(before, dimension) != getattr(after, dimension)
    )
    verdict = _transformation_verdict(spec, invariant_failures)
    return TransformationAudit(
        name=spec.name,
        kind=spec.kind,
        admissible=spec.admissible,
        gauge_pure=spec.gauge_pure,
        before_profile=before,
        after_profile=after,
        classifications=classifications,
        invariant_failure_dimensions=invariant_failures,
        verdict=verdict,
    )


def run_t111_audit() -> T111GaugeAuditResult:
    base = reference_system()
    audits = tuple(
        audit_transformation(base, spec) for spec in transformation_specs(base)
    )
    summaries = tuple(_dimension_summary(dimension, audits) for dimension in D1_DIMENSIONS)
    return T111GaugeAuditResult(
        allowed_transformations=(
            "observer relabeling",
            "record-label permutation preserving incidence",
            "holder relabeling preserving independence partitions",
            "causal-graph isomorphism preserving reachability",
            "access-boundary refinement",
            "access-boundary coarsening",
        ),
        negative_controls=tuple(
            audit.name for audit in audits if not audit.admissible
        ),
        reference_profile=compute_profile(base),
        audits=audits,
        dimension_summaries=summaries,
        strongest_claim=(
            "All four tested D1 dimensions are invariant under pure finite "
            "relabeling/isomorphism gauge maps in the reference audit, and all "
            "four are covariant under explicit access-boundary refinement or "
            "coarsening. Boundary changes are observer-frame data, not gauge "
            "redundancy."
        ),
        guardrail=(
            "T111 supplies only an invariance/covariance entry condition for "
            "future finality-connection work. It gives no curvature, gravity, "
            "or anomaly-cancellation upgrade."
        ),
        recommendation=(
            "Use the four D1 components as transportable boundary-indexed "
            "profile coordinates under the stated finite maps. Do not treat "
            "values across different access boundaries as one gauge-invariant "
            "physical scalar, and keep branch support and graph reversal count "
            "at formal status until separate physical reductions are supplied."
        ),
    )


def run_t111_analysis() -> dict[str, Any]:
    return t111_result_to_dict(run_t111_audit())


def t111_result_to_dict(result: T111GaugeAuditResult) -> dict[str, Any]:
    return {
        "allowed_transformations": list(result.allowed_transformations),
        "negative_controls": list(result.negative_controls),
        "reference_profile": _profile_to_dict(result.reference_profile),
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "dimension_summaries": [
            asdict(summary) for summary in result.dimension_summaries
        ],
        "strongest_claim": result.strongest_claim,
        "guardrail": result.guardrail,
        "recommendation": result.recommendation,
        "verdict": {
            "pure_gauge_maps_preserve_all_d1_dimensions": all(
                not audit.invariant_failure_dimensions
                for audit in result.audits
                if audit.admissible and audit.gauge_pure
            ),
            "boundary_maps_are_not_treated_as_gauge": all(
                not audit.gauge_pure
                and all(
                    item.classification == "covariant"
                    for item in audit.classifications
                )
                for audit in result.audits
                if audit.kind in BOUNDARY_KINDS
            ),
            "negative_controls_change_alleged_invariants": any(
                audit.invariant_failure_dimensions
                for audit in result.audits
                if not audit.admissible
            ),
            "no_curvature_gravity_or_anomaly_claim": True,
        },
    }


def is_ancestor(system: D1GaugeSystem, earlier: str, later: str) -> bool:
    if earlier == later:
        return True
    successors = _successors(system)
    pending = list(successors.get(earlier, ()))
    seen: set[str] = set()
    while pending:
        event = pending.pop()
        if event == later:
            return True
        if event not in seen:
            seen.add(event)
            pending.extend(successors.get(event, ()))
    return False


def _spec(
    base: D1GaugeSystem,
    name: str,
    transform: Callable[[D1GaugeSystem], D1GaugeSystem],
    kind: str,
    admissible: bool,
    gauge_pure: bool,
    description: str,
    transport_rule: str,
    negative_control_reason: str = "",
) -> TransformationSpec:
    return TransformationSpec(
        name=name,
        kind=kind,
        admissible=admissible,
        gauge_pure=gauge_pure,
        description=description,
        transformed_system=transform(base),
        transport_rule=transport_rule,
        negative_control_reason=negative_control_reason,
    )


def _classify_dimension(
    spec: TransformationSpec,
    before: D1GaugeProfile,
    after: D1GaugeProfile,
    dimension: str,
) -> DimensionClassification:
    before_value = getattr(before, dimension)
    after_value = getattr(after, dimension)
    if not spec.admissible:
        classification = "undefined"
        reason = spec.negative_control_reason
    elif spec.kind in PURE_GAUGE_KINDS:
        classification = "invariant" if before_value == after_value else "gauge-dependent"
        reason = (
            "value is unchanged under the stated gauge map"
            if before_value == after_value
            else "value changed under a map claimed as gauge, so it is not gauge-invariant"
        )
    elif spec.kind in BOUNDARY_KINDS:
        classification = "covariant"
        reason = (
            "value is recomputed on a different access boundary; the change is "
            "observer-frame boundary data, not gauge"
        )
    else:
        classification = "undefined"
        reason = "unrecognized transformation kind"
    return DimensionClassification(
        transformation=spec.name,
        dimension=dimension,
        classification=classification,
        before_value=before_value,
        after_value=after_value,
        transport_rule=spec.transport_rule,
        reason=reason,
    )


def _dimension_summary(
    dimension: str,
    audits: tuple[TransformationAudit, ...],
) -> DimensionSummary:
    pure = [
        item
        for audit in audits
        if audit.admissible and audit.gauge_pure
        for item in audit.classifications
        if item.dimension == dimension
    ]
    boundary = [
        item
        for audit in audits
        if audit.admissible and audit.kind in BOUNDARY_KINDS
        for item in audit.classifications
        if item.dimension == dimension
    ]
    negative_failures = tuple(
        audit.name
        for audit in audits
        if not audit.admissible and dimension in audit.invariant_failure_dimensions
    )
    pure_classification = (
        "invariant"
        if pure and all(item.classification == "invariant" for item in pure)
        else "gauge-dependent"
    )
    boundary_classification = (
        "covariant"
        if boundary and all(item.classification == "covariant" for item in boundary)
        else "undefined"
    )
    formal_only = dimension in {
        "causal_branch_support",
        "graph_reversal_count",
    }
    return DimensionSummary(
        dimension=dimension,
        pure_gauge_classification=pure_classification,
        boundary_classification=boundary_classification,
        negative_control_failures=negative_failures,
        future_connection_status=(
            "eligible only as a boundary-indexed transported coordinate"
        ),
        observable_status=(
            "formal-only in current physical claims"
            if formal_only
            else "conditionally observable once the access boundary and partition are declared"
        ),
    )


def _transformation_verdict(
    spec: TransformationSpec,
    invariant_failures: tuple[str, ...],
) -> str:
    if not spec.admissible:
        return (
            "negative control changed D1 dimensions without an admissible transport rule"
            if invariant_failures
            else "negative control happened not to change this finite profile"
        )
    if spec.gauge_pure:
        return (
            "pure gauge transformation preserved all D1 dimensions"
            if not invariant_failures
            else "claimed gauge transformation exposed gauge-dependent D1 data"
        )
    return "access-boundary transformation is covariant physical boundary data, not pure gauge"


def _successors(system: D1GaugeSystem) -> dict[str, set[str]]:
    successors = {event: set() for event in system.events}
    for earlier, later in system.causal_edges:
        successors.setdefault(earlier, set()).add(later)
        successors.setdefault(later, set())
    return successors


def _has_cycle(system: D1GaugeSystem) -> bool:
    successors = _successors(system)
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(event: str) -> bool:
        if event in visiting:
            return True
        if event in visited:
            return False
        visiting.add(event)
        for later in successors.get(event, ()):
            if visit(later):
                return True
        visiting.remove(event)
        visited.add(event)
        return False

    return any(visit(event) for event in successors)


def _antichain_width(system: D1GaugeSystem, events: tuple[str, ...]) -> int:
    unique_events = tuple(sorted(set(events)))
    for size in range(len(unique_events), 0, -1):
        for subset in combinations(unique_events, size):
            if all(
                not is_ancestor(system, left, right)
                and not is_ancestor(system, right, left)
                for left, right in combinations(subset, 2)
            ):
                return size
    return 0


def _profile_to_dict(profile: D1GaugeProfile) -> dict[str, Any]:
    return asdict(profile) | {
        "tuple_order": list(D1_DIMENSIONS),
        "profile_tuple": list(profile.as_tuple()),
    }


def _audit_to_dict(audit: TransformationAudit) -> dict[str, Any]:
    return {
        "name": audit.name,
        "kind": audit.kind,
        "admissible": audit.admissible,
        "gauge_pure": audit.gauge_pure,
        "before_profile": _profile_to_dict(audit.before_profile),
        "after_profile": _profile_to_dict(audit.after_profile),
        "classifications": [
            asdict(classification) for classification in audit.classifications
        ],
        "invariant_failure_dimensions": list(audit.invariant_failure_dimensions),
        "verdict": audit.verdict,
    }
