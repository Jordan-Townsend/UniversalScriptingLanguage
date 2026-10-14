# Conditional USL project schedule

This is an editable budget model, not an empirically calibrated completion forecast.

The snapshot has **244/606 scoped IDs**, **362 without a scoped profile**, **0 full standards**, and **0/21 completed entity tracks**. Existing scopes do not close whole-language obligations.

All 606 IDs have 15 generic prerequisite steps and 18 obligation dimensions. Exact version/dialect/library audits remain open; these templates are not completed normative audits.

## Conditional engineering budgets

Assumed 32 productive hours per lane per week. A lane is effective engineering capacity, not a virtual worker, CPU, or promise of autonomous work. Numbers below are hypothetical list schedules, with no host/license waits or newly discovered requirements. Cases are workload stress tests; none is a probability interval or asserted best/worst bound.

| Milestone | Budget case | Engineering hours | 1 lane | 20 lanes | 100 lanes |
|---|---|---:|---:|---:|---:|
| remaining_scoped_profiles | lean | 2,088 | 65 weeks | 4 weeks | 2 weeks |
| remaining_scoped_profiles | reference | 8,352 | 5.0 years | 15 weeks | 6 weeks |
| remaining_scoped_profiles | large | 33,408 | 20.1 years | 61 weeks | 24 weeks |
| full_pinned_profiles | lean | 138,320 | 83.1 years | 4.2 years | 52 weeks |
| full_pinned_profiles | reference | 553,280 | 332.5 years | 16.6 years | 4.0 years |
| full_pinned_profiles | large | 2,213,120 | 1330.0 years | 66.5 years | 16.1 years |

A full-profile budget includes the remaining whole-standard work for every original ID, including IDs with bounded scopes. Do not add the scoped milestone to that budget. Formats, logs and templates need their category-specific processing contract; many are not executable programming languages.

Shared family-core work is budgeted once. Per-ID semantics, independent tests and qualification remain separate. The proposed family reuse and hour allocations are assumptions, not proven compatible semantic artifacts or measured velocity.

## Why no committed full-project finish date

Full pinned-version language support has no measured completion rate yet. Nine IDs carry external host/license records; applicability still needs audit. The complete entity objective also has unbounded research/acceptance questions and unprovided devices/models. All 21 track next actions and dependencies remain in ENTITY_TRACKS.json. External waits and entity effort are unknown, not zero.

Universal termination/equivalence proofs for arbitrary programs cannot be guaranteed. Intent proof requires a formal contract and a supported proof domain; other cases must report unknown. Human-equivalent abilities and open-ended future learning do not currently define a finite, testable finish gate. These limitations keep the original whole-project ETA null.

## Partial workers and resource recovery

All 10,926 ID/dimension actors may be live concurrently, while physical jobs use measured resource admission. The existing qualification run coalesced 60 ID checks into 32 process jobs, preserved every ID's fresh checks, and built 414 exact pure artifacts for 10,926 logical requests. These figures do not measure compiler engineering productivity.

Overhead recovery: speedup = (1 + overhead/useful_work) / (1 + remaining_overhead/useful_work). Recovering half of 20% overhead gives 1.091×, not extra hardware. A hypothetical 5× speedup for 60% of engineering work gives 1.923× overall under Amdahl. Future skills and hosts receive no guaranteed credit before measurement.

Hardware discovery is read-only for this run. Registered remote capacity is counted only with explicit authorization, compatible workload support, and qualification evidence. There is no automatic network scan, paid allocation, or assumption that interacting with a device grants access to its resources.

## Fastest evidence-based route

1. Pin each ID's specification/version/category and convert the 15 template steps into actual chapter/feature/library obligations. Start license/platform requests alongside independent implementation work.
2. Maintain all logical workers, share exact pure artifacts by complete identity, and admit native jobs using live CPU/memory/I/O measurements. Never merge distinct program effects or replay execution evidence.
3. Build the shared IR and compatible family cores once, then implement per-ID deviations, native hosts, libraries, interop and independently authored intent contracts.
4. Qualify bounded profiles while full conformance remains open. Record active engineering hours, integration/review/rework and feature throughput for representative complex and simple IDs.
5. Replace every assumed hour budget with those observations. Compare sequential, parallel and collapsed routes end to end; promote improvements only after heldout correctness and cost checks. Report a calibrated forecast only when the audited scope and observed rate support it.

## Run

```bash
source /workspace/.onboarding/activate-usl.sh
python planner.py --source-root /workspace/usl-v4.10.0-clean-test --scoped-receipt semantic-final/brainfuck/qualification.json --output results
python -m unittest -v test_planner test_semantics
```

Elsewhere, supply the extracted v4.10 runtime with its dependencies installed. No native compilation is repeated or claimed by this planning addon. See assumptions.json, FAMILY_PLAN.csv, ALL_606_STEPS.json, capacity.json and results.json. The original snapshot files' SHA-256 identities are retained in inputs/provenance.json.
