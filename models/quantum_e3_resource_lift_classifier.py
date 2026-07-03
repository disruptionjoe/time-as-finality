"""T436 - quantum E3 resource-lift classifier.

T435 built the finite A-class admissible-menu gate: a phase datum can be
E3-style relative to A1 symmetry-respecting menus without a reference resource,
then become E0-declared when A2 admits the reference/asymmetry resource.

T436 adds the follow-on guardrail: do not read an A1-relative obstruction as an
absolute E3/no-go claim unless a predeclared exact no-go survives the A2
resource-lift audit. The T435 phase pair is therefore classified as relative,
not absolute. A synthetic no-go control proves the classifier can report the
absolute-after-resource shape, but it is calibration only.

Recorded-tier only. This is not a WAY theorem, not a quantum physics claim, not
a GU adapter, and not claim support.

Run:

    python -m models.quantum_e3_resource_lift_classifier --write-results
    python -m pytest tests/test_quantum_e3_resource_lift_classifier.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import quantum_e3_admissible_menu_gate as t435


ARTIFACT = "T436-quantum-e3-resource-lift-classifier-v0.1"
SOURCE_T435 = "results/T435-quantum-e3-admissible-menu-gate-v0.1-results.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"
SOURCE_OPEN_PROBLEM = "open-problems/finite-closed-capability-boundary-scope-theorem.md"

VERDICT = "QUANTUM_E3_RESOURCE_LIFT_CLASSIFIER_BUILT_T435_RELATIVE_NOT_ABSOLUTE"

HONEST_CEILING = (
    "Recorded-tier taxonomy guardrail only. T436 classifies resource-lift status "
    "for finite gate cases; it is not a WAY theorem, not a quantum physics claim, "
    "not a GU/TaF adapter, not cross-repo evidence, and not claim-ledger movement."
)


@dataclass(frozen=True)
class ResourceLiftPolicy:
    policy_id: str
    declared_before_pair: bool
    a2_reference_resource_considered: bool
    a2_reference_resource_admits_separator: bool
    exact_no_go_witness_predeclared: bool
    resource_cost_only_large_not_impossible: bool = False
    reads_hidden_resource_or_label: bool = False
    synthetic_control_only: bool = False


@dataclass(frozen=True)
class ResourceLiftCase:
    case_id: str
    description: str
    t435_candidate_id: str
    policy: ResourceLiftPolicy


def _t435_audit(candidate_id: str) -> dict[str, Any]:
    for candidate in t435.candidates():
        if candidate.candidate_id == candidate_id:
            return t435.evaluate_candidate(candidate)
    raise ValueError(f"unknown T435 candidate id: {candidate_id}")


def _policy_to_dict(policy: ResourceLiftPolicy) -> dict[str, Any]:
    return asdict(policy)


def classify_case(case: ResourceLiftCase) -> dict[str, Any]:
    audit = _t435_audit(case.t435_candidate_id)
    policy = case.policy
    baseline_admitted = bool(audit["admitted_e3_relative_to_a1"])

    if not baseline_admitted:
        absolute = False
        label = "NOT_E3_BASELINE_GATE_FAILED"
        reason = (
            "The underlying T435 candidate does not first clear the A1 relative "
            f"E3 gate: {audit['residue_label']}."
        )
    elif not policy.declared_before_pair:
        absolute = False
        label = "NOT_ADMITTED_RESOURCE_POLICY_POST_HOC"
        reason = "The resource-lift policy was not frozen before pair selection."
    elif policy.reads_hidden_resource_or_label:
        absolute = False
        label = "BLOCKED_HIDDEN_RESOURCE_OR_LABEL"
        reason = "The resource-lift packet reads a hidden label or hidden resource."
    elif not policy.a2_reference_resource_considered:
        absolute = False
        label = "A1_RELATIVE_ONLY_RESOURCE_LIFT_UNTESTED"
        reason = "The candidate is only classified relative to A1; A2 was not audited."
    elif policy.a2_reference_resource_admits_separator:
        absolute = False
        label = "A1_RELATIVE_LIFTED_TO_E0_BY_A2_REFERENCE"
        reason = "A2 admits a reference/asymmetry resource that recovers the separator."
    elif policy.resource_cost_only_large_not_impossible:
        absolute = False
        label = "NOT_ABSOLUTE_E3_COST_ONLY_E1_E2_CANDIDATE"
        reason = (
            "Large or family-dependent resource cost is an E1/E2-style burden, "
            "not a single-instance exact E3 no-go."
        )
    elif policy.exact_no_go_witness_predeclared:
        absolute = True
        label = "ABSOLUTE_E3_SHAPE_SURVIVES_A2_SYNTHETIC_CONTROL"
        reason = (
            "The A1 obstruction survives the A2 resource-lift audit because a "
            "predeclared exact no-go witness still forbids the separator. In this "
            "artifact this is synthetic calibration only."
        )
    else:
        absolute = False
        label = "NOT_ADMITTED_NO_EXACT_RESOURCE_NO_GO_WITNESS"
        reason = (
            "A2 did not declare the separator, but the packet lacks an independent "
            "predeclared exact no-go witness."
        )

    return {
        "case_id": case.case_id,
        "description": case.description,
        "source_t435_candidate_id": case.t435_candidate_id,
        "t435_residue_label": audit["residue_label"],
        "t435_a1_e3_admitted": baseline_admitted,
        "policy": _policy_to_dict(policy),
        "absolute_e3_after_resource_lift": absolute,
        "resource_lift_label": label,
        "reason": reason,
    }


def _policy(
    policy_id: str,
    declared_before_pair: bool = True,
    a2_reference_resource_considered: bool = True,
    a2_reference_resource_admits_separator: bool = False,
    exact_no_go_witness_predeclared: bool = False,
    resource_cost_only_large_not_impossible: bool = False,
    reads_hidden_resource_or_label: bool = False,
    synthetic_control_only: bool = False,
) -> ResourceLiftPolicy:
    return ResourceLiftPolicy(
        policy_id=policy_id,
        declared_before_pair=declared_before_pair,
        a2_reference_resource_considered=a2_reference_resource_considered,
        a2_reference_resource_admits_separator=a2_reference_resource_admits_separator,
        exact_no_go_witness_predeclared=exact_no_go_witness_predeclared,
        resource_cost_only_large_not_impossible=resource_cost_only_large_not_impossible,
        reads_hidden_resource_or_label=reads_hidden_resource_or_label,
        synthetic_control_only=synthetic_control_only,
    )


def cases() -> tuple[ResourceLiftCase, ...]:
    return (
        ResourceLiftCase(
            case_id="t435_phase_pair_lifted_by_a2_reference",
            description=(
                "The T435 main phase pair clears the A1 relative gate, but A2 admits "
                "the reference/asymmetry resource that recovers X."
            ),
            t435_candidate_id="z2_phase_pair_a1_no_reference",
            policy=_policy(
                "t435_declared_a2_reference",
                a2_reference_resource_admits_separator=True,
            ),
        ),
        ResourceLiftCase(
            case_id="t435_mixed_pair_lifted_by_a2_reference",
            description=(
                "The T435 dephased-mixture control is also A1-relative rather than "
                "absolute once the same A2 reference policy is admitted."
            ),
            t435_candidate_id="symmetric_mixed_state_control",
            policy=_policy(
                "t435_declared_a2_reference_for_mixed_control",
                a2_reference_resource_admits_separator=True,
            ),
        ),
        ResourceLiftCase(
            case_id="synthetic_exact_no_go_survives_a2",
            description=(
                "Synthetic calibration: the classifier can report an absolute E3 "
                "shape if a predeclared exact no-go still forbids the separator "
                "after A2 is considered."
            ),
            t435_candidate_id="z2_phase_pair_a1_no_reference",
            policy=_policy(
                "synthetic_exact_no_go_after_a2",
                exact_no_go_witness_predeclared=True,
                synthetic_control_only=True,
            ),
        ),
        ResourceLiftCase(
            case_id="large_resource_cost_not_single_instance_e3",
            description=(
                "A large or family-dependent resource cost without exact impossibility "
                "does not clear the absolute E3 classifier."
            ),
            t435_candidate_id="z2_phase_pair_a1_no_reference",
            policy=_policy(
                "cost_only_no_exact_no_go",
                resource_cost_only_large_not_impossible=True,
            ),
        ),
        ResourceLiftCase(
            case_id="a1_only_no_resource_lift_audit",
            description="A candidate that never audits A2 stays A1-relative only.",
            t435_candidate_id="z2_phase_pair_a1_no_reference",
            policy=_policy(
                "no_a2_audit",
                a2_reference_resource_considered=False,
            ),
        ),
        ResourceLiftCase(
            case_id="post_hoc_resource_policy_blocked",
            description="A resource policy selected after seeing the pair is blocked.",
            t435_candidate_id="z2_phase_pair_a1_no_reference",
            policy=_policy(
                "post_hoc_resource_policy",
                declared_before_pair=False,
            ),
        ),
        ResourceLiftCase(
            case_id="hidden_resource_oracle_blocked",
            description="A resource-lift packet that reads a hidden label is blocked.",
            t435_candidate_id="z2_phase_pair_a1_no_reference",
            policy=_policy(
                "hidden_resource_oracle",
                reads_hidden_resource_or_label=True,
            ),
        ),
        ResourceLiftCase(
            case_id="a1_visible_charge_control_not_e3",
            description="If A1 already distinguishes the pair, there is no E3 boundary.",
            t435_candidate_id="charge_population_visible_control",
            policy=_policy("visible_charge_policy"),
        ),
        ResourceLiftCase(
            case_id="classical_full_code_control_not_quantum_e3",
            description="Classical full-code controls remain T433-style declared cases.",
            t435_candidate_id="classical_full_code_control",
            policy=_policy("classical_full_code_policy"),
        ),
    )


def run() -> dict[str, Any]:
    classifications = [classify_case(case) for case in cases()]
    main = next(
        item
        for item in classifications
        if item["case_id"] == "t435_phase_pair_lifted_by_a2_reference"
    )
    absolute_controls = [
        item for item in classifications if item["absolute_e3_after_resource_lift"]
    ]
    blocked = [
        item
        for item in classifications
        if item["resource_lift_label"].startswith("NOT_")
        or item["resource_lift_label"].startswith("BLOCKED_")
    ]
    relative = [
        item
        for item in classifications
        if item["resource_lift_label"] == "A1_RELATIVE_LIFTED_TO_E0_BY_A2_REFERENCE"
    ]

    return {
        "artifact": ARTIFACT,
        "source_t435": SOURCE_T435,
        "source_taxonomy": SOURCE_TAXONOMY,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "purpose": (
            "Classify whether a T435-style A1 quantum E3 boundary survives or "
            "collapses when A2 reference/asymmetry resources are audited."
        ),
        "classification_requirements_for_absolute_e3": [
            "underlying case clears the T435 A1 relative E3 gate",
            "resource-lift policy is predeclared",
            "A2 reference/asymmetry resources are explicitly considered",
            "the A2 policy does not admit a separator that recovers the datum",
            "large resource cost alone is not counted as exact impossibility",
            "an independent exact no-go witness is predeclared",
            "no hidden label, post-hoc resource, or pair-specific selector is used",
        ],
        "classifications": classifications,
        "overall_verdict": {
            "verdict": VERDICT,
            "t435_main_pair_relative_not_absolute": (
                main["resource_lift_label"] == "A1_RELATIVE_LIFTED_TO_E0_BY_A2_REFERENCE"
                and not main["absolute_e3_after_resource_lift"]
            ),
            "relative_case_ids": [item["case_id"] for item in relative],
            "absolute_synthetic_control_ids": [item["case_id"] for item in absolute_controls],
            "blocked_or_rejected_case_ids": [item["case_id"] for item in blocked],
            "reading": (
                "T436 preserves T435 as an A1 admissible-menu control while blocking "
                "the stronger reading that T435 is an absolute E3/no-go result. "
                "The T435 phase pair is lifted to E0 once A2 admits the reference "
                "resource. Absolute E3 requires a separate exact no-go witness that "
                "survives the resource-lift audit."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Future quantum E3 attempts should report both A1 status and A2 resource-lift status.",
            "Do not cite T435 as an absolute no-go; it is relative to A1 without reference.",
            "A real absolute E3 artifact must bring an independently typed exact no-go witness.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["classification_requirements_for_absolute_e3"]]
    rows = [
        "| {case_id} | {base} | {label} | {absolute} |".format(
            case_id=item["case_id"],
            base="yes" if item["t435_a1_e3_admitted"] else "no",
            label=item["resource_lift_label"],
            absolute="yes" if item["absolute_e3_after_resource_lift"] else "no",
        )
        for item in result["classifications"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T436 - Quantum E3 Resource-Lift Classifier - v0.1 results",
            "",
            "> Recorded-tier taxonomy guardrail. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No claim promotion. This is not a "
            "WAY theorem, not a GU adapter, and not cross-repo evidence.",
            "",
            "- Spec (frozen first): `tests/T436-quantum-e3-resource-lift-classifier.md`",
            "- Model: `models/quantum_e3_resource_lift_classifier.py`",
            "- Tests: `tests/test_quantum_e3_resource_lift_classifier.py`",
            "- Artifact JSON: `results/T436-quantum-e3-resource-lift-classifier-v0.1.json`",
            "- Source control: `results/T435-quantum-e3-admissible-menu-gate-v0.1-results.md`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Absolute E3 Classification Requirements",
            "",
            *requirements,
            "",
            "## Case Classification",
            "",
            "| case | T435 A1 E3? | resource-lift label | absolute after resource lift? |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a resource-lift guardrail for quantum E3 taxonomy work. The T435 "
            "phase pair is recorded as A1-relative and A2-declared, not absolute.",
            "",
            "Does not earn: a WAY theorem, a quantum physics claim, a GU/TaF "
            "adapter, a claim-ledger update, public-posture movement, or cross-repo "
            "support.",
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
        json_path = results_dir / "T436-quantum-e3-resource-lift-classifier-v0.1.json"
        md_path = results_dir / "T436-quantum-e3-resource-lift-classifier-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
