# Product Shaping Patterns

Use the smallest pattern that resolves the next decision.

## `identify-assumptions`

Use when the idea sounds plausible but risk is hidden.

Output:

- assumption
- why it matters
- what would falsify it

## `prioritize-assumptions`

Use when there are many assumptions and only a few should drive action.

Output:

- top assumptions ranked by risk x impact
- why these outrank the rest
- what to test first

## `brainstorm-experiments`

Use when the risky assumption is known and you need the fastest honest proof.

Output:

- experiment
- signal sought
- cost / time
- stop condition

## `opportunity-solution-tree`

Use when the outcome is known but the solution space is wide or noisy.

Output:

- target outcome
- opportunity branches
- candidate solutions
- next experiment

## `product-strategy`

Use when the real problem is strategic fit, focus, positioning, or defensibility.

Output:

- target user
- painful job
- wedge
- strategic advantage
- non-goals

## `value-proposition`

Use when the buyer, pain, or promised outcome is still too soft.

Output:

- who
- current pain or job
- promised outcome
- why this beats the workaround

## `pre-mortem`

Use when execution is underway and avoidable failure needs to surface early.

Output:

- failure mode
- likely trigger
- early warning sign
- mitigation

## Exit Routing

Every product-shaping output should end by naming the next lane:

- `validation` if buyer, signal, or pain is still too soft
- `execution brief` or core `spec-bundle` if the next build step is straightforward and reversible
- `light architecture lane` if the solution crosses subsystems, needs a system map, or depends on invariants or local/cloud boundaries
- `full architecture pack` if the solution now implies schema changes, public API or event contracts, background jobs, auth/permissions logic, external integrations, or meaningful rollout/cost risk

## Chaining rule

Only chain when the next framework clearly depends on the previous one.

Good chain:

`identify-assumptions -> prioritize-assumptions -> brainstorm-experiments`

Bad chain:

running every framework because the repo had them available
