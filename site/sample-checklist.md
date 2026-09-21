# Free sample — Release QA checklist

Use this as a first-pass review for a small technical product. It is deliberately short; the full starter kit adds traceability, test planning, CI, and release-evidence templates. The included examples lean embedded, but the loop applies to any team that needs to show how a release was checked.

## Scope and ownership

- [ ] The product boundary, revision, toolchain, build system, and test environment are recorded.
- [ ] The project states what is **not** covered by this checklist.
- [ ] Every safety-, power-, communication-, and recovery-critical requirement has an owner.

## Build and reproducibility

- [ ] A clean checkout can build without an engineer's private machine state.
- [ ] Compiler, linker, SDK/HAL, and submodule versions are pinned or documented.
- [ ] The release artifact is generated from CI, not copied from a developer workstation.

## Tests and failure handling

- [ ] Host tests cover normal behavior and at least one failure path per critical module.
- [ ] Critical failure, recovery, and degraded-mode behavior are deliberate.
- [ ] Hardware-dependent tests are labelled separately from host tests.
- [ ] A failed test produces actionable evidence: log, input, expected result, and revision.

## Static analysis and review

- [ ] Static analysis runs on first-party code with the same include paths as the build.
- [ ] Warnings are either fixed or documented with a narrowly scoped rationale.
- [ ] A release review checks the diff, generated artifacts, and test report together.

## Boundary

This sample is a process aid. It is **not certification, regulated approval, or a substitute for a qualified engineering review**.
