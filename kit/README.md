# Fieldnote Release QA Starter Kit

Version: 0.1.0  
Audience: small teams shipping hardware, firmware, software, or other technical products. The current adapter uses embedded-project examples.

## What this is

A compact set of project files for making verification and release evidence repeatable:

1. identify requirements;
2. choose observable verification evidence;
3. run fast host tests;
4. run tests, analysis, and builds in CI;
5. preserve release evidence with the artifact.

## What this is not

This kit is **not** a certification, regulated sign-off, safety case, or professional engineering approval. It does not decide whether a product is safe. Adapt it to the actual product, interfaces, threat model, requirements, and standards that govern your project.

## Suggested adoption sequence

### Day 1 — inventory

Copy the checklist and record the product boundary, revision, toolchain, build system, test levels, and external interfaces.

### Day 2 — trace

Copy `templates/requirements-traceability.csv`. Add one row for every requirement that matters to behavior, recovery, power, communication, or data integrity.

### Day 3 — test

Copy `templates/test-plan.md`. Separate host tests, hardware tests, HIL tests, and manual inspections. Do not label a test "verified" until an artifact exists.

### Day 4 — gate

Copy `templates/ci-stm32.yml`. Replace the placeholder commands with the commands your repository already uses. For non-embedded projects, rename the adapter and keep the same evidence gates.

### Day 5 — triage

Use `templates/bug-report.yml` for failures. Every report should identify revision, hardware, input, expected behavior, observed behavior, and evidence.

## Adapting the current example

The included examples lean embedded because that is the first concrete adapter. For a software-only project, replace hardware-in-loop with integration or system tests. For a hardware product, keep the physical test and artifact trail. Do not claim domain qualification from this starter kit alone.

## License

The files are licensed for one purchasing project or one personal learning project. You may adapt them inside that project. Do not repackage, resell, or publish the bundle as a competing template product.
