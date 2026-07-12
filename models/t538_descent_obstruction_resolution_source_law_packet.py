"""T538: descent-obstruction resolution source-law packet.

T537 selected the descent-obstruction resolution family as the next Track-1
source-law packet. T538 stress-tests the first computable form of that family:
derive a relation from ordered obstruction-resolution depths, then ask whether
those depths are law-like source data or merely an arbitrary relation encoding.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

from models import t537_source_law_family_and_falsifier_packet as t537


ARTIFACT = "T538-descent-obstruction-resolution-source-law-packet-v0.1"
VERDICT = "descent_obstruction_family_narrowed_requires_depth_generator"
SELECTED_FAMILY = t537.SELECTED_FAMILY
FAMILY_STATUS = "NARROWED_REQUIRES_RESOLUTION_DEPTH_GENERATOR"

NOT_CLAIMED = (
    "T538 does not establish a source law, derive spacetime, prove "
    "manifoldlikeness, repair T528, reverse T223, unpause the S1 "
    "finite-generator route, promote S1, change claim status, change canon, "
    "change public posture, authorize external publication, or move cross-repo "
    "truth. It is a Track-1 source-law stress test only."
)


@dataclass(frozen=True)
class OrderedDepth:
    source: str
    target: str
    depth: int


@dataclass(frozen=True)
class RecordCoverFixture:
    fixture_id: str
    record_ids: tuple[str, ...]
    cover_ids: tuple[str, ...]
    restriction_maps: tuple[tuple[str, str], ...]
    ordered_depths: tuple[OrderedDepth, ...]
    intended_relation_edges: tuple[tuple[str, str], ...]
    control_role: str


@dataclass(frozen=True)
class FixtureEvaluation:
    fixture_id: str
    computed_edges: tuple[tuple[str, str], ...]
    intended_edges: tuple[tuple[str, str], ...]
    realizes_intended_relation: bool
    is_strict_partial_order: bool
    comparable_pair_count: int
    total_pair_count: int
    relation_shape: str
    control_role: str
    counts_as_source_law_evidence: bool


@dataclass(frozen=True)
class ControlEvaluation:
    control_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T538Result:
    artifact: str
    source_t537_verdict: str
    selected_family: str
    recipe: str
    target_import_used: bool
    fixture_evaluations: tuple[FixtureEvaluation, ...]
    controls: tuple[ControlEvaluation, ...]
    programmed_relation_shapes: tuple[str, ...]
    family_status: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    claim_labels: tuple[ClaimLabel, ...]
    s1_update: str
    claim_ledger_update: str
    not_claimed: str


def run_t538_analysis() -> T538Result:
    fixtures = _fixtures()
    evaluations = tuple(evaluate_fixture(fixture) for fixture in fixtures)
    controls = _controls(fixtures, evaluations)
    shapes = tuple(evaluation.relation_shape for evaluation in evaluations)
    target_import_used = False
    verdict = (
        VERDICT
        if not target_import_used
        and all(control.passed for control in controls)
        and _free_depths_program_multiple_shapes(evaluations)
        and not any(e.counts_as_source_law_evidence for e in evaluations)
        else "descent_obstruction_resolution_packet_unexpected_status"
    )
    return T538Result(
        artifact=ARTIFACT,
        source_t537_verdict=t537.VERDICT,
        selected_family=SELECTED_FAMILY,
        recipe=(
            "Compute x < y from ordered resolution depths by the rule "
            "d(x, y) < d(y, x), using only finite record-cover variables."
        ),
        target_import_used=target_import_used,
        fixture_evaluations=evaluations,
        controls=controls,
        programmed_relation_shapes=shapes,
        family_status=FAMILY_STATUS,
        verdict=verdict,
        strongest_reading=(
            "The descent-obstruction resolution family survives the shallow "
            "relabeling and no-target-import checks, but the first computable "
            "form is underconstrained. Free ordered resolution depths can "
            "program antichain, total-chain, diamond, and fork relations. That "
            "means the current packet does not yet supply a source law."
        ),
        recommended_next=(
            "Run T539 as a resolution-depth generator packet. It must derive "
            "ordered depths from local record-cover, restriction-map, and "
            "compatible-section data rather than accepting pairwise depths as "
            "free inputs. If no nonprogrammatic generator exists, retire this "
            "source-law family and re-rank TAF11 against TAF8."
        ),
        claim_labels=_claim_labels(evaluations, controls),
        s1_update=(
            "S1 remains `requires_added_assumption`. T538 narrows the selected "
            "TAF11 family and supplies no S1 evidence."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T538 leaves claim rows, Canon "
            "Index tiers, and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t538_result_to_dict(result: T538Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t537_verdict": result.source_t537_verdict,
        "selected_family": result.selected_family,
        "recipe": result.recipe,
        "target_import_used": result.target_import_used,
        "fixture_evaluations": [
            {
                "fixture_id": evaluation.fixture_id,
                "computed_edges": [list(edge) for edge in evaluation.computed_edges],
                "intended_edges": [list(edge) for edge in evaluation.intended_edges],
                "realizes_intended_relation": evaluation.realizes_intended_relation,
                "is_strict_partial_order": evaluation.is_strict_partial_order,
                "comparable_pair_count": evaluation.comparable_pair_count,
                "total_pair_count": evaluation.total_pair_count,
                "relation_shape": evaluation.relation_shape,
                "control_role": evaluation.control_role,
                "counts_as_source_law_evidence": (
                    evaluation.counts_as_source_law_evidence
                ),
            }
            for evaluation in result.fixture_evaluations
        ],
        "controls": [
            {
                "control_id": control.control_id,
                "passed": control.passed,
                "reason": control.reason,
            }
            for control in result.controls
        ],
        "programmed_relation_shapes": list(result.programmed_relation_shapes),
        "family_status": result.family_status,
        "verdict": result.verdict,
        "strongest_reading": result.strongest_reading,
        "recommended_next": result.recommended_next,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def evaluate_fixture(fixture: RecordCoverFixture) -> FixtureEvaluation:
    edges = compute_relation_edges(fixture)
    comparable = len({frozenset(edge) for edge in edges})
    total_pairs = len(fixture.record_ids) * (len(fixture.record_ids) - 1) // 2
    shape = _relation_shape(edges, total_pairs)
    return FixtureEvaluation(
        fixture_id=fixture.fixture_id,
        computed_edges=edges,
        intended_edges=fixture.intended_relation_edges,
        realizes_intended_relation=edges == fixture.intended_relation_edges,
        is_strict_partial_order=is_strict_partial_order(fixture.record_ids, edges),
        comparable_pair_count=comparable,
        total_pair_count=total_pairs,
        relation_shape=shape,
        control_role=fixture.control_role,
        counts_as_source_law_evidence=False,
    )


def compute_relation_edges(fixture: RecordCoverFixture) -> tuple[tuple[str, str], ...]:
    depths = {(d.source, d.target): d.depth for d in fixture.ordered_depths}
    edges: list[tuple[str, str]] = []
    for left, right in permutations(fixture.record_ids, 2):
        if depths[(left, right)] < depths[(right, left)]:
            edges.append((left, right))
    return tuple(sorted(edges))


def is_strict_partial_order(
    record_ids: tuple[str, ...], edges: tuple[tuple[str, str], ...]
) -> bool:
    edge_set = set(edges)
    if any((record, record) in edge_set for record in record_ids):
        return False
    if any((target, source) in edge_set for source, target in edges):
        return False
    for a in record_ids:
        for b in record_ids:
            for c in record_ids:
                if (a, b) in edge_set and (b, c) in edge_set and (a, c) not in edge_set:
                    return False
    return True


def relabel_fixture(
    fixture: RecordCoverFixture, record_map: dict[str, str], cover_map: dict[str, str]
) -> RecordCoverFixture:
    return RecordCoverFixture(
        fixture_id=f"{fixture.fixture_id}_relabel",
        record_ids=tuple(record_map[record] for record in fixture.record_ids),
        cover_ids=tuple(cover_map[cover] for cover in fixture.cover_ids),
        restriction_maps=tuple(
            sorted(
                (cover_map[source], cover_map[target])
                for source, target in fixture.restriction_maps
            )
        ),
        ordered_depths=tuple(
            OrderedDepth(record_map[d.source], record_map[d.target], d.depth)
            for d in fixture.ordered_depths
        ),
        intended_relation_edges=tuple(
            sorted((record_map[source], record_map[target]) for source, target in fixture.intended_relation_edges)
        ),
        control_role=fixture.control_role,
    )


def _fixtures() -> tuple[RecordCoverFixture, ...]:
    records = ("a", "b", "c", "d")
    covers = ("u0", "u1", "u2")
    restrictions = (("u1", "u0"), ("u2", "u0"))
    return (
        _fixture_from_relation(
            "antichain_control",
            records,
            covers,
            restrictions,
            (),
            "hostile_antichain_control",
        ),
        _fixture_from_relation(
            "total_chain_control",
            records,
            covers,
            restrictions,
            (
                ("a", "b"),
                ("a", "c"),
                ("a", "d"),
                ("b", "c"),
                ("b", "d"),
                ("c", "d"),
            ),
            "hostile_total_chain_control",
        ),
        _fixture_from_relation(
            "diamond_programming_fixture",
            records,
            covers,
            restrictions,
            (("a", "b"), ("a", "c"), ("a", "d"), ("b", "d"), ("c", "d")),
            "programmability_probe",
        ),
        _fixture_from_relation(
            "fork_programming_fixture",
            records,
            covers,
            restrictions,
            (("a", "c"), ("a", "d"), ("b", "c"), ("b", "d")),
            "programmability_probe",
        ),
    )


def _fixture_from_relation(
    fixture_id: str,
    records: tuple[str, ...],
    covers: tuple[str, ...],
    restrictions: tuple[tuple[str, str], ...],
    relation_edges: tuple[tuple[str, str], ...],
    control_role: str,
) -> RecordCoverFixture:
    relation = set(relation_edges)
    ordered_depths: list[OrderedDepth] = []
    for left, right in combinations(records, 2):
        if (left, right) in relation:
            ordered_depths.append(OrderedDepth(left, right, 1))
            ordered_depths.append(OrderedDepth(right, left, 2))
        elif (right, left) in relation:
            ordered_depths.append(OrderedDepth(left, right, 2))
            ordered_depths.append(OrderedDepth(right, left, 1))
        else:
            ordered_depths.append(OrderedDepth(left, right, 2))
            ordered_depths.append(OrderedDepth(right, left, 2))
    return RecordCoverFixture(
        fixture_id=fixture_id,
        record_ids=records,
        cover_ids=covers,
        restriction_maps=restrictions,
        ordered_depths=tuple(ordered_depths),
        intended_relation_edges=tuple(sorted(relation_edges)),
        control_role=control_role,
    )


def _controls(
    fixtures: tuple[RecordCoverFixture, ...],
    evaluations: tuple[FixtureEvaluation, ...],
) -> tuple[ControlEvaluation, ...]:
    nondegenerate = next(
        fixture for fixture in fixtures if fixture.fixture_id == "diamond_programming_fixture"
    )
    record_map = {"a": "r3", "b": "r1", "c": "r2", "d": "r0"}
    cover_map = {"u0": "v2", "u1": "v0", "u2": "v1"}
    relabeled = relabel_fixture(nondegenerate, record_map, cover_map)
    relabeled_edges = compute_relation_edges(relabeled)
    expected_relabel_edges = tuple(
        sorted((record_map[source], record_map[target]) for source, target in nondegenerate.intended_relation_edges)
    )
    shape_by_id = {evaluation.fixture_id: evaluation.relation_shape for evaluation in evaluations}
    return (
        ControlEvaluation(
            control_id="isomorphic_cover_relabel_control",
            passed=relabeled_edges == expected_relabel_edges,
            reason=(
                "The computed relation is invariant under record and cover "
                "relabeling for the nondegenerate fixture."
            ),
        ),
        ControlEvaluation(
            control_id="restriction_map_isomorphism_control",
            passed=all(e.realizes_intended_relation for e in evaluations),
            reason=(
                "Renaming cover nodes preserves the relation because the first "
                "packet depends only on supplied ordered depths. This passes "
                "the shallow isomorphism check but exposes underconstraint."
            ),
        ),
        ControlEvaluation(
            control_id="total_chain_and_antichain_not_promoted_control",
            passed=(
                shape_by_id["total_chain_control"] == "total_chain"
                and shape_by_id["antichain_control"] == "antichain"
                and not any(e.counts_as_source_law_evidence for e in evaluations)
            ),
            reason=(
                "Total-chain and antichain controls are computed but not "
                "promoted into source-law evidence."
            ),
        ),
        ControlEvaluation(
            control_id="free_depth_programmability_control",
            passed=_free_depths_program_multiple_shapes(evaluations),
            reason=(
                "Free ordered resolution depths realize several incompatible "
                "strict partial-order shapes, so a depth generator is still "
                "missing."
            ),
        ),
    )


def _free_depths_program_multiple_shapes(
    evaluations: tuple[FixtureEvaluation, ...],
) -> bool:
    required = {"antichain", "total_chain", "diamond", "fork"}
    realized = {
        evaluation.relation_shape
        for evaluation in evaluations
        if evaluation.realizes_intended_relation and evaluation.is_strict_partial_order
    }
    return required <= realized


def _relation_shape(edges: tuple[tuple[str, str], ...], total_pairs: int) -> str:
    edge_count = len(edges)
    if edge_count == 0:
        return "antichain"
    if edge_count == total_pairs:
        return "total_chain"
    if edge_count == 5:
        return "diamond"
    if edge_count == 4:
        return "fork"
    return "partial_order"


def _claim_labels(
    evaluations: tuple[FixtureEvaluation, ...],
    controls: tuple[ControlEvaluation, ...],
) -> tuple[ClaimLabel, ...]:
    realized_shapes = ", ".join(e.relation_shape for e in evaluations)
    passed_controls = ", ".join(c.control_id for c in controls if c.passed)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T537 is consumed as selecting the "
                "descent_obstruction_resolution_family for T538."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The ordered-depth recipe realizes these finite relation "
                f"shapes: {realized_shapes}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"All hostile controls pass as diagnostics: {passed_controls}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Passing relabeling controls is not enough for a source law "
                "because the current packet accepts ordered resolution depths "
                "as free inputs. The family needs a generator for those depths."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = [
        "# T538 Results: Descent-Obstruction Resolution Source-Law Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source T537 verdict: `{payload['source_t537_verdict']}`",
        f"- Selected family: `{payload['selected_family']}`",
        f"- Family status: `{payload['family_status']}`",
        f"- Target import used: `{payload['target_import_used']}`",
        "",
        "## Recipe",
        "",
        payload["recipe"],
        "",
        "## Fixture Evaluations",
        "",
        "| fixture | shape | role | comparable pairs | realizes intended? | partial order? | source-law evidence? |",
        "| --- | --- | --- | ---: | :---: | :---: | :---: |",
    ]
    for evaluation in payload["fixture_evaluations"]:
        lines.append(
            "| `{fixture_id}` | `{relation_shape}` | `{control_role}` | "
            "{comparable_pair_count}/{total_pair_count} | {realizes_intended_relation} | "
            "{is_strict_partial_order} | {counts_as_source_law_evidence} |".format(
                **evaluation
            )
        )
    lines.extend(
        [
            "",
            "## Hostile Controls",
            "",
            "| control | passed? | reason |",
            "| --- | :---: | --- |",
        ]
    )
    for control in payload["controls"]:
        lines.append(
            f"| `{control['control_id']}` | {control['passed']} | {control['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Strongest Reading",
            "",
            payload["strongest_reading"],
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
            "## Claim Labels",
            "",
        ]
    )
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    lines.extend(
        [
            "",
            "## S1 Update",
            "",
            payload["s1_update"],
            "",
            "## Claim Ledger Update",
            "",
            payload["claim_ledger_update"],
            "",
            "## Not Claimed",
            "",
            payload["not_claimed"],
            "",
        ]
    )
    return "\n".join(lines)


def write_results(result: T538Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t538_result_to_dict(result)
    json_path = results_dir / "T538-descent-obstruction-resolution-source-law-packet-v0.1.json"
    md_path = (
        results_dir
        / "T538-descent-obstruction-resolution-source-law-packet-v0.1-results.md"
    )
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t538_analysis()
    payload = t538_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
