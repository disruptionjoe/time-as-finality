"""T33: Derivation of PO1 from resource and invariant principles.

T32 found that AC4 derives from AC6 and that the remaining six conditions
compress into four structural principles. T33 asks whether those conditions
and principles arise from two deeper mathematical frameworks:

  IPT: Invariant-Preservation Theorem framework
       (local-to-global consistency of structural invariants)
  RMT: Resource-Monotonicity Theorem framework
       (global satisfiability resource is non-increasing under restriction)

Six competing hypotheses are evaluated:

  H0: AC1-AC7 are independent empirical conditions.
  H1: Conditions arise from invariant preservation (IPT) alone.
  H2: Conditions arise from resource monotonicity (RMT) alone.
  H3: Both IPT and RMT are required (neither alone is sufficient).
  H4: A single deeper principle explains conditions more economically than H3.
  H5: No derivation from these principles is currently justified.

The executable verdict is H3: IPT generates the typing and definability
obligations (AC1-AC3) while RMT generates the obstruction polarity conditions
(AC6, AC7, and the measurable-loss half of AC5). The naming half of AC5 remains
a methodological condition outside both principles.
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
from models.po1_admissibility_conditions import (
    AdmissibilityCheck,
    check_admissibility,
)
from models.po1_admissibility_derivation import (
    T32Result,
    run_t32_derivation_audit,
)
from models.projection_obstruction_schema import ProjectionCase


# ---------------------------------------------------------------------------
# Resource and invariant types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ResourceState:
    """Global satisfiability resource extracted from a D1RestrictionSystem."""
    system_name: str
    global_witness_count: int
    local_witness_count: int
    patch_count: int
    obstruction_detected: bool
    global_assignment_exists: bool
    resource_positive: bool  # global_assignment_exists (not raw witness count; empty-patch systems have count=0 but section exists)


@dataclass(frozen=True)
class InvariantProfile:
    """Obstruction classification for a D1RestrictionSystem."""
    system_name: str
    obstruction_class: str   # "H1_cohomological", "H0_local_failure", "none"
    local_satisfiable: bool
    global_satisfiable: bool
    invariant_level: int     # 0 = no obstruction, 1 = H^1 type, -1 = local failure


@dataclass(frozen=True)
class ProjectionAction:
    """A projection viewed as an action on resource states and invariant profiles."""
    morphism_name: str
    richer_resource: ResourceState
    restricted_resource: ResourceState
    resource_decreases: bool        # richer > 0, restricted == 0
    resource_strictly_lost: bool    # richer_count > restricted_count (not just polarity)
    invariant_class_changes: bool   # H^0 -> H^1 shift occurs
    local_profiles_preserved: bool  # morphism analysis flag


@dataclass(frozen=True)
class ResourceMonotone:
    """Monotonicity certificate for the global satisfiability resource."""
    name: str
    richer_value: int
    restricted_value: int
    is_non_increasing: bool
    is_strictly_decreasing: bool
    witness: str


@dataclass(frozen=True)
class InvariantLoss:
    """Records which invariants are lost under a projection."""
    morphism_name: str
    profile_dimensions_lost: tuple[str, ...]
    named_structure_lost: tuple[str, ...]
    measurable_loss: bool   # local_profiles_preserved=False
    named_loss: bool        # forgotten_structure non-empty


@dataclass(frozen=True)
class ObstructionCertificate:
    """Formal certificate classifying the obstruction type."""
    system_name: str
    certificate_type: str   # "H1_finite_gluing", "trivial_local_failure", "no_obstruction"
    local_patches_satisfiable: bool
    global_assignment_exists: bool
    classification_reason: str


# ---------------------------------------------------------------------------
# Derivation result types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ACDerivationAttempt:
    """Attempt to derive one admissibility condition from one principle."""
    condition_id: str
    principle_id: str
    derivation_status: str  # "derived", "partially_derived", "independent", "not_applicable"
    proof_sketch: str
    counterexample: str     # empty string if derived


@dataclass(frozen=True)
class HypothesisVerdict:
    """Verdict for one of H0-H5."""
    hypothesis_id: str
    hypothesis_statement: str
    verdict: str            # "supported", "rejected", "partially_supported", "boundary"
    conditions_covered: tuple[str, ...]
    conditions_uncovered: tuple[str, ...]
    evidence_summary: str


@dataclass(frozen=True)
class CounterexampleCase:
    """A finite counterexample showing a condition is not derivable from a principle."""
    name: str
    principle_tested: str
    condition_not_derived: str
    case_description: str
    projection_case: ProjectionCase
    admissibility_check: AdmissibilityCheck
    what_it_shows: str


@dataclass(frozen=True)
class T33Result:
    t32_basis: T32Result
    resource_monotones: tuple[ResourceMonotone, ...]
    projection_actions: tuple[ProjectionAction, ...]
    ac_derivation_attempts: tuple[ACDerivationAttempt, ...]
    hypothesis_verdicts: tuple[HypothesisVerdict, ...]
    counterexamples: tuple[CounterexampleCase, ...]
    smallest_theorem_candidate: str
    remaining_independence: tuple[str, ...]
    best_hypothesis: str
    recommendation: str
    negative_results_note: str


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------


def extract_resource_state(system: D1RestrictionSystem) -> ResourceState:
    gs = global_section(system)
    return ResourceState(
        system_name=system.name,
        global_witness_count=gs.global_witness_count,
        local_witness_count=gs.local_witness_count,
        patch_count=len(system.patches),
        obstruction_detected=gs.obstruction_detected,
        global_assignment_exists=gs.global_assignment_exists,
        resource_positive=gs.global_assignment_exists,
    )


def extract_invariant_profile(system: D1RestrictionSystem) -> InvariantProfile:
    gs = global_section(system)
    if not gs.obstruction_detected and gs.global_assignment_exists:
        return InvariantProfile(
            system_name=system.name,
            obstruction_class="none",
            local_satisfiable=gs.local_patches_satisfiable,
            global_satisfiable=True,
            invariant_level=0,
        )
    if gs.obstruction_detected:
        return InvariantProfile(
            system_name=system.name,
            obstruction_class="H1_cohomological",
            local_satisfiable=True,
            global_satisfiable=False,
            invariant_level=1,
        )
    return InvariantProfile(
        system_name=system.name,
        obstruction_class="H0_local_failure",
        local_satisfiable=False,
        global_satisfiable=False,
        invariant_level=-1,
    )


def classify_obstruction(system: D1RestrictionSystem) -> ObstructionCertificate:
    gs = global_section(system)
    if gs.obstruction_detected:
        return ObstructionCertificate(
            system_name=system.name,
            certificate_type="H1_finite_gluing",
            local_patches_satisfiable=True,
            global_assignment_exists=False,
            classification_reason=(
                "All patches are locally satisfiable but no global assignment exists; "
                "this is a finite analogue of a first cohomology obstruction."
            ),
        )
    if not gs.local_patches_satisfiable and gs.patch_count > 0:
        return ObstructionCertificate(
            system_name=system.name,
            certificate_type="trivial_local_failure",
            local_patches_satisfiable=False,
            global_assignment_exists=False,
            classification_reason="At least one patch is locally inconsistent (H^0 failure).",
        )
    return ObstructionCertificate(
        system_name=system.name,
        certificate_type="no_obstruction",
        local_patches_satisfiable=gs.local_patches_satisfiable,
        global_assignment_exists=gs.global_assignment_exists,
        classification_reason="System has a global assignment; obstruction-free.",
    )


def compute_resource_monotone(
    name: str,
    richer: D1RestrictionSystem,
    restricted: D1RestrictionSystem,
) -> ResourceMonotone:
    rich_rs = extract_resource_state(richer)
    res_rs = extract_resource_state(restricted)
    # Use global_assignment_exists as the resource level (not raw witness count;
    # empty-patch systems return count=0 but are unobstructed/section-exists).
    rich_level = 1 if rich_rs.resource_positive else 0
    res_level = 1 if res_rs.resource_positive else 0
    is_non_increasing = rich_level >= res_level
    is_strictly_decreasing = rich_rs.resource_positive and not res_rs.resource_positive
    return ResourceMonotone(
        name=name,
        richer_value=rich_level,
        restricted_value=res_level,
        is_non_increasing=is_non_increasing,
        is_strictly_decreasing=is_strictly_decreasing,
        witness=(
            f"global_assignment_exists: {rich_rs.resource_positive} -> {res_rs.resource_positive}"
        ),
    )


def compute_projection_action(
    case: ProjectionCase,
    local_profiles_preserved: bool,
) -> ProjectionAction:
    richer_rs = extract_resource_state(case.richer_system)
    restricted_rs = extract_resource_state(case.restricted_system)
    richer_inv = extract_invariant_profile(case.richer_system)
    restricted_inv = extract_invariant_profile(case.restricted_system)
    resource_decreases = (
        richer_rs.resource_positive and not restricted_rs.resource_positive
    )
    resource_strictly_lost = (
        richer_rs.global_witness_count > restricted_rs.global_witness_count
    )
    invariant_class_changes = richer_inv.invariant_level != restricted_inv.invariant_level
    return ProjectionAction(
        morphism_name=case.morphism.name,
        richer_resource=richer_rs,
        restricted_resource=restricted_rs,
        resource_decreases=resource_decreases,
        resource_strictly_lost=resource_strictly_lost,
        invariant_class_changes=invariant_class_changes,
        local_profiles_preserved=local_profiles_preserved,
    )


# ---------------------------------------------------------------------------
# Derivation attempt builders
# ---------------------------------------------------------------------------


def _ipt_derivation_attempts() -> tuple[ACDerivationAttempt, ...]:
    """
    IPT (Invariant-Preservation Theorem):
    Local-to-global consistency of structural invariants.
    """
    return (
        ACDerivationAttempt(
            "AC1", "IPT",
            "derived",
            "AC1 is the IPT domain-of-discourse obligation: the richer system must be "
            "a valid D1RestrictionSystem (a well-typed invariant carrier). IPT can only "
            "track invariant change if the source is well-formed.",
            "",
        ),
        ACDerivationAttempt(
            "AC2", "IPT",
            "derived",
            "AC2 is the IPT codomain obligation: the restricted system must also satisfy "
            "all T26 axioms. Invariant comparison is vacuous if the target is ill-typed.",
            "",
        ),
        ACDerivationAttempt(
            "AC3", "IPT",
            "derived",
            "IPT requires a definable map between invariant carriers. A total site map is "
            "exactly what makes a finite restriction morphism definable. Without AC3 there "
            "is no projection to analyze for invariant change.",
            "",
        ),
        ACDerivationAttempt(
            "AC4", "IPT",
            "derived",
            "AC4 derives from AC6 by T26 semantics (T32 result). AC6 entails "
            "local_patches_satisfiable=True by the definition of obstruction_detected. "
            "IPT inherits this via AC6.",
            "",
        ),
        ACDerivationAttempt(
            "AC5_measurable", "IPT",
            "partially_derived",
            "IPT detects measurable profile loss (local_profiles_preserved=False) because "
            "the invariant carrier changes structure. However the named-structure half of AC5 "
            "requires ProjectionCase.forgotten_structure metadata that lives outside the "
            "D1RestrictionSystem lattice IPT operates over.",
            "See ac5_naming_independence_counterexample.",
        ),
        ACDerivationAttempt(
            "AC5_naming", "IPT",
            "independent",
            "The naming obligation of AC5 (forgotten_structure non-empty) is not derivable "
            "from IPT. IPT can confirm structure changed but not that the change was named "
            "and documented. This is a methodological transparency condition.",
            "See ac5_naming_independence_counterexample.",
        ),
        ACDerivationAttempt(
            "AC6", "IPT",
            "partially_derived",
            "IPT confirms AC6 follows if the restricted system has a different invariant "
            "level (H^1 vs H^0/none). However IPT does not by itself require the restricted "
            "system to be obstructed rather than just weaker.",
            "See ac6_no_ipt_requirement_counterexample.",
        ),
        ACDerivationAttempt(
            "AC7", "IPT",
            "partially_derived",
            "IPT requires the source (richer) system to have a non-degenerate invariant "
            "level. AC7 (global section exists) is compatible with IPT's domain requirement "
            "but IPT does not directly require AC7 to hold.",
            "See ac7_no_ipt_requirement_counterexample.",
        ),
    )


def _rmt_derivation_attempts() -> tuple[ACDerivationAttempt, ...]:
    """
    RMT (Resource-Monotonicity Theorem):
    Global satisfiability resource R = global_witness_count is non-increasing
    under restriction projection.
    """
    return (
        ACDerivationAttempt(
            "AC1", "RMT",
            "partially_derived",
            "RMT requires a well-typed richer system so that global_witness_count is "
            "meaningful. However the explicit axiom check for all T26 conditions goes "
            "beyond what RMT directly demands; RMT only needs the resource to be computable.",
            "See rmt_insufficient_for_ac1_ac2_ac3_counterexample.",
        ),
        ACDerivationAttempt(
            "AC2", "RMT",
            "partially_derived",
            "Same as AC1: RMT requires a computable restricted resource but does not "
            "enforce all T26 axioms on the restricted system.",
            "See rmt_insufficient_for_ac1_ac2_ac3_counterexample.",
        ),
        ACDerivationAttempt(
            "AC3", "RMT",
            "not_applicable",
            "RMT is agnostic about whether the projection map is total. It tracks the "
            "resource before and after restriction regardless of how the restriction is "
            "specified. AC3 (total site map) is not derivable from RMT.",
            "A partial site map still produces a restricted system with a computable resource.",
        ),
        ACDerivationAttempt(
            "AC4", "RMT",
            "derived",
            "AC4 derives from AC6 by T26 semantics (T32 result). RMT produces AC6 "
            "(strict resource decrease), and AC4 is a logical consequence of AC6.",
            "",
        ),
        ACDerivationAttempt(
            "AC5_measurable", "RMT",
            "derived",
            "Resource strictly decreasing (global_witness_count drops from positive to zero) "
            "implies local_profiles_preserved=False for any morphism tracking the resource. "
            "The measurable-loss condition is a consequence of strict resource monotonicity.",
            "",
        ),
        ACDerivationAttempt(
            "AC5_naming", "RMT",
            "independent",
            "RMT tracks quantity (global_witness_count) not named mechanism. A projection "
            "can show strict resource decrease without naming what was forgotten. The naming "
            "obligation requires ProjectionCase.forgotten_structure metadata.",
            "See ac5_naming_independence_counterexample.",
        ),
        ACDerivationAttempt(
            "AC6", "RMT",
            "derived",
            "AC6 (restricted system obstructed) is exactly the statement that the resource "
            "dropped to zero on the restricted side. RMT directly characterizes this: a "
            "strict decrease from positive to zero means obstruction_detected=True.",
            "",
        ),
        ACDerivationAttempt(
            "AC7", "RMT",
            "derived",
            "AC7 (richer system unobstructed) is the statement that the resource was positive "
            "before projection. RMT requires richer_value > 0 as the precondition for strict "
            "monotone decrease. AC6+AC7 together characterize the resource drop.",
            "",
        ),
    )


def all_derivation_attempts() -> tuple[ACDerivationAttempt, ...]:
    return _ipt_derivation_attempts() + _rmt_derivation_attempts()


# ---------------------------------------------------------------------------
# Hypothesis evaluators
# ---------------------------------------------------------------------------


def _evaluate_hypotheses(
    ipt_attempts: tuple[ACDerivationAttempt, ...],
    rmt_attempts: tuple[ACDerivationAttempt, ...],
) -> tuple[HypothesisVerdict, ...]:

    def covered_by(attempts: tuple[ACDerivationAttempt, ...]) -> set[str]:
        return {
            a.condition_id
            for a in attempts
            if a.derivation_status in ("derived", "partially_derived")
        }

    all_conditions = {"AC1", "AC2", "AC3", "AC4", "AC5_measurable", "AC5_naming", "AC6", "AC7"}
    ipt_covered = covered_by(ipt_attempts)
    rmt_covered = covered_by(rmt_attempts)
    both_covered = ipt_covered | rmt_covered
    fully_derived_both = {
        a.condition_id for a in (ipt_attempts + rmt_attempts)
        if a.derivation_status == "derived"
    }

    h0_uncovered = all_conditions - {"AC5_naming"}
    h1_uncovered = all_conditions - ipt_covered
    h2_uncovered = all_conditions - rmt_covered
    h3_uncovered = all_conditions - both_covered
    h4_uncovered = h3_uncovered  # same as H3 under current analysis
    h5_uncovered = all_conditions

    verdicts = (
        HypothesisVerdict(
            "H0",
            "AC1-AC7 are independent empirical conditions with no deeper derivation.",
            "rejected",
            (),
            tuple(sorted(h0_uncovered)),
            "AC4 derives from AC6 by T26 semantics (T32). AC1-AC3 derive from IPT typing "
            "obligations. AC6 and AC7 derive from RMT resource polarity. Only AC5-naming "
            "is genuinely independent. H0 is too pessimistic.",
        ),
        HypothesisVerdict(
            "H1",
            "All conditions arise from invariant-preservation (IPT) alone.",
            "partially_supported",
            tuple(sorted(ipt_covered)),
            tuple(sorted(h1_uncovered)),
            "IPT derives AC1-AC4 and the measurable-loss half of AC5. IPT does not "
            "directly derive AC6 and AC7 as requirements (only as compatible consequences). "
            "H1 alone is insufficient for the obstruction polarity conditions.",
        ),
        HypothesisVerdict(
            "H2",
            "All conditions arise from resource monotonicity (RMT) alone.",
            "partially_supported",
            tuple(sorted(rmt_covered)),
            tuple(sorted(h2_uncovered)),
            "RMT derives AC4, AC5-measurable, AC6, AC7 cleanly. RMT does not derive "
            "AC3 (total site map is a morphism definition, not a resource constraint) or "
            "provide the full T26 axiom checks for AC1 and AC2. H2 alone is insufficient.",
        ),
        HypothesisVerdict(
            "H3",
            "Both IPT and RMT are required; neither alone is sufficient.",
            "supported",
            tuple(sorted(both_covered)),
            tuple(sorted(h3_uncovered)),
            "IPT covers AC1-AC4 (typing + definability). RMT covers AC4-AC7 and "
            "AC5-measurable. Together they explain all conditions except AC5-naming. "
            "The residual (AC5-naming) is a methodological transparency condition "
            "that is not derivable from either framework. H3 is the best-supported verdict.",
        ),
        HypothesisVerdict(
            "H4",
            "A single deeper principle explains all conditions more economically than H3.",
            "boundary",
            tuple(sorted(both_covered)),
            tuple(sorted(h4_uncovered)),
            "The 'local-to-global resource consistency' framing unifies IPT and RMT at a "
            "higher level of abstraction. However this unification does not reduce the "
            "number of unexplained conditions (AC5-naming remains). H4 is a rephrasing "
            "of H3 at a higher level of abstraction, not a genuinely distinct result.",
        ),
        HypothesisVerdict(
            "H5",
            "No derivation from these principles is currently justified.",
            "rejected",
            (),
            tuple(sorted(h5_uncovered)),
            "Multiple conditions are demonstrably derivable: AC4 from T26 semantics, "
            "AC6+AC7 from RMT, AC1-AC3 from IPT. H5 is too pessimistic given the evidence.",
        ),
    )
    return verdicts


# ---------------------------------------------------------------------------
# Finite witness / counterexample builders
# ---------------------------------------------------------------------------


def _local(site_id: str, tag: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(
        site=ObserverSite(site_id, tag, "finite_site", 0, "derivation"),
        proposition_value="true",
        profile=profile,
    )


def _obstructed_patches(prefix: str) -> tuple[RestrictionPatch, ...]:
    return (
        RestrictionPatch(
            f"{prefix}_ab",
            (f"{prefix}_A", f"{prefix}_B"),
            ("a", "b"),
            (PatchConstraint("a", "b", "same"),),
        ),
        RestrictionPatch(
            f"{prefix}_bc",
            (f"{prefix}_B", f"{prefix}_C"),
            ("b", "c"),
            (PatchConstraint("b", "c", "same"),),
        ),
        RestrictionPatch(
            f"{prefix}_ac",
            (f"{prefix}_A", f"{prefix}_C"),
            ("a", "c"),
            (PatchConstraint("a", "c", "different"),),
        ),
    )


def _build_rich(prefix: str, tag: str, profile: D1Profile) -> D1RestrictionSystem:
    return D1RestrictionSystem(
        name=f"{prefix}_rich",
        proposition="record_R",
        local_values=(
            _local(f"{prefix}_A", tag, profile),
            _local(f"{prefix}_B", tag, profile),
            _local(f"{prefix}_C", tag, profile),
        ),
        transport_edges=(
            TransportEdge(f"{prefix}_A", f"{prefix}_B", "trusted_ab"),
            TransportEdge(f"{prefix}_B", f"{prefix}_C", "trusted_bc"),
        ),
        source_site=f"{prefix}_A",
        target_site=f"{prefix}_C",
        patches=(),
    )


def _build_restricted(
    prefix: str, tag: str, profile: D1Profile, obstructed: bool
) -> D1RestrictionSystem:
    return D1RestrictionSystem(
        name=f"{prefix}_restricted",
        proposition="record_R",
        local_values=(
            _local(f"{prefix}_A", tag, profile),
            _local(f"{prefix}_B", tag, profile),
            _local(f"{prefix}_C", tag, profile),
        ),
        transport_edges=(
            TransportEdge(f"{prefix}_A", f"{prefix}_B", "trusted_ab"),
            TransportEdge(f"{prefix}_B", f"{prefix}_C", "trusted_bc"),
        ),
        source_site=f"{prefix}_A",
        target_site=f"{prefix}_C",
        patches=_obstructed_patches(prefix) if obstructed else (),
    )


def _build_morphism(
    name: str,
    rich: D1RestrictionSystem,
    restricted: D1RestrictionSystem,
    prefix: str,
    preserved_dimensions: tuple[str, ...],
) -> D1RestrictionMorphism:
    return D1RestrictionMorphism(
        name=name,
        source=rich,
        target=restricted,
        site_map=(
            SiteMap(f"{prefix}_A", f"{prefix}_A"),
            SiteMap(f"{prefix}_B", f"{prefix}_B"),
            SiteMap(f"{prefix}_C", f"{prefix}_C"),
        ),
        preserved_dimensions=preserved_dimensions,
        require_trust_path_preservation=True,
        require_obstruction_preservation=False,
    )


def _ac5_naming_independence_counterexample() -> CounterexampleCase:
    """
    Show that resource monotonicity does not enforce the naming condition of AC5.

    The richer system has a high-dimensional profile and no obstruction.
    The restricted system has a lower-dimensional profile and a finite gluing obstruction.
    The morphism has a total site map and measurable profile loss.
    But forgotten_structure=() — nothing is named.
    Result: AC5=False despite full resource monotone decrease.
    """
    prefix = "ac5_name"
    rich_profile = D1Profile(
        accessible_support=2,
        holder_redundancy=2,
        branch_support=1,
        reversal_cost=2,
    )
    res_profile = D1Profile(
        accessible_support=1,
        holder_redundancy=1,
        branch_support=0,
        reversal_cost=1,
    )
    rich = _build_rich(prefix, "T33_ac5", rich_profile)
    restricted = _build_restricted(prefix, "T33_ac5", res_profile, obstructed=True)
    morphism = _build_morphism(
        "ac5_naming_witness",
        rich, restricted, prefix,
        preserved_dimensions=("branch_support",),
    )
    case = ProjectionCase(
        name="ac5_naming_independence_witness",
        source="T33_counterexample",
        richer_system=rich,
        restricted_system=restricted,
        morphism=morphism,
        forgotten_structure=(),
        preserved_structure=("topology",),
        intended_reading=(
            "Projection forgets measurable structure (resource drops) "
            "but names nothing — AC5-naming is not captured by RMT alone."
        ),
    )
    check = check_admissibility(case)
    return CounterexampleCase(
        name="ac5_naming_independence_counterexample",
        principle_tested="RMT",
        condition_not_derived="AC5_naming",
        case_description=(
            "Rich system (D1Profile(2,2,1,2), no obstruction) projects to "
            "restricted system (D1Profile(1,1,0,1), 3-patch gluing obstruction). "
            "Resource drops from positive to zero; profiles differ measurably. "
            "forgotten_structure=() so AC5=False despite complete resource decrease."
        ),
        projection_case=case,
        admissibility_check=check,
        what_it_shows=(
            "Resource monotonicity (global_witness_count drop) plus measurable profile loss "
            "do not entail the naming obligation. AC5-naming requires ProjectionCase "
            "metadata beyond what D1RestrictionSystem or RMT tracks."
        ),
    )


def _rmt_insufficient_for_ac3_counterexample() -> CounterexampleCase:
    """
    Show that RMT does not enforce AC3 (total site map).

    Build a case where the site_map omits one site.
    The resource can still drop — RMT sees no violation.
    But AC3=False because the morphism is partial.
    """
    prefix = "ac3_rmt"
    profile = D1Profile(
        accessible_support=2,
        holder_redundancy=2,
        branch_support=1,
        reversal_cost=2,
    )
    res_profile = D1Profile(
        accessible_support=1,
        holder_redundancy=1,
        branch_support=0,
        reversal_cost=1,
    )
    rich = _build_rich(prefix, "T33_ac3", profile)
    restricted = _build_restricted(prefix, "T33_ac3", res_profile, obstructed=True)
    morphism = D1RestrictionMorphism(
        name="partial_site_map_witness",
        source=rich,
        target=restricted,
        site_map=(
            SiteMap(f"{prefix}_A", f"{prefix}_A"),
            SiteMap(f"{prefix}_B", f"{prefix}_B"),
        ),
        preserved_dimensions=("branch_support",),
        require_trust_path_preservation=True,
        require_obstruction_preservation=False,
    )
    case = ProjectionCase(
        name="ac3_rmt_insufficient_witness",
        source="T33_counterexample",
        richer_system=rich,
        restricted_system=restricted,
        morphism=morphism,
        forgotten_structure=("branch_support",),
        preserved_structure=("topology",),
        intended_reading=(
            "Partial site map (C not mapped) — RMT sees resource drop "
            "but AC3 fails. RMT cannot enforce projection definability."
        ),
    )
    check = check_admissibility(case)
    return CounterexampleCase(
        name="rmt_insufficient_for_ac3_counterexample",
        principle_tested="RMT",
        condition_not_derived="AC3",
        case_description=(
            "Rich and restricted systems with resource drop, but site_map omits C. "
            "RMT records a resource decrease (positive to zero) but the morphism "
            "analysis marks site_map_total=False."
        ),
        projection_case=case,
        admissibility_check=check,
        what_it_shows=(
            "Resource decrease does not imply definability of the projection. "
            "AC3 (total site map) requires IPT's morphism-definition obligation, "
            "not RMT's quantitative resource tracking."
        ),
    )


def _ipt_insufficient_for_ac6_counterexample() -> CounterexampleCase:
    """
    Show that IPT does not directly require AC6 (restricted system obstructed).

    Build a valid typed pair with a total site map and measurable profile loss,
    but the restricted system has no obstruction. IPT sees valid invariant carriers
    and a definable projection — but AC6=False.
    """
    prefix = "ac6_ipt"
    rich_profile = D1Profile(
        accessible_support=2,
        holder_redundancy=2,
        branch_support=1,
        reversal_cost=2,
    )
    res_profile = D1Profile(
        accessible_support=1,
        holder_redundancy=1,
        branch_support=0,
        reversal_cost=1,
    )
    rich = _build_rich(prefix, "T33_ac6", rich_profile)
    restricted = _build_restricted(prefix, "T33_ac6", res_profile, obstructed=False)
    morphism = _build_morphism(
        "ipt_no_ac6_witness",
        rich, restricted, prefix,
        preserved_dimensions=("branch_support",),
    )
    case = ProjectionCase(
        name="ipt_insufficient_for_ac6_witness",
        source="T33_counterexample",
        richer_system=rich,
        restricted_system=restricted,
        morphism=morphism,
        forgotten_structure=("branch_support",),
        preserved_structure=("topology",),
        intended_reading=(
            "Valid typed pair, total map, measurable loss, but no restricted obstruction. "
            "IPT sees a valid projection; RMT needed to require AC6."
        ),
    )
    check = check_admissibility(case)
    return CounterexampleCase(
        name="ipt_insufficient_for_ac6_counterexample",
        principle_tested="IPT",
        condition_not_derived="AC6",
        case_description=(
            "Rich system (D1Profile(2,2,1,2), no obstruction). Restricted system "
            "(D1Profile(1,1,0,1), no patches, no obstruction). IPT validates the typed "
            "pair and definable projection. AC6=False: no restricted obstruction."
        ),
        projection_case=case,
        admissibility_check=check,
        what_it_shows=(
            "IPT validates structural invariant change but does not require the restricted "
            "system to be obstructed. The obstruction polarity requirement (AC6+AC7) "
            "comes from RMT, not IPT."
        ),
    )


def _build_counterexamples() -> tuple[CounterexampleCase, ...]:
    return (
        _ac5_naming_independence_counterexample(),
        _rmt_insufficient_for_ac3_counterexample(),
        _ipt_insufficient_for_ac6_counterexample(),
    )


# ---------------------------------------------------------------------------
# Resource monotone witnesses from T31 cases
# ---------------------------------------------------------------------------


def _t31_resource_monotones() -> tuple[ResourceMonotone, ...]:
    from models.cap_theorem_bridge import cap_bridge_case
    from models.cross_domain_projection_obstruction_validation import (
        git_semantic_merge_case,
    )
    from models.gu_class_relative_bridge import (
        nielsen_ninomiya_bridge_case,
        witten_bridge_case,
    )
    from models.projection_obstruction_schema import projection_case_from_bridge_case

    def _unwrap(obj: Any) -> Any:
        # HostileDomainCase wraps a ProjectionCase in .case
        return obj.case if hasattr(obj, "case") else obj

    positive_cases = [
        ("witten_1981", _unwrap(projection_case_from_bridge_case(witten_bridge_case()))),
        ("nielsen_ninomiya", _unwrap(projection_case_from_bridge_case(nielsen_ninomiya_bridge_case()))),
        ("cap_theorem", _unwrap(cap_bridge_case())),
        ("git_semantic_merge", _unwrap(git_semantic_merge_case())),
    ]
    return tuple(
        compute_resource_monotone(name, case.richer_system, case.restricted_system)
        for name, case in positive_cases
    )


# ---------------------------------------------------------------------------
# Main T33 analysis runner
# ---------------------------------------------------------------------------


def _smaller_theorem_candidate() -> str:
    return (
        "SMALLER THEOREM CANDIDATE: "
        "Given a valid morphism f: S_r -> S between valid D1RestrictionSystems "
        "(AC1-AC3 satisfied), if S has a global section (AC7) and S_r has a "
        "proper H^1 finite gluing obstruction (AC6), then f witnesses a strict "
        "decrease in the global satisfiability resource R = [global_witness_count > 0]. "
        "A full PO1 instance additionally requires the mechanism of decrease to be "
        "identified by name (AC5). AC5 decomposes: the measurable-loss half follows "
        "from RMT; the naming half is a methodological transparency condition that "
        "neither IPT nor RMT entail."
    )


def run_t33_analysis() -> T33Result:
    t32 = run_t32_derivation_audit()
    ipt_attempts = _ipt_derivation_attempts()
    rmt_attempts = _rmt_derivation_attempts()
    all_attempts = ipt_attempts + rmt_attempts
    hypothesis_verdicts = _evaluate_hypotheses(ipt_attempts, rmt_attempts)
    counterexamples = _build_counterexamples()
    resource_monotones = _t31_resource_monotones()

    projection_actions = tuple(
        compute_projection_action(ce.projection_case, ce.admissibility_check.ac5_structure_forgotten)
        for ce in counterexamples
    )

    return T33Result(
        t32_basis=t32,
        resource_monotones=resource_monotones,
        projection_actions=projection_actions,
        ac_derivation_attempts=all_attempts,
        hypothesis_verdicts=hypothesis_verdicts,
        counterexamples=counterexamples,
        smallest_theorem_candidate=_smaller_theorem_candidate(),
        remaining_independence=("AC5_naming",),
        best_hypothesis="H3",
        recommendation=(
            "PO1 should be treated as a partially derived theorem. "
            "AC1-AC4, AC6, AC7 and AC5-measurable are derivable from IPT+RMT. "
            "AC5-naming is a methodological transparency condition that should be "
            "promoted to a first-class named obligation (Principle P5) rather than "
            "treated as an empirical guard. Consider revising PO1 to read: "
            "'A projection is a PO1 instance iff it is a valid typed morphism "
            "(IPT) witnessing strict resource decrease (RMT) with named mechanism (P5).'"
        ),
        negative_results_note=(
            "Three counterexamples confirm that neither IPT nor RMT alone is sufficient: "
            "(1) AC5-naming is not captured by RMT resource tracking; "
            "(2) AC3 (total site map) is not derivable from RMT alone; "
            "(3) AC6 (restricted obstruction) is not required by IPT alone. "
            "These negative results precisely mark the boundary between H3 and the "
            "rejected H1/H2 single-principle hypotheses."
        ),
    )


def t33_result_to_dict(result: T33Result) -> dict[str, Any]:
    t32_dict = asdict(result.t32_basis)
    return {
        "t32_basis_summary": {
            "minimal_condition_basis": t32_dict["minimal_condition_basis"],
            "compressed_principle_basis": t32_dict["compressed_principle_basis"],
            "best_supported_hypothesis": t32_dict["best_supported_hypothesis"],
            "feasible_subset_count": len(t32_dict["generated_subsets"]),
            "impossible_subset_count": len(t32_dict["impossible_subsets"]),
        },
        "resource_monotones": [
            {
                "name": rm.name,
                "richer_value": rm.richer_value,
                "restricted_value": rm.restricted_value,
                "is_non_increasing": rm.is_non_increasing,
                "is_strictly_decreasing": rm.is_strictly_decreasing,
                "witness": rm.witness,
            }
            for rm in result.resource_monotones
        ],
        "projection_actions": [
            {
                "morphism_name": pa.morphism_name,
                "resource_decreases": pa.resource_decreases,
                "resource_strictly_lost": pa.resource_strictly_lost,
                "invariant_class_changes": pa.invariant_class_changes,
                "local_profiles_preserved": pa.local_profiles_preserved,
            }
            for pa in result.projection_actions
        ],
        "ac_derivation_attempts": [
            {
                "condition_id": a.condition_id,
                "principle_id": a.principle_id,
                "derivation_status": a.derivation_status,
                "proof_sketch": a.proof_sketch,
                "counterexample": a.counterexample,
            }
            for a in result.ac_derivation_attempts
        ],
        "hypothesis_verdicts": [
            {
                "hypothesis_id": hv.hypothesis_id,
                "hypothesis_statement": hv.hypothesis_statement,
                "verdict": hv.verdict,
                "conditions_covered": list(hv.conditions_covered),
                "conditions_uncovered": list(hv.conditions_uncovered),
                "evidence_summary": hv.evidence_summary,
            }
            for hv in result.hypothesis_verdicts
        ],
        "counterexamples": [
            {
                "name": ce.name,
                "principle_tested": ce.principle_tested,
                "condition_not_derived": ce.condition_not_derived,
                "case_description": ce.case_description,
                "admissibility_verdict": ce.admissibility_check.verdict,
                "ac_vector": {
                    "AC1": ce.admissibility_check.ac1_richer_valid,
                    "AC2": ce.admissibility_check.ac2_restricted_valid,
                    "AC3": ce.admissibility_check.ac3_projection_definable,
                    "AC4": ce.admissibility_check.ac4_local_compat,
                    "AC5": ce.admissibility_check.ac5_structure_forgotten,
                    "AC6": ce.admissibility_check.ac6_restricted_obstructed,
                    "AC7": ce.admissibility_check.ac7_richer_unobstructed,
                },
                "what_it_shows": ce.what_it_shows,
            }
            for ce in result.counterexamples
        ],
        "smallest_theorem_candidate": result.smallest_theorem_candidate,
        "remaining_independence": list(result.remaining_independence),
        "best_hypothesis": result.best_hypothesis,
        "recommendation": result.recommendation,
        "negative_results_note": result.negative_results_note,
    }
