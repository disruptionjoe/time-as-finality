# T588: Record-Issuance Contract Fork Gate

## Why This Reopens Lane 1

T587 closed with an explicit stop: *"Do not continue producing T-number
scaffolds from T586 alone. Reopen Lane 1 only for a provenance-valid physical
source packet, a frozen capability witness, or a sharper counterexample that
changes the record-issuance contract."*

T588 invokes the third condition. It does not overlay another comparator on the
frozen T586 event system — T587 already showed that class of move is absorbed by
standard dependency and causal comparators. It instead asks a question T586 and
T587 both leave undeclared: **into what does a record get issued?**

Three answers are available and they are not equivalent. One is refutable.

## Construction Fork Declaration

Per the repository's construction-fork discipline: this gate uses the
**standard special-relativistic construction** of proper time as the invariant
arc length along a worldline. It does *not* use a program-native temporal
primitive. The refutation below therefore inherits standard relativity's
empirical support and does not depend on any Time as Finality claim.

## Target Claims

- The record-issuance contract is a distinct, declarable structure, separable
  from both the record-prerequisite filter T587 preserved and from any
  comparator on a frozen event system.
- At least one candidate issuance contract is refutable against existing
  measurement without new physics.

## Setup

A two-observer separation-and-reunion fixture with declared proper times. Both
observers issue records at a shared rate per unit of their own proper time.
Three issuance contracts are evaluated on the same fixture:

- **Contract A — per-observer ledgers.** Each observer issues into its own
  ledger. No global count exists at any time.
- **Contract B — single global ledger.** Observers are objects within one
  ledger carrying one monotone issuance count.
- **Contract C — regional ledgers merging on causal contact.** Each observer
  issues locally; ledger structure reconciles where worldlines meet.

The discriminating observable is the **record count each observer holds at
reunion**.

## Success Criteria

- Each contract yields a determinate reunion count per observer.
- Contract B is refuted: a single monotone global count cannot reproduce
  measured differential ageing while also being what observers read.
- Contracts A and C both reproduce the differential count.
- The refutation of B is invariant under the choice of proper-time ratio — it
  must not depend on the particular fixture numbers.
- The residual A-versus-C discriminator is stated and shown to be *not* settled
  by reunion counts alone.

## Failure Criteria

- Differential ageing is inserted into a contract rather than derived from it.
- The refutation of B depends on the specific proper-time ratio chosen.
- Contracts A and C are distinguished by reunion count, which would mean the
  fixture cannot pose the residual question.
- The gate is used to claim a preferred frame exists, does not exist, or that
  time, temporal order, or issuance has been derived.

## Known Physics Constraints

Differential ageing is taken as an empirical input, not derived: muon lifetime
dilation, CERN storage-ring measurements at γ ≈ 29, Hafele–Keating, and the
continuous relativistic correction required for GPS. The gate uses the
*existence* of differential ageing, not any particular value.

## What This Does Not Claim

T588 does not prove time, temporal order, issuance, a preferred frame's
existence or nonexistence, a universal capability measure, or any cross-repo
truth. It does not revive T586's downgraded order claim. It refutes one declared
bookkeeping contract and leaves two standing.

## Contribution Needed

Run `python -m models.t588_record_issuance_contract_fork_gate --write-results`
before using the result as source-owned input.
