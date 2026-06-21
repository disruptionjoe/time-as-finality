"""T148: paper-facing demotion gate for H7.

H7 has a supported finite constructor theorem (T18), but the obstruction stack
from T80 through T145 blocks its promotion as a physical or thermodynamic arrow.
This model makes that status explicit so paper-facing prose cannot cite the
conditional theorem as physical-arrow evidence.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.physical_record_deletion_fixed_accounting import run_t145_analysis


@dataclass(frozen=True)
class H7GateProfile:
    conditional_constructor_theorem: bool
    closed_reversible_obstruction: bool
    open_stochastic_absorbed: bool
    record_graph_reverse_grounded: bool
    fixed_accounting_deletion_candidate: bool
    fixed_accounting_capability_residue: bool


@dataclass(frozen=True)
class H7PaperFacingVerdict:
    profile: H7GateProfile
    paper_facing_status: str
    allowed_claims: tuple[str, ...]
    rejected_claims: tuple[str, ...]
    open_blockers: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    suggested_next: str


def current_h7_gate_profile() -> H7GateProfile:
    t145 = run_t145_analysis()
    return H7GateProfile(
        conditional_constructor_theorem=True,
        closed_reversible_obstruction=True,
        open_stochastic_absorbed=True,
        record_graph_reverse_grounded=False,
        fixed_accounting_deletion_candidate=bool(t145.h7_arrow_candidates),
        fixed_accounting_capability_residue=bool(
            t145.fixed_accounting_capability_splits
        ),
    )


def classify_h7_paper_status(profile: H7GateProfile) -> H7PaperFacingVerdict:
    if not profile.conditional_constructor_theorem:
        status = "unsupported"
    elif profile.fixed_accounting_deletion_candidate:
        status = "physical_arrow_candidate_requires_absorber_review"
    else:
        status = "demoted_to_constructor_resource_audit"

    allowed_claims = _allowed_claims(profile, status)
    rejected_claims = _rejected_claims(profile, status)
    blockers = _open_blockers(profile, status)

    return H7PaperFacingVerdict(
        profile=profile,
        paper_facing_status=status,
        allowed_claims=allowed_claims,
        rejected_claims=rejected_claims,
        open_blockers=blockers,
        strongest_claim=_strongest_claim(status),
        improved=(
            "T148 converts the H7 paper-facing status from scattered cautions "
            "into a gate. The finite constructor theorem remains usable, but "
            "physical-arrow language is blocked unless the T145 deletion gate "
            "or an equivalent absorber-matched substrate is cleared."
        ),
        weakened=(
            "This weakens H7's public role: current evidence supports a "
            "constructor/resource-accounting audit, not a derivation of the "
            "thermodynamic arrow or a physically grounded finality arrow."
        ),
        falsification_condition=(
            "T148 fails in H7's favor if a physically typed record substrate "
            "clears the fixed-accounting deletion gate: matched free-energy, "
            "capacity, sink, boundary, provenance, source-copy, and reversible-"
            "control data, plus a task-natural future-operation split and a "
            "constructor-impossible physical deletion reverse."
        ),
        h7_update=(
            "H7 is paper-facing only as a conditional constructor theorem and "
            "resource/reverse-edge audit discipline. It is demoted as a "
            "physical-arrow or thermodynamic-arrow claim until the fixed-"
            "accounting physical deletion gate is cleared."
        ),
        claim_ledger_update=(
            "Add T148 to H7: the current evidence stack supports conditional "
            "constructor/resource-accounting language only. T145's matched-"
            "accounting topology split is future-operation residue, not arrow "
            "evidence, so H7 paper-facing physical-arrow language is demoted."
        ),
        suggested_next=(
            "Stop adding generic H7 arrow prose. Either find a substrate-native "
            "physical deletion candidate that clears the T145/T148 gate, or use "
            "H7 only to audit resource, sink, boundary, provenance, and reverse-"
            "edge assumptions."
        ),
    )


def run_t148_analysis() -> H7PaperFacingVerdict:
    return classify_h7_paper_status(current_h7_gate_profile())


def _allowed_claims(profile: H7GateProfile, status: str) -> tuple[str, ...]:
    claims: list[str] = []
    if profile.conditional_constructor_theorem:
        claims.append("conditional D1-monotone constructor theorem")
    if profile.fixed_accounting_capability_residue:
        claims.append("future-operation/topology residue at fixed erasure accounting")
    claims.append("reverse-edge and resource-accounting audit discipline")
    if status == "physical_arrow_candidate_requires_absorber_review":
        claims.append("candidate physical-deletion route pending hostile absorber review")
    return tuple(claims)


def _rejected_claims(profile: H7GateProfile, status: str) -> tuple[str, ...]:
    if status == "physical_arrow_candidate_requires_absorber_review":
        return (
            "unreviewed promotion from candidate substrate to physical arrow",
            "thermodynamic-arrow derivation without standard absorber comparison",
        )

    rejected = [
        "derivation of the thermodynamic arrow from finality alone",
        "physical-arrow support from current record-graph or deletion fixtures",
        "promotion of fixed-erasure D1 topology split to arrow evidence",
    ]
    if profile.closed_reversible_obstruction:
        rejected.append("strict scalar finality monotone on closed finite reversible dynamics")
    if profile.open_stochastic_absorbed:
        rejected.append("independent open stochastic arrow without path, sink, or capacity accounting")
    if not profile.record_graph_reverse_grounded:
        rejected.append("constructor-impossible reverse in the current T1 record graph")
    return tuple(rejected)


def _open_blockers(profile: H7GateProfile, status: str) -> tuple[str, ...]:
    if status == "unsupported":
        return ("recover a valid finite constructor theorem before using H7",)
    if status == "physical_arrow_candidate_requires_absorber_review":
        return (
            "run hostile absorber review on the candidate physical deletion substrate",
            "compare the candidate against ordinary thermodynamic and stochastic accounts",
        )
    blockers = [
        "no physically typed record substrate clears the fixed-accounting deletion gate",
        "no current T1 reverse edge is constructor-impossible after resource accounting",
    ]
    if profile.fixed_accounting_capability_residue:
        blockers.append(
            "the surviving fixed-accounting split is future-operation residue, not reverse impossibility"
        )
    return tuple(blockers)


def _strongest_claim(status: str) -> str:
    if status == "unsupported":
        return "H7 should not be used even as a constructor theorem until T18 is replaced."
    if status == "physical_arrow_candidate_requires_absorber_review":
        return (
            "H7 has a candidate physical-deletion route, but it is not a "
            "paper-facing arrow claim until hostile thermodynamic, stochastic, "
            "and resource-accounting absorbers fail."
        )
    return (
        "H7 is supported only as a conditional constructor/resource-accounting "
        "claim. Current evidence blocks paper-facing physical-arrow language: "
        "closed reversible, open stochastic, T1 record-graph, and fixed-"
        "accounting physical-deletion screens all fail to produce a constructor-"
        "impossible physical reverse."
    )


def t148_result_to_dict(result: H7PaperFacingVerdict) -> dict[str, object]:
    return {
        "profile": {
            "conditional_constructor_theorem": (
                result.profile.conditional_constructor_theorem
            ),
            "closed_reversible_obstruction": (
                result.profile.closed_reversible_obstruction
            ),
            "open_stochastic_absorbed": result.profile.open_stochastic_absorbed,
            "record_graph_reverse_grounded": (
                result.profile.record_graph_reverse_grounded
            ),
            "fixed_accounting_deletion_candidate": (
                result.profile.fixed_accounting_deletion_candidate
            ),
            "fixed_accounting_capability_residue": (
                result.profile.fixed_accounting_capability_residue
            ),
        },
        "paper_facing_status": result.paper_facing_status,
        "allowed_claims": list(result.allowed_claims),
        "rejected_claims": list(result.rejected_claims),
        "open_blockers": list(result.open_blockers),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "suggested_next": result.suggested_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t148_result_to_dict(run_t148_analysis()), indent=2))
