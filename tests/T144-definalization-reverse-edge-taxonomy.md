# T144: Definalization Reverse-Edge Taxonomy

## Route

Thermodynamic arrow of time.

## Question

After T141 and T142, what exactly counts as a reverse edge for a finalized
record, and which reverse-edge classes are physical-arrow candidates versus
ordinary access, erasure, or governance moves?

## Motivation

The current H7 bottleneck is no longer "find any strict D1 decrease." The
blocking issue is that different kinds of "undo" were still too easy to blur:

- an observer can lose access while the record still exists;
- a support copy can be erased while the source remains;
- a record can be blindly reset or reversibly uncomputed; and
- a record can remain intact while reconstruction authority or provenance
  validity is revoked.

Without a reverse-edge taxonomy, future H7 witnesses can overclaim by calling
all of these definalization.

## Setup

Define four reverse-edge classes for record-finality audits:

1. `boundary_access_loss`
   Observer access, read rights, or causal reachability are reduced while the
   underlying record support remains.
2. `support_copy_removal`
   One support copy or branch-robustness contribution is removed while another
   authoritative source copy remains.
3. `physical_record_deletion`
   The record-bearing physical support itself is deleted, overwritten, or reset,
   either by correlated reversible uncopy or by blind erasure/free-energy cost.
4. `authority_or_provenance_loss`
   The record remains materially present, but certification, trust-domain
   separation, signing ancestry, or reconstruction authority is invalidated.

For each class, ask:

- what remains physically present;
- what D1 dimensions can change;
- whether the reverse is boundary, resource, thermodynamic, or governance;
- and whether the class can support an H7 physical-arrow reading.

## Success Criteria

- The artifact makes reverse-edge class a required declaration for future H7
  witnesses.
- It states clearly that not every D1 decrease is a thermodynamic or physical
  definalization.
- It isolates the only class that could plausibly support a physical-arrow
  reading: substrate-native physical record deletion whose reverse remains
  impossible after full absorber accounting.
- It leaves H7 weaker if all current witnesses fall into non-arrow classes.

## Failure Criteria

- Treating access revocation as record destruction.
- Treating support-copy removal as equivalent to deleting the full record.
- Treating governance or provenance invalidation as thermodynamic irreversibility.
- Treating ordinary erasure cost as constructor impossibility.

## Claim Impact

H7 is sharpened and narrowed again:

```text
Future H7 witnesses must name the reverse-edge class they block. Boundary
access loss, support-copy removal, and authority/provenance loss do not by
themselves support a physical arrow. Physical-arrow pressure can come only
from a substrate-native record-deletion reverse that remains impossible after
reversible-control, erasure, capacity, sink, and provenance accounting.
```

## Contribution Needed

Either:

1. exhibit a physically typed record substrate where a `physical_record_deletion`
   reverse is constructor-impossible under full accounting; or
2. keep H7 at the level of resource-accounting, access-boundary, or governance
   bookkeeping rather than arrow derivation.
