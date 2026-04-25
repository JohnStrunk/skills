#!/usr/bin/env bash
# Ensures all tracked text files have Unix (LF) line endings.
# This script is useful for fixing CRLF issues introduced on Windows.

set -euo pipefail

echo "Normalizing line endings to LF..."

# Use git to identify tracked files that are not binary and remove carriage returns.
# 'git grep -I' targets non-binary files.
git grep -I --name-only -z -e '' | xargs -0 sed -i 's/\r$//'

# Sync the git index with the normalized files.
# This is the specific git command used to re-process files through line-ending conversion.
git add --renormalize .

echo "Done. All tracked text files now use LF line endings."
