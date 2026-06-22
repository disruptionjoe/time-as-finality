"""T174: forgotten-dims persistence-gap screen.

This module executes MINI-GOAL-TS-002 from the TS persona sprint. It asks
whether non-empty cross-level ``forgotten_dims`` can produce a holonic
persistence gap after all lower-level obstructions have recovered, without an
explicit holonic persistence window.

The screen is intentionally narrow. It does not add lifecycle state or claim
status. It only separates:

* PG relative to the micro level, which can be inherited from meso lag; and
* residual PG after every lower level has recovered, which is the quantity that
  would count as an unscheduled holonic persistence candidate.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PGScenario:
    scenario_id: str
    holonic_rule: str
    micro_start: int = 10
    micro_end: int = 24
    meso_lag: int = 5
    explicit_retention: int = 0
    n_steps: int = 50
    forgotten_dims: tuple[str, ...] = ()


@dataclass(frozen=True)
class PGStep:
    t: int
    micro_obstructed: bool
    meso_obstructed: bool
    holonic_obstructed: bool


@dataclass(frozen=True)
class PGAudit:
    scenario_id: str
    holonic_rule: str
    forgotten_dims: tuple[str, ...]
    micro_last_obstructed: int | None
    meso_last_obstructed: int | None
    lower_last_obstructed: int | None
    holonic_last_obstructed: int | None
    micro_relative_pg: int
    inherited_meso_gap: int
    residual_pg_after_lower_recovery: int
    residual_requires_explicit_retention: bool
    forgotten_dims_alone_generated_residual_pg: bool
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T174Result:
    audits: tuple[PGAudit, ...]
    baseline_residual_pg: int
    no_explicit_residual_pg: int
    no_explicit_micro_relative_pg: int
    strongest_result: str
    governance_signal: str
    claim_ledger_update: str
    suggested_next: str
    not_claimed: str


def generate_pg_trajectory(scenario: PGScenario) -> tuple[PGStep, ...]:
    steps: list[PGStep] = []
    meso_start = scenario.micro_start + scenario.meso_lag
    meso_end = scenario.micro_end + scenario.meso_lag
    lower_end = max(scenario.micro_end, meso_end)

    for t in range(scenario.n_steps):
        micro = scenario.micro_start <= t <= scenario.micro_end
        meso = meso_start <= t <= meso_end
        if scenario.holonic_rule == "scheduled_window":
            holonic = scenario.micro_start <= t <= lower_end + scenario.explicit_retention
        elif scenario.holonic_rule == "propagate_current_lower":
            holonic = micro or meso
        elif scenario.holonic_rule == "explicit_recovery_retention":
            holonic = micro or meso or (lower_end < t <= lower_end + scenario.explicit_retention)
        else:
            raise ValueError(f"unknown holonic_rule: {scenario.holonic_rule}")

        steps.append(
            PGStep(
                t=t,
                micro_obstructed=micro,
                meso_obstructed=meso,
                holonic_obstructed=holonic,
            )
        )

    return tuple(steps)


def audit_pg_scenario(scenario: PGScenario) -> PGAudit:
    trajectory = generate_pg_trajectory(scenario)
    micro_last = _last_obstructed(trajectory, "micro")
    meso_last = _last_obstructed(trajectory, "meso")
    lower_last = max(value for value in (micro_last, meso_last) if value is not None)
    holonic_last = _last_obstructed(trajectory, "holonic")

    micro_pg = _positive_delta(holonic_last, micro_last)
    inherited_gap = _positive_delta(lower_last, micro_last)
    residual_pg = _positive_delta(holonic_last, lower_last)
    residual_requires_retention = residual_pg > 0 and scenario.holonic_rule != "propagate_current_lower"
    forgotten_dims_generated = (
        scenario.holonic_rule == "propagate_current_lower"
        and bool(scenario.forgotten_dims)
        and residual_pg > 0
    )
    verdict = _verdict_for_scenario(scenario, residual_pg, forgotten_dims_generated)

    return PGAudit(
        scenario_id=scenario.scenario_id,
        holonic_rule=scenario.holonic_rule,
        forgotten_dims=scenario.forgotten_dims,
        micro_last_obstructed=micro_last,
        meso_last_obstructed=meso_last,
        lower_last_obstructed=lower_last,
        holonic_last_obstructed=holonic_last,
        micro_relative_pg=micro_pg,
        inherited_meso_gap=inherited_gap,
        residual_pg_after_lower_recovery=residual_pg,
        residual_requires_explicit_retention=residual_requires_retention,
        forgotten_dims_alone_generated_residual_pg=forgotten_dims_generated,
        verdict=verdict,
        interpretation=_interpretation(scenario, micro_pg, inherited_gap, residual_pg, verdict),
    )


def run_t174_analysis() -> T174Result:
    scenarios = (
        PGScenario(
            scenario_id="scheduled_persistence_baseline",
            holonic_rule="scheduled_window",
            explicit_retention=5,
            forgotten_dims=("cross-level-recovery-detail",),
        ),
        PGScenario(
            scenario_id="no_explicit_persistence_with_forgotten_dims",
            holonic_rule="propagate_current_lower",
            forgotten_dims=("cross-level-recovery-detail",),
        ),
        PGScenario(
            scenario_id="no_forgotten_dims_control",
            holonic_rule="propagate_current_lower",
            forgotten_dims=(),
        ),
        PGScenario(
            scenario_id="explicit_recovery_retention_positive_control",
            holonic_rule="explicit_recovery_retention",
            explicit_retention=5,
            forgotten_dims=("cross-level-recovery-detail",),
        ),
    )
    audits = tuple(audit_pg_scenario(scenario) for scenario in scenarios)
    by_id = {audit.scenario_id: audit for audit in audits}
    no_explicit = by_id["no_explicit_persistence_with_forgotten_dims"]

    return T174Result(
        audits=audits,
        baseline_residual_pg=by_id["scheduled_persistence_baseline"].residual_pg_after_lower_recovery,
        no_explicit_residual_pg=no_explicit.residual_pg_after_lower_recovery,
        no_explicit_micro_relative_pg=no_explicit.micro_relative_pg,
        strongest_result=(
            "In this finite screen, non-empty forgotten_dims plus current "
            "lower-level propagation does not generate residual holonic "
            "persistence after all lower levels recover. The apparent PG "
            "relative to micro decomposes into meso inheritance plus any "
            "explicit holonic retention rule."
        ),
        governance_signal=(
            "Flag for future review only: the TS line remains useful as a "
            "diagnostic vocabulary, but PG should not be promoted as a new "
            "invariant unless a future topology screen produces residual PG "
            "without explicit retention or hidden scheduling."
        ),
        claim_ledger_update="None. T174 is a negative boundary screen, not a claim-status change.",
        suggested_next=(
            "Run MINI-GOAL-TS-003 over tree, linear, ring, and dense TTN "
            "topologies using residual PG after lower-level recovery as the "
            "primary metric."
        ),
        not_claimed=(
            "T174 does not prove that no TTN topology can create residual PG, "
            "does not add a recovery operation, and does not change H1, HEF, "
            "or any lifecycle state."
        ),
    )


def t174_result_to_dict(result: T174Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "scenario_id": audit.scenario_id,
                "holonic_rule": audit.holonic_rule,
                "forgotten_dims": list(audit.forgotten_dims),
                "micro_last_obstructed": audit.micro_last_obstructed,
                "meso_last_obstructed": audit.meso_last_obstructed,
                "lower_last_obstructed": audit.lower_last_obstructed,
                "holonic_last_obstructed": audit.holonic_last_obstructed,
                "micro_relative_pg": audit.micro_relative_pg,
                "inherited_meso_gap": audit.inherited_meso_gap,
                "residual_pg_after_lower_recovery": audit.residual_pg_after_lower_recovery,
                "residual_requires_explicit_retention": audit.residual_requires_explicit_retention,
                "forgotten_dims_alone_generated_residual_pg": (
                    audit.forgotten_dims_alone_generated_residual_pg
                ),
                "verdict": audit.verdict,
                "interpretation": audit.interpretation,
            }
            for audit in result.audits
        ],
        "baseline_residual_pg": result.baseline_residual_pg,
        "no_explicit_residual_pg": result.no_explicit_residual_pg,
        "no_explicit_micro_relative_pg": result.no_explicit_micro_relative_pg,
        "strongest_result": result.strongest_result,
        "governance_signal": result.governance_signal,
        "claim_ledger_update": result.claim_ledger_update,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _last_obstructed(trajectory: tuple[PGStep, ...], level: str) -> int | None:
    if level == "micro":
        return max((step.t for step in trajectory if step.micro_obstructed), default=None)
    if level == "meso":
        return max((step.t for step in trajectory if step.meso_obstructed), default=None)
    if level == "holonic":
        return max((step.t for step in trajectory if step.holonic_obstructed), default=None)
    raise ValueError(f"unknown level: {level}")


def _positive_delta(later: int | None, earlier: int | None) -> int:
    if later is None or earlier is None:
        return 0
    return max(0, later - earlier)


def _verdict_for_scenario(
    scenario: PGScenario,
    residual_pg: int,
    forgotten_dims_generated: bool,
) -> str:
    if scenario.holonic_rule == "scheduled_window":
        return "scheduled_residual_pg_positive_control" if residual_pg > 0 else "failed_baseline"
    if scenario.scenario_id == "no_explicit_persistence_with_forgotten_dims":
        return (
            "forgotten_dims_generated_residual_pg"
            if forgotten_dims_generated
            else "no_residual_pg_from_forgotten_dims"
        )
    if scenario.scenario_id == "no_forgotten_dims_control":
        return "no_residual_pg_without_forgotten_dims" if residual_pg == 0 else "unexpected_control_pg"
    if scenario.holonic_rule == "explicit_recovery_retention":
        return "explicit_retention_generates_residual_pg" if residual_pg > 0 else "failed_retention_control"
    return "unclassified_pg_case"


def _interpretation(
    scenario: PGScenario,
    micro_pg: int,
    inherited_gap: int,
    residual_pg: int,
    verdict: str,
) -> str:
    if verdict == "scheduled_residual_pg_positive_control":
        return (
            f"PG relative to micro is {micro_pg}, of which {inherited_gap} comes "
            f"from meso lag and {residual_pg} remains after lower-level recovery. "
            "The residual is scheduled by the holonic window."
        )
    if verdict == "no_residual_pg_from_forgotten_dims":
        return (
            f"PG relative to micro is still {micro_pg}, but it is entirely inherited "
            f"from lower-level lag ({inherited_gap}); residual PG after lower-level "
            "recovery is zero despite non-empty forgotten_dims."
        )
    if verdict == "no_residual_pg_without_forgotten_dims":
        return (
            "The no-forgotten-dims control also has zero residual PG, confirming "
            "that the propagated-current-lower rule itself carries no holonic "
            "recovery memory."
        )
    if verdict == "explicit_retention_generates_residual_pg":
        return (
            f"Residual PG is {residual_pg}, but it is produced by the explicit "
            "retention rule rather than by forgotten_dims alone."
        )
    return (
        f"{scenario.scenario_id} produced micro PG {micro_pg}, inherited gap "
        f"{inherited_gap}, residual PG {residual_pg}."
    )


if __name__ == "__main__":
    import json

    print(json.dumps(t174_result_to_dict(run_t174_analysis()), indent=2))
