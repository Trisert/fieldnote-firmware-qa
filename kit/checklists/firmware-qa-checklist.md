# Firmware QA checklist

Use one copy per project. Mark an item `done`, `partial`, `blocked`, or `not-applicable`, and link evidence where possible.

## 0. Project boundary

- [ ] Target MCU and exact part number recorded
- [ ] Board revision and hardware baseline recorded
- [ ] Compiler, linker, SDK/HAL, RTOS, and build-system versions recorded
- [ ] Product assumptions and explicit exclusions recorded
- [ ] Applicable standards, customer requirements, and ICDs listed

## 1. Requirements and interfaces

- [ ] Each critical requirement has a unique ID
- [ ] Each requirement has an owner and verification method
- [ ] Input ranges, units, endianness, timeouts, and error semantics are explicit
- [ ] External interfaces have a versioned contract or an explicitly blocked dependency
- [ ] Contradictions are recorded as decisions, not silently resolved in code

## 2. Build reproducibility

- [ ] Clean checkout builds from a documented command
- [ ] Toolchain version is pinned or captured in CI output
- [ ] Generated files are either reproducible or clearly classified as inputs
- [ ] Compiler warnings are visible and triaged
- [ ] Linker map and size report are retained for releases
- [ ] Release artifact has a revision, timestamp policy, and checksum

## 3. C/C++ hygiene

- [ ] First-party code is separated from vendor code in analysis scope
- [ ] Integer widths and signedness are deliberate at boundaries
- [ ] Buffer lengths are checked before copy, parse, or transmit
- [ ] Error returns are handled or explicitly documented as impossible
- [ ] ISR-shared state uses an intentional synchronization strategy
- [ ] Undefined, implementation-defined, and hardware-specific behavior is documented

## 4. RTOS and concurrency

- [ ] Task priorities have a written rationale
- [ ] Stack sizes have margin evidence, not only defaults
- [ ] Mutex ownership and timeout policy are documented
- [ ] ISR-to-task handoff is bounded and tested
- [ ] Queue overflow and task starvation behavior are defined
- [ ] Watchdog coverage includes the tasks that can prevent progress
- [ ] Allocation failure and stack overflow hooks are connected to a safe response

## 5. Power and timing

- [ ] Clock and power modes are documented for each operating state
- [ ] Wake sources and wake-failure behavior are tested
- [ ] Timeout values have a source or measurement
- [ ] Blocking operations are bounded or isolated from critical paths
- [ ] Worst-case message, flash, and sensor timings are recorded

## 6. Data integrity and recovery

- [ ] Persistent records have a version and integrity check
- [ ] Partial writes and interrupted updates are handled
- [ ] Reset reason is captured before it is overwritten
- [ ] Watchdog recovery path is tested, not only logged
- [ ] Corrupt configuration/data has a deterministic fallback
- [ ] Recovery cannot silently turn missing telemetry into a healthy value

## 7. Communications and parsing

- [ ] Frame length, version, and bounds are validated before access
- [ ] CRC/checksum coverage is documented
- [ ] Authentication and replay protection are either implemented or explicitly out of scope
- [ ] Retries, duplicates, timeouts, and out-of-order frames are tested
- [ ] Rejected commands are observable in telemetry/logs
- [ ] Radio/transport failure does not deadlock the main control path

## 8. Verification evidence

- [ ] Host unit tests cover critical normal and failure paths
- [ ] Mutation or fault-injection checks prove important assertions can fail
- [ ] Static analysis runs with real include paths and first-party scope
- [ ] Hardware-in-loop tests are separated from host tests
- [ ] Manual inspection records include revision and reviewer
- [ ] Every release has a test summary and known-limitations section

## 9. Release review

- [ ] Source diff reviewed
- [ ] Configuration and generated artifacts reviewed
- [ ] CI checks passed on the release revision
- [ ] Binary checksum and size recorded
- [ ] Open risks and blocked ICDs listed
- [ ] No placeholder pin, protocol, or safety assumption remains undocumented

## Final status

- Status: `todo | partial | ready-for-review | blocked`
- Revision:
- Reviewer:
- Date:
- Evidence index:
- Known limitations:
