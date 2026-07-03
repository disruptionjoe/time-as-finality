"""T435 - quantum E3 admissible-menu gate.

T433 discharged the classical finite-product C-fragment: every total datum is
E0-declared relative to A1 once the full co-present classical code is admitted.
T435 records the complementary quantum hinge in a deliberately small finite
symmetry toy.

With a predeclared parity/superselection generator P, A1 admits only
symmetry-respecting observables that commute with P and no reference/asymmetry
resource. The |+><+| and |-><-| states have the same A1 diagonal shadow, but the
relative-phase observable X separates them and does not commute with P. Thus the
boundary is E3-style relative to A1. If A2 admits the reference/asymmetry resource,
the same separator becomes declared/recoverable and the verdict drops to E0.

Recorded-tier only. This is not a WAY theorem, not a quantum-physics claim, not a
GU adapter, and not claim support.

Run:

    python -m models.quantum_e3_admissible_menu_gate --write-results
    python -m pytest tests/test_quantum_e3_admissible_menu_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T435-quantum-e3-admissible-menu-gate-v0.1"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"
SOURCE_OPEN_PROBLEM = "open-problems/finite-closed-capability-boundary-scope-theorem.md"
EPS = 1e-9

VERDICT = "QUANTUM_E3_A_CLASS_GATE_BUILT_NO_CLAIM_PROMOTION"

HONEST_CEILING = (
    "Recorded-tier taxonomy/admission gate only. This finite parity toy illustrates "
    "A1/A2 dependence for a standard symmetry-resource shape; it is not a WAY "
    "theorem, not a quantum physics claim, not a GU/TaF adapter, not cross-repo "
    "evidence, and not claim-ledger movement."
)

Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]


I2: Matrix = (
    (1 + 0j, 0 + 0j),
    (0 + 0j, 1 + 0j),
)
P_PARITY: Matrix = (
    (1 + 0j, 0 + 0j),
    (0 + 0j, -1 + 0j),
)
X_PHASE: Matrix = (
    (0 + 0j, 1 + 0j),
    (1 + 0j, 0 + 0j),
)


def _matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def _matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def _max_abs(matrix: Matrix) -> float:
    return max(abs(value) for row in matrix for value in row)


def commutator_norm(left: Matrix, right: Matrix) -> float:
    return _max_abs(
        _matrix_subtract(_matrix_multiply(left, right), _matrix_multiply(right, left))
    )


def commutes_with_parity(observable: Matrix) -> bool:
    return commutator_norm(observable, P_PARITY) <= EPS


def expectation(state: Matrix, observable: Matrix) -> float:
    product = _matrix_multiply(state, observable)
    return float((product[0][0] + product[1][1]).real)


def a1_shadow(state: Matrix) -> tuple[float, float]:
    """A1 symmetry-respecting observables see only the sector populations."""

    return (round(float(state[0][0].real), 12), round(float(state[1][1].real), 12))


def states_a1_equivalent(left: Matrix, right: Matrix) -> bool:
    return a1_shadow(left) == a1_shadow(right)


def density(state_id: str) -> Matrix:
    if state_id == "plus":
        return (
            (0.5 + 0j, 0.5 + 0j),
            (0.5 + 0j, 0.5 + 0j),
        )
    if state_id == "minus":
        return (
            (0.5 + 0j, -0.5 + 0j),
            (-0.5 + 0j, 0.5 + 0j),
        )
    if state_id == "charge_0":
        return (
            (1 + 0j, 0 + 0j),
            (0 + 0j, 0 + 0j),
        )
    if state_id == "charge_1":
        return (
            (0 + 0j, 0 + 0j),
            (0 + 0j, 1 + 0j),
        )
    if state_id == "maximally_mixed":
        return (
            (0.5 + 0j, 0 + 0j),
            (0 + 0j, 0.5 + 0j),
        )
    raise ValueError(f"unknown state id: {state_id}")


def observable(observable_id: str) -> Matrix:
    if observable_id == "I":
        return I2
    if observable_id == "P":
        return P_PARITY
    if observable_id == "X":
        return X_PHASE
    raise ValueError(f"unknown observable id: {observable_id}")


@dataclass(frozen=True)
class SymmetryPacket:
    packet_id: str
    regime: str
    source_kind: str
    declared_before_pair: bool
    shared_symmetry_across_pair: bool
    generator: str
    admissible_class: str
    reference_resource_admitted: bool
    separator_observable: str
    separator_declared_before_pair: bool
    reads_case_id_or_hidden_label: bool


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    description: str
    left_state: str
    right_state: str
    packet: SymmetryPacket


def _packet_to_dict(packet: SymmetryPacket) -> dict[str, Any]:
    return asdict(packet)


def evaluate_candidate(candidate: Candidate) -> dict[str, Any]:
    packet = candidate.packet
    left = density(candidate.left_state)
    right = density(candidate.right_state)
    sep = observable(packet.separator_observable)

    a1_equal = states_a1_equivalent(left, right)
    separator_gap = abs(expectation(left, sep) - expectation(right, sep))
    separator_separates = separator_gap > EPS
    separator_commutes = commutes_with_parity(sep)

    if packet.regime != "finite_quantum":
        admitted_e3 = False
        label = "control_not_quantum_e3_regime"
        reason = "The candidate is not in the finite quantum symmetry regime."
    elif packet.source_kind != "predeclared_symmetry_superselection":
        admitted_e3 = False
        label = "not_admitted_no_predeclared_symmetry"
        reason = "No predeclared symmetry/superselection packet is supplied."
    elif not packet.declared_before_pair or not packet.separator_declared_before_pair:
        admitted_e3 = False
        label = "not_admitted_post_hoc_symmetry_or_separator"
        reason = "The symmetry or separator was not frozen before pair selection."
    elif not packet.shared_symmetry_across_pair:
        admitted_e3 = False
        label = "not_admitted_pair_specific_symmetry"
        reason = "The two sides do not share one symmetry rule."
    elif packet.reads_case_id_or_hidden_label:
        admitted_e3 = False
        label = "blocked_hidden_label_oracle"
        reason = "The separator reads a hidden label rather than the declared quantum state."
    elif not a1_equal:
        admitted_e3 = False
        label = "no_boundary_a1_already_distinguishes"
        reason = "A1 symmetry-respecting statistics already distinguish the pair."
    elif not separator_separates:
        admitted_e3 = False
        label = "no_boundary_separator_does_not_split_capability"
        reason = "The declared separator does not split the pair."
    elif separator_commutes:
        admitted_e3 = False
        label = "no_e3_separator_is_a1_admissible"
        reason = "The separator commutes with the symmetry and is already A1-admissible."
    elif packet.admissible_class == "A2" or packet.reference_resource_admitted:
        admitted_e3 = False
        label = "E0_DECLARED_RELATIVE_TO_A2_REFERENCE_RESOURCE"
        reason = "A2 admits the reference/asymmetry resource that recovers the phase datum."
    elif packet.admissible_class != "A1":
        admitted_e3 = False
        label = "not_admitted_unknown_admissible_class"
        reason = "The admissible class must be named as A1 or A2 for this gate."
    else:
        admitted_e3 = True
        label = "E3_STRUCTURAL_SYMMETRY_RELATIVE_TO_A1_NO_REFERENCE"
        reason = (
            "The pair is A1-equivalent, the separator is noncommuting, and no "
            "reference/asymmetry resource is admitted."
        )

    return {
        "candidate_id": candidate.candidate_id,
        "description": candidate.description,
        "left_state": candidate.left_state,
        "right_state": candidate.right_state,
        "packet": _packet_to_dict(packet),
        "a1_shadow_left": list(a1_shadow(left)),
        "a1_shadow_right": list(a1_shadow(right)),
        "a1_statistics_equal": a1_equal,
        "separator_expectation_left": round(expectation(left, sep), 12),
        "separator_expectation_right": round(expectation(right, sep), 12),
        "separator_gap": round(separator_gap, 12),
        "separator_commutes_with_symmetry": separator_commutes,
        "separator_commutator_norm": round(commutator_norm(sep, P_PARITY), 12),
        "admitted_e3_relative_to_a1": admitted_e3,
        "residue_label": label,
        "reason": reason,
    }


def _packet(
    packet_id: str,
    regime: str = "finite_quantum",
    source_kind: str = "predeclared_symmetry_superselection",
    declared_before_pair: bool = True,
    shared_symmetry_across_pair: bool = True,
    admissible_class: str = "A1",
    reference_resource_admitted: bool = False,
    separator_observable: str = "X",
    separator_declared_before_pair: bool = True,
    reads_case_id_or_hidden_label: bool = False,
) -> SymmetryPacket:
    return SymmetryPacket(
        packet_id=packet_id,
        regime=regime,
        source_kind=source_kind,
        declared_before_pair=declared_before_pair,
        shared_symmetry_across_pair=shared_symmetry_across_pair,
        generator="P=diag(1,-1)",
        admissible_class=admissible_class,
        reference_resource_admitted=reference_resource_admitted,
        separator_observable=separator_observable,
        separator_declared_before_pair=separator_declared_before_pair,
        reads_case_id_or_hidden_label=reads_case_id_or_hidden_label,
    )


def candidates() -> tuple[Candidate, ...]:
    return (
        Candidate(
            candidate_id="z2_phase_pair_a1_no_reference",
            description=(
                "Main control: |+> and |-> share the A1 sector-population shadow, "
                "but X separates them and is not symmetry-admissible without a reference."
            ),
            left_state="plus",
            right_state="minus",
            packet=_packet("z2_phase_a1_no_reference"),
        ),
        Candidate(
            candidate_id="z2_phase_pair_a2_reference",
            description=(
                "A2 control: the same pair becomes declared once a reference/asymmetry "
                "resource admits X."
            ),
            left_state="plus",
            right_state="minus",
            packet=_packet(
                "z2_phase_a2_reference",
                admissible_class="A2",
                reference_resource_admitted=True,
            ),
        ),
        Candidate(
            candidate_id="charge_population_visible_control",
            description="A1 already distinguishes charge-sector populations.",
            left_state="charge_0",
            right_state="charge_1",
            packet=_packet("charge_population_visible", separator_observable="P"),
        ),
        Candidate(
            candidate_id="classical_full_code_control",
            description=(
                "Classical finite-code controls remain T433-style E0 declared, not "
                "quantum E3."
            ),
            left_state="plus",
            right_state="minus",
            packet=_packet(
                "classical_full_code_control",
                regime="classical_finite",
                source_kind="classical_full_code",
            ),
        ),
        Candidate(
            candidate_id="post_hoc_symmetry_selector",
            description="A symmetry-looking packet selected after the pair is rejected.",
            left_state="plus",
            right_state="minus",
            packet=_packet(
                "post_hoc_symmetry_selector",
                declared_before_pair=False,
            ),
        ),
        Candidate(
            candidate_id="hidden_label_phase_oracle",
            description="A separator that reads a hidden case label rather than state data.",
            left_state="plus",
            right_state="minus",
            packet=_packet(
                "hidden_label_phase_oracle",
                reads_case_id_or_hidden_label=True,
            ),
        ),
        Candidate(
            candidate_id="no_symmetry_packet",
            description="A noncommuting separator without a frozen symmetry packet.",
            left_state="plus",
            right_state="minus",
            packet=_packet(
                "no_symmetry_packet",
                source_kind="none",
            ),
        ),
        Candidate(
            candidate_id="symmetric_mixed_state_control",
            description=(
                "A coherent state and its dephased mixture are A1-equivalent; the "
                "phase capability is again E3-style only relative to A1 without reference."
            ),
            left_state="plus",
            right_state="maximally_mixed",
            packet=_packet("symmetric_mixed_state_control"),
        ),
    )


def run() -> dict[str, Any]:
    audits = [evaluate_candidate(candidate) for candidate in candidates()]
    admitted = [item for item in audits if item["admitted_e3_relative_to_a1"]]
    a2 = next(item for item in audits if item["candidate_id"] == "z2_phase_pair_a2_reference")
    main = next(item for item in audits if item["candidate_id"] == "z2_phase_pair_a1_no_reference")
    return {
        "artifact": ARTIFACT,
        "source_taxonomy": SOURCE_TAXONOMY,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "purpose": (
            "Make the quantum E3 admissible-menu hinge explicit after the T433 "
            "classical C-fragment proof certificate."
        ),
        "gate_requirements": [
            "finite quantum regime",
            "predeclared symmetry/superselection packet",
            "one shared symmetry rule across the pair",
            "admissible class A is named",
            "A1 statistics are equal",
            "separator is predeclared and capability-separating",
            "separator does not commute with the symmetry",
            "no A2 reference/asymmetry resource is admitted",
            "no hidden case label or post-hoc selector is used",
        ],
        "candidate_audits": audits,
        "overall_verdict": {
            "verdict": VERDICT,
            "main_pair_admitted_e3_relative_to_A1": main["admitted_e3_relative_to_a1"],
            "same_pair_A2_declared": (
                a2["residue_label"] == "E0_DECLARED_RELATIVE_TO_A2_REFERENCE_RESOURCE"
            ),
            "admitted_e3_candidate_ids": [item["candidate_id"] for item in admitted],
            "reading": (
                "T435 supplies a finite A-class control for the taxonomy: a relative "
                "phase datum can be structurally inaccessible to A1 symmetry-respecting "
                "menus, while the same datum becomes E0-declared when A2 admits the "
                "reference/asymmetry resource. This is a gate shape only, not a "
                "physics theorem or claim promotion."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Future quantum E3 attempts must name A, the symmetry, and the reference-resource policy.",
            "Do not revive the T421 GU-adjacent adapter as stated.",
            "Treat T435 as an internal taxonomy control, not as WAY proof or external-facing physics.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    rows = [
        "| {candidate_id} | {a1_equal} | {commutes} | {e3} | {label} |".format(
            candidate_id=item["candidate_id"],
            a1_equal="yes" if item["a1_statistics_equal"] else "no",
            commutes="yes" if item["separator_commutes_with_symmetry"] else "no",
            e3="yes" if item["admitted_e3_relative_to_a1"] else "no",
            label=item["residue_label"],
        )
        for item in result["candidate_audits"]
    ]
    requirements = [f"- {item}" for item in result["gate_requirements"]]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T435 - Quantum E3 Admissible-Menu Gate - v0.1 results",
            "",
            "> Recorded-tier taxonomy/admission gate. `TESTS.md`, `ROADMAP.md`, "
            "and `CLAIM-LEDGER.md` are untouched. No claim promotion. This is not "
            "a WAY theorem, not a GU adapter, and not cross-repo evidence.",
            "",
            "- Spec (frozen first): `tests/T435-quantum-e3-admissible-menu-gate.md`",
            "- Model: `models/quantum_e3_admissible_menu_gate.py`",
            "- Tests: `tests/test_quantum_e3_admissible_menu_gate.py`",
            "- Artifact JSON: `results/T435-quantum-e3-admissible-menu-gate-v0.1.json`",
            "- Run: `python -m pytest tests/test_quantum_e3_admissible_menu_gate.py -q`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Gate Requirements",
            "",
            *requirements,
            "",
            "## Candidate Audit",
            "",
            "| candidate | A1 equal? | separator commutes? | E3 relative to A1? | residue label |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: an internal finite A-class control for the taxonomy's quantum "
            "E3 hinge. The same phase datum is E3-style relative to A1 without a "
            "reference resource and E0-declared relative to A2 with that resource.",
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
        json_path = results_dir / "T435-quantum-e3-admissible-menu-gate-v0.1.json"
        md_path = results_dir / "T435-quantum-e3-admissible-menu-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
