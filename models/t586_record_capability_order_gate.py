"""T586: record-capability order gate.

This gate uses T585 only as a source-owned physical capability input. It tests
whether executable task dependence on produced records yields a finite
pre-temporal partial order, and it keeps clock, entropy, causal, and
irreversibility overreads out of the verdict.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any, Iterable

from models import t585_landauer_physical_capability_gate as t585


ARTIFACT = "T586-record-capability-order-gate-v0.1"
VERDICT = "RECORD_CAPABILITY_ORDER_FINITE_PARTIAL_ORDER_REVIEW_ONLY"


@dataclass(frozen=True)
class CapabilityEvent:
    event_id: str
    produced_records: tuple[str, ...]
    required_records: tuple[str, ...]
    executable_tasks: tuple[str, ...]
    clock_label: int
    entropy_rank: float
    causal_parents: tuple[str, ...]
    irreversible_operation: bool


@dataclass(frozen=True)
class DependencyEdge:
    source_event: str
    target_event: str
    record_id: str
    task_id: str


@dataclass(frozen=True)
class OrderReport:
    direct_edges: tuple[DependencyEdge, ...]
    closure: tuple[tuple[str, str], ...]
    missing_required_records: tuple[str, ...]
    irreflexive: bool
    transitive: bool
    antisymmetric: bool
    strict_partial_order: bool
    failure_class: str


@dataclass(frozen=True)
class OrderAudit:
    audit_id: str
    passed: bool
    relation: str
    reason: str


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class T586Result:
    artifact: str
    source_input: str
    source_input_checks: tuple[Check, ...]
    events: tuple[CapabilityEvent, ...]
    order_report: OrderReport
    cycle_counterexample: OrderReport
    audits: tuple[OrderAudit, ...]
    checks: tuple[Check, ...]
    theorem_statement: str
    physical_result: str
    verdict: str
    claim_ledger_update: str
    not_claimed: str
    next_work: str


Relation = frozenset[tuple[str, str]]


def record_dependency_edges(events: Iterable[CapabilityEvent]) -> tuple[DependencyEdge, ...]:
    event_list = tuple(events)
    producers = _producer_map(event_list)
    edges: list[DependencyEdge] = []
    for event in event_list:
        for record_id in event.required_records:
            producer = producers.get(record_id)
            if producer is None:
                continue
            for task_id in event.executable_tasks:
                edges.append(
                    DependencyEdge(
                        source_event=producer,
                        target_event=event.event_id,
                        record_id=record_id,
                        task_id=task_id,
                    )
                )
    return tuple(edges)


def build_order_report(events: Iterable[CapabilityEvent]) -> OrderReport:
    event_list = tuple(events)
    event_ids = tuple(event.event_id for event in event_list)
    edges = record_dependency_edges(event_list)
    direct = frozenset((edge.source_event, edge.target_event) for edge in edges)
    closure = transitive_closure(event_ids, direct)
    missing = _missing_required_records(event_list)
    irreflexive = all((event_id, event_id) not in closure for event_id in event_ids)
    transitive = _is_transitive(closure)
    antisymmetric = all((b, a) not in closure for a, b in closure if a != b)
    strict = irreflexive and transitive and antisymmetric and not missing
    if missing:
        failure = "MISSING_REQUIRED_RECORD"
    elif not irreflexive:
        failure = "CIRCULAR_RECORD_DEPENDENCY"
    elif not antisymmetric:
        failure = "SYMMETRIC_RECORD_DEPENDENCY"
    elif not transitive:
        failure = "NONTRANSITIVE_CLOSURE"
    else:
        failure = "NONE"
    return OrderReport(
        direct_edges=edges,
        closure=tuple(sorted(closure)),
        missing_required_records=missing,
        irreflexive=irreflexive,
        transitive=transitive,
        antisymmetric=antisymmetric,
        strict_partial_order=strict,
        failure_class=failure,
    )


def transitive_closure(event_ids: Iterable[str], relation: Relation) -> Relation:
    known = set(relation)
    ids = tuple(event_ids)
    changed = True
    while changed:
        changed = False
        additions = {
            (a, d)
            for a, b in known
            for c, d in known
            if b == c and (a, d) not in known
        }
        if additions:
            known.update(additions)
            changed = True
    return frozenset((a, b) for a, b in known if a in ids and b in ids)


def causal_relation(events: Iterable[CapabilityEvent]) -> Relation:
    event_list = tuple(events)
    direct = frozenset(
        (parent, event.event_id)
        for event in event_list
        for parent in event.causal_parents
    )
    return transitive_closure((event.event_id for event in event_list), direct)


def clock_label_relation(events: Iterable[CapabilityEvent]) -> Relation:
    event_list = tuple(events)
    return frozenset(
        (left.event_id, right.event_id)
        for left in event_list
        for right in event_list
        if left.clock_label < right.clock_label
    )


def entropy_rank_relation(events: Iterable[CapabilityEvent]) -> Relation:
    event_list = tuple(events)
    return frozenset(
        (left.event_id, right.event_id)
        for left in event_list
        for right in event_list
        if left.entropy_rank < right.entropy_rank
    )


def irreversible_edge_exists_outside_irreversible_flag(
    events: Iterable[CapabilityEvent], edges: Iterable[DependencyEdge]
) -> bool:
    by_id = {event.event_id: event for event in events}
    return any(
        not by_id[edge.source_event].irreversible_operation
        and not by_id[edge.target_event].irreversible_operation
        for edge in edges
    )


def run_t586_analysis() -> T586Result:
    source = t585.run_t585_analysis()
    events = _landauer_record_events()
    order = build_order_report(events)
    cycle = build_order_report(_cyclic_record_events())
    closure = frozenset(order.closure)
    permuted = tuple(
        replace(event, clock_label=100 - event.clock_label) for event in events
    )
    permuted_order = build_order_report(permuted)
    clock_relation = clock_label_relation(events)
    entropy_relation = entropy_rank_relation(events)
    causal = causal_relation(events)
    expected_closure = frozenset(
        {
            ("seed_known_record", "copy_known_record"),
            ("seed_known_record", "erase_standard_record"),
            ("seed_known_record", "certify_erased_record"),
            ("copy_known_record", "erase_standard_record"),
            ("copy_known_record", "certify_erased_record"),
            ("erase_standard_record", "certify_erased_record"),
        }
    )
    source_checks = (
        Check(
            "t585_verdict_available",
            source.verdict == t585.VERDICT,
            "T585 supplies the review-only Landauer physical capability fixture.",
        ),
        Check(
            "t585_erasure_capability_nontrivial",
            _has_t585_task(source, "known_zero_record", "erase_to_standard_record")
            and not _has_t585_task(
                source, "max_entropy_record", "erase_to_standard_record"
            ),
            "The fixed T585 work budget distinguishes erasure capability for known and max-entropy records.",
        ),
    )
    audits = (
        OrderAudit(
            "record_dependency_partial_order",
            order.strict_partial_order and closure == expected_closure,
            "STRICT_PARTIAL_ORDER" if order.strict_partial_order else order.failure_class,
            "The produced-record dependency closure is irreflexive, transitive, antisymmetric, and matches the preregistered finite fixture.",
        ),
        OrderAudit(
            "cycle_counterexample_rejected",
            not cycle.strict_partial_order
            and cycle.failure_class == "CIRCULAR_RECORD_DEPENDENCY",
            cycle.failure_class,
            "A two-event mutual record requirement creates reflexive closure and is rejected as circular.",
        ),
        OrderAudit(
            "clock_label_control",
            frozenset(permuted_order.closure) == closure
            and clock_relation != closure,
            "CLOCK_LABELS_NOT_USED",
            "Permuting presentation clock labels leaves the record order unchanged, and the clock-label total order is different.",
        ),
        OrderAudit(
            "entropy_scalar_control",
            entropy_relation != closure,
            "NOT_ENTROPY_SCALAR_ORDER",
            "The event entropy ranks do not reproduce the record-dependency partial order.",
        ),
        OrderAudit(
            "causal_overread_control",
            causal != closure and closure.issubset(causal),
            "STRICT_SUBRELATION_OF_SUPPLIED_CAUSAL_ORDER",
            "The supplied causal relation contains extra ordinary-causal edges not licensed by executable record dependence.",
        ),
        OrderAudit(
            "irreversible_computation_control",
            irreversible_edge_exists_outside_irreversible_flag(events, order.direct_edges),
            "NOT_REDUCED_TO_IRREVERSIBLE_OPERATION_FLAG",
            "At least one record-dependency edge connects two non-irreversible operations, so the order is not only an irreversibility flag.",
        ),
    )
    checks = source_checks + (
        Check(
            "all_events_executable_from_produced_records",
            not order.missing_required_records,
            "Every required record in the fixture is produced inside the declared event set.",
        ),
        Check(
            "record_order_is_partial_not_total",
            order.strict_partial_order
            and ("prepare_biased_reference", "seed_known_record") not in closure
            and ("seed_known_record", "prepare_biased_reference") not in closure,
            "The independent biased-reference event remains incomparable with the main chain.",
        ),
        Check(
            "controls_pass",
            all(audit.passed for audit in audits),
            "The partial-order result survives the cycle, clock, entropy, causal, and irreversibility controls.",
        ),
    )
    verdict = VERDICT if all(check.passed for check in checks) else "T586_GATE_FAILED"
    return T586Result(
        artifact=ARTIFACT,
        source_input="T585 Landauer physical capability gate, used as review-only source-owned physical input.",
        source_input_checks=source_checks,
        events=events,
        order_report=order,
        cycle_counterexample=cycle,
        audits=audits,
        checks=checks,
        theorem_statement=(
            "Finite theorem: for a finite event set with unique produced-record "
            "ownership, no missing required records, and an acyclic produced-record "
            "dependency graph, the strict transitive closure of executable "
            "task dependencies is a strict partial order. A record-dependency "
            "cycle is the finite counterexample boundary."
        ),
        physical_result=(
            "In the T585 one-bit memory fixture, produced-record dependence gives "
            "a noncircular finite event order for seed, copy, erase, and certify "
            "tasks while leaving an independent biased-reference event incomparable. "
            "The relation is invariant to clock-label presentation and is not the "
            "entropy scalar order, the supplied causal-order superset, or an "
            "irreversible-operation flag."
        ),
        verdict=verdict,
        claim_ledger_update="No claim-ledger or Canon Index update is earned.",
        not_claimed=(
            "T586 does not derive physical time, prove temporal issuance, replace "
            "causal order, establish a universal capability measure, promote TAF3 "
            "or TAF8, move S1, assert source-law novelty, change public posture, "
            "publish externally, or move cross-repo truth."
        ),
        next_work=(
            "Without a provenance-valid frozen p2c witness packet or a new "
            "physical source packet, the active lane has no higher-ranked "
            "unblocked hourly item. Future work should adjudicate such a packet "
            "or attack T586 with a stronger circularity, causal-collapse, or "
            "physical-naturalness counterexample."
        ),
    )


def _producer_map(events: Iterable[CapabilityEvent]) -> dict[str, str]:
    producers: dict[str, str] = {}
    for event in events:
        for record_id in event.produced_records:
            if record_id in producers:
                raise ValueError(f"record produced twice: {record_id}")
            producers[record_id] = event.event_id
    return producers


def _missing_required_records(events: Iterable[CapabilityEvent]) -> tuple[str, ...]:
    event_list = tuple(events)
    producers = _producer_map(event_list)
    missing = sorted(
        {
            record_id
            for event in event_list
            for record_id in event.required_records
            if record_id not in producers
        }
    )
    return tuple(missing)


def _is_transitive(relation: Relation) -> bool:
    return all(
        (a, d) in relation
        for a, b in relation
        for c, d in relation
        if b == c
    )


def _has_t585_task(result: t585.T585Result, state_id: str, task_id: str) -> bool:
    return any(
        envelope.state_id == state_id
        and any(point.task_id == task_id for point in envelope.points)
        for envelope in result.envelopes
    )


def _landauer_record_events() -> tuple[CapabilityEvent, ...]:
    return (
        CapabilityEvent(
            event_id="seed_known_record",
            produced_records=("r_known_zero",),
            required_records=(),
            executable_tasks=("certify_record_stability",),
            clock_label=20,
            entropy_rank=0.10,
            causal_parents=(),
            irreversible_operation=False,
        ),
        CapabilityEvent(
            event_id="copy_known_record",
            produced_records=("r_copied_zero",),
            required_records=("r_known_zero",),
            executable_tasks=("copy_stable_record",),
            clock_label=10,
            entropy_rank=0.70,
            causal_parents=("seed_known_record",),
            irreversible_operation=False,
        ),
        CapabilityEvent(
            event_id="erase_standard_record",
            produced_records=("r_erased_standard",),
            required_records=("r_copied_zero",),
            executable_tasks=("erase_to_standard_record",),
            clock_label=40,
            entropy_rank=0.20,
            causal_parents=("copy_known_record",),
            irreversible_operation=True,
        ),
        CapabilityEvent(
            event_id="certify_erased_record",
            produced_records=("r_erasure_certificate",),
            required_records=("r_erased_standard",),
            executable_tasks=("certify_record_stability",),
            clock_label=30,
            entropy_rank=0.40,
            causal_parents=("erase_standard_record", "prepare_biased_reference"),
            irreversible_operation=False,
        ),
        CapabilityEvent(
            event_id="prepare_biased_reference",
            produced_records=("r_biased_reference",),
            required_records=(),
            executable_tasks=("certify_record_stability",),
            clock_label=50,
            entropy_rank=0.30,
            causal_parents=("seed_known_record",),
            irreversible_operation=False,
        ),
    )


def _cyclic_record_events() -> tuple[CapabilityEvent, ...]:
    return (
        CapabilityEvent(
            event_id="cycle_a",
            produced_records=("r_a",),
            required_records=("r_b",),
            executable_tasks=("use_b",),
            clock_label=1,
            entropy_rank=0.1,
            causal_parents=(),
            irreversible_operation=False,
        ),
        CapabilityEvent(
            event_id="cycle_b",
            produced_records=("r_b",),
            required_records=("r_a",),
            executable_tasks=("use_a",),
            clock_label=2,
            entropy_rank=0.2,
            causal_parents=(),
            irreversible_operation=False,
        ),
    )


def result_to_dict(result: T586Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_input": result.source_input,
        "source_input_checks": [asdict(item) for item in result.source_input_checks],
        "events": [asdict(item) for item in result.events],
        "order_report": _order_report_to_dict(result.order_report),
        "cycle_counterexample": _order_report_to_dict(result.cycle_counterexample),
        "audits": [asdict(item) for item in result.audits],
        "checks": [asdict(item) for item in result.checks],
        "theorem_statement": result.theorem_statement,
        "physical_result": result.physical_result,
        "verdict": result.verdict,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
        "next_work": result.next_work,
    }


def _order_report_to_dict(report: OrderReport) -> dict[str, Any]:
    return {
        "direct_edges": [asdict(item) for item in report.direct_edges],
        "closure": [list(item) for item in report.closure],
        "missing_required_records": list(report.missing_required_records),
        "irreflexive": report.irreflexive,
        "transitive": report.transitive,
        "antisymmetric": report.antisymmetric,
        "strict_partial_order": report.strict_partial_order,
        "failure_class": report.failure_class,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T586 Results: Record-Capability Order Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source input: {payload['source_input']}",
        "",
        "## Theorem Boundary",
        "",
        payload["theorem_statement"],
        "",
        "## Direct Record Dependencies",
        "",
        "| source | target | record | task |",
        "| --- | --- | --- | --- |",
    ]
    for edge in payload["order_report"]["direct_edges"]:
        lines.append(
            f"| `{edge['source_event']}` | `{edge['target_event']}` | "
            f"`{edge['record_id']}` | `{edge['task_id']}` |"
        )
    lines.extend(
        [
            "",
            "## Audits",
            "",
            "| audit | passed? | relation | reason |",
            "| --- | :---: | --- | --- |",
        ]
    )
    for item in payload["audits"]:
        lines.append(
            f"| `{item['audit_id']}` | {item['passed']} | "
            f"`{item['relation']}` | {item['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Checks",
            "",
            "| check | passed? | reason |",
            "| --- | :---: | --- |",
        ]
    )
    for item in payload["checks"]:
        lines.append(f"| `{item['check_id']}` | {item['passed']} | {item['reason']} |")
    lines.extend(
        [
            "",
            "## Physical Result",
            "",
            payload["physical_result"],
            "",
            "## Claim Status",
            "",
            payload["claim_ledger_update"],
            "",
            "## Not Claimed",
            "",
            payload["not_claimed"],
            "",
            "## Next Work",
            "",
            payload["next_work"],
            "",
        ]
    )
    return "\n".join(lines)


def write_results(result: T586Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = result_to_dict(result)
    (results_dir / f"{ARTIFACT}.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (results_dir / f"{ARTIFACT}-results.md").write_text(
        render_markdown(payload), encoding="utf-8"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)
    result = run_t586_analysis()
    if args.write_results:
        write_results(result)
    print(json.dumps(result_to_dict(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
