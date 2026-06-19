"""Runner for T55B: Provenance-Aware Reconstruction Separation Audit."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.provenance_aware_reconstruction import run_t55b_analysis, t55b_result_to_dict


def _fmt_paths(paths) -> str:
    if not paths:
        return "    (none)"
    lines = []
    for p in paths:
        hop = "direct" if p.is_direct_observation else f"{len(p.path)-1}-hop"
        lines.append(f"    {p.record}: {' → '.join(p.path)}  ({hop})")
    return "\n".join(lines)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t55b_analysis()
    data = t55b_result_to_dict(result)

    out_path = Path("results") / "provenance-aware-reconstruction-separation-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T55B: Provenance-Aware Reconstruction Separation Audit ===")
    print()

    print("─── Propagation Scenarios ───")
    for s in result.scenarios:
        print(f"  {s.name}: observers={list(s.observers)}")
        for e in s.edges:
            print(f"    {e.source} → {e.target}: {sorted(e.records)} (step={e.step})")
        for o in s.origins:
            print(f"    origin: {o.observer} observes {o.record}")
    print()

    print("─── Observer States ───")
    for state in result.observer_states:
        print(f"  {state.observer} in {state.scenario}: {sorted(state.accessible_records)}")
        print("  provenance paths:")
        print(_fmt_paths(state.provenance_paths))
    print()

    print("─── Separation Witnesses ───")
    for w in result.separation_witnesses:
        print(f"  [{w.name}] {w.description}")
        print(f"    same_record_basis: {w.same_record_basis}")
        print(f"    same_provenance:   {w.same_provenance_structure}")
        print(f"    finding: {w.finding[:120]}...")
    print()

    print("─── Colimit Comparison (W_A scenarios) ───")
    for c in result.colimit_results:
        nr = sorted((a, b) for a, b in c.event_order if a != b)
        print(f"  {c.scenario_name}:")
        print(f"    accessible: {sorted(c.accessible_records)}")
        print(f"    event order (non-refl): {nr}")
        print(f"    AM holds: {c.am_holds}")
    identical = result.colimit_results[0].event_order == result.colimit_results[1].event_order
    print(f"  → Colimit orders identical: {identical}")
    print()

    print("─── W_D: Propagation Order vs Event-Finality Order ───")
    wd = result.event_order_ambiguity
    print(f"  accessible at C: {sorted(wd.accessible_at_observer)}")
    nc = sorted((a, b) for a, b in wd.order_concurrent if a != b)
    no = sorted((a, b) for a, b in wd.order_ordered if a != b)
    print(f"  event order (concurrent structure): {nc}")
    print(f"  event order (ordered structure):    {no}")
    print(f"  propagation_order_determines_event_order: {wd.propagation_order_determines_event_order}")
    print()

    print("─── W_T54: T54 Provenance-Blindness ───")
    wt54 = result.t54_invariance
    print(f"  basis_identical: {wt54.basis_identical}")
    print(f"  t54_input_identical: {wt54.t54_input_identical}")
    print()

    print("─── Hypothesis Verdicts ───")
    for h in result.hypothesis_verdicts:
        print(f"  [{h.hypothesis_id}] {h.status.upper()}")
        print(f"    {h.claim}")
    print()

    print("─── Recommendation ───")
    print(f"  {result.recommendation}")
    print()

    print("─── Open Questions ───")
    for i, q in enumerate(result.open_questions, 1):
        print(f"  {i}. {q[:100]}...")
    print()

    print(f"Best supported: {result.best_supported}")
    print()
    print(f"Results written to {out_path}")


if __name__ == "__main__":
    main()
