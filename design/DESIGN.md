---
version: alpha
name: Fieldnote / firmware QA
description: "A lit engineering-report identity for small embedded teams: evidence first, process second."
colors:
  primary: "oklch(54% 0.19 258)"
  secondary: "oklch(32% 0.12 258)"
  tertiary: "oklch(58% 0.18 28)"
  neutral: "oklch(96% 0.012 220)"
typography:
  display:
    fontFamily: Georgia
    fontSize: 7.6rem
    fontWeight: 400
    lineHeight: 0.91
    letterSpacing: "-0.045em"
  body:
    fontFamily: Arial
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
rounded:
  sm: 0px
spacing:
  shell: 48px
  section: "clamp(84px, 11vw, 150px)"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: 18px
  evidence-sheet:
    backgroundColor: "{colors.neutral}"
    textColor: "#1F2933"
    rounded: "{rounded.sm}"
    padding: 42px
---

## Overview

Fieldnote treats firmware QA as a document trail: requirements, tests, CI, and artifacts should remain connected after the person who ran the test has left the room.

## Colors

Signal blue is the identity hue. The page is light because evidence is meant to be read and reviewed. Red marks an open boundary or caution; green is reserved for actual passing states.

## Typography

Georgia gives the page the authority of a report without turning it into a lifestyle editorial. Arial keeps filenames, tables, and operational copy direct and legible.

## Layout

The page uses a restrained document grid with one deliberate break: the hero evidence sheet is offset and rotated against a blue backing field.

## Components

The evidence sheet is the signature component. Lists and traceability rows replace repeated feature cards.

## Do's and Don'ts

- Do show real filenames, requirements, and verification methods.
- Do keep the free sample useful and the commercial boundary honest.
- Do not imply certification, flight readiness, or safety approval.
- Do not add gradients, decorative metric strips, or generic dashboard cards.
