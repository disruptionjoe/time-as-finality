"""Runner for T38: minimal multiscale transport formalization."""

import json
import sys
from pathlib import Path

from models.minimal_multiscale_transport import run_t38_analysis, t38_result_to_dict


def main() -> None:
    result = run_t38_analysis()
    data = t38_result_to_dict(result)

    out_path = Path("results") / "minimal-multiscale-transport-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2))

    cr = result.compression_record
    er = result.emergence_record
    ls = result.level_skip_test
    sc = result.simultaneous_channels_analysis

    print("T38: Minimal Multiscale Transport Formalization")
    print()
    print("  Compression scenario:")
    print(f"    {cr.source_site_count} sites -> {cr.target_site_count} sites "
          f"(ratio {cr.compression_ratio})")
    print(f"    PO1 admissible:    {cr.po1_admissible}")
    print(f"    Retained:          {cr.retained_invariants}")
    print(f"    Lost detail:       {cr.lost_detail}")
    print()
    print("  Emergence scenario:")
    print(f"    Source patches:    {er.source_patch_count}")
    print(f"    Target patches:    {er.target_patch_count}")
    print(f"    Genuine emergence: {er.is_genuine_emergence}")
    print(f"    Source global sec: {er.source_has_global_section}")
    print(f"    Target global sec: {er.target_has_global_section}")
    print()
    print("  Level-skip test:")
    print(f"    Stepwise PO1:      {ls.stepwise_po1}")
    print(f"    Direct PO1:        {ls.direct_po1}")
    print(f"    Verdict equiv:     {ls.verdict_equivalent}")
    print(f"    Information equiv: {ls.information_equivalent}")
    print()
    print("  Simultaneous channels (T37 diamond):")
    print(f"    Path-dependent:    {sc.path_dependent}")
    print(f"    Verdict:           {sc.verdict}")
    print()
    print("  Hypothesis verdicts:")
    for h in result.hypothesis_evaluations:
        cov = int(h.coverage.coverage_fraction * 10)
        print(f"    {h.hypothesis_id}: {h.verdict:40s}  ({cov}/10 questions)")
    print()
    print(f"  Best supported:    {result.best_supported_hypothesis}")
    print(f"  New objects:       {result.new_objects_required}")
    print(f"  H2 required:       {result.h2_required}")
    print(f"  H3 required:       {result.h3_required}")
    print()
    print(f"  Results written to {out_path}")


if __name__ == "__main__":
    main()
    sys.exit(0)
