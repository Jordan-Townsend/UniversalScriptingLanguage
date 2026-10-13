# Follow-through decisions

```mermaid
flowchart TD
  A[Catalog ID and task intent] --> B{Exact specification, dialect and category audited?}
  B -- No --> C[Retrieve authoritative sources and audit obligations]
  B -- Yes --> D{Compatible native toolchain or format host available?}
  C -- Audit completed --> B
  C -- Reference blocked --> P[Continue independent parser, tooling and library inventory]
  D -- No --> E{Available installable public implementation?}
  E -- Yes --> F[Install pinned upstream tool and record provenance]
  E -- No --> G[Record exact host, license or device dependency]
  G --> P
  F --> H{Real frontend and typed semantic IR support the task?}
  D -- Yes --> H
  H -- No --> I[Implement missing grammar, types, effects and runtime behavior by family]
  I --> H
  H -- Yes --> J{Exact source, spec, runtime, dependency and platform identity matches artifact?}
  J -- Yes --> K[Reuse verified pure translation or compiled artifact]
  J -- No --> L[Recompute artifact and validate integrity]
  K --> M[Fresh original and generated native execution]
  L --> M
  M --> N{Native behavior and independent intent contracts agree?}
  N -- No --> O[Store counterexample, repair implementation, rerun affected checks]
  O --> H
  N -- Yes --> Q{All profile library, ABI, conformance and review gates pass?}
  Q -- No --> R[Keep scoped evidence and outstanding obligations visible]
  Q -- Yes --> S[Qualify this exact versioned profile]
  S --> T[Package, clean-extract, test and verify remote hashes]
  R --> T
  P --> R
```

Every catalog ID retains its own obligations. Family sharing reduces compatible
engineering work; it cannot transfer an unproved semantic guarantee. A blocked
native host does not block independent source/grammar/specification work.

The executable `followthrough.usl` runs the available branch: plan all 606 entries,
benchmark actual typed Python-to-JavaScript translation and fresh executions,
invoke existing native success-collapse, verify N/M factored integer work and
H0/H1/H2 updates, then losslessly collapse all evidence available before that
step into verified CAS. Final summary fields are stored separately to avoid
self-reference. 604 entries still lack typed source-translation profiles;
non-executable formats require category-appropriate processing contracts.

Optimization decisions are calibrated before the new heldout workload. Use
measured CPU time, wall time, and cache bytes; select minimum declared cost and
record Pareto alternatives. If parallel or factored execution is slower, retain
the sequential route. Exact artifacts may be reused; execution evidence and
external side effects are never replayed from a cache.

All available equation records are inventoried. Scheduling, exactness, cost,
fairness, compression, work avoidance and partial-update mechanisms are applied
to measured data. Amdahl is an explicitly optimistic bound. Physics, quantum,
finance and other models require their own measured inputs and appropriate tasks;
registry default numbers are not workload measurements.
