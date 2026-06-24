# T198: Cap_TI Positive / Null Control Suite

## Correction Notice

Updated after the T187 review/T200-T209 follow-up. The controls below are valid
only for the declared finite harmonic-proxy regime unless separately restated
for corrected LP or edge-capacity flow models. T209 now serves as the arithmetic
guardrail that prevents conflating those regimes.

## Target Claims

- Cap_TI Candidate C (`open-problems/cap-ti-capability-object-spec.md`)
- T193 minimal sufficient statistic result
- T194 hostile adversarial-family result

## Origin

The earlier Cap_TI work established three things:

1. Candidate C has a real positive split when the delivery-time summary differs
   (`T188`).
2. In the finite harmonic-proxy regime, the capability compresses to the
   reduced invariant `(n, T*)` (`T193`).
3. No stricter hostile split survives once `(n, T*)` is matched (`T194`).

What is still missing is a reusable control suite so later tests do not have to
re-derive those distinctions from scratch.

## Formal Target Or Obligation

Build a control family for Candidate C that cleanly separates:

1. **Positive controls**: `T*` differs, so the capability must split.
2. **Null controls**: `(n, T*)` is matched, so the capability must not split.
3. **Stress controls**: large visible structural differences that are still
   null because they do not move the reduced invariant.

The suite is judged successful if a later test can cite these control classes
instead of rebuilding the entire logic.

## Capability Under Test

In the current harmonic-proxy regime:

```text
Cap_TI^C(Y) = R(beta(Y), n(Y))
beta(Y) = 1 - log(T*(Y)) / log(n)
R(beta,n) = T*(Y)
```

So the suite should be keyed to `T*`.

## Control Classes

### Control P1: Alpha/Beta Positive Split

Use the T186/T187 pair:

```text
Alpha: n=5, path times {4,2,1}, T*_A = 1.714...
Beta:  n=5, path times {3,2,1}, T*_B = 1.636...
```

Shared:

```text
same causal order
same event count
same entropy class
same topology type
```

Expected:

```text
T*_A != T*_B => R_A != R_B
```

This is the canonical positive control.

### Control P2: Monotone Ordering Positive Family

Construct a one-parameter family of path-time triples where `T*` decreases
strictly:

```text
F_pos(m): {m+2, m+1, m}
```

for admissible integer `m >= 1`.

Expected:

```text
if T*(m1) > T*(m2), then R(m1) > R(m2).
```

This checks that the capability respects the reduced metric axis monotonically,
not just on one named witness pair.

### Control N1: Branch-Label Null

Keep the same path-time multiset and just permute labels across branches.

Expected:

```text
same T* => same R.
```

### Control N2: Compensated-Harmonic-Mean Null

Use two different path-time triples with the same reciprocal sum:

```text
Y1: {a,b,c}
Y2: {a',b',c'}
```

with

```text
1/a + 1/b + 1/c = 1/a' + 1/b' + 1/c'.
```

Expected:

```text
same T* => same R
```

even though variance/range/asymmetry differ.

### Control N3: Topology-Variation Null

Hold:

```text
same n
same T*
```

but vary internal branching arrangement or branch naming detail.

Expected:

```text
same T* => same R
```

under the current exact finite reading.

### Control S1: Causal-Order-Only Stress Null

Construct systems with visibly different causal details that still collapse once
`T*` is matched.

Purpose:

```text
show that not every rich-looking structural change is capability-relevant.
```

### Control S2: Higher-Moment Stress Null

Match `T*` while making variance, range, and skew as different as possible
within a finite admissible family.

Purpose:

```text
stress whether the exact finite capability has hidden dependence on moments
beyond harmonic mean.
```

### Control S3: Scale Stress Positive

Fix a path-time shape class and increase event count `n` only when the induced
`T*` changes under the chosen family construction.

Purpose:

```text
separate "size alone" from "size mediated through T*" effects.
```

## Positive Control Criteria

The suite passes its positive side if:

1. P1 splits as expected.
2. P2 shows monotone ordering of `R` with `T*`.

## Null Control Criteria

The suite passes its null side if:

1. N1 shows no split under branch relabeling.
2. N2 shows no split under compensated metric tradeoff with matched `T*`.
3. N3 shows no split under topology variation with matched `T*`.

## Stress Control Criteria

The suite passes its stress side if:

1. S1 and S2 remain null when `T*` is fixed.
2. S3 remains positive only when `T*` moves.

## Absorber Pass

The absorber from T193/T194 is now the suite’s design principle:

```text
for the finite harmonic-proxy regime,
T* is the capability axis.
```

So the suite’s purpose is not to rediscover the theorem, but to operationalize
it into reusable control classes:

- controls that vary `T*` should split;
- controls that preserve `T*` should not.

## Results

### 1. Positive controls are now explicitly keyed to `T*`

P1 and P2 formalize the currently valid positive axis:

```text
lower T* => lower R
higher T* => higher R
```

within the exact finite family.

### 2. Null controls are now explicitly keyed to matched `(n, T*)`

N1-N3 make the null logic reusable:

```text
branch relabeling
compensated time tradeoffs
topology detail changes
```

are all null so long as `T*` stays fixed.

### 3. Stress controls clarify what counts as a fake positive

S1-S3 formalize the main anti-overclaim lesson:

```text
rich visible structural change is not evidence of a capability split unless it
moves the reduced invariant.
```

### 4. What the suite does not do

The suite does not prove a new theorem beyond T193/T194. Its value is
operational:

```text
it turns the current exact-family logic into a reusable calibration harness.
```

## Verdict: promoted

Unlike T193 and T194, this test is not mainly a novelty claim. Its job is to
convert the current exact-family lessons into an explicit reusable suite.

It succeeds at that job:

```text
the control structure is now explicit,
reusable,
and keyed to the actual reduced invariant.
```

So for its intended role as infrastructure, the verdict is `promoted`.

## Falsification Conditions

The suite should be revised if:

1. a later test finds a real split with matched `(n, T*)`;
2. the exact finite Moses/T187 formula is replaced by a richer protocol;
3. a continuum bridge introduces a better control axis than `T*`.

## Next Step

Use this suite directly in:

```text
T197: absorber audit against scheduling / queueing / flow theory
T195: generalization beyond the current tree fixture family
```

and any future Candidate C promotion attempt.
