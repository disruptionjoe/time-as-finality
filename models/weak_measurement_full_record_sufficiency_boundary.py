"""T139: full-record sufficiency boundary for weak-measurement second meters.

This model closes a remaining Q1C loophole. A proposed second meter can look
branch-sensitive only because the "ordinary monitored record" was fixed too
coarsely. If the second meter is screened off by the full event-level monitored
record, then it does not supply an independent TaF axis even when it refines a
coarse dashboard or summary exported from that record.
"""

from __future__ import annotations

from dataclasses import dataclass


BRANCHES = ("branch_0", "branch_1")
FULL_RECORDS = ("x0", "x1")
SECOND_METER_OUTCOMES = ("cold", "hot")


@dataclass(frozen=True)
class FullRecordScenario:
    name: str
    full_record_channel: dict[str, dict[str, float]]
    coarse_summary_map: dict[str, str]
    second_meter_channel: dict[str, dict[str, dict[str, float]]]
    purpose: str


@dataclass(frozen=True)
class FullRecordAudit:
    scenario_name: str
    classification: str
    screened_off_by_full_record: bool
    screened_off_by_coarse_summary: bool
    fixed_coarse_summary_split_exists: bool
    fixed_full_record_split_exists: bool
    witness_summary: str | None
    witness_full_record: str | None
    interpretation: str


@dataclass(frozen=True)
class T139Result:
    audits: tuple[FullRecordAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    blocker: str
    recommended_next: str


def canonical_scenarios() -> tuple[FullRecordScenario, ...]:
    coarse_summary_loophole = FullRecordScenario(
        name="coarse_summary_refinement_only",
        full_record_channel={
            "branch_0": {"x0": 0.9, "x1": 0.1},
            "branch_1": {"x0": 0.1, "x1": 0.9},
        },
        coarse_summary_map={"x0": "mid", "x1": "mid"},
        second_meter_channel={
            branch: {
                "x0": {"cold": 1.0, "hot": 0.0},
                "x1": {"cold": 0.0, "hot": 1.0},
            }
            for branch in BRANCHES
        },
        purpose=(
            "The second meter only refines a deliberately coarsened ordinary log. "
            "It appears branch-sensitive if one fixes the coarse summary, but not "
            "if one fixes the full event-level monitored record."
        ),
    )
    full_record_downstream = FullRecordScenario(
        name="full_record_downstream_meter",
        full_record_channel={
            "branch_0": {"x0": 0.7, "x1": 0.3},
            "branch_1": {"x0": 0.4, "x1": 0.6},
        },
        coarse_summary_map={"x0": "low", "x1": "high"},
        second_meter_channel={
            branch: {
                "x0": {"cold": 0.95, "hot": 0.05},
                "x1": {"cold": 0.05, "hot": 0.95},
            }
            for branch in BRANCHES
        },
        purpose=(
            "The second meter is a downstream transform of the full standard record. "
            "It is null even before any coarse-summary loophole is considered."
        ),
    )
    branch_sensitive_escape = FullRecordScenario(
        name="branch_sensitive_extra_meter",
        full_record_channel={
            "branch_0": {"x0": 0.5, "x1": 0.5},
            "branch_1": {"x0": 0.5, "x1": 0.5},
        },
        coarse_summary_map={"x0": "mid", "x1": "mid"},
        second_meter_channel={
            "branch_0": {
                "x0": {"cold": 0.9, "hot": 0.1},
                "x1": {"cold": 0.9, "hot": 0.1},
            },
            "branch_1": {
                "x0": {"cold": 0.1, "hot": 0.9},
                "x1": {"cold": 0.1, "hot": 0.9},
            },
        },
        purpose=(
            "Logical escape witness: the second meter remains branch-sensitive even "
            "after the full standard record is fixed, so it cannot be dismissed as "
            "mere refinement of the ordinary log."
        ),
    )
    return (coarse_summary_loophole, full_record_downstream, branch_sensitive_escape)


def _probability_of_summary_given_branch(
    scenario: FullRecordScenario,
    branch: str,
    summary: str,
) -> float:
    return sum(
        probability
        for record, probability in scenario.full_record_channel[branch].items()
        if scenario.coarse_summary_map[record] == summary
    )


def _hot_probability_given_summary(
    scenario: FullRecordScenario,
    branch: str,
    summary: str,
) -> float | None:
    summary_probability = _probability_of_summary_given_branch(scenario, branch, summary)
    if summary_probability == 0.0:
        return None
    hot_probability = 0.0
    for record, probability in scenario.full_record_channel[branch].items():
        if scenario.coarse_summary_map[record] != summary:
            continue
        hot_probability += (
            probability / summary_probability
        ) * scenario.second_meter_channel[branch][record]["hot"]
    return round(hot_probability, 12)


def is_screened_off_by_full_record(scenario: FullRecordScenario) -> bool:
    for record in FULL_RECORDS:
        reference = None
        for branch in BRANCHES:
            if scenario.full_record_channel[branch][record] == 0.0:
                continue
            conditional = scenario.second_meter_channel[branch][record]
            if reference is None:
                reference = conditional
                continue
            for outcome in SECOND_METER_OUTCOMES:
                if abs(reference[outcome] - conditional[outcome]) > 1e-12:
                    return False
    return True


def is_screened_off_by_coarse_summary(scenario: FullRecordScenario) -> bool:
    summaries = tuple(dict.fromkeys(scenario.coarse_summary_map.values()))
    for summary in summaries:
        reference = None
        for branch in BRANCHES:
            hot_probability = _hot_probability_given_summary(scenario, branch, summary)
            if hot_probability is None:
                continue
            if reference is None:
                reference = hot_probability
                continue
            if abs(reference - hot_probability) > 1e-12:
                return False
    return True


def fixed_summary_split_witness(scenario: FullRecordScenario) -> tuple[str | None, bool]:
    summaries = tuple(dict.fromkeys(scenario.coarse_summary_map.values()))
    for summary in summaries:
        left = _hot_probability_given_summary(scenario, "branch_0", summary)
        right = _hot_probability_given_summary(scenario, "branch_1", summary)
        if left is None or right is None:
            continue
        if abs(left - right) > 1e-12:
            return summary, True
    return None, False


def fixed_full_record_split_witness(scenario: FullRecordScenario) -> tuple[str | None, bool]:
    for record in FULL_RECORDS:
        if any(scenario.full_record_channel[branch][record] == 0.0 for branch in BRANCHES):
            continue
        left = scenario.second_meter_channel["branch_0"][record]["hot"]
        right = scenario.second_meter_channel["branch_1"][record]["hot"]
        if abs(left - right) > 1e-12:
            return record, True
    return None, False


def classify_scenario(scenario: FullRecordScenario) -> FullRecordAudit:
    screened_by_full = is_screened_off_by_full_record(scenario)
    screened_by_coarse = is_screened_off_by_coarse_summary(scenario)
    witness_summary, coarse_split_exists = fixed_summary_split_witness(scenario)
    witness_full, full_split_exists = fixed_full_record_split_witness(scenario)

    if screened_by_full and coarse_split_exists:
        classification = "null_coarse_summary_loophole"
        interpretation = (
            "The second meter only beats an underspecified ordinary record. Once the "
            "full event-level monitored transcript is fixed, the apparent branch split vanishes."
        )
    elif screened_by_full:
        classification = "null_full_record_downstream"
        interpretation = (
            "The second meter is screened off even by the full standard record. It is "
            "a downstream readout variant, not an independent TaF axis."
        )
    elif full_split_exists:
        classification = "candidate_full_record_escape"
        interpretation = (
            "The second meter remains branch-sensitive after the full monitored record "
            "is fixed. This is the minimum structural escape class for Q1C."
        )
    else:
        classification = "indeterminate_non_screened_case"
        interpretation = (
            "The second meter is not screened off by the full record, but this witness "
            "family still does not produce a fixed-full-record branch split."
        )

    return FullRecordAudit(
        scenario_name=scenario.name,
        classification=classification,
        screened_off_by_full_record=screened_by_full,
        screened_off_by_coarse_summary=screened_by_coarse,
        fixed_coarse_summary_split_exists=coarse_split_exists,
        fixed_full_record_split_exists=full_split_exists,
        witness_summary=witness_summary,
        witness_full_record=witness_full,
        interpretation=interpretation,
    )


def run_t139_analysis() -> T139Result:
    audits = tuple(classify_scenario(scenario) for scenario in canonical_scenarios())
    return T139Result(
        audits=audits,
        strongest_claim=(
            "Q1C must hold fixed the full event-level ordinary monitored record, not a "
            "coarsened summary of it. A second meter that only refines an underspecified "
            "standard log is null even if it appears branch-sensitive at the summary level."
        ),
        improved=(
            "T139 closes a remaining loophole between T132 and T137: future weak-measurement "
            "proposals must now show independence from the full standard trajectory record, "
            "not merely from a plotted average, dashboard summary, or thresholded export."
        ),
        weakened=(
            "This weakens any rescue that keeps 'ordinary monitored statistics fixed' only at a "
            "coarse level. A same-summary split is not enough if the full event-level log already "
            "screens off the auxiliary meter."
        ),
        falsification_condition=(
            "T139 fails if a second meter that is conditionally determined by the full event-level "
            "ordinary monitored record can still produce a pre-registered fixed-full-record TaF verdict split."
        ),
        q1c_update=(
            "Q1C remains dormant. Strengthen the gate again: the ordinary monitored statistics held "
            "fixed must be the full pre-registered event-level standard record, not a coarsened summary "
            "that an auxiliary meter merely refines."
        ),
        blocker=(
            "No named monitored-qubit platform in the repo currently supplies an auxiliary meter that "
            "provably escapes screening-off by the full event-level standard trajectory record."
        ),
        recommended_next=(
            "Search only for a dual-meter protocol whose auxiliary channel remains verdict-changing after "
            "conditioning on the complete ordinary monitored transcript."
        ),
    )


def t139_result_to_dict(result: T139Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "scenario_name": audit.scenario_name,
                "classification": audit.classification,
                "screened_off_by_full_record": audit.screened_off_by_full_record,
                "screened_off_by_coarse_summary": audit.screened_off_by_coarse_summary,
                "fixed_coarse_summary_split_exists": audit.fixed_coarse_summary_split_exists,
                "fixed_full_record_split_exists": audit.fixed_full_record_split_exists,
                "witness_summary": audit.witness_summary,
                "witness_full_record": audit.witness_full_record,
                "interpretation": audit.interpretation,
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
