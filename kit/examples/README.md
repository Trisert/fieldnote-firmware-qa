# Adapter notes

The CI and templates are intentionally not tied to one repository. Before adopting them, replace the placeholders below.

## Build system

- `make test` → the command that runs native tests and exits non-zero on failure.
- `make cppcheck` → analysis command with the project's real include paths and defines.
- `make release` → target build that emits the release artifact.

## Target details

Record the exact MCU, board revision, clock, linker script, boot policy, non-volatile memory layout, and reset behavior. A checklist cannot compensate for an undocumented hardware boundary.

## Test doubles

Host tests should use small, intentional doubles for HAL and target-only symbols. Do not make the double more permissive than the real interface: a permissive fake can turn a hardware defect into a green host test.

## CI hardening

Pin tools where a version change can alter findings. Retain test logs, analyzer reports, linker maps, binary size, and checksums as artifacts. Make missing artifacts fail loudly.

## Small-satellite extension

For a PocketQube or other small-satellite project, add explicit evidence for power states, reset/recovery, radio framing, non-volatile memory integrity, fault containment, and HIL. Treat missing ICDs as blockers rather than filling gaps with invented assumptions.
