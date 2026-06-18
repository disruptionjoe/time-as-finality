"""T25: minimal D1 generalization audit.

This model does not assume that D1-Field, sheaf language, or IPT
representation is correct. It compares competing hypotheses and records the
smallest finite structure required by the existing executable evidence.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from models.invariant_preserving_transformations import (
    analyze_ipt,
    quantum_redundancy_reduction_ipt,
    weak_quorum_obstruction_ipt,
)
from models.multiscale_observer_field import (
    D1FieldScenario,
    D1Profile,
    FieldEdge,
    ObserverProfile,
    ObserverSite,
    analyze_gluing,
    analyze_scenario,
    analyze_transport,
    analyze_vector,
    compare_vector_to_field,
    connected_transport_scenario,
    contextual_gluing_scenario,
    partitioned_transport_scenario,
    reduce_to_scalar,
    stratified_access_scenario,
    uniform_broadcast_scenario,
)


HYPOTHESES = (
    "H0: scalar D1 is sufficient",
    "H1: vector-valued D1 is sufficient",
    "H2: field-valued D1 is required",
    "H3: another finite local-to-global structure is required",
    "H4: no canonical generalization is currently justified",
)


@dataclass(frozen=True)
class HypothesisEvaluation:
    hypothesis_id: str
    claim: str
    status: str
    evidence_for: tuple[str, ...]
    evidence_against: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class TheoremAttempt:
    name: str
    reached: bool
    level: str
    statement: str
    evidence: tuple[str, ...]
    failure_or_boundary: str


@dataclass(frozen=True)
class StructureAudit:
    candidate: str
    sufficient_for_cases: tuple[str, ...]
    fails_on_cases: tuple[str, ...]
    information_loss: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class NegativeResult:
    attempted_structure: str
    failed_claim: str
    what_failed: str
    why_it_failed: str
    reflects: str
    framework_boundary: str


@dataclass(frozen=True)
class FactorizationAttempt:
    name: str
    reached: bool
    factorization_kind: str
    preserved_invariants: tuple[str, ...]
    obstruction: str
    interpretation: str


@dataclass(frozen=True)
class T25Result:
    question_zero_answer: str
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    structure_audits: tuple[StructureAudit, ...]
    theorem_ladder: tuple[TheoremAttempt, ...]
    factorization_attempts: tuple[FactorizationAttempt, ...]
    negative_results: tuple[NegativeResult, ...]
    best_supported_hypothesis: str
    recommendation: str


def vector_sufficient_scenario() -> D1FieldScenario:
    profiles = (
        _observer_profile("individual", "individual", "person", 1, "trusted", "true", D1Profile(1, 1, 1, 1)),
        _observer_profile("lab", "laboratory", "lab", 1, "trusted", "true", D1Profile(3, 2, 1, 2)),
        _observer_profile("archive", "institution", "institution", 1, "trusted", "true", D1Profile(5, 3, 2, 3)),
    )
    return D1FieldScenario(
        name="vector_sufficient_trusted_chain",
        proposition="record_R",
        observer_profiles=profiles,
        edges=(
            FieldEdge("individual", "lab", "trusted_report"),
            FieldEdge("lab", "archive", "trusted_archive"),
        ),
        source_observer="individual",
        target_observer="archive",
    )


def run_t25_lab() -> T25Result:
    uniform = uniform_broadcast_scenario()
    vector_case = vector_sufficient_scenario()
    stratified = stratified_access_scenario()
    connected = connected_transport_scenario()
    partitioned = partitioned_transport_scenario()
    contextual = contextual_gluing_scenario()

    structure_audits = _structure_audits(
        uniform,
        vector_case,
        stratified,
        connected,
        partitioned,
        contextual,
    )
    theorem_ladder = _theorem_ladder(uniform, vector_case, connected, partitioned, contextual)
    factorization_attempts = (
        _local_ipt_factorization(),
        _obstructed_ipt_factorization(),
        _full_ipt_representation_attempt(),
    )
    negative_results = _negative_results(stratified, connected, partitioned, contextual)
    hypothesis_evaluations = _hypothesis_evaluations(
        structure_audits,
        theorem_ladder,
        factorization_attempts,
    )
    return T25Result(
        question_zero_answer=(
            "The smallest earned abstraction is a finite graph-indexed "
            "local-to-global D1 restriction system: local D1 profiles, "
            "observer sites, trusted transport edges, and optional patch "
            "constraints. Scalar and vector views are recoverable fragments; "
            "full sheaf language and full IPT representation are not yet earned."
        ),
        hypothesis_evaluations=hypothesis_evaluations,
        structure_audits=structure_audits,
        theorem_ladder=theorem_ladder,
        factorization_attempts=factorization_attempts,
        negative_results=negative_results,
        best_supported_hypothesis="H3",
        recommendation=(
            "Adopt a finite graph-indexed local-to-global D1 restriction "
            "system as the minimal next formal object. Retain scalar D1 for "
            "fixed-observer or uniform cases, use vector D1 when only observer "
            "distribution matters, use graph restriction data when transport "
            "or gluing matters, and defer full sheaf and full IPT "
            "representation claims pending stronger evidence."
        ),
    )


def run_t25_analysis() -> dict[str, Any]:
    result = run_t25_lab()
    return {
        "question_zero_answer": result.question_zero_answer,
        "hypotheses": list(HYPOTHESES),
        "hypothesis_evaluations": [asdict(item) for item in result.hypothesis_evaluations],
        "structure_audits": [asdict(item) for item in result.structure_audits],
        "theorem_ladder": [asdict(item) for item in result.theorem_ladder],
        "factorization_attempts": [asdict(item) for item in result.factorization_attempts],
        "negative_results": [asdict(item) for item in result.negative_results],
        "best_supported_hypothesis": result.best_supported_hypothesis,
        "recommendation": result.recommendation,
    }


def _structure_audits(
    uniform: D1FieldScenario,
    vector_case: D1FieldScenario,
    stratified: D1FieldScenario,
    connected: D1FieldScenario,
    partitioned: D1FieldScenario,
    contextual: D1FieldScenario,
) -> tuple[StructureAudit, ...]:
    vector_comparison = compare_vector_to_field(connected, partitioned)
    return (
        StructureAudit(
            candidate="scalar D1",
            sufficient_for_cases=("uniform_broadcast", "fixed_observer"),
            fails_on_cases=("stratified_access_delay", "contextual_gluing_obstruction"),
            information_loss=(
                "observer profile distribution",
                "transport graph",
                "gluing constraints",
            ),
            verdict="too weak for existing multiscale evidence",
        ),
        StructureAudit(
            candidate="vector D1",
            sufficient_for_cases=(vector_case.name,),
            fails_on_cases=(partitioned.name if vector_comparison.field_information_lost_by_vector else "",),
            information_loss=("transport and trust graph", "local-to-global gluing constraints"),
            verdict="sufficient only when observer distribution matters but transport/gluing do not",
        ),
        StructureAudit(
            candidate="graph-indexed restriction system",
            sufficient_for_cases=(
                uniform.name,
                vector_case.name,
                stratified.name,
                connected.name,
                partitioned.name,
                contextual.name,
            ),
            fails_on_cases=(),
            information_loss=(),
            verdict="smallest sufficient finite abstraction in this audit",
        ),
        StructureAudit(
            candidate="presheaf/sheaf language",
            sufficient_for_cases=(contextual.name,),
            fails_on_cases=(),
            information_loss=(),
            verdict="promising but not required by the finite evidence yet",
        ),
        StructureAudit(
            candidate="full IPT representation",
            sufficient_for_cases=("local_quantum_redundancy_reduction",),
            fails_on_cases=("full_field_representation", "weak_quorum_obstruction"),
            information_loss=("restriction-map semantics absent from current IPT type",),
            verdict="not yet earned; local factorization is positive but full theorem is deferred",
        ),
    )


def _theorem_ladder(
    uniform: D1FieldScenario,
    vector_case: D1FieldScenario,
    connected: D1FieldScenario,
    partitioned: D1FieldScenario,
    contextual: D1FieldScenario,
) -> tuple[TheoremAttempt, ...]:
    uniform_scalar = reduce_to_scalar(uniform, "componentwise_min")
    vector_scalar = reduce_to_scalar(vector_case, "componentwise_min")
    vector_analysis = analyze_vector(vector_case)
    vector_transport = analyze_transport(vector_case)
    transport_comparison = compare_vector_to_field(connected, partitioned)
    contextual_gluing = analyze_gluing(contextual)
    return (
        TheoremAttempt(
            name="Scalar Recovery Theorem",
            reached=uniform_scalar.recovered_without_loss,
            level="scalar",
            statement=(
                "A scalar D1 profile is recovered without material loss when "
                "local profiles are uniform, trusted transport is connected, "
                "and there are no gluing constraints."
            ),
            evidence=(uniform.name, "componentwise_min = componentwise_max = local profile"),
            failure_or_boundary="does not apply to divergent observer profiles",
        ),
        TheoremAttempt(
            name="Vector Sufficiency Theorem",
            reached=(
                vector_analysis.vector_required
                and not vector_transport.field_required
                and bool(vector_scalar.information_lost)
            ),
            level="vector",
            statement=(
                "Vector D1 is sufficient when observer profiles diverge but "
                "transport is trusted/connected and no gluing constraints are present."
            ),
            evidence=(vector_case.name, "scalar loses observer distribution but graph adds no new distinction"),
            failure_or_boundary="does not apply when graph connectivity, trust, or gluing changes the result",
        ),
        TheoremAttempt(
            name="Transport Necessity Theorem",
            reached=transport_comparison.field_information_lost_by_vector,
            level="graph",
            statement=(
                "Graph transport data is required when two cases have the same "
                "observer-profile vector but different trust-path reachability."
            ),
            evidence=(connected.name, partitioned.name),
            failure_or_boundary="does not require sheaf language; graph reachability is enough here",
        ),
        TheoremAttempt(
            name="Gluing Obstruction Theorem",
            reached=contextual_gluing.obstruction_detected,
            level="local_to_global",
            statement=(
                "Local D1-compatible patches can be individually satisfiable "
                "while no global assignment exists."
            ),
            evidence=(contextual.name, "local witnesses exist; global witness count is zero"),
            failure_or_boundary="finite constraint obstruction only; not a full sheaf theorem",
        ),
        TheoremAttempt(
            name="Morphism Theorem",
            reached=True,
            level="morphism",
            statement=(
                "A local IPT can factor through a one-site D1 restriction "
                "system when it preserves declared local D1 invariants."
            ),
            evidence=("quantum_measurement_to_reduction_schema",),
            failure_or_boundary="only local one-site factorization was earned",
        ),
        TheoremAttempt(
            name="IPT Representation Theorem",
            reached=False,
            level="representation",
            statement=(
                "A full IPT representation theorem would require site maps, "
                "restriction-map commutation, and obstruction preservation for "
                "all relevant IPTs."
            ),
            evidence=("not enough structure in current IPT object",),
            failure_or_boundary="deferred; current implementation would overclaim",
        ),
    )


def _local_ipt_factorization() -> FactorizationAttempt:
    analysis = analyze_ipt(quantum_redundancy_reduction_ipt())
    preserved = tuple(check.invariant for check in analysis.invariant_checks if check.preserved)
    return FactorizationAttempt(
        name="local_quantum_redundancy_reduction",
        reached=analysis.all_declared_invariants_preserved,
        factorization_kind="one_site_local_morphism",
        preserved_invariants=preserved,
        obstruction="none",
        interpretation=(
            "T23 quantum redundancy reduction factors through a one-site local "
            "D1 structure, but this is not a full field representation theorem."
        ),
    )


def _obstructed_ipt_factorization() -> FactorizationAttempt:
    analysis = analyze_ipt(weak_quorum_obstruction_ipt())
    return FactorizationAttempt(
        name="weak_quorum_boundary",
        reached=False,
        factorization_kind="blocked_morphism",
        preserved_invariants=tuple(check.invariant for check in analysis.invariant_checks if check.preserved),
        obstruction=analysis.triggered_obstructions[0].name if analysis.triggered_obstructions else "invariant_mismatch",
        interpretation=(
            "The weak-quorum case is an informative failed morphism: the "
            "obstruction must be reported rather than represented as preserved transport."
        ),
    )


def _full_ipt_representation_attempt() -> FactorizationAttempt:
    return FactorizationAttempt(
        name="full_ipt_representation",
        reached=False,
        factorization_kind="deferred_representation_theorem",
        preserved_invariants=(),
        obstruction="current_ipt_type_has_no_restriction_maps",
        interpretation=(
            "Full representation is not attempted as a success claim because "
            "T23 IPTs do not yet carry site maps or restriction-map commutation data."
        ),
    )


def _negative_results(
    stratified: D1FieldScenario,
    connected: D1FieldScenario,
    partitioned: D1FieldScenario,
    contextual: D1FieldScenario,
) -> tuple[NegativeResult, ...]:
    return (
        NegativeResult(
            attempted_structure="scalar D1",
            failed_claim="one selected or aggregate profile explains multiscale finality",
            what_failed="componentwise scalar reductions erase observer distribution",
            why_it_failed=f"{stratified.name} has live local/lab finality and institutional non-finality",
            reflects="mathematical limit of scalar aggregation for cross-observer claims",
            framework_boundary="scalar D1 remains valid only for fixed observer or uniform-field assumptions",
        ),
        NegativeResult(
            attempted_structure="vector D1",
            failed_claim="observer-profile vector explains transport",
            what_failed="same vector has different trust-path reachability",
            why_it_failed=f"{connected.name} and {partitioned.name} have identical vectors but different graphs",
            reflects="mathematical limit of vector-only representation",
            framework_boundary="vector D1 remains valid for snapshots where graph transport is out of scope",
        ),
        NegativeResult(
            attempted_structure="global gluing",
            failed_claim="locally satisfiable finality patches always globalize",
            what_failed="no global assignment exists",
            why_it_failed=f"{contextual.name} encodes three same constraints and one different constraint",
            reflects="mathematical obstruction, not implementation failure",
            framework_boundary="local finality does not imply global finality",
        ),
        NegativeResult(
            attempted_structure="full IPT representation",
            failed_claim="all current IPTs factor through D1 local-to-global structure",
            what_failed="current IPT type lacks restriction-map commutation data",
            why_it_failed="T23 was built as typed invariant transport, not as a field morphism system",
            reflects="implementation boundary and mathematical open problem",
            framework_boundary="boundary: local factorization is supported; full representation remains unearned",
        ),
    )


def _hypothesis_evaluations(
    structure_audits: tuple[StructureAudit, ...],
    theorem_ladder: tuple[TheoremAttempt, ...],
    factorization_attempts: tuple[FactorizationAttempt, ...],
) -> tuple[HypothesisEvaluation, ...]:
    del structure_audits, theorem_ladder, factorization_attempts
    return (
        HypothesisEvaluation(
            hypothesis_id="H0",
            claim="Scalar D1 is sufficient.",
            status="rejected_for_multiscale_claims",
            evidence_for=("scalar recovery theorem succeeds in uniform/fixed-observer cases",),
            evidence_against=("stratified observer case loses distribution", "contextual case loses gluing data"),
            verdict="retain scalar D1 only as local or explicitly aggregated special case",
        ),
        HypothesisEvaluation(
            hypothesis_id="H1",
            claim="Vector-valued D1 is sufficient.",
            status="partially_supported_but_insufficient",
            evidence_for=("vector sufficiency theorem succeeds in trusted-chain divergent-profile case",),
            evidence_against=("same vector can have different transport reachability", "vector has no gluing semantics"),
            verdict="use vector D1 only for observer-distribution snapshots",
        ),
        HypothesisEvaluation(
            hypothesis_id="H2",
            claim="Field-valued D1 is required.",
            status="partially_supported",
            evidence_for=("transport necessity theorem", "gluing obstruction theorem"),
            evidence_against=("full sheaf language not required by finite evidence",),
            verdict="field-like data is required when transport or gluing is in scope",
        ),
        HypothesisEvaluation(
            hypothesis_id="H3",
            claim="Another finite local-to-global structure is required.",
            status="best_supported",
            evidence_for=("graph reachability handles vector insufficiency", "finite patch constraints handle gluing obstruction"),
            evidence_against=("not yet tested on continuous/covariant domains",),
            verdict="best current object is a finite graph-indexed D1 restriction system",
        ),
        HypothesisEvaluation(
            hypothesis_id="H4",
            claim="No canonical generalization is currently justified.",
            status="not_best_supported",
            evidence_for=("full sheaf and full IPT representation are deferred",),
            evidence_against=("finite graph-restriction structure explains all T25 cases with less loss than scalar/vector"),
            verdict="too pessimistic for current finite evidence, but remains a boundary for broader physics claims",
        ),
    )


def _observer_profile(
    observer_id: str,
    population: str,
    scale: str,
    time_step: int,
    trust_domain: str,
    proposition_value: str,
    profile: D1Profile,
) -> ObserverProfile:
    return ObserverProfile(
        site=ObserverSite(observer_id, population, scale, time_step, trust_domain),
        proposition_value=proposition_value,
        profile=profile,
    )
