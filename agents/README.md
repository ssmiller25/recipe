# Recipe Agent Drafts

Confined draft persona set for `recipe/`.

## Usage

1. Choose one lead persona.
2. Add up to one supporting persona if needed.
3. Resolve cross-domain conflicts using `../../AGENTS.md`.

## Personas

- `personas/content.md` - recipe quality, readability, and metadata completion
- `personas/structure.md` - taxonomy, organization, and consistency
- `personas/publish.md` - build, preview, and release safety checks
- `personas/curation.md` - legacy content review using MUSTIE keep/refine/eliminate criteria

## Persona Invocation Examples

Example 1: content quality pass
```markdown
Lead Persona: content.md
Supporting Personas: none
Task: Improve clarity and metadata for three draft recipes.
Output Shape:
1. Edits made
2. Metadata fixes
3. Validation run
4. Remaining gaps
```

Example 2: structure plus release safety
```markdown
Lead Persona: structure.md
Supporting Personas: publish.md
Task: Reorganize taxonomy and verify no broken site navigation.
Output Shape:
1. Structural changes
2. Build/preview result
3. Risks
4. Rollback notes
```

Example 3: curation task
```markdown
Lead Persona: curation.md
Supporting Personas: content.md
Task: Review older recipes for keep/refine/archive/remove.
Output Shape (MUSTIE):
1. Item
2. MUSTIE flag(s)
3. Recommendation
4. Rationale
5. Redirect/update
```
