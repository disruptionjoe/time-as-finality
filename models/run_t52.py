"""Runner for T52: Symmetric Colimit Theorem."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.symmetric_colimit_theorem import run_t52_analysis, t52_result_to_dict


def _am_line(am) -> str:
    tag = "holds" if am.am_holds else f"FAILS — spurious={list(am.spurious)}, missing={list(am.missing)}"
    return f"  {am.witness_name}: AM {tag}  ({am.pairs_checked} pairs)"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t52_analysis()
    data = t52_result_to_dict(result)

    out_path = Path("results") / "symmetric-colimit-theorem-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T52: Symmetric Colimit Theorem ===")
    print()

    print("─── Events (axis profiles) ───")
    for e in result.events:
        adm = "PO1-admissible" if e.admissibility.po1_evidence else "NOT admissible"
        print(f"  {e.name}: causal={e.causal_magnitude}, info={e.info_magnitude}  [{adm}]")
    print()

    print("─── Apparent Orders ───")
    def nr(order):
        return sorted(p for p in order if p[0] != p[1])
    print(f"  Reference:  {nr(result.reference.apparent_order)}")
    print(f"  Observer A: {nr(result.observer_a.apparent_order)}"
          f"  (incomparable: {list(result.observer_a.incomparable_pairs)})")
    print(f"  Observer B: {nr(result.observer_b.apparent_order)}"
          f"  (incomparable: {list(result.observer_b.incomparable_pairs)})")
    print()

    print("─── Colimit ───")
    col = result.colimit
    print(f"  colimit order: {nr(col.colimit_order)}")
    print(f"  is_valid_partial_order: {col.is_valid_partial_order}"
          f"  (R={col.reflexive}, A={col.antisymmetric}, T={col.transitive})")
    print(f"  equals_reference: {col.equals_reference}")
    print(f"  new_from_A (in colimit, not in S_A): {list(col.new_from_a)}")
    print(f"  new_from_B (in colimit, not in S_B): {list(col.new_from_b)}")
    print()

    print("─── Axis Monotonicity (AM) ───")
    for am in (result.am_reference, result.am_observer_a, result.am_observer_b, result.am_colimit):
        print(_am_line(am))
    print()

    print("─── Phantom Incomparabilities ───")
    phantoms = [p for p in result.phantoms if p.is_phantom]
    if phantoms:
        for p in phantoms:
            print(f"  [{p.observer}] ({p.event_j}, {p.event_i}): "
                  f"observer_says={p.observer_says}, colimit_says={p.colimit_says}  ← PHANTOM")
    else:
        print("  None.")
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
