"""T126: causal-set embeddability screen for finality colimits.

This module is a finite necessary-condition filter. It asks whether a
canonical finality colimit order can even be treated as a causal-set candidate,
then applies small combinatorial diagnostics that reject obvious
non-manifoldlike controls. Passing the screen is not an embedding theorem and
does not derive spacetime, GR, metric geometry, or continuum structure.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations

from models.spacetime_aggregation import (
    aggregate_domains,
    compatible_chain_domains,
    partial_spacetime_domains,
)


Event = str
OrderPair = tuple[Event, Event]


@dataclass(frozen=True)
class FinalityColimitCausetDatum:
    name: str
    events: frozenset[Event]
    relation: frozenset[OrderPair]
    descent_gate_passed: bool
    canonical_colimit: bool
    phantom_gap_resolved: bool
    observer_only_gap_changes_strict_order: bool
    source: str
    minimum_events_for_manifold_filter: int = 6

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("name cannot be empty")
        relation_events = {event for pair in self.relation for event in pair}
        missing = relation_events - set(self.events)
        if missing:
            raise ValueError(f"relation references unknown events: {sorted(missing)}")


@dataclass(frozen=True)
class PosetAxiomReport:
    finite: bool
    reflexive: bool
    antisymmetric: bool
    transitive: bool
    locally_finite: bool
    failure_reasons: tuple[str, ...]

    @property
    def is_poset(self) -> bool:
        return (
            self.finite
            and self.reflexive
            and self.antisymmetric
            and self.transitive
            and self.locally_finite
        )


@dataclass(frozen=True)
class CausetDiagnostics:
    event_count: int
    strict_pair_count: int
    comparable_fraction: Fraction
    cover_relation_count: int
    link_density: Fraction
    height: int
    width: int
    rank_profile: tuple[int, ...]
    interval_counts_by_size: tuple[tuple[int, int], ...]
    interval_profile_counts: tuple[tuple[str, int], ...]
    largest_comparable_hub_fraction: Fraction
    largest_cover_hub_fraction: Fraction
    profile_spread_obstruction: bool


@dataclass(frozen=True)
class CausetAudit:
    name: str
    classification: str
    causal_set_candidate: bool
    manifold_filter_passed: bool
    poset_report: PosetAxiomReport
    diagnostics: CausetDiagnostics | None
    reason: str
    required_next: str
    not_claimed: str


@dataclass(frozen=True)
class T126Result:
    audits: tuple[CausetAudit, ...]
    descent_failures_blocked_before_causet_claims: bool
    t16_control_passes_causet_gate: bool
    invalid_relations_rejected: bool
    valid_posets_can_fail_manifold_filter: bool
    passing_filter_does_not_derive_spacetime: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


NOT_CLAIMED = (
    "Passing T126 is not a faithful embedding proof and does not derive "
    "spacetime, GR, metric structure, Lorentzian geometry, or continuum physics."
)


def non_strict_relation(
    events: frozenset[Event],
    strict_pairs: frozenset[OrderPair],
) -> frozenset[OrderPair]:
    """Return reflexive transitive closure of a finite strict relation."""

    closure = set(strict_pairs)
    changed = True
    while changed:
        changed = False
        for left, middle in tuple(closure):
            for candidate_middle, right in tuple(closure):
                if middle == candidate_middle and left != right and (left, right) not in closure:
                    closure.add((left, right))
                    changed = True
    return frozenset(closure | {(event, event) for event in events})


def audit_poset_axioms(
    events: frozenset[Event],
    relation: frozenset[OrderPair],
) -> PosetAxiomReport:
    failures: list[str] = []
    reflexive = all((event, event) in relation for event in events)
    if not reflexive:
        failures.append("missing_reflexive_pairs")

    antisymmetric = True
    for left, right in relation:
        if left != right and (right, left) in relation:
            antisymmetric = False
            failures.append("antisymmetry_violation")
            break

    transitive = True
    for left, middle in relation:
        for candidate_middle, right in relation:
            if middle == candidate_middle and (left, right) not in relation:
                transitive = False
                failures.append("transitivity_violation")
                break
        if not transitive:
            break

    return PosetAxiomReport(
        finite=True,
        reflexive=reflexive,
        antisymmetric=antisymmetric,
        transitive=transitive,
        locally_finite=True,
        failure_reasons=tuple(dict.fromkeys(failures)),
    )


def audit_finality_colimit_causet(
    datum: FinalityColimitCausetDatum,
) -> CausetAudit:
    placeholder_report = PosetAxiomReport(
        finite=True,
        reflexive=False,
        antisymmetric=False,
        transitive=False,
        locally_finite=True,
        failure_reasons=("causet_gate_not_reached",),
    )

    if not datum.descent_gate_passed:
        return CausetAudit(
            name=datum.name,
            classification="not_descent_datum",
            causal_set_candidate=False,
            manifold_filter_passed=False,
            poset_report=placeholder_report,
            diagnostics=None,
            reason=(
                "The T54-style descent gate failed or is missing, so no "
                "causal-set embeddability claim is meaningful."
            ),
            required_next="Repair event maps, overlap witnesses, record maps, and axis agreement first.",
            not_claimed=NOT_CLAIMED,
        )

    if not datum.canonical_colimit:
        return CausetAudit(
            name=datum.name,
            classification="noncanonical_colimit",
            causal_set_candidate=False,
            manifold_filter_passed=False,
            poset_report=placeholder_report,
            diagnostics=None,
            reason=(
                "The observer data admit more than one compatible completion, "
                "so there is no unique finality-colimit order to audit."
            ),
            required_next="Supply descent data that select a unique event-finality colimit.",
            not_claimed=NOT_CLAIMED,
        )

    poset_report = audit_poset_axioms(datum.events, datum.relation)
    if not poset_report.is_poset:
        return CausetAudit(
            name=datum.name,
            classification="not_poset",
            causal_set_candidate=False,
            manifold_filter_passed=False,
            poset_report=poset_report,
            diagnostics=None,
            reason=(
                "The candidate relation is not a finite partial order: "
                + ", ".join(poset_report.failure_reasons)
                + "."
            ),
            required_next="Produce a reflexive, antisymmetric, transitive colimit relation before causal-set screening.",
            not_claimed=NOT_CLAIMED,
        )

    diagnostics = compute_causet_diagnostics(datum.events, datum.relation)
    if (not datum.phantom_gap_resolved) or datum.observer_only_gap_changes_strict_order:
        return CausetAudit(
            name=datum.name,
            classification="phantom_gap_unresolved",
            causal_set_candidate=False,
            manifold_filter_passed=False,
            poset_report=poset_report,
            diagnostics=diagnostics,
            reason=(
                "Observer-apparent phantom gaps still change the strict order, "
                "so the tested relation is not yet the event-finality colimit."
            ),
            required_next="Separate observer-apparent order from ambient event-finality order before T126.",
            not_claimed=NOT_CLAIMED,
        )

    classification, reason, required_next, passed = _manifold_filter_verdict(
        datum,
        diagnostics,
    )
    return CausetAudit(
        name=datum.name,
        classification=classification,
        causal_set_candidate=True,
        manifold_filter_passed=passed,
        poset_report=poset_report,
        diagnostics=diagnostics,
        reason=reason,
        required_next=required_next,
        not_claimed=NOT_CLAIMED,
    )


def compute_causet_diagnostics(
    events: frozenset[Event],
    relation: frozenset[OrderPair],
) -> CausetDiagnostics:
    event_count = len(events)
    strict = _strict_pairs(relation)
    comparable_pair_limit = event_count * (event_count - 1) // 2
    strict_pair_count = len(strict)
    comparable_fraction = _fraction(strict_pair_count, comparable_pair_limit)
    covers = _cover_relations(events, strict)
    link_density = _fraction(len(covers), strict_pair_count)
    height = _height(events, strict)
    width = _width(events, strict)
    rank_profile = _rank_profile(events, strict)
    interval_counts, interval_profiles, profile_spread = _interval_summaries(
        events,
        strict,
    )

    comparable_hub = _largest_incidence_fraction(events, strict)
    cover_hub = _largest_incidence_fraction(events, covers)

    return CausetDiagnostics(
        event_count=event_count,
        strict_pair_count=strict_pair_count,
        comparable_fraction=comparable_fraction,
        cover_relation_count=len(covers),
        link_density=link_density,
        height=height,
        width=width,
        rank_profile=rank_profile,
        interval_counts_by_size=interval_counts,
        interval_profile_counts=interval_profiles,
        largest_comparable_hub_fraction=comparable_hub,
        largest_cover_hub_fraction=cover_hub,
        profile_spread_obstruction=profile_spread,
    )


def run_t126_analysis() -> T126Result:
    audits = tuple(
        audit_finality_colimit_causet(datum)
        for datum in canonical_t126_datums()
    )
    audit_map = {audit.name: audit for audit in audits}

    descent_failures_blocked = (
        audit_map["descent_failure_control"].classification == "not_descent_datum"
        and audit_map["noncanonical_boundary_control"].classification
        == "noncanonical_colimit"
    )
    valid_poset_failures = {
        audit.classification
        for audit in audits
        if audit.causal_set_candidate and not audit.manifold_filter_passed
    }

    return T126Result(
        audits=audits,
        descent_failures_blocked_before_causet_claims=descent_failures_blocked,
        t16_control_passes_causet_gate=audit_map["t16_positive_poset_control"].causal_set_candidate,
        invalid_relations_rejected=audit_map["cyclic_relation_control"].classification
        == "not_poset",
        valid_posets_can_fail_manifold_filter=bool(
            {
                "hub_nonlocality_obstruction",
                "interval_profile_obstruction",
                "rank_width_obstruction",
                "order_dimension_obstruction",
            }
            & valid_poset_failures
        ),
        passing_filter_does_not_derive_spacetime=True,
        strongest_claim=(
            "A finite finality colimit is not automatically spacetime-like. "
            "It must first be canonical descent data, then a valid finite "
            "causal-set candidate, and only then may it face manifoldlikeness "
            "necessary-condition filters. T126 finds valid posets that fail "
            "those filters."
        ),
        improved=(
            "T126 turns the S1 spacetime-colimit route into an executable "
            "screen with explicit rejection modes: malformed descent data, "
            "noncanonical completion, non-poset relations, unresolved phantom "
            "gaps, hub nonlocality, degenerate rank/width profiles, interval "
            "profile failures, and local dimension-profile inconsistency."
        ),
        weakened=(
            "This weakens any reading of T16/T51/T52/T54 as a spacetime "
            "derivation. A successful finite colimit can be only a small "
            "causal-set candidate, and several valid finality orders are now "
            "explicitly rejected before S1 may claim manifold-facing content."
        ),
        falsification_condition=(
            "T126 fails if a noncanonical or malformed observer colimit can "
            "legitimately be used as embeddability evidence, or if the selected "
            "finite diagnostics reject a known-good control after its scale, "
            "dimension class, and causal-set comparison target are declared."
        ),
        s1_update=(
            "S1 remains an open formal target. Future S1 witnesses must clear "
            "descent/canonicality, causal-set validity, phantom-gap, and finite "
            "manifoldlikeness screens before claiming spacetime-reconstruction "
            "residue."
        ),
        claim_ledger_update=(
            "Add T126 to S1: finite finality colimits now face an executable "
            "causal-set/manifoldlikeness necessary-condition audit. Passing the "
            "screen is filter-only, while valid-but-degenerate posets weaken "
            "spacetime-derivation language."
        ),
        open_blocker=(
            "No continuum limit, faithful embedding theorem, Lorentzian metric "
            "reconstruction, QFT algebra, or covariance result exists for the "
            "surviving finite controls."
        ),
        suggested_next=(
            "Connect a T54/T58 canonical colimit fixture directly to T126, then "
            "compare the survivors against a named causal-set dimension or "
            "sprinkling diagnostic instead of adding new spacetime prose."
        ),
    )


def canonical_t126_datums() -> tuple[FinalityColimitCausetDatum, ...]:
    return (
        t16_positive_poset_control(),
        t16_partial_order_control(),
        descent_failure_control(),
        noncanonical_boundary_control(),
        cyclic_relation_control(),
        phantom_gap_control(),
        hub_order_control(),
        complete_bipartite_layer_control(),
        degenerate_chain_control(),
        mixed_interval_profile_control(),
        grid_filter_pass_control(),
    )


def t16_positive_poset_control() -> FinalityColimitCausetDatum:
    result = aggregate_domains(compatible_chain_domains())
    assert result.global_structure is not None
    events = result.global_structure.events
    return FinalityColimitCausetDatum(
        name="t16_positive_poset_control",
        events=events,
        relation=non_strict_relation(events, result.global_structure.order_edges),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="T16 compatible-chain aggregation",
    )


def t16_partial_order_control() -> FinalityColimitCausetDatum:
    result = aggregate_domains(partial_spacetime_domains())
    assert result.global_structure is not None
    events = result.global_structure.events
    return FinalityColimitCausetDatum(
        name="t16_partial_order_control",
        events=events,
        relation=non_strict_relation(events, result.global_structure.order_edges),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="T16 disconnected partial-order aggregation",
    )


def descent_failure_control() -> FinalityColimitCausetDatum:
    events = frozenset({"a", "b"})
    return FinalityColimitCausetDatum(
        name="descent_failure_control",
        events=events,
        relation=non_strict_relation(events, frozenset({("a", "b")})),
        descent_gate_passed=False,
        canonical_colimit=False,
        phantom_gap_resolved=False,
        observer_only_gap_changes_strict_order=True,
        source="T54-style missing event-map failure",
    )


def noncanonical_boundary_control() -> FinalityColimitCausetDatum:
    events = frozenset({"a", "b", "c", "d"})
    return FinalityColimitCausetDatum(
        name="noncanonical_boundary_control",
        events=events,
        relation=non_strict_relation(events, frozenset({("a", "b"), ("c", "d")})),
        descent_gate_passed=True,
        canonical_colimit=False,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="T53-style ambiguous observer completion",
    )


def cyclic_relation_control() -> FinalityColimitCausetDatum:
    events = frozenset({"a", "b", "c"})
    relation = frozenset(
        {
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
            ("a", "b"),
            ("b", "a"),
            ("b", "c"),
        }
    )
    return FinalityColimitCausetDatum(
        name="cyclic_relation_control",
        events=events,
        relation=relation,
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="explicit cyclic/non-antisymmetric relation",
    )


def phantom_gap_control() -> FinalityColimitCausetDatum:
    events = frozenset({"e1", "e2", "e3"})
    return FinalityColimitCausetDatum(
        name="phantom_gap_control",
        events=events,
        relation=non_strict_relation(events, frozenset({("e1", "e3"), ("e2", "e3")})),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=False,
        observer_only_gap_changes_strict_order=True,
        source="T56/T58-style observer-apparent gap not yet separated",
    )


def hub_order_control() -> FinalityColimitCausetDatum:
    events = frozenset({"hub", "l1", "l2", "l3", "l4", "l5", "l6", "l7"})
    strict = frozenset(("hub", leaf) for leaf in events if leaf != "hub")
    return FinalityColimitCausetDatum(
        name="hub_order_control",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="valid star-shaped poset with an unnatural covering hub",
    )


def complete_bipartite_layer_control() -> FinalityColimitCausetDatum:
    bottom = tuple(f"b{i}" for i in range(4))
    top = tuple(f"t{i}" for i in range(4))
    events = frozenset(bottom + top)
    strict = frozenset((left, right) for left in bottom for right in top)
    return FinalityColimitCausetDatum(
        name="complete_bipartite_layer_control",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="valid two-layer complete bipartite order",
    )


def degenerate_chain_control() -> FinalityColimitCausetDatum:
    events = frozenset(f"c{i}" for i in range(7))
    strict = frozenset(
        (f"c{i}", f"c{j}")
        for i in range(7)
        for j in range(i + 1, 7)
    )
    return FinalityColimitCausetDatum(
        name="degenerate_chain_control",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="valid total chain, rejected for the selected 1+1-ish screen",
    )


def mixed_interval_profile_control() -> FinalityColimitCausetDatum:
    events = frozenset({"a", "b", "c", "d", "e", "f", "g", "h"})
    strict_generators = frozenset(
        {
            ("a", "b"),
            ("b", "c"),
            ("c", "d"),
            ("e", "f"),
            ("e", "g"),
            ("f", "h"),
            ("g", "h"),
        }
    )
    return FinalityColimitCausetDatum(
        name="mixed_interval_profile_control",
        events=events,
        relation=non_strict_relation(events, strict_generators),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="two equal-size intervals with incompatible internal profiles",
    )


def grid_filter_pass_control() -> FinalityColimitCausetDatum:
    points = tuple(f"p{i}{j}" for i in range(3) for j in range(3))
    events = frozenset(points)
    strict = frozenset(
        (f"p{i}{j}", f"p{k}{l}")
        for i in range(3)
        for j in range(3)
        for k in range(3)
        for l in range(3)
        if (i, j) != (k, l) and i <= k and j <= l
    )
    return FinalityColimitCausetDatum(
        name="grid_filter_pass_control",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="small 3x3 product-order control that passes this filter only",
    )


def t126_result_to_dict(result: T126Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "descent_failures_blocked_before_causet_claims": (
            result.descent_failures_blocked_before_causet_claims
        ),
        "t16_control_passes_causet_gate": result.t16_control_passes_causet_gate,
        "invalid_relations_rejected": result.invalid_relations_rejected,
        "valid_posets_can_fail_manifold_filter": (
            result.valid_posets_can_fail_manifold_filter
        ),
        "passing_filter_does_not_derive_spacetime": (
            result.passing_filter_does_not_derive_spacetime
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


def _manifold_filter_verdict(
    datum: FinalityColimitCausetDatum,
    diagnostics: CausetDiagnostics,
) -> tuple[str, str, str, bool]:
    if diagnostics.event_count < datum.minimum_events_for_manifold_filter:
        return (
            "insufficient_scale",
            "The relation is a finite causal-set candidate, but the witness is too small for the selected manifoldlikeness diagnostics.",
            "Use the candidate only as a causal-set gate control or build a larger colimit.",
            False,
        )

    if diagnostics.largest_cover_hub_fraction >= Fraction(3, 4):
        return (
            "hub_nonlocality_obstruction",
            "One event supplies covering links to most of the set, producing an unnatural universal-hub profile for this screen.",
            "Replace the hub order with a colimit whose covering relations are locally distributed.",
            False,
        )

    if diagnostics.height == diagnostics.event_count or diagnostics.width == diagnostics.event_count:
        return (
            "rank_width_obstruction",
            "The rank/width profile is degenerate for the selected finite control class.",
            "Declare a different comparison class or supply a less degenerate candidate.",
            False,
        )

    if diagnostics.profile_spread_obstruction:
        return (
            "order_dimension_obstruction",
            "Equal-size intervals have incompatible internal height/width profiles, so the local effective-dimension diagnostic is unstable.",
            "Match interval profiles or use a named dimension estimator with a declared tolerance.",
            False,
        )

    if (
        diagnostics.height <= 2
        and diagnostics.strict_pair_count >= diagnostics.event_count
        and diagnostics.link_density >= Fraction(9, 10)
    ):
        return (
            "interval_profile_obstruction",
            "Almost every comparable pair is a covering link, leaving no Alexandrov-interval structure at this scale.",
            "Supply intervals with nontrivial interior structure or lower the claim to a finite poset control.",
            False,
        )

    return (
        "passes_filter_only",
        "No selected finite obstruction was found. This is only a necessary-condition pass.",
        "Compare against stronger causal-set dimension, sprinkling, locality, or continuum-limit diagnostics.",
        True,
    )


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


def _height(events: frozenset[Event], strict: frozenset[OrderPair]) -> int:
    successors = {event: {right for left, right in strict if left == event} for event in events}
    memo: dict[Event, int] = {}

    def visit(event: Event) -> int:
        if event in memo:
            return memo[event]
        memo[event] = 1 + max((visit(successor) for successor in successors[event]), default=0)
        return memo[event]

    return max((visit(event) for event in events), default=0)


def _width(events: frozenset[Event], strict: frozenset[OrderPair]) -> int:
    ordered = tuple(sorted(events))
    for size in range(len(ordered), 0, -1):
        for subset in combinations(ordered, size):
            if _is_antichain(subset, strict):
                return size
    return 0


def _is_antichain(subset: tuple[Event, ...], strict: frozenset[OrderPair]) -> bool:
    for left, right in combinations(subset, 2):
        if (left, right) in strict or (right, left) in strict:
            return False
    return True


def _rank_profile(events: frozenset[Event], strict: frozenset[OrderPair]) -> tuple[int, ...]:
    predecessors = {event: {left for left, right in strict if right == event} for event in events}
    ranks: dict[Event, int] = {}

    def rank(event: Event) -> int:
        if event in ranks:
            return ranks[event]
        ranks[event] = 1 + max((rank(predecessor) for predecessor in predecessors[event]), default=0)
        return ranks[event]

    for event in events:
        rank(event)
    max_rank = max(ranks.values(), default=0)
    return tuple(sum(1 for value in ranks.values() if value == level) for level in range(1, max_rank + 1))


def _interval_summaries(
    events: frozenset[Event],
    strict: frozenset[OrderPair],
) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[str, int], ...], bool]:
    counts_by_size: dict[int, int] = {}
    profile_counts: dict[str, int] = {}
    profiles_by_size: dict[int, set[tuple[int, int]]] = {}

    for left, right in strict:
        interior = frozenset(
            event
            for event in events
            if (left, event) in strict and (event, right) in strict
        )
        size = len(interior)
        counts_by_size[size] = counts_by_size.get(size, 0) + 1
        if not interior:
            profile = (0, 0)
        else:
            interior_strict = frozenset(
                (a, b)
                for a, b in strict
                if a in interior and b in interior
            )
            profile = (_height(interior, interior_strict), _width(interior, interior_strict))
        profile_key = f"size={size};height={profile[0]};width={profile[1]}"
        profile_counts[profile_key] = profile_counts.get(profile_key, 0) + 1
        profiles_by_size.setdefault(size, set()).add(profile)

    profile_spread = any(
        size >= 2 and len(profiles) > 1
        for size, profiles in profiles_by_size.items()
    )
    return (
        tuple(sorted(counts_by_size.items())),
        tuple(sorted(profile_counts.items())),
        profile_spread,
    )


def _largest_incidence_fraction(
    events: frozenset[Event],
    pairs: frozenset[OrderPair],
) -> Fraction:
    if len(events) <= 1:
        return Fraction(0, 1)
    incident_counts = {
        event: sum(1 for left, right in pairs if event in {left, right})
        for event in events
    }
    return Fraction(max(incident_counts.values(), default=0), len(events) - 1)


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _audit_to_dict(audit: CausetAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "classification": audit.classification,
        "causal_set_candidate": audit.causal_set_candidate,
        "manifold_filter_passed": audit.manifold_filter_passed,
        "poset_report": _poset_report_to_dict(audit.poset_report),
        "diagnostics": (
            _diagnostics_to_dict(audit.diagnostics)
            if audit.diagnostics is not None
            else None
        ),
        "reason": audit.reason,
        "required_next": audit.required_next,
        "not_claimed": audit.not_claimed,
    }


def _poset_report_to_dict(report: PosetAxiomReport) -> dict[str, object]:
    return {
        "finite": report.finite,
        "reflexive": report.reflexive,
        "antisymmetric": report.antisymmetric,
        "transitive": report.transitive,
        "locally_finite": report.locally_finite,
        "failure_reasons": list(report.failure_reasons),
        "is_poset": report.is_poset,
    }


def _diagnostics_to_dict(diagnostics: CausetDiagnostics) -> dict[str, object]:
    return {
        "event_count": diagnostics.event_count,
        "strict_pair_count": diagnostics.strict_pair_count,
        "comparable_fraction": _fraction_to_dict(diagnostics.comparable_fraction),
        "cover_relation_count": diagnostics.cover_relation_count,
        "link_density": _fraction_to_dict(diagnostics.link_density),
        "height": diagnostics.height,
        "width": diagnostics.width,
        "rank_profile": list(diagnostics.rank_profile),
        "interval_counts_by_size": [
            {"size": size, "count": count}
            for size, count in diagnostics.interval_counts_by_size
        ],
        "interval_profile_counts": [
            {"profile": profile, "count": count}
            for profile, count in diagnostics.interval_profile_counts
        ],
        "largest_comparable_hub_fraction": _fraction_to_dict(
            diagnostics.largest_comparable_hub_fraction
        ),
        "largest_cover_hub_fraction": _fraction_to_dict(
            diagnostics.largest_cover_hub_fraction
        ),
        "profile_spread_obstruction": diagnostics.profile_spread_obstruction,
    }


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t126_result_to_dict(run_t126_analysis()), indent=2))
