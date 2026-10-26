# ClearFocus Studio Ebook Funnel

A responsive, interactive portfolio demonstration for the fictional independent brand ClearFocus Studio.

## Experience

- Free Ebook landing page with in-browser name and email validation.
- Thank-you and optional US$19 planner upsell.
- Clearly labelled simulated checkout with no card fields or payment processing.
- Success page with a complete planner download.
- Real 8-page Focus Reset PDF and 6-page printable Focus Planner PDF.
- Hash routing for reliable refreshes on GitHub Pages repository paths.

No form data is saved, transmitted, logged, or placed in the URL. This project does not use a backend.

## Local development

Requires Node.js 20 or newer.

```bash
pnpm install
pnpm dev
```

## Build

```bash
pnpm build
pnpm test:sites
```

The GitHub Actions workflow builds and deploys `dist/client` to GitHub Pages after every push to `main`. In repository settings, Pages must use **GitHub Actions** as its source.

The PDFs can be regenerated with:

```bash
python3 scripts/generate_pdfs.py
```

