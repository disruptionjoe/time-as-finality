"""T107: finite loss-relocation audit.

The motivating conjecture is not a conservation law. It is the weaker and
more testable claim that structure forgotten by a projection can reappear as a
target-side reconstruction debt, constraint surface, admissibility obligation,
or absorbed freedom.

This module derives those relocations from finite preimage fibers. The witness
obligation is not attached as metadata: it is computed from source lifts whose
target-visible behavior cannot be judged from the projected state alone.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable


AxisValue = str | int | bool


@dataclass(frozen=True)
class SourceState:
    state_id: str
    target_id: str
    axes: tuple[tuple[str, AxisValue], ...]

    def axis(self, name: str) -> AxisValue:
        for axis_name, value in self.axes:
            if axis_name == name:
                return value
        raise KeyError(name)


@dataclass(frozen=True)
class ProjectionScenario:
    name: str
    lost_axis: str
    displaced_form: str
    source_states: tuple[SourceState, ...]
    target_pair: tuple[str, str]
    source_rule_name: str
    source_rule: Callable[[SourceState, SourceState], bool]
    expected_reading: str


@dataclass(frozen=True)
class LiftJudgment:
    left_source: str
    right_source: str
    allowed: bool


@dataclass(frozen=True)
class RelocationVerdict:
    scenario: str
    lost_axis: str
    displaced_form: str
    target_pair: tuple[str, str]
    lift_judgments: tuple[LiftJudgment, ...]
    hidden_values: tuple[AxisValue, ...]
    derived_witness_pairs: tuple[tuple[str, str], ...]
    relocation_class: str
    source_rule_name: str
    expected_reading: str

    @property
    def lift_verdicts(self) -> frozenset[bool]:
        return frozenset(judgment.allowed for judgment in self.lift_judgments)


@dataclass(frozen=True)
class T107Result:
    verdicts: tuple[RelocationVerdict, ...]
    derived_debt_count: int
    stable_constraint_count: int
    absorbed_freedom_count: int
    false_conservation_rejected: bool
    source_anchored_derivation: bool
    six_axis_bridge: tuple[tuple[str, str, str], ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    tf1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _state(state_id: str, target_id: str, **axes: AxisValue) -> SourceState:
    return SourceState(
        state_id=state_id,
        target_id=target_id,
        axes=tuple(sorted(axes.items())),
    )


def scenarios() -> tuple[ProjectionScenario, ...]:
    return (
        ProjectionScenario(
            name="charge_neutrality_debt",
            lost_axis="charge",
            displaced_form="admissibility_condition",
            source_states=(
                _state("matter_plus", "matter", charge=1),
                _state("matter_minus", "matter", charge=-1),
            ),
            target_pair=("matter", "matter"),
            source_rule_name="neutral_pair_allowed",
            source_rule=lambda left, right: int(left.axis("charge")) + int(right.axis("charge")) == 0,
            expected_reading=(
                "Forgetting charge does not erase the charge rule; it creates a "
                "target-side obligation to recover a lift before judging whether "
                "the interaction is allowed."
            ),
        ),
        ProjectionScenario(
            name="spin_orientation_debt",
            lost_axis="spin",
            displaced_form="orientation_debt",
            source_states=(
                _state("spin_up", "spin_shadow", spin="up"),
                _state("spin_down", "spin_shadow", spin="down"),
            ),
            target_pair=("spin_shadow", "spin_shadow"),
            source_rule_name="opposite_spin_coupling",
            source_rule=lambda left, right: left.axis("spin") != right.axis("spin"),
            expected_reading=(
                "Forgetting spin orientation leaves a coupling judgment that "
                "depends on which hidden orientations are lifted."
            ),
        ),
        ProjectionScenario(
            name="mass_persistence_debt",
            lost_axis="mass",
            displaced_form="persistence_debt",
            source_states=(
                _state("light_body", "body", mass=1),
                _state("heavy_body", "body", mass=3),
            ),
            target_pair=("body", "body"),
            source_rule_name="combined_mass_persists",
            source_rule=lambda left, right: int(left.axis("mass")) + int(right.axis("mass")) >= 4,
            expected_reading=(
                "Forgetting mass leaves persistence/resistance as a debt: the "
                "target body cannot decide persistence without a mass lift."
            ),
        ),
        ProjectionScenario(
            name="phase_history_debt",
            lost_axis="phase",
            displaced_form="path_memory",
            source_states=(
                _state("phase_zero", "path_shadow", phase=0),
                _state("phase_pi", "path_shadow", phase=1),
            ),
            target_pair=("path_shadow", "path_shadow"),
            source_rule_name="equal_phase_interferes",
            source_rule=lambda left, right: left.axis("phase") == right.axis("phase"),
            expected_reading=(
                "Forgetting phase does not make phase irrelevant; it becomes "
                "path-memory debt for interference-sensitive judgments."
            ),
        ),
        ProjectionScenario(
            name="gauge_representative_absorbed",
            lost_axis="gauge",
            displaced_form="absorbed_freedom",
            source_states=(
                _state("gauge_rep_0", "field_shadow", gauge="g0", invariant_charge=1),
                _state("gauge_rep_1", "field_shadow", gauge="g1", invariant_charge=1),
            ),
            target_pair=("field_shadow", "field_shadow"),
            source_rule_name="same_invariant_charge",
            source_rule=lambda left, right: left.axis("invariant_charge") == right.axis("invariant_charge"),
            expected_reading=(
                "Forgetting a pure gauge representative can be harmless when "
                "the judged rule is gauge-invariant across all lifts."
            ),
        ),
        ProjectionScenario(
            name="lorentz_access_constraint",
            lost_axis="lorentz_frame",
            displaced_form="frame_constraint",
            source_states=(
                _state("event_a_frame_0", "event_a", lorentz_frame="f0", causal_access=False),
                _state("event_a_frame_1", "event_a", lorentz_frame="f1", causal_access=False),
                _state("event_b_frame_0", "event_b", lorentz_frame="f0", causal_access=False),
                _state("event_b_frame_1", "event_b", lorentz_frame="f1", causal_access=False),
            ),
            target_pair=("event_a", "event_b"),
            source_rule_name="causal_access_exists",
            source_rule=lambda left, right: bool(left.axis("causal_access") and right.axis("causal_access")),
            expected_reading=(
                "Forgetting frame labels can still leave a stable target-side "
                "constraint when every source lift denies causal access."
            ),
        ),
    )


def _fiber(scenario: ProjectionScenario, target_id: str) -> tuple[SourceState, ...]:
    return tuple(state for state in scenario.source_states if state.target_id == target_id)


def _hidden_values(states: tuple[SourceState, ...], axis: str) -> tuple[AxisValue, ...]:
    return tuple(sorted({state.axis(axis) for state in states}, key=str))


def analyze_scenario(scenario: ProjectionScenario) -> RelocationVerdict:
    left_fiber = _fiber(scenario, scenario.target_pair[0])
    right_fiber = _fiber(scenario, scenario.target_pair[1])
    lift_judgments = tuple(
        LiftJudgment(
            left_source=left.state_id,
            right_source=right.state_id,
            allowed=scenario.source_rule(left, right),
        )
        for left, right in product(left_fiber, right_fiber)
    )
    verdicts = frozenset(judgment.allowed for judgment in lift_judgments)
    hidden_values = _hidden_values(left_fiber + right_fiber, scenario.lost_axis)

    if verdicts == frozenset({True, False}):
        relocation_class = "reconstruction_debt"
        derived_witness_pairs = tuple(
            (judgment.left_source, judgment.right_source) for judgment in lift_judgments
        )
    elif verdicts == frozenset({False}):
        relocation_class = "stable_constraint_surface"
        derived_witness_pairs = ()
    elif len(hidden_values) > 1:
        relocation_class = "absorbed_freedom"
        derived_witness_pairs = ()
    else:
        relocation_class = "no_observable_relocation"
        derived_witness_pairs = ()

    return RelocationVerdict(
        scenario=scenario.name,
        lost_axis=scenario.lost_axis,
        displaced_form=scenario.displaced_form,
        target_pair=scenario.target_pair,
        lift_judgments=lift_judgments,
        hidden_values=hidden_values,
        derived_witness_pairs=derived_witness_pairs,
        relocation_class=relocation_class,
        source_rule_name=scenario.source_rule_name,
        expected_reading=scenario.expected_reading,
    )


def six_axis_bridge() -> tuple[tuple[str, str, str], ...]:
    return (
        ("L1 substrate", "lost internal coordinate", "target constraint or debt"),
        ("L2 observer", "lost resolving access", "admissibility obligation"),
        ("L3 pairing", "lost coupling channel", "provenance requirement"),
        ("L4 causal order", "lost frame/order witness", "access constraint"),
        ("L5 emergence", "lost microstate distinction", "stable equivalence class"),
        ("L6 coordination loop", "lost feedback state", "reconstruction debt"),
    )


def run_t107_analysis() -> T107Result:
    verdicts = tuple(analyze_scenario(scenario) for scenario in scenarios())
    derived_debt_count = sum(
        verdict.relocation_class == "reconstruction_debt" for verdict in verdicts
    )
    stable_constraint_count = sum(
        verdict.relocation_class == "stable_constraint_surface" for verdict in verdicts
    )
    absorbed_freedom_count = sum(
        verdict.relocation_class == "absorbed_freedom" for verdict in verdicts
    )
    source_anchored_derivation = all(
        verdict.relocation_class != "reconstruction_debt" or verdict.derived_witness_pairs
        for verdict in verdicts
    )

    return T107Result(
        verdicts=verdicts,
        derived_debt_count=derived_debt_count,
        stable_constraint_count=stable_constraint_count,
        absorbed_freedom_count=absorbed_freedom_count,
        false_conservation_rejected=absorbed_freedom_count > 0,
        source_anchored_derivation=source_anchored_derivation,
        six_axis_bridge=six_axis_bridge(),
        strongest_claim=(
            "A finite projection can relocate lost structure into target-side "
            "debt or constraint when target judgments vary across source "
            "lifts. The relocation is derived from preimage fibers, not from "
            "free-text loss labels. But there is no conservation law: gauge-like "
            "lost structure can be absorbed when every lift gives the same "
            "invariant judgment."
        ),
        improved=(
            "T107 turns the intuition 'track where lost structure goes' into a "
            "finite audit rule: inspect source lifts of a target judgment. "
            "Mixed lift verdicts derive reconstruction debt; uniform forbidden "
            "lifts derive a constraint surface; uniform invariant lifts absorb "
            "the loss."
        ),
        weakened=(
            "This weakens any strong conservation slogan. Lost structure need "
            "not reappear as a new object. It reappears only when a target-side "
            "judgment remains lift-dependent or uniformly constrained after "
            "projection."
        ),
        falsification_condition=(
            "Reject the relocation program as independent content if every "
            "derived debt is recoverable from ordinary target CSP data without "
            "source-fiber inspection, or if source-fiber inspection never "
            "separates debt, stable constraint, and absorbed freedom beyond "
            "standard provenance bookkeeping."
        ),
        tf1_update=(
            "TF1 gains a sharper candidate semantics: a LossKernel witness "
            "obligation is derivable when a target judgment has mixed verdicts "
            "over the source preimage fiber. Non-empty loss is not enough, and "
            "some loss is absorbed."
        ),
        claim_ledger_update=(
            "Add T107 to TF1: loss relocation is modeled by source-fiber lift "
            "analysis. Mixed lift verdicts produce reconstruction debt, "
            "uniform forbidden lifts produce a stable constraint surface, and "
            "uniform invariant lifts show absorbed freedom. This supports a "
            "source-anchored derivation path while rejecting conservation-style "
            "language."
        ),
        open_blocker=(
            "The finite rule must be compared against why-not provenance, "
            "abstract interpretation, lenses, and CSP explanation machinery. "
            "T107 supplies semantics, not prior-art separation."
        ),
        recommended_next=(
            "Re-express T99's typed witness obligations with this source-fiber "
            "rule and test whether the quotient separation still survives."
        ),
    )


def _judgment_to_dict(judgment: LiftJudgment) -> dict[str, object]:
    return {
        "left_source": judgment.left_source,
        "right_source": judgment.right_source,
        "allowed": judgment.allowed,
    }


def _verdict_to_dict(verdict: RelocationVerdict) -> dict[str, object]:
    return {
        "scenario": verdict.scenario,
        "lost_axis": verdict.lost_axis,
        "displaced_form": verdict.displaced_form,
        "target_pair": list(verdict.target_pair),
        "lift_judgments": [_judgment_to_dict(judgment) for judgment in verdict.lift_judgments],
        "hidden_values": list(verdict.hidden_values),
        "derived_witness_pairs": [list(pair) for pair in verdict.derived_witness_pairs],
        "relocation_class": verdict.relocation_class,
        "source_rule_name": verdict.source_rule_name,
        "expected_reading": verdict.expected_reading,
    }


def t107_result_to_dict(result: T107Result) -> dict[str, object]:
    return {
        "verdicts": [_verdict_to_dict(verdict) for verdict in result.verdicts],
        "derived_debt_count": result.derived_debt_count,
        "stable_constraint_count": result.stable_constraint_count,
        "absorbed_freedom_count": result.absorbed_freedom_count,
        "false_conservation_rejected": result.false_conservation_rejected,
        "source_anchored_derivation": result.source_anchored_derivation,
        "six_axis_bridge": [list(row) for row in result.six_axis_bridge],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "tf1_update": result.tf1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t107_result_to_dict(run_t107_analysis()), indent=2))
