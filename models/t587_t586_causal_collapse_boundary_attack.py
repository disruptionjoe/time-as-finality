"""T587: T586 causal-collapse and boundary-input attack.

This gate reopens T586 as an attack. It asks whether the T586
record-capability order has any relation-level residue beyond ordinary
dependency or causal comparators on the same frozen event system, and it
separates record production from other boundary-input classes.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import t586_record_capability_order_gate as t586


ARTIFACT = "T587-t586-causal-collapse-boundary-attack-v0.1"
VERDICT = "T586_DOWNGRADED_TO_TYPED_RECORD_PREREQUISITE_FILTER_REVIEW_ONLY"


Relation = frozenset[tuple[str, str]]


@dataclass(frozen=True)
class ComparatorReport:
    comparator_id: str
    relation: tuple[tuple[str, str], ...]
    record_minus_comparator: tuple[tuple[str, str], ...]
    comparator_minus_record: tuple[tuple[str, str], ...]
    record_relation_status: str
    collapse_result: str
    reason: str


@dataclass(frozen=True)
class BoundaryInputClass:
    class_id: str
    classification: str
    counts_as_record_source: bool
    reason: str


@dataclass(frozen=True)
class AttackAudit:
    audit_id: str
    passed: bool
    result_class: str
    reason: str


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class T587Result:
    artifact: str
    source_gate: str
    source_verdict: str
    record_order: tuple[tuple[str, str], ...]
    comparators: tuple[ComparatorReport, ...]
    boundary_inputs: tuple[BoundaryInputClass, ...]
    audits: tuple[AttackAudit, ...]
    checks: tuple[Check, ...]
    adjudication: str
    physical_result: str
    verdict: str
    claim_ledger_update: str
    not_claimed: str
    next_work: str


def run_t587_analysis() -> T587Result:
    source = t586.run_t586_analysis()
    events = source.events
    record_order = frozenset(source.order_report.closure)

    direct_record_dependency = frozenset(
        (edge.source_event, edge.target_event)
        for edge in source.order_report.direct_edges
    )
    ordinary_dependency = t586.transitive_closure(
        (event.event_id for event in events), direct_record_dependency
    )
    causal_parent_direct = frozenset(
        (parent, event.event_id)
        for event in events
        for parent in event.causal_parents
    )
    strongest_standard_dependency = t586.transitive_closure(
        (event.event_id for event in events),
        direct_record_dependency | causal_parent_direct,
    )
    causal_order = t586.causal_relation(events)

    comparators = (
        _compare(
            "ordinary_task_prerequisite_dependency",
            record_order,
            ordinary_dependency,
            (
                "If ordinary dependency is allowed to mean task prerequisite on "
                "produced records, the T586 relation is exactly that dependency "
                "closure rather than a new relation type."
            ),
        ),
        _compare(
            "strongest_standard_dependency_order",
            record_order,
            strongest_standard_dependency,
            (
                "Adding all declared causal parents gives a strict superset of "
                "the record order; the extra edges are ordinary causal/input "
                "dependencies not licensed as executable record prerequisites."
            ),
        ),
        _compare(
            "supplied_causal_order",
            record_order,
            causal_order,
            (
                "The supplied causal order absorbs every record-order edge and "
                "adds nonrecord causal dependencies, so T586 cannot replace or "
                "out-rank causal order on this fixture."
            ),
        ),
        _compare(
            "clock_label_order",
            record_order,
            t586.clock_label_relation(events),
            "Clock labels disagree with the record order and remain only a presentation control.",
        ),
        _compare(
            "entropy_rank_order",
            record_order,
            t586.entropy_rank_relation(events),
            "Entropy ranks disagree with the record order and cannot supply the claimed relation.",
        ),
    )
    boundary_inputs = _boundary_input_classes()
    comparator_by_id = {item.comparator_id: item for item in comparators}
    admitted_boundary_ids = {
        item.class_id for item in boundary_inputs if item.counts_as_record_source
    }
    audits = (
        AttackAudit(
            "ordinary_dependency_collapse_detected",
            comparator_by_id[
                "ordinary_task_prerequisite_dependency"
            ].record_relation_status
            == "EQUAL",
            "COLLAPSES_TO_TASK_PREREQUISITE_DEPENDENCY",
            "The untyped task-prerequisite dependency comparator exactly reproduces T586.",
        ),
        AttackAudit(
            "strongest_dependency_absorbs_record_order",
            comparator_by_id[
                "strongest_standard_dependency_order"
            ].record_relation_status
            == "RECORD_SUBRELATION",
            "RECORD_ORDER_IS_TYPED_SUBRELATION",
            "The strongest standard dependency comparator strictly contains the T586 record order.",
        ),
        AttackAudit(
            "causal_order_absorbs_record_order",
            comparator_by_id["supplied_causal_order"].record_relation_status
            == "RECORD_SUBRELATION",
            "CAUSAL_SUPERSET_ABSORBS_RELATION",
            "Every T586 record-order edge is already causally ordered in the frozen fixture.",
        ),
        AttackAudit(
            "boundary_input_firebreak",
            admitted_boundary_ids
            == {"physical_record_production", "native_record_issuance_rule"},
            "ONLY_ISSUED_RECORDS_COUNT",
            "Access, intervention, section choice, flux, stochastic input, and observer readout are not counted without an issued record consumed by a task.",
        ),
    )
    checks = (
        Check(
            "source_t586_review_only_available",
            source.verdict == t586.VERDICT,
            "T586 supplies the finite review-only record-capability-order fixture.",
        ),
        Check(
            "dependency_and_causal_comparators_attacked",
            all(audit.passed for audit in audits[:3]),
            "The ordinary-dependency, strongest-dependency, and causal comparators all reach a definite collapse/absorption result.",
        ),
        Check(
            "boundary_classes_are_typed",
            audits[3].passed,
            "The boundary-input screen admits only explicit record production or native record issuance.",
        ),
        Check(
            "no_relation_level_residual_claimed",
            all(audit.passed for audit in audits),
            "The only survivor is a typed filter over standard dependency/causal structure, not a new temporal relation.",
        ),
    )
    verdict = VERDICT if all(check.passed for check in checks) else "T587_ATTACK_FAILED"
    return T587Result(
        artifact=ARTIFACT,
        source_gate=source.artifact,
        source_verdict=source.verdict,
        record_order=_sorted_relation(record_order),
        comparators=comparators,
        boundary_inputs=boundary_inputs,
        audits=audits,
        checks=checks,
        adjudication=(
            "T587 returns a downgrade. T586 has no relation-level residual beyond "
            "ordinary task-prerequisite dependency and is absorbed by the strongest "
            "standard dependency and causal comparators on the frozen event system. "
            "What survives is a typed record-prerequisite filter: it identifies which "
            "causal dependencies are issued-record prerequisites for executable tasks."
        ),
        physical_result=(
            "The T586 Landauer fixture still distinguishes issued records from "
            "access changes, interventions, observer readouts, stochastic inputs, "
            "continuous flux, and section choices. That distinction is useful as a "
            "screen against boundary-input overread, but it does not derive physical "
            "time or an independent temporal order."
        ),
        verdict=verdict,
        claim_ledger_update="No claim-ledger or Canon Index update is earned.",
        not_claimed=(
            "T587 does not prove time, temporal issuance, source-law novelty, "
            "causal-order replacement, a universal capability measure, TAF3, TAF8, "
            "S1, public-posture movement, external publication, or cross-repo truth."
        ),
        next_work=(
            "Do not continue producing T-number scaffolds from T586 alone. Reopen "
            "Lane 1 only for a provenance-valid physical source packet, a frozen "
            "capability witness, or a sharper counterexample that changes the "
            "record-issuance contract."
        ),
    )


def _compare(
    comparator_id: str,
    record_order: Relation,
    comparator: Relation,
    reason: str,
) -> ComparatorReport:
    record_minus = record_order - comparator
    comparator_minus = comparator - record_order
    if not record_minus and not comparator_minus:
        status = "EQUAL"
        collapse = "RELATION_LEVEL_COLLAPSE"
    elif not record_minus:
        status = "RECORD_SUBRELATION"
        collapse = "ABSORBED_AS_TYPED_SUBRELATION"
    elif not comparator_minus:
        status = "RECORD_SUPERRELATION"
        collapse = "COMPARATOR_TOO_WEAK"
    else:
        status = "OVERLAP_ONLY"
        collapse = "NO_COLLAPSE"
    return ComparatorReport(
        comparator_id=comparator_id,
        relation=_sorted_relation(comparator),
        record_minus_comparator=_sorted_relation(record_minus),
        comparator_minus_record=_sorted_relation(comparator_minus),
        record_relation_status=status,
        collapse_result=collapse,
        reason=reason,
    )


def _boundary_input_classes() -> tuple[BoundaryInputClass, ...]:
    return (
        BoundaryInputClass(
            "physical_record_production",
            "RECORD_ORDER_ADMISSIBLE",
            True,
            "A stable produced record with a unique producer may support a task-prerequisite edge.",
        ),
        BoundaryInputClass(
            "access_change",
            "ACCESS_COMPLETION_NOT_RECORD_SOURCE",
            False,
            "Changing who can read a record changes access; it does not issue a new produced record.",
        ),
        BoundaryInputClass(
            "capability_change",
            "CAPABILITY_DELTA_NOT_RECORD_SOURCE_BY_ITSELF",
            False,
            "A changed envelope is evidence for capability comparison, not an event-order edge unless an issued record is consumed.",
        ),
        BoundaryInputClass(
            "final_boundary_selection",
            "SECTION_CHOICE_NOT_RECORD_SOURCE",
            False,
            "Choosing a boundary or section is a metatheoretic selection unless the source model issues a record token.",
        ),
        BoundaryInputClass(
            "observer_readout",
            "READOUT_NOT_RECORD_SOURCE_BY_ITSELF",
            False,
            "Readout may reveal a record; readout alone is not native record production.",
        ),
        BoundaryInputClass(
            "physical_intervention",
            "CAUSAL_INPUT_NOT_RECORD_SOURCE_BY_ITSELF",
            False,
            "An intervention can be a causal parent without being an issued-record prerequisite.",
        ),
        BoundaryInputClass(
            "autonomous_feedback",
            "FEEDBACK_REQUIRES_EXPLICIT_ISSUANCE_RULE",
            False,
            "Feedback counts only when the model emits a stable record consumed by a later executable task.",
        ),
        BoundaryInputClass(
            "edge_defect_degrees_of_freedom",
            "STATE_VARIABLE_NOT_RECORD_SOURCE_BY_ITSELF",
            False,
            "Edge or defect degrees of freedom are source variables until an issuance rule turns them into records.",
        ),
        BoundaryInputClass(
            "continuous_source_flux",
            "FLUX_REQUIRES_FROZEN_RECORD_PACKET",
            False,
            "Continuous flux must be discretized or recorded by a declared source rule before it can enter the record order.",
        ),
        BoundaryInputClass(
            "stochastic_input",
            "SAMPLE_NOT_RECORD_SOURCE_BY_ITSELF",
            False,
            "Random input is not a record-order source unless the sampled outcome is issued as a stable record.",
        ),
        BoundaryInputClass(
            "native_record_issuance_rule",
            "RECORD_ORDER_ADMISSIBLE",
            True,
            "A source-owned issuance rule is the explicit bridge from physical input to produced-record prerequisite.",
        ),
    )


def _sorted_relation(relation: Relation) -> tuple[tuple[str, str], ...]:
    return tuple(sorted(relation))


def result_to_dict(result: T587Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_gate": result.source_gate,
        "source_verdict": result.source_verdict,
        "record_order": [list(item) for item in result.record_order],
        "comparators": [
            {
                **asdict(item),
                "relation": [list(edge) for edge in item.relation],
                "record_minus_comparator": [
                    list(edge) for edge in item.record_minus_comparator
                ],
                "comparator_minus_record": [
                    list(edge) for edge in item.comparator_minus_record
                ],
            }
            for item in result.comparators
        ],
        "boundary_inputs": [asdict(item) for item in result.boundary_inputs],
        "audits": [asdict(item) for item in result.audits],
        "checks": [asdict(item) for item in result.checks],
        "adjudication": result.adjudication,
        "physical_result": result.physical_result,
        "verdict": result.verdict,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
        "next_work": result.next_work,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T587 Results: T586 Causal-Collapse Boundary Attack",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source gate: `{payload['source_gate']}`",
        f"- Source verdict: `{payload['source_verdict']}`",
        "",
        "## Adjudication",
        "",
        payload["adjudication"],
        "",
        "## Comparator Attack",
        "",
        "| comparator | status | collapse result | record-only edges | comparator-only edges |",
        "| --- | --- | --- | ---: | ---: |",
    ]
    for item in payload["comparators"]:
        lines.append(
            f"| `{item['comparator_id']}` | `{item['record_relation_status']}` | "
            f"`{item['collapse_result']}` | {len(item['record_minus_comparator'])} | "
            f"{len(item['comparator_minus_record'])} |"
        )
    lines.extend(
        [
            "",
            "## Boundary-Input Screen",
            "",
            "| class | classification | counts? | reason |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for item in payload["boundary_inputs"]:
        lines.append(
            f"| `{item['class_id']}` | `{item['classification']}` | "
            f"{item['counts_as_record_source']} | {item['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Audits",
            "",
            "| audit | passed? | result class | reason |",
            "| --- | :---: | --- | --- |",
        ]
    )
    for item in payload["audits"]:
        lines.append(
            f"| `{item['audit_id']}` | {item['passed']} | "
            f"`{item['result_class']}` | {item['reason']} |"
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


def write_results(result: T587Result, results_dir: Path = Path("results")) -> None:
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
    result = run_t587_analysis()
    if args.write_results:
        write_results(result)
    print(json.dumps(result_to_dict(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
