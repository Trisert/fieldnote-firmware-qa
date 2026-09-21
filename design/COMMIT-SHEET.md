# COMMIT-SHEET — Fieldnote / release QA

## 1. Peak / Signature
The hero evidence sheet: a physical-looking release record that traces one requirement through a test, CI run, and artifact. A visitor should describe the page as “the release QA page with the evidence sheet,” not as another SaaS landing page.

## 2. Color
Primary: `oklch(54% 0.19 258)` signal blue, commitment tier: committed. It is not lavender, cream, or the usual dark purple/blue developer glow; it comes from a printed engineering report and a test-bench indicator. Background target mean L: approximately `0.91`; this is a lit workbench/document surface where evidence should be readable, not a night-mode dashboard.

## 3. Type
Display: Georgia / Times-style serif for report headlines. Text: Arial / Helvetica-style grotesque for operational copy. Axis: editorial document × utilitarian interface. Inter is rejected because it would return the category default and erase the report metaphor.

## 4. Grid break
The hero’s evidence sheet crosses the normal reading grid as a rotated, offset physical sheet with a blue backing. The rest of the page returns to a restrained document grid so the break remains singular.

## 5. Motion budget
No scroll-triggered animation. One interaction family: short transform/color feedback on links and buttons. The product must remain readable with JavaScript disabled and in a file preview.

## 6. Reflex check
- a) Generic QA page: near-black background, mono labels, amber accent, status header, metric strip, repeated cards.
- b) Generic anti-SaaS response: beige editorial page, oversized serif headline, vague manifesto copy, and decorative paper texture.
- c) Chosen deviation: a cool lit report surface with one saturated signal-blue field, concrete evidence rows, and a single physical release sheet as the signature.

## 7. House tells broken
1. Near-black background → cool paper/workbench lightness so the content reads like a document.
2. Status-bar header and mono service labels → quiet wordmark plus normal navigation; labels use the text family, not terminal chrome.
3. Identical feature-card grid → traceability table and manifest rows with unequal content and real filenames.
