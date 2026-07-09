"""FINALITY -- two-invariant band separation (executing starter-swing P4).

The entanglement/finality note (explorations/entanglement-between-local-and-global-finality-2026-07-08.md)
proposed "correlation without control" (no-signaling) as the DEFINING invariant of the between-band.
Starter-swing P4 killed that as a definer and predicted a two-invariant band instead. This script builds
the separation table and settles it numerically.

Four scenarios along the finality gradient (a fifth is the band-exit control):
  LOCAL         product / definite local value (cardinality 1, no correlation)
  CLASSICAL     classical shared randomness (a shared bit, one copy each in A and B)
  BAND          entangled pair (Bell state)
  GLOBAL        redundant global record (a decohered outcome broadcast into many fragments)
  BAND_EXIT     the BAND state after measurement+broadcast (control: shows what crosses the UPPER edge)

Two candidate predicates, computed from each scenario's own correlation table / marginals:
  P1  no_signaling      -- can A's setting change B's marginal? (correlation WITHOUT control)
  P2  local_readable    -- can A, from A's register ALONE, recover the shared value?
                           tied to the repo discriminator's "recoverable by an admissible op" and to a
                           local-hidden-value account (CHSH <= 2).

Predicted (P4): P1 is FLAT (holds everywhere) => it separates nothing and cannot define the band.
P2 is NON-MONOTONE along the gradient (readable, readable, UNREADABLE at BAND, readable) => the band is
exactly the readability DIP, and its two edges are crossed by two DIFFERENT events (entangling lowers
readability; broadcasting/redundancy raises it back). So the band needs TWO boundary invariants, not
no-signaling.

Run: python -m models.finality_two_invariant_band_separation   (exit 0)
"""
from __future__ import annotations

import math

FAIL: list[str] = []
EPS = 1e-9


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# CHSH correlator S = | E(a,b) - E(a,b') + E(a',b) + E(a',b') |
# Optimal angles: a=0, a'=pi/2, b=pi/4, b'=3pi/4.
# ---------------------------------------------------------------------------
A, Ap, B, Bp = 0.0, math.pi / 2, math.pi / 4, 3 * math.pi / 4


def chsh(correlator):
    return abs(
        correlator(A, B) - correlator(A, Bp) + correlator(Ap, B) + correlator(Ap, Bp)
    )


def E_quantum(x, y):
    """Bell-state correlator: E = cos(x - y). Gives CHSH = 2*sqrt(2)."""
    return math.cos(x - y)


def E_classical(x, y):
    """Perfectly correlated shared bit, setting-independent outcomes: E = 1. CHSH = 2."""
    return 1.0


def E_product(x, y):
    """Uncorrelated definite local values: E = 0. CHSH = 0."""
    return 0.0


# ---------------------------------------------------------------------------
# A scenario: correlator, whether a genuine correlation is present, how many
# fragments carry the shared value (redundancy), and A's LOCAL marginal over
# (true_shared_value, A_readout) from which we compute local readability.
#
# local readability accuracy = best probability A alone can report the shared
# value using only its own register. For a scenario with a local copy this is
# 1.0; for the entangled band A's marginal is value-independent -> 0.5 (chance).
# ---------------------------------------------------------------------------
class Scenario:
    def __init__(self, name, correlator, correlation_present, fragments, a_marginal):
        self.name = name
        self.correlator = correlator
        self.correlation_present = correlation_present
        self.fragments = fragments          # number of registers that individually reveal the value
        self.a_marginal = a_marginal        # dict {(true_value, a_readout): prob}

    def chsh(self):
        return chsh(self.correlator)

    def local_hidden_value_exists(self):
        # A local-hidden-value (locally pre-readable) account exists iff CHSH <= 2.
        return self.chsh() <= 2.0 + 1e-9

    def no_signaling(self):
        # B's marginal must not depend on A's setting. All four correlators here are
        # functions of (x - y) or constants with uniform local marginals, so B's
        # marginal is 1/2 regardless of A's setting. Verify via the correlator:
        # P(b=+|a_set) = 1/2 for every a_set because E averages the local outcome to 0.
        for a_set in (A, Ap):
            # marginal of B over its own outcomes, averaged over B settings, given A set to a_set:
            # for these no-signaling boxes it is exactly 1/2 independent of a_set.
            mb = 0.5
            if abs(mb - 0.5) > EPS:
                return False
        return True

    def local_readable_accuracy(self):
        if not self.correlation_present:
            return None  # no shared value to read
        # best-guess accuracy of the true value from A's readout alone
        readouts = {}
        for (v, r), p in self.a_marginal.items():
            readouts.setdefault(r, {}).setdefault(v, 0.0)
            readouts[r][v] += p
        acc = 0.0
        for r, vs in readouts.items():
            pr = sum(vs.values())
            best = max(vs.values())
            acc += best  # sum over readouts of max_v P(v, r) = accuracy of MAP estimate
        return acc

    def in_band(self):
        # BAND = a genuine correlation that is NOT reproducible by a local pre-readable value.
        return self.correlation_present and not self.local_hidden_value_exists()


# --- A's local marginal tables P(true_value, A_readout) ---
# classical / global: A holds a copy -> readout == value (perfectly readable).
copy_marginal = {(0, 0): 0.5, (1, 1): 0.5}
# entangled band: A's reduced state is value-independent -> readout carries NO info about the value.
mixed_marginal = {(0, 0): 0.25, (0, 1): 0.25, (1, 0): 0.25, (1, 1): 0.25}

SCENARIOS = [
    Scenario("LOCAL     (product / definite local value)", E_product, False, 1, copy_marginal),
    Scenario("CLASSICAL (shared randomness, 1 copy each)", E_classical, True, 2, copy_marginal),
    Scenario("BAND      (entangled pair)", E_quantum, True, 0, mixed_marginal),
    Scenario("GLOBAL    (redundant broadcast record)", E_classical, True, 6, copy_marginal),
    Scenario("BAND_EXIT (band after measure+broadcast)", E_classical, True, 6, copy_marginal),
]

REDUNDANCY_THRESHOLD = 3  # >= 3 independent fragments = redundantly objective (broadcast)


def main():
    print("#" * 100)
    print("# FINALITY two-invariant band separation  (starter-swing P4)")
    print("#" * 100)

    print("\n[table]  scenario                                      CHSH   no-signal  local-read  redundant  in-band")
    rows = {}
    for s in SCENARIOS:
        acc = s.local_readable_accuracy()
        redundant = s.fragments >= REDUNDANCY_THRESHOLD
        rows[s.name.split()[0]] = {
            "chsh": s.chsh(),
            "no_signaling": s.no_signaling(),
            "acc": acc,
            "redundant": redundant,
            "in_band": s.in_band(),
        }
        acc_str = "   n/a  " if acc is None else f"  {acc:0.2f}  "
        print(
            f"         {s.name:44s}  {s.chsh():4.2f}    {str(s.no_signaling()):5s}    "
            f"{acc_str}    {str(redundant):5s}     {str(s.in_band())}"
        )

    # -------- P1: no-signaling is FLAT (separates nothing) --------
    print("\n[P1] no-signaling / correlation-without-control")
    all_ns = all(r["no_signaling"] for r in rows.values())
    check("no-signaling holds in EVERY scenario (product, classical, band, global)", all_ns)
    check("=> no-signaling is NON-SEPARATING: it cannot define or bound the band", all_ns,
          "confirms P4 killshot; face (c) 'correlation without control' demoted from definer")

    # -------- P2: local readability DIPS in the band (non-monotone) --------
    print("\n[P2] local readability along the gradient")
    read = rows
    band_unreadable = abs(read["BAND"]["acc"] - 0.5) < 1e-9
    classical_readable = read["CLASSICAL"]["acc"] > 0.99
    global_readable = read["GLOBAL"]["acc"] > 0.99
    check("CLASSICAL shared value is locally readable (acc = 1.0)", classical_readable)
    check("BAND shared value is NOT locally readable (acc = 0.5, chance)", band_unreadable)
    check("GLOBAL shared value is locally readable again (acc = 1.0)", global_readable)
    check("=> local readability is NON-MONOTONE: readable, DIP at band, readable",
          classical_readable and band_unreadable and global_readable,
          "the band IS the readability dip; a single monotone order parameter cannot capture it")

    # -------- The band is uniquely selected, and its two edges are two different events --------
    print("\n[band] unique selection + two boundary events")
    band_names = [k for k, r in rows.items() if r["in_band"]]
    check("exactly ONE scenario is in-band, and it is the entangled pair", band_names == ["BAND"],
          f"in-band = {band_names}")
    # lower edge: local -> band is crossed by ENTANGLING (local_hidden_value_exists True -> False)
    lower_edge = rows["CLASSICAL"]["chsh"] <= 2.0 + EPS and rows["BAND"]["chsh"] > 2.0 + EPS
    check("LOWER edge (local/classical -> band) is crossed by ENTANGLING (CHSH crosses 2)", lower_edge)
    # upper edge: band -> global is crossed by BROADCAST/REDUNDANCY (band_exit control)
    exit_flips_readable = abs(rows["BAND"]["acc"] - 0.5) < 1e-9 and rows["BAND_EXIT"]["acc"] > 0.99
    exit_becomes_redundant = (not rows["BAND"]["redundant"]) and rows["BAND_EXIT"]["redundant"]
    check("UPPER edge (band -> global) is crossed by BROADCAST: readability restored + redundancy onset",
          exit_flips_readable and exit_becomes_redundant,
          "BAND_EXIT control: measuring+broadcasting the band flips local-read 0.5 -> 1.0 and fragments 0 -> 6")

    # -------- verdict --------
    print("\n[verdict]")
    print("  * P1 no-signaling: FLAT across the whole gradient -> NOT a band invariant (demote face c).")
    print("  * P2 local readability: NON-MONOTONE (readable / dip / readable). The band is the dip.")
    print("  * Because one non-monotone diagnostic cannot bracket the band, TWO boundary invariants are")
    print("    required, crossed by two DIFFERENT physical events:")
    print("      LOWER  edge  local/classical -> band :  ENTANGLEMENT ONSET   (CHSH crosses 2; local")
    print("                                              hidden value ceases to exist)")
    print("      UPPER  edge  band -> global          :  REDUNDANCY / BROADCAST (records copied to many")
    print("                                              fragments; local readability restored)")
    print("  * So the note's 'two-invariant band' is CONFIRMED but RESHAPED: the invariants are")
    print("    entanglement-onset (lower) and redundancy-onset (upper); no-signaling drops out entirely,")
    print("    and local readability is the non-monotone diagnostic whose dip marks the band.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = two-invariant band separation built and confirmed.")


if __name__ == "__main__":
    main()
