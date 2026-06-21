"""T153: Lorentzian causal-diamond/domain-of-dependence screen.

T151 showed that direct classical record access factors through a declared
causal-access graph. T153 replaces the graph proxy with a small 1+1 Minkowski
screen: causal pasts, causal diamonds, spacelike separation, and a finite
domain-of-dependence interval.

The point is absorptive. If a TaF verdict changes only because the Lorentzian
causal relation, access diamond, or domain of dependence changed, the residue
belongs to standard causal structure rather than to a new finality mechanism.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


EPSILON = 1e-9


@dataclass(frozen=True)
class MinkowskiEvent:
    event_id: str
    t: float
    x: float
    records: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        if not self.event_id:
            raise ValueError("event_id cannot be empty")


@dataclass(frozen=True)
class CausalDiamond:
    diamond_id: str
    past_tip: MinkowskiEvent
    future_tip: MinkowskiEvent

    def __post_init__(self) -> None:
        if not self.diamond_id:
            raise ValueError("diamond_id cannot be empty")
        if not causally_precedes(self.past_tip, self.future_tip):
            raise ValueError("past_tip must causally precede future_tip")

    def contains(self, event: MinkowskiEvent) -> bool:
        return causally_precedes(self.past_tip, event) and causally_precedes(
            event,
            self.future_tip,
        )


@dataclass(frozen=True)
class InitialDataInterval:
    interval_id: str
    t0: float
    x_min: float
    x_max: float

    def __post_init__(self) -> None:
        if not self.interval_id:
            raise ValueError("interval_id cannot be empty")
        if self.x_min > self.x_max:
            raise ValueError("x_min must be <= x_max")

    def future_domain_contains(self, event: MinkowskiEvent) -> bool:
        """Future D(S) for a 1+1 interval on the Cauchy slice t=t0.

        For wave-speed c=1, every past-directed causal curve from (t, x) must
        hit the initial slice inside [x_min, x_max]. In 1+1 Minkowski this is
        equivalent to [x - dt, x + dt] being contained in that interval.
        """

        if event.t < self.t0 - EPSILON:
            return False
        dt = event.t - self.t0
        return (
            event.x - dt >= self.x_min - EPSILON
            and event.x + dt <= self.x_max + EPSILON
        )


@dataclass(frozen=True)
class LorentzianAudit:
    case_id: str
    classification: str
    residue_label: str
    taf_adds_independent_content: bool
    lorentzian_data_matched: bool
    capability_split: bool
    causal_relation: str
    domain_of_dependence_status: str
    reason: str
    weakened_claim: str
    required_next: str


@dataclass(frozen=True)
class T153Result:
    audits: tuple[LorentzianAudit, ...]
    remote_signal_guardrail_passed: bool
    spacelike_reconciliation_guardrail_passed: bool
    domain_dependence_absorbs_reconstructability: bool
    changed_diamond_absorbed: bool
    fixed_lorentzian_data_no_residue: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    r1_update: str
    s1_update: str
    b1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def interval_squared(left: MinkowskiEvent, right: MinkowskiEvent) -> float:
    dt = right.t - left.t
    dx = right.x - left.x
    return dt * dt - dx * dx


def causally_precedes(left: MinkowskiEvent, right: MinkowskiEvent) -> bool:
    dt = right.t - left.t
    dx = abs(right.x - left.x)
    return dt >= -EPSILON and dt + EPSILON >= dx


def spacelike_separated(left: MinkowskiEvent, right: MinkowskiEvent) -> bool:
    return not causally_precedes(left, right) and not causally_precedes(right, left)


def common_future_contains(
    left: MinkowskiEvent,
    right: MinkowskiEvent,
    future_event: MinkowskiEvent,
) -> bool:
    return causally_precedes(left, future_event) and causally_precedes(
        right,
        future_event,
    )


def remote_signal_control() -> LorentzianAudit:
    source = MinkowskiEvent("remote_emission", 0.0, -5.0, frozenset({"photon"}))
    collection = MinkowskiEvent("telescope_log", 6.0, 0.0, frozenset({"ccd_log"}))
    accessible = causally_precedes(source, collection)

    return LorentzianAudit(
        case_id="remote_signal_causal_past",
        classification="remote_signal_is_causal_record_access",
        residue_label="translation_residue",
        taf_adds_independent_content=False,
        lorentzian_data_matched=True,
        capability_split=False,
        causal_relation="source_in_observer_causal_past",
        domain_of_dependence_status="not_domain_case",
        reason=(
            "The remote source is in the observer's causal past through a "
            "received light signal. Direct local participation is absent, but "
            "record access is present."
        ),
        weakened_claim=(
            "R1 may distinguish received records from direct participation, "
            "but must not treat remote astronomical sources as unobserved."
        ),
        required_next=(
            "Keep participation and received-record access as separate typed "
            "relations in S1/R1 models."
        ),
    ) if accessible else _failed_fixture("remote_signal_causal_past")


def spacelike_reconciliation_control() -> LorentzianAudit:
    left = MinkowskiEvent("left_event", 0.0, -1.0, frozenset({"left_record"}))
    right = MinkowskiEvent("right_event", 0.0, 1.0, frozenset({"right_record"}))
    comparator = MinkowskiEvent("later_comparator", 3.0, 0.0)
    spacelike = spacelike_separated(left, right)
    later_reconciles = common_future_contains(left, right, comparator)

    return LorentzianAudit(
        case_id="spacelike_pair_later_reconciliation",
        classification="spacelike_no_invariant_order_later_reconciles",
        residue_label="translation_residue",
        taf_adds_independent_content=False,
        lorentzian_data_matched=True,
        capability_split=False,
        causal_relation="spacelike_pair_with_common_future",
        domain_of_dependence_status="not_domain_case",
        reason=(
            "The two events have no invariant causal order, but both can enter "
            "a later common record. This supports no-global-commit-order "
            "language only as ordinary Lorentzian causality."
        ),
        weakened_claim=(
            "R1 should say local records can later reconcile inside a common "
            "future, not that TaF supplies a replacement simultaneity rule."
        ),
        required_next=(
            "Any stronger R1 claim must preserve invariant interval structure "
            "and frame-independent causal order."
        ),
    ) if spacelike and later_reconciles else _failed_fixture(
        "spacelike_pair_later_reconciliation"
    )


def domain_dependence_control() -> LorentzianAudit:
    initial_interval = InitialDataInterval("slice_interval", 0.0, -2.0, 2.0)
    inside = MinkowskiEvent("inside_future_domain", 1.0, 0.0)
    outside = MinkowskiEvent("outside_future_domain", 1.5, 1.0)
    inside_determined = initial_interval.future_domain_contains(inside)
    outside_determined = initial_interval.future_domain_contains(outside)

    return LorentzianAudit(
        case_id="domain_of_dependence_interval",
        classification="domain_of_dependence_absorbs_reconstructability",
        residue_label="absorbed_by_lorentzian_causality",
        taf_adds_independent_content=False,
        lorentzian_data_matched=False,
        capability_split=True,
        causal_relation="same_initial_slice_different_domain_membership",
        domain_of_dependence_status="inside_control_true_outside_control_false",
        reason=(
            "The reconstruction split is exactly membership in the future "
            "domain of dependence of the initial interval. The outside control "
            "requires initial data beyond the interval."
        ),
        weakened_claim=(
            "S1/B1 reconstructability language is absorbed when it tracks only "
            "ordinary domains of dependence."
        ),
        required_next=(
            "Name a capability not represented by causal pasts, diamonds, or "
            "domains of dependence before claiming TaF residue."
        ),
    ) if inside_determined and not outside_determined else _failed_fixture(
        "domain_of_dependence_interval"
    )


def changed_diamond_boundary_control() -> LorentzianAudit:
    source = MinkowskiEvent("source_record", 0.0, 0.0)
    narrow_future_tip = MinkowskiEvent("narrow_collection", 1.0, 2.0)
    wide_future_tip = MinkowskiEvent("wide_collection", 3.0, 0.0)
    narrow_access = causally_precedes(source, narrow_future_tip)
    wide_access = causally_precedes(source, wide_future_tip)

    return LorentzianAudit(
        case_id="same_source_changed_access_diamond",
        classification="verdict_split_absorbed_by_changed_access_diamond",
        residue_label="absorbed_by_lorentzian_access_boundary",
        taf_adds_independent_content=False,
        lorentzian_data_matched=False,
        capability_split=True,
        causal_relation="same_source_different_collection_event",
        domain_of_dependence_status="not_domain_case",
        reason=(
            "The source is inaccessible to the narrow collection event and "
            "accessible to the wider future event. The verdict split follows "
            "from a changed access diamond, not from a new finality predicate."
        ),
        weakened_claim=(
            "Same local source data do not create TaF residue when the observer "
            "access diamond changes."
        ),
        required_next=(
            "For any future S1 witness, match the observer world tube and "
            "access diamond before scoring finality differences."
        ),
    ) if (not narrow_access and wide_access) else _failed_fixture(
        "same_source_changed_access_diamond"
    )


def fixed_lorentzian_data_control() -> LorentzianAudit:
    past_tip = MinkowskiEvent("past_tip", -1.0, 0.0)
    source = MinkowskiEvent("source_record", 0.0, 0.0)
    future_tip = MinkowskiEvent("future_tip", 3.0, 0.0)
    diamond = CausalDiamond("matched_diamond", past_tip, future_tip)
    first_access = diamond.contains(source)
    second_access = diamond.contains(
        MinkowskiEvent("source_record_relabelled", source.t, source.x)
    )

    return LorentzianAudit(
        case_id="fixed_lorentzian_data_control",
        classification="fixed_lorentzian_data_no_finality_split",
        residue_label="negative_control",
        taf_adds_independent_content=False,
        lorentzian_data_matched=True,
        capability_split=False,
        causal_relation="matched_source_and_access_diamond",
        domain_of_dependence_status="not_domain_case",
        reason=(
            "When the event coordinates and access diamond are matched, a "
            "record relabel does not change the causal-access verdict."
        ),
        weakened_claim=(
            "T153 finds no same-Lorentzian-data finality split in its controls."
        ),
        required_next=(
            "A live residue must split verdicts after matching the Lorentzian "
            "causal data, observer world tube, and domain-of-dependence inputs."
        ),
    ) if first_access and second_access else _failed_fixture(
        "fixed_lorentzian_data_control"
    )


def canonical_t153_audits() -> tuple[LorentzianAudit, ...]:
    return (
        remote_signal_control(),
        spacelike_reconciliation_control(),
        domain_dependence_control(),
        changed_diamond_boundary_control(),
        fixed_lorentzian_data_control(),
    )


def run_t153_analysis() -> T153Result:
    audits = canonical_t153_audits()
    by_id = {audit.case_id: audit for audit in audits}

    remote_ok = (
        by_id["remote_signal_causal_past"].classification
        == "remote_signal_is_causal_record_access"
    )
    spacelike_ok = (
        by_id["spacelike_pair_later_reconciliation"].classification
        == "spacelike_no_invariant_order_later_reconciles"
    )
    domain_absorbed = (
        by_id["domain_of_dependence_interval"].classification
        == "domain_of_dependence_absorbs_reconstructability"
    )
    changed_diamond_absorbed = (
        by_id["same_source_changed_access_diamond"].classification
        == "verdict_split_absorbed_by_changed_access_diamond"
    )
    fixed_data_no_residue = (
        by_id["fixed_lorentzian_data_control"].classification
        == "fixed_lorentzian_data_no_finality_split"
    )

    return T153Result(
        audits=audits,
        remote_signal_guardrail_passed=remote_ok,
        spacelike_reconciliation_guardrail_passed=spacelike_ok,
        domain_dependence_absorbs_reconstructability=domain_absorbed,
        changed_diamond_absorbed=changed_diamond_absorbed,
        fixed_lorentzian_data_no_residue=fixed_data_no_residue,
        strongest_claim=(
            "In the tested 1+1 Lorentzian controls, R1/S1/B1 access and "
            "reconstructability verdicts factor through ordinary causal pasts, "
            "causal diamonds, spacelike separation with common futures, and "
            "domains of dependence. TaF adds no independent spacetime or "
            "black-hole mechanism in this screen."
        ),
        improved=(
            "T153 upgrades T151 from an abstract record-channel graph to a "
            "minimal Lorentzian absorber. It supplies explicit checks for "
            "remote observation, spacelike reconciliation, changed access "
            "diamonds, and domain-of-dependence reconstructability."
        ),
        weakened=(
            "S1 and B1 are weakened wherever their verdicts change only because "
            "standard causal-access or domain-of-dependence data changed. R1 "
            "remains safe as no-global-commit-order language, not as a new "
            "relativity substitute."
        ),
        falsification_condition=(
            "T153 fails in TaF's favor only if a future fixture matches the "
            "Lorentzian causal relation, observer world tube, access diamond, "
            "domain-of-dependence inputs, record channels, and boundary data, "
            "yet still produces a task-natural finality capability split not "
            "expressible as standard causal access or reconstructability."
        ),
        r1_update=(
            "Add T153 to R1: spacelike events lack invariant causal order but "
            "can reconcile through a common future record. Remote signals are "
            "causal record access. This supports locality discipline, not a "
            "replacement time rule."
        ),
        s1_update=(
            "Add T153 to S1: any finality-colimit or consensus-envelope model "
            "must carry Lorentzian causal data, access diamonds, and domain-of-"
            "dependence inputs before claiming spacetime-facing residue."
        ),
        b1_update=(
            "Add T153 to B1: direct-classical horizon language remains ordinary "
            "causal-access/domain-of-dependence bookkeeping unless a native "
            "black-hole information capability is typed."
        ),
        claim_ledger_update=(
            "T153 gives R1/S1/B1 a Lorentzian causal-diamond screen. The tested "
            "verdicts factor through causal pasts, common futures, changed "
            "access diamonds, and domains of dependence. No same-Lorentzian-"
            "data TaF residue is found."
        ),
        open_blocker=(
            "The screen is 1+1 Minkowski only. It has no curvature, global "
            "hyperbolicity theorem, black-hole metric, QFT algebra, holographic "
            "encoding, semiclassical gravity, or continuum finality-colimit "
            "construction."
        ),
        suggested_next=(
            "Use T153 as the absorber gate for S1/B1. The next non-null move is "
            "either a causal-set/manifoldlikeness implementation for T126 or a "
            "named Schwarzschild/de Sitter causal-access witness with native "
            "absorber variables declared up front."
        ),
    )


def t153_result_to_dict(result: T153Result) -> dict[str, Any]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "remote_signal_guardrail_passed": result.remote_signal_guardrail_passed,
        "spacelike_reconciliation_guardrail_passed": (
            result.spacelike_reconciliation_guardrail_passed
        ),
        "domain_dependence_absorbs_reconstructability": (
            result.domain_dependence_absorbs_reconstructability
        ),
        "changed_diamond_absorbed": result.changed_diamond_absorbed,
        "fixed_lorentzian_data_no_residue": result.fixed_lorentzian_data_no_residue,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "r1_update": result.r1_update,
        "s1_update": result.s1_update,
        "b1_update": result.b1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


def _audit_to_dict(audit: LorentzianAudit) -> dict[str, object]:
    return {
        "case_id": audit.case_id,
        "classification": audit.classification,
        "residue_label": audit.residue_label,
        "taf_adds_independent_content": audit.taf_adds_independent_content,
        "lorentzian_data_matched": audit.lorentzian_data_matched,
        "capability_split": audit.capability_split,
        "causal_relation": audit.causal_relation,
        "domain_of_dependence_status": audit.domain_of_dependence_status,
        "reason": audit.reason,
        "weakened_claim": audit.weakened_claim,
        "required_next": audit.required_next,
    }


def _failed_fixture(case_id: str) -> LorentzianAudit:
    return LorentzianAudit(
        case_id=case_id,
        classification="failed_fixture",
        residue_label="invalid_control",
        taf_adds_independent_content=False,
        lorentzian_data_matched=False,
        capability_split=False,
        causal_relation="invalid",
        domain_of_dependence_status="invalid",
        reason="The intended Lorentzian control did not satisfy its setup.",
        weakened_claim="Do not promote a failed control.",
        required_next="Repair the fixture before drawing a claim update.",
    )


if __name__ == "__main__":
    import json

    print(json.dumps(t153_result_to_dict(run_t153_analysis()), indent=2))
