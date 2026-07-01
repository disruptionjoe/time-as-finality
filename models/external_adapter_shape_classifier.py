"""T382: external adapter shape classifier.

T381 narrowed the live object to a minimal two-null-channel adapter within the
observer-relativity requirement screen. T382 classifies possible adapter shapes
for coupling something external into the shared compatibility substrate without
importing global time.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


if __package__ in (None, ""):
    sys.path.append(str(Path(__file__).resolve().parents[1]))


@dataclass(frozen=True)
class AdapterShape:
    adapter_id: str
    imports_global_time: bool
    channel_count: int
    independent_null_directions: int
    local_coupling: bool
    overcomplete: bool
    preserves_reciprocal_scaling: bool
    description: str


@dataclass(frozen=True)
class AdapterCriterion:
    criterion_id: str
    passes: bool
    reason: str


@dataclass(frozen=True)
class AdapterVerdict:
    adapter_id: str
    status: str
    classification: str
    passes: bool
    criteria: tuple[AdapterCriterion, ...]
    reason: str


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T382Result:
    uniquely_clean_adapter: str
    two_null_adapter_uniquely_clean: bool
    absolute_clock_rejected: bool
    scalar_source_action_rejected: bool
    one_channel_rejected: bool
    overcomplete_adapter_demoted: bool
    gauge_like_adapter_partial: bool
    adapter_verdicts: tuple[AdapterVerdict, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str


def adapter_shapes() -> tuple[AdapterShape, ...]:
    return (
        AdapterShape(
            adapter_id="absolute_clock",
            imports_global_time=True,
            channel_count=0,
            independent_null_directions=0,
            local_coupling=False,
            overcomplete=False,
            preserves_reciprocal_scaling=False,
            description="external adapter supplies a universal time parameter",
        ),
        AdapterShape(
            adapter_id="scalar_source_action",
            imports_global_time=False,
            channel_count=0,
            independent_null_directions=0,
            local_coupling=True,
            overcomplete=False,
            preserves_reciprocal_scaling=False,
            description="external adapter touches the substrate through one scalar action value",
        ),
        AdapterShape(
            adapter_id="one_signal_channel",
            imports_global_time=False,
            channel_count=1,
            independent_null_directions=1,
            local_coupling=True,
            overcomplete=False,
            preserves_reciprocal_scaling=False,
            description="external adapter exposes one primitive signal direction",
        ),
        AdapterShape(
            adapter_id="two_null_channel",
            imports_global_time=False,
            channel_count=2,
            independent_null_directions=2,
            local_coupling=True,
            overcomplete=False,
            preserves_reciprocal_scaling=True,
            description="external adapter exposes two independent primitive null signal directions",
        ),
        AdapterShape(
            adapter_id="overcomplete_multi_channel",
            imports_global_time=False,
            channel_count=3,
            independent_null_directions=3,
            local_coupling=True,
            overcomplete=True,
            preserves_reciprocal_scaling=False,
            description="external adapter exposes more primitive directions than a 1+1 null basis can use",
        ),
        AdapterShape(
            adapter_id="gauge_like_local_adapter",
            imports_global_time=False,
            channel_count=2,
            independent_null_directions=2,
            local_coupling=True,
            overcomplete=False,
            preserves_reciprocal_scaling=False,
            description="external adapter changes local labels without fixing the reciprocal signal calibration",
        ),
    )


def evaluate_adapter(shape: AdapterShape) -> AdapterVerdict:
    criteria = (
        AdapterCriterion(
            "no_global_time_import",
            not shape.imports_global_time,
            "adapter must not supply an absolute clock",
        ),
        AdapterCriterion(
            "local_substrate_coupling",
            shape.local_coupling,
            "adapter should touch local compatibility relations, not a global readout",
        ),
        AdapterCriterion(
            "two_independent_null_directions",
            shape.independent_null_directions == 2,
            "observer relativity needs two independent null signal directions",
        ),
        AdapterCriterion(
            "minimal_not_overcomplete",
            shape.channel_count == 2 and not shape.overcomplete,
            "adapter should be the minimal primitive interface, not an undercomplete or overcomplete one",
        ),
        AdapterCriterion(
            "reciprocal_scaling_support",
            shape.preserves_reciprocal_scaling,
            "adapter must support the reciprocal observer family that preserves the interval",
        ),
    )
    passes = all(criterion.passes for criterion in criteria)
    if passes:
        status = "uniquely_clean"
        classification = "survivor"
        reason = "minimal two-null-channel adapter satisfies every declared coupling criterion"
    elif shape.imports_global_time:
        status = "rejected_global_clock"
        classification = "null"
        reason = "absolute time solves the problem by importing the thing the substrate is meant to render"
    elif shape.channel_count == 0:
        status = "rejected_no_signal_geometry"
        classification = "null"
        reason = "scalar coupling has no directional signal geometry for relativity"
    elif shape.independent_null_directions < 2:
        status = "rejected_undercomplete"
        classification = "null"
        reason = "one signal direction cannot support two-sided observer relativity"
    elif shape.overcomplete:
        status = "demoted_overcomplete"
        classification = "demoted"
        reason = "extra primitive directions overconstrain or must factor through the two-null basis"
    elif not shape.preserves_reciprocal_scaling:
        status = "partial_gauge_relabel_only"
        classification = "partial"
        reason = "local relabeling may preserve substrate identity but does not supply observer calibration"
    else:
        status = "failed"
        classification = "null"
        reason = "adapter misses a required criterion"

    return AdapterVerdict(
        adapter_id=shape.adapter_id,
        status=status,
        classification=classification,
        passes=passes,
        criteria=criteria,
        reason=reason,
    )


def evaluate_adapters() -> tuple[AdapterVerdict, ...]:
    return tuple(evaluate_adapter(shape) for shape in adapter_shapes())


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            "adapter_uniqueness",
            "supported_within_declared_shapes",
            False,
            "the two-null-channel adapter is the only clean survivor among the declared shapes",
        ),
        ComparatorVerdict(
            "shape_catalog_completeness",
            "still_absorbs",
            True,
            "the classifier does not enumerate every mathematically possible adapter",
        ),
        ComparatorVerdict(
            "external_origin",
            "still_open",
            True,
            "the classifier can say which shape is clean, not where it comes from",
        ),
        ComparatorVerdict(
            "global_clock_shortcut",
            "rejected",
            False,
            "absolute clock adapters are explicitly rejected as importing global time",
        ),
    )


def run_t382_analysis() -> T382Result:
    verdicts = evaluate_adapters()
    by_id = {verdict.adapter_id: verdict for verdict in verdicts}
    survivors = tuple(verdict.adapter_id for verdict in verdicts if verdict.passes)
    clean = survivors[0] if survivors else ""
    return T382Result(
        uniquely_clean_adapter=clean,
        two_null_adapter_uniquely_clean=survivors == ("two_null_channel",),
        absolute_clock_rejected=by_id["absolute_clock"].status == "rejected_global_clock",
        scalar_source_action_rejected=(
            by_id["scalar_source_action"].status == "rejected_no_signal_geometry"
        ),
        one_channel_rejected=by_id["one_signal_channel"].status == "rejected_undercomplete",
        overcomplete_adapter_demoted=(
            by_id["overcomplete_multi_channel"].status == "demoted_overcomplete"
        ),
        gauge_like_adapter_partial=(
            by_id["gauge_like_local_adapter"].status == "partial_gauge_relabel_only"
        ),
        adapter_verdicts=verdicts,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict="two_null_channel_adapter_uniquely_clean_within_catalog",
        strongest_claim=(
            "Among the declared external-adapter shapes, the two-null-channel adapter is the only "
            "one that avoids global time import, couples locally, provides two independent null "
            "signal directions, stays minimal, and supports reciprocal observer scaling."
        ),
        claim_ledger_update=(
            "Register T382 as adapter-shape evidence: the two-null-channel object is the cleanest "
            "external interface candidate, but catalog completeness and origin remain open."
        ),
    )


def t382_result_to_dict(result: T382Result) -> dict[str, object]:
    return {
        "uniquely_clean_adapter": result.uniquely_clean_adapter,
        "two_null_adapter_uniquely_clean": result.two_null_adapter_uniquely_clean,
        "absolute_clock_rejected": result.absolute_clock_rejected,
        "scalar_source_action_rejected": result.scalar_source_action_rejected,
        "one_channel_rejected": result.one_channel_rejected,
        "overcomplete_adapter_demoted": result.overcomplete_adapter_demoted,
        "gauge_like_adapter_partial": result.gauge_like_adapter_partial,
        "adapter_verdicts": [
            {
                "adapter_id": verdict.adapter_id,
                "status": verdict.status,
                "classification": verdict.classification,
                "passes": verdict.passes,
                "criteria": [
                    {
                        "criterion_id": criterion.criterion_id,
                        "passes": criterion.passes,
                        "reason": criterion.reason,
                    }
                    for criterion in verdict.criteria
                ],
                "reason": verdict.reason,
            }
            for verdict in result.adapter_verdicts
        ],
        "comparator_verdicts": [
            {
                "comparator_id": verdict.comparator_id,
                "status": verdict.status,
                "absorbs": verdict.absorbs,
                "reason": verdict.reason,
            }
            for verdict in result.comparator_verdicts
        ],
        "overall_verdict": result.overall_verdict,
        "strongest_claim": result.strongest_claim,
        "claim_ledger_update": result.claim_ledger_update,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t382_result_to_dict(run_t382_analysis()), indent=2))
