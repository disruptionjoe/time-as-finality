"""Runner for T50: Axis Monotonicity Theorem."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.axis_monotonicity_theorem import run_t50_analysis, t50_result_to_dict


def _print_am(label: str, am) -> None:
    print(f"{label}:")
    print(f"  axes:            {am.axes}")
    print(f"  pairs checked:   {am.pairs_checked}")
    print(f"  AM holds:        {am.am_holds}")
    print(f"  violations:      {len(am.violations)}  (spurious={am.spurious_count}, missing={am.missing_count})")
    for v in am.violations:
        tag = "SPURIOUS" if v.in_magnitude_order and not v.in_record_order else "MISSING"
        print(f"    [{tag}] ({v.event_j}, {v.event_i}): record={v.in_record_order}, mag={v.in_magnitude_order}")


def _print_nec(label: str, r) -> None:
    print(f"{label}:")
    print(f"  axes:            {r.axes_used}")
    print(f"  match:           {r.matching_pairs}/{r.total_pairs}  exact={r.is_exact_match}")
    if r.spurious_pairs:
        print(f"  spurious pairs:  {list(r.spurious_pairs)}  (magnitude says ≤ but record says ||)")
    if r.missing_pairs:
        print(f"  missing pairs:   {list(r.missing_pairs)}  (record says ≤ but magnitude says ||)")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t50_analysis()
    data = t50_result_to_dict(result)

    out_path = Path("results") / "axis-monotonicity-theorem-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T50: Axis Monotonicity Theorem ===")
    print()

    print("─── Sufficiency: AM check on T48 normal witness ───")
    _print_am("T48 normal (2-axis: causal, info)", result.am_normal)
    print()

    print("─── Counterexample: AM check on violating witness ───")
    print("  O3_violating: D1Profile(..., reversal_cost=1) — causal axis reversed vs O1")
    print("  Record containment: O1.records ⊆ U3.records → e1 ≤_rec e3_violating")
    print("  Axis reversal:      causal(e1)=2 > causal(e3_viol)=1 → NOT e1 ≤_mag e3_viol")
    _print_am("T50 violating (2-axis: causal, info)", result.am_violating)
    print()

    print("─── Axis Necessity: single-axis reconstruction on T48 witness ───")
    _print_nec("Causal only", result.necessity_causal_only)
    _print_nec("Info only", result.necessity_info_only)
    _print_nec("2-axis (causal + info)", result.necessity_2axis)
    print()

    print("─── Anti-Scalar Corollary ───")
    for line in result.anti_scalar_corollary.splitlines():
        print(f"  {line}")
    print()

    print("─── Hypothesis Verdicts ───")
    for h in result.hypothesis_evaluations:
        print(f"  {h.hypothesis_id} [{h.status}]")
        print(f"    {h.claim}")
        print(f"    evidence: {h.evidence}")
    print()

    print(f"Best supported: {result.best_supported}")
    print()
    print(f"Results written to {out_path}")


if __name__ == "__main__":
    main()
