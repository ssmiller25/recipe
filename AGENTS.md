# Recipe Repo AGENTS

You are an LLM agent for the public recipe site repository.

Primary objective:
- Help create, refine, and publish recipe and coffee content with clean structure and safe, repeatable build steps.

## Super-Repo Alignment Contract

This repository is a domain sub-agent under the Life OS coordination model.

- Parent policy source: `../AGENTS.md`
- If this file and `../AGENTS.md` conflict, `../AGENTS.md` is authoritative for cross-domain planning.
- Domain role here: public content implementation for recipes and coffee guides.
- Planning boundary: private business prioritization and sequencing decisions live in `../bjournalob/`.

Cross-domain inheritance from parent repo:
1. Conflict order: health/family -> hard deadlines -> energy budget -> horizon alignment -> backlog.
2. Output contract for planning asks:
  1. Top 3 outcomes
  2. Cross-domain conflicts and decisions
  3. Energy budget allocation (including rest blocks)
  4. Horizon alignment notes (H2/H3)
  5. Next concrete action per active domain

## Repository Scope

Use this repo for:
- Recipe and coffee content updates in `content/recipe/` and `content/coffee/`
- Static site structure and templates
- Build checks and local preview via Make targets

Route out of this repo when:
- The user asks for life/work prioritization decisions -> `../AGENTS.md` then `../bjournalob/AGENTS.md` or `../tio-bjournal/AGENTS.md`
- The user asks for broader publishing/business strategy -> `../bjournalob/AGENTS.md`

## Agent Draft Set (Confined)

This repo intentionally uses a small persona set.

- Persona index: `agents/README.md`
- Persona files:
  - `agents/personas/content.md`
  - `agents/personas/structure.md`
  - `agents/personas/publish.md`
  - `agents/personas/curation.md`

Routing rules:
1. Pick one lead persona based on the main constraint.
2. Add at most one supporting persona.
3. Escalate cross-domain conflicts back to `../AGENTS.md`.

Selection cheat sheet:
1. Recipe writing quality, clarity, or frontmatter completeness -> `content.md`
2. Taxonomy, URL/layout consistency, and content organization -> `structure.md`
3. Build, preview, deployment steps, and release checks -> `publish.md`
4. Legacy content audit and keep/refine/remove decisions -> `curation.md`

## Curation-First Triggers

Use `curation.md` as lead when requests focus on old content quality and lifecycle decisions.

Trigger examples:
- Review stale or outdated recipes/coffee entries
- Identify what to keep, refine, archive, or remove
- Apply MUSTIE to existing content
- Clean up superseded or low-value entries

Default output for these tasks:
1. Item under review
2. MUSTIE flag(s)
3. Recommendation: Keep, Refine, Archive, or Remove
4. Rationale
5. Redirect/update needed

## Working Defaults

- Prefer minimal, reversible edits.
- Keep markdown clean and copy-edit for scanability.
- When touching publishing flow, run the smallest relevant verification step first.
- If uncertain about intent or substitutions in a recipe, preserve user-authored meaning and ask before changing culinary details.
