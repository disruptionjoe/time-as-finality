"""Observerse protocol-stack ablation -- does each layer earn its slot? (compositionality/illustration grade)

Predeclared: full stack sustains coherent structure; removing each layer collapses it in ITS mode.
Layers (persona-sourced 4-core + governance 5th): issuance, admissibility, sybil_finality, consensus,
governance. Metric: SCS = sustained coherent structure = mean of the last third of N(t), where N(t) is
per-tick admitted novelty x coherence x shared-fraction. Deterministic accounting model of N-C-K.

HONEST GRADE: illustration/compositionality, NOT validation. Each layer's removal is mechanized to cause
its collapse, so it collapses -- the value is (a) making each layer's failure mode precise and (b) the
governance minimality crux: governance is load-bearing IFF issued novelty over the horizon exceeds what
fixed initial rules anticipate (the personas' undecidability argument). Reported under BOTH rule-sizings
so the crux is visible, not rigged. Run: python -m models.observerse_stack_ablation
"""
from __future__ import annotations

K, T, BETA0, TAU = 5, 150, 1.0, 40.0


def _R0(fill_ticks: float) -> float:
    return sum(K * BETA0 / (1 + t / TAU) for t in range(1, int(fill_ticks) + 1))


def run(issuance=True, admissibility=True, sybil=True, consensus=True, governance=True,
        rule_fill=TAU) -> float:
    U = 0.0
    R = _R0(rule_fill)          # initial admissible-rule capacity (what fixed rules anticipate)
    contra = 0.0
    cohere = 1.0
    N = []
    for t in range(1, T + 1):
        beta_t = BETA0 / (1 + t / TAU)
        raw = K * beta_t if issuance else 0.0
        if not admissibility:
            contra = min(1.0, contra + 0.02)     # contradictions accumulate -> incoherence
        admitted = raw * max(0.0, 1.0 - contra)
        if governance:
            R = max(R, U + admitted)             # rules follow novelty (anti-ossification)
        over = max(0.0, (U + admitted) - R)      # novelty beyond fixed rules is rejected
        admitted = max(0.0, admitted - over)
        U += admitted
        if not sybil:
            cohere = max(0.0, cohere - 0.015)     # fake-observer capture erodes coherence
        share = 1.0 if consensus else 1.0 / K     # consensus-off -> shared structure fragments to 1/K
        N.append(admitted * cohere * share)
    third = T // 3
    return sum(N[-third:]) / third


def main() -> None:
    full = run()
    rows = [
        ("FULL STACK (all 5)", full, "-- baseline"),
        ("- issuance", run(issuance=False), "FREEZE (finite game / chain)"),
        ("- admissibility", run(admissibility=False), "INCOHERENCE (contradictions)"),
        ("- sybil/finality", run(sybil=False), "CAPTURE (fake observers)"),
        ("- consensus", run(consensus=False), "FRAGMENT (K disjoint realities)"),
        ("- governance (near-term rules)", run(governance=False, rule_fill=TAU), "OSSIFICATION"),
        ("- governance (full-horizon rules)", run(governance=False, rule_fill=T), "no collapse (rules anticipated all)"),
    ]
    print("[observerse stack ablation] SCS = sustained coherent structure (higher = infinite game)\n")
    print(f"  {'configuration':<34} {'SCS':>7}   predicted mode")
    for name, scs, mode in rows:
        drop = "" if name.startswith("FULL") else f"  ({scs/full*100:4.0f}% of full)"
        print(f"  {name:<34} {scs:>7.3f}{drop}   {mode}")

    gov_near = rows[5][1]
    gov_full = rows[6][1]
    print("\n[verdict]")
    print(f"  * The 4 core layers each EARN their slot: removing issuance/admissibility/sybil/consensus")
    print(f"    each drops SCS to <=20% of full (freeze / incoherence / capture / fragment).")
    print(f"  * GOVERNANCE minimality crux: with near-term rules it OSSIFIES (SCS {gov_near:.3f}, "
          f"{gov_near/full*100:.0f}% of full);")
    print(f"    with rules that anticipate the FULL horizon it does not collapse (SCS {gov_full:.3f}).")
    print(f"    So governance is load-bearing IFF issued novelty exceeds what fixed rules anticipate --")
    print(f"    which is exactly the personas' undecidability argument (admissible extensions cannot be")
    print(f"    precomputed). Under that argument the minimum is 5, not 4.")
    print(f"  * Grade: illustration/compositionality -- each removal was mechanized to cause its mode;")
    print(f"    the content is the precise failure map + the governance conditional, not that reality is this.")


if __name__ == "__main__":
    main()
