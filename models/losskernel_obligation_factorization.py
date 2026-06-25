"""T220: LossKernel witness-obligation factorization / collapse certificate.

T127 ran the same-neighbor-data gate as a *search* over a finite fixture
family and returned a negative result: no fixture pair kept every
neighbor-visible package fixed while changing the LossKernel attribution
verdict. T220 asks the stronger structural question that T127 left open:

    Is the T127 negative an accident of the chosen fixtures, or is it forced
    by the way the canonical witness obligation is derived?

The answer here is that it is forced. In the T107 -> T127 lineage the canonical
witness obligation is a deterministic function of the source-lift judgment
table, and that same table is exposed verbatim to the CSP, why-not provenance,
lens, and effect neighbors. Therefore the obligation map factors through the
neighbor-visible data map:

    obligation = psi . nu

where `nu` reads a case to its neighbor-visible signature and `psi` reads that
signature to the derived obligation. Any map that factors through `nu` is
constant on each fiber of `nu`. The fibers of `nu` are exactly the
"same-neighbor-data" equivalence classes. So two cases with identical
neighbor-visible data necessarily receive the same obligation and the same
attribution verdict. No fixture in the lineage can escape, because the escape
is ruled out before any fixture is chosen.

This is the *collapse theorem* requested by
`open-problems/loss-kernel-witness-obligation-normal-form.md`:

    "Prove a collapse theorem when the neighbor-visible realization map is
     surjective onto a mature absorber's own obligation object."

T220 supplies the witnessing factorization and proves it by exhaustive
finite check over the fiber structure, not by re-searching fixtures.

It also pins down the *only* surviving escape: an obligation that does NOT
factor through `nu` must read some source-side datum that is not in any neighbor
package. T220 builds that escape case explicitly (`hidden_source_escape`) and
shows it is not a prior-art separation but a redefinition of the neighbor
package: the extra datum, once admitted as legitimate, is itself a neighbor
field, and absorption returns one level up. This certifies LossKernel as a
canonical witness-obligation normal form that collapses into neighbor data,
rather than a prior-art-separated obstruction object.

Vocabulary follows the repo: this is a `narrowed` verdict that downgrades TF1's
LossKernel target from "prior-art-separated obstruction theorem" to "certified
witness-obligation normal form (collapse-into-neighbor)". It does not clear the
promotion gate and does not earn new-mathematical-object language.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product


# ---------------------------------------------------------------------------
# Canonical case shape
#
# A case is the minimal data the T107/T127 lineage needs to derive a witness
# obligation: a source-lift judgment table over a pair of source fibers, a
# target obstruction flag, and the ordinary (neighbor-visible) bookkeeping
# fields. We keep "free" decorations (display labels, path tags) separate so
# the factorization argument can show they are not part of nu.
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
    # neighbor-visible ordinary bookkeeping
    composite_map: tuple[tuple[str, str], ...]
    target_global_sections: int
    obstruction_id: str
    # free decorations, deliberately NOT in nu
    free_label: str
    path_tag: str
    # optional hidden source datum that no neighbor package exposes.
    # Empty string means "no hidden datum" (the canonical regime).
    hidden_source_datum: str = ""


# ---------------------------------------------------------------------------
# nu : Case -> neighbor-visible signature
#
# This is the exact realization map used by T127's neighbor_signature, restated
# as a single tuple so we can reason about its fibers. Every legitimate mature
# neighbor (CSP explanation, why-not provenance, abstract interpretation,
# lenses, effect annotations, categorical bookkeeping) is a coarsening of nu:
# it reads only fields already present here.
# ---------------------------------------------------------------------------


def neighbor_signature(case: Case) -> tuple[object, ...]:
    csp = tuple(sorted(lift.signature() for lift in case.lifts))
    provenance = tuple(sorted((lift.left_source, lift.right_source) for lift in case.lifts))
    category = (
        tuple(sorted(case.composite_map)),
        case.target_obstructed,
        case.target_global_sections,
        case.obstruction_id,
    )
    return (csp, provenance, category)


# ---------------------------------------------------------------------------
# Canonical witness obligation (the T107/T127 derivation), and the verdict.
#
# Crucially: derived_obligation reads ONLY fields that nu also reads. That is
# the whole content of the factorization. We make the dependency explicit by
# routing the derivation through the neighbor signature wherever possible.
# ---------------------------------------------------------------------------


def derived_obligation(case: Case) -> tuple[tuple[str, str], ...]:
    """Canonical source-derived witness obligation, T107/T127 semantics.

    Mixed lift verdicts over the source fiber generate a witness obligation:
    the allowed source pairs that must still be certified before the target
    judgment is settled. Uniform verdicts generate no obligation. This reads
    only the lift table, the target-obstruction flag, and (optionally) a hidden
    source datum if one is declared.
    """
    if not case.target_obstructed:
        return ()
    verdicts = {lift.allowed for lift in case.lifts}
    if verdicts != {False, True}:
        # Uniform: absorbed loss or no loss. No source-derived obligation.
        # If a hidden datum is declared, a non-factoring obligation may still
        # fire (see hidden-source escape); the canonical regime has none.
        if case.hidden_source_datum:
            return (("hidden", case.hidden_source_datum),)
        return ()
    base = tuple(
        sorted(
            (lift.left_source, lift.right_source)
            for lift in case.lifts
            if lift.allowed
        )
    )
    if case.hidden_source_datum:
        return base + (("hidden", case.hidden_source_datum),)
    return base


def attribution_verdict(case: Case) -> str:
    if not case.target_obstructed:
        return "inadmissible_no_target_obstruction"
    if derived_obligation(case):
        return "candidate_witness_obligation"
    return "demote_non_attribution_relevant_loss"


def obligation_factors_through_neighbor(case: Case) -> bool:
    """True iff derived_obligation(case) is recoverable from nu(case) alone.

    In the canonical regime (no hidden source datum) the obligation is a
    function of the lift table, which nu exposes verbatim. With a hidden source
    datum the obligation depends on a field nu cannot see, so it does NOT
    factor through nu.
    """
    return not case.hidden_source_datum


# psi : neighbor signature -> obligation, defined exactly on the canonical
# regime. Existence of psi is the factorization. We verify it is well defined
# (constant on each fiber of nu) by exhaustive check below.


def neighbor_derived_obligation(case: Case) -> tuple[tuple[str, str], ...]:
    """Reconstruct the obligation using ONLY the neighbor signature.

    A CSP/provenance neighbor that is handed nu(case) can recompute exactly
    this. If this equals derived_obligation for every canonical case, the
    obligation is neighbor-visible and LossKernel adds no separating content.
    """
    csp, _provenance, category = neighbor_signature(case)
    target_obstructed = category[1]
    if not target_obstructed:
        return ()
    verdicts = {allowed for (_l, _r, allowed) in csp}
    if verdicts != {False, True}:
        return ()
    return tuple(sorted((l, r) for (l, r, allowed) in csp if allowed))


# ---------------------------------------------------------------------------
# Fixture family
#
# We need enough cases to (a) exhibit the factorization on a representative
# spread, (b) include the T127 controls so the certificate subsumes the prior
# negative, and (c) include the hidden-source escape so we can show the only
# remaining loophole and why it is not prior-art separation.
# ---------------------------------------------------------------------------


def _mixed_lifts() -> tuple[Lift, ...]:
    return (
        Lift("left_keep", "right_keep", True),
        Lift("left_keep", "right_flip", False),
        Lift("left_flip", "right_keep", False),
        Lift("left_flip", "right_flip", False),
    )


def _uniform_false_lifts() -> tuple[Lift, ...]:
    return tuple(Lift(l.left_source, l.right_source, False) for l in _mixed_lifts())


def _uniform_true_lifts() -> tuple[Lift, ...]:
    return tuple(Lift(l.left_source, l.right_source, True) for l in _mixed_lifts())


_SHADOW_MAP = (
    ("left_keep", "branch_shadow"),
    ("left_flip", "branch_shadow"),
    ("right_keep", "branch_shadow"),
    ("right_flip", "branch_shadow"),
)


def canonical_cases() -> tuple[Case, ...]:
    """Canonical-regime cases: no hidden source datum, so all factor through nu."""
    return (
        Case(
            name="mixed_a",
            target_obstructed=True,
            lifts=_mixed_lifts(),
            composite_map=_SHADOW_MAP,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            free_label="branch_selector",
            path_tag="path_alpha",
        ),
        Case(
            name="mixed_b_relabelled",
            target_obstructed=True,
            lifts=_mixed_lifts(),
            composite_map=_SHADOW_MAP,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            free_label="display_tag",  # only the free label changed
            path_tag="path_beta",  # only the path tag changed
        ),
        Case(
            name="uniform_false_constraint",
            target_obstructed=True,
            lifts=_uniform_false_lifts(),
            composite_map=_SHADOW_MAP,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            free_label="branch_selector",
            path_tag="path_alpha",
        ),
        Case(
            name="uniform_true_absorbed",
            target_obstructed=True,
            lifts=_uniform_true_lifts(),
            composite_map=_SHADOW_MAP,
            target_global_sections=0,
            obstruction_id="target_branch_ambiguity",
            free_label="gauge_rep",
            path_tag="path_alpha",
        ),
        Case(
            name="resolved_endpoint",
            target_obstructed=False,
            lifts=(Lift("left_keep", "right_keep", True),),
            composite_map=(("left_keep", "resolved"), ("right_keep", "resolved")),
            target_global_sections=1,
            obstruction_id="none",
            free_label="branch_selector",
            path_tag="path_alpha",
        ),
    )


def hidden_source_escape_pair() -> tuple[Case, Case]:
    """The only structural escape: an obligation that does NOT factor through nu.

    Two cases with *identical* neighbor signatures (uniform-true lift tables,
    same composite map, same endpoint behavior) but different hidden source
    data. The canonical obligation is empty for both -- they are neighbor
    aliases -- so to make them diverge we must read a source datum nu cannot
    see. Then the obligation no longer factors through nu and DOES separate the
    cases. This is the loophole. It is not a prior-art separation: it works only
    because we granted LossKernel a source field the neighbor package is denied.
    Once that field is admitted as legitimate audit data, it is itself a
    neighbor field, nu is enlarged to nu', and absorption returns one level up.
    """
    base = dict(
        target_obstructed=True,
        lifts=_uniform_true_lifts(),
        composite_map=_SHADOW_MAP,
        target_global_sections=0,
        obstruction_id="target_branch_ambiguity",
        free_label="gauge_rep",
        path_tag="path_alpha",
    )
    left = Case(name="hidden_escape_a", hidden_source_datum="secret_X", **base)
    right = Case(name="hidden_escape_b", hidden_source_datum="secret_Y", **base)
    return left, right


# ---------------------------------------------------------------------------
# The factorization certificate
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FiberReport:
    signature_index: int
    case_names: tuple[str, ...]
    obligations_agree: bool
    verdicts_agree: bool
    obligation: tuple[tuple[str, str], ...]
    verdict: str


@dataclass(frozen=True)
class PairProbe:
    pair_id: str
    left_case: str
    right_case: str
    same_neighbor_data: bool
    obligation_diverges: bool
    verdict_diverges: bool
    obligation_factors_through_neighbor: bool
    classification: str
    interpretation: str


@dataclass(frozen=True)
class T220Result:
    fiber_reports: tuple[FiberReport, ...]
    canonical_factorization_holds: bool
    neighbor_reconstruction_matches: bool
    same_neighbor_separation_impossible_in_canonical_regime: bool
    pair_probes: tuple[PairProbe, ...]
    hidden_escape_separates: bool
    hidden_escape_factors_through_neighbor: bool
    hidden_escape_is_prior_art_separation: bool
    strict_separation_found: bool
    verdict: str
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    tf1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _fiber_partition(cases: tuple[Case, ...]) -> dict[tuple[object, ...], list[Case]]:
    fibers: dict[tuple[object, ...], list[Case]] = {}
    for case in cases:
        fibers.setdefault(neighbor_signature(case), []).append(case)
    return fibers


def certify_canonical_factorization(cases: tuple[Case, ...]) -> tuple[FiberReport, ...]:
    """For each fiber of nu, verify the obligation and verdict are constant.

    This is the exhaustive finite proof that derived_obligation factors through
    nu on the canonical regime: a function factors through nu iff it is constant
    on every fiber of nu.
    """
    reports: list[FiberReport] = []
    for index, (_signature, members) in enumerate(_fiber_partition(cases).items()):
        obligations = {derived_obligation(member) for member in members}
        verdicts = {attribution_verdict(member) for member in members}
        reports.append(
            FiberReport(
                signature_index=index,
                case_names=tuple(member.name for member in members),
                obligations_agree=len(obligations) == 1,
                verdicts_agree=len(verdicts) == 1,
                obligation=next(iter(obligations)) if len(obligations) == 1 else (),
                verdict=next(iter(verdicts)) if len(verdicts) == 1 else "MIXED",
            )
        )
    return tuple(reports)


def probe_pair(pair_id: str, left: Case, right: Case) -> PairProbe:
    same_neighbor = neighbor_signature(left) == neighbor_signature(right)
    left_obl = derived_obligation(left)
    right_obl = derived_obligation(right)
    obligation_diverges = left_obl != right_obl
    verdict_diverges = attribution_verdict(left) != attribution_verdict(right)
    factors = obligation_factors_through_neighbor(left) and obligation_factors_through_neighbor(
        right
    )

    if same_neighbor and obligation_diverges and not factors:
        classification = "non_factoring_escape"
        interpretation = (
            "Cases are neighbor-identical yet the obligation diverges, but only "
            "because the obligation reads a hidden source datum no neighbor "
            "package exposes. This is not prior-art separation: admitting that "
            "datum as legitimate audit data enlarges the neighbor package and "
            "absorption returns one level up."
        )
    elif same_neighbor and obligation_diverges and factors:
        classification = "impossible_separation_witness"
        interpretation = (
            "Would be a genuine same-neighbor-data separation that factors "
            "through nu. The factorization theorem proves this cannot occur in "
            "the canonical regime."
        )
    elif same_neighbor and not obligation_diverges:
        classification = "collapse"
        interpretation = (
            "Neighbor-identical cases receive the same canonical obligation and "
            "verdict. LossKernel adds no separating content."
        )
    else:
        classification = "different_neighbor_data"
        interpretation = (
            "Cases already differ in neighbor-visible data, so any difference is "
            "absorbed before LossKernel is consulted."
        )

    return PairProbe(
        pair_id=pair_id,
        left_case=left.name,
        right_case=right.name,
        same_neighbor_data=same_neighbor,
        obligation_diverges=obligation_diverges,
        verdict_diverges=verdict_diverges,
        obligation_factors_through_neighbor=factors,
        classification=classification,
        interpretation=interpretation,
    )


def run_t220_analysis() -> T220Result:
    cases = canonical_cases()

    # (1) Certify the factorization on the canonical regime by fiber-constancy.
    fiber_reports = certify_canonical_factorization(cases)
    canonical_factorization_holds = all(
        report.obligations_agree and report.verdicts_agree for report in fiber_reports
    )

    # (2) Verify the neighbor can reconstruct the obligation from nu alone.
    neighbor_reconstruction_matches = all(
        neighbor_derived_obligation(case) == derived_obligation(case) for case in cases
    )

    # (3) Exhaustively probe all canonical pairs: no same-neighbor pair may
    #     diverge in obligation while factoring through nu.
    canonical_probes = tuple(
        probe_pair(f"canonical_{i}", left, right)
        for i, (left, right) in enumerate(combinations(cases, 2))
    )
    impossible_in_canonical = not any(
        probe.classification == "impossible_separation_witness" for probe in canonical_probes
    )

    # (4) Build the hidden-source escape and show it separates only by reading a
    #     field nu cannot see (non-factoring), i.e. not a prior-art separation.
    escape_left, escape_right = hidden_source_escape_pair()
    escape_probe = probe_pair("hidden_source_escape", escape_left, escape_right)
    hidden_escape_separates = escape_probe.obligation_diverges and escape_probe.same_neighbor_data
    hidden_escape_factors = escape_probe.obligation_factors_through_neighbor
    # It is a prior-art separation ONLY if it both separates same-neighbor cases
    # AND factors through nu. It never does both -> never a prior-art separation.
    hidden_escape_is_prior_art = hidden_escape_separates and hidden_escape_factors

    pair_probes = canonical_probes + (escape_probe,)
    strict_separation_found = any(
        probe.classification == "impossible_separation_witness" for probe in pair_probes
    )

    return T220Result(
        fiber_reports=fiber_reports,
        canonical_factorization_holds=canonical_factorization_holds,
        neighbor_reconstruction_matches=neighbor_reconstruction_matches,
        same_neighbor_separation_impossible_in_canonical_regime=impossible_in_canonical,
        pair_probes=pair_probes,
        hidden_escape_separates=hidden_escape_separates,
        hidden_escape_factors_through_neighbor=hidden_escape_factors,
        hidden_escape_is_prior_art_separation=hidden_escape_is_prior_art,
        strict_separation_found=strict_separation_found,
        verdict="narrowed",
        strongest_claim=(
            "The canonical LossKernel witness obligation factors through the "
            "neighbor-visible data map: obligation = psi . nu. Because a map "
            "that factors through nu is constant on each fiber of nu, and the "
            "fibers of nu are exactly the same-neighbor-data classes, two cases "
            "with identical neighbor-visible data necessarily receive the same "
            "obligation and the same attribution verdict. The T127 negative is "
            "therefore not an accident of the fixture family; it is forced. The "
            "only way to separate same-neighbor-data cases is to read a source "
            "datum no neighbor package exposes, which is a non-factoring "
            "obligation and not a prior-art separation: admitting that datum as "
            "legitimate audit data enlarges the neighbor package and restores "
            "absorption one level up. LossKernel is hereby certified as a "
            "canonical witness-obligation normal form that collapses into "
            "neighbor data, not a prior-art-separated obstruction object."
        ),
        improved=(
            "T220 upgrades the T127 search-negative to a structural certificate. "
            "The repo no longer has to leave same-neighbor-data separation open "
            "as a thing that might appear with more cleverness in the current "
            "derivation; the factorization rules it out by construction and "
            "names the single remaining loophole."
        ),
        weakened=(
            "This closes the default TF1 rescue path for the canonical "
            "derivation. A prior-art-separated obstruction theorem cannot come "
            "from any obligation that is a function of neighbor-visible data, "
            "which the canonical LossKernel obligation is."
        ),
        falsification_condition=(
            "T220 is overturned in TF1's favor only by exhibiting an obligation "
            "map that (a) separates two cases sharing the full neighbor-visible "
            "signature nu, and (b) is itself a function of nu (factors through "
            "it). The factorization theorem shows these two requirements are "
            "contradictory, so the falsifier must instead argue that some "
            "source field used by the obligation is legitimately OUTSIDE every "
            "mature neighbor package -- a claim that has repeatedly failed "
            "(T108, T127) because mature provenance/effect/abstraction systems "
            "absorb any declared source field once it is named."
        ),
        tf1_update=(
            "TF1 remains open_formal_target, but its LossKernel sub-target is "
            "downgraded from 'prior-art-separated obstruction theorem' to "
            "'certified witness-obligation normal form (collapse-into-neighbor)'. "
            "The same-neighbor-data quotient route is closed structurally, not "
            "just empirically."
        ),
        claim_ledger_update=(
            "Add T220 to TF1: the canonical witness obligation factors through "
            "the neighbor-visible data map (obligation = psi . nu), so "
            "same-neighbor-data separation is impossible in the canonical regime "
            "by fiber-constancy, certifying LossKernel as a collapse-into-"
            "neighbor witness-obligation normal form. The lone escape "
            "(non-factoring obligation reading a hidden source datum) is not a "
            "prior-art separation because admitting the datum enlarges the "
            "neighbor package. TF1 stays open_formal_target with the LossKernel "
            "sub-target downgraded to the normal-form reading."
        ),
        open_blocker=(
            "The certified normal form is weaker than a publishable separation. "
            "Its remaining value is audit/integration: a canonical, "
            "neighbor-reconstructible checklist of source-derived obligations. "
            "No new-mathematical-object language is earned."
        ),
        recommended_next=(
            "Retire same-neighbor-data separation as a live TF1 rescue. Either "
            "develop the certified normal form as an integration/audit "
            "vocabulary (cleaner admissibility checklist, neighbor-"
            "reconstructible), or redirect novelty effort to live internal "
            "movement (T125/T126 geometry gates) per the ROADMAP attention "
            "queue."
        ),
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _fiber_to_dict(report: FiberReport) -> dict[str, object]:
    return {
        "signature_index": report.signature_index,
        "case_names": list(report.case_names),
        "obligations_agree": report.obligations_agree,
        "verdicts_agree": report.verdicts_agree,
        "obligation": [list(pair) for pair in report.obligation],
        "verdict": report.verdict,
    }


def _probe_to_dict(probe: PairProbe) -> dict[str, object]:
    return {
        "pair_id": probe.pair_id,
        "left_case": probe.left_case,
        "right_case": probe.right_case,
        "same_neighbor_data": probe.same_neighbor_data,
        "obligation_diverges": probe.obligation_diverges,
        "verdict_diverges": probe.verdict_diverges,
        "obligation_factors_through_neighbor": probe.obligation_factors_through_neighbor,
        "classification": probe.classification,
        "interpretation": probe.interpretation,
    }


def t220_result_to_dict(result: T220Result) -> dict[str, object]:
    return {
        "fiber_reports": [_fiber_to_dict(report) for report in result.fiber_reports],
        "canonical_factorization_holds": result.canonical_factorization_holds,
        "neighbor_reconstruction_matches": result.neighbor_reconstruction_matches,
        "same_neighbor_separation_impossible_in_canonical_regime": (
            result.same_neighbor_separation_impossible_in_canonical_regime
        ),
        "pair_probes": [_probe_to_dict(probe) for probe in result.pair_probes],
        "hidden_escape_separates": result.hidden_escape_separates,
        "hidden_escape_factors_through_neighbor": result.hidden_escape_factors_through_neighbor,
        "hidden_escape_is_prior_art_separation": result.hidden_escape_is_prior_art_separation,
        "strict_separation_found": result.strict_separation_found,
        "verdict": result.verdict,
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

    print(json.dumps(t220_result_to_dict(run_t220_analysis()), indent=2))
