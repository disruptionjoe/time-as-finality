"""T15: generated integrated finality stress laboratory.

T14 is a single constructed witness.  T15 turns that witness into a bounded,
deterministic generator and searches the generated family for robust regions
and minimal breakpoints.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from statistics import mean

from models.proof_carrying_finality import (
    IdealProofSystem,
    ProofCertificate,
    opposite_claim_state,
)
from models.t1_record_graph import Record
from models.t14_integrated_finality import (
    Bits,
    IntegratedObserver,
    IntegratedRecordGraph,
)


HIDDEN_STATE: Bits = (1, 1, 1, 1, 1, 0, 0, 0, 0)
CHANNELS = ("grav", "em", "social")


@dataclass(frozen=True)
class GeneratedCaseConfig:
    case_id: str
    core_size: int
    weights: tuple[int, ...]
    masked_phase_indices: frozenset[int] = frozenset()
    include_forged: bool = False
    include_valid_dissent: bool = False


@dataclass(frozen=True)
class CaseEvaluation:
    case_id: str
    config: GeneratedCaseConfig
    core_profile: tuple[int, int, int, int]
    core_readout: float
    constructive_readout: float
    coupling_diverges: bool
    expression_preserves_identity: bool
    forged_rejected: bool
    valid_dissent_visible: bool
    profile_readout_separation: bool
    verified_social_readout: float | None
    breakpoint_labels: tuple[str, ...]

    @property
    def robust_success(self) -> bool:
        return (
            self.coupling_diverges
            and self.expression_preserves_identity
            and self.profile_readout_separation
            and not self.config.include_forged
            and not self.config.include_valid_dissent
        )


def _core_channel(index: int) -> str:
    return "grav" if index % 2 == 0 else "em"


def _core_tag(index: int) -> str:
    return "phase" if index % 2 == 1 else "base"


def _add_chain_events(graph: IntegratedRecordGraph, core_size: int) -> None:
    events = tuple(f"e{index + 1}" for index in range(core_size)) + ("observe",)
    for event in events:
        graph.add_event(event)
    for earlier, later in zip(events, events[1:]):
        graph.add_causal_edge(earlier, later)


def _valid_certificate(
    proof_system: IdealProofSystem,
    source_id: str,
    nonce: str,
) -> ProofCertificate:
    return proof_system.issue_leaf(source_id, HIDDEN_STATE, 0, nonce)


def build_generated_case(
    config: GeneratedCaseConfig,
) -> tuple[IntegratedRecordGraph, dict[str, IntegratedObserver]]:
    if config.core_size < 2:
        raise ValueError("core_size must be at least 2")
    if len(config.weights) != config.core_size:
        raise ValueError("weights length must match core_size")
    if any(weight not in (-1, 1) for weight in config.weights):
        raise ValueError("weights must be +1 or -1")

    proof_system = IdealProofSystem(key=f"t15-{config.case_id}".encode())
    graph = IntegratedRecordGraph(proof_system)
    _add_chain_events(graph, config.core_size)

    for index, weight in enumerate(config.weights):
        record_id = f"r{index + 1}"
        graph.add_integrated_record(
            Record(
                record_id,
                "X",
                "true",
                f"e{index + 1}",
                f"h{index + 1}",
                1.0,
            ),
            channel=_core_channel(index),
            weight=weight,
            expression_tags=frozenset({_core_tag(index)}),
            certificate=_valid_certificate(
                proof_system, f"source-{index + 1}", f"core-{index + 1}"
            ),
        )

    next_index = config.core_size + 1
    if config.include_forged:
        graph.add_integrated_record(
            Record("r-forged", "X", "true", "e2", f"h{next_index}", 1.0),
            channel="social",
            weight=-1,
            expression_tags=frozenset({"adversarial"}),
            certificate=proof_system.forge("forged-source", claim=0, epoch=0),
        )
        next_index += 1
    if config.include_valid_dissent:
        graph.add_integrated_record(
            Record("r-valid-dissent", "X", "true", "e2", f"h{next_index}", 1.0),
            channel="social",
            weight=-1,
            expression_tags=frozenset({"dissent"}),
            certificate=proof_system.issue_leaf(
                "dissent-source",
                opposite_claim_state(len(HIDDEN_STATE), claim=0),
                0,
                "valid-dissent",
            ),
        )

    holders = frozenset(record.holder for record in graph.records.values())
    masked_context = (("phase", False),) if config.masked_phase_indices else ()
    observers = {
        "core": IntegratedObserver(
            f"O_core_{config.case_id}",
            "observe",
            frozenset({"grav", "em"}),
            holders,
        ),
        "grav_only": IntegratedObserver(
            f"O_grav_{config.case_id}",
            "observe",
            frozenset({"grav"}),
            holders,
        ),
        "masked": IntegratedObserver(
            f"O_masked_{config.case_id}",
            "observe",
            frozenset({"grav", "em"}),
            holders,
            expression_context=masked_context,
        ),
        "raw_social": IntegratedObserver(
            f"O_raw_{config.case_id}",
            "observe",
            frozenset(CHANNELS),
            holders,
            require_valid_proofs=False,
        ),
        "verified_social": IntegratedObserver(
            f"O_verified_{config.case_id}",
            "observe",
            frozenset(CHANNELS),
            holders,
            require_valid_proofs=True,
        ),
    }
    return graph, observers


def _all_constructive_config(config: GeneratedCaseConfig) -> GeneratedCaseConfig:
    return GeneratedCaseConfig(
        case_id=f"{config.case_id}-constructive",
        core_size=config.core_size,
        weights=(1,) * config.core_size,
        masked_phase_indices=config.masked_phase_indices,
        include_forged=config.include_forged,
        include_valid_dissent=config.include_valid_dissent,
    )


def evaluate_case(config: GeneratedCaseConfig) -> CaseEvaluation:
    graph, observers = build_generated_case(config)
    constructive, constructive_observers = build_generated_case(
        _all_constructive_config(config)
    )
    threshold = 1
    core = observers["core"]
    grav_only = observers["grav_only"]
    masked = observers["masked"]
    verified_social = observers["verified_social"]
    raw_social = observers["raw_social"]

    core_profile = graph.profile_for(core, "X", "true", threshold)
    constructive_profile = constructive.profile_for(
        constructive_observers["core"], "X", "true", threshold
    )
    core_readout = graph.readout_for(core, "X", "true")
    constructive_readout = constructive.readout_for(
        constructive_observers["core"], "X", "true"
    )
    grav_profile = graph.profile_for(grav_only, "X", "true", threshold)
    masked_visible = graph.visible_records(masked)
    core_visible = graph.visible_records(core)
    masked_core_visible = tuple(
        record
        for record in masked_visible
        if record.record_id.startswith("r") and record.record_id[1:].isdigit()
    )
    expression_preserves_identity = bool(config.masked_phase_indices) and len(
        masked_core_visible
    ) < len(core_visible)
    raw_ids = {record.record_id for record in graph.visible_records(raw_social)}
    verified_ids = {
        record.record_id for record in graph.visible_records(verified_social)
    }

    labels = []
    if config.include_forged and "r-forged" in raw_ids:
        labels.append("forgery_visible_without_proof_filter")
    if config.include_valid_dissent and "r-valid-dissent" in verified_ids:
        labels.append("valid_dissent_survives_proof_filter")
    if not graph.view_for(core).reconstruct_value(core.t1_observer(), "X", threshold):
        labels.append("core_fails_to_reconstruct")
    if core_profile == constructive_profile and core_readout != constructive_readout:
        labels.append("profile_readout_nonfactorization")
    if expression_preserves_identity:
        labels.append("expression_hides_stored_identity")

    verified_social_readout = (
        graph.readout_for(verified_social, "X", "true")
        if config.include_valid_dissent or config.include_forged
        else None
    )
    return CaseEvaluation(
        case_id=config.case_id,
        config=config,
        core_profile=core_profile,
        core_readout=core_readout,
        constructive_readout=constructive_readout,
        coupling_diverges=grav_profile != core_profile,
        expression_preserves_identity=expression_preserves_identity,
        forged_rejected=not config.include_forged or "r-forged" not in verified_ids,
        valid_dissent_visible=config.include_valid_dissent
        and "r-valid-dissent" in verified_ids,
        profile_readout_separation=core_profile == constructive_profile
        and core_readout != constructive_readout,
        verified_social_readout=verified_social_readout,
        breakpoint_labels=tuple(labels),
    )


def generated_configs() -> tuple[GeneratedCaseConfig, ...]:
    configs: list[GeneratedCaseConfig] = []
    for core_size in (2, 3, 4, 5):
        for weights in product((-1, 1), repeat=core_size):
            if all(weight == 1 for weight in weights):
                continue
            for mask_phase in (False, True):
                masked_indices = (
                    frozenset(index for index in range(core_size) if _core_tag(index) == "phase")
                    if mask_phase
                    else frozenset()
                )
                for include_forged, include_valid_dissent in (
                    (False, False),
                    (True, False),
                    (False, True),
                    (True, True),
                ):
                    configs.append(
                        GeneratedCaseConfig(
                            case_id=(
                                f"n{core_size}-w{''.join('p' if w > 0 else 'm' for w in weights)}"
                                f"-mask{int(mask_phase)}"
                                f"-f{int(include_forged)}d{int(include_valid_dissent)}"
                            ),
                            core_size=core_size,
                            weights=weights,
                            masked_phase_indices=masked_indices,
                            include_forged=include_forged,
                            include_valid_dissent=include_valid_dissent,
                        )
                    )
    return tuple(configs)


def _minimal(
    evaluations: tuple[CaseEvaluation, ...],
    predicate,
) -> CaseEvaluation | None:
    matches = [evaluation for evaluation in evaluations if predicate(evaluation)]
    if not matches:
        return None
    return sorted(
        matches,
        key=lambda evaluation: (
            evaluation.config.core_size,
            len(evaluation.config.masked_phase_indices),
            evaluation.config.include_forged,
            evaluation.config.include_valid_dissent,
            evaluation.case_id,
        ),
    )[0]


def _case_summary(evaluation: CaseEvaluation | None) -> dict[str, object] | None:
    if evaluation is None:
        return None
    config = evaluation.config
    return {
        "case_id": evaluation.case_id,
        "core_size": config.core_size,
        "weights": config.weights,
        "masked_phase_indices": sorted(config.masked_phase_indices),
        "include_forged": config.include_forged,
        "include_valid_dissent": config.include_valid_dissent,
        "core_profile": evaluation.core_profile,
        "core_readout": evaluation.core_readout,
        "constructive_readout": evaluation.constructive_readout,
        "verified_social_readout": evaluation.verified_social_readout,
        "breakpoint_labels": evaluation.breakpoint_labels,
    }


def run_t15_analysis() -> dict[str, object]:
    evaluations = tuple(evaluate_case(config) for config in generated_configs())
    robust_successes = tuple(e for e in evaluations if e.robust_success)
    profile_separations = tuple(e for e in evaluations if e.profile_readout_separation)
    forged_cases = tuple(e for e in evaluations if e.config.include_forged)
    dissent_cases = tuple(e for e in evaluations if e.config.include_valid_dissent)
    expression_cases = tuple(e for e in evaluations if e.expression_preserves_identity)
    return {
        "case_count": len(evaluations),
        "sweep_axes": {
            "core_sizes": [2, 3, 4, 5],
            "weight_patterns": "all non-all-positive +/-1 patterns",
            "expression_masking": [False, True],
            "adversary_modes": ["none", "forged", "valid_dissent", "both"],
        },
        "fractions": {
            "robust_success": len(robust_successes) / len(evaluations),
            "profile_readout_separation": len(profile_separations) / len(evaluations),
            "coupling_divergence": mean(e.coupling_diverges for e in evaluations),
            "expression_preserves_identity": mean(
                e.expression_preserves_identity for e in evaluations
            ),
            "forged_rejection_when_present": mean(e.forged_rejected for e in forged_cases),
            "valid_dissent_visible_when_present": mean(
                e.valid_dissent_visible for e in dissent_cases
            ),
        },
        "minimal_witnesses": {
            "robust_success": _case_summary(
                _minimal(evaluations, lambda e: e.robust_success)
            ),
            "profile_readout_separation": _case_summary(
                _minimal(evaluations, lambda e: e.profile_readout_separation)
            ),
            "expression_hides_stored_identity": _case_summary(
                _minimal(evaluations, lambda e: e.expression_preserves_identity)
            ),
        },
        "minimal_breakpoints": {
            "forgery_visible_without_proof_filter": _case_summary(
                _minimal(
                    evaluations,
                    lambda e: "forgery_visible_without_proof_filter"
                    in e.breakpoint_labels,
                )
            ),
            "valid_dissent_survives_proof_filter": _case_summary(
                _minimal(
                    evaluations,
                    lambda e: "valid_dissent_survives_proof_filter"
                    in e.breakpoint_labels,
                )
            ),
            "core_fails_to_reconstruct": _case_summary(
                _minimal(
                    evaluations,
                    lambda e: "core_fails_to_reconstruct" in e.breakpoint_labels,
                )
            ),
        },
        "verdict": {
            "t14_is_not_single_case_only": len(robust_successes) > 0,
            "signed_readout_separation_is_common_in_sweep": len(profile_separations)
            > len(evaluations) / 2,
            "proof_filter_rejects_forgery_when_required": all(
                e.forged_rejected for e in forged_cases
            ),
            "proof_filter_does_not_eliminate_valid_dissent": all(
                e.valid_dissent_visible for e in dissent_cases
            ),
            "generated_family_still_uses_assigned_phase_weights": True,
        },
    }
