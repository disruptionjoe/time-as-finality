"""T172: issuance-to-finality bridge audit.

This module tests a narrow bridge suggested by the Temporal Issuance note:
source-side realization order may project into observer-side TaF finality
data, but observer finality should not be treated as the source order itself.

The fixtures are finite and intentionally hostile. They ask whether a TaF
readout preserves source-order, source-measure, access, and gluing capability
objects, or whether the apparent arrow is coming from cadence, observer
boundary, hidden source structure, or missing reconciliation data.
"""

from __future__ import annotations

from dataclasses import dataclass


Edge = tuple[str, str]


@dataclass(frozen=True)
class ObserverRecord:
    observer: str
    event_id: str
    local_tick: int
    payload: str = "record"


@dataclass(frozen=True)
class IssuanceScenario:
    scenario_id: str
    events: tuple[str, ...]
    source_edges: tuple[Edge, ...]
    mu: tuple[tuple[str, int], ...]
    records: tuple[ObserverRecord, ...]
    gluing_edges: tuple[Edge, ...] = ()
    access_by_tick: tuple[tuple[int, tuple[str, ...]], ...] = ()


@dataclass(frozen=True)
class BridgeFixture:
    fixture_id: str
    fixture_kind: str
    task: str
    left: IssuanceScenario
    right: IssuanceScenario
    question: str


@dataclass(frozen=True)
class BridgeAudit:
    fixture_id: str
    fixture_kind: str
    task: str
    same_source_order: bool
    same_observer_records: bool
    same_taf_readout_edges: bool
    same_mu: bool
    finality_profile_split: bool
    source_capability_split: bool
    taf_readout_split: bool
    left_source_order_recovered: bool
    right_source_order_recovered: bool
    left_access_scores: tuple[tuple[int, int], ...]
    right_access_scores: tuple[tuple[int, int], ...]
    left_access_monotone: bool
    right_access_monotone: bool
    h7_source_arrow_upgrade_candidate: bool
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T172Result:
    audits: tuple[BridgeAudit, ...]
    reflection_controls: tuple[str, ...]
    cadence_boundaries: tuple[str, ...]
    source_capability_losses: tuple[str, ...]
    mu_invisible_losses: tuple[str, ...]
    access_boundary_cases: tuple[str, ...]
    gluing_failures: tuple[str, ...]
    h7_arrow_candidates: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


def scenario_source_order(scenario: IssuanceScenario) -> tuple[Edge, ...]:
    return transitive_closure(scenario.events, scenario.source_edges)


def scenario_readout_edges(scenario: IssuanceScenario) -> tuple[Edge, ...]:
    raw_edges = set(scenario.gluing_edges)
    by_observer: dict[str, list[ObserverRecord]] = {}
    for record in scenario.records:
        by_observer.setdefault(record.observer, []).append(record)

    for records in by_observer.values():
        ordered = sorted(records, key=lambda record: (record.local_tick, record.event_id))
        for index, earlier in enumerate(ordered):
            for later in ordered[index + 1 :]:
                if earlier.local_tick < later.local_tick and earlier.event_id != later.event_id:
                    raw_edges.add((earlier.event_id, later.event_id))

    return transitive_closure(scenario.events, tuple(sorted(raw_edges)))


def source_order_recovered_by_readout(scenario: IssuanceScenario) -> bool:
    visible = set(visible_events(scenario))
    source_visible = {
        edge
        for edge in scenario_source_order(scenario)
        if edge[0] in visible and edge[1] in visible
    }
    readout = set(scenario_readout_edges(scenario))
    source = set(scenario_source_order(scenario))

    return source_visible <= readout and readout <= source


def visible_events(scenario: IssuanceScenario) -> tuple[str, ...]:
    return tuple(sorted({record.event_id for record in scenario.records}))


def observer_record_signature(scenario: IssuanceScenario) -> tuple[tuple[str, str, int, str], ...]:
    return tuple(
        sorted(
            (
                record.observer,
                record.event_id,
                record.local_tick,
                record.payload,
            )
            for record in scenario.records
        )
    )


def mu_signature(scenario: IssuanceScenario) -> tuple[tuple[str, int], ...]:
    return tuple(sorted(scenario.mu))


def finality_profile(scenario: IssuanceScenario) -> tuple[tuple[int, int], ...]:
    if scenario.access_by_tick:
        return tuple(
            (tick, len(set(events)))
            for tick, events in sorted(scenario.access_by_tick, key=lambda item: item[0])
        )

    ticks = sorted({record.local_tick for record in scenario.records})
    profile: list[tuple[int, int]] = []
    for tick in ticks:
        available = {
            record.event_id
            for record in scenario.records
            if record.local_tick <= tick
        }
        profile.append((tick, len(available)))
    return tuple(profile)


def capability_key(scenario: IssuanceScenario, task: str, *, source: bool) -> object:
    if source:
        order_key: object = (scenario.events, scenario_source_order(scenario))
        if task == "source_mu_profile":
            return (order_key, mu_signature(scenario))
        return order_key

    readout_key: object = (visible_events(scenario), scenario_readout_edges(scenario))
    if task == "observer_finality_profile":
        return (readout_key, finality_profile(scenario))
    return readout_key


def is_monotone_score(profile: tuple[tuple[int, int], ...]) -> bool:
    scores = [score for _, score in profile]
    return all(next_score >= score for score, next_score in zip(scores, scores[1:]))


def transitive_closure(events: tuple[str, ...], edges: tuple[Edge, ...]) -> tuple[Edge, ...]:
    event_set = set(events)
    adjacency: dict[str, set[str]] = {event: set() for event in events}
    for start, end in edges:
        if start not in event_set or end not in event_set:
            raise ValueError(f"edge {(start, end)!r} refers to an unknown event")
        if start != end:
            adjacency[start].add(end)

    closure: set[Edge] = set()
    for start in events:
        stack = list(adjacency[start])
        visited: set[str] = set()
        while stack:
            end = stack.pop()
            if end in visited:
                continue
            visited.add(end)
            if start != end:
                closure.add((start, end))
            stack.extend(adjacency[end] - visited)

    return tuple(sorted(closure))


def bridge_fixture_family() -> tuple[BridgeFixture, ...]:
    positive = IssuanceScenario(
        scenario_id="sound_chain",
        events=("a", "b", "c"),
        source_edges=(("a", "b"), ("b", "c")),
        mu=(("a", 1), ("b", 1), ("c", 1)),
        records=(
            ObserverRecord("O", "a", 0),
            ObserverRecord("O", "b", 1),
            ObserverRecord("O", "c", 2),
        ),
    )

    cadence_fast = positive
    cadence_slow = IssuanceScenario(
        scenario_id="sound_chain_slow_cadence",
        events=("a", "b", "c"),
        source_edges=(("a", "b"), ("b", "c")),
        mu=(("a", 1), ("b", 1), ("c", 1)),
        records=(
            ObserverRecord("O", "a", 0),
            ObserverRecord("O", "b", 2),
            ObserverRecord("O", "c", 4),
        ),
    )

    hidden_before_c = IssuanceScenario(
        scenario_id="hidden_issuance_before_c",
        events=("a", "c", "h"),
        source_edges=(("a", "c"), ("h", "c")),
        mu=(("a", 1), ("c", 1), ("h", 3)),
        records=(ObserverRecord("O", "a", 0), ObserverRecord("O", "c", 1)),
    )
    hidden_independent = IssuanceScenario(
        scenario_id="hidden_issuance_independent",
        events=("a", "c", "h"),
        source_edges=(("a", "c"),),
        mu=(("a", 1), ("c", 1), ("h", 3)),
        records=(ObserverRecord("O", "a", 0), ObserverRecord("O", "c", 1)),
    )

    mu_low = IssuanceScenario(
        scenario_id="same_order_low_mu",
        events=("a", "b", "c"),
        source_edges=(("a", "b"), ("a", "c")),
        mu=(("a", 1), ("b", 1), ("c", 1)),
        records=(
            ObserverRecord("O", "a", 0),
            ObserverRecord("O", "b", 1),
            ObserverRecord("O", "c", 1),
        ),
    )
    mu_high = IssuanceScenario(
        scenario_id="same_order_high_mu",
        events=("a", "b", "c"),
        source_edges=(("a", "b"), ("a", "c")),
        mu=(("a", 5), ("b", 1), ("c", 1)),
        records=(
            ObserverRecord("O", "a", 0),
            ObserverRecord("O", "b", 1),
            ObserverRecord("O", "c", 1),
        ),
    )

    access_monotone = IssuanceScenario(
        scenario_id="monotone_access_readout",
        events=("a", "b", "c"),
        source_edges=(("a", "b"), ("b", "c")),
        mu=(("a", 1), ("b", 1), ("c", 1)),
        records=(
            ObserverRecord("O", "a", 0),
            ObserverRecord("O", "b", 1),
            ObserverRecord("O", "c", 3),
        ),
        access_by_tick=((0, ("a",)), (1, ("a", "b")), (2, ("a", "b")), (3, ("a", "b", "c"))),
    )
    access_loss = IssuanceScenario(
        scenario_id="nonmonotone_access_loss",
        events=("a", "b", "c"),
        source_edges=(("a", "b"), ("b", "c")),
        mu=(("a", 1), ("b", 1), ("c", 1)),
        records=(
            ObserverRecord("O", "a", 0),
            ObserverRecord("O", "b", 1),
            ObserverRecord("O", "c", 3),
        ),
        access_by_tick=((0, ("a",)), (1, ("a", "b")), (2, ("a",)), (3, ("a", "c"))),
    )

    a_before_b = IssuanceScenario(
        scenario_id="a_before_b_without_gluing",
        events=("a", "b"),
        source_edges=(("a", "b"),),
        mu=(("a", 1), ("b", 1)),
        records=(ObserverRecord("OA", "a", 0), ObserverRecord("OB", "b", 0)),
    )
    b_before_a = IssuanceScenario(
        scenario_id="b_before_a_without_gluing",
        events=("a", "b"),
        source_edges=(("b", "a"),),
        mu=(("a", 1), ("b", 1)),
        records=(ObserverRecord("OA", "a", 0), ObserverRecord("OB", "b", 0)),
    )

    return (
        BridgeFixture(
            fixture_id="sound_record_generation_reflection_control",
            fixture_kind="positive_reflection_control",
            task="source_order_reconstruction",
            left=positive,
            right=positive,
            question="Does a sound single-observer record chain recover visible source order?",
        ),
        BridgeFixture(
            fixture_id="same_issuance_different_cadence",
            fixture_kind="cadence_boundary",
            task="source_order_reconstruction",
            left=cadence_fast,
            right=cadence_slow,
            question="Can cadence change apparent finality without changing source order?",
        ),
        BridgeFixture(
            fixture_id="same_records_different_hidden_issuance",
            fixture_kind="hidden_source_loss",
            task="source_order_reconstruction",
            left=hidden_before_c,
            right=hidden_independent,
            question="Can identical observer records hide different source realization order?",
        ),
        BridgeFixture(
            fixture_id="same_issuance_records_different_mu",
            fixture_kind="mu_invisible_loss",
            task="source_mu_profile",
            left=mu_low,
            right=mu_high,
            question="Is mu decorative for finality readout, or task-relevant source data?",
        ),
        BridgeFixture(
            fixture_id="nonmonotone_access_loss",
            fixture_kind="access_boundary",
            task="source_order_reconstruction",
            left=access_monotone,
            right=access_loss,
            question="Does nonmonotone finality support come from source order or observer access?",
        ),
        BridgeFixture(
            fixture_id="gluing_failure_global_order_not_assumed",
            fixture_kind="gluing_failure",
            task="source_order_reconstruction",
            left=a_before_b,
            right=b_before_a,
            question="Can local records without gluing determine global source order?",
        ),
    )


def audit_bridge_fixture(fixture: BridgeFixture) -> BridgeAudit:
    left_source_key = capability_key(fixture.left, fixture.task, source=True)
    right_source_key = capability_key(fixture.right, fixture.task, source=True)
    left_readout_key = capability_key(fixture.left, fixture.task, source=False)
    right_readout_key = capability_key(fixture.right, fixture.task, source=False)
    left_profile = finality_profile(fixture.left)
    right_profile = finality_profile(fixture.right)

    same_source_order = (
        fixture.left.events == fixture.right.events
        and scenario_source_order(fixture.left) == scenario_source_order(fixture.right)
    )
    same_records = observer_record_signature(fixture.left) == observer_record_signature(fixture.right)
    same_readout = scenario_readout_edges(fixture.left) == scenario_readout_edges(fixture.right)
    same_mu = mu_signature(fixture.left) == mu_signature(fixture.right)
    source_split = left_source_key != right_source_key
    readout_split = left_readout_key != right_readout_key
    finality_split = left_profile != right_profile
    left_recovered = source_order_recovered_by_readout(fixture.left)
    right_recovered = source_order_recovered_by_readout(fixture.right)
    left_access_monotone = is_monotone_score(left_profile)
    right_access_monotone = is_monotone_score(right_profile)
    verdict = _verdict_for_fixture(
        fixture=fixture,
        source_split=source_split,
        readout_split=readout_split,
        finality_split=finality_split,
        left_recovered=left_recovered,
        right_recovered=right_recovered,
        right_access_monotone=right_access_monotone,
    )

    return BridgeAudit(
        fixture_id=fixture.fixture_id,
        fixture_kind=fixture.fixture_kind,
        task=fixture.task,
        same_source_order=same_source_order,
        same_observer_records=same_records,
        same_taf_readout_edges=same_readout,
        same_mu=same_mu,
        finality_profile_split=finality_split,
        source_capability_split=source_split,
        taf_readout_split=readout_split,
        left_source_order_recovered=left_recovered,
        right_source_order_recovered=right_recovered,
        left_access_scores=left_profile,
        right_access_scores=right_profile,
        left_access_monotone=left_access_monotone,
        right_access_monotone=right_access_monotone,
        h7_source_arrow_upgrade_candidate=False,
        verdict=verdict,
        interpretation=_interpretation(fixture, verdict),
    )


def run_t172_analysis() -> T172Result:
    audits = tuple(audit_bridge_fixture(fixture) for fixture in bridge_fixture_family())
    reflection_controls = _fixture_ids(audits, "positive_source_readout_reflection")
    cadence_boundaries = _fixture_ids(audits, "cadence_boundary_not_source_arrow")
    source_capability_losses = _fixture_ids(audits, "source_capability_lost_by_taf_readout")
    mu_invisible_losses = _fixture_ids(audits, "mu_invisible_to_taf_readout")
    access_boundary_cases = _fixture_ids(audits, "access_boundary_not_source_arrow")
    gluing_failures = _fixture_ids(audits, "gluing_failure_not_global_order")
    h7_candidates = tuple(
        audit.fixture_id for audit in audits if audit.h7_source_arrow_upgrade_candidate
    )

    return T172Result(
        audits=audits,
        reflection_controls=reflection_controls,
        cadence_boundaries=cadence_boundaries,
        source_capability_losses=source_capability_losses,
        mu_invisible_losses=mu_invisible_losses,
        access_boundary_cases=access_boundary_cases,
        gluing_failures=gluing_failures,
        h7_arrow_candidates=h7_candidates,
        strongest_claim=(
            "Finality can be a sound observer-side reflection of a source "
            "realization order only when record generation, access, cadence, "
            "and gluing data are fixed. The same finite TaF readout can lose "
            "hidden source order or source-measure data; cadence and access "
            "can change apparent finality without changing source order; and "
            "unglued local records do not determine a global realization order."
        ),
        improved=(
            "T172 turns the Temporal Issuance bridge into an executable "
            "projection-sufficiency audit. It supplies a positive reflection "
            "control plus hostile fixtures for cadence, hidden issuance, mu, "
            "access loss, and gluing."
        ),
        weakened=(
            "This weakens any H7 or TaF prose that reads finality as generating "
            "source-level temporal direction. At most, finality is currently a "
            "typed observer readout or certificate of source order under "
            "declared soundness and reconstruction conditions."
        ),
        falsification_condition=(
            "The bridge earns a stronger claim only if a non-gerrymandered "
            "source system and observer projection prove that TaF finality "
            "preserves the declared source capability across cadence changes, "
            "hidden issuance alternatives, mu-sensitive tasks, access loss, "
            "and gluing ambiguity without importing ordinary time, entropy, "
            "information growth, or a preferred global frontier."
        ),
        h7_update=(
            "Add T172 to H7 as a source/readout recast: H7 remains "
            "weakened_conditional. Finality-induced direction should be "
            "treated as an observer-side reflection or factorization test, not "
            "as source-level arrow generation."
        ),
        claim_ledger_update=(
            "T172 tests the Temporal Issuance bridge. A sound record chain can "
            "reflect visible source order, but same-readout hidden issuance, "
            "mu-sensitive source tasks, nonmonotone access, and missing gluing "
            "all block finality-alone source-arrow readings."
        ),
        open_blocker=(
            "No typed source dynamics for issuance order or mu has yet survived "
            "absorber tests against ordinary causal order, entropy, information "
            "growth, record reconstruction, or a hidden global frontier."
        ),
        suggested_next=(
            "Run an absorber map for Temporal Issuance against causal sets, "
            "block-universe causal order, stochastic thermodynamics, and "
            "information-theoretic growth before adding richer bridge models."
        ),
        not_claimed=(
            "T172 does not import Temporal Issuance as true, does not derive "
            "the thermodynamic arrow, does not replace physical time, and does "
            "not prove that records create source realization order."
        ),
    )


def t172_result_to_dict(result: T172Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "fixture_id": audit.fixture_id,
                "fixture_kind": audit.fixture_kind,
                "task": audit.task,
                "same_source_order": audit.same_source_order,
                "same_observer_records": audit.same_observer_records,
                "same_taf_readout_edges": audit.same_taf_readout_edges,
                "same_mu": audit.same_mu,
                "finality_profile_split": audit.finality_profile_split,
                "source_capability_split": audit.source_capability_split,
                "taf_readout_split": audit.taf_readout_split,
                "left_source_order_recovered": audit.left_source_order_recovered,
                "right_source_order_recovered": audit.right_source_order_recovered,
                "left_access_scores": list(audit.left_access_scores),
                "right_access_scores": list(audit.right_access_scores),
                "left_access_monotone": audit.left_access_monotone,
                "right_access_monotone": audit.right_access_monotone,
                "h7_source_arrow_upgrade_candidate": audit.h7_source_arrow_upgrade_candidate,
                "verdict": audit.verdict,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "reflection_controls": list(result.reflection_controls),
        "cadence_boundaries": list(result.cadence_boundaries),
        "source_capability_losses": list(result.source_capability_losses),
        "mu_invisible_losses": list(result.mu_invisible_losses),
        "access_boundary_cases": list(result.access_boundary_cases),
        "gluing_failures": list(result.gluing_failures),
        "h7_arrow_candidates": list(result.h7_arrow_candidates),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _fixture_ids(audits: tuple[BridgeAudit, ...], verdict: str) -> tuple[str, ...]:
    return tuple(audit.fixture_id for audit in audits if audit.verdict == verdict)


def _verdict_for_fixture(
    *,
    fixture: BridgeFixture,
    source_split: bool,
    readout_split: bool,
    finality_split: bool,
    left_recovered: bool,
    right_recovered: bool,
    right_access_monotone: bool,
) -> str:
    if fixture.fixture_kind == "positive_reflection_control":
        if left_recovered and right_recovered and not source_split:
            return "positive_source_readout_reflection"
        return "failed_reflection_control"
    if fixture.fixture_kind == "cadence_boundary":
        if fixture.left.source_edges == fixture.right.source_edges and finality_split:
            return "cadence_boundary_not_source_arrow"
    if fixture.fixture_kind == "hidden_source_loss":
        if source_split and not readout_split:
            return "source_capability_lost_by_taf_readout"
    if fixture.fixture_kind == "mu_invisible_loss":
        if source_split and not readout_split:
            return "mu_invisible_to_taf_readout"
    if fixture.fixture_kind == "access_boundary":
        if not right_access_monotone:
            return "access_boundary_not_source_arrow"
    if fixture.fixture_kind == "gluing_failure":
        if source_split and not readout_split:
            return "gluing_failure_not_global_order"
    return "unclassified_bridge_case"


def _interpretation(fixture: BridgeFixture, verdict: str) -> str:
    if verdict == "positive_source_readout_reflection":
        return (
            "The observer record chain is sound for visible source order. This "
            "is a reflection control, not evidence that finality generated the "
            "source order."
        )
    if verdict == "cadence_boundary_not_source_arrow":
        return (
            "The source order and readout order are unchanged while the local "
            "finality profile changes with observer cadence. The apparent "
            "timing is observer-side."
        )
    if verdict == "source_capability_lost_by_taf_readout":
        return (
            "Identical records and TaF readout edges hide a difference in "
            "source realization order. The source capability does not factor "
            "through the readout."
        )
    if verdict == "mu_invisible_to_taf_readout":
        return (
            "The same issuance order and observer records can carry different "
            "source mu data. Mu is decorative for plain finality order, but it "
            "is lost if the declared task needs source-measure information."
        )
    if verdict == "access_boundary_not_source_arrow":
        return (
            "The source order is unchanged while accessible finality support "
            "drops. The nonmonotonicity is an observer-boundary effect, not a "
            "source-arrow result."
        )
    if verdict == "gluing_failure_not_global_order":
        return (
            "The same unglued local records are compatible with different "
            "global source orders. Global order must be reconstructed by "
            "declared gluing data, not assumed."
        )
    return f"{fixture.fixture_id} did not match a declared bridge verdict."


if __name__ == "__main__":
    import json

    print(json.dumps(t172_result_to_dict(run_t172_analysis()), indent=2))
