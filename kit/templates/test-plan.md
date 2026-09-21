# Firmware test plan

## Document control

- Project:
- Revision:
- Target MCU / board:
- Firmware revision:
- Test owner:
- Reviewers:
- Date:

## Test levels

| Level | Purpose | Environment | Evidence | Gate |
|---|---|---|---|---|
| Host unit | Fast behavior and failure-path checks | Native compiler | Test log + revision | Required |
| Static analysis | Defects and suspicious constructs | Pinned analyzer | Analyzer report | Required |
| Firmware build | Target compile/link/package | ARM toolchain | Map, size, checksum | Required |
| HIL | Real buses, timing, reset, and peripherals | Board + fixture | Capture/log/measurement | As applicable |
| Manual inspection | Hardware and interface assumptions | Review session | Signed checklist | Required |

## Entry criteria

- [ ] Requirements and interface versions are available
- [ ] Test build is identified
- [ ] Known blockers are recorded
- [ ] Test hardware and instruments are calibrated/available where applicable

## Test cases

For each case, record:

- ID and linked requirement;
- setup and firmware revision;
- input and expected result;
- observed result;
- artifact path;
- pass/fail/blocked;
- reviewer and date.

## Failure policy

A failed test is not silently converted into a warning. If the test is intentionally blocked, record the missing dependency and owner. If a test is changed, retain the reason and review the impact on existing evidence.

## Exit criteria

- [ ] All required cases are pass or formally dispositioned
- [ ] Failed/blocked cases have owners and next actions
- [ ] CI artifacts are retained
- [ ] Known limitations are included in the release note
- [ ] Reviewer has inspected the final revision, not an earlier local build
