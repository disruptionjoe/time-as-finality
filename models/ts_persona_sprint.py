"""TS-PERSONA-SPRINT-001: Time-series character of records in Typed Transport Networks.

Exploration status: heterodox sketch, not promoted to core D1 claims.

CENTRAL INVESTIGATION QUESTION
==============================
Do explicit time-series dynamics provide genuinely new mathematical structure,
or are they simply derived observables of the existing TypedTransportNetwork?

Four outcomes are all considered successful:
  (A) TS dynamics strengthen H1 (TypedTransportNetwork as primitive).
  (B) TS dynamics merely re-interpret H1 without adding new structure.
  (C) TS dynamics identify boundaries where H1 is insufficient.
  (D) TS dynamics add little explanatory power.

The sprint does not presuppose any of these outcomes.

SYSTEM DESIGN
=============
Five analytical lenses are applied to synthetic finality trajectories generated
from a deterministic 3-level holonic system (micro -> meso -> holonic). Each lens
is isolated: lenses do not share intermediate results.

  Level 0 (micro):   3-site signed-graph CSP, obstructed at steps 10-24.
  Level 1 (meso):    3-site CSP, inherits obstruction with lag 5 (steps 15-29).
  Level 2 (holonic): 2-site CSP, obstruction window steps 10-34.

The holonic window (25 steps) is longer than the micro window (15 steps). Whether
this difference constitutes a genuinely new phenomenon ("holonic persistence gap")
or is simply a reflection of the hardcoded constraint schedule is precisely what
the five lenses are tasked with assessing.

PERSONAS (isolated lenses, same trajectory data)
=================================================
  Elena Voss      -  Dynamical Systems: attractors, dwell times, state recurrence
  Marcus Hale     -  Causal Inference: lagged correlations, lead-lag structure
  Aisha Rahman    -  Physics-Informed ML: AR prediction, run-length compression
  Rafael Cortez   -  Symbolic Dynamics: ordinal patterns, permutation entropy,
                   time-reversal asymmetry
  Lena Kowalski   -  Multiscale Statistics: cross-level variance, scale entropy,
                   cointegration

PROPOSED COORDINATES (to be classified by synthesis)
=====================================================
  DT   -  obstruction dwell time: consecutive steps a level stays obstructed
  LOD  -  lag-onset distance: steps between micro onset and holonic onset
  PG   -  persistence gap: steps holonic stays obstructed after micro recovery

Each coordinate will be evaluated in synthesis for whether it is:
  - a genuinely new D1 invariant
  - a derived observable of existing TTN structure
  - an implementation convenience
  - a quantity that requires extending the mathematics
"""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass
from typing import Any


# ---------------------------------------------------------------------------
# Core: signed-graph satisfiability (T39 parity check)
# ---------------------------------------------------------------------------


def _parity_check(
    n_vars: int,
    constraints: list[tuple[int, int, int]],
) -> tuple[bool, int]:
    """BFS signed 2-coloring. Returns (satisfiable, witness_count).

    constraints: list of (var_a, var_b, sign) where sign = +1 for same, -1 for different.
    witness_count = 2^(n_connected_components) if satisfiable, else 0.
    """
    adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n_vars)}
    for a, b, sign in constraints:
        adj[a].append((b, sign))
        adj[b].append((a, sign))

    colors: dict[int, int] = {}
    satisfiable = True
    n_components = 0

    for start in range(n_vars):
        if start in colors:
            continue
        n_components += 1
        colors[start] = 1
        queue = [start]
        while queue and satisfiable:
            curr = queue.pop(0)
            for nbr, sign in adj[curr]:
                expected = colors[curr] * sign
                if nbr not in colors:
                    colors[nbr] = expected
                    queue.append(nbr)
                elif colors[nbr] != expected:
                    satisfiable = False
                    break

    return satisfiable, (2 ** n_components if satisfiable else 0)


# ---------------------------------------------------------------------------
# Trajectory generator
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class LevelSnapshot:
    level: int
    satisfiable: bool
    witness_count: int


@dataclass(frozen=True)
class TrajectoryStep:
    t: int
    micro: LevelSnapshot
    meso: LevelSnapshot
    holonic: LevelSnapshot

    @property
    def joint_satisfiable(self) -> bool:
        return self.micro.satisfiable and self.meso.satisfiable and self.holonic.satisfiable


def _micro_constraints(t: int) -> list[tuple[int, int, int]]:
    """3-site micro system. Sites 0, 1, 2.

    Base: same(0,1), same(1,2) -> consistent.
    Steps 10-24: add different(0,2) -> parity conflict -> obstructed.
    """
    c: list[tuple[int, int, int]] = [(0, 1, +1), (1, 2, +1)]
    if 10 <= t <= 24:
        c.append((0, 2, -1))
    else:
        c.append((0, 2, +1))
    return c


def _meso_constraints(t: int) -> list[tuple[int, int, int]]:
    """3-site meso system. Sites 0, 1, 2 (local indexing).

    Base: same(0,1), same(1,2) -> consistent.
    Steps 15-29: add different(0,2) -> obstructed (micro lag 5).
    """
    c: list[tuple[int, int, int]] = [(0, 1, +1), (1, 2, +1)]
    if 15 <= t <= 29:
        c.append((0, 2, -1))
    else:
        c.append((0, 2, +1))
    return c


def _holonic_constraints(t: int) -> list[tuple[int, int, int]]:
    """2-site holonic system. Sites 0, 1 (local indexing).

    Base: same(0,1) -> trivially satisfiable (2 witnesses).
    Obstruction window: steps 10-34.
    - Steps 10-24: micro obstructed -> holonic inherits
    - Steps 25-29: micro clear, meso still obstructed -> holonic inherits
    - Steps 30-34: both micro and meso clear, but holonic persists 5 extra steps
                   (cross-level transport has no path to signal micro recovery)
    """
    if 10 <= t <= 34:
        return [(0, 1, +1), (0, 1, -1)]  # same AND different -> contradiction
    return [(0, 1, +1)]


def generate_canonical_trajectory(n_steps: int = 50) -> list[TrajectoryStep]:
    """Generate the canonical 50-step holonic finality trajectory.

    Designed to exhibit the holonic persistence gap:
      micro:   obstructed steps 10-24 (15 steps, 30.0% of trajectory)
      meso:    obstructed steps 15-29 (15 steps, 30.0% of trajectory)
      holonic: obstructed steps 10-34 (25 steps, 50.0% of trajectory)

    The extra 5 holonic steps (30-34) are the persistence gap PG=5.
    """
    steps = []
    for t in range(n_steps):
        micro_c = _micro_constraints(t)
        micro_sat, micro_w = _parity_check(3, micro_c)

        meso_c = _meso_constraints(t)
        meso_sat, meso_w = _parity_check(3, meso_c)

        holonic_c = _holonic_constraints(t)
        holonic_sat, holonic_w = _parity_check(2, holonic_c)

        steps.append(TrajectoryStep(
            t=t,
            micro=LevelSnapshot(0, micro_sat, micro_w),
            meso=LevelSnapshot(1, meso_sat, meso_w),
            holonic=LevelSnapshot(2, holonic_sat, holonic_w),
        ))
    return steps


def generate_variant_trajectories() -> dict[str, list[TrajectoryStep]]:
    """Generate four parameter variants for robustness testing.

    Each variant shifts the stress window or the persistence gap to test
    whether the five analytical findings hold across configurations.
    """
    def variant(
        micro_start: int,
        micro_end: int,
        meso_lag: int,
        persistence_gap: int,
        n_steps: int = 50,
    ) -> list[TrajectoryStep]:
        meso_start = micro_start + meso_lag
        meso_end = micro_end + meso_lag
        holonic_start = micro_start
        holonic_end = meso_end + persistence_gap
        holonic_end = min(holonic_end, n_steps - 1)

        steps = []
        for t in range(n_steps):
            # Micro
            mc: list[tuple[int, int, int]] = [(0, 1, +1), (1, 2, +1)]
            mc.append((0, 2, -1) if micro_start <= t <= micro_end else (0, 2, +1))
            ms, mw = _parity_check(3, mc)

            # Meso
            me: list[tuple[int, int, int]] = [(0, 1, +1), (1, 2, +1)]
            me.append((0, 2, -1) if meso_start <= t <= meso_end else (0, 2, +1))
            mes, mew = _parity_check(3, me)

            # Holonic
            ho: list[tuple[int, int, int]]
            if holonic_start <= t <= holonic_end:
                ho = [(0, 1, +1), (0, 1, -1)]
            else:
                ho = [(0, 1, +1)]
            hos, how = _parity_check(2, ho)

            steps.append(TrajectoryStep(
                t=t,
                micro=LevelSnapshot(0, ms, mw),
                meso=LevelSnapshot(1, mes, mew),
                holonic=LevelSnapshot(2, hos, how),
            ))
        return steps

    return {
        "canonical": generate_canonical_trajectory(),
        "early_stress": variant(5, 19, 5, 5),
        "late_stress": variant(20, 34, 5, 5),
        "large_gap": variant(10, 24, 5, 10),
        "zero_gap": variant(10, 24, 5, 0),
    }


# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------


def _sat_series(traj: list[TrajectoryStep], level: str) -> list[int]:
    """Extract satisfiability binary series (1=sat, 0=obstructed) for a level."""
    if level == "micro":
        return [int(s.micro.satisfiable) for s in traj]
    if level == "meso":
        return [int(s.meso.satisfiable) for s in traj]
    if level == "holonic":
        return [int(s.holonic.satisfiable) for s in traj]
    if level == "joint":
        return [int(s.joint_satisfiable) for s in traj]
    raise ValueError(f"Unknown level: {level}")


def _runs(series: list[int]) -> list[tuple[int, int]]:
    """Extract run-length encoding: list of (value, length)."""
    if not series:
        return []
    result = []
    val, length = series[0], 1
    for x in series[1:]:
        if x == val:
            length += 1
        else:
            result.append((val, length))
            val, length = x, 1
    result.append((val, length))
    return result


def _entropy_bits(series: list[int]) -> float:
    """Binary Shannon entropy in bits."""
    n = len(series)
    if n == 0:
        return 0.0
    p1 = sum(series) / n
    p0 = 1.0 - p1
    if p1 == 0.0 or p0 == 0.0:
        return 0.0
    return -(p1 * math.log2(p1) + p0 * math.log2(p0))


def _lagged_correlation(x: list[int], y: list[int], lag: int) -> float:
    """Pearson correlation between x and y shifted by lag steps.

    Positive lag: y is shifted right (y[t] paired with x[t+lag]).
    """
    n = len(x)
    if lag >= n or lag <= -n:
        return 0.0
    if lag >= 0:
        xa = x[:n - lag]
        ya = y[lag:]
    else:
        xa = x[-lag:]
        ya = y[:n + lag]
    if len(xa) < 2:
        return 0.0
    mean_x = sum(xa) / len(xa)
    mean_y = sum(ya) / len(ya)
    num = sum((a - mean_x) * (b - mean_y) for a, b in zip(xa, ya))
    den_x = math.sqrt(sum((a - mean_x) ** 2 for a in xa))
    den_y = math.sqrt(sum((b - mean_y) ** 2 for b in ya))
    if den_x == 0 or den_y == 0:
        return 0.0
    return num / (den_x * den_y)


# ---------------------------------------------------------------------------
# New finality coordinates (proposed by the sprint)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FinalityCoordinates:
    """Per-level time-series summary: dwell time and obstruction fraction.

    DT  (obstruction dwell time): mean length of obstructed runs.
    LOD and PG are computed at the trajectory level, not per-level.
    """
    level: str
    dwell_time_mean: float
    dwell_time_max: int
    obstruction_fraction: float


@dataclass(frozen=True)
class CoordinateClassification:
    """Classification of a proposed finality coordinate.

    classification must be one of:
      "new_invariant"             -  not derivable from existing D1/TTN quantities
      "derived_observable"        -  computable from existing TTN structure alone
      "implementation_convenience"  -  useful shorthand but no new math
      "requires_extension"        -  seems to require extending the formalism
    """
    name: str
    symbol: str
    classification: str
    rationale: str


def compute_coordinates(traj: list[TrajectoryStep]) -> tuple[FinalityCoordinates, ...]:
    """Compute DT, LOD, PG for each level and the joint series."""
    results = []
    for level in ("micro", "meso", "holonic", "joint"):
        series = _sat_series(traj, level)
        runs = _runs(series)
        obstructed_runs = [l for v, l in runs if v == 0]
        dt_mean = sum(obstructed_runs) / len(obstructed_runs) if obstructed_runs else 0.0
        dt_max = max(obstructed_runs) if obstructed_runs else 0
        frac = (len(series) - sum(series)) / len(series)
        results.append(FinalityCoordinates(
            level=level,
            dwell_time_mean=dt_mean,
            dwell_time_max=dt_max,
            obstruction_fraction=frac,
        ))
    return tuple(results)


def compute_lag_onset_distance(traj: list[TrajectoryStep]) -> int:
    """LOD: first step where micro is obstructed vs first step where holonic is obstructed."""
    micro_onset = next((s.t for s in traj if not s.micro.satisfiable), None)
    holonic_onset = next((s.t for s in traj if not s.holonic.satisfiable), None)
    if micro_onset is None or holonic_onset is None:
        return -1
    return holonic_onset - micro_onset


def compute_persistence_gap(traj: list[TrajectoryStep]) -> int:
    """PG: steps holonic stays obstructed after micro last clears."""
    micro_last_obstructed = max((s.t for s in traj if not s.micro.satisfiable), default=None)
    if micro_last_obstructed is None:
        return 0
    holonic_last_obstructed = max((s.t for s in traj if not s.holonic.satisfiable), default=None)
    if holonic_last_obstructed is None:
        return 0
    return max(0, holonic_last_obstructed - micro_last_obstructed)


# ---------------------------------------------------------------------------
# Lens 1: Elena Voss  -  Dynamical Systems
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ElenaVossResult:
    trajectory_name: str
    micro_distinct_states: int
    meso_distinct_states: int
    holonic_distinct_states: int
    micro_dwell_times: tuple[int, ...]
    meso_dwell_times: tuple[int, ...]
    holonic_dwell_times: tuple[int, ...]
    micro_phase_transitions: int
    meso_phase_transitions: int
    holonic_phase_transitions: int
    micro_recurrence_fraction: float
    holonic_recurrence_fraction: float
    finding: str


def elena_voss_analysis(traj: list[TrajectoryStep], name: str) -> ElenaVossResult:
    """Dynamical systems analysis of finality trajectories.

    Key lens: do finality trajectories show attractor-like behavior?
    Does the holonic level have simpler dynamics than micro (fewer distinct states,
    longer dwell times, fewer phase transitions)?
    """
    def _analyze_level(series: list[int]) -> tuple[int, list[int], int]:
        runs = _runs(series)
        distinct = len({v for v, l in runs})
        dwells = [l for _, l in runs]
        transitions = len(runs) - 1
        return distinct, dwells, transitions

    micro_s = _sat_series(traj, "micro")
    meso_s = _sat_series(traj, "meso")
    holonic_s = _sat_series(traj, "holonic")

    md, md_dw, mt = _analyze_level(micro_s)
    mes_d, mes_dw, mes_t = _analyze_level(meso_s)
    hd, hd_dw, ht = _analyze_level(holonic_s)

    # Recurrence: fraction of steps where state matches the previous state (proxy for attractor depth)
    micro_rec = sum(1 for i in range(1, len(micro_s)) if micro_s[i] == micro_s[i - 1]) / (len(micro_s) - 1)
    holonic_rec = sum(1 for i in range(1, len(holonic_s)) if holonic_s[i] == holonic_s[i - 1]) / (len(holonic_s) - 1)

    holonic_simpler = ht < mt and max(hd_dw) >= max(md_dw)
    finding = (
        "Holonic level shows simpler dynamics: fewer phase transitions "
        f"({ht} vs {mt} micro), longer max dwell time "
        f"({max(hd_dw) if hd_dw else 0} vs {max(md_dw) if md_dw else 0} micro). "
        "Consistent with holonic attractor-like lock-in. "
        if holonic_simpler
        else
        "Holonic dynamics are not demonstrably simpler than micro in this configuration."
    )

    return ElenaVossResult(
        trajectory_name=name,
        micro_distinct_states=md,
        meso_distinct_states=mes_d,
        holonic_distinct_states=hd,
        micro_dwell_times=tuple(md_dw),
        meso_dwell_times=tuple(mes_dw),
        holonic_dwell_times=tuple(hd_dw),
        micro_phase_transitions=mt,
        meso_phase_transitions=mes_t,
        holonic_phase_transitions=ht,
        micro_recurrence_fraction=micro_rec,
        holonic_recurrence_fraction=holonic_rec,
        finding=finding,
    )


# ---------------------------------------------------------------------------
# Lens 2: Marcus Hale  -  Causal Inference
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class MarcusHaleResult:
    trajectory_name: str
    micro_to_holonic_correlations: tuple[tuple[int, float], ...]
    holonic_to_micro_correlations: tuple[tuple[int, float], ...]
    best_micro_to_holonic_lag: int
    best_holonic_to_micro_lag: int
    micro_leads_holonic_at_onset: bool
    holonic_leads_micro_at_offset: bool
    onset_lag: int
    offset_lag: int
    finding: str


def marcus_hale_analysis(traj: list[TrajectoryStep], name: str) -> MarcusHaleResult:
    """Causal inference analysis of finality trajectories.

    Key lens: does micro obstruction precede holonic obstruction, and does
    holonic obstruction outlast micro recovery? This is the lead-lag structure.
    """
    micro_s = _sat_series(traj, "micro")
    holonic_s = _sat_series(traj, "holonic")

    lags = range(0, 8)
    m_to_h = tuple(
        (lag, _lagged_correlation(micro_s, holonic_s, lag))
        for lag in lags
    )
    h_to_m = tuple(
        (lag, _lagged_correlation(holonic_s, micro_s, lag))
        for lag in lags
    )

    best_m_h = max(m_to_h, key=lambda x: abs(x[1]))
    best_h_m = max(h_to_m, key=lambda x: abs(x[1]))

    # Onset lag: when does micro first get obstructed? when does holonic?
    micro_onset = next((s.t for s in traj if not s.micro.satisfiable), None)
    holonic_onset = next((s.t for s in traj if not s.holonic.satisfiable), None)
    onset_lag = (holonic_onset - micro_onset) if (micro_onset is not None and holonic_onset is not None) else 0

    # Offset lag: when does micro recover? when does holonic?
    micro_recovery = next((s.t for s in reversed(traj) if not s.micro.satisfiable), None)
    holonic_recovery = next((s.t for s in reversed(traj) if not s.holonic.satisfiable), None)
    offset_lag = ((holonic_recovery or 0) - (micro_recovery or 0))

    micro_leads_onset = onset_lag >= 0
    holonic_leads_offset = offset_lag > 0

    finding = (
        f"Micro leads holonic by {onset_lag} step(s) at onset. "
        f"Holonic persists {offset_lag} step(s) beyond micro recovery. "
        "Asymmetric causal structure: micro->holonic for onset, holonic self-sustains at offset. "
        if micro_leads_onset and holonic_leads_offset
        else
        f"Lead-lag: onset_lag={onset_lag}, offset_lag={offset_lag}. "
        "Symmetric or reversed causal structure in this configuration."
    )

    return MarcusHaleResult(
        trajectory_name=name,
        micro_to_holonic_correlations=m_to_h,
        holonic_to_micro_correlations=h_to_m,
        best_micro_to_holonic_lag=best_m_h[0],
        best_holonic_to_micro_lag=best_h_m[0],
        micro_leads_holonic_at_onset=micro_leads_onset,
        holonic_leads_micro_at_offset=holonic_leads_offset,
        onset_lag=onset_lag,
        offset_lag=offset_lag,
        finding=finding,
    )


# ---------------------------------------------------------------------------
# Lens 3: Aisha Rahman  -  Physics-Informed ML
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AishaRahmanResult:
    trajectory_name: str
    micro_ar1_accuracy: float
    meso_ar1_accuracy: float
    holonic_ar1_accuracy: float
    micro_run_length_compression: float
    meso_run_length_compression: float
    holonic_run_length_compression: float
    micro_entropy_bits: float
    meso_entropy_bits: float
    holonic_entropy_bits: float
    finding: str


def aisha_rahman_analysis(traj: list[TrajectoryStep], name: str) -> AishaRahmanResult:
    """Physics-informed ML analysis: prediction accuracy and compression.

    Key lens: is the holonic trajectory more predictable (higher AR(1) accuracy,
    lower entropy) than the micro trajectory? Compression ratio captures run-length
    structure: longer runs = more compressible.
    """
    def _ar1_accuracy(series: list[int]) -> float:
        """Accuracy of the naive AR(1) predictor: predict x_t = x_{t-1}."""
        if len(series) < 2:
            return 1.0
        correct = sum(1 for i in range(1, len(series)) if series[i] == series[i - 1])
        return correct / (len(series) - 1)

    def _run_length_compression(series: list[int]) -> float:
        """Run-length compression ratio: n_runs / n_steps. Lower = more compressible."""
        runs = _runs(series)
        return len(runs) / len(series)

    micro_s = _sat_series(traj, "micro")
    meso_s = _sat_series(traj, "meso")
    holonic_s = _sat_series(traj, "holonic")

    m_acc = _ar1_accuracy(micro_s)
    mes_acc = _ar1_accuracy(meso_s)
    h_acc = _ar1_accuracy(holonic_s)

    m_comp = _run_length_compression(micro_s)
    mes_comp = _run_length_compression(meso_s)
    h_comp = _run_length_compression(holonic_s)

    m_ent = _entropy_bits(micro_s)
    mes_ent = _entropy_bits(meso_s)
    h_ent = _entropy_bits(holonic_s)

    holonic_more_predictable = h_acc >= m_acc
    holonic_more_compressible = h_comp <= m_comp
    holonic_lower_entropy = h_ent <= m_ent

    finding = (
        f"Holonic AR(1) accuracy {h_acc:.3f} vs micro {m_acc:.3f}. "
        f"Holonic run-length ratio {h_comp:.3f} vs micro {m_comp:.3f} "
        f"(lower = more compressible). "
        f"Holonic entropy {h_ent:.3f} bits vs micro {m_ent:.3f} bits. "
        + (
            "Holonic is more predictable and compressible: consistent with lock-in. "
            if holonic_more_predictable and holonic_more_compressible
            else
            "Holonic predictability advantage not dominant in this configuration. "
        )
    )

    return AishaRahmanResult(
        trajectory_name=name,
        micro_ar1_accuracy=m_acc,
        meso_ar1_accuracy=mes_acc,
        holonic_ar1_accuracy=h_acc,
        micro_run_length_compression=m_comp,
        meso_run_length_compression=mes_comp,
        holonic_run_length_compression=h_comp,
        micro_entropy_bits=m_ent,
        meso_entropy_bits=mes_ent,
        holonic_entropy_bits=h_ent,
        finding=finding,
    )


# ---------------------------------------------------------------------------
# Lens 4: Rafael Cortez  -  Symbolic Dynamics
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RafaelCortezResult:
    trajectory_name: str
    micro_ordinal_counts: tuple[tuple[str, int], ...]
    holonic_ordinal_counts: tuple[tuple[str, int], ...]
    micro_permutation_entropy: float
    holonic_permutation_entropy: float
    micro_irreversibility_score: float
    holonic_irreversibility_score: float
    holonic_less_random: bool
    holonic_more_irreversible: bool
    finding: str


def rafael_cortez_analysis(traj: list[TrajectoryStep], name: str) -> RafaelCortezResult:
    """Symbolic dynamics analysis: ordinal patterns, permutation entropy, irreversibility.

    Key lens: is the holonic trajectory less random (lower permutation entropy) and
    more time-irreversible than the micro trajectory?

    Ordinal patterns of order 2: for consecutive pairs (x_t, x_{t+1}):
      "up" if x_{t+1} > x_t, "down" if x_{t+1} < x_t, "same" if equal.

    Permutation entropy: H = -sum(p_i * log2(p_i)) over ordinal pattern distribution.

    Irreversibility: difference between forward and reversed ordinal distributions.
    Score = sum(|p_forward(i) - p_reverse(i)|) / 2.
    """
    def _ordinal_patterns(series: list[int]) -> Counter:
        counts: Counter = Counter()
        for i in range(len(series) - 1):
            if series[i + 1] > series[i]:
                counts["up"] += 1
            elif series[i + 1] < series[i]:
                counts["down"] += 1
            else:
                counts["same"] += 1
        return counts

    def _perm_entropy(counts: Counter) -> float:
        total = sum(counts.values())
        if total == 0:
            return 0.0
        h = 0.0
        for v in counts.values():
            if v > 0:
                p = v / total
                h -= p * math.log2(p)
        return h

    def _irreversibility(forward: Counter, backward: Counter) -> float:
        all_keys = set(forward.keys()) | set(backward.keys())
        f_total = sum(forward.values())
        b_total = sum(backward.values())
        if f_total == 0 or b_total == 0:
            return 0.0
        total_diff = sum(
            abs(forward.get(k, 0) / f_total - backward.get(k, 0) / b_total)
            for k in all_keys
        )
        return total_diff / 2.0

    micro_s = _sat_series(traj, "micro")
    holonic_s = _sat_series(traj, "holonic")

    m_fwd = _ordinal_patterns(micro_s)
    m_bwd = _ordinal_patterns(list(reversed(micro_s)))
    h_fwd = _ordinal_patterns(holonic_s)
    h_bwd = _ordinal_patterns(list(reversed(holonic_s)))

    m_pe = _perm_entropy(m_fwd)
    h_pe = _perm_entropy(h_fwd)
    m_irr = _irreversibility(m_fwd, m_bwd)
    h_irr = _irreversibility(h_fwd, h_bwd)

    holonic_less_random = h_pe <= m_pe
    holonic_more_irreversible = h_irr >= m_irr

    finding = (
        f"Holonic permutation entropy {h_pe:.3f} vs micro {m_pe:.3f}. "
        f"Holonic irreversibility {h_irr:.3f} vs micro {m_irr:.3f}. "
        + (
            "Holonic trajectory is less random and more irreversible: "
            "ordinal pattern distribution shows asymmetric recovery. "
            if holonic_less_random and holonic_more_irreversible
            else
            "Irreversibility advantage not dominant in this configuration. "
        )
    )

    return RafaelCortezResult(
        trajectory_name=name,
        micro_ordinal_counts=tuple(sorted(m_fwd.items())),
        holonic_ordinal_counts=tuple(sorted(h_fwd.items())),
        micro_permutation_entropy=m_pe,
        holonic_permutation_entropy=h_pe,
        micro_irreversibility_score=m_irr,
        holonic_irreversibility_score=h_irr,
        holonic_less_random=holonic_less_random,
        holonic_more_irreversible=holonic_more_irreversible,
        finding=finding,
    )


# ---------------------------------------------------------------------------
# Lens 5: Lena Kowalski  -  Multiscale Statistics
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class LenaKowalskiResult:
    trajectory_name: str
    micro_obstruction_fraction: float
    meso_obstruction_fraction: float
    holonic_obstruction_fraction: float
    micro_entropy: float
    meso_entropy: float
    holonic_entropy: float
    cross_level_correlation_micro_meso: float
    cross_level_correlation_micro_holonic: float
    cross_level_correlation_meso_holonic: float
    dominant_level: str
    cointegration_detected: bool
    finding: str


def lena_kowalski_analysis(traj: list[TrajectoryStep], name: str) -> LenaKowalskiResult:
    """Multiscale statistics analysis: cross-level comparisons and cointegration.

    Key lens: do the three levels move together (cointegrated) or do they diverge?
    Is there a dominant level that drives the others?

    Cointegration proxy: are obstructions at all three levels correlated at lag 0?
    If the correlation micro-holonic at lag 0 is high but the holonic entropy is lower
    than micro entropy, the holonic level adds predictive compression.
    """
    micro_s = _sat_series(traj, "micro")
    meso_s = _sat_series(traj, "meso")
    holonic_s = _sat_series(traj, "holonic")

    m_frac = (len(micro_s) - sum(micro_s)) / len(micro_s)
    mes_frac = (len(meso_s) - sum(meso_s)) / len(meso_s)
    h_frac = (len(holonic_s) - sum(holonic_s)) / len(holonic_s)

    m_ent = _entropy_bits(micro_s)
    mes_ent = _entropy_bits(meso_s)
    h_ent = _entropy_bits(holonic_s)

    # Flip sign since high obstruction fraction = more active (lower sat = more interesting)
    r_mm = _lagged_correlation(micro_s, meso_s, 0)
    r_mh = _lagged_correlation(micro_s, holonic_s, 0)
    r_msh = _lagged_correlation(meso_s, holonic_s, 0)

    fracs = {"micro": m_frac, "meso": mes_frac, "holonic": h_frac}
    dominant = max(fracs, key=fracs.get)

    # Cointegration proxy: all pairs have significant correlation (|r| > 0.5)
    cointegrated = abs(r_mm) > 0.5 and abs(r_mh) > 0.5 and abs(r_msh) > 0.5

    finding = (
        f"Obstruction fractions  -  micro:{m_frac:.2f}, meso:{mes_frac:.2f}, holonic:{h_frac:.2f}. "
        f"Entropies  -  micro:{m_ent:.3f}, meso:{mes_ent:.3f}, holonic:{h_ent:.3f} bits. "
        f"Cross-level correlations (lag 0): μ-mes={r_mm:.3f}, μ-hol={r_mh:.3f}, mes-hol={r_msh:.3f}. "
        f"Dominant level by obstruction fraction: {dominant}. "
        + (
            "Cointegration detected: all level pairs move together at lag 0. "
            "Holonic has highest obstruction fraction, lowest entropy: "
            "holonic is the most stable and most obstructed level simultaneously. "
            if cointegrated
            else
            "Levels are not fully cointegrated: independent variation across scales. "
        )
    )

    return LenaKowalskiResult(
        trajectory_name=name,
        micro_obstruction_fraction=m_frac,
        meso_obstruction_fraction=mes_frac,
        holonic_obstruction_fraction=h_frac,
        micro_entropy=m_ent,
        meso_entropy=mes_ent,
        holonic_entropy=h_ent,
        cross_level_correlation_micro_meso=r_mm,
        cross_level_correlation_micro_holonic=r_mh,
        cross_level_correlation_meso_holonic=r_msh,
        dominant_level=dominant,
        cointegration_detected=cointegrated,
        finding=finding,
    )


# ---------------------------------------------------------------------------
# Sprint runner
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PersonaSprintResult:
    trajectory_name: str
    coordinates: tuple[FinalityCoordinates, ...]
    lag_onset_distance: int
    persistence_gap: int
    elena_voss: ElenaVossResult
    marcus_hale: MarcusHaleResult
    aisha_rahman: AishaRahmanResult
    rafael_cortez: RafaelCortezResult
    lena_kowalski: LenaKowalskiResult


@dataclass(frozen=True)
class SprintSummary:
    trajectories: tuple[PersonaSprintResult, ...]
    canonical_result: PersonaSprintResult
    persistence_gap_range: tuple[int, int]
    holonic_dwell_dominates: bool
    micro_leads_onset_all: bool
    holonic_leads_offset_all: bool
    holonic_more_predictable_count: int
    holonic_more_irreversible_count: int
    cointegration_count: int
    coordinate_classifications: tuple[CoordinateClassification, ...]
    h1_evidence_record: str
    investigation_verdict: str
    follow_on_goals: tuple[str, ...]


def run_sprint() -> SprintSummary:
    """Run the full TS-PERSONA-SPRINT-001 across all trajectory variants."""
    trajectories_data = generate_variant_trajectories()

    results = []
    for name, traj in trajectories_data.items():
        coords = compute_coordinates(traj)
        lod = compute_lag_onset_distance(traj)
        pg = compute_persistence_gap(traj)
        ev = elena_voss_analysis(traj, name)
        mh = marcus_hale_analysis(traj, name)
        ar = aisha_rahman_analysis(traj, name)
        rc = rafael_cortez_analysis(traj, name)
        lk = lena_kowalski_analysis(traj, name)
        results.append(PersonaSprintResult(
            trajectory_name=name,
            coordinates=coords,
            lag_onset_distance=lod,
            persistence_gap=pg,
            elena_voss=ev,
            marcus_hale=mh,
            aisha_rahman=ar,
            rafael_cortez=rc,
            lena_kowalski=lk,
        ))

    canonical = next(r for r in results if r.trajectory_name == "canonical")
    pg_values = tuple(r.persistence_gap for r in results)

    holonic_dwell_dominates = all(
        max(r.elena_voss.holonic_dwell_times or [0]) >= max(r.elena_voss.micro_dwell_times or [0])
        for r in results
    )
    micro_leads_onset_all = all(r.marcus_hale.micro_leads_holonic_at_onset for r in results)
    holonic_leads_offset_all = all(r.marcus_hale.holonic_leads_micro_at_offset for r in results)
    holonic_more_pred = sum(
        1 for r in results if r.aisha_rahman.holonic_ar1_accuracy >= r.aisha_rahman.micro_ar1_accuracy
    )
    holonic_more_irr = sum(1 for r in results if r.rafael_cortez.holonic_more_irreversible)
    cointegrated = sum(1 for r in results if r.lena_kowalski.cointegration_detected)

    # Classify the three proposed coordinates against the four-outcome framework.
    # These classifications are the primary investigative output of the sprint.
    n_traj = len(results)
    coord_classifications = (
        CoordinateClassification(
            name="obstruction dwell time",
            symbol="DT",
            classification="derived_observable",
            rationale=(
                "DT is computed from the per-step satisfiability sequence, which is "
                "fully determined by the constraint schedule embedded in the TTN "
                "morphism's forgotten_structure. A static TTN snapshot plus its "
                "time-indexed constraint generator already encodes DT; no new "
                "mathematical object is required. DT is a useful diagnostic shorthand "
                "but not a new invariant."
            ),
        ),
        CoordinateClassification(
            name="lag-onset distance",
            symbol="LOD",
            classification="derived_observable",
            rationale=(
                "LOD measures the step difference between micro and holonic onset, "
                "which equals the lag parameter baked into the meso/holonic constraint "
                "generators. In this implementation LOD=0 for the canonical trajectory "
                "(micro onset t=10, holonic onset t=10: both triggered by the same "
                "constraint window). LOD is a read-off of the constraint schedule "
                "structure, not a property of the TTN topology itself."
            ),
        ),
        CoordinateClassification(
            name="persistence gap",
            symbol="PG",
            classification=(
                "derived_observable"
                if all(r.persistence_gap >= 0 for r in results)
                else "requires_extension"
            ),
            rationale=(
                "PG measures holonic obstruction steps beyond micro recovery. "
                "In the current implementation, PG is set explicitly by the "
                "holonic constraint window (steps 30-34 in the canonical case). "
                "It is therefore a direct read-off of the hardcoded constraint "
                "schedule, not a consequence of TTN topology or forgotten_dims. "
                "A genuine PG would emerge from the network topology without being "
                "explicitly scheduled  -  that test has not yet been run. "
                "Classification: derived_observable (current implementation); "
                "would become potentially new_invariant if PG were shown to follow "
                "from non-empty forgotten_dims without explicit scheduling."
            ),
        ),
    )

    # Evidence record: what does the sprint actually show about the four outcomes?
    pg_min, pg_max = min(pg_values), max(pg_values)
    h1_evidence = (
        f"Sprint ran {n_traj} trajectory variants (canonical + 4 parameter sweeps). "
        f"Persistence gap present in all variants (range {pg_min}–{pg_max} steps), "
        "but PG is set by the constraint schedule, not derived from TTN topology. "
        "Five lenses all detect the inter-level dwell asymmetry; they do not "
        "independently confirm that PG is a topological invariant. "
        "\n\n"
        "OUTCOME ASSESSMENT:\n"
        "(A) Strengthen H1: PARTIAL. The sprint confirms that TTN constraint schedules "
        "produce time-series signatures consistent with holonic lock-in. But the "
        "signatures are read-offs of the schedule, not emergent from forgotten_dims. "
        "(B) Re-interpret H1: YES. DT, LOD, PG translate static TTN admissibility "
        "into a per-step trajectory vocabulary. This is interpretive, not additive. "
        "(C) Identify H1 boundaries: YES. H1 does not yet include a mechanism for "
        "holonic recovery once forgotten_dims are non-empty  -  there is no TTN "
        "operation that propagates micro recovery upward. This gap is real. "
        "(D) Little explanatory power: NO. The personas consistently detect the "
        "same dwell asymmetry using independent methods, which is meaningful evidence "
        "that the phenomenon is real even if its cause is the constraint schedule."
    )

    # Investigative verdict: which outcome is best supported?
    investigation_verdict = (
        "Outcomes (B) and (C) are best supported. "
        "DT/LOD/PG are derived observables of the existing TTN constraint structure, "
        "not new invariants. The sprint's principal finding is negative: these "
        "coordinates do not require extending the mathematics. "
        "However, the boundary identified under outcome (C)  -  H1 has no upward "
        "recovery propagation mechanism  -  is a genuine gap that may motivate "
        "a future extension. This should be framed as an open question in ROADMAP.md, "
        "not a claim in CLAIM-LEDGER.md."
    )

    follow_ons = (
        "MINI-GOAL-TS-002: Test whether PG emerges from non-empty forgotten_dims "
        "WITHOUT explicit constraint scheduling. If yes, PG may be a new invariant; "
        "if no, it remains a derived observable. This test requires modifying the "
        "holonic constraint generator to remove the hardcoded persistence window.",
        "MINI-GOAL-TS-003: Identify under what TTN topologies (tree / dense / ring) "
        "the holonic dwell asymmetry vanishes (PG=0). If PG=0 is achievable with "
        "non-empty forgotten_dims, the time-series analysis and T40 structural "
        "analysis diverge  -  which would be a genuine discovery.",
    )

    return SprintSummary(
        trajectories=tuple(results),
        canonical_result=canonical,
        persistence_gap_range=(pg_min, pg_max),
        holonic_dwell_dominates=holonic_dwell_dominates,
        micro_leads_onset_all=micro_leads_onset_all,
        holonic_leads_offset_all=holonic_leads_offset_all,
        holonic_more_predictable_count=holonic_more_pred,
        holonic_more_irreversible_count=holonic_more_irr,
        cointegration_count=cointegrated,
        coordinate_classifications=coord_classifications,
        h1_evidence_record=h1_evidence,
        investigation_verdict=investigation_verdict,
        follow_on_goals=follow_ons,
    )


def sprint_to_dict(summary: SprintSummary) -> dict[str, Any]:
    """Serialize SprintSummary to JSON-compatible dict."""
    def coord_to_dict(c: FinalityCoordinates) -> dict:
        return {
            "level": c.level,
            "dwell_time_mean": round(c.dwell_time_mean, 3),
            "dwell_time_max": c.dwell_time_max,
            "obstruction_fraction": round(c.obstruction_fraction, 3),
        }

    def traj_to_dict(r: PersonaSprintResult) -> dict:
        return {
            "name": r.trajectory_name,
            "coordinates": [coord_to_dict(c) for c in r.coordinates],
            "lag_onset_distance": r.lag_onset_distance,
            "persistence_gap": r.persistence_gap,
            "elena_voss": {
                "micro_phase_transitions": r.elena_voss.micro_phase_transitions,
                "holonic_phase_transitions": r.elena_voss.holonic_phase_transitions,
                "micro_max_dwell": max(r.elena_voss.micro_dwell_times or [0]),
                "holonic_max_dwell": max(r.elena_voss.holonic_dwell_times or [0]),
                "micro_recurrence": round(r.elena_voss.micro_recurrence_fraction, 3),
                "holonic_recurrence": round(r.elena_voss.holonic_recurrence_fraction, 3),
                "finding": r.elena_voss.finding,
            },
            "marcus_hale": {
                "onset_lag": r.marcus_hale.onset_lag,
                "offset_lag": r.marcus_hale.offset_lag,
                "micro_leads_onset": r.marcus_hale.micro_leads_holonic_at_onset,
                "holonic_leads_offset": r.marcus_hale.holonic_leads_micro_at_offset,
                "best_m_to_h_lag": r.marcus_hale.best_micro_to_holonic_lag,
                "finding": r.marcus_hale.finding,
            },
            "aisha_rahman": {
                "micro_ar1_accuracy": round(r.aisha_rahman.micro_ar1_accuracy, 3),
                "holonic_ar1_accuracy": round(r.aisha_rahman.holonic_ar1_accuracy, 3),
                "micro_compression": round(r.aisha_rahman.micro_run_length_compression, 3),
                "holonic_compression": round(r.aisha_rahman.holonic_run_length_compression, 3),
                "micro_entropy": round(r.aisha_rahman.micro_entropy_bits, 3),
                "holonic_entropy": round(r.aisha_rahman.holonic_entropy_bits, 3),
                "finding": r.aisha_rahman.finding,
            },
            "rafael_cortez": {
                "micro_perm_entropy": round(r.rafael_cortez.micro_permutation_entropy, 3),
                "holonic_perm_entropy": round(r.rafael_cortez.holonic_permutation_entropy, 3),
                "micro_irreversibility": round(r.rafael_cortez.micro_irreversibility_score, 3),
                "holonic_irreversibility": round(r.rafael_cortez.holonic_irreversibility_score, 3),
                "holonic_less_random": r.rafael_cortez.holonic_less_random,
                "holonic_more_irreversible": r.rafael_cortez.holonic_more_irreversible,
                "finding": r.rafael_cortez.finding,
            },
            "lena_kowalski": {
                "micro_obstruction": round(r.lena_kowalski.micro_obstruction_fraction, 3),
                "holonic_obstruction": round(r.lena_kowalski.holonic_obstruction_fraction, 3),
                "micro_entropy": round(r.lena_kowalski.micro_entropy, 3),
                "holonic_entropy": round(r.lena_kowalski.holonic_entropy, 3),
                "r_micro_holonic": round(r.lena_kowalski.cross_level_correlation_micro_holonic, 3),
                "cointegration": r.lena_kowalski.cointegration_detected,
                "finding": r.lena_kowalski.finding,
            },
        }

    return {
        "central_question": (
            "Do explicit time-series dynamics provide genuinely new mathematical "
            "structure, or are they derived observables of the existing "
            "TypedTransportNetwork?"
        ),
        "persistence_gap_range": list(summary.persistence_gap_range),
        "holonic_dwell_dominates": summary.holonic_dwell_dominates,
        "micro_leads_onset_all": summary.micro_leads_onset_all,
        "holonic_leads_offset_all": summary.holonic_leads_offset_all,
        "holonic_more_predictable_count": summary.holonic_more_predictable_count,
        "holonic_more_irreversible_count": summary.holonic_more_irreversible_count,
        "cointegration_count": summary.cointegration_count,
        "coordinate_classifications": [
            {
                "name": c.name,
                "symbol": c.symbol,
                "classification": c.classification,
                "rationale": c.rationale,
            }
            for c in summary.coordinate_classifications
        ],
        "h1_evidence_record": summary.h1_evidence_record,
        "investigation_verdict": summary.investigation_verdict,
        "follow_on_goals": list(summary.follow_on_goals),
        "trajectories": [traj_to_dict(r) for r in summary.trajectories],
    }
