# Changelog

User-visible package changes are recorded here. PR and GitHub Release summaries
derive from these entries; an Unreleased entry is not a published release.

## Unreleased

No unreleased changes.

## 0.9.0 — 2026-10-21

### Added

- Site option `askr.reading-width: normal|wide` selects a consistent 630px or
  780px body base across docked, floating and absent sidebars.
- Accessible table scroll regions, `.askr-symbol-table`, `.askr-table-compact`
  and `.askr-table-numeric`, including wrapping-div use with captionless tables.
- Ordered `askr.page-facts` entries with `key` and `label`, reading flat scalar
  page values beneath the title description while preserving native metadata.
- `.askr-wide-figure` preserves intrinsic diagram size inside an accessible
  scroll region, and Mermaid follows Askr's light/dark palette.
- Calm treatments for native theorem-like blocks and proofs.

### Changed

- Display math Copy is compact and supports labelled equations and tight lists.
  Source stays in data attributes; manual-copy text is created only after a
  clipboard failure. Site `askr.math-copy`, flat page `askr-math-copy` and
  per-equation `.no-math-copy` control availability.
- Public border tokens use dedicated Askr Sass sources; text-grade muted colors,
  callout titles, dark important/caution hues and link hover improve contrast.
  Table headers use a 1px decorative rule and a 1.35 line height.
- Documented consumer options `respect-user-color-scheme: true` and
  `smooth-scroll: false`. Reader-toggle controls share Askr's control size,
  border, radius, colors and hover treatment; spacing beside search accounts
  for the reader toggle. Other P1 navigation, headings, native-element, CJK,
  print, root-font, localization and cleanup work is deferred.
- Kept the installation format, normal-width default, enabled math Copy, footer
  credit and Quarto `>=1.9.38 <1.11`. Palette defaults changed as described above.
  Sass border overrides now use `$qdk-border`, and muted text uses
  `$qdk-muted-text`; public CSS property names remain available. Invalid
  reading-width values or malformed page-facts configuration raise render errors.

## 0.8.0 — 2026-10-10

### Changed

- Askr's image viewer now has a shared inline/modal pan-and-zoom engine for
  SVG, PNG and JPEG, with zoom controls, Fit, fullscreen and gallery navigation.
- Existing image buttons remain supported; `mode="inline"` embeds interactive
  controls and preserves the camera when expanded and returned to the article.
- GLightbox runtime is replaced. Its effect, desc-position and css-class options
  are not supported and explicit use is reported during rendering.

### Compatibility and observation limits

- Quarto 1.10.18 remains the release-render environment. `lightbox` eligibility,
  exclusions, groups and the existing button syntax remain supported.
- Native touchscreen pinch and JavaScript-disabled browser operation were not
  exercised. Captions/descriptions are displayed as text. SVG is loaded as an
  image, not parsed as layout geometry; zoom does not increase raster resolution.

## 0.7.0 — 2026-10-09

### Added

- Native Header tools and Footer links receive coordinated icon controls,
  light/dark colors and responsive spacing. Authors retain Quarto configuration.
- Default opt-out Powered by Askr credit uses the installed extension version,
  separate from document versions; existing Footer content is preserved.
- Header and footer links Usage guidance, including accessible native icon links
  and the credit opt-out. Gallery shows a single Powered by Askr credit line,
  without additional descriptive right-side text.

## 0.6.1 — 2026-10-06

### Fixed

- Header Areas use the existing navigation disclosure when the title, Areas
  and controls no longer fit. Long titles retain their accessible name while
  truncating when necessary; resizing does not leave an open overlay behind.
- The Gallery no longer loads Zenscroll alongside Notebook RequireJS output,
  avoiding `Mismatched anonymous define() module`. Native CSS retains smooth
  scrolling and respects reduced-motion preferences. RequireJS is not removed.

### Notes

- No new navigation configuration is required. Mobile Pages behavior remains
  separate from the adaptive Areas menu.
- A consumer that explicitly enables Quarto `smooth-scroll: true` still asks
  Quarto to load Zenscroll; use `false` to avoid that upstream loader conflict.

## 0.6.0

### Added

- Optional Header Logout entry through `askr.logout.href` and `label`, with
  protected-documentation Usage guidance. Askr navigates to the configured
  destination; the identity provider owns sessions and logout scope.
- Quarto native image Lightbox by default, with `askr-image-view` buttons for
  existing figures or button-only image entries, plus Image viewer Usage.
- Viewer styling and focus restoration without a second viewer library.

### Limits

- Public Gallery does not enable Logout. No deployment configuration or real
  identity-provider logout is performed by Askr.
- Lightbox uses the original image; enlargement does not create resolution.
- The published Figures page had the RequireJS/Zenscroll conflict addressed
  in the 0.6.1 entry above.
