# Brand Site Template — ported from brand.artificenyc.org

**Source:** https://brand.artificenyc.org/ (title: "ARTIFICE Media Kit")
**Fetched:** 2026-10-14
**File:** `brand-artificenyc-template.html` (56 KB, single file)
**Target use:** Structural template for **brand.studioartifice.com**, to be committed to the GitHub repo `renaise/studio-artifice-brand` once it exists.

## What the template contains

A complete, self-contained brand/media-kit page. All CSS lives in one inline `<style>` block (~18.6 KB) driven by `:root` custom properties; all JS is one inline script (print button + copy-to-clipboard for boilerplate blocks). No external stylesheets, no webfont downloads, no framework.

Sections, in order:
1. Name, facts and boilerplate (with copyable boilerplate variants: `bp-std`, `bp-short`, `bp-ext`)
2. Marks and minimum sizes
3. Logo files (download/display grid of the lockups)
4. WHITEBOX and BLACKBOX (program marks, covers, icons)
5. Color — "Two grounds, one accent"
6. Typography — "One typeface: Helvetica Now Display"
7. Imagery — "Document the work and the room"
8. Chapters, nodes, [ ENTER ] (program marks)
9. Voice — "Describe the work rather than praise it"

## Design tokens (from `:root`, for adaptation)

- Grounds/text: `--bg:#0e0e0e`, `--surface:#151515`, `--text:#fcfaf5`, muted steps `--text-2/3/4`
- Accent: `--cobalt:#0000ee` (hover `--cobalt-2:#5a6cff`)
- Type: `--sans:"Helvetica Now Display","Helvetica Neue",Helvetica,Arial,sans-serif` — system stack, no font files to host
- Tracking tokens: display `-0.022em`, reading `-0.01em`, labels `0.08em`
- Canon note in the source CSS: values are mirrored from index.artificenyc.org (Pages project `es-artifice`)

## External dependencies (the only ones)

Images, all relative paths under `assets/` — NOT included in this folder; they stay on the source site until the SAFX versions are produced:
`lockup.svg`, `cover-lab.png`, `mark-lockup.png`, `artifice-wordmark.png`, `wb-icon.svg`, `bb-icon.svg`, `wb-cover.jpg`, `bb-cover.jpg`, `photo-wb.png`, `photo-bb.png`, `chapters-mark.png`, `nodes-mark.png`, `favicon.png`, and `assets/logos/` (7 ArtificeNYC WhiteBox/BlackBox lockup SVGs).

The Cloudflare-injected `email-decode.min.js` script tag from the live fetch was stripped (edge artifact, not part of the source).

## How to adapt for Studio Artifice (SAFX)

Entity separation applies: this template is Artifice NYC (nonprofit) content being reused as a *pattern* for Studio Artifice LLC. Before anything ships:

1. **Swap all copy.** Replace AFX boilerplate, program names (WHITEBOX/BLACKBOX/Chapters/ENTER), and voice examples with the Studio Artifice Brand Story (Drive: "Studio Artifice — Brand Story", 2026-10-14, 04_Brand).
2. **Swap the marks.** ArtificeNYC lockups out; Studio Artifice device + wordmark + Ⓐ monogram SVGs in (masters live with the Brand Story files).
3. **Retune the tokens.** Keep the structure (grounds, surface, one accent) but set SAFX values from the Brand Story: ink `#0E0E0E`, paper `#F4F1EA`, linen `#FCFAF5`, panel `#171717`, line `#242424`, cobalt `#0000EE`, plus the four phase colors (Strategy `#D2FF1E`, Identity `#FF1BD1`, Application `#00EBEF`, Activation `#0009FF`) which the AFX template has no equivalent for.
4. **Replace the program sections.** WHITEBOX/BLACKBOX and Chapters/Nodes sections become the four phases (Strategy, Identity, Applications, Production) and the worldsite concept.
5. **Produce an `assets/` folder** with SAFX images at the same relative paths so the template runs unmodified.
6. Deploy target: Cloudflare Pages at **brand.studioartifice.com** from repo `renaise/studio-artifice-brand`.
