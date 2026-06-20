"""T91: platform audit for weak-measurement independent D1 axes.

This model instantiates T90 on concrete experimental platform families.
It does not simulate lab dynamics. It audits whether a proposed branch-live
or reversal-cost axis is pre-registered, independent of standard monitored
statistics, and usable without postselection.
"""

from __future__ import annotations

from dataclasses import dataclass


DERIVED_STANDARD = "derived_from_standard_record"
INTERVENTION = "intervention_channel"
POSTSELECTED = "postselected_outcome"


@dataclass(frozen=True)
class PlatformCandidate:
    platform: str
    paper_anchor: str
    candidate_axis: str
    source_type: str
    pre_registered: bool
    independent_of_standard_record: bool
    requires_postselection: bool
    can_change_taf_verdict_with_standard_record_fixed: bool
    notes: str


@dataclass(frozen=True)
class PlatformAudit:
    platform: str
    paper_anchor: str
    candidate_axis: str
    classification: str
    blocker: str
    notes: str


@dataclass(frozen=True)
class T91Result:
    audits: tuple[PlatformAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    blocker: str
    recommended_next: str


def classify_candidate(candidate: PlatformCandidate) -> PlatformAudit:
    if not candidate.pre_registered:
        classification = "null_not_preregistered"
        blocker = "candidate axis is not fixed before analysis"
    elif candidate.requires_postselection:
        classification = "null_postselected_axis"
        blocker = "candidate axis depends on success-conditioned or null-outcome selection"
    elif not candidate.independent_of_standard_record:
        classification = "null_same_record_derivation"
        blocker = "candidate axis is reconstructed from the same monitoring record as the standard trajectory"
    elif not candidate.can_change_taf_verdict_with_standard_record_fixed:
        classification = "not_isolated"
        blocker = "no isolated verdict change survives with standard monitored statistics held fixed"
    else:
        classification = "candidate_non_null_platform"
        blocker = "none"

    return PlatformAudit(
        platform=candidate.platform,
        paper_anchor=candidate.paper_anchor,
        candidate_axis=candidate.candidate_axis,
        classification=classification,
        blocker=blocker,
        notes=candidate.notes,
    )


def platform_candidates() -> tuple[PlatformCandidate, ...]:
    return (
        PlatformCandidate(
            platform="superconducting homodyne trajectory",
            paper_anchor="Murch et al. 2013 / Kumar et al. 2018",
            candidate_axis="branch-live witness from homodyne current plus Bayesian trajectory estimate",
            source_type=DERIVED_STANDARD,
            pre_registered=True,
            independent_of_standard_record=False,
            requires_postselection=False,
            can_change_taf_verdict_with_standard_record_fixed=False,
            notes=(
                "The same continuous homodyne current that fixes coherence decay and "
                "trajectory reconstruction also fixes the proposed branch-live readout. "
                "No extra D1 axis is named beyond a refined function of the standard record."
            ),
        ),
        PlatformCandidate(
            platform="superconducting phase-qubit uncollapse",
            paper_anchor="Katz et al. 2008",
            candidate_axis="reversal-cost witness from partial-collapse reversal success",
            source_type=POSTSELECTED,
            pre_registered=True,
            independent_of_standard_record=False,
            requires_postselection=True,
            can_change_taf_verdict_with_standard_record_fixed=False,
            notes=(
                "The apparent undo witness is conditioned on the second measurement's null/success "
                "outcome after a designed pulse sequence. That makes it a postselected recovery event, "
                "not an independently metered reversal-cost observable."
            ),
        ),
        PlatformCandidate(
            platform="three-level superconducting quantum-jump reversal",
            paper_anchor="Minev et al. 2019",
            candidate_axis="mid-flight warning and feedback reversal as branch-live or reversal witness",
            source_type=INTERVENTION,
            pre_registered=True,
            independent_of_standard_record=False,
            requires_postselection=False,
            can_change_taf_verdict_with_standard_record_fixed=False,
            notes=(
                "The warning signal is the no-click interval in the same monitoring stream used to infer "
                "the trajectory, and the reversal is a fixed feedback policy triggered by that stream. "
                "This validates controllable trajectory theory, but it does not isolate a D1 axis beyond "
                "the monitored record itself."
            ),
        ),
    )


def run_t91_analysis() -> T91Result:
    audits = tuple(classify_candidate(candidate) for candidate in platform_candidates())
    strongest_claim = (
        "The concrete superconducting weak-measurement platforms audited here "
        "do not yet supply an independent D1 branch-support or reversal-cost "
        "observable. They validate quantum trajectory control, but the proposed "
        "TaF axes collapse either to the same monitored record or to postselected recovery."
    )
    improved = (
        "T91 replaces T90's platform placeholder with a concrete negative audit. "
        "The repo can now say which named experimental families fail the independent-axis test and why."
    )
    weakened = (
        "This weakens the idea that currently standard superconducting weak-measurement "
        "setups already contain a hidden TaF discriminator waiting to be relabeled."
    )
    falsification_condition = (
        "T91 fails if a named weak-measurement platform supplies a pre-registered "
        "branch/provenance/reversal observable that is not reconstructible from the "
        "same standard monitoring record, does not rely on success-conditioned "
        "postselection, and changes the TaF verdict while the standard record is held fixed."
    )
    q1_update = (
        "Keep Q1 partially supported, but narrow the T12 route further: known "
        "superconducting homodyne, uncollapse, and quantum-jump-reversal platforms "
        "do not yet instantiate the independent D1 axis required by T90."
    )
    blocker = (
        "The missing object is still the same one: a pre-registered branch, "
        "provenance, or reversal-cost observable that is operationally distinct "
        "from the monitored trajectory record itself."
    )
    recommended_next = (
        "Stop treating standard homodyne/jump-reversal platforms as near-ready T12 "
        "tests. Search instead for a duplicated-record provenance channel during monitoring "
        "or a physically metered undo cost that is fixed before analysis and not success-conditioned."
    )
    return T91Result(
        audits=audits,
        strongest_claim=strongest_claim,
        improved=improved,
        weakened=weakened,
        falsification_condition=falsification_condition,
        q1_update=q1_update,
        blocker=blocker,
        recommended_next=recommended_next,
    )


def t91_result_to_dict(result: T91Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "platform": audit.platform,
                "paper_anchor": audit.paper_anchor,
                "candidate_axis": audit.candidate_axis,
                "classification": audit.classification,
                "blocker": audit.blocker,
                "notes": audit.notes,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }
