# Idea Validation Playbook

Use this before PRD for serious product ideas.

## 0. Contract-Clean Gate

Run this first when an idea is even loosely adjacent to old client work, moderation work, sensitive corp data, disputed rights, or restricted tooling.

Hard reject the idea if it:

- uses contract-bound data, logs, labels, screenshots, or derived patterns
- automates or delegates work that a contract expects to be done personally
- depends on hidden third-party help, account sharing, or prohibited tools
- relies on gray scraping, ToS evasion, or sensitive data without a clean right to process it

Prefer ideas that start from:

- the builder's own data and personally controlled uploads
- public official feeds, APIs, docs, and exports
- newly collected clean data with explicit rights

If the idea fails here, park it before scoring buyer, pain, or wedge.

## One-Screen Template

### 1. Idea

- one-sentence idea
- why now

### 2. Buyer

- exact buyer / operator
- how reachable they are
- why we understand them

### 3. Pain

- painful recurring job / loss / delay
- current workaround
- cost of the workaround

### 4. Outcome

- promised outcome
- why it is better than the workaround
- what labor / time / risk it replaces

### 5. Wedge

- one function
- one buyer
- one problem
- fastest proof path:
  - manual service
  - concierge flow
  - tiny demo
  - narrow prototype

### 6. Distribution

- first channel
- first hook
- why users will notice it

### 7. Proof

- target signals
- minimum signal needed before PRD

### 8. Market Sanity

- rough buyer count
- rough yearly value of the pain
- rough price range

### 9. Personal Fit

- why it fits the builder
- what context edge we have
- what feels misaligned

### 10. Kill Criteria

- what would make us park or reshape the idea

## Defaults

- prefer pain over cleverness
- prefer the builder as user zero whenever possible
- prefer one function / one buyer / one painful problem
- prefer manual proof before heavy build
- validate distribution early
- prefer not to open architecture work until the idea has at least one believable signal
- if the value cannot be sold natively from a page, example, or self-serve demo without a call, treat that as a weak fit
- compare agent products to labor replaced, not cheap SaaS
- copying a proven wedge is allowed

## Exit Routing

After the one-screen brief, choose the smallest honest next lane:

- stay in validation if signal is weak, contradictory, or hypothetical
- move to `product-shaping` if the next uncertainty is assumptions, strategy, or wedge selection
- move to a short execution brief or core `spec-bundle` if the build is small and reversible
- move to a `light architecture lane` if the likely build crosses subsystems, needs a system map, or has a real local/cloud boundary
- move to a `full architecture pack` if the likely build includes schema changes, public API or event contracts, background jobs, auth/permissions logic, external integrations, or meaningful rollout/cost risk
