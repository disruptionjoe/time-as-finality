"""T30: hostile cross-domain validation of PO1.

This module tests whether the T29 Projection-Obstruction Schema remains
meaningful outside the physics and GU examples that motivated it. It reuses
T29's ProjectionCase and analyzer directly, and adds only domain metadata plus
H0-H4 hypothesis evaluation.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    global_section,
    validate_system,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.projection_obstruction_schema import (
    ProjectionCase,
    ProjectionCaseAnalysis,
    analyze_projection_case,
)


CLASSIFICATION_BY_OUTCOME = {
    "faithful_projection_obstruction": "projection-created obstruction",
    "lossy_projection_no_new_obstruction": "lossy projection without obstruction",
    "shared_obstruction_not_projection_created": "shared obstruction",
    "non_definable_projection": "non-definable projection",
}

HYPOTHESES = (
    "H0: PO1 is domain-specific to GU/no-go style cases",
    "H1: PO1 applies to at least one non-physics inherited domain",
    "H2: PO1 applies across multiple unrelated domains with the same finite structure",
    "H3: PO1 requires modification to handle non-physics domains",
    "H4: PO1 is too broad or underconstrained to be useful",
)


@dataclass(frozen=True)
class HostileDomainCase:
    domain: str
    expected_bias: str
    independent_projection_basis: str
    hostile_reason: str
    case: ProjectionCase
    admissible_to_po1: bool = True
    admissibility_warning: str = ""


@dataclass(frozen=True)
class HostileCaseAnalysis:
    domain: str
    expected_bias: str
    classification: str
    supports_po1: bool
    meaningful_po1_fit: bool
    hypothesis_signal: str
    hostile_reason: str
    independent_projection_basis: str
    analysis: ProjectionCaseAnalysis


@dataclass(frozen=True)
class HypothesisEvaluation:
    hypothesis_id: str
    status: str
    evidence_for: tuple[str, ...]
    evidence_against: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class T30Result:
    analyses: tuple[HostileCaseAnalysis, ...]
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    best_supported_hypothesis: str
    po1_recommendation: str
    admissibility_constraints: tuple[str, ...]


def git_semantic_merge_case() -> HostileDomainCase:
    """Positive hostile case: semantic merge metadata resolves a path conflict."""
    richer = D1RestrictionSystem(
        name="git_semantic_merge_richer",
        proposition="clean_merge_after_rename",
        local_values=(
            _local("git_left_rename", "left_branch", "version_control", "renamed", D1Profile(2, 1, 1, 2)),
            _local("git_right_edit", "right_branch", "version_control", "edited", D1Profile(2, 1, 1, 2)),
            _local("git_merge_driver", "merge_driver", "version_control", "rename_aware", D1Profile(3, 2, 1, 1)),
        ),
        transport_edges=(
            TransportEdge("git_left_rename", "git_merge_driver", "rename_metadata"),
            TransportEdge("git_right_edit", "git_merge_driver", "content_application"),
        ),
        source_site="git_left_rename",
        target_site="git_merge_driver",
        patches=(
            RestrictionPatch(
                "rename_records_new_path",
                ("git_left_rename", "git_merge_driver"),
                ("old_path", "new_path"),
                (PatchConstraint("old_path", "new_path", "different"),),
            ),
            RestrictionPatch(
                "driver_uses_new_path",
                ("git_left_rename", "git_merge_driver"),
                ("new_path", "merge_target"),
                (PatchConstraint("new_path", "merge_target", "same"),),
            ),
            RestrictionPatch(
                "right_edit_applies_to_target",
                ("git_right_edit", "git_merge_driver"),
                ("right_target", "merge_target"),
                (PatchConstraint("right_target", "merge_target", "same"),),
            ),
        ),
    )
    restricted = _three_patch_obstruction_system(
        name="git_path_only_merge_restricted",
        proposition="clean_merge_after_rename",
        site_ids=("git_base_path", "git_left_path", "git_right_path"),
        populations=("base_commit", "left_branch", "right_branch"),
        patch_ids=("left_preserves_base", "right_preserves_base", "paths_diverge"),
        variable_prefix="git_path",
        profile=D1Profile(1, 1, 0, 3),
    )
    morphism = D1RestrictionMorphism(
        name="git_forget_rename_metadata",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("git_left_rename", "git_left_path"),
            SiteMap("git_right_edit", "git_right_path"),
            SiteMap("git_merge_driver", "git_base_path"),
        ),
        preserved_dimensions=("reversal_cost",),
    )
    return HostileDomainCase(
        domain="git merge conflict",
        expected_bias="positive",
        independent_projection_basis="forget rename detection and semantic merge driver, retain only path-level equality constraints",
        hostile_reason="Git merge is a developer workflow, not a physics no-go theorem.",
        case=ProjectionCase(
            name="git_semantic_merge",
            source="T30",
            richer_system=richer,
            restricted_system=restricted,
            morphism=morphism,
            forgotten_structure=(
                "rename metadata",
                "semantic merge driver",
                "branch support for divergent path names",
            ),
            preserved_structure=("branch endpoints", "path-level merge proposition"),
            intended_reading=(
                "A rename-aware merge has a finite global section, while the "
                "path-only projection creates a local-to-global merge conflict."
            ),
        ),
    )


def database_expand_contract_case() -> HostileDomainCase:
    """Negative control: projection loses rollout detail without creating obstruction."""
    richer = D1RestrictionSystem(
        name="database_expand_contract_richer",
        proposition="schema_migration_contract",
        local_values=(
            _local("db_old_table", "legacy_schema", "database", "readable", D1Profile(2, 2, 1, 2)),
            _local("db_compat_view", "compatibility_view", "database", "bridging", D1Profile(3, 2, 1, 1)),
            _local("db_new_table", "new_schema", "database", "readable", D1Profile(2, 2, 1, 2)),
        ),
        transport_edges=(
            TransportEdge("db_old_table", "db_compat_view", "view_mapping"),
            TransportEdge("db_compat_view", "db_new_table", "dual_write"),
        ),
        source_site="db_old_table",
        target_site="db_new_table",
        patches=(
            _same_patch("old_to_view", ("db_old_table", "db_compat_view"), ("old_key", "view_key")),
            _same_patch("view_to_new", ("db_compat_view", "db_new_table"), ("view_key", "new_key")),
        ),
    )
    restricted = D1RestrictionSystem(
        name="database_flat_schema_restricted",
        proposition="schema_migration_contract",
        local_values=(
            _local("db_legacy_column", "legacy_schema", "database", "readable", D1Profile(1, 1, 0, 2)),
            _local("db_app_contract", "application", "database", "compatible", D1Profile(1, 1, 0, 2)),
            _local("db_new_column", "new_schema", "database", "readable", D1Profile(1, 1, 0, 2)),
        ),
        transport_edges=(
            TransportEdge("db_legacy_column", "db_app_contract", "app_mapping"),
            TransportEdge("db_app_contract", "db_new_column", "new_mapping"),
        ),
        source_site="db_legacy_column",
        target_site="db_new_column",
        patches=(
            _same_patch("legacy_to_app", ("db_legacy_column", "db_app_contract"), ("legacy_key", "app_key")),
            _same_patch("app_to_new", ("db_app_contract", "db_new_column"), ("app_key", "new_key")),
        ),
    )
    morphism = D1RestrictionMorphism(
        name="database_forget_expand_contract_rollout",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("db_old_table", "db_legacy_column"),
            SiteMap("db_compat_view", "db_app_contract"),
            SiteMap("db_new_table", "db_new_column"),
        ),
        preserved_dimensions=("reversal_cost",),
    )
    return HostileDomainCase(
        domain="database schema migration",
        expected_bias="negative",
        independent_projection_basis="forget expand-contract rollout metadata, retain flat old/app/new schema compatibility",
        hostile_reason="A safe migration can lose operational detail without producing an impossibility result.",
        case=ProjectionCase(
            name="database_expand_contract",
            source="T30",
            richer_system=richer,
            restricted_system=restricted,
            morphism=morphism,
            forgotten_structure=(
                "compatibility view rollout stage",
                "dual-write support",
                "deployment order metadata",
            ),
            preserved_structure=("old/app/new schema contract", "trusted migration path"),
            intended_reading=(
                "Projection loses migration detail, but both systems still "
                "have global sections. This should not count as PO1 support."
            ),
        ),
    )


def financial_risk_tail_model_case() -> HostileDomainCase:
    """High-stakes hostile case: tail-risk structure resolves flat risk obstruction.

    This is a finite toy model only. It is not a claim about any real portfolio,
    capital model, regulatory model, or investment decision.
    """
    richer = D1RestrictionSystem(
        name="financial_tail_risk_richer",
        proposition="portfolio_survives_stress",
        local_values=(
            _local("credit_tail_engine", "credit_risk", "risk_model", "tail_aware", D1Profile(3, 2, 1, 3)),
            _local("liquidity_feedback_engine", "liquidity_risk", "risk_model", "feedback_aware", D1Profile(3, 2, 1, 3)),
            _local("portfolio_stress_engine", "portfolio_risk", "risk_model", "stress_aware", D1Profile(4, 3, 1, 2)),
        ),
        transport_edges=(
            TransportEdge("credit_tail_engine", "portfolio_stress_engine", "stress_factor_transport"),
            TransportEdge("liquidity_feedback_engine", "portfolio_stress_engine", "liquidity_feedback_transport"),
        ),
        source_site="credit_tail_engine",
        target_site="portfolio_stress_engine",
        patches=(
            RestrictionPatch(
                "tail_regime_splits_normal_loss",
                ("credit_tail_engine", "portfolio_stress_engine"),
                ("normal_loss", "tail_loss"),
                (PatchConstraint("normal_loss", "tail_loss", "different"),),
            ),
            RestrictionPatch(
                "liquidity_buffer_tracks_tail",
                ("liquidity_feedback_engine", "portfolio_stress_engine"),
                ("liquidity_buffer", "tail_loss"),
                (PatchConstraint("liquidity_buffer", "tail_loss", "same"),),
            ),
            RestrictionPatch(
                "capital_buffer_tracks_liquidity",
                ("liquidity_feedback_engine", "portfolio_stress_engine"),
                ("capital_buffer", "liquidity_buffer"),
                (PatchConstraint("capital_buffer", "liquidity_buffer", "same"),),
            ),
        ),
    )
    restricted = _three_patch_obstruction_system(
        name="financial_flat_risk_restricted",
        proposition="portfolio_survives_stress",
        site_ids=("flat_credit_limit", "flat_liquidity_limit", "flat_portfolio_limit"),
        populations=("credit_desk", "liquidity_desk", "portfolio_committee"),
        patch_ids=("credit_agrees_with_portfolio", "liquidity_agrees_with_portfolio", "tail_dependence_breaks_flat_independence"),
        variable_prefix="flat_risk",
        profile=D1Profile(1, 1, 0, 4),
    )
    morphism = D1RestrictionMorphism(
        name="financial_forget_tail_dependence",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("credit_tail_engine", "flat_credit_limit"),
            SiteMap("liquidity_feedback_engine", "flat_liquidity_limit"),
            SiteMap("portfolio_stress_engine", "flat_portfolio_limit"),
        ),
        preserved_dimensions=("reversal_cost",),
    )
    return HostileDomainCase(
        domain="financial risk model",
        expected_bias="high_stakes_positive",
        independent_projection_basis=(
            "forget stress regimes, tail dependence, and liquidity feedback; "
            "retain only flat local risk-limit compatibility"
        ),
        hostile_reason=(
            "Financial risk is high-stakes and punishes vague analogies. The "
            "case must remain a toy finite model, not a finance theorem."
        ),
        case=ProjectionCase(
            name="financial_tail_risk_model",
            source="T30",
            richer_system=richer,
            restricted_system=restricted,
            morphism=morphism,
            forgotten_structure=(
                "stress-regime split between normal and tail losses",
                "tail dependence between credit and liquidity losses",
                "liquidity feedback and capital buffer structure",
            ),
            preserved_structure=("portfolio stress proposition", "flat risk-limit sites"),
            intended_reading=(
                "A tail-aware stress model has a finite global section, while "
                "the flattened local-limit projection creates a gluing "
                "obstruction. This is only a toy risk model."
            ),
        ),
    )


def access_control_inheritance_case() -> HostileDomainCase:
    """Negative control: policy contradiction exists before and after projection."""
    richer = _three_patch_obstruction_system(
        name="access_control_priority_richer",
        proposition="effective_permission",
        site_ids=("acl_role_allow", "acl_group_inherit", "acl_statutory_deny"),
        populations=("role_policy", "group_policy", "statutory_policy"),
        patch_ids=("role_allows_group", "group_inherits_resource", "statute_denies_role"),
        variable_prefix="acl_effect",
        profile=D1Profile(2, 2, 1, 3),
    )
    restricted = _three_patch_obstruction_system(
        name="access_control_flat_policy_restricted",
        proposition="effective_permission",
        site_ids=("flat_role", "flat_group", "flat_resource"),
        populations=("role_policy", "group_policy", "resource_policy"),
        patch_ids=("flat_role_group_same", "flat_group_resource_same", "flat_role_resource_different"),
        variable_prefix="flat_acl",
        profile=D1Profile(1, 1, 0, 2),
    )
    morphism = D1RestrictionMorphism(
        name="access_control_forget_policy_metadata",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("acl_role_allow", "flat_role"),
            SiteMap("acl_group_inherit", "flat_group"),
            SiteMap("acl_statutory_deny", "flat_resource"),
        ),
        preserved_dimensions=("reversal_cost",),
    )
    return HostileDomainCase(
        domain="access-control policy inheritance",
        expected_bias="negative",
        independent_projection_basis="flatten policy provenance and retain only effective allow/deny compatibility",
        hostile_reason="The richer policy object does not resolve the conflict; it only names it with more metadata.",
        case=ProjectionCase(
            name="access_control_inheritance",
            source="T30",
            richer_system=richer,
            restricted_system=restricted,
            morphism=morphism,
            forgotten_structure=("policy provenance", "priority labels", "audit explanation metadata"),
            preserved_structure=("effective permission contradiction",),
            intended_reading=(
                "Both rich and restricted policy systems are obstructed. This "
                "is inherited obstruction, not projection-created obstruction."
            ),
        ),
    )


def translator_poet_boundary_case() -> HostileDomainCase:
    """Anti-overclaim case: lost poetic meaning is not automatically PO1."""
    richer = D1RestrictionSystem(
        name="poetic_translation_richer",
        proposition="poem_translated_with_force",
        local_values=(
            _local("source_poem", "source_language", "translation", "poetic_form", D1Profile(3, 2, 1, 2)),
            _local("translator_poetics", "translator", "translation", "interpretive_notes", D1Profile(4, 2, 1, 1)),
            _local("target_poem", "target_language", "translation", "rendered_poem", D1Profile(3, 2, 1, 2)),
        ),
        transport_edges=(
            TransportEdge("source_poem", "translator_poetics", "reading"),
            TransportEdge("translator_poetics", "target_poem", "rendering"),
        ),
        source_site="source_poem",
        target_site="target_poem",
        patches=(
            _same_patch("image_carries_over", ("source_poem", "translator_poetics"), ("source_image", "interpreted_image")),
            _same_patch("image_rendered", ("translator_poetics", "target_poem"), ("interpreted_image", "target_image")),
        ),
    )
    restricted = D1RestrictionSystem(
        name="literal_translation_restricted",
        proposition="poem_translated_with_force",
        local_values=(
            _local("source_lexeme", "source_language", "translation", "literal_word", D1Profile(1, 1, 0, 2)),
            _local("target_lexeme", "target_language", "translation", "literal_word", D1Profile(1, 1, 0, 2)),
        ),
        transport_edges=(TransportEdge("source_lexeme", "target_lexeme", "dictionary_lookup"),),
        source_site="source_lexeme",
        target_site="target_lexeme",
        patches=(
            _same_patch("literal_word_mapping", ("source_lexeme", "target_lexeme"), ("source_word", "target_word")),
        ),
    )
    morphism = D1RestrictionMorphism(
        name="translation_forget_poetics",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("source_poem", "source_lexeme"),
            SiteMap("translator_poetics", "target_lexeme"),
            SiteMap("target_poem", "target_lexeme"),
        ),
        preserved_dimensions=("reversal_cost",),
    )
    return HostileDomainCase(
        domain="translator / poet",
        expected_bias="anti_overclaim",
        independent_projection_basis=(
            "forget image, rhythm, register, and interpretive poetics; retain "
            "only literal word mapping"
        ),
        hostile_reason=(
            "Translation loss is real, but PO1 should not absorb every loss of "
            "meaning into a finite gluing-obstruction claim."
        ),
        case=ProjectionCase(
            name="translator_poet_boundary",
            source="T30",
            richer_system=richer,
            restricted_system=restricted,
            morphism=morphism,
            forgotten_structure=(
                "poetic image",
                "rhythm and register",
                "translator judgment",
                "cultural resonance",
            ),
            preserved_structure=("literal word mapping",),
            intended_reading=(
                "The projection loses poetic structure, but the finite model "
                "does not produce a canonical gluing obstruction. This should "
                "block PO1 overreach."
            ),
        ),
        admissible_to_po1=False,
        admissibility_warning=(
            "No canonical finite same/different restriction system captures "
            "poetic force; treating this as PO1 would overclaim."
        ),
    )


def type_system_macro_boundary_case() -> HostileDomainCase:
    """Boundary case: macro expansion changes the site vocabulary."""
    richer = D1RestrictionSystem(
        name="type_system_macro_expansion_richer",
        proposition="type_preserving_compilation",
        local_values=(
            _local("typed_source_term", "source_language", "compiler", "typed", D1Profile(2, 1, 1, 2)),
            _local("macro_expansion_phase", "macro_system", "compiler", "expanded", D1Profile(3, 1, 1, 2)),
            _local("core_type_checker", "core_language", "compiler", "checked", D1Profile(2, 1, 1, 2)),
            _local("runtime_contract", "runtime", "compiler", "guarded", D1Profile(2, 1, 1, 1)),
        ),
        transport_edges=(
            TransportEdge("typed_source_term", "macro_expansion_phase", "expand"),
            TransportEdge("macro_expansion_phase", "core_type_checker", "check_core"),
            TransportEdge("core_type_checker", "runtime_contract", "emit_contract"),
        ),
        source_site="typed_source_term",
        target_site="runtime_contract",
        patches=(
            _same_patch("source_to_macro", ("typed_source_term", "macro_expansion_phase"), ("source_type", "expanded_type")),
            _same_patch("macro_to_core", ("macro_expansion_phase", "core_type_checker"), ("expanded_type", "core_type")),
            _same_patch("core_to_runtime", ("core_type_checker", "runtime_contract"), ("core_type", "runtime_type")),
        ),
    )
    restricted = D1RestrictionSystem(
        name="type_system_no_macro_restricted",
        proposition="type_preserving_compilation",
        local_values=(
            _local("syntax_node", "source_language", "compiler", "typed", D1Profile(1, 1, 0, 2)),
            _local("core_node", "core_language", "compiler", "checked", D1Profile(1, 1, 0, 2)),
            _local("runtime_node", "runtime", "compiler", "guarded", D1Profile(1, 1, 0, 1)),
        ),
        transport_edges=(
            TransportEdge("syntax_node", "core_node", "desugar"),
            TransportEdge("core_node", "runtime_node", "emit"),
        ),
        source_site="syntax_node",
        target_site="runtime_node",
        patches=(
            _same_patch("syntax_to_core", ("syntax_node", "core_node"), ("syntax_type", "core_type")),
            _same_patch("core_to_runtime", ("core_node", "runtime_node"), ("core_type", "runtime_type")),
        ),
    )
    morphism = D1RestrictionMorphism(
        name="type_system_forget_macro_phase",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("typed_source_term", "syntax_node"),
            SiteMap("core_type_checker", "core_node"),
            SiteMap("runtime_contract", "runtime_node"),
        ),
        preserved_dimensions=("reversal_cost",),
    )
    return HostileDomainCase(
        domain="type systems and macro expansion",
        expected_bias="boundary",
        independent_projection_basis="attempt to erase macro-expansion phase and compare source/core/runtime only",
        hostile_reason="Macro expansion introduces an intermediate syntactic category with no target site.",
        case=ProjectionCase(
            name="type_system_macro_expansion",
            source="T30",
            richer_system=richer,
            restricted_system=restricted,
            morphism=morphism,
            forgotten_structure=("macro expansion phase", "expanded syntax category"),
            preserved_structure=("source to core to runtime compilation intent",),
            intended_reading=(
                "The projection is not definable inside T26 because one source "
                "site has no target. This is a boundary, not PO1 support."
            ),
        ),
    )


def t30_hostile_cases() -> tuple[HostileDomainCase, ...]:
    return (
        git_semantic_merge_case(),
        financial_risk_tail_model_case(),
        translator_poet_boundary_case(),
    )


def analyze_hostile_case(case: HostileDomainCase) -> HostileCaseAnalysis:
    analysis = analyze_projection_case(case.case)
    raw_classification = CLASSIFICATION_BY_OUTCOME.get(analysis.schema.outcome, "no meaningful PO1 fit")
    classification = raw_classification if case.admissible_to_po1 else "no meaningful PO1 fit"
    supports_po1 = analysis.schema.schema_instance and case.admissible_to_po1
    meaningful = case.admissible_to_po1 and analysis.schema.outcome != "non_definable_projection"
    signal = _hypothesis_signal(supports_po1, analysis.schema.outcome, case.admissible_to_po1)
    return HostileCaseAnalysis(
        domain=case.domain,
        expected_bias=case.expected_bias,
        classification=classification,
        supports_po1=supports_po1,
        meaningful_po1_fit=meaningful,
        hypothesis_signal=signal,
        hostile_reason=case.hostile_reason if not case.admissibility_warning else f"{case.hostile_reason} {case.admissibility_warning}",
        independent_projection_basis=case.independent_projection_basis,
        analysis=analysis,
    )


def run_t30_lab() -> T30Result:
    analyses = tuple(analyze_hostile_case(case) for case in t30_hostile_cases())
    hypothesis_evaluations = _hypothesis_evaluations(analyses)
    return T30Result(
        analyses=analyses,
        hypothesis_evaluations=hypothesis_evaluations,
        best_supported_hypothesis="H2 with H4 admissibility constraints",
        po1_recommendation=(
            "Keep PO1 at partially_supported, but strengthen the evidence "
            "within that status. T30 finds two unrelated non-physics positive "
            "instances and one anti-overclaim boundary. The schema is not "
            "merely GU-specific, but translator/poet shows that future uses "
            "must pass an admissibility check before being counted as PO1 "
            "evidence."
        ),
        admissibility_constraints=(
            "Projection must be independently motivated by the domain, not chosen only to force a contradiction.",
            "The richer system must have a global section and the restricted system must be obstructed.",
            "Forgotten structure must be the same structure that resolves the restricted obstruction.",
            "Lossy projection without obstruction is not positive evidence.",
            "Shared obstruction is not positive evidence.",
            "Incomplete site maps are boundary cases, not failed positive instances.",
        ),
    )


def run_t30_analysis() -> dict[str, Any]:
    result = run_t30_lab()
    return {
        "hypotheses": list(HYPOTHESES),
        "analyses": [_analysis_to_dict(analysis) for analysis in result.analyses],
        "hypothesis_evaluations": [asdict(item) for item in result.hypothesis_evaluations],
        "best_supported_hypothesis": result.best_supported_hypothesis,
        "po1_recommendation": result.po1_recommendation,
        "admissibility_constraints": list(result.admissibility_constraints),
    }


def _hypothesis_evaluations(
    analyses: tuple[HostileCaseAnalysis, ...],
) -> tuple[HypothesisEvaluation, ...]:
    positives = tuple(item.analysis.case.name for item in analyses if item.supports_po1)
    non_positive = tuple(item.analysis.case.name for item in analyses if not item.supports_po1)
    non_definable = tuple(
        item.analysis.case.name
        for item in analyses
        if item.analysis.schema.outcome == "non_definable_projection"
    )
    negative_controls = tuple(
        item.analysis.case.name
        for item in analyses
        if item.analysis.schema.outcome
        in {"lossy_projection_no_new_obstruction", "shared_obstruction_not_projection_created"}
    )
    anti_overclaim = tuple(
        item.analysis.case.name
        for item in analyses
        if not item.meaningful_po1_fit
    )
    return (
        HypothesisEvaluation(
            hypothesis_id="H0",
            status="rejected_in_finite_scope",
            evidence_for=tuple(),
            evidence_against=positives,
            verdict="At least one non-physics hostile case instantiates PO1.",
        ),
        HypothesisEvaluation(
            hypothesis_id="H1",
            status="supported",
            evidence_for=positives,
            evidence_against=tuple(),
            verdict="PO1 applies to at least one non-physics domain in T30.",
        ),
        HypothesisEvaluation(
            hypothesis_id="H2",
            status="supported_in_finite_scope" if len(positives) >= 2 else "not_yet_supported",
            evidence_for=positives,
            evidence_against=non_positive,
            verdict=(
                "T30 shows multiple unrelated non-physics positives, but not universality."
                if len(positives) >= 2
                else "T30 does not show broad cross-domain generality."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H3",
            status="not_supported_by_current_candidates" if not non_definable else "partially_supported",
            evidence_for=non_definable,
            evidence_against=_unique(positives + anti_overclaim),
            verdict=(
                "The revised T30 candidate set does not require new machinery; "
                "the translator/poet boundary is an admissibility failure, not "
                "a category upgrade."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H4",
            status="partially_supported_as_warning",
            evidence_for=_unique(negative_controls + anti_overclaim),
            evidence_against=positives,
            verdict="PO1 is useful only with admissibility constraints; meaningful loss alone is not finite gluing obstruction.",
        ),
    )


def _unique(items: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(items))


def _hypothesis_signal(supports_po1: bool, outcome: str, admissible: bool) -> str:
    if not admissible:
        return "supports H4 anti-overclaim boundary"
    if supports_po1:
        return "supports H1/H2 and pushes against H0"
    if outcome == "non_definable_projection":
        return "supports H3 boundary"
    if outcome == "lossy_projection_no_new_obstruction":
        return "supports H4 constraint: loss alone is insufficient"
    if outcome == "shared_obstruction_not_projection_created":
        return "supports H4 constraint: inherited obstruction is insufficient"
    return "no meaningful PO1 fit"


def _analysis_to_dict(item: HostileCaseAnalysis) -> dict[str, Any]:
    analysis = item.analysis
    case = analysis.case
    return {
        "name": case.name,
        "domain": item.domain,
        "expected_bias": item.expected_bias,
        "classification": item.classification,
        "supports_po1": item.supports_po1,
        "meaningful_po1_fit": item.meaningful_po1_fit,
        "hypothesis_signal": item.hypothesis_signal,
        "hostile_reason": item.hostile_reason,
        "independent_projection_basis": item.independent_projection_basis,
        "intended_reading": case.intended_reading,
        "richer_system": _system_summary(case.richer_system),
        "restricted_system": _system_summary(case.restricted_system),
        "morphism": asdict(analysis.morphism_analysis),
        "schema": asdict(analysis.schema),
        "forgotten_structure": list(case.forgotten_structure),
        "preserved_structure": list(case.preserved_structure),
        "verdict": analysis.verdict,
    }


def _system_summary(system: D1RestrictionSystem) -> dict[str, Any]:
    validation = validate_system(system)
    section = global_section(system)
    return {
        "name": system.name,
        "site_count": len(system.site_ids()),
        "patch_count": len(system.patches),
        "edge_count": len(system.transport_edges),
        "validation_valid": validation.valid,
        "global_assignment_exists": section.global_assignment_exists,
        "local_witness_count": section.local_witness_count,
        "global_witness_count": section.global_witness_count,
        "obstruction_detected": section.obstruction_detected,
    }


def _three_patch_obstruction_system(
    name: str,
    proposition: str,
    site_ids: tuple[str, str, str],
    populations: tuple[str, str, str],
    patch_ids: tuple[str, str, str],
    variable_prefix: str,
    profile: D1Profile,
) -> D1RestrictionSystem:
    left, middle, right = site_ids
    a = f"{variable_prefix}_a"
    b = f"{variable_prefix}_b"
    c = f"{variable_prefix}_c"
    return D1RestrictionSystem(
        name=name,
        proposition=proposition,
        local_values=(
            _local(left, populations[0], "restriction_site", "local", profile),
            _local(middle, populations[1], "restriction_site", "local", profile),
            _local(right, populations[2], "restriction_site", "local", profile),
        ),
        transport_edges=(
            TransportEdge(left, middle, "trusted_local"),
            TransportEdge(middle, right, "trusted_local"),
        ),
        source_site=left,
        target_site=right,
        patches=(
            RestrictionPatch(patch_ids[0], (left, middle), (a, b), (PatchConstraint(a, b, "same"),)),
            RestrictionPatch(patch_ids[1], (middle, right), (b, c), (PatchConstraint(b, c, "same"),)),
            RestrictionPatch(patch_ids[2], (left, right), (a, c), (PatchConstraint(a, c, "different"),)),
        ),
    )


def _same_patch(
    patch_id: str,
    site_ids: tuple[str, str],
    variables: tuple[str, str],
) -> RestrictionPatch:
    return RestrictionPatch(
        patch_id=patch_id,
        site_ids=site_ids,
        variables=variables,
        constraints=(PatchConstraint(variables[0], variables[1], "same"),),
    )


def _local(
    observer_id: str,
    population: str,
    scale: str,
    value: str,
    profile: D1Profile,
) -> LocalD1Value:
    return LocalD1Value(
        site=ObserverSite(observer_id, population, scale, 0, "t30"),
        proposition_value=value,
        profile=profile,
    )
