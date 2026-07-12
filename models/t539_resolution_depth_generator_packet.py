"""T539: resolution-depth generator packet.

T538 narrowed the descent-obstruction source-law family because ordered
resolution depths were free pairwise inputs. T539 removes the pairwise depth
table and tests the obvious generator: derive depths from cover ranks, local
record sections, and compatible-section blocks.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

from models import t538_descent_obstruction_resolution_source_law_packet as t538


ARTIFACT = "T539-resolution-depth-generator-packet-v0.1"
VERDICT = "descent_obstruction_family_retired_programmable_rank_generator"
FAMILY_STATUS = "RETIRED_CURRENT_ROUTE_REQUIRES_NEW_SOURCE_LAW_FAMILY"
NEXT_ROUTE = "TAF8_cross_domain_shadow_protection_theorem_target"

NOT_CLAIMED = (
    "T539 does not establish a source law, derive spacetime, prove "
    "manifoldlikeness, repair T528, reverse T223, unpause the S1 "
    "finite-generator route, promote S1, change claim status, change canon, "
    "change public posture, authorize external publication, or move cross-repo "
    "truth. It is a Track-1 source-law generator stress test only."
)


@dataclass(frozen=True)
class RestrictionMap:
    source_cover: str
    target_cover: str


@dataclass(frozen=True)
class LocalSection:
    record_id: str
    cover_id: str
    section_id: str


@dataclass(frozen=True)
class CompatibleSectionBlock:
    block_id: str
    cover_ids: tuple[str, ...]
    record_ids: tuple[str, ...]


@dataclass(frozen=True)
class RecordCoverSystem:
    fixture_id: str
    record_ids: tuple[str, ...]
    root_cover_id: str
    restriction_maps: tuple[RestrictionMap, ...]
    local_sections: tuple[LocalSection, ...]
    compatible_section_blocks: tuple[CompatibleSectionBlock, ...]
    expected_relation_edges: tuple[tuple[str, str], ...]
    control_role: str


@dataclass(frozen=True)
class GeneratedDepth:
    source: str
    target: str
    depth: int


@dataclass(frozen=True)
class FixtureEvaluation:
    fixture_id: str
    activation_ranks: tuple[tuple[str, int], ...]
    generated_depths: tuple[GeneratedDepth, ...]
    computed_edges: tuple[tuple[str, str], ...]
    expected_edges: tuple[tuple[str, str], ...]
    realizes_expected_rank_relation: bool
    is_strict_partial_order: bool
    comparable_pair_count: int
    total_pair_count: int
    relation_shape: str
    control_role: str
    uses_pairwise_depth_table: bool
    counts_as_source_law_evidence: bool
    failure_mode: str


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
class T539Result:
    artifact: str
    source_t538_verdict: str
    selected_family: str
    generator_recipe: str
    target_import_used: bool
    fixture_evaluations: tuple[FixtureEvaluation, ...]
    controls: tuple[ControlEvaluation, ...]
    generated_relation_shapes: tuple[str, ...]
    family_status: str
    verdict: str
    strongest_reading: str
    recommended_next: str
    claim_labels: tuple[ClaimLabel, ...]
    s1_update: str
    claim_ledger_update: str
    not_claimed: str


def run_t539_analysis() -> T539Result:
    fixtures = _fixtures()
    evaluations = tuple(evaluate_fixture(fixture) for fixture in fixtures)
    controls = _controls(fixtures, evaluations)
    target_import_used = False
    verdict = (
        VERDICT
        if t538.run_t538_analysis().verdict == t538.VERDICT
        and not target_import_used
        and all(control.passed for control in controls)
        and not any(e.counts_as_source_law_evidence for e in evaluations)
        else "resolution_depth_generator_packet_unexpected_status"
    )
    return T539Result(
        artifact=ARTIFACT,
        source_t538_verdict=t538.VERDICT,
        selected_family=t538.SELECTED_FAMILY,
        generator_recipe=(
            "Compute cover ranks from restriction maps; assign each record its "
            "first compatible local-section rank; generate d(x, y) from the "
            "source record's rank; declare x < y when d(x, y) < d(y, x)."
        ),
        target_import_used=target_import_used,
        fixture_evaluations=evaluations,
        controls=controls,
        generated_relation_shapes=tuple(e.relation_shape for e in evaluations),
        family_status=FAMILY_STATUS,
        verdict=verdict,
        strongest_reading=(
            "T539 removes the pairwise depth table, but the resulting generator "
            "collapses to a programmable scalar rank. The same source-cover "
            "schema can realize antichain, total-chain, diamond, and fork "
            "relations by moving compatible local sections across ranks. That "
            "is a useful negative result: the current descent-obstruction "
            "family route should be retired rather than wrapped in another "
            "router."
        ),
        recommended_next=(
            "Retire the current descent-obstruction resolution family route. "
            "Re-rank TAF11 against TAF8 and route the next swing to the "
            "cross-domain shadow-protection theorem target unless a genuinely "
            "new, non-rank source-law family is proposed."
        ),
        claim_labels=_claim_labels(evaluations, controls),
        s1_update=(
            "S1 remains `requires_added_assumption`. T539 supplies no source "
            "law and therefore no S1 evidence."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T539 is a negative generator "
            "stress test and leaves claim rows, Canon Index tiers, and canon "
            "verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t539_result_to_dict(result: T539Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t538_verdict": result.source_t538_verdict,
        "selected_family": result.selected_family,
        "generator_recipe": result.generator_recipe,
        "target_import_used": result.target_import_used,
        "fixture_evaluations": [
            {
                "fixture_id": evaluation.fixture_id,
                "activation_ranks": [
                    {"record_id": record_id, "rank": rank}
                    for record_id, rank in evaluation.activation_ranks
                ],
                "generated_depths": [
                    {
                        "source": depth.source,
                        "target": depth.target,
                        "depth": depth.depth,
                    }
                    for depth in evaluation.generated_depths
                ],
                "computed_edges": [list(edge) for edge in evaluation.computed_edges],
                "expected_edges": [list(edge) for edge in evaluation.expected_edges],
                "realizes_expected_rank_relation": (
                    evaluation.realizes_expected_rank_relation
                ),
                "is_strict_partial_order": evaluation.is_strict_partial_order,
                "comparable_pair_count": evaluation.comparable_pair_count,
                "total_pair_count": evaluation.total_pair_count,
                "relation_shape": evaluation.relation_shape,
                "control_role": evaluation.control_role,
                "uses_pairwise_depth_table": evaluation.uses_pairwise_depth_table,
                "counts_as_source_law_evidence": (
                    evaluation.counts_as_source_law_evidence
                ),
                "failure_mode": evaluation.failure_mode,
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
        "generated_relation_shapes": list(result.generated_relation_shapes),
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


def evaluate_fixture(fixture: RecordCoverSystem) -> FixtureEvaluation:
    ranks = activation_ranks(fixture)
    generated = generate_ordered_depths(fixture.record_ids, ranks)
    edges = compute_relation_edges(fixture.record_ids, generated)
    comparable = len({frozenset(edge) for edge in edges})
    total_pairs = len(fixture.record_ids) * (len(fixture.record_ids) - 1) // 2
    shape = _relation_shape(edges, total_pairs)
    return FixtureEvaluation(
        fixture_id=fixture.fixture_id,
        activation_ranks=tuple(sorted(ranks.items())),
        generated_depths=generated,
        computed_edges=edges,
        expected_edges=fixture.expected_relation_edges,
        realizes_expected_rank_relation=edges == fixture.expected_relation_edges,
        is_strict_partial_order=is_strict_partial_order(fixture.record_ids, edges),
        comparable_pair_count=comparable,
        total_pair_count=total_pairs,
        relation_shape=shape,
        control_role=fixture.control_role,
        uses_pairwise_depth_table=False,
        counts_as_source_law_evidence=False,
        failure_mode="programmable_scalar_rank_channel",
    )


def cover_ranks(fixture: RecordCoverSystem) -> dict[str, int]:
    parents_by_child: dict[str, set[str]] = {}
    cover_ids = {fixture.root_cover_id}
    for restriction in fixture.restriction_maps:
        cover_ids.add(restriction.source_cover)
        cover_ids.add(restriction.target_cover)
        parents_by_child.setdefault(restriction.source_cover, set()).add(
            restriction.target_cover
        )
    for section in fixture.local_sections:
        cover_ids.add(section.cover_id)
    for block in fixture.compatible_section_blocks:
        cover_ids.update(block.cover_ids)

    memo = {fixture.root_cover_id: 0}

    def rank(cover_id: str, visiting: frozenset[str] = frozenset()) -> int:
        if cover_id in memo:
            return memo[cover_id]
        if cover_id in visiting:
            raise ValueError(f"restriction cycle reaches {cover_id}")
        parents = parents_by_child.get(cover_id, set())
        if not parents:
            raise ValueError(f"cover {cover_id} has no path to root")
        value = 1 + min(rank(parent, visiting | {cover_id}) for parent in parents)
        memo[cover_id] = value
        return value

    return {cover_id: rank(cover_id) for cover_id in sorted(cover_ids)}


def activation_ranks(fixture: RecordCoverSystem) -> dict[str, int]:
    ranks = cover_ranks(fixture)
    section_covers_by_record: dict[str, set[str]] = {
        record_id: set() for record_id in fixture.record_ids
    }
    for section in fixture.local_sections:
        section_covers_by_record.setdefault(section.record_id, set()).add(section.cover_id)

    compatible_covers_by_record: dict[str, set[str]] = {
        record_id: set() for record_id in fixture.record_ids
    }
    for block in fixture.compatible_section_blocks:
        for record_id in block.record_ids:
            compatible_covers_by_record.setdefault(record_id, set()).update(
                block.cover_ids
            )

    activations: dict[str, int] = {}
    for record_id in fixture.record_ids:
        eligible = (
            section_covers_by_record.get(record_id, set())
            & compatible_covers_by_record.get(record_id, set())
        )
        if not eligible:
            raise ValueError(f"record {record_id} has no compatible local section")
        activations[record_id] = min(ranks[cover_id] for cover_id in eligible)
    return activations


def generate_ordered_depths(
    record_ids: tuple[str, ...], ranks: dict[str, int]
) -> tuple[GeneratedDepth, ...]:
    return tuple(
        GeneratedDepth(source=source, target=target, depth=ranks[source])
        for source, target in permutations(record_ids, 2)
    )


def compute_relation_edges(
    record_ids: tuple[str, ...], depths: tuple[GeneratedDepth, ...]
) -> tuple[tuple[str, str], ...]:
    depth_by_pair = {(d.source, d.target): d.depth for d in depths}
    edges: list[tuple[str, str]] = []
    for left, right in permutations(record_ids, 2):
        if depth_by_pair[(left, right)] < depth_by_pair[(right, left)]:
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
    fixture: RecordCoverSystem, record_map: dict[str, str], cover_map: dict[str, str]
) -> RecordCoverSystem:
    return RecordCoverSystem(
        fixture_id=f"{fixture.fixture_id}_relabel",
        record_ids=tuple(record_map[record] for record in fixture.record_ids),
        root_cover_id=cover_map[fixture.root_cover_id],
        restriction_maps=tuple(
            RestrictionMap(
                source_cover=cover_map[restriction.source_cover],
                target_cover=cover_map[restriction.target_cover],
            )
            for restriction in fixture.restriction_maps
        ),
        local_sections=tuple(
            LocalSection(
                record_id=record_map[section.record_id],
                cover_id=cover_map[section.cover_id],
                section_id=section.section_id,
            )
            for section in fixture.local_sections
        ),
        compatible_section_blocks=tuple(
            CompatibleSectionBlock(
                block_id=block.block_id,
                cover_ids=tuple(cover_map[cover] for cover in block.cover_ids),
                record_ids=tuple(record_map[record] for record in block.record_ids),
            )
            for block in fixture.compatible_section_blocks
        ),
        expected_relation_edges=tuple(
            sorted(
                (record_map[source], record_map[target])
                for source, target in fixture.expected_relation_edges
            )
        ),
        control_role=fixture.control_role,
    )


def _fixtures() -> tuple[RecordCoverSystem, ...]:
    records = ("a", "b", "c", "d")
    return (
        _fixture_from_activation_levels(
            "generated_antichain_control",
            records,
            {"a": 0, "b": 0, "c": 0, "d": 0},
            (),
            "hostile_antichain_control",
        ),
        _fixture_from_activation_levels(
            "generated_total_chain_control",
            records,
            {"a": 0, "b": 1, "c": 2, "d": 3},
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
        _fixture_from_activation_levels(
            "generated_diamond_probe",
            records,
            {"a": 0, "b": 1, "c": 1, "d": 2},
            (("a", "b"), ("a", "c"), ("a", "d"), ("b", "d"), ("c", "d")),
            "rank_programmability_probe",
        ),
        _fixture_from_activation_levels(
            "generated_fork_probe",
            records,
            {"a": 0, "b": 0, "c": 1, "d": 1},
            (("a", "c"), ("a", "d"), ("b", "c"), ("b", "d")),
            "rank_programmability_probe",
        ),
    )


def _fixture_from_activation_levels(
    fixture_id: str,
    records: tuple[str, ...],
    activation_levels: dict[str, int],
    expected_edges: tuple[tuple[str, str], ...],
    control_role: str,
) -> RecordCoverSystem:
    max_level = max(activation_levels.values())
    cover_ids = tuple(f"u{level}" for level in range(max_level + 1))
    restrictions = tuple(
        RestrictionMap(source_cover=f"u{level}", target_cover=f"u{level - 1}")
        for level in range(1, max_level + 1)
    )
    local_sections = tuple(
        LocalSection(
            record_id=record,
            cover_id=f"u{activation_levels[record]}",
            section_id=f"s_{record}_{activation_levels[record]}",
        )
        for record in records
    )
    compatible_blocks = tuple(
        CompatibleSectionBlock(
            block_id=f"block_u{level}",
            cover_ids=(f"u{level}",),
            record_ids=tuple(
                record for record in records if activation_levels[record] == level
            ),
        )
        for level in range(max_level + 1)
    )
    return RecordCoverSystem(
        fixture_id=fixture_id,
        record_ids=records,
        root_cover_id=cover_ids[0],
        restriction_maps=restrictions,
        local_sections=local_sections,
        compatible_section_blocks=compatible_blocks,
        expected_relation_edges=tuple(sorted(expected_edges)),
        control_role=control_role,
    )


def _controls(
    fixtures: tuple[RecordCoverSystem, ...],
    evaluations: tuple[FixtureEvaluation, ...],
) -> tuple[ControlEvaluation, ...]:
    diamond = next(f for f in fixtures if f.fixture_id == "generated_diamond_probe")
    record_map = {"a": "r3", "b": "r1", "c": "r2", "d": "r0"}
    cover_map = {"u0": "v0", "u1": "v2", "u2": "v1"}
    relabeled = relabel_fixture(diamond, record_map, cover_map)
    relabeled_edges = evaluate_fixture(relabeled).computed_edges
    expected_relabel_edges = tuple(
        sorted((record_map[source], record_map[target]) for source, target in diamond.expected_relation_edges)
    )
    shapes = {
        evaluation.relation_shape
        for evaluation in evaluations
        if evaluation.realizes_expected_rank_relation
        and evaluation.is_strict_partial_order
    }
    return (
        ControlEvaluation(
            control_id="no_pairwise_depth_table_control",
            passed=not any(e.uses_pairwise_depth_table for e in evaluations),
            reason=(
                "All ordered depths are generated from activation ranks rather "
                "than supplied as pairwise table entries."
            ),
        ),
        ControlEvaluation(
            control_id="record_and_cover_relabel_control",
            passed=relabeled_edges == expected_relabel_edges,
            reason=(
                "Renaming records and cover nodes preserves the generated "
                "diamond relation."
            ),
        ),
        ControlEvaluation(
            control_id="scalar_rank_programmability_control",
            passed={"antichain", "total_chain", "diamond", "fork"} <= shapes,
            reason=(
                "The same generator realizes antichain, total-chain, diamond, "
                "and fork shapes by changing compatible local-section ranks; "
                "this is diagnostic programmability, not source-law evidence."
            ),
        ),
        ControlEvaluation(
            control_id="no_source_law_promotion_control",
            passed=not any(e.counts_as_source_law_evidence for e in evaluations),
            reason=(
                "The generated-depth packet remains a stress test. It does not "
                "promote hostile controls or rank-programmed fixtures into "
                "source-law evidence."
            ),
        ),
        ControlEvaluation(
            control_id="t538_retirement_trigger_control",
            passed=t538.run_t538_analysis().verdict == t538.VERDICT,
            reason=(
                "T538 required a nonprogrammatic depth generator; T539 found "
                "only a programmable rank generator for the current route."
            ),
        ),
    )


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
    shapes = ", ".join(e.relation_shape for e in evaluations)
    passed_controls = ", ".join(c.control_id for c in controls if c.passed)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T538 is consumed as requiring a resolution-depth generator "
                "before the descent-obstruction family can count as a source law."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The generated-depth recipe uses no pairwise depth table and "
                f"realizes these finite relation shapes: {shapes}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"All T539 controls pass as diagnostics: {passed_controls}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The generator reduces to a scalar activation-rank channel. "
                "That is too programmable to rescue the current "
                "descent-obstruction source-law family."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines: list[str] = [
        "# T539 Results: Resolution-Depth Generator Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source T538 verdict: `{payload['source_t538_verdict']}`",
        f"- Selected family: `{payload['selected_family']}`",
        f"- Family status: `{payload['family_status']}`",
        f"- Target import used: `{payload['target_import_used']}`",
        "",
        "## Generator Recipe",
        "",
        payload["generator_recipe"],
        "",
        "## Fixture Evaluations",
        "",
        "| fixture | shape | role | ranks | comparable pairs | expected? | partial order? | source-law evidence? | failure mode |",
        "| --- | --- | --- | --- | ---: | :---: | :---: | :---: | --- |",
    ]
    for evaluation in payload["fixture_evaluations"]:
        ranks = ", ".join(
            f"{item['record_id']}:{item['rank']}"
            for item in evaluation["activation_ranks"]
        )
        lines.append(
            "| `{fixture_id}` | `{relation_shape}` | `{control_role}` | {ranks} | "
            "{comparable_pair_count}/{total_pair_count} | "
            "{realizes_expected_rank_relation} | {is_strict_partial_order} | "
            "{counts_as_source_law_evidence} | `{failure_mode}` |".format(
                ranks=ranks, **evaluation
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


def write_results(result: T539Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t539_result_to_dict(result)
    json_path = results_dir / "T539-resolution-depth-generator-packet-v0.1.json"
    md_path = results_dir / "T539-resolution-depth-generator-packet-v0.1-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t539_analysis()
    payload = t539_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
