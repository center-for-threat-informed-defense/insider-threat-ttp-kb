SOURCEDIR = docs/
BUILDDIR = docs/_build/

docs-ci: ## Generate HTML documentation for publishing to GitHub Pages.
	sphinx-build -M dirhtml "$(SOURCEDIR)" "$(BUILDDIR)" -W --keep-going

docs-html: ## Generate HTML documentation for local viewing.
	sphinx-build -M html "$(SOURCEDIR)" "$(BUILDDIR)"

docs-pdf: ## Generate PDF documentation.
	poetry export --dev --without-hashes -f requirements.txt -o docs/requirements.txt
	docker run --rm -v "$(PWD)/docs":/docs sphinxdoc/sphinx-latexpdf:4.3.1 \
		bash -c "pip install -r requirements.txt && sphinx-build -M latexpdf /docs /docs/_build"
	rm docs/requirements.txt

docs-server: ## Run server for local editing of docs.
	sphinx-autobuild -b dirhtml -a "$(SOURCEDIR)" "$(BUILDDIR)"
