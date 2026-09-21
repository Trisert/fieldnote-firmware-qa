# Embedded Firmware QA Starter Kit

A small, practical quality-assurance pack for STM32/C/FreeRTOS projects.

## What this repository contains

- `site/` — the validation landing page and free sample.
- `kit/` — the paid-product candidate: checklists, templates, and CI scaffolding.
- `scripts/build_bundle.py` — deterministic ZIP builder.
- `tests/` — artifact and privacy checks.

## Product boundary

This is a **starter kit**, not a safety certification, flight-readiness approval, or substitute for a qualified engineering review. Adapt every checklist to the target MCU, board, interface control documents, threat model, and applicable standards.

The first market hypothesis is broader than PocketQube: STM32, C, FreeRTOS, and small embedded teams. The spaceflight/PocketQube material is an optional extension, not the core audience.

## Local verification

```sh
python3 scripts/build_bundle.py
python3 -m unittest discover -s tests -v
python3 -m http.server 4173 --directory site
```

Open <http://127.0.0.1:4173/> for the landing page.

## Checkout status

The landing page deliberately contains no fake payment URL. Configure a Payhip/Ko-fi/Gumroad checkout only after validating the offer and replacing the `data-checkout-url` placeholder in `site/index.html`.
