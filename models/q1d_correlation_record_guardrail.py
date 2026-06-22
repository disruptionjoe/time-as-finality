"""T170: Q1D correlation-record timing guardrail.

T21 already gives Q1D a finite CHSH/contextuality certificate. This module
tests a different failure mode: using finality language to read a later
reconciled correlation record back into an earlier local record, or allowing a
local record to depend on a spacelike remote setting.

The audit is intentionally finite and conservative. It is a guardrail over
language and model admissibility, not a new Bell theorem, detector model, or
quantum prediction.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import sqrt


Outcome = int
SETTING_PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))
TOLERANCE = 1e-9


@dataclass(frozen=True)
class JointOutcome:
    alice: Outcome
    bob: Outcome
    probability: float


@dataclass(frozen=True)
class CorrelationContext:
    name: str
    alice_setting: int
    bob_setting: int
    outcomes: tuple[JointOutcome, ...]

    @property
    def total_probability(self) -> float:
        return sum(outcome.probability for outcome in self.outcomes)

    @property
    def correlation(self) -> float:
        return sum(
            outcome.alice * outcome.bob * outcome.probability
            for outcome in self.outcomes
        )

    def alice_marginal(self) -> dict[Outcome, float]:
        return {
            value: sum(
                outcome.probability
                for outcome in self.outcomes
                if outcome.alice == value
            )
            for value in (-1, 1)
        }

    def bob_marginal(self) -> dict[Outcome, float]:
        return {
            value: sum(
                outcome.probability
                for outcome in self.outcomes
                if outcome.bob == value
            )
            for value in (-1, 1)
        }


@dataclass(frozen=True)
class CorrelationRecordScenario:
    scenario_id: str
    contexts: tuple[CorrelationContext, ...]
    correlation_record_stage: str
    claims_prior_local_values: bool
    claimed_quantum_prediction: bool
    purpose: str


@dataclass(frozen=True)
class CorrelationRecordAudit:
    scenario_id: str
    no_signalling: bool
    max_marginal_delta: float
    max_chsh_score: float
    violates_classical_bound: bool
    exceeds_tsirelson_bound: bool
    correlation_record_stage: str
    claims_prior_local_values: bool
    claimed_quantum_prediction: bool
    classification: str
    allowed_language: str
    rejected_language: str
    interpretation: str


@dataclass(frozen=True)
class T170Result:
    audits: tuple[CorrelationRecordAudit, ...]
    admissible_contextual_guardrails: tuple[str, ...]
    null_signalling_cases: tuple[str, ...]
    null_hidden_variable_cases: tuple[str, ...]
    null_premature_export_cases: tuple[str, ...]
    postquantum_guardrail_only_cases: tuple[str, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1d_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def canonical_q1d_guardrail_scenarios() -> tuple[CorrelationRecordScenario, ...]:
    quantum_contexts = quantum_tsirelson_contexts()
    pr_contexts = pr_box_contexts()
    return (
        CorrelationRecordScenario(
            scenario_id="classical_reconciled_baseline",
            contexts=classical_global_contexts(),
            correlation_record_stage="after_causal_comparison",
            claims_prior_local_values=True,
            claimed_quantum_prediction=False,
            purpose=(
                "A noncontextual baseline where global preassigned local values "
                "are compatible with the CHSH bound."
            ),
        ),
        CorrelationRecordScenario(
            scenario_id="quantum_contextual_reconciled_record",
            contexts=quantum_contexts,
            correlation_record_stage="after_causal_comparison",
            claims_prior_local_values=False,
            claimed_quantum_prediction=True,
            purpose=(
                "A Tsirelson-saturating no-signalling box whose correlation "
                "record is formed only after ordinary causal comparison."
            ),
        ),
        CorrelationRecordScenario(
            scenario_id="pr_box_no_signalling_guardrail_only",
            contexts=pr_contexts,
            correlation_record_stage="after_causal_comparison",
            claims_prior_local_values=False,
            claimed_quantum_prediction=False,
            purpose=(
                "A no-signalling but post-quantum control showing that "
                "no-signalling alone is not a quantum prediction."
            ),
        ),
        CorrelationRecordScenario(
            scenario_id="signalling_remote_setting_leak",
            contexts=signalling_marginal_contexts(),
            correlation_record_stage="local_record_stage",
            claims_prior_local_values=False,
            claimed_quantum_prediction=True,
            purpose=(
                "A false-positive control where Alice's local marginal depends "
                "on Bob's setting."
            ),
        ),
        CorrelationRecordScenario(
            scenario_id="hidden_variable_retrofit",
            contexts=quantum_contexts,
            correlation_record_stage="after_causal_comparison",
            claims_prior_local_values=True,
            claimed_quantum_prediction=True,
            purpose=(
                "A language-level false positive: the Tsirelson box is treated "
                "as if it had earlier local hidden values."
            ),
        ),
        CorrelationRecordScenario(
            scenario_id="premature_correlation_export",
            contexts=quantum_contexts,
            correlation_record_stage="local_record_stage",
            claims_prior_local_values=False,
            claimed_quantum_prediction=True,
            purpose=(
                "A timing false positive: the later joint correlation is "
                "declared final at a separated local record stage."
            ),
        ),
        CorrelationRecordScenario(
            scenario_id="pr_box_mislabelled_quantum_prediction",
            contexts=pr_contexts,
            correlation_record_stage="after_causal_comparison",
            claims_prior_local_values=False,
            claimed_quantum_prediction=True,
            purpose=(
                "A post-quantum no-signalling control mislabelled as a quantum "
                "prediction."
            ),
        ),
    )


def classical_global_contexts() -> tuple[CorrelationContext, ...]:
    return tuple(
        _deterministic_context(name=f"A{x}B{y}", x=x, y=y, alice=1, bob=1)
        for x, y in SETTING_PAIRS
    )


def quantum_tsirelson_contexts() -> tuple[CorrelationContext, ...]:
    value = 1.0 / sqrt(2.0)
    correlations = {
        (0, 0): value,
        (0, 1): value,
        (1, 0): value,
        (1, 1): -value,
    }
    return tuple(
        _unbiased_context(f"A{x}B{y}", x, y, correlations[(x, y)])
        for x, y in SETTING_PAIRS
    )


def pr_box_contexts() -> tuple[CorrelationContext, ...]:
    correlations = {
        (0, 0): 1.0,
        (0, 1): 1.0,
        (1, 0): 1.0,
        (1, 1): -1.0,
    }
    return tuple(
        _unbiased_context(f"A{x}B{y}", x, y, correlations[(x, y)])
        for x, y in SETTING_PAIRS
    )


def signalling_marginal_contexts() -> tuple[CorrelationContext, ...]:
    alice_plus_by_remote_setting = {
        (0, 0): 0.85,
        (0, 1): 0.15,
        (1, 0): 0.85,
        (1, 1): 0.15,
    }
    return tuple(
        _independent_biased_context(
            name=f"A{x}B{y}",
            x=x,
            y=y,
            alice_plus_probability=alice_plus_by_remote_setting[(x, y)],
            bob_plus_probability=0.5,
        )
        for x, y in SETTING_PAIRS
    )


def audit_correlation_record_scenario(
    scenario: CorrelationRecordScenario,
) -> CorrelationRecordAudit:
    _validate_scenario(scenario)
    max_marginal_delta = _max_marginal_delta(scenario.contexts)
    no_signalling = max_marginal_delta <= TOLERANCE
    max_chsh_score = _max_chsh_score(scenario.contexts)
    classical_bound = 2.0
    tsirelson_bound = 2.0 * sqrt(2.0)
    violates_classical = max_chsh_score > classical_bound + TOLERANCE
    exceeds_tsirelson = max_chsh_score > tsirelson_bound + TOLERANCE
    classification = _classification(
        scenario=scenario,
        no_signalling=no_signalling,
        violates_classical=violates_classical,
        exceeds_tsirelson=exceeds_tsirelson,
    )
    return CorrelationRecordAudit(
        scenario_id=scenario.scenario_id,
        no_signalling=no_signalling,
        max_marginal_delta=max_marginal_delta,
        max_chsh_score=max_chsh_score,
        violates_classical_bound=violates_classical,
        exceeds_tsirelson_bound=exceeds_tsirelson,
        correlation_record_stage=scenario.correlation_record_stage,
        claims_prior_local_values=scenario.claims_prior_local_values,
        claimed_quantum_prediction=scenario.claimed_quantum_prediction,
        classification=classification,
        allowed_language=_allowed_language(classification),
        rejected_language=_rejected_language(classification),
        interpretation=_interpretation(scenario, classification),
    )


def run_t170_analysis() -> T170Result:
    audits = tuple(
        audit_correlation_record_scenario(scenario)
        for scenario in canonical_q1d_guardrail_scenarios()
    )
    by_classification = _group_by_classification(audits)
    admissible = by_classification["admissible_contextual_reconciliation_record"]
    null_signalling = by_classification["null_signalling_local_record"]
    null_hidden = by_classification["null_hidden_variable_overclaim"]
    null_premature = by_classification["null_premature_correlation_record"]
    postquantum = by_classification["postquantum_no_signalling_guardrail_only"]

    if admissible != ("quantum_contextual_reconciled_record",):
        raise AssertionError("exactly one quantum contextual guardrail case should pass")
    if null_signalling != ("signalling_remote_setting_leak",):
        raise AssertionError("signalling marginal leak must be null")
    if null_hidden != ("hidden_variable_retrofit",):
        raise AssertionError("hidden-variable retrofit must be null")
    if null_premature != ("premature_correlation_export",):
        raise AssertionError("premature correlation export must be null")
    if postquantum != ("pr_box_no_signalling_guardrail_only",):
        raise AssertionError("PR-box control should remain guardrail-only")

    return T170Result(
        audits=audits,
        admissible_contextual_guardrails=admissible,
        null_signalling_cases=null_signalling,
        null_hidden_variable_cases=null_hidden,
        null_premature_export_cases=null_premature,
        postquantum_guardrail_only_cases=postquantum,
        strongest_claim=(
            "Q1D can safely say that no-signalling contextual correlations may "
            "produce local records first and a joint correlation record only "
            "after causal comparison. It cannot say that the later correlation "
            "was already an earlier local hidden fact, and it cannot let local "
            "record-finality depend on a remote setting."
        ),
        improved=(
            "T170 makes the reconciliation-time boundary executable. Future "
            "Q1 language now has finite null controls for signalling marginals, "
            "hidden-variable retrofits, premature correlation export, and "
            "post-quantum boxes mislabelled as quantum predictions."
        ),
        weakened=(
            "This weakens Q1D's positive content to admissible language only. "
            "The passing quantum fixture adds no measurement dynamics, no new "
            "Bell inequality, no collapse account, and no empirical discriminator."
        ),
        falsification_condition=(
            "T170 fails if a model can keep no-signalling local marginals, "
            "violate the classical CHSH bound within the quantum Tsirelson "
            "limit, treat the correlation record as available only after "
            "causal comparison, avoid prior-local-value language, and still "
            "require rejection by the Q1D guardrail."
        ),
        q1d_update=(
            "Q1D remains guardrail-only. The current safe formulation is a "
            "stage rule: local record-finality is local-marginal constrained; "
            "joint correlation finality is a later causal-reconciliation record."
        ),
        claim_ledger_update=(
            "Add T170 to Q1D: no-signalling contextual correlations are "
            "admissible only when local records do not depend on remote "
            "settings and the joint correlation is recorded after causal "
            "comparison. Signalling, hidden-variable retrofits, premature "
            "correlation export, and post-quantum-as-quantum readings are null."
        ),
        open_blocker=(
            "No theorem connects this finite stage guardrail to a general "
            "decoherent-histories, algebraic-QFT, or detector-level account of "
            "classical record formation."
        ),
        recommended_next=(
            "Use T170 as a prose gate for Q1D. Do not add more Bell-style toy "
            "models unless they introduce a new typed capability object or "
            "bridge the stage rule into a mature quantum-record framework."
        ),
    )


def t170_result_to_dict(result: T170Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "scenario_id": audit.scenario_id,
                "no_signalling": audit.no_signalling,
                "max_marginal_delta": audit.max_marginal_delta,
                "max_chsh_score": audit.max_chsh_score,
                "violates_classical_bound": audit.violates_classical_bound,
                "exceeds_tsirelson_bound": audit.exceeds_tsirelson_bound,
                "correlation_record_stage": audit.correlation_record_stage,
                "claims_prior_local_values": audit.claims_prior_local_values,
                "claimed_quantum_prediction": audit.claimed_quantum_prediction,
                "classification": audit.classification,
                "allowed_language": audit.allowed_language,
                "rejected_language": audit.rejected_language,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "admissible_contextual_guardrails": list(
            result.admissible_contextual_guardrails
        ),
        "null_signalling_cases": list(result.null_signalling_cases),
        "null_hidden_variable_cases": list(result.null_hidden_variable_cases),
        "null_premature_export_cases": list(result.null_premature_export_cases),
        "postquantum_guardrail_only_cases": list(
            result.postquantum_guardrail_only_cases
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1d_update": result.q1d_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _unbiased_context(
    name: str,
    x: int,
    y: int,
    correlation: float,
) -> CorrelationContext:
    return CorrelationContext(
        name=name,
        alice_setting=x,
        bob_setting=y,
        outcomes=tuple(
            JointOutcome(alice=a, bob=b, probability=(1.0 + a * b * correlation) / 4.0)
            for a, b in product((-1, 1), repeat=2)
        ),
    )


def _deterministic_context(
    name: str,
    x: int,
    y: int,
    alice: Outcome,
    bob: Outcome,
) -> CorrelationContext:
    return CorrelationContext(
        name=name,
        alice_setting=x,
        bob_setting=y,
        outcomes=tuple(
            JointOutcome(a, b, 1.0 if (a, b) == (alice, bob) else 0.0)
            for a, b in product((-1, 1), repeat=2)
        ),
    )


def _independent_biased_context(
    name: str,
    x: int,
    y: int,
    alice_plus_probability: float,
    bob_plus_probability: float,
) -> CorrelationContext:
    def probability(value: Outcome, plus_probability: float) -> float:
        return plus_probability if value == 1 else 1.0 - plus_probability

    return CorrelationContext(
        name=name,
        alice_setting=x,
        bob_setting=y,
        outcomes=tuple(
            JointOutcome(
                a,
                b,
                probability(a, alice_plus_probability)
                * probability(b, bob_plus_probability),
            )
            for a, b in product((-1, 1), repeat=2)
        ),
    )


def _validate_scenario(scenario: CorrelationRecordScenario) -> None:
    seen_pairs = {
        (context.alice_setting, context.bob_setting)
        for context in scenario.contexts
    }
    if seen_pairs != set(SETTING_PAIRS):
        raise ValueError(f"{scenario.scenario_id} must contain all four CHSH settings")
    for context in scenario.contexts:
        if abs(context.total_probability - 1.0) > TOLERANCE:
            raise ValueError(f"{context.name} probabilities do not sum to one")
        if any(outcome.probability < -TOLERANCE for outcome in context.outcomes):
            raise ValueError(f"{context.name} contains a negative probability")


def _max_marginal_delta(contexts: tuple[CorrelationContext, ...]) -> float:
    by_pair = {(context.alice_setting, context.bob_setting): context for context in contexts}
    deltas: list[float] = []
    for x in (0, 1):
        alice_marginals = [
            by_pair[(x, y)].alice_marginal()
            for y in (0, 1)
        ]
        deltas.extend(_marginal_deltas(alice_marginals[0], alice_marginals[1]))
    for y in (0, 1):
        bob_marginals = [
            by_pair[(x, y)].bob_marginal()
            for x in (0, 1)
        ]
        deltas.extend(_marginal_deltas(bob_marginals[0], bob_marginals[1]))
    return max(deltas)


def _marginal_deltas(
    first: dict[Outcome, float],
    second: dict[Outcome, float],
) -> tuple[float, float]:
    return tuple(abs(first[value] - second[value]) for value in (-1, 1))


def _max_chsh_score(contexts: tuple[CorrelationContext, ...]) -> float:
    correlations = {
        (context.alice_setting, context.bob_setting): context.correlation
        for context in contexts
    }
    ordered = [correlations[pair] for pair in SETTING_PAIRS]
    scores = []
    for signs in product((-1, 1), repeat=4):
        if signs[0] * signs[1] * signs[2] * signs[3] == -1:
            scores.append(abs(sum(sign * value for sign, value in zip(signs, ordered))))
    return max(scores)


def _classification(
    scenario: CorrelationRecordScenario,
    no_signalling: bool,
    violates_classical: bool,
    exceeds_tsirelson: bool,
) -> str:
    if not no_signalling:
        return "null_signalling_local_record"
    if scenario.claims_prior_local_values and violates_classical:
        return "null_hidden_variable_overclaim"
    if scenario.correlation_record_stage != "after_causal_comparison" and violates_classical:
        return "null_premature_correlation_record"
    if scenario.claimed_quantum_prediction and exceeds_tsirelson:
        return "null_postquantum_as_quantum_prediction"
    if exceeds_tsirelson:
        return "postquantum_no_signalling_guardrail_only"
    if violates_classical:
        return "admissible_contextual_reconciliation_record"
    return "classical_reconciliation_baseline"


def _group_by_classification(
    audits: tuple[CorrelationRecordAudit, ...],
) -> dict[str, tuple[str, ...]]:
    classifications = {
        "admissible_contextual_reconciliation_record",
        "null_signalling_local_record",
        "null_hidden_variable_overclaim",
        "null_premature_correlation_record",
        "postquantum_no_signalling_guardrail_only",
        "null_postquantum_as_quantum_prediction",
        "classical_reconciliation_baseline",
    }
    return {
        classification: tuple(
            audit.scenario_id
            for audit in audits
            if audit.classification == classification
        )
        for classification in classifications
    }


def _allowed_language(classification: str) -> str:
    if classification == "admissible_contextual_reconciliation_record":
        return (
            "Local records may be context-valid before comparison; the joint "
            "correlation record becomes final only after causal reconciliation."
        )
    if classification == "postquantum_no_signalling_guardrail_only":
        return (
            "The case can be used only as a no-signalling/post-quantum guardrail "
            "control, not as a quantum prediction."
        )
    if classification == "classical_reconciliation_baseline":
        return (
            "A prior local-value reading is admissible only because the fixture "
            "does not violate the CHSH classical bound."
        )
    return "No Q1D support language is admissible for this fixture."


def _rejected_language(classification: str) -> str:
    if classification == "null_signalling_local_record":
        return "Reject any claim that local finality can depend on a remote setting."
    if classification == "null_hidden_variable_overclaim":
        return (
            "Reject any claim that a later CHSH-violating correlation record was "
            "already an earlier local hidden fact."
        )
    if classification == "null_premature_correlation_record":
        return (
            "Reject any claim that the joint correlation is locally finalized "
            "before the parties can compare records."
        )
    if classification == "null_postquantum_as_quantum_prediction":
        return "Reject treating a post-quantum no-signalling box as a quantum prediction."
    return "Reject upgrading this guardrail into measurement dynamics or a new inequality."


def _interpretation(
    scenario: CorrelationRecordScenario,
    classification: str,
) -> str:
    if classification == "admissible_contextual_reconciliation_record":
        return (
            f"{scenario.scenario_id} passes only as Q1D guardrail language: "
            "no-signalling local records first, correlation record after "
            "ordinary causal comparison."
        )
    if classification == "postquantum_no_signalling_guardrail_only":
        return (
            f"{scenario.scenario_id} preserves no-signalling but exceeds the "
            "quantum Tsirelson bound, so it is a boundary control."
        )
    if classification == "classical_reconciliation_baseline":
        return (
            f"{scenario.scenario_id} is a classical baseline, not evidence for "
            "under-finalized quantum correlations."
        )
    return f"{scenario.scenario_id} is null for Q1D: {scenario.purpose}"


if __name__ == "__main__":
    import json

    print(json.dumps(t170_result_to_dict(run_t170_analysis()), indent=2))
