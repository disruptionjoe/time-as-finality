"""Runner for T58: Gap-Phantom Equivalence Audit."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.gap_phantom_equivalence import run_t58_audit, t58_result_to_dict


def _pairs(pairs) -> list[tuple[str, str]]:
    return sorted(tuple(p) for p in pairs)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t58_audit()
    data = t58_result_to_dict(result)

    out_path = Path("results") / "gap-phantom-equivalence-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("=== T58: Gap-Phantom Equivalence Audit ===")
    print()

    print("--- Observer Gap Audits ---")
    for audit in result.observer_audits:
        print(f"  [{audit.source_test}] {audit.observer}: {audit.classification}")
        print(f"    A(U):      {_pairs(audit.ambient_pairs)}")
        print(f"    F(U):      {_pairs(audit.apparent_pairs)}")
        print(f"    G(U):      {_pairs(audit.gap_pairs)}")
        print(f"    phantoms:  {_pairs(audit.phantom_pairs)}")
        print(f"    suborder:  {audit.local_is_suborder}")
    print()

    print("--- Hostile Control ---")
    control = result.control_audit
    print(f"  {control.observer}: {control.classification}")
    print(f"    A(U):           {_pairs(control.ambient_pairs)}")
    print(f"    F(U):           {_pairs(control.apparent_pairs)}")
    print(f"    G(U):           {_pairs(control.gap_pairs)}")
    print(f"    phantoms:       {_pairs(control.phantom_pairs)}")
    print(f"    spurious local: {_pairs(control.spurious_apparent_pairs)}")
    print()

    print("--- Hypothesis Verdicts ---")
    for h in result.hypothesis_evaluations:
        print(f"  {h.hypothesis_id} [{h.status}]")
        print(f"    {h.claim}")
        print(f"    evidence: {h.evidence}")
    print()

    print(f"Best supported: {result.best_supported}")
    print()
    print(result.finding)
    print()
    print(f"Boundary: {result.boundary}")
    print()
    print(f"Results written to {out_path}")


if __name__ == "__main__":
    main()
