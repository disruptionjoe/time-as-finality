"""RL-004 audit: preservation-flag boundary for typed transport composition.

T41 proves category laws for D1RestrictionMorphisms after ignoring morphism
names. Its own boundary leaves one case open: morphisms whose preservation
requirements are active via require_trust_path_preservation or
require_obstruction_preservation.

This audit does not change composition semantics. It records the current
behavior: _compose_morphisms returns a relaxed composed morphism with both
preservation flags set to False, so T41's category result is best read as a
result about the flag-erased morphism skeleton.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any

from models.d1_restriction_system import D1_DIMENSIONS, D1RestrictionMorphism
from models.transport_network import _compose_morphisms
from models.typed_transport_category import (
    _make_aligned_morphism,
    _make_category_system,
    make_identity,
    morphisms_equal_modulo_name,
)


@dataclass(frozen=True)
class FlagBoundaryCheck:
    label: str
    original_flags: tuple[bool, bool]
    composed_flags: tuple[bool, bool]
    skeleton_equal_modulo_name: bool
    flag_equal: bool
    interpretation: str


@dataclass(frozen=True)
class FlagBoundaryAudit:
    composition_check: FlagBoundaryCheck
    left_unit_check: FlagBoundaryCheck
    right_unit_check: FlagBoundaryCheck
    t41_skeleton_category_preserved: bool
    flagged_morphism_category_unproved: bool
    boundary: str
    recommendation: str


def _flag_tuple(morphism: D1RestrictionMorphism) -> tuple[bool, bool]:
    return (
        morphism.require_trust_path_preservation,
        morphism.require_obstruction_preservation,
    )


def _with_preservation_flags(
    morphism: D1RestrictionMorphism,
) -> D1RestrictionMorphism:
    return replace(
        morphism,
        require_trust_path_preservation=True,
        require_obstruction_preservation=True,
    )


def _check_against_original(
    label: str,
    original: D1RestrictionMorphism,
    composed: D1RestrictionMorphism,
) -> FlagBoundaryCheck:
    skeleton_equal = morphisms_equal_modulo_name(original, composed, label).equal_modulo_name
    flag_equal = _flag_tuple(original) == _flag_tuple(composed)
    interpretation = (
        "Skeleton equality holds, but preservation flags are erased by the current "
        "composition helper."
        if skeleton_equal and not flag_equal
        else "Current composition preserves both skeleton equality and flags."
    )
    return FlagBoundaryCheck(
        label=label,
        original_flags=_flag_tuple(original),
        composed_flags=_flag_tuple(composed),
        skeleton_equal_modulo_name=skeleton_equal,
        flag_equal=flag_equal,
        interpretation=interpretation,
    )


def run_flag_boundary_audit() -> FlagBoundaryAudit:
    """Run the preservation-flag boundary audit for RL-004/T41."""
    sys_a = _make_category_system("Flag_A", "fa")
    sys_b = _make_category_system("Flag_B", "fb")
    sys_c = _make_category_system("Flag_C", "fc")

    f = _with_preservation_flags(
        _make_aligned_morphism("flagged_f_A_B", sys_a, sys_b, D1_DIMENSIONS)
    )
    g = _with_preservation_flags(
        _make_aligned_morphism("flagged_g_B_C", sys_b, sys_c, D1_DIMENSIONS)
    )

    fg = _compose_morphisms(f, g)

    id_a = make_identity(sys_a)
    id_b = make_identity(sys_b)
    left = _compose_morphisms(id_a, f)
    right = _compose_morphisms(f, id_b)

    composition_check = FlagBoundaryCheck(
        label="flagged_f_A_B ; flagged_g_B_C",
        original_flags=_flag_tuple(f),
        composed_flags=_flag_tuple(fg),
        skeleton_equal_modulo_name=(
            fg.source.name == f.source.name
            and fg.target.name == g.target.name
            and frozenset(fg.preserved_dimensions)
            == (frozenset(f.preserved_dimensions) & frozenset(g.preserved_dimensions))
        ),
        flag_equal=_flag_tuple(fg) == _flag_tuple(f),
        interpretation=(
            "Composing two preservation-constrained morphisms yields a relaxed "
            "morphism under current _compose_morphisms semantics."
        ),
    )
    left_unit_check = _check_against_original("id_A ; flagged_f_A_B", f, left)
    right_unit_check = _check_against_original("flagged_f_A_B ; id_B", f, right)

    t41_skeleton_category_preserved = (
        composition_check.skeleton_equal_modulo_name
        and left_unit_check.skeleton_equal_modulo_name
        and right_unit_check.skeleton_equal_modulo_name
    )
    flagged_morphism_category_unproved = (
        not composition_check.flag_equal
        or not left_unit_check.flag_equal
        or not right_unit_check.flag_equal
    )

    return FlagBoundaryAudit(
        composition_check=composition_check,
        left_unit_check=left_unit_check,
        right_unit_check=right_unit_check,
        t41_skeleton_category_preserved=t41_skeleton_category_preserved,
        flagged_morphism_category_unproved=flagged_morphism_category_unproved,
        boundary=(
            "T41's category law remains supported for source, target, site_map, "
            "and preserved_dimensions. It should not be read as proving category "
            "laws for preservation-constrained morphisms where the two requirement "
            "flags are part of morphism identity."
        ),
        recommendation=(
            "Do not patch _compose_morphisms silently. A future RL-004 move should "
            "define whether preservation flags compose by conjunction, disjunction, "
            "separate evidence objects, or a typed obligation layer, then rerun "
            "the identity and associativity laws under that explicit semantics."
        ),
    )


def flag_boundary_audit_to_dict(result: FlagBoundaryAudit) -> dict[str, Any]:
    def check_to_dict(check: FlagBoundaryCheck) -> dict[str, Any]:
        return {
            "label": check.label,
            "original_flags": list(check.original_flags),
            "composed_flags": list(check.composed_flags),
            "skeleton_equal_modulo_name": check.skeleton_equal_modulo_name,
            "flag_equal": check.flag_equal,
            "interpretation": check.interpretation,
        }

    return {
        "composition_check": check_to_dict(result.composition_check),
        "left_unit_check": check_to_dict(result.left_unit_check),
        "right_unit_check": check_to_dict(result.right_unit_check),
        "t41_skeleton_category_preserved": result.t41_skeleton_category_preserved,
        "flagged_morphism_category_unproved": result.flagged_morphism_category_unproved,
        "boundary": result.boundary,
        "recommendation": result.recommendation,
    }
