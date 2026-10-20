#!/bin/bash
# Double-click (or run) to publish public/ to Cloudflare Pages (project safx-research).
cd "$(dirname "$0")"
npx --yes wrangler@latest pages project list 2>/dev/null | grep -q "safx-research" || \
  npx --yes wrangler@latest pages project create safx-research --production-branch main
npx --yes wrangler@latest pages deploy public --project-name safx-research --branch main --commit-dirty=true
read -n 1 -s -r -p "Done. Press any key to close."
