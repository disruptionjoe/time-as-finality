"""T99: LossKernel quotient-separation audit.

T73 showed that the current LossKernel machinery earns a powerset-union
annotation law on finite fixtures. T99 asks the harder quotient question:
does anything survive after quotienting by same endpoints, same ordinary
composite map, same endpoint behavior, and same naive lost-label set?

The answer here is intentionally mixed. A label-only LossKernel fails the
quotient gate. A witness-carrying LossKernel can separate the fixtures, but
only by adding source-anchored witness obligations that are not present in
the label-union object.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class EndpointBehavior:
    target_obstructed: bool
    target_global_sections: int
    obstruction_ids: tuple[str, ...]
    observables: tuple[tuple[str, str], ...]

    def signature(self) -> tuple[object, ...]:
        return (
            self.target_obstructed,
            self.target_global_sections,
            tuple(sorted(self.obstruction_ids)),
            tuple(sorted(self.observables)),
        )


@dataclass(frozen=True)
class TypedLossWitness:
    label: str
    witness_id: str
    witness_type: str
    source_anchor: str
    resolves_obstruction: bool
    obstruction_id: str

    def signature(self) -> tuple[object, ...]:
        return (
            self.label,
            self.witness_id,
            self.witness_type,
            self.source_anchor,
            self.resolves_obstruction,
            self.obstruction_id,
        )


@dataclass(frozen=True)
class PathCase:
    name: str
    family: str
    source_id: str
    target_id: str
    ordinary_composite_map: tuple[tuple[str, str], ...]
    endpoint_behavior: EndpointBehavior
    naive_loss_labels: frozenset[str]
    typed_loss: tuple[TypedLossWitness, ...]
    purpose: str


@dataclass(frozen=True)
class QuotientGroup:
    group_id: str
    case_names: tuple[str, ...]
    verdicts: tuple[str, ...]
    typed_signatures: tuple[tuple[tuple[object, ...], ...], ...]
    naive_key_shared: bool
    naive_collision: bool
    typed_witness_separates: bool


@dataclass(frozen=True)
class T99Result:
    cases: tuple[PathCase, ...]
    quotient_groups: tuple[QuotientGroup, ...]
    naive_label_kernel_fails_quotient_gate: bool
    typed_witness_kernel_separates_collision: bool
    same_typed_control_collapses: bool
    endpoint_difference_control_excluded: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    tf1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def obstruction_endpoint() -> EndpointBehavior:
    return EndpointBehavior(
        target_obstructed=True,
        target_global_sections=0,
        obstruction_ids=("target_branch_ambiguity",),
        observables=(
            ("target_visible_state", "lumped_branch"),
            ("compatible_source_preimages", "2"),
        ),
    )


def unobstructed_endpoint() -> EndpointBehavior:
    return EndpointBehavior(
        target_obstructed=False,
        target_global_sections=1,
        obstruction_ids=(),
        observables=(
            ("target_visible_state", "resolved_branch"),
            ("compatible_source_preimages", "1"),
        ),
    )


def shared_ordinary_map() -> tuple[tuple[str, str], ...]:
    return (
        ("left_source_branch", "lumped_branch"),
        ("right_source_branch", "lumped_branch"),
    )


def path_fixtures() -> tuple[PathCase, ...]:
    """Return finite fixtures for the quotient test."""

    relevant_branch_loss = TypedLossWitness(
        label="branch_selector",
        witness_id="signed_preimage_selector",
        witness_type="source_global_section_resolver",
        source_anchor="source_certificate:branch-preimage-resolves-ambiguity",
        resolves_obstruction=True,
        obstruction_id="target_branch_ambiguity",
    )
    decorative_branch_loss = TypedLossWitness(
        label="branch_selector",
        witness_id="display_color_tag",
        witness_type="decorative_metadata",
        source_anchor="source_annotation:display-only-color",
        resolves_obstruction=False,
        obstruction_id="none",
    )
    duplicate_relevant_loss = TypedLossWitness(
        label="branch_selector",
        witness_id="signed_preimage_selector",
        witness_type="source_global_section_resolver",
        source_anchor="source_certificate:branch-preimage-resolves-ambiguity",
        resolves_obstruction=True,
        obstruction_id="target_branch_ambiguity",
    )

    return (
        PathCase(
            name="collision_path_relevant_witness",
            family="same_naive_quotient_collision",
            source_id="S_branch_fixture",
            target_id="T_lumped_branch",
            ordinary_composite_map=shared_ordinary_map(),
            endpoint_behavior=obstruction_endpoint(),
            naive_loss_labels=frozenset({"branch_selector"}),
            typed_loss=(relevant_branch_loss,),
            purpose=(
                "Same ordinary endpoint data as the decorative path, but the "
                "lost branch_selector is a source-side witness resolving the "
                "target ambiguity."
            ),
        ),
        PathCase(
            name="collision_path_decorative_label",
            family="same_naive_quotient_collision",
            source_id="S_branch_fixture",
            target_id="T_lumped_branch",
            ordinary_composite_map=shared_ordinary_map(),
            endpoint_behavior=obstruction_endpoint(),
            naive_loss_labels=frozenset({"branch_selector"}),
            typed_loss=(decorative_branch_loss,),
            purpose=(
                "Same ordinary endpoint data and same naive lost label, but "
                "the lost branch_selector is only a display annotation."
            ),
        ),
        PathCase(
            name="same_typed_alias_a",
            family="same_typed_control",
            source_id="S_alias_fixture",
            target_id="T_alias_lumped_branch",
            ordinary_composite_map=shared_ordinary_map(),
            endpoint_behavior=obstruction_endpoint(),
            naive_loss_labels=frozenset({"branch_selector"}),
            typed_loss=(duplicate_relevant_loss,),
            purpose="Control: an alias of the relevant typed witness should collapse.",
        ),
        PathCase(
            name="same_typed_alias_b",
            family="same_typed_control",
            source_id="S_alias_fixture",
            target_id="T_alias_lumped_branch",
            ordinary_composite_map=shared_ordinary_map(),
            endpoint_behavior=obstruction_endpoint(),
            naive_loss_labels=frozenset({"branch_selector"}),
            typed_loss=(duplicate_relevant_loss,),
            purpose="Control: same typed loss data should not create a new distinction.",
        ),
        PathCase(
            name="endpoint_difference_control",
            family="endpoint_difference_control",
            source_id="S_branch_fixture",
            target_id="T_resolved_branch",
            ordinary_composite_map=(("left_source_branch", "resolved_branch"),),
            endpoint_behavior=unobstructed_endpoint(),
            naive_loss_labels=frozenset({"branch_selector"}),
            typed_loss=(relevant_branch_loss,),
            purpose=(
                "Control: same lost label but a different unobstructed endpoint "
                "is not evidence for quotient survival."
            ),
        ),
    )


def attribution_verdict(case: PathCase) -> str:
    if not case.endpoint_behavior.target_obstructed:
        return "inadmissible_no_target_obstruction"
    if not case.naive_loss_labels:
        return "inadmissible_no_loss"

    obstruction_ids = set(case.endpoint_behavior.obstruction_ids)
    has_relevant_witness = any(
        witness.resolves_obstruction and witness.obstruction_id in obstruction_ids
        for witness in case.typed_loss
    )
    if has_relevant_witness:
        return "admissible_typed_attribution"
    return "inadmissible_label_only_metadata"


def naive_quotient_key(case: PathCase) -> tuple[object, ...]:
    return (
        case.source_id,
        case.target_id,
        tuple(sorted(case.ordinary_composite_map)),
        case.endpoint_behavior.signature(),
        tuple(sorted(case.naive_loss_labels)),
    )


def typed_signature(case: PathCase) -> tuple[tuple[object, ...], ...]:
    return tuple(sorted(witness.signature() for witness in case.typed_loss))


def group_by_naive_quotient(cases: tuple[PathCase, ...]) -> tuple[QuotientGroup, ...]:
    grouped: dict[tuple[object, ...], list[PathCase]] = {}
    for case in cases:
        grouped.setdefault(naive_quotient_key(case), []).append(case)

    result: list[QuotientGroup] = []
    for index, (_, members) in enumerate(grouped.items(), start=1):
        verdicts = tuple(attribution_verdict(member) for member in members)
        signatures = tuple(typed_signature(member) for member in members)
        unique_verdicts = set(verdicts)
        unique_signatures = set(signatures)
        result.append(
            QuotientGroup(
                group_id=f"naive_quotient_group_{index}",
                case_names=tuple(member.name for member in members),
                verdicts=verdicts,
                typed_signatures=signatures,
                naive_key_shared=len(members) > 1,
                naive_collision=len(members) > 1 and len(unique_verdicts) > 1,
                typed_witness_separates=(
                    len(members) > 1
                    and len(unique_signatures) == len(unique_verdicts)
                    and len(unique_verdicts) > 1
                ),
            )
        )
    return tuple(result)


def _group_for_family(
    groups: tuple[QuotientGroup, ...],
    cases: tuple[PathCase, ...],
    family: str,
) -> QuotientGroup:
    names = {case.name for case in cases if case.family == family}
    for group in groups:
        if names <= set(group.case_names):
            return group
    raise ValueError(f"No quotient group contains family {family!r}")


def run_t99_analysis() -> T99Result:
    cases = path_fixtures()
    groups = group_by_naive_quotient(cases)
    collision_group = _group_for_family(groups, cases, "same_naive_quotient_collision")
    same_typed_group = _group_for_family(groups, cases, "same_typed_control")

    endpoint_control = next(case for case in cases if case.family == "endpoint_difference_control")
    endpoint_control_excluded = not any(
        endpoint_control.name in group.case_names and group.naive_collision
        for group in groups
    )

    naive_fails = collision_group.naive_collision
    typed_separates = collision_group.typed_witness_separates
    same_typed_collapses = (
        same_typed_group.naive_key_shared
        and not same_typed_group.naive_collision
        and len(set(same_typed_group.typed_signatures)) == 1
    )

    return T99Result(
        cases=cases,
        quotient_groups=groups,
        naive_label_kernel_fails_quotient_gate=naive_fails,
        typed_witness_kernel_separates_collision=typed_separates,
        same_typed_control_collapses=same_typed_collapses,
        endpoint_difference_control_excluded=endpoint_control_excluded,
        strongest_claim=(
            "The label-only LossKernel does not survive the quotient gate: two "
            "paths can share endpoints, ordinary composite map, endpoint "
            "behavior, and naive lost-label set while receiving opposite "
            "attribution verdicts. A typed witness kernel separates them only "
            "if LossKernel records source-anchored witness obligations, not "
            "just lost labels."
        ),
        improved=(
            "T99 turns the open quotient-survival worry into an executable "
            "audit. It shows exactly where the current T73 union law is too "
            "weak and what extra data would be required for TF1 to become a "
            "serious attribution object."
        ),
        weakened=(
            "This weakens LossKernel promotion. The current powerset-union "
            "object is not enough for quotient/prior-art separation. Without "
            "source-anchored witness obligations, LossKernel remains a "
            "provenance/effect-style annotation."
        ),
        falsification_condition=(
            "Reject theorem-level TF1 language if future LossKernel definitions "
            "cannot canonically derive witness obligations from the morphism "
            "and source/target structures, or if those obligations collapse to "
            "ordinary provenance labels under the same quotient."
        ),
        tf1_update=(
            "TF1 remains an open formal target. T99 supplies a conditional "
            "salvage path: typed loss must include source witnesses that "
            "resolve target obstructions. Label-only loss is refuted as a "
            "sufficient object for the quotient gate."
        ),
        claim_ledger_update=(
            "Add T99 to TF1: naive label-union LossKernel fails quotient "
            "survival; only a source-anchored witness-obligation kernel "
            "separates same-endpoint, same-map, same-behavior, same-label "
            "fixtures, so TF1 remains open and cannot be promoted from T73."
        ),
        open_blocker=(
            "The typed witness obligations in T99 are still fixture-declared. "
            "The next blocker is canonical derivation: the obligation must be "
            "computed from a morphism and finite restriction systems, not "
            "hand-attached as metadata."
        ),
        recommended_next=(
            "Rebuild one T34 or T37 fixture with explicit source sections and "
            "target obstruction certificates, then derive the T99 witness "
            "obligation mechanically from the restriction map."
        ),
    )


def _case_to_dict(case: PathCase) -> dict[str, object]:
    return {
        "name": case.name,
        "family": case.family,
        "source_id": case.source_id,
        "target_id": case.target_id,
        "ordinary_composite_map": [list(pair) for pair in case.ordinary_composite_map],
        "endpoint_behavior": {
            "target_obstructed": case.endpoint_behavior.target_obstructed,
            "target_global_sections": case.endpoint_behavior.target_global_sections,
            "obstruction_ids": list(case.endpoint_behavior.obstruction_ids),
            "observables": [list(pair) for pair in case.endpoint_behavior.observables],
        },
        "naive_loss_labels": sorted(case.naive_loss_labels),
        "typed_loss": [
            {
                "label": witness.label,
                "witness_id": witness.witness_id,
                "witness_type": witness.witness_type,
                "source_anchor": witness.source_anchor,
                "resolves_obstruction": witness.resolves_obstruction,
                "obstruction_id": witness.obstruction_id,
            }
            for witness in case.typed_loss
        ],
        "attribution_verdict": attribution_verdict(case),
        "purpose": case.purpose,
    }


def _group_to_dict(group: QuotientGroup) -> dict[str, object]:
    return {
        "group_id": group.group_id,
        "case_names": list(group.case_names),
        "verdicts": list(group.verdicts),
        "typed_signatures": [
            [list(signature_item) for signature_item in signature]
            for signature in group.typed_signatures
        ],
        "naive_key_shared": group.naive_key_shared,
        "naive_collision": group.naive_collision,
        "typed_witness_separates": group.typed_witness_separates,
    }


def t99_result_to_dict(result: T99Result) -> dict[str, object]:
    return {
        "cases": [_case_to_dict(case) for case in result.cases],
        "quotient_groups": [_group_to_dict(group) for group in result.quotient_groups],
        "naive_label_kernel_fails_quotient_gate": result.naive_label_kernel_fails_quotient_gate,
        "typed_witness_kernel_separates_collision": result.typed_witness_kernel_separates_collision,
        "same_typed_control_collapses": result.same_typed_control_collapses,
        "endpoint_difference_control_excluded": result.endpoint_difference_control_excluded,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "tf1_update": result.tf1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }
