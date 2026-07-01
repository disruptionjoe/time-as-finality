"""T384: synthesis packet for the shared-substrate relativity ladder."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LadderFinding:
    test_id: str
    finding: str


@dataclass(frozen=True)
class Premise:
    premise_id: str
    statement: str


@dataclass(frozen=True)
class OpenObject:
    object_id: str
    statement: str


@dataclass(frozen=True)
class T384Result:
    claim_level: str
    theorem_like_statement: str
    premise_bundle: tuple[Premise, ...]
    forced_outputs: tuple[str, ...]
    open_objects: tuple[OpenObject, ...]
    ladder_findings: tuple[LadderFinding, ...]
    external_adapter_reading: str
    next_goal: str
    overall_verdict: str
    plain_english_summary: str


def premise_bundle() -> tuple[Premise, ...]:
    return (
        Premise(
            "shared_generated_substrate",
            "A shared compatibility substrate exists and source rows do not store observer time/space coordinates.",
        ),
        Premise(
            "two_independent_null_channels",
            "The adapter supplies exactly two independent primitive null compatibility-signal directions.",
        ),
        Premise(
            "bilinear_interval",
            "The interval object is a symmetric bilinear form over the two signal lineages.",
        ),
        Premise(
            "round_trip_calibration",
            "Observers calibrate by reciprocal round-trip signal counts.",
        ),
        Premise(
            "invariant_signal_unit",
            "The primitive signal unit is shared; c = 1 is a rest-rendering normalization.",
        ),
        Premise(
            "exact_access_minimality",
            "The adapter has exact record-level access and no extra primitive signal direction.",
        ),
    )


def ladder_findings() -> tuple[LadderFinding, ...]:
    return (
        LadderFinding(
            "T377",
            "A fixed no-time-column compatibility table can render observer-relative simultaneity with a shared interval.",
        ),
        LadderFinding(
            "T378",
            "The rank-like structure can be generated from local compatibility edges rather than stored as source columns.",
        ),
        LadderFinding(
            "T379",
            "Given invariant signal propagation and round-trip calibration, Lorentz-pattern beta/gamma/time dilation are derived.",
        ),
        LadderFinding(
            "T380",
            "Two independent null channels force the product interval up to scale, but the two-channel basis is not derived.",
        ),
        LadderFinding(
            "T381",
            "Within declared observer-relativity requirements, the minimal two-null-channel adapter is the unique survivor.",
        ),
        LadderFinding(
            "T382",
            "Among declared external adapter shapes, the two-null-channel adapter is uniquely clean.",
        ),
        LadderFinding(
            "T383",
            "Targeted perturbations show the pattern is premise-sensitive but fails in interpretable ways.",
        ),
    )


def open_objects() -> tuple[OpenObject, ...]:
    return (
        OpenObject(
            "basis_origin",
            "Derive or independently motivate why exactly two primitive null compatibility-signal directions exist.",
        ),
        OpenObject(
            "bilinear_null_premise",
            "Explain why the compatibility invariant should be symmetric bilinear and why primitive signals are null.",
        ),
        OpenObject(
            "nonfinite_nonfixed_extension",
            "Extend beyond finite generated closures and fixed catalog screens.",
        ),
        OpenObject(
            "physical_interpretation",
            "Clarify whether the two-null-channel adapter is internal substrate structure or an external interface.",
        ),
    )


def run_t384_analysis() -> T384Result:
    theorem_like = (
        "Given a generated shared compatibility substrate, exactly two independent primitive null "
        "compatibility-signal directions, a symmetric bilinear interval, reciprocal round-trip "
        "observer calibration, invariant signal-unit normalization, exact access, and minimality, "
        "the finite screen forces Lorentz-pattern observer relativity: simultaneity disagreement, "
        "time dilation, reciprocal observer transforms, and invariant interval recovery."
    )
    return T384Result(
        claim_level="conditional_pattern_theorem_not_physical_derivation",
        theorem_like_statement=theorem_like,
        premise_bundle=premise_bundle(),
        forced_outputs=(
            "observer simultaneity disagreement",
            "gamma/beta Lorentz-pattern coefficients",
            "time dilation from round-trip calibration",
            "reciprocal interval-preserving observer transforms",
            "shared interval recovery without source time/space columns",
        ),
        open_objects=open_objects(),
        ladder_findings=ladder_findings(),
        external_adapter_reading=(
            "The best current external-adapter shape is a minimal two-null-channel compatibility interface: "
            "it couples locally without importing global time and supplies the signal geometry needed for observer relativity."
        ),
        next_goal=(
            "Attack basis_origin: derive, motivate, or falsify the existence of exactly two primitive null "
            "compatibility-signal directions."
        ),
        overall_verdict="conditional_lorentz_pattern_forced_open_object_is_two_null_basis_origin",
        plain_english_summary=(
            "The campaign moved the question from 'does this look relativistic?' to 'what exact adapter makes "
            "relativity unavoidable?' The answer is conditional: if the shared substrate has a minimal two-null-channel "
            "signal interface, the Lorentz pattern follows. The remaining hard problem is why that interface exists."
        ),
    )


def t384_result_to_dict(result: T384Result) -> dict[str, object]:
    return {
        "claim_level": result.claim_level,
        "theorem_like_statement": result.theorem_like_statement,
        "premise_bundle": [
            {"premise_id": premise.premise_id, "statement": premise.statement}
            for premise in result.premise_bundle
        ],
        "forced_outputs": list(result.forced_outputs),
        "open_objects": [
            {"object_id": item.object_id, "statement": item.statement}
            for item in result.open_objects
        ],
        "ladder_findings": [
            {"test_id": finding.test_id, "finding": finding.finding}
            for finding in result.ladder_findings
        ],
        "external_adapter_reading": result.external_adapter_reading,
        "next_goal": result.next_goal,
        "overall_verdict": result.overall_verdict,
        "plain_english_summary": result.plain_english_summary,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t384_result_to_dict(run_t384_analysis()), indent=2))
