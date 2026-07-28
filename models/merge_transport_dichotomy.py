"""Merge-transport dichotomy for connection-based readings of the finality
preorder: machine check.

CLAIMS CHECKED (finite instances; the symbolic proofs live in the comments and
are general -- the enumeration corroborates them, it does not carry the
generality):

(a) TRANSPORT MONOID LAW. For a join-semilattice (L, v), transport-by-s is
    T_s(x) = x v s. Then {T_s} u {id} is a commutative idempotent monoid under
    composition: (T_s o T_t)(x) = T_s(T_t(x)) = T_{s v t}(x), and
    T_s o T_s = T_s. Transports are inflationary: x <= T_s(x).
    Checked exhaustively on: ALL labeled join-semilattices on n <= 5 elements
    (enumerated two independent ways for n <= 4 -- poset-with-all-joins and
    commutative-idempotent-associative operation tables -- counts must agree),
    plus powerset lattices 2^[n] for n <= 4, plus the meet-dual on 2^[3]
    (the meet-semilattice codomain of T242, by order duality).

(b) FOLKLORE LEMMA (units of an idempotent monoid are trivial). In any monoid
    M in which every element is idempotent, the group of units is {e}:
        x invertible => x = x.e = x.(x.x^-1) = (x.x).x^-1 = x.x^-1 = e.
    Uses associativity and idempotence only; commutativity is NOT required.
    Checked exhaustively on ALL unital monoids with every element idempotent
    on <= 4 elements (identity fixed WLOG at index 0), which includes
    non-commutative bands (e.g. left-zero band + adjoined identity).

(b') SET-LEVEL LEMMA. Any idempotent endofunction is the identity or
    non-injective: if f(x) != x then x and f(x) are distinct points with
    f(x) = f(f(x)). Checked exhaustively on all endofunctions of sets of
    size <= 6.

(c) COROLLARY (identically trivial holonomy for semilattice merge transport).
    Per enumerated semilattice: every invertible (bijective) T_s equals id,
    and then s is a bottom element; every T_s != id is non-injective. Any
    path composite equals T_{join of edge labels}, is idempotent, and is
    invertible only if it is id. So holonomy is trivial IDENTICALLY -- over
    every semilattice, every graph, every labeling -- not merely flat for
    particular connection data. Loop demo run on the powerset of the D1
    dimension universe {a, h, b, r}: the ONLY edge labelings of a loop whose
    loop composite is a bijection are the all-bottom labelings, whose
    composite is id.

(d) COMPLEMENTARY HORN (non-confluent / information-destroying merge).
    Per-key last-writer-wins override on partial maps is redelivery-idempotent
    (T_s o T_s = T_s) but NON-confluent (T_s o T_t != T_t o T_s); every
    non-identity transport is non-injective, hence not a fiber isomorphism,
    hence defines no principal/Ehresmann connection at all (parallel
    transport is by definition invertible). The label monoid is a
    NON-commutative band with trivial units, so on the finite fiber every
    invertible composite of these transports is id. Destructive overwrite
    (constant map) is the extreme information-destroying case.

(e) DICHOTOMY (printed as the closing summary). Either the merge transports
    are honest fiber isomorphisms -- and then, being invertible idempotents,
    every one of them is the identity (the nothing-happens sector) -- or some
    transport genuinely merges, and then it is non-injective and the
    connection reading is not defined at that edge. There is no third sector.

Complexity posture: finite_witness + poly_decider style. Exhaustive
enumeration over declared small universes; no search over completions, no
sampling, no hardness claim. Pure Python, no dependencies.
Exit 0 = every assertion held.
"""

from __future__ import annotations

from itertools import combinations, permutations, product

# Known labeled poset counts (OEIS A001035) used as an enumeration guard.
LABELED_POSET_COUNTS = {1: 1, 2: 3, 3: 19, 4: 219, 5: 4231}


# ---------------------------------------------------------------------------
# Enumeration: labeled posets and labeled join-semilattices on n elements
# ---------------------------------------------------------------------------

def all_labeled_posets(n):
    """All strict partial orders on range(n).

    A partial order is determined by assigning each unordered pair {a, b} one
    of three states (incomparable, a < b, b < a) subject to transitivity, so
    the 3^(n choose 2) assignments with a transitivity filter enumerate every
    labeled poset exactly once.
    """
    pairs = list(combinations(range(n), 2))
    posets = []
    for orient in product((0, 1, 2), repeat=len(pairs)):
        lt = set()
        for (a, b), o in zip(pairs, orient):
            if o == 1:
                lt.add((a, b))
            elif o == 2:
                lt.add((b, a))
        ok = True
        for (a, b) in lt:
            for c in range(n):
                if (b, c) in lt and (a, c) not in lt:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            posets.append(frozenset(lt))
    return posets


def join_table(n, lt):
    """Join table j[a][b] if (range(n), lt) is a join-semilattice, else None.

    Requires every pair to have a UNIQUE least upper bound.
    """
    def leq(a, b):
        return a == b or (a, b) in lt

    j = [[None] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            ubs = [c for c in range(n) if leq(a, c) and leq(b, c)]
            least = [u for u in ubs if all(leq(u, v) for v in ubs)]
            if len(least) != 1:
                return None
            j[a][b] = least[0]
    return j


def count_semilattice_ops(n):
    """Independent cross-check enumeration: commutative idempotent associative
    binary operations on range(n). These are in canonical bijection with
    labeled join-semilattices (order: a <= b iff a v b = b)."""
    pairs = list(combinations(range(n), 2))
    count = 0
    for vals in product(range(n), repeat=len(pairs)):
        op = [[None] * n for _ in range(n)]
        for i in range(n):
            op[i][i] = i
        for (a, b), v in zip(pairs, vals):
            op[a][b] = op[b][a] = v
        ok = True
        for a in range(n):
            for b in range(n):
                row = op[a][b]
                for c in range(n):
                    if op[row][c] != op[a][op[b][c]]:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            count += 1
    return count


# ---------------------------------------------------------------------------
# (a) + (c): transport laws and the trivial-units corollary, per semilattice
# ---------------------------------------------------------------------------

def check_semilattice_transport(n, lt, j):
    """Verify (a) and (c) on one labeled join-semilattice given by join table j.

    Returns (num_identity_transports, num_noninjective_transports).
    """
    def leq(a, b):
        return a == b or (a, b) in lt

    identity = tuple(range(n))

    # (a) transport monoid law, commutativity, idempotence, inflationarity.
    for s in range(n):
        for t in range(n):
            st = j[s][t]
            for x in range(n):
                # (T_s o T_t)(x) = T_s(T_t(x)) must equal T_{s v t}(x).
                assert j[j[x][t]][s] == j[x][st], "composition law failed"
                # commutativity of transports.
                assert j[j[x][t]][s] == j[j[x][s]][t], "commutativity failed"
        for x in range(n):
            # idempotence T_s o T_s = T_s.
            assert j[j[x][s]][s] == j[x][s], "idempotence failed"
            # inflationary: x <= T_s(x)  (the directed 2-cell direction).
            assert leq(x, j[x][s]), "inflationarity failed"

    # (c) corollary: invertible => identity => s is a bottom element;
    #     non-identity => non-injective (with an internal collision witness).
    n_id, n_noninj = 0, 0
    for s in range(n):
        T = tuple(j[x][s] for x in range(n))
        if len(set(T)) == n:  # bijective transport
            assert T == identity, "invertible transport that is not id"
            assert all(leq(s, x) for x in range(n)), \
                "identity transport whose label is not a bottom element"
            n_id += 1
        else:
            assert T != identity
            # exhibit the collision the symbolic proof names: pick x with
            # T_s(x) != x; then x and T_s(x) are distinct with equal images.
            x = next(x for x in range(n) if T[x] != x)
            assert T[T[x]] == T[x] and T[x] != x
            n_noninj += 1
    return n_id, n_noninj


def check_all_small_semilattices(max_n=5):
    report = {}
    for n in range(1, max_n + 1):
        posets = all_labeled_posets(n)
        assert len(posets) == LABELED_POSET_COUNTS[n], \
            f"poset enumeration broken at n={n}"
        semis = []
        for lt in posets:
            j = join_table(n, lt)
            if j is not None:
                semis.append((lt, j))
        tot_id = tot_noninj = 0
        for lt, j in semis:
            a, b = check_semilattice_transport(n, lt, j)
            tot_id += a
            tot_noninj += b
        report[n] = {
            "labeled_posets": len(posets),
            "labeled_join_semilattices": len(semis),
            "identity_transports": tot_id,
            "noninjective_transports": tot_noninj,
        }
        # every transport is exactly one of: identity / non-injective
        assert tot_id + tot_noninj == n * len(semis)
        if n <= 4:
            ops = count_semilattice_ops(n)
            assert ops == len(semis), \
                f"cross-check failed at n={n}: ops={ops} posets={len(semis)}"
            report[n]["op_table_cross_check"] = ops
    return report


def check_powerset(n):
    """Powerset lattice 2^[n] as bitmasks; join = OR. Same checks as above."""
    full = 1 << n
    elems = list(range(full))
    identity = tuple(elems)
    for s in elems:
        for t in elems:
            for x in elems:
                assert (x | t) | s == x | (s | t)
                assert (x | t) | s == (x | s) | t
        T = tuple(x | s for x in elems)
        assert tuple((x | s) | s for x in elems) == T  # idempotent
        if len(set(T)) == full:
            assert T == identity and s == 0
        else:
            assert s != 0
    # meet-dual spot check on 2^[3] (T242's meet-semilattice codomain):
    if n == 3:
        top = full - 1
        for s in elems:
            for t in elems:
                for x in elems:
                    assert (x & t) & s == x & (s & t)
            T = tuple(x & s for x in elems)
            assert tuple((x & s) & s for x in elems) == T
            if len(set(T)) == full:
                assert T == identity and s == top
    return True


# ---------------------------------------------------------------------------
# (b): the folklore lemma, exhaustively on small unital idempotent monoids
# ---------------------------------------------------------------------------

def check_unital_idempotent_monoids(max_n=4):
    """Enumerate ALL monoids on range(n) (identity fixed at 0 WLOG) in which
    every element is idempotent -- including NON-commutative bands -- and
    assert the group of units is exactly {0}."""
    report = {}
    for n in range(1, max_n + 1):
        free = [(a, b) for a in range(1, n) for b in range(1, n) if a != b]
        total = noncomm = 0
        for vals in product(range(n), repeat=len(free)):
            op = [[None] * n for _ in range(n)]
            for b in range(n):
                op[0][b] = b
            for a in range(n):
                op[a][0] = a
            for a in range(1, n):
                op[a][a] = a  # idempotence forced on the diagonal
            for (a, b), v in zip(free, vals):
                op[a][b] = v
            ok = True
            for a in range(n):
                for b in range(n):
                    row = op[a][b]
                    for c in range(n):
                        if op[row][c] != op[a][op[b][c]]:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    break
            if not ok:
                continue
            total += 1
            if any(op[a][b] != op[b][a] for a in range(n) for b in range(n)):
                noncomm += 1
            units = [x for x in range(n)
                     if any(op[x][y] == 0 and op[y][x] == 0
                            for y in range(n))]
            assert units == [0], f"nontrivial unit in an idempotent monoid: {op}"
        report[n] = {"unital_idempotent_monoids": total,
                     "of_which_noncommutative": noncomm}
    # the lemma's non-commutative reach is real, not vacuous:
    assert report[3]["of_which_noncommutative"] > 0
    return report


def check_idempotent_endofunctions(max_n=6):
    """(b') every idempotent endofunction is the identity or non-injective."""
    for n in range(1, max_n + 1):
        identity = tuple(range(n))
        for f in product(range(n), repeat=n):
            if all(f[f[x]] == f[x] for x in range(n)):
                assert f == identity or len(set(f)) < n
    return True


# ---------------------------------------------------------------------------
# (c) loop demo on the D1 dimension universe {a, h, b, r}
# ---------------------------------------------------------------------------

D1_DIMENSIONS = ("a", "h", "b", "r")  # accessible_support, holder_redundancy,
                                      # branch_support, reversal_cost


def check_loop_demo():
    """Triangle loop v0 -> v1 -> v2 -> v0 with fiber 2^{a,h,b,r} (bitmasks).

    Facts checked:
      - the loop composite equals T_{join of the edge labels}, in every
        traversal order (path-order independence inside the loop);
      - for the witness labels {a}, {h,r}, {b} the composite is the constant
        map onto the full set -- maximally non-injective;
      - over ALL 16^3 labelings of the triangle, the loop composite is a
        bijection iff all three labels are bottom (empty), iff the composite
        is the identity: the invertible-holonomy sector is exactly the
        nothing-happens sector;
      - two-path discrepancy cannot be packaged as holonomy: for paths with
        label-joins P = {a,h} and Q = {r}, T_P != T_Q, but T_Q is
        non-injective, so no function g satisfies g o T_Q = id and the
        would-be comparison "T_Q^{-1} o T_P" does not exist. What does exist
        is the directed comparison x <= T_P(x), x <= T_Q(x) -- the
        lax/oplax 2-cell shape, not a group element.
    """
    full = (1 << len(D1_DIMENSIONS)) - 1
    elems = list(range(full + 1))
    identity = tuple(elems)

    def T(s):
        return tuple(x | s for x in elems)

    def comp(F, G):  # (F o G)(x) = F(G(x))
        return tuple(F[G[x]] for x in elems)

    A, H, B, R = 1, 2, 4, 8
    labels = (A, H | R, B)  # {a}, {h,r}, {b}
    join = A | H | R | B
    composites = set()
    for perm in permutations(labels):
        F = T(perm[0])
        for s in perm[1:]:
            F = comp(T(s), F)
        composites.add(F)
    assert composites == {T(join)}, "loop composite is not T_{join of labels}"
    assert T(join) == tuple(full for _ in elems)  # constant map here
    assert len(set(T(join))) == 1  # maximally non-injective

    # all labelings: invertible loop composite <=> all labels bottom <=> id
    for s1 in elems:
        for s2 in elems:
            for s3 in elems:
                Floop = comp(T(s3), comp(T(s2), T(s1)))
                assert Floop == T(s1 | s2 | s3)
                if len(set(Floop)) == len(elems):
                    assert (s1, s2, s3) == (0, 0, 0) and Floop == identity
                else:
                    assert (s1, s2, s3) != (0, 0, 0)

    # two-path discrepancy: real difference, but not group-valued.
    TP, TQ = T(A | H), T(R)
    assert TP != TQ
    x, y = 0, R  # T_Q collides: T_Q(empty) == T_Q({r})
    assert x != y and TQ[x] == TQ[y]
    # no left inverse g with g o T_Q = id can exist:
    # g(T_Q(x)) would need to be both x and y. Directed cells DO exist:
    for x in elems:
        assert x | TP[x] == TP[x] and x | TQ[x] == TQ[x]  # x <= T(x)
    return True


# ---------------------------------------------------------------------------
# (d) complementary horn: non-confluent and information-destroying merges
# ---------------------------------------------------------------------------

def check_lww_override():
    """Per-key last-writer-wins override on partial maps {k0,k1} -> {0,1}.

    States: all 9 partial maps. T_s(x) = x overridden by s ({**x, **s}).
    """
    keys = (0, 1)
    states = []
    for v0 in (None, 0, 1):
        for v1 in (None, 0, 1):
            d = {}
            if v0 is not None:
                d[0] = v0
            if v1 is not None:
                d[1] = v1
            states.append(tuple(sorted(d.items())))
    assert len(states) == 9

    def override(x, s):  # {**x, **s}
        d = dict(x)
        d.update(dict(s))
        return tuple(sorted(d.items()))

    def T(s):
        return {x: override(x, s) for x in states}

    def comp(F, G):
        return {x: F[G[x]] for x in states}

    identity = {x: x for x in states}
    empty = ()

    # label monoid: compose_labels(s, t) is the label of T_s o T_t.
    def compose_labels(s, t):  # apply t first, then s: {**t, **s}
        return override(t, s)

    n_noncommuting_pairs = 0
    for s in states:
        Ts = T(s)
        # redelivery idempotence
        assert comp(Ts, Ts) == Ts
        # label idempotence (band law)
        assert compose_labels(s, s) == s
        for t in states:
            # composition law: T_s o T_t = T_{compose_labels(s, t)}
            assert comp(Ts, T(t)) == T(compose_labels(s, t))
            if comp(Ts, T(t)) != comp(T(t), Ts):
                n_noncommuting_pairs += 1
    assert n_noncommuting_pairs > 0, "override merge unexpectedly confluent"

    # explicit non-confluence witness: s = {k0: 0}, t = {k0: 1}
    s, t = ((0, 0),), ((0, 1),)
    assert comp(T(s), T(t))[empty] == s  # t then s: s wins
    assert comp(T(t), T(s))[empty] == t  # s then t: t wins
    assert comp(T(s), T(t)) != comp(T(t), T(s))

    # units of the label band are trivial; transports: injective <=> s empty
    for s in states:
        inverses = [y for y in states
                    if compose_labels(s, y) == empty
                    and compose_labels(y, s) == empty]
        if s == empty:
            assert inverses == [empty]
        else:
            assert inverses == []
        Ts = T(s)
        injective = len(set(Ts.values())) == len(states)
        if s == empty:
            assert injective and Ts == identity
        else:
            assert not injective
            # explicit collision: two states differing at a key s writes
            k, v = s[0]
            x1 = ((k, 0),)
            x2 = ((k, 1),)
            assert x1 != x2 and Ts[x1] == Ts[x2]

    # finite fiber: every invertible composite of these transports is id.
    # (Composites are T_{some label}; invertible <=> label empty <=> id.)
    for s in states:
        for t in states:
            F = comp(T(s), T(t))
            if len(set(F.values())) == len(states):
                assert F == identity

    # destructive overwrite register (extreme information destruction):
    V = (0, 1)
    for c in V:
        const = {x: c for x in V}
        assert len(set(const.values())) == 1  # maximally non-injective
    return True


# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------

def main():
    print("MERGE-TRANSPORT DICHOTOMY: MACHINE CHECK")
    print("=" * 72)

    rep_a = check_all_small_semilattices(max_n=5)
    print("\n(a)+(c) join-semilattice transport monoid + trivial units,")
    print("        exhaustive over ALL labeled join-semilattices, n <= 5:")
    for n, r in rep_a.items():
        line = (f"  n={n}: posets={r['labeled_posets']}"
                f"  join-semilattices={r['labeled_join_semilattices']}"
                f"  transports: id={r['identity_transports']}"
                f" noninj={r['noninjective_transports']}")
        if "op_table_cross_check" in r:
            line += f"  [op-table cross-check: {r['op_table_cross_check']} OK]"
        print(line)
    print("  every transport is exactly one of: identity | non-injective.")
    print("  every bijective transport IS the identity, labeled by a bottom.")

    for n in range(1, 5):
        check_powerset(n)
    print("\n(a)+(c) powerset lattices 2^[n], n <= 4: PASS "
          "(incl. meet-dual on 2^[3] -- T242's meet-semilattice codomain).")

    rep_b = check_unital_idempotent_monoids(max_n=4)
    print("\n(b) folklore lemma -- units of an idempotent monoid are trivial,")
    print("    exhaustive over ALL unital all-idempotent monoids, n <= 4")
    print("    (commutativity NOT assumed):")
    for n, r in rep_b.items():
        print(f"  n={n}: monoids={r['unital_idempotent_monoids']}"
              f"  non-commutative={r['of_which_noncommutative']}"
              "  units={e} in all")

    check_idempotent_endofunctions(max_n=6)
    print("\n(b') every idempotent endofunction on |V| <= 6 is the identity")
    print("     or non-injective: PASS (exhaustive over all n^n functions).")

    check_loop_demo()
    print("\n(c) loop demo on 2^{a,h,b,r} (D1 dimension universe):")
    print("  - loop composite = T_(join of edge labels), traversal-order free;")
    print("  - witness labels {a},{h,r},{b}: composite is the CONSTANT map;")
    print("  - over all 16^3 labelings: loop composite bijective <=> all")
    print("    labels bottom <=> composite = id (nothing-happens sector);")
    print("  - two-path discrepancy T_{a,h} != T_{r} exists but T_{r} has no")
    print("    inverse, so no group-valued holonomy packages it; the")
    print("    inflationary directed cells x <= T(x) survive (lax shape).")

    check_lww_override()
    print("\n(d) complementary horn (LWW override on 9 partial maps):")
    print("  - redelivery-idempotent, NON-confluent (order-dependent pairs")
    print("    exhibited); label monoid is a non-commutative band, units {e};")
    print("  - every non-identity transport non-injective => not a fiber")
    print("    isomorphism => no principal/Ehresmann connection at that edge;")
    print("  - on the finite fiber every invertible composite is id;")
    print("  - destructive overwrite = constant map (extreme case).")

    print("\n(e) DICHOTOMY (both horns machine-checked):")
    print("  EITHER transports are fiber isomorphisms -- then, being")
    print("  invertible idempotents, each is the identity and the connection")
    print("  hosts only the sector in which nothing happens --")
    print("  OR some transport genuinely merges -- then it is non-injective")
    print("  and no connection is defined at that edge. No third sector.")
    print("\nALL ASSERTIONS PASSED (exit 0).")


if __name__ == "__main__":
    main()
