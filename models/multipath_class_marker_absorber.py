"""T397: Multipath class-marker absorber audit.

T395 found that a k >= 3 class-coarse record over composition orders has a
class-graded structure: cross-class coherences obey binary duality, within-class
coherences are gamma-flat, and a perfect class record caps path/order
postdiction at 2/k. T395 named multipath duality as the absorber to run before
investing in a temporal-order inequality.

This model replaces composition-order labels with generic path labels while
keeping only the class-marker algebra. If the signatures match exactly, the
T395 k >= 3 residue is absorbed at this level: it is branch/path marker
bookkeeping, not yet composition-order-specific structure.
"""

from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


TOL = 1e-12
ARTIFACT = "T397-multipath-class-marker-absorber-v0.1"
GAMMA_SWEEP = (
    0.0,
    math.pi / 4.0,
    math.pi / 2.0,
    3.0 * math.pi / 4.0,
    math.pi,
)


@dataclass(frozen=True)
class ScalarizationResiduals:
    mean: float
    minimum: float
    maximum: float


@dataclass(frozen=True)
class MarkerSignature:
    label: str
    k: int
    class_sizes: tuple[int, int]
    gamma: float
    marker_overlap: float
    class_distinguishability: float
    path_postdiction_success: float
    perfect_record_path_ceiling: float
    within_class_factor: float
    cross_class_factor: float
    normalized_pairwise_factors: tuple[tuple[str, str, float], ...]
    scalarization_residuals: ScalarizationResiduals


@dataclass(frozen=True)
class BipartitionSweep:
    k: int
    bipartitions_checked: int
    gamma_values_checked: int
    within_class_flat_all: bool
    cross_class_duality_all: bool
    postdiction_formula_all: bool
    scalarizations_fail_binary_at_perfect_record_all: bool


@dataclass(frozen=True)
class T397Result:
    artifact: str
    canonical_equivalence: bool
    canonical_three_order: tuple[MarkerSignature, ...]
    generic_three_path: tuple[MarkerSignature, ...]
    six_path_parity: tuple[MarkerSignature, ...]
    exhaustive_bipartition_sweeps: tuple[BipartitionSweep, ...]
    full_resolution_path_postdiction_at_perfect_record: float
    full_resolution_max_pairwise_coherence_at_perfect_record: float
    absorber_verdict: str
    strongest_safe_claim: str
    direction_a_update: str
    falsification_condition: str
    next_gate: str


def class_id(classes: dict[str, int], label: str) -> int:
    value = classes[label]
    if value not in (0, 1):
        raise ValueError("T397 only audits two-class markers")
    return value


def validate_classes(labels: tuple[str, ...], classes: dict[str, int]) -> tuple[int, int]:
    if len(labels) < 3:
        raise ValueError("T397 starts at k >= 3")
    if set(labels) != set(classes):
        raise ValueError("class map must contain exactly the labels")
    sizes = (
        sum(1 for label in labels if class_id(classes, label) == 0),
        sum(1 for label in labels if class_id(classes, label) == 1),
    )
    if sizes[0] == 0 or sizes[1] == 0:
        raise ValueError("both classes must be nonempty")
    return sizes


def marker_overlap(gamma: float) -> float:
    """Inner product between the two pure class-marker states."""

    return math.cos(gamma / 2.0)


def class_distinguishability(gamma: float) -> float:
    """Trace-distance distinguishability of the two class-marker states."""

    return math.sin(gamma / 2.0)


def path_postdiction_success(k: int, gamma: float) -> float:
    """Best individual-path success from only a two-class marker.

    Within a class all path states are identical, so the individual-path
    success objective gives one distinguishable slot per class. For two pure
    class-marker states this is the equal-class Helstrom factor scaled by 2/k:

      P_path = (1 + sin(gamma / 2)) / k.
    """

    return (1.0 + class_distinguishability(gamma)) / float(k)


def normalized_pairwise_factors(
    labels: tuple[str, ...], classes: dict[str, int], gamma: float
) -> tuple[tuple[str, str, float], ...]:
    overlap = marker_overlap(gamma)
    factors: list[tuple[str, str, float]] = []
    for i, left in enumerate(labels):
        for right in labels[i + 1 :]:
            factor = 1.0 if class_id(classes, left) == class_id(classes, right) else overlap
            factors.append((left, right, factor))
    return tuple(factors)


def scalarization_residuals(
    labels: tuple[str, ...], classes: dict[str, int], gamma: float
) -> ScalarizationResiduals:
    factors = [factor for _, _, factor in normalized_pairwise_factors(labels, classes, gamma)]
    k = len(labels)
    # T395's disclosed global scalarization: rescale path postdiction from
    # random-guess baseline 1/k to the [0, 1] range.
    p_path = path_postdiction_success(k, gamma)
    d_global = (p_path - 1.0 / k) / (1.0 - 1.0 / k)
    mean_factor = sum(factors) / len(factors)
    return ScalarizationResiduals(
        mean=d_global * d_global + mean_factor * mean_factor - 1.0,
        minimum=d_global * d_global + min(factors) * min(factors) - 1.0,
        maximum=d_global * d_global + max(factors) * max(factors) - 1.0,
    )


def signature(
    label: str, labels: tuple[str, ...], classes: dict[str, int], gamma: float
) -> MarkerSignature:
    sizes = validate_classes(labels, classes)
    factors = normalized_pairwise_factors(labels, classes, gamma)
    within = [factor for left, right, factor in factors if classes[left] == classes[right]]
    cross = [factor for left, right, factor in factors if classes[left] != classes[right]]
    within_factor = within[0] if within else 1.0
    cross_factor = cross[0] if cross else marker_overlap(gamma)
    return MarkerSignature(
        label=label,
        k=len(labels),
        class_sizes=sizes,
        gamma=gamma,
        marker_overlap=marker_overlap(gamma),
        class_distinguishability=class_distinguishability(gamma),
        path_postdiction_success=path_postdiction_success(len(labels), gamma),
        perfect_record_path_ceiling=2.0 / float(len(labels)),
        within_class_factor=within_factor,
        cross_class_factor=cross_factor,
        normalized_pairwise_factors=factors,
        scalarization_residuals=scalarization_residuals(labels, classes, gamma),
    )


def generic_three_path_labels() -> tuple[str, ...]:
    return ("p0", "p1", "p2")


def generic_three_path_classes() -> dict[str, int]:
    return {"p0": 0, "p1": 1, "p2": 0}


def t395_three_order_labels() -> tuple[str, ...]:
    return ("ABC", "BAC", "CAB")


def t395_three_order_classes() -> dict[str, int]:
    # Same partition as T395's canonical "A before B" class record:
    # {ABC, CAB} versus {BAC}.
    return {"ABC": 0, "BAC": 1, "CAB": 0}


def six_path_parity_labels() -> tuple[str, ...]:
    return tuple(f"p{i}" for i in range(6))


def six_path_parity_classes() -> dict[str, int]:
    return {f"p{i}": i % 2 for i in range(6)}


def structure_only(signature_value: MarkerSignature) -> dict[str, object]:
    """Drop label names so generic paths can be compared with order labels."""

    return {
        "k": signature_value.k,
        "class_sizes": tuple(sorted(signature_value.class_sizes)),
        "gamma": signature_value.gamma,
        "marker_overlap": signature_value.marker_overlap,
        "class_distinguishability": signature_value.class_distinguishability,
        "path_postdiction_success": signature_value.path_postdiction_success,
        "perfect_record_path_ceiling": signature_value.perfect_record_path_ceiling,
        "within_class_factor": signature_value.within_class_factor,
        "cross_class_factor": signature_value.cross_class_factor,
        "factor_multiset": tuple(
            sorted(round(factor, 15) for _, _, factor in signature_value.normalized_pairwise_factors)
        ),
        "residuals": (
            signature_value.scalarization_residuals.mean,
            signature_value.scalarization_residuals.minimum,
            signature_value.scalarization_residuals.maximum,
        ),
    }


def signatures_match(left: MarkerSignature, right: MarkerSignature) -> bool:
    l_struct = structure_only(left)
    r_struct = structure_only(right)
    for key, l_value in l_struct.items():
        r_value = r_struct[key]
        if isinstance(l_value, tuple):
            if len(l_value) != len(r_value):
                return False
            for a, b in zip(l_value, r_value):
                if isinstance(a, float):
                    if abs(a - b) > TOL:
                        return False
                elif a != b:
                    return False
        elif isinstance(l_value, float):
            if abs(l_value - r_value) > TOL:
                return False
        elif l_value != r_value:
            return False
    return True


def nontrivial_bipartitions(k: int) -> Iterable[dict[str, int]]:
    labels = tuple(f"p{i}" for i in range(k))
    # Fix p0 in class 0 to quotient by class-complement symmetry.
    for mask in range(1, 2 ** (k - 1)):
        classes = {labels[0]: 0}
        for bit_index, label in enumerate(labels[1:]):
            classes[label] = 1 if (mask >> bit_index) & 1 else 0
        if any(value == 1 for value in classes.values()):
            yield classes


def scalarizations_fail_binary_at_perfect_record(sig: MarkerSignature) -> bool:
    residuals = sig.scalarization_residuals
    return (
        abs(residuals.mean) > 1e-6
        and abs(residuals.minimum) > 1e-6
        and abs(residuals.maximum) > 1e-6
    )


def run_bipartition_sweep(k: int) -> BipartitionSweep:
    labels = tuple(f"p{i}" for i in range(k))
    checked = 0
    within_ok = True
    cross_ok = True
    postdiction_ok = True
    scalarization_ok = True
    for classes in nontrivial_bipartitions(k):
        checked += 1
        for gamma in GAMMA_SWEEP:
            sig = signature(f"k{k}", labels, classes, gamma)
            if abs(sig.within_class_factor - 1.0) > TOL:
                within_ok = False
            if abs(sig.cross_class_factor - marker_overlap(gamma)) > TOL:
                cross_ok = False
            if abs(sig.path_postdiction_success - (1.0 + math.sin(gamma / 2.0)) / k) > TOL:
                postdiction_ok = False
        perfect = signature(f"k{k}", labels, classes, math.pi)
        if not scalarizations_fail_binary_at_perfect_record(perfect):
            scalarization_ok = False
    return BipartitionSweep(
        k=k,
        bipartitions_checked=checked,
        gamma_values_checked=len(GAMMA_SWEEP),
        within_class_flat_all=within_ok,
        cross_class_duality_all=cross_ok,
        postdiction_formula_all=postdiction_ok,
        scalarizations_fail_binary_at_perfect_record_all=scalarization_ok,
    )


def run_t397_analysis() -> T397Result:
    generic = tuple(
        signature(
            "generic_three_path",
            generic_three_path_labels(),
            generic_three_path_classes(),
            gamma,
        )
        for gamma in GAMMA_SWEEP
    )
    order = tuple(
        signature(
            "t395_three_order",
            t395_three_order_labels(),
            t395_three_order_classes(),
            gamma,
        )
        for gamma in GAMMA_SWEEP
    )
    six = tuple(
        signature(
            "six_path_parity",
            six_path_parity_labels(),
            six_path_parity_classes(),
            gamma,
        )
        for gamma in GAMMA_SWEEP
    )
    equivalence = all(signatures_match(generic_sig, order_sig) for generic_sig, order_sig in zip(generic, order))
    sweeps = tuple(run_bipartition_sweep(k) for k in (3, 4, 5, 6))
    return T397Result(
        artifact=ARTIFACT,
        canonical_equivalence=equivalence,
        canonical_three_order=order,
        generic_three_path=generic,
        six_path_parity=six,
        exhaustive_bipartition_sweeps=sweeps,
        full_resolution_path_postdiction_at_perfect_record=1.0,
        full_resolution_max_pairwise_coherence_at_perfect_record=0.0,
        absorber_verdict=(
            "absorbed: the T395 k>=3 class-coarse record signature is exactly "
            "generic multipath class-marker algebra in this finite audit"
        ),
        strongest_safe_claim=(
            "For two-class records over k>=3 equally weighted branches, the "
            "T395 signatures depend only on the class partition and the marker "
            "overlap cos(gamma/2): same-class coherences are unchanged, "
            "cross-class coherences are multiplied by cos(gamma/2), individual "
            "path postdiction is (1+sin(gamma/2))/k, and the perfect class "
            "record ceiling is 2/k. Composition-order labels add no extra "
            "structure in this branch-marker model."
        ),
        direction_a_update=(
            "Do not promote T395's k>=3 partial-record residue as a temporal-"
            "order inequality ingredient by itself. Direction A should move to "
            "a genuine causal-process witness, multi-holder finality/reversal "
            "cost, or another structure not already present in generic "
            "multipath class markers."
        ),
        falsification_condition=(
            "This absorber would fail if a composition-order family with the "
            "same class partition and marker overlaps produced a capability, "
            "causal witness, or coherence invariant that is not reproduced by "
            "the generic path-marker signature."
        ),
        next_gate=(
            "Replace visibility with a causal-process witness or add D1-native "
            "multi-holder/reversal-cost structure before attempting any "
            "record-order inequality."
        ),
    )


def residuals_to_dict(residuals: ScalarizationResiduals) -> dict[str, float]:
    return {
        "mean": residuals.mean,
        "minimum": residuals.minimum,
        "maximum": residuals.maximum,
    }


def signature_to_dict(sig: MarkerSignature) -> dict[str, object]:
    return {
        "label": sig.label,
        "k": sig.k,
        "class_sizes": list(sig.class_sizes),
        "gamma": sig.gamma,
        "marker_overlap": sig.marker_overlap,
        "class_distinguishability": sig.class_distinguishability,
        "path_postdiction_success": sig.path_postdiction_success,
        "perfect_record_path_ceiling": sig.perfect_record_path_ceiling,
        "within_class_factor": sig.within_class_factor,
        "cross_class_factor": sig.cross_class_factor,
        "normalized_pairwise_factors": [
            {"left": left, "right": right, "factor": factor}
            for left, right, factor in sig.normalized_pairwise_factors
        ],
        "scalarization_residuals": residuals_to_dict(sig.scalarization_residuals),
    }


def sweep_to_dict(sweep: BipartitionSweep) -> dict[str, object]:
    return {
        "k": sweep.k,
        "bipartitions_checked": sweep.bipartitions_checked,
        "gamma_values_checked": sweep.gamma_values_checked,
        "within_class_flat_all": sweep.within_class_flat_all,
        "cross_class_duality_all": sweep.cross_class_duality_all,
        "postdiction_formula_all": sweep.postdiction_formula_all,
        "scalarizations_fail_binary_at_perfect_record_all": (
            sweep.scalarizations_fail_binary_at_perfect_record_all
        ),
    }


def t397_result_to_dict(result: T397Result) -> dict[str, object]:
    return {
        "artifact": result.artifact,
        "canonical_equivalence": result.canonical_equivalence,
        "canonical_three_order": [signature_to_dict(sig) for sig in result.canonical_three_order],
        "generic_three_path": [signature_to_dict(sig) for sig in result.generic_three_path],
        "six_path_parity": [signature_to_dict(sig) for sig in result.six_path_parity],
        "exhaustive_bipartition_sweeps": [
            sweep_to_dict(sweep) for sweep in result.exhaustive_bipartition_sweeps
        ],
        "full_resolution_path_postdiction_at_perfect_record": (
            result.full_resolution_path_postdiction_at_perfect_record
        ),
        "full_resolution_max_pairwise_coherence_at_perfect_record": (
            result.full_resolution_max_pairwise_coherence_at_perfect_record
        ),
        "absorber_verdict": result.absorber_verdict,
        "strongest_safe_claim": result.strongest_safe_claim,
        "direction_a_update": result.direction_a_update,
        "falsification_condition": result.falsification_condition,
        "next_gate": result.next_gate,
    }


def gamma_label(gamma: float) -> str:
    if abs(gamma) < TOL:
        return "0"
    if abs(gamma - math.pi / 4.0) < TOL:
        return "pi/4"
    if abs(gamma - math.pi / 2.0) < TOL:
        return "pi/2"
    if abs(gamma - 3.0 * math.pi / 4.0) < TOL:
        return "3pi/4"
    if abs(gamma - math.pi) < TOL:
        return "pi"
    return f"{gamma:.6f}"


def markdown_results(result: T397Result) -> str:
    canonical_pi = result.canonical_three_order[-1]
    six_pi = result.six_path_parity[-1]
    sweep_lines = "\n".join(
        (
            f"| {sweep.k} | {sweep.bipartitions_checked} | "
            f"{sweep.within_class_flat_all} | {sweep.cross_class_duality_all} | "
            f"{sweep.postdiction_formula_all} | "
            f"{sweep.scalarizations_fail_binary_at_perfect_record_all} |"
        )
        for sweep in result.exhaustive_bipartition_sweeps
    )
    canonical_rows = "\n".join(
        (
            f"| {gamma_label(sig.gamma)} | {sig.marker_overlap:.6f} | "
            f"{sig.class_distinguishability:.6f} | "
            f"{sig.path_postdiction_success:.6f} | "
            f"{sig.within_class_factor:.6f} | {sig.cross_class_factor:.6f} |"
        )
        for sig in result.canonical_three_order
    )
    return f"""# T397 Results: Multipath Class-Marker Absorber Audit

- **Artifact:** `{result.artifact}`
- **Spec:** [tests/T397-multipath-class-marker-absorber.md](../tests/T397-multipath-class-marker-absorber.md)
- **Model:** [models/multipath_class_marker_absorber.py](../models/multipath_class_marker_absorber.py)
- **Test:** [tests/test_multipath_class_marker_absorber.py](../tests/test_multipath_class_marker_absorber.py)
- **Numbers:** [T397-multipath-class-marker-absorber-v0.1.json](T397-multipath-class-marker-absorber-v0.1.json)
- **Tags:** direction_a, absorber_audit, multipath_marker, t395_followup, no_claim_promotion

## Verdict

**{result.absorber_verdict}.**

The generic three-path class marker and T395's canonical three-order class
record have identical structure-only signatures at every gamma in the declared
sweep. The k>=3 class-coarse record behavior depends only on the class
partition and the marker overlap `cos(gamma/2)`, not on whether the branch
labels are composition orders.

## Canonical Three-Order / Three-Path Sweep

| gamma | marker overlap | class D | path success | within factor | cross factor |
| --- | ---: | ---: | ---: | ---: | ---: |
{canonical_rows}

At `gamma = pi`, the perfect class record gives individual path/order
postdiction `{canonical_pi.path_postdiction_success:.6f}` = `2/3` while
same-class coherence remains unchanged and cross-class coherence is zero.

## Scalarization Check At Perfect Class Record

T395's tested global scalarizations fail the binary circle in the generic
absorber too:

| case | mean residual | min residual | max residual |
| --- | ---: | ---: | ---: |
| three-order / three-path | {canonical_pi.scalarization_residuals.mean:.6f} | {canonical_pi.scalarization_residuals.minimum:.6f} | {canonical_pi.scalarization_residuals.maximum:.6f} |
| six-path parity | {six_pi.scalarization_residuals.mean:.6f} | {six_pi.scalarization_residuals.minimum:.6f} | {six_pi.scalarization_residuals.maximum:.6f} |

This is no longer evidence of temporal-order-specific structure; it is a
generic consequence of asking a scalar pair to summarize a class partition with
within-class coherence left intact.

## Exhaustive Bipartition Sweep

All nontrivial two-class bipartitions are checked up to class-complement
symmetry for k = 3..6.

| k | bipartitions | within flat | cross duality | postdiction formula | scalarizations fail at pi |
| ---: | ---: | --- | --- | --- | --- |
{sweep_lines}

## Direction-A Update

{result.direction_a_update}

## Strongest Safe Claim

{result.strongest_safe_claim}

## Falsification Condition

{result.falsification_condition}

## Next Gate

{result.next_gate}
"""


def write_artifacts(result: T397Result) -> None:
    root = Path(__file__).resolve().parents[1]
    results_dir = root / "results"
    json_path = results_dir / "T397-multipath-class-marker-absorber-v0.1.json"
    md_path = results_dir / "T397-multipath-class-marker-absorber-v0.1-results.md"
    json_path.write_text(json.dumps(t397_result_to_dict(result), indent=2) + "\n", encoding="utf-8")
    md_path.write_text(markdown_results(result), encoding="utf-8")


def main(argv: list[str]) -> int:
    result = run_t397_analysis()
    if "--write-artifacts" in argv:
        write_artifacts(result)
    print(json.dumps(t397_result_to_dict(result), indent=2))
    print()
    print("=" * 72)
    print("SUMMARY -- T397 Multipath Class-Marker Absorber Audit")
    print("=" * 72)
    print(f"canonical equivalence: {result.canonical_equivalence}")
    for sig in result.canonical_three_order:
        print(
            f"gamma={gamma_label(sig.gamma):>5}: "
            f"D={sig.class_distinguishability:.6f}, "
            f"P_path={sig.path_postdiction_success:.6f}, "
            f"within={sig.within_class_factor:.6f}, "
            f"cross={sig.cross_class_factor:.6f}"
        )
    print(result.absorber_verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
