"""Runner for T47: PO1 DAG theorem."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.po1_dag_theorem import run_t47_analysis, t47_result_to_dict


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t47_analysis()
    data = t47_result_to_dict(result)

    out_path = Path("results") / "po1-dag-theorem-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T47: PO1 DAG Theorem ===")
    print()
    print("Systems:")
    for n in result.system_nodes:
        print(f"  {n.name:35s}  sites={n.site_count}  obstructed={str(n.obstructed):5s}  layer={n.layer}")
    print()

    po1_edges = [(r.source, r.target) for r in result.edge_results if r.is_po1]
    by_failure: dict[str, int] = {}
    for r in result.edge_results:
        if not r.is_po1:
            by_failure[r.primary_failure] = by_failure.get(r.primary_failure, 0) + 1

    print(f"Pairs tested: {len(result.edge_results)}")
    print(f"PO1-admissible edges: {len(po1_edges)}")
    for src, tgt in po1_edges:
        print(f"  {src} -> {tgt}")
    print()
    print("Rejected edges by primary failure:")
    for reason, count in sorted(by_failure.items()):
        print(f"  {reason}: {count}")
    print()

    dag = result.dag_analysis
    print(f"DAG check:         {dag.is_dag}")
    print(f"Max path depth:    {dag.max_depth}")
    print(f"Bipartite:         {dag.bipartite_confirmed}")
    print(f"Pre-finality:      {dag.pre_finality_nodes}")
    print(f"Post-finality:     {dag.post_finality_nodes}")
    print(f"Topological sort:  {dag.topological_sort}")
    print()
    print("Theorem:")
    print(f"  {result.theorem_statement}")
    print()
    print("Corollaries:")
    print(f"  Depth:     {result.corollary_depth}")
    print(f"  Bipartite: {result.corollary_bipartite}")
    print(f"  Border:    {result.corollary_border}")
    print()
    print("Hypotheses:")
    for h in result.hypothesis_evaluations:
        print(f"  {h.hypothesis_id} [{h.status}]: {h.claim}")
    print()
    print(f"Best supported: {result.best_supported}")
    print()
    print(f"Results written to {out_path}")


if __name__ == "__main__":
    main()
