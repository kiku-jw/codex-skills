# {{PROJECT_NAME}} Contracts

## Domain Objects

| Object | Key fields | States | Invariants | Notes |
| --- | --- | --- | --- | --- |
| ExampleObject | `id`, `status` | `pending`, `active` | Replace with real invariant | Replace with real object |

## API / IPC / Event Contracts

### Contract C1

- direction:
- trigger:
- owner:
- used by milestone or task:
- input:
- output:
- failure modes:
- invariants:
- evidence to verify:

### Contract C2

- direction:
- trigger:
- owner:
- used by milestone or task:
- input:
- output:
- failure modes:
- invariants:
- evidence to verify:

## Queue / Job States

| Job | Pending | Running | Completed | Failed | Idempotency | Used by milestone or task |
| --- | --- | --- | --- | --- | --- | --- |
| ExampleJob | waiting for trigger | worker claimed | output persisted | retry or surface error | replace me | |

## External Integrations

- provider:
  - purpose:
  - request shape:
  - response shape:
  - retries / limits:
  - secrets / auth:
  - used by milestone or task:

## Auth / Permissions

- actor:
  - can trigger:
  - server-side checks:
  - rate limits if public-facing:
