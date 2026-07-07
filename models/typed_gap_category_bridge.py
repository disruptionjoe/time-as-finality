"""T492 - typed gap category bridge.

T113 showed that a typed subobject of H0(G), not raw H0(G), classifies
phantom incomparability for order-pair gaps. T92 showed that T19-style unary
proposition gaps restrict under explicit typing and audit hypotheses.

This audit asks whether those two results share a common typed-gap schema or
whether they only rhyme at the level of H0 failure shape.

The answer is intentionally conservative: a minimal finite typed-gap schema is
supported, but section-object identity, raw H0 classification, cohomology,
physical torsion, consciousness, and complexity-class readings are blocked.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models.accessible_witness_gap_restriction import run_t92_analysis
from models.gap_presheaf_classification import run_t113_analysis


ARTIFACT = "T492-typed-gap-category-bridge-v0.1"
VERDICT = "COMMON_TYPED_GAP_SCHEMA_SUPPORTED_OBJECT_IDENTITY_BLOCKED"

SOURCE_T92 = "results/accessible-witness-gap-restriction-v0.1-results.md"
SOURCE_T113 = "results/gap-presheaf-classification-v0.1-results.md"
SOURCE_T89 = "tests/T89-accessible-witness-gap-lemma.md"
SOURCE_GAP_PROBLEM = "open-problems/gap-presheaf-classification.md"
SOURCE_AWGR_PROBLEM = "open-problems/accessible-witness-gap-restriction-theorem.md"

HONEST_CEILING = (
    "Finite typed-schema bridge only. T492 supports a common typed-gap schema "
    "for T113 order-pair phantom gaps and T92 unary proposition gaps, but blocks "
    "object identity, raw H0(G) classification, a general cohomology theorem, "
    "physical torsion language, consciousness claims, complexity-class claims, "
    "claim-ledger movement, public posture, and cross-repo support."
)


@dataclass(frozen=True)
class GapInstanceSummary:
    instance_id: str
    source: str
    carrier_kind: str
    target_kind: str
    typed_rule: str
    closure_status: str
    raw_gap_status: str
    positive_count: int
    control_count: int
    strongest_reading: str
    blocked_reading: str


@dataclass(frozen=True)
class BridgeCandidate:
    candidate_id: str
    description: str
    requires_same_carrier: bool
    requires_raw_h0_classifier: bool
    requires_common_schema_only: bool
    requires_t113_typed_exactness: bool
    requires_t92_restriction_closure: bool
    requires_controls_rejected: bool
    promotes_cohomology_or_torsion: bool = False
    promotes_consciousness_or_complexity: bool = False


@dataclass(frozen=True)
class CandidateEvaluation:
    candidate_id: str
    admitted: bool
    label: str
    reason: str
    candidate: BridgeCandidate


@dataclass(frozen=True)
class T492Result:
    artifact: str
    sources: dict[str, str]
    t113_summary: GapInstanceSummary
    t92_summary: GapInstanceSummary
    abstract_schema: tuple[str, ...]
    candidate_evaluations: tuple[CandidateEvaluation, ...]
    verdict: str
    reading: str
    no_identity_reasons: tuple[str, ...]
    claim_update: str
    open_blocker: str
    recommended_next: tuple[str, ...]
    honest_ceiling: str


def _summarize_t113() -> GapInstanceSummary:
    result = run_t113_analysis()
    control_count = sum(
        1
        for audit in result.section_audits
        if audit.classification
        in {"invalid_local_order_control", "noncanonical_ambient_diagnostic"}
    )
    return GapInstanceSummary(
        instance_id="t113_order_pair_phantom_gap",
        source=SOURCE_T113,
        carrier_kind="nonreflexive_order_pair_sections",
        target_kind="phantom_incomparability_witnesses",
        typed_rule=(
            "endpoint-accessible + canonical ambient completion + F(U) subset A(U) "
            "+ local incomparability"
        ),
        closure_status=(
            "FRP restriction closure preserved"
            if result.frp_restriction_closure_preserved
            else "restriction closure failed"
        ),
        raw_gap_status=(
            "raw H0(G) refuted as classifier"
            if not result.raw_h0_equals_phantoms
            else "raw H0(G) matched in this run"
        ),
        positive_count=len(result.typed_gap_sections),
        control_count=control_count,
        strongest_reading=result.best_supported,
        blocked_reading=(
            "Raw H0(G), physical torsion, GU validation, and general "
            "cohomology/sheafification readings remain blocked."
        ),
    )


def _summarize_t92() -> GapInstanceSummary:
    result = run_t92_analysis()
    positives = [
        audit
        for audit in result.audits
        if audit.classification == "conditional_theorem_witness"
    ]
    controls = [
        audit
        for audit in result.audits
        if audit.classification
        in {"semantic_relabeling_boundary", "audit_monotonicity_boundary"}
    ]
    positive_gap_entries = sum(
        len(row["G"])
        for audit in positives
        for row in audit.patch_table
    )
    return GapInstanceSummary(
        instance_id="t92_unary_accessible_witness_gap",
        source=SOURCE_T92,
        carrier_kind="unary_typed_proposition_sections",
        target_kind="accessible_witness_unauditability_gaps",
        typed_rule=(
            "ambient restriction + audit monotonicity + stable proposition typing"
        ),
        closure_status=result.theorem_status,
        raw_gap_status=(
            "not a raw T58 order-pair object; T92 uses typed proposition gaps"
        ),
        positive_count=positive_gap_entries,
        control_count=len(controls),
        strongest_reading=result.strongest_claim,
        blocked_reading=(
            "T92 does not identify T19 proposition gaps with T58 order-pair gaps "
            "and does not prove a consciousness or complexity-class result."
        ),
    )


def _bridge_candidates() -> tuple[BridgeCandidate, ...]:
    return (
        BridgeCandidate(
            candidate_id="common_minimal_typed_gap_schema",
            description=(
                "T113 and T92 share a finite typed-gap schema: patches, ambient "
                "object A, local/auditable subobject F, gap G=A-F, typed "
                "admissibility predicate, and restriction closure."
            ),
            requires_same_carrier=False,
            requires_raw_h0_classifier=False,
            requires_common_schema_only=True,
            requires_t113_typed_exactness=True,
            requires_t92_restriction_closure=True,
            requires_controls_rejected=True,
        ),
        BridgeCandidate(
            candidate_id="raw_h0_gap_identity",
            description="Raw H0(G) is the common classifier for both branches.",
            requires_same_carrier=False,
            requires_raw_h0_classifier=True,
            requires_common_schema_only=False,
            requires_t113_typed_exactness=False,
            requires_t92_restriction_closure=True,
            requires_controls_rejected=True,
        ),
        BridgeCandidate(
            candidate_id="same_section_object_identity",
            description="T113 and T92 use the same section object.",
            requires_same_carrier=True,
            requires_raw_h0_classifier=False,
            requires_common_schema_only=False,
            requires_t113_typed_exactness=True,
            requires_t92_restriction_closure=True,
            requires_controls_rejected=True,
        ),
        BridgeCandidate(
            candidate_id="cohomology_or_physical_torsion_promotion",
            description="The bridge promotes T92/T113 into cohomology or physical torsion language.",
            requires_same_carrier=False,
            requires_raw_h0_classifier=False,
            requires_common_schema_only=False,
            requires_t113_typed_exactness=True,
            requires_t92_restriction_closure=True,
            requires_controls_rejected=True,
            promotes_cohomology_or_torsion=True,
        ),
        BridgeCandidate(
            candidate_id="consciousness_or_complexity_promotion",
            description="The bridge promotes T92 into a consciousness or complexity-class claim.",
            requires_same_carrier=False,
            requires_raw_h0_classifier=False,
            requires_common_schema_only=False,
            requires_t113_typed_exactness=False,
            requires_t92_restriction_closure=True,
            requires_controls_rejected=True,
            promotes_consciousness_or_complexity=True,
        ),
        BridgeCandidate(
            candidate_id="semantic_relabeling_as_bridge",
            description="Semantic relabeling may identify proposition gaps with observer-state gaps.",
            requires_same_carrier=True,
            requires_raw_h0_classifier=False,
            requires_common_schema_only=False,
            requires_t113_typed_exactness=False,
            requires_t92_restriction_closure=False,
            requires_controls_rejected=False,
        ),
        BridgeCandidate(
            candidate_id="local_reversal_as_gap",
            description="Local reversal/conflict controls may count as typed gaps.",
            requires_same_carrier=False,
            requires_raw_h0_classifier=True,
            requires_common_schema_only=False,
            requires_t113_typed_exactness=False,
            requires_t92_restriction_closure=False,
            requires_controls_rejected=False,
        ),
    )


def _evaluate_candidate(
    candidate: BridgeCandidate,
    t113: GapInstanceSummary,
    t92: GapInstanceSummary,
) -> CandidateEvaluation:
    same_carrier = t113.carrier_kind == t92.carrier_kind
    t113_typed_exact = "typed subobject" in t113.strongest_reading
    t113_raw_ok = "refuted" not in t113.raw_gap_status
    t92_closure = t92.closure_status == "supported_with_explicit_boundaries"
    controls_rejected = t113.control_count >= 2 and t92.control_count >= 2

    failures: list[str] = []
    if candidate.requires_same_carrier and not same_carrier:
        failures.append("carrier_mismatch")
    if candidate.requires_raw_h0_classifier and not t113_raw_ok:
        failures.append("raw_h0_refuted_by_t113")
    if candidate.requires_t113_typed_exactness and not t113_typed_exact:
        failures.append("t113_typed_exactness_missing")
    if candidate.requires_t92_restriction_closure and not t92_closure:
        failures.append("t92_restriction_closure_missing")
    if candidate.requires_controls_rejected and not controls_rejected:
        failures.append("controls_not_rejected")
    if candidate.promotes_cohomology_or_torsion:
        failures.append("cohomology_torsion_promotion_blocked")
    if candidate.promotes_consciousness_or_complexity:
        failures.append("consciousness_complexity_promotion_blocked")

    if candidate.requires_common_schema_only and not failures:
        return CandidateEvaluation(
            candidate_id=candidate.candidate_id,
            admitted=True,
            label="ADMITTED_COMMON_TYPED_GAP_SCHEMA_NO_IDENTITY",
            reason=(
                "Both branches instantiate the same minimal finite schema while "
                "keeping carrier kind, target kind, and typing predicates distinct."
            ),
            candidate=candidate,
        )

    if failures:
        return CandidateEvaluation(
            candidate_id=candidate.candidate_id,
            admitted=False,
            label="REJECTED_" + "_".join(failures).upper(),
            reason="; ".join(failures),
            candidate=candidate,
        )

    return CandidateEvaluation(
        candidate_id=candidate.candidate_id,
        admitted=False,
        label="REJECTED_OVERCLAIM_NOT_SCHEMA_ONLY",
        reason=(
            "The candidate does not fail a low-level check, but it asks for more "
            "than the common finite typed-gap schema supports."
        ),
        candidate=candidate,
    )


def run() -> T492Result:
    t113 = _summarize_t113()
    t92 = _summarize_t92()
    evaluations = tuple(
        _evaluate_candidate(candidate, t113, t92)
        for candidate in _bridge_candidates()
    )
    admitted = [item for item in evaluations if item.admitted]

    abstract_schema = (
        "finite patch family with restriction maps",
        "ambient object A(U) of content fixed by the larger system",
        "local or auditable subobject F(U) with a declared inclusion into A(U)",
        "gap object G(U)=A(U)-F(U) or its typed subobject",
        "typed admissibility predicate tau selecting meaningful gap sections",
        "restriction closure rho(tau(G(U))) subset tau(G(V)) for V subset U",
        "domain-specific target interpretation kept outside the schema",
    )

    no_identity_reasons = (
        "T113 carriers are nonreflexive ordered event-pair sections; T92 carriers are unary typed proposition sections.",
        "T113 classifies phantom incomparability witnesses; T92 classifies accessible-witness unauditability gaps.",
        "T113's typing rule is endpoint/canonical/local-incomparability; T92's typing rule is ambient-restriction/audit-monotonicity/stable-proposition-typing.",
        "T113 refutes raw H0(G) as too broad, so a raw-gap identity cannot be the bridge.",
        "T92 explicitly blocks identifying T19 proposition gaps with T58 order-pair gaps.",
    )

    if len(admitted) == 1 and admitted[0].candidate_id == "common_minimal_typed_gap_schema":
        verdict = VERDICT
        reading = (
            "T113 and T92 share a common finite typed-gap schema, but not the "
            "same section object, classifier, or theorem target. The useful "
            "abstraction is a typed gap-system interface: A, F, G, restriction, "
            "and an admissibility predicate tau. The target interpretation stays "
            "domain-specific."
        )
    else:
        verdict = "TYPED_GAP_BRIDGE_UNRESOLVED"
        reading = "The audit did not isolate a clean common schema."

    return T492Result(
        artifact=ARTIFACT,
        sources={
            "t92": SOURCE_T92,
            "t113": SOURCE_T113,
            "t89": SOURCE_T89,
            "gap_presheaf_problem": SOURCE_GAP_PROBLEM,
            "accessible_witness_problem": SOURCE_AWGR_PROBLEM,
        },
        t113_summary=t113,
        t92_summary=t92,
        abstract_schema=abstract_schema,
        candidate_evaluations=evaluations,
        verdict=verdict,
        reading=reading,
        no_identity_reasons=no_identity_reasons,
        claim_update=(
            "none; C1/gap language may be sharpened only as a finite typed-gap "
            "schema shared across distinct section objects"
        ),
        open_blocker=(
            "T492 does not prove a general category theorem. A future result "
            "would need explicit morphisms between typed gap systems and a "
            "natural transformation or equivalence theorem, not just two "
            "instances of a schema."
        ),
        recommended_next=(
            "Use the typed-gap schema as a checklist for future T19/T58 bridge attempts.",
            "Do not use raw H0(G), physical torsion, cohomology, consciousness, or complexity-class language from T492.",
            "If this branch continues, define morphisms between typed gap systems and test a third carrier kind.",
        ),
        honest_ceiling=HONEST_CEILING,
    )


def t492_result_to_dict(result: T492Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "sources": result.sources,
        "t113_summary": asdict(result.t113_summary),
        "t92_summary": asdict(result.t92_summary),
        "abstract_schema": list(result.abstract_schema),
        "candidate_evaluations": [
            {
                "candidate_id": item.candidate_id,
                "admitted": item.admitted,
                "label": item.label,
                "reason": item.reason,
                "candidate": asdict(item.candidate),
            }
            for item in result.candidate_evaluations
        ],
        "verdict": result.verdict,
        "reading": result.reading,
        "no_identity_reasons": list(result.no_identity_reasons),
        "claim_update": result.claim_update,
        "open_blocker": result.open_blocker,
        "recommended_next": list(result.recommended_next),
        "honest_ceiling": result.honest_ceiling,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    eval_rows = [
        "| {candidate_id} | {admitted} | {label} | {reason} |".format(
            candidate_id=item["candidate_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["label"],
            reason=item["reason"],
        )
        for item in payload["candidate_evaluations"]
    ]
    schema_lines = [f"- {item}" for item in payload["abstract_schema"]]
    no_identity = [f"- {item}" for item in payload["no_identity_reasons"]]
    next_lines = [f"- {item}" for item in payload["recommended_next"]]

    return "\n".join(
        [
            "# T492 - Typed Gap Category Bridge - v0.1 results",
            "",
            "> Finite typed-schema bridge only. `CLAIM-LEDGER.md`, `ROADMAP.md`, "
            "`README.md`, North Star files, public posture, hard policy, and "
            "cross-repo truth are untouched.",
            "",
            "- Spec: `tests/T492-typed-gap-category-bridge.md`",
            "- Model: `models/typed_gap_category_bridge.py`",
            "- Tests: `tests/test_typed_gap_category_bridge.py`",
            "- Artifact JSON: `results/T492-typed-gap-category-bridge-v0.1.json`",
            "- Sources: T92, T113, T89, and the gap-presheaf / accessible-witness open problems",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["reading"],
            "",
            "## Abstract Schema",
            "",
            *schema_lines,
            "",
            "## Instance Summary",
            "",
            "| Instance | Carrier | Target | Positive count | Controls | Raw-gap status |",
            "| --- | --- | --- | ---: | ---: | --- |",
            "| {instance_id} | {carrier_kind} | {target_kind} | {positive_count} | {control_count} | {raw_gap_status} |".format(
                **payload["t113_summary"]
            ),
            "| {instance_id} | {carrier_kind} | {target_kind} | {positive_count} | {control_count} | {raw_gap_status} |".format(
                **payload["t92_summary"]
            ),
            "",
            "## Candidate Evaluation",
            "",
            "| Candidate | Admitted? | Label | Reason |",
            "| --- | --- | --- | --- |",
            *eval_rows,
            "",
            "## Why Identity Is Blocked",
            "",
            *no_identity,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a conservative typed-gap schema shared by T113 and T92, useful as "
            "a future bridge checklist.",
            "",
            "Does not earn: section-object identity, raw H0 classification, a "
            "general category theorem, cohomology, physical torsion, consciousness "
            "or complexity-class claims, claim-ledger movement, public posture, or "
            "cross-repo support.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Open Blocker",
            "",
            payload["open_blocker"],
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

    payload = t492_result_to_dict(run())
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T492-typed-gap-category-bridge-v0.1.json"
        md_path = results_dir / "T492-typed-gap-category-bridge-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
