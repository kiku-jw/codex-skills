# {{PROJECT_NAME}} Contracts

## Domain objects

| Object | Key fields | States | Invariants | Notes |
| --- | --- | --- | --- | --- |
| ExampleObject | `id`, `status` | `pending`, `active` | Only one active object per user | Replace with real objects |

## API / IPC / event contracts

### Contract C1

- direction:
- trigger:
- owner:
- used by epic/task:
- input:
- output:
- failure modes:
- invariants:
- evidence to verify:

### Contract C2

- direction:
- trigger:
- owner:
- used by epic/task:
- input:
- output:
- failure modes:
- invariants:
- evidence to verify:

## Queue / job states

| Job | Pending | Running | Completed | Failed | Idempotency | Used by epic/task |
| --- | --- | --- | --- | --- | --- | --- |
| ExampleJob | waiting for trigger | worker claimed | output persisted | retry or surface error | job key is deduped by input hash | |

## External integrations

- provider:
  - purpose:
  - request shape:
  - response shape:
  - retries / limits:
  - secrets / auth:
  - used by epic/task:

## Auth / permissions

- actor:
  - can trigger:
  - server-side checks:
  - rate limits if public-facing:
