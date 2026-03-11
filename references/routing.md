# Routing

Choose the lightest format that makes the structure obvious.

## Architecture overview

Use:

- CSS grid cards for text-heavy systems
- Mermaid only when connections are the main story

Good for:

- service boundaries
- product pipelines
- repo or subsystem maps

## Flowchart or pipeline

Use:

- Mermaid flowchart when edges matter
- CSS steps or cards when narration matters more than graph topology

## Comparison or audit table

Use:

- semantic HTML table

Good for:

- tool comparisons
- rollout checklists
- risk matrices

## Timeline

Use:

- CSS timeline with cards

Good for:

- incident history
- launch plan
- investigation chronology

## Dashboard or KPI summary

Use:

- CSS card grid
- Chart.js only if trends materially help

## Decision rule

If the user mainly needs:

- relationships -> diagram
- scanning across rows and columns -> table
- sequence over time -> timeline
- grouped explanation -> card-based explainer
