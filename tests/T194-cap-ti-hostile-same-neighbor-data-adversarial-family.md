# T194: Cap_TI Hostile Same-Neighbor-Data Adversarial Family

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. The hostile-family collapse
below is conditional on the finite harmonic-proxy regime where `R = T*`. It
does not prove exact Moses minimality, and it should not be exported as a
statement about corrected LP or edge-capacity DAG flow models.

## Target Claims

- Cap_TI Candidate C (`open-problems/cap-ti-capability-object-spec.md`)
- T188 hostile same-neighbor-data split
- T193 minimal sufficient statistic result

## Origin

T188 showed a real physical-substrate split:

```text
same causal order
same gluing topology
different delivery-time metric
=> different beta
=> different predicted reconciliation cost
```

T193 then compressed Candidate C much further:

```text
for the finite harmonic-proxy regime,
R(beta,n) = T*
```

where `T*` is the harmonic mean of path delivery times.

That changes the hostile question. We no longer ask whether the full metric
object matters. We ask the sharper adversarial question:

```text
Can Candidate C still split once (n, T*) are held fixed?
```

## Formal Target Or Obligation

Construct adversarial families that preserve the reduced freeze:

```text
same n
same T*
same causal order
same event count
same entropy class
same gluing-topology type
```

while varying richer metric or topological detail.

If any such family still changes the Candidate C value, T193 is too weak.
If all such families collapse, the reduced invariant survives hostile pressure.

## Capability Under Test

Candidate C value:

```text
Cap_TI^C(Y) = R(beta(Y), n(Y))
```

For the finite harmonic-proxy reading:

```text
beta(Y) = 1 - log(T*(Y)) / log(n)
R(beta,n) = n^(1-beta) = T*(Y)
```

So the hostile target is very explicit:

```text
hold T*(Y) fixed and try to change R anyway.
```

## Adversarial Family Templates

### Family A: Baseline Positive-Control Split

This is the original Alpha/Beta family from T186/T187.

```text
Alpha: n=5, path times {4,2,1}, T*_A = 1.714...
Beta:  n=5, path times {3,2,1}, T*_B = 1.636...
```

Shared:

```text
same causal order
same event count
same entropy class
same gluing topology type
```

Difference:

```text
T*_A != T*_B
```

Expected result:

```text
R_A != R_B
```

This is a positive control, not a hostile reduced-freeze family.

### Family B: Branch-Label Permutation Family

Take a fixed path-time multiset, for example:

```text
{4,2,1}
```

Construct two systems with the same causal-order shape and same path-time
multiset, but assign the times to different named branches:

```text
Y1: slow branch on arm A, medium on B, fast on C
Y2: slow branch on arm B, medium on C, fast on A
```

Then:

```text
same n
same T*
same full time multiset
same causal order
```

Expected result:

```text
R(Y1) = R(Y2)
```

This tests whether mere metric relabeling can force a false split.

### Family C: Compensated Metric Tradeoff Family

Construct two systems with different full delivery-time distributions but the
same harmonic mean:

```text
Y1: path times {a,b,c}
Y2: path times {a',b',c'}
```

such that

```text
1/a + 1/b + 1/c = 1/a' + 1/b' + 1/c'
```

and therefore

```text
T*(Y1) = T*(Y2).
```

Example template:

```text
Choose a base triple {t1,t2,t3}.
Increase one path time by delta > 0.
Decrease a second path time so the reciprocal sum stays constant.
Hold the third fixed.
```

This produces different variance, range, and path asymmetry while preserving
the exact reduced invariant `T*`.

Expected result:

```text
R(Y1) = R(Y2)
```

if T193 is right.

### Family D: Topology-Variation-With-Matched-T* Family

Construct two finite source systems with different branching detail but the
same event count and same harmonic-mean delivery-time summary:

```text
Y_tree: shallow 3-path merge
Y_layered: same n, different internal arrangement, same T*
```

Expected result:

```text
R(Y_tree) = R(Y_layered)
```

provided the exact Candidate C value continues to depend only on `T*`.

This tests whether richer topological detail matters once the reduced metric
summary is fixed.

## Positive Control

Family A must preserve the known Alpha/Beta split:

```text
T*_A != T*_B => R_A != R_B.
```

This confirms the test is not trivializing the capability away.

## Negative Controls

### Negative Control 1: Branch relabeling only

Family B checks that branch naming or placement alone cannot produce a split.

### Negative Control 2: Same T*, different higher moments

Family C checks whether variance/range/asymmetry beyond `T*` changes the
capability.

### Negative Control 3: Same T*, different branching detail

Family D checks whether richer topological detail changes the capability once
the reduced metric summary is fixed.

## Absorber Pass

The natural absorber is the same statistical-compression reading from T193:

```text
if the exact decision value is a function only of T*,
then no finer metric or topological detail should survive a strict same-data
freeze once T* is matched.
```

The hostile test is therefore straightforward:

- if any family with matched `(n, T*)` still splits, the absorber fails and
  T193 was too optimistic;
- if all such families collapse, the absorber is correct and Candidate C is a
  harmonic-mean-based capability in the current finite exact family.

## Results

### 1. Positive control survives

Family A reproduces the original split:

```text
T*_Alpha = 1.714...
T*_Beta  = 1.636...
=> R_Alpha != R_Beta
```

So Candidate C remains nontrivial when the reduced invariant differs.

### 2. All matched-(n,T*) adversarial families collapse in the exact finite reading

For Families B, C, and D, the exact T187 formula gives:

```text
R(Y) = T*(Y)
```

Therefore if

```text
n(Y1) = n(Y2)
T*(Y1) = T*(Y2),
```

then automatically

```text
R(Y1) = R(Y2).
```

This is independent of:

- branch labeling;
- higher moments of the delivery-time distribution;
- richer path asymmetry;
- extra topological detail not entering `T*`.

### 3. No strict hostile survivor remains in the current exact finite family

T194 therefore finds no adversarial family with:

```text
same (n, T*)
different Candidate C value.
```

The hostile split from T188 remains real, but only because `T*` differed.
There is no deeper same-neighbor-data residue beyond the reduced invariant in
the current harmonic-proxy family.

### 4. What survives

Candidate C survives as:

```text
a harmonic-mean-based capability
```

not as a capability that depends on finer-grained metric or topological detail
beyond that summary.

## Verdict: narrowed

T194 does not kill Candidate C, because the positive control still works when
`T*` differs.

But it **does** narrow the hostile claim:

```text
no stricter same-neighbor-data adversarial family survives once (n, T*) are
matched in the current harmonic-proxy family.
```

So the surviving capability is smaller and cleaner than the original “full
metric transport” reading.

## Falsification Conditions

This verdict should be revisited if:

1. a family is found with matched `(n, T*)` but different exact Candidate C
   values;
2. the reconciliation protocol is enriched so that `R` depends on more than
   `T*`;
3. a continuum/WBE bridge introduces additional scale-sensitive quantities not
   visible in the finite harmonic-mean formula.

Without one of those, the current hostile family result stands.

## Next Step

The best follow-on moves are:

```text
T198: build explicit positive/null controls using T* as the key control axis.
T197: test whether this harmonic-mean-based capability is mostly absorbed by
      standard scheduling / queueing / flow theory.
```
