"""T506: boundary-adapter dimension-carrying embedding gate.

The second boundary-adapter build found a precise defect: the flat D1 profile
collapses the pure-physical dimension distinction because a two-site physical
sector can map many-to-one into a one-site physical sub-sector. This module
makes the named fix executable in a local synthetic fixture. It tests whether a
dimension-carrying capability encoding blocks that collapse while preserving
the already-protected physical/mirror face distinction.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from itertools import product
from pathlib import Path
from typing import Any

from models.boundary_adapter_functor import GUBDY_INCLUSIONS, GUBDY_OBJECTS, build_F
from models.d1_restriction_system import (
    D1_DIMENSIONS,
    D1RestrictionMorphism,
    SiteMap,
    analyze_morphism,
)


ARTIFACT = "T506-boundary-adapter-dimension-carrying-embedding-gate-v0.1"
VERDICT = "DIMENSION_CARRYING_EMBEDDING_GATE_BUILT_REVIEW_ONLY"
SOURCE_OPEN_PROBLEM = "open-problems/boundary-adapter-as-functor-spec-2026-07-07.md"
SOURCE_BUILD = "models/boundary_adapter_functor_faithfulness.py"

LEQ = {(item, item) for item in GUBDY_OBJECTS} | set(GUBDY_INCLUSIONS)
PAIRS = tuple((source, target) for source in GUBDY_OBJECTS for target in GUBDY_OBJECTS)


@dataclass(frozen=True)
class EncodingPacket:
    packet_id: str
    description: str
    phys_accessible: int
    mirror_accessible: int
    carries_dimension_atoms: bool
    exact_atom_identity: bool
    site_map_injective: bool
    preserves_face_kind: bool
    fixed_before_mapping: bool
    includes_flat_baseline_control: bool
    includes_physics_wrong_control: bool
    requests_claim_or_public_posture: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class EncodingDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    order_reflects_full_poset: bool
    inclusions_preserved: bool
    dimension_collapse_blocked: bool
    mirror_face_protected: bool
    flat_baseline_control_present: bool
    physics_wrong_control_present: bool
    counts_as_claim_evidence: bool
    missing_requirements: tuple[str, ...]
    spurious_morphisms: tuple[str, ...]
    missing_inclusions: tuple[str, ...]
    strongest_allowed_reading: str


def run() -> dict[str, Any]:
    packets = packet_fixtures()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    by_id = {decision.packet_id: decision for decision in decisions}

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "source_build": SOURCE_BUILD,
        "objective": (
            "Turn the named post-faithfulness defect into a TaF-side gate: a "
            "dimension-carrying capability encoding must block the flat D1 "
            "many-to-one physical-sector collapse while preserving the "
            "physical/mirror face distinction and remaining review-only."
        ),
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "overall": {
            "flat_baseline_rejected_for_dimension_collapse": (
                by_id["flat_profile_baseline"].label
                == "REJECTED_FLAT_PROFILE_DIMENSION_COLLAPSE"
            ),
            "exact_dimension_encoding_admitted": by_id[
                "exact_dimension_carrying_embedding"
            ].admitted,
            "exact_dimension_encoding_order_reflects_full_poset": by_id[
                "exact_dimension_carrying_embedding"
            ].order_reflects_full_poset,
            "exact_dimension_encoding_blocks_wplus_to_wplus0": by_id[
                "exact_dimension_carrying_embedding"
            ].dimension_collapse_blocked,
            "cardinality_only_control_rejected": (
                by_id["cardinality_only_physics_wrong_control"].label
                == "REJECTED_CARDINALITY_ONLY_FACE_COLLAPSE"
            ),
            "noninjective_dimension_control_rejected": (
                by_id["noninjective_dimension_token_control"].label
                == "REJECTED_NONINJECTIVE_DIMENSION_ENCODING"
            ),
            "review_target_only": True,
            "claim_movement": False,
            "roadmap_movement": False,
            "readme_movement": False,
            "north_star_movement": False,
            "public_posture_movement": False,
            "hard_policy_movement": False,
            "protected_license_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
            "sibling_repo_inspection": False,
            "current_two_adapter_gate_closed": False,
        },
        "future_dimension_packet_minimum": future_dimension_packet_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T506 shows, in a local synthetic TaF fixture, that the known "
            "flat-profile collapse can be blocked by carrying exact dimension "
            "atoms and requiring injective, face-preserving morphisms. Under "
            "that stricter encoding, the finite GUBdy order is reflected "
            "exactly: expected inclusions remain and the spurious F(W+) -> "
            "F(W+0) collapse is blocked. The result is an admission pattern, "
            "not a real GU/TI/TaF adapter result: cardinality-only, "
            "noninjective, retuned, physics-wrong, claim, external, and "
            "cross-repo shortcuts remain rejected or blocked."
        ),
    }


def packet_fixtures() -> tuple[EncodingPacket, ...]:
    return (
        EncodingPacket(
            packet_id="flat_profile_baseline",
            description=(
                "Current flat D1 profile: two physical sites can map "
                "many-to-one into one physical site."
            ),
            phys_accessible=1,
            mirror_accessible=0,
            carries_dimension_atoms=False,
            exact_atom_identity=False,
            site_map_injective=False,
            preserves_face_kind=True,
            fixed_before_mapping=True,
            includes_flat_baseline_control=True,
            includes_physics_wrong_control=True,
        ),
        EncodingPacket(
            packet_id="exact_dimension_carrying_embedding",
            description=(
                "Candidate fix: carry exact dimension atoms and require "
                "injective, face-preserving site maps."
            ),
            phys_accessible=1,
            mirror_accessible=0,
            carries_dimension_atoms=True,
            exact_atom_identity=True,
            site_map_injective=True,
            preserves_face_kind=True,
            fixed_before_mapping=True,
            includes_flat_baseline_control=True,
            includes_physics_wrong_control=True,
        ),
        EncodingPacket(
            packet_id="cardinality_only_physics_wrong_control",
            description=(
                "Counts dimensions but does not preserve face kind; with "
                "mirror.accessible=1 it can map hidden/mirror to physical."
            ),
            phys_accessible=1,
            mirror_accessible=1,
            carries_dimension_atoms=True,
            exact_atom_identity=False,
            site_map_injective=True,
            preserves_face_kind=False,
            fixed_before_mapping=True,
            includes_flat_baseline_control=True,
            includes_physics_wrong_control=True,
        ),
        EncodingPacket(
            packet_id="noninjective_dimension_token_control",
            description=(
                "Declares a dimension-carrying token but still permits "
                "many-to-one site maps."
            ),
            phys_accessible=1,
            mirror_accessible=0,
            carries_dimension_atoms=True,
            exact_atom_identity=False,
            site_map_injective=False,
            preserves_face_kind=True,
            fixed_before_mapping=True,
            includes_flat_baseline_control=True,
            includes_physics_wrong_control=True,
        ),
        EncodingPacket(
            packet_id="posthoc_retyping_shortcut",
            description=(
                "Adds dimension labels after seeing the desired adapter target "
                "rather than fixing them before the morphism test."
            ),
            phys_accessible=1,
            mirror_accessible=0,
            carries_dimension_atoms=True,
            exact_atom_identity=True,
            site_map_injective=True,
            preserves_face_kind=True,
            fixed_before_mapping=False,
            includes_flat_baseline_control=True,
            includes_physics_wrong_control=True,
        ),
        EncodingPacket(
            packet_id="claim_cross_repo_shortcut",
            description=(
                "Treats the synthetic encoding gate as permission to move "
                "adapter identity, public posture, or sibling-repo truth."
            ),
            phys_accessible=1,
            mirror_accessible=0,
            carries_dimension_atoms=True,
            exact_atom_identity=True,
            site_map_injective=True,
            preserves_face_kind=True,
            fixed_before_mapping=True,
            includes_flat_baseline_control=True,
            includes_physics_wrong_control=True,
            requests_claim_or_public_posture=True,
            requests_external_publication=True,
            requests_cross_repo_truth=True,
        ),
    )


def evaluate_packet(packet: EncodingPacket) -> EncodingDecision:
    exists = _existence_table(packet)
    spurious = tuple(_pair_label(a, b) for a, b in PAIRS if exists[(a, b)] and (a, b) not in LEQ)
    missing_inclusions = tuple(_pair_label(a, b) for a, b in LEQ if not exists[(a, b)])
    inclusions_preserved = not missing_inclusions
    order_reflects = not spurious and inclusions_preserved
    dimension_collapse_blocked = not exists[("W+", "W+0")]
    mirror_face_protected = (
        not exists[("W-", "W+")]
        and not exists[("W+", "W-")]
        and not exists[("W-", "W+0")]
        and not exists[("W+0", "W-")]
    )
    missing = missing_requirements(packet)

    if packet.requests_claim_or_public_posture:
        return _decision(
            packet,
            False,
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            "stop",
            order_reflects,
            inclusions_preserved,
            dimension_collapse_blocked,
            mirror_face_protected,
            missing,
            spurious,
            missing_inclusions,
            "Synthetic dimension encoding cannot move claims, public posture, or hard policy.",
        )
    if packet.requests_external_publication or packet.requests_cross_repo_truth:
        return _decision(
            packet,
            False,
            "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT",
            "stop",
            order_reflects,
            inclusions_preserved,
            dimension_collapse_blocked,
            mirror_face_protected,
            missing,
            spurious,
            missing_inclusions,
            "External publication and sibling-repo truth movement are outside this run.",
        )
    if not packet.fixed_before_mapping:
        return _decision(
            packet,
            False,
            "REJECTED_POSTHOC_DIMENSION_RETUNING",
            "reject",
            order_reflects,
            inclusions_preserved,
            dimension_collapse_blocked,
            mirror_face_protected,
            missing,
            spurious,
            missing_inclusions,
            "Dimension atoms must be fixed before the adapter target is selected.",
        )
    if not packet.carries_dimension_atoms and not dimension_collapse_blocked:
        return _decision(
            packet,
            False,
            "REJECTED_FLAT_PROFILE_DIMENSION_COLLAPSE",
            "reject",
            order_reflects,
            inclusions_preserved,
            dimension_collapse_blocked,
            mirror_face_protected,
            missing,
            spurious,
            missing_inclusions,
            "The flat D1 profile still admits the spurious F(W+) -> F(W+0) collapse.",
        )
    if packet.carries_dimension_atoms and not packet.site_map_injective and not dimension_collapse_blocked:
        return _decision(
            packet,
            False,
            "REJECTED_NONINJECTIVE_DIMENSION_ENCODING",
            "reject",
            order_reflects,
            inclusions_preserved,
            dimension_collapse_blocked,
            mirror_face_protected,
            missing,
            spurious,
            missing_inclusions,
            "Dimension labels do not help if many-to-one site maps are still allowed.",
        )
    if packet.carries_dimension_atoms and not mirror_face_protected:
        return _decision(
            packet,
            False,
            "REJECTED_CARDINALITY_ONLY_FACE_COLLAPSE",
            "reject",
            order_reflects,
            inclusions_preserved,
            dimension_collapse_blocked,
            mirror_face_protected,
            missing,
            spurious,
            missing_inclusions,
            "Counting dimension without face-kind and physics grounding loses the mirror/physical guard.",
        )
    if missing:
        return _decision(
            packet,
            False,
            "REJECTED_INCOMPLETE_DIMENSION_PACKET",
            "reject",
            order_reflects,
            inclusions_preserved,
            dimension_collapse_blocked,
            mirror_face_protected,
            missing,
            spurious,
            missing_inclusions,
            "The packet lacks the fixed encoding, controls, or morphism discipline.",
        )
    if not order_reflects:
        return _decision(
            packet,
            False,
            "REJECTED_ORDER_REFLECTION_FAILURE",
            "reject",
            order_reflects,
            inclusions_preserved,
            dimension_collapse_blocked,
            mirror_face_protected,
            missing,
            spurious,
            missing_inclusions,
            "The encoded target does not reflect the finite boundary-sector order exactly.",
        )

    return _decision(
        packet,
        True,
        "ADMITTED_DIMENSION_CARRYING_EMBEDDING_REVIEW_TARGET",
        "review_only",
        order_reflects,
        inclusions_preserved,
        dimension_collapse_blocked,
        mirror_face_protected,
        (),
        spurious,
        missing_inclusions,
        "Local synthetic review target only: exact dimension atoms plus injective face-preserving maps block the known collapse.",
    )


def missing_requirements(packet: EncodingPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.carries_dimension_atoms:
        missing.append("dimension_atoms")
    if packet.carries_dimension_atoms and not packet.site_map_injective:
        missing.append("injective_site_map")
    if packet.carries_dimension_atoms and not packet.exact_atom_identity:
        missing.append("exact_atom_identity")
    if packet.carries_dimension_atoms and not packet.preserves_face_kind:
        missing.append("face_kind_preservation")
    if not packet.fixed_before_mapping:
        missing.append("predeclared_dimension_encoding")
    if not packet.includes_flat_baseline_control:
        missing.append("flat_baseline_control")
    if not packet.includes_physics_wrong_control:
        missing.append("physics_wrong_control")
    return tuple(missing)


def future_dimension_packet_minimum() -> tuple[str, ...]:
    return (
        "cite the flat-profile collapse F(W+) -> F(W+0) as the defect being repaired",
        "predeclare dimension atoms before selecting the adapter target",
        "preserve exact dimension atoms or give an equivalent invariant",
        "require injective site maps or an explicit no-many-to-one substitute",
        "preserve physical-vs-mirror or accessible-vs-hidden face kind",
        "include the flat D1 baseline as a negative control",
        "include a physics-wrong or source-wrong mirror/hidden control",
        "prove all expected source inclusions still map to reached target morphisms",
        "prove no non-source-order target morphisms appear",
        "keep the result review-only until real source-category truth is supplied by the owning surface",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "real GU source category",
        "real TI source-category truth",
        "real GU/TaF adapter",
        "real TI/TaF adapter",
        "GU/TI/TaF adapter identity",
        "two-adapter gate closure",
        "de-correlated adapter arrival",
        "dimension-carrying encoding adopted as repo canon",
        "claim-ledger movement",
        "roadmap movement",
        "README movement",
        "North Star movement",
        "public-posture movement",
        "hard-policy movement",
        "external publication",
        "cross-repo truth movement",
    )


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {packet_id} | {admitted} | {label} | {order} | {collapse} | {mirror} | {missing} | {spurious} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            order="yes" if decision["order_reflects_full_poset"] else "no",
            collapse="yes" if decision["dimension_collapse_blocked"] else "no",
            mirror="yes" if decision["mirror_face_protected"] else "no",
            missing=", ".join(decision["missing_requirements"]) or "none",
            spurious=", ".join(decision["spurious_morphisms"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    future = [f"- {item}" for item in payload["future_dimension_packet_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T506 - Boundary-Adapter Dimension-Carrying Embedding Gate - v0.1 results",
            "",
            "> TaF-side synthetic review gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T506-boundary-adapter-dimension-carrying-embedding-gate.md`",
            "- Model: `models/boundary_adapter_dimension_carrying_embedding_gate.py`",
            "- Tests: `tests/test_boundary_adapter_dimension_carrying_embedding_gate.py`",
            f"- Source open problem: `{payload['source_open_problem']}`",
            f"- Source build: `{payload['source_build']}`",
            f"- Artifact JSON: `results/{ARTIFACT}.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Full order reflection? | Blocks W+ -> W+0? | Protects mirror face? | Missing requirements | Spurious morphisms |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Future Dimension Packet Minimum",
            "",
            *future,
            "",
            "## What This Does Not Earn",
            "",
            *blocked,
            "",
        ]
    )


def _existence_table(packet: EncodingPacket) -> dict[tuple[str, str], bool]:
    return {
        (source, target): _morphism_exists(packet, source, target)
        for source, target in PAIRS
    }


def _morphism_exists(packet: EncodingPacket, source: str, target: str) -> bool:
    f_obj, _ = build_F(
        phys_accessible=packet.phys_accessible,
        mirror_accessible=packet.mirror_accessible,
    )
    source_system = f_obj[source]
    target_system = f_obj[target]
    source_sites = list(source_system.site_ids())
    target_sites = list(target_system.site_ids())
    for combo in product(target_sites, repeat=len(source_sites)):
        if packet.carries_dimension_atoms:
            if packet.site_map_injective and len(set(combo)) != len(combo):
                continue
            if packet.exact_atom_identity and any(src != tgt for src, tgt in zip(source_sites, combo)):
                continue
            if packet.preserves_face_kind and any(
                _face_kind(src) != _face_kind(tgt)
                for src, tgt in zip(source_sites, combo)
            ):
                continue
        morphism = D1RestrictionMorphism(
            name=f"probe_{source}_to_{target}",
            source=source_system,
            target=target_system,
            site_map=tuple(
                SiteMap(src, tgt) for src, tgt in zip(source_sites, combo)
            ),
            preserved_dimensions=D1_DIMENSIONS,
            require_trust_path_preservation=False,
            require_obstruction_preservation=False,
        )
        if analyze_morphism(morphism).reached:
            return True
    return False


def _face_kind(site_id: str) -> str:
    if site_id.startswith("phys"):
        return "physical"
    if site_id.startswith("mirror"):
        return "mirror"
    return "unknown"


def _pair_label(source: str, target: str) -> str:
    return f"{source}->{target}"


def _decision(
    packet: EncodingPacket,
    admitted: bool,
    label: str,
    action: str,
    order_reflects_full_poset: bool,
    inclusions_preserved: bool,
    dimension_collapse_blocked: bool,
    mirror_face_protected: bool,
    missing_requirements: tuple[str, ...],
    spurious_morphisms: tuple[str, ...],
    missing_inclusions: tuple[str, ...],
    strongest_allowed_reading: str,
) -> EncodingDecision:
    return EncodingDecision(
        packet_id=packet.packet_id,
        admitted=admitted,
        label=label,
        action=action,
        review_target_only=admitted,
        order_reflects_full_poset=order_reflects_full_poset,
        inclusions_preserved=inclusions_preserved,
        dimension_collapse_blocked=dimension_collapse_blocked,
        mirror_face_protected=mirror_face_protected,
        flat_baseline_control_present=packet.includes_flat_baseline_control,
        physics_wrong_control_present=packet.includes_physics_wrong_control,
        counts_as_claim_evidence=False,
        missing_requirements=missing_requirements,
        spurious_morphisms=spurious_morphisms,
        missing_inclusions=missing_inclusions,
        strongest_allowed_reading=strongest_allowed_reading,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT}.json"
        md_path = results_dir / f"{ARTIFACT}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
