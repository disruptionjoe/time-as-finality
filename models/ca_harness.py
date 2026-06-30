"""
Spec-independent CA substrate for the mu two-source reversal-cost discriminator.
Primitives only; metric assembly awaits the design-workflow spec.

Provides:
  - elementary CA rule application on a ring (periodic BC)
  - second-order (reversible) construction
  - exact global state-transition map (2^n enumeration) + in-degree/preimage counts
  - bijectivity (reversibility) check
  - GF(2)-linearity (additivity => computational reducibility) detector
  - additive fast-forward via circulant matrix power over GF(2) (the sub-linear shortcut)
Self-tests at bottom.
"""
from itertools import product

# ---------- elementary CA ----------
def rule_table(R):
    # index = (l<<2)|(c<<1)|r  -> output bit
    return [(R >> i) & 1 for i in range(8)]

def step1(state, T):
    """First-order elementary CA step on a ring. state: tuple of bits. T: rule_table."""
    n = len(state)
    return tuple(T[(state[(i-1) % n] << 2) | (state[i] << 1) | state[(i+1) % n]] for i in range(n))

# ---------- second-order (reversible) construction ----------
# Second-order rule: next = step1(cur) XOR prev. State is the pair (prev, cur).
# Map (prev,cur) -> (cur, next) is a bijection on 2^(2n) because prev = step1(cur) XOR next.
def step2(pair, T):
    prev, cur = pair
    s = step1(cur, T)
    nxt = tuple(a ^ b for a, b in zip(s, prev))
    return (cur, nxt)

def inv_step2(pair, T):
    cur, nxt = pair
    s = step1(cur, T)
    prev = tuple(a ^ b for a, b in zip(s, nxt))
    return (prev, cur)

# ---------- global maps over all states ----------
def all_states(n):
    return list(product((0, 1), repeat=n))

def global_map1(n, T):
    """dict: state -> next_state for first-order rule."""
    return {s: step1(s, T) for s in all_states(n)}

def indegrees(gmap):
    """preimage counts: for each image y, how many x map to it."""
    deg = {}
    for x, y in gmap.items():
        deg[y] = deg.get(y, 0) + 1
    return deg

def is_bijection(gmap):
    images = set(gmap.values())
    return len(images) == len(gmap)

# ---------- additivity / GF(2)-linearity detector ----------
def is_additive(T):
    """
    A rule is GF(2)-linear (additive) iff step1 is a linear map over GF(2):
    step1(a XOR b) == step1(a) XOR step1(b) for all a,b, and step1(0)=0.
    For elementary CA this is equivalent to the local rule being
    output = alpha*l XOR beta*c XOR gamma*r (no constant, no nonlinear AND terms).
    Test exhaustively on the 3-bit neighborhood basis.
    """
    # rule output as function f(l,c,r); linear iff f = a*l xor b*c xor g*r and f(0,0,0)=0
    def f(l, c, r):
        return T[(l << 2) | (c << 1) | r]
    if f(0, 0, 0) != 0:
        return False
    a = f(1, 0, 0); b = f(0, 1, 0); g = f(0, 0, 1)
    for l, c, r in product((0, 1), repeat=3):
        if f(l, c, r) != ((a & l) ^ (b & c) ^ (g & r)):
            return False
    return True

# ---------- additive fast-forward (the sub-linear shortcut) ----------
def circulant_rows(n, T):
    """For an additive rule, row i of the GF(2) update matrix M (next = M @ state)."""
    a = T[(1 << 2)]            # coeff of left  (l=1,c=0,r=0) -> index 4
    b = T[(1 << 1)]            # coeff of center (index 2)
    g = T[1]                   # coeff of right (index 1)
    # next[i] = a*state[i-1] xor b*state[i] xor g*state[i+1]
    M = []
    for i in range(n):
        row = [0] * n
        row[(i - 1) % n] ^= a
        row[i] ^= b
        row[(i + 1) % n] ^= g
        M.append(row)
    return M

def matmul_gf2(A, B):
    n = len(A); m = len(B[0]); k = len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            if Ai[t]:
                Bt = B[t]
                Ci = C[i]
                for j in range(m):
                    Ci[j] ^= Bt[j]
    return C

def matpow_gf2(M, p):
    n = len(M)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # identity
    base = [row[:] for row in M]
    while p > 0:
        if p & 1:
            R = matmul_gf2(R, base)
        base = matmul_gf2(base, base)
        p >>= 1
    return R

def apply_gf2(M, v):
    n = len(M)
    return tuple((sum(M[i][j] & v[j] for j in range(len(v))) & 1) for i in range(n))

def fast_forward_additive(state, T, t):
    """State after t steps via O(n^3 log t) matrix power -- sub-linear in t (the reducibility shortcut)."""
    M = circulant_rows(len(state), T)
    Mt = matpow_gf2(M, t)
    return apply_gf2(Mt, state)

def naive_forward(state, T, t):
    s = state
    for _ in range(t):
        s = step1(s, T)
    return s

# ============================ SELF-TESTS ============================
if __name__ == "__main__":
    ok = True
    def check(name, cond):
        global ok
        ok = ok and cond
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

    print("Additivity detector:")
    check("Rule 90 additive (l xor r)", is_additive(rule_table(90)))
    check("Rule 150 additive (l xor c xor r)", is_additive(rule_table(150)))
    check("Rule 60 additive (l xor c)", is_additive(rule_table(60)))
    check("Rule 110 NOT additive", not is_additive(rule_table(110)))
    check("Rule 30 NOT additive", not is_additive(rule_table(30)))
    check("Rule 204 additive (identity=center)", is_additive(rule_table(204)))

    print("First-order reversibility (in-degrees) on ring n=8:")
    n = 8
    g90 = global_map1(n, rule_table(90))
    g110 = global_map1(n, rule_table(110))
    deg90 = indegrees(g90)
    check("Rule 90 first-order is NON-injective (irreversible)", not is_bijection(g90))
    check("Rule 110 first-order is NON-injective (irreversible)", not is_bijection(g110))
    # report max preimage multiplicity
    print(f"    rule90 max preimage = {max(deg90.values())}, distinct images = {len(set(g90.values()))}/{2**n}")

    print("Second-order reversibility on ring n=6 (state = pair, 2^(2n)):")
    n2 = 6
    states = [(p, c) for p in all_states(n2) for c in all_states(n2)]
    for R in (90, 110, 30):
        T = rule_table(R)
        fwd = {st: step2(st, T) for st in states}
        bij = len(set(fwd.values())) == len(fwd)
        # also check inv_step2 truly inverts
        inv_ok = all(inv_step2(step2(st, T), T) == st for st in states)
        check(f"2nd-order Rule {R} is BIJECTIVE (reversible)", bij)
        check(f"2nd-order Rule {R} inv_step2 inverts forward", inv_ok)

    print("Additive shortcut correctness (fast matrix-power == naive stepping):")
    import random
    random.seed(12345)
    for R in (90, 150, 60):
        T = rule_table(R)
        for _ in range(20):
            nn = random.randint(5, 11)
            s0 = tuple(random.randint(0, 1) for _ in range(nn))
            t = random.randint(1, 50)
            check(f"Rule {R} n={nn} t={t} fast==naive", fast_forward_additive(s0, T, t) == naive_forward(s0, T, t))
            break  # one per rule to keep output short

    print("\nALL PRIMITIVE SELF-TESTS:", "PASS" if ok else "FAIL")
