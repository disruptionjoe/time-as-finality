"""T494 - Levin/Fields primary-source competency absorber gate.

T493 made the N16 Levin/Fields competency neighbor executable but left the
source status pointer-grade. This gate records a bounded primary-source check
for the N16 scope and keeps the result from becoming claim support.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T494-levin-fields-primary-source-absorber-gate-v0.1"
VERDICT = "PRIMARY_SOURCE_COMPETENCY_ABSORBER_BUILT_NO_CLAIM_MOVEMENT"

SOURCE_N16 = "literature/N16-levin-competency-capability-neighbor.md"
SOURCE_N17 = "literature/N17-levin-fields-primary-source-competency-absorber.md"
SOURCE_T493 = "results/T493-levin-competency-cr-absorber-gate-v0.1-results.md"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"

HONEST_CEILING = (
    "Primary-source absorber note and admission gate only. T494 checks the "
    "core N16 source family for calibration/absorber use, but does not prove "
    "novelty over Levin/Fields competency, does not import active inference or "
    "free-energy mechanisms into TaF, does not prove a region-indexed "
    "capability discriminator, and does not move claims, roadmap, README, "
    "North Star, public posture, hard policy, protected-license material, "
    "external publication, or cross-repo truth."
)

READING = (
    "The primary sources support N16 as a real calibration neighbor: they "
    "frame competency as scale-agnostic navigation or problem-solving across "
    "spaces, cognitive light cones as bounded measurement/action horizons, and "
    "polycomputing as observer-dependent computational modeling. The same "
    "sources strengthen the absorber warning. If C(R) is just the full "
    "intervention-measured task-success profile in a declared region/menu/task "
    "context, T493 already absorbs it as competency-style bookkeeping. The "
    "surplus target remains only T407-style spread over simpler observed "
    "statistics, not novelty over a full competency profile."
)


@dataclass(frozen=True)
class SourceFact:
    source_id: str
    citation: str
    url: str
    primary_source_checked: bool
    supports_competency_navigation: bool = False
    supports_observer_access_boundary: bool = False
    supports_scale_or_substrate_agnosticism: bool = False
    supports_external_mechanism_neighbor: bool = False
    supports_polycomputing_observer_dependence: bool = False
    supports_taf_c_r_novelty: bool = False
    imports_taf_mechanism: bool = False
    note: str = ""


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    description: str
    uses_primary_source_check: bool
    treats_as_calibration_neighbor: bool = False
    treats_as_absorber_warning: bool = False
    uses_cognitive_light_cone_for_region_indexing: bool = False
    equates_single_statistic_with_full_c_r: bool = False
    imports_active_inference_or_free_energy: bool = False
    claims_novelty_over_competency: bool = False
    claims_public_or_cross_repo_update: bool = False
    claims_polycomputing_objective_identity: bool = False


@dataclass(frozen=True)
class Evaluation:
    candidate_id: str
    admitted: bool
    label: str
    action: str
    reason: str
    candidate: Candidate


def primary_sources() -> tuple[SourceFact, ...]:
    return (
        SourceFact(
            source_id="fields_levin_2022_competency",
            citation=(
                "Chris Fields and Michael Levin, Competency in Navigating "
                "Arbitrary Spaces as an Invariant for Analyzing Cognition in "
                "Diverse Embodiments, Entropy 24(6):819, 2022."
            ),
            url="https://doi.org/10.3390/e24060819",
            primary_source_checked=True,
            supports_competency_navigation=True,
            supports_scale_or_substrate_agnosticism=True,
            note=(
                "Supports the core N16 calibration: competency is framed as "
                "problem-space navigation across embodiments, not as TaF "
                "record finality."
            ),
        ),
        SourceFact(
            source_id="levin_2022_tame",
            citation=(
                "Michael Levin, Technological Approach to Mind Everywhere: An "
                "Experimentally-Grounded Framework for Understanding Diverse "
                "Bodies and Minds, Frontiers in Systems Neuroscience 16:768201, "
                "2022."
            ),
            url="https://doi.org/10.3389/fnsys.2022.768201",
            primary_source_checked=True,
            supports_competency_navigation=True,
            supports_scale_or_substrate_agnosticism=True,
            note=(
                "Supports TAME as a substrate-agnostic agency/competency frame, "
                "not as an imported TaF mechanism."
            ),
        ),
        SourceFact(
            source_id="levin_2019_computational_boundary",
            citation=(
                "Michael Levin, The Computational Boundary of a Self: "
                "Developmental Bioelectricity Drives Multicellularity and "
                "Scale-Free Cognition, Frontiers in Psychology 10:2688, 2019."
            ),
            url="https://doi.org/10.3389/fpsyg.2019.02688",
            primary_source_checked=True,
            supports_observer_access_boundary=True,
            supports_scale_or_substrate_agnosticism=True,
            note=(
                "Supports cognitive light cone language as a bounded "
                "measurement/action horizon, a calibration neighbor for "
                "region-indexed capability."
            ),
        ),
        SourceFact(
            source_id="fields_levin_2020_scale_free_biology",
            citation=(
                "Chris Fields and Michael Levin, Scale-Free Biology: "
                "Integrating Evolutionary and Developmental Thinking, "
                "BioEssays 42(8):e1900228, 2020."
            ),
            url="https://doi.org/10.1002/bies.201900228",
            primary_source_checked=True,
            supports_scale_or_substrate_agnosticism=True,
            supports_external_mechanism_neighbor=True,
            note=(
                "Supports active-inference and predictive-coding as external "
                "scale-free biology neighbors; it does not license importing "
                "those mechanisms into TaF C(R)."
            ),
        ),
        SourceFact(
            source_id="zhang_goldstein_levin_2023_sorting",
            citation=(
                "Taining Zhang, Adam Goldstein, and Michael Levin, Classical "
                "Sorting Algorithms as a Model of Morphogenesis, arXiv:2401.05375, "
                "2023."
            ),
            url="https://doi.org/10.48550/arXiv.2401.05375",
            primary_source_checked=True,
            supports_competency_navigation=True,
            supports_scale_or_substrate_agnosticism=True,
            note=(
                "Supports a minimal problem-space traversal calibration, not a "
                "biological or TaF claim."
            ),
        ),
        SourceFact(
            source_id="bongard_levin_2022_polycomputing",
            citation=(
                "Joshua Bongard and Michael Levin, There's Plenty of Room Right "
                "Here: Biological Systems as Evolved, Overloaded, Multi-scale "
                "Machines, arXiv:2212.10675, 2022."
            ),
            url="https://doi.org/10.48550/arXiv.2212.10675",
            primary_source_checked=True,
            supports_polycomputing_observer_dependence=True,
            note=(
                "Supports observer-dependent computational modeling as a "
                "guardrail against objective-identity overreads."
            ),
        ),
    )


def source_audit() -> dict[str, Any]:
    sources = primary_sources()
    checked_ids = [source.source_id for source in sources if source.primary_source_checked]
    calibration_ids = [
        source.source_id
        for source in sources
        if source.supports_competency_navigation
        or source.supports_observer_access_boundary
        or source.supports_polycomputing_observer_dependence
    ]
    absorber_risk_ids = [
        source.source_id
        for source in sources
        if source.supports_competency_navigation
        or source.supports_external_mechanism_neighbor
        or source.supports_polycomputing_observer_dependence
    ]
    return {
        "source_count": len(sources),
        "checked_ids": checked_ids,
        "all_core_sources_checked": len(checked_ids) == len(sources),
        "calibration_ids": calibration_ids,
        "absorber_risk_ids": absorber_risk_ids,
        "supports_taf_c_r_novelty_ids": [
            source.source_id for source in sources if source.supports_taf_c_r_novelty
        ],
        "imports_taf_mechanism_ids": [
            source.source_id for source in sources if source.imports_taf_mechanism
        ],
    }


def candidates() -> tuple[Candidate, ...]:
    return (
        Candidate(
            candidate_id="n16_primary_source_status_upgrade",
            description=(
                "Upgrade N16 from pointer-grade to primary-source checked for "
                "the bounded calibration/absorber scope."
            ),
            uses_primary_source_check=True,
            treats_as_calibration_neighbor=True,
            treats_as_absorber_warning=True,
        ),
        Candidate(
            candidate_id="competency_as_full_profile_absorber",
            description=(
                "Treat full competency/problem-space success profile as an "
                "absorber warning for current C(R)."
            ),
            uses_primary_source_check=True,
            treats_as_absorber_warning=True,
        ),
        Candidate(
            candidate_id="cognitive_light_cone_region_indexing_calibration",
            description=(
                "Use cognitive light cone as a calibration neighbor for bounded "
                "measurement/action horizons."
            ),
            uses_primary_source_check=True,
            treats_as_calibration_neighbor=True,
            uses_cognitive_light_cone_for_region_indexing=True,
        ),
        Candidate(
            candidate_id="single_statistic_equals_full_c_r",
            description=(
                "Treat one observed navigation/readout statistic as equivalent "
                "to the full C(R) profile."
            ),
            uses_primary_source_check=True,
            equates_single_statistic_with_full_c_r=True,
        ),
        Candidate(
            candidate_id="active_inference_mechanism_import",
            description=(
                "Import active-inference or free-energy mechanisms into TaF C(R)."
            ),
            uses_primary_source_check=True,
            imports_active_inference_or_free_energy=True,
        ),
        Candidate(
            candidate_id="novelty_over_competency_shortcut",
            description=(
                "Treat source resonance as evidence that TaF is novel over "
                "Levin/Fields competency."
            ),
            uses_primary_source_check=True,
            claims_novelty_over_competency=True,
        ),
        Candidate(
            candidate_id="polycomputing_objective_identity_shortcut",
            description=(
                "Treat observer-dependent polycomputing as objective identity "
                "between Levin/Fields and TaF C(R)."
            ),
            uses_primary_source_check=True,
            claims_polycomputing_objective_identity=True,
        ),
        Candidate(
            candidate_id="public_or_cross_repo_update_shortcut",
            description=(
                "Use the source check to update public posture or cross-repo "
                "absorber truth."
            ),
            uses_primary_source_check=True,
            claims_public_or_cross_repo_update=True,
        ),
    )


def evaluate(candidate: Candidate, audit: dict[str, Any]) -> Evaluation:
    if candidate.claims_public_or_cross_repo_update:
        return Evaluation(
            candidate.candidate_id,
            False,
            "BLOCKED_PUBLIC_OR_CROSS_REPO_UPDATE",
            "stop",
            "Source checking inside TaF does not authorize public posture or cross-repo truth movement.",
            candidate,
        )
    if candidate.claims_novelty_over_competency:
        return Evaluation(
            candidate.candidate_id,
            False,
            "BLOCKED_NOVELTY_OVER_COMPETENCY_SHORTCUT",
            "stop",
            "The checked sources increase absorber pressure; they do not prove TaF novelty.",
            candidate,
        )
    if candidate.imports_active_inference_or_free_energy:
        return Evaluation(
            candidate.candidate_id,
            False,
            "REJECTED_MECHANISM_IMPORT",
            "reject",
            "Scale-free biology and active-inference sources remain external neighbors, not TaF mechanisms.",
            candidate,
        )
    if candidate.claims_polycomputing_objective_identity:
        return Evaluation(
            candidate.candidate_id,
            False,
            "REJECTED_POLYCOMPUTING_OBJECTIVE_IDENTITY",
            "reject",
            "Polycomputing supports observer-dependent modeling, not objective identity with C(R).",
            candidate,
        )
    if candidate.equates_single_statistic_with_full_c_r:
        return Evaluation(
            candidate.candidate_id,
            False,
            "REJECTED_SINGLE_STATISTIC_FULL_PROFILE_COLLAPSE",
            "reject",
            "T493 already shows a single observed statistic collides with the full C(R) profile.",
            candidate,
        )
    if candidate.uses_cognitive_light_cone_for_region_indexing:
        return Evaluation(
            candidate.candidate_id,
            True,
            "ADMITTED_REGION_INDEXING_CALIBRATION_NO_CLAIM",
            "calibrate",
            "Cognitive light cone sources back bounded measurement/action horizon language only.",
            candidate,
        )
    if candidate.treats_as_absorber_warning and audit["all_core_sources_checked"]:
        return Evaluation(
            candidate.candidate_id,
            True,
            "ADMITTED_PRIMARY_SOURCE_ABSORBER_WARNING_NO_CLAIM",
            "absorb_or_calibrate",
            "Core N16 sources are checked for bounded use and strengthen the competency absorber warning.",
            candidate,
        )
    return Evaluation(
        candidate.candidate_id,
        False,
        "REJECTED_UNBOUNDED_SOURCE_READING",
        "reject",
        "The candidate exceeds the checked calibration/absorber scope.",
        candidate,
    )


def run() -> dict[str, Any]:
    audit = source_audit()
    evaluations = [evaluate(candidate, audit) for candidate in candidates()]
    admitted = [item.candidate_id for item in evaluations if item.admitted]
    return {
        "artifact": ARTIFACT,
        "sources": {
            "n16": SOURCE_N16,
            "n17": SOURCE_N17,
            "t493": SOURCE_T493,
            "open_problem": SOURCE_OPEN_PROBLEM,
        },
        "primary_sources": [asdict(source) for source in primary_sources()],
        "source_audit": audit,
        "candidate_evaluations": [
            {
                "candidate_id": item.candidate_id,
                "admitted": item.admitted,
                "label": item.label,
                "action": item.action,
                "reason": item.reason,
                "candidate": asdict(item.candidate),
            }
            for item in evaluations
        ],
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_candidate_ids": admitted,
            "n16_upgraded_for_bounded_scope": (
                "n16_primary_source_status_upgrade" in admitted
            ),
            "calibration_only": True,
            "claim_movement": False,
            "public_or_cross_repo_movement": False,
        },
        "reading": READING,
        "claim_ledger_update": "none; no claim promotion or demotion",
        "recommended_next": [
            "Cite N17, not the old pointer-grade N16 text, for Levin/Fields source status.",
            "Keep using T493 as the executable C(R)-versus-competency absorber gate.",
            "Do not reopen Direction A unless the packet clears T460 and survives the T493/T494 competency absorbers.",
            "Do not import active-inference, free-energy, or polycomputing mechanism language into TaF without a separate gate.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    source_rows = [
        "| {source_id} | {checked} | {cal} | {absorber} |".format(
            source_id=source["source_id"],
            checked="yes" if source["primary_source_checked"] else "no",
            cal="yes"
            if (
                source["supports_competency_navigation"]
                or source["supports_observer_access_boundary"]
                or source["supports_polycomputing_observer_dependence"]
            )
            else "no",
            absorber="yes"
            if (
                source["supports_competency_navigation"]
                or source["supports_external_mechanism_neighbor"]
                or source["supports_polycomputing_observer_dependence"]
            )
            else "no",
        )
        for source in payload["primary_sources"]
    ]
    eval_rows = [
        "| {candidate_id} | {admitted} | {label} | {action} | {reason} |".format(
            candidate_id=item["candidate_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["label"],
            action=item["action"],
            reason=item["reason"],
        )
        for item in payload["candidate_evaluations"]
    ]
    next_lines = [f"- {item}" for item in payload["recommended_next"]]

    return "\n".join(
        [
            "# T494 - Levin/Fields Primary-Source Competency Absorber Gate - v0.1 results",
            "",
            "> Primary-source absorber note and admission gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, protected-license, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T494-levin-fields-primary-source-absorber-gate.md`",
            "- Model: `models/levin_fields_primary_source_absorber_gate.py`",
            "- Tests: `tests/test_levin_fields_primary_source_absorber_gate.py`",
            "- Literature note: `literature/N17-levin-fields-primary-source-competency-absorber.md`",
            "- Artifact JSON: `results/T494-levin-fields-primary-source-absorber-gate-v0.1.json`",
            "",
            f"## Overall verdict: {payload['overall_verdict']['verdict']}",
            "",
            payload["reading"],
            "",
            "## Source Audit",
            "",
            "| Source | Checked? | Calibration? | Absorber risk? |",
            "| --- | --- | --- | --- |",
            *source_rows,
            "",
            "## Candidate Evaluation",
            "",
            "| Candidate | Admitted? | Label | Action | Reason |",
            "| --- | --- | --- | --- | --- |",
            *eval_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a primary-source-backed N17 absorber note and a reproducible gate for bounded N16 use.",
            "",
            "Does not earn: novelty over Levin/Fields competency, active-inference mechanism import, region-indexed discriminator success, claim status, public posture, hard-policy movement, or cross-repo support.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_lines,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T494-levin-fields-primary-source-absorber-gate-v0.1.json"
        md_path = results_dir / "T494-levin-fields-primary-source-absorber-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
