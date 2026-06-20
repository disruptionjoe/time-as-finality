"""T92: accessible-witness gap restriction theorem audit.

This module turns the T19/T58 open target into a finite theorem check over
typed proposition-domain witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Proposition:
    name: str
    witness_events: frozenset[str]
    threshold: int = 1
    ambient_true: bool = True


@dataclass(frozen=True)
class Patch:
    name: str
    events: frozenset[str]


@dataclass(frozen=True)
class PropositionSystem:
    name: str
    propositions: tuple[Proposition, ...]
    patches: tuple[Patch, ...]
    restriction_overrides: dict[tuple[str, str, str], str | None] | None = None
    auditable_overrides: dict[str, frozenset[str]] | None = None

    def prop_names(self) -> frozenset[str]:
        return frozenset(prop.name for prop in self.propositions)

    def prop_by_name(self) -> dict[str, Proposition]:
        return {prop.name: prop for prop in self.propositions}


@dataclass(frozen=True)
class GapRestrictionViolation:
    larger_patch: str
    smaller_patch: str
    source_prop: str
    restricted_prop: str
    explanation: str


@dataclass(frozen=True)
class NonLiftingExample:
    larger_patch: str
    smaller_patch: str
    prop: str
    explanation: str


@dataclass(frozen=True)
class SystemAudit:
    system_name: str
    nested_pairs: int
    ambient_restriction_holds: bool
    audit_monotonicity_holds: bool
    stable_typing_holds: bool
    gap_restriction_holds: bool
    violations: tuple[GapRestrictionViolation, ...]
    non_lifting_examples: tuple[NonLiftingExample, ...]
    patch_table: tuple[dict[str, Any], ...]
    classification: str
    interpretation: str


@dataclass(frozen=True)
class T92Result:
    audits: tuple[SystemAudit, ...]
    theorem_status: str
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    claim_update: str
    open_blocker: str
    suggested_next: str


def ambient(system: PropositionSystem, patch: Patch) -> frozenset[str]:
    return frozenset(prop.name for prop in system.propositions if prop.ambient_true)


def auditable(system: PropositionSystem, patch: Patch) -> frozenset[str]:
    if system.auditable_overrides and patch.name in system.auditable_overrides:
        return system.auditable_overrides[patch.name]

    return frozenset(
        prop.name
        for prop in system.propositions
        if len(prop.witness_events & patch.events) >= prop.threshold
    )


def gap(system: PropositionSystem, patch: Patch) -> frozenset[str]:
    return ambient(system, patch) - auditable(system, patch)


def nested_patch_pairs(system: PropositionSystem) -> tuple[tuple[Patch, Patch], ...]:
    pairs: list[tuple[Patch, Patch]] = []
    for larger in system.patches:
        for smaller in system.patches:
            if larger.name == smaller.name:
                continue
            if smaller.events < larger.events:
                pairs.append((larger, smaller))
    return tuple(pairs)


def restrict_prop(
    system: PropositionSystem,
    larger: Patch,
    smaller: Patch,
    prop_name: str,
) -> str | None:
    if system.restriction_overrides:
        key = (larger.name, smaller.name, prop_name)
        if key in system.restriction_overrides:
            return system.restriction_overrides[key]
    return prop_name if prop_name in system.prop_names() else None


def restrict_set(
    system: PropositionSystem,
    larger: Patch,
    smaller: Patch,
    props: frozenset[str],
) -> frozenset[str]:
    restricted = {
        maybe
        for prop in props
        for maybe in (restrict_prop(system, larger, smaller, prop),)
        if maybe is not None
    }
    return frozenset(restricted)


def check_ambient_restriction(system: PropositionSystem) -> bool:
    for larger, smaller in nested_patch_pairs(system):
        if not restrict_set(system, larger, smaller, ambient(system, larger)) <= ambient(system, smaller):
            return False
    return True


def check_audit_monotonicity(system: PropositionSystem) -> bool:
    for larger, smaller in nested_patch_pairs(system):
        if not auditable(system, smaller) <= auditable(system, larger):
            return False
    return True


def check_stable_typing(system: PropositionSystem) -> bool:
    for larger, smaller in nested_patch_pairs(system):
        for prop in system.prop_names():
            restricted = restrict_prop(system, larger, smaller, prop)
            if restricted is not None and restricted != prop:
                return False
    return True


def audit_system(system: PropositionSystem) -> SystemAudit:
    violations: list[GapRestrictionViolation] = []
    non_lifting: list[NonLiftingExample] = []
    pairs = nested_patch_pairs(system)

    for larger, smaller in pairs:
        larger_gap = gap(system, larger)
        smaller_gap = gap(system, smaller)
        restricted_gap = restrict_set(system, larger, smaller, larger_gap)

        for prop in sorted(restricted_gap - smaller_gap):
            source_props = [
                source
                for source in larger_gap
                if restrict_prop(system, larger, smaller, source) == prop
            ]
            source = sorted(source_props)[0] if source_props else prop
            violations.append(
                GapRestrictionViolation(
                    larger_patch=larger.name,
                    smaller_patch=smaller.name,
                    source_prop=source,
                    restricted_prop=prop,
                    explanation=(
                        "A larger-patch gap restricts to a proposition that is "
                        "not a smaller-patch gap."
                    ),
                )
            )

        for prop in sorted(smaller_gap - restricted_gap):
            non_lifting.append(
                NonLiftingExample(
                    larger_patch=larger.name,
                    smaller_patch=smaller.name,
                    prop=prop,
                    explanation=(
                        "The smaller patch has a gap that does not lift from "
                        "the larger patch; closure is not surjectivity."
                    ),
                )
            )

    ambient_ok = check_ambient_restriction(system)
    audit_ok = check_audit_monotonicity(system)
    typing_ok = check_stable_typing(system)
    gap_ok = len(violations) == 0

    if gap_ok and ambient_ok and audit_ok and typing_ok:
        classification = "conditional_theorem_witness"
        interpretation = (
            "Gap restriction holds under ambient restriction, audit "
            "monotonicity, and stable proposition typing."
        )
    elif not gap_ok and not typing_ok:
        classification = "semantic_relabeling_boundary"
        interpretation = (
            "Gap restriction fails because proposition restriction relabels "
            "a self-finality proposition into an already-auditable observer "
            "proposition."
        )
    elif not gap_ok and not audit_ok:
        classification = "audit_monotonicity_boundary"
        interpretation = (
            "Gap restriction fails because a smaller patch can audit a "
            "proposition that the larger patch cannot audit."
        )
    elif not gap_ok:
        classification = "restriction_failure"
        interpretation = "Gap restriction fails; inspect the violated condition."
    else:
        classification = "condition_failure_without_gap_failure"
        interpretation = (
            "One theorem condition fails, but this witness did not expose a "
            "gap-restriction violation."
        )

    patch_table = tuple(
        {
            "patch": patch.name,
            "events": sorted(patch.events),
            "A": sorted(ambient(system, patch)),
            "F": sorted(auditable(system, patch)),
            "G": sorted(gap(system, patch)),
        }
        for patch in system.patches
    )

    return SystemAudit(
        system_name=system.name,
        nested_pairs=len(pairs),
        ambient_restriction_holds=ambient_ok,
        audit_monotonicity_holds=audit_ok,
        stable_typing_holds=typing_ok,
        gap_restriction_holds=gap_ok,
        violations=tuple(violations),
        non_lifting_examples=tuple(non_lifting),
        patch_table=patch_table,
        classification=classification,
        interpretation=interpretation,
    )


def t19_proposition_gap_system() -> PropositionSystem:
    propositions = (
        Proposition(
            name="R_obs",
            witness_events=frozenset({"e_R_recv", "e_R_rec1", "e_R_final"}),
            threshold=1,
        ),
        Proposition(
            name="R_self_finality",
            witness_events=frozenset({"e_E1", "e_E2"}),
            threshold=2,
        ),
    )
    patches = (
        Patch(
            name="U_int",
            events=frozenset({"e_src", "e_R_recv", "e_R_rec1", "e_R_final"}),
        ),
        Patch(
            name="U_one_external_witness",
            events=frozenset(
                {"e_src", "e_R_recv", "e_R_rec1", "e_R_final", "e_E1"}
            ),
        ),
        Patch(
            name="U_ext",
            events=frozenset(
                {
                    "e_src",
                    "e_R_recv",
                    "e_R_rec1",
                    "e_R_final",
                    "e_E1",
                    "e_E2",
                    "e_meta",
                }
            ),
        ),
    )
    return PropositionSystem(
        name="t19_unary_accessible_witness_gap",
        propositions=propositions,
        patches=patches,
    )


def non_chain_proposition_gap_system() -> PropositionSystem:
    propositions = (
        Proposition("O_obs", frozenset({"o_state"}), 1),
        Proposition("O_left_witness", frozenset({"left_witness"}), 1),
        Proposition(
            "O_joint_self_finality",
            frozenset({"left_witness", "right_witness"}),
            2,
        ),
    )
    patches = (
        Patch("U_local", frozenset({"o_base", "o_state"})),
        Patch("U_left", frozenset({"o_base", "o_state", "left_witness"})),
        Patch("U_right", frozenset({"o_base", "o_state", "right_witness"})),
        Patch(
            "U_joint",
            frozenset({"o_base", "o_state", "left_witness", "right_witness"}),
        ),
        Patch(
            "U_full",
            frozenset(
                {
                    "o_base",
                    "o_state",
                    "left_witness",
                    "right_witness",
                    "auditor",
                }
            ),
        ),
    )
    return PropositionSystem(
        name="non_chain_joint_witness_gap",
        propositions=propositions,
        patches=patches,
    )


def semantic_relabeling_control_system() -> PropositionSystem:
    propositions = (
        Proposition("R_obs", frozenset({"e_R_final"}), 1),
        Proposition("R_self_finality", frozenset({"e_external_witness"}), 1),
    )
    patches = (
        Patch("U_small", frozenset({"e_R_final"})),
        Patch("U_large", frozenset({"e_R_final", "e_context"})),
    )
    return PropositionSystem(
        name="semantic_relabeling_control",
        propositions=propositions,
        patches=patches,
        restriction_overrides={
            ("U_large", "U_small", "R_self_finality"): "R_obs",
        },
    )


def audit_monotonicity_control_system() -> PropositionSystem:
    propositions = (
        Proposition("R_obs", frozenset({"e_R_final"}), 1),
        Proposition("R_self_finality", frozenset({"e_external_witness"}), 1),
    )
    patches = (
        Patch("U_small", frozenset({"e_R_final"})),
        Patch("U_large", frozenset({"e_R_final", "e_context"})),
    )
    return PropositionSystem(
        name="audit_monotonicity_control",
        propositions=propositions,
        patches=patches,
        auditable_overrides={
            "U_small": frozenset({"R_obs", "R_self_finality"}),
            "U_large": frozenset({"R_obs"}),
        },
    )


def run_t92_analysis() -> T92Result:
    systems = (
        t19_proposition_gap_system(),
        non_chain_proposition_gap_system(),
        semantic_relabeling_control_system(),
        audit_monotonicity_control_system(),
    )
    audits = tuple(audit_system(system) for system in systems)
    positive = audits[:2]
    controls = audits[2:]

    positives_pass = all(
        audit.classification == "conditional_theorem_witness" for audit in positive
    )
    controls_fail = all(not audit.gap_restriction_holds for audit in controls)

    theorem_status = (
        "supported_with_explicit_boundaries"
        if positives_pass and controls_fail
        else "unresolved_or_failed"
    )

    strongest_claim = (
        "For finite typed proposition-domain accessible-witness systems, "
        "G(U)=A(U)-F(U) restricts contravariantly when ambient truth restricts, "
        "local auditability is monotone under patch inclusion, and proposition "
        "types are not relabeled under restriction. The T19 unary gap and a "
        "non-chain joint-witness gap both satisfy these conditions."
    )
    weakened_claim = (
        "T92 does not prove a general cohomology theorem or a consciousness "
        "claim. It shows that the T19 accessible-witness gap can join the "
        "T56-T58 H0 gap program only under explicit proposition-typing and "
        "audit-monotonicity hypotheses."
    )
    falsification_condition = (
        "T92 fails if a well-typed nested proposition-domain witness satisfies "
        "ambient restriction and audit monotonicity but has a larger-patch gap "
        "whose restriction is not a smaller-patch gap."
    )
    claim_update = (
        "C1 may be sharpened, not upgraded: the first-person/third-person "
        "finality gap has a finite degree-0 accessible-witness form with "
        "restriction closure for typed proposition-domain witness systems."
    )
    open_blocker = (
        "The result is still finite and conditional. It does not place "
        "FIRST-PERSON-FINALITY in a complexity class and does not identify "
        "T19 proposition gaps with T58 order-pair gaps."
    )
    suggested_next = (
        "Generalize the proof sketch into a short formal lemma, then test "
        "whether T19 proposition gaps and T58 order-pair gaps share a common "
        "typed gap category or only the same H0 failure shape."
    )

    return T92Result(
        audits=audits,
        theorem_status=theorem_status,
        strongest_claim=strongest_claim,
        weakened_claim=weakened_claim,
        falsification_condition=falsification_condition,
        claim_update=claim_update,
        open_blocker=open_blocker,
        suggested_next=suggested_next,
    )


def t92_result_to_dict(result: T92Result) -> dict[str, Any]:
    return {
        "theorem_status": result.theorem_status,
        "audits": [
            {
                "system_name": audit.system_name,
                "nested_pairs": audit.nested_pairs,
                "ambient_restriction_holds": audit.ambient_restriction_holds,
                "audit_monotonicity_holds": audit.audit_monotonicity_holds,
                "stable_typing_holds": audit.stable_typing_holds,
                "gap_restriction_holds": audit.gap_restriction_holds,
                "violations": [
                    {
                        "larger_patch": violation.larger_patch,
                        "smaller_patch": violation.smaller_patch,
                        "source_prop": violation.source_prop,
                        "restricted_prop": violation.restricted_prop,
                        "explanation": violation.explanation,
                    }
                    for violation in audit.violations
                ],
                "non_lifting_examples": [
                    {
                        "larger_patch": example.larger_patch,
                        "smaller_patch": example.smaller_patch,
                        "prop": example.prop,
                        "explanation": example.explanation,
                    }
                    for example in audit.non_lifting_examples
                ],
                "patch_table": list(audit.patch_table),
                "classification": audit.classification,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "claim_update": result.claim_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }
