"""T387: ten-persona gap audit for the T376-T386 relativity chain.

This audit asks whether the recent relativity-substrate ladder is missing any
important gap after T386. It is not a claim upgrade. It is a structured review
from ten different technical lenses, with the output reduced to prioritized
open objects and a recommended next goal.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PersonaLens:
    persona_id: str
    lens: str
    audit_question: str


@dataclass(frozen=True)
class PersonaFinding:
    persona_id: str
    gap_id: str
    severity: int
    finding: str
    why_it_matters: str
    proposed_next_test: str


@dataclass(frozen=True)
class GapSynthesis:
    gap_id: str
    status: str
    severity_score: int
    supporting_personas: tuple[str, ...]
    plain_english_gap: str
    recommended_action: str


@dataclass(frozen=True)
class T387Result:
    persona_count: int
    finding_count: int
    missing_anything: bool
    claim_upgrade_allowed: bool
    top_gap_ids: tuple[str, ...]
    known_open_gap_ids: tuple[str, ...]
    gap_syntheses: tuple[GapSynthesis, ...]
    persona_lenses: tuple[PersonaLens, ...]
    persona_findings: tuple[PersonaFinding, ...]
    recommended_next_goal: str
    overall_verdict: str
    strongest_plain_english_takeaway: str
    claim_ledger_update: str


def persona_lenses() -> tuple[PersonaLens, ...]:
    return (
        PersonaLens(
            "mathematical_formalist",
            "mathematical formalist",
            "Are the definitions strong enough to support theorem-like claims?",
        ),
        PersonaLens(
            "relativity_physicist",
            "relativity physicist",
            "Does the chain really produce relativistic structure rather than a protocol analogy?",
        ),
        PersonaLens(
            "distributed_systems_engineer",
            "distributed systems engineer",
            "Which protocol assumptions are being smuggled into compatibility?",
        ),
        PersonaLens(
            "category_sheaf_theorist",
            "category/sheaf theorist",
            "Does local compatibility glue into the claimed global observer structure?",
        ),
        PersonaLens(
            "information_theorist",
            "information theorist",
            "Where do channel capacity, signal units, and information bounds enter?",
        ),
        PersonaLens(
            "gauge_invariance_auditor",
            "gauge/coordinate auditor",
            "Which objects are invariant and which are gauge labels?",
        ),
        PersonaLens(
            "adversarial_security_reviewer",
            "adversarial/security reviewer",
            "Can spoofed, asymmetric, or corrupted attestations pass the screen?",
        ),
        PersonaLens(
            "minimality_auditor",
            "minimality/model-selection auditor",
            "Is minimality justified or only selected because it gives the desired basis?",
        ),
        PersonaLens(
            "experimental_falsification_designer",
            "experimental/falsification designer",
            "What positive and negative fixtures would discriminate the claim?",
        ),
        PersonaLens(
            "paper_reviewer",
            "paper reviewer",
            "What would a skeptical reviewer say is still unsupported?",
        ),
    )


def persona_findings() -> tuple[PersonaFinding, ...]:
    return (
        PersonaFinding(
            "mathematical_formalist",
            "mutual_attestability_semantics_origin",
            5,
            "T386 assumes a sharpened meaning of compatibility as mutual local attestability.",
            "Without a formal semantics for compatibility, the derivation remains conditional.",
            "Define raw, symmetric, mutual, and finalizable compatibility as separate finite predicates.",
        ),
        PersonaFinding(
            "mathematical_formalist",
            "catalog_completeness_boundary",
            3,
            "The protocol and adapter catalogs are targeted screens, not exhaustive classifications.",
            "A theorem-like statement needs either completeness conditions or explicit catalog scope.",
            "Add a catalog-scope lemma naming the allowed finite protocol features.",
        ),
        PersonaFinding(
            "relativity_physicist",
            "nullness_bilinearity_origin",
            5,
            "Two directed handshake legs are not automatically null directions with a bilinear interval.",
            "The current chain motivates two legs, but nullness and bilinearity are still separate premises.",
            "Screen whether mutual attestability plus invariance forces null primitive legs or only labels them.",
        ),
        PersonaFinding(
            "relativity_physicist",
            "higher_dimensional_extension",
            4,
            "The ladder is effectively 1+1; it does not yet explain a 3+1 or 14D-to-4D lift.",
            "A 1+1 signal basis may be a slice, not the full geometry.",
            "Build a fixture that distinguishes slice relativity from a higher-dimensional adapter projection.",
        ),
        PersonaFinding(
            "distributed_systems_engineer",
            "mutual_attestability_semantics_origin",
            5,
            "Acknowledgment protocols solve delivery semantics, not necessarily compatibility semantics.",
            "A send/ack loop can certify message exchange while saying little about record compatibility.",
            "Test compatibility as finalizable shared state, not just message receipt.",
        ),
        PersonaFinding(
            "distributed_systems_engineer",
            "failure_mode_semantics",
            4,
            "Timeout, retry, duplication, and partial failure are not yet part of the handshake origin screen.",
            "Distributed protocols need failure semantics before attestation can be treated as primitive.",
            "Add controls for delayed, duplicated, lost, and retried attestations.",
        ),
        PersonaFinding(
            "category_sheaf_theorist",
            "local_to_global_attestation_descent",
            4,
            "Local mutual attestations have not been shown to glue into a consistent observer family.",
            "Pairwise witnesses can conflict on overlaps unless descent or cocycle conditions are checked.",
            "Construct a three-observer overlap fixture with compatible and incompatible attestations.",
        ),
        PersonaFinding(
            "category_sheaf_theorist",
            "gauge_relabel_equivalence_proof",
            3,
            "Gauge-like relabeling is repeatedly marked partial, but no quotient proof is present.",
            "A relabeling that preserves all tests could be mistaken for new structure.",
            "Build an equivalence-class screen for relabel-only versus signal-bearing adapters.",
        ),
        PersonaFinding(
            "information_theorist",
            "signal_unit_capacity_origin",
            4,
            "The shared signal unit and speed-limit reading are not derived from information constraints.",
            "The current c = 1 normalization works only after a common signal unit is granted.",
            "Test whether finite information transfer bounds motivate a single invariant signal unit.",
        ),
        PersonaFinding(
            "information_theorist",
            "two_leg_to_null_signal_bridge",
            5,
            "A two-leg protocol gives two directions, but not yet why those directions are null signals.",
            "The bridge from communication legs to null geometry is the fragile step.",
            "Compare handshake legs that are causal-but-timelike, null, delayed, and noisy.",
        ),
        PersonaFinding(
            "gauge_invariance_auditor",
            "hidden_foliation_and_coordinate_import",
            4,
            "The screens reject obvious global clocks, but subtler hidden orderings still need controls.",
            "A protocol may encode an order parameter without naming it a clock.",
            "Add hidden-order controls using monotone counters, queues, or append indices.",
        ),
        PersonaFinding(
            "gauge_invariance_auditor",
            "gauge_relabel_equivalence_proof",
            4,
            "The distinction between observer transform, gauge relabel, and physical signal needs a quotient.",
            "Otherwise the model may count presentation changes as substrate structure.",
            "Create invariance checks under relabeling, reciprocal scaling, and endpoint renaming.",
        ),
        PersonaFinding(
            "adversarial_security_reviewer",
            "attestation_authenticity",
            4,
            "Mutual attestability assumes receipts are authentic and not spoofed or replayed.",
            "A false receipt can fake mutuality while breaking compatibility.",
            "Add spoof, replay, and equivocation controls for the attestation relation.",
        ),
        PersonaFinding(
            "adversarial_security_reviewer",
            "nonnegative_count_authenticity",
            3,
            "Signed counts are rejected, but forged nonnegative counts are not yet screened.",
            "Nonnegative does not imply trustworthy or source-owned.",
            "Test source ownership and provenance of nonnegative compatibility counts.",
        ),
        PersonaFinding(
            "minimality_auditor",
            "minimality_principle_origin",
            5,
            "Minimality is doing real work in selecting two legs over richer protocols.",
            "The model needs to explain why nature or the adapter should choose minimality.",
            "Screen minimality as compression, exact access, or no-redundant-witness principle.",
        ),
        PersonaFinding(
            "minimality_auditor",
            "catalog_completeness_boundary",
            3,
            "Targeted catalogs can miss a nonminimal protocol that reduces to the same invariant.",
            "The claim should say whether overcomplete protocols are impossible or merely redundant.",
            "Add reduction checks showing extra phases factor through the two-leg basis.",
        ),
        PersonaFinding(
            "experimental_falsification_designer",
            "discriminating_positive_controls",
            4,
            "The ladder has many negative controls, but needs sharper positive controls for mutuality.",
            "A good next screen should show exactly what mutual attestability adds over symmetry labels.",
            "Construct paired fixtures: symmetric scalar token, mutual receipt, and one-sided receipt.",
        ),
        PersonaFinding(
            "experimental_falsification_designer",
            "failure_mode_semantics",
            4,
            "Latency and retry behavior could turn a clean two-leg story into a family of partial protocols.",
            "Robustness under realistic protocol disturbances matters for the adapter reading.",
            "Add delay, retry, duplicate, and dropped-return controls.",
        ),
        PersonaFinding(
            "paper_reviewer",
            "claim_boundary_packaging",
            4,
            "The paper-facing claim needs a crisp hierarchy of assumptions and derived outputs.",
            "Readers will reject the result if conditional premises are scattered across tests.",
            "Write a theorem ledger that separates derived, motivated, imported, and open objects.",
        ),
        PersonaFinding(
            "paper_reviewer",
            "mutual_attestability_semantics_origin",
            5,
            "A reviewer will ask why compatibility should mean mutual attestability at all.",
            "This is now the highest-leverage objection after T386.",
            "Make the next goal a mutual-attestability semantics origin screen.",
        ),
    )


GAP_TEXT: dict[str, tuple[str, str]] = {
    "mutual_attestability_semantics_origin": (
        "The chain now depends on compatibility meaning mutual local attestability.",
        "Next, test whether record-finality semantics force mutual attestability or merely allow it.",
    ),
    "nullness_bilinearity_origin": (
        "Two directed legs do not yet explain why primitive legs are null or why the interval is bilinear.",
        "Screen nullness and bilinearity as separate origins after the mutuality semantics pass.",
    ),
    "two_leg_to_null_signal_bridge": (
        "The bridge from a two-leg protocol to two null signal directions is still fragile.",
        "Compare two-leg protocols that are null, timelike, delayed, noisy, or only causal.",
    ),
    "minimality_principle_origin": (
        "Minimality selects the clean two-leg answer, but minimality itself is not derived.",
        "Test minimality as compression, exact-access, or no-redundant-witness pressure.",
    ),
    "local_to_global_attestation_descent": (
        "Pairwise mutual attestations may not glue into a consistent multi-observer structure.",
        "Build an overlap/descent fixture for three or more observers.",
    ),
    "higher_dimensional_extension": (
        "The current ladder is mostly 1+1 and may be only a slice of the intended geometry.",
        "Test whether the two-null basis is a slice, projection, or adapter face of a higher-dimensional system.",
    ),
    "failure_mode_semantics": (
        "Timeout, retry, duplication, dropped returns, and delays are not in the origin screen.",
        "Add disturbance controls for realistic handshake protocols.",
    ),
    "gauge_relabel_equivalence_proof": (
        "Gauge relabeling is marked partial, but the quotient/invariance proof is not explicit.",
        "Create a relabel-equivalence screen separating labels from physical signal structure.",
    ),
    "hidden_foliation_and_coordinate_import": (
        "A protocol can hide a global order without calling it a clock.",
        "Add controls for monotone counters, queues, append order, and implicit foliations.",
    ),
    "signal_unit_capacity_origin": (
        "The invariant signal unit remains granted rather than derived from information constraints.",
        "Screen whether finite transfer capacity motivates a shared signal unit.",
    ),
    "attestation_authenticity": (
        "Mutual receipts can be spoofed, replayed, or equivocated.",
        "Add spoof, replay, equivocation, receipt-authenticity, and provenance controls.",
    ),
    "nonnegative_count_authenticity": (
        "Nonnegative counts can still be forged or unowned.",
        "Test source ownership and provenance for nonnegative primitive counts.",
    ),
    "discriminating_positive_controls": (
        "The ladder needs sharper positives for exactly what mutuality contributes.",
        "Build matched scalar, one-sided, symmetric-label, and mutual-receipt fixtures.",
    ),
    "catalog_completeness_boundary": (
        "The screens are targeted catalogs, not exhaustive classifications.",
        "State catalog scope and add reduction checks for overcomplete variants.",
    ),
    "claim_boundary_packaging": (
        "The derived, motivated, imported, and open objects need paper-facing separation.",
        "Write a theorem ledger after the next semantics-origin screen.",
    ),
}


TOP_GAPS = (
    "mutual_attestability_semantics_origin",
    "nullness_bilinearity_origin",
    "two_leg_to_null_signal_bridge",
    "minimality_principle_origin",
    "local_to_global_attestation_descent",
)


KNOWN_OPEN_GAPS = (
    "nullness_bilinearity_origin",
    "higher_dimensional_extension",
    "catalog_completeness_boundary",
    "claim_boundary_packaging",
)


def synthesize_gaps(findings: tuple[PersonaFinding, ...]) -> tuple[GapSynthesis, ...]:
    ordered_gap_ids: list[str] = []
    by_gap: dict[str, list[PersonaFinding]] = {}
    for finding in findings:
        by_gap.setdefault(finding.gap_id, []).append(finding)
        if finding.gap_id not in ordered_gap_ids:
            ordered_gap_ids.append(finding.gap_id)

    syntheses: list[GapSynthesis] = []
    for gap_id in ordered_gap_ids:
        grouped = by_gap[gap_id]
        severity_score = sum(finding.severity for finding in grouped)
        status = "top_priority" if gap_id in TOP_GAPS else "important"
        if gap_id in KNOWN_OPEN_GAPS:
            status = "known_open_object"
        supporting_personas = tuple(finding.persona_id for finding in grouped)
        plain_gap, action = GAP_TEXT[gap_id]
        syntheses.append(
            GapSynthesis(
                gap_id=gap_id,
                status=status,
                severity_score=severity_score,
                supporting_personas=supporting_personas,
                plain_english_gap=plain_gap,
                recommended_action=action,
            )
        )
    return tuple(syntheses)


def run_t387_analysis() -> T387Result:
    lenses = persona_lenses()
    findings = persona_findings()
    syntheses = synthesize_gaps(findings)
    return T387Result(
        persona_count=len(lenses),
        finding_count=len(findings),
        missing_anything=True,
        claim_upgrade_allowed=False,
        top_gap_ids=TOP_GAPS,
        known_open_gap_ids=KNOWN_OPEN_GAPS,
        gap_syntheses=syntheses,
        persona_lenses=lenses,
        persona_findings=findings,
        recommended_next_goal=(
            "T388 mutual-attestability semantics origin screen: test whether "
            "record-finality compatibility requires mutual local attestability, "
            "with controls for scalar tokens, symmetric labels, one-sided readout, "
            "global reconciliation, spoofed receipts, and asymmetric persistence."
        ),
        overall_verdict="ten_persona_audit_finds_no_claim_upgrade_but_prioritizes_mutual_attestability_semantics",
        strongest_plain_english_takeaway=(
            "The ladder is not obviously broken, but it is still conditional. The main thing "
            "we may be missing is a derivation of why compatibility should mean mutual local "
            "attestability. Close behind are the bridge from two protocol legs to null "
            "geometry, the origin of bilinearity, the justification for minimality, and "
            "multi-observer descent."
        ),
        claim_ledger_update=(
            "Register T387 as a persona audit: no claim upgrade; next work should attack "
            "mutual_attestability_semantics_origin before paper-facing synthesis."
        ),
    )


def t387_result_to_dict(result: T387Result) -> dict[str, object]:
    return {
        "persona_count": result.persona_count,
        "finding_count": result.finding_count,
        "missing_anything": result.missing_anything,
        "claim_upgrade_allowed": result.claim_upgrade_allowed,
        "top_gap_ids": list(result.top_gap_ids),
        "known_open_gap_ids": list(result.known_open_gap_ids),
        "gap_syntheses": [
            {
                "gap_id": gap.gap_id,
                "status": gap.status,
                "severity_score": gap.severity_score,
                "supporting_personas": list(gap.supporting_personas),
                "plain_english_gap": gap.plain_english_gap,
                "recommended_action": gap.recommended_action,
            }
            for gap in result.gap_syntheses
        ],
        "persona_lenses": [
            {
                "persona_id": lens.persona_id,
                "lens": lens.lens,
                "audit_question": lens.audit_question,
            }
            for lens in result.persona_lenses
        ],
        "persona_findings": [
            {
                "persona_id": finding.persona_id,
                "gap_id": finding.gap_id,
                "severity": finding.severity,
                "finding": finding.finding,
                "why_it_matters": finding.why_it_matters,
                "proposed_next_test": finding.proposed_next_test,
            }
            for finding in result.persona_findings
        ],
        "recommended_next_goal": result.recommended_next_goal,
        "overall_verdict": result.overall_verdict,
        "strongest_plain_english_takeaway": result.strongest_plain_english_takeaway,
        "claim_ledger_update": result.claim_ledger_update,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t387_result_to_dict(run_t387_analysis()), indent=2))
