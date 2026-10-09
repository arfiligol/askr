# Changelog

User-visible package changes are recorded here. PR and GitHub Release summaries
derive from these entries; an Unreleased entry is not a published release.

## Unreleased

No pending package changes.

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
