"""T145: fixed-accounting screen for physical record deletion.

T144 isolated physical record deletion as the only reverse-edge class with
possible H7 arrow upside. This model asks the next absorber question: after
free-energy, capacity, sink, boundary, provenance, source-copy, and reversible
control data are matched, does any current deletion-shaped fixture still supply
physical-arrow evidence?
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import log


LANDAUER_NAT_PER_BIT = log(2.0)


@dataclass(frozen=True)
class AbsorberVector:
    erased_bits: int
    beta_work_floor: float
    blank_capacity_delta: int
    sink_delta: int
    boundary_access: str
    provenance_state: str
    reversible_control: str
    source_copy_state: str


@dataclass(frozen=True)
class DeletionFixture:
    fixture_id: str
    source: str
    reverse_edge_class: str
    left_label: str
    right_label: str
    left_d1_delta: tuple[int, int, int, int]
    right_d1_delta: tuple[int, int, int, int]
    left_absorber: AbsorberVector
    right_absorber: AbsorberVector
    future_operation: str
    left_future_available: bool
    right_future_available: bool
    reverse_status: str
    physical_reading: str


@dataclass(frozen=True)
class DeletionAudit:
    fixture_id: str
    source: str
    reverse_edge_class: str
    absorber_vector_matched: bool
    absorber_mismatch_fields: tuple[str, ...]
    d1_topology_split: bool
    future_operation: str
    future_operation_split: bool
    reverse_status: str
    h7_upgrade_candidate: bool
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T145Result:
    audits: tuple[DeletionAudit, ...]
    fixed_accounting_capability_splits: tuple[str, ...]
    h7_arrow_candidates: tuple[str, ...]
    no_current_fixed_accounting_deletion_arrow: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def one_bit_blind_reset_vector() -> AbsorberVector:
    return AbsorberVector(
        erased_bits=1,
        beta_work_floor=LANDAUER_NAT_PER_BIT,
        blank_capacity_delta=1,
        sink_delta=0,
        boundary_access="matched_observer_boundary",
        provenance_state="matched_valid_provenance",
        reversible_control="blind_reset_only",
        source_copy_state="authoritative_source_remains",
    )


def fixture_family() -> tuple[DeletionFixture, ...]:
    one_bit = one_bit_blind_reset_vector()
    correlated_uncopy = AbsorberVector(
        erased_bits=0,
        beta_work_floor=0.0,
        blank_capacity_delta=1,
        sink_delta=0,
        boundary_access="matched_observer_boundary",
        provenance_state="matched_valid_provenance",
        reversible_control="full_source_copy_uncopy_handle",
        source_copy_state="authoritative_source_remains",
    )
    two_bit = AbsorberVector(
        erased_bits=2,
        beta_work_floor=2 * LANDAUER_NAT_PER_BIT,
        blank_capacity_delta=2,
        sink_delta=0,
        boundary_access="matched_observer_boundary",
        provenance_state="matched_valid_provenance",
        reversible_control="blind_reset_only",
        source_copy_state="authoritative_source_remains",
    )
    sink_export = AbsorberVector(
        erased_bits=1,
        beta_work_floor=LANDAUER_NAT_PER_BIT,
        blank_capacity_delta=1,
        sink_delta=1,
        boundary_access="matched_observer_boundary",
        provenance_state="matched_valid_provenance",
        reversible_control="blind_reset_only",
        source_copy_state="authoritative_source_remains",
    )
    access_loss = AbsorberVector(
        erased_bits=0,
        beta_work_floor=0.0,
        blank_capacity_delta=0,
        sink_delta=0,
        boundary_access="observer_access_revoked",
        provenance_state="matched_valid_provenance",
        reversible_control="not_applicable",
        source_copy_state="record_support_intact",
    )
    provenance_loss = AbsorberVector(
        erased_bits=0,
        beta_work_floor=0.0,
        blank_capacity_delta=0,
        sink_delta=0,
        boundary_access="matched_observer_boundary",
        provenance_state="authority_or_signature_invalidated",
        reversible_control="not_applicable",
        source_copy_state="record_support_intact",
    )

    return (
        DeletionFixture(
            fixture_id="same_floor_branch_topology_split",
            source="T142 same-chain copy vs branch-spread copy",
            reverse_edge_class="physical_record_deletion",
            left_label="same_chain_copy_blind_reset",
            right_label="branch_spread_copy_blind_reset",
            left_d1_delta=(1, 1, 0, 1),
            right_d1_delta=(1, 1, 1, 1),
            left_absorber=one_bit,
            right_absorber=one_bit,
            future_operation="survive_one_branch_failure",
            left_future_available=False,
            right_future_available=True,
            reverse_status="ordinary_erasure_accounted",
            physical_reading=(
                "Fixed one-bit blind-erasure accounting can still leave a "
                "branch-robustness capability split, but the reverse edge is "
                "ordinary deletion accounting rather than constructor "
                "impossibility."
            ),
        ),
        DeletionFixture(
            fixture_id="correlated_uncopy_vs_blind_reset",
            source="T142 uncopy/erasure split",
            reverse_edge_class="physical_record_deletion",
            left_label="correlated_uncopy_available",
            right_label="blind_reset_only",
            left_d1_delta=(1, 1, 0, 1),
            right_d1_delta=(1, 1, 0, 1),
            left_absorber=correlated_uncopy,
            right_absorber=one_bit,
            future_operation="restore_blank_target_without_heat",
            left_future_available=True,
            right_future_available=False,
            reverse_status="absorbed_by_reversible_control_and_erasure_cost",
            physical_reading=(
                "The split is real, but it is exactly the standard distinction "
                "between retaining the reversible source-copy handle and losing "
                "it before blind reset."
            ),
        ),
        DeletionFixture(
            fixture_id="one_bit_vs_two_bit_blind_reset",
            source="erasure-cost hostile control",
            reverse_edge_class="physical_record_deletion",
            left_label="delete_one_record_bit",
            right_label="delete_two_record_bits",
            left_d1_delta=(1, 1, 0, 1),
            right_d1_delta=(2, 2, 0, 2),
            left_absorber=one_bit,
            right_absorber=two_bit,
            future_operation="pay_same_blind_reset_floor",
            left_future_available=True,
            right_future_available=False,
            reverse_status="absorbed_by_erasure_cost",
            physical_reading=(
                "Different deletion burden here is just different erased-bit "
                "and free-energy accounting."
            ),
        ),
        DeletionFixture(
            fixture_id="hidden_sink_export_control",
            source="T106/T116 sink-accounting warning",
            reverse_edge_class="physical_record_deletion",
            left_label="blind_reset_without_exported_sink",
            right_label="blind_reset_with_exported_sink_history",
            left_d1_delta=(1, 1, 0, 1),
            right_d1_delta=(1, 1, 0, 1),
            left_absorber=one_bit,
            right_absorber=sink_export,
            future_operation="recover_deleted_history_from_sink",
            left_future_available=False,
            right_future_available=True,
            reverse_status="absorbed_by_sink_state",
            physical_reading=(
                "The future-operation split comes from hidden exported history, "
                "not from fixed-accounting physical deletion."
            ),
        ),
        DeletionFixture(
            fixture_id="observer_access_revocation",
            source="T141 access grant reverse",
            reverse_edge_class="boundary_access_loss",
            left_label="record_readable_to_observer",
            right_label="record_unreadable_to_observer",
            left_d1_delta=(1, 1, 0, 1),
            right_d1_delta=(-1, -1, 0, -1),
            left_absorber=access_loss,
            right_absorber=access_loss,
            future_operation="observer_can_read_record",
            left_future_available=True,
            right_future_available=False,
            reverse_status="not_physical_record_deletion",
            physical_reading=(
                "The record support can remain intact; only the observer access "
                "boundary changes."
            ),
        ),
        DeletionFixture(
            fixture_id="authority_provenance_revocation",
            source="T144 authority/provenance class",
            reverse_edge_class="authority_or_provenance_loss",
            left_label="signed_admissible_record",
            right_label="unsigned_or_revoked_record",
            left_d1_delta=(0, 0, 0, 1),
            right_d1_delta=(0, 0, 0, -1),
            left_absorber=provenance_loss,
            right_absorber=provenance_loss,
            future_operation="use_record_for_claim_review",
            left_future_available=True,
            right_future_available=False,
            reverse_status="governance_not_thermodynamic",
            physical_reading=(
                "The record can remain materially present while claim-review "
                "authority is revoked."
            ),
        ),
    )


def audit_fixture(fixture: DeletionFixture) -> DeletionAudit:
    mismatches = absorber_mismatch_fields(fixture.left_absorber, fixture.right_absorber)
    absorber_matched = not mismatches
    future_split = fixture.left_future_available != fixture.right_future_available
    topology_split = fixture.left_d1_delta != fixture.right_d1_delta
    candidate = is_h7_upgrade_candidate(
        reverse_edge_class=fixture.reverse_edge_class,
        absorber_vector_matched=absorber_matched,
        future_operation_split=future_split,
        reverse_status=fixture.reverse_status,
    )
    verdict = _verdict(fixture, mismatches, absorber_matched, future_split, candidate)

    return DeletionAudit(
        fixture_id=fixture.fixture_id,
        source=fixture.source,
        reverse_edge_class=fixture.reverse_edge_class,
        absorber_vector_matched=absorber_matched,
        absorber_mismatch_fields=mismatches,
        d1_topology_split=topology_split,
        future_operation=fixture.future_operation,
        future_operation_split=future_split,
        reverse_status=fixture.reverse_status,
        h7_upgrade_candidate=candidate,
        verdict=verdict,
        interpretation=_interpretation(fixture, verdict),
    )


def absorber_mismatch_fields(left: AbsorberVector, right: AbsorberVector) -> tuple[str, ...]:
    left_values = asdict(left)
    right_values = asdict(right)
    return tuple(
        field for field, value in left_values.items() if value != right_values[field]
    )


def is_h7_upgrade_candidate(
    *,
    reverse_edge_class: str,
    absorber_vector_matched: bool,
    future_operation_split: bool,
    reverse_status: str,
) -> bool:
    return (
        reverse_edge_class == "physical_record_deletion"
        and absorber_vector_matched
        and future_operation_split
        and reverse_status == "constructor_impossible_after_full_accounting"
    )


def run_t145_analysis() -> T145Result:
    audits = tuple(audit_fixture(fixture) for fixture in fixture_family())
    fixed_accounting_splits = tuple(
        audit.fixture_id
        for audit in audits
        if audit.reverse_edge_class == "physical_record_deletion"
        and audit.absorber_vector_matched
        and audit.future_operation_split
    )
    h7_candidates = tuple(
        audit.fixture_id for audit in audits if audit.h7_upgrade_candidate
    )

    return T145Result(
        audits=audits,
        fixed_accounting_capability_splits=fixed_accounting_splits,
        h7_arrow_candidates=h7_candidates,
        no_current_fixed_accounting_deletion_arrow=not h7_candidates,
        strongest_claim=(
            "At fixed free-energy floor, blank-capacity change, sink state, "
            "observer boundary, provenance state, source-copy status, and "
            "reversible-control access, the current fixtures contain one real "
            "split: branch topology changes future branch-failure robustness. "
            "That is a capability/topology residue, not H7 arrow evidence, "
            "because the deletion reverse remains ordinary erasure accounting. "
            "All arrow-looking deletion splits change an absorber variable or "
            "belong to a non-deletion reverse-edge class."
        ),
        improved=(
            "T145 turns the T142/T144 open blocker into an executable screen. "
            "Future H7 deletion witnesses must now hold the absorber vector "
            "fixed and still block the reverse for substrate-native reasons."
        ),
        weakened=(
            "The common escape 'D1 topology differs at fixed erasure floor' is "
            "not enough for a physical arrow. It can support a task-specific "
            "future-operation split, but H7 needs a constructor-impossible "
            "physical deletion reverse after full accounting."
        ),
        falsification_condition=(
            "T145 fails in H7's favor if a physically typed record substrate "
            "exhibits a physical_record_deletion pair with the full absorber "
            "vector matched, a task-natural future-operation split, and a "
            "reverse status of constructor_impossible_after_full_accounting."
        ),
        h7_update=(
            "Add T145 to H7: fixed-accounting D1 topology splits are capability "
            "residue unless the physical deletion reverse is impossible after "
            "free-energy, capacity, sink, boundary, provenance, source-copy, "
            "and reversible-control accounting are matched."
        ),
        claim_ledger_update=(
            "T145 screens the only remaining H7 physical-arrow class. At fixed "
            "absorber data, the current branch-topology split changes future "
            "operation availability but not reverse admissibility. Deletion-like "
            "arrow candidates are absorbed by changed erasure work, control "
            "handles, sink state, access boundary, or provenance class."
        ),
        open_blocker=(
            "No physically typed record substrate currently gives a "
            "constructor-impossible physical deletion reverse under matched "
            "free-energy, capacity, sink, boundary, provenance, source-copy, "
            "and reversible-control data."
        ),
        suggested_next=(
            "Either search for a substrate-native physical deletion candidate "
            "that clears the T145 gate, or demote H7's paper-facing role to a "
            "resource-accounting and reverse-edge audit discipline."
        ),
    )


def _verdict(
    fixture: DeletionFixture,
    mismatches: tuple[str, ...],
    absorber_matched: bool,
    future_split: bool,
    candidate: bool,
) -> str:
    if fixture.reverse_edge_class != "physical_record_deletion":
        return "non_deletion_reverse_class"
    if candidate:
        return "h7_physical_arrow_candidate"
    if not absorber_matched:
        if "sink_delta" in mismatches:
            return "absorbed_by_sink_accounting"
        if {"erased_bits", "beta_work_floor"} & set(mismatches):
            return "absorbed_by_erasure_work_accounting"
        if "reversible_control" in mismatches:
            return "absorbed_by_reversible_control_accounting"
        return "absorbed_by_accounting_mismatch"
    if future_split:
        return "fixed_accounting_capability_split_not_arrow"
    return "fixed_accounting_no_arrow_residue"


def _interpretation(fixture: DeletionFixture, verdict: str) -> str:
    if verdict == "fixed_accounting_capability_split_not_arrow":
        return (
            f"{fixture.fixture_id} preserves a task-specific capability split "
            "under matched accounting, but it does not block the deletion "
            "reverse. Treat it as FOA/topology residue, not H7 arrow evidence."
        )
    if verdict == "non_deletion_reverse_class":
        return (
            f"{fixture.fixture_id} is not physical record deletion. "
            f"{fixture.physical_reading}"
        )
    if verdict.startswith("absorbed_by"):
        return f"{fixture.fixture_id} is absorbed: {fixture.physical_reading}"
    if verdict == "h7_physical_arrow_candidate":
        return (
            f"{fixture.fixture_id} would reopen H7 because deletion remains "
            "constructor-impossible after full accounting."
        )
    return f"{fixture.fixture_id} has no arrow residue after fixed accounting."


def t145_result_to_dict(result: T145Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "fixture_id": audit.fixture_id,
                "source": audit.source,
                "reverse_edge_class": audit.reverse_edge_class,
                "absorber_vector_matched": audit.absorber_vector_matched,
                "absorber_mismatch_fields": list(audit.absorber_mismatch_fields),
                "d1_topology_split": audit.d1_topology_split,
                "future_operation": audit.future_operation,
                "future_operation_split": audit.future_operation_split,
                "reverse_status": audit.reverse_status,
                "h7_upgrade_candidate": audit.h7_upgrade_candidate,
                "verdict": audit.verdict,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "fixed_accounting_capability_splits": list(
            result.fixed_accounting_capability_splits
        ),
        "h7_arrow_candidates": list(result.h7_arrow_candidates),
        "no_current_fixed_accounting_deletion_arrow": (
            result.no_current_fixed_accounting_deletion_arrow
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t145_result_to_dict(run_t145_analysis()), indent=2))
