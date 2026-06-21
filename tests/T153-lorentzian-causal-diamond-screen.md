# T153: Lorentzian Causal-Diamond Screen

## Route

Spacetime reconstruction / black holes / causal access.

## Target Claims

- [R1: Relativity And No Global Commit Order](../claims/R1-relativity-no-global-commit-order.md)
- [S1: Spacetime As Consensus Envelope](../claims/S1-spacetime-consensus-envelope.md)
- [B1: Black Holes As Finality-Domain Boundaries](../claims/B1-black-holes-finality-boundaries.md)

## Question

After replacing the T151 causal-access graph proxy with explicit 1+1
Lorentzian causal structure, does any Time as Finality residue remain for
classical record access or reconstructability?

## Motivation

T151 showed that direct classical horizon and boundary language factors
through a declared causal-access graph. B1 then asked for a Lorentzian
causal-diamond or domain-of-dependence version before any stronger claim.

T153 supplies that absorber. It intentionally tries to make R1/S1/B1 collapse
to standard causal pasts, causal diamonds, spacelike separation with common
future reconciliation, and domains of dependence.

## Setup

Use a minimal 1+1 Minkowski model with speed `c = 1`:

```text
p <= q iff q.t - p.t >= |q.x - p.x|
causal diamond D(a,b) = J+(a) intersection J-(b)
future domain of dependence of [-L,L] at t=0:
  event (t,x) is in D+ iff [x-t, x+t] subset [-L,L]
```

The fixtures are:

1. `remote_signal_causal_past`
   A remote emission enters the observer's causal past through a received
   signal. This is record access without direct participation.
2. `spacelike_pair_later_reconciliation`
   Spacelike events have no invariant causal order but can both enter a later
   common future record.
3. `domain_of_dependence_interval`
   One event is determined by an initial interval and one is not. The split is
   exactly domain-of-dependence membership.
4. `same_source_changed_access_diamond`
   The same source record is inaccessible to a narrow collection event and
   accessible to a wider future collection event. The split is changed
   Lorentzian access data.
5. `fixed_lorentzian_data_control`
   With matched event coordinates and access diamond, a record relabel does
   not change the causal-access verdict.

## Success Criteria

- Remote astronomical signals count as causal record access.
- Spacelike events are not given a global order, but later reconciliation is
  allowed inside their common future.
- Reconstructability splits caused by domains of dependence are classified as
  standard Lorentzian absorber content.
- Verdict splits caused by changed access diamonds are not TaF residue.
- Matched Lorentzian causal data produce no finality split in the negative
  control.

## Failure Criteria

- The screen denies ordinary remote observation through received signals.
- Spacelike separation is converted into a hidden global commit order.
- Domain-of-dependence membership is promoted as a new finality mechanism.
- Changed access diamonds are mistaken for same-data residue.
- A claim is promoted without matching causal relation, observer world tube,
  access diamond, record channels, and domain-of-dependence inputs.

## Claim Impact

R1 remains safe as locality discipline:

```text
spacelike events lack invariant causal order but can later reconcile through a
common future record.
```

S1 and B1 are weakened:

```text
if a finality or boundary verdict changes only because causal past, access
diamond, or domain-of-dependence data changed, the result is standard
Lorentzian causal structure, not independent TaF spacetime evidence.
```

## Reproduction

```bash
python -m unittest tests.test_lorentzian_causal_diamond_screen -v
python -m models.run_t153
```
