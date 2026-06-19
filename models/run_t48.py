"""Runner for T48: FinaliEvent Structure."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.finali_event_structure import run_t48_analysis, t48_result_to_dict


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t48_analysis()
    data = t48_result_to_dict(result)

    out_path = Path("results") / "finali-event-structure-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T48: FinaliEvent Structure ===")
    print()

    print("Events:")
    for e in result.events:
        verdict = "PO1" if e.admissibility.po1_evidence else f"FAIL({e.admissibility.verdict})"
        print(
            f"  {e.name:30s}  {e.morphism.source.name} -> {e.morphism.target.name}"
            f"  [{verdict}]  causal={e.causal_magnitude}  info={e.info_magnitude}"
        )
    print()

    print("Record bases:")
    for b in result.record_bases:
        print(f"  {b.system_name:30s}  {sorted(b.records)}")
    print()

    print("Direct dependencies (record containment):")
    if result.direct_dependencies:
        for dep in result.direct_dependencies:
            print(f"  {dep.predecessor} <= {dep.successor}")
            print(f"    basis: {dep.basis}")
    else:
        print("  (none)")
    print()

    po = result.partial_order
    print(f"Partial order verification:")
    print(f"  Reflexive:     {po.reflexive}")
    print(f"  Antisymmetric: {po.antisymmetric}")
    print(f"  Transitive:    {po.transitive}")
    print(f"  Is partial order: {po.is_partial_order}")
    print(f"  Order pairs ({len(po.order_pairs)} total): {list(po.order_pairs)}")
    print()

    print(f"Incomparable pairs: {result.incomparable_pairs}")
    print(f"Root events:        {result.root_events}")
    print()

    print("Hasse diagram:")
    for line in result.hasse_description.splitlines():
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
