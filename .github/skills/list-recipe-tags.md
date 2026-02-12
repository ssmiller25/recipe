---
name: list-recipe-tags
description: List all unique tags used in recipe front matter.
inputs: []
outputs:
  - name: tags
    description: Unique tags, sorted alphabetically.
    type: array
command: python3 scripts/list_recipe_tags.py --format json
---

Use this skill to retrieve the current tag list for validating new recipes.
