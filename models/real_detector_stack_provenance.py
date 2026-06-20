"""T75: map a realistic detector/logging stack into T72/T74.

The selected stack is a photon time-tagging architecture:

    photon detector -> PicoQuant HydraHarp 500 time tagger
    -> White Rabbit synchronized timing fabric
    -> hash-chained RFC 3161-style signed archive

The timing parameters are anchored to public device/protocol specs. The
cryptographic, trust, batching, and DAG ranges are plausible engineering
posteriors for an explicitly instrumented lab stack, not measured calibration
posteriors from a deployed experiment.
"""

from __future__ import annotations

from dataclasses import dataclass
import random

from models.provenance_protocol_monte_carlo import (
    FamilyOutcome,
    PriorFamily,
    Range,
    sample_family,
)


SAMPLE_COUNT = 400
SEED = 75031


@dataclass(frozen=True)
class CalibrationSource:
    parameter: str
    value_used: str
    source: str
    interpretation: str


@dataclass(frozen=True)
class StackMapping:
    name: str
    posterior: PriorFamily
    outcome: FamilyOutcome
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T75Result:
    sample_count: int
    seed: int
    selected_stack: str
    source_notes: tuple[CalibrationSource, ...]
    mappings: tuple[StackMapping, ...]
    strongest_claim: str
    weakened_claim: str
    q1_update: str
    blocker: str
    recommended_next: str


def calibration_sources() -> tuple[CalibrationSource, ...]:
    return (
        CalibrationSource(
            parameter="time tagger timing precision",
            value_used="HydraHarp 500: 1 ps base resolution, 2.5 ps RMS timing precision, 680 ps dead time, 85 Mcps throughput",
            source="https://www.picoquant.com/products/time-tagging-tcspc-electronics/",
            interpretation=(
                "Anchors local time-tag uncertainty well below a nanosecond "
                "for a high-control photon-counting stack."
            ),
        ),
        CalibrationSource(
            parameter="distributed timing",
            value_used="White Rabbit: sub-nanosecond distributed timing; CERN notes few-picosecond precision",
            source="https://openscience.cern/node/447",
            interpretation=(
                "Supports a declared shared clock for distributed detector "
                "nodes, but the exact deployment still needs calibration."
            ),
        ),
        CalibrationSource(
            parameter="signed archive",
            value_used="RFC 3161-style timestamp tokens sign hash imprints and include unique serial numbers",
            source="https://www.ietf.org/rfc/rfc3161.txt",
            interpretation=(
                "Motivates high verification and low forgery priors for an "
                "explicitly signed archive, not for ordinary unsigned logs."
            ),
        ),
    )


def selected_stack_posterior() -> PriorFamily:
    return PriorFamily(
        name="hydraharp_wr_signed_archive",
        local_sigma=Range(0.003, 0.020),
        archive_sigma=Range(0.010, 0.080),
        batching_window=Range(0.020, 0.180),
        tag_retention=Range(0.975, 0.999),
        verification=Range(0.985, 0.9995),
        forgery=Range(0.0000, 0.0040),
        spoof_independent=Range(0.0000, 0.0060),
        unique_independent_tag=Range(0.975, 0.999),
        detector_trust=Range(0.930, 0.990),
        archive_trust=Range(0.940, 0.995),
        transport_trust=Range(0.930, 0.990),
        p_change_dependent=Range(0.920, 0.995),
        p_change_independent=Range(0.000, 0.060),
        back_action=Range(0.000, 0.025),
        observability=Range(0.950, 0.999),
        signed_edge=Range(0.970, 0.9995),
        truncation=Range(0.000, 0.035),
        false_shared_edge=Range(0.000, 0.020),
        confidence_floor=Range(0.780, 0.850),
        max_false_risk=Range(0.120, 0.220),
        declared_threshold_prob=1.0,
        purpose=(
            "Photon time-tagging stack with White Rabbit timing and a signed, "
            "hash-chained provenance archive."
        ),
    )


def unsigned_control_posterior() -> PriorFamily:
    base = selected_stack_posterior()
    return PriorFamily(
        name="hydraharp_wr_unsigned_archive_control",
        local_sigma=base.local_sigma,
        archive_sigma=base.archive_sigma,
        batching_window=base.batching_window,
        tag_retention=Range(0.500, 0.900),
        verification=Range(0.350, 0.700),
        forgery=Range(0.050, 0.250),
        spoof_independent=Range(0.050, 0.300),
        unique_independent_tag=Range(0.450, 0.850),
        detector_trust=base.detector_trust,
        archive_trust=Range(0.600, 0.850),
        transport_trust=Range(0.650, 0.900),
        p_change_dependent=base.p_change_dependent,
        p_change_independent=base.p_change_independent,
        back_action=base.back_action,
        observability=Range(0.350, 0.750),
        signed_edge=Range(0.000, 0.300),
        truncation=Range(0.100, 0.450),
        false_shared_edge=Range(0.030, 0.250),
        confidence_floor=base.confidence_floor,
        max_false_risk=base.max_false_risk,
        declared_threshold_prob=0.85,
        purpose=(
            "Same timing hardware, but without a signed provenance archive or "
            "reliable ancestry graph."
        ),
    )


def run_t75_analysis() -> T75Result:
    rng = random.Random(SEED)
    stack = selected_stack_posterior()
    control = unsigned_control_posterior()
    mappings = (
        _classify_mapping(stack, rng),
        _classify_mapping(control, rng),
    )
    selected = mappings[0]
    if selected.outcome.robust_rate >= 0.8:
        q1_update = (
            "Q1 remains partially supported as an instrumentation/provenance "
            "claim for explicitly engineered detector stacks."
        )
        strongest_claim = (
            "A realistic photon time-tagging stack can occupy the engineered "
            "T74 recovery region if it combines picosecond time tags, "
            "sub-nanosecond clock distribution, and signed hash-chain archive "
            "provenance."
        )
    else:
        q1_update = (
            "Detector Q1 should be demoted to a conditional accounting "
            "framework requiring externally supplied provenance."
        )
        strongest_claim = (
            "The selected realistic detector stack does not occupy the T74 "
            "engineered recovery region under the mapped posteriors."
        )
    return T75Result(
        sample_count=SAMPLE_COUNT,
        seed=SEED,
        selected_stack=stack.name,
        source_notes=calibration_sources(),
        mappings=mappings,
        strongest_claim=strongest_claim,
        weakened_claim=(
            "The positive result is carried by engineered provenance logging, "
            "not by detector timing alone. The unsigned-control variant loses "
            "robust recovery despite retaining the same time-tagging hardware."
        ),
        q1_update=q1_update,
        blocker=(
            "The timing inputs are source-anchored, but authentication, trust, "
            "batching, back-action, and DAG-observability ranges are plausible "
            "engineering posteriors rather than measured deployment posteriors."
        ),
        recommended_next=(
            "Replace the signed-archive priors with measurements from one lab "
            "deployment: event-loss logs, signature-verification failures, "
            "archive replay tests, perturbation tests, and DAG truncation audits."
        ),
    )


def t75_result_to_dict(result: T75Result) -> dict[str, object]:
    return {
        "sample_count": result.sample_count,
        "seed": result.seed,
        "selected_stack": result.selected_stack,
        "source_notes": [
            {
                "parameter": note.parameter,
                "value_used": note.value_used,
                "source": note.source,
                "interpretation": note.interpretation,
            }
            for note in result.source_notes
        ],
        "mappings": [
            {
                "name": mapping.name,
                "verdict": mapping.verdict,
                "interpretation": mapping.interpretation,
                "posterior_ranges": _posterior_to_dict(mapping.posterior),
                "outcome": _outcome_to_dict(mapping.outcome),
            }
            for mapping in result.mappings
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "q1_update": result.q1_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def _classify_mapping(family: PriorFamily, rng: random.Random) -> StackMapping:
    outcome = sample_family(family, rng, SAMPLE_COUNT)
    if outcome.robust_rate >= 0.8:
        verdict = "robust_recovery"
        interpretation = "The mapped stack occupies the T74 engineered recovery region."
    elif outcome.false_independence_rate > 0.0:
        verdict = "false_independence_risk"
        interpretation = "Copied provenance is sometimes accepted as independent."
    elif outcome.false_dependence_rate > 0.0:
        verdict = "false_dependence_risk"
        interpretation = "Independent provenance is sometimes accepted as dependent."
    elif outcome.threshold_dependent_rate > 0.5:
        verdict = "threshold_dependent_failure"
        interpretation = "Most samples require thresholds not justified by the protocol."
    else:
        verdict = "conservative_withhold"
        interpretation = "The protocol usually withholds D1 rather than fixing provenance."
    return StackMapping(
        name=family.name,
        posterior=family,
        outcome=outcome,
        verdict=verdict,
        interpretation=interpretation,
    )


def _range_to_list(value: Range) -> list[float]:
    return [value.low, value.high]


def _posterior_to_dict(family: PriorFamily) -> dict[str, object]:
    return {
        "local_sigma": _range_to_list(family.local_sigma),
        "archive_sigma": _range_to_list(family.archive_sigma),
        "batching_window": _range_to_list(family.batching_window),
        "tag_retention": _range_to_list(family.tag_retention),
        "verification": _range_to_list(family.verification),
        "forgery": _range_to_list(family.forgery),
        "spoof_independent": _range_to_list(family.spoof_independent),
        "unique_independent_tag": _range_to_list(family.unique_independent_tag),
        "detector_trust": _range_to_list(family.detector_trust),
        "archive_trust": _range_to_list(family.archive_trust),
        "transport_trust": _range_to_list(family.transport_trust),
        "p_change_dependent": _range_to_list(family.p_change_dependent),
        "p_change_independent": _range_to_list(family.p_change_independent),
        "back_action": _range_to_list(family.back_action),
        "observability": _range_to_list(family.observability),
        "signed_edge": _range_to_list(family.signed_edge),
        "truncation": _range_to_list(family.truncation),
        "false_shared_edge": _range_to_list(family.false_shared_edge),
        "confidence_floor": _range_to_list(family.confidence_floor),
        "max_false_risk": _range_to_list(family.max_false_risk),
        "declared_threshold_prob": family.declared_threshold_prob,
        "purpose": family.purpose,
    }


def _outcome_to_dict(outcome: FamilyOutcome) -> dict[str, object]:
    return {
        "sample_count": outcome.sample_count,
        "robust_rate": outcome.robust_rate,
        "withhold_rate": outcome.withhold_rate,
        "threshold_dependent_rate": outcome.threshold_dependent_rate,
        "false_independence_rate": outcome.false_independence_rate,
        "false_dependence_rate": outcome.false_dependence_rate,
        "computable_d1_rate": outcome.computable_d1_rate,
        "robust_count": outcome.robust_count,
        "withhold_count": outcome.withhold_count,
        "threshold_dependent_count": outcome.threshold_dependent_count,
        "false_independence_count": outcome.false_independence_count,
        "false_dependence_count": outcome.false_dependence_count,
        "computable_d1_count": outcome.computable_d1_count,
    }
