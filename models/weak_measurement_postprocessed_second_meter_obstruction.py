"""T137: downstream second-meter obstruction for weak measurement.

This model isolates one sharp failure mode for Q1C.

Suppose a standard monitored record Y is already fixed, and a proposed second
meter Z is generated only by a downstream classical kernel K(Z|Y). Then Z is
screened off by Y: no branch-sensitive split survives once the ordinary record
is held fixed. A simultaneous meter only helps if it is not conditionally
determined by the ordinary monitored record.
"""

from __future__ import annotations

from dataclasses import dataclass


BRANCHES = ("branch_0", "branch_1")
RECORDS = ("low", "high")
SECOND_METER_OUTCOMES = ("cold", "hot")


@dataclass(frozen=True)
class DualMeterScenario:
    name: str
    monitored_channel: dict[str, dict[str, float]]
    second_meter_channel: dict[str, dict[str, dict[str, float]]]
    purpose: str


@dataclass(frozen=True)
class SecondMeterAudit:
    scenario_name: str
    classification: str
    postprocessed_from_standard_record: bool
    fixed_record_split_exists: bool
    witness_record: str | None
    witness_gap: float
    interpretation: str


@dataclass(frozen=True)
class T137Result:
    audits: tuple[SecondMeterAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    blocker: str
    recommended_next: str


def canonical_scenarios() -> tuple[DualMeterScenario, ...]:
    monitored_channel = {
        "branch_0": {"low": 0.8, "high": 0.2},
        "branch_1": {"low": 0.2, "high": 0.8},
    }
    exact_copy = {
        branch: {
            "low": {"cold": 1.0, "hot": 0.0},
            "high": {"cold": 0.0, "hot": 1.0},
        }
        for branch in BRANCHES
    }
    noisy_copy = {
        branch: {
            "low": {"cold": 0.9, "hot": 0.1},
            "high": {"cold": 0.1, "hot": 0.9},
        }
        for branch in BRANCHES
    }
    latent_independent_meter = {
        "branch_0": {
            "low": {"cold": 0.9, "hot": 0.1},
            "high": {"cold": 0.9, "hot": 0.1},
        },
        "branch_1": {
            "low": {"cold": 0.1, "hot": 0.9},
            "high": {"cold": 0.1, "hot": 0.9},
        },
    }
    return (
        DualMeterScenario(
            name="exact_duplicate_meter",
            monitored_channel=monitored_channel,
            second_meter_channel=exact_copy,
            purpose=(
                "Positive control: the second meter is an exact copy of the "
                "ordinary monitored record."
            ),
        ),
        DualMeterScenario(
            name="noisy_downstream_meter",
            monitored_channel=monitored_channel,
            second_meter_channel=noisy_copy,
            purpose=(
                "The second meter is physically distinct but only a noisy "
                "downstream transform of the ordinary monitored record."
            ),
        ),
        DualMeterScenario(
            name="branch_sensitive_independent_meter",
            monitored_channel=monitored_channel,
            second_meter_channel=latent_independent_meter,
            purpose=(
                "Escape witness: the second meter depends on the latent branch "
                "rather than being screened off by the ordinary record."
            ),
        ),
    )


def is_postprocessed_from_standard_record(scenario: DualMeterScenario) -> bool:
    for record in RECORDS:
        reference = None
        for branch in BRANCHES:
            if scenario.monitored_channel[branch][record] == 0.0:
                continue
            conditional = scenario.second_meter_channel[branch][record]
            if reference is None:
                reference = conditional
                continue
            for outcome in SECOND_METER_OUTCOMES:
                if abs(reference[outcome] - conditional[outcome]) > 1e-12:
                    return False
    return True


def fixed_record_split_witness(
    scenario: DualMeterScenario,
) -> tuple[str | None, float]:
    best_record = None
    best_gap = 0.0
    for record in RECORDS:
        if any(scenario.monitored_channel[branch][record] == 0.0 for branch in BRANCHES):
            continue
        low = scenario.second_meter_channel["branch_0"][record]["hot"]
        high = scenario.second_meter_channel["branch_1"][record]["hot"]
        gap = abs(low - high)
        if gap > best_gap:
            best_record = record
            best_gap = gap
    return best_record, round(best_gap, 12)


def classify_scenario(scenario: DualMeterScenario) -> SecondMeterAudit:
    postprocessed = is_postprocessed_from_standard_record(scenario)
    witness_record, witness_gap = fixed_record_split_witness(scenario)
    split_exists = witness_gap > 0.0

    if postprocessed:
        classification = "null_downstream_transform"
        interpretation = (
            "Once the ordinary monitored record is fixed, the second meter adds "
            "no branch-sensitive information. Physical distinctness alone is null."
        )
    elif split_exists:
        classification = "candidate_branch_sensitive_second_meter"
        interpretation = (
            "The second meter is not screened off by the ordinary record and can, "
            "in principle, distinguish branches while the monitored record is fixed."
        )
    else:
        classification = "no_fixed_record_split"
        interpretation = (
            "The second meter is not a pure downstream transform, but this witness "
            "family still does not produce a fixed-record branch split."
        )

    return SecondMeterAudit(
        scenario_name=scenario.name,
        classification=classification,
        postprocessed_from_standard_record=postprocessed,
        fixed_record_split_exists=split_exists,
        witness_record=witness_record if split_exists else None,
        witness_gap=witness_gap,
        interpretation=interpretation,
    )


def run_t137_analysis() -> T137Result:
    audits = tuple(classify_scenario(scenario) for scenario in canonical_scenarios())
    return T137Result(
        audits=audits,
        strongest_claim=(
            "A simultaneous second meter does not reopen Q1C when it is only a "
            "downstream classical transform of the standard monitored record. "
            "Conditioned on the ordinary record, such a meter cannot produce the "
            "branch-sensitive split that Q1C requires."
        ),
        improved=(
            "T137 upgrades the vague phrase 'independent second meter' into a "
            "conditional-independence test. The repo can now reject physically "
            "distinct but downstream-equivalent meters without another literature loop."
        ),
        weakened=(
            "This weakens the softer rescue story that any simultaneous thermal, "
            "calorimetric, or auxiliary channel would help merely by being a second "
            "piece of hardware. If it is screened off by the standard record, it is null."
        ),
        falsification_condition=(
            "T137 fails if a second meter that is demonstrably only a downstream "
            "kernel of the standard monitored record still yields a pre-registered "
            "fixed-record TaF verdict split."
        ),
        q1c_update=(
            "Q1C remains dormant. Add a stronger gate: a proposed simultaneous "
            "second meter is null whenever its statistics are conditionally "
            "determined by the ordinary monitored record."
        ),
        blocker=(
            "The missing object is now sharper than 'any second meter': the repo "
            "needs a branch-sensitive meter that is not screened off by the ordinary "
            "monitoring record and is fixed before analysis."
        ),
        recommended_next=(
            "Search only for monitored-qubit protocols where the auxiliary meter "
            "couples to hidden branch-relevant structure not recoverable from the "
            "ordinary trajectory record or its downstream transforms."
        ),
    )


def t137_result_to_dict(result: T137Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "scenario_name": audit.scenario_name,
                "classification": audit.classification,
                "postprocessed_from_standard_record": audit.postprocessed_from_standard_record,
                "fixed_record_split_exists": audit.fixed_record_split_exists,
                "witness_record": audit.witness_record,
                "witness_gap": audit.witness_gap,
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
