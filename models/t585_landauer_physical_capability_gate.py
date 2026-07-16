"""T585: Landauer one-bit memory physical capability gate.

This gate instantiates the T583/T584 capability contract in one small known
physical system: a one-bit memory coupled to a thermal bath and work store.
The operation cost is induced from the Landauer erasure lower bound in
normalized kBT ln 2 units. The result is a physical capability fixture, not a
time, issuance, or claim-ledger result.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any

from models import t583_capability_contract_v1 as t583


ARTIFACT = "T585-landauer-physical-capability-gate-v0.1"
VERDICT = "LANDAUER_PHYSICAL_CAPABILITY_INSTANTIATES_QUOTIENT_REVIEW_ONLY"
K_BOLTZMANN = 1.380649e-23
REFERENCE_TEMPERATURE_K = 300.0
LANDAUER_JOULE = K_BOLTZMANN * REFERENCE_TEMPERATURE_K * math.log(2.0)


@dataclass(frozen=True)
class MemoryState:
    state_id: str
    p_one: float
    stable_record: bool
    encoding: str
    display_label: str
    sensor_serial: str


@dataclass(frozen=True)
class PhysicalCapabilityAudit:
    audit_id: str
    relation: str
    passed: bool
    completion_class: str
    reason: str


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class T585Result:
    artifact: str
    source_contract: str
    source_system: str
    source_law: str
    landauer_costs: dict[str, float]
    contexts: tuple[t583.CapabilityContext, ...]
    envelopes: tuple[t583.CapabilityEnvelope, ...]
    audits: tuple[PhysicalCapabilityAudit, ...]
    assessments: tuple[t583.PairAssessment, ...]
    checks: tuple[Check, ...]
    physical_result: str
    verdict: str
    claim_ledger_update: str
    not_claimed: str
    next_work: str


def binary_entropy_bits(p: float) -> float:
    if p < 0.0 or p > 1.0:
        raise ValueError("probability must lie in [0, 1]")
    if p in (0.0, 1.0):
        return 0.0
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def landauer_work_units(state: MemoryState) -> float:
    """Minimum reset work in normalized kBT ln 2 units."""
    return round(binary_entropy_bits(state.p_one), 9)


def units_to_joules(units: float) -> float:
    return units * LANDAUER_JOULE


def joules_to_units(joules: float) -> float:
    return joules / LANDAUER_JOULE


def projected_metadata(
    state: MemoryState, context: t583.CapabilityContext
) -> dict[str, Any]:
    metadata = {
        "entropy_bits": landauer_work_units(state),
        "encoding": state.encoding,
        "record_stable": state.stable_record,
        "display_label": state.display_label,
        "sensor_serial": state.sensor_serial,
        "coordinate_name": f"{state.display_label}_coordinate",
    }
    return t583.project_irrelevant_metadata(metadata, context)


def envelope_for(
    *,
    context: t583.CapabilityContext,
    state: MemoryState,
    state_id: str | None = None,
    observer_mode: str = "state_aware",
    representation: str = "normalized",
) -> t583.CapabilityEnvelope:
    return t583.attainable_envelope(
        context=context,
        state_id=state_id or state.state_id,
        candidates=_points_for_state(
            context=context,
            state=state,
            observer_mode=observer_mode,
            representation=representation,
        ),
    )


def run_t585_analysis() -> T585Result:
    base = _base_context()
    blind = replace(
        base,
        context_id="ctx_blind_distribution_access",
        access_profile=("record_readout", "thermal_bath_temperature", "work_store"),
        access_provenance="record_distribution_not_accessible",
    )
    low_budget = replace(
        base,
        context_id="ctx_low_work_budget",
        resource_provenance="same_bath_low_work_store",
        budget=replace(base.budget, energy=0.30),
    )
    known = MemoryState("known_zero_record", 0.0, True, "canonical", "zero", "S-A")
    biased = MemoryState("biased_record", 0.10, True, "canonical", "biased", "S-B")
    unknown = MemoryState("max_entropy_record", 0.50, True, "canonical", "unknown", "S-C")
    swapped = MemoryState(
        "biased_record_bit_label_swapped",
        0.90,
        True,
        "bit_label_swapped",
        "biased-swapped",
        "S-D",
    )
    coarse = replace(biased, display_label="coarse", sensor_serial="S-Z")

    known_envelope = envelope_for(context=base, state=known)
    biased_envelope = envelope_for(context=base, state=biased)
    unknown_envelope = envelope_for(context=base, state=unknown)
    biased_joule_envelope = envelope_for(
        context=replace(base, context_id="ctx_joule_representation"),
        state=biased,
        state_id="biased_record_joule_representation",
        representation="joule",
    )
    swapped_envelope = envelope_for(
        context=replace(base, context_id="ctx_bit_label_swapped"),
        state=swapped,
    )
    blind_known_envelope = envelope_for(
        context=blind,
        state=known,
        state_id="known_zero_blind_distribution",
        observer_mode="blind_worst_case",
    )
    low_budget_biased_envelope = envelope_for(
        context=low_budget,
        state=biased,
        state_id="biased_low_work_budget",
    )

    known_unknown_relation = t583.compare_envelopes(known_envelope, unknown_envelope)
    unit_relation = t583.compare_envelopes(biased_envelope, biased_joule_envelope)
    gauge_relation = t583.compare_envelopes(biased_envelope, swapped_envelope)
    coarse_stable = projected_metadata(biased, base) == projected_metadata(coarse, base)

    access = t583.assess_pair(
        pair_id="blind_distribution_access_control",
        left_context=base,
        right_context=blind,
        left_envelope=known_envelope,
        right_envelope=blind_known_envelope,
        evidence=t583.PairEvidence(source_law_present=True),
    )
    resource = t583.assess_pair(
        pair_id="low_work_store_budget_control",
        left_context=base,
        right_context=low_budget,
        left_envelope=biased_envelope,
        right_envelope=low_budget_biased_envelope,
        evidence=t583.PairEvidence(source_law_present=True),
    )
    hidden_state = t583.assess_pair(
        pair_id="same_display_hidden_entropy_completion",
        left_context=base,
        right_context=base,
        left_envelope=known_envelope,
        right_envelope=unknown_envelope,
        evidence=t583.PairEvidence(
            native_state_completion_available=True,
            source_law_present=True,
        ),
    )
    costs = {
        "known_zero_record": landauer_work_units(known),
        "biased_record": landauer_work_units(biased),
        "max_entropy_record": landauer_work_units(unknown),
        "biased_record_bit_label_swapped": landauer_work_units(swapped),
    }
    audits = (
        PhysicalCapabilityAudit(
            "source_law_capability_distinction",
            known_unknown_relation,
            known_unknown_relation == "SUPERSET",
            "SOURCE_STATE_INDUCED_PHYSICAL_CAPABILITY_DELTA",
            "A low-entropy memory can erase inside the fixed work budget while a max-entropy memory cannot.",
        ),
        PhysicalCapabilityAudit(
            "joule_unit_representation",
            unit_relation,
            unit_relation == "EQUIVALENT",
            "RENAMING_OR_REPRESENTATION_EQUIVALENCE",
            "Joule costs at the reference temperature normalize back to the same kBT ln 2 units.",
        ),
        PhysicalCapabilityAudit(
            "bit_label_gauge_swap",
            gauge_relation,
            gauge_relation == "EQUIVALENT",
            "RENAMING_OR_GAUGE_EQUIVALENCE",
            "Swapping bit labels changes p_one to 1-p_one but preserves entropy and the native envelope.",
        ),
        PhysicalCapabilityAudit(
            "irrelevant_metadata_coarse_graining",
            "EQUIVALENT" if coarse_stable else "CHANGED",
            coarse_stable,
            "IRRELEVANT_COARSE_GRAINING",
            "Display and sensor fields drop while entropy, encoding, and record stability remain fixed.",
        ),
        PhysicalCapabilityAudit(
            "blind_distribution_access_control",
            access.capability_relation,
            access.verdict == "ACCESS_COMPLETION",
            access.completion_class,
            "Removing distribution access forces a worst-case reset accounting and is classified as access completion.",
        ),
        PhysicalCapabilityAudit(
            "low_work_store_budget_control",
            resource.capability_relation,
            resource.verdict == "RESOURCE_BUDGET_COMPLETION",
            resource.completion_class,
            "Changing the work budget removes feasible erasure and is classified as resource/budget completion.",
        ),
        PhysicalCapabilityAudit(
            "same_display_hidden_entropy_completion",
            hidden_state.capability_relation,
            hidden_state.verdict == "NATIVE_STATE_COMPLETION",
            hidden_state.completion_class,
            "Same display label with different source entropy is absorbed by native thermodynamic state completion.",
        ),
    )
    checks = (
        Check(
            "landauer_costs_ordered",
            costs["known_zero_record"] == 0.0
            and 0.0 < costs["biased_record"] < 1.0
            and costs["max_entropy_record"] == 1.0,
            "The source law separates known, biased, and max-entropy one-bit memories.",
        ),
        Check(
            "physical_capability_nontrivial",
            known_unknown_relation == "SUPERSET"
            and _has_task(known_envelope, "erase_to_standard_record")
            and not _has_task(unknown_envelope, "erase_to_standard_record"),
            "Under the fixed work budget, erasure is feasible for the known record but not for the max-entropy record.",
        ),
        Check(
            "unit_representation_invariant",
            unit_relation == "EQUIVALENT",
            "Changing from normalized units to joules and back preserves the capability envelope.",
        ),
        Check(
            "bit_label_gauge_invariant",
            gauge_relation == "EQUIVALENT",
            "The bit-label gauge swap preserves the entropy-derived capability envelope.",
        ),
        Check(
            "irrelevant_coarse_graining_invariant",
            coarse_stable,
            "Display and sensor fields declared irrelevant do not alter the physical payload.",
        ),
        Check(
            "access_control_absorbed",
            access.verdict == "ACCESS_COMPLETION",
            "Loss of distribution access is not counted as intrinsic capability change.",
        ),
        Check(
            "resource_budget_control_absorbed",
            resource.verdict == "RESOURCE_BUDGET_COMPLETION",
            "A changed work budget is not counted as intrinsic capability change.",
        ),
        Check(
            "hidden_state_completion_absorbed",
            hidden_state.verdict == "NATIVE_STATE_COMPLETION",
            "Hidden entropy differences are handled as native source-state completion.",
        ),
    )
    verdict = VERDICT if all(check.passed for check in checks) else "T585_GATE_FAILED"
    return T585Result(
        artifact=ARTIFACT,
        source_contract="T583 CapabilityContract v1 plus T584 invariance quotient",
        source_system="one_bit_memory_erasure_with_thermal_bath_and_work_store",
        source_law=(
            "Minimum reset work is represented in normalized kBT ln 2 units as "
            "the binary entropy of the one-bit memory state."
        ),
        landauer_costs=costs,
        contexts=(base, blind, low_budget),
        envelopes=(
            known_envelope,
            biased_envelope,
            unknown_envelope,
            biased_joule_envelope,
            swapped_envelope,
            blind_known_envelope,
            low_budget_biased_envelope,
        ),
        audits=audits,
        assessments=(access, resource, hidden_state),
        checks=checks,
        physical_result=(
            "The surviving capability quotient has a concrete physical "
            "instantiation: a fixed work budget distinguishes erasure capability "
            "for known, biased, and max-entropy one-bit memory states while "
            "remaining invariant under unit representation, bit-label gauge, "
            "and declared irrelevant metadata."
        ),
        verdict=verdict,
        claim_ledger_update="No claim-ledger or Canon Index update is earned.",
        not_claimed=(
            "T585 does not derive time, temporal order, issuance, a universal "
            "capability measure, a new thermodynamic theorem, a source law beyond "
            "the declared Landauer-style input, public posture, publication, "
            "TAF3, TAF8, S1, or cross-repo truth."
        ),
        next_work=(
            "Use the physical capability model only as a source-owned input for "
            "the next burden: test whether record-dependent capability change "
            "can define a noncircular order rather than restating background "
            "time, entropy, access, or resources."
        ),
    )


def _base_context() -> t583.CapabilityContext:
    return t583.CapabilityContext(
        context_id="ctx_landauer_memory",
        source_theory="one_bit_memory_landauer_erasure",
        region_id="R_memory_cell",
        observer_id="O_local_controller",
        access_profile=(
            "memory_record_distribution",
            "record_readout",
            "thermal_bath_temperature",
            "work_store",
        ),
        access_provenance="declared_local_lab_memory_access",
        task_family=("erase_to_standard_record", "certify_record_stability"),
        operation_menu=("landauer_reset", "stability_readout"),
        menu_provenance="law_derived_landauer_bound",
        resource_provenance="fixed_thermal_bath_and_work_store",
        budget=t583.Budget(
            energy=0.75,
            time=5.0,
            communication=1.0,
            memory=1.0,
            error=0.01,
        ),
        horizon="single_reset_cycle",
        physical_equivalence="unit_representation_and_bit_label_swap",
        gauge_quotient="logical_bit_label_swap",
        native_comparison="task_indexed_pareto_cover",
        irrelevant_coarse_graining_fields=(
            "display_label",
            "sensor_serial",
            "coordinate_name",
        ),
    )


def _points_for_state(
    *,
    context: t583.CapabilityContext,
    state: MemoryState,
    observer_mode: str,
    representation: str,
) -> tuple[t583.PerformancePoint, ...]:
    reset_units = (
        1.0 if observer_mode == "blind_worst_case" else landauer_work_units(state)
    )
    if representation == "joule":
        reset_units = round(joules_to_units(units_to_joules(reset_units)), 9)
    elif representation != "normalized":
        raise ValueError(f"unknown representation: {representation}")
    points = [
        t583.PerformancePoint(
            "erase_to_standard_record",
            success=0.999,
            energy_cost=reset_units,
            time_cost=1.0 + reset_units,
            communication_cost=0.0,
            memory_cost=0.1,
            error=0.001,
            protocol_id="landauer_reset",
        )
    ]
    if state.stable_record:
        points.append(
            t583.PerformancePoint(
                "certify_record_stability",
                success=0.995,
                energy_cost=0.05,
                time_cost=0.2,
                communication_cost=0.1,
                memory_cost=0.1,
                error=0.002,
                protocol_id="stability_readout",
            )
        )
    return tuple(points)


def _has_task(envelope: t583.CapabilityEnvelope, task_id: str) -> bool:
    return any(point.task_id == task_id for point in envelope.points)


def _envelope_summary(envelope: t583.CapabilityEnvelope) -> dict[str, Any]:
    return {
        "context_id": envelope.context_id,
        "state_id": envelope.state_id,
        "native_structure": envelope.native_structure,
        "points": [asdict(point) for point in envelope.points],
    }


def result_to_dict(result: T585Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_contract": result.source_contract,
        "source_system": result.source_system,
        "source_law": result.source_law,
        "landauer_costs": result.landauer_costs,
        "contexts": [asdict(item) for item in result.contexts],
        "envelopes": [_envelope_summary(item) for item in result.envelopes],
        "audits": [asdict(item) for item in result.audits],
        "assessments": [asdict(item) for item in result.assessments],
        "checks": [asdict(item) for item in result.checks],
        "physical_result": result.physical_result,
        "verdict": result.verdict,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
        "next_work": result.next_work,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T585 Results: Landauer Physical Capability Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source contract: {payload['source_contract']}",
        f"- Source system: `{payload['source_system']}`",
        "",
        "## Source Law",
        "",
        payload["source_law"],
        "",
        "| state | reset work in kBT ln 2 units |",
        "| --- | ---: |",
    ]
    for state_id, cost in payload["landauer_costs"].items():
        lines.append(f"| `{state_id}` | {cost} |")
    lines.extend(
        [
            "",
            "## Audits",
            "",
            "| audit | relation | passed? | completion class | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for item in payload["audits"]:
        lines.append(
            f"| `{item['audit_id']}` | `{item['relation']}` | "
            f"{item['passed']} | `{item['completion_class']}` | "
            f"{item['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Checks",
            "",
            "| check | passed? | reason |",
            "| --- | :---: | --- |",
        ]
    )
    for item in payload["checks"]:
        lines.append(f"| `{item['check_id']}` | {item['passed']} | {item['reason']} |")
    lines.extend(
        [
            "",
            "## Physical Result",
            "",
            payload["physical_result"],
            "",
            "## Claim Status",
            "",
            payload["claim_ledger_update"],
            "",
            "## Not Claimed",
            "",
            payload["not_claimed"],
            "",
            "## Next Work",
            "",
            payload["next_work"],
            "",
        ]
    )
    return "\n".join(lines)


def write_results(result: T585Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = result_to_dict(result)
    (results_dir / f"{ARTIFACT}.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (results_dir / f"{ARTIFACT}-results.md").write_text(
        render_markdown(payload), encoding="utf-8"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)
    result = run_t585_analysis()
    if args.write_results:
        write_results(result)
    print(json.dumps(result_to_dict(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
