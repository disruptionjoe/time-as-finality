"""T101: adjudicate Q1 into explicit subclaims and gates.

Q1 has accumulated useful but heterogeneous evidence: access-boundary record
accounting, detector-provenance admissibility, weak-measurement null criteria,
and contextuality/no-signalling guardrails. This module asks whether the current
Q1 umbrella still deserves to be treated as one partially supported claim.

The result is intentionally weakening: no current branch earns new measurement
dynamics or empirical support. The strongest surviving content is a split
program of observer-indexed record accounting plus a blocked detector protocol
gate. Weak measurement is reinstatement-only, and contextuality is background
discipline rather than a new prediction.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvidenceItem:
    test_id: str
    branch_id: str
    role: str
    status: str
    note: str


@dataclass(frozen=True)
class BranchAdjudication:
    branch_id: str
    proposed_claim_id: str
    current_status: str
    evidence_ids: tuple[str, ...]
    earned_content: str
    not_earned: str
    kill_condition: str
    reinstatement_condition: str
    next_gate: str


@dataclass(frozen=True)
class T101Result:
    evidence: tuple[EvidenceItem, ...]
    branches: tuple[BranchAdjudication, ...]
    q1_should_split_before_paper_language: bool
    no_branch_earns_new_measurement_dynamics: bool
    detector_branch_externally_blocked: bool
    weak_measurement_reinstatement_only: bool
    contextuality_branch_is_guardrail_only: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def evidence_items() -> tuple[EvidenceItem, ...]:
    """Return the Q1 evidence set used by the adjudication."""

    return (
        EvidenceItem(
            test_id="T2",
            branch_id="access_boundary_accounting",
            role="support",
            status="partial_support",
            note=(
                "Decohered-but-inaccessible witness separates pointer "
                "decoherence from observer-relative D1 finality, without "
                "adding collapse dynamics."
            ),
        ),
        EvidenceItem(
            test_id="T21",
            branch_id="contextuality_guardrail",
            role="guardrail",
            status="known_physics_alignment",
            note=(
                "CHSH/contextuality witness disciplines Q1 against global "
                "noncontextual records; it is Bell-adjacent structure, not a "
                "new quantum prediction."
            ),
        ),
        EvidenceItem(
            test_id="T22",
            branch_id="access_boundary_accounting",
            role="support",
            status="partial_support",
            note=(
                "Environmental redundancy and independence-corrected holder "
                "counts connect D1 to Quantum-Darwinism-style observables."
            ),
        ),
        EvidenceItem(
            test_id="T62",
            branch_id="access_boundary_accounting",
            role="weakener",
            status="narrowed_to_access_boundary",
            note=(
                "Separates decoherence, redundancy, and access; demotes Q1 "
                "away from new noisy measurement dynamics."
            ),
        ),
        EvidenceItem(
            test_id="T66-T83",
            branch_id="detector_provenance_protocol",
            role="weakener",
            status="null_criterion",
            note=(
                "Detector-side Q1 is null unless pre-registered raw logs beat "
                "passive statistics, dashboards, and post hoc partitions."
            ),
        ),
        EvidenceItem(
            test_id="T85-T87",
            branch_id="detector_provenance_protocol",
            role="support",
            status="admissibility_protocol",
            note=(
                "Ambiguous-tag controls and raw-log contract leave a narrow "
                "pre-registered provenance route, but no empirical upgrade."
            ),
        ),
        EvidenceItem(
            test_id="T95-T100",
            branch_id="detector_provenance_protocol",
            role="blocker",
            status="external_deployment_blocker",
            note=(
                "The detector route requires an augmented packet, dry-run "
                "governance, and at least four independent authority domains."
            ),
        ),
        EvidenceItem(
            test_id="T90-T94",
            branch_id="weak_measurement_discriminator",
            role="blocker",
            status="reinstatement_only",
            note=(
                "Weak measurement is blocked unless a real platform names an "
                "independent pre-registered branch, provenance, or undo-cost "
                "axis that changes the TaF verdict."
            ),
        ),
        EvidenceItem(
            test_id="T65",
            branch_id="contextuality_guardrail",
            role="guardrail",
            status="known_theorem_alignment",
            note=(
                "Bell holonomy reduction supports causal-boundary discipline "
                "but should not be sold as a TaF-specific measurement result."
            ),
        ),
    )


def branch_adjudications(evidence: tuple[EvidenceItem, ...]) -> tuple[BranchAdjudication, ...]:
    ids_by_branch: dict[str, tuple[str, ...]] = {}
    for item in evidence:
        ids_by_branch[item.branch_id] = ids_by_branch.get(item.branch_id, ()) + (item.test_id,)

    return (
        BranchAdjudication(
            branch_id="q1_umbrella",
            proposed_claim_id="Q1 umbrella only",
            current_status="too_broad_for_single_partially_supported_claim",
            evidence_ids=tuple(item.test_id for item in evidence),
            earned_content=(
                "Q1 is useful as an index into several record-finality research "
                "threads, but those threads now have different evidence types "
                "and different kill conditions."
            ),
            not_earned=(
                "A single physics-facing claim that quantum states are "
                "under-finalized in one operational sense across decoherence, "
                "detectors, weak measurement, and Bell/contextuality."
            ),
            kill_condition=(
                "Kill single-claim Q1 presentation if the branches continue to "
                "require different observables, evidence gates, and null "
                "criteria."
            ),
            reinstatement_condition=(
                "Reinstate a unified Q1 only if one operational observable "
                "connects access-boundary, detector, and weak-measurement "
                "routes without post hoc branch-specific rules."
            ),
            next_gate=(
                "Split Q1 into subclaims before any paper, public abstract, or "
                "theorem-facing language uses it as one supported conjecture."
            ),
        ),
        BranchAdjudication(
            branch_id="access_boundary_accounting",
            proposed_claim_id="Q1A access-boundary record accounting",
            current_status="survives_as_record_accounting",
            evidence_ids=ids_by_branch["access_boundary_accounting"],
            earned_content=(
                "Observer access and independence partitions can differ from "
                "pointer decoherence and environmental redundancy in finite "
                "record models."
            ),
            not_earned=(
                "New measurement dynamics, Born-rule content, collapse, or a "
                "calibration-free discriminator beyond decoherence and Quantum "
                "Darwinism."
            ),
            kill_condition=(
                "Demote if every physical implementation reduces D1 finality "
                "to standard redundancy plus ordinary causal reachability."
            ),
            reinstatement_condition=(
                "Upgrade only if a physics-grounded model produces an "
                "access/independence verdict not recoverable from standard "
                "decoherence, redundancy, and causal-access data."
            ),
            next_gate=(
                "Write this as the narrow surviving Q1A claim and compare it "
                "directly to decoherence and Quantum Darwinism."
            ),
        ),
        BranchAdjudication(
            branch_id="detector_provenance_protocol",
            proposed_claim_id="Q1B detector provenance admissibility",
            current_status="externally_blocked_protocol_admissibility",
            evidence_ids=ids_by_branch["detector_provenance_protocol"],
            earned_content=(
                "A detector record can be admitted for D1 scoring only after "
                "pre-registered raw-log provenance, hostile controls, and "
                "authority separation fix the independence partition."
            ),
            not_earned=(
                "Empirical detector support, native detector-physics novelty, "
                "or a route carried by timing hardware alone."
            ),
            kill_condition=(
                "Demote the detector route below the active Q1 frontier if no "
                "real deployment can satisfy the T97/T100 packet with at least "
                "four non-conflicting authority domains before data collection."
            ),
            reinstatement_condition=(
                "Upgrade only after a real event-level packet passes T87/T97/"
                "T100 and then changes the T76/T86 verdict without policy or "
                "schema edits."
            ),
            next_gate=(
                "Stop synthetic detector modeling unless it names a real lab "
                "workflow that can freeze the packet pre-data."
            ),
        ),
        BranchAdjudication(
            branch_id="weak_measurement_discriminator",
            proposed_claim_id="Q1C weak-measurement discriminator",
            current_status="dormant_reinstatement_only",
            evidence_ids=ids_by_branch["weak_measurement_discriminator"],
            earned_content=(
                "A non-null weak-measurement discriminator shape is known: an "
                "independent pre-registered axis must change the TaF verdict "
                "with standard monitored statistics fixed."
            ),
            not_earned=(
                "A named platform that supplies that axis. Current homodyne, "
                "uncollapse, quantum-jump, and undo-cost examples collapse to "
                "same-record or postselection nulls."
            ),
            kill_condition=(
                "Keep weak measurement dormant while candidates fail to name "
                "the independent axis before analysis."
            ),
            reinstatement_condition=(
                "Reinstate immediately if a platform supplies a raw-log axis "
                "independent of the monitoring stream, control schedule, and "
                "success-conditioned recovery."
            ),
            next_gate=(
                "Require the independent-axis declaration before any further "
                "weak-measurement model is built."
            ),
        ),
        BranchAdjudication(
            branch_id="contextuality_guardrail",
            proposed_claim_id="Q1D contextuality guardrail",
            current_status="context_only_not_prediction",
            evidence_ids=ids_by_branch["contextuality_guardrail"],
            earned_content=(
                "Q1 can be stated without violating Bell, no-signalling, or "
                "the absence of a global noncontextual record assignment."
            ),
            not_earned=(
                "Any new Bell theorem, hidden-variable repair, or distinct "
                "quantum-foundations prediction."
            ),
            kill_condition=(
                "Delete Q1D as a claim if it cannot state a task beyond "
                "known contextuality/no-signalling discipline."
            ),
            reinstatement_condition=(
                "Promote only if it yields a record-access theorem not already "
                "captured by standard contextuality or causal-boundary facts."
            ),
            next_gate=(
                "Keep contextuality in the literature/guardrail layer until a "
                "nonredundant theorem target is named."
            ),
        ),
    )


def run_t101_analysis() -> T101Result:
    evidence = evidence_items()
    branches = branch_adjudications(evidence)
    by_id = {branch.branch_id: branch for branch in branches}

    q1_should_split = (
        by_id["q1_umbrella"].current_status
        == "too_broad_for_single_partially_supported_claim"
    )
    detector_blocked = (
        by_id["detector_provenance_protocol"].current_status
        == "externally_blocked_protocol_admissibility"
    )
    weak_reinstatement_only = (
        by_id["weak_measurement_discriminator"].current_status
        == "dormant_reinstatement_only"
    )
    contextuality_guardrail_only = (
        by_id["contextuality_guardrail"].current_status
        == "context_only_not_prediction"
    )
    no_new_dynamics = all(
        "New measurement dynamics" in branch.not_earned
        or "Empirical detector support" in branch.not_earned
        or "named platform" in branch.not_earned
        or "Any new Bell theorem" in branch.not_earned
        or "single physics-facing claim" in branch.not_earned
        for branch in branches
    )

    return T101Result(
        evidence=evidence,
        branches=branches,
        q1_should_split_before_paper_language=q1_should_split,
        no_branch_earns_new_measurement_dynamics=no_new_dynamics,
        detector_branch_externally_blocked=detector_blocked,
        weak_measurement_reinstatement_only=weak_reinstatement_only,
        contextuality_branch_is_guardrail_only=contextuality_guardrail_only,
        strongest_claim=(
            "Q1 no longer behaves like one partially supported physics "
            "conjecture. Its earned content splits into access-boundary record "
            "accounting, a blocked detector-provenance admissibility protocol, "
            "a dormant weak-measurement discriminator gate, and a "
            "contextuality/no-signalling guardrail. None currently earns new "
            "measurement dynamics or empirical quantum support."
        ),
        improved=(
            "T101 turns Q1 from an overloaded ledger line into an adjudicated "
            "decision tree with explicit subclaims, kill conditions, and "
            "reinstatement gates. A serious reader can now see which parts are "
            "physics-facing, which are protocol-facing, and which are only "
            "guardrails."
        ),
        weakened=(
            "This weakens Q1 by rejecting single-claim presentation. Detector "
            "provenance remains externally blocked, weak measurement is "
            "reinstatement-only, and contextuality contributes discipline "
            "rather than novelty. The surviving access-boundary content must "
            "compete directly with decoherence, Quantum Darwinism, and ordinary "
            "causal reachability."
        ),
        falsification_condition=(
            "T101 fails if one operational observable or theorem connects the "
            "access-boundary, detector, and weak-measurement routes without "
            "branch-specific rules; if a real detector packet passes T87/T97/"
            "T100 and yields a nonstandard verdict; or if a weak-measurement "
            "platform names an independent pre-registered axis satisfying T93."
        ),
        q1_update=(
            "Keep Q1 only as an umbrella pointer until it is split. The "
            "paper-facing claims should be Q1A access-boundary record "
            "accounting, Q1B detector provenance admissibility, Q1C dormant "
            "weak-measurement discriminator gate, and Q1D contextuality "
            "guardrail."
        ),
        claim_ledger_update=(
            "Add T101 to Q1: the current evidence no longer supports treating "
            "Q1 as one partially supported physics conjecture. It should be "
            "split before paper language; no branch currently earns new "
            "measurement dynamics or empirical support."
        ),
        open_blocker=(
            "The project must decide whether to create separate claim files for "
            "Q1A-Q1D or to demote Q1 to a roadmap umbrella. Without that split, "
            "the ledger hides incompatible evidence standards inside one "
            "status label."
        ),
        recommended_next=(
            "Implement the Q1 split in the claim ledger and write the Q1A "
            "literature comparison against decoherence, Quantum Darwinism, "
            "consistent histories, relational quantum mechanics, QBism, and "
            "many-worlds."
        ),
    )


def t101_result_to_dict(result: T101Result) -> dict[str, object]:
    return {
        "evidence": [
            {
                "test_id": item.test_id,
                "branch_id": item.branch_id,
                "role": item.role,
                "status": item.status,
                "note": item.note,
            }
            for item in result.evidence
        ],
        "branches": [
            {
                "branch_id": branch.branch_id,
                "proposed_claim_id": branch.proposed_claim_id,
                "current_status": branch.current_status,
                "evidence_ids": list(branch.evidence_ids),
                "earned_content": branch.earned_content,
                "not_earned": branch.not_earned,
                "kill_condition": branch.kill_condition,
                "reinstatement_condition": branch.reinstatement_condition,
                "next_gate": branch.next_gate,
            }
            for branch in result.branches
        ],
        "q1_should_split_before_paper_language": result.q1_should_split_before_paper_language,
        "no_branch_earns_new_measurement_dynamics": result.no_branch_earns_new_measurement_dynamics,
        "detector_branch_externally_blocked": result.detector_branch_externally_blocked,
        "weak_measurement_reinstatement_only": result.weak_measurement_reinstatement_only,
        "contextuality_branch_is_guardrail_only": result.contextuality_branch_is_guardrail_only,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }
