# STM32 Embedded Firmware QA Starter Kit

Version: 0.1.0  
Audience: STM32/C/FreeRTOS projects, students, makers, and small engineering teams.

## What this is

A compact set of project files for making firmware verification repeatable:

1. identify requirements;
2. choose observable verification evidence;
3. run fast host tests;
4. run static analysis and target builds in CI;
5. preserve release evidence with the artifact.

## What this is not

This kit is **not** a certification, flight-readiness approval, safety case, or professional engineering sign-off. It does not decide whether a product is safe. Adapt it to the actual board, MCU, interfaces, threat model, requirements, and standards that govern your project.

## Suggested adoption sequence

### Day 1 — inventory

Copy the checklist and record target MCU, board revision, compiler, RTOS, build system, and external interfaces.

### Day 2 — trace

Copy `templates/requirements-traceability.csv`. Add one row for every requirement that matters to behavior, recovery, power, communication, or data integrity.

### Day 3 — test

Copy `templates/test-plan.md`. Separate host tests, hardware tests, HIL tests, and manual inspections. Do not label a test "verified" until an artifact exists.

### Day 4 — gate

Copy `templates/ci-stm32.yml`. Replace the placeholder commands with the commands your repository already uses. Keep the gate loud: missing tools and missing artifacts should fail the job.

### Day 5 — triage

Use `templates/bug-report.yml` for failures. Every report should identify revision, hardware, input, expected behavior, observed behavior, and evidence.

## PocketQube / small-satellite extension

The kit is intentionally broader than PocketQube. For a small-satellite project, add mission-specific sections for power modes, watchdog recovery, communications framing, fault containment, non-volatile memory integrity, and hardware-in-loop evidence. Do not claim space qualification from this starter kit alone.

## License

The files are licensed for one purchasing project or one personal learning project. You may adapt them inside that project. Do not repackage, resell, or publish the bundle as a competing template product.
