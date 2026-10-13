# Recorded follow-through results

The final `.usl` run passed every measured check. Eight addon regression tests
passed, including cache mutation, changed source/identity, fresh execution on
cache hits, deliberately wrong intent and exact evidence restoration.

| Measurement | Sequential baseline | Selected route |
|---|---:|---:|
| Held-out wall time | 3.4244 s | 1.2725 s |
| Translation artifacts built | 12 | 4 |
| Artifacts reused | 0 | 8 |
| Fresh native executions in held-out batch | 24 | 24 |

The selected route was `parallel_collapse`, with three resource-admitted worker
threads launching real Python/Node native processes. The observed held-out wall
speedup was **2.6911×**, and 66.67% of repeated translation builds were avoided.
This is a small pure integer/list/filter profile; each original and translated
program was also checked against an independent host sum oracle. The complete
benchmark ran **156 fresh native executions** across calibration and holdout.

Three calibration trials per route, with rotating order, selected the lowest
declared measured cost before the four new held-out fixtures were constructed.
The cost is CPU seconds + wall seconds + 0.01 seconds per cache MiB. CPU time
includes reaped native children. The held-out timing is a single comparison pair,
not a confidence interval or a general-language performance guarantee.

The existing success-collapse search freshly tested six USL targets against the
independent sum-of-first-n-odd-integers contract. PHP won the measured search and
passed a new n=53 native case, producing 2809. All probe costs are recorded;
winner latency alone is not the search's end-to-end cost. Those executions are
additional to the 156 translation-benchmark executions.

Factored integer reduction and H0/full, H2/delta and H1/reuse paths all matched
independent integer arithmetic. The adaptive executor selected **serial** for
the 65,536-element bookkeeping workload because the other routes were slower.
Three delta computations still required a full reference audit and fingerprint
scan. Audit/scan costs remain counted; reduced arithmetic is not proof of
end-to-end work avoidance.

Lossless collapse converted 619,352 raw evidence bytes into a 34,610-byte
serialized codec frame: **17.90× compression**, with byte-exact restoration and
exact CAS duplicate reuse. The payload includes plan, benchmark, success search,
numeric audit, equation inventory and supervisor source. Final summary fields
are separate to avoid self-reference. This reduces stored evidence, not pending
semantic implementation work.

All **57 available equation records** were inventoried. Thirteen applicable
mechanisms were used: exact artifact identity/reuse, semantic checks, factoring,
incremental updates, compression, work avoidance, speedup, resource ratios,
fairness, cost minimization and Pareto selection. Amdahl's p=1 calculation is
explicitly an optimistic bound. Physics/quantum/finance and other equations need
appropriate tasks and measured inputs; registry defaults are not measurements.

The v4.5 source and its 669-passed/9-skipped regression evidence remain
unchanged. No new fully qualified language or human sense is claimed by this
optimization addon. Full-objective completion remains false.
