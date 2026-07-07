"""T498 - authoritative commit / settlement composite stack gate.

This builds the second composite absorber-stack lane named after T496/T497.
The fixture tests whether an apparent local-record finality split survives
after granting full log, ledger, server, rollback, and completion-rights
absorbers. The admitted output is composite explanation / review target only,
not a distributed-systems metaphor for TaF and not claim movement.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Iterable


ARTIFACT = "T498-authoritative-commit-settlement-stack-gate-v0.1"
VERDICT = "AUTHORITATIVE_COMMIT_SETTLEMENT_STACK_BUILT_COMPOSITE_EXPLANATION"
SOURCE_T496 = "tests/T496-bridge-functor-admission-packet-gate.md"
SOURCE_T497 = "tests/T497-bounded-retrieval-source-checked-stack-gate.md"
SOURCE_PROGRESS_LANES = "open-problems/composite-absorber-stack-progress-lanes.md"
SOURCE_PACKET_REPORT = "technical-reports/TECHNICAL-REPORT-bridge-functor-admission-packet-v0.1.md"

HONEST_CEILING = (
    "T498 is a finite authoritative-settlement composite explanation and "
    "review target. It does not prove Time as Finality, does not promote a "
    "distributed-systems metaphor into physics, and does not move claim ledger, "
    "roadmap, README, North Star, public posture, hard policy, external "
    "publication, or cross-repo truth."
)


Projection = Callable[["SettlementState"], tuple[Any, ...]]
Capability = Callable[["SettlementState"], tuple[Any, ...]]


@dataclass(frozen=True)
class SettlementState:
    state_id: str
    local_visible_record: str
    client_claim: str
    server_verdict: str
    ledger_log: tuple[str, ...]
    rollback_rule: str
    completion_rights: tuple[str, ...]


@dataclass(frozen=True)
class StackAbsorber:
    absorber_id: str
    status: str
    granted_form: str
    effect: str


@dataclass(frozen=True)
class ProjectionEvaluation:
    projection_label: str
    capability_label: str
    factorizes: bool
    expected_factorizes: bool
    projection_class_count: int
    capability_class_count: int
    max_capability_spread: int
    expected_max_spread: int
    non_singleton_fiber_count: int
    label: str


@dataclass(frozen=True)
class Reading:
    reading_id: str
    description: str
    admits_composite_explanation: bool = False
    claims_local_marker_residual: bool = False
    claims_distributed_systems_metaphor: bool = False
    requests_claim_movement: bool = False
    requests_public_posture_movement: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth_movement: bool = False


@dataclass(frozen=True)
class ReadingDecision:
    reading_id: str
    admitted: bool
    label: str
    action: str
    reason: str


def source_states() -> tuple[SettlementState, ...]:
    local_record = "client:order-7:commit-marker-visible"
    client_claim = "committed"
    return (
        SettlementState(
            state_id="settled_commit",
            local_visible_record=local_record,
            client_claim=client_claim,
            server_verdict="settled",
            ledger_log=("client_submit", "server_accept", "ledger_commit"),
            rollback_rule="rollback_closed",
            completion_rights=("client_record", "server_verdict", "ledger_log", "rollback_rule"),
        ),
        SettlementState(
            state_id="pending_reconciliation",
            local_visible_record=local_record,
            client_claim=client_claim,
            server_verdict="pending",
            ledger_log=("client_submit", "server_accept", "reconciliation_open"),
            rollback_rule="rollback_open",
            completion_rights=("client_record", "server_verdict", "ledger_log", "rollback_rule"),
        ),
        SettlementState(
            state_id="rolled_back_commit",
            local_visible_record=local_record,
            client_claim=client_claim,
            server_verdict="rolled_back",
            ledger_log=("client_submit", "server_accept", "rollback_recorded"),
            rollback_rule="rollback_closed",
            completion_rights=("client_record", "server_verdict", "ledger_log", "rollback_rule"),
        ),
        SettlementState(
            state_id="fork_conflict",
            local_visible_record=local_record,
            client_claim=client_claim,
            server_verdict="conflict",
            ledger_log=("client_submit", "server_accept", "competing_authority_commit"),
            rollback_rule="adjudication_required",
            completion_rights=("client_record", "server_verdict", "ledger_log", "rollback_rule"),
        ),
    )


def project_local_visible(state: SettlementState) -> tuple[Any, ...]:
    return ("local_visible", state.local_visible_record, state.client_claim)


def project_client_claim_only(state: SettlementState) -> tuple[Any, ...]:
    return ("client_claim", state.client_claim)


def project_ledger_server_completion(state: SettlementState) -> tuple[Any, ...]:
    return (
        "ledger_server_completion",
        state.server_verdict,
        state.ledger_log,
        state.rollback_rule,
    )


def project_full_authority_completion(state: SettlementState) -> tuple[Any, ...]:
    return (
        "full_authority_completion",
        state.local_visible_record,
        state.client_claim,
        state.server_verdict,
        state.ledger_log,
        state.rollback_rule,
        state.completion_rights,
    )


def cap_local_display(state: SettlementState) -> tuple[Any, ...]:
    return ("can_display_local_receipt", state.local_visible_record, state.client_claim)


def cap_authoritative_settlement(state: SettlementState) -> tuple[Any, ...]:
    by_verdict = {
        "settled": ("settled", "spendable", "rollback_closed", "authoritative"),
        "pending": ("provisional", "not_spendable", "rollback_open", "not_final"),
        "rolled_back": ("voided", "not_spendable", "rollback_closed", "authoritative_void"),
        "conflict": ("conflict", "not_spendable", "adjudication_required", "not_final"),
    }
    return ("settlement_capability",) + by_verdict[state.server_verdict]


def absorber_stack() -> tuple[StackAbsorber, ...]:
    return (
        StackAbsorber(
            absorber_id="local_visible_record",
            status="granted_and_tested",
            granted_form="The client-local commit marker and client claim are visible.",
            effect="Local display capability factors, but settlement capability does not.",
        ),
        StackAbsorber(
            absorber_id="server_verdict_completion",
            status="granted_and_tested",
            granted_form="The authoritative server verdict is visible.",
            effect="Settlement status is no longer inferred from the local marker.",
        ),
        StackAbsorber(
            absorber_id="ledger_log_completion",
            status="granted_and_tested",
            granted_form="The ledger or authority log is visible.",
            effect="Commit, pending reconciliation, rollback, and conflict histories are distinguished.",
        ),
        StackAbsorber(
            absorber_id="rollback_reconciliation_rule",
            status="granted_and_tested",
            granted_form="Rollback window and adjudication rules are part of the state.",
            effect="Provisional versus closed finality is ordinary settlement bookkeeping.",
        ),
        StackAbsorber(
            absorber_id="explicit_completion_rights",
            status="granted_and_tested",
            granted_form="The observer profile states whether client, server, ledger, and rule fields are accessible.",
            effect="The capability split is classified as access/completion mismatch, not new finality structure.",
        ),
    )


def evaluate_factorization(
    states: Iterable[SettlementState],
    projection: Projection,
    capability: Capability,
) -> tuple[bool, int, int, int, int]:
    fibers: dict[tuple[Any, ...], set[tuple[Any, ...]]] = defaultdict(set)
    capability_values: set[tuple[Any, ...]] = set()
    for state in states:
        p_value = projection(state)
        c_value = capability(state)
        fibers[p_value].add(c_value)
        capability_values.add(c_value)
    spreads = [len(values) for values in fibers.values()]
    return (
        all(spread == 1 for spread in spreads),
        len(fibers),
        len(capability_values),
        max(spreads),
        sum(1 for spread in spreads if spread > 1),
    )


def projection_evaluations() -> tuple[ProjectionEvaluation, ...]:
    states = source_states()
    scenarios: tuple[tuple[str, str, Projection, Capability, bool, int], ...] = (
        (
            "local_visible",
            "authoritative_settlement",
            project_local_visible,
            cap_authoritative_settlement,
            False,
            4,
        ),
        (
            "local_visible",
            "local_display",
            project_local_visible,
            cap_local_display,
            True,
            1,
        ),
        (
            "client_claim_only",
            "authoritative_settlement",
            project_client_claim_only,
            cap_authoritative_settlement,
            False,
            4,
        ),
        (
            "ledger_server_completion",
            "authoritative_settlement",
            project_ledger_server_completion,
            cap_authoritative_settlement,
            True,
            1,
        ),
        (
            "full_authority_completion",
            "authoritative_settlement",
            project_full_authority_completion,
            cap_authoritative_settlement,
            True,
            1,
        ),
    )

    rows: list[ProjectionEvaluation] = []
    for projection_label, capability_label, projection, capability, expected, spread in scenarios:
        factorizes, p_count, c_count, max_spread, non_singleton = evaluate_factorization(
            states, projection, capability
        )
        if factorizes == expected and max_spread == spread:
            label = "EXPECTED_SETTLEMENT_STACK_BEHAVIOR"
        elif factorizes == expected:
            label = "EXPECTED_FACTORING_UNEXPECTED_SPREAD"
        else:
            label = "UNEXPECTED_FACTORING_BEHAVIOR"
        rows.append(
            ProjectionEvaluation(
                projection_label=projection_label,
                capability_label=capability_label,
                factorizes=factorizes,
                expected_factorizes=expected,
                projection_class_count=p_count,
                capability_class_count=c_count,
                max_capability_spread=max_spread,
                expected_max_spread=spread,
                non_singleton_fiber_count=non_singleton,
                label=label,
            )
        )
    return tuple(rows)


def readings() -> tuple[Reading, ...]:
    return (
        Reading(
            reading_id="authoritative_commit_composite_explanation",
            description="Local finality appearance is explained by server, ledger, rollback, and completion-rights state.",
            admits_composite_explanation=True,
        ),
        Reading(
            reading_id="local_marker_as_finality_residual",
            description="Treat same local commit marker with different authority states as new finality residue.",
            claims_local_marker_residual=True,
        ),
        Reading(
            reading_id="distributed_systems_metaphor_proves_taf",
            description="Use ledger or game settlement as a metaphor proving Time as Finality.",
            claims_distributed_systems_metaphor=True,
        ),
        Reading(
            reading_id="claim_or_public_posture_shortcut",
            description="Move a claim, roadmap, README, North Star, or public posture from the fixture.",
            requests_claim_movement=True,
            requests_public_posture_movement=True,
        ),
        Reading(
            reading_id="external_or_cross_repo_shortcut",
            description="Publish externally or update another repository from this settlement fixture.",
            requests_external_publication=True,
            requests_cross_repo_truth_movement=True,
        ),
    )


def decide_reading(reading: Reading) -> ReadingDecision:
    if reading.requests_external_publication or reading.requests_cross_repo_truth_movement:
        return ReadingDecision(
            reading.reading_id,
            False,
            "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT",
            "stop",
            "The fixture does not authorize external publication or cross-repo truth movement.",
        )
    if reading.requests_claim_movement or reading.requests_public_posture_movement:
        return ReadingDecision(
            reading.reading_id,
            False,
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            "stop",
            "Composite explanation does not move claims, roadmap, README, North Star, or public posture.",
        )
    if reading.claims_distributed_systems_metaphor:
        return ReadingDecision(
            reading.reading_id,
            False,
            "REJECTED_DISTRIBUTED_SYSTEMS_METAPHOR",
            "reject",
            "Settlement systems are a domain-native fixture here, not proof of TaF or physics.",
        )
    if reading.claims_local_marker_residual:
        return ReadingDecision(
            reading.reading_id,
            False,
            "REJECTED_UNDERDESCRIBED_LOCAL_PROJECTION",
            "reject",
            "The local-marker split disappears after granting native server, ledger, rollback, and completion state.",
        )
    if reading.admits_composite_explanation:
        return ReadingDecision(
            reading.reading_id,
            True,
            "ADMITTED_COMPOSITE_ABSORBER_EXPLANATION",
            "record",
            "The stack explains apparent settlement finality as local record plus authority completion.",
        )
    return ReadingDecision(
        reading.reading_id,
        False,
        "REJECTED_UNTYPED_READING",
        "reject",
        "The reading is outside the declared authoritative-settlement stack.",
    )


def run() -> dict[str, Any]:
    states = source_states()
    evaluations = projection_evaluations()
    decisions = tuple(decide_reading(reading) for reading in readings())
    all_expected = all(
        evaluation.factorizes == evaluation.expected_factorizes
        and evaluation.max_capability_spread == evaluation.expected_max_spread
        for evaluation in evaluations
    )

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "source_t496": SOURCE_T496,
        "source_t497": SOURCE_T497,
        "source_progress_lanes": SOURCE_PROGRESS_LANES,
        "source_packet_report": SOURCE_PACKET_REPORT,
        "honest_ceiling": HONEST_CEILING,
        "source_states": [asdict(state) for state in states],
        "absorber_stack": [asdict(absorber) for absorber in absorber_stack()],
        "projection_evaluations": [asdict(evaluation) for evaluation in evaluations],
        "reading_decisions": [asdict(decision) for decision in decisions],
        "overall": {
            "all_projection_checks_expected": all_expected,
            "local_visible_settlement_factorizes": False,
            "full_authority_completion_factorizes": True,
            "outcome": "COMPOSITE_ABSORBER_EXPLANATION",
            "review_target_only": True,
            "claim_movement": False,
            "roadmap_movement": False,
            "readme_movement": False,
            "north_star_movement": False,
            "public_posture_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "strongest_result": (
            "A single client-visible commit marker supports the native local "
            "display task but has a four-way settlement capability spread across "
            "settled, pending, rolled-back, and conflict authority states. Full "
            "server/ledger/log/rollback completion restores factorization, so "
            "the result is a composite absorber explanation of authoritative "
            "settlement rather than new finality residue."
        ),
        "recommended_next": (
            "If this lane continues, source-check a domain-native commit or "
            "consensus protocol and compare its exact finality/rollback rules "
            "against the T498 finite stack before using any theorem language."
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    state_rows = [
        "| {state_id} | {server} | {rollback} | {log} |".format(
            state_id=state["state_id"],
            server=state["server_verdict"],
            rollback=state["rollback_rule"],
            log=", ".join(state["ledger_log"]),
        )
        for state in payload["source_states"]
    ]
    absorber_rows = [
        "| {absorber_id} | {status} | {granted} | {effect} |".format(
            absorber_id=absorber["absorber_id"],
            status=absorber["status"],
            granted=absorber["granted_form"],
            effect=absorber["effect"],
        )
        for absorber in payload["absorber_stack"]
    ]
    evaluation_rows = [
        "| {projection} | {capability} | {factorizes} | {spread} | {expected} | {label} |".format(
            projection=evaluation["projection_label"],
            capability=evaluation["capability_label"],
            factorizes="yes" if evaluation["factorizes"] else "no",
            spread=evaluation["max_capability_spread"],
            expected=evaluation["expected_max_spread"],
            label=evaluation["label"],
        )
        for evaluation in payload["projection_evaluations"]
    ]
    reading_rows = [
        "| {reading_id} | {admitted} | {label} | {action} | {reason} |".format(
            reading_id=decision["reading_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            action=decision["action"],
            reason=decision["reason"],
        )
        for decision in payload["reading_decisions"]
    ]

    return "\n".join(
        [
            "# T498 - Authoritative Commit / Settlement Stack Gate - v0.1 results",
            "",
            "> Composite explanation only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T498-authoritative-commit-settlement-stack-gate.md`",
            "- Model: `models/authoritative_commit_settlement_stack_gate.py`",
            "- Tests: `tests/test_authoritative_commit_settlement_stack_gate.py`",
            "- Progress lanes: `open-problems/composite-absorber-stack-progress-lanes.md`",
            "- Bridge-Functor gate: `tests/T496-bridge-functor-admission-packet-gate.md`",
            "- Artifact JSON: `results/T498-authoritative-commit-settlement-stack-gate-v0.1.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Source States",
            "",
            "| State | Server verdict | Rollback rule | Ledger log |",
            "| --- | --- | --- | --- |",
            *state_rows,
            "",
            "## Absorber Stack",
            "",
            "| Absorber | Status | Granted form | Effect |",
            "| --- | --- | --- | --- |",
            *absorber_rows,
            "",
            "## Projection Checks",
            "",
            "| Projection | Capability | Factors? | Max spread | Expected spread | Label |",
            "| --- | --- | --- | ---: | ---: | --- |",
            *evaluation_rows,
            "",
            "## Reading Decisions",
            "",
            "| Reading | Admitted? | Label | Action | Reason |",
            "| --- | --- | --- | --- | --- |",
            *reading_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a finite composite explanation of authoritative settlement as local record plus server, ledger, rollback, and completion-rights state.",
            "",
            "Does not earn: a TaF proof, physics mechanism, claim-ledger movement, roadmap movement, README movement, North Star movement, public-posture movement, external-publication permission, or cross-repo truth movement.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T498-authoritative-commit-settlement-stack-gate-v0.1.json"
        md_path = results_dir / "T498-authoritative-commit-settlement-stack-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
