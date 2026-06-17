"""T21: Bell/CHSH mapping for finality sheaf obstruction.

This lab builds a finite contextuality model for the T13 sheaf idea. It uses
the standard CHSH parity pattern: four local measurement contexts are each
locally satisfiable, but no single global assignment satisfies all of them.

The result is a structural Bell-style certificate, not a quantum simulation.
It maps the no-global-hidden-variable assignment to the TaF claim that local
finality sections need not glue into a global finality section.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


Outcome = int


@dataclass(frozen=True)
class MeasurementSetting:
    name: str
    party: str


@dataclass(frozen=True)
class MeasurementContext:
    name: str
    left: MeasurementSetting
    right: MeasurementSetting
    parity: Outcome
    finality_score: int = 1

    def is_satisfied_by(self, assignment: dict[str, Outcome]) -> bool:
        return assignment[self.left.name] * assignment[self.right.name] == self.parity


@dataclass(frozen=True)
class LocalFinalitySection:
    context: MeasurementContext
    assignments: tuple[tuple[Outcome, Outcome], ...]
    finality_score: int

    @property
    def variables(self) -> tuple[str, str]:
        return (self.context.left.name, self.context.right.name)

    @property
    def relation(self) -> str:
        return "same" if self.context.parity == 1 else "different"


@dataclass(frozen=True)
class CHSHFinalityScenario:
    name: str
    settings: tuple[MeasurementSetting, ...]
    contexts: tuple[MeasurementContext, ...]


@dataclass(frozen=True)
class ContextualityWitness:
    parity_product: Outcome
    expected_noncontextual_product: Outcome
    contradiction: str


@dataclass(frozen=True)
class CHSHFinalityAnalysis:
    scenario: CHSHFinalityScenario
    local_sections: tuple[LocalFinalitySection, ...]
    all_local_sections_exist: bool
    no_global_assignment: bool
    contextuality_witness: ContextualityWitness
    compatible_on_named_overlaps: bool
    h1_style_obstruction: bool
    physical_interpretation: str


def canonical_chsh_finality_scenario() -> CHSHFinalityScenario:
    a0 = MeasurementSetting("A0", "Alice")
    a1 = MeasurementSetting("A1", "Alice")
    b0 = MeasurementSetting("B0", "Bob")
    b1 = MeasurementSetting("B1", "Bob")
    return CHSHFinalityScenario(
        name="canonical_chsh_finality_obstruction",
        settings=(a0, a1, b0, b1),
        contexts=(
            MeasurementContext("A0B0", a0, b0, 1),
            MeasurementContext("A0B1", a0, b1, 1),
            MeasurementContext("A1B0", a1, b0, 1),
            MeasurementContext("A1B1", a1, b1, -1),
        ),
    )


def local_section_for_context(context: MeasurementContext) -> LocalFinalitySection:
    assignments = tuple(
        (left, right)
        for left, right in product((-1, 1), repeat=2)
        if left * right == context.parity
    )
    return LocalFinalitySection(
        context=context,
        assignments=assignments,
        finality_score=context.finality_score,
    )


def analyze_chsh_finality(
    scenario: CHSHFinalityScenario | None = None,
) -> CHSHFinalityAnalysis:
    chosen = scenario or canonical_chsh_finality_scenario()
    local_sections = tuple(local_section_for_context(context) for context in chosen.contexts)
    all_local = all(section.assignments for section in local_sections)
    no_global = not _global_assignment_exists(chosen)
    witness = _contextuality_witness(chosen)
    return CHSHFinalityAnalysis(
        scenario=chosen,
        local_sections=local_sections,
        all_local_sections_exist=all_local,
        no_global_assignment=no_global,
        contextuality_witness=witness,
        compatible_on_named_overlaps=_compatible_on_named_overlaps(local_sections),
        h1_style_obstruction=all_local and no_global,
        physical_interpretation=(
            "Each measurement context supports local finality, but the four "
            "contexts cannot be glued into one global assignment of outcomes."
        ),
    )


def run_t21_analysis() -> dict[str, object]:
    result = analyze_chsh_finality()
    return {
        "scenario": {
            "name": result.scenario.name,
            "settings": [
                {"name": setting.name, "party": setting.party}
                for setting in result.scenario.settings
            ],
            "contexts": [
                {
                    "name": context.name,
                    "left": context.left.name,
                    "right": context.right.name,
                    "parity": context.parity,
                    "relation": "same" if context.parity == 1 else "different",
                    "finality_score": context.finality_score,
                }
                for context in result.scenario.contexts
            ],
        },
        "local_sections": [
            {
                "context": section.context.name,
                "variables": list(section.variables),
                "relation": section.relation,
                "assignments": [list(item) for item in section.assignments],
                "finality_score": section.finality_score,
            }
            for section in result.local_sections
        ],
        "checks": {
            "all_local_sections_exist": result.all_local_sections_exist,
            "compatible_on_named_overlaps": result.compatible_on_named_overlaps,
            "no_global_assignment": result.no_global_assignment,
            "h1_style_obstruction": result.h1_style_obstruction,
        },
        "contextuality_witness": {
            "parity_product": result.contextuality_witness.parity_product,
            "expected_noncontextual_product": (
                result.contextuality_witness.expected_noncontextual_product
            ),
            "contradiction": result.contextuality_witness.contradiction,
        },
        "interpretation": {
            "physical_interpretation": result.physical_interpretation,
            "bell_mapping": (
                "The product of observed context parities is -1, while any "
                "global hidden-variable assignment would force product +1."
            ),
            "taf_mapping": (
                "Local finality sections exist for all contexts, but no global "
                "finality section exists."
            ),
            "guardrail": (
                "This is a finite contextuality certificate, not a simulation "
                "of quantum amplitudes or a derivation of Bell probabilities."
            ),
        },
        "verdict": {
            "bell_chsh_mapping_constructed": True,
            "local_finality_without_global_section": result.h1_style_obstruction,
            "contextuality_certificate_detected": result.no_global_assignment,
            "physical_referent_is_structural_not_probabilistic": True,
        },
    }


def _global_assignment_exists(scenario: CHSHFinalityScenario) -> bool:
    setting_names = [setting.name for setting in scenario.settings]
    for values in product((-1, 1), repeat=len(setting_names)):
        assignment = dict(zip(setting_names, values))
        if all(context.is_satisfied_by(assignment) for context in scenario.contexts):
            return True
    return False


def _contextuality_witness(scenario: CHSHFinalityScenario) -> ContextualityWitness:
    parity_product = 1
    for context in scenario.contexts:
        parity_product *= context.parity
    return ContextualityWitness(
        parity_product=parity_product,
        expected_noncontextual_product=1,
        contradiction=(
            "Multiplying all four context equations gives -1 on the observed "
            "side, but every global assignment squares each variable and gives +1."
        ),
    )


def _compatible_on_named_overlaps(
    sections: tuple[LocalFinalitySection, ...],
) -> bool:
    # In the CHSH cover, contexts overlap by one named measurement setting.
    # Each local section permits both outcomes for each single setting, so
    # restrictions to named single-setting overlaps agree.
    possible_by_variable: dict[str, set[Outcome]] = {}
    for section in sections:
        for variable_index, variable in enumerate(section.variables):
            outcomes = {assignment[variable_index] for assignment in section.assignments}
            if variable in possible_by_variable and possible_by_variable[variable] != outcomes:
                return False
            possible_by_variable[variable] = outcomes
    return True
