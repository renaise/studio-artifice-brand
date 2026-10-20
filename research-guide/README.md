# Studio Artifice research page

The current R&D laid out in the structure of the final Brand Guideline page
(reference: id-idler.pages.dev, the #tokens / #refs way of documenting).
Cloudflare Pages project `safx-research`. Separate from the PR #1 brand site.

- `public/index.html` is the whole page (no build step). Sections: About, Mark, Color,
  Grayscale, Typography, Atoms, The Reading, Studies, Tokens, References.
- `public/studies/` are the scrubbed study pages from rnd-compilation/pages.
- `public/img/` are thumbnails cropped from screenshots of those pages, plus reference images.
- Run `deploy.command` on the Mac to publish (wrangler, logged in there).
- Type: Helvetica Now Display via local install only (not self-hosted: no web licence),
  fallback Helvetica Neue, Helvetica, Arial. No monospace anywhere.
