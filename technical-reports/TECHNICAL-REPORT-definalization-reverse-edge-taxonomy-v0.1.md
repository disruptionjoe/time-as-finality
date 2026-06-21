# Technical Report: Definalization Reverse-Edge Taxonomy v0.1

## Claim Under Test

T141 and T142 left H7 with a sharper blocker than "find a strict D1 decrease."
The real blocker is semantic and physical:

```text
which reverse edge is actually being claimed impossible?
```

If access loss, support-copy erasure, physical deletion, and
authority/provenance invalidation are treated as one thing, H7 can appear
stronger than it is.

## Artifact

T144 introduces a four-way reverse-edge taxonomy for H7 audits:

| Reverse-edge class | What changes | What stays | Default absorber |
| --- | --- | --- | --- |
| `boundary_access_loss` | observer access or causal reachability | record support still exists | boundary/accounting |
| `support_copy_removal` | one redundancy or branch-support copy | source or other support copies remain | resource or reversible uncopy |
| `physical_record_deletion` | record-bearing support itself | no identical support copy assumed | reversible control or ordinary erasure/free-energy accounting |
| `authority_or_provenance_loss` | certification, trust, or reconstruction rights | physical marks may remain | governance/provenance accounting |

The taxonomy does not solve H7. It prevents future H7 work from hiding behind
an ambiguous "definalization" label.

## Result

The current H7 witness stack occupies only non-upgrading classes.

### 1. Boundary Access Loss

This is not physical record destruction. It is the reverse of the T141 access
grant case. The observer loses access, but the record can remain fully present
for another observer or in the substrate itself.

This can change D1, but it is a boundary change, not arrow evidence.

### 2. Support-Copy Removal

This covers redundancy and branch-robustness decreases when a copied support
record is removed but another source copy remains. T141 and T142 already show
that this splits into ordinary cases:

- correlated reversible uncopy if the source-copy handle is retained;
- blind erase or overwrite if that handle is unavailable.

So support-copy removal is not constructor impossibility. It is resource or
control accounting.

### 3. Physical Record Deletion

This is the only reverse-edge class with any realistic H7 physical-arrow
upside. But current evidence still fails to promote it. T142 already absorbs
the present T1 examples:

- with full reversible handle, deletion becomes uncopy;
- without it, deletion becomes ordinary erasure/free-energy accounting.

So the current repo still lacks a physically typed record substrate where
record deletion remains impossible after full absorber accounting.

### 4. Authority Or Provenance Loss

A record can remain physically present while losing reconstruction authority,
certification, or admissible provenance. That matters for Q1B-style evidence
discipline and may matter for future capability, but it is not thermodynamic
irreversibility.

This class should never be silently promoted into H7 physical-arrow language.

## Current Strongest Claim

H7 is best read as a reverse-edge audit discipline:

```text
before treating a finality increase as arrow-bearing, state which reverse edge
is blocked and show that the block survives the correct absorber for that
class.
```

Under T144, only the `physical_record_deletion` class could possibly support a
future physical-arrow reading, and no current witness clears that bar.

## What This Improved

T144 improves the program in three ways.

First, it makes H7 more falsifiable. A future witness must now declare what
"undo" means before claiming directional content.

Second, it blocks a known failure mode: inflating observer access changes,
support-copy changes, or provenance invalidation into physical irreversibility.

Third, it links the repo's existing negative results into one discipline:

- T141 handles boundary versus copy/erase on the T1 substrate;
- T142 calibrates copy/erase against reversible control and ordinary erasure;
- T144 says governance/provenance loss is a different reverse-edge class again.

## What This Weakened Or Falsified

T144 weakens any residual H7 reading that still says "definalization" without
typing the reverse edge.

More concretely, it falsifies the sloppy inference:

```text
D1 decreased
=> a physically irreversible record was destroyed
=> H7 gained arrow evidence
```

That chain is no longer admissible. The reverse-edge class must be stated and
audited first.

## Falsification Condition

T144 fails in H7's favor only if a future witness shows that one of the
currently non-upgrading classes was misclassified, or if a physically typed
`physical_record_deletion` case survives all of the following while still
blocking the reverse:

- reversible source-copy control;
- ordinary blind erasure/free-energy accounting;
- sink/capacity bookkeeping;
- observer-boundary and access accounting;
- provenance and authority accounting.

## Open Blocker

The repo still lacks a physically typed substrate where record deletion, not
mere access loss or support-copy loss, is impossible for substrate-native
reasons after full absorber accounting.

## Claim Ledger Update

Add T144 to H7:

```text
T144 introduces a reverse-edge taxonomy for H7. Boundary access loss,
support-copy removal, physical record deletion, and authority/provenance loss
must be distinguished. Only physically typed record deletion can support a
future H7 physical-arrow reading, and no current witness clears that bar.
```

## Recommended Next Move

Either:

1. try to build one physically typed `physical_record_deletion` witness at
   fixed free-energy, capacity, sink, boundary, reversible-control, and
   provenance data; or
2. further demote H7's paper-facing language from arrow claim to
   resource-accounting and reverse-edge audit discipline.
