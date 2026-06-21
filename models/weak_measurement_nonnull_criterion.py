"""T132: executable weak-measurement non-null criterion."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProtocolShape:
    name: str
    preregistered_rule: bool
    event_level_or_intervention_defined: bool
    holder_independent: bool
    branch_independent: bool
    reversal_independent: bool
    standard_verdict_fixed: bool
    taf_verdict_changes: bool
    derived_from_same_record: bool
    branch_support_constant: bool
    reversal_monotone_proxy: bool
    uses_post_hoc_label: bool

    def independent_axes(self) -> tuple[str, ...]:
        axes: list[str] = []
        if self.holder_independent:
            axes.append("holder_redundancy")
        if self.branch_independent:
            axes.append("branch_support")
        if self.reversal_independent:
            axes.append("reversal_cost")
        return tuple(axes)


@dataclass(frozen=True)
class ProtocolAudit:
    name: str
    independent_axes: tuple[str, ...]
    classification: str
    passes_nonnull_gate: bool
    blocker: str


@dataclass(frozen=True)
class T132Result:
    audits: tuple[ProtocolAudit, ...]
    null_count: int
    candidate_count: int
    strongest_claim: str
    what_improved: str
    weakened_claim: str
    falsification_condition: str
    q1c_update: str
    blocker: str
    recommended_next: str


def protocol_shapes() -> tuple[ProtocolShape, ...]:
    return (
        ProtocolShape(
            name="threshold_only_homodyne",
            preregistered_rule=True,
            event_level_or_intervention_defined=True,
            holder_independent=False,
            branch_independent=False,
            reversal_independent=False,
            standard_verdict_fixed=False,
            taf_verdict_changes=True,
            derived_from_same_record=True,
            branch_support_constant=False,
            reversal_monotone_proxy=False,
            uses_post_hoc_label=False,
        ),
        ProtocolShape(
            name="semantic_partition_relabel",
            preregistered_rule=False,
            event_level_or_intervention_defined=False,
            holder_independent=False,
            branch_independent=True,
            reversal_independent=False,
            standard_verdict_fixed=True,
            taf_verdict_changes=True,
            derived_from_same_record=False,
            branch_support_constant=False,
            reversal_monotone_proxy=False,
            uses_post_hoc_label=True,
        ),
        ProtocolShape(
            name="same_record_branch_live",
            preregistered_rule=True,
            event_level_or_intervention_defined=True,
            holder_independent=False,
            branch_independent=True,
            reversal_independent=False,
            standard_verdict_fixed=True,
            taf_verdict_changes=True,
            derived_from_same_record=True,
            branch_support_constant=False,
            reversal_monotone_proxy=False,
            uses_post_hoc_label=False,
        ),
        ProtocolShape(
            name="constant_branch_support_family",
            preregistered_rule=True,
            event_level_or_intervention_defined=True,
            holder_independent=False,
            branch_independent=True,
            reversal_independent=False,
            standard_verdict_fixed=True,
            taf_verdict_changes=False,
            derived_from_same_record=False,
            branch_support_constant=True,
            reversal_monotone_proxy=False,
            uses_post_hoc_label=False,
        ),
        ProtocolShape(
            name="undo_energy_proxy",
            preregistered_rule=True,
            event_level_or_intervention_defined=True,
            holder_independent=False,
            branch_independent=False,
            reversal_independent=True,
            standard_verdict_fixed=True,
            taf_verdict_changes=True,
            derived_from_same_record=False,
            branch_support_constant=False,
            reversal_monotone_proxy=True,
            uses_post_hoc_label=False,
        ),
        ProtocolShape(
            name="independent_meter_not_decisive",
            preregistered_rule=True,
            event_level_or_intervention_defined=True,
            holder_independent=False,
            branch_independent=False,
            reversal_independent=True,
            standard_verdict_fixed=True,
            taf_verdict_changes=False,
            derived_from_same_record=False,
            branch_support_constant=False,
            reversal_monotone_proxy=False,
            uses_post_hoc_label=False,
        ),
        ProtocolShape(
            name="preregistered_channel_intervention_candidate",
            preregistered_rule=True,
            event_level_or_intervention_defined=True,
            holder_independent=True,
            branch_independent=False,
            reversal_independent=False,
            standard_verdict_fixed=True,
            taf_verdict_changes=True,
            derived_from_same_record=False,
            branch_support_constant=False,
            reversal_monotone_proxy=False,
            uses_post_hoc_label=False,
        ),
    )


def classify_protocol(shape: ProtocolShape) -> ProtocolAudit:
    independent_axes = shape.independent_axes()
    if not shape.preregistered_rule:
        return ProtocolAudit(
            name=shape.name,
            independent_axes=independent_axes,
            classification="null_unpreregistered_or_post_hoc",
            passes_nonnull_gate=False,
            blocker="The verdict rule is not fixed before analysis.",
        )
    if shape.uses_post_hoc_label or not shape.event_level_or_intervention_defined:
        return ProtocolAudit(
            name=shape.name,
            independent_axes=independent_axes,
            classification="null_semantic_or_post_hoc_axis",
            passes_nonnull_gate=False,
            blocker="The extra axis is semantic or post hoc rather than measured or intervention-defined.",
        )
    if shape.derived_from_same_record:
        return ProtocolAudit(
            name=shape.name,
            independent_axes=independent_axes,
            classification="null_same_record_derivation",
            passes_nonnull_gate=False,
            blocker="The extra axis is reconstructed from the same monitoring record used by standard trajectory theory.",
        )
    if shape.branch_support_constant:
        return ProtocolAudit(
            name=shape.name,
            independent_axes=independent_axes,
            classification="null_constant_branch_support",
            passes_nonnull_gate=False,
            blocker="Branch support is fixed by construction, so it cannot separate TaF verdicts.",
        )
    if shape.reversal_monotone_proxy:
        return ProtocolAudit(
            name=shape.name,
            independent_axes=independent_axes,
            classification="null_monotone_proxy_cost",
            passes_nonnull_gate=False,
            blocker="The reversal-cost variable is only a monotone proxy of ordinary support or coherence loss.",
        )
    if not independent_axes:
        return ProtocolAudit(
            name=shape.name,
            independent_axes=independent_axes,
            classification="null_no_independent_axis",
            passes_nonnull_gate=False,
            blocker="No D1 coordinate is independently operationalized.",
        )
    if not shape.standard_verdict_fixed:
        return ProtocolAudit(
            name=shape.name,
            independent_axes=independent_axes,
            classification="null_standard_statistics_also_change",
            passes_nonnull_gate=False,
            blocker="The purported witness does not isolate TaF from ordinary decoherence or redundancy changes.",
        )
    if not shape.taf_verdict_changes:
        return ProtocolAudit(
            name=shape.name,
            independent_axes=independent_axes,
            classification="independent_but_not_decisive",
            passes_nonnull_gate=False,
            blocker="An independent meter exists, but it does not change the TaF verdict under fixed standard statistics.",
        )
    return ProtocolAudit(
        name=shape.name,
        independent_axes=independent_axes,
        classification="candidate_non_null_protocol",
        passes_nonnull_gate=True,
        blocker="No blocker in the finite audit; this is the minimum admissible shape, not empirical support.",
    )


def run_t132_analysis() -> T132Result:
    audits = tuple(classify_protocol(shape) for shape in protocol_shapes())
    candidate_count = sum(1 for audit in audits if audit.passes_nonnull_gate)
    null_count = len(audits) - candidate_count
    return T132Result(
        audits=audits,
        null_count=null_count,
        candidate_count=candidate_count,
        strongest_claim=(
            "The weak-measurement route is non-null only in a narrow shape: a pre-registered, "
            "event-level or intervention-defined D1 axis must change the TaF verdict while the "
            "ordinary decoherence and redundancy verdict stays fixed."
        ),
        what_improved=(
            "T132 upgrades the weak-measurement gate from prose into a reusable audit that can reject "
            "same-record, post hoc, constant-branch, and monotone-proxy proposals before platform-specific modeling."
        ),
        weakened_claim=(
            "Most apparent T12 rescue moves are null in the present repo framing. Naming a second label, "
            "a different threshold, a constant branch count, or an undo-energy proxy does not produce a discriminator."
        ),
        falsification_condition=(
            "T132 fails if a protocol lacking a pre-registered independent axis legitimately changes the TaF verdict "
            "under fixed standard statistics, or if an admitted candidate turns out to be reconstructible from the same monitored record."
        ),
        q1c_update=(
            "Keep Q1C dormant. The surviving task is not to search for another suggestive weak-measurement story, "
            "but to name one concrete independent measured axis and show that it alone changes the TaF verdict."
        ),
        blocker=(
            "No real platform in the repo currently instantiates the admissible candidate shape with a measured, "
            "verdict-changing independent axis."
        ),
        recommended_next=(
            "Try a single monitored platform with an intervention-defined provenance or duplicated-channel axis; "
            "if that cannot be specified before modeling, demote T12 from experimental route to standing obstruction."
        ),
    )


def t132_result_to_dict(result: T132Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "name": audit.name,
                "independent_axes": list(audit.independent_axes),
                "classification": audit.classification,
                "passes_nonnull_gate": audit.passes_nonnull_gate,
                "blocker": audit.blocker,
            }
            for audit in result.audits
        ],
        "null_count": result.null_count,
        "candidate_count": result.candidate_count,
        "strongest_claim": result.strongest_claim,
        "what_improved": result.what_improved,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "q1c_update": result.q1c_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }
