---
name: Recipe Site Build Rules
description: Conventions for Hugo layout/config/build-related changes in recipe repo.
applyTo: "config.yaml,layouts/**/*.html,themes/**/*.html,static/**/*,scripts/**/*.sh,Makefile"
---
# Recipe site and build rules

- Keep changes small and reversible for layout/config/build paths.
- Preserve existing theme conventions and avoid broad refactors unless requested.
- Run the smallest relevant validation command before broad build steps.
- Call out publish risk and rollback path for deployment-impacting changes.
- Escalate cross-domain prioritization back to parent AGENTS guidance.

## Validation Quick Checks

Run the smallest set that matches the change:

1. Run the standardized repo smoke check:
```bash
make smoke-check
```
2. Verify changed files are in expected site/build paths:
```bash
git diff --name-only -- config.yaml layouts/ themes/ static/ scripts/ Makefile
```
3. Build the site:
```bash
make build
```
4. If templates/layouts changed, run local preview smoke test:
```bash
make run
```
