"""T584: finite invariance morphism gate for CapabilityContract v1.

This gate lifts T583 from label controls to declared morphism classes. It
tests whether the task-indexed capability envelope factors through admissible
representation, gauge, and irrelevant-coarse-graining quotients, while catching
the smallest task-vocabulary merge counterexample as inadmissible.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any

from models import t583_capability_contract_v1 as t583


ARTIFACT = "T584-capability-invariance-morphism-gate-v0.1"
VERDICT = "CAPABILITY_INVARIANCE_MORPHISMS_SURVIVE_FINITE_GATE_REVIEW_ONLY"


@dataclass(frozen=True)
class RawPoint:
    raw_task: str
    success_percent: float
    energy_value: float
    energy_unit: str
    time_value: float
    time_unit: str
    communication_value: float
    communication_unit: str
    memory_value: float
    memory_unit: str
    error_ppm: float
    protocol_label: str
    implementation_trace: str
    gauge_phase_turns: float
    metadata: dict[str, str]


@dataclass(frozen=True)
class MorphismSpec:
    morphism_id: str
    kind: str
    admissible: bool
    task_aliases: dict[str, str]
    drop_metadata_fields: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class MorphismAudit:
    morphism_id: str
    kind: str
    admissible: bool
    relation: str
    invariant_or_caught: bool
    substantive_change: str
    reason: str


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class T584Result:
    artifact: str
    source_contract: str
    audits: tuple[MorphismAudit, ...]
    checks: tuple[Check, ...]
    survivor_statement: str
    counterexample_statement: str
    verdict: str
    claim_ledger_update: str
    not_claimed: str
    next_work: str


UNIT_FACTORS = {
    "J": 1.0,
    "mJ": 0.001,
    "s": 1.0,
    "ms": 0.001,
    "message": 1.0,
    "packet": 1.0,
    "cell": 1.0,
    "KiB": 1.0,
}


def raw_to_point(raw: RawPoint, spec: MorphismSpec) -> t583.PerformancePoint:
    """Canonicalize one raw implementation record into the T583 envelope type."""
    task_id = spec.task_aliases.get(raw.raw_task, raw.raw_task)
    return t583.PerformancePoint(
        task_id=task_id,
        success=raw.success_percent / 100.0,
        energy_cost=raw.energy_value * UNIT_FACTORS[raw.energy_unit],
        time_cost=raw.time_value * UNIT_FACTORS[raw.time_unit],
        communication_cost=raw.communication_value
        * UNIT_FACTORS[raw.communication_unit],
        memory_cost=raw.memory_value * UNIT_FACTORS[raw.memory_unit],
        error=raw.error_ppm / 1_000_000.0,
        protocol_id=raw.protocol_label,
    )


def projected_metadata(raw: RawPoint, spec: MorphismSpec) -> dict[str, str]:
    return {
        key: value
        for key, value in raw.metadata.items()
        if key not in spec.drop_metadata_fields
    }


def envelope_for(
    *,
    context: t583.CapabilityContext,
    state_id: str,
    raws: tuple[RawPoint, ...],
    spec: MorphismSpec,
) -> t583.CapabilityEnvelope:
    points = tuple(raw_to_point(raw, spec) for raw in raws)
    return t583.attainable_envelope(
        context=context,
        state_id=state_id,
        candidates=points,
    )


def audit_morphism(
    *,
    baseline: t583.CapabilityEnvelope,
    transformed: t583.CapabilityEnvelope,
    spec: MorphismSpec,
    substantive_change: str,
) -> MorphismAudit:
    relation = t583.compare_envelopes(baseline, transformed)
    if spec.admissible:
        ok = relation == "EQUIVALENT"
        reason = (
            "Admissible physical-equivalence morphism preserves the native envelope."
            if ok
            else "Admissible morphism changed the envelope, so invariance fails."
        )
    else:
        ok = relation != "EQUIVALENT"
        reason = (
            "Non-equivalence exposes the proposed morphism as inadmissible."
            if ok
            else "The counterexample collapsed without detecting a boundary."
        )
    return MorphismAudit(
        morphism_id=spec.morphism_id,
        kind=spec.kind,
        admissible=spec.admissible,
        relation=relation,
        invariant_or_caught=ok,
        substantive_change=substantive_change,
        reason=reason,
    )


def run_t584_analysis() -> T584Result:
    context = t583._base_context()
    base_spec = MorphismSpec(
        morphism_id="identity",
        kind="identity",
        admissible=True,
        task_aliases={},
        drop_metadata_fields=("display_label", "coordinate_name", "telemetry_bin"),
        reason="Reference representation.",
    )
    unit_representation = MorphismSpec(
        morphism_id="unit_and_interface_representation",
        kind="representation",
        admissible=True,
        task_aliases={"rr": "recover_record", "cr": "certify_record"},
        drop_metadata_fields=("display_label", "coordinate_name", "telemetry_bin"),
        reason="Changes units, raw task interface, protocol labels, and traces only.",
    )
    gauge_shift = MorphismSpec(
        morphism_id="gauge_orbit_phase_shift",
        kind="gauge",
        admissible=True,
        task_aliases={"rr": "recover_record", "cr": "certify_record"},
        drop_metadata_fields=("display_label", "coordinate_name", "telemetry_bin"),
        reason="Moves within the declared gauge orbit without changing observables.",
    )
    coarse = MorphismSpec(
        morphism_id="telemetry_coarse_graining",
        kind="irrelevant_coarse_graining",
        admissible=True,
        task_aliases={},
        drop_metadata_fields=("display_label", "coordinate_name", "telemetry_bin"),
        reason="Drops fields declared irrelevant before comparison.",
    )
    bad_merge = MorphismSpec(
        morphism_id="task_vocabulary_merge_counterexample",
        kind="inadmissible_task_coarse_graining",
        admissible=False,
        task_aliases={"certify_record": "recover_record"},
        drop_metadata_fields=("display_label", "coordinate_name", "telemetry_bin"),
        reason="Merges distinct task semantics and changes the capability type.",
    )

    baseline_raw = _baseline_raw()
    baseline = envelope_for(
        context=context,
        state_id="substantive_record_fixture",
        raws=baseline_raw,
        spec=base_spec,
    )
    represented = envelope_for(
        context=replace(
            context,
            context_id="ctx_unit_interface_representation",
            representation_label="sensor_bus_milliunit_interface",
        ),
        state_id="same_physics_sensor_bus",
        raws=_represented_raw(),
        spec=unit_representation,
    )
    gauge = envelope_for(
        context=replace(
            context,
            context_id="ctx_gauge_shift",
            gauge_representative="phase_shifted_representative",
        ),
        state_id="same_physics_gauge_shifted",
        raws=_gauge_shifted_raw(),
        spec=gauge_shift,
    )
    coarse_envelope = envelope_for(
        context=context,
        state_id="same_physics_coarse_telemetry",
        raws=_coarse_raw(),
        spec=coarse,
    )
    merged = envelope_for(
        context=context,
        state_id="bad_task_merge",
        raws=baseline_raw,
        spec=bad_merge,
    )
    distinct_equal = envelope_for(
        context=context,
        state_id="different_controller_same_envelope",
        raws=_distinct_equal_raw(),
        spec=base_spec,
    )

    audits = (
        audit_morphism(
            baseline=baseline,
            transformed=represented,
            spec=unit_representation,
            substantive_change=(
                "raw tasks, units, protocol labels, and implementation traces differ"
            ),
        ),
        audit_morphism(
            baseline=baseline,
            transformed=gauge,
            spec=gauge_shift,
            substantive_change="gauge phase and representative differ",
        ),
        audit_morphism(
            baseline=baseline,
            transformed=coarse_envelope,
            spec=coarse,
            substantive_change="telemetry and display fields are removed",
        ),
        audit_morphism(
            baseline=baseline,
            transformed=merged,
            spec=bad_merge,
            substantive_change="certification task is merged into recovery task",
        ),
    )
    metadata_stable = all(
        projected_metadata(left, coarse) == projected_metadata(right, coarse)
        for left, right in zip(baseline_raw, _coarse_raw())
    )
    distinct_relation = t583.compare_envelopes(baseline, distinct_equal)
    checks = (
        Check(
            "admissible_morphisms_preserve_capability",
            all(audit.invariant_or_caught for audit in audits if audit.admissible),
            "Representation, gauge, and irrelevant coarse-graining preserve the envelope.",
        ),
        Check(
            "substantive_representation_change",
            represented.state_id != baseline.state_id
            and audits[0].relation == "EQUIVALENT",
            "Representation changes raw units, interface names, and implementation traces.",
        ),
        Check(
            "gauge_factors_through_quotient",
            audits[1].relation == "EQUIVALENT",
            "Gauge representative and phase changes do not create new capabilities.",
        ),
        Check(
            "irrelevant_coarse_graining_stable",
            metadata_stable and audits[2].relation == "EQUIVALENT",
            "Declared irrelevant metadata drops without changing the physical payload.",
        ),
        Check(
            "task_merge_counterexample_caught",
            audits[3].invariant_or_caught and audits[3].relation != "EQUIVALENT",
            "Merging distinct task semantics changes the envelope and is rejected.",
        ),
        Check(
            "capability_not_state_identity",
            distinct_relation == "EQUIVALENT"
            and distinct_equal.state_id != baseline.state_id,
            "Different controller traces can remain capability-equivalent.",
        ),
    )
    verdict = VERDICT if all(check.passed for check in checks) else "T584_GATE_FAILED"
    return T584Result(
        artifact=ARTIFACT,
        source_contract="T583 CapabilityContract v1",
        audits=audits,
        checks=checks,
        survivor_statement=(
            "In this finite fixture, capability factors through the declared "
            "representation, gauge, and irrelevant-coarse-graining quotient."
        ),
        counterexample_statement=(
            "The smallest found counterexample is a task-vocabulary merge: "
            "certification and recovery cannot be coarse-grained into one task "
            "without changing the native capability type."
        ),
        verdict=verdict,
        claim_ledger_update="No claim-ledger or Canon Index update is earned.",
        not_claimed=(
            "T584 is a finite invariance gate only. It does not establish a "
            "universal capability measure, physical time, issuance, a source "
            "law, a genuine physical model, or cross-repo identity."
        ),
        next_work=(
            "Instantiate the surviving quotient in a genuine physical system "
            "with source-derived states, operations, resources, costs, records, "
            "access, gauge quotient, and measured or law-derived task performance."
        ),
    )


def _baseline_raw() -> tuple[RawPoint, ...]:
    return (
        RawPoint("recover_record", 90.0, 2.0, "J", 4.0, "s", 0.0, "message", 1.0, "cell", 50_000, "recover_fast", "controller_A", 0.00, {"physical_payload": "same", "display_label": "alpha", "telemetry_bin": "high"}),
        RawPoint("recover_record", 95.0, 4.0, "J", 7.0, "s", 0.0, "message", 1.0, "cell", 30_000, "recover_high", "controller_A", 0.00, {"physical_payload": "same", "display_label": "alpha", "telemetry_bin": "high"}),
        RawPoint("certify_record", 98.0, 1.0, "J", 2.0, "s", 1.0, "message", 2.0, "cell", 10_000, "certify", "controller_A", 0.00, {"physical_payload": "same", "display_label": "alpha", "telemetry_bin": "high"}),
        RawPoint("recover_record", 80.0, 3.0, "J", 5.0, "s", 0.0, "message", 2.0, "cell", 80_000, "dominated", "controller_A", 0.00, {"physical_payload": "same", "display_label": "alpha", "telemetry_bin": "high"}),
    )


def _represented_raw() -> tuple[RawPoint, ...]:
    return (
        RawPoint("rr", 90.0, 2000.0, "mJ", 4000.0, "ms", 0.0, "packet", 1.0, "KiB", 50_000, "bus_a", "controller_B_milli", 0.25, {"physical_payload": "same", "display_label": "beta", "telemetry_bin": "low"}),
        RawPoint("rr", 95.0, 4000.0, "mJ", 7000.0, "ms", 0.0, "packet", 1.0, "KiB", 30_000, "bus_b", "controller_B_milli", 0.25, {"physical_payload": "same", "display_label": "beta", "telemetry_bin": "low"}),
        RawPoint("cr", 98.0, 1000.0, "mJ", 2000.0, "ms", 1.0, "packet", 2.0, "KiB", 10_000, "bus_c", "controller_B_milli", 0.25, {"physical_payload": "same", "display_label": "beta", "telemetry_bin": "low"}),
        RawPoint("rr", 80.0, 3000.0, "mJ", 5000.0, "ms", 0.0, "packet", 2.0, "KiB", 80_000, "bus_d", "controller_B_milli", 0.25, {"physical_payload": "same", "display_label": "beta", "telemetry_bin": "low"}),
    )


def _gauge_shifted_raw() -> tuple[RawPoint, ...]:
    return tuple(
        replace(
            raw,
            raw_task="rr" if raw.raw_task == "recover_record" else "cr",
            gauge_phase_turns=raw.gauge_phase_turns + 0.5,
        )
        for raw in _baseline_raw()
    )


def _coarse_raw() -> tuple[RawPoint, ...]:
    return tuple(
        replace(
            raw,
            metadata={
                "physical_payload": "same",
                "display_label": "coarse",
                "telemetry_bin": "merged",
            },
        )
        for raw in _baseline_raw()
    )


def _distinct_equal_raw() -> tuple[RawPoint, ...]:
    return tuple(
        replace(raw, implementation_trace="controller_C_independent")
        for raw in _baseline_raw()
    )


def result_to_dict(result: T584Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_contract": result.source_contract,
        "audits": [asdict(item) for item in result.audits],
        "checks": [asdict(item) for item in result.checks],
        "survivor_statement": result.survivor_statement,
        "counterexample_statement": result.counterexample_statement,
        "verdict": result.verdict,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
        "next_work": result.next_work,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T584 Results: Capability Invariance Morphism Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source contract: {payload['source_contract']}",
        "",
        "## Morphism Audits",
        "",
        "| morphism | kind | admissible? | relation | passed? | substantive change |",
        "| --- | --- | :---: | --- | :---: | --- |",
    ]
    for item in payload["audits"]:
        lines.append(
            f"| `{item['morphism_id']}` | `{item['kind']}` | "
            f"{item['admissible']} | `{item['relation']}` | "
            f"{item['invariant_or_caught']} | {item['substantive_change']} |"
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
            "## Survivor",
            "",
            payload["survivor_statement"],
            "",
            "## Counterexample Boundary",
            "",
            payload["counterexample_statement"],
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


def write_results(result: T584Result, results_dir: Path = Path("results")) -> None:
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
    result = run_t584_analysis()
    if args.write_results:
        write_results(result)
    print(json.dumps(result_to_dict(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
