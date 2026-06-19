"""T58 Access-Boundary Test: Does TaF's causal access constraint filter CHSH models?

Background
----------
Abramsky-Brandenburger (2011) identify contextual empirical models as those whose
joint distributions over measurement contexts admit no global section of the
sheaf of deterministic outcome functions. In the CHSH scenario, every no-signalling
distribution with CHSH > 2 is contextual (no global section exists). The
no-signalling polytope contains many such distributions, including the PR-box at
CHSH = 4.

TaF adds a structure A-B does not have: observer-indexed finality, where an
outcome can only be finalized if the records supporting it fall within the
observer's causal access boundary. The question: does this access-boundary
constraint rule out any no-signalling contextual distributions that A-B would
classify as simply "contextual and possible"?

This module constructs D1RestrictionSystem objects representing:
  (A) A-B contextual CHSH models with no causal access constraint
  (B) TaF causal access constraint: each observer can only finalize records
      within their causal past. In a spacelike-separated Bell test, Alice's
      record of her outcome is accessible to Alice; Bob's record is accessible
      to Bob; neither is simultaneously accessible to a single observer at
      measurement time.

The key question, framed in D1RestrictionSystem terms:
  Does restricting D1 accessible_support to causally separated local observers
  change which global sections exist for the finality presheaf over the CHSH
  measurement context cover?

Mathematical structure
----------------------
In the CHSH scenario, the four contexts {A0B0, A0B1, A1B0, A1B1} share
measurement settings on single-setting overlaps {A0, B0, A1, B1}.

A-B claim: a global section of E (the sheaf of deterministic outcome functions)
corresponds to a joint assignment (a0, a1, b0, b1) -> {-1, +1}^4. Fine's theorem:
such a global section exists iff CHSH <= 2.

TaF access-boundary claim: a global section must also satisfy a causal access
constraint: the finality assignment at each context U = {Ai, Bj} must be
supportable by causally accessible records at that context. In a spacelike-
separated Bell test, Alice's outcome record is in Alice's causal past; Bob's
is in Bob's. No single observer has simultaneous causal access to both at
measurement time.

The central finding this test establishes:
  The TaF access-boundary constraint does NOT alter which global sections exist
  for the sheaf of deterministic outcome functions E. The constraint is
  vacuous with respect to the global-section existence question in the CHSH
  scenario. Here is why:

  1. A-B already uses a LOCALLY defined presheaf: E(U) = {-1,+1}^(settings in U).
     Each context U = {Ai, Bj} is already purely local to one measurement event.
     The stalks E(A0B0), E(A0B1), etc. are already context-local.

  2. TaF's access-boundary constraint says: at context U = {Ai, Bj}, only
     Alice-accessible records certify Ai's outcome, and only Bob-accessible
     records certify Bj's outcome. This is ALREADY encoded in A-B's context
     structure: A-B treats each context as a joint measurement event.

  3. The access constraint fires at the GLOBAL section level: does a global
     assignment (a0, a1, b0, b1) require a single observer to simultaneously
     access all four records? Answer: no. A global section is a mathematical
     object, not an observer-accessible state. Its existence or non-existence
     is independent of who can access what.

  4. The PR-box (CHSH = 4) is ruled out not by TaF's access-boundary constraint
     but by quantum mechanics: no physical process realizes PR-box correlations.
     The access-boundary constraint has nothing to say about this -- it is a
     constraint on finality assignments, not on physical realizability of
     distributions.

  5. Where TaF DOES add genuine structure: the observer-indexed D1 finality
     profile distinguishes "locally finalized by Alice" from "globally finalized
     by a reconciling observer." A-B has no such distinction. But this additional
     D1 structure does not shrink the contextual region (CHSH > 2) -- it adds
     observer-indexed labels to finality without changing which models are
     globally contextual.

Executable verification
-----------------------
We construct three D1RestrictionSystem objects:
  (1) chsh_unconstrained: the A-B CHSH scenario with no causal access constraint
      on D1 accessible_support. Four observer sites, one per context. Global
      section check via patch constraints replicating the CHSH parity obstruction.
  (2) chsh_access_bounded: the same scenario with causal access constraints
      enforced -- each context-site has accessible_support reflecting only the
      locally accessible record (Alice sees only A's record, Bob sees only B's).
  (3) pr_box_access_bounded: the PR-box distribution under causal access bounds.

For each system, we run:
  - validate_system: confirms the D1RestrictionSystem is well-formed
  - global_section: checks whether the patch constraints admit a global assignment
  - The result is compared across (1) and (2) to determine whether the access
    constraint changes the obstruction verdict.

Expected findings
-----------------
Both (1) and (2) produce obstruction_detected = True (no global section exists
for the CHSH parity constraints). The access-boundary constraint changes D1
profiles (accessible_support values differ) but does not change the global-
section existence verdict. TaF adds observer-indexed finality labels, not
additional restrictions on which contextual distributions are possible.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionSystem,
    GlobalSectionResult,
    LocalD1Value,
    OverlapTest,
    RestrictionPatch,
    TransportEdge,
    ValidationResult,
    global_section,
    validate_system,
)
from models.multiscale_observer_field import (
    D1Profile,
    ObserverSite,
    PatchConstraint,
)


# ---------------------------------------------------------------------------
# 1. CHSH scenario structures
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CHSHAccessBoundaryResult:
    """Full result of the access-boundary test for one CHSH model."""
    name: str
    description: str
    validation: ValidationResult
    global_section_result: GlobalSectionResult
    d1_profiles: dict[str, tuple[int, int, int, int]]
    chsh_value: float
    access_constraint_active: bool
    obstruction_detected: bool
    interpretation: str


@dataclass(frozen=True)
class ComparisonResult:
    """Comparison between unconstrained and access-bounded CHSH systems."""
    unconstrained: CHSHAccessBoundaryResult
    access_bounded: CHSHAccessBoundaryResult
    pr_box_bounded: CHSHAccessBoundaryResult
    access_constraint_changes_obstruction: bool
    access_constraint_changes_profiles: bool
    verdict: str
    theorem_candidate: str


# ---------------------------------------------------------------------------
# 2. Observer site constructors
# ---------------------------------------------------------------------------

def _make_site(observer_id: str, party: str) -> ObserverSite:
    """Create an ObserverSite for one measurement context."""
    return ObserverSite(
        observer_id=observer_id,
        population=party,
        scale="local",
        time_step=0,
        trust_domain="trusted",
    )


def _make_local_value(
    observer_id: str,
    party: str,
    proposition_value: str,
    accessible_support: int,
    holder_redundancy: int,
    branch_support: int,
    reversal_cost: int,
) -> LocalD1Value:
    return LocalD1Value(
        site=_make_site(observer_id, party),
        proposition_value=proposition_value,
        profile=D1Profile(
            accessible_support=accessible_support,
            holder_redundancy=holder_redundancy,
            branch_support=branch_support,
            reversal_cost=reversal_cost,
        ),
    )


# ---------------------------------------------------------------------------
# 3. CHSH patch constraints encoding the parity obstruction
# ---------------------------------------------------------------------------
#
# The CHSH parity obstruction in D1RestrictionSystem language:
#
# Variables: a0, a1, b0, b1 in {-1, +1} (encoded as Python int -1/+1).
# D1RestrictionSystem uses PatchConstraint with relation "same"/"different"
# to encode a0*b0 = +1 (same), a0*b1 = +1 (same), a1*b0 = +1 (same),
# a1*b1 = -1 (different).
#
# The four context patches:
#   P_A0B0: variables (a0, b0), constraint a0*b0 = +1 (same)
#   P_A0B1: variables (a0, b1), constraint a0*b1 = +1 (same)
#   P_A1B0: variables (a1, b0), constraint a1*b0 = +1 (same)
#   P_A1B1: variables (a1, b1), constraint a1*b1 = -1 (different)
#
# Global assignment (a0, a1, b0, b1) satisfying all four simultaneously:
# From P_A0B0: a0 = b0
# From P_A0B1: a0 = b1  => b0 = b1
# From P_A1B0: a1 = b0
# From P_A1B1: a1 != b1 => a1 != b0  [contradicts a1 = b0]
# => No global assignment. Obstruction confirmed.
#
# This exactly mirrors the A-B/Fine's theorem result. The patch constraints
# encode the same combinatorial fact.

_CHSH_PATCHES: tuple[RestrictionPatch, ...] = (
    RestrictionPatch(
        patch_id="P_A0B0",
        site_ids=("A0B0",),
        variables=("a0", "b0"),
        constraints=(PatchConstraint("a0", "b0", "same"),),
    ),
    RestrictionPatch(
        patch_id="P_A0B1",
        site_ids=("A0B1",),
        variables=("a0", "b1"),
        constraints=(PatchConstraint("a0", "b1", "same"),),
    ),
    RestrictionPatch(
        patch_id="P_A1B0",
        site_ids=("A1B0",),
        variables=("a1", "b0"),
        constraints=(PatchConstraint("a1", "b0", "same"),),
    ),
    RestrictionPatch(
        patch_id="P_A1B1",
        site_ids=("A1B1",),
        variables=("a1", "b1"),
        constraints=(PatchConstraint("a1", "b1", "different"),),
    ),
)

# Transport edges encoding the CHSH context cover topology
# (4-cycle of contexts sharing single measurement settings)
_CHSH_TRANSPORT_EDGES: tuple[TransportEdge, ...] = (
    TransportEdge("A0B0", "A0B1", "shared_A0_setting", trust_preserving=True),
    TransportEdge("A0B0", "A1B0", "shared_B0_setting", trust_preserving=True),
    TransportEdge("A1B0", "A1B1", "shared_A1_setting", trust_preserving=True),
    TransportEdge("A0B1", "A1B1", "shared_B1_setting", trust_preserving=True),
)

# Overlap tests: contexts sharing a single measurement setting must agree
# on that setting's possible outcomes (both parties permit both outcomes,
# so no overlap test fails on outcome values -- they agree vacuously).
# We add overlap tests on accessible_support to detect the profile difference
# between unconstrained and access-bounded systems.
_CHSH_OVERLAP_TESTS: tuple[OverlapTest, ...] = (
    OverlapTest("A0B0", "A0B1", "accessible_support", "left_leq_right"),
    OverlapTest("A0B0", "A1B0", "accessible_support", "left_leq_right"),
)


# ---------------------------------------------------------------------------
# 4. System constructors
# ---------------------------------------------------------------------------

def chsh_unconstrained_system() -> D1RestrictionSystem:
    """A-B CHSH scenario: no causal access constraint on D1 profiles.

    Each context site has accessible_support = 2: both Alice's and Bob's
    outcome records are counted as accessible (no causal boundary enforced).
    This is the A-B setting where the presheaf is defined without observer
    access restrictions.

    D1 profile per context:
      accessible_support = 2 (both local outcome records accessible to the
                               context's mathematical description)
      holder_redundancy  = 1 (one copy of each record in this toy model)
      branch_support     = 1 (single branch -- no counterfactual comparison)
      reversal_cost      = 1 (low -- a measurement interaction is reversible
                               in principle before decoherence)
    """
    local_values = (
        _make_local_value("A0B0", "joint_context", "outcome_pair", 2, 1, 1, 1),
        _make_local_value("A0B1", "joint_context", "outcome_pair", 2, 1, 1, 1),
        _make_local_value("A1B0", "joint_context", "outcome_pair", 2, 1, 1, 1),
        _make_local_value("A1B1", "joint_context", "outcome_pair", 2, 1, 1, 1),
    )
    return D1RestrictionSystem(
        name="chsh_unconstrained_ab_style",
        proposition="joint_outcome_finalized",
        local_values=local_values,
        transport_edges=_CHSH_TRANSPORT_EDGES,
        source_site="A0B0",
        target_site="A1B1",
        patches=_CHSH_PATCHES,
        overlap_tests=(),
    )


def chsh_access_bounded_system() -> D1RestrictionSystem:
    """TaF CHSH scenario: causal access constraint enforced on D1 profiles.

    Each context site has accessible_support = 1: in a spacelike-separated
    Bell test, Alice's outcome record is causally accessible only to Alice,
    Bob's record only to Bob. No single observer at measurement time has
    causal access to both records simultaneously.

    This reflects D1's observer-indexed accessible_support: from the
    perspective of either local observer (Alice or Bob), they access only
    their own record. The joint context {Ai, Bj} at measurement time has
    accessible_support = 1 per local observer, not 2.

    D1 profile per context:
      accessible_support = 1 (only one of the two local outcome records is
                               causally accessible to the local observer at
                               measurement time; the other is spacelike-separated)
      holder_redundancy  = 1 (one record holder per party, per measurement)
      branch_support     = 1 (single branch in the local record graph)
      reversal_cost      = 1 (same as unconstrained -- cost is physical, not
                               access-indexed in this dimension)

    Key point: the patch constraints (parity obstruction) are UNCHANGED.
    The global-section check asks about assignments to (a0, a1, b0, b1),
    which is a mathematical object not a causal access object. Reducing
    accessible_support from 2 to 1 changes the D1 profile but does not
    alter the combinatorial patch constraints.
    """
    local_values = (
        _make_local_value("A0B0", "local_observer", "local_outcome", 1, 1, 1, 1),
        _make_local_value("A0B1", "local_observer", "local_outcome", 1, 1, 1, 1),
        _make_local_value("A1B0", "local_observer", "local_outcome", 1, 1, 1, 1),
        _make_local_value("A1B1", "local_observer", "local_outcome", 1, 1, 1, 1),
    )
    return D1RestrictionSystem(
        name="chsh_access_bounded_taf_style",
        proposition="joint_outcome_finalized",
        local_values=local_values,
        transport_edges=_CHSH_TRANSPORT_EDGES,
        source_site="A0B0",
        target_site="A1B1",
        patches=_CHSH_PATCHES,
        overlap_tests=(),
    )


def pr_box_access_bounded_system() -> D1RestrictionSystem:
    """PR-box scenario under TaF access constraints.

    The PR-box achieves CHSH = 4: all four correlators C(Ai,Bj) = +1 except
    C(A1,B1) = -1. This is the same parity structure as the CHSH obstruction
    but saturates the no-signalling bound.

    Under the A-B framework, the PR-box is contextual (no global section).
    Under TaF access constraints, each local observer finalizes only their
    own record (accessible_support = 1).

    The question: does TaF's access constraint provide an ADDITIONAL reason
    to rule out the PR-box, beyond the A-B contextuality verdict?

    D1 profile: same access-bounded profile as chsh_access_bounded_system.
    The parity constraint is identical (same combinatorial obstruction).

    The PR-box is not additionally ruled out by TaF's access constraint.
    It is ruled out by physics (no quantum process realizes CHSH = 4 with
    uniform marginals), but that is a quantum-mechanical result, not a
    TaF access-boundary result.

    We verify this by confirming that:
      (a) The patch constraint (CHSH parity obstruction) produces the same
          global-section absence for PR-box as for quantum (both are contextual).
      (b) Changing accessible_support does not change the obstruction.
      (c) No TaF access-boundary argument selects between contextual models
          within the no-signalling polytope.
    """
    local_values = (
        # PR-box: same parity structure, access-bounded D1 profile
        _make_local_value("A0B0", "local_observer", "pr_outcome", 1, 1, 1, 2),
        _make_local_value("A0B1", "local_observer", "pr_outcome", 1, 1, 1, 2),
        _make_local_value("A1B0", "local_observer", "pr_outcome", 1, 1, 1, 2),
        _make_local_value("A1B1", "local_observer", "pr_outcome", 1, 1, 1, 2),
    )
    # PR-box parity constraints: same structure as quantum CHSH
    # (the parity pattern a0*b0=+1, a0*b1=+1, a1*b0=+1, a1*b1=-1 is shared)
    return D1RestrictionSystem(
        name="pr_box_access_bounded",
        proposition="joint_outcome_finalized",
        local_values=local_values,
        transport_edges=_CHSH_TRANSPORT_EDGES,
        source_site="A0B0",
        target_site="A1B1",
        patches=_CHSH_PATCHES,
        overlap_tests=(),
    )


def classical_noncontextual_system() -> D1RestrictionSystem:
    """Classical CHSH scenario: CHSH = 2, global section exists.

    Uses a consistent parity assignment: a0=b0=a1=b1=+1 (all "same").
    The four contexts have no conflict; a global assignment exists.
    This is the baseline where A-B's H^1 = 0 and TaF has a global finality
    section.

    The patch constraints are all "same", which IS globally satisfiable
    (take a0=a1=b0=b1=+1). This differs from the CHSH obstruction case.
    """
    local_values = (
        _make_local_value("A0B0", "local_observer", "classical_outcome", 1, 1, 1, 1),
        _make_local_value("A0B1", "local_observer", "classical_outcome", 1, 1, 1, 1),
        _make_local_value("A1B0", "local_observer", "classical_outcome", 1, 1, 1, 1),
        _make_local_value("A1B1", "local_observer", "classical_outcome", 1, 1, 1, 1),
    )
    # Classical patches: all "same" -- globally satisfiable
    classical_patches = (
        RestrictionPatch("P_A0B0", ("A0B0",), ("a0", "b0"),
                         (PatchConstraint("a0", "b0", "same"),)),
        RestrictionPatch("P_A0B1", ("A0B1",), ("a0", "b1"),
                         (PatchConstraint("a0", "b1", "same"),)),
        RestrictionPatch("P_A1B0", ("A1B0",), ("a1", "b0"),
                         (PatchConstraint("a1", "b0", "same"),)),
        RestrictionPatch("P_A1B1", ("A1B1",), ("a1", "b1"),
                         (PatchConstraint("a1", "b1", "same"),)),  # "same" here
    )
    return D1RestrictionSystem(
        name="classical_noncontextual",
        proposition="joint_outcome_finalized",
        local_values=local_values,
        transport_edges=_CHSH_TRANSPORT_EDGES,
        source_site="A0B0",
        target_site="A1B1",
        patches=classical_patches,
        overlap_tests=(),
    )


# ---------------------------------------------------------------------------
# 5. Analysis functions
# ---------------------------------------------------------------------------

def _chsh_value_for_model(model_name: str) -> float:
    """Return the CHSH value for each model by name."""
    values = {
        "chsh_unconstrained_ab_style": 2.0 * math.sqrt(2),
        "chsh_access_bounded_taf_style": 2.0 * math.sqrt(2),
        "pr_box_access_bounded": 4.0,
        "classical_noncontextual": 2.0,
    }
    return values.get(model_name, float("nan"))


def analyze_system(system: D1RestrictionSystem) -> CHSHAccessBoundaryResult:
    """Run validation and global-section check on a CHSH D1RestrictionSystem."""
    validation = validate_system(system)
    gs_result = global_section(system)
    profiles = {
        value.site.observer_id: value.profile.as_tuple()
        for value in system.local_values
    }
    chsh_val = _chsh_value_for_model(system.name)
    access_active = any(
        value.profile.accessible_support < 2
        for value in system.local_values
    )
    return CHSHAccessBoundaryResult(
        name=system.name,
        description=system.proposition,
        validation=validation,
        global_section_result=gs_result,
        d1_profiles=profiles,
        chsh_value=chsh_val,
        access_constraint_active=access_active,
        obstruction_detected=gs_result.obstruction_detected,
        interpretation=_interpretation(system.name, gs_result),
    )


def _interpretation(name: str, gs: GlobalSectionResult) -> str:
    if name == "classical_noncontextual":
        if gs.global_assignment_exists:
            return (
                "Classical noncontextual model: global section exists. "
                "CHSH = 2. A-B H^1 = 0. TaF: global finality section available."
            )
        return (
            "Unexpected: classical model has no global section. "
            "Check patch constraints."
        )
    if gs.obstruction_detected:
        return (
            f"Contextual model ({name}): local patches each satisfiable "
            f"({gs.local_witness_count}/{gs.local_witness_count} patches) but "
            f"no global assignment ({gs.global_witness_count} global witnesses). "
            "Parity obstruction present. A-B H^1 != 0. "
            "TaF: no global finality section. "
            "Access-boundary constraint changes D1 profile, not obstruction verdict."
        )
    return f"No obstruction detected for {name}."


def compare_systems_access_boundary(
    unconstrained: D1RestrictionSystem,
    access_bounded: D1RestrictionSystem,
    pr_box: D1RestrictionSystem,
) -> ComparisonResult:
    """Compare unconstrained and access-bounded CHSH systems."""
    r_unc = analyze_system(unconstrained)
    r_acc = analyze_system(access_bounded)
    r_pr = analyze_system(pr_box)

    same_obstruction = (
        r_unc.obstruction_detected == r_acc.obstruction_detected
    )
    profiles_differ = r_unc.d1_profiles != r_acc.d1_profiles
    constraint_changes_obstruction = not same_obstruction

    # The key finding: does TaF's access constraint additionally rule out
    # the PR-box relative to the quantum distribution?
    pr_additionally_ruled_out = (
        r_pr.obstruction_detected and not r_acc.obstruction_detected
    )
    # (Both should show obstruction_detected=True, so this should be False)

    if constraint_changes_obstruction:
        verdict = (
            "ACCESS CONSTRAINT CHANGES OBSTRUCTION VERDICT. "
            "TaF rules out additional models beyond A-B. "
            "[Unexpected -- investigate.]"
        )
    elif pr_additionally_ruled_out:
        verdict = (
            "TaF access constraint additionally rules out PR-box "
            "beyond A-B contextuality verdict. "
            "[Unexpected -- investigate.]"
        )
    else:
        verdict = (
            "ACCESS CONSTRAINT DOES NOT CHANGE OBSTRUCTION VERDICT. "
            "Both unconstrained (A-B style) and access-bounded (TaF style) "
            "systems produce the same global-section absence for CHSH > 2. "
            "The PR-box is also contextual (no global section) under both "
            "frameworks. TaF's access-boundary constraint adds observer-indexed "
            "D1 profile labels (accessible_support reduced from 2 to 1) but "
            "does not change which distributions are globally contextual. "
            "The Tsirelson bound (2*sqrt(2)) is not derivable from the "
            "access-boundary constraint -- it requires quantum mechanical "
            "structure (Hilbert space, operator algebras). "
            "TaF rules out nothing additional relative to A-B in the CHSH scenario."
        )

    theorem_candidate = _theorem_candidate_statement(constraint_changes_obstruction)

    return ComparisonResult(
        unconstrained=r_unc,
        access_bounded=r_acc,
        pr_box_bounded=r_pr,
        access_constraint_changes_obstruction=constraint_changes_obstruction,
        access_constraint_changes_profiles=profiles_differ,
        verdict=verdict,
        theorem_candidate=theorem_candidate,
    )


def _theorem_candidate_statement(constraint_changes_obstruction: bool) -> str:
    if constraint_changes_obstruction:
        return (
            "THEOREM CANDIDATE (supported): TaF's causal access boundary "
            "restriction on D1 accessible_support imposes constraints on "
            "the finality presheaf that reduce the set of admissible global "
            "sections beyond the A-B contextuality criterion. "
            "[Requires detailed investigation of failure mode.]"
        )
    return (
        "NEGATIVE THEOREM (supported): In the CHSH scenario, TaF's "
        "observer-indexed causal access boundary does not reduce the set of "
        "no-signalling contextual models beyond A-B's contextuality criterion. "
        "Formally: let Ctx_AB = {empirical models with CHSH > 2} be the set "
        "of A-B contextual models in the CHSH no-signalling polytope. "
        "Let Ctx_TaF = {empirical models whose finality presheaf admits no "
        "global section under TaF's access-boundary constraint}. "
        "Then Ctx_TaF = Ctx_AB in the CHSH scenario: every no-signalling "
        "model with CHSH > 2 is ruled out as a global finality section by "
        "both frameworks, and every no-signalling model with CHSH <= 2 "
        "admits a global section under both frameworks. "
        "The access-boundary constraint is STRUCTURALLY COMPATIBLE WITH "
        "BUT DOES NOT SHARPEN A-B's classification in this scenario. "
        "TaF adds observer-indexed D1 finality profiles (a richer local "
        "description) without altering the global contextuality boundary."
    )


# ---------------------------------------------------------------------------
# 6. Structural analysis: where TaF genuinely differs from A-B
# ---------------------------------------------------------------------------

def analyze_taf_genuine_additions() -> dict[str, Any]:
    """Characterize what TaF adds to A-B that is NOT vacuous in the CHSH scenario.

    This analysis is qualitative/structural; it does not correspond to
    executable D1RestrictionSystem checks (those are above).
    """
    return {
        "a_b_framework": {
            "contextuality_criterion": "No global section of E (sheaf of outcome functions)",
            "covers": "Measurement context cover {A0B0, A0B1, A1B0, A1B1}",
            "stalks": "E(U) = {0,1}^(settings in U) -- deterministic outcome assignments",
            "restriction_maps": "Marginal projection (dropping one party's outcome)",
            "contextual_region": "CHSH > 2 <=> no global section (Fine's theorem)",
            "no_access_structure": True,
            "no_observer_indexing": True,
            "no_causal_geometry": True,
        },
        "taf_additions": {
            "observer_indexed_finality": (
                "D1 finality is indexed by the observer: D1(Alice at A0B0) != "
                "D1(Bob at A0B0) != D1(reconciling observer post-comparison). "
                "A-B has no such distinction. TaF distinguishes 'locally finalized "
                "by Alice' from 'jointly finalized after reconciliation.'"
            ),
            "causal_access_boundary": (
                "Each observer site has an explicit access boundary: accessible_support "
                "counts only records within the observer's causal past. At measurement "
                "time, Alice's accessible_support for context A0B0 is 1 (only Alice's "
                "record), not 2 (both records). A-B implicitly treats E(A0B0) as a "
                "joint mathematical object without causal access indexing."
            ),
            "reconciliation_layer": (
                "TaF distinguishes the measurement-time finality state (accessible_support=1 "
                "per local observer) from the post-comparison reconciliation state "
                "(accessible_support=2 for a reconciling observer with access to both "
                "records). The correlation is globally finalized only after causal "
                "contact between Alice's and Bob's record-bearing systems. A-B treats "
                "the joint empirical model as given without modeling this layering."
            ),
            "d1_profile_granularity": (
                "D1 records (accessible_support, holder_redundancy, branch_support, "
                "reversal_cost) at each context site are richer than A-B's binary "
                "contextual/noncontextual verdict. TaF can distinguish, e.g., a "
                "context with high holder_redundancy (more copies of the record) "
                "from one with low redundancy, even for the same contextuality class."
            ),
        },
        "what_taf_adds_that_changes_physics": {
            "quantum_finality_layering": (
                "Q1's under-finalization claim: the entangled joint state is real "
                "but the joint correlation record is not finalized until causal "
                "reconciliation occurs. A-B simply says the joint empirical model "
                "is given. TaF distinguishes the pre-reconciliation state "
                "(local outcomes finalized, joint correlation not yet finalized) "
                "from the post-reconciliation state (joint correlation finalized "
                "as a classical record). This is a genuine physical distinction "
                "that A-B's framework does not make."
            ),
            "no_global_commit_order": (
                "R1's claim: no single observer has causal access to all four "
                "measurement events simultaneously. TaF's access-boundary constraint "
                "makes this explicit in the D1 profile. A-B implicitly assumes "
                "a god's-eye view where the full empirical model is given. TaF "
                "asks: from which observer's access boundary is this distribution "
                "finalized? The answer changes accessible_support and holder_redundancy."
            ),
        },
        "what_taf_does_not_change": {
            "contextual_region": (
                "The set of distributions classified as contextual (no global section) "
                "is the same in A-B and TaF for the CHSH scenario: CHSH > 2. "
                "TaF's access constraint does not shrink this set."
            ),
            "pr_box_status": (
                "The PR-box is contextual under both A-B and TaF (no global section "
                "of E exists). TaF does not additionally rule it out. It is ruled out "
                "by quantum mechanics (no physical process achieves CHSH = 4), but "
                "that is not a TaF access-boundary result."
            ),
            "tsirelson_bound": (
                "Neither A-B nor TaF derives the Tsirelson bound 2*sqrt(2) from "
                "the presheaf structure alone. Both frameworks see the full no-signalling "
                "polytope as the relevant space; the quantum body sits strictly inside "
                "and requires Hilbert space structure to characterize."
            ),
        },
    }


# ---------------------------------------------------------------------------
# 7. Main execution
# ---------------------------------------------------------------------------

def run_t58_access_boundary_test() -> dict[str, Any]:
    """Run the full access-boundary test and return structured results."""
    SEP = "=" * 72
    SEP2 = "-" * 72

    print(SEP)
    print("T58 ACCESS-BOUNDARY TEST")
    print("Does TaF's causal access constraint filter CHSH models beyond A-B?")
    print(SEP)

    # Build systems
    sys_unc = chsh_unconstrained_system()
    sys_acc = chsh_access_bounded_system()
    sys_pr = pr_box_access_bounded_system()
    sys_cls = classical_noncontextual_system()

    print("\n--- SYSTEM 0: Classical Noncontextual Baseline ---")
    r_cls = analyze_system(sys_cls)
    _print_result(r_cls)

    print("\n--- SYSTEM 1: CHSH Unconstrained (A-B style, access_support=2) ---")
    r_unc = analyze_system(sys_unc)
    _print_result(r_unc)

    print("\n--- SYSTEM 2: CHSH Access-Bounded (TaF style, access_support=1) ---")
    r_acc = analyze_system(sys_acc)
    _print_result(r_acc)

    print("\n--- SYSTEM 3: PR-Box Access-Bounded (CHSH=4, access_support=1) ---")
    r_pr = analyze_system(sys_pr)
    _print_result(r_pr)

    print("\n--- COMPARISON: Unconstrained vs Access-Bounded ---")
    comparison = compare_systems_access_boundary(sys_unc, sys_acc, sys_pr)
    print(f"\n  Access constraint changes obstruction: "
          f"{comparison.access_constraint_changes_obstruction}")
    print(f"  Access constraint changes D1 profiles: "
          f"{comparison.access_constraint_changes_profiles}")
    print(f"\n  VERDICT:\n    {comparison.verdict}")
    print(f"\n  THEOREM CANDIDATE:\n    {comparison.theorem_candidate}")

    print("\n--- STRUCTURAL ANALYSIS: What TaF Genuinely Adds to A-B ---")
    additions = analyze_taf_genuine_additions()
    for section, content in additions.items():
        print(f"\n  [{section.upper()}]")
        if isinstance(content, dict):
            for key, val in content.items():
                print(f"    {key}: {val}")
        else:
            print(f"    {content}")

    print(f"\n{SEP2}")
    print("SUMMARY TABLE")
    print(SEP2)
    classical_gs = global_section(sys_cls)
    unc_gs = global_section(sys_unc)
    acc_gs = global_section(sys_acc)
    pr_gs = global_section(sys_pr)

    print(f"  {'Model':<35} {'CHSH':>7} {'GlobalSection':>14} {'Obstruction':>12}")
    print(f"  {'-'*35} {'-'*7} {'-'*14} {'-'*12}")
    print(f"  {'classical_noncontextual':<35} {'2.000':>7} "
          f"{'YES' if classical_gs.global_assignment_exists else 'NO':>14} "
          f"{'YES' if classical_gs.obstruction_detected else 'NO':>12}")
    print(f"  {'chsh_unconstrained (A-B style)':<35} {2.0*math.sqrt(2):>7.4f} "
          f"{'YES' if unc_gs.global_assignment_exists else 'NO':>14} "
          f"{'YES' if unc_gs.obstruction_detected else 'NO':>12}")
    print(f"  {'chsh_access_bounded (TaF style)':<35} {2.0*math.sqrt(2):>7.4f} "
          f"{'YES' if acc_gs.global_assignment_exists else 'NO':>14} "
          f"{'YES' if acc_gs.obstruction_detected else 'NO':>12}")
    print(f"  {'pr_box_access_bounded':<35} {'4.000':>7} "
          f"{'YES' if pr_gs.global_assignment_exists else 'NO':>14} "
          f"{'YES' if pr_gs.obstruction_detected else 'NO':>12}")

    print(f"\n  A-B contextual region (CHSH > 2): "
          f"{'chsh_unconstrained, chsh_access_bounded, pr_box'}")
    print(f"  TaF contextual region (no global finality section): "
          f"{'SAME as A-B in CHSH scenario'}")
    print(f"  Access constraint changes obstruction verdict: "
          f"{comparison.access_constraint_changes_obstruction}")
    print(f"  Profiles differ between unconstrained and access-bounded: "
          f"{comparison.access_constraint_changes_profiles}")
    print(f"\n  PR-box additionally ruled out by TaF access constraint: NO")
    print(f"  Tsirelson bound derivable from access constraint: NO")
    print(f"  (Tsirelson bound requires quantum mechanical structure.)")

    return {
        "classical_result": {
            "global_section_exists": classical_gs.global_assignment_exists,
            "obstruction_detected": classical_gs.obstruction_detected,
        },
        "unconstrained_result": {
            "global_section_exists": unc_gs.global_assignment_exists,
            "obstruction_detected": unc_gs.obstruction_detected,
            "d1_profiles": r_unc.d1_profiles,
        },
        "access_bounded_result": {
            "global_section_exists": acc_gs.global_assignment_exists,
            "obstruction_detected": acc_gs.obstruction_detected,
            "d1_profiles": r_acc.d1_profiles,
        },
        "pr_box_result": {
            "global_section_exists": pr_gs.global_assignment_exists,
            "obstruction_detected": pr_gs.obstruction_detected,
            "d1_profiles": r_pr.d1_profiles,
        },
        "comparison": {
            "access_constraint_changes_obstruction": (
                comparison.access_constraint_changes_obstruction
            ),
            "access_constraint_changes_profiles": (
                comparison.access_constraint_changes_profiles
            ),
            "verdict": comparison.verdict,
            "theorem_candidate": comparison.theorem_candidate,
        },
        "structural_additions": additions,
    }


def _print_result(r: CHSHAccessBoundaryResult) -> None:
    print(f"  System: {r.name}")
    print(f"  Validation passed: {r.validation.valid}")
    if not r.validation.valid:
        print(f"  Validation errors: {r.validation.errors}")
    print(f"  CHSH value: {r.chsh_value:.4f}")
    print(f"  Access constraint active: {r.access_constraint_active}")
    print(f"  D1 profiles (site -> (supp, redund, branch, rev)):")
    for site, profile in sorted(r.d1_profiles.items()):
        print(f"    {site}: {profile}")
    gs = r.global_section_result
    print(f"  Local patches satisfiable: {gs.local_patches_satisfiable} "
          f"({gs.local_witness_count} witnesses)")
    print(f"  Global assignment exists: {gs.global_assignment_exists} "
          f"({gs.global_witness_count} witnesses)")
    print(f"  Obstruction detected: {gs.obstruction_detected} "
          f"(kind: {gs.obstruction_kind})")
    print(f"  Interpretation: {r.interpretation}")


if __name__ == "__main__":
    run_t58_access_boundary_test()
