"""T168: exact-sector / gauge restriction screen for H7.

T160 left exact sector and gauge restrictions as a family-level null screen:
they do not reopen H7 unless they admit a finite operational substrate where
physical record deletion remains constructor-impossible after full accounting.

This module turns that screen into a finite audit. It does not model gauge
field dynamics. It tests the proof obligation shape: sector conservation,
compensating reservoirs, gauge-orbit redundancy, exact ideal restrictions, and
finite symmetry-breaking controls must be named before "deletion impossible"
can count as H7 evidence.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import log


LANDAUER_NAT_PER_BIT = log(2.0)


@dataclass(frozen=True)
class SectorAbsorberVector:
    erased_bits: int
    beta_work_floor: float
    blank_capacity_delta: int
    sink_delta: int
    observer_boundary: str
    provenance_state: str
    source_copy_state: str
    reversible_control: str
    conserved_quantity_bookkeeping: str
    compensating_reservoir_state: str
    gauge_orbit_treatment: str
    sector_enforcement: str
    allowed_control_class: str


@dataclass(frozen=True)
class SectorFixture:
    fixture_id: str
    source: str
    reverse_edge_class: str
    left_label: str
    right_label: str
    left_d1_profile: tuple[int, int, int, int]
    right_d1_profile: tuple[int, int, int, int]
    left_absorber: SectorAbsorberVector
    right_absorber: SectorAbsorberVector
    finite_operational_substrate: bool
    gauge_invariant_difference: bool
    future_operation: str
    left_future_available: bool
    right_future_available: bool
    reverse_status: str
    physical_reading: str


@dataclass(frozen=True)
class SectorAudit:
    fixture_id: str
    source: str
    reverse_edge_class: str
    absorber_vector_matched: bool
    absorber_mismatch_fields: tuple[str, ...]
    finite_operational_substrate: bool
    gauge_invariant_difference: bool
    d1_topology_split: bool
    future_operation: str
    future_operation_split: bool
    reverse_status: str
    h7_upgrade_candidate: bool
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T168Result:
    audits: tuple[SectorAudit, ...]
    sector_rule_stipulations: tuple[str, ...]
    reservoir_absorptions: tuple[str, ...]
    gauge_redundancies: tuple[str, ...]
    fixed_accounting_topology_residues: tuple[str, ...]
    h7_arrow_candidates: tuple[str, ...]
    no_sector_fixture_clears_h7: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


def one_bit_sector_vector(
    *,
    conserved_quantity_bookkeeping: str = "global_charge_accounting_matched",
    compensating_reservoir_state: str = "matched_no_reservoir_change",
    gauge_orbit_treatment: str = "physical_orbit_fixed",
    sector_enforcement: str = "finite_operational_enforcement",
    reversible_control: str = "finite_control_available",
    allowed_control_class: str = "charge_conserving_finite_controls",
    sink_delta: int = 0,
) -> SectorAbsorberVector:
    return SectorAbsorberVector(
        erased_bits=1,
        beta_work_floor=LANDAUER_NAT_PER_BIT,
        blank_capacity_delta=1,
        sink_delta=sink_delta,
        observer_boundary="matched_observer_boundary",
        provenance_state="matched_valid_provenance",
        source_copy_state="authoritative_source_remains",
        reversible_control=reversible_control,
        conserved_quantity_bookkeeping=conserved_quantity_bookkeeping,
        compensating_reservoir_state=compensating_reservoir_state,
        gauge_orbit_treatment=gauge_orbit_treatment,
        sector_enforcement=sector_enforcement,
        allowed_control_class=allowed_control_class,
    )


def fixture_family() -> tuple[SectorFixture, ...]:
    matched_sector_rule = one_bit_sector_vector(
        conserved_quantity_bookkeeping="local_sector_only_no_reservoir_declared",
        compensating_reservoir_state="no_compensating_reservoir_declared",
    )
    compensated_left = one_bit_sector_vector(
        conserved_quantity_bookkeeping="global_charge_accounting_matched",
        compensating_reservoir_state="reservoir_initial_charge_available",
    )
    compensated_right = one_bit_sector_vector(
        conserved_quantity_bookkeeping="global_charge_accounting_matched",
        compensating_reservoir_state="reservoir_charge_changed_by_delete",
        sink_delta=1,
    )
    pure_gauge_left = one_bit_sector_vector(
        gauge_orbit_treatment="representative_label_A"
    )
    pure_gauge_right = one_bit_sector_vector(
        gauge_orbit_treatment="representative_label_B"
    )
    exact_sector = one_bit_sector_vector(
        sector_enforcement="exact_superselection_ideal",
        allowed_control_class="sector_changing_controls_forbidden_by_axiom",
        reversible_control="no_finite_sector_changing_control_admitted",
    )
    finite_leak_left = one_bit_sector_vector(
        sector_enforcement="large_finite_symmetry_penalty",
        allowed_control_class="finite_symmetry_breaking_controls_denied",
        reversible_control="restricted_control_available",
    )
    finite_leak_right = one_bit_sector_vector(
        sector_enforcement="large_finite_symmetry_penalty",
        allowed_control_class="finite_symmetry_breaking_controls_admitted",
        reversible_control="finite_symmetry_breaking_control_available",
    )
    matched_topology = one_bit_sector_vector()

    return (
        SectorFixture(
            fixture_id="local_sector_delete_forbidden_without_reservoir",
            source="finite charged record with only local sector bookkeeping",
            reverse_edge_class="physical_record_deletion",
            left_label="charged_record_present",
            right_label="neutral_blank_without_compensator",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(0, 0, 0, 0),
            left_absorber=matched_sector_rule,
            right_absorber=matched_sector_rule,
            finite_operational_substrate=True,
            gauge_invariant_difference=True,
            future_operation="delete_record_while_preserving_declared_sector",
            left_future_available=False,
            right_future_available=True,
            reverse_status="operation_forbidden_by_declared_sector_rule",
            physical_reading=(
                "Deletion is impossible only because the allowed operation "
                "class excludes the compensating degree of freedom that would "
                "carry the conserved quantity."
            ),
        ),
        SectorFixture(
            fixture_id="compensating_reservoir_restores_deletion",
            source="charged record with explicit reservoir accounting",
            reverse_edge_class="physical_record_deletion",
            left_label="record_plus_reservoir_before_delete",
            right_label="blank_plus_reservoir_after_delete",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(0, 0, 0, 0),
            left_absorber=compensated_left,
            right_absorber=compensated_right,
            finite_operational_substrate=True,
            gauge_invariant_difference=True,
            future_operation="delete_record_with_global_charge_conservation",
            left_future_available=False,
            right_future_available=True,
            reverse_status="finite_control_possible_with_reservoir_accounting",
            physical_reading=(
                "Once the compensating reservoir is in the source description, "
                "the apparent sector obstruction becomes ordinary conserved-"
                "quantity and sink accounting."
            ),
        ),
        SectorFixture(
            fixture_id="gauge_relabeling_record_loss",
            source="same physical gauge orbit with different representatives",
            reverse_edge_class="gauge_relabeling",
            left_label="representative_A",
            right_label="representative_B",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(0, 1, 0, 1),
            left_absorber=pure_gauge_left,
            right_absorber=pure_gauge_right,
            finite_operational_substrate=True,
            gauge_invariant_difference=False,
            future_operation="change_representative_label",
            left_future_available=True,
            right_future_available=True,
            reverse_status="pure_gauge_or_relabeling",
            physical_reading=(
                "The visible record label changes, but the physical gauge orbit "
                "does not. This is not physical deletion."
            ),
        ),
        SectorFixture(
            fixture_id="exact_superselection_constructor_lock",
            source="exact superselection or sector-changing ban",
            reverse_edge_class="physical_record_deletion",
            left_label="sector_locked_record",
            right_label="sector_changing_delete",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(0, 0, 0, 0),
            left_absorber=exact_sector,
            right_absorber=exact_sector,
            finite_operational_substrate=False,
            gauge_invariant_difference=True,
            future_operation="delete_across_exact_sector_boundary",
            left_future_available=False,
            right_future_available=True,
            reverse_status="constructor_stipulated_by_exact_sector",
            physical_reading=(
                "The reverse is forbidden by an exact sector axiom, not by a "
                "finite substrate-native deletion obstruction."
            ),
        ),
        SectorFixture(
            fixture_id="finite_symmetry_breaking_control",
            source="finite sector enforcement with a symmetry-breaking control",
            reverse_edge_class="physical_record_deletion",
            left_label="restricted_controls_only",
            right_label="symmetry_breaking_control_admitted",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(0, 0, 0, 0),
            left_absorber=finite_leak_left,
            right_absorber=finite_leak_right,
            finite_operational_substrate=True,
            gauge_invariant_difference=True,
            future_operation="delete_record_with_finite_symmetry_breaking",
            left_future_available=False,
            right_future_available=True,
            reverse_status="finite_control_or_leak_possible",
            physical_reading=(
                "Finite enforcement can make deletion costly or unavailable to "
                "a restricted controller, but admitting the finite control turns "
                "the effect into control/resource accounting."
            ),
        ),
        SectorFixture(
            fixture_id="matched_sector_branch_topology_residue",
            source="T145-style topology residue carried by charged branches",
            reverse_edge_class="physical_record_deletion",
            left_label="single_holder_charged_record",
            right_label="branch_spread_charged_record",
            left_d1_profile=(1, 1, 0, 1),
            right_d1_profile=(1, 1, 1, 1),
            left_absorber=matched_topology,
            right_absorber=matched_topology,
            finite_operational_substrate=True,
            gauge_invariant_difference=True,
            future_operation="survive_one_charged_branch_failure",
            left_future_available=False,
            right_future_available=True,
            reverse_status="finite_control_deletion_possible",
            physical_reading=(
                "The fixed-accounting split is a future-operation topology "
                "residue, but sector conservation does not make deletion "
                "constructor-impossible."
            ),
        ),
    )


def audit_fixture(fixture: SectorFixture) -> SectorAudit:
    mismatches = absorber_mismatch_fields(fixture.left_absorber, fixture.right_absorber)
    absorber_matched = not mismatches
    future_split = fixture.left_future_available != fixture.right_future_available
    topology_split = fixture.left_d1_profile != fixture.right_d1_profile
    candidate = is_sector_h7_upgrade_candidate(
        reverse_edge_class=fixture.reverse_edge_class,
        absorber_vector_matched=absorber_matched,
        finite_operational_substrate=fixture.finite_operational_substrate,
        gauge_invariant_difference=fixture.gauge_invariant_difference,
        future_operation_split=future_split,
        reverse_status=fixture.reverse_status,
    )
    verdict = _verdict(fixture, mismatches, absorber_matched, candidate)

    return SectorAudit(
        fixture_id=fixture.fixture_id,
        source=fixture.source,
        reverse_edge_class=fixture.reverse_edge_class,
        absorber_vector_matched=absorber_matched,
        absorber_mismatch_fields=mismatches,
        finite_operational_substrate=fixture.finite_operational_substrate,
        gauge_invariant_difference=fixture.gauge_invariant_difference,
        d1_topology_split=topology_split,
        future_operation=fixture.future_operation,
        future_operation_split=future_split,
        reverse_status=fixture.reverse_status,
        h7_upgrade_candidate=candidate,
        verdict=verdict,
        interpretation=_interpretation(fixture, verdict),
    )


def absorber_mismatch_fields(
    left: SectorAbsorberVector,
    right: SectorAbsorberVector,
) -> tuple[str, ...]:
    left_values = asdict(left)
    right_values = asdict(right)
    return tuple(
        field for field, value in left_values.items() if value != right_values[field]
    )


def is_sector_h7_upgrade_candidate(
    *,
    reverse_edge_class: str,
    absorber_vector_matched: bool,
    finite_operational_substrate: bool,
    gauge_invariant_difference: bool,
    future_operation_split: bool,
    reverse_status: str,
) -> bool:
    return (
        reverse_edge_class == "physical_record_deletion"
        and absorber_vector_matched
        and finite_operational_substrate
        and gauge_invariant_difference
        and future_operation_split
        and reverse_status == "constructor_impossible_after_full_accounting"
    )


def run_t168_analysis() -> T168Result:
    audits = tuple(audit_fixture(fixture) for fixture in fixture_family())
    sector_rule_stipulations = tuple(
        audit.fixture_id
        for audit in audits
        if audit.verdict == "sector_rule_stipulation_not_arrow"
    )
    reservoir_absorptions = tuple(
        audit.fixture_id
        for audit in audits
        if audit.verdict == "absorbed_by_conserved_quantity_or_reservoir_accounting"
    )
    gauge_redundancies = tuple(
        audit.fixture_id for audit in audits if audit.verdict == "pure_gauge_redundancy"
    )
    topology_residues = tuple(
        audit.fixture_id
        for audit in audits
        if audit.verdict == "fixed_accounting_sector_topology_residue_not_arrow"
    )
    h7_candidates = tuple(
        audit.fixture_id for audit in audits if audit.h7_upgrade_candidate
    )

    return T168Result(
        audits=audits,
        sector_rule_stipulations=sector_rule_stipulations,
        reservoir_absorptions=reservoir_absorptions,
        gauge_redundancies=gauge_redundancies,
        fixed_accounting_topology_residues=topology_residues,
        h7_arrow_candidates=h7_candidates,
        no_sector_fixture_clears_h7=not h7_candidates,
        strongest_claim=(
            "Exact sector or gauge restrictions do not currently reopen H7. "
            "In the finite audit, deletion impossibility is absorbed by a "
            "declared operation-class ban, conserved-quantity reservoir "
            "accounting, pure gauge redundancy, exact ideal-sector stipulation, "
            "or finite control/enforcement data. The only matched-accounting "
            "split is again future-operation topology residue, not physical-"
            "arrow evidence."
        ),
        improved=(
            "T168 converts the T160 sector/gauge null family into an executable "
            "screen. Future proposals must say whether the alleged deletion "
            "obstruction is gauge-invariant, finite-operational, and still "
            "present after compensating reservoirs and allowed controls are "
            "included."
        ),
        weakened=(
            "This weakens any H7 route that points at superselection, exact "
            "symmetry, gauge redundancy, or sector conservation as automatic "
            "record finality. Those structures may constrain operations, but "
            "they do not by themselves supply a matched-accounting physical "
            "deletion arrow."
        ),
        falsification_condition=(
            "T168 fails in H7's favor only if a finite, physically typed sector "
            "or gauge substrate supplies a gauge-invariant record-deletion task "
            "whose absorber vector is matched, whose compensating reservoirs "
            "and allowed controls are explicit, and whose physical deletion "
            "reverse remains constructor-impossible after full accounting."
        ),
        h7_update=(
            "Add T168 to H7: exact sector and gauge restriction proposals are "
            "null by default. They reopen H7 only with a finite operational "
            "substrate, a gauge-invariant deletion distinction, matched "
            "conserved-quantity/reservoir/control data, and a deletion reverse "
            "that remains constructor-impossible after that accounting."
        ),
        claim_ledger_update=(
            "T168 grounds the T160 superselection/gauge screen. Sector-rule "
            "bans, compensating-reservoir changes, gauge relabelings, exact "
            "ideal locks, and finite enforcement/control differences do not "
            "clear H7; the remaining matched topology split is capability "
            "residue rather than arrow evidence."
        ),
        open_blocker=(
            "No finite sector or gauge fixture in the current audit yields a "
            "gauge-invariant, matched-accounting, constructor-impossible "
            "physical_record_deletion reverse."
        ),
        suggested_next=(
            "Do not spend more H7 effort on generic superselection or gauge "
            "language. The remaining ungrounded T160 family is horizon/access; "
            "screen it as non-deletion unless a proposal names actual physical "
            "record destruction rather than reachability loss."
        ),
        not_claimed=(
            "T168 is not a theorem of gauge theory, not a claim that exact "
            "superselection rules are false, and not a physical model of charge "
            "dynamics. It is a finite H7 audit gate for avoiding false deletion "
            "residue."
        ),
    )


def t168_result_to_dict(result: T168Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "fixture_id": audit.fixture_id,
                "source": audit.source,
                "reverse_edge_class": audit.reverse_edge_class,
                "absorber_vector_matched": audit.absorber_vector_matched,
                "absorber_mismatch_fields": list(audit.absorber_mismatch_fields),
                "finite_operational_substrate": audit.finite_operational_substrate,
                "gauge_invariant_difference": audit.gauge_invariant_difference,
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
        "sector_rule_stipulations": list(result.sector_rule_stipulations),
        "reservoir_absorptions": list(result.reservoir_absorptions),
        "gauge_redundancies": list(result.gauge_redundancies),
        "fixed_accounting_topology_residues": list(
            result.fixed_accounting_topology_residues
        ),
        "h7_arrow_candidates": list(result.h7_arrow_candidates),
        "no_sector_fixture_clears_h7": result.no_sector_fixture_clears_h7,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _verdict(
    fixture: SectorFixture,
    mismatches: tuple[str, ...],
    absorber_matched: bool,
    candidate: bool,
) -> str:
    if fixture.reverse_edge_class != "physical_record_deletion":
        return "pure_gauge_redundancy"
    if not fixture.gauge_invariant_difference:
        return "pure_gauge_redundancy"
    if candidate:
        return "h7_physical_arrow_candidate"
    if not fixture.finite_operational_substrate:
        return "absorbed_by_exact_sector_idealization"
    if {
        "conserved_quantity_bookkeeping",
        "compensating_reservoir_state",
        "sink_delta",
    } & set(mismatches):
        return "absorbed_by_conserved_quantity_or_reservoir_accounting"
    if {
        "sector_enforcement",
        "reversible_control",
        "allowed_control_class",
    } & set(mismatches):
        return "absorbed_by_finite_control_or_enforcement_accounting"
    if (
        absorber_matched
        and fixture.reverse_status == "operation_forbidden_by_declared_sector_rule"
    ):
        return "sector_rule_stipulation_not_arrow"
    if absorber_matched and fixture.left_future_available != fixture.right_future_available:
        return "fixed_accounting_sector_topology_residue_not_arrow"
    return "fixed_accounting_no_arrow_residue"


def _interpretation(fixture: SectorFixture, verdict: str) -> str:
    if verdict == "sector_rule_stipulation_not_arrow":
        return (
            f"{fixture.fixture_id} forbids deletion by the declared operation "
            f"class: {fixture.physical_reading}"
        )
    if verdict == "absorbed_by_conserved_quantity_or_reservoir_accounting":
        return (
            f"{fixture.fixture_id} is conserved-quantity or reservoir accounting: "
            f"{fixture.physical_reading}"
        )
    if verdict == "pure_gauge_redundancy":
        return (
            f"{fixture.fixture_id} has no gauge-invariant deletion distinction: "
            f"{fixture.physical_reading}"
        )
    if verdict == "absorbed_by_exact_sector_idealization":
        return (
            f"{fixture.fixture_id} relies on an exact ideal sector restriction: "
            f"{fixture.physical_reading}"
        )
    if verdict == "absorbed_by_finite_control_or_enforcement_accounting":
        return (
            f"{fixture.fixture_id} is finite control/enforcement accounting: "
            f"{fixture.physical_reading}"
        )
    if verdict == "fixed_accounting_sector_topology_residue_not_arrow":
        return (
            f"{fixture.fixture_id} preserves a future-operation split under "
            "matched sector accounting, but deletion remains possible under the "
            "declared finite controls. Treat it as topology residue, not H7 "
            "arrow evidence."
        )
    if verdict == "h7_physical_arrow_candidate":
        return (
            f"{fixture.fixture_id} would reopen H7 because finite-sector "
            "deletion remains impossible after full accounting."
        )
    return f"{fixture.fixture_id} has no H7 arrow residue after sector accounting."


if __name__ == "__main__":
    import json

    print(json.dumps(t168_result_to_dict(run_t168_analysis()), indent=2))
