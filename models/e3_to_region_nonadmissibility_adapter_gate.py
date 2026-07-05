"""T453 - E3 to region nonadmissibility adapter gate.

T447 built a finite exact E3 no-go relative to a declared finite non-wrapping
exact-catalyst policy. T452 requires a region-indexed packet to do more: clear
the T434/T445 region screen, name the law-sector completion being blocked, and
show that completion is physically non-admissible rather than merely outside R.

This adapter gate tests whether the existing T447 packet discharges that T452
burden. The result is intentionally conservative: T447 is useful as an exact
no-go witness pattern, but it does not by itself become a region-indexed
capability discriminator.

Run:

    python -m models.e3_to_region_nonadmissibility_adapter_gate --write-results
    python -m pytest tests/test_e3_to_region_nonadmissibility_adapter_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import law_sector_nonadmissibility_gate as t452
from models import quantum_e3_exact_no_go_big_swing as t447


ARTIFACT = "T453-e3-to-region-nonadmissibility-adapter-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T445 = "results/T445-region-capability-substrate-law-big-swing-v0.1-results.md"
SOURCE_T447 = "results/T447-quantum-e3-exact-no-go-big-swing-v0.1-results.md"
SOURCE_T452 = "results/T452-law-sector-nonadmissibility-gate-v0.1-results.md"
SOURCE_N14 = "literature/N14-h7-sector-gauge-absorber.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "T447_E3_NO_GO_DOES_NOT_DISCHARGE_REGION_T452_BURDEN"

HONEST_CEILING = (
    "Recorded-tier adapter gate only. T453 shows that the existing T447 finite "
    "exact no-go is a useful witness pattern but does not discharge T452's "
    "region-indexed law-sector nonadmissibility burden. The only admitted shape "
    "is a synthetic integrated future target. This is not a region-indexed "
    "discriminator success, not a WAY theorem, not a quantum physics theorem, "
    "not a GU/TaF adapter, not claim-ledger movement, and not public posture."
)


@dataclass(frozen=True)
class AdapterCandidate:
    candidate_id: str
    description: str
    source: str
    has_t447_exact_no_go_witness: bool
    t447_survives_declared_finite_a2: bool
    clears_t434_law_admission: bool
    r_statistics_and_interventions_matched: bool
    boundary_menu_splits_capability: bool
    law_sector_completion_named: bool
    allowed_operations_frozen: bool = True
    a2_resource_lift_audited: bool = True
    exact_witness_targets_named_completion: bool = False
    completion_merely_hidden_from_r: bool = False
    completion_factors_through_admitted_policy: bool = False
    sector_gauge_generic_claim: bool = False
    negative_control_present: bool = True
    synthetic_control_only: bool = False


def _candidate_to_dict(candidate: AdapterCandidate) -> dict[str, Any]:
    return asdict(candidate)


def _t447_main_case() -> dict[str, Any]:
    return next(
        item
        for item in t447.run()["case_audits"]
        if item["case_id"] == "finite_nonwrapping_exact_catalyst_charge_flip"
    )


def _t452_current_packet() -> dict[str, Any]:
    return next(
        item
        for item in t452.run()["packet_evaluations"]
        if item["packet_id"] == "current_t445_z2_law_packet"
    )


def _base_region_packet_ok(candidate: AdapterCandidate) -> bool:
    return (
        candidate.clears_t434_law_admission
        and candidate.r_statistics_and_interventions_matched
        and candidate.boundary_menu_splits_capability
        and candidate.law_sector_completion_named
    )


def evaluate_candidate(candidate: AdapterCandidate) -> dict[str, Any]:
    admitted = False

    if candidate.sector_gauge_generic_claim:
        label = "ROUTES_TO_N14_SECTOR_GAUGE_ABSORBER"
        reason = (
            "Generic sector, gauge, or superselection language is absorber-owned "
            "unless it names a finite region task, fixed operation/resource class, "
            "and exact witness after reservoir, reference, boundary, and gauge data "
            "are matched."
        )
    elif not candidate.has_t447_exact_no_go_witness:
        label = "NOT_ADMITTED_NO_T447_STYLE_EXACT_WITNESS"
        reason = "The adapter lacks the exact no-go witness that T452 requires."
    elif not candidate.t447_survives_declared_finite_a2:
        label = "NOT_ADMITTED_E3_WITNESS_LIFTED_BY_A2_CONTROL"
        reason = "The proposed E3 witness does not survive its own A2 resource-lift audit."
    elif not _base_region_packet_ok(candidate):
        label = "NOT_REGION_INDEXED_BASE_PACKET_MISSING"
        reason = (
            "T447 alone is not a region-indexed packet: it does not supply the "
            "T434/T445 region equality certificates, boundary capability split, "
            "and named law-sector completion required by T452."
        )
    elif candidate.completion_merely_hidden_from_r:
        label = "NOT_ADMITTED_T452_ABSORBER_STILL_FIRES"
        reason = (
            "The region packet still treats completion as outside R rather than "
            "physically non-admissible. Adding a T447 citation does not tie the "
            "exact witness to the named T445 law-sector completion."
        )
    elif not candidate.allowed_operations_frozen:
        label = "NOT_ADMITTED_ALLOWED_OPERATIONS_UNFROZEN"
        reason = "The adapter must freeze the operation/resource class before pair selection."
    elif not candidate.a2_resource_lift_audited:
        label = "NOT_ADMITTED_A2_RESOURCE_LIFT_UNTESTED"
        reason = "The adapter must audit A2 resource/reference completions."
    elif not candidate.exact_witness_targets_named_completion:
        label = "NOT_ADMITTED_EXACT_WITNESS_NOT_TIED_TO_COMPLETION"
        reason = (
            "The exact no-go witness must forbid the same completion that restores "
            "factorization in the region packet."
        )
    elif candidate.completion_factors_through_admitted_policy:
        label = "E0_DECLARED_BY_ADMITTED_REFERENCE_OR_POLICY_COMPLETION"
        reason = (
            "The capability split factors through an admissible reference or policy "
            "completion. This is an E0-declared boundary, not T452 nonadmissibility."
        )
    elif not candidate.negative_control_present:
        label = "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
        reason = "A nearby negative control is required before admitting the adapter."
    else:
        admitted = True
        label = "ADMITTED_E3_REGION_ADAPTER_REVIEW_TARGET_NO_PROMOTION"
        reason = (
            "The candidate has the region certificates, a T447-style exact witness "
            "tied to the named completion, frozen operations, A2 audit, and a "
            "negative control. It is admitted only as a synthetic future target."
        )

    return {
        "candidate_id": candidate.candidate_id,
        "description": candidate.description,
        "source": candidate.source,
        "candidate": _candidate_to_dict(candidate),
        "admitted": admitted,
        "adapter_label": label,
        "reason": reason,
    }


def candidates() -> tuple[AdapterCandidate, ...]:
    t447_main = _t447_main_case()
    t452_current = _t452_current_packet()
    t447_survives = bool(t447_main["survives_declared_finite_a2_resource_lift"])
    current_t445_base = bool(
        t452_current["packet"]["clears_t434_law_admission"]
        and t452_current["packet"]["r_statistics_and_interventions_matched"]
        and t452_current["packet"]["boundary_menu_splits_capability"]
        and t452_current["packet"]["law_sector_completion_named"]
    )

    return (
        AdapterCandidate(
            candidate_id="bare_t447_exact_no_go",
            description=(
                "T447 main finite non-wrapping exact-catalyst no-go considered "
                "without any region-indexed pair."
            ),
            source=SOURCE_T447,
            has_t447_exact_no_go_witness=True,
            t447_survives_declared_finite_a2=t447_survives,
            clears_t434_law_admission=False,
            r_statistics_and_interventions_matched=False,
            boundary_menu_splits_capability=False,
            law_sector_completion_named=False,
            exact_witness_targets_named_completion=True,
        ),
        AdapterCandidate(
            candidate_id="citation_only_t445_plus_t447",
            description=(
                "The current T445 region packet plus a citation to T447, without "
                "tying T447's exact no-go to T445's named law-sector completion."
            ),
            source=f"{SOURCE_T445}; {SOURCE_T447}; {SOURCE_T452}",
            has_t447_exact_no_go_witness=True,
            t447_survives_declared_finite_a2=t447_survives,
            clears_t434_law_admission=current_t445_base,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            exact_witness_targets_named_completion=False,
            completion_merely_hidden_from_r=bool(
                t452_current["packet"]["completion_merely_hidden_from_r"]
            ),
        ),
        AdapterCandidate(
            candidate_id="reference_policy_pair",
            description=(
                "A pair that differs only by finite non-wrapping versus cyclic or "
                "consumed reference policy. It can split capability, but the policy "
                "completion itself explains the split."
            ),
            source=SOURCE_T447,
            has_t447_exact_no_go_witness=True,
            t447_survives_declared_finite_a2=t447_survives,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            exact_witness_targets_named_completion=True,
            completion_factors_through_admitted_policy=True,
        ),
        AdapterCandidate(
            candidate_id="generic_sector_gauge_claim",
            description=(
                "A generic superselection/gauge-sector claim with no finite region "
                "task and no matched reservoir/reference/boundary/gauge audit."
            ),
            source=SOURCE_N14,
            has_t447_exact_no_go_witness=False,
            t447_survives_declared_finite_a2=False,
            clears_t434_law_admission=False,
            r_statistics_and_interventions_matched=False,
            boundary_menu_splits_capability=False,
            law_sector_completion_named=False,
            sector_gauge_generic_claim=True,
        ),
        AdapterCandidate(
            candidate_id="synthetic_integrated_e3_region_packet",
            description=(
                "Synthetic calibration target: a future packet with T445-style "
                "region certificates and a T447-style exact no-go tied to the named "
                "law-sector completion."
            ),
            source=ARTIFACT,
            has_t447_exact_no_go_witness=True,
            t447_survives_declared_finite_a2=True,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            exact_witness_targets_named_completion=True,
            synthetic_control_only=True,
        ),
        AdapterCandidate(
            candidate_id="synthetic_missing_negative_control",
            description="A nearby integrated packet with no negative control.",
            source=ARTIFACT,
            has_t447_exact_no_go_witness=True,
            t447_survives_declared_finite_a2=True,
            clears_t434_law_admission=True,
            r_statistics_and_interventions_matched=True,
            boundary_menu_splits_capability=True,
            law_sector_completion_named=True,
            exact_witness_targets_named_completion=True,
            negative_control_present=False,
            synthetic_control_only=True,
        ),
    )


def run() -> dict[str, Any]:
    evaluations = [evaluate_candidate(candidate) for candidate in candidates()]
    admitted = [item for item in evaluations if item["admitted"]]
    current_like = next(
        item for item in evaluations if item["candidate_id"] == "citation_only_t445_plus_t447"
    )
    bare_t447 = next(
        item for item in evaluations if item["candidate_id"] == "bare_t447_exact_no_go"
    )

    return {
        "artifact": ARTIFACT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t445": SOURCE_T445,
            "t447": SOURCE_T447,
            "t452": SOURCE_T452,
            "n14": SOURCE_N14,
            "taxonomy": SOURCE_TAXONOMY,
        },
        "purpose": (
            "Test whether the existing T447 finite exact E3 no-go can discharge "
            "T452's region-indexed law-sector nonadmissibility burden."
        ),
        "adapter_requirements": [
            "inherit a T447-style exact no-go witness that survives A2 audit",
            "clear the T434/T445 region-law base packet",
            "match all declared R-supported statistics and interventions",
            "split capability only under the boundary/law menu",
            "name the law-sector completion being blocked",
            "tie the exact witness to that named completion",
            "freeze the operation/resource class before pair selection",
            "include a negative control",
            "avoid generic sector/gauge language and admitted reference-policy completion",
        ],
        "candidate_evaluations": evaluations,
        "overall_verdict": {
            "verdict": VERDICT,
            "bare_t447_label": bare_t447["adapter_label"],
            "citation_only_t445_plus_t447_label": current_like["adapter_label"],
            "admitted_candidate_ids": [item["candidate_id"] for item in admitted],
            "admitted_candidates_are_synthetic_only": all(
                item["candidate"]["synthetic_control_only"] for item in admitted
            ),
            "current_artifacts_discharge_region_burden": False,
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "T447 supplies an exact finite no-go witness pattern, but T447 "
                "alone has no region-indexed pair, and the current T445+T447 "
                "citation-only route still leaves the T452 absorber firing. A "
                "reference-policy split factors through admitted completion. Only "
                "a synthetic integrated packet is admitted as a future review target."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Do not cite T447 alone as discharging the region-indexed discriminator.",
            "A future Direction-A packet must integrate the exact no-go with the same completion that otherwise restores factorization.",
            "Reject generic sector/gauge shortcuts through the N14 absorber unless they supply a finite matched-accounting task packet.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    requirements = [f"- {item}" for item in result["adapter_requirements"]]
    rows = [
        "| {candidate_id} | {admitted} | {label} |".format(
            candidate_id=item["candidate_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["adapter_label"],
        )
        for item in result["candidate_evaluations"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T453 - E3 To Region Nonadmissibility Adapter Gate - v0.1 results",
            "",
            "> Recorded-tier adapter gate. `CLAIM-LEDGER.md`, `TESTS.md`, "
            "`ROADMAP.md`, README, North Star files, public posture, hard policy, "
            "and cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T453-e3-to-region-nonadmissibility-adapter-gate.md`",
            "- Model: `models/e3_to_region_nonadmissibility_adapter_gate.py`",
            "- Tests: `tests/test_e3_to_region_nonadmissibility_adapter_gate.py`",
            "- Artifact JSON: `results/T453-e3-to-region-nonadmissibility-adapter-gate-v0.1.json`",
            "- Sources: T445, T447, T452, N14, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Adapter Requirements",
            "",
            *requirements,
            "",
            "## Candidate Evaluation",
            "",
            "| candidate | admitted? | adapter label |",
            "| --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a routing gate that blocks a tempting shortcut from T447's finite "
            "exact E3 no-go to the region-indexed T452 burden.",
            "",
            "Does not earn: a region-indexed discriminator success, a real substrate "
            "law, a quantum physics theorem, a WAY theorem, a GU/TaF adapter, "
            "claim-ledger movement, public posture, or cross-repo support.",
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            *next_steps,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = (
            results_dir / "T453-e3-to-region-nonadmissibility-adapter-gate-v0.1.json"
        )
        md_path = (
            results_dir
            / "T453-e3-to-region-nonadmissibility-adapter-gate-v0.1-results.md"
        )
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
