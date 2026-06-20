"""Write T88 Pati-Salam typed-forgetting crosswalk results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.pati_salam_typed_forgetting_crosswalk import (
    run_t88_analysis,
    t88_result_to_dict,
)


RESULTS_JSON = Path("results/pati-salam-typed-forgetting-crosswalk-v0.1.json")
RESULTS_MD = Path("results/pati-salam-typed-forgetting-crosswalk-v0.1-results.md")


def main() -> None:
    payload = t88_result_to_dict(run_t88_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T88 Results: Pati-Salam Typed Forgetting Crosswalk",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Transport comparison",
        "",
        "| Map | Rule | LossKernel | Exact table match | n values | Verdict |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for key in ("standard_audit", "bl_only_audit"):
        audit = payload[key]
        losskernel = ", ".join(audit["losskernel"]) or "empty"
        n_values = ", ".join(str(value) for value in audit["n_values"])
        lines.append(
            "| "
            f"{audit['name']} | "
            f"`{audit['hypercharge_rule']}` | "
            f"{losskernel} | "
            f"{audit['exact_table_match']} | "
            f"{n_values} | "
            f"{audit['verdict']} |"
        )
    lines.extend(
        [
            "",
            "## Standard multiplets",
            "",
            "| SU3 | SU2_L dim | n=6Y | Dim |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for multiplet in payload["standard_audit"]["multiplets"]:
        lines.append(
            "| "
            f"{multiplet['su3']} | "
            f"{multiplet['su2_l_dim']} | "
            f"{multiplet['n']} | "
            f"{multiplet['dim']} |"
        )
    lines.extend(
        [
            "",
            "## B-L only projection multiplets",
            "",
            "| SU3 | SU2_L dim | n=6Y' | Dim |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for multiplet in payload["bl_only_audit"]["multiplets"]:
        lines.append(
            "| "
            f"{multiplet['su3']} | "
            f"{multiplet['su2_l_dim']} | "
            f"{multiplet['n']} | "
            f"{multiplet['dim']} |"
        )
    lines.extend(
        [
            "",
            "## Loss attribution",
            "",
            payload["loss_attribution"],
            "",
            "## PO1 status",
            "",
            payload["po1_status"],
            "",
            "## Falsification condition",
            "",
            payload["falsification_condition"],
            "",
            "## TaF update",
            "",
            payload["taf_update"],
            "",
            "## Next move",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
