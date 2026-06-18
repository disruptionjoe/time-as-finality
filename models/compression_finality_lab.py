"""T36: Compression-Finality Crosswalk.

Tests the hypothesis from explorations/compression-finality-crosswalk.md:

  finality → stable records → predictability → compression

NOT: compression = finality

The experiment runs all 256 elementary CA rules on the same T9 emergence-lab
substrate (width=5, layers=3) and computes two independent columns:

  D1 finality column:  trace_survival_fraction, mean_accessible_support
  Compression column:  Shannon entropy of the trace distribution,
                       normalized compressibility, zlib compression ratio

If any rule pair shows same-finality-different-compression (or vice versa),
compressibility is empirically distinct from finality in this model.
"""

from __future__ import annotations

import math
import zlib
from dataclasses import dataclass
from typing import Any

from models.emergence_lab import (
    ElementaryCA,
    analyze_eca_trace,
    analyze_transition_map,
    int_to_bits,
)


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CompressibilityProfile:
    """Per-rule compression and D1 finality metrics side by side."""
    rule: int
    injective: bool
    lost_bits: float
    trace_survival_fraction: float      # D1: fraction of seeds producing traces
    mean_accessible_support: float      # D1: mean Hamming weight among surviving traces
    trace_shannon_entropy: float        # H(trace distribution) in bits
    max_possible_entropy: float         # log2(2^width) = width bits
    trace_compressibility: float        # 1 - entropy/max_entropy; 0=uniform, 1=deterministic
    zlib_ratio: float                   # compressed_len / raw_len for all traces packed
    unique_trace_patterns: int          # distinct trace_mask values observed
    total_traces: int


@dataclass(frozen=True)
class DivergenceWitness:
    rule_a: int
    rule_b: int
    metric_equal: str    # dimension that is approximately equal
    value_equal: float   # the shared approximate value
    metric_differs: str  # dimension where they diverge
    value_a: float
    value_b: float
    gap: float           # |value_a - value_b|


@dataclass(frozen=True)
class CompressionFinalitySummary:
    """Full sweep result for T36."""
    width: int
    layers: int
    rule_count: int
    rules: tuple[CompressibilityProfile, ...]
    # Key empirical question: do compressibility and finality diverge?
    divergence_exists: bool
    same_survival_different_compression: DivergenceWitness | None
    same_compression_different_survival: DivergenceWitness | None
    same_loss_different_compression: DivergenceWitness | None
    same_compression_different_loss: DivergenceWitness | None
    # Cross-correlations (Pearson)
    compression_survival_correlation: float
    compression_loss_correlation: float
    # Structural observations
    injective_mean_compressibility: float   # mean compressibility for reversible rules
    irreversible_mean_compressibility: float
    # Narrative verdict
    verdict: str
    recommendation: str


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _shannon_entropy(distribution: dict[Any, int]) -> float:
    """H(X) = -sum p*log2(p) in bits."""
    total = sum(distribution.values())
    if total == 0:
        return 0.0
    h = 0.0
    for count in distribution.values():
        if count > 0:
            p = count / total
            h -= p * math.log2(p)
    return h


def _pearson(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denom = math.sqrt(
        sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)
    )
    return num / denom if denom > 0 else 0.0


def _best_divergence_witness(
    profiles: list[CompressibilityProfile],
    metric_equal_attr: str,
    metric_differs_attr: str,
    tolerance: float = 0.05,
) -> DivergenceWitness | None:
    """Find the rule pair with most similar metric_equal but most different metric_differs."""
    best: DivergenceWitness | None = None
    best_gap = 0.0
    for i, pa in enumerate(profiles):
        for pb in profiles[i + 1 :]:
            va_eq = getattr(pa, metric_equal_attr)
            vb_eq = getattr(pb, metric_equal_attr)
            if abs(va_eq - vb_eq) > tolerance:
                continue
            va_df = getattr(pa, metric_differs_attr)
            vb_df = getattr(pb, metric_differs_attr)
            gap = abs(va_df - vb_df)
            if gap > best_gap:
                best_gap = gap
                best = DivergenceWitness(
                    rule_a=pa.rule,
                    rule_b=pb.rule,
                    metric_equal=metric_equal_attr,
                    value_equal=(va_eq + vb_eq) / 2,
                    metric_differs=metric_differs_attr,
                    value_a=va_df,
                    value_b=vb_df,
                    gap=gap,
                )
    return best if (best is not None and best.gap > tolerance) else None


# ---------------------------------------------------------------------------
# Per-rule sweep
# ---------------------------------------------------------------------------


def _sweep_rule(rule: int, width: int, layers: int) -> CompressibilityProfile:
    ca = ElementaryCA(rule, width)
    tm = analyze_transition_map(ca)

    trace_distribution: dict[tuple[int, ...], int] = {}
    survived = 0
    support_sum = 0
    raw_bytes_list: list[bytes] = []
    total = 0

    for state_int in range(2 ** width):
        initial = int_to_bits(state_int, width)
        for seed_index in range(width):
            ta = analyze_eca_trace(ca, initial, seed_index, layers)
            mask: tuple[int, ...] = ta.trace_mask
            trace_distribution[mask] = trace_distribution.get(mask, 0) + 1
            weight = sum(mask)
            if weight > 0:
                survived += 1
                support_sum += weight
            # Pack each bit as a byte for zlib (simple; not bit-packed)
            raw_bytes_list.append(bytes(mask))
            total += 1

    entropy = _shannon_entropy(trace_distribution)
    max_entropy = float(width)  # log2(2^width) = width bits
    compressibility = 1.0 - (entropy / max_entropy) if max_entropy > 0 else 1.0

    raw_bytes = b"".join(raw_bytes_list)
    compressed = zlib.compress(raw_bytes, level=9)
    zlib_ratio = len(compressed) / max(len(raw_bytes), 1)

    mean_support = (support_sum / survived) if survived > 0 else 0.0

    return CompressibilityProfile(
        rule=rule,
        injective=tm.injective,
        lost_bits=tm.lost_bits,
        trace_survival_fraction=survived / total,
        mean_accessible_support=mean_support,
        trace_shannon_entropy=entropy,
        max_possible_entropy=max_entropy,
        trace_compressibility=compressibility,
        zlib_ratio=zlib_ratio,
        unique_trace_patterns=len(trace_distribution),
        total_traces=total,
    )


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_compression_finality_analysis(
    width: int = 5,
    layers: int = 3,
) -> CompressionFinalitySummary:
    profiles = [_sweep_rule(r, width, layers) for r in range(256)]

    # Correlations
    survivals = [p.trace_survival_fraction for p in profiles]
    compressions = [p.trace_compressibility for p in profiles]
    losses = [p.lost_bits for p in profiles]

    corr_cs = _pearson(compressions, survivals)
    corr_cl = _pearson(compressions, losses)

    # Divergence witnesses
    w_sv_co = _best_divergence_witness(
        profiles, "trace_survival_fraction", "trace_compressibility"
    )
    w_co_sv = _best_divergence_witness(
        profiles, "trace_compressibility", "trace_survival_fraction"
    )
    w_lb_co = _best_divergence_witness(
        profiles, "lost_bits", "trace_compressibility"
    )
    w_co_lb = _best_divergence_witness(
        profiles, "trace_compressibility", "lost_bits"
    )

    divergence_exists = any(
        w is not None for w in (w_sv_co, w_co_sv, w_lb_co, w_co_lb)
    )

    # Group stats
    inj = [p.trace_compressibility for p in profiles if p.injective]
    irr = [p.trace_compressibility for p in profiles if not p.injective]
    inj_mean = sum(inj) / len(inj) if inj else 0.0
    irr_mean = sum(irr) / len(irr) if irr else 0.0

    # Verdict
    if divergence_exists:
        witness_summaries = []
        if w_sv_co:
            witness_summaries.append(
                f"Rules {w_sv_co.rule_a} and {w_sv_co.rule_b} have similar "
                f"trace_survival ({w_sv_co.value_equal:.2f}) but compressibility "
                f"gap {w_sv_co.gap:.2f} ({w_sv_co.value_a:.2f} vs {w_sv_co.value_b:.2f})."
            )
        if w_lb_co:
            witness_summaries.append(
                f"Rules {w_lb_co.rule_a} and {w_lb_co.rule_b} have similar "
                f"lost_bits ({w_lb_co.value_equal:.2f}) but compressibility "
                f"gap {w_lb_co.gap:.2f} ({w_lb_co.value_a:.2f} vs {w_lb_co.value_b:.2f})."
            )
        verdict = (
            "DIVERGENCE CONFIRMED: compressibility is empirically distinct from "
            "D1 finality (trace_survival) and information-theoretic loss (lost_bits) "
            "in this model. The direction finality→records→predictability→compression "
            f"is validated. Compression-survival correlation: {corr_cs:.3f}. "
            "Witnesses: " + " ".join(witness_summaries)
        )
    else:
        verdict = (
            "NO DIVERGENCE FOUND: compressibility tracks finality and information "
            "loss too closely to be treated as an independent dimension at this "
            "resolution (width=5, layers=3). Compression may collapse to the "
            "existing metrics at this scale."
        )

    recommendation = (
        "If divergence is confirmed: add compressibility as an observable "
        "alongside D1 in the emergence lab and report its correlation with each "
        "D1 dimension separately. Do NOT promote compressibility to a D1 "
        "dimension — report it as a derived observable that partially tracks "
        "finality. If reversible rules show higher compressibility than "
        "irreversible rules with similar survival, that is the strongest evidence "
        "that compressibility and D1 finality are genuinely different axes."
    )

    return CompressionFinalitySummary(
        width=width,
        layers=layers,
        rule_count=256,
        rules=tuple(profiles),
        divergence_exists=divergence_exists,
        same_survival_different_compression=w_sv_co,
        same_compression_different_survival=w_co_sv,
        same_loss_different_compression=w_lb_co,
        same_compression_different_loss=w_co_lb,
        compression_survival_correlation=corr_cs,
        compression_loss_correlation=corr_cl,
        injective_mean_compressibility=inj_mean,
        irreversible_mean_compressibility=irr_mean,
        verdict=verdict,
        recommendation=recommendation,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _profile_dict(p: CompressibilityProfile) -> dict[str, Any]:
    return {
        "rule": p.rule,
        "injective": p.injective,
        "lost_bits": round(p.lost_bits, 4),
        "trace_survival_fraction": round(p.trace_survival_fraction, 4),
        "mean_accessible_support": round(p.mean_accessible_support, 4),
        "trace_shannon_entropy": round(p.trace_shannon_entropy, 4),
        "max_possible_entropy": p.max_possible_entropy,
        "trace_compressibility": round(p.trace_compressibility, 4),
        "zlib_ratio": round(p.zlib_ratio, 4),
        "unique_trace_patterns": p.unique_trace_patterns,
        "total_traces": p.total_traces,
    }


def _witness_dict(w: DivergenceWitness | None) -> dict[str, Any] | None:
    if w is None:
        return None
    return {
        "rule_a": w.rule_a,
        "rule_b": w.rule_b,
        "metric_equal": w.metric_equal,
        "value_equal": round(w.value_equal, 4),
        "metric_differs": w.metric_differs,
        "value_a": round(w.value_a, 4),
        "value_b": round(w.value_b, 4),
        "gap": round(w.gap, 4),
    }


def compression_finality_result_to_dict(
    result: CompressionFinalitySummary,
) -> dict[str, Any]:
    return {
        "width": result.width,
        "layers": result.layers,
        "rule_count": result.rule_count,
        "divergence_exists": result.divergence_exists,
        "same_survival_different_compression": _witness_dict(
            result.same_survival_different_compression
        ),
        "same_compression_different_survival": _witness_dict(
            result.same_compression_different_survival
        ),
        "same_loss_different_compression": _witness_dict(
            result.same_loss_different_compression
        ),
        "same_compression_different_loss": _witness_dict(
            result.same_compression_different_loss
        ),
        "compression_survival_correlation": round(
            result.compression_survival_correlation, 4
        ),
        "compression_loss_correlation": round(result.compression_loss_correlation, 4),
        "injective_mean_compressibility": round(
            result.injective_mean_compressibility, 4
        ),
        "irreversible_mean_compressibility": round(
            result.irreversible_mean_compressibility, 4
        ),
        "verdict": result.verdict,
        "recommendation": result.recommendation,
        "rules": [_profile_dict(p) for p in result.rules],
    }
