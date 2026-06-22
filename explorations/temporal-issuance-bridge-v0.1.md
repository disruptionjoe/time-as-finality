# Temporal Issuance Bridge v0.1

## Status

Exploration and bridge note. This is not a TaF claim promotion, not a merge of
the `temporal-issuance` and `time-as-finality` ledgers, and not evidence for a
new physical arrow.

External source checked: `disruptionjoe/temporal-issuance` at commit
`02c86cfb0386038fd528061266023ab3536be242`.

## Why This Exists

The Temporal Issuance repo frames the source intuition differently from this
repo. TaF has often asked whether records, stabilization, and finality can
reconstruct or induce temporal direction. Temporal Issuance asks whether a
deeper local process of constraint realization is what makes records and
observer histories possible.

That suggests a serious directional correction:

```text
not: records/finality -> physical arrow
but: issuance/realization order -> observer records -> finality readout
```

If this correction is right, some TaF attempts are backwards when interpreted
as source-level physics. The current H7 demotions are not failures to defend;
they are evidence that record-finality should be treated as an observer-facing
certificate or projection, not as the primitive generator of the arrow.

## Bridge Object

Use the Temporal Issuance seed object as source-side structure:

```text
Y_TI = (
  R,       realized events / constraints
  <,       realization-dependency order
  mu,      issuance measure
  dR,      local frontier or boundary, if it survives relativity
  O_i,     observer sites
  kappa_i, local record cadence
  A_i,     access relation
  G        gluing / reconciliation rules
)
```

Use TaF as observer-facing projection:

```text
pi_TaF(Y_TI, O_i) =
  finite record graph / D1 profiles / FinaliEvents /
  observer colimits / reconstruction and capability data
```

The bridge question is then a projection-sufficiency question:

```text
Does pi_TaF preserve the capability object needed for temporal reconstruction,
record reconciliation, or future-operation availability?
```

The source question is different:

```text
Can < and mu be typed without ordinary time, entropy, record finality, or a
preferred global frontier doing the real work?
```

## Current Best Reconciliation

TaF should remain the audit language for observer-side finality. Temporal
Issuance, if it survives, is a candidate source language for the process whose
observer shadows appear as records, finality, and temporal reconstruction.

The corrected relation is:

```text
Temporal Issuance supplies candidate source dynamics.
Time as Finality supplies observer-indexed readout and falsification tests.
Capability Projection asks what the readout preserves or loses.
```

This preserves the useful TaF work without making finality carry too much
source-level burden.

## What This Changes

H7 should not be pursued as:

```text
finality alone derives the thermodynamic or physical arrow
```

That reading is already demoted by T80, T82, T84, T106, T110, T116, T122,
T124, T141, T142, T145, T148, T152, T160, and T168.

H7 becomes more useful as:

```text
finality is a monotone observer-readable certificate of a source-side
realization order, when the record channel is sound and the absorber variables
are matched
```

That is a weaker claim, but it is better typed and less backwards.

## What This Does Not Change

- C1 remains weakened: record frontiers can reconstruct finite
  observer-relative partial orders under conditions, but this does not prove
  physical time or phenomenal time.
- H7 remains `weakened_conditional`: finality-induced direction is a
  constructor/resource-accounting theorem unless a source-side physical model
  earns more.
- Temporal Issuance is not imported as true. It is a candidate source object
  with strong absorber threats.
- The two repos should not merge claim ledgers.

## Absorber Threats

Temporal Issuance is killed or absorbed for TaF purposes if:

1. The realization order `<` is just causal order with new vocabulary.
2. The issuance measure `mu` is just entropy, action, volume, information,
   probability mass, or another standard monotone.
3. The frontier `dR` requires a preferred global foliation.
4. The observer cadence `kappa_i` smuggles in ordinary time.
5. Records are required to define issuance, making the source/readout relation
   circular.
6. The full bridge factors through existing causal-set, block-universe,
   thermodynamic-arrow, information-theoretic, or TaF record-reconstruction
   machinery with no residue.

## Candidate Theorem Shape

Let `Y_TI` be a local issuance system with a realization-dependency order `<`
and observers `(O_i, kappa_i, A_i)`. Let `pi_TaF` generate record-finality data
from observer-accessible realized constraints.

A useful theorem would not say that records create the arrow. It would say:

```text
Under sound record generation, monotone local realization, and declared
observer access/cadence rules, the TaF finality preorder is a reflection or
projection of the source realization order, up to the declared observer
equivalence and gluing data.
```

Failure of this theorem is also valuable. It would show whether TaF finality
tracks issuance, loses issuance-relevant capability, or adds only ordinary
record-accounting structure.

## Minimal Executable Next Test

T172 now supplies the first finite `issuance_to_finality` bridge model with:

1. A source realization DAG of constraints.
2. A local issuance measure candidate `mu`.
3. Two observer cadences `kappa_i`.
4. Access relations `A_i`.
5. A record-generation rule from realized constraints to TaF records.
6. A gluing rule `G` for reconciling observer-local records.

Required fixtures:

- same issuance, different cadence: different apparent finality without
  changing source order;
- same observer records, different hidden issuance: tests whether TaF loses
  source capability;
- same issuance and records, different `mu`: tests whether the measure is
  decorative;
- nonmonotone access loss: tests whether finality readout is observer-boundary
  rather than source-arrow;
- gluing failure: tests whether global structure is reconstructed, not
  assumed.

## T172 Executable Result

[T172](../tests/T172-issuance-to-finality-bridge.md) implements the bridge as a
projection-sufficiency audit. The positive control shows that a sound observer
record chain can reflect visible source order. The hostile controls are more
important: same TaF readout can hide hidden source order or `mu` data, cadence
and access can change apparent finality without changing source order, and
unglued local records do not determine global source order.

This weakens the bridge rather than promoting it. TaF finality is currently a
candidate observer-side certificate or projection of source realization order,
not a source-level generator of the arrow.

## Claim Ledger Update

No claim should be promoted.

Recommended stance:

```text
H7 remains weakened_conditional. Temporal Issuance suggests that TaF's
physical-arrow attempts are backwards if read as source dynamics. Recast H7 as
an observer-readout/factorization test: finality may certify or project a
source-side realization order, but finality alone has not derived that order.
```

## Suggested Next

Run an absorber map before adding richer bridge models. If Temporal Issuance
collapses into causal order, entropy, information growth, ordinary record
reconstruction, or a hidden global frontier, record absorption rather than
preserving the bridge.
