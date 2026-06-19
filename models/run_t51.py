"""Runner for T51: Multi-Observer Apparent Finality Colimit."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.multi_observer_apparent_finality_colimit import (
    run_t51_analysis,
    t51_result_to_dict,
)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t51_analysis()
    data = t51_result_to_dict(result)

    out_path = Path("results") / "multi-observer-apparent-finality-colimit-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T51: Multi-Observer Apparent Finality Colimit ===")
    print()

    print("─── Record Bases ───")
    for b in result.observer_a.record_bases:
        if b.system_name.startswith("U"):
            b_b = next(rb for rb in result.observer_b.record_bases
                       if rb.system_name == b.system_name)
            if b.records != b_b.records:
                print(f"  {b.system_name}:")
                print(f"    Observer A: {sorted(b.records)}")
                print(f"    Observer B: {sorted(b_b.records)}  ← restricted")
            else:
                print(f"  {b.system_name}: {sorted(b.records)}")
    print()

    print("─── Apparent Orders ───")
    for obs in (result.observer_a, result.observer_b):
        non_refl = sorted(p for p in obs.apparent_order if p[0] != p[1])
        print(f"  {obs.name}: {non_refl}")
        if obs.incomparable_pairs:
            print(f"    incomparable: {list(obs.incomparable_pairs)}")
    print()

    print("─── Colimit ───")
    col = result.colimit
    non_refl_col = sorted(p for p in col.colimit_order if p[0] != p[1])
    print(f"  colimit order: {non_refl_col}")
    print(f"  is_partial_order: {col.is_partial_order}  "
          f"(reflexive={col.reflexive}, antisymmetric={col.antisymmetric}, "
          f"transitive={col.transitive})")
    if col.new_orderings:
        print(f"  new orderings (in colimit, not in S_B): {list(col.new_orderings)}")
    print()

    print("─── Phantom Incomparabilities ───")
    phantoms = [p for p in result.phantom_results if p.is_phantom]
    if phantoms:
        for p in phantoms:
            print(f"  [{p.observer_name}] ({p.event_j}, {p.event_i}): "
                  f"observer_sees={p.observer_sees}, colimit_says={p.colimit_says}  ← PHANTOM")
    else:
        print("  None detected.")
    print()

    print("─── T47 Consistency ───")
    print(f"  {result.t47_consistency}")
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
