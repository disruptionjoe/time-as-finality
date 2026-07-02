"""T402: Causal-domain boundary-forcing screen.

T401 cleared a finite finality-native task shape, but the separator was still
absorbed as ordinary joint-record access. T402 tests the next stronger lane:
make the boundary-crossing task live in a finite physical substrate, using a
1+1 causal-domain screen.

The conservative result is absorptive. A common-future verdict event is in the
causal future / domain of dependence of both boundary inputs, while the bounded
region R alone cannot determine the verdict. That makes boundary crossing
forced by the setup, but the separator is still explained by ordinary causal
domain completion plus joint input access. No claim promotion follows.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Any, Callable

from models.lorentzian_causal_diamond_screen import (
    InitialDataInterval,
    MinkowskiEvent,
    common_future_contains,
    spacelike_separated,
)


ARTIFACT = "T402-causal-domain-boundary-forcing-screen-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"

VERDICT = (
    "finite physical-substrate forced-boundary candidate built: a common-future "
    "verdict event is causally downstream of both R and B inputs, while R-only "
    "statistics and declared R interventions remain flat; the result clears the "
    "causal-domain task-shape burden but is absorbed by ordinary causal-domain "
    "completion and joint input access, so no claim-ledger movement is earned"
)

FALSIFICATION_CONDITION = (
    "This screen would fail if any R-supported statistic separated the pair, if "
    "the verdict event were determined by the R-only domain, if boundary access "
    "were merely optional rather than forced by the common-future task, or if "
    "causal-domain completion were ignored as the absorber."
)

Pair = tuple[int, int]
Distribution = dict[Pair, float]

PAIRS: tuple[Pair, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))
REGION_MAPS: dict[str, Callable[[int], int]] = {
    "identity": lambda bit: bit,
    "flip": lambda bit: 1 - bit,
    "erase_to_0": lambda bit: 0,
    "erase_to_1": lambda bit: 1,
}


@dataclass(frozen=True)
class CausalDomainFixture:
    left_region_event: MinkowskiEvent
    right_boundary_event: MinkowskiEvent
    common_future_verdict_event: MinkowskiEvent
    region_only_initial_data: InitialDataInterval
    boundary_only_initial_data: InitialDataInterval
    joint_initial_data: InitialDataInterval


@dataclass(frozen=True)
class TaskCandidate:
    case_id: str
    task_statement: str
    declared_before_pair: bool
    requires_common_future_event: bool
    verdict_event_in_joint_domain: bool
    region_only_domain_suffices: bool
    boundary_menu_merely_admitted: bool
    smuggles_hidden_datum_into_R: bool = False
    closure_key_contains_separator: bool = False
    class_marker_signature_only: bool = False
    domain_native_physical_task: bool = False


def _rounded(value: float) -> float:
    if abs(value) < 1e-12:
        return 0.0
    if abs(value - 1.0) < 1e-12:
        return 1.0
    if abs(value - 0.5) < 1e-12:
        return 0.5
    return round(value, 12)


def _pair_label(pair: Pair) -> str:
    return f"{pair[0]}{pair[1]}"


def _serializable_dist(dist: Distribution) -> dict[str, float]:
    return {_pair_label(pair): _rounded(dist.get(pair, 0.0)) for pair in PAIRS}


def causal_domain_fixture() -> CausalDomainFixture:
    left = MinkowskiEvent("R_input", 0.0, -1.0, frozenset({"left_record"}))
    right = MinkowskiEvent("B_input", 0.0, 1.0, frozenset({"right_record"}))
    verdict = MinkowskiEvent("common_future_verdict", 1.0, 0.0)
    return CausalDomainFixture(
        left_region_event=left,
        right_boundary_event=right,
        common_future_verdict_event=verdict,
        region_only_initial_data=InitialDataInterval("R_only_slice", 0.0, -1.0, -1.0),
        boundary_only_initial_data=InitialDataInterval("B_only_slice", 0.0, 1.0, 1.0),
        joint_initial_data=InitialDataInterval("RB_joint_slice", 0.0, -1.0, 1.0),
    )


def source_pair_distributions() -> dict[str, Distribution]:
    return {
        "aligned": {(0, 0): 0.5, (1, 1): 0.5},
        "anti_aligned": {(0, 1): 0.5, (1, 0): 0.5},
    }


def _marginal(dist: Distribution, axis: str) -> dict[int, float]:
    idx = 0 if axis == "R" else 1
    out = {0: 0.0, 1: 0.0}
    for pair, prob in dist.items():
        out[pair[idx]] += prob
    return {key: _rounded(value) for key, value in out.items()}


def _binary_table(dist: dict[int, float]) -> list[float]:
    return [_rounded(dist[0]), _rounded(dist[1])]


def _total_variation(a: dict[Any, float], b: dict[Any, float]) -> float:
    keys = set(a) | set(b)
    return _rounded(0.5 * sum(abs(a.get(key, 0.0) - b.get(key, 0.0)) for key in keys))


def _binary_success_from_tv(tv: float) -> float:
    return _rounded(0.5 * (1.0 + tv))


def _region_intervention_table(dist: Distribution) -> dict[str, list[float]]:
    marginal = _marginal(dist, "R")
    out: dict[str, list[float]] = {}
    for name, fn in REGION_MAPS.items():
        moved = {0: 0.0, 1: 0.0}
        for bit, prob in marginal.items():
            moved[fn(bit)] += prob
        out[name] = _binary_table(moved)
    return out


def _max_table_diff(a: dict[str, list[float]], b: dict[str, list[float]]) -> float:
    diff = 0.0
    for key in a:
        diff = max(diff, max(abs(x - y) for x, y in zip(a[key], b[key])))
    return _rounded(diff)


def _relation_distribution(dist: Distribution) -> dict[str, float]:
    same = 0.0
    different = 0.0
    for (region_bit, boundary_bit), prob in dist.items():
        if region_bit == boundary_bit:
            same += prob
        else:
            different += prob
    return {"same": _rounded(same), "different": _rounded(different)}


def _event_dict(event: MinkowskiEvent) -> dict[str, Any]:
    return {
        "event_id": event.event_id,
        "t": event.t,
        "x": event.x,
        "records": sorted(event.records),
    }


def _interval_dict(interval: InitialDataInterval) -> dict[str, Any]:
    return {
        "interval_id": interval.interval_id,
        "t0": interval.t0,
        "x_min": interval.x_min,
        "x_max": interval.x_max,
    }


def _causal_geometry(fixture: CausalDomainFixture) -> dict[str, Any]:
    left = fixture.left_region_event
    right = fixture.right_boundary_event
    verdict = fixture.common_future_verdict_event
    r_only = fixture.region_only_initial_data.future_domain_contains(verdict)
    b_only = fixture.boundary_only_initial_data.future_domain_contains(verdict)
    joint = fixture.joint_initial_data.future_domain_contains(verdict)
    return {
        "events": {
            "R_input": _event_dict(left),
            "B_input": _event_dict(right),
            "common_future_verdict": _event_dict(verdict),
        },
        "initial_data_intervals": {
            "R_only": _interval_dict(fixture.region_only_initial_data),
            "B_only": _interval_dict(fixture.boundary_only_initial_data),
            "RB_joint": _interval_dict(fixture.joint_initial_data),
        },
        "R_and_B_are_spacelike": spacelike_separated(left, right),
        "verdict_in_common_future": common_future_contains(left, right, verdict),
        "R_only_domain_contains_verdict": r_only,
        "B_only_domain_contains_verdict": b_only,
        "RB_joint_domain_contains_verdict": joint,
        "boundary_crossing_forced_by_domain": joint and not r_only and not b_only,
    }


def _main_pair_audit() -> dict[str, Any]:
    dists = source_pair_distributions()
    aligned = dists["aligned"]
    anti = dists["anti_aligned"]
    aligned_R = _marginal(aligned, "R")
    anti_R = _marginal(anti, "R")
    aligned_B = _marginal(aligned, "B")
    anti_B = _marginal(anti, "B")
    region_table_aligned = _region_intervention_table(aligned)
    region_table_anti = _region_intervention_table(anti)
    region_tv = _total_variation(aligned_R, anti_R)
    boundary_tv = _total_variation(aligned_B, anti_B)
    full_tv = _total_variation(aligned, anti)
    relation_aligned = _relation_distribution(aligned)
    relation_anti = _relation_distribution(anti)

    return {
        "pair": ["aligned", "anti_aligned"],
        "source_distributions": {
            "aligned": _serializable_dist(aligned),
            "anti_aligned": _serializable_dist(anti),
        },
        "region_marginals": {
            "aligned": _binary_table(aligned_R),
            "anti_aligned": _binary_table(anti_R),
        },
        "boundary_marginals": {
            "aligned": _binary_table(aligned_B),
            "anti_aligned": _binary_table(anti_B),
        },
        "region_total_variation": region_tv,
        "boundary_local_total_variation": boundary_tv,
        "full_joint_total_variation": full_tv,
        "all_R_supported_statistic_bound": region_tv,
        "all_boundary_local_statistic_bound": boundary_tv,
        "finite_region_intervention_menu": {
            "maps": list(REGION_MAPS),
            "n_statistics": len(REGION_MAPS),
            "max_diff": _max_table_diff(region_table_aligned, region_table_anti),
            "aligned": region_table_aligned,
            "anti_aligned": region_table_anti,
        },
        "region_only_binary_success": _binary_success_from_tv(region_tv),
        "boundary_local_binary_success": _binary_success_from_tv(boundary_tv),
        "common_future_verdict_success": _binary_success_from_tv(full_tv),
        "common_future_verdict_relation": {
            "aligned": relation_aligned,
            "anti_aligned": relation_anti,
            "separates_pair": relation_aligned != relation_anti,
            "binary_success": 1.0,
        },
    }


def _candidate_cases(geometry: dict[str, Any]) -> list[TaskCandidate]:
    return [
        TaskCandidate(
            case_id="causal_common_future_verdict_task",
            task_statement=(
                "Issue the common-future final verdict only at the event whose "
                "causal past contains both the bounded-region input and the "
                "boundary input."
            ),
            declared_before_pair=True,
            requires_common_future_event=True,
            verdict_event_in_joint_domain=geometry["RB_joint_domain_contains_verdict"],
            region_only_domain_suffices=geometry["R_only_domain_contains_verdict"],
            boundary_menu_merely_admitted=False,
            domain_native_physical_task=True,
        ),
        TaskCandidate(
            case_id="optional_joint_state_label",
            task_statement=(
                "Admit arbitrary joint R:B access and label which source "
                "distribution was prepared."
            ),
            declared_before_pair=True,
            requires_common_future_event=False,
            verdict_event_in_joint_domain=geometry["RB_joint_domain_contains_verdict"],
            region_only_domain_suffices=False,
            boundary_menu_merely_admitted=True,
        ),
        TaskCandidate(
            case_id="region_hidden_source_bit",
            task_statement=(
                "Give R an additional hidden bit naming aligned versus "
                "anti-aligned before causal propagation."
            ),
            declared_before_pair=True,
            requires_common_future_event=False,
            verdict_event_in_joint_domain=False,
            region_only_domain_suffices=True,
            boundary_menu_merely_admitted=False,
            smuggles_hidden_datum_into_R=True,
        ),
        TaskCandidate(
            case_id="closure_key_shortcut",
            task_statement=(
                "Attach a precomputed closure key to the bounded region that "
                "already contains the same/different verdict."
            ),
            declared_before_pair=True,
            requires_common_future_event=False,
            verdict_event_in_joint_domain=False,
            region_only_domain_suffices=True,
            boundary_menu_merely_admitted=False,
            closure_key_contains_separator=True,
        ),
        TaskCandidate(
            case_id="class_marker_shortcut",
            task_statement=(
                "Use the global aligned/anti-aligned class name instead of the "
                "causal inputs at the verdict event."
            ),
            declared_before_pair=True,
            requires_common_future_event=False,
            verdict_event_in_joint_domain=False,
            region_only_domain_suffices=True,
            boundary_menu_merely_admitted=False,
            class_marker_signature_only=True,
        ),
    ]


def _first_failure(candidate: TaskCandidate, metrics: dict[str, Any]) -> str | None:
    if metrics["all_R_supported_statistic_bound"] != 0.0:
        return "fails_region_statistic_equality"
    if metrics["finite_region_intervention_menu"]["max_diff"] != 0.0:
        return "fails_region_intervention_equality"
    if metrics["all_boundary_local_statistic_bound"] != 0.0:
        return "fails_boundary_local_equality"
    if (
        metrics["common_future_verdict_relation"]["binary_success"]
        <= metrics["region_only_binary_success"]
    ):
        return "fails_boundary_crossing_advantage"
    if not candidate.declared_before_pair:
        return "not_predeclared"
    if candidate.smuggles_hidden_datum_into_R:
        return "hidden_datum_smuggled_into_region"
    if candidate.closure_key_contains_separator:
        return "absorbed_by_closure_key"
    if candidate.class_marker_signature_only:
        return "absorbed_by_class_marker_signature"
    if candidate.boundary_menu_merely_admitted:
        return "optional_boundary_menu_only"
    if not candidate.requires_common_future_event:
        return "task_does_not_require_common_future_event"
    if not candidate.verdict_event_in_joint_domain:
        return "verdict_not_in_joint_domain"
    if candidate.region_only_domain_suffices:
        return "region_domain_already_suffices"
    if not candidate.domain_native_physical_task:
        return "not_domain_native_physical_task"
    return None


def _residue_label(
    candidate: TaskCandidate, formal_pass: bool, failure: str | None
) -> str:
    if formal_pass and candidate.domain_native_physical_task:
        return "candidate_physical_forced_task_absorbed_by_causal_domain"
    if formal_pass:
        return "formal_positive_control_only"
    if failure == "optional_boundary_menu_only":
        return "absorbed_optional_enlarged_access"
    if failure == "hidden_datum_smuggled_into_region":
        return "blocked_hidden_datum_smuggling"
    if failure == "absorbed_by_closure_key":
        return "absorbed_closure_key_bookkeeping"
    if failure == "absorbed_by_class_marker_signature":
        return "absorbed_class_marker_signature"
    return "failed_causal_domain_task_gate"


def _audit_candidate(candidate: TaskCandidate, metrics: dict[str, Any]) -> dict[str, Any]:
    failure = _first_failure(candidate, metrics)
    formal_pass = failure is None
    boundary_success = metrics["common_future_verdict_relation"]["binary_success"]
    return {
        "candidate": asdict(candidate),
        "measurement_gate": {
            "region_statistics_equal": metrics[
                "all_R_supported_statistic_bound"
            ]
            == 0.0,
            "region_intervention_statistics_equal": metrics[
                "finite_region_intervention_menu"
            ]["max_diff"]
            == 0.0,
            "boundary_local_statistics_equal": metrics[
                "all_boundary_local_statistic_bound"
            ]
            == 0.0,
            "common_future_verdict_advantage": _rounded(
                boundary_success - metrics["region_only_binary_success"]
            ),
            "joint_domain_restores_capability": metrics[
                "full_joint_total_variation"
            ]
            == 1.0,
        },
        "causal_domain_task_gate": "pass" if formal_pass else "fail",
        "failure_label": failure,
        "physical_substrate_burden_cleared": (
            formal_pass and candidate.domain_native_physical_task
        ),
        "residue_label": _residue_label(candidate, formal_pass, failure),
    }


def _controls(fixture: CausalDomainFixture) -> dict[str, Any]:
    region_visible_a: Distribution = {(0, 0): 0.5, (0, 1): 0.5}
    region_visible_b: Distribution = {(1, 0): 0.5, (1, 1): 0.5}
    region_visible_tv = _total_variation(
        _marginal(region_visible_a, "R"), _marginal(region_visible_b, "R")
    )
    off_axis_event = MinkowskiEvent("off_axis_event", 1.0, 2.5)
    return {
        "region_visible_control": {
            "pair": ["R_always_0", "R_always_1"],
            "region_total_variation": region_visible_tv,
            "region_only_binary_success": _binary_success_from_tv(region_visible_tv),
            "purpose": (
                "teeth control: R-supported readouts distinguish pairs when "
                "the R marginal actually differs"
            ),
        },
        "causal_domain_negative_control": {
            "event": _event_dict(off_axis_event),
            "RB_joint_domain_contains_event": (
                fixture.joint_initial_data.future_domain_contains(off_axis_event)
            ),
            "purpose": (
                "null control: the declared joint interval does not determine "
                "events outside its future domain"
            ),
        },
    }


def _absorber_audit(
    metrics: dict[str, Any], geometry: dict[str, Any]
) -> dict[str, Any]:
    return {
        "lorentzian_causal_domain_completion": {
            "status": "absorbs",
            "reason": (
                "The verdict event is in the common future and joint domain of "
                "the R and B inputs, but not in the R-only or B-only domain. The "
                "capability split follows from ordinary causal-domain data."
            ),
            "R_only_domain_contains_verdict": geometry[
                "R_only_domain_contains_verdict"
            ],
            "RB_joint_domain_contains_verdict": geometry[
                "RB_joint_domain_contains_verdict"
            ],
        },
        "ordinary_joint_input_completion": {
            "status": "absorbs_after_domain_access",
            "reason": (
                "Once the common-future event has both incoming records, the "
                "same/different verdict is an ordinary function of joint inputs."
            ),
            "full_joint_total_variation": metrics["full_joint_total_variation"],
        },
        "R_supported_intervention_underdescription": {
            "status": "certified_no_separator",
            "reason": (
                "Equal R marginals imply equality for every declared R-supported "
                "map/readout; the finite menu is an executable check."
            ),
            "all_R_supported_statistic_bound": metrics[
                "all_R_supported_statistic_bound"
            ],
        },
        "claim_promotion": {
            "status": "blocked",
            "reason": (
                "The artifact supplies a physical-substrate absorber screen, not "
                "a same-causal-data finality or physics residue."
            ),
        },
    }


def run_causal_domain_boundary_forcing_screen() -> dict[str, Any]:
    fixture = causal_domain_fixture()
    geometry = _causal_geometry(fixture)
    metrics = _main_pair_audit()
    audits = [_audit_candidate(candidate, metrics) for candidate in _candidate_cases(geometry)]
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "setup": {
            "substrate": "finite 1+1 causal-domain record propagation",
            "region_R": "left input event at t=0, x=-1",
            "boundary_B": "right input event at t=0, x=1",
            "task": (
                "issue a common-future final verdict at t=1, x=0 from the "
                "same/different relation of the incoming records"
            ),
            "declared_before_pair": True,
        },
        "causal_geometry": geometry,
        "main_pair_audit": metrics,
        "causal_domain_task_audits": audits,
        "controls": _controls(fixture),
        "absorber_audit": _absorber_audit(metrics, geometry),
        "summary": {
            "pass_cases": [
                item["candidate"]["case_id"]
                for item in audits
                if item["causal_domain_task_gate"] == "pass"
            ],
            "physical_substrate_pass_cases": [
                item["candidate"]["case_id"]
                for item in audits
                if item["physical_substrate_burden_cleared"]
            ],
            "blocked_cases": {
                item["candidate"]["case_id"]: item["failure_label"]
                for item in audits
                if item["causal_domain_task_gate"] == "fail"
            },
        },
        "verdict": VERDICT,
        "residue_label": "candidate_physical_forced_task_absorbed_by_causal_domain_completion",
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Treat T402 as a physical-substrate absorber screen, not a claim upgrade.",
            "Do not repeat causal-domain completion as if it were a surviving discriminator.",
            "A future upgrade needs a same-causal-domain-data capability split not expressible as causal reachability, domain of dependence, or ordinary joint input completion.",
        ],
        "falsification_condition": FALSIFICATION_CONDITION,
    }


if __name__ == "__main__":
    print(
        json.dumps(
            run_causal_domain_boundary_forcing_screen(),
            indent=2,
            sort_keys=True,
        )
    )
