"""T142: thermodynamic calibration for H7 copy/erase survivors.

T141 showed that strict D1 increases on the T1 record graph do not have
constructor-impossible reverses. This model checks the next absorber: once
copy and branch-support reversals are calibrated against reversible uncopy
and ordinary erasure/free-energy accounting, is any independent H7 arrow left?
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log

from models.t1_record_graph_admissibility_ledger import run_t141_analysis


LANDAUER_NAT_PER_BIT = log(2.0)


@dataclass(frozen=True)
class ReverseMode:
    mode_id: str
    description: str
    erased_bits: int
    beta_work_lower_bound: float
    required_access: tuple[str, ...]
    standard_absorber: str
    verdict: str


@dataclass(frozen=True)
class T1ThermoCalibration:
    case_id: str
    before_profile: tuple[int, int, int, int]
    after_profile: tuple[int, int, int, int]
    d1_delta: tuple[int, int, int, int]
    strict_forward_increase: bool
    reverse_modes: tuple[ReverseMode, ...]
    overall_verdict: str
    reason: str


@dataclass(frozen=True)
class ResourceDrawdownCalibration:
    model_id: str
    source: str
    resource_units_drawn_down: int
    physical_unit_named: bool
    blank_memory_interpretation: str
    verdict: str
    reason: str


@dataclass(frozen=True)
class T142Result:
    t1_calibrations: tuple[T1ThermoCalibration, ...]
    resource_drawdown_calibration: ResourceDrawdownCalibration
    no_t1_strict_increase_has_independent_thermo_arrow: bool
    copy_reverses_have_zero_heat_uncopy_mode: bool
    copy_reverses_have_landauer_reset_mode: bool
    same_landauer_floor_different_d1_topology: bool
    h7_upgrade_status: str
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def landauer_bound_bits(erased_bits: int) -> float:
    """Return the dimensionless beta*W lower bound for blind bit erasure."""

    if erased_bits < 0:
        raise ValueError("erased_bits must be nonnegative")
    return erased_bits * LANDAUER_NAT_PER_BIT


def _boundary_revoke_mode() -> ReverseMode:
    return ReverseMode(
        mode_id="boundary_revoke",
        description=(
            "Reverse the D1 increase by changing observer access while leaving "
            "the physical records intact."
        ),
        erased_bits=0,
        beta_work_lower_bound=0.0,
        required_access=("access-control state",),
        standard_absorber="observer-boundary/accounting state",
        verdict="reversible_boundary_change",
    )


def _correlated_uncopy_mode() -> ReverseMode:
    return ReverseMode(
        mode_id="correlated_uncopy",
        description=(
            "Use the source-copy correlation and reversible control to uncopy "
            "the added record into a blank target rather than blindly reset it."
        ),
        erased_bits=0,
        beta_work_lower_bound=0.0,
        required_access=(
            "source record",
            "target copy",
            "copy provenance",
            "reversible control operation",
        ),
        standard_absorber="reversible computing with full correlation access",
        verdict="reversible_when_full_microstate_available",
    )


def _blind_reset_mode() -> ReverseMode:
    return ReverseMode(
        mode_id="blind_reset",
        description=(
            "Reset or overwrite the added record without using the source-copy "
            "correlation as a reversible uncopy handle."
        ),
        erased_bits=1,
        beta_work_lower_bound=landauer_bound_bits(1),
        required_access=("heat bath", "reset protocol", "blank-state target"),
        standard_absorber="Landauer-style erasure/free-energy accounting",
        verdict="standard_erasure_cost_if_uncopy_unavailable",
    )


def calibrate_t1_cases() -> tuple[T1ThermoCalibration, ...]:
    audits = {audit.case_id: audit for audit in run_t141_analysis().audits}
    calibrations: list[T1ThermoCalibration] = []

    for case_id in (
        "access_grant_existing_record",
        "copy_to_fresh_holder",
        "branch_spread_copy",
        "access_loss_without_erasure_control",
    ):
        audit = audits[case_id]
        d1_delta = tuple(
            after - before
            for before, after in zip(audit.before_profile, audit.after_profile)
        )
        if case_id == "access_grant_existing_record":
            reverse_modes = (_boundary_revoke_mode(),)
            verdict = "boundary_absorbed"
            reason = (
                "The strict D1 increase is an access-profile change. It has no "
                "thermodynamic arrow content once access-control state is part "
                "of the substrate."
            )
        elif case_id in {"copy_to_fresh_holder", "branch_spread_copy"}:
            reverse_modes = (_correlated_uncopy_mode(), _blind_reset_mode())
            verdict = "reversible_or_landauer_absorbed"
            reason = (
                "The copy-based D1 increase has two ordinary reversals: zero "
                "blind-erasure cost if full correlation/control access permits "
                "uncopy, or a one-bit erasure/free-energy ledger if the copy is "
                "blindly reset."
            )
        else:
            reverse_modes = (_boundary_revoke_mode(),)
            verdict = "non_arrow_control"
            reason = (
                "The control is not a strict forward D1 increase and therefore "
                "does not supply an arrow-bearing calibration case."
            )

        calibrations.append(
            T1ThermoCalibration(
                case_id=case_id,
                before_profile=audit.before_profile,
                after_profile=audit.after_profile,
                d1_delta=d1_delta,
                strict_forward_increase=audit.strict_forward_increase,
                reverse_modes=reverse_modes,
                overall_verdict=verdict,
                reason=reason,
            )
        )
    return tuple(calibrations)


def calibrate_resource_drawdown() -> ResourceDrawdownCalibration:
    return ResourceDrawdownCalibration(
        model_id="test_c_resource_drawdown",
        source="T128 minimal living arrow",
        resource_units_drawn_down=3,
        physical_unit_named=False,
        blank_memory_interpretation=(
            "If each unit is a blank record cell, recharge/reset is ordinary "
            "memory-preparation and erasure/free-energy accounting. If the unit "
            "is not physically typed, the finite drawdown is only an accounting "
            "token."
        ),
        verdict="not_physical_without_named_free_energy_or_capacity_unit",
        reason=(
            "The T128 survivor becomes physics-facing only after the resource "
            "unit is mapped to a real free-energy, blank-memory, fuel, sink, or "
            "capacity variable. Otherwise it is a formal drawdown coordinate."
        ),
    )


def run_t142_analysis() -> T142Result:
    calibrations = calibrate_t1_cases()
    by_id = {case.case_id: case for case in calibrations}

    strict_cases = tuple(case for case in calibrations if case.strict_forward_increase)
    no_independent_thermo_arrow = all(
        case.overall_verdict
        in {"boundary_absorbed", "reversible_or_landauer_absorbed"}
        for case in strict_cases
    )

    copy_cases = (
        by_id["copy_to_fresh_holder"],
        by_id["branch_spread_copy"],
    )
    copy_reverses_have_zero_heat_uncopy_mode = all(
        any(mode.mode_id == "correlated_uncopy" and mode.erased_bits == 0 for mode in case.reverse_modes)
        for case in copy_cases
    )
    copy_reverses_have_landauer_reset_mode = all(
        any(
            mode.mode_id == "blind_reset"
            and abs(mode.beta_work_lower_bound - LANDAUER_NAT_PER_BIT) < 1e-12
            for mode in case.reverse_modes
        )
        for case in copy_cases
    )
    same_landauer_floor_different_d1_topology = (
        _blind_reset_floor(copy_cases[0]) == _blind_reset_floor(copy_cases[1])
        and copy_cases[0].d1_delta != copy_cases[1].d1_delta
    )

    return T142Result(
        t1_calibrations=calibrations,
        resource_drawdown_calibration=calibrate_resource_drawdown(),
        no_t1_strict_increase_has_independent_thermo_arrow=no_independent_thermo_arrow,
        copy_reverses_have_zero_heat_uncopy_mode=copy_reverses_have_zero_heat_uncopy_mode,
        copy_reverses_have_landauer_reset_mode=copy_reverses_have_landauer_reset_mode,
        same_landauer_floor_different_d1_topology=same_landauer_floor_different_d1_topology,
        h7_upgrade_status="thermodynamic_absorption_not_upgrade",
        strongest_claim=(
            "The remaining H7 copy/branch-support survivors are absorbed by "
            "standard thermodynamic distinctions. With full source-copy "
            "correlation and reversible control they can be uncomputed without "
            "blind erasure; without that access, resetting the added record is "
            "ordinary erasure/free-energy accounting. D1 still distinguishes "
            "record topology at fixed erasure floor, but that does not by "
            "itself ground a physical arrow."
        ),
        improved=(
            "T142 separates three notions that were easy to conflate: D1 record "
            "topology, reversible uncopy under full microstate access, and "
            "blind erasure cost under coarse-grained reset. This makes the H7 "
            "thermodynamic absorber explicit."
        ),
        weakened=(
            "H7 cannot use T1 copy or branch-spread gains as independent "
            "thermodynamic-arrow evidence. Their reverse is either reversible "
            "with the correlation/control handle or absorbed by ordinary "
            "erasure/free-energy accounting. The T128 resource drawdown also "
            "stays formal until its resource unit is physically typed."
        ),
        falsification_condition=(
            "T142 fails in H7's favor only if a physically typed record "
            "substrate gives a strict D1 increase whose reverse remains "
            "inadmissible after full reversible-correlation access, heat-bath "
            "erasure cost, blank-capacity use, sink state, and boundary "
            "conditions are all included and matched."
        ),
        h7_update=(
            "Add T142 to H7: T1 copy/branch gains are thermodynamically "
            "absorbed, not arrow evidence. D1 topology can vary at fixed "
            "one-bit erasure floor, but reverse admissibility is still settled "
            "by reversible uncopy access or standard erasure/free-energy "
            "accounting."
        ),
        claim_ledger_update=(
            "T142 calibrates the T141/T128 survivor against thermodynamic "
            "absorbers. Access grants are boundary changes; copied records can "
            "be reversed by correlated uncopy when the full handle remains, or "
            "by ordinary one-bit erasure/free-energy accounting when blindly "
            "reset. H7 remains a resource-accounting/constructor lemma, not a "
            "thermodynamic-arrow derivation."
        ),
        open_blocker=(
            "Find a physically typed record substrate where D1 topology changes "
            "future operation availability at fixed free-energy, capacity, "
            "sink, boundary, provenance, and reversible-control data."
        ),
        suggested_next=(
            "Either demote H7's paper-facing label to resource-accounting lemma, "
            "or attempt a non-equilibrium physical model with named free-energy "
            "and capacity variables fixed before D1 scoring."
        ),
    )


def _blind_reset_floor(case: T1ThermoCalibration) -> float:
    for mode in case.reverse_modes:
        if mode.mode_id == "blind_reset":
            return mode.beta_work_lower_bound
    return -1.0


def t142_result_to_dict(result: T142Result) -> dict[str, object]:
    return {
        "t1_calibrations": [
            {
                "case_id": case.case_id,
                "before_profile": list(case.before_profile),
                "after_profile": list(case.after_profile),
                "d1_delta": list(case.d1_delta),
                "strict_forward_increase": case.strict_forward_increase,
                "reverse_modes": [
                    {
                        "mode_id": mode.mode_id,
                        "description": mode.description,
                        "erased_bits": mode.erased_bits,
                        "beta_work_lower_bound": mode.beta_work_lower_bound,
                        "required_access": list(mode.required_access),
                        "standard_absorber": mode.standard_absorber,
                        "verdict": mode.verdict,
                    }
                    for mode in case.reverse_modes
                ],
                "overall_verdict": case.overall_verdict,
                "reason": case.reason,
            }
            for case in result.t1_calibrations
        ],
        "resource_drawdown_calibration": {
            "model_id": result.resource_drawdown_calibration.model_id,
            "source": result.resource_drawdown_calibration.source,
            "resource_units_drawn_down": (
                result.resource_drawdown_calibration.resource_units_drawn_down
            ),
            "physical_unit_named": result.resource_drawdown_calibration.physical_unit_named,
            "blank_memory_interpretation": (
                result.resource_drawdown_calibration.blank_memory_interpretation
            ),
            "verdict": result.resource_drawdown_calibration.verdict,
            "reason": result.resource_drawdown_calibration.reason,
        },
        "no_t1_strict_increase_has_independent_thermo_arrow": (
            result.no_t1_strict_increase_has_independent_thermo_arrow
        ),
        "copy_reverses_have_zero_heat_uncopy_mode": (
            result.copy_reverses_have_zero_heat_uncopy_mode
        ),
        "copy_reverses_have_landauer_reset_mode": (
            result.copy_reverses_have_landauer_reset_mode
        ),
        "same_landauer_floor_different_d1_topology": (
            result.same_landauer_floor_different_d1_topology
        ),
        "h7_upgrade_status": result.h7_upgrade_status,
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

    print(json.dumps(t142_result_to_dict(run_t142_analysis()), indent=2))
