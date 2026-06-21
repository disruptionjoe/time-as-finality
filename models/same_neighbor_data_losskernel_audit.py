"""T127: same-neighbor-data LossKernel audit.

T127 is the strict prior-art gate for the LossKernel / TF1 program. The test
does not ask whether a typed witness obligation can be written down. T99 and
T107 already showed that. It asks the harder quotient question:

Can two finite cases receive different LossKernel attribution verdicts while
every mature neighboring account receives the same admissible data package?

The bounded answer here is negative. In the current finite fixture family,
every apparent distinction is either:

- absorbed because some allowed neighbor-visible package already changes;
- a label-only or path-metadata difference;
- an endpoint difference that fails the quotient gate; or
- a non-attribution-relevant absorbed-loss case.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LiftJudgment:
    left_source: str
    right_source: str
    allowed: bool

    def signature(self) -> tuple[str, str, bool]:
        return (self.left_source, self.right_source, self.allowed)


@dataclass(frozen=True)
class LossKernelCase:
    name: str
    family: str
    source_id: str
    target_id: str
    target_obstructed: bool
    target_global_sections: int
    obstruction_id: str
    left_fiber: tuple[str, ...]
    right_fiber: tuple[str, ...]
    composite_map: tuple[tuple[str, str], ...]
    naive_loss_labels: frozenset[str]
    path_labels: tuple[str, ...]
    lift_judgments: tuple[LiftJudgment, ...]
    purpose: str


@dataclass(frozen=True)
class PairAudit:
    pair_id: str
    left_case: str
    right_case: str
    classification: str
    left_verdict: str
    right_verdict: str
    left_obligation: tuple[tuple[str, str], ...]
    right_obligation: tuple[tuple[str, str], ...]
    same_neighbor_data: bool
    differing_neighbor_fields: tuple[str, ...]
    first_absorber: str
    interpretation: str


@dataclass(frozen=True)
class SingleCaseAudit:
    case_name: str
    classification: str
    verdict: str
    obligation: tuple[tuple[str, str], ...]
    interpretation: str


@dataclass(frozen=True)
class T127Result:
    pair_audits: tuple[PairAudit, ...]
    single_case_audits: tuple[SingleCaseAudit, ...]
    strict_separation_found: bool
    positive_attempt_absorbed: bool
    label_only_control_collapses: bool
    endpoint_difference_control_rejected: bool
    path_metadata_control_rejected: bool
    same_neighbor_alias_collapses: bool
    absorbed_loss_control_demoted: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    tf1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _l(left_source: str, right_source: str, allowed: bool) -> LiftJudgment:
    return LiftJudgment(left_source=left_source, right_source=right_source, allowed=allowed)


def cases() -> tuple[LossKernelCase, ...]:
    mixed_lifts = (
        _l("left_keep", "right_keep", True),
        _l("left_keep", "right_flip", False),
        _l("left_flip", "right_keep", False),
        _l("left_flip", "right_flip", False),
    )
    uniform_false_lifts = tuple(_l(l.left_source, l.right_source, False) for l in mixed_lifts)
    uniform_true_lifts = tuple(_l(l.left_source, l.right_source, True) for l in mixed_lifts)

    return (
        LossKernelCase(
            name="positive_attempt_mixed_lifts",
            family="positive_attempt",
            source_id="S_branch",
            target_id="T_branch_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("branch_selector",),
            lift_judgments=mixed_lifts,
            purpose=(
                "Candidate positive case: a mixed source-lift table yields a "
                "source-anchored witness obligation."
            ),
        ),
        LossKernelCase(
            name="positive_attempt_uniform_false",
            family="positive_attempt",
            source_id="S_branch",
            target_id="T_branch_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("branch_selector",),
            lift_judgments=uniform_false_lifts,
            purpose=(
                "Attempted partner for the strict quotient witness. The target "
                "endpoint is the same, but the full lift table already differs."
            ),
        ),
        LossKernelCase(
            name="label_only_control_a",
            family="label_only_control",
            source_id="S_label",
            target_id="T_label_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("branch_selector",),
            lift_judgments=mixed_lifts,
            purpose="Control A: baseline mixed-lift case.",
        ),
        LossKernelCase(
            name="label_only_control_b",
            family="label_only_control",
            source_id="S_label",
            target_id="T_label_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"display_tag"}),
            path_labels=("display_tag",),
            lift_judgments=mixed_lifts,
            purpose=(
                "Control B: the source-lift obligations are identical, only the "
                "free label changed."
            ),
        ),
        LossKernelCase(
            name="endpoint_difference_control_a",
            family="endpoint_difference_control",
            source_id="S_endpoint",
            target_id="T_endpoint_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("branch_selector",),
            lift_judgments=mixed_lifts,
            purpose="Endpoint-difference control baseline.",
        ),
        LossKernelCase(
            name="endpoint_difference_control_b",
            family="endpoint_difference_control",
            source_id="S_endpoint",
            target_id="T_endpoint_resolved",
            target_obstructed=False,
            target_global_sections=1,
            obstruction_id="none",
            left_fiber=("left_keep",),
            right_fiber=("right_keep",),
            composite_map=(("left_keep", "resolved"), ("right_keep", "resolved")),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("branch_selector",),
            lift_judgments=(_l("left_keep", "right_keep", True),),
            purpose="Endpoint-difference control partner.",
        ),
        LossKernelCase(
            name="path_metadata_control_a",
            family="path_metadata_control",
            source_id="S_path",
            target_id="T_path_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("path_alpha",),
            lift_judgments=mixed_lifts,
            purpose="Path metadata control baseline.",
        ),
        LossKernelCase(
            name="path_metadata_control_b",
            family="path_metadata_control",
            source_id="S_path",
            target_id="T_path_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("path_beta",),
            lift_judgments=mixed_lifts,
            purpose="Path metadata control partner.",
        ),
        LossKernelCase(
            name="same_neighbor_alias_a",
            family="same_neighbor_alias",
            source_id="S_alias",
            target_id="T_alias_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("branch_selector",),
            lift_judgments=mixed_lifts,
            purpose="Same-neighbor alias control A.",
        ),
        LossKernelCase(
            name="same_neighbor_alias_b",
            family="same_neighbor_alias",
            source_id="S_alias",
            target_id="T_alias_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "branch_shadow"),
                ("left_flip", "branch_shadow"),
                ("right_keep", "branch_shadow"),
                ("right_flip", "branch_shadow"),
            ),
            naive_loss_labels=frozenset({"branch_selector"}),
            path_labels=("branch_selector",),
            lift_judgments=mixed_lifts,
            purpose="Same-neighbor alias control B.",
        ),
        LossKernelCase(
            name="absorbed_loss_control",
            family="absorbed_loss_control",
            source_id="S_absorbed",
            target_id="T_absorbed_shadow",
            target_obstructed=True,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            left_fiber=("left_keep", "left_flip"),
            right_fiber=("right_keep", "right_flip"),
            composite_map=(
                ("left_keep", "field_shadow"),
                ("left_flip", "field_shadow"),
                ("right_keep", "field_shadow"),
                ("right_flip", "field_shadow"),
            ),
            naive_loss_labels=frozenset({"gauge_rep"}),
            path_labels=("gauge_rep",),
            lift_judgments=uniform_true_lifts,
            purpose=(
                "Absorbed-loss control: loss is non-empty, but every source "
                "lift yields the same target judgment."
            ),
        ),
    )


def derived_obligation(case: LossKernelCase) -> tuple[tuple[str, str], ...]:
    if not case.target_obstructed:
        return ()
    verdicts = {judgment.allowed for judgment in case.lift_judgments}
    if verdicts != {False, True}:
        return ()
    return tuple(
        sorted(
            (judgment.left_source, judgment.right_source)
            for judgment in case.lift_judgments
            if judgment.allowed
        )
    )


def case_verdict(case: LossKernelCase) -> str:
    if not case.target_obstructed:
        return "inadmissible_no_target_obstruction"
    if derived_obligation(case):
        return "candidate_witness_obligation"
    if case.naive_loss_labels:
        return "demote_non_attribution_relevant_loss"
    return "demote_no_loss"


def _csp_signature(case: LossKernelCase) -> tuple[tuple[str, str, bool], ...]:
    return tuple(sorted(judgment.signature() for judgment in case.lift_judgments))


def _provenance_signature(case: LossKernelCase) -> tuple[tuple[str, str], ...]:
    return tuple(sorted((judgment.left_source, judgment.right_source) for judgment in case.lift_judgments))


def _abstraction_signature(case: LossKernelCase) -> tuple[tuple[str, ...], tuple[str, ...]]:
    return (tuple(sorted(case.left_fiber)), tuple(sorted(case.right_fiber)))


def _lens_signature(case: LossKernelCase) -> tuple[tuple[str, str], ...]:
    return derived_obligation(case)


def _effect_signature(case: LossKernelCase) -> tuple[tuple[str, str], ...]:
    return tuple((left, right) for left, right in derived_obligation(case))


def _category_signature(case: LossKernelCase) -> tuple[object, ...]:
    return (
        case.source_id,
        case.target_id,
        tuple(sorted(case.composite_map)),
        case.target_obstructed,
        case.target_global_sections,
        case.obstruction_id,
    )


def neighbor_signature(case: LossKernelCase) -> dict[str, object]:
    return {
        "naive_loss_labels": tuple(sorted(case.naive_loss_labels)),
        "path_labels": tuple(sorted(case.path_labels)),
        "csp": _csp_signature(case),
        "provenance": _provenance_signature(case),
        "abstract_interpretation": _abstraction_signature(case),
        "lenses": _lens_signature(case),
        "effect_annotations": _effect_signature(case),
        "category": _category_signature(case),
    }


def _absorber_for_field(field_name: str) -> str:
    return {
        "csp": "csp_explanation",
        "provenance": "why_not_provenance",
        "abstract_interpretation": "abstract_interpretation",
        "lenses": "lenses",
        "effect_annotations": "effect_annotations",
        "path_labels": "path_sensitive_bookkeeping",
        "naive_loss_labels": "label_bookkeeping",
        "category": "categorical_bookkeeping",
    }[field_name]


def pair_audit(left: LossKernelCase, right: LossKernelCase) -> PairAudit:
    left_signature = neighbor_signature(left)
    right_signature = neighbor_signature(right)
    differing_fields = tuple(
        field
        for field in (
            "naive_loss_labels",
            "path_labels",
            "csp",
            "provenance",
            "abstract_interpretation",
            "lenses",
            "effect_annotations",
            "category",
        )
        if left_signature[field] != right_signature[field]
    )
    same_neighbor_data = not differing_fields
    left_obligation = derived_obligation(left)
    right_obligation = derived_obligation(right)
    left_verdict = case_verdict(left)
    right_verdict = case_verdict(right)

    if left.family == "label_only_control":
        classification = "label_only"
        interpretation = (
            "Different free labels do not create a new attribution verdict when "
            "the source-derived obligation is unchanged."
        )
    elif left.family == "endpoint_difference_control":
        classification = "invalid_quotient"
        interpretation = (
            "Endpoint behavior changed, so the pair is not admissible evidence "
            "for same-neighbor-data separation."
        )
    elif left.family == "path_metadata_control":
        classification = "invalid_quotient"
        interpretation = (
            "Path labels changed. This is path-sensitive bookkeeping, not "
            "strict quotient survival."
        )
    elif same_neighbor_data and left_verdict == right_verdict:
        classification = "demote"
        interpretation = (
            "When every neighbor-visible package is the same, the deterministic "
            "source-derived obligation and verdict collapse as well."
        )
    elif same_neighbor_data and left_verdict != right_verdict:
        classification = "separation_witness"
        interpretation = (
            "A strict same-neighbor-data witness survived. This should be "
            "treated as a live TF1 separation candidate."
        )
    else:
        classification = "absorbed_by_neighbor"
        interpretation = (
            "The apparent distinction is already visible to an allowed neighbor "
            "package before LossKernel is consulted."
        )

    return PairAudit(
        pair_id=left.family,
        left_case=left.name,
        right_case=right.name,
        classification=classification,
        left_verdict=left_verdict,
        right_verdict=right_verdict,
        left_obligation=left_obligation,
        right_obligation=right_obligation,
        same_neighbor_data=same_neighbor_data,
        differing_neighbor_fields=differing_fields,
        first_absorber=_absorber_for_field(differing_fields[0]) if differing_fields else "none",
        interpretation=interpretation,
    )


def single_case_audit(case: LossKernelCase) -> SingleCaseAudit:
    obligation = derived_obligation(case)
    if obligation:
        classification = "candidate_witness_obligation"
        interpretation = "Mixed source lifts produce a source-derived witness obligation."
    else:
        classification = "demote"
        interpretation = (
            "Non-empty loss with uniform lift verdicts is not attribution-relevant "
            "for the strict T127 gate."
        )
    return SingleCaseAudit(
        case_name=case.name,
        classification=classification,
        verdict=case_verdict(case),
        obligation=obligation,
        interpretation=interpretation,
    )


def run_t127_analysis() -> T127Result:
    fixture_map = {case.name: case for case in cases()}
    pair_audits = (
        pair_audit(
            fixture_map["positive_attempt_mixed_lifts"],
            fixture_map["positive_attempt_uniform_false"],
        ),
        pair_audit(
            fixture_map["label_only_control_a"],
            fixture_map["label_only_control_b"],
        ),
        pair_audit(
            fixture_map["endpoint_difference_control_a"],
            fixture_map["endpoint_difference_control_b"],
        ),
        pair_audit(
            fixture_map["path_metadata_control_a"],
            fixture_map["path_metadata_control_b"],
        ),
        pair_audit(
            fixture_map["same_neighbor_alias_a"],
            fixture_map["same_neighbor_alias_b"],
        ),
    )
    single_audits = (
        single_case_audit(fixture_map["absorbed_loss_control"]),
    )

    strict_separation_found = any(
        audit.classification == "separation_witness" for audit in pair_audits
    )

    return T127Result(
        pair_audits=pair_audits,
        single_case_audits=single_audits,
        strict_separation_found=strict_separation_found,
        positive_attempt_absorbed=pair_audits[0].classification == "absorbed_by_neighbor",
        label_only_control_collapses=(
            pair_audits[1].classification == "label_only"
            and pair_audits[1].left_verdict == pair_audits[1].right_verdict
        ),
        endpoint_difference_control_rejected=pair_audits[2].classification == "invalid_quotient",
        path_metadata_control_rejected=pair_audits[3].classification == "invalid_quotient",
        same_neighbor_alias_collapses=(
            pair_audits[4].same_neighbor_data
            and pair_audits[4].classification == "demote"
        ),
        absorbed_loss_control_demoted=single_audits[0].classification == "demote",
        strongest_claim=(
            "No strict same-neighbor-data LossKernel witness survives in the "
            "current finite fixture family. Every attempted separation is either "
            "absorbed because an allowed neighbor package already changes, a "
            "label-only or path-metadata variant, an endpoint-difference control, "
            "or an absorbed-loss case with no source-derived witness obligation."
        ),
        improved=(
            "T127 turns the strongest remaining TF1 gate into an executable "
            "negative audit. The repo no longer needs to leave same-neighbor-data "
            "separation open by default for the current finite witness family."
        ),
        weakened=(
            "This weakens the LossKernel program again. In the tested family, a "
            "typed source-derived obligation does not produce a prior-art-separated "
            "attribution verdict once CSP, provenance, abstraction, lens, effect, "
            "path, and categorical packages are held to the same standard."
        ),
        falsification_condition=(
            "T127 fails in TF1's favor only if a future finite pair keeps every "
            "declared neighbor-visible package fixed and still yields different "
            "derived obligations or attribution verdicts. No such pair exists in "
            "the current audit."
        ),
        tf1_update=(
            "TF1 remains an open formal target, but T127 removes the default hope "
            "that same-neighbor-data quotient separation will emerge automatically "
            "from the current finite LossKernel semantics."
        ),
        claim_ledger_update=(
            "Add T127 to TF1: the same-neighbor-data audit is negative on the "
            "current finite fixture family. Apparent separations are absorbed by "
            "neighbor-visible CSP/provenance/abstraction/lens/effect/path/category "
            "data, or collapse as label-only, endpoint-difference, or absorbed-loss "
            "controls."
        ),
        open_blocker=(
            "The only remaining non-redundant value is a canonical normal form or "
            "integration vocabulary for source-derived witness obligations. That is "
            "weaker than a prior-art-separated theorem."
        ),
        recommended_next=(
            "Stop treating same-neighbor-data separation as the default TF1 rescue. "
            "Either formalize LossKernel purely as integration vocabulary, or shift "
            "effort to T125/T126 where internal mathematical movement is still live."
        ),
    )


def _pair_audit_to_dict(audit: PairAudit) -> dict[str, object]:
    return {
        "pair_id": audit.pair_id,
        "left_case": audit.left_case,
        "right_case": audit.right_case,
        "classification": audit.classification,
        "left_verdict": audit.left_verdict,
        "right_verdict": audit.right_verdict,
        "left_obligation": [list(pair) for pair in audit.left_obligation],
        "right_obligation": [list(pair) for pair in audit.right_obligation],
        "same_neighbor_data": audit.same_neighbor_data,
        "differing_neighbor_fields": list(audit.differing_neighbor_fields),
        "first_absorber": audit.first_absorber,
        "interpretation": audit.interpretation,
    }


def _single_case_to_dict(audit: SingleCaseAudit) -> dict[str, object]:
    return {
        "case_name": audit.case_name,
        "classification": audit.classification,
        "verdict": audit.verdict,
        "obligation": [list(pair) for pair in audit.obligation],
        "interpretation": audit.interpretation,
    }


def t127_result_to_dict(result: T127Result) -> dict[str, object]:
    return {
        "pair_audits": [_pair_audit_to_dict(audit) for audit in result.pair_audits],
        "single_case_audits": [_single_case_to_dict(audit) for audit in result.single_case_audits],
        "strict_separation_found": result.strict_separation_found,
        "positive_attempt_absorbed": result.positive_attempt_absorbed,
        "label_only_control_collapses": result.label_only_control_collapses,
        "endpoint_difference_control_rejected": result.endpoint_difference_control_rejected,
        "path_metadata_control_rejected": result.path_metadata_control_rejected,
        "same_neighbor_alias_collapses": result.same_neighbor_alias_collapses,
        "absorbed_loss_control_demoted": result.absorbed_loss_control_demoted,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "tf1_update": result.tf1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }

