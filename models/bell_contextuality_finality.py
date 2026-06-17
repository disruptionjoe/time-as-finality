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
from math import cos, pi, sqrt


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


@dataclass(frozen=True)
class CorrelationContext:
    name: str
    left: str
    right: str
    correlation: float
    model_type: str

    @property
    def same_probability(self) -> float:
        return (1.0 + self.correlation) / 2.0

    @property
    def different_probability(self) -> float:
        return (1.0 - self.correlation) / 2.0


@dataclass(frozen=True)
class CHSHProbabilityModel:
    name: str
    model_type: str
    contexts: tuple[CorrelationContext, ...]
    global_assignment_available: bool
    no_signalling: bool
    description: str

    @property
    def chsh_score(self) -> float:
        values = {context.name: context.correlation for context in self.contexts}
        return values["A0B0"] + values["A0B1"] + values["A1B0"] - values["A1B1"]

    @property
    def finality_status(self) -> str:
        if self.global_assignment_available:
            return "global_noncontextual_section_available"
        return "local_sections_without_global_assignment"


@dataclass(frozen=True)
class ProbabilityComparisonResult:
    models: tuple[CHSHProbabilityModel, ...]
    classical_bound: float
    tsirelson_bound: float
    no_signalling_bound: float
    quantum_exceeds_classical: bool
    quantum_respects_tsirelson: bool
    pr_box_exceeds_tsirelson: bool


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
    probability_result = compare_probability_models()
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
        "probability_models": {
            "bounds": {
                "classical": probability_result.classical_bound,
                "tsirelson": probability_result.tsirelson_bound,
                "no_signalling": probability_result.no_signalling_bound,
            },
            "models": [
                {
                    "name": model.name,
                    "model_type": model.model_type,
                    "description": model.description,
                    "chsh_score": model.chsh_score,
                    "global_assignment_available": model.global_assignment_available,
                    "no_signalling": model.no_signalling,
                    "finality_status": model.finality_status,
                    "contexts": [
                        {
                            "name": context.name,
                            "left": context.left,
                            "right": context.right,
                            "correlation": context.correlation,
                            "same_probability": context.same_probability,
                            "different_probability": context.different_probability,
                        }
                        for context in model.contexts
                    ],
                }
                for model in probability_result.models
            ],
            "checks": {
                "quantum_exceeds_classical": probability_result.quantum_exceeds_classical,
                "quantum_respects_tsirelson": probability_result.quantum_respects_tsirelson,
                "pr_box_exceeds_tsirelson": probability_result.pr_box_exceeds_tsirelson,
            },
        },
        "verdict": {
            "bell_chsh_mapping_constructed": True,
            "local_finality_without_global_section": result.h1_style_obstruction,
            "contextuality_certificate_detected": result.no_global_assignment,
            "physical_referent_is_structural_not_probabilistic": True,
            "probability_bearing_chsh_model_added": True,
            "classical_quantum_pr_separation_detected": (
                probability_result.quantum_exceeds_classical
                and probability_result.quantum_respects_tsirelson
                and probability_result.pr_box_exceeds_tsirelson
            ),
        },
    }


def classical_deterministic_model() -> CHSHProbabilityModel:
    # One global assignment: A0=A1=B0=B1=+1. This saturates the
    # classical CHSH bound and provides the noncontextual baseline.
    contexts = (
        CorrelationContext("A0B0", "A0", "B0", 1.0, "classical"),
        CorrelationContext("A0B1", "A0", "B1", 1.0, "classical"),
        CorrelationContext("A1B0", "A1", "B0", 1.0, "classical"),
        CorrelationContext("A1B1", "A1", "B1", 1.0, "classical"),
    )
    return CHSHProbabilityModel(
        name="classical_global_assignment",
        model_type="classical_noncontextual",
        contexts=contexts,
        global_assignment_available=True,
        no_signalling=True,
        description="A deterministic hidden-variable assignment with CHSH score 2.",
    )


def quantum_tsirelson_model() -> CHSHProbabilityModel:
    angles = {
        "A0B0": (0.0, pi / 4),
        "A0B1": (0.0, -pi / 4),
        "A1B0": (pi / 2, pi / 4),
        "A1B1": (pi / 2, -pi / 4),
    }
    contexts = tuple(
        CorrelationContext(
            name=name,
            left=name[:2],
            right=name[2:],
            correlation=cos(left_angle - right_angle),
            model_type="quantum",
        )
        for name, (left_angle, right_angle) in angles.items()
    )
    return CHSHProbabilityModel(
        name="quantum_tsirelson_target",
        model_type="quantum_contextual",
        contexts=contexts,
        global_assignment_available=False,
        no_signalling=True,
        description="Angle correlations giving CHSH score 2*sqrt(2).",
    )


def pr_box_model() -> CHSHProbabilityModel:
    contexts = (
        CorrelationContext("A0B0", "A0", "B0", 1.0, "pr_box"),
        CorrelationContext("A0B1", "A0", "B1", 1.0, "pr_box"),
        CorrelationContext("A1B0", "A1", "B0", 1.0, "pr_box"),
        CorrelationContext("A1B1", "A1", "B1", -1.0, "pr_box"),
    )
    return CHSHProbabilityModel(
        name="pr_box_no_signalling_extreme",
        model_type="post_quantum_no_signalling",
        contexts=contexts,
        global_assignment_available=False,
        no_signalling=True,
        description="No-signalling extremal correlations with CHSH score 4.",
    )


def compare_probability_models() -> ProbabilityComparisonResult:
    models = (
        classical_deterministic_model(),
        quantum_tsirelson_model(),
        pr_box_model(),
    )
    classical_bound = 2.0
    tsirelson_bound = 2.0 * sqrt(2.0)
    no_signalling_bound = 4.0
    quantum = models[1]
    pr_box = models[2]
    tolerance = 1e-9
    return ProbabilityComparisonResult(
        models=models,
        classical_bound=classical_bound,
        tsirelson_bound=tsirelson_bound,
        no_signalling_bound=no_signalling_bound,
        quantum_exceeds_classical=quantum.chsh_score > classical_bound,
        quantum_respects_tsirelson=abs(quantum.chsh_score - tsirelson_bound) < tolerance,
        pr_box_exceeds_tsirelson=pr_box.chsh_score > tsirelson_bound,
    )


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
