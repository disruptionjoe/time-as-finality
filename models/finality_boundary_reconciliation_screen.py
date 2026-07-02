"""T401: Finality-boundary reconciliation screen.

T400 left the next Direction-A burden as a domain-native physical or finality
task whose boundary crossing is forced by the declared setup. This artifact
uses a deliberately finite record-reconciliation task: a bounded-region record
holder R and a boundary holder B each carry one event bit, and the task is to
issue a merged/final record verdict only after checking whether the two holders
attest the same event value.

The two source distributions have identical R marginals, identical B
marginals, and identical statistics after every declared R-supported
intervention/readout. The reconciliation relation differs only in the joint
R:B record. The result clears the finality-task shape as a finite candidate,
but it is still absorbed as ordinary joint-record access, not claim promotion.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Any, Callable


ARTIFACT = "T401-finality-boundary-reconciliation-screen-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"

VERDICT = (
    "finite finality-native forced-task candidate built: same R and B local "
    "statistics, including the declared R intervention/readout menu, do not "
    "separate aligned from anti-aligned record pairs, while the predeclared "
    "record-reconciliation task forces the R:B relation and separates them; "
    "the result is absorbed as ordinary joint-record access and earns no "
    "claim-ledger movement"
)

FALSIFICATION_CONDITION = (
    "This screen would fail if any R-supported statistic separated the pair, "
    "if the reconciliation task did not require both record holders, if a "
    "shortcut key or class marker did the work, or if the ordinary joint-record "
    "absorber were ignored."
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
class TaskCandidate:
    case_id: str
    task_statement: str
    declared_before_pair: bool
    requires_boundary_variables: bool
    boundary_relation_is_task_native: bool
    boundary_menu_merely_admitted: bool
    smuggles_hidden_datum_into_R: bool = False
    closure_key_contains_separator: bool = False
    class_marker_signature_only: bool = False
    domain_native_finality_task: bool = False


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


def record_pair_distributions() -> dict[str, Distribution]:
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


def _main_pair_audit() -> dict[str, Any]:
    dists = record_pair_distributions()
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
        "joint_record_binary_success": _binary_success_from_tv(full_tv),
        "boundary_crossing_menu": {
            "record_reconciliation_relation": {
                "aligned": relation_aligned,
                "anti_aligned": relation_anti,
                "separates_pair": relation_aligned != relation_anti,
                "binary_success": 1.0,
            }
        },
    }


def _candidate_cases() -> list[TaskCandidate]:
    return [
        TaskCandidate(
            case_id="finality_record_reconciliation_task",
            task_statement=(
                "Issue a merged/final record verdict only after checking "
                "whether the bounded-region record and boundary-holder record "
                "attest the same event value."
            ),
            declared_before_pair=True,
            requires_boundary_variables=True,
            boundary_relation_is_task_native=True,
            boundary_menu_merely_admitted=False,
            domain_native_finality_task=True,
        ),
        TaskCandidate(
            case_id="optional_joint_state_label",
            task_statement=(
                "Admit any joint R:B readout and label which source distribution "
                "was prepared."
            ),
            declared_before_pair=True,
            requires_boundary_variables=False,
            boundary_relation_is_task_native=False,
            boundary_menu_merely_admitted=True,
        ),
        TaskCandidate(
            case_id="hidden_datum_in_R_shortcut",
            task_statement=(
                "Give R an extra hidden task bit naming aligned versus anti-aligned."
            ),
            declared_before_pair=True,
            requires_boundary_variables=False,
            boundary_relation_is_task_native=False,
            boundary_menu_merely_admitted=False,
            smuggles_hidden_datum_into_R=True,
        ),
        TaskCandidate(
            case_id="closure_key_shortcut",
            task_statement=(
                "Add a precomputed closure key to R that already contains the "
                "same/different separator."
            ),
            declared_before_pair=True,
            requires_boundary_variables=False,
            boundary_relation_is_task_native=False,
            boundary_menu_merely_admitted=False,
            closure_key_contains_separator=True,
        ),
        TaskCandidate(
            case_id="class_marker_shortcut",
            task_statement=(
                "Use the global aligned/anti-aligned class name instead of the "
                "per-event record relation."
            ),
            declared_before_pair=True,
            requires_boundary_variables=False,
            boundary_relation_is_task_native=False,
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
        metrics["boundary_crossing_menu"]["record_reconciliation_relation"][
            "binary_success"
        ]
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
    if not candidate.requires_boundary_variables:
        return "task_does_not_require_boundary_variables"
    if not candidate.boundary_relation_is_task_native:
        return "boundary_relation_not_task_native"
    return None


def _residue_label(
    candidate: TaskCandidate, formal_pass: bool, failure: str | None
) -> str:
    if formal_pass and candidate.domain_native_finality_task:
        return "candidate_finality_native_forced_task_absorbed"
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
    return "failed_forced_task_gate"


def _audit_candidate(candidate: TaskCandidate, metrics: dict[str, Any]) -> dict[str, Any]:
    failure = _first_failure(candidate, metrics)
    formal_pass = failure is None
    boundary_success = metrics["boundary_crossing_menu"][
        "record_reconciliation_relation"
    ]["binary_success"]
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
            "boundary_crossing_advantage": _rounded(
                boundary_success - metrics["region_only_binary_success"]
            ),
            "region_enlargement_restores_capability": metrics[
                "full_joint_total_variation"
            ]
            == 1.0,
        },
        "formal_forced_task_gate": "pass" if formal_pass else "fail",
        "failure_label": failure,
        "domain_native_burden_cleared": (
            formal_pass and candidate.domain_native_finality_task
        ),
        "residue_label": _residue_label(candidate, formal_pass, failure),
    }


def _controls() -> dict[str, Any]:
    region_visible_a: Distribution = {(0, 0): 0.5, (0, 1): 0.5}
    region_visible_b: Distribution = {(1, 0): 0.5, (1, 1): 0.5}
    uniform_joint: Distribution = {pair: 0.25 for pair in PAIRS}
    region_visible_tv = _total_variation(
        _marginal(region_visible_a, "R"), _marginal(region_visible_b, "R")
    )
    uniform_relation = _relation_distribution(uniform_joint)
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
        "uncorrelated_boundary_control": {
            "distribution": _serializable_dist(uniform_joint),
            "record_reconciliation_relation": uniform_relation,
            "binary_success_against_aligned_or_anti": 0.5,
            "purpose": (
                "null control: local marginals alone do not supply a determinate "
                "same/different reconciliation relation"
            ),
        },
    }


def _absorber_audit(metrics: dict[str, Any]) -> dict[str, Any]:
    return {
        "ordinary_joint_record_completion": {
            "status": "absorbs",
            "reason": (
                "Once both holder records are admitted, the same/different "
                "relation is an ordinary joint-record fact."
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
        "closure_key_or_SBS_shortcut": {
            "status": "blocked_not_invoked",
            "reason": (
                "The passing task computes the per-event holder relation. A "
                "precomputed key naming that relation is audited separately and "
                "fails as closure-key bookkeeping."
            ),
        },
        "class_marker_signature": {
            "status": "blocked",
            "reason": (
                "The source class name is not accepted as a substitute for the "
                "per-event reconciliation relation."
            ),
        },
        "claim_promotion": {
            "status": "blocked",
            "reason": (
                "The result is finite record-reconciliation discipline and is "
                "absorbed by ordinary joint-record access."
            ),
        },
    }


def run_finality_boundary_reconciliation_screen() -> dict[str, Any]:
    metrics = _main_pair_audit()
    audits = [_audit_candidate(candidate, metrics) for candidate in _candidate_cases()]
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "setup": {
            "region_R": "bounded holder of one event record bit",
            "boundary_B": "boundary holder of one event record bit",
            "task": (
                "issue a merged/final record verdict by checking whether the "
                "two holders attest the same event value"
            ),
            "declared_before_pair": True,
        },
        "main_pair_audit": metrics,
        "forced_task_audits": audits,
        "controls": _controls(),
        "absorber_audit": _absorber_audit(metrics),
        "summary": {
            "formal_pass_cases": [
                item["candidate"]["case_id"]
                for item in audits
                if item["formal_forced_task_gate"] == "pass"
            ],
            "domain_native_pass_cases": [
                item["candidate"]["case_id"]
                for item in audits
                if item["domain_native_burden_cleared"]
            ],
            "blocked_cases": {
                item["candidate"]["case_id"]: item["failure_label"]
                for item in audits
                if item["formal_forced_task_gate"] == "fail"
            },
        },
        "verdict": VERDICT,
        "residue_label": "candidate_finality_native_forced_task_absorbed_as_joint_record_access",
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Treat T401 as a finite finality-native task screen, not a physics or claim upgrade.",
            "Use the same forced-task audit before any stronger physical boundary-crossing discriminator.",
            "A future upgrade needs an absorber-resistant physical setup, not just ordinary joint-record reconciliation.",
        ],
        "falsification_condition": FALSIFICATION_CONDITION,
    }


if __name__ == "__main__":
    print(
        json.dumps(
            run_finality_boundary_reconciliation_screen(),
            indent=2,
            sort_keys=True,
        )
    )
