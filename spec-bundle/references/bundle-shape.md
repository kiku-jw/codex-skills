# Bundle Shape

Use this reference when the user wants a real agent-ready build packet rather than a loose PRD.

## What belongs in the bundle

Keep it compact. The default core bundle has five files:

1. `prd.md`
2. `contracts.md`
3. `schema.sql`
4. `test-plan.md`
5. `epics.md`

Add the architecture pack only when it reduces confusion:

6. `blueprint.md`
7. `gate-matrix.md`
8. `adr/` for decision records

Not every project needs all of these. Include only what reduces confusion.

## File-by-file guidance

### `prd.md`

Use for:

- product goal
- scope and non-goals
- user flow
- hard constraints
- success criteria

Good sign:

- a developer can explain what must exist in v1 and what is intentionally out

Bad sign:

- the document reads like launch copy or investor language

### `contracts.md`

Use for:

- API shapes
- IPC / event payloads
- queue/job states
- background-worker inputs and outputs
- external integration boundaries
- contract invariants
- task or epic traceability

Good sign:

- another developer can implement against this file without guessing the payload shape or who depends on it

Bad sign:

- it repeats the PRD in prose and has no concrete request/response/state detail

### `schema.sql`

Use for:

- real tables
- relationships
- enum/state columns
- indexes that matter to the first version

Good sign:

- it answers “what will actually be persisted and how is it linked?”

Bad sign:

- the project has meaningful persistence but the data model only exists in your head

### `test-plan.md`

Use for:

- acceptance criteria
- high-value happy paths
- failure modes
- fixtures or sample inputs that matter
- gate-closing evidence when the work has hard or soft gates

Good sign:

- review can check the result against explicit behavior instead of vibes

Bad sign:

- it says “write tests” but does not say what must be true

### `epics.md`

Use for:

- GitHub-ready breakdown
- phase order
- dependencies
- task inputs and outputs
- evidence and “done means …” for each chunk

Good sign:

- the work can be split into issues without rethinking the whole project or guessing what proof each task must leave behind

Bad sign:

- the breakdown is either one giant blob or fifty micro-tasks with no narrative

### `blueprint.md`

Use for:

- system map
- component boundaries
- data or control flow
- invariants
- local/cloud boundary
- architecture pressure points

Good sign:

- a developer can explain how the system is supposed to hang together before coding the risky parts

Bad sign:

- it duplicates the PRD or turns into a pretty essay with no operational value

### `gate-matrix.md`

Use for:

- hard gates that block irreversible or expensive work
- soft gates that must close before rollout or handoff
- required evidence to close each gate

Good sign:

- risky work cannot quietly move forward on vibes alone

Bad sign:

- every tiny question becomes a gate and the file turns into bureaucracy

### `adr/`

Use for:

- irreversible decisions
- decisions with meaningful downside
- decisions that will be revisited later unless the reasoning is preserved

Good sign:

- future you can see why the choice was made, not just what the choice was

Bad sign:

- trivial UI or naming choices get promoted into ADR theater

## When a full bundle is worth it

Prefer a full bundle when at least two are true:

- work will span sessions
- more than one repo/system is involved
- rollout or security risk exists
- a second agent or reviewer will touch it
- the project has meaningful data/contracts/background jobs
- the task will likely become a public artifact or reusable product

Prefer the architecture pack when at least one is true:

- schema or migration work exists
- public API, IPC, or event contracts matter
- background jobs or queues exist
- auth or permissions logic changes
- external integrations or rate/cost constraints matter
- local/cloud boundary or degraded mode needs explicit treatment

## When a brief is enough

Skip the full bundle when:

- the work is tiny and reversible
- no durable data or contract exists
- one developer can finish it in one sitting without handoff
- the missing clarity is tactical, not architectural

## Quality bar

The bundle is ready when:

- a coder knows what to build
- a reviewer knows how to judge it
- a future you can reopen it in a week and still trust it
- risky decisions, gates, and task evidence are traceable without re-reading chat

If it does not achieve those three things, shorten it or sharpen it.
