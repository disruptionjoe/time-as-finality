"""Recursive composition laboratory for observer-indexed record finality.

The model separates an underlying evidence join from observer-facing
finality profiles. "Epigenetic" structure is operationalized narrowly as
inherited, context-dependent expression marks over immutable record identity.
No fixed recursion depth or self-similar geometry is assumed.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import combinations, product
from math import inf
from random import Random
from typing import Iterable, Literal, Mapping


Value = str
CheckpointPolicy = Literal["lossy", "provenance"]


@dataclass(frozen=True, order=True)
class RecordToken:
    token_id: str
    provenance: frozenset[str]
    proposition: str
    value: Value
    holder: str
    branch: str
    reversal_cost: float = 1.0
    expression_tags: frozenset[str] = frozenset()
    assignment: tuple[tuple[str, Value], ...] = ()

    def __post_init__(self) -> None:
        if not self.token_id:
            raise ValueError("token id is required")
        if not self.provenance:
            raise ValueError("provenance cannot be empty")
        if self.reversal_cost < 0:
            raise ValueError("reversal cost must be non-negative")
        variables = [variable for variable, _ in self.assignment]
        if len(variables) != len(set(variables)):
            raise ValueError("an assignment cannot repeat a variable")


@dataclass(frozen=True, order=True)
class ExpressionMark:
    tag: str
    expressed: bool


@dataclass(frozen=True)
class RecursiveRecord:
    node_id: str
    tokens: tuple[RecordToken, ...] = ()
    children: tuple["RecursiveRecord", ...] = ()
    local_marks: tuple[ExpressionMark, ...] = ()

    def __post_init__(self) -> None:
        if not self.node_id:
            raise ValueError("node id is required")
        if len({token.token_id for token in self.tokens}) != len(self.tokens):
            raise ValueError("duplicate token id inside one node")


@dataclass(frozen=True)
class ObserverContext:
    accessible_holders: frozenset[str] | None = None
    inherited_marks: tuple[ExpressionMark, ...] = ()


@dataclass(frozen=True)
class FinalityProfile:
    accessible_support: int
    holder_redundancy: int
    branch_support: int
    reversal_cost: float

    def as_tuple(self) -> tuple[int, int, int, float]:
        return (
            self.accessible_support,
            self.holder_redundancy,
            self.branch_support,
            self.reversal_cost,
        )

    def no_more_final_than(self, other: "FinalityProfile") -> bool:
        return all(left <= right for left, right in zip(self.as_tuple(), other.as_tuple()))

    def componentwise_max(self, other: "FinalityProfile") -> "FinalityProfile":
        return FinalityProfile(
            accessible_support=max(self.accessible_support, other.accessible_support),
            holder_redundancy=max(self.holder_redundancy, other.holder_redundancy),
            branch_support=max(self.branch_support, other.branch_support),
            reversal_cost=max(self.reversal_cost, other.reversal_cost),
        )


@dataclass(frozen=True)
class Counterexample:
    name: str
    size: int
    detail: dict[str, object]


def leaf(
    token_id: str,
    proposition: str,
    value: Value,
    *,
    source_id: str | None = None,
    holder: str | None = None,
    branch: str | None = None,
    reversal_cost: float = 1.0,
    expression_tags: Iterable[str] = (),
    assignment: Mapping[str, Value] | None = None,
) -> RecursiveRecord:
    source = source_id or token_id
    token = RecordToken(
        token_id=token_id,
        provenance=frozenset({source}),
        proposition=proposition,
        value=value,
        holder=holder or f"holder-{token_id}",
        branch=branch or f"branch-{token_id}",
        reversal_cost=reversal_cost,
        expression_tags=frozenset(expression_tags),
        assignment=tuple(sorted((assignment or {}).items())),
    )
    return RecursiveRecord(node_id=f"node-{token_id}", tokens=(token,))


def compose(
    node_id: str,
    children: Iterable[RecursiveRecord],
    local_marks: Iterable[ExpressionMark] = (),
) -> RecursiveRecord:
    children = tuple(children)
    if not children:
        raise ValueError("composition requires at least one child")
    return RecursiveRecord(
        node_id=node_id,
        children=children,
        local_marks=tuple(local_marks),
    )


def _updated_marks(
    inherited: Mapping[str, bool],
    local_marks: Iterable[ExpressionMark],
) -> dict[str, bool]:
    result = dict(inherited)
    for mark in local_marks:
        result[mark.tag] = mark.expressed
    return result


def expressed_tokens(
    record: RecursiveRecord,
    observer: ObserverContext | None = None,
) -> tuple[RecordToken, ...]:
    observer = observer or ObserverContext()
    inherited = {mark.tag: mark.expressed for mark in observer.inherited_marks}
    tokens: dict[str, RecordToken] = {}
    pending: list[tuple[RecursiveRecord, Mapping[str, bool]]] = [(record, inherited)]
    while pending:
        node, marks = pending.pop()
        active_marks = _updated_marks(marks, node.local_marks)
        for token in node.tokens:
            if observer.accessible_holders is not None and token.holder not in observer.accessible_holders:
                continue
            if all(active_marks.get(tag, True) for tag in token.expression_tags):
                existing = tokens.get(token.token_id)
                if existing is not None and existing != token:
                    raise ValueError(f"token id {token.token_id!r} has conflicting definitions")
                tokens[token.token_id] = token
        for child in node.children:
            pending.append((child, active_marks))
    return tuple(sorted(tokens.values()))


def stored_tokens(record: RecursiveRecord) -> tuple[RecordToken, ...]:
    """Return immutable token identity without applying expression marks."""

    tokens: dict[str, RecordToken] = {}
    pending = [record]
    while pending:
        node = pending.pop()
        for token in node.tokens:
            existing = tokens.get(token.token_id)
            if existing is not None and existing != token:
                raise ValueError(f"token id {token.token_id!r} has conflicting definitions")
            tokens[token.token_id] = token
        pending.extend(node.children)
    return tuple(sorted(tokens.values()))


def evidence_join(
    *records: RecursiveRecord,
    observer: ObserverContext | None = None,
) -> frozenset[RecordToken]:
    """Canonical provenance-preserving join of visible token states."""

    tokens: dict[str, RecordToken] = {}
    for record in records:
        for token in expressed_tokens(record, observer):
            existing = tokens.get(token.token_id)
            if existing is not None and existing != token:
                raise ValueError(f"token id {token.token_id!r} has conflicting definitions")
            tokens[token.token_id] = token
    return frozenset(tokens.values())


def join_states(
    left: frozenset[RecordToken],
    right: frozenset[RecordToken],
) -> frozenset[RecordToken]:
    by_id = {token.token_id: token for token in left}
    for token in right:
        existing = by_id.get(token.token_id)
        if existing is not None and existing != token:
            raise ValueError(f"token id {token.token_id!r} has conflicting definitions")
        by_id[token.token_id] = token
    return frozenset(by_id.values())


def relevant_tokens(
    record: RecursiveRecord,
    proposition: str,
    value: Value,
    observer: ObserverContext | None = None,
) -> tuple[RecordToken, ...]:
    return tuple(
        token
        for token in expressed_tokens(record, observer)
        if token.proposition == proposition and token.value == value
    )


def provenance_support(tokens: Iterable[RecordToken]) -> frozenset[str]:
    return frozenset().union(*(token.provenance for token in tokens))


def minimum_reversal_cost(
    tokens: tuple[RecordToken, ...],
    threshold: int,
) -> float:
    if threshold < 1:
        raise ValueError("threshold must be positive")
    if len(provenance_support(tokens)) < threshold:
        return 0.0
    best = inf
    for size in range(1, len(tokens) + 1):
        for removed in combinations(tokens, size):
            removed_ids = {token.token_id for token in removed}
            remaining = tuple(token for token in tokens if token.token_id not in removed_ids)
            if len(provenance_support(remaining)) < threshold:
                best = min(best, sum(token.reversal_cost for token in removed))
    return best


def finality_profile(
    record: RecursiveRecord,
    proposition: str,
    value: Value,
    threshold: int,
    observer: ObserverContext | None = None,
) -> FinalityProfile:
    tokens = relevant_tokens(record, proposition, value, observer)
    return FinalityProfile(
        accessible_support=len(provenance_support(tokens)),
        holder_redundancy=len({token.holder for token in tokens}),
        branch_support=len({token.branch for token in tokens}),
        reversal_cost=minimum_reversal_cost(tokens, threshold),
    )


def reconstruct_value(
    record: RecursiveRecord,
    proposition: str,
    threshold: int,
    observer: ObserverContext | None = None,
) -> Value | None:
    values = sorted(
        {
            token.value
            for token in expressed_tokens(record, observer)
            if token.proposition == proposition
        }
    )
    winners = [
        value
        for value in values
        if finality_profile(record, proposition, value, threshold, observer).accessible_support
        >= threshold
    ]
    return winners[0] if len(winners) == 1 else None


def checkpoint(
    record: RecursiveRecord,
    checkpoint_id: str,
    proposition: str,
    threshold: int,
    policy: CheckpointPolicy,
    observer: ObserverContext | None = None,
    reversal_cost: float = 1.0,
) -> RecursiveRecord:
    value = reconstruct_value(record, proposition, threshold, observer)
    if value is None:
        raise ValueError("cannot checkpoint an unresolved proposition")
    supporting = relevant_tokens(record, proposition, value, observer)
    if policy == "lossy":
        provenance = frozenset({f"checkpoint-source:{checkpoint_id}"})
    elif policy == "provenance":
        provenance = provenance_support(supporting)
    else:
        raise ValueError(f"unknown checkpoint policy: {policy}")
    token = RecordToken(
        token_id=f"checkpoint:{checkpoint_id}",
        provenance=provenance,
        proposition=proposition,
        value=value,
        holder=f"checkpoint-holder:{checkpoint_id}",
        branch=f"checkpoint-branch:{checkpoint_id}",
        reversal_cost=reversal_cost,
    )
    return RecursiveRecord(node_id=f"checkpoint-node:{checkpoint_id}", tokens=(token,))


def nested(
    base: RecursiveRecord,
    depth: int,
    *,
    mark_at: int | None = None,
    mark: ExpressionMark | None = None,
) -> RecursiveRecord:
    """Wrap a record at arbitrary finite depth without assuming layer count."""

    if depth < 0:
        raise ValueError("depth cannot be negative")
    current = base
    for level in range(depth):
        marks = (mark,) if mark is not None and mark_at == level else ()
        current = compose(f"nested-{level}", (current,), marks)
    return current


def grouping_variants(records: tuple[RecursiveRecord, ...]) -> tuple[RecursiveRecord, ...]:
    if len(records) != 3:
        raise ValueError("grouping comparison currently requires three records")
    left = compose("left-root", (compose("left-pair", records[:2]), records[2]))
    right = compose("right-root", (records[0], compose("right-pair", records[1:])))
    flat = compose("flat-root", records)
    return left, right, flat


def assignments_compatible(tokens: Iterable[RecordToken]) -> bool:
    combined: dict[str, Value] = {}
    for token in tokens:
        for variable, value in token.assignment:
            if variable in combined and combined[variable] != value:
                return False
            combined[variable] = value
    return True


def local_contexts_glue(
    records: Iterable[RecursiveRecord],
    observer: ObserverContext | None = None,
) -> bool:
    return assignments_compatible(
        token
        for record in records
        for token in expressed_tokens(record, observer)
    )


def evidence_join_laws(states: tuple[frozenset[RecordToken], ...]) -> dict[str, bool]:
    commutative = all(
        join_states(left, right) == join_states(right, left)
        for left in states
        for right in states
    )
    associative = all(
        join_states(join_states(left, right), third)
        == join_states(left, join_states(right, third))
        for left in states
        for right in states
        for third in states
    )
    idempotent = all(join_states(state, state) == state for state in states)
    return {
        "commutative": commutative,
        "associative": associative,
        "idempotent": idempotent,
    }


def find_profile_join_counterexample() -> Counterexample:
    left = leaf("a", "P", "true")
    right = leaf("b", "P", "true")
    merged = compose("merged", (left, right))
    left_profile = finality_profile(left, "P", "true", threshold=1)
    right_profile = finality_profile(right, "P", "true", threshold=1)
    merged_profile = finality_profile(merged, "P", "true", threshold=1)
    expected_lub = left_profile.componentwise_max(right_profile)
    if merged_profile == expected_lub:
        raise AssertionError("expected a profile join counterexample")
    return Counterexample(
        name="profile_merge_is_not_least_upper_bound",
        size=2,
        detail={
            "left": left_profile.as_tuple(),
            "right": right_profile.as_tuple(),
            "componentwise_lub": expected_lub.as_tuple(),
            "merged": merged_profile.as_tuple(),
        },
    )


def find_conflict_counterexample() -> Counterexample:
    true_record = leaf("true", "P", "true")
    false_record = leaf("false", "P", "false")
    merged = compose("conflict", (true_record, false_record))
    if reconstruct_value(true_record, "P", 1) is None:
        raise AssertionError("local true record should resolve")
    if reconstruct_value(false_record, "P", 1) is None:
        raise AssertionError("local false record should resolve")
    if reconstruct_value(merged, "P", 1) is not None:
        raise AssertionError("conflicting merge should be unresolved")
    return Counterexample(
        name="locally_final_records_merge_to_unresolved",
        size=2,
        detail={
            "left_decision": "true",
            "right_decision": "false",
            "merged_decision": None,
        },
    )


def find_duplicate_inflation_counterexample() -> Counterexample:
    first = leaf("copy-a", "P", "true", source_id="shared")
    second = leaf("copy-b", "P", "true", source_id="shared")
    merged = compose("duplicate", (first, second))
    tokens = relevant_tokens(merged, "P", "true")
    naive_support = len(tokens)
    certified_support = len(provenance_support(tokens))
    if naive_support <= certified_support:
        raise AssertionError("expected naive duplicate inflation")
    return Counterexample(
        name="duplicate_tokens_inflate_naive_support",
        size=2,
        detail={
            "naive_token_support": naive_support,
            "provenance_support": certified_support,
        },
    )


def find_coarse_graining_order_change() -> Counterexample:
    candidates: list[RecursiveRecord] = []
    for size in range(1, 4):
        for costs in product((1.0, 2.0), repeat=size):
            records = tuple(
                leaf(
                    f"candidate-{size}-{index}-{int(cost)}",
                    "P",
                    "true",
                    reversal_cost=cost,
                )
                for index, cost in enumerate(costs)
            )
            candidates.append(records[0] if size == 1 else compose(f"bundle-{size}-{costs}", records))
    for left, right in combinations(candidates, 2):
        left_profile = finality_profile(left, "P", "true", threshold=1)
        right_profile = finality_profile(right, "P", "true", threshold=1)
        if not left_profile.no_more_final_than(right_profile):
            continue
        left_checkpoint = checkpoint(left, "left", "P", 1, "provenance", reversal_cost=4.0)
        right_checkpoint = checkpoint(right, "right", "P", 1, "lossy", reversal_cost=1.0)
        left_after = finality_profile(left_checkpoint, "P", "true", 1)
        right_after = finality_profile(right_checkpoint, "P", "true", 1)
        if not right_after.no_more_final_than(left_after):
            continue
        if left_after == right_after:
            continue
        return Counterexample(
            name="coarse_graining_changes_finality_order",
            size=len(expressed_tokens(left)) + len(expressed_tokens(right)),
            detail={
                "left_before": left_profile.as_tuple(),
                "right_before": right_profile.as_tuple(),
                "left_after": left_after.as_tuple(),
                "right_after": right_after.as_tuple(),
            },
        )
    raise AssertionError("no coarse-graining order-change counterexample found")


def find_local_to_global_counterexample() -> Counterexample:
    left = leaf("local-a", "P", "true", assignment={"x": "0"})
    right = leaf("local-b", "P", "true", assignment={"x": "1"})
    if not local_contexts_glue((left,)) or not local_contexts_glue((right,)):
        raise AssertionError("each local context should be consistent")
    if local_contexts_glue((left, right)):
        raise AssertionError("the local contexts should not admit a global assignment")
    return Counterexample(
        name="locally_consistent_records_fail_to_glue",
        size=2,
        detail={
            "left_assignment": {"x": "0"},
            "right_assignment": {"x": "1"},
            "global_section_exists": False,
        },
    )


def epigenetic_history_counterexample() -> Counterexample:
    tagged = leaf("tagged", "P", "true", expression_tags=("methylated",))
    unmarked = nested(tagged, 4)
    silenced = compose(
        "silenced",
        (nested(tagged, 4),),
        local_marks=(ExpressionMark("methylated", False),),
    )
    reactivated = compose(
        "silenced-then-reprogrammed",
        (
            compose(
                "reactivation-site",
                (nested(tagged, 4),),
                local_marks=(ExpressionMark("methylated", True),),
            ),
        ),
        local_marks=(ExpressionMark("methylated", False),),
    )
    return Counterexample(
        name="same_record_identity_different_inherited_expression",
        size=1,
        detail={
            "unmarked_support": finality_profile(unmarked, "P", "true", 1).accessible_support,
            "silenced_support": finality_profile(silenced, "P", "true", 1).accessible_support,
            "reactivated_support": finality_profile(
                reactivated, "P", "true", 1
            ).accessible_support,
            "record_identity_preserved_while_silenced": provenance_support(
                stored_tokens(unmarked)
            )
            == provenance_support(stored_tokens(silenced))
            == provenance_support(stored_tokens(reactivated)),
        },
    )


def depth_sweep(max_depth: int = 64) -> dict[str, object]:
    base = leaf("depth-source", "P", "true", expression_tags=("context",))
    neutral_profiles = []
    silenced_profiles = []
    for depth in range(max_depth + 1):
        neutral = nested(base, depth)
        silenced = nested(
            base,
            depth,
            mark_at=max(0, depth // 2) if depth else None,
            mark=ExpressionMark("context", False) if depth else None,
        )
        neutral_profiles.append(finality_profile(neutral, "P", "true", 1).as_tuple())
        silenced_profiles.append(finality_profile(silenced, "P", "true", 1).as_tuple())
    return {
        "depths_tested": max_depth + 1,
        "maximum_depth": max_depth,
        "neutral_invariant": len(set(neutral_profiles)) == 1,
        "silencing_inherited_at_every_positive_depth": all(
            profile[0] == 0 for profile in silenced_profiles[1:]
        ),
    }


def exhaustive_composition_sweep(source_count: int = 4) -> dict[str, object]:
    """Evaluate every non-empty subset and every ordered subset pair."""

    if not 1 <= source_count <= 8:
        raise ValueError("source count must be in [1, 8]")
    sources = tuple(leaf(f"s{index}", "P", "true") for index in range(source_count))
    bundles: list[RecursiveRecord] = []
    for mask in range(1, 2**source_count):
        selected = tuple(
            source for index, source in enumerate(sources) if mask & (1 << index)
        )
        bundles.append(
            selected[0] if len(selected) == 1 else compose(f"subset-{mask}", selected)
        )

    pair_count = 0
    monotone_count = 0
    exact_profile_lub_count = 0
    decision_preserved_count = 0
    for left in bundles:
        for right in bundles:
            pair_count += 1
            merged = compose(f"pair-{pair_count}", (left, right))
            left_profile = finality_profile(left, "P", "true", 1)
            right_profile = finality_profile(right, "P", "true", 1)
            merged_profile = finality_profile(merged, "P", "true", 1)
            monotone_count += (
                left_profile.no_more_final_than(merged_profile)
                and right_profile.no_more_final_than(merged_profile)
            )
            exact_profile_lub_count += (
                merged_profile == left_profile.componentwise_max(right_profile)
            )
            decision_preserved_count += reconstruct_value(merged, "P", 1) == "true"

    provenance_support_preserved = 0
    lossy_support_preserved = 0
    provenance_holder_preserved = 0
    provenance_branch_preserved = 0
    for index, bundle in enumerate(bundles):
        before = finality_profile(bundle, "P", "true", 1)
        provenance_checkpoint = checkpoint(
            bundle,
            f"provenance-{index}",
            "P",
            1,
            "provenance",
        )
        lossy_checkpoint = checkpoint(
            bundle,
            f"lossy-{index}",
            "P",
            1,
            "lossy",
        )
        provenance_after = finality_profile(
            provenance_checkpoint, "P", "true", 1
        )
        lossy_after = finality_profile(lossy_checkpoint, "P", "true", 1)
        provenance_support_preserved += (
            provenance_after.accessible_support == before.accessible_support
        )
        lossy_support_preserved += (
            lossy_after.accessible_support == before.accessible_support
        )
        provenance_holder_preserved += (
            provenance_after.holder_redundancy == before.holder_redundancy
        )
        provenance_branch_preserved += (
            provenance_after.branch_support == before.branch_support
        )

    return {
        "source_count": source_count,
        "nonempty_states": len(bundles),
        "ordered_pairs": pair_count,
        "transparent_merge_monotonicity_fraction": monotone_count / pair_count,
        "transparent_merge_decision_preservation_fraction": decision_preserved_count
        / pair_count,
        "profile_merge_equals_componentwise_lub_fraction": exact_profile_lub_count
        / pair_count,
        "provenance_checkpoint_support_preservation_fraction": provenance_support_preserved
        / len(bundles),
        "lossy_checkpoint_support_preservation_fraction": lossy_support_preserved
        / len(bundles),
        "provenance_checkpoint_holder_preservation_fraction": provenance_holder_preserved
        / len(bundles),
        "provenance_checkpoint_branch_preservation_fraction": provenance_branch_preserved
        / len(bundles),
    }


def randomized_grouping_trials(trials: int = 500, seed: int = 11) -> dict[str, object]:
    rng = Random(seed)
    neutral_invariant = 0
    epigenetic_grouping_dependent = 0
    for trial in range(trials):
        records = tuple(
            leaf(
                f"trial-{trial}-{index}",
                "P",
                "true",
                expression_tags=("shared-context",),
            )
            for index in range(3)
        )
        variants = grouping_variants(records)
        states = tuple(evidence_join(variant) for variant in variants)
        neutral_invariant += len(set(states)) == 1

        target = rng.randrange(3)
        marked_child = compose(
            f"marked-{trial}",
            (records[target],),
            local_marks=(ExpressionMark("shared-context", False),),
        )
        marked_variants = (
            compose(
                "m-local",
                tuple(
                    marked_child if index == target else record
                    for index, record in enumerate(records)
                ),
            ),
            compose(
                "m-ancestor",
                records,
                local_marks=(ExpressionMark("shared-context", False),),
            ),
        )
        marked_states = tuple(evidence_join(variant) for variant in marked_variants)
        epigenetic_grouping_dependent += len(set(marked_states)) > 1
    return {
        "trials": trials,
        "neutral_grouping_invariance_fraction": neutral_invariant / trials,
        "context_placement_dependence_fraction": epigenetic_grouping_dependent / trials,
    }


def run_compositional_analysis() -> dict[str, object]:
    sample_records = tuple(leaf(name, "P", "true") for name in ("a", "b", "c"))
    states = tuple(evidence_join(record) for record in sample_records) + (
        evidence_join(compose("ab", sample_records[:2])),
    )
    return {
        "evidence_join_laws": evidence_join_laws(states),
        "counterexamples": {
            counterexample.name: counterexample
            for counterexample in (
                find_profile_join_counterexample(),
                find_conflict_counterexample(),
                find_duplicate_inflation_counterexample(),
                find_coarse_graining_order_change(),
                find_local_to_global_counterexample(),
                epigenetic_history_counterexample(),
            )
        },
        "depth_sweep": depth_sweep(max_depth=1024),
        "exhaustive_composition_sweep": exhaustive_composition_sweep(),
        "grouping_trials": randomized_grouping_trials(),
    }
