# Temporal Issuance Source Object Spec

## Status

Reopen burden and source-object specification for the Temporal Issuance bridge.
This is not H7 evidence, not a causal-set claim, not a thermodynamic-arrow
derivation, and not a physical-time replacement.

## Route

Thermodynamic arrow of time / Time as Finality source-readout bridge.

## Why This Exists

T172 showed that an observer-side TaF readout can reflect a visible source
order in a positive control, but it can also lose hidden source order, lose
`mu`, change apparent finality under cadence variation, change support under
access loss, and fail to determine global order without gluing data. N13 then
mapped those lost fields to mature absorbers: causal order, causal-set
dynamics, stochastic thermodynamics, information theory, instrumentation, and
TaF reconstruction.

The next useful move is therefore not a richer issuance model. It is a source
object contract. If the contract maps every field to a known absorber, the
Temporal Issuance bridge is translation residue until a new nonabsorbed source
primitive is supplied.

## Current Strongest Claim

Temporal Issuance currently survives only as a stress test for whether TaF
finality is a sound observer-side readout of a separately typed source
process:

```text
source realization process -> observer records -> finality readout
```

The repo has not earned:

```text
finality -> source arrow
```

or:

```text
issuance vocabulary -> new physical arrow
```

## Minimal Source Object

A Temporal Issuance proposal must freeze:

```text
Y_TI = (
  R,        realized events, constraints, or source tokens
  <,        source precedence or dependency relation
  mu,       source measure
  dR,       local frontier, boundary, or access cut
  O_i,      observer worldlines, sites, or interfaces
  kappa_i, observer cadence or sampling map
  A_i,      observer access relation
  M,        source-to-record generation map
  G         identity, overlap, and gluing data
)
```

The proposal must also declare:

```text
pi_TaF : Y_TI -> X_TaF
Cap_TI : Y_TI -> K_TI
R_K_TI  native comparison on K_TI
```

`Cap_TI` cannot be merely "recover the hidden issuance variable." It must be a
task-natural capability, such as source-order certification, record-channel
calibration, future-operation availability, or reconstruction reliability
under declared observer access and gluing.

## Field Absorber Table

| Field | Required typing before use | Default absorber status |
| --- | --- | --- |
| `R` | Event, constraint, token, or state ontology; admissible realizations. | Absorbed by ordinary event/state modeling unless it adds a nonabsorbed physical primitive. |
| `<` | Partial order, causal order, dependency order, or label order; invariance under relabeling. | Absorbed by relativistic causal order or causal-set order if causal; null if it is only a hidden birth label or preferred global sequence. |
| `mu` | Units, domain, comparison rule, additivity or monotonicity, and transformation behavior. | Absorbed by volume/counting, entropy production, work, heat, free energy, path probability, Shannon information, statistical complexity, or record counting unless a matched-data split survives. |
| `dR` | Local boundary/frontier object; covariance or label invariance; no hidden global present. | Absorbed by Cauchy surfaces, causal diamonds, domains of dependence, horizons, causal-set stems/past sets, or observer access cuts. |
| `O_i` | Observer worldline/site/interface plus physical access limits. | Absorbed by relativity, instrumentation, and TaF observer/access profiles. |
| `kappa_i` | Sampling map, clock relation, cadence, or bandwidth with operational units. | Absorbed by proper time, detector sampling, synchronization protocol, or channel bandwidth unless source-side status is independently typed. |
| `A_i` | Access relation over source tokens and records; boundary changes distinguished from source changes. | Absorbed by causal accessibility, detector coupling, observer boundary, or record-channel policy. |
| `M` | Source-to-record generation rule, independent of finality definitions. | Circular if records or finality define issuance; otherwise absorbed by measurement, instrumentation, provenance, or TaF record-generation machinery. |
| `G` | Identity, overlap, consistency, and reconciliation data for local records. | Absorbed by TaF colimit/descent machinery, causal-set reconstruction gates, or ordinary database/distributed-system gluing unless residue remains after those data are matched. |

## Same-Neighbor-Data Freeze

Before claiming Temporal Issuance residue, compare only source systems with the
following vector fixed or explicitly declared irrelevant:

```text
causal order
spacetime or causal-set volume/counting data
observer worldlines and access regions
detector sampling/cadence
thermodynamic path, reservoir, work, heat, and free-energy ledgers
information state, compression, and statistical-complexity ledgers
record-generation rule
identity, overlap, and gluing data
gauge, label, basis, and foliation convention
```

If the candidate pair differs in any field above, the split belongs to the
neighboring absorber unless the proposal explains why that field is not
legitimate same-neighbor data.

## Source-Spec Collapse Lemma

For a declared `Y_TI`, `pi_TaF`, and `Cap_TI`, if every component of `Cap_TI`
is a function of the same-neighbor-data freeze vector plus TaF gluing data, then
Temporal Issuance contributes no independent source-side capability residue.

Equivalently, after granting the absorber vector:

```text
pi_TaF(y1) ~=_X pi_TaF(y2)
and absorber_vector(y1) = absorber_vector(y2)
  => Cap_TI(y1) R_K_TI Cap_TI(y2)
```

unless a new source primitive is named. This is not a novel theorem. It is the
fiber-constancy discipline applied to the bridge, and it prevents hidden
issuance labels from being counted as evidence.

## Non-null Reopen Burden

Temporal Issuance becomes live again only if a future artifact supplies all of
the following before modeling:

1. A non-circular source primitive or relation in `Y_TI` that is not reducible
   to causal order, volume/counting, thermodynamic ledgers, information state,
   instrumentation, or TaF gluing.
2. Units, invariance or covariance behavior, operational comparison, and
   admissible transformations for that primitive.
3. A task-natural `Cap_TI` and native comparison `R_K_TI` declared before the
   witness pair is selected.
4. A positive preservation control showing that `pi_TaF` can preserve the
   declared capability when the record channel is sound.
5. A hostile same-neighbor-data split where the absorber vector is matched but
   `Cap_TI` still differs.
6. A demotion rule naming which absorber field would collapse the proposal.

Without all six, richer issuance models are decorative.

## Null Outcomes

Treat the bridge as translation residue if:

- `<` is causal order, causal-set order, dependency bookkeeping, or birth-label
  order without a label-invariant observable;
- `mu` is volume, count, entropy, free energy, work, path probability,
  information, statistical complexity, action-like bookkeeping, or record
  count with no matched-data split;
- `dR` requires a preferred global frontier;
- `kappa_i` is observer proper time, detector cadence, synchronization, or
  bandwidth;
- `A_i` is ordinary causal access, detector coupling, or boundary policy;
- `M` defines issuance through records, stabilized finality, or reconstruction
  success;
- `G` is ordinary TaF descent, identity/overlap bookkeeping, or causal-set
  reconstruction; or
- the alleged split disappears after the same-neighbor-data freeze.

## Decision Rule

No new Temporal Issuance toy model should be treated as H7 progress until this
file's source-object contract is filled by a nonabsorbed primitive and a
matched-data hostile split.

If no such primitive is named, close the bridge as translation residue for H7
and keep it only as a useful stress test for source/readout discipline.

## What This Improves

- Converts the post-T172/N13 blocker into a checkable source-object contract.
- Prevents hidden birth order, cadence, access, or gluing data from being
  smuggled in as new arrow evidence.
- Makes the bridge easier for a serious causal-set, thermodynamics,
  information, or instrumentation reviewer to reject or repair.

## What This Weakens

This weakens Temporal Issuance as an open-ended route for H7. Under the current
field list, every declared source component is absorber-owned by default. The
branch needs a new non-circular source primitive or it should stop consuming
model-building effort.

## Claim Ledger Update

H7 remains `weakened_conditional`. Temporal Issuance is not current H7
evidence. The source-object specification maps all currently declared fields
of `Y_TI` to existing absorber families by default; the bridge reopens only
with a nonabsorbed source primitive, a task-natural capability object, and a
hostile same-neighbor-data split after causal, thermodynamic, information,
instrumentation, access, cadence, and gluing variables are matched.

## GU/TI/TaF Reciprocal Bridge Note

The 2026-06-24 reciprocal bridge review is preserved in
`gu-ti-taf-reciprocal-bridge-contract.md`.

This source-object spec remains the local TaF authority. The new bridge note
adds three routing constraints for future Temporal Issuance imports:

1. Fill a GU-style six-axis table before modeling any physical-source claim.
2. Separate observer-domain colimits from source or record filtrations; do not
   identify TaF colimits with GU/TI filtered sheaf colimits without a typed
   double diagram.
3. Treat `lambda_max` absorption claims as conditional until access windows,
   cadence/resource clocks, queue/frontier behavior, and gluing data are
   explicitly typed.
