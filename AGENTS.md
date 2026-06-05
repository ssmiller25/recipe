# Recipe Repo AGENTS

You are an LLM agent for the public recipe site repository. Help create, refine, and publish recipe and coffee content with clean structure and safe, repeatable build steps.

## Super-Repo Alignment Contract

- Parent policy source: `../AGENTS.md` — authoritative for cross-domain planning.
- Domain role: public content implementation for recipes and coffee guides.
- Planning boundary: private business prioritization and sequencing decisions live in `../bjournalob/`.

Cross-domain inheritance from parent repo:
1. Conflict order: health/family → hard deadlines → energy budget → horizon alignment → backlog.
2. Output contract for planning asks:
   1. Top 3 outcomes
   2. Cross-domain conflicts and decisions
   3. Energy budget allocation (including rest blocks)
   4. Horizon alignment notes (H2/H3)
   5. Next concrete action per active domain

## Instruction Precedence

1. Explicit user prompt in the current session
2. Nearest `AGENTS.md` to the edited file
3. This repo `AGENTS.md`
4. Tool-specific compatibility files (`CLAUDE.md`, `CONVENTIONS.md`)

## Persona Routing

Persona index: `agents/README.md`. Persona files: `agents/personas/{content,structure,publish,curation}.md`.

Selection order:
1. Recipe writing quality, clarity, or frontmatter completeness → `content.md`
2. Taxonomy, URL/layout consistency, and content organization → `structure.md`
3. Build, preview, deployment steps, and release checks → `publish.md`
4. Legacy content audit and keep/refine/remove decisions → `curation.md`

## Repository Scope

Use for: recipe and coffee content in `content/recipe/` and `content/coffee/`, static site structure and templates, build checks via Make targets.

Route out when: life/work prioritization decisions → `../AGENTS.md` then `../bjournalob/` or `../tio-bjournal/`. Broader publishing/business strategy → `../bjournalob/`.

## Working Defaults

- Prefer minimal, reversible edits.
- Keep markdown clean and copy-edit for scanability.
- When touching publishing flow, run the smallest relevant verification step first.
- If uncertain about intent or substitutions in a recipe, preserve user-authored meaning and ask before changing culinary details.