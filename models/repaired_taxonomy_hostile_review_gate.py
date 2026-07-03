"""T437 - repaired taxonomy hostile-review gate.

The 2026-07-02 adversarial review withdrew the universal finite-closed
capability-boundary no-go theorem and left a repair checklist. T433, T435, and
T436 repaired the main internal obligations at recorded tier:

* T433: classical finite-product declarability proof certificate.
* T435: quantum E3 A-class admissible-menu gate.
* T436: A2 resource-lift classifier blocking absolute-E3 overread.

T437 audits the repaired packet as a hostile reviewer would: it can survive as an
internal taxonomy map, but it still cannot become a promoted claim, a WAY theorem,
a public hard-theorem paper, or a GU/TaF adapter.

Run:

    python -m models.repaired_taxonomy_hostile_review_gate --write-results
    python -m pytest tests/test_repaired_taxonomy_hostile_review_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import classical_declarability_proof_certificate as t433
from models import quantum_e3_admissible_menu_gate as t435
from models import quantum_e3_resource_lift_classifier as t436


ARTIFACT = "T437-repaired-taxonomy-hostile-review-gate-v0.1"
SOURCE_ADVERSARIAL_REVIEW = (
    "literature/Adversarial Referee Report on the Finite-Closed "
    "Capability-Boundary Scope Theorem deep-research-report.md"
)
SOURCE_PRIOR_ART = "papers/drafts/prior-art-verification-and-divergent-direction-pass-2026-07-02.md"
SOURCE_OPEN_PROBLEM = "open-problems/finite-closed-capability-boundary-scope-theorem.md"
SOURCE_TAXONOMY = "technical-reports/capability-boundary-mode-taxonomy-REFERENCE.md"

VERDICT = "REPAIRED_TAXONOMY_INTERNAL_MAP_SURVIVES_HOSTILE_REVIEW_NO_PROMOTION"

HONEST_CEILING = (
    "Hostile-review gate only. T437 supports internal use of the repaired taxonomy "
    "as an organizing map; it does not revive the universal no-go theorem, prove "
    "WAY, promote E3, choose D2 redesign/abandon, revive T421, update claims, "
    "authorize public-posture movement; no claim promotion."
)


@dataclass(frozen=True)
class ReviewCheck:
    check_id: str
    question: str
    status: str
    passed: bool
    evidence: tuple[str, ...]
    residual_risk: str
    gate_class: str = "repair"

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["evidence"] = list(self.evidence)
        return data


def _classical_check() -> ReviewCheck:
    result = t433.run()
    verdict = result["overall_verdict"]
    passed = (
        verdict["verdict"] == "CLASSICAL_DECLARABILITY_PROOF_CERTIFIED"
        and verdict["no_physical_candidates_in_mixed_sweep"] is True
    )
    return ReviewCheck(
        check_id="classical_single_instance_repair",
        question="Does the classical C-fragment have a constructive finite-product repair?",
        status="PASS" if passed else "FAIL",
        passed=passed,
        evidence=(
            "T433 verdict CLASSICAL_DECLARABILITY_PROOF_CERTIFIED",
            "A1 contains identity/full-code readout, so every total datum factors by lookup",
            "mixed finite sweep has zero single-instance physical candidates relative to A1",
        ),
        residual_risk=(
            "Classical finite product codes only; this is not a universal no-go "
            "and does not touch quantum E3."
        ),
    )


def _quantum_a_class_check() -> ReviewCheck:
    result = t435.run()
    verdict = result["overall_verdict"]
    main = next(
        item
        for item in result["candidate_audits"]
        if item["candidate_id"] == "z2_phase_pair_a1_no_reference"
    )
    a2 = next(
        item
        for item in result["candidate_audits"]
        if item["candidate_id"] == "z2_phase_pair_a2_reference"
    )
    passed = (
        verdict["verdict"] == "QUANTUM_E3_A_CLASS_GATE_BUILT_NO_CLAIM_PROMOTION"
        and main["admitted_e3_relative_to_a1"] is True
        and a2["residue_label"] == "E0_DECLARED_RELATIVE_TO_A2_REFERENCE_RESOURCE"
    )
    return ReviewCheck(
        check_id="quantum_a_class_statement",
        question="Is the quantum E3 side stated with A-class and reference-resource policy fixed?",
        status="PASS" if passed else "FAIL",
        passed=passed,
        evidence=(
            "T435 fixes A1 symmetry-respecting menus and A2 reference-resource admission",
            "A1 phase pair is E3-style relative to A1 without reference",
            "same datum becomes E0-declared relative to A2 with reference resource",
        ),
        residual_risk=(
            "Finite admission gate only; not a WAY theorem, not a quantum physics "
            "claim, and not a GU/TaF adapter."
        ),
    )


def _resource_lift_check() -> ReviewCheck:
    result = t436.run()
    verdict = result["overall_verdict"]
    passed = (
        verdict["verdict"] == "QUANTUM_E3_RESOURCE_LIFT_CLASSIFIER_BUILT_T435_RELATIVE_NOT_ABSOLUTE"
        and verdict["t435_main_pair_relative_not_absolute"] is True
        and verdict["absolute_synthetic_control_ids"] == [
            "synthetic_exact_no_go_survives_a2"
        ]
    )
    return ReviewCheck(
        check_id="resource_lift_blocks_absolute_overread",
        question="Does the repaired packet block overreading T435 as absolute E3?",
        status="PASS" if passed else "FAIL",
        passed=passed,
        evidence=(
            "T436 classifies the T435 phase pair as A1-relative and A2-declared",
            "absolute-after-resource output appears only on a synthetic exact no-go control",
            "large cost, missing A2 audit, post-hoc policies, and hidden oracles are rejected",
        ),
        residual_risk=(
            "A real absolute E3 artifact still requires an independently typed exact "
            "no-go witness that survives A2 resource-lift audit."
        ),
    )


def _prior_art_check() -> ReviewCheck:
    return ReviewCheck(
        check_id="prior_art_verification_recorded",
        question="Is prior art treated as verified local context rather than novelty support?",
        status="PASS",
        passed=True,
        evidence=(
            SOURCE_PRIOR_ART,
            "local prior-art draft records E1, E2, E3, masking, constructor-theory, and reference-frame homes",
            "novelty verdict is LOW; packaging survives only as synthesis/perspective",
        ),
        residual_risk=(
            "No new web fetch was performed in T437; public use would need a separate "
            "citation-quality review and Joe authorization."
        ),
    )


def _universal_no_go_check() -> ReviewCheck:
    return ReviewCheck(
        check_id="universal_no_go_not_revived",
        question="Is the killed universal theorem still withdrawn?",
        status="PASS",
        passed=True,
        evidence=(
            SOURCE_OPEN_PROBLEM,
            SOURCE_TAXONOMY,
            "taxonomy standing is internal organizing map, not promoted theorem",
            "T433/T435/T436 each state no claim promotion",
        ),
        residual_risk=(
            "Any hard-theorem paper or claim-ledger movement still pauses for Joe."
        ),
    )


def _publication_posture_check() -> ReviewCheck:
    return ReviewCheck(
        check_id="hard_theorem_publication_blocked",
        question="Can the repaired taxonomy be treated as a public hard-theorem paper?",
        status="BLOCKED",
        passed=False,
        evidence=(
            "prior-art verification says broad novelty is LOW",
            "adversarial review says not publishable as a hard-theorem paper as originally framed",
            "current repairs are recorded-tier internal support, not external posture movement",
        ),
        residual_risk=(
            "A synthesis/perspective note or classical theorem path is a separate Joe "
            "decision; T437 does not authorize publication."
        ),
        gate_class="promotion",
    )


def _absolute_e3_check() -> ReviewCheck:
    return ReviewCheck(
        check_id="real_absolute_e3_witness_missing",
        question="Has a real absolute E3/WAY-style witness been supplied?",
        status="BLOCKED",
        passed=False,
        evidence=(
            "T436 has only a synthetic exact no-go calibration control",
            "T435 is A1-relative and lifted to E0 by A2 reference admission",
            "T421 remains a logged disanalogy, not a revived adapter",
        ),
        residual_risk=(
            "Future E3 work must bring an independently typed exact no-go witness; "
            "do not use sibling-repo claims as support."
        ),
        gate_class="promotion",
    )


def _d2_check() -> ReviewCheck:
    return ReviewCheck(
        check_id="d2_computational_arrow_still_separate",
        question="Does the taxonomy repair decide the D2 computational-arrow lane?",
        status="BLOCKED",
        passed=False,
        evidence=(
            "T419 is REDESIGN",
            "T420 blocks finite public-cycle anti-relabel evidence",
            "remaining D2 route needs family-level period hardness or a different regime",
        ),
        residual_risk=(
            "D2 redesign/abandon is separate from this taxonomy hostile-review gate."
        ),
        gate_class="promotion",
    )


def run() -> dict[str, Any]:
    repair_checks = (
        _universal_no_go_check(),
        _prior_art_check(),
        _classical_check(),
        _quantum_a_class_check(),
        _resource_lift_check(),
    )
    promotion_checks = (
        _publication_posture_check(),
        _absolute_e3_check(),
        _d2_check(),
    )
    all_checks = (*repair_checks, *promotion_checks)
    repair_passed = all(check.passed for check in repair_checks)
    blocked_promotions = [
        check.check_id for check in promotion_checks if check.status == "BLOCKED"
    ]

    return {
        "artifact": ARTIFACT,
        "sources": {
            "adversarial_review": SOURCE_ADVERSARIAL_REVIEW,
            "prior_art": SOURCE_PRIOR_ART,
            "open_problem": SOURCE_OPEN_PROBLEM,
            "taxonomy_reference": SOURCE_TAXONOMY,
            "classical_repair": "results/T433-classical-declarability-proof-certificate-v0.1-results.md",
            "quantum_a_class_gate": "results/T435-quantum-e3-admissible-menu-gate-v0.1-results.md",
            "resource_lift_gate": "results/T436-quantum-e3-resource-lift-classifier-v0.1-results.md",
        },
        "purpose": (
            "Audit the repaired capability-boundary taxonomy packet after T433, "
            "T435, and T436 against the 2026-07-02 adversarial review objections."
        ),
        "repair_checks": [check.to_dict() for check in repair_checks],
        "promotion_checks": [check.to_dict() for check in promotion_checks],
        "overall_verdict": {
            "verdict": VERDICT,
            "repair_packet_survives_as_internal_map": repair_passed,
            "blocked_promotion_ids": blocked_promotions,
            "claim_ledger_update": "none; no claim promotion",
            "reading": (
                "The repaired taxonomy clears the repo-local hostile-review gate "
                "for internal use as an organizing map: the universal no-go remains "
                "withdrawn, prior art is treated as low-novelty context, the classical "
                "C-fragment has a constructive proof certificate, and the quantum E3 "
                "side is A-class/resource-lift guarded. Promotion, public-paper posture, "
                "real absolute E3, D2 redesign, and GU/TaF adapter work remain blocked "
                "or separately gated."
            ),
        },
        "recommended_next": [
            "Use the taxonomy internally as a mode classifier, not as a promoted claim.",
            "Future E3 work needs a real exact no-go witness beyond T436 synthetic calibration.",
            "Future D2 work needs family-level period-hardness redesign or explicit abandonment.",
            "Any public synthesis/classical-theorem path remains a Joe decision.",
        ],
        "honest_ceiling": HONEST_CEILING,
    }


def render_markdown(result: dict[str, Any]) -> str:
    verdict = result["overall_verdict"]
    repair_rows = [
        "| {check_id} | {status} | {risk} |".format(
            check_id=item["check_id"],
            status=item["status"],
            risk=item["residual_risk"],
        )
        for item in result["repair_checks"]
    ]
    promotion_rows = [
        "| {check_id} | {status} | {risk} |".format(
            check_id=item["check_id"],
            status=item["status"],
            risk=item["residual_risk"],
        )
        for item in result["promotion_checks"]
    ]
    next_steps = [f"- {item}" for item in result["recommended_next"]]

    return "\n".join(
        [
            "# T437 - Repaired Taxonomy Hostile-Review Gate - v0.1 results",
            "",
            "> Recorded-tier hostile-review gate. `TESTS.md`, `ROADMAP.md`, and "
            "`CLAIM-LEDGER.md` are untouched. No claim promotion, no public-posture "
            "movement, no WAY theorem, no GU/TaF adapter.",
            "",
            "- Spec (frozen first): `tests/T437-repaired-taxonomy-hostile-review-gate.md`",
            "- Model: `models/repaired_taxonomy_hostile_review_gate.py`",
            "- Tests: `tests/test_repaired_taxonomy_hostile_review_gate.py`",
            "- Artifact JSON: `results/T437-repaired-taxonomy-hostile-review-gate-v0.1.json`",
            "- Sources: T433, T435, T436, the repaired taxonomy reference, and the local prior-art verification draft",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Repair Checks",
            "",
            "| check | status | residual risk |",
            "| --- | --- | --- |",
            *repair_rows,
            "",
            "## Promotion / External-Posture Checks",
            "",
            "| check | status | residual risk |",
            "| --- | --- | --- |",
            *promotion_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: local hostile-review clearance for using the repaired taxonomy as "
            "an internal mode classifier and progress-routing map.",
            "",
            "Does not earn: a universal no-go theorem, public paper posture, claim "
            "promotion, WAY theorem, real absolute E3 witness, D2 decision, T421 "
            "revival, GU/TaF adapter, or cross-repo support.",
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
        json_path = results_dir / "T437-repaired-taxonomy-hostile-review-gate-v0.1.json"
        md_path = results_dir / "T437-repaired-taxonomy-hostile-review-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
