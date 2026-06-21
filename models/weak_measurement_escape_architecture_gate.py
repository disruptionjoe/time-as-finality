"""T146: architecture gate for weak-measurement Q1C escape proposals.

T139 and T143 jointly imply that Q1C should no longer ask only whether a
"second meter" exists. The relevant filter is architectural: what kind of
auxiliary channel is being proposed relative to the full ordinary event log and
the declared monitored instrument?
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Q1CArchitectureInput:
    full_event_standard_record_fixed: bool
    auxiliary_screened_off_by_full_record: bool
    auxiliary_is_proxy_or_postselected: bool
    same_declared_instrument: bool
    captures_extra_environment_structure: bool
    explicitly_enlarges_instrument: bool
    preserved_comparison_target_declared: bool
    verdict_changes: bool


@dataclass(frozen=True)
class Q1CArchitectureAudit:
    name: str
    classification: str
    active_route: bool
    reason: str
    required_next: str


@dataclass(frozen=True)
class T146Result:
    audits: tuple[Q1CArchitectureAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    blocker: str
    recommended_next: str


def classify_architecture(case: Q1CArchitectureInput, *, name: str) -> Q1CArchitectureAudit:
    if not case.full_event_standard_record_fixed:
        return Q1CArchitectureAudit(
            name=name,
            classification="null_coarse_standard_record",
            active_route=False,
            reason=(
                "The proposal does not hold fixed the full pre-registered ordinary "
                "event log, so it falls to the T139 coarse-record loophole."
            ),
            required_next="Condition on the full event-level ordinary monitored transcript.",
        )
    if case.auxiliary_screened_off_by_full_record:
        return Q1CArchitectureAudit(
            name=name,
            classification="null_screened_off_by_full_record",
            active_route=False,
            reason=(
                "Once the full ordinary transcript is fixed, the auxiliary channel "
                "carries no extra verdict-bearing content."
            ),
            required_next="Show an auxiliary axis that survives full-record conditioning.",
        )
    if case.auxiliary_is_proxy_or_postselected:
        return Q1CArchitectureAudit(
            name=name,
            classification="null_proxy_or_postselection",
            active_route=False,
            reason=(
                "The proposed axis is a schedule proxy or success-conditioned readout, "
                "not an independently calibrated event-level meter."
            ),
            required_next="Replace the proxy with a calibrated pre-analysis auxiliary channel.",
        )
    if case.same_declared_instrument and not case.captures_extra_environment_structure:
        return Q1CArchitectureAudit(
            name=name,
            classification="null_same_instrument_default",
            active_route=False,
            reason=(
                "The proposal stays inside the same declared monitored instrument and "
                "names no extra environment or detector structure beyond the full "
                "ordinary transcript."
            ),
            required_next=(
                "Either tie the auxiliary channel to extra environment structure or "
                "declare an explicit instrument enlargement."
            ),
        )
    if case.explicitly_enlarges_instrument and not case.preserved_comparison_target_declared:
        return Q1CArchitectureAudit(
            name=name,
            classification="underdeclared_instrument_enlargement",
            active_route=False,
            reason=(
                "The proposal changes the monitored instrument but does not pre-declare "
                "what fixed-standard comparison is still meant to survive."
            ),
            required_next="State the enlarged instrument and preserved comparison target in advance.",
        )
    if not case.verdict_changes:
        return Q1CArchitectureAudit(
            name=name,
            classification="independent_but_not_decisive",
            active_route=False,
            reason=(
                "The auxiliary channel is not screened off, but it still does not "
                "change the admissible TaF verdict."
            ),
            required_next="Show a verdict split under the fixed-record comparison.",
        )
    if case.captures_extra_environment_structure and not case.explicitly_enlarges_instrument:
        return Q1CArchitectureAudit(
            name=name,
            classification="candidate_extra_environment_escape",
            active_route=True,
            reason=(
                "This is a live Q1C escape class: the auxiliary channel is tied to "
                "extra environment or detector structure that survives full-record "
                "conditioning and changes the verdict."
            ),
            required_next="Tie the extra environment structure to a named monitored-qubit platform.",
        )
    if case.explicitly_enlarges_instrument and case.preserved_comparison_target_declared:
        return Q1CArchitectureAudit(
            name=name,
            classification="candidate_enlarged_instrument_escape",
            active_route=True,
            reason=(
                "This is a live Q1C escape class: the proposal openly enlarges the "
                "instrument and declares the comparison target it claims to preserve."
            ),
            required_next="Write the enlarged-instrument protocol and audit the preserved comparison.",
        )
    return Q1CArchitectureAudit(
        name=name,
        classification="underdescribed_architecture",
        active_route=False,
        reason="The proposal does not yet specify enough architecture detail to be evaluated honestly.",
        required_next="Declare record, instrument, auxiliary channel, and verdict role precisely.",
    )


def canonical_architectures() -> tuple[tuple[str, Q1CArchitectureInput], ...]:
    return (
        (
            "coarse_record_only",
            Q1CArchitectureInput(
                full_event_standard_record_fixed=False,
                auxiliary_screened_off_by_full_record=False,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=True,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                verdict_changes=True,
            ),
        ),
        (
            "screened_off_by_full_record",
            Q1CArchitectureInput(
                full_event_standard_record_fixed=True,
                auxiliary_screened_off_by_full_record=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=True,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                verdict_changes=True,
            ),
        ),
        (
            "proxy_or_postselected",
            Q1CArchitectureInput(
                full_event_standard_record_fixed=True,
                auxiliary_screened_off_by_full_record=False,
                auxiliary_is_proxy_or_postselected=True,
                same_declared_instrument=False,
                captures_extra_environment_structure=True,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                verdict_changes=True,
            ),
        ),
        (
            "same_instrument_default_null",
            Q1CArchitectureInput(
                full_event_standard_record_fixed=True,
                auxiliary_screened_off_by_full_record=False,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=True,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                verdict_changes=True,
            ),
        ),
        (
            "extra_environment_candidate",
            Q1CArchitectureInput(
                full_event_standard_record_fixed=True,
                auxiliary_screened_off_by_full_record=False,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=False,
                captures_extra_environment_structure=True,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                verdict_changes=True,
            ),
        ),
        (
            "enlarged_instrument_candidate",
            Q1CArchitectureInput(
                full_event_standard_record_fixed=True,
                auxiliary_screened_off_by_full_record=False,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=False,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=True,
                preserved_comparison_target_declared=True,
                verdict_changes=True,
            ),
        ),
    )


def current_frontier_case() -> tuple[str, Q1CArchitectureInput]:
    return (
        "current_frontier",
        Q1CArchitectureInput(
            full_event_standard_record_fixed=True,
            auxiliary_screened_off_by_full_record=False,
            auxiliary_is_proxy_or_postselected=False,
            same_declared_instrument=True,
            captures_extra_environment_structure=False,
            explicitly_enlarges_instrument=False,
            preserved_comparison_target_declared=False,
            verdict_changes=False,
        ),
    )


def run_t146_analysis() -> T146Result:
    audits = tuple(
        classify_architecture(case, name=name) for name, case in canonical_architectures()
    )
    current_name, current_case = current_frontier_case()
    current_audit = classify_architecture(current_case, name=current_name)
    audits = audits + (current_audit,)
    return T146Result(
        audits=audits,
        strongest_claim=(
            "After T139 and T143, only two live Q1C architecture classes remain: "
            "an auxiliary channel tied to extra environment structure that survives "
            "full-record conditioning, or an openly enlarged instrument with a "
            "pre-declared preserved comparison target. Same-instrument auxiliary "
            "hardware is null by default."
        ),
        improved=(
            "T146 converts the post-T143 prose into an executable architecture gate. "
            "Future weak-measurement proposals can now be rejected before any "
            "literature or toy-model effort if they do not fit one of the two live "
            "escape classes."
        ),
        weakened=(
            "This weakens the generic 'second meter' route further. Hardware "
            "distinctness, unscreened rhetoric, and undeclared instrument changes no "
            "longer count as progress."
        ),
        falsification_condition=(
            "T146 fails if a same-declared-instrument auxiliary channel with no extra "
            "environment handle and no explicit instrument enlargement still yields a "
            "pre-registered verdict-changing axis that survives the full-record gate."
        ),
        q1c_update=(
            "Q1C remains dormant. Filter future proposals by architecture first: only "
            "extra-environment channels or explicitly enlarged instruments with a "
            "declared preserved comparison target remain live."
        ),
        blocker=(
            "The repo still has no named monitored-qubit platform in either live "
            "escape class."
        ),
        recommended_next=(
            "Stop generic second-meter searches. Search only for a platform with an "
            "unscreened extra-environment channel or for an explicit enlarged-"
            "instrument protocol that states its preserved comparison target."
        ),
    )


def t146_result_to_dict(result: T146Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "name": audit.name,
                "classification": audit.classification,
                "active_route": audit.active_route,
                "reason": audit.reason,
                "required_next": audit.required_next,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1c_update": result.q1c_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t146_result_to_dict(run_t146_analysis()), indent=2))
