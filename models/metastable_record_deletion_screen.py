"""T152: metastable-record deletion screen for H7.

T145 left one possible H7 physical-arrow route: a substrate-native physical
record deletion whose reverse remains constructor-impossible after full
absorber accounting. This model tests the most natural candidate substrate:
metastable records protected by finite barriers.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import exp, log


LANDAUER_NAT_PER_BIT = log(2.0)


@dataclass(frozen=True)
class MetastableAbsorberVector:
    erased_bits: int
    beta_work_floor: float
    blank_capacity_delta: int
    sink_delta: int
    boundary_access: str
    provenance_state: str
    reversible_control: str
    source_copy_state: str
    beta_barrier: float | None
    reservoir_state: str
    control_window: str


@dataclass(frozen=True)
class MetastableFixture:
    fixture_id: str
    source: str
    reverse_edge_class: str
    left_label: str
    right_label: str
    left_d1_profile: tuple[int, int, int, int]
    right_d1_profile: tuple[int, int, int, int]
    left_absorber: MetastableAbsorberVector
    right_absorber: MetastableAbsorberVector
    horizon: float
    retention_threshold: float
    future_operation: str
    left_future_available: bool
    right_future_available: bool
    reverse_status: str
    physical_reading: str


@dataclass(frozen=True)
class MetastableAudit:
    fixture_id: str
    source: str
    reverse_edge_class: str
    absorber_vector_matched: bool
    absorber_mismatch_fields: tuple[str, ...]
    finite_barriers: bool
    left_survival_probability: float
    right_survival_probability: float
    d1_topology_split: bool
    future_operation: str
    future_operation_split: bool
    reverse_status: str
    h7_upgrade_candidate: bool
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T152Result:
    audits: tuple[MetastableAudit, ...]
    metastable_lifetime_residues: tuple[str, ...]
    fixed_accounting_topology_residues: tuple[str, ...]
    h7_arrow_candidates: tuple[str, ...]
    no_finite_metastable_substrate_clears_h7: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def one_bit_metastable_vector(
    *,
    beta_barrier: float | None,
    reservoir_state: str = "matched_room_temperature_bath",
    reversible_control: str = "finite_control_available",
    control_window: str = "control_available_within_horizon",
    sink_delta: int = 0,
) -> MetastableAbsorberVector:
    return MetastableAbsorberVector(
        erased_bits=1,
        beta_work_floor=LANDAUER_NAT_PER_BIT,
        blank_capacity_delta=1,
        sink_delta=sink_delta,
        boundary_access="matched_observer_boundary",
        provenance_state="matched_valid_provenance",
        reversible_control=reversible_control,
        source_copy_state="authoritative_source_remains",
        beta_barrier=beta_barrier,
        reservoir_state=reservoir_state,
        control_window=control_window,
    )


def escape_rate(beta_barrier: float | None, attempt_rate: float = 1.0) -> float:
    """Finite barriers have nonzero escape rate; None denotes a stipulated lock."""

    if beta_barrier is None:
        return 0.0
    if beta_barrier < 0:
        raise ValueError("beta_barrier must be nonnegative")
    return attempt_rate * exp(-beta_barrier)


def survival_probability(
    beta_barrier: float | None,
    horizon: float,
    attempt_rate: float = 1.0,
) -> float:
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    return exp(-escape_rate(beta_barrier, attempt_rate) * horizon)


def fixture_family() -> tuple[MetastableFixture, ...]:
    high_barrier = one_bit_metastable_vector(beta_barrier=30.0)
    low_barrier = one_bit_metastable_vector(beta_barrier=5.0)
    matched_branch_barrier = one_bit_metastable_vector(beta_barrier=20.0)
    infinite_lock = one_bit_metastable_vector(beta_barrier=None)
    no_control = one_bit_metastable_vector(
        beta_barrier=20.0,
        reversible_control="no_substrate_control_available_to_observer",
        control_window="control_denied_by_boundary",
    )
    cooled_barrier = one_bit_metastable_vector(
        beta_barrier=30.0,
        reservoir_state="changed_cold_reservoir_or_barrier_engineering",
    )

    return (
        MetastableFixture(
            fixture_id="finite_barrier_lifetime_split",
            source="finite metastable memory barrier",
            reverse_edge_class="physical_record_deletion",
            left_label="high_barrier_record",
            right_label="low_barrier_record",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(1, 1, 0, 1),
            left_absorber=high_barrier,
            right_absorber=low_barrier,
            horizon=1000.0,
            retention_threshold=0.99,
            future_operation="retain_record_through_horizon",
            left_future_available=True,
            right_future_available=False,
            reverse_status="finite_rate_possible_with_barrier_accounting",
            physical_reading=(
                "The long-lived side survives the horizon because its finite "
                "barrier is larger. That is ordinary kinetic lifetime "
                "accounting, not constructor impossibility."
            ),
        ),
        MetastableFixture(
            fixture_id="same_barrier_branch_topology_split",
            source="T145 branch-topology residue instantiated in a metastable cell",
            reverse_edge_class="physical_record_deletion",
            left_label="same_chain_metastable_copy",
            right_label="branch_spread_metastable_copy",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(1, 1, 1, 1),
            left_absorber=matched_branch_barrier,
            right_absorber=matched_branch_barrier,
            horizon=1000.0,
            retention_threshold=0.99,
            future_operation="survive_one_branch_failure",
            left_future_available=False,
            right_future_available=True,
            reverse_status="finite_rate_or_control_deletion_possible",
            physical_reading=(
                "Metastability can carry the T145 topology residue, but the "
                "record can still be deleted by finite control or finite-rate "
                "barrier crossing."
            ),
        ),
        MetastableFixture(
            fixture_id="infinite_barrier_constructor_lock",
            source="infinite-barrier idealization",
            reverse_edge_class="physical_record_deletion",
            left_label="finite_high_barrier_record",
            right_label="infinite_barrier_record",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(1, 1, 0, 1),
            left_absorber=high_barrier,
            right_absorber=infinite_lock,
            horizon=1000.0,
            retention_threshold=0.99,
            future_operation="make_deletion_impossible",
            left_future_available=False,
            right_future_available=True,
            reverse_status="constructor_stipulated_by_infinite_barrier",
            physical_reading=(
                "An infinite barrier can forbid deletion only by changing the "
                "admissible state space or imposing an ideal constructor "
                "constraint. It is not a finite metastable substrate result."
            ),
        ),
        MetastableFixture(
            fixture_id="control_window_denial",
            source="finite metastable record with observer control withheld",
            reverse_edge_class="physical_record_deletion",
            left_label="finite_control_available",
            right_label="control_denied_to_observer",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(1, 1, 0, 1),
            left_absorber=matched_branch_barrier,
            right_absorber=no_control,
            horizon=1000.0,
            retention_threshold=0.99,
            future_operation="delete_record_on_demand",
            left_future_available=True,
            right_future_available=False,
            reverse_status="blocked_by_observer_control_boundary",
            physical_reading=(
                "The reverse is blocked only relative to an observer/control "
                "boundary. That is access accounting, not substrate-native "
                "physical deletion impossibility."
            ),
        ),
        MetastableFixture(
            fixture_id="hidden_cold_reservoir_or_engineered_barrier",
            source="reservoir/barrier engineering control",
            reverse_edge_class="physical_record_deletion",
            left_label="ordinary_bath_record",
            right_label="cooled_or_engineered_record",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(1, 1, 0, 1),
            left_absorber=low_barrier,
            right_absorber=cooled_barrier,
            horizon=1000.0,
            retention_threshold=0.99,
            future_operation="retain_record_through_horizon",
            left_future_available=False,
            right_future_available=True,
            reverse_status="absorbed_by_reservoir_and_barrier_state",
            physical_reading=(
                "The apparent arrow comes from changing reservoir or barrier "
                "engineering data that ordinary metastability already tracks."
            ),
        ),
    )


def audit_fixture(fixture: MetastableFixture) -> MetastableAudit:
    mismatches = absorber_mismatch_fields(fixture.left_absorber, fixture.right_absorber)
    absorber_matched = not mismatches
    future_split = fixture.left_future_available != fixture.right_future_available
    topology_split = fixture.left_d1_profile != fixture.right_d1_profile
    finite_barriers = (
        fixture.left_absorber.beta_barrier is not None
        and fixture.right_absorber.beta_barrier is not None
    )
    left_survival = survival_probability(
        fixture.left_absorber.beta_barrier,
        fixture.horizon,
    )
    right_survival = survival_probability(
        fixture.right_absorber.beta_barrier,
        fixture.horizon,
    )
    candidate = is_metastable_h7_upgrade_candidate(
        reverse_edge_class=fixture.reverse_edge_class,
        absorber_vector_matched=absorber_matched,
        finite_barriers=finite_barriers,
        future_operation_split=future_split,
        reverse_status=fixture.reverse_status,
    )
    verdict = _verdict(fixture, mismatches, absorber_matched, finite_barriers, candidate)

    return MetastableAudit(
        fixture_id=fixture.fixture_id,
        source=fixture.source,
        reverse_edge_class=fixture.reverse_edge_class,
        absorber_vector_matched=absorber_matched,
        absorber_mismatch_fields=mismatches,
        finite_barriers=finite_barriers,
        left_survival_probability=left_survival,
        right_survival_probability=right_survival,
        d1_topology_split=topology_split,
        future_operation=fixture.future_operation,
        future_operation_split=future_split,
        reverse_status=fixture.reverse_status,
        h7_upgrade_candidate=candidate,
        verdict=verdict,
        interpretation=_interpretation(fixture, verdict),
    )


def absorber_mismatch_fields(
    left: MetastableAbsorberVector,
    right: MetastableAbsorberVector,
) -> tuple[str, ...]:
    left_values = asdict(left)
    right_values = asdict(right)
    return tuple(
        field for field, value in left_values.items() if value != right_values[field]
    )


def is_metastable_h7_upgrade_candidate(
    *,
    reverse_edge_class: str,
    absorber_vector_matched: bool,
    finite_barriers: bool,
    future_operation_split: bool,
    reverse_status: str,
) -> bool:
    return (
        reverse_edge_class == "physical_record_deletion"
        and absorber_vector_matched
        and finite_barriers
        and future_operation_split
        and reverse_status == "constructor_impossible_after_full_accounting"
    )


def run_t152_analysis() -> T152Result:
    audits = tuple(audit_fixture(fixture) for fixture in fixture_family())
    lifetime_residues = tuple(
        audit.fixture_id
        for audit in audits
        if audit.verdict == "absorbed_by_kinetic_barrier_accounting"
    )
    topology_residues = tuple(
        audit.fixture_id
        for audit in audits
        if audit.verdict == "fixed_accounting_metastable_topology_residue_not_arrow"
    )
    h7_candidates = tuple(
        audit.fixture_id for audit in audits if audit.h7_upgrade_candidate
    )

    return T152Result(
        audits=audits,
        metastable_lifetime_residues=lifetime_residues,
        fixed_accounting_topology_residues=topology_residues,
        h7_arrow_candidates=h7_candidates,
        no_finite_metastable_substrate_clears_h7=not h7_candidates,
        strongest_claim=(
            "Finite metastable barriers can make records long-lived and can "
            "support task-specific retention capabilities, but they do not "
            "make physical deletion constructor-impossible. Barrier height, "
            "reservoir state, control windows, and horizon choices are ordinary "
            "kinetic/resource data. Infinite barriers or denied controls create "
            "stipulated constructor or boundary restrictions. The only matched "
            "finite-barrier split is the T145 branch-topology residue, which "
            "changes future operation availability but not reverse admissibility."
        ),
        improved=(
            "T152 screens the most plausible physical-deletion substrate left "
            "after T145/T148. It turns 'stable record' into a finite barrier, "
            "lifetime, control, and reservoir audit rather than a shortcut to "
            "physical-arrow language."
        ),
        weakened=(
            "Metastability does not reopen H7 as a thermodynamic-arrow claim. "
            "Finite lifetime is kinetic residue, infinite lifetime is an ideal "
            "constraint, and observer-inaccessible deletion is a control-boundary "
            "fact."
        ),
        falsification_condition=(
            "T152 fails in H7's favor only if a finite, physically typed "
            "metastable record substrate has matched barrier, reservoir, "
            "erasure, capacity, sink, observer-boundary, provenance, source-copy, "
            "and reversible-control data, a task-natural future-operation split, "
            "and a physical deletion reverse that is constructor-impossible "
            "rather than merely exponentially unlikely or observer-inaccessible."
        ),
        h7_update=(
            "Add T152 to H7: metastable records are lifetime/resource absorbers, "
            "not physical-arrow evidence. Finite barriers give nonzero deletion "
            "routes; infinite barriers and missing controls are constructor or "
            "boundary stipulations; matched finite-barrier topology remains "
            "future-operation residue."
        ),
        claim_ledger_update=(
            "T152 tests the remaining physical-deletion gate against metastable "
            "records. No finite-barrier fixture clears H7. The route is absorbed "
            "by kinetic barrier/lifetime accounting, reservoir or control "
            "state, constructor idealization, or the already-demoted T145 "
            "future-operation topology residue."
        ),
        open_blocker=(
            "No finite metastable substrate in the current audit yields a "
            "constructor-impossible physical deletion reverse after full "
            "barrier, reservoir, control, sink, capacity, boundary, provenance, "
            "and source-copy accounting."
        ),
        suggested_next=(
            "Leave H7 in conditional constructor/resource-audit status unless "
            "a named finite physical record substrate can satisfy the T152 "
            "falsification condition. The next higher-value thermodynamic move "
            "would be a stochastic-thermodynamic citation map for this absorber."
        ),
    )


def _verdict(
    fixture: MetastableFixture,
    mismatches: tuple[str, ...],
    absorber_matched: bool,
    finite_barriers: bool,
    candidate: bool,
) -> str:
    if fixture.reverse_edge_class != "physical_record_deletion":
        return "non_deletion_reverse_class"
    if candidate:
        return "h7_physical_arrow_candidate"
    if "reservoir_state" in mismatches:
        return "absorbed_by_reservoir_or_temperature_accounting"
    if "beta_barrier" in mismatches:
        if not finite_barriers:
            return "absorbed_by_infinite_barrier_stipulation"
        return "absorbed_by_kinetic_barrier_accounting"
    if {"reversible_control", "control_window"} & set(mismatches):
        return "absorbed_by_control_boundary"
    if not absorber_matched:
        return "absorbed_by_accounting_mismatch"
    if fixture.left_future_available != fixture.right_future_available:
        return "fixed_accounting_metastable_topology_residue_not_arrow"
    return "fixed_accounting_no_arrow_residue"


def _interpretation(fixture: MetastableFixture, verdict: str) -> str:
    if verdict == "fixed_accounting_metastable_topology_residue_not_arrow":
        return (
            f"{fixture.fixture_id} preserves a future-operation split under "
            "matched finite metastable accounting, but deletion remains finite-"
            "rate or finite-control possible. Treat it as topology residue, not "
            "H7 arrow evidence."
        )
    if verdict == "absorbed_by_kinetic_barrier_accounting":
        return (
            f"{fixture.fixture_id} is absorbed by finite barrier/lifetime "
            f"accounting: {fixture.physical_reading}"
        )
    if verdict == "absorbed_by_infinite_barrier_stipulation":
        return (
            f"{fixture.fixture_id} relies on an infinite barrier idealization: "
            f"{fixture.physical_reading}"
        )
    if verdict == "absorbed_by_control_boundary":
        return (
            f"{fixture.fixture_id} is observer/control-boundary accounting: "
            f"{fixture.physical_reading}"
        )
    if verdict == "absorbed_by_reservoir_or_temperature_accounting":
        return (
            f"{fixture.fixture_id} is reservoir or barrier-engineering "
            f"accounting: {fixture.physical_reading}"
        )
    if verdict == "h7_physical_arrow_candidate":
        return (
            f"{fixture.fixture_id} would reopen H7 because finite-substrate "
            "deletion remains impossible after full accounting."
        )
    return f"{fixture.fixture_id} has no H7 arrow residue after metastable accounting."


def t152_result_to_dict(result: T152Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "fixture_id": audit.fixture_id,
                "source": audit.source,
                "reverse_edge_class": audit.reverse_edge_class,
                "absorber_vector_matched": audit.absorber_vector_matched,
                "absorber_mismatch_fields": list(audit.absorber_mismatch_fields),
                "finite_barriers": audit.finite_barriers,
                "left_survival_probability": audit.left_survival_probability,
                "right_survival_probability": audit.right_survival_probability,
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
        "metastable_lifetime_residues": list(result.metastable_lifetime_residues),
        "fixed_accounting_topology_residues": list(
            result.fixed_accounting_topology_residues
        ),
        "h7_arrow_candidates": list(result.h7_arrow_candidates),
        "no_finite_metastable_substrate_clears_h7": (
            result.no_finite_metastable_substrate_clears_h7
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

    print(json.dumps(t152_result_to_dict(run_t152_analysis()), indent=2))
