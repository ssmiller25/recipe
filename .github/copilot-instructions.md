# GitHub Copilot Instructions for Recipe Workspace

## Recipe Format Guidelines

When creating or editing recipe markdown files in this workspace:

### Measurements
- Use text-based fractions (1/2, 1/4, 1/8, 3/4, etc.) instead of fraction symbols (½, ¼, ⅛, ¾)
- This ensures better compatibility and readability across all platforms

### Recipe Structure
- Follow the Hugo front matter format with:
  - `title`: Recipe name
  - `date`: Creation date
  - `tags`: Array of relevant tags (e.g., lunch, dinner, dessert)
    - **Important**: Always use existing tags from the recipe collection
    - Search existing recipes to find appropriate tags before creating new ones
    - Only add a new tag after asking the user for approval
    - All new recipes should be marked "to-try" unless specified otherwise
  - `layout`: Set to "recipe"
  - `servings`: Number of servings
  - `prep_time`: Time in minutes
  - `cook`: Boolean (true/false)
  - `cook_increment`: "minutes" or "hours"
  - `cook_time`: Time value or blank
  - `calories`: kcal value or blank

### Sections
1. **Introduction** (optional): Brief description after front matter
2. **Ingredients**: Bulleted list with proper measurements
3. **Instructions**: Numbered steps
4. **Source/Story**: Attribution or background story
5. **Notes** (optional): Additional tips or variations
