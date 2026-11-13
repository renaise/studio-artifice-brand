# Studio Artifice brand guidelines

The Studio Artifice brand guideline site: one static page covering About, Mark, Color, Typography, Motion, Artifact, Origins and Voice, with every mark and artifact download it links to.

## What's here

| Path | Contents |
| --- | --- |
| `index.html` | The whole page. Styles and scripts are inline; design tokens are CSS variables at the top. |
| `assets/marks/` | Brand mark, wordmark, Ⓐ monogram, horizontal and vertical lockups (light and dark), and the four phase favicons, each as SVG and PNG. |
| `assets/artifact/` | Thermal mannequin stills, color and grayscale, PNG and JPG. |
| `assets/motion/` | Rive files for the cover board and the sting, plus the Rive web runtime (2.44.1) served locally. |
| `pages/` | The live 3D mannequin embed and its model. |
| `img/` | Images for the Artifact and Origins sections. |
| `_headers` | Sends `X-Robots-Tag: noindex, nofollow`. |

There is no build step.

## Preview

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploy

This repository is connected to Cloudflare Pages (project `studio-artifice-brand`). Pushing to a branch makes a preview; merging to `main` publishes the production site. The site root is the repository root.

## Updating

- Marks: export the SVG from the Figma master, render the PNG at the same pixel size as the current file, and replace both under the same name.
- Motion: edit the Rive file, export a signed `.riv`, and replace it in `assets/motion/`.
- The link-preview image (`og:image` in `index.html`) is an absolute URL. Update it when the site moves to its final domain.

## Brand rules

- Helvetica Now Display only. No monospace. Nothing heavier than weight 500.
- Phases, always in this order: Strategy #D2FF1E, Identity #FF1BD1, Applications #00EBEF, Production #0009FF.
- The brand mark is a square beside a screw: a circle with a cross cut out.
- Corners are 2px, lines are 1px.
- Clear space is measured from the wordmark; the Ⓐ monogram's height is not counted.

The page names Helvetica Now Display but does not embed it, since embedding needs a web license. Without one, visitors who don't have the font installed see Helvetica Neue or Arial.
