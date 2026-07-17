# Evaluation Matrix

Use this structure when comparing candidates.

## Table shape

```md
| Tool | Type | Maturity | Signals | Why it fits | Main limits | Link |
```

## Suggested meanings

- `Tool` - product, repo, package, API, or MCP server name
- `Type` - SaaS, library, API, MCP server, model, no-code, or similar
- `Maturity` - established, new, niche, archived, or similar short label
- `Signals` - GitHub stars, archived flag, repeated discovery across sources, notable adoption signal
- `Why it fits` - why it matches this exact task, stack, or workflow
- `Main limits` - pricing, missing features, lock-in, setup burden, or maintenance risk
- `Link` - official page or official repo

## Questions to answer

- Does it solve the actual job, not just an adjacent one?
- Is it maintained now?
- Does it fit the current stack and operating constraints?
- Is the integration cost lower than building it?
- Does it create lock-in, review risk, or hidden ops cost?
- Did it appear across multiple sources, or only once?

## Deduplication rule

If a tool appears in multiple sources, keep one row and aggregate the signals.

Examples:

- `Found via GitHub + awesome-list`
- `★ 8.2k`
- `Archived`

## Recommendation pattern

End with three short calls:

- `Try first`
- `Avoid for now`
- `Build it ourselves instead` when appropriate
