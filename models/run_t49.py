"""Runner for T49: Reconstruction Without Background Time."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.reconstruction_without_background_time import run_t49_analysis, t49_result_to_dict


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t49_analysis()
    data = t49_result_to_dict(result)

    out_path = Path("results") / "reconstruction-without-background-time-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T49: Reconstruction Without Background Time ===")
    print()

    print("Axis profiles (from T48 events, target system D1Profiles):")
    print(f"  {'Event':35s}  causal  info  obs  branch")
    for p in result.axis_profiles:
        print(f"  {p.event_name:35s}  {p.causal:6d}  {p.info:4d}  {p.obs_access:3d}  {p.branch:6d}")
    print()

    print("Record-dependency order (from T48):")
    for ej, ei in result.record_order_pairs:
        tag = "" if ej == ei else "  (non-trivial)"
        print(f"  {ej} <= {ei}{tag}")
    print()

    def print_cmp(label: str, cmp) -> None:
        print(f"{label}:")
        print(f"  axes:          {cmp.axes_used}")
        print(f"  match:         {cmp.matching_pairs}/{cmp.total_pairs}  exact={cmp.is_exact_match}")
        if cmp.mismatched_pairs:
            print(f"  mismatches:    {list(cmp.mismatched_pairs)}")
        print(f"  incomparable (ref): {cmp.incomparable_pairs_in_ref}")
        print(f"  incomparable (mag): {cmp.incomparable_pairs_in_mag}")

    print_cmp("2-axis order (causal, info)", result.comparison_2axis)
    print()
    print_cmp("3-axis order (causal, info, obs_access)", result.comparison_3axis_obs)
    print()
    print_cmp("4-axis order (all axes)", result.comparison_4axis)
    print()

    print("Valid topological sorts (linear extensions of record-dependency order):")
    for sort in result.topological_sorts:
        print(f"  {list(sort)}")
    print(f"  Total: {len(result.topological_sorts)}")
    print()

    print("Anti-Scalar Theorem:")
    print(f"  Incomparable pairs:        {result.anti_scalar.incomparable_pairs}")
    print(f"  Total preorder possible:   {result.anti_scalar.total_preorder_possible}")
    print(f"  Theorem holds:             {result.anti_scalar.theorem_holds}")
    print()

    print("Reconstruction statement:")
    for line in result.reconstruction_statement.splitlines():
        print(f"  {line}")
    print()

    print("Hypotheses:")
    for h in result.hypothesis_evaluations:
        print(f"  {h.hypothesis_id} [{h.status}]: {h.claim}")
        print(f"    evidence: {h.evidence}")
    print()

    print(f"Best supported: {result.best_supported}")
    print()
    print(f"Results written to {out_path}")


if __name__ == "__main__":
    main()
