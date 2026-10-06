# Askr release plan

## Goal and state

This repository owns the `askr-html` native Quarto HTML extension and its local
gallery. Askr is the reading page: measure, type, citations, and callouts.
Quiet Quartz remains the visual theme name. The **0.4.2 release** targets
Quarto 1.10.18. The public format is `askr-html`. Visual semantics remain
CONVERGING until explicit Human
acceptance; a version number, merge, or tag does not establish semantic
stabilization or deployment.

## Ownership and interfaces

### Active 0.5.0 engineering package (2026-10-06)

Human authorized execution of this package. Owner/writer: Askr Lead in the
registered local child checkout, `arfiligol/askr` on `develop`, starting at
`efab6e77ba91a9d7b71dd2816a4e191769683e89`. State: CONVERGING / LOCAL CANDIDATE.
No Cursor writer is active. Worker leases, when allocated, are disjoint.

1. Restore grouped tabs' visual selection, content, ARIA selection and keyboard
   tab stops to one native Quarto state. Quarto retains switching, grouping and
   persistence; Askr synchronizes accessibility attributes from native active
   classes, including initial load and page return. Preserve .9rem labels and
   current spacing. If a narrow package fix is not viable, report evidence and
   discuss Plan B rather than silently removing groups.
2. Resolve version links relative to the deployment site root, separately from
   version roots and page paths. Manifest `/` means the site root, including
   repository-prefix deployments. Keep the corresponding page and missing-page
   version-home behavior without hardcoded product paths. Use a disclosure
   button and ordinary links, native Enter/Space and Tab/Shift-Tab, Escape with
   trigger-focus restoration, and outside/focus-leave closing without stealing
   outside focus.
3. Exclude controls from prose-link styling. Publish global and component
   design tokens (tabs, callouts, navigation/version/search, code, tables and
   blockquotes) while preserving `askr-html` and existing `--qdk-*` names.
   Sass owns compile-time defaults and derived CSS variables; theme-color reads
   the actual canvas token. Consumer bases remain authoritative at responsive
   sizes. Keep one external gallery version manifest; existing inline consumer
   input remains supported. Document overrides and show real rendered examples.
4. Investigate a Quarto compatibility range rather than locking one patch.
   Keep 1.10.18 as reproducible CI baseline. Inspect native dependencies and
   upstream changes, then observe range boundaries/relevant changed releases.
   Report supported range separately from actually observed versions. No broad
   unobserved 1.x claim, adapter framework or standing CI version matrix.

Required observations: desktop/mobile light/dark grouped tabs via mouse and
keyboard, state/content/ARIA agreement, reload and page return; root and
repository-prefix version routes including history/missing pages; disclosure
focus; a clean independent consumer with token overrides; and selected Quarto
versions. Source and rendered DOM/browser observations support these claims,
not a synthetic PASS label. Temporary probes and screenshots stay outside the
repository. Record interpretation and exact inputs in `VALIDATION.md`. No
durable test writes or general validation framework are authorized.

Independent review covers the frozen reusable/public-interface candidate.
Present the full candidate for Human semantic acceptance before 0.5.0
develop-to-main promotion, tag and actual Pages/public-site verification.
Do not modify consumers, root pins, infrastructure or private artifacts. The
separately received logout-action design context is pending Human discussion
and is not part of this package.

Candidate implementation and the assigned browser observations are complete;
see `VALIDATION.md` for actual inputs, outcomes and limits. The range candidate
is stable Quarto `>=1.9.38 <1.11`, with 1.10.18 retained for CI. Public component
tokens are documented in `usage/tokens.qmd`. Final independent delta review
found no remaining requirement-backed defects. Human acceptance precedes
publication; this is not a released 0.5.0 yet.

#### Human acceptance packet: 0.5.0 engineering candidate

- Scope and behavior: grouped native tabs agree across content, selection,
  ARIA and tab stops, including keyboard/reload/return. Version disclosure uses
  ordinary links and predictable focus; routes remain deployment-root-relative.
  Prose/control styling is separated. Global/component overrides have one
  Sass compile authority and meaningful responsive consumer bases.
- Public interfaces: existing `askr-html`, `--qdk-*` names and version manifest
  fields remain; documented component tokens are added. Candidate Quarto range
  is stable `>=1.9.38 <1.11`, with 1.10.18 as CI baseline. Global radius default
  now actually controls component radii at the existing effective 6px value.
- Ownership: Quarto owns tab selection/persistence, collapse and search;
  Askr mirrors presentation/accessibility and owns tokens. Consumers own their
  styles, content, manifest and hosting. Historical sites are unchanged.
- Failure and edges: missing manifests keep the native brand (or existing
  inline input); same-origin 404 links use the selected version home. Network
  failure retains the original link; modified/external links stay browser-native.
  Invalid Sass/CSS inputs use native compiler/browser behavior, not invented
  replacement values. Native group persistence is unchanged.
- Limits/exclusions: not every Quarto patch was exercised; prerelease support,
  1.11 adapters, scientific output, new tests, consumer changes, root pins,
  logout and infrastructure are excluded. A custom host error document remains
  a consumer/hosting responsibility.
- Completed evidence: actual desktop/mobile light/dark browser operations,
  independent consumer and root/prefix routing observations, selected-version
  renders/source investigation and independent review, detailed in VALIDATION.
- Unresolved semantic decisions: none proposed by the implementation. Human
  acceptance is pending; source candidate is not semantic acceptance.
- Delivery: candidate checkpoint on develop, then after explicit acceptance
  promote main/tag 0.5.0 and observe actual CI, Pages and public routes. The
  Pages-hosted 404 receipt is intentionally pending that delivery stage.

### Current bounded typography adjustment

Reduce native grouped-tabset labels to 0.9rem, following the Human-requested
smaller candidate after the H4 comparison. Preserve Cursor's current tab styling, native
group synchronization, content, and heading sizes. Observe computed H3/H4/tab
sizes and desktop (1440 × 900) and mobile (390 × 844) screenshots, then exercise
the Palace/AEDT group synchronization. The Human requested publication on
2026-10-06: checkpoint develop, promote main, tag v0.4.2, and verify the
existing Pages workflow and public tabset. No consumer update, root pin,
new durable tests, or stabilization are assigned.

The Human retained the 0.9rem label candidate and requested tighter vertical
spacing: reduce label padding to .35rem and remove duplicate first/last child
block margins inside native tab panes. Preserve horizontal spacing and content
padding. Inspect the current preview at desktop and mobile sizes.

The extension is self-contained at `_extensions/askr` and exposes one public
format name: `askr-html`. Its token authority is `qdk.scss`: documented Quarto
Sass variables own color, type, callout color, code, navbar, sidebar, and grid
widths, and `scss:rules` applies the remaining Quartz-derived visuals without
importing a Quartz runtime. Schibsted Grotesk (400/700) owns titles and navigation UI;
Source Sans 3 (400/600 plus italic) is the locally pinned Source Sans Pro
successor used for body text; IBM Plex Mono owns code. Consumers own content, IA, execution,
math engine, viewer behavior, privacy, data, and navigation choices. The
gallery at this repository root is the source-backed evaluation surface.
The shared token authority distinguishes content dividers from quieter layout
dividers in each native theme; manual Markdown `---` is the opt-in content
divider, while sidebar and navigation boundaries use the layout token.
Askr is a reusable design-system candidate for direct SCQ-repository adoption.
Its layout contract is the theme variables `$grid-sidebar-width` and
`$grid-margin-width` at 264px, `$grid-body-width` and `$grid-docked-body-width`
at 630px, and `$grid-column-gutter-width` at 26px. The root font size is 18px. `$sidebar-border` is
false. One `scss:rules` track list restates the docked grid from those
variables so the 630px measure stays centered; Quarto's own formula would add
200px to the body and leave the spare space in a right-hand 5fr column. That
track rule is the residual coupling to Quarto's grid line names.

## Candidate behavior and failure boundaries

The candidate supplies local fonts/icons, Quartz-on-Quarto light and dark
tokens, accessible focus, and native Quarto callout styling. It does not replace Quarto collapse,
navigation, highlighting, copying, execution, or rendering runtimes. If the
extension cannot be resolved by Quarto, a consumer must fix its extension
reference; it must not silently fall back to a remotely hosted asset or a
Quartz runtime. Callout type determines color independent of nesting depth.
The five Quarto-native types are reproduced within their DOM boundary; Quartz's
additional twelve-family showcase/aliases are not exposed because doing so
would require a new authoring syntax transformer or public contract.

## Exclusions

No tests are written while this scope is CONVERGING. A merge from `develop`
into `main` renders this gallery and publishes it to GitHub Pages. Askr does
not deploy a consumer's site. It also does not provide analytics, a separate
search engine, graphs, backlinks, hover previews, robots, emoji, consumer APIs,
or scientific execution policy. The theme styles Quarto's native overlay search.
A website turns that control on with `search.location: navbar` and
`search.type: overlay`. This gallery does that.

## Validation endpoint

Render this gallery and a clean consumer that installs the reviewed version tag,
including a documented Sass override. Inspect desktop/mobile and light/dark
native Quarto behavior, focus, overflow, callout nesting/collapse, navigation,
TOC and code-copy. Record factual outcomes in `VALIDATION.md`; those findings
are not Human acceptance gates.

## Consolidated visual regression checklist

Before a final candidate review, inspect the native Quarto surface in this
order: Callout geometry/rhythm (including nested and collapsed forms), Header
alignment and toggle visibility, Layout tracks with and without a TOC plus
mobile, Divider hierarchy, Typography rhythm, Code surface/overflow/copy, then
the combined light/dark system. This checklist is a CONVERGING review aid, not
an automated test suite or acceptance gate.
