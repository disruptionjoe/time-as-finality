"""T434 - substrate-law admission gate.

T406 showed that a revision-capability split is absorbed when the only changed
object is the finite transition relation. T434 turns the next burden into a
small executable admission gate: a future positive route needs a predeclared,
domain-native law or measured substrate dynamics package that forces the
transition relation without reading the transition table itself.

Recorded-tier only. The synthetic positive controls are gate-shape examples,
not real substrate physics and not claim support.

Run:

    python -m models.substrate_law_admission_gate --write-results
    python -m pytest tests/test_substrate_law_admission_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models.transition_system_operation_unavailability_gate import (
    run_transition_system_operation_unavailability_gate,
)


ARTIFACT = "T434-substrate-law-admission-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_ARTIFACT = "T406-transition-system-operation-unavailability-gate-v0.1"
MIN_MEASURED_REPLICATES = 8

VERDICT = "SUBSTRATE_LAW_ADMISSION_GATE_BUILT_CURRENT_T406_NOT_ADMITTED"

HONEST_CEILING = (
    "Admission gate only. Synthetic controls show what would pass the gate; "
    "they do not name a real physical substrate law, do not discharge the "
    "region-indexed capability discriminator, and do not move claims."
)


@dataclass(frozen=True)
class LawPackage:
    package_id: str
    source_kind: str
    declared_before_pair: bool
    shared_formula_across_pair: bool
    reads_transition_relation: bool
    reads_case_id_or_hidden_label: bool
    uses_allowed_substrate_observables: bool
    preserves_fixed_accounting: bool
    derives_declared_transition_relation: bool
    has_negative_control: bool
    measurement_replicates: int = 0
    formula: str = ""
    substrate_observables: tuple[str, ...] = ()


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    description: str
    capability_split: bool
    fixed_accounting_projection_equal: bool
    transition_system_completion_equal: bool
    law_package: LawPackage | None = None
    synthetic_positive_control: bool = False


def _package_to_dict(package: LawPackage | None) -> dict[str, Any] | None:
    if package is None:
        return None
    data = asdict(package)
    data["substrate_observables"] = list(package.substrate_observables)
    return data


def evaluate_candidate(candidate: Candidate) -> dict[str, Any]:
    package = candidate.law_package

    if not candidate.capability_split:
        admitted = False
        label = "not_needed_no_capability_split"
        reason = "No revision-capability split is present."
    elif not candidate.fixed_accounting_projection_equal:
        admitted = False
        label = "absorbed_by_fixed_accounting_completion"
        reason = "The pair changes fixed accounting before any law verdict matters."
    elif package is None or package.source_kind == "none":
        admitted = False
        label = "not_admitted_no_independent_law_or_measurement"
        reason = "The split is still only a transition-system difference."
    elif package.source_kind not in {
        "conservation_law",
        "measured_dynamics",
        "transition_table",
    }:
        admitted = False
        label = "not_admitted_unknown_source_kind"
        reason = "The package source kind is not an admitted law or measured-dynamics source."
    elif not package.declared_before_pair:
        admitted = False
        label = "not_admitted_post_hoc_law"
        reason = "The law package was not frozen before the pair was selected."
    elif not package.shared_formula_across_pair:
        admitted = False
        label = "not_admitted_pair_specific_law"
        reason = "The two sides use different formulae rather than one shared law."
    elif package.reads_transition_relation:
        admitted = False
        label = "not_admitted_transition_table_restatement"
        reason = "The package restates the transition relation it is supposed to force."
    elif package.reads_case_id_or_hidden_label:
        admitted = False
        label = "blocked_hidden_label_law"
        reason = "The package reads a hidden case label rather than substrate data."
    elif not package.uses_allowed_substrate_observables:
        admitted = False
        label = "not_admitted_non_native_observable"
        reason = "The package uses observables outside the declared substrate vocabulary."
    elif not package.preserves_fixed_accounting:
        admitted = False
        label = "absorbed_by_fixed_accounting_completion"
        reason = "The package changes resource, provenance, control, or boundary accounting."
    elif (
        package.source_kind == "measured_dynamics"
        and (
            package.measurement_replicates < MIN_MEASURED_REPLICATES
            or not package.has_negative_control
        )
    ):
        admitted = False
        label = "not_admitted_underpowered_measured_dynamics"
        reason = "Measured dynamics needs repeated evidence and a negative control."
    elif not package.derives_declared_transition_relation:
        admitted = False
        label = "not_admitted_law_does_not_force_transition"
        reason = "The package does not derive the operation-availability split."
    else:
        admitted = True
        if package.source_kind == "measured_dynamics":
            label = "admitted_measured_dynamics_forced_transition_candidate"
            reason = (
                "The measured-dynamics packet is predeclared, controlled, and "
                "derives the transition relation without reading it."
            )
        else:
            label = "admitted_conservation_law_forced_transition_candidate"
            reason = (
                "The law packet is predeclared, shared, substrate-native, and "
                "derives the transition relation without reading it."
            )

    return {
        "candidate_id": candidate.candidate_id,
        "description": candidate.description,
        "capability_split": candidate.capability_split,
        "fixed_accounting_projection_equal": candidate.fixed_accounting_projection_equal,
        "transition_system_completion_equal": candidate.transition_system_completion_equal,
        "law_package": _package_to_dict(package),
        "synthetic_positive_control": candidate.synthetic_positive_control,
        "admitted": admitted,
        "residue_label": label,
        "reason": reason,
    }


def _law(
    package_id: str,
    source_kind: str = "conservation_law",
    declared_before_pair: bool = True,
    shared_formula_across_pair: bool = True,
    reads_transition_relation: bool = False,
    reads_case_id_or_hidden_label: bool = False,
    uses_allowed_substrate_observables: bool = True,
    preserves_fixed_accounting: bool = True,
    derives_declared_transition_relation: bool = True,
    has_negative_control: bool = True,
    measurement_replicates: int = 0,
    formula: str = "revise allowed iff substrate invariant remains neutral",
    substrate_observables: tuple[str, ...] = ("substrate_invariant", "operation_delta"),
) -> LawPackage:
    return LawPackage(
        package_id=package_id,
        source_kind=source_kind,
        declared_before_pair=declared_before_pair,
        shared_formula_across_pair=shared_formula_across_pair,
        reads_transition_relation=reads_transition_relation,
        reads_case_id_or_hidden_label=reads_case_id_or_hidden_label,
        uses_allowed_substrate_observables=uses_allowed_substrate_observables,
        preserves_fixed_accounting=preserves_fixed_accounting,
        derives_declared_transition_relation=derives_declared_transition_relation,
        has_negative_control=has_negative_control,
        measurement_replicates=measurement_replicates,
        formula=formula,
        substrate_observables=substrate_observables,
    )


def _t406_main_pair() -> dict[str, Any]:
    t406 = run_transition_system_operation_unavailability_gate()
    return t406["main_pair_summary"]


def candidates() -> tuple[Candidate, ...]:
    main = _t406_main_pair()
    return (
        Candidate(
            candidate_id="bare_t406_main_pair",
            description="The T406 main split with no independent law package.",
            capability_split=main["capability_split"],
            fixed_accounting_projection_equal=main["fixed_accounting_projection_equal"],
            transition_system_completion_equal=main["transition_system_completion_equal"],
        ),
        Candidate(
            candidate_id="transition_table_restatement",
            description="A package that reproduces the edge set by reading the edge set.",
            capability_split=True,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=False,
            law_package=_law(
                "transition_table_restatement",
                source_kind="transition_table",
                reads_transition_relation=True,
                formula="revise allowed iff a revise_verdict edge is listed",
                substrate_observables=("transition_edges",),
            ),
        ),
        Candidate(
            candidate_id="post_hoc_conservation_selector",
            description="A conservation-looking rule selected after seeing the pair.",
            capability_split=True,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=False,
            law_package=_law(
                "post_hoc_selector",
                declared_before_pair=False,
            ),
        ),
        Candidate(
            candidate_id="pair_specific_law",
            description="Each side gets its own rule, so the law is not one shared domain law.",
            capability_split=True,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=False,
            law_package=_law(
                "pair_specific_law",
                shared_formula_across_pair=False,
            ),
        ),
        Candidate(
            candidate_id="hidden_label_law",
            description="A rule that reads hidden case labels rather than substrate observables.",
            capability_split=True,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=False,
            law_package=_law(
                "hidden_label_law",
                reads_case_id_or_hidden_label=True,
                formula="revise allowed iff case_id == reachable",
                substrate_observables=("case_id",),
            ),
        ),
        Candidate(
            candidate_id="non_native_observable",
            description="A rule that uses an undeclared substrate observable.",
            capability_split=True,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=False,
            law_package=_law(
                "non_native_observable",
                uses_allowed_substrate_observables=False,
                substrate_observables=("oracle_transition_secret",),
            ),
        ),
        Candidate(
            candidate_id="underpowered_measured_dynamics",
            description="A measured-dynamics packet with too little evidence and no control.",
            capability_split=True,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=False,
            law_package=_law(
                "underpowered_measured_dynamics",
                source_kind="measured_dynamics",
                has_negative_control=False,
                measurement_replicates=2,
                formula="measured transition attempts determine revise availability",
                substrate_observables=("attempt_log", "failure_mode"),
            ),
        ),
        Candidate(
            candidate_id="fixed_accounting_change_control",
            description="A law-looking split that also changes fixed accounting.",
            capability_split=True,
            fixed_accounting_projection_equal=False,
            transition_system_completion_equal=False,
            law_package=_law("fixed_accounting_change_control"),
        ),
        Candidate(
            candidate_id="conservation_law_positive_control",
            description=(
                "Synthetic control: one predeclared conservation-style rule derives "
                "revise availability from substrate invariants, not from edges."
            ),
            capability_split=True,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=False,
            law_package=_law(
                "conservation_law_positive_control",
                formula=(
                    "revise_verdict allowed iff measured substrate charge plus "
                    "operation delta remains in the neutral sector"
                ),
                substrate_observables=("charge_sector", "operation_charge_delta"),
            ),
            synthetic_positive_control=True,
        ),
        Candidate(
            candidate_id="measured_dynamics_positive_control",
            description=(
                "Synthetic control: a predeclared repeated dynamics protocol derives "
                "operation availability without reading the transition table."
            ),
            capability_split=True,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=False,
            law_package=_law(
                "measured_dynamics_positive_control",
                source_kind="measured_dynamics",
                measurement_replicates=12,
                formula=(
                    "revise_verdict admitted iff the predeclared substrate-dynamics "
                    "attempt protocol succeeds in the neutral control and fails in "
                    "the blocked control"
                ),
                substrate_observables=(
                    "predeclared_attempt_log",
                    "instrumented_failure_mode",
                ),
            ),
            synthetic_positive_control=True,
        ),
        Candidate(
            candidate_id="matched_transition_no_split_control",
            description="A matched-transition control where no capability split exists.",
            capability_split=False,
            fixed_accounting_projection_equal=True,
            transition_system_completion_equal=True,
            law_package=_law("matched_transition_no_split_control"),
        ),
    )


def run() -> dict[str, Any]:
    audits = [evaluate_candidate(candidate) for candidate in candidates()]
    admitted = [item for item in audits if item["admitted"]]
    current = next(item for item in audits if item["candidate_id"] == "bare_t406_main_pair")
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "source_artifact": SOURCE_ARTIFACT,
        "purpose": (
            "Turn T406's remaining burden into an executable admission gate for "
            "future substrate-law or measured-dynamics transition splits."
        ),
        "gate_requirements": [
            "law or measured-dynamics package frozen before pair selection",
            "one shared formula/protocol across both sides",
            "does not read the transition relation",
            "does not read hidden case labels",
            "uses declared substrate observables",
            "preserves fixed accounting",
            "derives the declared transition relation",
            "measured dynamics has enough repeated evidence and a negative control",
        ],
        "minimum_measured_replicates": MIN_MEASURED_REPLICATES,
        "candidate_audits": audits,
        "overall_verdict": {
            "verdict": VERDICT,
            "current_t406_main_pair_admitted": current["admitted"],
            "admitted_candidate_ids": [item["candidate_id"] for item in admitted],
            "synthetic_positive_controls_only": all(
                item["synthetic_positive_control"] for item in admitted
            ),
            "reading": (
                "The current T406 split remains unadmitted because no independent "
                "domain-native law or measured-dynamics packet forces the transition "
                "relation. Synthetic controls show the admissible shape for a future "
                "run but do not supply real physics or claim support."
            ),
        },
        "honest_ceiling": HONEST_CEILING,
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Do not repeat T406 by changing only the transition relation.",
            "Future Direction-A work must first supply a concrete law or measured-dynamics packet that clears T434.",
            "Treat admitted synthetic controls as gate calibration only, not evidence.",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    rows = [
        "| {candidate_id} | {admitted} | {residue_label} | {synthetic} |".format(
            candidate_id=item["candidate_id"],
            admitted="yes" if item["admitted"] else "no",
            residue_label=item["residue_label"],
            synthetic="yes" if item["synthetic_positive_control"] else "no",
        )
        for item in result["candidate_audits"]
    ]

    requirements = [f"- {item}" for item in result["gate_requirements"]]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T434 - Substrate-Law Admission Gate - v0.1 results",
            "",
            "> Recorded-tier admission gate. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. Synthetic positive controls are "
            "gate calibration only, not real substrate evidence.",
            "",
            "- Spec (frozen first): `tests/T434-substrate-law-admission-gate.md`",
            "- Model: `models/substrate_law_admission_gate.py`",
            "- Tests: `tests/test_substrate_law_admission_gate.py`",
            "- Artifact JSON: `results/T434-substrate-law-admission-gate-v0.1.json`",
            "- Run: `python -m pytest tests/test_substrate_law_admission_gate.py -q`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Gate Requirements",
            "",
            *requirements,
            "",
            "## Candidate Audit",
            "",
            "| candidate | admitted? | residue label | synthetic control? |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reusable admission gate for the post-T406 burden. The "
            "current T406 transition split is not admitted; transition-table "
            "restatements, post hoc laws, hidden labels, non-native observables, "
            "underpowered measurements, and fixed-accounting changes are rejected.",
            "",
            "Does not earn: a real substrate law, a physical-arrow theorem, a "
            "region-indexed discriminator success, a claim-ledger update, public "
            "posture movement, or cross-repo support.",
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
        json_path = results_dir / "T434-substrate-law-admission-gate-v0.1.json"
        md_path = results_dir / "T434-substrate-law-admission-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
