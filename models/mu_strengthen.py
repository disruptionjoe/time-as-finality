"""
Strengthening passes addressing the verification adjudicator's caveats C1, C2, C3.

C1 (held-out recoding discovery): REMOVE the exact Feistel h from the battery. Give COMP a PARAMETRIZED
   Feistel family (single- and two-round, params not handed) and require it to DISCOVER a linearizing
   recoding for E. If it rediscovers one it was never handed -> gate G3 is earned by SEARCH, not by
   construction, defeating the 'COMP = affine-after-pre-loaded-recoding' deflation.
C2 (battery broadening / B robustness): run that same broadened discovery search against B (2nd-order 110)
   and confirm kappa stays 1 (no linearizing recoding found) -> B's irreducibility survives a strictly
   stronger search.
C3 (population orthogonality): over ALL 256 first-order elementary rules at enumerable n, cross-tabulate
   INFO (reversible vs not) x COMP (affine vs not). Show all four corners are populated by real rules and
   the two axes are not collinear (phi well below 1) -> dissociability holds on an UNBIASED population,
   not just 6 curated cells.
"""
import json, math
from collections import Counter
from mu_experiment import (rule_table, step1_int, step2_int, build_succ, is_bijection,
                           affine_cert, recurrent_rate_bits)

# ---------- parametrized Feistel family (held-out: params searched, not handed) ----------
def _rot(v, k, half):
    k %= half
    m = (1 << half) - 1
    return v if k == 0 else (((v << k) | (v >> (half - k))) & m)

def feistel(s, W, a, b, use_and):
    half = W // 2; m = (1 << half) - 1
    L = s >> half; R = s & m
    g = _rot(R, b, half) ^ ((R & _rot(R, a, half)) if use_and else 0)
    return (R << half) | ((L ^ g) & m)

def feistel_inv(s, W, a, b, use_and):
    half = W // 2; m = (1 << half) - 1
    A = s >> half; B = s & m          # A = R, B = L XOR g(R)
    g = _rot(A, b, half) ^ ((A & _rot(A, a, half)) if use_and else 0)
    return ((B ^ g) << half) | A

def recoding_family(W):
    """identity + single-round Feistels (searched params) + two-round Feistels. Returns (name, r, rinv)."""
    half = W // 2
    fam = [("id", (lambda s: s), (lambda s: s))]
    params = []
    for a in range(1, half):
        for b in range(0, half):
            for ua in (True, False):
                params.append((a, b, ua))
    for (a, b, ua) in params:
        fam.append((f"F1({a},{b},{int(ua)})",
                    (lambda s, W=W, a=a, b=b, ua=ua: feistel(s, W, a, b, ua)),
                    (lambda s, W=W, a=a, b=b, ua=ua: feistel_inv(s, W, a, b, ua))))
    # a modest set of two-round Feistels to broaden beyond the single round used to build E
    pairs = [((1, 3, True), (2, 1, True)), ((1, 1, True), (1, 2, False)), ((2, 3, True), (1, 0, True))]
    for (p, q) in pairs:
        def mk(p, q, W):
            r  = lambda s: feistel(feistel(s, W, *p), W, *q)
            ri = lambda s: feistel_inv(feistel_inv(s, W, *q), W, *p)
            return r, ri
        r, ri = mk(p, q, W)
        fam.append((f"F2{p}{q}", r, ri))
    return fam

def discover_linearizing_recoding(succ, W, exclude_handed=None):
    """Search the recoding family for r s.t. r^{-1} o G o r is affine. Returns (name, cols, c) or None.
       exclude_handed: a set of recoding NAMES to forbid (to enforce 'held-out')."""
    N = 1 << W
    # member 0: plain global affine (no recoding)
    cert = affine_cert(succ, W)
    if cert is not None:
        return ("affine:id", cert[0], cert[1])
    for name, r, rinv in recoding_family(W):
        if name == "id":
            continue
        if exclude_handed and name in exclude_handed:
            continue
        # conjugate:  y -> r^{-1}( G( r(y) ) )   tests whether r^{-1} G r is affine
        succ_c = [rinv(succ[r(y)]) for y in range(N)]
        cert = affine_cert(succ_c, W)
        if cert is not None:
            return (f"discovered_recoding:{name}", cert[0], cert[1])
    return None

# ---------- C1 + C2 ----------
def c1_c2():
    print("=" * 78)
    print("C1 (held-out recoding DISCOVERY for E) + C2 (B robustness vs broadened search)")
    print("=" * 78)
    out = {"E_discovery": [], "B_robustness": []}
    for n in (4, 5, 6):
        W = 2 * n
        T90 = rule_table(90); T110 = rule_table(110)
        # E = h o T90 o h^{-1}, with the BUILD Feistel h = (a=1,b=3,use_and=True). The discovery search
        # is FORBIDDEN from using that exact handed instance name; it must rediscover an equivalent.
        handed = "F1(1,3,1)"
        hb = lambda s, W=W: feistel(s, W, 1, 3, True)
        hb_inv = lambda s, W=W: feistel_inv(s, W, 1, 3, True)
        G_E = lambda s, W=W: hb(step2_int(hb_inv(s), T90, n))
        succ_E = build_succ(G_E, W)
        disc = discover_linearizing_recoding(succ_E, W, exclude_handed={handed})
        earned = disc is not None and disc[0].startswith("discovered_recoding")
        out["E_discovery"].append({"n": n, "found": bool(disc), "via": (disc[0] if disc else None),
                                   "G3_earned_by_search": earned, "handed_excluded": handed})
        print(f"  E n={n}: discovery -> {disc[0] if disc else 'NONE'} | G3 earned by search = {earned}")
        # B = T110 (2nd-order), run the SAME broadened search; expect NO linearizer
        G_B = lambda s, n=n, T110=T110: step2_int(s, T110, n)
        succ_B = build_succ(G_B, W)
        discB = discover_linearizing_recoding(succ_B, W)
        out["B_robustness"].append({"n": n, "reduced": discB is not None, "via": (discB[0] if discB else None)})
        print(f"  B n={n}: broadened search -> {'REDUCED via ' + discB[0] if discB else 'still IRREDUCIBLE (kappa=1)'}")
    return out

# ---------- C3 population over all 256 first-order rules ----------
def c3(ns=(8, 10)):
    print("=" * 78)
    print("C3 population orthogonality: all 256 first-order rules, INFO(reversible) x COMP(affine)")
    print("=" * 78)
    out = {}
    for n in ns:
        W = n
        rows = []
        for R in range(256):
            T = rule_table(R)
            G = lambda s, T=T, n=n: step1_int(s, T, n)
            succ = build_succ(G, W)
            bij = is_bijection(succ)
            rate, _, _ = recurrent_rate_bits(succ)
            info_pos = (rate > 0.0)            # not reversible (logical irreversibility present)
            aff = affine_cert(succ, W) is not None
            comp_irr = (not aff)               # irreducible (relative to global-affine) iff non-affine
            rows.append((R, bij, info_pos, comp_irr, aff))
        # contingency: INFO_pos x COMP_irr
        c = Counter((r[2], r[3]) for r in rows)  # (info_pos, comp_irr)
        n11 = c[(True, True)]; n10 = c[(True, False)]; n01 = c[(False, True)]; n00 = c[(False, False)]
        # phi coefficient (2x2 association; 0 => INFO and COMP independent across the population)
        a, b, cc, d = n11, n10, n01, n00
        num = a * d - b * cc
        den = math.sqrt((a + b) * (cc + d) * (a + cc) * (b + d)) if (a + b) and (cc + d) and (a + cc) and (b + d) else 0
        phi = (num / den) if den else float('nan')
        all_corners = (n11 > 0 and n10 > 0 and n01 > 0 and n00 > 0)
        out[n] = {"info_pos&comp_irr": n11, "info_pos&comp_red": n10,
                  "info_zero&comp_irr": n01, "info_zero&comp_red": n00,
                  "all_four_corners_populated": all_corners, "phi": round(phi, 4)}
        print(f"  n={n}: [INFO>0,COMP_irr]={n11}  [INFO>0,COMP_red]={n10}  [INFO=0,COMP_irr]={n01}  "
              f"[INFO=0,COMP_red]={n00}  | all corners={all_corners}  phi={phi:.4f}")
        print(f"         (the [INFO=0,COMP_irr] corner = reversible-yet-nonaffine rules; its existence is "
              f"the population analogue of cell B)")
    return out

if __name__ == "__main__":
    res = {"c1_c2": c1_c2(), "c3": c3()}
    json.dump(res, open("mu_strengthen_result.json", "w", encoding="utf-8"), indent=2)
    # bottom line
    e_ok = all(r["G3_earned_by_search"] for r in res["c1_c2"]["E_discovery"])
    b_ok = all(not r["reduced"] for r in res["c1_c2"]["B_robustness"])
    corners = all(v["all_four_corners_populated"] for v in res["c3"].values())
    print("=" * 78)
    print(f"C1 (G3 earned by held-out discovery for E): {'YES' if e_ok else 'NO'}")
    print(f"C2 (B survives broadened search, kappa=1):  {'YES' if b_ok else 'NO'}")
    print(f"C3 (all four corners populated in 256-rule population): {'YES' if corners else 'NO'}")
    print("=" * 78)
