# T52: Symmetric Colimit Theorem

## Target Claims

- [H1: Record Reconstruction](../HYPOTHESES.md)
- [T50: Axis Monotonicity Theorem](T50-axis-monotonicity-theorem.md)
- [T51: Multi-Observer Apparent Finality Colimit](T51-multi-observer-apparent-finality-colimit.md)

## Central Question

When two observers each have strictly partial and complementary record access
over a 4-event FinaliEvent Structure, does the colimit of their apparent
finality structures:

1. Produce a consistent event-finality order (T47 acyclicity holds)?
2. Recover orderings invisible to BOTH observers symmetrically?
3. Equal the full event-finality reference (colimit is complete)?
4. Satisfy AM at the event-finality level, even when apparent AM fails locally?

## Setup

**4-event witness:** e1_alpha, e2_beta, e3_gamma, e4_delta.

**Full event-finality record bases:**

| System | Records |
|--------|---------|
| U1_alpha_source | {r1_raw} |
| U2_beta_source | {r2_raw} |
| U3_gamma_source | {r1_locked, r3_raw} |
| U4_delta_source | {r1_locked, r2_locked, r4_raw} |
| O1_alpha_locked | {r1_locked} |
| O2_beta_locked | {r2_locked} |
| O3_gamma_locked | {r3_locked} |
| O4_delta_locked | {r4_locked} |

**Full event-finality order (reference):**
- e1 ≤ e3: O1.records = {r1_locked} ⊆ U3.records ✓
- e1 ≤ e4: O1.records = {r1_locked} ⊆ U4.records ✓
- e2 ≤ e4: O2.records = {r2_locked} ⊆ U4.records ✓
- e1 || e2: no containment between O1/U2 or O2/U1
- e2 || e3: r2_locked ∉ U3.records; r1_locked ∉ U2.records
- e3 || e4: r3_locked ∉ U4.records; r4_locked ∉ U3.records

**Observer A (restricted: U4 missing r1_locked):**
- U4_delta_source.records = {r2_locked, r4_raw} ← missing r1_locked
- A sees: e2 ≤ e4 (r2_locked ∈ A's U4), e1 ≤ e3 (U3 unchanged)
- A CANNOT see: e1 ≤ e4 (r1_locked ∉ A's U4)
- A's phantom: (e1_alpha, e4_delta) — appears incomparable to A

**Observer B (restricted: U3 missing r1_locked):**
- U3_gamma_source.records = {r3_raw} ← missing r1_locked
- B sees: e1 ≤ e4, e2 ≤ e4 (U4 unchanged)
- B CANNOT see: e1 ≤ e3 (r1_locked ∉ B's U3)
- B's phantom: (e1_alpha, e3_gamma) — appears incomparable to B

**Colimit (merge A and B's bases):**
- U3_gamma merged: {r3_raw} ∪ {r1_locked, r3_raw} = {r1_locked, r3_raw} ✓
- U4_delta merged: {r2_locked, r4_raw} ∪ {r1_locked, r2_locked, r4_raw} = {r1_locked, r2_locked, r4_raw} ✓
- Colimit order = full reference: {e1≤e3, e1≤e4, e2≤e4}

**Symmetry of loss:**
- A loses (e1,e4) — the cross-chain ordering visible only from B's U4 records
- B loses (e1,e3) — the chain ordering visible only from A's U3 records
- Neither A nor B alone recovers the full reference; together they do

## Axis Profiles

The (causal, info) magnitudes are properties of target systems, unchanged
across observer boundaries:

| Event | causal (reversal_cost) | info (holder_redundancy) |
|-------|----------------------|------------------------|
| e1_alpha | 2 | 1 |
| e2_beta | 1 | 3 |
| e3_gamma | 4 | 2 |
| e4_delta | 3 | 4 |

**AM on reference order (predicted):** Holds. All 12 non-reflexive pairs match
(verified by construction — profiles designed to be Pareto-incomparable exactly
where record order is incomparable).

**AM on Observer A's apparent order (predicted):** Fails. Pair (e1,e4):
magnitude says e1 ≤ e4 (causal 2≤3, info 1≤4), but A's record order says e1 || e4.
SPURIOUS violation — magnitude over-represents A's apparent order.

**AM on Observer B's apparent order (predicted):** Fails. Pair (e1,e3):
magnitude says e1 ≤ e3 (causal 2≤4, info 1≤2), but B's record order says e1 || e3.
SPURIOUS violation — magnitude over-represents B's apparent order.

**AM on colimit (predicted):** Holds. Colimit = reference = full event-finality
order. AM on reference holds → AM on colimit holds.

## The New Phenomenon

T51 showed apparent AM can hold locally (each observer's apparent structure
satisfies AM) while the colimit adds orderings.

T52 reveals a different phenomenon: apparent AM FAILS locally for each bounded
observer (the magnitude order over-represents their restricted record order),
but AM is RESTORED at the event-finality level (the colimit repairs the
defect). The phantom incomparabilities that cause AM failure in apparent
structures are exactly the pairs recovered by the colimit.

AM is not a local property — it is an event-finality property. Bounded causal
access breaks AM locally by introducing phantom incomparabilities. The colimit
repairs them.

## Hypotheses Evaluated

- H_COLIMIT_CONSISTENT: Colimit of S_A and S_B is a valid partial order
  (reflexive, antisymmetric, transitive). T47 acyclicity guarantees this for
  PO1-admissible events.

- H_SYMMETRIC_PHANTOM: Observer A has exactly 1 phantom (e1||e4 apparent, e1≤e4
  in colimit). Observer B has exactly 1 phantom (e1||e3 apparent, e1≤e3 in
  colimit). The phantoms are distinct and symmetric.

- H_COLIMIT_COMPLETE: Colimit equals the full event-finality reference order.
  Neither A nor B alone recovers it; together they do. Both contribute new
  orderings to the colimit.

- H_AM_RESTORED: AM fails on each observer's apparent structure (1 SPURIOUS
  violation each). AM holds on the colimit (0 violations). AM is an
  event-finality property, repaired by the colimit.

## Success Criteria

1. Colimit: reflexive=True, antisymmetric=True, transitive=True.
2. Observer A apparent order: {e1≤e3, e2≤e4} only — missing (e1,e4).
3. Observer B apparent order: {e1≤e4, e2≤e4} only — missing (e1,e3).
4. Colimit order: {e1≤e3, e1≤e4, e2≤e4} = reference.
5. New orderings in colimit not in S_A: {(e1,e4)}. Not in S_B: {(e1,e3)}.
6. Colimit equals reference: True.
7. AM on A: exactly 1 SPURIOUS at (e1,e4). AM on B: exactly 1 SPURIOUS at (e1,e3).
8. AM on colimit: 0 violations. AM holds.
9. All 4 hypotheses: supported.

## Failure Criteria

1. Colimit antisymmetry violation.
   (Would contradict T47 for PO1-admissible 4-event witness.)

2. Observer A or B already sees the full reference order.
   (Would mean the restriction was not applied or has no effect.)

3. Colimit ≠ reference (colimit is incomplete).
   (Would mean two complementary observers are insufficient — a third is needed.)

4. AM holds on both apparent structures (no SPURIOUS violations).
   (Would mean phantom incomparabilities don't break AM locally —
   the new phenomenon doesn't occur at this witness.)

5. AM fails on colimit.
   (Would mean a new and stronger result: even event-finality AM can fail.
   This would require investigating why the axis profiles fail to track
   the colimit's record order — a potential T53 target.)

## Known Constraints

- 4 events, 8 D1 systems, 2 observers. Both observers see all 4 events
  (same event set, different record bases). The restriction affects only
  source system record bases (U systems), not target (O).

- The "AM-repaired-by-colimit" phenomenon is specific to this witness:
  the axis profiles were designed to match the full event-finality order.
  A witness with axis profiles mismatched to the reference order would
  break AM even at the colimit level. This is the T50 counterexample
  problem lifted to the multi-observer setting.

- Colimit associativity (colimit of colimits = full colimit) is not tested
  here (only 2 observers). T53 would add a 3rd observer with a complementary
  restriction and test whether (S_A ⊔ S_B) ⊔ S_C = S_A ⊔ S_B ⊔ S_C.

## Connection to Prior Results

- T51: T51 showed the asymmetric case (A has full access, B is bounded).
  T52 lifts this to the symmetric case — both observers are bounded, and
  the colimit is genuinely new relative to both. The "AM-repaired" phenomenon
  is new: T51 observers both had correct local AM; T52 observers do not.

- T50: AM is a condition on the full record basis. T52 shows this explicitly:
  a restricted record basis breaks AM locally (phantom incomparabilities
  appear as spurious magnitude-order pairs). The colimit restores the full
  record basis and therefore restores AM.

- T47: Guarantees colimit consistency. T52 is the first test of T47's
  acyclicity guarantee in a genuinely multi-observer 4-event setting.
