"""T390: class-shape alignment screen.

This screen uses the GU-formalization repo as a source of class-level material,
not as a target to vindicate GU. The question is whether TaF's current chain
fits the broader Clifford-RS / chimeric-bundle observerse class information:

    record-finalizable shared state
      -> mutual local attestability
      -> bidirectional handshake
      -> open two-leg-to-null bridge

The verdict is deliberately adversarial. The class material does not solve the
two-leg-to-null bridge, and the newest temporal-issuance explorations warn that
shadow/projection language is often an absorber: it can name useful interface
vocabulary without proving that the metaphor is the correct source structure.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ClassSourceFact:
    fact_id: str
    source_path: str
    statement: str
    relevance_to_taf: str


@dataclass(frozen=True)
class TemporalIssuanceCaution:
    caution_id: str
    source_path: str
    statement: str
    consequence_for_taf: str


@dataclass(frozen=True)
class AlignmentVerdict:
    alignment_id: str
    taf_object: str
    class_feature: str
    classification: str
    fit_strength: str
    resolves_two_leg_to_null_bridge: bool
    reason: str
    next_test: str


@dataclass(frozen=True)
class ComparatorVerdict:
    comparator_id: str
    status: str
    absorbs: bool
    reason: str


@dataclass(frozen=True)
class T390Result:
    uses_class_not_gu_specific: bool
    class_material_resolves_two_leg_to_null_bridge: bool
    class_material_supplies_testable_bridge_hypothesis: bool
    temporal_issuance_demotes_shadow_definiteness: bool
    shadow_projection_definiteness_rejected: bool
    source_action_observer_slice_rejected: bool
    generation_chirality_mapping_rejected: bool
    direct_14d_to_two_leg_identity_rejected: bool
    strongest_fit_ids: tuple[str, ...]
    rejected_overfit_ids: tuple[str, ...]
    source_facts: tuple[ClassSourceFact, ...]
    temporal_issuance_cautions: tuple[TemporalIssuanceCaution, ...]
    alignment_verdicts: tuple[AlignmentVerdict, ...]
    comparator_verdicts: tuple[ComparatorVerdict, ...]
    overall_verdict: str
    strongest_claim: str
    claim_ledger_update: str
    recommended_next_goal: str


def class_source_facts() -> tuple[ClassSourceFact, ...]:
    return (
        ClassSourceFact(
            "class_not_gu_specific",
            "gu-formalization/RESEARCH-PROGRAM.md",
            (
                "The surviving program is described as a GU-independent class of geometry: "
                "the Clifford-RS / chimeric-bundle observerse."
            ),
            "TaF should align to the class-level structure, not to GU-specific closure claims.",
        ),
        ClassSourceFact(
            "observer_universe_external_boundary",
            "gu-formalization/RESEARCH-PROGRAM.md",
            (
                "The interior observer universe is balanced and reversible; chirality or "
                "generation count is external boundary data."
            ),
            "This resembles TaF's distinction between observer rendering and external/interface conditions.",
        ),
        ClassSourceFact(
            "class_structural_law_external_count",
            "gu-formalization/RESEARCH-PROGRAM.md",
            (
                "No covariant operator interior to the Clifford-RS sector is currently able "
                "to force an odd chiral generation count."
            ),
            "This warns against mapping TaF's two-leg signal basis to generation count or chirality.",
        ),
        ClassSourceFact(
            "missing_source_action_spec",
            "gu-formalization/docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md",
            (
                "The missing RS/IG source action must satisfy BV consistency, force the "
                "constraint by Noether identity, supply a non-equivariant compensator, "
                "realize the constraint cohomologically, and provide global boundary/index data."
            ),
            "This is a candidate shape for a real interface rulebook, not a solved TaF bridge.",
        ),
        ClassSourceFact(
            "source_action_observer_slice_killed",
            "gu-formalization/docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md",
            (
                "The source action as the observer's slice or one global object with the "
                "index was explicitly marked a forced analogy."
            ),
            "TaF must not revive that mapping by renaming the handshake as the source action.",
        ),
        ClassSourceFact(
            "forgetful_image_relation_side",
            "gu-formalization/canon/no-go-class-relative-map.md",
            (
                "Class-relative maps emphasize richer substrate data and forgetful shadows; "
                "the relation-side can survive while the mechanism is forgotten."
            ),
            (
                "This is a possible pattern for TaF's observer rendering, but it must be "
                "treated as a cautioned heuristic rather than a favored ontology."
            ),
        ),
        ClassSourceFact(
            "riemannian_ehresmannian_shadow",
            "gu-formalization/canon/no-go-class-relative-map.md",
            (
                "The Riemannian-reduction functor forgets Ehresmannian distortion data while "
                "retaining the smooth effective relation-side."
            ),
            (
                "This suggests an analogy to test with absorber controls; it does not make "
                "shadow projection the correct metaphor by default."
            ),
        ),
        ClassSourceFact(
            "truth_seeking_posture",
            "gu-formalization/RESEARCH-POSTURE.md",
            (
                "GU is used as a generative test case; the method keeps only falsifiable "
                "structure that survives adversarial checks."
            ),
            "The alignment screen should be adversarial and allowed to reject attractive matches.",
        ),
    )


def temporal_issuance_cautions() -> tuple[TemporalIssuanceCaution, ...]:
    return (
        TemporalIssuanceCaution(
            "record_table_demoted_to_interface",
            "temporal-issuance/explorations/E107-record-table-online-issuance-lift-or-demote-2026-07-01.md",
            (
                "The record-table route is useful interface vocabulary but is demoted as "
                "an independent formal object; it does not beat fixed precontainment by itself."
            ),
            (
                "TaF should not treat a good projection/interface map as evidence that the "
                "shadow metaphor is source-correct."
            ),
        ),
        TemporalIssuanceCaution(
            "external_completion_absorbs_lc_witness",
            "temporal-issuance/explorations/E108-online-issuance-witness-machine-check-2026-07-01.md",
            (
                "The local-constructive witness is executable, but external Platonist "
                "completion still absorbs the whole trace outside the local constructive class."
            ),
            (
                "A class-relative success can be real while still failing as physical or "
                "metaphysical source evidence."
            ),
        ),
        TemporalIssuanceCaution(
            "projection_access_negative_rejected",
            "temporal-issuance/explorations/E113-oi-lc-assembly-source-adapter-fixture-2026-07-01.md",
            (
                "Projection access, fixed complete assembly space, experimenter-added schema, "
                "and fixed search processes are all rejected as source evidence."
            ),
            (
                "Any TaF shadow/projection story needs negative controls for fixed-source, "
                "bounded access, modeler schema, and fixed search or dynamics."
            ),
        ),
        TemporalIssuanceCaution(
            "candidate_scout_not_evidence",
            "temporal-issuance/explorations/E112-oi-lc-candidate-scout-w1-w6-table-2026-07-01.md",
            (
                "A fixture-candidate verdict means test this next, not evidence; GU-style "
                "adapter language remains parked under bounded-access and gauge-language pressure."
            ),
            (
                "T390 should route to an absorber screen, not to a confirmation-seeking "
                "class-shadow derivation."
            ),
        ),
    )


def alignment_verdicts() -> tuple[AlignmentVerdict, ...]:
    return (
        AlignmentVerdict(
            "taf_record_finality_to_class_observer_universe",
            "record-finalizable shared-state compatibility",
            "observer universe as rendered interior plus external boundary/interface conditions",
            "natural_fit",
            "strong",
            False,
            (
                "Both frames distinguish an internally rendered observer world from the "
                "boundary/interface conditions that make it physically nontrivial."
            ),
            "Test whether TaF finalizable records behave like a relation-side shadow of richer class data.",
        ),
        AlignmentVerdict(
            "taf_finality_to_class_forgetful_shadow",
            "observer rendering from finalizable compatibility",
            "class-relative forgetful image where relation-side survives and mechanism is lost",
            "cautionary_bridge_heuristic",
            "medium",
            False,
            (
                "The class map gives a possible pattern for TaF, but temporal-issuance "
                "E107-E113 warn that projection/access language can be absorbed by fixed "
                "source, fixed boundary, bounded-access, or modeler-schema explanations."
            ),
            "Build an absorber screen before using shadow projection as a live bridge metaphor.",
        ),
        AlignmentVerdict(
            "taf_handshake_to_source_rulebook",
            "minimal bidirectional handshake",
            "missing RS/IG source action as an interface rulebook",
            "partial_hypothesis",
            "medium",
            False,
            (
                "Both are rulebook-shaped interface objects, but the source action has BV, "
                "Noether, cohomology, and global boundary requirements absent from TaF's handshake."
            ),
            "Ask whether TaF's handshake can be upgraded to a typed source-rulebook without importing nullness.",
        ),
        AlignmentVerdict(
            "taf_two_leg_to_ehresmannian_hidden_mechanism",
            "two-leg-to-null signal bridge",
            "Riemannian shadow forgetting Ehresmannian mechanism data",
            "cautionary_bridge_heuristic",
            "weak_to_medium",
            False,
            (
                "The class material suggests one place to look, but the temporal-issuance "
                "controls make this only a hypothesis to try to break, not a derivation."
            ),
            "Compare null, timelike, delayed, hidden-mechanism, fixed-source, and bounded-access fixtures.",
        ),
        AlignmentVerdict(
            "taf_two_null_basis_to_generation_chirality",
            "two primitive null compatibility-signal directions",
            "external chirality or odd generation count",
            "rejected_overfit",
            "none",
            False,
            (
                "The class documents treat chirality/generation count as an external count "
                "problem. TaF's two signal directions are not the same object."
            ),
            "Keep chirality/generation count out of the TaF bridge unless a concrete functor is built.",
        ),
        AlignmentVerdict(
            "taf_handshake_as_source_action_observer_slice",
            "bidirectional handshake or observer rendering",
            "source action equals observer slice/global index",
            "rejected_overfit",
            "none",
            False,
            (
                "The GU-formalization capstone explicitly marks this source-action/observer-slice "
                "reading as a forced analogy."
            ),
            "Reject any alignment that depends on source action = observer slice.",
        ),
        AlignmentVerdict(
            "taf_two_legs_as_14d_class_identity",
            "two protocol legs",
            "14-dimensional class geometry",
            "rejected_overfit",
            "none",
            False,
            (
                "A 14D class object can host or project structures, but it is not identical "
                "to TaF's two primitive legs."
            ),
            "Require an explicit projection or shadow functor before using 14D class data.",
        ),
        AlignmentVerdict(
            "taf_nullness_from_class_material",
            "nullness and bilinear interval",
            "class-level geometry and noncompact-fiber/Ehresmannian data",
            "open_not_resolved",
            "partial",
            False,
            (
                "The class material gives plausible geometric machinery, but it does not by "
                "itself derive TaF's nullness, bilinearity, or invariant signal unit."
            ),
            "Run the two-leg-to-null screen with class-shadow controls.",
        ),
    )


def comparator_verdicts() -> tuple[ComparatorVerdict, ...]:
    return (
        ComparatorVerdict(
            "gu_specific_vindication",
            "rejected_scope",
            False,
            "the screen uses GU-formalization only as class-level source material, not as a GU proof",
        ),
        ComparatorVerdict(
            "two_leg_to_null_bridge",
            "still_open",
            True,
            "the class material suggests a metaphor to stress-test but does not resolve nullness or bilinearity",
        ),
        ComparatorVerdict(
            "forgetful_shadow_hypothesis",
            "demoted_to_cautionary_heuristic",
            True,
            "temporal-issuance controls show projection/access stories can be interface vocabulary without source evidence",
        ),
        ComparatorVerdict(
            "temporal_issuance_projection_absorber",
            "active_caution",
            True,
            "E107-E113 require fixed-source, fixed-boundary, bounded-access, schema, and search/dynamics controls",
        ),
        ComparatorVerdict(
            "source_action_shortcut",
            "blocked",
            False,
            "the source-action-as-observer-slice analogy is explicitly killed in the source repo",
        ),
        ComparatorVerdict(
            "chirality_generation_shortcut",
            "blocked",
            False,
            "external generation/chirality is a different class-level problem from TaF's two-leg basis",
        ),
    )


def run_t390_analysis() -> T390Result:
    verdicts = alignment_verdicts()
    strongest = tuple(
        verdict.alignment_id
        for verdict in verdicts
        if verdict.classification == "natural_fit"
    )
    rejected = tuple(
        verdict.alignment_id
        for verdict in verdicts
        if verdict.classification == "rejected_overfit"
    )
    return T390Result(
        uses_class_not_gu_specific=True,
        class_material_resolves_two_leg_to_null_bridge=False,
        class_material_supplies_testable_bridge_hypothesis=True,
        temporal_issuance_demotes_shadow_definiteness=True,
        shadow_projection_definiteness_rejected=True,
        source_action_observer_slice_rejected=(
            "taf_handshake_as_source_action_observer_slice" in rejected
        ),
        generation_chirality_mapping_rejected=(
            "taf_two_null_basis_to_generation_chirality" in rejected
        ),
        direct_14d_to_two_leg_identity_rejected=(
            "taf_two_legs_as_14d_class_identity" in rejected
        ),
        strongest_fit_ids=strongest,
        rejected_overfit_ids=rejected,
        source_facts=class_source_facts(),
        temporal_issuance_cautions=temporal_issuance_cautions(),
        alignment_verdicts=verdicts,
        comparator_verdicts=comparator_verdicts(),
        overall_verdict=(
            "class_material_suggests_shadow_heuristic_but_temporal_issuance_rejects_definite_projection_metaphor"
        ),
        strongest_claim=(
            "The GU-formalization class material does not solve TaF's two-leg-to-null bridge. "
            "Its shadow/projection language is useful only as a cautioned heuristic. The "
            "new temporal-issuance explorations show why that metaphor cannot be treated "
            "as definitely correct: fixed-source, fixed-boundary, bounded-access, schema, "
            "and search/dynamics absorbers can reproduce projection-style stories. Direct "
            "mappings to source action, 14D geometry, or generation/chirality remain rejected "
            "as overfits."
        ),
        claim_ledger_update=(
            "Register T390 as a class-shape alignment screen: use the class material as a "
            "hypothesis generator, not a GU vindication or definitive shadow metaphor; "
            "next target is a projection-metaphor absorber screen."
        ),
        recommended_next_goal=(
            "T391 projection-metaphor absorber screen: test whether the shadow/projection "
            "reading of TaF's two-leg-to-null bridge survives fixed-source, fixed-boundary, "
            "bounded-access, modeler-schema, search/dynamics, timelike-leg, delayed/noisy-leg, "
            "gauge-relabel, source-action, generation/chirality, and direct-14D controls."
        ),
    )


def t390_result_to_dict(result: T390Result) -> dict[str, object]:
    return {
        "uses_class_not_gu_specific": result.uses_class_not_gu_specific,
        "class_material_resolves_two_leg_to_null_bridge": (
            result.class_material_resolves_two_leg_to_null_bridge
        ),
        "class_material_supplies_testable_bridge_hypothesis": (
            result.class_material_supplies_testable_bridge_hypothesis
        ),
        "temporal_issuance_demotes_shadow_definiteness": (
            result.temporal_issuance_demotes_shadow_definiteness
        ),
        "shadow_projection_definiteness_rejected": (
            result.shadow_projection_definiteness_rejected
        ),
        "source_action_observer_slice_rejected": result.source_action_observer_slice_rejected,
        "generation_chirality_mapping_rejected": result.generation_chirality_mapping_rejected,
        "direct_14d_to_two_leg_identity_rejected": result.direct_14d_to_two_leg_identity_rejected,
        "strongest_fit_ids": list(result.strongest_fit_ids),
        "rejected_overfit_ids": list(result.rejected_overfit_ids),
        "source_facts": [
            {
                "fact_id": fact.fact_id,
                "source_path": fact.source_path,
                "statement": fact.statement,
                "relevance_to_taf": fact.relevance_to_taf,
            }
            for fact in result.source_facts
        ],
        "temporal_issuance_cautions": [
            {
                "caution_id": caution.caution_id,
                "source_path": caution.source_path,
                "statement": caution.statement,
                "consequence_for_taf": caution.consequence_for_taf,
            }
            for caution in result.temporal_issuance_cautions
        ],
        "alignment_verdicts": [
            {
                "alignment_id": verdict.alignment_id,
                "taf_object": verdict.taf_object,
                "class_feature": verdict.class_feature,
                "classification": verdict.classification,
                "fit_strength": verdict.fit_strength,
                "resolves_two_leg_to_null_bridge": verdict.resolves_two_leg_to_null_bridge,
                "reason": verdict.reason,
                "next_test": verdict.next_test,
            }
            for verdict in result.alignment_verdicts
        ],
        "comparator_verdicts": [
            {
                "comparator_id": verdict.comparator_id,
                "status": verdict.status,
                "absorbs": verdict.absorbs,
                "reason": verdict.reason,
            }
            for verdict in result.comparator_verdicts
        ],
        "overall_verdict": result.overall_verdict,
        "strongest_claim": result.strongest_claim,
        "claim_ledger_update": result.claim_ledger_update,
        "recommended_next_goal": result.recommended_next_goal,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t390_result_to_dict(run_t390_analysis()), indent=2))
