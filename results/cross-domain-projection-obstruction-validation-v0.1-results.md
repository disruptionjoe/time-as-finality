# Cross-Domain Projection-Obstruction Validation v0.1 Results

## Commands

```bash
python -m models.run_t30
python -m unittest tests.test_cross_domain_projection_obstruction_validation -v
```

## Verdict

T30 provides hostile cross-domain evidence for PO1.

Best supported hypothesis:

```text
H1 with H3/H4 constraints
```

PO1 recommendation:

```text
Keep PO1 partially_supported, but constrain it.
```

## Case Classification

| Domain | Case | Classification | PO1 support |
| --- | --- | --- | --- |
| Git merge conflict | `git_semantic_merge` | projection-created obstruction | yes |
| Database schema migration | `database_expand_contract` | lossy projection without obstruction | no |
| Access-control policy inheritance | `access_control_inheritance` | shared obstruction | no |
| Type systems and macro expansion | `type_system_macro_expansion` | non-definable projection | no |

## Hypothesis Verdicts

| Hypothesis | Status |
| --- | --- |
| H0 | rejected in finite scope |
| H1 | supported |
| H2 | not yet supported |
| H3 | partially supported |
| H4 | partially supported as warning |

## Admissibility Constraints

Future PO1 evidence should require:

- projection independently motivated by the domain;
- richer system has a global section;
- restricted system is obstructed;
- forgotten structure resolves the restricted obstruction;
- lossy projection without obstruction is excluded;
- shared obstruction is excluded;
- non-definable projection is treated as a boundary.

## Non-Claims

T30 does not prove PO1 is universal.

T30 does not prove external theorems about Git, databases, access-control
systems, or type systems.

T30 does not promote PO1 beyond `partially_supported`.
