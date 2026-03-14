# Search Patterns

Use current-year queries and verify finalists at the primary source.

## Source selection

Choose sources by task type:

| Task type | Web | GitHub | MCP catalogs | Awesome-lists | Package check |
| --- | --- | --- | --- | --- | --- |
| SaaS or hosted service | yes | optional | no | optional | no |
| Library or SDK | yes | yes | no | yes | yes |
| MCP server | yes | yes | yes | optional | no |
| API platform | yes | yes | no | optional | optional |
| Model or AI tool | yes | yes | optional | yes | no |
| Unclear | yes | yes | yes when relevant | yes | finalists only |

Default rule:

- web plus GitHub for most searches
- add MCP catalogs for MCP questions
- add awesome-lists when curation is likely useful
- check package registries only for finalists

## Source priority

1. official documentation or product page
2. official GitHub repository
3. official pricing or plan page
4. curated discovery sources such as awesome-lists
5. comparison articles only as supporting discovery

## Query patterns

### Web

- `best [task] tools [current year]`
- `[task] software official`
- `[task] api official`
- `[task] pricing official`
- `[task] open source tool [current year]`

### GitHub

Use `gh search repos` when available:

- `gh search repos "[task]" --sort=stars --limit 10`
- `gh search repos "[task] tool" --sort=stars --limit 10`
- `gh search repos "[task] mcp" --sort=stars --limit 10`

Fallback if `gh` is unavailable:

- `site:github.com [task] tool`
- `site:github.com [task] mcp`

### MCP catalogs

- `site:smithery.ai [task]`
- `site:github.com/modelcontextprotocol/servers [task]`
- `site:docs.anthropic.com mcp server [task]`

### Awesome-lists

- `awesome [topic] github`
- `site:github.com awesome [task]`

If an awesome-list is relevant, open its README and extract only the tools that fit the task.
Then verify those tools at their official repo or product page.

### Package discovery

Use package pages to verify finalists, not as the first discovery source.

- `npm [package-name]`
- `pypi [package-name]`

## Trivial-task filter

Stop the full search and recommend custom code when:

- the task is a one-off script
- the job is covered by the standard library or a tiny wrapper
- integration cost clearly exceeds the work saved

## When to browse

Always browse for this skill. Recommendations here are temporally unstable.
