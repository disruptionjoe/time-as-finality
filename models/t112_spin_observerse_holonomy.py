"""T112: spin-observerse holonomy Step 2 finite/proxy audit.

This module formalizes the bounded audit requested by T112. It does not
validate Geometric Unity physics and it does not derive quantum probabilities.
It checks whether the CHSH 4-cycle can be represented by a finite spin-lift
proxy whose Z/2 phase matches the T63 Cech representative, while preserving the
T65 controls:

* naive observerse Y has no nontrivial loop in this fixture;
* Y_spin supplies only a candidate Z/2 host;
* the CHSH phase/sign is computed under a declared angle convention;
* local causality implies holonomy +1, but holonomy +1 does not imply local
  causality;
* probabilistic CHSH holonomy is representative-dependent outside the declared
  majority representative family.

The final theorem statement remains conditional under H3: the finite Cech
transition function is identified with spin holonomy only if the declared
spin-loop embedding is accepted.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import cos, isclose, pi, sin, sqrt
from typing import Iterable


Outcome = int
Section = dict[str, tuple[Outcome, Outcome]]


CONTEXTS = ("A0B0", "A0B1", "A1B1", "A1B0")
LOOP_EDGES = (
    ("A0B0", "A0B1"),
    ("A0B1", "A1B1"),
    ("A1B1", "A1B0"),
    ("A1B0", "A0B0"),
)
SHARED_SETTING = {
    ("A0B0", "A0B1"): "Alice_A0",
    ("A0B1", "A1B1"): "Bob_B1",
    ("A1B1", "A1B0"): "Alice_A1",
    ("A1B0", "A0B0"): "Bob_B0",
}
OUTCOMES = (+1, -1)


@dataclass(frozen=True)
class AngleConvention:
    """Declared CHSH angle and spin-lift convention."""

    name: str
    alice_a0: float
    alice_a1: float
    bob_b0: float
    bob_b1: float
    chsh_formula: str
    spin_lift_rule: str


@dataclass(frozen=True)
class TopologyProxyAudit:
    naive_y_pi1_order: int
    naive_y_nontrivial_z2_holonomy_available: bool
    spin_lift_pi1_order: int
    spin_lift_z2_candidate_available: bool
    verdict: str


@dataclass(frozen=True)
class PhaseAudit:
    convention: AngleConvention
    edge_angle_changes: tuple[tuple[str, str, float], ...]
    positive_generator_total_angle: float
    positive_generator_phase: tuple[float, float]
    positive_generator_z2_sign: int
    signed_closed_total_angle: float
    signed_closed_z2_sign: int
    convention_is_load_bearing: bool
    verdict: str


@dataclass(frozen=True)
class CHSHAudit:
    correlations: dict[str, float]
    chsh_value: float
    abs_chsh_matches_tsirelson: bool
    majority_section_count: int
    majority_holonomies: tuple[int, ...]
    canonical_majority_section: Section
    canonical_transition_pattern: tuple[int, int, int, int]
    canonical_holonomy: int


@dataclass(frozen=True)
class CausalControlAudit:
    total_sections: int
    locally_causal_sections: int
    locally_causal_all_holonomy_plus_one: bool
    holonomy_plus_one_sections: int
    non_lc_holonomy_plus_one_sections: int
    biconditional_restored: bool
    example_non_lc_holonomy_plus_one: Section
    example_non_lc_transition_pattern: tuple[int, int, int, int]


@dataclass(frozen=True)
class RepresentativeControlAudit:
    all_support_sections: int
    all_support_holonomy_counts: dict[int, int]
    majority_representatives_all_holonomy_minus_one: bool
    arbitrary_support_has_holonomy_plus_one: bool
    arbitrary_support_has_holonomy_minus_one: bool
    representative_dependence_present: bool
    example_support_holonomy_plus_one: Section
    example_support_holonomy_minus_one: Section
    verdict: str


@dataclass(frozen=True)
class T112AuditResult:
    topology: TopologyProxyAudit
    phase: PhaseAudit
    chsh: CHSHAudit
    causal_control: CausalControlAudit
    representative_control: RepresentativeControlAudit
    finite_proxy_passed: bool
    h3_status: str
    strongest_conditional_claim: str
    not_claimed: tuple[str, ...]
    open_blocker: str
    recommended_next: str
    claim_boundary: str


def default_angle_convention() -> AngleConvention:
    return AngleConvention(
        name="T112_standard_chsh_positive_generator_spin_lift",
        alice_a0=0.0,
        alice_a1=pi / 2.0,
        bob_b0=pi / 4.0,
        bob_b1=-pi / 4.0,
        chsh_formula="S = E00 + E01 + E10 - E11 for singlet Eij = -cos(Ai-Bj)",
        spin_lift_rule=(
            "Each detector-setting change is lifted as a positive pi/2 "
            "generator step in the spin frame; four changes give total 2*pi. "
            "This is a finite proxy convention, not an unconstrained solid-angle "
            "theorem."
        ),
    )


def run_t112_audit(
    convention: AngleConvention | None = None,
) -> T112AuditResult:
    convention = convention or default_angle_convention()
    topology = audit_topology_proxy()
    phase = audit_phase_proxy(convention)
    chsh = audit_chsh(convention)
    causal = audit_causal_controls()
    representative = audit_representative_controls(convention)

    finite_proxy_passed = (
        not topology.naive_y_nontrivial_z2_holonomy_available
        and topology.spin_lift_z2_candidate_available
        and phase.positive_generator_z2_sign == -1
        and phase.signed_closed_z2_sign == +1
        and chsh.canonical_holonomy == -1
        and phase.positive_generator_z2_sign == chsh.canonical_holonomy
        and causal.locally_causal_all_holonomy_plus_one
        and not causal.biconditional_restored
        and representative.representative_dependence_present
    )

    return T112AuditResult(
        topology=topology,
        phase=phase,
        chsh=chsh,
        causal_control=causal,
        representative_control=representative,
        finite_proxy_passed=finite_proxy_passed,
        h3_status=(
            "conditional: H3 must identify the finite Cech transition "
            "cochain with the declared Y_spin spin-holonomy loop"
        ),
        strongest_conditional_claim=(
            "Under H3 and the declared positive-generator spin-lift convention, "
            "the CHSH majority-representative Cech holonomy -1 is realized by "
            "the Z/2 spin-lift candidate phase -1. The naive observerse Y "
            "control blocks the same claim without the spin lift."
        ),
        not_claimed=(
            "GU physics is validated",
            "quantum probabilities or Tsirelson's bound are derived from TaF",
            "all contextuality is spin holonomy",
            "holonomy +1 is equivalent to local causality",
            "the signed closed detector path has phase -1 without the declared lift",
        ),
        open_blocker=(
            "The continuous bipartite Berry/solid-angle theorem is still not "
            "proved. This artifact only audits the finite spin-lift proxy and "
            "makes the H3/convention dependence explicit."
        ),
        recommended_next=(
            "If promoted, replace the finite positive-generator proxy with a "
            "continuous spin-frame path theorem whose solid angle and orientation "
            "are invariantly specified."
        ),
        claim_boundary=(
            "T112 sharpens the T63 dictionary conditionally. It preserves T65's "
            "one-way causal reading and leaves the false LC iff holonomy +1 "
            "biconditional false."
        ),
    )


def audit_topology_proxy() -> TopologyProxyAudit:
    return TopologyProxyAudit(
        naive_y_pi1_order=1,
        naive_y_nontrivial_z2_holonomy_available=False,
        spin_lift_pi1_order=2,
        spin_lift_z2_candidate_available=True,
        verdict=(
            "Naive Y is the negative control; only the spin lift supplies a "
            "Z/2 candidate host for the loop."
        ),
    )


def audit_phase_proxy(convention: AngleConvention) -> PhaseAudit:
    edge_changes = _edge_angle_changes(convention)
    positive_total = sum(abs(change) for _, _, change in edge_changes)
    positive_phase = (cos(positive_total / 2.0), sin(positive_total / 2.0))
    positive_sign = _phase_to_z2_sign(positive_phase)

    signed_total = sum(change for _, _, change in edge_changes)
    signed_phase = (cos(signed_total / 2.0), sin(signed_total / 2.0))
    signed_sign = _phase_to_z2_sign(signed_phase)

    return PhaseAudit(
        convention=convention,
        edge_angle_changes=edge_changes,
        positive_generator_total_angle=positive_total,
        positive_generator_phase=positive_phase,
        positive_generator_z2_sign=positive_sign,
        signed_closed_total_angle=signed_total,
        signed_closed_z2_sign=signed_sign,
        convention_is_load_bearing=positive_sign != signed_sign,
        verdict=(
            "The declared positive-generator spin lift gives phase -1. The "
            "signed closed-angle control gives +1, so the lift convention and "
            "H3 identification are load-bearing."
        ),
    )


def audit_chsh(convention: AngleConvention) -> CHSHAudit:
    angles = _context_angles(convention)
    correlations = {
        context: -cos(alice - bob)
        for context, (alice, bob) in angles.items()
    }
    chsh_value = (
        correlations["A0B0"]
        + correlations["A0B1"]
        + correlations["A1B0"]
        - correlations["A1B1"]
    )
    majority_sections = most_probable_sections(convention)
    majority_holonomies = tuple(holonomy(section) for section in majority_sections)
    canonical = majority_sections[0]
    return CHSHAudit(
        correlations=correlations,
        chsh_value=chsh_value,
        abs_chsh_matches_tsirelson=isclose(abs(chsh_value), 2.0 * sqrt(2.0), abs_tol=1e-12),
        majority_section_count=len(majority_sections),
        majority_holonomies=tuple(sorted(set(majority_holonomies))),
        canonical_majority_section=canonical,
        canonical_transition_pattern=transition_pattern(canonical),
        canonical_holonomy=holonomy(canonical),
    )


def audit_causal_controls() -> CausalControlAudit:
    sections = tuple(all_deterministic_sections())
    lc_sections = tuple(section for section in sections if is_locally_causal(section))
    hol_plus = tuple(section for section in sections if holonomy(section) == +1)
    non_lc_hol_plus = tuple(
        section for section in hol_plus if not is_locally_causal(section)
    )
    example = non_lc_hol_plus[0]
    return CausalControlAudit(
        total_sections=len(sections),
        locally_causal_sections=len(lc_sections),
        locally_causal_all_holonomy_plus_one=all(
            holonomy(section) == +1 for section in lc_sections
        ),
        holonomy_plus_one_sections=len(hol_plus),
        non_lc_holonomy_plus_one_sections=len(non_lc_hol_plus),
        biconditional_restored=len(hol_plus) == len(lc_sections),
        example_non_lc_holonomy_plus_one=example,
        example_non_lc_transition_pattern=transition_pattern(example),
    )


def audit_representative_controls(
    convention: AngleConvention,
) -> RepresentativeControlAudit:
    sections = tuple(all_deterministic_sections())
    counts = {
        -1: sum(1 for section in sections if holonomy(section) == -1),
        +1: sum(1 for section in sections if holonomy(section) == +1),
    }
    majority = most_probable_sections(convention)
    majority_all_minus = all(holonomy(section) == -1 for section in majority)
    plus_example = next(section for section in sections if holonomy(section) == +1)
    minus_example = next(section for section in sections if holonomy(section) == -1)
    representative_dependence = counts[-1] > 0 and counts[+1] > 0
    return RepresentativeControlAudit(
        all_support_sections=len(sections),
        all_support_holonomy_counts=counts,
        majority_representatives_all_holonomy_minus_one=majority_all_minus,
        arbitrary_support_has_holonomy_plus_one=counts[+1] > 0,
        arbitrary_support_has_holonomy_minus_one=counts[-1] > 0,
        representative_dependence_present=representative_dependence,
        example_support_holonomy_plus_one=plus_example,
        example_support_holonomy_minus_one=minus_example,
        verdict=(
            "All maximum-probability representatives for the declared CHSH "
            "angles have holonomy -1, but the full nonzero support contains "
            "both holonomy classes. The probabilistic CHSH holonomy statement "
            "is therefore representative-qualified."
        ),
    )


def most_probable_sections(convention: AngleConvention) -> tuple[Section, ...]:
    choices_by_context: list[tuple[tuple[Outcome, Outcome], ...]] = []
    for context in CONTEXTS:
        alice, bob = _context_angles(convention)[context]
        probabilities = [
            ((a_out, b_out), quantum_probability(alice, bob, a_out, b_out))
            for a_out, b_out in product(OUTCOMES, OUTCOMES)
        ]
        best = max(probability for _, probability in probabilities)
        choices = tuple(
            outcome_pair
            for outcome_pair, probability in probabilities
            if isclose(probability, best, abs_tol=1e-12)
        )
        choices_by_context.append(choices)

    return tuple(
        dict(zip(CONTEXTS, combo)) for combo in product(*choices_by_context)
    )


def quantum_probability(
    alice_angle: float,
    bob_angle: float,
    alice_outcome: Outcome,
    bob_outcome: Outcome,
) -> float:
    correlation = -cos(alice_angle - bob_angle)
    return (1.0 + alice_outcome * bob_outcome * correlation) / 4.0


def all_deterministic_sections() -> Iterable[Section]:
    local_pairs = tuple(product(OUTCOMES, OUTCOMES))
    for combo in product(local_pairs, repeat=len(CONTEXTS)):
        yield dict(zip(CONTEXTS, combo))


def is_locally_causal(section: Section) -> bool:
    return (
        section["A0B0"][0] == section["A0B1"][0]
        and section["A1B1"][0] == section["A1B0"][0]
        and section["A0B0"][1] == section["A1B0"][1]
        and section["A0B1"][1] == section["A1B1"][1]
    )


def transition_pattern(section: Section) -> tuple[int, int, int, int]:
    return tuple(
        transition_function(section[left], left, section[right], right)
        for left, right in LOOP_EDGES
    )


def holonomy(section: Section) -> int:
    value = 1
    for transition in transition_pattern(section):
        value *= transition
    return value


def transition_function(
    left_section: tuple[Outcome, Outcome],
    left_context: str,
    right_section: tuple[Outcome, Outcome],
    right_context: str,
) -> int:
    shared = SHARED_SETTING[(left_context, right_context)]
    left = _shared_outcome(left_section, shared)
    right = _shared_outcome(right_section, shared)
    return +1 if left == right else -1


def t112_result_to_dict(result: T112AuditResult) -> dict[str, object]:
    return {
        "topology": {
            "naive_y_pi1_order": result.topology.naive_y_pi1_order,
            "naive_y_nontrivial_z2_holonomy_available": (
                result.topology.naive_y_nontrivial_z2_holonomy_available
            ),
            "spin_lift_pi1_order": result.topology.spin_lift_pi1_order,
            "spin_lift_z2_candidate_available": (
                result.topology.spin_lift_z2_candidate_available
            ),
            "verdict": result.topology.verdict,
        },
        "phase": {
            "convention": {
                "name": result.phase.convention.name,
                "alice_a0": result.phase.convention.alice_a0,
                "alice_a1": result.phase.convention.alice_a1,
                "bob_b0": result.phase.convention.bob_b0,
                "bob_b1": result.phase.convention.bob_b1,
                "chsh_formula": result.phase.convention.chsh_formula,
                "spin_lift_rule": result.phase.convention.spin_lift_rule,
            },
            "edge_angle_changes": [
                {
                    "edge": edge,
                    "party": party,
                    "signed_delta_radians": delta,
                }
                for edge, party, delta in result.phase.edge_angle_changes
            ],
            "positive_generator_total_angle": (
                result.phase.positive_generator_total_angle
            ),
            "positive_generator_phase": list(result.phase.positive_generator_phase),
            "positive_generator_z2_sign": result.phase.positive_generator_z2_sign,
            "signed_closed_total_angle": result.phase.signed_closed_total_angle,
            "signed_closed_z2_sign": result.phase.signed_closed_z2_sign,
            "convention_is_load_bearing": result.phase.convention_is_load_bearing,
            "verdict": result.phase.verdict,
        },
        "chsh": {
            "correlations": result.chsh.correlations,
            "chsh_value": result.chsh.chsh_value,
            "abs_chsh_matches_tsirelson": result.chsh.abs_chsh_matches_tsirelson,
            "majority_section_count": result.chsh.majority_section_count,
            "majority_holonomies": list(result.chsh.majority_holonomies),
            "canonical_majority_section": _section_to_dict(
                result.chsh.canonical_majority_section
            ),
            "canonical_transition_pattern": list(
                result.chsh.canonical_transition_pattern
            ),
            "canonical_holonomy": result.chsh.canonical_holonomy,
        },
        "causal_control": {
            "total_sections": result.causal_control.total_sections,
            "locally_causal_sections": result.causal_control.locally_causal_sections,
            "locally_causal_all_holonomy_plus_one": (
                result.causal_control.locally_causal_all_holonomy_plus_one
            ),
            "holonomy_plus_one_sections": (
                result.causal_control.holonomy_plus_one_sections
            ),
            "non_lc_holonomy_plus_one_sections": (
                result.causal_control.non_lc_holonomy_plus_one_sections
            ),
            "biconditional_restored": result.causal_control.biconditional_restored,
            "example_non_lc_holonomy_plus_one": _section_to_dict(
                result.causal_control.example_non_lc_holonomy_plus_one
            ),
            "example_non_lc_transition_pattern": list(
                result.causal_control.example_non_lc_transition_pattern
            ),
        },
        "representative_control": {
            "all_support_sections": result.representative_control.all_support_sections,
            "all_support_holonomy_counts": {
                str(key): value
                for key, value in result.representative_control.all_support_holonomy_counts.items()
            },
            "majority_representatives_all_holonomy_minus_one": (
                result.representative_control.majority_representatives_all_holonomy_minus_one
            ),
            "arbitrary_support_has_holonomy_plus_one": (
                result.representative_control.arbitrary_support_has_holonomy_plus_one
            ),
            "arbitrary_support_has_holonomy_minus_one": (
                result.representative_control.arbitrary_support_has_holonomy_minus_one
            ),
            "representative_dependence_present": (
                result.representative_control.representative_dependence_present
            ),
            "example_support_holonomy_plus_one": _section_to_dict(
                result.representative_control.example_support_holonomy_plus_one
            ),
            "example_support_holonomy_minus_one": _section_to_dict(
                result.representative_control.example_support_holonomy_minus_one
            ),
            "verdict": result.representative_control.verdict,
        },
        "finite_proxy_passed": result.finite_proxy_passed,
        "h3_status": result.h3_status,
        "strongest_conditional_claim": result.strongest_conditional_claim,
        "not_claimed": list(result.not_claimed),
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
        "claim_boundary": result.claim_boundary,
    }


def _context_angles(convention: AngleConvention) -> dict[str, tuple[float, float]]:
    return {
        "A0B0": (convention.alice_a0, convention.bob_b0),
        "A0B1": (convention.alice_a0, convention.bob_b1),
        "A1B1": (convention.alice_a1, convention.bob_b1),
        "A1B0": (convention.alice_a1, convention.bob_b0),
    }


def _edge_angle_changes(
    convention: AngleConvention,
) -> tuple[tuple[str, str, float], ...]:
    return (
        (
            "A0B0->A0B1",
            "Bob",
            _principal_delta(convention.bob_b0, convention.bob_b1),
        ),
        (
            "A0B1->A1B1",
            "Alice",
            _principal_delta(convention.alice_a0, convention.alice_a1),
        ),
        (
            "A1B1->A1B0",
            "Bob",
            _principal_delta(convention.bob_b1, convention.bob_b0),
        ),
        (
            "A1B0->A0B0",
            "Alice",
            _principal_delta(convention.alice_a1, convention.alice_a0),
        ),
    )


def _principal_delta(start: float, end: float) -> float:
    delta = (end - start + pi) % (2.0 * pi) - pi
    if isclose(delta, -pi, abs_tol=1e-12):
        return pi
    return delta


def _phase_to_z2_sign(phase: tuple[float, float]) -> int:
    real, imaginary = phase
    if isclose(real, -1.0, abs_tol=1e-12) and isclose(imaginary, 0.0, abs_tol=1e-12):
        return -1
    if isclose(real, +1.0, abs_tol=1e-12) and isclose(imaginary, 0.0, abs_tol=1e-12):
        return +1
    raise ValueError(f"phase is not in the Z/2 subgroup: {phase}")


def _shared_outcome(section: tuple[Outcome, Outcome], shared_label: str) -> Outcome:
    alice_outcome, bob_outcome = section
    return alice_outcome if shared_label.startswith("Alice") else bob_outcome


def _section_to_dict(section: Section) -> dict[str, list[int]]:
    return {context: [int(a), int(b)] for context, (a, b) in section.items()}


if __name__ == "__main__":
    import json

    print(json.dumps(t112_result_to_dict(run_t112_audit()), indent=2))
