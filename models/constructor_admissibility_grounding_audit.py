"""T124: constructor-admissibility grounding audit for H7.

T18 proves a conditional theorem: if admissible transformations are monotone in
D1, strict finalization has an impossible reverse. T124 asks whether that
admissibility relation is physically grounded in the existing H7 witness
families, or whether it is imported by a resource boundary, coarse-graining,
exported history, hidden environment, or stipulation.
"""

from __future__ import annotations

from dataclasses import dataclass


CONSTRUCTOR_IMPOSSIBLE = "constructor-impossible"
CONSTRUCTOR_ADMISSIBLE = "constructor-admissible possible"
RESOURCE_IMPOSSIBLE = "resource-impossible"
RESOURCE_CONSUMING_POSSIBLE = "resource-consuming possible"
REVERSIBLE_POSSIBLE = "reversible possible"
STOCHASTIC_BALANCED = "stochastic-balanced possible"
COARSE_GRAINED_ONLY = "coarse-grained-only possible"

CONSTRUCTOR_ONLY = "constructor_only"
RESOURCE_ACCOUNTING_ONLY = "resource_accounting_only"
REJECTED_REVERSIBLE = "rejected_reversible"
REJECTED_STATIONARY = "rejected_stationary"


@dataclass(frozen=True)
class TransformationCase:
    case_id: str
    source: str
    forward_edge: str
    d1_delta: str
    accounting_boundary: str
    forward_status: str
    reverse_edge: str
    reverse_status: str
    reverse_blocker: str
    named_resource_or_condition: str
    verdict: str
    reason: str


@dataclass(frozen=True)
class TransformationAudit:
    case_id: str
    source: str
    forward_edge: str
    d1_delta: str
    accounting_boundary: str
    forward_status: str
    reverse_edge: str
    reverse_status: str
    reverse_blocker: str
    named_resource_or_condition: str
    reverse_classified: bool
    strict_forward_increase: bool
    permits_unqualified_physical_arrow: bool
    permits_constructor_reading: bool
    permits_resource_accounting_reading: bool
    verdict: str
    reason: str


@dataclass(frozen=True)
class T124Result:
    audits: tuple[TransformationAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def transformation_cases() -> tuple[TransformationCase, ...]:
    return (
        TransformationCase(
            case_id="t18_constructor_rule",
            source="T18",
            forward_edge="less finalized record -> more finalized record",
            d1_delta="strict increase by premise",
            accounting_boundary="formal admissibility relation",
            forward_status=CONSTRUCTOR_ADMISSIBLE,
            reverse_edge="more finalized record -> less finalized record",
            reverse_status=CONSTRUCTOR_IMPOSSIBLE,
            reverse_blocker="reverse is excluded by the D1-monotone admissibility rule",
            named_resource_or_condition="constructor admissibility premise",
            verdict=CONSTRUCTOR_ONLY,
            reason=(
                "This is a valid conditional theorem, but it does not ground the "
                "premise in substrate physics."
            ),
        ),
        TransformationCase(
            case_id="t80_reversible_window_definalization",
            source="T80",
            forward_edge="Rule-30 reversible physical step with raw window D1 decrease",
            d1_delta="decrease, not strict finalization",
            accounting_boundary="closed reversible second-order cellular automaton",
            forward_status=REVERSIBLE_POSSIBLE,
            reverse_edge="direct inverse second-order CA step",
            reverse_status=REVERSIBLE_POSSIBLE,
            reverse_blocker="none when the full reversible state is included",
            named_resource_or_condition="none",
            verdict=REJECTED_REVERSIBLE,
            reason=(
                "Raw physical steps cannot be identified with T18 admissible "
                "steps; the inverse exists in the same accounted substrate."
            ),
        ),
        TransformationCase(
            case_id="t84_cyclic_export_accounting",
            source="T84",
            forward_edge="cyclic memory overwrite plus exported overwritten slot",
            d1_delta="strict accounted-support increase",
            accounting_boundary="local ring plus exported history channel",
            forward_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_edge="restore prior ring and unexport the overwritten slot",
            reverse_status=REVERSIBLE_POSSIBLE,
            reverse_blocker="blocked only if exported history or heat-bath channel is excluded",
            named_resource_or_condition="exported history or erasure channel",
            verdict=RESOURCE_ACCOUNTING_ONLY,
            reason=(
                "The monotone lives in exported history or erasure accounting, "
                "not in autonomous cyclic memory."
            ),
        ),
        TransformationCase(
            case_id="t106_bounded_sink_forward_branch",
            source="T106",
            forward_edge="ordered export into a bounded blank sink",
            d1_delta="strict forward-branch accounted-support increase",
            accounting_boundary="ring memory plus finite sink, before unwind",
            forward_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_edge="reversible unwind after including the sink state",
            reverse_status=REVERSIBLE_POSSIBLE,
            reverse_blocker="blocked only while the sink return path is omitted",
            named_resource_or_condition="finite blank sink capacity and excluded return path",
            verdict=RESOURCE_ACCOUNTING_ONLY,
            reason=(
                "The forward branch is monotone while sink capacity is consumed; "
                "the closed bounded cycle has a return-path decrease."
            ),
        ),
        TransformationCase(
            case_id="t110_closed_permutation_orbit",
            source="T110",
            forward_edge="putative scalar increase along a finite permutation edge",
            d1_delta="cannot be globally nondecreasing and strict on a closed orbit",
            accounting_boundary="closed finite reversible state space",
            forward_status=REVERSIBLE_POSSIBLE,
            reverse_edge="later edge on the same finite orbit returns to the start",
            reverse_status=REVERSIBLE_POSSIBLE,
            reverse_blocker="none inside the closed permutation orbit",
            named_resource_or_condition="none",
            verdict=REJECTED_REVERSIBLE,
            reason=(
                "A strict scalar monotone on a finite closed orbit is impossible "
                "unless some edge decreases or a boundary is omitted."
            ),
        ),
        TransformationCase(
            case_id="t116_open_export_recorder",
            source="T116",
            forward_edge="append/export a record through an open recorder",
            d1_delta="strict accounted-record increase",
            accounting_boundary="system plus exported history and path irreversibility",
            forward_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_edge="erase or unexport the record through the environment",
            reverse_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_blocker=(
                "requires reversing path irreversibility or paying the erasure/export account"
            ),
            named_resource_or_condition="path log-ratio, exported history, or fresh blank capacity",
            verdict=RESOURCE_ACCOUNTING_ONLY,
            reason=(
                "The arrow is absorbed by standard stochastic thermodynamics "
                "or capacity/export accounting."
            ),
        ),
        TransformationCase(
            case_id="t122_stationary_markov_upward_move",
            source="T122",
            forward_edge="upward score transition inside stationary support",
            d1_delta="local increase balanced by downward drift elsewhere",
            accounting_boundary="finite Markov chain at stationary distribution",
            forward_status=STOCHASTIC_BALANCED,
            reverse_edge="stationary-support downward or balancing transitions",
            reverse_status=STOCHASTIC_BALANCED,
            reverse_blocker="none; stationarity forces zero weighted drift",
            named_resource_or_condition="none",
            verdict=REJECTED_STATIONARY,
            reason=(
                "A positive-looking stochastic move is not a scalar finality "
                "arrow on stationary support; stationarity forces zero "
                "weighted drift."
            ),
        ),
        TransformationCase(
            case_id="t128_resource_drawdown",
            source="T128",
            forward_edge="R3 -> R2 -> R1 -> R0 finite resource consumption",
            d1_delta="strict drawdown increase",
            accounting_boundary="finite nonrenewed capacity with depleted boundary",
            forward_status=RESOURCE_CONSUMING_POSSIBLE,
            reverse_edge="R0 -> R1 -> R2 -> R3 refill path",
            reverse_status=RESOURCE_IMPOSSIBLE,
            reverse_blocker="requires an external refill resource or boundary reset",
            named_resource_or_condition="finite nonrenewed capacity",
            verdict=RESOURCE_ACCOUNTING_ONLY,
            reason=(
                "This is the strongest non-stipulative finite survivor, but it "
                "is resource drawdown rather than a new thermodynamic arrow."
            ),
        ),
        TransformationCase(
            case_id="t128_constructor_restricted",
            source="T128",
            forward_edge="C0 -> C1 -> C2 allowed constructor steps",
            d1_delta="strict constructor-rank increase",
            accounting_boundary="declared constructor admissibility relation",
            forward_status=CONSTRUCTOR_ADMISSIBLE,
            reverse_edge="C2 -> C1 -> C0",
            reverse_status=CONSTRUCTOR_IMPOSSIBLE,
            reverse_blocker="reverse transformations are stipulated inadmissible",
            named_resource_or_condition="excluded reverse channel",
            verdict=CONSTRUCTOR_ONLY,
            reason=(
                "This survives formally, but its direction is imported by the "
                "admissibility relation."
            ),
        ),
    )


def audit_case(case: TransformationCase) -> TransformationAudit:
    strict_forward_increase = case.d1_delta.startswith("strict")
    reverse_classified = bool(case.reverse_edge and case.reverse_status)
    permits_constructor = (
        strict_forward_increase
        and case.reverse_status == CONSTRUCTOR_IMPOSSIBLE
        and case.verdict == CONSTRUCTOR_ONLY
    )
    permits_resource = (
        strict_forward_increase
        and case.verdict == RESOURCE_ACCOUNTING_ONLY
        and case.named_resource_or_condition != "none"
    )
    permits_unqualified = False
    return TransformationAudit(
        case_id=case.case_id,
        source=case.source,
        forward_edge=case.forward_edge,
        d1_delta=case.d1_delta,
        accounting_boundary=case.accounting_boundary,
        forward_status=case.forward_status,
        reverse_edge=case.reverse_edge,
        reverse_status=case.reverse_status,
        reverse_blocker=case.reverse_blocker,
        named_resource_or_condition=case.named_resource_or_condition,
        reverse_classified=reverse_classified,
        strict_forward_increase=strict_forward_increase,
        permits_unqualified_physical_arrow=permits_unqualified,
        permits_constructor_reading=permits_constructor,
        permits_resource_accounting_reading=permits_resource,
        verdict=case.verdict,
        reason=case.reason,
    )


def run_t124_analysis() -> T124Result:
    audits = tuple(audit_case(case) for case in transformation_cases())
    _validate_audits(audits)
    return T124Result(
        audits=audits,
        strongest_claim=(
            "H7 can be used only as an audited admissibility ledger: every "
            "strict D1-increasing edge must classify the reverse edge under the "
            "same accounting boundary. Current witnesses permit only "
            "constructor-only or resource-accounting readings, never an "
            "unqualified physical arrow."
        ),
        improved=(
            "T124 turns the T18 admissibility premise into a checkable ledger. "
            "It records whether each candidate arrow is blocked by constructor "
            "impossibility, finite resource depletion, exported history, "
            "erasure, omitted return path, or stationarity/reversibility controls."
        ),
        weakened=(
            "No existing H7 witness grounds a new thermodynamic arrow. The "
            "best non-stipulative survivor is T128 resource drawdown; the formal "
            "constructor survivor works only by excluding the reverse by rule."
        ),
        falsification_condition=(
            "T124 is falsified, and H7 could strengthen, by a finite or "
            "physically calibrated record substrate with a strict D1-increasing "
            "edge whose reverse is constructor-impossible under the same full "
            "state accounting, without relying on omitted environment, sink "
            "capacity, erasure, postselection, coarse-graining, stationarity "
            "violation, or stipulated admissibility."
        ),
        h7_update=(
            "Add T124 to H7 as the reverse-edge grounding gate. H7 should not "
            "be read physically unless the reverse edge is audited under the "
            "same substrate and its impossibility or resource boundary is named."
        ),
        claim_ledger_update=(
            "H7 remains partially supported only as a constructor/resource "
            "accounting lemma. T124 audits the reverse edge for T18, T80, T84, "
            "T106, T110, T116, T122, and T128-style cases. All strict surviving "
            "edges are either resource/accounting edges or constructor-only "
            "stipulations; reversible and stationary controls reject any "
            "unqualified physical-arrow reading."
        ),
        open_blocker=(
            "The missing upgrade is a physically grounded constructor-"
            "impossibility relation for record deletion or definalization that "
            "does not reduce to ordinary resource, entropy, boundary, or "
            "coarse-graining accounting."
        ),
        suggested_next=(
            "Either thermodynamically calibrate the T128 resource drawdown "
            "fixture against standard free-energy/capacity accounting, or move "
            "expected value to T127 LossKernel prior-art separation."
        ),
    )


def t124_result_to_dict(result: T124Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


def _validate_audits(audits: tuple[TransformationAudit, ...]) -> None:
    if not audits:
        raise ValueError("T124 requires at least one transformation audit")
    case_ids = tuple(audit.case_id for audit in audits)
    if len(set(case_ids)) != len(case_ids):
        raise ValueError("duplicate T124 case ids")
    for audit in audits:
        if audit.strict_forward_increase and not audit.reverse_classified:
            raise ValueError(f"{audit.case_id} has no reverse-edge classification")
        if audit.permits_unqualified_physical_arrow:
            raise AssertionError(f"{audit.case_id} promoted an unqualified arrow")


def _audit_to_dict(audit: TransformationAudit) -> dict[str, object]:
    return {
        "case_id": audit.case_id,
        "source": audit.source,
        "forward_edge": audit.forward_edge,
        "d1_delta": audit.d1_delta,
        "accounting_boundary": audit.accounting_boundary,
        "forward_status": audit.forward_status,
        "reverse_edge": audit.reverse_edge,
        "reverse_status": audit.reverse_status,
        "reverse_blocker": audit.reverse_blocker,
        "named_resource_or_condition": audit.named_resource_or_condition,
        "reverse_classified": audit.reverse_classified,
        "strict_forward_increase": audit.strict_forward_increase,
        "permits_unqualified_physical_arrow": (
            audit.permits_unqualified_physical_arrow
        ),
        "permits_constructor_reading": audit.permits_constructor_reading,
        "permits_resource_accounting_reading": (
            audit.permits_resource_accounting_reading
        ),
        "verdict": audit.verdict,
        "reason": audit.reason,
    }
