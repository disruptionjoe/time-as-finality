"""T583: executable CapabilityContract v1 review instrument.

The contract represents capability as a region-indexed, task-indexed Pareto
envelope of attainable performance and cost points under one explicit audit
context. It is not a scalar by default and it does not derive physics.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any, Iterable


ARTIFACT = "T583-capability-contract-v1-v0.1"
VERDICT = "CAPABILITY_CONTRACT_V1_IMPLEMENTED_REVIEW_ONLY"
CANDIDATE_CEILING = "CAPABILITY_DELTA_REVIEW_CANDIDATE"
W192_VERDICT = "EXPLICIT_STATE_RESOURCE_COMPLETION"


@dataclass(frozen=True)
class Budget:
    energy: float
    time: float
    communication: float
    memory: float
    error: float


@dataclass(frozen=True)
class CapabilityContext:
    context_id: str
    source_theory: str
    region_id: str
    observer_id: str
    access_profile: tuple[str, ...]
    access_provenance: str
    task_family: tuple[str, ...]
    operation_menu: tuple[str, ...]
    menu_provenance: str
    resource_provenance: str
    budget: Budget
    horizon: str
    physical_equivalence: str
    gauge_quotient: str
    native_comparison: str
    irrelevant_coarse_graining_fields: tuple[str, ...]
    representation_label: str = "canonical"
    gauge_representative: str = "canonical"

    def semantic_dict(self) -> dict[str, Any]:
        """Return the representation-independent context used for comparison."""
        payload = asdict(self)
        payload.pop("context_id")
        payload.pop("representation_label")
        payload.pop("gauge_representative")
        payload["access_profile"] = sorted(self.access_profile)
        payload["task_family"] = sorted(self.task_family)
        payload["operation_menu"] = sorted(self.operation_menu)
        payload["irrelevant_coarse_graining_fields"] = sorted(
            self.irrelevant_coarse_graining_fields
        )
        return payload


@dataclass(frozen=True)
class PerformancePoint:
    task_id: str
    success: float
    energy_cost: float
    time_cost: float
    communication_cost: float
    memory_cost: float
    error: float
    protocol_id: str

    def canonical(self, task_aliases: dict[str, str] | None = None) -> "PerformancePoint":
        aliases = task_aliases or {}
        return replace(
            self,
            task_id=aliases.get(self.task_id, self.task_id),
            success=round(self.success, 9),
            energy_cost=round(self.energy_cost, 9),
            time_cost=round(self.time_cost, 9),
            communication_cost=round(self.communication_cost, 9),
            memory_cost=round(self.memory_cost, 9),
            error=round(self.error, 9),
            protocol_id="canonical_protocol",
        )


@dataclass(frozen=True)
class CapabilityEnvelope:
    context_id: str
    state_id: str
    native_structure: str
    points: tuple[PerformancePoint, ...]


@dataclass(frozen=True)
class PairEvidence:
    visible_projection_equal: bool = True
    explicit_state_resource_changed: bool = False
    fixed_source_null_reproduces: bool = False
    native_state_completion_available: bool = False
    physical_boundary_forced: bool = False
    source_law_present: bool = False
    completion_nonadmissibility_proved: bool = False
    independent_holdout: bool = False
    evidence_origin: str = "finite_control"


@dataclass(frozen=True)
class PairAssessment:
    pair_id: str
    capability_relation: str
    context_differences: tuple[str, ...]
    completion_class: str
    verdict: str
    positive_capability_verdict_allowed: bool
    reason: str


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class T583Result:
    artifact: str
    contract_status: str
    capability_definition: dict[str, Any]
    null_completion_classes: tuple[str, ...]
    contexts: tuple[CapabilityContext, ...]
    envelopes: tuple[CapabilityEnvelope, ...]
    assessments: tuple[PairAssessment, ...]
    checks: tuple[Check, ...]
    w192_verdict: str
    synthetic_candidate_ceiling: str
    verdict: str
    claim_ledger_update: str
    not_claimed: str


def point_is_feasible(point: PerformancePoint, budget: Budget) -> bool:
    return (
        point.energy_cost <= budget.energy
        and point.time_cost <= budget.time
        and point.communication_cost <= budget.communication
        and point.memory_cost <= budget.memory
        and point.error <= budget.error
    )


def point_covers(left: PerformancePoint, right: PerformancePoint) -> bool:
    """Return whether left is at least as capable as right for one task."""
    return (
        left.task_id == right.task_id
        and left.success >= right.success
        and left.energy_cost <= right.energy_cost
        and left.time_cost <= right.time_cost
        and left.communication_cost <= right.communication_cost
        and left.memory_cost <= right.memory_cost
        and left.error <= right.error
    )


def point_strictly_dominates(left: PerformancePoint, right: PerformancePoint) -> bool:
    if not point_covers(left, right):
        return False
    return left != right


def attainable_envelope(
    *,
    context: CapabilityContext,
    state_id: str,
    candidates: Iterable[PerformancePoint],
    task_aliases: dict[str, str] | None = None,
) -> CapabilityEnvelope:
    canonical = [point.canonical(task_aliases) for point in candidates]
    admissible = [
        point
        for point in canonical
        if point.task_id in context.task_family and point_is_feasible(point, context.budget)
    ]
    frontier = [
        point
        for point in admissible
        if not any(
            point_strictly_dominates(other, point)
            for other in admissible
            if other is not point
        )
    ]
    frontier.sort(
        key=lambda point: (
            point.task_id,
            -point.success,
            point.energy_cost,
            point.time_cost,
            point.communication_cost,
            point.memory_cost,
            point.error,
        )
    )
    return CapabilityEnvelope(
        context_id=context.context_id,
        state_id=state_id,
        native_structure="task_indexed_pareto_preorder",
        points=tuple(frontier),
    )


def envelope_covers(left: CapabilityEnvelope, right: CapabilityEnvelope) -> bool:
    return all(any(point_covers(a, b) for a in left.points) for b in right.points)


def compare_envelopes(left: CapabilityEnvelope, right: CapabilityEnvelope) -> str:
    left_covers = envelope_covers(left, right)
    right_covers = envelope_covers(right, left)
    if left_covers and right_covers:
        return "EQUIVALENT"
    if left_covers:
        return "SUPERSET"
    if right_covers:
        return "SUBSET"
    return "INCOMPARABLE"


def context_differences(
    left: CapabilityContext, right: CapabilityContext
) -> tuple[str, ...]:
    differences: list[str] = []
    if sorted(left.access_profile) != sorted(right.access_profile):
        differences.append("access_profile")
    if left.access_provenance != right.access_provenance:
        differences.append("access_provenance")
    if sorted(left.task_family) != sorted(right.task_family):
        differences.append("task_family")
    if sorted(left.operation_menu) != sorted(right.operation_menu):
        differences.append("operation_menu")
    if left.menu_provenance != right.menu_provenance:
        differences.append("menu_provenance")
    if left.resource_provenance != right.resource_provenance:
        differences.append("resource_provenance")
    if left.budget != right.budget:
        differences.append("cost_error_budget")
    if left.horizon != right.horizon:
        differences.append("horizon")
    if left.physical_equivalence != right.physical_equivalence:
        differences.append("physical_equivalence")
    if left.gauge_quotient != right.gauge_quotient:
        differences.append("gauge_quotient")
    if left.native_comparison != right.native_comparison:
        differences.append("native_comparison")
    return tuple(differences)


def assess_pair(
    *,
    pair_id: str,
    left_context: CapabilityContext,
    right_context: CapabilityContext,
    left_envelope: CapabilityEnvelope,
    right_envelope: CapabilityEnvelope,
    evidence: PairEvidence,
) -> PairAssessment:
    relation = compare_envelopes(left_envelope, right_envelope)
    differences = context_differences(left_context, right_context)
    if relation == "EQUIVALENT":
        return PairAssessment(
            pair_id,
            relation,
            differences,
            "NO_CAPABILITY_DELTA",
            "PRESERVATION_CONTROL_PASS",
            False,
            "The native task-performance-cost envelopes are equivalent.",
        )
    if evidence.explicit_state_resource_changed:
        return PairAssessment(
            pair_id,
            relation,
            differences,
            W192_VERDICT,
            W192_VERDICT,
            False,
            "The capability delta is decided by explicit state or resource access.",
        )
    if "task_family" in differences:
        completion = "TASK_REDEFINITION_COMPLETION"
    elif "operation_menu" in differences or "menu_provenance" in differences:
        completion = "MENU_COMPLETION"
    elif "access_profile" in differences or "access_provenance" in differences:
        completion = "ACCESS_COMPLETION"
    elif (
        "resource_provenance" in differences
        or "cost_error_budget" in differences
        or "horizon" in differences
    ):
        completion = "RESOURCE_BUDGET_COMPLETION"
    elif evidence.fixed_source_null_reproduces:
        completion = "FIXED_SOURCE_COMPLETION"
    elif evidence.native_state_completion_available:
        completion = "NATIVE_STATE_COMPLETION"
    else:
        completion = "NO_ADMITTED_COMPLETION_FOUND_IN_DECLARED_SCOPE"
    if completion != "NO_ADMITTED_COMPLETION_FOUND_IN_DECLARED_SCOPE":
        return PairAssessment(
            pair_id,
            relation,
            differences,
            completion,
            completion,
            False,
            "A named completion or context difference reproduces the capability delta.",
        )
    review_ready = all(
        (
            evidence.visible_projection_equal,
            evidence.physical_boundary_forced,
            evidence.source_law_present,
            evidence.completion_nonadmissibility_proved,
            evidence.independent_holdout,
        )
    )
    return PairAssessment(
        pair_id,
        relation,
        differences,
        completion,
        CANDIDATE_CEILING if review_ready else "CAPABILITY_DELTA_INCOMPLETE_REVIEW",
        False,
        "A synthetic or finite contract pass cannot establish a physical capability theorem.",
    )


def project_irrelevant_metadata(
    metadata: dict[str, Any], context: CapabilityContext
) -> dict[str, Any]:
    return {
        key: value
        for key, value in metadata.items()
        if key not in context.irrelevant_coarse_graining_fields
    }


def run_t583_analysis() -> T583Result:
    base = _base_context()
    renamed = replace(
        base,
        context_id="ctx_renamed_gauge",
        representation_label="renamed_coordinates",
        gauge_representative="gauge_rep_b",
    )
    low_budget = replace(
        base,
        context_id="ctx_low_budget",
        resource_provenance="declared_low_energy_budget",
        budget=replace(base.budget, energy=1.0),
    )
    w192_before = _w192_context(False)
    w192_after = _w192_context(True)

    base_envelope = attainable_envelope(
        context=base, state_id="state_alpha", candidates=_base_points()
    )
    equal_state_envelope = attainable_envelope(
        context=base, state_id="state_beta_distinct", candidates=_base_points()
    )
    renamed_envelope = attainable_envelope(
        context=renamed,
        state_id="gauge_named_state",
        candidates=_renamed_points(),
        task_aliases={"task_r": "recover_record", "task_c": "certify_record"},
    )
    low_budget_envelope = attainable_envelope(
        context=low_budget, state_id="state_alpha", candidates=_base_points()
    )
    nonfactor_left = attainable_envelope(
        context=base,
        state_id="flat_left",
        candidates=(_base_points()[0],),
    )
    nonfactor_right = attainable_envelope(
        context=base,
        state_id="flat_right",
        candidates=(_base_points()[2],),
    )
    w192_before_envelope = attainable_envelope(
        context=w192_before, state_id="w192_before", candidates=()
    )
    w192_after_envelope = attainable_envelope(
        context=w192_after,
        state_id="w192_after",
        candidates=(_w192_point(),),
    )
    synthetic_left = attainable_envelope(
        context=base, state_id="synthetic_left", candidates=(_base_points()[0],)
    )
    synthetic_right = attainable_envelope(
        context=base, state_id="synthetic_right", candidates=(_base_points()[2],)
    )

    preservation = assess_pair(
        pair_id="renaming_gauge_preservation",
        left_context=base,
        right_context=renamed,
        left_envelope=base_envelope,
        right_envelope=renamed_envelope,
        evidence=PairEvidence(),
    )
    equal_nontrivial = assess_pair(
        pair_id="distinct_states_equal_capability",
        left_context=base,
        right_context=base,
        left_envelope=base_envelope,
        right_envelope=equal_state_envelope,
        evidence=PairEvidence(),
    )
    budget_completion = assess_pair(
        pair_id="budget_mutation_control",
        left_context=base,
        right_context=low_budget,
        left_envelope=base_envelope,
        right_envelope=low_budget_envelope,
        evidence=PairEvidence(),
    )
    negative_nonfactor = assess_pair(
        pair_id="negative_nonfactorization_control",
        left_context=base,
        right_context=base,
        left_envelope=nonfactor_left,
        right_envelope=nonfactor_right,
        evidence=PairEvidence(native_state_completion_available=True),
    )
    w192 = assess_pair(
        pair_id="w192_explicit_state_resource_absorption",
        left_context=w192_before,
        right_context=w192_after,
        left_envelope=w192_before_envelope,
        right_envelope=w192_after_envelope,
        evidence=PairEvidence(
            explicit_state_resource_changed=True,
            fixed_source_null_reproduces=True,
        ),
    )
    synthetic = assess_pair(
        pair_id="synthetic_complete_candidate",
        left_context=base,
        right_context=base,
        left_envelope=synthetic_left,
        right_envelope=synthetic_right,
        evidence=PairEvidence(
            physical_boundary_forced=True,
            source_law_present=True,
            completion_nonadmissibility_proved=True,
            independent_holdout=True,
            evidence_origin="synthetic",
        ),
    )
    coarse_left = {"physical_payload": "same", "display_label": "alpha"}
    coarse_right = {"physical_payload": "same", "display_label": "beta"}
    coarse_stable = (
        project_irrelevant_metadata(coarse_left, base)
        == project_irrelevant_metadata(coarse_right, base)
    )
    assessments = (
        preservation,
        equal_nontrivial,
        budget_completion,
        negative_nonfactor,
        w192,
        synthetic,
    )
    checks = (
        Check(
            "pareto_not_scalar_default",
            base_envelope.native_structure == "task_indexed_pareto_preorder"
            and len(base_envelope.points) >= 3,
            "Capability is a task-indexed Pareto envelope with incomparable cost-performance tradeoffs.",
        ),
        Check(
            "explicit_cost_error_budget",
            base.budget.energy == 5.0 and base.budget.error == 0.1,
            "Energy, time, communication, memory, and error budgets are explicit.",
        ),
        Check(
            "access_menu_resource_provenance",
            all(
                (
                    base.access_provenance,
                    base.menu_provenance,
                    base.resource_provenance,
                )
            ),
            "Access, menu, and resource provenance are mandatory context fields.",
        ),
        Check(
            "renaming_gauge_invariance",
            preservation.capability_relation == "EQUIVALENT"
            and base.semantic_dict() == renamed.semantic_dict(),
            "Task aliases and gauge or representation labels do not change the envelope.",
        ),
        Check(
            "irrelevant_coarse_graining_stability",
            coarse_stable,
            "Declared presentation-only fields are removed without changing physical payload.",
        ),
        Check(
            "equal_capability_nontriviality",
            base_envelope.state_id != equal_state_envelope.state_id
            and equal_nontrivial.capability_relation == "EQUIVALENT",
            "Distinct physical state identifiers may have equal capability envelopes.",
        ),
        Check(
            "positive_preservation_control",
            preservation.verdict == "PRESERVATION_CONTROL_PASS",
            "A representation-equivalent pair preserves capability.",
        ),
        Check(
            "negative_nonfactorization_control",
            negative_nonfactor.capability_relation == "INCOMPARABLE"
            and negative_nonfactor.verdict == "NATIVE_STATE_COMPLETION",
            "A visible-flat capability split is detected and then honestly absorbed by native state completion.",
        ),
        Check(
            "resource_budget_completion",
            budget_completion.verdict == "RESOURCE_BUDGET_COMPLETION",
            "A changed cost budget is classified as completion, not intrinsic capability creation.",
        ),
        Check(
            "w192_absorption",
            w192.verdict == W192_VERDICT
            and not w192.positive_capability_verdict_allowed,
            "W192 remains explicit state/resource completion.",
        ),
        Check(
            "synthetic_review_ceiling",
            synthetic.verdict == CANDIDATE_CEILING
            and not synthetic.positive_capability_verdict_allowed,
            "Even the fully populated synthetic case stops at review-candidate status.",
        ),
    )
    verdict = VERDICT if all(check.passed for check in checks) else "CONTRACT_CHECK_FAILED"
    return T583Result(
        artifact=ARTIFACT,
        contract_status="provisional_executable_review_instrument",
        capability_definition={
            "object": "C(R,O,T,M,B,h)",
            "value": "task-indexed nondominated attainable performance-cost-error envelope",
            "native_comparison": "Pareto cover preorder with equivalence, superset, subset, or incomparability",
            "scalar_default": False,
            "physics_direction": "known physics to induced capability object",
        },
        null_completion_classes=(
            "NO_CAPABILITY_DELTA",
            "RENAMING_OR_GAUGE_EQUIVALENCE",
            "IRRELEVANT_COARSE_GRAINING",
            "TASK_REDEFINITION_COMPLETION",
            "MENU_COMPLETION",
            "ACCESS_COMPLETION",
            "RESOURCE_BUDGET_COMPLETION",
            W192_VERDICT,
            "FIXED_SOURCE_COMPLETION",
            "NATIVE_STATE_COMPLETION",
        ),
        contexts=(base, renamed, low_budget, w192_before, w192_after),
        envelopes=(
            base_envelope,
            equal_state_envelope,
            renamed_envelope,
            low_budget_envelope,
            nonfactor_left,
            nonfactor_right,
            w192_before_envelope,
            w192_after_envelope,
            synthetic_left,
            synthetic_right,
        ),
        assessments=assessments,
        checks=checks,
        w192_verdict=w192.verdict,
        synthetic_candidate_ceiling=synthetic.verdict,
        verdict=verdict,
        claim_ledger_update="No claim-ledger or Canon Index update is earned.",
        not_claimed=(
            "T583 does not establish a universal capability measure, a scalar arrow, "
            "a physical capability transition, a source law, time emergence, issuance, "
            "or cross-repo identity. It does not move claims, canon, public posture, "
            "publication, TAF3, TAF8, S1, or cross-repo truth."
        ),
    )


def _base_context() -> CapabilityContext:
    return CapabilityContext(
        context_id="ctx_base",
        source_theory="finite_declared_control_fixture",
        region_id="R_demo",
        observer_id="O_local",
        access_profile=("local_record", "local_control"),
        access_provenance="declared_local_lab_access",
        task_family=("recover_record", "certify_record"),
        operation_menu=("apply_recovery", "certify_record"),
        menu_provenance="law_derived_finite_control",
        resource_provenance="fixed_declared_budget",
        budget=Budget(5.0, 10.0, 2.0, 8.0, 0.1),
        horizon="ten_steps",
        physical_equivalence="renaming_and_gauge_quotient",
        gauge_quotient="declared_orbit_equivalence_v1",
        native_comparison="task_indexed_pareto_cover",
        irrelevant_coarse_graining_fields=("display_label", "coordinate_name"),
        gauge_representative="gauge_rep_a",
    )


def _w192_context(has_psi: bool) -> CapabilityContext:
    return CapabilityContext(
        context_id="w192_after" if has_psi else "w192_before",
        source_theory="frozen_w192_written_spinor_proxy",
        region_id="R_W192",
        observer_id="O_algebraic_proxy",
        access_profile=("structural_handles", "psi_record") if has_psi else ("structural_handles",),
        access_provenance="packet_declared_psi_access" if has_psi else "packet_declared_no_psi_access",
        task_family=("record_conditioned_vertex_lift",),
        operation_menu=("construct_record_conditioned_vertex_lift",),
        menu_provenance="frozen_proxy_menu",
        resource_provenance="frozen_psi_present" if has_psi else "frozen_psi_absent",
        budget=Budget(1.0, 1.0, 0.0, 1.0, 0.0),
        horizon="not_supplied",
        physical_equivalence="proxy_gauge_scope_only",
        gauge_quotient="native_joint_quotient_absent",
        native_comparison="task_indexed_pareto_cover",
        irrelevant_coarse_graining_fields=("display_label",),
        representation_label="written_spinor_proxy",
        gauge_representative="not_supplied",
    )


def _base_points() -> tuple[PerformancePoint, ...]:
    return (
        PerformancePoint("recover_record", 0.90, 2.0, 4.0, 0.0, 1.0, 0.05, "recover_fast"),
        PerformancePoint("recover_record", 0.95, 4.0, 7.0, 0.0, 1.0, 0.03, "recover_high"),
        PerformancePoint("certify_record", 0.98, 1.0, 2.0, 1.0, 2.0, 0.01, "certify"),
        PerformancePoint("recover_record", 0.80, 3.0, 5.0, 0.0, 2.0, 0.08, "dominated"),
    )


def _renamed_points() -> tuple[PerformancePoint, ...]:
    return tuple(
        replace(
            point,
            task_id="task_r" if point.task_id == "recover_record" else "task_c",
            protocol_id=f"renamed_{index}",
        )
        for index, point in enumerate(_base_points())
    )


def _w192_point() -> PerformancePoint:
    return PerformancePoint(
        "record_conditioned_vertex_lift", 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, "L_psi"
    )


def result_to_dict(result: T583Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "contract_status": result.contract_status,
        "capability_definition": result.capability_definition,
        "null_completion_classes": list(result.null_completion_classes),
        "contexts": [asdict(item) for item in result.contexts],
        "envelopes": [asdict(item) for item in result.envelopes],
        "assessments": [asdict(item) for item in result.assessments],
        "checks": [asdict(item) for item in result.checks],
        "w192_verdict": result.w192_verdict,
        "synthetic_candidate_ceiling": result.synthetic_candidate_ceiling,
        "verdict": result.verdict,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def artifact_to_dict(result: T583Result) -> dict[str, Any]:
    """Return the bounded durable receipt written under results/."""
    return {
        "artifact": result.artifact,
        "contract_status": result.contract_status,
        "capability_definition": result.capability_definition,
        "null_completion_classes": list(result.null_completion_classes),
        "context_inventory": [
            {
                "context_id": item.context_id,
                "region_id": item.region_id,
                "access_provenance": item.access_provenance,
                "menu_provenance": item.menu_provenance,
                "resource_provenance": item.resource_provenance,
                "budget": asdict(item.budget),
                "native_comparison": item.native_comparison,
            }
            for item in result.contexts
        ],
        "assessments": [asdict(item) for item in result.assessments],
        "checks": [asdict(item) for item in result.checks],
        "w192_verdict": result.w192_verdict,
        "synthetic_candidate_ceiling": result.synthetic_candidate_ceiling,
        "verdict": result.verdict,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T583 Results: CapabilityContract v1",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- W192: `{payload['w192_verdict']}`",
        f"- Synthetic ceiling: `{payload['synthetic_candidate_ceiling']}`",
        "- Default object: task-indexed attainable performance-cost-error Pareto envelope.",
        "- Scalar default: False.",
        "",
        "## Checks",
        "",
        "| check | passed? | reason |",
        "| --- | :---: | --- |",
    ]
    for item in payload["checks"]:
        lines.append(f"| `{item['check_id']}` | {item['passed']} | {item['reason']} |")
    lines.extend(
        [
            "",
            "## Pair Assessments",
            "",
            "| pair | relation | completion class | verdict | positive allowed? |",
            "| --- | --- | --- | --- | :---: |",
        ]
    )
    for item in payload["assessments"]:
        lines.append(
            f"| `{item['pair_id']}` | `{item['capability_relation']}` | "
            f"`{item['completion_class']}` | `{item['verdict']}` | "
            f"{item['positive_capability_verdict_allowed']} |"
        )
    lines.extend(
        [
            "",
            "## Claim Status",
            "",
            payload["claim_ledger_update"],
            "",
            "## Not Claimed",
            "",
            payload["not_claimed"],
            "",
        ]
    )
    return "\n".join(lines)


def write_results(result: T583Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = artifact_to_dict(result)
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
    result = run_t583_analysis()
    if args.write_results:
        write_results(result)
    print(json.dumps(result_to_dict(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
