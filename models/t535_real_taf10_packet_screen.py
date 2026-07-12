"""T535 - real TAF10 packet screen.

T535 tries to replace T533's synthetic future C(R) surplus target with a real
packet shape drawn from existing repo material. It consumes the T533 classifier
criteria for the full-stack match and independent noncompletion witness checks.

This screen does not prove a C(R) success. It classifies existing-source packet
families and names the exact missing field if no real packet clears.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import t533_cr_surplus_starter_packet_classifier as t533


ARTIFACT = "T535-real-taf10-packet-screen-v0.1"
VERDICT = "NO_REAL_TAF10_PACKET_IN_HAND_PAUSE"
T533_CRITERIA_SOURCE = t533.ARTIFACT

HONEST_CEILING = (
    "T535 is a Track-2 screen only. It does not prove a C(R) success, does "
    "not replace the Track-1 source-law question, does not move claims, canon, "
    "roadmap, North Star, public posture, hard policy, external publication, "
    "or cross-repo truth."
)

EXACT_MISSING_FIELD = (
    "a real data-bearing packet with reproducible exact-match certificates for "
    "full competency, resource, permission, and provenance profiles, plus a "
    "predeclared domain-native non-task-success noncompletion witness whose "
    "split is independent of those profiles and is not absorbed as a resource, "
    "competency, permission, provenance, joint-record, or completion field"
)

SOURCE_PATHS = {
    "t407": "results/T407-region-capability-no-go-v0.1.json",
    "t398": "results/T398-resource-profile-absorber-v0.1.json",
    "t411": "results/T411-departed-record-capability-discriminator-v0.1.json",
    "t412": "results/T412-separator-refactorization-gate-v0.1.json",
    "t493": "results/T493-levin-competency-cr-absorber-gate-v0.1.json",
    "t494": "results/T494-levin-fields-primary-source-absorber-gate-v0.1.json",
    "t516": "results/T516-isotropic-shareability-closed-form-v0.1.json",
    "t517": "results/T517-monogamy-wall-bft-threshold-v0.1.json",
    "t519": "results/T519-quantum-darwinism-replication-invariant-gate-v0.1.json",
    "t520": "results/T520-copy-law-single-use-key-absorber-screen-v0.1.json",
    "t521": "results/T521-detector-manifest-template-gate-v0.1.json",
}


@dataclass(frozen=True)
class ExistingSourceCandidate:
    candidate_id: str
    source_family: str
    source_keys: tuple[str, ...]
    source_basis: str
    t533_packet: t533.Packet
    data_bearing_packet: bool
    known_absorber: str
    intended_taf10_reading: str
    useful_remainder: str
    expected_outcome: str


@dataclass(frozen=True)
class CandidateClassification:
    candidate_id: str
    source_family: str
    outcome: str
    t533_label: str
    full_stack_exact_match: bool
    independent_noncompletion_witness: bool
    data_bearing_packet: bool
    source_json_present: bool
    known_absorber: str
    missing_fields: tuple[str, ...]
    reason: str
    useful_remainder: str


def _load_json(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def source_floor() -> dict[str, Any]:
    loaded = {key: _load_json(path) for key, path in SOURCE_PATHS.items()}
    return {
        "t533_criteria_source": T533_CRITERIA_SOURCE,
        "source_paths": dict(SOURCE_PATHS),
        "source_artifacts": {
            key: data.get("artifact")
            or data.get("artifact_id")
            or data.get("model")
            or "unknown"
            for key, data in loaded.items()
        },
        "source_verdicts": {
            "t398": loaded["t398"]["absorber_verdict"],
            "t412": loaded["t412"]["verdict"],
            "t493": loaded["t493"]["overall_verdict"]["verdict"],
            "t494": loaded["t494"]["overall_verdict"]["verdict"],
            "t520": loaded["t520"]["verdict"],
            "t521": loaded["t521"]["verdict"],
        },
        "computed_source_flags": {
            "t398_capability_factors_through_resource_profile": loaded["t398"][
                "factorization_audit"
            ]["capability_factors_through_resource_profile"],
            "t398_same_resource_capability_splits": loaded["t398"][
                "factorization_audit"
            ]["same_resource_capability_splits"],
            "t493_full_profile_absorbs_current_c_r": loaded["t493"][
                "overall_verdict"
            ]["full_profile_absorbs_current_c_r"],
            "t494_primary_source_scope_checked": loaded["t494"]["overall_verdict"][
                "n16_upgraded_for_bounded_scope"
            ],
            "t520_resource_reproduces_all_scenarios": all(
                row["reproduced_by_resource_ledger"]
                for row in loaded["t520"]["scenarios"]
            ),
            "t521_template_has_no_data_boundary": loaded["t521"][
                "has_no_data_boundary"
            ],
            "t521_has_observed_value_commitment": loaded["t521"][
                "has_observed_value_commitment"
            ],
        },
        "t533_absorber_floor": t533.absorber_floor(),
    }


def _cert(layer: str, values: tuple[str, ...]) -> t533.ProfileCertificate:
    return t533.ProfileCertificate(
        layer=layer,
        left_profile=values,
        right_profile=values,
        certificate_source=f"existing_source_exact_{layer}_match",
    )


def _mismatch(
    layer: str,
    left: tuple[str, ...],
    right: tuple[str, ...],
) -> t533.ProfileCertificate:
    return t533.ProfileCertificate(
        layer=layer,
        left_profile=left,
        right_profile=right,
        certificate_source=f"existing_source_{layer}_mismatch",
    )


def candidates() -> tuple[ExistingSourceCandidate, ...]:
    matched_permission = _cert(
        "permission_profile",
        ("declared_region=R", "declared_menu=fixed", "boundary_policy=fixed"),
    )
    matched_provenance = _cert(
        "provenance_profile",
        ("source_artifacts=checked", "result_json=present", "predecessor_chain=declared"),
    )

    return (
        ExistingSourceCandidate(
            candidate_id="t407_t398_t493_t494_current_cr_family",
            source_family="T407/T398/T493/T494 current C(R) family",
            source_keys=("t407", "t398", "t493", "t494"),
            source_basis=(
                "T407 realizes flat declared statistics with capability-profile "
                "spread; T398 and T493/T494 absorb the current reading once "
                "resource and full competency profiles are admitted."
            ),
            t533_packet=t533.Packet(
                packet_id="t407_t398_t493_t494_current_cr_family",
                description="Current C(R) family reread as a TAF10 surplus packet.",
                fixed_region_menu_task_context=True,
                checks_t500_t529_floor=True,
                competency=_mismatch(
                    "full_competency_profile",
                    ("undo_cross=pass", "class_readout=2/3"),
                    ("undo_cross=fail", "class_readout=1"),
                ),
                resource=_mismatch("resource_profile", ("U2_R0",), ("U0_R3",)),
                permission=matched_permission,
                provenance=matched_provenance,
                witness=t533.NoncompletionWitness(
                    witness_id="t407_capability_profile_split",
                    capability_kind="task_success_coordinate",
                    left_value="undo_cross_pass",
                    right_value="undo_cross_fail",
                    predeclared=True,
                    domain_native=True,
                    independent_from_stack_profiles=False,
                    not_task_success_coordinate=False,
                    not_completion_field=True,
                ),
            ),
            data_bearing_packet=True,
            known_absorber="resource profile and full competency profile completion",
            intended_taf10_reading="surplus over simple observed statistics",
            useful_remainder="review material over simple statistics only",
            expected_outcome="REVIEW_ONLY",
        ),
        ExistingSourceCandidate(
            candidate_id="t411_t412_departed_record_boundary_family",
            source_family="T411/T412 physical-boundary lineage",
            source_keys=("t411", "t412"),
            source_basis=(
                "T411 supplied an exact finite witness before review; the later "
                "addendum absorbs the physical-boundary reading by joint-record "
                "completion, and T412 requires an admissible factorization guardrail."
            ),
            t533_packet=t533.Packet(
                packet_id="t411_t412_departed_record_boundary_family",
                description="Departed-record boundary reread as a TAF10 packet.",
                fixed_region_menu_task_context=True,
                checks_t500_t529_floor=True,
                competency=_mismatch(
                    "full_competency_profile",
                    ("restorable_at_R_plus=true",),
                    ("restorable_at_R_plus=false",),
                ),
                resource=_mismatch(
                    "resource_profile",
                    ("reach=R_plus_with_retained_tier1",),
                    ("reach=R_plus_product_completion",),
                ),
                permission=_mismatch(
                    "permission_profile",
                    ("R_excludes_copresent_tier1",),
                    ("joint_record_completion_admitted",),
                ),
                provenance=_mismatch(
                    "provenance_profile",
                    ("cascade_history=retained_correlation",),
                    ("cascade_history=departed_trace",),
                ),
                witness=t533.NoncompletionWitness(
                    witness_id="t411_restoration_finality_split",
                    capability_kind="restoration_task_success",
                    left_value="restorable_at_R_plus",
                    right_value="final_at_R_plus",
                    predeclared=True,
                    domain_native=True,
                    independent_from_stack_profiles=False,
                    not_task_success_coordinate=False,
                    not_completion_field=False,
                ),
            ),
            data_bearing_packet=True,
            known_absorber="joint-record completion and declared-boundary bookkeeping",
            intended_taf10_reading="physical noncompletion after R-supported equality",
            useful_remainder="certificate toolkit calibration, not a TAF10 packet",
            expected_outcome="FALSIFIED",
        ),
        ExistingSourceCandidate(
            candidate_id="t516_t517_t519_quantum_access_monogamy_lane",
            source_family="T514-T520 quantum access and monogamy lane",
            source_keys=("t516", "t517", "t519"),
            source_basis=(
                "The quantum lane preserves a real access-structure strut, but "
                "T517 falsifies the BFT threshold correspondence and T519 keeps "
                "the replication invariant translation-only."
            ),
            t533_packet=t533.Packet(
                packet_id="t516_t517_t519_quantum_access_monogamy_lane",
                description="Quantum access/monogamy lane reread as a C(R) packet.",
                fixed_region_menu_task_context=False,
                checks_t500_t529_floor=True,
                competency=None,
                resource=_cert(
                    "resource_profile",
                    ("shareability_wall=closed_form", "replication=translation_only"),
                ),
                permission=None,
                provenance=matched_provenance,
                witness=None,
            ),
            data_bearing_packet=True,
            known_absorber="not a C(R) packet; routes to TAF6 rather than TAF10",
            intended_taf10_reading="quantum access noncompletion target",
            useful_remainder="narrowed successor for TAF6 access-structure work",
            expected_outcome="NARROWED",
        ),
        ExistingSourceCandidate(
            candidate_id="t520_single_use_key_copy_law_packet",
            source_family="T520 copy-law single-use-key screen",
            source_keys=("t520",),
            source_basis=(
                "T520 supplies a real single-use-key quantity, but the finality "
                "verdict vector equals the resource ledger vector in every scenario."
            ),
            t533_packet=t533.Packet(
                packet_id="t520_single_use_key_copy_law_packet",
                description="Single-use-key authority reread as noncompletion.",
                fixed_region_menu_task_context=True,
                checks_t500_t529_floor=True,
                competency=_mismatch(
                    "full_competency_profile",
                    ("can_finalize_now=true", "max_authoritative_copies=1"),
                    ("can_finalize_now=false", "max_authoritative_copies=0"),
                ),
                resource=_mismatch(
                    "resource_profile",
                    ("remaining_key_authority=1",),
                    ("remaining_key_authority=0",),
                ),
                permission=_mismatch(
                    "permission_profile",
                    ("decrypt_right=present",),
                    ("decrypt_right=absent",),
                ),
                provenance=matched_provenance,
                witness=t533.NoncompletionWitness(
                    witness_id="single_use_key_authority",
                    capability_kind="resource_completion_field",
                    left_value="completion_available",
                    right_value="completion_blocked",
                    predeclared=True,
                    domain_native=True,
                    independent_from_stack_profiles=False,
                    not_task_success_coordinate=True,
                    not_completion_field=False,
                ),
            ),
            data_bearing_packet=True,
            known_absorber="resource monotone computes the finality verdict vector",
            intended_taf10_reading="noncompletion via exactly-one authority",
            useful_remainder="negative guardrail for copy-law finality readings",
            expected_outcome="FALSIFIED",
        ),
        ExistingSourceCandidate(
            candidate_id="t521_detector_manifest_template_lane",
            source_family="T521 detector provenance lane",
            source_keys=("t521",),
            source_basis=(
                "T521 builds the manifest template and no-data boundary; it does "
                "not contain observed detector payloads or a filled real packet."
            ),
            t533_packet=t533.Packet(
                packet_id="t521_detector_manifest_template_lane",
                description="Detector manifest template reread as a TAF10 packet.",
                fixed_region_menu_task_context=True,
                checks_t500_t529_floor=True,
                competency=None,
                resource=None,
                permission=None,
                provenance=_cert(
                    "provenance_profile",
                    ("manifest_template=complete", "observed_payload=absent"),
                ),
                witness=None,
            ),
            data_bearing_packet=False,
            known_absorber="no data-bearing packet in hand",
            intended_taf10_reading="detector provenance noncompletion target",
            useful_remainder="pause until a predeclared filled manifest exists",
            expected_outcome="PAUSE",
        ),
    )


def _source_json_present(candidate: ExistingSourceCandidate) -> bool:
    return all(Path(SOURCE_PATHS[key]).exists() for key in candidate.source_keys)


def _missing_from_packet(packet: t533.Packet) -> tuple[str, ...]:
    missing = list(t533.missing_layers(packet))
    if not t533.witness_is_admissible(packet.witness):
        missing.append("independent_non_task_success_noncompletion_witness")
    return tuple(missing)


def classify_candidate(
    candidate: ExistingSourceCandidate,
    floor: dict[str, Any],
) -> CandidateClassification:
    t533_row = t533.classify(candidate.t533_packet, floor["t533_absorber_floor"])
    missing = _missing_from_packet(candidate.t533_packet)
    full_stack_exact_match = not t533.missing_layers(candidate.t533_packet)
    independent_witness = t533.witness_is_admissible(candidate.t533_packet.witness)
    source_present = _source_json_present(candidate)

    if not source_present:
        outcome = "PAUSE"
        reason = "One or more source JSON artifacts are missing."
    elif not candidate.data_bearing_packet:
        outcome = "PAUSE"
        reason = (
            "The source is structurally useful but has no data-bearing packet "
            "with observed values and profile certificates."
        )
    elif candidate.expected_outcome == "REVIEW_ONLY":
        outcome = "REVIEW_ONLY"
        reason = (
            "The source remains useful only under a weaker review reading; it "
            "does not match the full T533 stack or supply an independent "
            "non-task-success noncompletion witness."
        )
    elif candidate.expected_outcome == "NARROWED":
        outcome = "NARROWED"
        reason = (
            "The source narrows a real adjacent lane, but it is not a full "
            "TAF10 C(R) surplus packet."
        )
    elif candidate.known_absorber != "none":
        outcome = "FALSIFIED"
        reason = f"The intended TAF10 reading is absorbed by {candidate.known_absorber}."
    elif full_stack_exact_match and independent_witness and t533_row.admitted:
        outcome = "CLEARED"
        reason = "The candidate clears the imported T533 criteria and no absorber is recorded."
    else:
        outcome = "PAUSE"
        reason = "The candidate is real but still misses the full T533 packet burden."

    return CandidateClassification(
        candidate_id=candidate.candidate_id,
        source_family=candidate.source_family,
        outcome=outcome,
        t533_label=t533_row.label,
        full_stack_exact_match=full_stack_exact_match,
        independent_noncompletion_witness=independent_witness,
        data_bearing_packet=candidate.data_bearing_packet,
        source_json_present=source_present,
        known_absorber=candidate.known_absorber,
        missing_fields=missing,
        reason=reason,
        useful_remainder=candidate.useful_remainder,
    )


def claim_table(classifications: tuple[CandidateClassification, ...]) -> tuple[dict[str, str], ...]:
    cleared = [item.candidate_id for item in classifications if item.outcome == "CLEARED"]
    return (
        {
            "claim": "T535 consumed the T533 full-stack and witness criteria.",
            "status": "COMPUTED",
            "confidence": "high",
            "basis": f"Imported {T533_CRITERIA_SOURCE} and used t533.classify, missing_layers, and witness_is_admissible.",
        },
        {
            "claim": "At least two existing-source packet candidates were evaluated.",
            "status": "COMPUTED",
            "confidence": "high",
            "basis": f"Evaluated {len(classifications)} candidates from existing result JSON artifacts.",
        },
        {
            "claim": "No evaluated real-source candidate clears the TAF10 packet burden.",
            "status": "COMPUTED",
            "confidence": "high",
            "basis": f"Cleared candidate ids: {cleared}.",
        },
        {
            "claim": "The blocking field is the absence of a full-stack-matched independent non-task-success noncompletion witness not absorbed by native completion.",
            "status": "ARGUED",
            "confidence": "medium",
            "basis": "This phrases the shared missing field across the T407/T398, T411/T412, T520, and T521 failures.",
        },
        {
            "claim": "T535 should feed TAF9/TAF3 only as a negative or pause packet, not as C(R) success.",
            "status": "ARGUED",
            "confidence": "medium",
            "basis": "Track 2 remains subordinate to the source-law lane and no candidate cleared.",
        },
    )


def run() -> dict[str, Any]:
    floor = source_floor()
    classified = tuple(classify_candidate(candidate, floor) for candidate in candidates())
    cleared = [item.candidate_id for item in classified if item.outcome == "CLEARED"]
    outcomes = {item.outcome: 0 for item in classified}
    for item in classified:
        outcomes[item.outcome] = outcomes.get(item.outcome, 0) + 1

    return {
        "artifact": ARTIFACT,
        "verdict": "REAL_TAF10_PACKET_CLEARED" if cleared else VERDICT,
        "t533_criteria_source": T533_CRITERIA_SOURCE,
        "honest_ceiling": HONEST_CEILING,
        "exact_missing_field_if_none_clears": "" if cleared else EXACT_MISSING_FIELD,
        "source_floor": floor,
        "candidate_inputs": [asdict(candidate) for candidate in candidates()],
        "classifications": [asdict(item) for item in classified],
        "claim_table": list(claim_table(classified)),
        "overall": {
            "candidate_count": len(classified),
            "cleared_candidate_ids": cleared,
            "outcome_counts": outcomes,
            "real_taf10_packet_in_hand": bool(cleared),
            "current_c_r_success": bool(cleared),
            "surplus_over_full_stack_proved": bool(cleared),
            "track_2_subordinate": True,
            "claim_movement": False,
            "canon_or_public_posture_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "integration_notes": (
            "No registry or card update is made by T535. Parent integration can "
            "record TAF10 as paused unless a future packet supplies the exact "
            "missing field. The negative result can feed TAF3 only as a "
            "noncompletion-target absence, not as a C(R) success."
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {candidate_id} | {outcome} | {full_stack} | {witness} | {data} | {label} | {missing} | {reason} |".format(
            candidate_id=item["candidate_id"],
            outcome=item["outcome"],
            full_stack="yes" if item["full_stack_exact_match"] else "no",
            witness="yes" if item["independent_noncompletion_witness"] else "no",
            data="yes" if item["data_bearing_packet"] else "no",
            label=item["t533_label"],
            missing=", ".join(item["missing_fields"]) or "none",
            reason=item["reason"],
        )
        for item in payload["classifications"]
    ]
    claims = [
        "| {status} | {confidence} | {claim} | {basis} |".format(**item)
        for item in payload["claim_table"]
    ]
    source_flags = payload["source_floor"]["computed_source_flags"]
    flags = [f"| {key} | {value} |" for key, value in sorted(source_flags.items())]

    return "\n".join(
        [
            "# T535 - Real TAF10 Packet Screen - v0.1 results",
            "",
            "> Track-2 screen only. No claim-ledger, Canon Index, canon verdict, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T535-real-taf10-packet-screen.md`",
            "- Model: `models/t535_real_taf10_packet_screen.py`",
            "- Tests: `tests/test_t535_real_taf10_packet_screen.py`",
            "- Artifact JSON: `results/T535-real-taf10-packet-screen-v0.1.json`",
            f"- T533 criteria source: `{payload['t533_criteria_source']}`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            "T535 did not find a real packet that replaces T533's synthetic future target.",
            "",
            "Exact missing field if none clears:",
            "",
            payload["exact_missing_field_if_none_clears"],
            "",
            "## Source Floor Checks",
            "",
            "| Check | Value |",
            "| --- | --- |",
            *flags,
            "",
            "## Candidate Classifications",
            "",
            "| Candidate | Outcome | Full stack exact match? | Independent witness? | Data-bearing? | T533 label | Missing fields | Reason |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Claims",
            "",
            "| Status | Confidence | Claim | Basis |",
            "| --- | --- | --- | --- |",
            *claims,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reproducible TAF10 screen over real existing-source packet candidates.",
            "",
            "Does not earn: a C(R) success, a proof of surplus over the full stack, claim movement, canon movement, public posture, external publication, cross-repo truth, or a replacement for the Track-1 source-law question.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Integration Notes",
            "",
            payload["integration_notes"],
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
        json_path = results_dir / "T535-real-taf10-packet-screen-v0.1.json"
        md_path = results_dir / "T535-real-taf10-packet-screen-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
