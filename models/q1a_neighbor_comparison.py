"""T102: Q1A neighbor comparison gate.

Q1A is the narrow surviving quantum branch after T101: access-boundary record
accounting over already formed records. This module asks a harsher question:
what would it take for Q1A to distinguish itself from nearby measurement or
interpretation frameworks rather than merely restating them?
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NeighborAudit:
    neighbor_id: str
    shared_content: str
    taf_candidate_delta: str
    current_verdict: str
    earns_paper_facing_distinction_now: bool
    collapse_condition: str


@dataclass(frozen=True)
class T102Result:
    neighbors: tuple[NeighborAudit, ...]
    q1a_survives_only_as_access_boundary_accounting: bool
    fixed_data_distinction_gate: str
    no_neighbor_comparison_yet_earns_paper_facing_distinction: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def neighbor_audits() -> tuple[NeighborAudit, ...]:
    return (
        NeighborAudit(
            neighbor_id="decoherence",
            shared_content=(
                "Environment-induced suppression of interference and stable "
                "pointer-basis record formation."
            ),
            taf_candidate_delta=(
                "Q1A adds an observer-indexed finality verdict: a record can "
                "be decohered yet not finalized for a given observer because "
                "the observer lacks the required accessible cut."
            ),
            current_verdict="narrow_partial_delta",
            earns_paper_facing_distinction_now=False,
            collapse_condition=(
                "Collapse Q1A into decoherence language if every D1 verdict is "
                "recoverable from reduced-state decoherence plus ordinary "
                "observer reachability."
            ),
        ),
        NeighborAudit(
            neighbor_id="quantum_darwinism",
            shared_content=(
                "Redundant environmental encodings and observer access via "
                "fragment sampling."
            ),
            taf_candidate_delta=(
                "Q1A keeps accessible redundancy and independence-corrected "
                "holder redundancy separate, so correlated duplicate fragments "
                "need not count as independent finality support."
            ),
            current_verdict="narrow_partial_delta",
            earns_paper_facing_distinction_now=False,
            collapse_condition=(
                "Collapse Q1A into Quantum Darwinism if admissible fragment "
                "partitioning always makes D1 holder redundancy numerically "
                "identical to accessible redundancy."
            ),
        ),
        NeighborAudit(
            neighbor_id="consistent_histories",
            shared_content=(
                "Classical-looking record families and history-level "
                "consistency constraints."
            ),
            taf_candidate_delta=(
                "Q1A would need an observer-indexed finality preorder that is "
                "not just a rephrasing of choosing a consistent coarse-grained "
                "history family with records."
            ),
            current_verdict="not_yet_earned",
            earns_paper_facing_distinction_now=False,
            collapse_condition=(
                "Collapse Q1A into consistent-histories language if every "
                "access-boundary verdict can be represented as an ordinary "
                "record-bearing consistent set choice."
            ),
        ),
        NeighborAudit(
            neighbor_id="relational_quantum_mechanics",
            shared_content=(
                "Observer-relative facts and the refusal of one observer-"
                "independent outcome inventory."
            ),
            taf_candidate_delta=(
                "Q1A would need explicit threshold and independence rules that "
                "constrain when observer-relative facts count as finalized, "
                "rather than merely stating relativity of facts."
            ),
            current_verdict="not_yet_earned",
            earns_paper_facing_distinction_now=False,
            collapse_condition=(
                "Collapse Q1A into RQM if its observer-relative finality talk "
                "adds no rule beyond ordinary relational facts."
            ),
        ),
        NeighborAudit(
            neighbor_id="qbism",
            shared_content=(
                "Agent-indexed statements about what counts as available to an "
                "observer."
            ),
            taf_candidate_delta=(
                "Q1A treats finality as a constraint on physical record "
                "availability and independence, not merely a personal "
                "probability update."
            ),
            current_verdict="category_separation_only",
            earns_paper_facing_distinction_now=False,
            collapse_condition=(
                "Collapse Q1A into QBist language if every claimed finality "
                "change can be rewritten as an agent credence update with no "
                "additional record-side predicate."
            ),
        ),
        NeighborAudit(
            neighbor_id="many_worlds",
            shared_content=(
                "No-collapse branching and branch-relative records for local "
                "observers."
            ),
            taf_candidate_delta=(
                "Q1A would need access-boundary or independence-sensitive "
                "verdicts not already implied by branch-relative record "
                "availability in Everettian language."
            ),
            current_verdict="not_yet_earned",
            earns_paper_facing_distinction_now=False,
            collapse_condition=(
                "Collapse Q1A into many-worlds language if every surviving "
                "witness is just branch-relative access bookkeeping."
            ),
        ),
    )


def fixed_data_distinction_gate() -> str:
    return (
        "Q1A earns paper-facing distinction only after one witness holds fixed "
        "the standard quantum-side data used by nearby frameworks "
        "(decoherence/pointer-basis evidence, fragment-information summaries, "
        "and ordinary branch/history availability) while changing the D1 "
        "verdict solely through observer-specific access-boundary or "
        "independence structure."
    )


def run_t102_analysis() -> T102Result:
    neighbors = neighbor_audits()

    return T102Result(
        neighbors=neighbors,
        q1a_survives_only_as_access_boundary_accounting=True,
        fixed_data_distinction_gate=fixed_data_distinction_gate(),
        no_neighbor_comparison_yet_earns_paper_facing_distinction=all(
            not audit.earns_paper_facing_distinction_now for audit in neighbors
        ),
        strongest_claim=(
            "Q1A currently survives only as observer-indexed access-boundary "
            "and independence accounting over already formed records. It does "
            "not yet earn a paper-facing distinction from decoherence, Quantum "
            "Darwinism, consistent histories, RQM, QBism, or many-worlds. The "
            "best remaining candidate delta is a fixed-data witness where the "
            "standard quantum-side summaries stay the same but the D1 verdict "
            "changes because accessible support or independence structure "
            "changes."
        ),
        improved=(
            "T102 converts the vague 'compare to the literature' obligation "
            "into a concrete admission gate. The repo now has an explicit rule "
            "for when Q1A is merely a redescription and when it would count as "
            "a genuine distinction."
        ),
        weakened=(
            "This weakens Q1A again. The current access-boundary branch should "
            "not be presented as a distinct measurement framework or "
            "interpretation. At present it is a bookkeeping layer whose "
            "surviving deltas are only partial and neighbor-relative."
        ),
        falsification_condition=(
            "T102 fails in Q1A's favor if one witness keeps the ordinary "
            "quantum-side summaries fixed and still forces a different D1 "
            "verdict that nearby frameworks cannot absorb without adding Q1A's "
            "access-boundary or independence predicate. T102 succeeds against "
            "Q1A if every proposed witness can be rewritten entirely inside "
            "decoherence, accessible redundancy, consistent-set choice, "
            "relational facts, personalist credence, or branch-relative access."
        ),
        claim_ledger_update=(
            "Add T102 to Q1: the surviving Q1A branch should be stated only as "
            "access-boundary and independence accounting until it clears a "
            "fixed-data neighbor-comparison gate against decoherence, Quantum "
            "Darwinism, consistent histories, RQM, QBism, and many-worlds."
        ),
        open_blocker=(
            "The repo still lacks one decisive fixed-data witness. Current T2/"
            "T22/T62/T64 examples show partial separation, but they do not yet "
            "hold enough standard-neighbor summaries fixed to force a clean "
            "external distinction."
        ),
        recommended_next=(
            "Build one finite witness family where decoherence, accessible raw "
            "redundancy, and branch/history availability stay fixed while only "
            "the independence partition or access cut changes the D1 verdict."
        ),
    )


def t102_result_to_dict(result: T102Result) -> dict[str, object]:
    return {
        "neighbors": [audit.__dict__ for audit in result.neighbors],
        "q1a_survives_only_as_access_boundary_accounting": (
            result.q1a_survives_only_as_access_boundary_accounting
        ),
        "fixed_data_distinction_gate": result.fixed_data_distinction_gate,
        "no_neighbor_comparison_yet_earns_paper_facing_distinction": (
            result.no_neighbor_comparison_yet_earns_paper_facing_distinction
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t102_result_to_dict(run_t102_analysis()), indent=2))
