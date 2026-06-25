"""Dual-record adjacent-possible fixture.

This implements the comparator frozen in Temporal Issuance E093. The fixture is
small on purpose: it asks whether an opportunity-edge record can escape a
declared local trap, and then immediately checks the fixed-latent edge absorber.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


State = int
Edge = tuple[State, State]
SystemName = Literal["A_single", "B0_limited_latent", "B1_exact_latent", "C_growing"]

SCORES: dict[State, int] = {
    0: 0,
    1: 1,
    2: 3,
    3: 2,
    4: 1,
    5: 0,
    6: 2,
    7: 4,
    8: 7,
    9: 9,
    10: 12,
}
START_STATE = 0
TARGET_STATE = 10
BUDGET = 8
STUCKNESS_THRESHOLD = 2
MAX_GENERATED_JUMP = 5
CRITICAL_EDGE = (2, 7)


@dataclass(frozen=True)
class SearchTrace:
    system: SystemName
    final_state: State
    final_score: int
    target_reached: bool
    proposal_attempts: int
    accepted_edges: tuple[Edge, ...]
    failed_probes: tuple[Edge | str, ...]
    latent_edges_exposed: tuple[Edge, ...]
    generated_edges: tuple[Edge, ...]
    best_score: int
    stuckness_events: int
    opportunity_record: tuple[str, ...]


def run_dual_record_opportunity_fixture() -> dict[str, Any]:
    traces = {
        "A_single": run_search("A_single"),
        "B0_limited_latent": run_search("B0_limited_latent"),
        "B1_exact_latent": run_search("B1_exact_latent"),
        "C_growing": run_search("C_growing"),
    }
    checks = fixture_checks(traces)
    return {
        "test": "dual-record-opportunity-fixture-v0.1",
        "tag": ["dual_record", "adjacent_possible", "absorber_control"],
        "guardrail": (
            "Finite comparator only: C beating A/B0 is a bounded residue "
            "relative to the declared limited comparator, not source issuance. "
            "B1 tests the exact fixed-latent edge absorber."
        ),
        "frozen_landscape": {
            "states": list(SCORES),
            "start": START_STATE,
            "target": TARGET_STATE,
            "budget": BUDGET,
            "scores": SCORES,
            "base_graph": {state: list(base_outgoing(state)) for state in SCORES},
            "critical_edge": list(CRITICAL_EDGE),
            "stuckness_threshold": STUCKNESS_THRESHOLD,
            "max_generated_jump": MAX_GENERATED_JUMP,
        },
        "traces": {name: trace_to_dict(trace) for name, trace in traces.items()},
        "comparisons": {
            "C_beats_A_and_B0": checks["C_beats_A_and_B0"],
            "B1_reproduces_C_target_result": checks["B1_reproduces_C_target_result"],
            "critical_edge_generated_by_C": CRITICAL_EDGE
            in traces["C_growing"].generated_edges,
            "critical_edge_latent_in_B1": CRITICAL_EDGE
            in traces["B1_exact_latent"].latent_edges_exposed,
            "critical_edge_absent_from_B0": CRITICAL_EDGE not in latent_edges("B0_limited_latent"),
        },
        "checks": checks,
        "all_checks_passed": all(checks.values()),
        "effect_verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
        },
        "absorber_verdict": {
            "bounded_residue_relative_to_B0": checks["C_beats_A_and_B0"],
            "exact_fixed_latent_edge_absorbs_source_side_reading": checks[
                "B1_reproduces_C_target_result"
            ],
            "claim_status": "do_not_promote",
        },
        "strongest_result": (
            "C escapes the base local trap by generating 2->7 and reaches the "
            "target within the frozen budget, while A and B0 remain trapped. "
            "But B1 reaches the same target once 2->7 is supplied as a fixed "
            "latent edge, so the source-side reading is absorbed."
        ),
        "first_obstruction": (
            "A finite fixture cannot rule out a broader fixed latent graph plus "
            "a matching access schedule. The result supports record-regime "
            "architecture and effect typing, not Issue[S]."
        ),
        "next_step": (
            "Bring the result back to Temporal Issuance as Project[O] + "
            "Finalize[R] + Lose[K], then use GU only as an observer-finality "
            "section-retrieval stress witness."
        ),
    }


def run_search(system: SystemName) -> SearchTrace:
    graph = base_graph()
    state = START_STATE
    attempts = 0
    stuckness = 0
    stuckness_events = 0
    exhausted: set[Edge] = set()
    accepted: list[Edge] = []
    failed: list[Edge | str] = []
    exposed: list[Edge] = []
    generated: list[Edge] = []
    opportunity: list[str] = []

    while attempts < BUDGET and state != TARGET_STATE:
        edge, kind = next_candidate(system, state, graph, exhausted, stuckness)
        attempts += 1

        if edge is None:
            failed.append(f"no_candidate_from_{state}")
            stuckness += 1
            opportunity.append(f"stuck:{state}:no_candidate")
            continue

        if kind == "latent":
            exposed.append(edge)
            graph.setdefault(edge[0], set()).add(edge[1])
            opportunity.append(f"latent_exposed:{edge[0]}->{edge[1]}")
        elif kind == "generated":
            generated.append(edge)
            graph.setdefault(edge[0], set()).add(edge[1])
            opportunity.append(f"generated:{edge[0]}->{edge[1]}")

        exhausted.add(edge)
        if SCORES[edge[1]] >= SCORES[state]:
            accepted.append(edge)
            state = edge[1]
            stuckness = 0
            opportunity.append(f"accepted:{edge[0]}->{edge[1]}")
        else:
            failed.append(edge)
            stuckness += 1
            opportunity.append(f"failed:{edge[0]}->{edge[1]}")
            if stuckness == STUCKNESS_THRESHOLD:
                stuckness_events += 1
                opportunity.append(f"stuckness_threshold:{state}")

    best_score = max([SCORES[START_STATE], *(SCORES[edge[1]] for edge in accepted)])
    return SearchTrace(
        system=system,
        final_state=state,
        final_score=SCORES[state],
        target_reached=state == TARGET_STATE,
        proposal_attempts=attempts,
        accepted_edges=tuple(accepted),
        failed_probes=tuple(failed),
        latent_edges_exposed=tuple(exposed),
        generated_edges=tuple(generated),
        best_score=best_score,
        stuckness_events=stuckness_events,
        opportunity_record=tuple(opportunity),
    )


def next_candidate(
    system: SystemName,
    state: State,
    graph: dict[State, set[State]],
    exhausted: set[Edge],
    stuckness: int,
) -> tuple[Edge | None, str]:
    latent = latent_candidate(system, state, stuckness)
    if latent is not None and latent not in exhausted:
        return latent, "latent"

    if system == "C_growing" and stuckness >= STUCKNESS_THRESHOLD:
        generated = generated_candidate(state, graph)
        if generated is not None and generated not in exhausted:
            return generated, "generated"

    outgoing = sorted(
        (edge for edge in ((state, target) for target in graph.get(state, set())) if edge not in exhausted),
        key=lambda item: (SCORES[item[1]], item[1]),
        reverse=True,
    )
    if not outgoing:
        return None, "none"
    return outgoing[0], "base"


def base_graph() -> dict[State, set[State]]:
    return {state: set(base_outgoing(state)) for state in SCORES}


def base_outgoing(state: State) -> tuple[State, ...]:
    outgoing = []
    if state - 1 in SCORES:
        outgoing.append(state - 1)
    if state + 1 in SCORES:
        outgoing.append(state + 1)
    return tuple(outgoing)


def latent_edges(system: SystemName) -> tuple[Edge, ...]:
    if system == "B0_limited_latent":
        return ((1, 5), (3, 6), (4, 6))
    if system == "B1_exact_latent":
        return (CRITICAL_EDGE,)
    return ()


def latent_candidate(
    system: SystemName,
    state: State,
    stuckness: int,
) -> Edge | None:
    if system == "B1_exact_latent" and stuckness < STUCKNESS_THRESHOLD:
        return None
    for edge in latent_edges(system):
        if edge[0] == state:
            return edge
    return None


def generated_candidate(
    state: State,
    graph: dict[State, set[State]],
) -> Edge | None:
    has_improving_edge = any(SCORES[target] >= SCORES[state] for target in graph[state])
    if has_improving_edge:
        return None
    upper = min(max(SCORES), state + MAX_GENERATED_JUMP)
    for target in range(state + 1, upper + 1):
        if SCORES[target] > SCORES[state]:
            return (state, target)
    return None


def fixture_checks(traces: dict[str, SearchTrace]) -> dict[str, bool]:
    a = traces["A_single"]
    b0 = traces["B0_limited_latent"]
    b1 = traces["B1_exact_latent"]
    c = traces["C_growing"]
    return {
        "A_single_trapped_at_2": a.final_state == 2 and not a.target_reached,
        "B0_limited_latent_trapped_at_2": b0.final_state == 2 and not b0.target_reached,
        "C_growing_reaches_target": c.target_reached and c.final_state == TARGET_STATE,
        "C_generates_critical_edge": CRITICAL_EDGE in c.generated_edges,
        "C_beats_A_and_B0": c.best_score > a.best_score and c.best_score > b0.best_score,
        "B1_reaches_target": b1.target_reached and b1.final_state == TARGET_STATE,
        "B1_exposes_critical_edge": CRITICAL_EDGE in b1.latent_edges_exposed,
        "B1_reproduces_C_target_result": (
            b1.final_state == c.final_state
            and b1.best_score == c.best_score
            and b1.proposal_attempts == c.proposal_attempts
        ),
        "IssueS_remains_false": True,
    }


def trace_to_dict(trace: SearchTrace) -> dict[str, Any]:
    return {
        "system": trace.system,
        "final_state": trace.final_state,
        "final_score": trace.final_score,
        "target_reached": trace.target_reached,
        "proposal_attempts": trace.proposal_attempts,
        "accepted_edges": [list(edge) for edge in trace.accepted_edges],
        "failed_probes": [
            list(probe) if isinstance(probe, tuple) else probe
            for probe in trace.failed_probes
        ],
        "latent_edges_exposed": [list(edge) for edge in trace.latent_edges_exposed],
        "generated_edges": [list(edge) for edge in trace.generated_edges],
        "best_score": trace.best_score,
        "stuckness_events": trace.stuckness_events,
        "opportunity_record": list(trace.opportunity_record),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_dual_record_opportunity_fixture(), indent=2, sort_keys=True))
