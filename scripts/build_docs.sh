#!/usr/bin/env bash
# Assemble the MkDocs source tree in docs/ (a build artifact; gitignored).
# MkDocs does not allow docs_dir to be the repository root, so the Markdown
# that lives at the root is copied into docs/ with its relative layout intact.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf docs
mkdir -p docs/github
cp README.md docs/index.md
cp CONTRIBUTING.md CHANGELOG.md DATASHEET.md LICENSE docs/
cp -R taxonomy governance docs/
# MkDocs always skips dot-directories, so the contribution templates are
# published under github/ and links to .github/ are rewritten in the copies.
cp -R .github/ISSUE_TEMPLATE .github/TAXONOMY_STRUCTURE_TEMPLATE.md .github/PULL_REQUEST_TEMPLATE.md docs/github/
grep -rl '\.github/' docs --include='*.md' | xargs sed -i.bak 's#\.github/#github/#g'
find docs -name '*.bak' -delete
echo "docs/ assembled. Build with: mkdocs build --strict"
