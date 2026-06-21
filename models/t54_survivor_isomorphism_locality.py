"""T164: isomorphism and locality audit for T163 survivor classes.

T163 found 26 labeled six-event T54 rank-pair survivors. This module asks a
more invariant question: how many distinct finite poset shapes do those labels
represent, and how structurally thin are the surviving shapes?

The result is still finite control work. It is not spacetime evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    CausetDiagnostics,
    Event,
    OrderPair,
    compute_causet_diagnostics,
)
from models.t54_rank_pair_family_census import (
    InfoPermutation,
    T163CaseAudit,
    audit_t163_family,
    t163_t126_datum_for_permutation,
)


@dataclass(frozen=True)
class T164ClassAudit:
    class_id: str
    representative_permutation: InfoPermutation
    member_permutations: tuple[InfoPermutation, ...]
    dual_quotient_id: str
    labeled_member_count: int
    strict_pair_count: int
    cover_relation_count: int
    height: int
    width: int
    rank_profile: tuple[int, ...]
    cover_degree_profile: tuple[int, ...]
    comparable_degree_profile: tuple[int, ...]
    max_cover_hub_fraction: Fraction
    interval_counts_by_size: tuple[tuple[int, int], ...]
    max_interval_interior_size: int
    locality_label: str


@dataclass(frozen=True)
class T164Result:
    stable_labeled_survivor_count: int
    oriented_isomorphism_class_count: int
    order_dual_quotient_class_count: int
    largest_oriented_class_size: int
    singleton_oriented_class_count: int
    strict_pair_count_by_oriented_class: tuple[tuple[int, int], ...]
    cover_degree_profiles_by_oriented_class: tuple[tuple[tuple[int, ...], int], ...]
    all_classes_height_three: bool
    all_classes_parent_intervals_thin: bool
    all_classes_low_cover_hub: bool
    class_audits: tuple[T164ClassAudit, ...]
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


NOT_CLAIMED = (
    "T164 does not show a random sprinkling law, faithful embedding, metric or "
    "Lorentzian reconstruction, covariance, or a continuum limit. It only "
    "quotients the T163 six-event survivor set by finite-poset shape and adds "
    "a first structural locality guardrail."
)


def run_t164_analysis() -> T164Result:
    stable_audits = tuple(
        audit
        for audit in audit_t163_family()
        if audit.outcome_bucket == "t159_stable_survivor"
    )
    oriented_groups = _oriented_isomorphism_groups(stable_audits)
    oriented_keys = tuple(sorted(oriented_groups))
    oriented_id_by_key = {
        key: f"C{index:02d}" for index, key in enumerate(oriented_keys, start=1)
    }
    dual_id_by_key = _dual_quotient_ids(oriented_keys)

    class_audits = tuple(
        _class_audit(
            class_id=oriented_id_by_key[key],
            dual_quotient_id=dual_id_by_key[key],
            audits=oriented_groups[key],
        )
        for key in oriented_keys
    )
    strict_distribution = _count_by_key(
        class_audits,
        key=lambda audit: audit.strict_pair_count,
    )
    cover_distribution = _count_by_key(
        class_audits,
        key=lambda audit: audit.cover_degree_profile,
    )

    return T164Result(
        stable_labeled_survivor_count=len(stable_audits),
        oriented_isomorphism_class_count=len(class_audits),
        order_dual_quotient_class_count=len(set(dual_id_by_key.values())),
        largest_oriented_class_size=max(
            (audit.labeled_member_count for audit in class_audits),
            default=0,
        ),
        singleton_oriented_class_count=sum(
            1 for audit in class_audits if audit.labeled_member_count == 1
        ),
        strict_pair_count_by_oriented_class=strict_distribution,
        cover_degree_profiles_by_oriented_class=cover_distribution,
        all_classes_height_three=all(audit.height == 3 for audit in class_audits),
        all_classes_parent_intervals_thin=all(
            audit.max_interval_interior_size <= 1 for audit in class_audits
        ),
        all_classes_low_cover_hub=all(
            audit.max_cover_hub_fraction <= Fraction(3, 5)
            for audit in class_audits
        ),
        class_audits=class_audits,
        strongest_claim=(
            "The 26 labeled T163 survivors reduce to 15 oriented finite-poset "
            "isomorphism classes, or 9 classes if order-dual shapes are also "
            "identified. Every surviving class is a six-event height-3, "
            "parent-interval-thin control; the survivor set is structurally "
            "narrow rather than a broad spacetime-like family."
        ),
        improved=(
            "T164 removes label inflation from the T163 positive boundary and "
            "adds invariant shape diagnostics: class multiplicity, order-dual "
            "collapse, strict-pair counts, Hasse-cover degree profiles, rank "
            "profiles, and maximum parent interval size."
        ),
        weakened_or_falsified=(
            "This weakens the optimistic reading of T163. The 26 survivors are "
            "not 26 independent structures; they collapse to 15 oriented shapes "
            "with maximum labeled multiplicity 2, and all remain tiny, thin "
            "six-event controls rather than locality-rich causal-set samples."
        ),
        falsification_condition=(
            "T164 fails if the canonical labeling does not preserve finite "
            "poset isomorphism, if any non-surviving T163 case enters the "
            "quotient, or if the class counts are interpreted as a continuum, "
            "sprinkling, embedding, covariance, or metric result."
        ),
        s1_update=(
            "S1 remains open_formal_target. The finite boundary is cleaner: "
            "there is a small invariant survivor family after T163, but it is "
            "label-compressed and structurally thin."
        ),
        claim_ledger_update=(
            "Add T164 to S1: the 26 labeled T163 survivors quotient to 15 "
            "oriented finite-poset isomorphism classes and 9 order-dual classes; "
            "all are height-3 six-event controls with parent intervals of size "
            "at most 1. Treat them as a narrow finite target for stronger "
            "locality/sprinkling stress tests, not as spacetime evidence."
        ),
        open_blocker=(
            "No random-sprinkling comparison, neighborhood-growth law, "
            "dimension estimator beyond ordering fraction, embedding theorem, "
            "covariance result, Lorentzian metric reconstruction, or continuum "
            "bridge exists for the 15 oriented survivor classes."
        ),
        suggested_next=(
            "Run a declared finite locality or random-sprinkling stress test on "
            "the 15 oriented classes, preferably one that can reject thin "
            "height-3 controls without relying on labels."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t164_result_to_dict(result: T164Result) -> dict[str, Any]:
    return {
        "stable_labeled_survivor_count": result.stable_labeled_survivor_count,
        "oriented_isomorphism_class_count": result.oriented_isomorphism_class_count,
        "order_dual_quotient_class_count": result.order_dual_quotient_class_count,
        "largest_oriented_class_size": result.largest_oriented_class_size,
        "singleton_oriented_class_count": result.singleton_oriented_class_count,
        "strict_pair_count_by_oriented_class": [
            {"strict_pair_count": count, "class_count": class_count}
            for count, class_count in result.strict_pair_count_by_oriented_class
        ],
        "cover_degree_profiles_by_oriented_class": [
            {
                "cover_degree_profile": list(profile),
                "class_count": class_count,
            }
            for profile, class_count in result.cover_degree_profiles_by_oriented_class
        ],
        "all_classes_height_three": result.all_classes_height_three,
        "all_classes_parent_intervals_thin": result.all_classes_parent_intervals_thin,
        "all_classes_low_cover_hub": result.all_classes_low_cover_hub,
        "class_audits": [_class_audit_to_dict(audit) for audit in result.class_audits],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_falsified": result.weakened_or_falsified,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _oriented_isomorphism_groups(
    audits: tuple[T163CaseAudit, ...],
) -> dict[str, tuple[T163CaseAudit, ...]]:
    groups: dict[str, list[T163CaseAudit]] = {}
    for audit in audits:
        datum = t163_t126_datum_for_permutation(audit.info_permutation)
        key = _canonical_poset_key(datum.events, _strict_pairs(datum.relation))
        groups.setdefault(key, []).append(audit)
    return {
        key: tuple(sorted(group, key=lambda audit: audit.info_permutation))
        for key, group in groups.items()
    }


def _dual_quotient_ids(oriented_keys: tuple[str, ...]) -> dict[str, str]:
    dual_keys = {
        key: min(key, _canonical_dual_key_from_key(key))
        for key in oriented_keys
    }
    quotient_keys = tuple(sorted(set(dual_keys.values())))
    quotient_id_by_key = {
        key: f"D{index:02d}" for index, key in enumerate(quotient_keys, start=1)
    }
    return {key: quotient_id_by_key[dual_keys[key]] for key in oriented_keys}


def _class_audit(
    *,
    class_id: str,
    dual_quotient_id: str,
    audits: tuple[T163CaseAudit, ...],
) -> T164ClassAudit:
    representative = audits[0]
    datum = t163_t126_datum_for_permutation(representative.info_permutation)
    strict = _strict_pairs(datum.relation)
    covers = _cover_relations(datum.events, strict)
    diagnostics = compute_causet_diagnostics(datum.events, datum.relation)
    max_interval = _max_interval_interior_size(diagnostics)

    return T164ClassAudit(
        class_id=class_id,
        representative_permutation=representative.info_permutation,
        member_permutations=tuple(audit.info_permutation for audit in audits),
        dual_quotient_id=dual_quotient_id,
        labeled_member_count=len(audits),
        strict_pair_count=diagnostics.strict_pair_count,
        cover_relation_count=diagnostics.cover_relation_count,
        height=diagnostics.height,
        width=diagnostics.width,
        rank_profile=diagnostics.rank_profile,
        cover_degree_profile=_degree_profile(datum.events, covers),
        comparable_degree_profile=_degree_profile(datum.events, strict),
        max_cover_hub_fraction=diagnostics.largest_cover_hub_fraction,
        interval_counts_by_size=diagnostics.interval_counts_by_size,
        max_interval_interior_size=max_interval,
        locality_label=_locality_label(diagnostics, max_interval),
    )


def _canonical_dual_key_from_key(key: str) -> str:
    size = _key_size(key)
    events = tuple(str(index) for index in range(size))
    strict = _strict_pairs_from_key(key, events)
    dual = frozenset((right, left) for left, right in strict)
    return _canonical_poset_key(frozenset(events), dual)


def _canonical_poset_key(
    events: frozenset[Event],
    strict: frozenset[OrderPair],
) -> str:
    ordered_events = tuple(sorted(events))
    size = len(ordered_events)
    best: str | None = None
    for old_events_by_new_label in permutations(ordered_events):
        bits = []
        for left_new in range(size):
            for right_new in range(size):
                if left_new == right_new:
                    continue
                left_old = old_events_by_new_label[left_new]
                right_old = old_events_by_new_label[right_new]
                bits.append("1" if (left_old, right_old) in strict else "0")
        candidate = "".join(bits)
        if best is None or candidate < best:
            best = candidate
    if best is None:
        return ""
    return best


def _key_size(key: str) -> int:
    size = 0
    while size * (size - 1) < len(key):
        size += 1
    if size * (size - 1) != len(key):
        raise ValueError(f"invalid canonical key length: {len(key)}")
    return size


def _strict_pairs_from_key(
    key: str,
    events: tuple[Event, ...],
) -> frozenset[OrderPair]:
    pairs: set[OrderPair] = set()
    cursor = 0
    for left in events:
        for right in events:
            if left == right:
                continue
            if key[cursor] == "1":
                pairs.add((left, right))
            cursor += 1
    return frozenset(pairs)


def _strict_pairs(relation: frozenset[OrderPair]) -> frozenset[OrderPair]:
    return frozenset((left, right) for left, right in relation if left != right)


def _cover_relations(
    events: frozenset[Event],
    strict: frozenset[OrderPair],
) -> frozenset[OrderPair]:
    covers: set[OrderPair] = set()
    for left, right in strict:
        if not any(
            (left, middle) in strict and (middle, right) in strict
            for middle in events
            if middle not in {left, right}
        ):
            covers.add((left, right))
    return frozenset(covers)


def _degree_profile(
    events: frozenset[Event],
    pairs: frozenset[OrderPair],
) -> tuple[int, ...]:
    return tuple(
        sorted(
            sum(1 for left, right in pairs if event in {left, right})
            for event in events
        )
    )


def _max_interval_interior_size(diagnostics: CausetDiagnostics) -> int:
    if not diagnostics.interval_counts_by_size:
        return 0
    return max(size for size, count in diagnostics.interval_counts_by_size if count > 0)


def _locality_label(
    diagnostics: CausetDiagnostics,
    max_interval_interior_size: int,
) -> str:
    if diagnostics.largest_cover_hub_fraction > Fraction(3, 5):
        return "cover_hub_warning"
    if max_interval_interior_size <= 1:
        return "thin_height3_control"
    return "requires_stronger_locality_test"


def _count_by_key(
    audits: tuple[T164ClassAudit, ...],
    *,
    key: Any,
) -> tuple[tuple[Any, int], ...]:
    counts: dict[Any, int] = {}
    for audit in audits:
        value = key(audit)
        counts[value] = counts.get(value, 0) + 1
    return tuple(sorted(counts.items()))


def _class_audit_to_dict(audit: T164ClassAudit) -> dict[str, Any]:
    return {
        "class_id": audit.class_id,
        "representative_permutation": list(audit.representative_permutation),
        "member_permutations": [list(member) for member in audit.member_permutations],
        "dual_quotient_id": audit.dual_quotient_id,
        "labeled_member_count": audit.labeled_member_count,
        "strict_pair_count": audit.strict_pair_count,
        "cover_relation_count": audit.cover_relation_count,
        "height": audit.height,
        "width": audit.width,
        "rank_profile": list(audit.rank_profile),
        "cover_degree_profile": list(audit.cover_degree_profile),
        "comparable_degree_profile": list(audit.comparable_degree_profile),
        "max_cover_hub_fraction": _fraction_to_dict(audit.max_cover_hub_fraction),
        "interval_counts_by_size": [
            {"size": size, "count": count}
            for size, count in audit.interval_counts_by_size
        ],
        "max_interval_interior_size": audit.max_interval_interior_size,
        "locality_label": audit.locality_label,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t164_result_to_dict(run_t164_analysis()), indent=2))
