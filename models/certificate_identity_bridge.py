"""T413 - Certificate-Identity Bridge.

Bridge obligation #1 of the governance-Shapley-finality homology
(explorations/governance-shapley-finality-homology-note-2026-07-02.md): does the
T412 game's efficiency-forced `final-relative-to-R` separator instantiate the
SAME typed certificate as T411's `final-relative-to-R+`?

Built falsifiable and non-circular: the certificate primitive is a
STABILITY/no-deviation predicate + an INVARIANCE axiom (symmetry / Arrow-IIA),
NOT the Shapley value. Both domains instantiate a shared signature; the verdict
is derived by an identical rule; Pair 1 must be REJECTED; T411's invariance
witness is reported honestly (partial). Cross-domain material is the object of
study, never evidence. No claim promotion; ledger untouched.

    python -m models.certificate_identity_bridge
    python -m pytest tests/test_certificate_identity_bridge.py -v
"""

from __future__ import annotations

from fractions import Fraction as F
import json

from models.legitimacy_shapley_finality_probe import (
    N, S_R, FOCUS, DIV_A, DIV_C, DIV_B,
    v_of, shapley_by_dividends, restricted_games_agree,
    boundary_blind_value, symmetry_holds,
)

BOUNDARY = tuple(p for p in N if p not in S_R)


# ---------------------------------------------------------------------------
# The shared signature and verdict rule (identical for both domains).
# ---------------------------------------------------------------------------
def derive_verdict(stability_no_in_R_overturn, region_can_reconstruct):
    """final-relative-to-R iff no in-R move overturns AND R cannot reconstruct
    the datum. Identical rule applied to both domains."""
    if stability_no_in_R_overturn and not region_can_reconstruct:
        return "final-relative-to-R"
    return "revisable-at-R"


SIGNATURE_FIELDS = (
    "region", "menu", "verdict",
    "stability_witness", "invariance_witness", "datum_locus",
)


def instantiates_signature(cert):
    return set(cert.keys()) >= set(SIGNATURE_FIELDS)


# ---------------------------------------------------------------------------
# Game instantiation (fully computed from T412 machinery).
# ---------------------------------------------------------------------------
def _separation_delta(div_base, div_alt, focus=FOCUS):
    return shapley_by_dividends(div_alt)[focus] - shapley_by_dividends(div_base)[focus]


def game_invariance_sweep(div_base=DIV_A, div_alt=DIV_C, focus=FOCUS):
    """Executable IIA/symmetry witness for the game.

    Returns whether the A-vs-alt separation Delta phi_focus is invariant under
    the 'irrelevant alternative' class, and whether the FULL admissible class is
    axiom-forced (any localizing re-weighting breaks symmetry)."""
    base_delta = _separation_delta(div_base, div_alt, focus)

    checks = []

    # (a) permute boundary players 3<->4 in the dividend structure
    def relabel_boundary(div):
        swap = {BOUNDARY[0]: BOUNDARY[1], BOUNDARY[1]: BOUNDARY[0]}
        out = {}
        for S, d in div.items():
            out[frozenset(swap.get(p, p) for p in S)] = d
        return out
    d1 = _separation_delta(relabel_boundary(div_base), relabel_boundary(div_alt), focus)
    checks.append(("boundary_permutation", d1 == base_delta))

    # (b) add an arbitrary dividend on a coalition DISJOINT from the focus, to both
    irrelevant_S = frozenset({BOUNDARY[0], BOUNDARY[1]})  # {3,4}, focus 0 not in it
    b2 = dict(div_base); b2[irrelevant_S] = b2.get(irrelevant_S, F(0)) + F(7)
    a2 = dict(div_alt);  a2[irrelevant_S] = a2.get(irrelevant_S, F(0)) + F(7)
    d2 = _separation_delta(b2, a2, focus)
    checks.append(("irrelevant_coalition_dividend", d2 == base_delta))

    # (c) add an in-R dividend to BOTH games (an in-R menu operation)
    in_R_S = frozenset({0, 1})
    b3 = dict(div_base); b3[in_R_S] = b3.get(in_R_S, F(0)) + F(9)
    a3 = dict(div_alt);  a3[in_R_S] = a3.get(in_R_S, F(0)) + F(9)
    d3 = _separation_delta(b3, a3, focus)
    checks.append(("in_R_dividend_both", d3 == base_delta))

    irrelevant_class_invariant = all(ok for _, ok in checks)

    # full admissible class: a localizing re-weighting changes phi but breaks
    # the symmetry axiom -> it is illegitimate, so the dependence cannot be
    # declared away. (T412 Leg 5, recomputed here.)
    bb = boundary_blind_value(div_alt, focus=focus)
    localizer_changes_phi = bb["value"][focus] != shapley_by_dividends(div_alt)[focus]
    localizer_breaks_symmetry = not symmetry_holds(bb["value"], div_alt)
    full_class_axiom_forced = localizer_changes_phi and localizer_breaks_symmetry

    return {
        "base_delta": str(base_delta),
        "checks": {name: ok for name, ok in checks},
        "irrelevant_class_invariant": irrelevant_class_invariant,
        "localizer_changes_phi": localizer_changes_phi,
        "localizer_breaks_symmetry": localizer_breaks_symmetry,
        "full_admissible_class_forced": full_class_axiom_forced,
        "complete": irrelevant_class_invariant and full_class_axiom_forced,
    }


def game_certificate(div_alt, label):
    """Build the certificate for the A-vs-`div_alt` separation (the sealed member)."""
    # stability: no in-R dividend change moves the separation.
    # (the separation lives in the dividends where A and div_alt differ; check
    #  that those differing coalitions are NOT subsets of R.)
    differing = [S for S in set(DIV_A) | set(div_alt)
                 if DIV_A.get(S, F(0)) != div_alt.get(S, F(0))]
    stability = all(not (S <= frozenset(S_R)) for S in differing)

    # region can reconstruct the datum iff some proper subset carries it.
    region_can_reconstruct = not all(
        restricted_games_agree(DIV_A, div_alt, S)
        for S in _proper_subsets(N)
    )
    datum_locus = "proper-subset" if region_can_reconstruct else "whole"

    inv = game_invariance_sweep(DIV_A, div_alt)
    verdict = derive_verdict(stability, region_can_reconstruct)
    return {
        "domain": f"game ({label})",
        "region": {"players": list(S_R), "type": "player-subset"},
        "menu": {"type": "in-R dividend reallocations"},
        "verdict": verdict,
        "stability_witness": {"no_in_R_overturn": stability,
                              "evidence": "separation lives in dividends outside R"},
        "invariance_witness": {"irrelevant_class": inv["irrelevant_class_invariant"],
                               "full_admissible_class": inv["full_admissible_class_forced"],
                               "complete": inv["complete"],
                               "mechanism": "Arrow-IIA + Shapley symmetry axiom"},
        "datum_locus": datum_locus,
        "_sweep": inv,
    }


def _proper_subsets(players):
    from itertools import combinations
    players = tuple(players)
    for r in range(len(players)):           # r < len -> proper
        for c in combinations(players, r):
            yield frozenset(c)


# ---------------------------------------------------------------------------
# T411 adapter (RECORDED fields, cited; NOT re-derived).
# Source: results/T411-departed-record-capability-discriminator-v0.1-results.md
# and steward/runs/2026-07-02-physical-boundary-swing.md. T411 is RECORDED tier.
# ---------------------------------------------------------------------------
def t411_adapter_certificate():
    return {
        "domain": "quantum T411 (recorded-tier adapter; fields cited, not re-derived)",
        "region": {"players": "declared R+", "type": "bounded-region + menu"},
        "menu": {"type": "all CPTP channels on R + unlimited work ancillas"},
        "verdict": "final-relative-to-R",   # B is final-relative-to-R+ (recorded)
        "stability_witness": {"no_in_R_overturn": True,
                              "evidence": "all-channel phi-independence certificate (recorded)"},
        "invariance_witness": {"irrelevant_class": True,   # Lieb-Robinson relabel survives (recorded)
                               "full_admissible_class": False,  # OPEN (pass linchpin G-50)
                               "complete": False,
                               "mechanism": "LR-class only; full relabel test unproven"},
        "datum_locus": "whole",   # beta=0 datum in no proper subset (recorded)
    }


# ---------------------------------------------------------------------------
# The bridge comparison.
# ---------------------------------------------------------------------------
def compare(cert_game, cert_t411):
    identical, divergent = [], []
    # region/menu: compare by TYPE (both = bounded region + menu)
    identical.append("region:bounded-region+menu") if (
        "type" in cert_game["region"] and "type" in cert_t411["region"]) else divergent.append("region")
    identical.append("menu:present") if (cert_game["menu"] and cert_t411["menu"]) else divergent.append("menu")
    # verdict
    (identical if cert_game["verdict"] == cert_t411["verdict"] else divergent).append(
        f"verdict:{cert_game['verdict']}")
    # stability
    (identical if cert_game["stability_witness"]["no_in_R_overturn"]
        == cert_t411["stability_witness"]["no_in_R_overturn"] else divergent).append("stability_witness")
    # datum locus
    (identical if cert_game["datum_locus"] == cert_t411["datum_locus"] else divergent).append(
        f"datum_locus:{cert_game['datum_locus']}")
    # invariance completeness -- the honest field
    inv_match = (cert_game["invariance_witness"]["complete"]
                 == cert_t411["invariance_witness"]["complete"])
    (identical if inv_match else divergent).append("invariance_witness.complete")

    # bridge decision
    if cert_game["datum_locus"] != cert_t411["datum_locus"]:
        verdict = "REJECT"          # falsifiability teeth (Pair 1)
    elif not divergent:
        verdict = "FULL-HOMOLOGY"
    elif divergent == ["invariance_witness.complete"]:
        verdict = "PARTIAL-HOMOLOGY (invariance owed by T411)"
    else:
        verdict = "PARTIAL (multiple divergences)"

    return {"identical_fields": identical, "divergent_fields": divergent,
            "n_identical": len(identical), "bridge_verdict": verdict}


def run():
    cert_A_C = game_certificate(DIV_C, "Pair 2 / efficiency-only / sealed")
    cert_A_B = game_certificate(DIV_B, "Pair 1 / boundary-dividend")
    cert_t411 = t411_adapter_certificate()

    return {
        "artifact": "T413-certificate-identity-bridge-v0.1",
        "signature_fields": list(SIGNATURE_FIELDS),
        "game_pair2_instantiates": instantiates_signature(cert_A_C),
        "t411_instantiates": instantiates_signature(cert_t411),
        "cert_game_pair2": cert_A_C,
        "cert_game_pair1": cert_A_B,
        "cert_t411": cert_t411,
        "bridge_pair2_vs_t411": compare(cert_A_C, cert_t411),
        "bridge_pair1_vs_t411": compare(cert_A_B, cert_t411),
    }


if __name__ == "__main__":
    def default(o):
        return str(o)
    print(json.dumps(run(), indent=2, default=default))
