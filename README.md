# Fieldnote Release QA Starter Kit

A small, practical release-quality pack for technical teams shipping hardware, firmware, or software.

## What this repository contains

- `site/` — the validation landing page and free sample.
- `kit/` — the paid-product candidate: checklists, templates, and CI scaffolding.
- `scripts/build_bundle.py` — deterministic ZIP builder.
- `tests/` — artifact and privacy checks.

## Product boundary

This is a **starter kit**, not a certification, regulated sign-off, or substitute for a qualified engineering review. Adapt every checklist to the product, interfaces, threat model, requirements, and applicable standards.

The first adapter uses embedded-project examples because they make the evidence problem concrete. The product hypothesis is broader: small technical teams that need a lightweight, traceable release process.

## Local verification

```sh
python3 scripts/build_bundle.py
python3 -m unittest discover -s tests -v
python3 -m http.server 4173 --directory site
```

Open <http://127.0.0.1:4173/> for the landing page.

## Checkout status

The landing page deliberately contains no fake payment URL. Configure a Payhip/Ko-fi/Gumroad checkout only after validating the offer and replacing the `data-checkout-url` placeholder in `site/index.html`.
