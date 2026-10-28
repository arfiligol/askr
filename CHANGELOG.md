# Changelog

User-visible package changes are recorded here. PR and GitHub Release summaries
derive from these entries; an Unreleased entry is not a published release.

## Unreleased

## 0.13.3 — 2026-10-28

### Changed

- Highlight the current Page List link with a theme-aware row tint and
  semibold label.
- Preserve the actual published 0.13.2 documentation site under `/v0.13.2/`.

## 0.13.2 — 2026-10-28

### Added

- Add bilingual License pages and document native footer links for project
  licenses and third-party notices.

### Changed

- Style Quarto filename code blocks with one shared frame, wrapping filenames,
  local source scrolling, and the existing Copy control.
- Document Safari's clipboard limits on HTTP previews. Copy behavior is unchanged.

## 0.13.1 — 2026-10-27

### Fixed

- Remove the extra top space added by shared Copy controls in native code
  blocks, including displayed Mermaid source, while retaining the text button
  and copy feedback.

## 0.13.0 — 2026-10-27

### Added

- Add `askr-chart-view` for trusted local interactive HTML, inline or through a
  button opening a floating window. Charts keep their own controls and colors;
  the Askr frame follows the site theme. Inline and floating states are independent.
  The floating toolbar provides Open source and Close.
- Give static images and interactive charts separate bilingual Component pages,
  retaining the existing Figures image-viewer fragments as links. Group the two
  pages under a native top-level Viewers sidebar section with current-page expansion.
- Include an offline Plotly sine-curve demonstration with an explicit MIT
  license. Plotly is a Gallery asset, not an extension dependency.

### Changed

- Preserve the actual published 0.12.1 documentation as an unmaintained archive
  and retain older release snapshots in the version selector.
- Remove the current standalone CJK specimen pages; the bilingual documentation
  now demonstrates typography through real pages. Historical snapshots remain intact.
- Use a shared text `Copy` control for displayed-math source, Mermaid source
  and native code blocks. A successful copy shows `Copied!` on the button with
  a green outline for about two seconds, then restores `Copy`; native code
  retains Quarto's `code-copy` setting without its icon-and-tooltip control.

### Limits

- Chart exports are trusted same-origin HTML, served over HTTP(S). Companion
  resources require native `project.resources` or a self-contained export.
  Askr does not recolor the chart, synchronize frame state or add chart zoom controls.
- Touch gestures for the Chart viewer have not been exercised.

## 0.12.1 — 2026-10-26

### Fixed

- Keep the mobile Pages button aligned with the navbar when a native site
  announcement appears above it, including wrapped text and dismissal.
- Give Header controls consistent 150ms ease-in-out color, background, border
  and shadow transitions, disabled when reduced motion is requested. The Search
  icon inherits the control color so its visible glyph follows the transition.

### Added

- Support Quarto's native site-wide announcement bar with wrapping content,
  theme-aware colors and an accessible close control.
- Add English and Traditional Chinese announcement guides and a bilingual
  Gallery demonstration using the native `website.announcement` settings.

## 0.12.0 — 2026-10-25

### Added

- Add the CSS-only native Card component using `.askr-card`,
  `.askr-card-body`, and `.askr-card-title` on nested Quarto fenced divs. The
  heading link is primary navigation; the shell has no click handler, and body
  links retain their native destinations.

## 0.11.0 — 2026-10-21

### Added

- Native Mermaid blocks can opt into the floating viewer, with zoom, pan, Fit,
  on-demand source disclosure and Copy from the authored block.

### Fixed

- The current docs selector lists the actual published 0.10.0 and 0.9.0 sites
  and the frozen 0.3.0 site. A full render generates archive-specific manifests
  for the modern 0.10 and 0.9 selectors and the legacy 0.3 selector.
- The generated 0.3.0 manifest marks 0.3.0 as current and links to version
  homepages; the published 0.3.0 HTML and authored snapshot stay unchanged.

### Documentation

- Documented the archived versions as historical, unmaintained sites and the
  next-release step for preserving the then-current published site.

## 0.10.0 — 2026-10-21

### Added

- Optional site-level `askr.languages` adds a current-tab Header language
  selector, independent of Areas, with validated destinations and an explicit
  current-language marker. The selector is absent unless configured; existing
  navbar language links and all other defaults remain unchanged.
- The Gallery source now builds separate English and Traditional Chinese
  websites with their own navigation and search. Both use the optional selector
  to link their homepages, and both render the same three executable examples.

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
