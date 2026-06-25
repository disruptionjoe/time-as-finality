"""G7: SBS-style objectivity approximation for the S6 density fixture.

This builds on G6. For the controlled-rotation density-matrix fixture, the
conditional environment state for pointer 0 is |0>, while the conditional state
for pointer 1 is cos(theta)|0> + sin(theta)|1>. The pure-state trace distance is
sin(theta), which gives a finite conditional distinguishability score.

This is an SBS approximation, not an SBS theorem: it checks whether
distinguishable, redundant, conditionally product-like fragments line up with
the S6 descent threshold.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sin
from typing import Any

from models.s6_g6_density_matrix_bridge import (
    DESCENT_SUPPORT,
    MI_THRESHOLD,
    STRENGTHS,
    analyze_strength,
)


DISTINGUISHABILITY_THRESHOLD = 0.6
SBS_CLOSURE_THRESHOLD = 0.55


@dataclass(frozen=True)
class SBSFragmentScore:
    name: str
    mutual_information: float
    conditional_distinguishability: float
    redundant: bool
    distinguishable: bool
    objective_fragment: bool


@dataclass(frozen=True)
class SBSLevel:
    strength: float
    fragment_scores: tuple[SBSFragmentScore, ...]
    objective_fragment_count: int
    redundant_count: int
    average_distinguishability: float
    conditional_independence_defect: float
    sbs_closure_score: float
    sbs_objective: bool
    descent_stable: bool


def run_g7_sbs_approximation() -> dict[str, Any]:
    sweep = tuple(sbs_level(strength) for strength in STRENGTHS)
    sbs_threshold = next(level for level in sweep if level.sbs_objective)
    descent_threshold = next(level for level in sweep if level.descent_stable)
    checks = {
        "sbs_threshold_detected": sbs_threshold.strength == 1.2,
        "sbs_matches_descent_threshold": (
            sbs_threshold.strength == descent_threshold.strength
        ),
        "objective_fragments_have_distinguishability": all(
            fragment.conditional_distinguishability >= DISTINGUISHABILITY_THRESHOLD
            for fragment in sbs_threshold.fragment_scores
            if fragment.objective_fragment
        ),
        "conditional_independence_defect_zero_in_product_fixture": all(
            level.conditional_independence_defect == 0.0 for level in sweep
        ),
        "closure_score_crosses_threshold": (
            sbs_threshold.sbs_closure_score >= SBS_CLOSURE_THRESHOLD
        ),
    }
    return {
        "test": "s6-g7-sbs-approximation-v0.1",
        "tag": ["finite_witness", "sbs_approximation", "absorber_checked"],
        "guardrail": (
            "SBS-style score over a controlled-rotation product fixture only: "
            "not a proof of Spectrum Broadcast Structure and not a physical "
            "objectivity theorem."
        ),
        "parameters": {
            "mutual_information_threshold": MI_THRESHOLD,
            "distinguishability_threshold": DISTINGUISHABILITY_THRESHOLD,
            "descent_support": DESCENT_SUPPORT,
            "sbs_closure_threshold": SBS_CLOSURE_THRESHOLD,
        },
        "checks": checks,
        "all_checks_passed": all(checks.values()),
        "sbs_threshold": _level_to_dict(sbs_threshold),
        "descent_threshold": _level_to_dict(descent_threshold),
        "sweep": [_level_to_dict(level) for level in sweep],
        "absorber_verdict": {
            "Quantum_Darwinism_or_SBS": "granted_as_neighbor_absorber",
            "S6_residue": (
                "S6 keeps the typed descent/loss/provenance audit around the "
                "objectivity threshold; it does not own SBS."
            ),
        },
        "effect_verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
        },
        "strongest_result": (
            "The SBS-style closure score first crosses threshold at strength=1.2, "
            "the same point where G6 descent stabilizes. This supports S6 as a "
            "bridge metric around objectivity while conceding the physical "
            "objectivity mechanism to Quantum Darwinism/SBS."
        ),
        "first_obstruction": (
            "The fixture has zero conditional-independence defect by construction "
            "because the conditional environment states factor. A real SBS test "
            "must compute this from a less ideal density-matrix model."
        ),
        "next_step": (
            "Use the generic finite descent engine from G8 to consume these SBS "
            "scores without bespoke threshold logic."
        ),
    }


def sbs_level(strength: float) -> SBSLevel:
    density_level = analyze_strength(strength)
    fragments = tuple(
        SBSFragmentScore(
            name=fragment.name,
            mutual_information=fragment.mutual_information,
            conditional_distinguishability=sin(fragment.theta),
            redundant=fragment.redundant,
            distinguishable=sin(fragment.theta) >= DISTINGUISHABILITY_THRESHOLD,
            objective_fragment=(
                fragment.redundant
                and sin(fragment.theta) >= DISTINGUISHABILITY_THRESHOLD
            ),
        )
        for fragment in density_level.fragments
    )
    objective_count = sum(1 for fragment in fragments if fragment.objective_fragment)
    redundant_count = sum(1 for fragment in fragments if fragment.redundant)
    average_distinguishability = (
        sum(fragment.conditional_distinguishability for fragment in fragments)
        / len(fragments)
    )
    conditional_independence_defect = 0.0
    closure_score = (
        objective_count
        / len(fragments)
        * average_distinguishability
        * (1.0 - conditional_independence_defect)
    )
    return SBSLevel(
        strength=strength,
        fragment_scores=fragments,
        objective_fragment_count=objective_count,
        redundant_count=redundant_count,
        average_distinguishability=average_distinguishability,
        conditional_independence_defect=conditional_independence_defect,
        sbs_closure_score=closure_score,
        sbs_objective=(
            objective_count >= DESCENT_SUPPORT
            and closure_score >= SBS_CLOSURE_THRESHOLD
        ),
        descent_stable=density_level.descent_stable,
    )


def _level_to_dict(level: SBSLevel) -> dict[str, Any]:
    return {
        "strength": level.strength,
        "objective_fragment_count": level.objective_fragment_count,
        "redundant_count": level.redundant_count,
        "average_distinguishability": round(level.average_distinguishability, 6),
        "conditional_independence_defect": level.conditional_independence_defect,
        "sbs_closure_score": round(level.sbs_closure_score, 6),
        "sbs_objective": level.sbs_objective,
        "descent_stable": level.descent_stable,
        "fragment_scores": [
            {
                "name": fragment.name,
                "mutual_information": round(fragment.mutual_information, 6),
                "conditional_distinguishability": round(
                    fragment.conditional_distinguishability, 6
                ),
                "redundant": fragment.redundant,
                "distinguishable": fragment.distinguishable,
                "objective_fragment": fragment.objective_fragment,
            }
            for fragment in level.fragment_scores
        ],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_g7_sbs_approximation(), indent=2, sort_keys=True))
