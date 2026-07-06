"""T470: observer-shadow composition gate.

This module runs the first bounded check requested by
open-problems/observer-shadow-category.md. It asks whether a conservative
observer-shadow object/morphism schema can represent two existing finite
families without promoting a global category claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models.losskernel_obligation_factorization import (
    Case,
    canonical_cases,
    derived_obligation,
    hidden_source_escape_pair,
    neighbor_signature,
)
from models.transport_network import (
    PathAdmissibility,
    _path_accumulated_forgotten,
    run_t37_analysis,
)


ARTIFACT_ID = "T470-observer-shadow-composition-gate-v0.1"
VERDICT = "OBSERVER_SHADOW_SCHEMA_BUILT_INDEXED_COMPLETION_REQUIRED_NO_PROMOTION"


@dataclass(frozen=True)
class ShadowAuditObject:
    """A conservative observer-shadow audit object."""

    object_id: str
    family: str
    source_system: str
    observer_profile: str
    shadow_projection: str
    shadow_key: tuple[str, ...]
    capability_object: str
    capability_value: str
    native_comparison: str
    declared_indices: tuple[str, ...]


@dataclass(frozen=True)
class ShadowMorphismCheck:
    """A proposed morphism/comparison between two audit objects."""

    check_id: str
    family: str
    source_object_id: str
    target_object_id: str
    proposed_morphism: str
    same_shadow: bool
    capability_equivalent: bool
    protection_preserved: bool
    classification: str
    obstruction: str
    repaired_by: str


@dataclass(frozen=True)
class FamilySummary:
    family: str
    checks: tuple[str, ...]
    passes_shared_schema: bool
    requires_indexed_completion: bool
    strongest_reading: str
    not_earned: tuple[str, ...]


@dataclass(frozen=True)
class T470Result:
    objects: tuple[ShadowAuditObject, ...]
    checks: tuple[ShadowMorphismCheck, ...]
    family_summaries: tuple[FamilySummary, ...]
    verdict: str
    shared_schema_expresses_both_families: bool
    endpoint_only_global_category_supported: bool
    indexed_atlas_required: bool
    claim_ledger_update: str
    strongest_reading: str
    future_packet_minimum: tuple[str, ...]
    not_earned: tuple[str, ...]


def run_t470_analysis() -> T470Result:
    """Run the T470 bounded observer-shadow composition gate."""

    transport_objects = _transport_objects()
    losskernel_objects = _losskernel_objects()
    objects = transport_objects + losskernel_objects
    object_map = {obj.object_id: obj for obj in objects}

    checks = (
        _check_pair(
            "transport_endpoint_only_collapse",
            object_map["transport_endpoint_via_L_A"],
            object_map["transport_endpoint_via_L_B"],
            proposed_morphism="collapse paths to the same endpoint shadow",
            fail_classification="composition_requires_path_index",
            obstruction=(
                "The two transport paths share the same endpoint shadow but have "
                "different accumulated forgotten structure and different PO1 "
                "capability verdicts."
            ),
            repaired_by="index the shadow by path label and accumulated forgotten structure",
        ),
        _check_pair(
            "transport_path_indexed_completion",
            object_map["transport_path_indexed_via_L_A"],
            object_map["transport_path_indexed_via_L_B"],
            proposed_morphism="compare after path-indexed completion",
            fail_classification="unexpected_transport_completion_failure",
            obstruction="none",
            repaired_by="already separated by path-indexed observer-shadow data",
        ),
        _check_pair(
            "losskernel_neighbor_factoring_preserves",
            object_map["losskernel_neighbor_mixed_a"],
            object_map["losskernel_neighbor_mixed_b"],
            proposed_morphism="factor through neighbor-visible nu",
            fail_classification="unexpected_losskernel_factor_failure",
            obstruction="none",
            repaired_by="not needed",
        ),
        _check_pair(
            "losskernel_hidden_source_omitted",
            object_map["losskernel_hidden_omitted_a"],
            object_map["losskernel_hidden_omitted_b"],
            proposed_morphism="omit hidden source datum from neighbor shadow",
            fail_classification="state_completion_required",
            obstruction=(
                "The cases share the same neighbor-visible signature but the "
                "obligation reads a hidden source datum outside that signature."
            ),
            repaired_by=(
                "admit the hidden source datum into the shadow index, which routes "
                "the distinction back to ordinary state completion"
            ),
        ),
        _check_pair(
            "losskernel_hidden_source_completed",
            object_map["losskernel_hidden_completed_a"],
            object_map["losskernel_hidden_completed_b"],
            proposed_morphism="compare after hidden-source completion",
            fail_classification="unexpected_losskernel_completion_failure",
            obstruction="none",
            repaired_by="already separated by completed neighbor-visible state",
        ),
    )

    transport_summary = FamilySummary(
        family="typed_transport",
        checks=(
            "transport_endpoint_only_collapse",
            "transport_path_indexed_completion",
        ),
        passes_shared_schema=True,
        requires_indexed_completion=True,
        strongest_reading=(
            "Typed transport fits the shared schema only when the observer-shadow "
            "object carries path and accumulated-loss indices. Endpoint-only "
            "composition loses load-bearing data."
        ),
        not_earned=(
            "observer-shadow category theorem",
            "PO1 functor repair",
            "new D1 or PO1 claim movement",
        ),
    )
    losskernel_summary = FamilySummary(
        family="losskernel",
        checks=(
            "losskernel_neighbor_factoring_preserves",
            "losskernel_hidden_source_omitted",
            "losskernel_hidden_source_completed",
        ),
        passes_shared_schema=True,
        requires_indexed_completion=True,
        strongest_reading=(
            "LossKernel fits the same schema as a neighbor-visible factoring "
            "case. The only separating escape requires source-state completion, "
            "which T220 already routes back to absorption."
        ),
        not_earned=(
            "LossKernel prior-art-separated theorem",
            "TF1 promotion",
            "new mathematical object language",
        ),
    )

    return T470Result(
        objects=objects,
        checks=checks,
        family_summaries=(transport_summary, losskernel_summary),
        verdict=VERDICT,
        shared_schema_expresses_both_families=True,
        endpoint_only_global_category_supported=False,
        indexed_atlas_required=True,
        claim_ledger_update="none",
        strongest_reading=(
            "A shared observer-shadow audit-object schema can express both "
            "finite families, but verdict preservation is not automatic under "
            "endpoint-only composition. The first bounded run supports an "
            "indexed audit atlas, not a single global observer-shadow category."
        ),
        future_packet_minimum=(
            "declare source system, observer/access profile, shadow projection, capability object, and native comparison",
            "state which indices are part of the observer-shadow object before comparing morphisms",
            "include a positive preservation control where same shadow gives same capability",
            "include a negative or hostile control where omitted indices break preservation",
            "name the completion that repairs the bookkeeping and whether it routes to an absorber",
        ),
        not_earned=(
            "observer-shadow category theorem",
            "North Star geometry proof",
            "D1, PO1, TF1, or LossKernel promotion",
            "physics or consciousness claim",
            "claim-ledger movement",
            "public-posture movement",
        ),
    )


def _transport_objects() -> tuple[ShadowAuditObject, ...]:
    result = run_t37_analysis()
    diamond = result.diamond_network_analysis
    po1_path = next(pa for pa in diamond.path_admissibilities if pa.is_po1_instance)
    non_po1_path = next(pa for pa in diamond.path_admissibilities if not pa.is_po1_instance)

    return (
        _transport_object(
            "transport_endpoint_via_L_A",
            po1_path,
            indexed=False,
        ),
        _transport_object(
            "transport_endpoint_via_L_B",
            non_po1_path,
            indexed=False,
        ),
        _transport_object(
            "transport_path_indexed_via_L_A",
            po1_path,
            indexed=True,
        ),
        _transport_object(
            "transport_path_indexed_via_L_B",
            non_po1_path,
            indexed=True,
        ),
    )


def _transport_object(
    object_id: str,
    path_admissibility: PathAdmissibility,
    *,
    indexed: bool,
) -> ShadowAuditObject:
    path = path_admissibility.path
    forgotten = _path_accumulated_forgotten(path)
    base_key = (
        "network:diamond_network",
        f"source:{path.source_name}",
        f"target:{path.target_name}",
    )
    if indexed:
        shadow_key = base_key + (
            f"path:{path_admissibility.path_label}",
            "forgotten:" + ",".join(forgotten or ("none",)),
        )
        indices = ("endpoint", "path_label", "accumulated_forgotten_structure")
    else:
        shadow_key = base_key
        indices = ("endpoint",)
    return ShadowAuditObject(
        object_id=object_id,
        family="typed_transport",
        source_system="T37 diamond typed-transport network",
        observer_profile="D1 restriction observer over SRC/TGT endpoint",
        shadow_projection="transport endpoint shadow" if not indexed else "path-indexed transport shadow",
        shadow_key=shadow_key,
        capability_object="PO1 admissibility verdict",
        capability_value="po1" if path_admissibility.is_po1_instance else "not_po1",
        native_comparison="boolean equality on PO1 evidence",
        declared_indices=indices,
    )


def _losskernel_objects() -> tuple[ShadowAuditObject, ...]:
    cases = {case.name: case for case in canonical_cases()}
    mixed_a = cases["mixed_a"]
    mixed_b = cases["mixed_b_relabelled"]
    hidden_a, hidden_b = hidden_source_escape_pair()
    return (
        _losskernel_object(
            "losskernel_neighbor_mixed_a",
            mixed_a,
            include_hidden=False,
        ),
        _losskernel_object(
            "losskernel_neighbor_mixed_b",
            mixed_b,
            include_hidden=False,
        ),
        _losskernel_object(
            "losskernel_hidden_omitted_a",
            hidden_a,
            include_hidden=False,
        ),
        _losskernel_object(
            "losskernel_hidden_omitted_b",
            hidden_b,
            include_hidden=False,
        ),
        _losskernel_object(
            "losskernel_hidden_completed_a",
            hidden_a,
            include_hidden=True,
        ),
        _losskernel_object(
            "losskernel_hidden_completed_b",
            hidden_b,
            include_hidden=True,
        ),
    )


def _losskernel_object(
    object_id: str,
    case: Case,
    *,
    include_hidden: bool,
) -> ShadowAuditObject:
    base_key = ("nu:" + _signature_digest(neighbor_signature(case)),)
    if include_hidden:
        shadow_key = base_key + (f"hidden_source:{case.hidden_source_datum}",)
        indices = ("neighbor_signature", "hidden_source_datum")
        projection = "completed neighbor-visible signature"
    else:
        shadow_key = base_key
        indices = ("neighbor_signature",)
        projection = "neighbor-visible signature nu"

    return ShadowAuditObject(
        object_id=object_id,
        family="losskernel",
        source_system="T220 LossKernel witness-obligation fixture",
        observer_profile="mature-neighbor audit observer",
        shadow_projection=projection,
        shadow_key=shadow_key,
        capability_object="canonical witness obligation",
        capability_value=_obligation_label(case),
        native_comparison="tuple equality on obligation normal form",
        declared_indices=indices,
    )


def _check_pair(
    check_id: str,
    source: ShadowAuditObject,
    target: ShadowAuditObject,
    *,
    proposed_morphism: str,
    fail_classification: str,
    obstruction: str,
    repaired_by: str,
) -> ShadowMorphismCheck:
    same_shadow = source.shadow_key == target.shadow_key
    capability_equivalent = source.capability_value == target.capability_value
    protection_preserved = (not same_shadow) or capability_equivalent

    if protection_preserved and same_shadow:
        classification = "verdict_preserved"
        final_obstruction = "none"
        final_repair = "not needed"
    elif protection_preserved and not same_shadow:
        classification = "separated_after_completion"
        final_obstruction = "none"
        final_repair = repaired_by
    else:
        classification = fail_classification
        final_obstruction = obstruction
        final_repair = repaired_by

    return ShadowMorphismCheck(
        check_id=check_id,
        family=source.family,
        source_object_id=source.object_id,
        target_object_id=target.object_id,
        proposed_morphism=proposed_morphism,
        same_shadow=same_shadow,
        capability_equivalent=capability_equivalent,
        protection_preserved=protection_preserved,
        classification=classification,
        obstruction=final_obstruction,
        repaired_by=final_repair,
    )


def _signature_digest(signature: tuple[object, ...]) -> str:
    return hashlib.sha256(repr(signature).encode("utf-8")).hexdigest()[:12]


def _obligation_label(case: Case) -> str:
    obligation = derived_obligation(case)
    if not obligation:
        return "empty_obligation"
    return "|".join(f"{left}:{right}" for left, right in obligation)


def t470_result_to_dict(result: T470Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "objects": [_object_to_dict(obj) for obj in result.objects],
        "checks": [_check_to_dict(check) for check in result.checks],
        "family_summaries": [_summary_to_dict(summary) for summary in result.family_summaries],
        "shared_schema_expresses_both_families": result.shared_schema_expresses_both_families,
        "endpoint_only_global_category_supported": result.endpoint_only_global_category_supported,
        "indexed_atlas_required": result.indexed_atlas_required,
        "claim_ledger_update": result.claim_ledger_update,
        "strongest_reading": result.strongest_reading,
        "future_packet_minimum": list(result.future_packet_minimum),
        "not_earned": list(result.not_earned),
    }


def render_markdown(result: T470Result) -> str:
    check_rows = []
    for check in result.checks:
        check_rows.append(
            "| {check_id} | {family} | {same_shadow} | {capability_equivalent} | {protection_preserved} | {classification} |".format(
                check_id=check.check_id,
                family=check.family,
                same_shadow=check.same_shadow,
                capability_equivalent=check.capability_equivalent,
                protection_preserved=check.protection_preserved,
                classification=check.classification,
            )
        )

    summary_rows = []
    for summary in result.family_summaries:
        summary_rows.append(
            "| {family} | {passes} | {requires} | {reading} |".format(
                family=summary.family,
                passes=summary.passes_shared_schema,
                requires=summary.requires_indexed_completion,
                reading=summary.strongest_reading,
            )
        )

    minimum = [f"- {item}" for item in result.future_packet_minimum]
    not_earned = [f"- {item}" for item in result.not_earned]

    return "\n".join(
        [
            "# T470 - Observer-Shadow Composition Gate - v0.1 results",
            "",
            "> First bounded run for `open-problems/observer-shadow-category.md`. "
            "No claim status, roadmap, README, North Star, public-posture, hard-policy, "
            "or cross-repo movement.",
            "",
            "- Spec: `tests/T470-observer-shadow-composition-gate.md`",
            "- Model: `models/observer_shadow_composition_gate.py`",
            "- Tests: `tests/test_observer_shadow_composition_gate.py`",
            "- Artifact JSON: `results/T470-observer-shadow-composition-gate-v0.1.json`",
            "- Source open problem: `open-problems/observer-shadow-category.md`",
            "- Reused fixtures: T37/T41 typed transport and T220 LossKernel factorization",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## Family Summaries",
            "",
            "| family | shared schema works? | indexed completion required? | strongest reading |",
            "| --- | --- | --- | --- |",
            *summary_rows,
            "",
            "## Morphism Checks",
            "",
            "| check | family | same shadow? | capability equivalent? | protection preserved? | classification |",
            "| --- | --- | --- | --- | --- | --- |",
            *check_rows,
            "",
            "## Future Packet Minimum",
            "",
            *minimum,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _object_to_dict(obj: ShadowAuditObject) -> dict[str, Any]:
    return {
        "object_id": obj.object_id,
        "family": obj.family,
        "source_system": obj.source_system,
        "observer_profile": obj.observer_profile,
        "shadow_projection": obj.shadow_projection,
        "shadow_key": list(obj.shadow_key),
        "capability_object": obj.capability_object,
        "capability_value": obj.capability_value,
        "native_comparison": obj.native_comparison,
        "declared_indices": list(obj.declared_indices),
    }


def _check_to_dict(check: ShadowMorphismCheck) -> dict[str, Any]:
    return {
        "check_id": check.check_id,
        "family": check.family,
        "source_object_id": check.source_object_id,
        "target_object_id": check.target_object_id,
        "proposed_morphism": check.proposed_morphism,
        "same_shadow": check.same_shadow,
        "capability_equivalent": check.capability_equivalent,
        "protection_preserved": check.protection_preserved,
        "classification": check.classification,
        "obstruction": check.obstruction,
        "repaired_by": check.repaired_by,
    }


def _summary_to_dict(summary: FamilySummary) -> dict[str, Any]:
    return {
        "family": summary.family,
        "checks": list(summary.checks),
        "passes_shared_schema": summary.passes_shared_schema,
        "requires_indexed_completion": summary.requires_indexed_completion,
        "strongest_reading": summary.strongest_reading,
        "not_earned": list(summary.not_earned),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t470_analysis()
    result_dict = t470_result_to_dict(result)
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(result_dict, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result_dict, indent=2))


if __name__ == "__main__":
    main()
