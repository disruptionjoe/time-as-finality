"""T447 - quantum E3 exact no-go big swing.

This is a recorded-tier finite toy attempt at the "absolute E3" lane that T436
left open. The packet deliberately does not claim a physics theorem.

Toy target:

    S has two charge sectors, 0 and 1.
    The forbidden task is an exact charge-flip unitary on S.
    A1 admits no reference and preserves charge.
    A2 admits a finite, non-wrapping charge-ladder reference, but requires exact
    catalytic return and exact total-charge conservation.

In this declared A2 toy, implementing the charge flip would require a finite
unilateral charge-shift operator to have a nonzero unit-modulus eigenvector.
Finite unilateral shifts are nilpotent, so no such vector exists. That is an
exact finite no-go relative to the declared finite catalytic A2 policy.

The artifact also records why this still does not earn an unrestricted absolute
E3 or public physics claim: cyclic references, consumed references, and ideal
phase references route away from this finite exact packet.

Run:

    python -m models.quantum_e3_exact_no_go_big_swing --write-results
    python -m pytest tests/test_quantum_e3_exact_no_go_big_swing.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import quantum_e3_resource_lift_classifier as t436


ARTIFACT = "T447-quantum-e3-exact-no-go-big-swing-v0.1"
SOURCE_T435 = "results/T435-quantum-e3-admissible-menu-gate-v0.1-results.md"
SOURCE_T436 = "results/T436-quantum-e3-resource-lift-classifier-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = (
    "QUANTUM_E3_FINITE_CATALYTIC_NO_GO_PACKET_BUILT_RECORDED_TIER_NOT_"
    "UNRESTRICTED_ABSOLUTE"
)

HONEST_CEILING = (
    "Recorded-tier finite toy only. T447 builds an exact no-go relative to a "
    "declared finite non-wrapping exact-catalyst A2 policy. It is not a WAY "
    "theorem, not a quantum physics claim, not a GU/TaF adapter, not cross-repo "
    "evidence, not claim-ledger movement, and not an unrestricted absolute E3 "
    "result."
)


@dataclass(frozen=True)
class A2ResourcePolicy:
    policy_id: str
    declared_before_task: bool
    a2_reference_resource_considered: bool
    reference_kind: str
    exact_catalyst_return_required: bool
    total_charge_conservation_required: bool
    exact_no_go_witness_predeclared: bool
    reference_dimension: int | None = None
    resource_cost_only_large_not_impossible: bool = False
    reads_hidden_label_or_case_id: bool = False


@dataclass(frozen=True)
class ExactNoGoCandidate:
    case_id: str
    description: str
    regime: str
    system_charge_sectors: tuple[int, ...]
    task_kind: str
    target_changes_system_charge: bool
    a1_shadow_equal_or_task_invisible: bool
    policy: A2ResourcePolicy


def finite_nonwrapping_shift_certificate(dimension: int) -> dict[str, Any]:
    """Return the finite-shift obstruction used by the main packet.

    A non-wrapping finite ladder shift S is nilpotent: S**dimension = 0. If an
    exact catalytic implementation of a charge-changing system operation returns
    the reference unchanged, the reference vector eta would need S eta = lambda
    eta with |lambda| = 1. Applying S**dimension gives 0 = lambda**dimension eta,
    so eta must be zero. No usable reference state satisfies that.
    """

    if dimension < 1:
        raise ValueError("dimension must be positive")

    return {
        "reference_model": "finite_nonwrapping_charge_ladder",
        "dimension": dimension,
        "shift_operator": "unilateral_weighted_shift",
        "nilpotent_power": dimension,
        "requires_nonzero_unit_modulus_eigenvector": True,
        "has_nonzero_unit_modulus_eigenvector": False,
        "proof_obligation": "S eta = lambda eta with |lambda| = 1",
        "proof": (
            "Finite non-wrapping shifts are nilpotent. If S^N = 0 and "
            "S eta = lambda eta with |lambda| = 1, then 0 = S^N eta = "
            "lambda^N eta, so eta = 0. Exact catalytic return needs a nonzero "
            "eta, contradiction."
        ),
    }


def cyclic_shift_control_certificate(dimension: int) -> dict[str, Any]:
    """Return the cyclic-control certificate that blocks overclaiming."""

    if dimension < 1:
        raise ValueError("dimension must be positive")

    return {
        "reference_model": "finite_cyclic_charge_reference",
        "dimension": dimension,
        "shift_operator": "cyclic_shift",
        "nilpotent_power": None,
        "requires_nonzero_unit_modulus_eigenvector": True,
        "has_nonzero_unit_modulus_eigenvector": True,
        "example_eigenvector": "uniform superposition over cyclic charges",
        "control_reading": (
            "A cyclic reference is a different toy policy. It has exact shift "
            "eigenvectors, so the finite non-wrapping nilpotent no-go does not "
            "survive this control."
        ),
    }


def _policy_to_dict(policy: A2ResourcePolicy) -> dict[str, Any]:
    return asdict(policy)


def _a1_audit(candidate: ExactNoGoCandidate) -> dict[str, Any]:
    if candidate.regime != "finite_quantum_charge_toy":
        return {
            "a1_structural_obstruction": False,
            "a1_label": "NOT_QUANTUM_E3_REGIME",
            "a1_reason": "The case is not in the declared finite quantum charge-toy regime.",
        }

    if not candidate.a1_shadow_equal_or_task_invisible:
        return {
            "a1_structural_obstruction": False,
            "a1_label": "A1_ALREADY_SEES_OR_CAN_DO_TASK",
            "a1_reason": "A1 is not blind to the candidate distinction or task.",
        }

    if candidate.task_kind != "exact_charge_flip_unitary":
        return {
            "a1_structural_obstruction": False,
            "a1_label": "TASK_NOT_THE_CHARGE_FLIP_NO_GO_TARGET",
            "a1_reason": "The case is a control, not the exact charge-flip target.",
        }

    if not candidate.target_changes_system_charge:
        return {
            "a1_structural_obstruction": False,
            "a1_label": "TASK_DOES_NOT_CHANGE_SYSTEM_CHARGE",
            "a1_reason": "The task does not force a charge-changing operation.",
        }

    return {
        "a1_structural_obstruction": True,
        "a1_label": "A1_EXACT_STRUCTURAL_OBSTRUCTION_CHARGE_CHANGE_NO_REFERENCE",
        "a1_reason": (
            "With no reference resource and exact charge conservation, A1 cannot "
            "implement a system operation that changes the charge sector."
        ),
    }


def _t436_relative_control() -> dict[str, Any]:
    classifications = t436.run()["classifications"]
    main = next(
        item
        for item in classifications
        if item["case_id"] == "t435_phase_pair_lifted_by_a2_reference"
    )
    return {
        "source_case_id": main["case_id"],
        "t436_label": main["resource_lift_label"],
        "t436_absolute_after_resource_lift": main["absolute_e3_after_resource_lift"],
        "control_reading": (
            "The T435 phase pair remains the relative-not-absolute control: A2 "
            "reference resources recover the separator."
        ),
    }


def evaluate_candidate(candidate: ExactNoGoCandidate) -> dict[str, Any]:
    policy = candidate.policy
    certificate: dict[str, Any] | None = None
    survives_declared_a2 = False
    unrestricted_absolute_earned = False

    if policy.reference_kind == "t435_phase_reference_control":
        a1 = {
            "a1_structural_obstruction": True,
            "a1_label": "T435_A1_RELATIVE_PHASE_OBSTRUCTION_CONTROL",
            "a1_reason": (
                "The T435 phase pair is A1-equivalent under the parity shadow "
                "and separated only by the A2 reference policy."
            ),
        }
        certificate = _t436_relative_control()
        label = "T435_CONTROL_A1_RELATIVE_LIFTED_BY_A2_REFERENCE"
        reason = "The T435 phase pair remains relative to A1 and lifted by A2."
    else:
        a1 = _a1_audit(candidate)

    if policy.reference_kind == "t435_phase_reference_control":
        pass
    elif not a1["a1_structural_obstruction"]:
        label = "NOT_E3_A1_BASELINE_FAILED"
        reason = a1["a1_reason"]
    elif not policy.declared_before_task:
        label = "BLOCKED_POST_HOC_NO_GO_WITNESS"
        reason = "The no-go/resource policy was selected after the task."
    elif policy.reads_hidden_label_or_case_id:
        label = "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
        reason = "The packet reads a hidden case label rather than the declared state/task."
    elif policy.resource_cost_only_large_not_impossible:
        label = "NOT_EXACT_E3_COST_ONLY_E1_E2_CANDIDATE"
        reason = "Large resource cost is not an exact single-instance no-go."
    elif not policy.total_charge_conservation_required:
        label = "NOT_STRUCTURAL_NO_CONSERVATION_RULE"
        reason = "The structural conservation rule is not part of the candidate."
    elif not policy.a2_reference_resource_considered:
        label = "A1_RELATIVE_ONLY_A2_RESOURCE_LIFT_UNTESTED"
        reason = "The case clears only the A1 obstruction; A2 has not been audited."
    elif not policy.exact_no_go_witness_predeclared:
        label = "NOT_ADMITTED_NO_PREDECLARED_EXACT_NO_GO_WITNESS"
        reason = "The packet lacks a frozen exact no-go witness."
    elif policy.reference_kind == "finite_nonwrapping_charge_ladder":
        if policy.reference_dimension is None:
            label = "NOT_ADMITTED_REFERENCE_DIMENSION_MISSING"
            reason = "The finite reference dimension must be declared."
        elif not policy.exact_catalyst_return_required:
            label = "RESOURCE_COMPLETION_REFERENCE_MAY_CHANGE_NOT_ABSOLUTE"
            reason = (
                "Without exact catalytic return, the finite reference can be "
                "spent or changed; that is resource completion, not an exact "
                "A2 no-go."
            )
        else:
            certificate = finite_nonwrapping_shift_certificate(policy.reference_dimension)
            survives_declared_a2 = True
            label = "FINITE_A2_EXACT_CATALYTIC_NO_GO_SURVIVES_TOY_RESOURCE_LIFT"
            reason = (
                "The charge flip would require a nonzero unit-modulus eigenvector "
                "of a finite non-wrapping shift. The shift is nilpotent, so the "
                "exact catalyst equation has only the zero solution."
            )
    elif policy.reference_kind == "finite_cyclic_charge_reference":
        if policy.reference_dimension is None:
            label = "NOT_ADMITTED_REFERENCE_DIMENSION_MISSING"
            reason = "The cyclic reference dimension must be declared."
        else:
            certificate = cyclic_shift_control_certificate(policy.reference_dimension)
            label = "LIFTED_BY_CYCLIC_REFERENCE_TOY_CONTROL"
            reason = (
                "A cyclic reference has exact shift eigenvectors, so this control "
                "blocks reading the non-wrapping finite no-go as unrestricted."
            )
    elif policy.reference_kind == "consumed_charge_battery":
        label = "RESOURCE_COMPLETION_CONSUMED_REFERENCE_NOT_ABSOLUTE"
        reason = (
            "A consumable charge battery changes state to supply the charge. That "
            "is an A2 resource completion, not an exact catalytic no-go."
        )
    elif policy.reference_kind == "ideal_phase_reference":
        label = "ROUTES_TO_IDEAL_OR_LIMIT_REFERENCE_NOT_FINITE_EXACT"
        reason = (
            "An ideal phase reference is outside the finite non-wrapping toy. It "
            "routes to idealization/E1-style review or an E0 ideal-reference policy."
        )
    else:
        label = "NOT_ADMITTED_UNKNOWN_REFERENCE_POLICY"
        reason = "The A2 reference policy is not one of the declared controls."

    return {
        "case_id": candidate.case_id,
        "description": candidate.description,
        "regime": candidate.regime,
        "system_charge_sectors": list(candidate.system_charge_sectors),
        "task_kind": candidate.task_kind,
        "target_changes_system_charge": candidate.target_changes_system_charge,
        "a1_shadow_equal_or_task_invisible": candidate.a1_shadow_equal_or_task_invisible,
        "a1_audit": a1,
        "policy": _policy_to_dict(policy),
        "certificate": certificate,
        "survives_declared_finite_a2_resource_lift": survives_declared_a2,
        "unrestricted_absolute_e3_earned": unrestricted_absolute_earned,
        "resource_lift_label": label,
        "reason": reason,
    }


def _policy(
    policy_id: str,
    reference_kind: str = "finite_nonwrapping_charge_ladder",
    declared_before_task: bool = True,
    a2_reference_resource_considered: bool = True,
    exact_catalyst_return_required: bool = True,
    total_charge_conservation_required: bool = True,
    exact_no_go_witness_predeclared: bool = True,
    reference_dimension: int | None = 5,
    resource_cost_only_large_not_impossible: bool = False,
    reads_hidden_label_or_case_id: bool = False,
) -> A2ResourcePolicy:
    return A2ResourcePolicy(
        policy_id=policy_id,
        declared_before_task=declared_before_task,
        a2_reference_resource_considered=a2_reference_resource_considered,
        reference_kind=reference_kind,
        exact_catalyst_return_required=exact_catalyst_return_required,
        total_charge_conservation_required=total_charge_conservation_required,
        exact_no_go_witness_predeclared=exact_no_go_witness_predeclared,
        reference_dimension=reference_dimension,
        resource_cost_only_large_not_impossible=resource_cost_only_large_not_impossible,
        reads_hidden_label_or_case_id=reads_hidden_label_or_case_id,
    )


def _charge_flip_case(
    case_id: str,
    description: str,
    policy: A2ResourcePolicy,
    a1_shadow_equal_or_task_invisible: bool = True,
    target_changes_system_charge: bool = True,
    task_kind: str = "exact_charge_flip_unitary",
) -> ExactNoGoCandidate:
    return ExactNoGoCandidate(
        case_id=case_id,
        description=description,
        regime="finite_quantum_charge_toy",
        system_charge_sectors=(0, 1),
        task_kind=task_kind,
        target_changes_system_charge=target_changes_system_charge,
        a1_shadow_equal_or_task_invisible=a1_shadow_equal_or_task_invisible,
        policy=policy,
    )


def candidates() -> tuple[ExactNoGoCandidate, ...]:
    return (
        _charge_flip_case(
            case_id="finite_nonwrapping_exact_catalyst_charge_flip",
            description=(
                "Main packet: exact charge flip under total charge conservation "
                "with a finite non-wrapping A2 reference that must be returned "
                "exactly."
            ),
            policy=_policy("finite_nonwrapping_exact_catalyst", reference_dimension=5),
        ),
        _charge_flip_case(
            case_id="a1_only_missing_a2_audit",
            description="A case that clears A1 but never runs the A2 resource-lift audit.",
            policy=_policy(
                "missing_a2_audit",
                a2_reference_resource_considered=False,
                exact_no_go_witness_predeclared=True,
            ),
        ),
        _charge_flip_case(
            case_id="finite_reference_may_be_consumed",
            description=(
                "Finite charge resource without exact catalytic return is resource "
                "completion, not an exact no-go."
            ),
            policy=_policy(
                "finite_reference_may_be_consumed",
                exact_catalyst_return_required=False,
            ),
        ),
        _charge_flip_case(
            case_id="consumed_charge_battery_control",
            description="A declared consumed charge battery supplies the missing charge.",
            policy=_policy(
                "consumed_charge_battery",
                reference_kind="consumed_charge_battery",
                exact_catalyst_return_required=False,
                reference_dimension=None,
            ),
        ),
        _charge_flip_case(
            case_id="cyclic_reference_control",
            description=(
                "A finite cyclic reference has exact shift eigenvectors and blocks "
                "unrestricted overclaiming."
            ),
            policy=_policy(
                "cyclic_reference",
                reference_kind="finite_cyclic_charge_reference",
                reference_dimension=5,
            ),
        ),
        _charge_flip_case(
            case_id="ideal_phase_reference_control",
            description="An ideal phase reference is outside the finite exact packet.",
            policy=_policy(
                "ideal_phase_reference",
                reference_kind="ideal_phase_reference",
                reference_dimension=None,
            ),
        ),
        _charge_flip_case(
            case_id="post_hoc_exact_witness_blocked",
            description="A no-go witness chosen after seeing the target is blocked.",
            policy=_policy("post_hoc_exact_witness", declared_before_task=False),
        ),
        _charge_flip_case(
            case_id="hidden_label_oracle_blocked",
            description="A policy that reads a hidden case label is blocked.",
            policy=_policy("hidden_label_oracle", reads_hidden_label_or_case_id=True),
        ),
        _charge_flip_case(
            case_id="large_resource_cost_only_control",
            description="Large resource burden alone routes to E1/E2, not exact E3.",
            policy=_policy(
                "large_resource_cost_only",
                resource_cost_only_large_not_impossible=True,
            ),
        ),
        _charge_flip_case(
            case_id="a1_visible_task_control",
            description="A control where A1 already sees or can do the task.",
            policy=_policy("a1_visible_task_control"),
            a1_shadow_equal_or_task_invisible=False,
            target_changes_system_charge=False,
            task_kind="sector_population_readout",
        ),
        ExactNoGoCandidate(
            case_id="t435_phase_pair_relative_control",
            description="The T435/T436 phase pair remains the relative-not-absolute control.",
            regime="finite_quantum_parity_phase_toy",
            system_charge_sectors=(0, 1),
            task_kind="relative_phase_separator",
            target_changes_system_charge=False,
            a1_shadow_equal_or_task_invisible=True,
            policy=_policy(
                "t435_phase_reference_control",
                reference_kind="t435_phase_reference_control",
                reference_dimension=None,
            ),
        ),
    )


def run() -> dict[str, Any]:
    audits = [evaluate_candidate(candidate) for candidate in candidates()]
    main = next(
        item
        for item in audits
        if item["case_id"] == "finite_nonwrapping_exact_catalyst_charge_flip"
    )
    finite_survivors = [
        item["case_id"]
        for item in audits
        if item["survives_declared_finite_a2_resource_lift"]
    ]
    unrestricted = [
        item["case_id"] for item in audits if item["unrestricted_absolute_e3_earned"]
    ]
    routed_controls = [
        item["case_id"]
        for item in audits
        if item["resource_lift_label"]
        in {
            "LIFTED_BY_CYCLIC_REFERENCE_TOY_CONTROL",
            "RESOURCE_COMPLETION_CONSUMED_REFERENCE_NOT_ABSOLUTE",
            "ROUTES_TO_IDEAL_OR_LIMIT_REFERENCE_NOT_FINITE_EXACT",
            "T435_CONTROL_A1_RELATIVE_LIFTED_BY_A2_REFERENCE",
        }
    ]

    return {
        "artifact": ARTIFACT,
        "source_taxonomy": SOURCE_TAXONOMY,
        "source_t435": SOURCE_T435,
        "source_t436": SOURCE_T436,
        "purpose": (
            "Attempt a finite exact structural-symmetry no-go packet after the "
            "T435/T436 A1/A2 discipline, while recording any route back to "
            "relative/not-absolute."
        ),
        "declared_packet": {
            "system": "two-sector charge toy with system charges {0, 1}",
            "target_task": "exact charge-flip unitary on the system",
            "a1_policy": "no reference resource; exact charge-conserving operations",
            "a2_policy": (
                "finite non-wrapping charge-ladder reference; exact total-charge "
                "conservation; exact catalytic return"
            ),
            "exact_witness": "finite nilpotent shift has no nonzero unit-modulus eigenvector",
        },
        "case_audits": audits,
        "overall_verdict": {
            "verdict": VERDICT,
            "main_case_label": main["resource_lift_label"],
            "main_case_survives_declared_finite_a2": main[
                "survives_declared_finite_a2_resource_lift"
            ],
            "finite_a2_survivor_case_ids": finite_survivors,
            "unrestricted_absolute_e3_case_ids": unrestricted,
            "routed_not_absolute_control_case_ids": routed_controls,
            "reading": (
                "T447 gets a positive finite toy packet: under the declared finite "
                "non-wrapping exact-catalyst A2 policy, exact charge-flip would "
                "require a nonzero unit-modulus eigenvector of a nilpotent shift, "
                "which is impossible. The artifact still does not earn an "
                "unrestricted absolute E3 result, because cyclic, consumed, ideal, "
                "and T435-style reference policies route away from the finite "
                "catalytic no-go."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Treat the main case as finite exact-catalytic A2 residue only.",
            "Do not cite this as a WAY theorem or public quantum-physics claim.",
            "Any stronger E3 attempt must type the resource policy before the task and handle cyclic, consumed, and ideal-reference absorbers.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    packet = result["declared_packet"]
    rows = [
        "| {case_id} | {a1} | {label} | {survives} | {absolute} |".format(
            case_id=item["case_id"],
            a1="yes" if item["a1_audit"]["a1_structural_obstruction"] else "no",
            label=item["resource_lift_label"],
            survives="yes" if item["survives_declared_finite_a2_resource_lift"] else "no",
            absolute="yes" if item["unrestricted_absolute_e3_earned"] else "no",
        )
        for item in result["case_audits"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T447 - Quantum E3 Exact No-Go Big Swing - v0.1 results",
            "",
            "> Recorded-tier finite toy. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No claim promotion. This is not a "
            "WAY theorem, not a quantum physics claim, not a GU adapter, and not "
            "cross-repo evidence.",
            "",
            "- Spec (frozen first): `tests/T447-quantum-e3-exact-no-go-big-swing.md`",
            "- Model: `models/quantum_e3_exact_no_go_big_swing.py`",
            "- Tests: `tests/test_quantum_e3_exact_no_go_big_swing.py`",
            "- Artifact JSON: `results/T447-quantum-e3-exact-no-go-big-swing-v0.1.json`",
            "- Source control: `results/T436-quantum-e3-resource-lift-classifier-v0.1-results.md`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Declared Packet",
            "",
            f"- System: {packet['system']}",
            f"- Target task: {packet['target_task']}",
            f"- A1 policy: {packet['a1_policy']}",
            f"- A2 policy: {packet['a2_policy']}",
            f"- Exact witness: {packet['exact_witness']}",
            "",
            "## Case Audit",
            "",
            "| case | A1 obstruction? | resource-lift label | finite A2 survives? | unrestricted absolute? |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a finite exact no-go packet relative to the declared "
            "non-wrapping exact-catalyst A2 policy. The no-go witness is the "
            "nilpotence of the finite shift required by exact charge conservation "
            "and exact catalyst return.",
            "",
            "Does not earn: an unrestricted absolute E3 result, a WAY theorem, a "
            "quantum physics claim, a GU/TaF adapter, a claim-ledger update, "
            "public-posture movement, or cross-repo support.",
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_steps,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T447-quantum-e3-exact-no-go-big-swing-v0.1.json"
        md_path = results_dir / "T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
