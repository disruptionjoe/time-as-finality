"""T108: prior-art absorption audit for source-fiber loss relocation.

T107 gave LossKernel a sharper finite semantics: inspect source lifts of a
target judgment. T108 asks whether that separates from nearby established
machinery. The answer is deliberately conservative: not yet. Several neighbors
can express the same finite behavior once they are allowed the same source
fiber and judgment relation.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NeighborAudit:
    neighbor: str
    primary_object: str
    absorbs_reconstruction_debt: bool
    absorbs_stable_constraint: bool
    absorbs_absorbed_freedom: bool
    absorption_mechanism: str
    remaining_delta: str
    verdict: str


@dataclass(frozen=True)
class T108Result:
    audits: tuple[NeighborAudit, ...]
    strict_separation_from_all_neighbors: bool
    label_only_loss_refuted_again: bool
    surviving_delta: str
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    tf1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def neighbor_audits() -> tuple[NeighborAudit, ...]:
    return (
        NeighborAudit(
            neighbor="why_not_provenance",
            primary_object="missing derivation inputs and failed query explanations",
            absorbs_reconstruction_debt=True,
            absorbs_stable_constraint=True,
            absorbs_absorbed_freedom=False,
            absorption_mechanism=(
                "Mixed source-lift verdicts can be reported as missing "
                "witnesses or missing derivation choices for the target answer."
            ),
            remaining_delta=(
                "T107 classifies the same witness gap as relocation of a lost "
                "axis, but that is presentation unless the axis typing changes "
                "the explanation calculus."
            ),
            verdict="absorbed_except_taxonomy",
        ),
        NeighborAudit(
            neighbor="abstract_interpretation",
            primary_object="concretization fiber under an abstraction map",
            absorbs_reconstruction_debt=True,
            absorbs_stable_constraint=True,
            absorbs_absorbed_freedom=True,
            absorption_mechanism=(
                "The source fiber is exactly a concretization set. Mixed "
                "verdicts are loss of precision; uniform verdicts are sound "
                "abstract judgments."
            ),
            remaining_delta=(
                "T107's relocation words add no formal power unless LossKernel "
                "supplies a typed attribution or composition law not captured "
                "by the abstraction/concretization pair."
            ),
            verdict="absorbed",
        ),
        NeighborAudit(
            neighbor="lenses",
            primary_object="view, source complement, and bidirectional update law",
            absorbs_reconstruction_debt=True,
            absorbs_stable_constraint=True,
            absorbs_absorbed_freedom=True,
            absorption_mechanism=(
                "The projected target is a view; the forgotten source fiber is "
                "the complement needed for well-behaved putback or update."
            ),
            remaining_delta=(
                "T107 is not yet a lens theorem. A separation would need a "
                "judgment-sensitive obstruction or debt not representable as "
                "ordinary complement/update information."
            ),
            verdict="absorbed",
        ),
        NeighborAudit(
            neighbor="csp_explanation",
            primary_object="constraints, conflicts, diagnoses, and solution fibers",
            absorbs_reconstruction_debt=True,
            absorbs_stable_constraint=True,
            absorbs_absorbed_freedom=True,
            absorption_mechanism=(
                "A target judgment over source lifts can be encoded as a CSP. "
                "Mixed verdicts become ambiguity over solutions; uniformly "
                "forbidden lifts become conflicts."
            ),
            remaining_delta=(
                "This confirms the existing T39 warning: obstruction mechanics "
                "are not novel. Only typed attribution over the projection may "
                "remain."
            ),
            verdict="absorbed",
        ),
        NeighborAudit(
            neighbor="effect_annotations",
            primary_object="monoidal or graded annotations on computations",
            absorbs_reconstruction_debt=True,
            absorbs_stable_constraint=False,
            absorbs_absorbed_freedom=True,
            absorption_mechanism=(
                "A sufficiently rich effect can carry the same source witness "
                "obligations that T99 required. Label-only effects fail, but "
                "witness-carrying effects absorb T107's finite data."
            ),
            remaining_delta=(
                "The only remaining gap is whether LossKernel has a canonical "
                "source-derived witness law rather than arbitrary annotations."
            ),
            verdict="absorbed_by_rich_effects_not_label_only",
        ),
    )


def run_t108_analysis() -> T108Result:
    audits = neighbor_audits()
    strict_separation = any(
        not (
            audit.absorbs_reconstruction_debt
            and audit.absorbs_stable_constraint
            and audit.absorbs_absorbed_freedom
        )
        and audit.verdict not in {
            "absorbed_except_taxonomy",
            "absorbed_by_rich_effects_not_label_only",
        }
        for audit in audits
    )

    return T108Result(
        audits=audits,
        strict_separation_from_all_neighbors=strict_separation,
        label_only_loss_refuted_again=True,
        surviving_delta=(
            "A possible synthesis object remains: a canonical, typed, "
            "source-fiber witness law for projection-created reconstruction "
            "debt. That is not yet a separation from why-not provenance, "
            "abstract interpretation, lenses, CSP explanation, or rich effect "
            "systems."
        ),
        strongest_claim=(
            "T107 does not currently separate from the named prior-art families. "
            "Given the same source fiber and target judgment, abstract "
            "interpretation, lenses, CSP explanation, why-not provenance, and "
            "rich effect annotations can absorb the finite behavior. The "
            "remaining TF1 window is a typed normal form and canonical "
            "source-derived witness law, not a new obstruction mechanism."
        ),
        improved=(
            "T108 prevents premature promotion of LossKernel. It identifies "
            "exactly where T107 is useful: as a unifying source-fiber audit and "
            "claim-discipline vocabulary, not yet as proof of mathematical "
            "novelty."
        ),
        weakened=(
            "This weakens TF1's novelty claim. Source-fiber loss relocation is "
            "very close to standard concretization, complement, provenance, "
            "conflict, and effect machinery."
        ),
        falsification_condition=(
            "T108 fails in TF1's favor only if a future fixture has the same "
            "ordinary provenance, abstraction/concretization, lens complement, "
            "CSP conflict/diagnosis data, and rich effect annotation, but still "
            "requires a different LossKernel attribution verdict."
        ),
        tf1_update=(
            "TF1 remains open and should not claim prior-art separation. The "
            "next admissible target is a quotient witness against rich effects "
            "and abstract interpretation, not against label-only provenance."
        ),
        claim_ledger_update=(
            "Add T108 to TF1: source-fiber loss relocation does not yet separate "
            "from why-not provenance, abstract interpretation, lenses, CSP "
            "explanation, or rich effect annotations. The surviving delta is a "
            "possible typed normal form for source-derived witness obligations."
        ),
        open_blocker=(
            "Construct a same-neighbor-data quotient fixture: same provenance, "
            "same abstraction fibers, same lens complement, same CSP conflicts, "
            "and same rich effects, but different LossKernel attribution. "
            "Without that, separation is unearned."
        ),
        recommended_next=(
            "Try to build the same-neighbor-data quotient fixture. If it fails, "
            "demote LossKernel to an integration vocabulary over existing "
            "formal tools."
        ),
    )


def _audit_to_dict(audit: NeighborAudit) -> dict[str, object]:
    return {
        "neighbor": audit.neighbor,
        "primary_object": audit.primary_object,
        "absorbs_reconstruction_debt": audit.absorbs_reconstruction_debt,
        "absorbs_stable_constraint": audit.absorbs_stable_constraint,
        "absorbs_absorbed_freedom": audit.absorbs_absorbed_freedom,
        "absorption_mechanism": audit.absorption_mechanism,
        "remaining_delta": audit.remaining_delta,
        "verdict": audit.verdict,
    }


def t108_result_to_dict(result: T108Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "strict_separation_from_all_neighbors": result.strict_separation_from_all_neighbors,
        "label_only_loss_refuted_again": result.label_only_loss_refuted_again,
        "surviving_delta": result.surviving_delta,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "tf1_update": result.tf1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t108_result_to_dict(run_t108_analysis()), indent=2))
