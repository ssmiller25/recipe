HUGO_VERSION := 0.122.0
NOTES_REF := refs/notes/site-display

help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.phony: run
run: .bin/hugo generate-commits   ## Run site
	@.bin/hugo serve

.phony: build
build: .bin/hugo generate-commits   ## Build the site
	@.bin/hugo

.phony: generate-commits
generate-commits:   ## Generate commits data for home page
	uv run scripts/generate-commits-data.py

.phony: note
note:   ## Add/edit a display-override note for a commit: make note HASH=<commit-hash>
	@test -n "$(HASH)" || (echo "Usage: make note HASH=<commit-hash>"; exit 1)
	@git notes --ref=$(NOTES_REF) edit $(HASH)
	@echo "Note saved locally. Run 'make notes-push' to publish it."

.phony: notes-push
notes-push:   ## Publish local display-override notes to origin
	@git push origin $(NOTES_REF)

.phony: notes-sync
notes-sync:   ## Fetch display-override notes from origin
	@git fetch origin $(NOTES_REF):$(NOTES_REF)

.phony: smoke-check
smoke-check: ## Run lightweight repository smoke checks
	@test -f AGENTS.md
	@test -f README.md
	@test -f config.yaml
	@test -d content/recipe
	@test -d content/coffee
	@git status -s >/dev/null
	@echo "recipe smoke checks passed"

.phony: newcontent
# TODO, actually implement base on parameter?
# hugo new content recipe/kamala-tuna-melt.md
# OR
# hugo new content coffee/espresso-cream-honey.md
# and can auto-open in codespaces with
# `code <filename>`

.phony: newsite
newsite: .bin/hugo  ## New hugo site - only used once
	@.bin/hugo new site . --force --format yaml
	@find . -maxdepth 1 -type d -not -name '.*' | while read dir; do touch $${dir}/.gitkeep; done

.bin/hugo:
	@mkdir .bin || true
	@curl -Lo .bin/hugo.tar.gz https://github.com/gohugoio/hugo/releases/download/v$(HUGO_VERSION)/hugo_$(HUGO_VERSION)_linux-amd64.tar.gz
	@tar -xzf .bin/hugo.tar.gz -C .bin
	@rm .bin/hugo.tar.gz

# Help Source: https://gist.github.com/prwhite/8168133
