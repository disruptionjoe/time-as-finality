"""T398: Resource-Profile Absorber for the T407 C(R) object.

This model runs the named absorber gate from T407 one level up. It does not
verify external LOCC, coherence, or majorization literature. Instead it asks
the finite internal question that a resource-theory reviewer would raise:

    If the T407 capability profile C(R) is admitted as the resource state,
    and the declared region/menu/task context is admitted as the operation
    context, does any formal anti-scalar residue remain?

Verdict: no formal resource-order residue remains in this finite family. The
T407 profile quotient is exactly a product resource preorder: a 3-chain of
undo capability times a 4-chain of readout capability. The no-scalar result
is absorbed as ordinary non-total resource convertibility. The statistics-flat
class is absorbed as an incomplete observer shadow that omits the resource
profile. The remaining value is translation residue: T407 is still a useful
region-indexed physical realization and statistics/capability audit, but not
a promoted new resource-theory object.
"""

from __future__ import annotations

import json
from itertools import combinations
from typing import Any

from models.region_capability_no_go import (
    FEATURED_PAIR,
    NAMED_CONFIGS,
    TASK_NAMES,
    TOL_EXACT,
    V_STAR,
    run_analysis,
)


ARTIFACT = "T398-resource-profile-absorber-v0.1"

ABSORBER_VERDICT = (
    "absorbed_as_finite_product_resource_preorder: once C(R) profiles are "
    "admitted as resource states under the declared region/menu/task context, "
    "the anti-scalar and incomparability content is exactly a product "
    "resource-preorder fact; T407 remains translation residue / physical "
    "realization, not a promoted resource-theory residue"
)

FALSIFICATION_CONDITION = (
    "This absorber would fail if two configurations in the same admitted "
    "resource profile and same declared context split on a capability verdict, "
    "or if the region index induced a conversion obstruction not captured by "
    "the admitted profile preorder plus declared region/menu/task context."
)


def _round(x: float) -> float:
    return round(float(x), 12)


def profile_tuple(profile: dict[str, float]) -> tuple[float, ...]:
    return tuple(_round(profile[name]) for name in TASK_NAMES)


def undo_axis(profile: tuple[float, ...]) -> tuple[float, float]:
    return profile[0], profile[1]


def readout_axis(profile: tuple[float, ...]) -> tuple[float, float]:
    return profile[2], profile[3]


def resource_leq(a: tuple[float, ...], b: tuple[float, ...]) -> bool:
    """T407 enactability order: a <= b iff b can do at least everything a can."""
    return all(x <= y + TOL_EXACT for x, y in zip(a, b))


def _profile_objects(t397: dict[str, Any]) -> list[dict[str, Any]]:
    by_profile: dict[tuple[float, ...], list[str]] = {}
    for config_key, entry in t397["profiles"].items():
        by_profile.setdefault(profile_tuple(entry["profile"]), []).append(config_key)

    undo_levels = sorted({undo_axis(p) for p in by_profile})
    readout_levels = sorted({readout_axis(p) for p in by_profile})
    undo_rank = {axis: i for i, axis in enumerate(undo_levels)}
    readout_rank = {axis: i for i, axis in enumerate(readout_levels)}

    objects = []
    for profile in sorted(
        by_profile,
        key=lambda p: (undo_rank[undo_axis(p)], readout_rank[readout_axis(p)]),
    ):
        u_rank = undo_rank[undo_axis(profile)]
        r_rank = readout_rank[readout_axis(profile)]
        objects.append(
            {
                "id": f"U{u_rank}_R{r_rank}",
                "profile": profile,
                "undo_axis": undo_axis(profile),
                "readout_axis": readout_axis(profile),
                "undo_rank": u_rank,
                "readout_rank": r_rank,
                "configs": sorted(by_profile[profile]),
            }
        )
    return objects


def _relations(objects: list[dict[str, Any]]) -> dict[str, Any]:
    relation_pairs = []
    strict_pairs = []
    incomparable_pairs = []
    for a, b in combinations(objects, 2):
        a_le_b = resource_leq(a["profile"], b["profile"])
        b_le_a = resource_leq(b["profile"], a["profile"])
        if a_le_b:
            relation_pairs.append([a["id"], b["id"]])
            strict_pairs.append([a["id"], b["id"]])
        elif b_le_a:
            relation_pairs.append([b["id"], a["id"]])
            strict_pairs.append([b["id"], a["id"]])
        else:
            incomparable_pairs.append(sorted([a["id"], b["id"]]))

    # Keep T407's relation accounting: relation_size is strict comparable
    # unordered pairs; reflexives are reported separately for the preorder.
    reflexive_pairs = [[obj["id"], obj["id"]] for obj in objects]
    return {
        "relation_pairs": reflexive_pairs + relation_pairs,
        "strict_pairs": strict_pairs,
        "relation_size": len(relation_pairs),
        "preorder_size_including_reflexives": len(reflexive_pairs) + len(relation_pairs),
        "n_incomparable_pairs": len(incomparable_pairs),
        "incomparable_pairs": sorted(incomparable_pairs),
    }


def _monotone_audit(objects: list[dict[str, Any]], relations: dict[str, Any], t397: dict[str, Any]) -> dict[str, Any]:
    id_to_obj = {obj["id"]: obj for obj in objects}
    axes_monotone = True
    for lower_id, upper_id in relations["relation_pairs"]:
        lower = id_to_obj[lower_id]
        upper = id_to_obj[upper_id]
        axes_monotone = axes_monotone and lower["undo_rank"] <= upper["undo_rank"]
        axes_monotone = axes_monotone and lower["readout_rank"] <= upper["readout_rank"]

    axis_pairs = {(obj["undo_rank"], obj["readout_rank"]) for obj in objects}
    return {
        "undo_axis_levels": sorted({obj["undo_axis"] for obj in objects}),
        "readout_axis_levels": sorted({obj["readout_axis"] for obj in objects}),
        "n_undo_levels": len({obj["undo_axis"] for obj in objects}),
        "n_readout_levels": len({obj["readout_axis"] for obj in objects}),
        "axis_pair_count": len(axis_pairs),
        "axes_jointly_classify": len(axis_pairs) == len(objects),
        "axes_monotone": bool(axes_monotone),
        "scalar_absorbed": {
            "t397_weak_orders_scanned": t397["leg2"]["scalar_refutation_exhaustive"]["n_weak_orders_scanned"],
            "t397_reproducing_scalars": t397["leg2"]["scalar_refutation_exhaustive"]["n_reproducing_scalars"],
            "absorber_reading": (
                "no total scalar is expected in a two-coordinate resource "
                "preorder; this is an absorbed non-total-order fact, not a "
                "new scalar no-go"
            ),
        },
    }


def _factorization_audit(t397: dict[str, Any], objects: list[dict[str, Any]]) -> dict[str, Any]:
    profile_to_object = {obj["profile"]: obj["id"] for obj in objects}
    config_to_object = {
        config_key: profile_to_object[profile_tuple(entry["profile"])]
        for config_key, entry in t397["profiles"].items()
    }

    same_resource_splits: list[dict[str, Any]] = []
    for obj in objects:
        passes_seen = {}
        for config_key in obj["configs"]:
            passes = tuple(
                bool(t397["profiles"][config_key]["passes"][task])
                for task in TASK_NAMES
            )
            passes_seen.setdefault(passes, []).append(config_key)
        if len(passes_seen) > 1:
            same_resource_splits.append({"object": obj["id"], "passes": passes_seen})

    flat_class = next(
        c
        for c in t397["leg3"]["statistics_partition"]["classes"]
        if "|".join(NAMED_CONFIGS["pristine"]) in c
    )
    flat_resources = sorted({config_to_object[config] for config in flat_class})
    featured = {
        name: config_to_object["|".join(NAMED_CONFIGS[name])]
        for name in FEATURED_PAIR
    }

    return {
        "n_configs": len(config_to_object),
        "n_resource_objects": len(objects),
        "same_resource_capability_splits": same_resource_splits,
        "capability_factors_through_resource_profile": len(same_resource_splits) == 0,
        "statistics_flat_class": {
            "size": len(flat_class),
            "stats_constant": t397["leg3"]["capability_test_undecidable_by_statistics"][
                "flat_class_statistics_constant"
            ],
            "n_resource_objects_realized": len(flat_resources),
            "resource_objects_realized": flat_resources,
            "spans_all_resource_objects": len(flat_resources) == len(objects),
        },
        "featured_pair_resource_objects": featured,
        "featured_pair_same_statistics_different_resource": (
            featured[FEATURED_PAIR[0]] != featured[FEATURED_PAIR[1]]
            and t397["leg3"]["featured_pair"]["stats_max_diff"] < TOL_EXACT
        ),
        "capability_test": {
            "test": f"undo_cross >= v* ({V_STAR})",
            "factors_through_resource_profile": True,
            "not_decidable_from_declared_statistics": t397["leg3"][
                "capability_test_undecidable_by_statistics"
            ]["test_nonconstant_on_flat_class"],
        },
    }


def _absorber_challenges() -> dict[str, Any]:
    return {
        "anti_scalar_theorem_shape": {
            "status": "absorbed",
            "reason": (
                "A product of two resource coordinates naturally has "
                "incomparable elements and no faithful scalar total preorder."
            ),
        },
        "statistics_flatness": {
            "status": "absorbed_as_incomplete_shadow",
            "reason": (
                "Declared Z-readout statistics omit the admitted resource "
                "profile. Once the profile is granted, capability verdicts "
                "factor through it."
            ),
        },
        "region_indexing": {
            "status": "absorbed_as_context_parameter",
            "reason": (
                "The declared region, menu, and task family are exactly the "
                "resource-theory context. The current finite artifact does not "
                "derive an additional conversion obstruction beyond that context."
            ),
        },
        "physical_realization": {
            "status": "translation_residue",
            "reason": (
                "The exact T407 construction remains useful as a region-indexed "
                "audit example where statistics and capability typing diverge."
            ),
        },
    }


def run_resource_profile_absorber() -> dict[str, Any]:
    t397 = run_analysis()
    objects = _profile_objects(t397)
    relations = _relations(objects)
    monotones = _monotone_audit(objects, relations, t397)
    factorization = _factorization_audit(t397, objects)
    return {
        "artifact": ARTIFACT,
        "source_artifact": t397["artifact"],
        "resource_frame": {
            "objects": "mutual-convertibility classes of admitted C(R) profiles",
            "preorder": "componentwise capability dominance in the declared region/menu/task context",
            "free_downgrade_reading": (
                "a higher profile can simulate a lower one by declining or "
                "discarding available task capability"
            ),
            "external_prior_art_status": (
                "not verified here; this is the finite internal resource-preorder "
                "absorber gate requested by T407"
            ),
        },
        "resource_objects": objects,
        "relations": relations,
        "monotone_audit": monotones,
        "factorization_audit": factorization,
        "absorber_challenges": _absorber_challenges(),
        "absorber_verdict": ABSORBER_VERDICT,
        "residue_label": "translation_residue",
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Keep C(R) as a region-indexed audit/readout object, not a promoted resource-theory novelty claim.",
            "For a stronger discriminator, require equality under all R-supported intervention statistics and separation only by a boundary-crossing menu.",
            "Run a separate verified literature note before any external-facing resource-theory language.",
        ],
        "falsification_condition": FALSIFICATION_CONDITION,
    }


if __name__ == "__main__":
    print(json.dumps(run_resource_profile_absorber(), indent=2, sort_keys=True))
