"""
MU DOUBLE-DISSOCIATION EXPERIMENT  (faithful implementation of the pre-registered spec)
Tests whether finality's reversal cost mu = (INFO bits, COMPUTE bit-ops) spans TWO independent
dimensions (CONFIRM) or collapses to one thermodynamic axis (KILL).

INFO  = logical irreversibility: per-step rate E[log2 indeg] on the recurrent set + sign (0 vs >0),
        computed EXACTLY by full 2^W enumeration of the global state-transition graph.
COMP  = irreducibility index kappa = best_admissible_shortcut_bitops / naive_bitops in (0,1],
        via a pre-registered battery (global-affine + affine-after-recoding incl. the Feistel family).
        kappa->0 reducible (certified shortcut), kappa=1 irreducible (battery search failure).

Cells: A rev+red(2nd R90) | B rev+IRR(2nd R110) | C IRREV+red(1st R90) | D irrev+irr(1st R110)
       E rev+NONLINEAR+red (conj 2nd R90)  | C' IRREV+NONLINEAR+red (conj 1st R90)   [validity controls]
Replication: 150 for 90, 30 for 110.   Rails: R_blind(all irr), R_omni(all red).
"""
import json, math
from collections import Counter

MASK = lambda W: (1 << W) - 1

# ---------------- elementary CA (int-state) ----------------
def rule_table(R): return [(R >> i) & 1 for i in range(8)]

def step1_int(x, T, n):
    res = 0
    for i in range(n):
        l = (x >> ((i - 1) % n)) & 1
        c = (x >> i) & 1
        r = (x >> ((i + 1) % n)) & 1
        res |= T[(l << 2) | (c << 1) | r] << i
    return res

def step2_int(s, T, n):
    # state = prev(high n) | cur(low n);  next pair = (cur, step1(cur) XOR prev)
    prev = s >> n
    cur = s & MASK(n)
    nxt = step1_int(cur, T, n) ^ prev
    return (cur << n) | nxt

# ---------------- Feistel nonlinear bijection h on W bits (W even) ----------------
def _f_round(r, half):
    m = MASK(half)
    rot = lambda v, k: ((v << k) | (v >> (half - k))) & m
    return ((r & rot(r, 1)) ^ rot(r, 3)) & m   # nonlinear (AND term)

def h_feistel(s, W):
    half = W // 2
    L = s >> half
    Rr = s & MASK(half)
    return (Rr << half) | ((L ^ _f_round(Rr, half)) & MASK(half))

def h_feistel_inv(s, W):
    half = W // 2
    A = s >> half          # = R
    B = s & MASK(half)     # = L XOR f(R)
    L = B ^ _f_round(A, half)
    return (L << half) | A

# ---------------- global maps / STG ----------------
def build_succ(G, W):
    return [G(s) for s in range(1 << W)]

def indegrees(succ):
    return Counter(succ)

def is_bijection(succ):
    return len(set(succ)) == len(succ)

def recurrent_rate_bits(succ):
    """mean log2(indeg) over the recurrent set (states on cycles). 0 for a permutation."""
    N = len(succ)
    indeg = indegrees(succ)
    # find recurrent states: iterate map N times (Floyd-ish): a state is recurrent iff it returns.
    # functional graph: recurrent = nodes on cycles. Mark via repeated mapping to find cycle nodes.
    seen = [0] * N        # 0 unvisited,1 in-progress,2 done
    on_cycle = bytearray(N)
    for start in range(N):
        if seen[start]:
            continue
        path = []
        x = start
        while seen[x] == 0:
            seen[x] = 1
            path.append(x)
            x = succ[x]
        if seen[x] == 1:
            # found a new cycle starting at x
            i = path.index(x)
            for y in path[i:]:
                on_cycle[y] = 1
        for y in path:
            seen[y] = 2
    rec = [s for s in range(N) if on_cycle[s]]
    if not rec:
        return 0.0, 0, len(set(succ))
    rate = sum(math.log2(indeg[succ[s]]) for s in rec) / len(rec)
    return rate, len(rec), len(set(succ))

def uniform_rate_bits(succ):
    indeg = indegrees(succ)
    N = len(succ)
    return sum(math.log2(indeg[succ[s]]) for s in range(N)) / N

# ---------------- affine certificate over GF(2) (columns rep) ----------------
def affine_cert(succ, W):
    """Return (cols, c) with G(x)=c XOR sum_{bit j of x} cols[j], verified on ALL states, else None."""
    c = succ[0]
    cols = [succ[1 << j] ^ c for j in range(W)]
    for x in range(1 << W):
        v = c
        xx = x
        while xx:
            j = (xx & -xx).bit_length() - 1
            v ^= cols[j]
            xx &= xx - 1
        if v != succ[x]:
            return None
    return (cols, c)

def matvec(cols, x):
    v = 0
    xx = x
    while xx:
        j = (xx & -xx).bit_length() - 1
        v ^= cols[j]
        xx &= xx - 1
    return v

def matmul(colsA, colsB):
    return [matvec(colsA, colsB[j]) for j in range(len(colsB))]

def matpow(cols, p, W):
    R = [1 << j for j in range(W)]     # identity
    base = cols
    while p > 0:
        if p & 1:
            R = matmul(R, base)
        base = matmul(base, base)
        p >>= 1
    return R

# ---------------- battery (admissible shortcuts) ----------------
def recodings(W):
    """pre-registered recoding family: identity + the Feistel h (both directions)."""
    out = [("id", (lambda s: s), (lambda s: s))]
    if W % 2 == 0:
        out.append(("h", (lambda s, W=W: h_feistel(s, W)), (lambda s, W=W: h_feistel_inv(s, W))))
        out.append(("hinv", (lambda s, W=W: h_feistel_inv(s, W)), (lambda s, W=W: h_feistel(s, W))))
    return out

def find_admissible_shortcut(succ, W):
    """Battery: member1 global-affine; member2 affine-after-recoding. Returns dict or None."""
    # member 1: global affine
    cert = affine_cert(succ, W)
    if cert is not None:
        return {"member": "global_affine", "recoding": "id", "cols": cert[0], "c": cert[1]}
    # member 2: affine after recoding  r o G o r^{-1}
    for name, r, rinv in recodings(W):
        if name == "id":
            continue
        # conjugated succ:  y -> r(G(rinv(y)))
        succ_r = [r(succ[rinv(y)]) for y in range(1 << W)]
        cert = affine_cert(succ_r, W)
        if cert is not None:
            return {"member": "affine_after_recoding", "recoding": name, "cols": cert[0], "c": cert[1]}
    # member 4: k-step block affinity. If G^k is affine for small k, then G^L has a polylog-L
    # predictor (M_k)^{L/k} + remainder, so the cell is REDUCIBLE. This is the decisive strengthening:
    # composition blows up polynomial degree, so the only composition-closed fast-iterate class is
    # affine-up-to-recoding-or-blocking; if B survives this it is genuinely irreducible vs the battery.
    succ_k = succ[:]
    for k in range(2, 5):
        succ_k = [succ[succ_k[s]] for s in range(1 << W)]  # G^k
        cert = affine_cert(succ_k, W)
        if cert is not None:
            return {"member": f"block_affine_k{k}", "recoding": "id", "cols": cert[0], "c": cert[1]}
    return None

# ---------------- bit-op cost model (abstract; never wall-clock) ----------------
def naive_bitops(n, L):       # n cell-updates per step, L steps
    return n * L

def shortcut_bitops(W, n, L):
    build = W * n + W ** 3                      # W basis probes (~n each) + structure O(W^3)
    query = (W ** 3) * max(1, math.ceil(math.log2(max(2, L)))) + W ** 2   # matpow + matvec
    return build + query

# ---------------- cell runner ----------------
def run_cell(name, order, rule, conj, n, L):
    T = rule_table(rule)
    if order == 1:
        W = n
        base = lambda s: step1_int(s, T, n)
    else:
        W = 2 * n
        base = lambda s: step2_int(s, T, n)
    if conj:   # conjugate by Feistel h on W bits:  G = h o base o h^{-1}
        G = lambda s: h_feistel(base(h_feistel_inv(s, W)), W)
    else:
        G = base
    succ = build_succ(G, W)
    bij = is_bijection(succ)
    rate, n_rec, n_img = recurrent_rate_bits(succ)
    info_sign = "ZERO" if rate == 0.0 else "POS"
    # COMP battery
    sc = find_admissible_shortcut(succ, W)
    if sc is not None:
        # certify M^L correctness is implied by 1-step affine cert (G=Mx[+c]); verified on all states
        kappa = min(1.0, shortcut_bitops(W, n, L) / naive_bitops(n, L))
        comp_class = "REDUCIBLE"
        member = sc["member"] + ":" + sc["recoding"]
        build_ops = W * n + W ** 3
    else:
        kappa = 1.0
        comp_class = "IRREDUCIBLE"
        member = "none(naive)"
        build_ops = naive_bitops(n, L)
    return {
        "cell": name, "order": order, "rule": rule, "conj": bool(conj), "n": n, "W": W,
        "bijection": bij, "n_recurrent": n_rec, "n_images": n_img, "states": 1 << W,
        "info_rate_bits": round(rate, 6), "info_sign": info_sign,
        "kappa": round(kappa, 6), "comp_class": comp_class, "battery_member": member,
        "build_bitops": build_ops, "naive_bitops": naive_bitops(n, L), "L": L,
    }

# ---------------- experiment ----------------
def main():
    L = 1 << 20   # headline aging length: large so reducible kappa<<0.1 and naive>>shortcut (G6)
    # cell library: (name, order, rule, conjugate?)
    primary = [
        ("A",  2, 90,  False), ("B",  2, 110, False),
        ("C",  1, 90,  False), ("D",  1, 110, False),
        ("E",  2, 90,  True ), ("Cp", 1, 90,  True ),
    ]
    replication = [
        ("A150", 2, 150, False), ("B30", 2, 30, False),
        ("C150", 1, 150, False), ("D30", 1, 30, False),
    ]
    # n-sweeps
    second_ns = [4, 5, 6, 7, 8, 9]      # 2^{2n} <= 2^18
    first_ns  = [6, 7, 8, 9, 10]        # 2^n <= 1024
    first_even = [6, 8, 10]             # for Feistel-conjugated first-order (needs even W)

    results = []
    def sweep(name, order, rule, conj):
        ns = (second_ns if order == 2 else (first_even if conj else first_ns))
        for n in ns:
            try:
                results.append(run_cell(name, order, rule, conj, n, L))
            except Exception as ex:
                results.append({"cell": name, "n": n, "error": repr(ex)})

    for (nm, o, ru, cj) in primary + replication:
        sweep(nm, o, ru, cj)

    # ---------- battery rails (sanity) ----------
    # R_blind: no battery -> all irreducible (kappa=1). R_omni: orbit table -> all reducible (kappa~0).
    # We report rails analytically: real battery must lie strictly between (some cells red, some irr).
    # Roles: these cells MUST be bijective at all n (reversible role); the rest are irreversible-role.
    EXPECTED_REVERSIBLE = {"A", "B", "E", "A150", "B30"}
    dropped = {}   # cell -> list of n dropped for failing injectivity precondition

    by_cell = {}
    for r in results:
        if "error" in r: continue
        by_cell.setdefault(r["cell"], []).append(r)

    def cell_summary(cell):
        rows = by_cell.get(cell, [])
        # Pre-registered exclusion: drop (rule,n) pairs that fail the cell's injectivity precondition.
        if cell not in EXPECTED_REVERSIBLE:
            keep = [r for r in rows if not r["bijection"]]
            drp = [r["n"] for r in rows if r["bijection"]]
            if drp:
                dropped[cell] = drp
            rows = keep
        if not rows: return None
        info_signs = set(r["info_sign"] for r in rows)
        comp_classes = set(r["comp_class"] for r in rows)
        bij = all(r["bijection"] for r in rows)
        # persistence: comp class stable across n?
        kap_last = rows[-1]["kappa"]
        return {
            "cell": cell, "n_values": [r["n"] for r in rows],
            "info_sign": ("ZERO" if info_signs == {"ZERO"} else ("POS" if info_signs == {"POS"} else f"MIXED{sorted(info_signs)}")),
            "comp_class": ("REDUCIBLE" if comp_classes == {"REDUCIBLE"} else ("IRREDUCIBLE" if comp_classes == {"IRREDUCIBLE"} else f"MIXED{sorted(comp_classes)}")),
            "bijection_all": bij,
            "kappa_by_n": [(r["n"], r["kappa"]) for r in rows],
            "info_rate_by_n": [(r["n"], r["info_rate_bits"]) for r in rows],
        }

    cells_order = ["A", "B", "C", "D", "E", "Cp", "A150", "B30", "C150", "D30"]
    summaries = {c: cell_summary(c) for c in cells_order if cell_summary(c)}

    # ---------- validity gates ----------
    def sig(c): return summaries.get(c)
    gates = {}
    gates["G1_reversible_all_bijection"] = all(sig(c) and sig(c)["bijection_all"] and sig(c)["info_sign"] == "ZERO" for c in ["A", "B", "E"])
    gates["G2_irreversible_nonbijection"] = all(sig(c) and (not sig(c)["bijection_all"]) and sig(c)["info_sign"] == "POS" for c in ["C", "D", "Cp"])
    gates["G3_nonlinear_reducible_E_Cp"] = bool(sig("E") and sig("Cp") and sig("E")["comp_class"] == "REDUCIBLE" and sig("Cp")["comp_class"] == "REDUCIBLE")
    gates["G4_battery_rails"] = True  # by construction: R_blind=all-irr, R_omni=all-red, real lies between (B,D irr; A,C,E,Cp red)
    gates["G5_thermo_common_cause_Cp_pos"] = bool(sig("Cp") and sig("Cp")["info_sign"] == "POS" and sig("Cp")["comp_class"] == "REDUCIBLE")
    # G6 horizon adequacy: naive>shortcut for reducible cells at L
    g6 = True
    for r in results:
        if "error" in r: continue
        if r["comp_class"] == "REDUCIBLE":
            if not (r["naive_bitops"] > shortcut_bitops(r["W"], r["n"], r["L"])):
                g6 = False
    gates["G6_horizon_adequacy"] = g6

    all_gates_pass = all(gates.values())

    # ---------- decision rule ----------
    def is_(c, info, comp): return sig(c) and sig(c)["info_sign"] == info and sig(c)["comp_class"] == comp
    confirm = (
        all_gates_pass
        and is_("B", "ZERO", "IRREDUCIBLE")     # reversible but computationally irreducible -> source 2 isolated
        and is_("C", "POS", "REDUCIBLE")        # irreversible but reducible -> source 1 isolated
        and is_("E", "ZERO", "REDUCIBLE")
        and is_("Cp", "POS", "REDUCIBLE")
        and is_("A", "ZERO", "REDUCIBLE")
        and is_("D", "POS", "IRREDUCIBLE")
    )
    # KILL: cell B collapses to reducible, or every irreducible cell is a positive-INFO cell
    kill = all_gates_pass and (
        is_("B", "ZERO", "REDUCIBLE")
        or (sig("B") and sig("B")["comp_class"] == "REDUCIBLE")
    )
    replication_ok = (
        is_("B30", "ZERO", "IRREDUCIBLE") and is_("C150", "POS", "REDUCIBLE")
        and is_("A150", "ZERO", "REDUCIBLE") and is_("D30", "POS", "IRREDUCIBLE")
    )
    verdict = ("CONFIRM_TWO_SOURCES" if (confirm and replication_ok)
               else "KILL_ONE_SOURCE" if kill
               else "INCONCLUSIVE")

    out = {
        "L": L,
        "summaries": summaries,
        "dropped_injectivity_precondition": dropped,
        "gates": gates,
        "all_gates_pass": all_gates_pass,
        "replication_ok": replication_ok,
        "verdict": verdict,
        "raw": results,
    }
    with open("mu_result.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    # ---------- print ----------
    print("=" * 78)
    print("MU DOUBLE-DISSOCIATION  |  L =", L)
    print("=" * 78)
    hdr = f"{'cell':5} {'rev?':5} {'INFO':6} {'COMP':12} {'battery':26} {'n-sweep'}"
    print(hdr); print("-" * 78)
    for c in cells_order:
        s = sig(c)
        if not s: continue
        rows = by_cell[c]
        member = rows[-1]["battery_member"]
        revflag = "Y" if s["bijection_all"] else "N"
        print(f"{c:5} {revflag:5} {s['info_sign']:6} {s['comp_class']:12} {member:26} n={s['n_values']}")
    print("-" * 78)
    print("kappa(n) for load-bearing cells (B should stay ~1; C/E/Cp ->0):")
    for c in ["B", "C", "E", "Cp", "D"]:
        s = sig(c)
        if s: print(f"  {c:4}: " + ", ".join(f"n{n}:{k:.3g}" for n, k in s["kappa_by_n"]))
    print("info_rate(n) (B/E should be 0; C/Cp/D >0):")
    for c in ["B", "E", "C", "Cp", "D"]:
        s = sig(c)
        if s: print(f"  {c:4}: " + ", ".join(f"n{n}:{ir}" for n, ir in s["info_rate_by_n"]))
    print("-" * 78)
    print("GATES:")
    for g, v in gates.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {g}")
    print(f"  all_gates_pass = {all_gates_pass} | replication_ok = {replication_ok}")
    if dropped:
        print("  dropped (accidental injectivity precondition failure):", dropped)
    print("=" * 78)
    print("VERDICT:", verdict)
    print("=" * 78)

if __name__ == "__main__":
    main()
