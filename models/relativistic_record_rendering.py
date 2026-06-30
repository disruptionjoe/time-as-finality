"""T377: relativistic record-rendering fixture.

This fixture asks whether a finite record carrier with no primitive time column
can render two observer histories that disagree on simultaneity while preserving
an interval-like invariant. It also reports the absorber pressure: a finite,
fixed u/v carrier is still a fixed-schema / fixed-completed-table object.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


FORBIDDEN_SOURCE_COLUMNS = frozenset(
    {"t", "time", "timestamp", "x", "space", "metric", "interval", "proper_time"}
)


@dataclass(frozen=True)
class CarrierRecord:
    record_id: str
    u_rank: int
    v_rank: int
    parents: tuple[str, ...] = ()


@dataclass(frozen=True)
class RelativisticRecordCarrier:
    records: tuple[CarrierRecord, ...]
    source_columns: tuple[str, ...] = ("record_id", "u_rank", "v_rank", "parents")

    def by_id(self) -> dict[str, CarrierRecord]:
        return {record.record_id: record for record in self.records}


@dataclass(frozen=True)
class ObserverRender:
    observer_id: str
    u_scale: Fraction


@dataclass(frozen=True)
class RenderedRecord:
    observer_id: str
    record_id: str
    rendered_u: Fraction
    rendered_v: Fraction
    coord_time: Fraction
    coord_space: Fraction


@dataclass(frozen=True)
class PairInvariant:
    left_id: str
    right_id: str
    carrier_interval: int
    observer_a_interval: Fraction
    observer_b_interval: Fraction
    causal_relation: str


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T377Result:
    carrier_valid: bool
    no_primitive_time_column: bool
    rendered_interval_invariant: bool
    simultaneity_disagreement: bool
    simultaneity_pair: tuple[str, str]
    causal_order_only_sufficient: bool
    pair_invariants: tuple[PairInvariant, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str


def canonical_carrier() -> RelativisticRecordCarrier:
    """Return a small finite 1+1 carrier in lightlike propagation ranks.

    The source rows have no t/x fields. The u/v ranks are propagation lineages.
    Rendered observers may later turn them into time/space coordinates.
    """

    return RelativisticRecordCarrier(
        records=(
            CarrierRecord("origin", 0, 0),
            CarrierRecord("near", 1, 1, ("origin",)),
            CarrierRecord("u_only", 3, 0, ("origin",)),
            CarrierRecord("v_only", 0, 3, ("origin",)),
            CarrierRecord("future", 3, 3, ("near", "u_only", "v_only")),
            CarrierRecord("far", 5, 5, ("future",)),
        )
    )


def canonical_observers() -> tuple[ObserverRender, ObserverRender]:
    return (
        ObserverRender("A", Fraction(1, 1)),
        ObserverRender("B", Fraction(2, 1)),
    )


def validate_carrier(carrier: RelativisticRecordCarrier) -> bool:
    records = carrier.by_id()
    if len(records) != len(carrier.records):
        return False
    for record in carrier.records:
        if record.u_rank < 0 or record.v_rank < 0:
            return False
        for parent_id in record.parents:
            parent = records.get(parent_id)
            if parent is None:
                return False
            if parent.u_rank > record.u_rank or parent.v_rank > record.v_rank:
                return False
    return True


def has_no_primitive_time_column(carrier: RelativisticRecordCarrier) -> bool:
    return not (set(carrier.source_columns) & FORBIDDEN_SOURCE_COLUMNS)


def carrier_interval(left: CarrierRecord, right: CarrierRecord) -> int:
    return (right.u_rank - left.u_rank) * (right.v_rank - left.v_rank)


def causal_relation(left: CarrierRecord, right: CarrierRecord) -> str:
    du = right.u_rank - left.u_rank
    dv = right.v_rank - left.v_rank
    if du == 0 and dv == 0:
        return "same_record"
    if du >= 0 and dv >= 0:
        return "future_or_null"
    if du <= 0 and dv <= 0:
        return "past_or_null"
    return "spacelike"


def render_record(record: CarrierRecord, observer: ObserverRender) -> RenderedRecord:
    rendered_u = observer.u_scale * record.u_rank
    rendered_v = Fraction(record.v_rank, 1) / observer.u_scale
    return RenderedRecord(
        observer_id=observer.observer_id,
        record_id=record.record_id,
        rendered_u=rendered_u,
        rendered_v=rendered_v,
        coord_time=(rendered_u + rendered_v) / 2,
        coord_space=(rendered_u - rendered_v) / 2,
    )


def rendered_interval(
    left: CarrierRecord,
    right: CarrierRecord,
    observer: ObserverRender,
) -> Fraction:
    left_rendered = render_record(left, observer)
    right_rendered = render_record(right, observer)
    dt = right_rendered.coord_time - left_rendered.coord_time
    dx = right_rendered.coord_space - left_rendered.coord_space
    return dt * dt - dx * dx


def pair_invariants(
    carrier: RelativisticRecordCarrier,
    observers: tuple[ObserverRender, ObserverRender],
) -> tuple[PairInvariant, ...]:
    first, second = observers
    return tuple(
        PairInvariant(
            left_id=left.record_id,
            right_id=right.record_id,
            carrier_interval=carrier_interval(left, right),
            observer_a_interval=rendered_interval(left, right, first),
            observer_b_interval=rendered_interval(left, right, second),
            causal_relation=causal_relation(left, right),
        )
        for left, right in combinations(carrier.records, 2)
    )


def intervals_are_invariant(rows: tuple[PairInvariant, ...]) -> bool:
    return all(
        row.observer_a_interval
        == row.observer_b_interval
        == Fraction(row.carrier_interval, 1)
        for row in rows
    )


def simultaneity_disagreement(
    carrier: RelativisticRecordCarrier,
    observers: tuple[ObserverRender, ObserverRender],
) -> tuple[bool, tuple[str, str]]:
    first, second = observers
    records = carrier.by_id()
    candidate_pairs = (("u_only", "v_only"),)
    for left_id, right_id in candidate_pairs:
        left = records[left_id]
        right = records[right_id]
        left_first = render_record(left, first)
        right_first = render_record(right, first)
        left_second = render_record(left, second)
        right_second = render_record(right, second)
        if (
            left_first.coord_time == right_first.coord_time
            and left_second.coord_time != right_second.coord_time
        ):
            return True, (left_id, right_id)
    return False, ("", "")


def causal_order_only_sufficient(rows: tuple[PairInvariant, ...]) -> bool:
    """Return whether causal comparability alone determines interval magnitude."""

    by_relation: dict[str, set[int]] = {}
    for row in rows:
        by_relation.setdefault(row.causal_relation, set()).add(row.carrier_interval)
    return all(len(intervals) <= 1 for intervals in by_relation.values())


def comparator_verdicts(result_bits: dict[str, bool]) -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            comparator_id="minkowski_first",
            status="not_imported_but_null_rank_caveat",
            absorbs=False,
            reason=(
                "source rows contain no t/x/metric fields; rendered coordinates are outputs, "
                "though the u/v rank structure is mathematically lightlike after rendering"
            ),
        ),
        ComparatorVerdict(
            comparator_id="fixed_schema_log",
            status="fixed_carrier_schema_absorbs",
            absorbs=True,
            reason=(
                "the finite source schema fixes u_rank, v_rank, and the interval product rule; "
                "this is stronger than an ordinary append log but still a fixed schema"
            ),
        ),
        ComparatorVerdict(
            comparator_id="fixed_completed_table",
            status="finite_completed_table_absorbs",
            absorbs=True,
            reason=(
                "the finite carrier can be pre-enumerated, so the shared substrate can be read "
                "as a completed compatibility table rather than a live compatibility generator"
            ),
        ),
        ComparatorVerdict(
            comparator_id="hidden_preferred_foliation",
            status="not_required",
            absorbs=False,
            reason=(
                "interval agreement and simultaneity disagreement are computed from u/v ranks and "
                "observer scaling; no single global total order is used"
            ),
        ),
        ComparatorVerdict(
            comparator_id="causal_order_only",
            status="insufficient",
            absorbs=False,
            reason=(
                "causal comparability does not determine interval magnitude; the same relation "
                "contains multiple interval values"
            ),
        ),
        ComparatorVerdict(
            comparator_id="t376_fixed_admissibility",
            status="guardrail_triggers",
            absorbs=True,
            reason=(
                "compatibility and interval admissibility are fixed in this v0.1 fixture, so the "
                "result is reconstruction-layer evidence only"
            ),
        ),
    )


def run_t377_analysis() -> T377Result:
    carrier = canonical_carrier()
    observers = canonical_observers()
    rows = pair_invariants(carrier, observers)
    simultaneity_ok, simultaneity_pair = simultaneity_disagreement(carrier, observers)
    causal_sufficient = causal_order_only_sufficient(rows)
    result_bits = {
        "carrier_valid": validate_carrier(carrier),
        "no_primitive_time_column": has_no_primitive_time_column(carrier),
        "rendered_interval_invariant": intervals_are_invariant(rows),
        "simultaneity_disagreement": simultaneity_ok,
        "causal_order_only_sufficient": causal_sufficient,
    }
    fixed_absorbed = True
    rendered_success = (
        result_bits["carrier_valid"]
        and result_bits["no_primitive_time_column"]
        and result_bits["rendered_interval_invariant"]
        and result_bits["simultaneity_disagreement"]
        and not result_bits["causal_order_only_sufficient"]
    )
    return T377Result(
        carrier_valid=result_bits["carrier_valid"],
        no_primitive_time_column=result_bits["no_primitive_time_column"],
        rendered_interval_invariant=result_bits["rendered_interval_invariant"],
        simultaneity_disagreement=result_bits["simultaneity_disagreement"],
        simultaneity_pair=simultaneity_pair,
        causal_order_only_sufficient=result_bits["causal_order_only_sufficient"],
        pair_invariants=rows,
        comparator_verdicts=comparator_verdicts(result_bits),
        overall_verdict=(
            "rendered_interval_recovered_but_fixed_carrier_absorbed"
            if rendered_success and fixed_absorbed
            else "fixture_failed"
        ),
        strongest_claim=(
            "A finite no-time-column u/v compatibility substrate can render two observer "
            "coordinate histories with different simultaneity slices and the same interval-like "
            "invariant; however the fixed carrier schema and finite completed-table absorbers "
            "still fire."
        ),
        claim_ledger_update=(
            "Register T377 as a relativistic compatibility-substrate calibration, not a temporal "
            "issuance result and not a claim upgrade. It supports the shared-substrate question "
            "but does not defeat fixed-schema or fixed-completed-table absorption."
        ),
    )


def t377_result_to_dict(result: T377Result) -> dict[str, object]:
    return {
        "carrier_valid": result.carrier_valid,
        "no_primitive_time_column": result.no_primitive_time_column,
        "rendered_interval_invariant": result.rendered_interval_invariant,
        "simultaneity_disagreement": result.simultaneity_disagreement,
        "simultaneity_pair": list(result.simultaneity_pair),
        "causal_order_only_sufficient": result.causal_order_only_sufficient,
        "pair_invariants": [
            {
                "left_id": row.left_id,
                "right_id": row.right_id,
                "carrier_interval": row.carrier_interval,
                "observer_a_interval": str(row.observer_a_interval),
                "observer_b_interval": str(row.observer_b_interval),
                "causal_relation": row.causal_relation,
            }
            for row in result.pair_invariants
        ],
        "comparator_verdicts": [
            {
                "comparator_id": verdict.comparator_id,
                "status": verdict.status,
                "absorbs": verdict.absorbs,
                "reason": verdict.reason,
            }
            for verdict in result.comparator_verdicts
        ],
        "overall_verdict": result.overall_verdict,
        "strongest_claim": result.strongest_claim,
        "claim_ledger_update": result.claim_ledger_update,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t377_result_to_dict(run_t377_analysis()), indent=2))
