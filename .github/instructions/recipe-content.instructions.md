---
name: Recipe Content Rules
description: Conventions for recipe and coffee content markdown files.
applyTo: "content/recipe/**/*.md,content/coffee/**/*.md,archetypes/**/*.md"
---
# Recipe content rules

- Preserve recipe intent and avoid changing ingredient semantics without explicit request.
- Improve readability with concise sections, clear step order, and practical timing cues.
- Keep frontmatter complete and consistent with existing taxonomy.
- For curation tasks, use MUSTIE output shape and specify redirect/update needs.
- Prefer minimal edits that are easy to review and rollback.

## Validation Quick Checks

Run the smallest set that matches the change:

1. Run the standardized repo smoke check:
```bash
make smoke-check
```
2. Verify modified files are content-scoped:
```bash
git diff --name-only -- content/recipe/ content/coffee/ archetypes/
```
3. Validate markdown frontmatter shape on changed files (spot check):
```bash
rg -n "^---$|^title:|^date:|^draft:" content/recipe content/coffee archetypes -g "*.md"
```
4. Build the site when content or taxonomy changes are substantial:
```bash
make build
```
