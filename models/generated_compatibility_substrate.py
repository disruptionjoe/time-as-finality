"""T378: generated shared-compatibility substrate fixture.

T377 showed that a fixed no-time-column u/v table can render observer-relative
coordinates with a shared interval-like invariant. This fixture removes the
stored u_rank/v_rank source columns. It generates a finite shared substrate from
local compatibility-channel edges, derives rank-like lineage counts from paths,
and then runs the same relativistic rendering checks.

The honest boundary is important: this weakens the explicit fixed-table
absorber, but a finite deterministic generator rule can still be expanded into a
completed table.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


LEFT_CHANNEL = "left_compatibility"
RIGHT_CHANNEL = "right_compatibility"
CHANNEL_STEPS = {
    LEFT_CHANNEL: (1, 0),
    RIGHT_CHANNEL: (0, 1),
}

FORBIDDEN_SOURCE_COLUMNS = frozenset(
    {
        "t",
        "time",
        "timestamp",
        "x",
        "space",
        "metric",
        "interval",
        "proper_time",
        "u",
        "v",
        "u_rank",
        "v_rank",
        "rank_u",
        "rank_v",
        "left_rank",
        "right_rank",
        "coord_time",
        "coord_space",
    }
)

LANDMARK_RANKS = {
    "origin": (0, 0),
    "near": (1, 1),
    "left_only": (3, 0),
    "right_only": (0, 3),
    "future": (3, 3),
    "far": (5, 5),
}


@dataclass(frozen=True)
class GeneratedRecord:
    record_id: str
    parents: tuple[str, ...] = ()


@dataclass(frozen=True)
class CompatibilityEdge:
    parent_id: str
    child_id: str
    channel: str


@dataclass(frozen=True)
class GeneratedCompatibilitySubstrate:
    records: tuple[GeneratedRecord, ...]
    edges: tuple[CompatibilityEdge, ...]
    generation_rule: str = "local_two_channel_commuting_closure"
    source_columns: tuple[str, ...] = (
        "record_id",
        "parents",
        "incoming_compatibility_channels",
    )

    def by_id(self) -> dict[str, GeneratedRecord]:
        return {record.record_id: record for record in self.records}

    def incoming_edges_by_child(self) -> dict[str, tuple[CompatibilityEdge, ...]]:
        grouped: dict[str, list[CompatibilityEdge]] = {
            record.record_id: [] for record in self.records
        }
        for edge in self.edges:
            grouped.setdefault(edge.child_id, []).append(edge)
        return {
            child_id: tuple(sorted(edges, key=lambda edge: (edge.channel, edge.parent_id)))
            for child_id, edges in grouped.items()
        }


@dataclass(frozen=True)
class ObserverRender:
    observer_id: str
    left_scale: Fraction


@dataclass(frozen=True)
class RenderedGeneratedRecord:
    observer_id: str
    record_id: str
    derived_left: int
    derived_right: int
    rendered_left: Fraction
    rendered_right: Fraction
    coord_time: Fraction
    coord_space: Fraction


@dataclass(frozen=True)
class ObserverInterval:
    observer_id: str
    interval: Fraction


@dataclass(frozen=True)
class PairInvariant:
    left_id: str
    right_id: str
    derived_interval: int
    observer_intervals: tuple[ObserverInterval, ...]
    causal_relation: str


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T378Result:
    substrate_valid: bool
    source_schema_has_no_rank_or_time_columns: bool
    source_rows_have_no_rank_or_time_fields: bool
    path_independent_rank_derivation: bool
    append_order_independent: bool
    rendered_interval_invariant: bool
    simultaneity_disagreement: bool
    simultaneity_pair: tuple[str, str]
    simultaneity_same_observers: tuple[str, ...]
    simultaneity_different_observers: tuple[str, ...]
    causal_order_only_sufficient: bool
    record_count: int
    edge_count: int
    observer_count: int
    checked_pair_count: int
    sample_pair_invariants: tuple[PairInvariant, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str


def generate_compatibility_substrate(
    left_steps: int = 5,
    right_steps: int = 5,
) -> GeneratedCompatibilitySubstrate:
    """Generate a finite substrate by local two-channel compatibility closure.

    Coordinates are used only as construction scaffolding. The exported source
    rows contain record ids, parent ids, and local incoming compatibility
    channels; rank-like values are reconstructed later from path counts.
    """

    if left_steps < 1 or right_steps < 1:
        raise ValueError("left_steps and right_steps must be positive")

    coord_to_id: dict[tuple[int, int], str] = {}
    ordered_coords: list[tuple[int, int]] = []
    counter = 0
    for depth in range(left_steps + right_steps + 1):
        left_min = max(0, depth - right_steps)
        left_max = min(left_steps, depth)
        for left in range(left_min, left_max + 1):
            right = depth - left
            coord_to_id[(left, right)] = f"r{counter:02d}"
            ordered_coords.append((left, right))
            counter += 1

    records: list[GeneratedRecord] = []
    edges: list[CompatibilityEdge] = []
    for left, right in ordered_coords:
        child_id = coord_to_id[(left, right)]
        parents: list[str] = []
        if left > 0:
            parent_id = coord_to_id[(left - 1, right)]
            parents.append(parent_id)
            edges.append(
                CompatibilityEdge(
                    parent_id=parent_id,
                    child_id=child_id,
                    channel=LEFT_CHANNEL,
                )
            )
        if right > 0:
            parent_id = coord_to_id[(left, right - 1)]
            parents.append(parent_id)
            edges.append(
                CompatibilityEdge(
                    parent_id=parent_id,
                    child_id=child_id,
                    channel=RIGHT_CHANNEL,
                )
            )
        records.append(GeneratedRecord(record_id=child_id, parents=tuple(parents)))

    return GeneratedCompatibilitySubstrate(records=tuple(records), edges=tuple(edges))


def canonical_observers() -> tuple[ObserverRender, ...]:
    return (
        ObserverRender("A_rest", Fraction(1, 1)),
        ObserverRender("B_boost_2", Fraction(2, 1)),
        ObserverRender("C_boost_half", Fraction(1, 2)),
        ObserverRender("D_boost_three_halves", Fraction(3, 2)),
    )


def source_rows(
    substrate: GeneratedCompatibilitySubstrate,
) -> tuple[dict[str, object], ...]:
    incoming = substrate.incoming_edges_by_child()
    rows: list[dict[str, object]] = []
    for record in substrate.records:
        rows.append(
            {
                "record_id": record.record_id,
                "parents": record.parents,
                "incoming_compatibility_channels": tuple(
                    edge.channel for edge in incoming[record.record_id]
                ),
            }
        )
    return tuple(rows)


def validate_substrate(substrate: GeneratedCompatibilitySubstrate) -> bool:
    records = substrate.by_id()
    if len(records) != len(substrate.records):
        return False

    incoming = substrate.incoming_edges_by_child()
    root_count = 0
    for record in substrate.records:
        if record.record_id not in incoming:
            return False
        if not record.parents:
            root_count += 1
        edge_parents = tuple(edge.parent_id for edge in incoming[record.record_id])
        if sorted(record.parents) != sorted(edge_parents):
            return False

    for edge in substrate.edges:
        if edge.channel not in CHANNEL_STEPS:
            return False
        if edge.parent_id not in records or edge.child_id not in records:
            return False

    return root_count == 1


def source_schema_has_no_rank_or_time_columns(
    substrate: GeneratedCompatibilitySubstrate,
) -> bool:
    return not (set(substrate.source_columns) & FORBIDDEN_SOURCE_COLUMNS)


def source_rows_have_no_rank_or_time_fields(
    substrate: GeneratedCompatibilitySubstrate,
) -> bool:
    return all(not (set(row) & FORBIDDEN_SOURCE_COLUMNS) for row in source_rows(substrate))


def derived_rank_sets(
    substrate: GeneratedCompatibilitySubstrate,
) -> dict[str, frozenset[tuple[int, int]]]:
    incoming = substrate.incoming_edges_by_child()
    record_ids = set(substrate.by_id())
    memo: dict[str, frozenset[tuple[int, int]]] = {}
    visiting: set[str] = set()

    def walk(record_id: str) -> frozenset[tuple[int, int]]:
        if record_id not in record_ids:
            raise ValueError(f"unknown record id: {record_id}")
        if record_id in memo:
            return memo[record_id]
        if record_id in visiting:
            raise ValueError(f"cycle detected at record id: {record_id}")

        visiting.add(record_id)
        edges = incoming[record_id]
        if not edges:
            ranks = frozenset({(0, 0)})
        else:
            rank_values: set[tuple[int, int]] = set()
            for edge in edges:
                left_step, right_step = CHANNEL_STEPS[edge.channel]
                for left_rank, right_rank in walk(edge.parent_id):
                    rank_values.add(
                        (left_rank + left_step, right_rank + right_step)
                    )
            ranks = frozenset(rank_values)
        visiting.remove(record_id)
        memo[record_id] = ranks
        return ranks

    return {record.record_id: walk(record.record_id) for record in substrate.records}


def path_independent_rank_derivation(
    substrate: GeneratedCompatibilitySubstrate,
) -> bool:
    return all(len(ranks) == 1 for ranks in derived_rank_sets(substrate).values())


def derived_ranks(substrate: GeneratedCompatibilitySubstrate) -> dict[str, tuple[int, int]]:
    ranks_by_record = derived_rank_sets(substrate)
    non_unique = [
        record_id for record_id, rank_values in ranks_by_record.items() if len(rank_values) != 1
    ]
    if non_unique:
        raise ValueError(f"non-unique rank derivation for records: {non_unique}")
    return {
        record_id: next(iter(rank_values))
        for record_id, rank_values in ranks_by_record.items()
    }


def landmark_ids(substrate: GeneratedCompatibilitySubstrate) -> dict[str, str]:
    ranks = derived_ranks(substrate)
    by_rank = {rank: record_id for record_id, rank in ranks.items()}
    return {
        label: by_rank[rank]
        for label, rank in LANDMARK_RANKS.items()
        if rank in by_rank
    }


def reversed_order_substrate(
    substrate: GeneratedCompatibilitySubstrate,
) -> GeneratedCompatibilitySubstrate:
    return GeneratedCompatibilitySubstrate(
        records=tuple(reversed(substrate.records)),
        edges=tuple(reversed(substrate.edges)),
        generation_rule=substrate.generation_rule,
        source_columns=substrate.source_columns,
    )


def append_order_independent(substrate: GeneratedCompatibilitySubstrate) -> bool:
    return derived_ranks(substrate) == derived_ranks(reversed_order_substrate(substrate))


def render_record(
    record_id: str,
    ranks: dict[str, tuple[int, int]],
    observer: ObserverRender,
) -> RenderedGeneratedRecord:
    derived_left, derived_right = ranks[record_id]
    rendered_left = observer.left_scale * derived_left
    rendered_right = Fraction(derived_right, 1) / observer.left_scale
    return RenderedGeneratedRecord(
        observer_id=observer.observer_id,
        record_id=record_id,
        derived_left=derived_left,
        derived_right=derived_right,
        rendered_left=rendered_left,
        rendered_right=rendered_right,
        coord_time=(rendered_left + rendered_right) / 2,
        coord_space=(rendered_left - rendered_right) / 2,
    )


def derived_interval(
    left_id: str,
    right_id: str,
    ranks: dict[str, tuple[int, int]],
) -> int:
    left_left, left_right = ranks[left_id]
    right_left, right_right = ranks[right_id]
    return (right_left - left_left) * (right_right - left_right)


def rendered_interval(
    left_id: str,
    right_id: str,
    ranks: dict[str, tuple[int, int]],
    observer: ObserverRender,
) -> Fraction:
    left_rendered = render_record(left_id, ranks, observer)
    right_rendered = render_record(right_id, ranks, observer)
    dt = right_rendered.coord_time - left_rendered.coord_time
    dx = right_rendered.coord_space - left_rendered.coord_space
    return dt * dt - dx * dx


def causal_relation(
    left_id: str,
    right_id: str,
    ranks: dict[str, tuple[int, int]],
) -> str:
    left_left, left_right = ranks[left_id]
    right_left, right_right = ranks[right_id]
    d_left = right_left - left_left
    d_right = right_right - left_right
    if d_left == 0 and d_right == 0:
        return "same_record"
    if d_left >= 0 and d_right >= 0:
        return "future_or_null"
    if d_left <= 0 and d_right <= 0:
        return "past_or_null"
    return "spacelike"


def pair_invariants(
    substrate: GeneratedCompatibilitySubstrate,
    observers: tuple[ObserverRender, ...],
    record_ids: tuple[str, ...] | None = None,
) -> tuple[PairInvariant, ...]:
    ranks = derived_ranks(substrate)
    ids = record_ids if record_ids is not None else tuple(record.record_id for record in substrate.records)
    rows: list[PairInvariant] = []
    for left_id, right_id in combinations(ids, 2):
        rows.append(
            PairInvariant(
                left_id=left_id,
                right_id=right_id,
                derived_interval=derived_interval(left_id, right_id, ranks),
                observer_intervals=tuple(
                    ObserverInterval(
                        observer_id=observer.observer_id,
                        interval=rendered_interval(left_id, right_id, ranks, observer),
                    )
                    for observer in observers
                ),
                causal_relation=causal_relation(left_id, right_id, ranks),
            )
        )
    return tuple(rows)


def intervals_are_invariant(rows: tuple[PairInvariant, ...]) -> bool:
    return all(
        all(
            observer_interval.interval == Fraction(row.derived_interval, 1)
            for observer_interval in row.observer_intervals
        )
        for row in rows
    )


def simultaneity_disagreement(
    substrate: GeneratedCompatibilitySubstrate,
    observers: tuple[ObserverRender, ...],
) -> tuple[bool, tuple[str, str], tuple[str, ...], tuple[str, ...]]:
    ranks = derived_ranks(substrate)
    landmarks = landmark_ids(substrate)
    left_id = landmarks["left_only"]
    right_id = landmarks["right_only"]
    same: list[str] = []
    different: list[str] = []
    for observer in observers:
        left_rendered = render_record(left_id, ranks, observer)
        right_rendered = render_record(right_id, ranks, observer)
        if left_rendered.coord_time == right_rendered.coord_time:
            same.append(observer.observer_id)
        else:
            different.append(observer.observer_id)
    return bool(same and different), (left_id, right_id), tuple(same), tuple(different)


def causal_order_only_sufficient(rows: tuple[PairInvariant, ...]) -> bool:
    by_relation: dict[str, set[int]] = {}
    for row in rows:
        by_relation.setdefault(row.causal_relation, set()).add(row.derived_interval)
    return all(len(intervals) <= 1 for intervals in by_relation.values())


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            comparator_id="minkowski_first",
            status="not_imported",
            absorbs=False,
            reason=(
                "source rows contain no t/x/metric/interval fields; rendered coordinates and "
                "interval values are outputs of observer render maps over derived lineages"
            ),
        ),
        ComparatorVerdict(
            comparator_id="explicit_uv_rank_schema",
            status="rank_columns_removed",
            absorbs=False,
            reason=(
                "the exported source rows do not store u_rank/v_rank or left/right rank columns; "
                "rank-like values are reconstructed from local compatibility-channel paths"
            ),
        ),
        ComparatorVerdict(
            comparator_id="prewritten_completed_table",
            status="weakened_by_generation",
            absorbs=False,
            reason=(
                "the fixture no longer starts from the T377 completed rank table; it generates "
                "records by local parent/channel closure before reconstructing ranks"
            ),
        ),
        ComparatorVerdict(
            comparator_id="finite_closure_completion",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "because the generator is finite and deterministic, an adversary can still expand "
                "its closure into a completed compatibility table after the fact"
            ),
        ),
        ComparatorVerdict(
            comparator_id="fixed_generator_rule",
            status="still_absorbs",
            absorbs=True,
            reason=(
                "the two-channel commuting-closure rule and finite bounds are fixed; this is not "
                "yet a nonfixed compatibility law"
            ),
        ),
        ComparatorVerdict(
            comparator_id="hidden_append_order_or_foliation",
            status="not_required",
            absorbs=False,
            reason=(
                "derived ranks and interval recovery are graph/path properties and are unchanged "
                "when the exported record and edge order is reversed"
            ),
        ),
        ComparatorVerdict(
            comparator_id="causal_order_only",
            status="insufficient",
            absorbs=False,
            reason=(
                "records with the same causal relation can have different interval magnitudes, "
                "so causal comparability alone does not explain the invariant"
            ),
        ),
    )


def run_t378_analysis() -> T378Result:
    substrate = generate_compatibility_substrate()
    observers = canonical_observers()
    all_rows = pair_invariants(substrate, observers)
    landmarks = landmark_ids(substrate)
    sample_ids = tuple(landmarks[label] for label in LANDMARK_RANKS)
    sample_rows = pair_invariants(substrate, observers, sample_ids)
    simultaneity_ok, pair, same_observers, different_observers = (
        simultaneity_disagreement(substrate, observers)
    )
    causal_sufficient = causal_order_only_sufficient(all_rows)
    result_bits = {
        "substrate_valid": validate_substrate(substrate),
        "source_schema_has_no_rank_or_time_columns": (
            source_schema_has_no_rank_or_time_columns(substrate)
        ),
        "source_rows_have_no_rank_or_time_fields": (
            source_rows_have_no_rank_or_time_fields(substrate)
        ),
        "path_independent_rank_derivation": path_independent_rank_derivation(substrate),
        "append_order_independent": append_order_independent(substrate),
        "rendered_interval_invariant": intervals_are_invariant(all_rows),
        "simultaneity_disagreement": simultaneity_ok,
        "causal_order_only_sufficient": causal_sufficient,
    }
    rendered_success = (
        result_bits["substrate_valid"]
        and result_bits["source_schema_has_no_rank_or_time_columns"]
        and result_bits["source_rows_have_no_rank_or_time_fields"]
        and result_bits["path_independent_rank_derivation"]
        and result_bits["append_order_independent"]
        and result_bits["rendered_interval_invariant"]
        and result_bits["simultaneity_disagreement"]
        and not result_bits["causal_order_only_sufficient"]
    )
    return T378Result(
        substrate_valid=result_bits["substrate_valid"],
        source_schema_has_no_rank_or_time_columns=result_bits[
            "source_schema_has_no_rank_or_time_columns"
        ],
        source_rows_have_no_rank_or_time_fields=result_bits[
            "source_rows_have_no_rank_or_time_fields"
        ],
        path_independent_rank_derivation=result_bits[
            "path_independent_rank_derivation"
        ],
        append_order_independent=result_bits["append_order_independent"],
        rendered_interval_invariant=result_bits["rendered_interval_invariant"],
        simultaneity_disagreement=result_bits["simultaneity_disagreement"],
        simultaneity_pair=pair,
        simultaneity_same_observers=same_observers,
        simultaneity_different_observers=different_observers,
        causal_order_only_sufficient=result_bits["causal_order_only_sufficient"],
        record_count=len(substrate.records),
        edge_count=len(substrate.edges),
        observer_count=len(observers),
        checked_pair_count=len(all_rows),
        sample_pair_invariants=sample_rows,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict=(
            "generated_shared_substrate_recovers_relativism_but_fixed_rule_absorbed"
            if rendered_success
            else "fixture_failed"
        ),
        strongest_claim=(
            "A finite local compatibility generator with no source time/space/rank columns can "
            "derive path-independent lineage ranks from a shared substrate, after which multiple "
            "observers recover a common interval-like invariant while disagreeing on simultaneity. "
            "This removes T377's explicit rank table but not the fixed-rule or finite-closure "
            "absorbers."
        ),
        claim_ledger_update=(
            "Register T378 as a generated shared-substrate calibration. It is stronger than T377 "
            "against explicit u/v table absorption, but it remains a calibration because the "
            "generator law and finite closure are still fixed."
        ),
    )


def _pair_invariant_to_dict(row: PairInvariant) -> dict[str, object]:
    return {
        "left_id": row.left_id,
        "right_id": row.right_id,
        "derived_interval": row.derived_interval,
        "observer_intervals": [
            {
                "observer_id": observer_interval.observer_id,
                "interval": str(observer_interval.interval),
            }
            for observer_interval in row.observer_intervals
        ],
        "causal_relation": row.causal_relation,
    }


def t378_result_to_dict(result: T378Result) -> dict[str, object]:
    return {
        "substrate_valid": result.substrate_valid,
        "source_schema_has_no_rank_or_time_columns": (
            result.source_schema_has_no_rank_or_time_columns
        ),
        "source_rows_have_no_rank_or_time_fields": (
            result.source_rows_have_no_rank_or_time_fields
        ),
        "path_independent_rank_derivation": result.path_independent_rank_derivation,
        "append_order_independent": result.append_order_independent,
        "rendered_interval_invariant": result.rendered_interval_invariant,
        "simultaneity_disagreement": result.simultaneity_disagreement,
        "simultaneity_pair": list(result.simultaneity_pair),
        "simultaneity_same_observers": list(result.simultaneity_same_observers),
        "simultaneity_different_observers": list(result.simultaneity_different_observers),
        "causal_order_only_sufficient": result.causal_order_only_sufficient,
        "record_count": result.record_count,
        "edge_count": result.edge_count,
        "observer_count": result.observer_count,
        "checked_pair_count": result.checked_pair_count,
        "sample_pair_invariants": [
            _pair_invariant_to_dict(row) for row in result.sample_pair_invariants
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

    print(json.dumps(t378_result_to_dict(run_t378_analysis()), indent=2))
