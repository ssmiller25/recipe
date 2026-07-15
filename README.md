# Miller Family Recipes

Family Recipes, in a static site.

## Local Build

```sh
make build   # Generate commits data and build the site
make run     # Generate commits data and serve locally
```

## Correcting a commit's displayed text

The homepage renders git commit messages directly (see `scripts/generate-commits-data.py`),
so a typo or unclear message would otherwise be permanent-looking without
editing history. Instead, attach a "display override" note — it doesn't
touch the commit or its hash, so no history rewrite or force-push is needed:

```sh
make note HASH=<commit-hash>   # opens $EDITOR: first line = heading,
                                # blank line, then body text
make notes-push                # publish the note to origin
```

A commit with no note shows its real message, unchanged. To remove an
override: `git notes --ref=refs/notes/site-display remove <commit-hash>`.

Notes live under `refs/notes/site-display` and aren't fetched by a normal
`git pull`/clone, so pull down anyone else's notes with:

```sh
make notes-sync
```

