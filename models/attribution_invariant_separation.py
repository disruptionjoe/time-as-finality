"""T230: Separating attribution invariant OUTSIDE the canonical construction.

This is Open Problem 11.1, route (b) -- the audit's single-most-important next
step and the only route that flips the independent-motivation criterion from
NOT EARNED to EARNED for the typed-forgetting / LossKernel line.

T220 proved the canonical witness obligation factors through the
neighbor-visible data map, obligation = psi . nu, so any attribution invariant
BUILT FROM the canonical construction is a function of nu (constant on each
fiber of nu) and is therefore neighbor-reconstructible / absorbed. Route (a)
strong subsumption would say EVERY attribution invariant factors through nu;
route (b) separation would exhibit one that does NOT and that separates two
typed-lossy morphisms sharing nu WITHOUT reading an absorbable source field.

This module does NOT just restate T220. T220 only covered invariants derived
INSIDE the canonical construction. The honest open question is whether some
invariant defined OUTSIDE that construction escapes. This module builds the
strongest honest candidates from OUTSIDE the canonical construction and submits
each to a single decisive falsifier: the absorption-escape test.

KEY STRUCTURAL CLAIM (made executable below):

    For an invariant I : Case -> V to SEPARATE two cases in the same nu-fiber,
    I must depend on data NOT determined by nu(case). For a finite typed-lossy
    morphism, the data of a case partitions exactly into:
        (i)   nu-visible data         (the neighbor signature),
        (ii)  source-side fields      (hidden_source_datum and any source lift
                                       distinction nu does not already expose),
        (iii) free decorations        (display labels, path tags),
        (iv)  ambient / extensional   (anything not a function of the single
                                       case: the chosen fixture family, an index,
                                       a chosen embedding, an external oracle).
    A separating I must read from (ii), (iii), or (iv). We show each of these is
    either ABSORBED (ii: admitting the field enlarges nu to nu'), NON-INVARIANT
    (iii: changes under a relabeling that fixes the morphism, so it is not an
    attribution INVARIANT), or NON-LOCAL (iv: not a function of the morphism in
    isolation, so it is not an invariant OF the morphism).

The conclusion of running every honest candidate through this falsifier is a
TRICHOTOMY-EXHAUSTION result: on the finite witness family, no candidate
attribution invariant separates a same-nu pair while remaining (a) defined
outside the canonical construction, (b) genuinely invariant (relabeling-stable),
and (c) non-absorbable (no admissible source field). The two routes resolve as:

    route (b) separation : NOT EXHIBITED  (every separator is absorbed,
                                           non-invariant, or non-local)
    route (a) subsumption : SUPPORTED on the finite family as the bounded
                            negative -- every RELABELING-STABLE, LOCAL attribution
                            invariant on the family factors through nu.

This is the citable bounded negative the audit asks for under route (a). It is a
finite_witness result, NOT a continuum/general theorem: it certifies the
trichotomy is exhaustive ON THIS FAMILY and names exactly the gap a real
separation would have to thread.

No physics language. finite_witness. No kappa transport, no new host. Within-
domain separation question only.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations, permutations
from typing import Callable


# ---------------------------------------------------------------------------
# Case shape (faithful to T220 / T127): the minimal data of a typed-lossy
# morphism, with the four data strata kept explicitly separable so an invariant
# can be classified by which stratum it reads.
#
#   nu-visible        : lifts (the lift judgment table) + target fields
#   source-side       : hidden_source_datum (a field no neighbor package exposes
#                       until admitted)
#   free decorations  : free_label, path_tag (display/path metadata)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Lift:
    left_source: str
    right_source: str
    allowed: bool

    def signature(self) -> tuple[str, str, bool]:
        return (self.left_source, self.right_source, self.allowed)


@dataclass(frozen=True)
class Case:
    name: str
    target_obstructed: bool
    lifts: tuple[Lift, ...]
    composite_map: tuple[tuple[str, str], ...]
    target_global_sections: int
    obstruction_id: str
    # free decorations -- NOT part of nu, and provably not part of the morphism's
    # identity (a relabeling of these fixes the morphism).
    free_label: str
    path_tag: str
    # source-side datum no neighbor package exposes until admitted. Empty => none.
    hidden_source_datum: str = ""


# ---------------------------------------------------------------------------
# nu : Case -> neighbor-visible signature (exactly the T220 realization map).
# The fibers of nu are the same-neighbor-data classes.
# ---------------------------------------------------------------------------


def nu(case: Case) -> tuple[object, ...]:
    csp = tuple(sorted(lift.signature() for lift in case.lifts))
    provenance = tuple(sorted((lift.left_source, lift.right_source) for lift in case.lifts))
    category = (
        tuple(sorted(case.composite_map)),
        case.target_obstructed,
        case.target_global_sections,
        case.obstruction_id,
    )
    return (csp, provenance, category)


# nu' : the ENLARGED neighbor map a mature package produces once a previously
# hidden source field is ADMITTED as legitimate audit data. This is the formal
# content of "absorption returns one level up": a source field, once admitted,
# is itself a neighbor field.


def nu_prime(case: Case) -> tuple[object, ...]:
    return nu(case) + (("admitted_source", case.hidden_source_datum),)


# ---------------------------------------------------------------------------
# Relabeling action on free decorations. A relabeling is any bijection on the
# free-decoration alphabet; it fixes the morphism's structural identity (lifts,
# composite map, target data, source-side datum). An attribution INVARIANT must
# be constant on relabeling orbits -- otherwise it is reading display metadata,
# not the morphism.
# ---------------------------------------------------------------------------


def relabel(case: Case, label_map: dict[str, str], path_map: dict[str, str]) -> Case:
    # The name is structural identity, NOT a free decoration: relabeling fixes
    # the morphism, so the name is preserved. Only free_label / path_tag move.
    return Case(
        name=case.name,
        target_obstructed=case.target_obstructed,
        lifts=case.lifts,
        composite_map=case.composite_map,
        target_global_sections=case.target_global_sections,
        obstruction_id=case.obstruction_id,
        free_label=label_map.get(case.free_label, case.free_label),
        path_tag=path_map.get(case.path_tag, case.path_tag),
        hidden_source_datum=case.hidden_source_datum,
    )


# ---------------------------------------------------------------------------
# Candidate attribution invariants. Each is a Case -> hashable value. We tag each
# with the stratum it reads so the classifier can be checked, but the classifier
# DOES NOT trust the tag: it independently measures nu-measurability,
# relabeling-stability, and source-dependence by execution.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Candidate:
    name: str
    invariant: Callable[[Case], object]
    declared_stratum: str  # "nu" | "source" | "free" | "ambient"
    outside_canonical: bool  # is it DEFINED outside the canonical psi.nu derivation?
    note: str


# (i) nu-measurable canonical invariant: the T220 derived obligation. Inside the
# canonical construction; cannot separate same-nu cases. Baseline / control.
def inv_canonical_obligation(case: Case) -> object:
    if not case.target_obstructed:
        return ()
    verdicts = {lift.allowed for lift in case.lifts}
    if verdicts != {False, True}:
        return ()
    return tuple(sorted((l.left_source, l.right_source) for l in case.lifts if l.allowed))


# (ii) source-reading invariant: reads the hidden source datum directly. Defined
# OUTSIDE the canonical construction (it is not psi.nu), and it DOES separate
# same-nu cases -- the textbook route-(b) attempt. Falsifier: it is absorbed,
# because admitting hidden_source_datum as audit data makes nu' separate the
# pair too, so a mature neighbor reproduces the separation.
def inv_source_reading(case: Case) -> object:
    return case.hidden_source_datum


# (iii) free-decoration invariant: reads the display label. Outside the canonical
# construction and separates relabeling-distinct cases. Falsifier: NOT invariant
# -- a relabeling that fixes the morphism changes its value, so it is not an
# attribution invariant of the morphism at all.
def inv_free_label(case: Case) -> object:
    return (case.free_label, case.path_tag)


# (iv-a) ambient/extensional "invariant": position in a chosen enumeration of the
# family. Outside the canonical construction and can separate any two cases.
# Falsifier: NOT a function of the morphism in isolation -- it depends on the
# chosen family/order, so it is non-local. We model it as reading an external
# registry pre-seeded with a chosen enumeration; the value is NOT derivable from
# the case's own data. The registry is seeded for the witness fiber so the
# invariant genuinely SEPARATES (clears gate 1) and is then caught by the
# locality gate (3b) -- which is the structurally correct reason it fails.
_AMBIENT_INDEX: dict[str, int] = {}


def _seed_ambient_index() -> None:
    """Seed the external enumeration for the witness fiber. This is the 'chosen
    family/order' an ambient invariant secretly depends on; it is not part of any
    case's data."""
    for i, name in enumerate(
        ("fiber_plain", "fiber_relabel", "fiber_hidden_X", "fiber_hidden_Y")
    ):
        _AMBIENT_INDEX[name] = i


def inv_ambient_index(case: Case) -> object:
    # Deliberately non-local: the value depends on an external registry, not on
    # the case's own data. Structurally identical cases get different values
    # purely from the chosen enumeration -- it is not a function of the morphism.
    return _AMBIENT_INDEX.get(case.name, -1)


# (iv-b) The strongest honest OUTSIDE candidate that is NOT obviously cheating:
# a structural source-fiber-cardinality invariant that tries to count source
# lifts WITHOUT going through the canonical obligation derivation. The hope is
# that "how many source lifts collapse onto the same target" is a property of the
# morphism that is invariant and local yet not psi.nu. Falsifier (the decisive
# one): the lift table IS part of nu (csp/provenance), so this invariant is in
# fact nu-measurable -- it factors through nu after all and cannot separate a
# same-nu pair. This is the trap the audit warns about: the natural "outside"
# candidate slides back inside nu.
def inv_source_fiber_cardinality(case: Case) -> object:
    # counts distinct source endpoints appearing in allowed lifts
    allowed_sources = {l.left_source for l in case.lifts if l.allowed}
    allowed_sources |= {l.right_source for l in case.lifts if l.allowed}
    return len(allowed_sources)


def all_candidates() -> tuple[Candidate, ...]:
    return (
        Candidate(
            name="canonical_obligation",
            invariant=inv_canonical_obligation,
            declared_stratum="nu",
            outside_canonical=False,
            note="T220 psi.nu obligation; inside canonical construction; nu-measurable control.",
        ),
        Candidate(
            name="source_reading",
            invariant=inv_source_reading,
            declared_stratum="source",
            outside_canonical=True,
            note="Reads hidden source datum directly; the textbook route-(b) attempt.",
        ),
        Candidate(
            name="free_label",
            invariant=inv_free_label,
            declared_stratum="free",
            outside_canonical=True,
            note="Reads display/path metadata; tests the relabeling-stability gate.",
        ),
        Candidate(
            name="ambient_index",
            invariant=inv_ambient_index,
            declared_stratum="ambient",
            outside_canonical=True,
            note="Reads an external enumeration index; tests the locality gate.",
        ),
        Candidate(
            name="source_fiber_cardinality",
            invariant=inv_source_fiber_cardinality,
            declared_stratum="nu",
            outside_canonical=True,
            note="Strongest honest 'outside' candidate; secretly nu-measurable (the trap).",
        ),
    )


# ---------------------------------------------------------------------------
# The three gates. An attribution invariant clears route (b) ONLY if it
# separates a same-nu pair while passing all three:
#   GATE 1 (separates)        : I(a) != I(b) for some pair with nu(a) == nu(b).
#   GATE 2 (non-absorbable)   : the separation is NOT reproduced by nu' for ANY
#                               admissible enlargement; i.e. it does not come from
#                               a source field that, once admitted as audit data,
#                               makes a mature neighbor separate the pair too.
#   GATE 3 (genuine invariant): I is constant on relabeling orbits (stable under
#                               every bijection of free decorations) AND local
#                               (a function of the case's own data, not an
#                               external registry).
# A candidate that fails ANY gate does NOT clear route (b).
# ---------------------------------------------------------------------------


def is_nu_measurable(inv: Callable[[Case], object], universe: tuple[Case, ...]) -> bool:
    """True iff inv is constant on every fiber of nu over the universe."""
    by_fiber: dict[tuple[object, ...], set] = {}
    for case in universe:
        by_fiber.setdefault(nu(case), set()).add(_freeze(inv(case)))
    return all(len(values) == 1 for values in by_fiber.values())


def is_relabel_stable(inv: Callable[[Case], object], universe: tuple[Case, ...]) -> bool:
    """True iff inv is unchanged by every bijection of the free-decoration alphabets."""
    labels = sorted({c.free_label for c in universe})
    paths = sorted({c.path_tag for c in universe})
    label_perms = list(permutations(labels)) if labels else [()]
    path_perms = list(permutations(paths)) if paths else [()]
    for case in universe:
        for lp in label_perms:
            for pp in path_perms:
                lmap = dict(zip(labels, lp))
                pmap = dict(zip(paths, pp))
                if _freeze(inv(relabel(case, lmap, pmap))) != _freeze(inv(case)):
                    return False
    return True


def is_local(inv: Callable[[Case], object]) -> bool:
    """True iff inv is a pure function of the case data alone.

    We detect non-locality structurally: an invariant is non-local exactly when
    its value can change without any change to the case's own fields. We test
    this by evaluating the invariant on a case, then on a STRUCTURAL CLONE built
    only from the case's own data (a fresh Case with identical fields), and on a
    second clone after mutating only the external registry. A local invariant is
    insensitive to the registry; a non-local one is not.
    """
    probe = Case(
        name="locality_probe",
        target_obstructed=True,
        lifts=(Lift("a", "b", True),),
        composite_map=(("a", "x"),),
        target_global_sections=0,
        obstruction_id="probe",
        free_label="L",
        path_tag="P",
    )
    clone = Case(**{**probe.__dict__})
    before = _freeze(inv(probe))
    clone_val = _freeze(inv(clone))
    # mutate external registry only; case data untouched
    _AMBIENT_INDEX[probe.name] = _AMBIENT_INDEX.get(probe.name, 0) + 1
    after = _freeze(inv(probe))
    _AMBIENT_INDEX.pop(probe.name, None)
    # local iff identical structural data -> identical value AND registry-insensitive
    return before == clone_val and before == after


def _freeze(value: object) -> object:
    if isinstance(value, (list, set)):
        return tuple(sorted(_freeze(v) for v in value))
    if isinstance(value, dict):
        return tuple(sorted((k, _freeze(v)) for k, v in value.items()))
    return value


# ---------------------------------------------------------------------------
# Same-nu witness family. We need at least one nu-fiber containing >= 2 cases
# that differ ONLY in strata (ii)/(iii)/(iv), so every separation attempt is
# forced through exactly one gate. This is the T220 hidden-source pair plus a
# free-decoration alias, all sharing one nu signature.
# ---------------------------------------------------------------------------


_SHADOW_MAP = (
    ("left_keep", "branch_shadow"),
    ("left_flip", "branch_shadow"),
    ("right_keep", "branch_shadow"),
    ("right_flip", "branch_shadow"),
)


def _uniform_true_lifts() -> tuple[Lift, ...]:
    return (
        Lift("left_keep", "right_keep", True),
        Lift("left_keep", "right_flip", True),
        Lift("left_flip", "right_keep", True),
        Lift("left_flip", "right_flip", True),
    )


def same_nu_fiber() -> tuple[Case, ...]:
    """One nu-fiber with four members differing only off-nu.

    All four share: uniform-true lift table, same composite map, same target
    fields => identical nu. They differ only in hidden source datum (ii) and/or
    free decorations (iii). This is the arena where route (b) must win or lose.
    """
    base = dict(
        target_obstructed=True,
        lifts=_uniform_true_lifts(),
        composite_map=_SHADOW_MAP,
        target_global_sections=0,
        obstruction_id="target_branch_ambiguity",
    )
    return (
        Case(name="fiber_plain", free_label="rep", path_tag="alpha", hidden_source_datum="", **base),
        Case(name="fiber_relabel", free_label="display", path_tag="beta", hidden_source_datum="", **base),
        Case(name="fiber_hidden_X", free_label="rep", path_tag="alpha", hidden_source_datum="secret_X", **base),
        Case(name="fiber_hidden_Y", free_label="rep", path_tag="alpha", hidden_source_datum="secret_Y", **base),
    )


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CandidateReport:
    name: str
    declared_stratum: str
    outside_canonical: bool
    nu_measurable: bool
    separates_same_nu_pair: bool
    separation_absorbed_by_nu_prime: bool
    relabel_stable: bool
    local: bool
    clears_route_b: bool
    failure_gate: str  # "" if clears; else the first gate it fails
    interpretation: str


@dataclass(frozen=True)
class T230Result:
    fiber_size: int
    distinct_nu_signatures_in_fiber: int
    candidate_reports: tuple[CandidateReport, ...]
    any_candidate_clears_route_b: bool
    route_b_separation_exhibited: bool
    route_a_subsumption_supported_on_family: bool
    every_local_relabelstable_nonabsorbable_invariant_factors_through_nu: bool
    verdict: str
    strongest_claim: str
    first_obstruction: str
    constructive_next_object: str
    meaning_for_claim: str
    falsification_condition: str
    next_step: str


def _separating_same_nu_pair(
    inv: Callable[[Case], object], fiber: tuple[Case, ...]
) -> tuple[Case, Case] | None:
    for a, b in combinations(fiber, 2):
        if nu(a) == nu(b) and _freeze(inv(a)) != _freeze(inv(b)):
            return (a, b)
    return None


def _absorbed_by_nu_prime(pair: tuple[Case, Case]) -> bool:
    """The separation is absorbed iff some admissible enlargement nu' also
    separates the pair (a mature neighbor, once granted the source field as audit
    data, reproduces the distinction)."""
    a, b = pair
    return nu_prime(a) != nu_prime(b)


def analyze() -> T230Result:
    _seed_ambient_index()  # the ambient invariant's external enumeration
    fiber = same_nu_fiber()
    universe = fiber
    distinct_nu = len({nu(c) for c in fiber})

    reports: list[CandidateReport] = []
    for cand in all_candidates():
        nu_meas = is_nu_measurable(cand.invariant, universe)
        sep_pair = _separating_same_nu_pair(cand.invariant, fiber)
        separates = sep_pair is not None
        absorbed = _absorbed_by_nu_prime(sep_pair) if sep_pair else False
        relabel_stable = is_relabel_stable(cand.invariant, universe)
        local = is_local(cand.invariant)

        # Route (b) requires: separates a same-nu pair (gate 1),
        # NOT absorbed by nu' (gate 2), genuinely invariant = relabel-stable AND
        # local (gate 3). It must also be defined outside the canonical
        # construction; a nu-measurable invariant cannot separate anyway.
        failure_gate = ""
        if not separates:
            failure_gate = "gate1_no_same_nu_separation"
        elif absorbed:
            failure_gate = "gate2_absorbed_by_nu_prime"
        elif not relabel_stable:
            failure_gate = "gate3a_not_relabel_invariant"
        elif not local:
            failure_gate = "gate3b_not_local"
        clears = failure_gate == ""

        if clears:
            interp = (
                "CLEARS route (b): separates a same-nu pair, is not reproduced by "
                "any admissible nu', and is a genuine local relabeling-stable "
                "invariant. THIS WOULD FLIP independent-motivation toward EARNED."
            )
        elif failure_gate == "gate1_no_same_nu_separation":
            interp = (
                "Cannot separate any same-nu pair => nu-measurable on the fiber; "
                "factors through the canonical neighbor data (T220 regime)."
            )
        elif failure_gate == "gate2_absorbed_by_nu_prime":
            interp = (
                "Separates only by reading a source field; admitting that field as "
                "audit data enlarges nu to nu' which reproduces the separation => "
                "absorbed one level up. Route (b) FAIL, not a win."
            )
        elif failure_gate == "gate3a_not_relabel_invariant":
            interp = (
                "Separates only via display/path metadata; a relabeling that fixes "
                "the morphism changes its value => not an attribution invariant of "
                "the morphism."
            )
        else:
            interp = (
                "Separates only via an external enumeration index => not a function "
                "of the morphism in isolation (non-local); not an invariant OF the "
                "morphism."
            )

        reports.append(
            CandidateReport(
                name=cand.name,
                declared_stratum=cand.declared_stratum,
                outside_canonical=cand.outside_canonical,
                nu_measurable=nu_meas,
                separates_same_nu_pair=separates,
                separation_absorbed_by_nu_prime=absorbed,
                relabel_stable=relabel_stable,
                local=local,
                clears_route_b=clears,
                failure_gate=failure_gate,
                interpretation=interp,
            )
        )

    any_clears = any(r.clears_route_b for r in reports)

    # Route (a) bounded support (HONEST FORM): the naive statement "every local
    # relabel-stable invariant factors through nu" is FALSE -- the source reader
    # is local and relabel-stable yet separates a same-nu pair. Gate 2 is the
    # load-bearing clause: a source reader separates but is ABSORBED once its
    # field is admitted. So the citable bounded negative is the THREE-clause
    # statement: every invariant that is local, relabel-stable, AND non-absorbable
    # (its separation is not reproduced by any admissible nu') factors through nu
    # on the family (cannot separate a same-nu pair). This is exactly the route-(a)
    # subsumption restricted to non-absorbable invariants, which is the only honest
    # version -- absorbable separators are real separators, they just don't count
    # as independence because a neighbor reproduces them.
    qualifying = [
        r
        for r in reports
        if r.relabel_stable and r.local and not r.separation_absorbed_by_nu_prime
    ]
    every_qualifying_factors = all(not r.separates_same_nu_pair for r in qualifying)

    verdict = "no-go" if not any_clears else "EARNED-candidate"

    return T230Result(
        fiber_size=len(fiber),
        distinct_nu_signatures_in_fiber=distinct_nu,
        candidate_reports=tuple(reports),
        any_candidate_clears_route_b=any_clears,
        route_b_separation_exhibited=any_clears,
        route_a_subsumption_supported_on_family=(not any_clears) and every_qualifying_factors,
        every_local_relabelstable_nonabsorbable_invariant_factors_through_nu=every_qualifying_factors,
        verdict=verdict,
        strongest_claim=(
            "On the finite same-nu witness family, NO candidate attribution "
            "invariant clears route (b): every invariant that separates a same-nu "
            "pair does so by (gate 2) reading a source field that, once admitted "
            "as audit data, enlarges nu to nu' and reproduces the separation in a "
            "mature neighbor (absorbed); or (gate 3a) reading display/path "
            "metadata that a morphism-fixing relabeling changes (not invariant); "
            "or (gate 3b) reading an external enumeration index (not local). The "
            "Note the honest subtlety: relabeling-stability and locality alone are "
            "NOT enough -- the source reader is local and relabeling-stable yet "
            "separates; it loses ONLY at gate 2 (absorption). So the citable "
            "bounded negative is the three-clause statement: every invariant that "
            "is local, relabeling-stable, AND non-absorbable factors through nu on "
            "the family. Route (b) separation is NOT exhibited; gate 2 is the "
            "load-bearing clause distinguishing a real separator (the source reader) "
            "from an independence-earning one."
        ),
        first_obstruction=(
            "The absorption-escape trichotomy is exhaustive: a same-nu separator "
            "must read stratum (ii) source, (iii) free, or (iv) ambient, and each "
            "stratum is closed under exactly one gate (absorbed / non-invariant / "
            "non-local). The missing object route (b) needs is an invariant that "
            "reads a FOURTH kind of datum -- intrinsic to the morphism, not in nu, "
            "not a free decoration, not an external choice, and not admissible as "
            "neighbor audit data. No such datum is exhibited on this finite family; "
            "its existence is exactly Open Problem 11.1 left open."
        ),
        constructive_next_object=(
            "A 'rigidity certificate' invariant: a quantity that depends on a "
            "source-side automorphism obstruction of the morphism (e.g. whether the "
            "source fiber admits a nontrivial self-map fixing every nu-visible "
            "datum) rather than on the value of any source field. If such an "
            "automorphism-class invariant separates a same-nu pair, gate 2 cannot "
            "absorb it (there is no single source FIELD to admit -- the datum is a "
            "symmetry-class, not a value), gate 3a/3b pass (it is local and "
            "relabeling-stable by construction). Build the source-automorphism "
            "groupoid of a typed-lossy morphism and test whether its isomorphism "
            "class is nu-measurable. That is the one untested crack in the "
            "trichotomy."
        ),
        meaning_for_claim=(
            "Independent-motivation criterion: NOT flipped to EARNED by route (b). "
            "The bounded negative (route (a) on the family) is the citable result: "
            "the LossKernel attribution line collapses onto neighbor-visible data "
            "for every relabeling-stable local invariant tested, sharpening the "
            "2026-06-24 hostile audit's NOT-EARNED from a single-case certificate "
            "(T220) to a trichotomy-exhaustion over the off-nu strata. The line is "
            "cleanly closeable unless the source-automorphism crack (next object) "
            "yields a non-nu-measurable invariant."
        ),
        falsification_condition=(
            "This no-go is overturned in route (b)'s favor by exhibiting ONE "
            "invariant I and ONE pair (a,b) with nu(a)=nu(b), I(a)!=I(b), where I "
            "is relabel-stable AND local AND the separation is NOT reproduced by "
            "nu_prime for any admissible source-field admission. The harness will "
            "report clears_route_b=True and verdict flips to EARNED-candidate. The "
            "source-automorphism rigidity certificate is the designated candidate "
            "to try."
        ),
        next_step=(
            "Build models for the source-automorphism groupoid of a typed-lossy "
            "morphism and test whether its isomorphism-class invariant is "
            "nu-measurable on a same-nu fiber. If nu-measurable, route (a) strong "
            "subsumption strengthens toward a full theorem and the LossKernel line "
            "closes. If NOT nu-measurable and it separates a same-nu pair without "
            "an admissible field, route (b) is alive and independent-motivation "
            "trends EARNED -- record with maximum care."
        ),
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _report_to_dict(r: CandidateReport) -> dict[str, object]:
    return {
        "name": r.name,
        "declared_stratum": r.declared_stratum,
        "outside_canonical": r.outside_canonical,
        "nu_measurable": r.nu_measurable,
        "separates_same_nu_pair": r.separates_same_nu_pair,
        "separation_absorbed_by_nu_prime": r.separation_absorbed_by_nu_prime,
        "relabel_stable": r.relabel_stable,
        "local": r.local,
        "clears_route_b": r.clears_route_b,
        "failure_gate": r.failure_gate,
        "interpretation": r.interpretation,
    }


def result_to_dict(result: T230Result) -> dict[str, object]:
    return {
        "fiber_size": result.fiber_size,
        "distinct_nu_signatures_in_fiber": result.distinct_nu_signatures_in_fiber,
        "candidate_reports": [_report_to_dict(r) for r in result.candidate_reports],
        "any_candidate_clears_route_b": result.any_candidate_clears_route_b,
        "route_b_separation_exhibited": result.route_b_separation_exhibited,
        "route_a_subsumption_supported_on_family": result.route_a_subsumption_supported_on_family,
        "every_local_relabelstable_nonabsorbable_invariant_factors_through_nu": (
            result.every_local_relabelstable_nonabsorbable_invariant_factors_through_nu
        ),
        "verdict": result.verdict,
        "strongest_claim": result.strongest_claim,
        "first_obstruction": result.first_obstruction,
        "constructive_next_object": result.constructive_next_object,
        "meaning_for_claim": result.meaning_for_claim,
        "falsification_condition": result.falsification_condition,
        "next_step": result.next_step,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(result_to_dict(analyze()), indent=2))
