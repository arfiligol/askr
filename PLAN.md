# Askr release plan

## 0.8.0 publication authorization — 2026-10-10

Human authorized publication of the presented dual-mode viewer candidate.
Publish the develop checkpoint through a develop-to-main PR, annotated v0.8.0
tag and GitHub Release; complete the existing main/Pages workflows, observe the
public viewer and synchronize the durable child checkout. Update version metadata,
install instructions, Gallery selector and Changelog. Preserve prior runtime
observations for unchanged implementation; freshly render release metadata and
check the exact publication diff. No new tests, root pins, consumers or deployment
configuration changes. Semantic state remains CONVERGING; publication permission
does not claim the unobserved touch/no-JavaScript cases or stabilization.

## Dual-mode image viewer — local candidate, 2026-10-10

Askr Lead owns the extension, Figures and Usage. Implement the Human's dual-mode
plan: SVG/PNG/JPEG, inline interaction and a shared modal engine, existing button
syntax, Quarto image eligibility/paths/captions/groups, focus and state continuity.
CONVERGING; LOCAL CANDIDATE only; no_test_writes. No commit, push, publication,
consumer edits, infrastructure or root pins. Remove the active GLightbox runtime.
Observe actual desktop/tablet/mobile light/dark rendering and operations,
inline/modal state, galleries, keyboard/touch, failures and temporary consumer
installation. Record the actual observation source and remaining limits in
VALIDATION.md; source inspection alone does not prove interaction.

Implementation and local preview are available. Actual mouse/keyboard/modal,
responsive chrome, gallery/failure and resource-path observations are recorded.
Actual touchscreen pinch and JavaScript-disabled browser observations remain
incomplete; this candidate is not labeled fully validated or accepted.

## 0.7.0 publication authorization — 2026-10-09

Human requested removal of Gallery's descriptive right-side Footer text and
publication of the native Header / Footer link package. Keep one Powered by
Askr credit line in Gallery; preserve consumer-authored Footer content.
Complete the develop checkpoint, develop-to-main PR, annotated v0.7.0 tag,
GitHub Release, existing Pages CI/deployment, public rendering observation
and clean durable-checkout synchronization. Do not update consumers, root
pins, infrastructure or durable tests. Use prior unchanged implementation
observations; freshly render release metadata and inspect the corrected
Footer in the local and published site. Publication supersedes only the
prior local-only endpoint; no automated-test stabilization is assigned.

## Native Header / Footer links — local candidate, 2026-10-09

Owner: Askr Lead; base fff9ab1 on develop, clean at intake. Implement the
Human-assigned native navbar.tools and page-footer styling, responsive links
and default opt-out Powered by Askr credit from installed extension metadata.
Authors own all navigation content; no second link configuration, no automatic
commit display, no consumer or root-pin changes. CONVERGING, local preview only;
no commit, push, publication or durable tests. Reuse existing structure.
Observe actual desktop/tablet/mobile light/dark rendering, long labels and
Header fit transition, link destinations/keyboard/Areas controls, footer with
and without authored content, credit disabled and metadata version provenance.
Record render/runtime observations in Validation and changes in Unreleased.

## 0.6.1 publication authorization — 2026-10-06

Human requested the complete publication flow for the adaptive Areas and
RequireJS repair candidate. Deliver a develop checkpoint, develop-to-main PR,
v0.6.1 tag and GitHub Release using CHANGELOG, existing Pages CI/deployment,
public-site observation and clean local synchronization. The prior local-only
endpoint is superseded for this delivery. No root pins, consumer or deployment
configuration changes, new tests or stabilization are assigned. Semantic scope
remains CONVERGING; release authorization is not automated-test stabilization.
Reuse the recorded unchanged core implementation observations; render changed
release documentation, verify exact source/tag identities and observe actual
CI and published HTML/runtime rather than infer deployment from Git.

## 0.6.0 publication authorization — 2026-10-06

The Human requested publication of the optional Logout and native image-viewer
candidate so the NCUAS Private Repo owner can test it. Endpoint: checkpoint
`develop`, promote to `main` by PR, tag/release `v0.6.0`, observe the existing
Pages workflow and actual public routes, and synchronize this durable child
checkout. Publication is authorized; these new semantic scopes remain
CONVERGING, not automatically accepted or stabilized. No durable tests,
root pins, NCUAS integration, infrastructure edits, or real authentication
actions. Retain prior rendered/source-review evidence for unchanged feature
bytes; render release metadata and install instructions, verify exact Git/tag
and deployment identities, and inspect published Usage/Figures. Existing
historical 0.3.0 contents remain unchanged; no new history directory is assigned.
The local-only endpoint below is superseded only for this release delivery.

## Optional logout and native image viewer — local candidate, 2026-10-06

State: CONVERGING; endpoint: LOCAL CANDIDATE and running preview only. The
Human assigned this bounded implementation and observations, not publication
or automated-test stabilization. The Askr owner is the primary writer for
extension, Gallery, Usage, and these receipts. `test_policy = no_test_writes`.

- `askr.logout.href` (required when logout is configured) accepts HTTPS or a
  domain-root `/` path; `label` defaults to Logout. Absence means no control.
  An accessible Header icon navigates the current tab. Authentik/deployment
  owns session state, outpost endpoints, and real logout; Askr owns no account,
  cookie, or session handling. Invalid configuration fails at render time.
- `askr-html` defaults to native `lightbox: auto`. Native `.nolightbox`, page
  `lightbox: false`, linked/inline image treatment, captions, galleries, zoom,
  drag, and close remain Quarto's responsibility. Askr styles controls and
  descriptions and restores focus to the entry that opened the viewer.
- `askr-image-view` accepts exactly one `target` (an existing eligible image/
  figure ID) or `src` (a hidden native image), and optional `label` (View image).
  Bad targets and disabled-Lightbox conflicts fail during rendering; there is
  no image-page fallback. Non-HTML produces ordinary image/figure links.
- Add two Usage pages and real Figures examples using existing public assets.
  Never add private URLs/assets, change pixels, or promise sharper upscaling.

Required evidence: non-executing render; actual desktop/mobile light/dark
opening from image and both button forms, caption/relative-path handling,
native zoom/drag, Escape/close, reading-position and focus restoration;
excluded/linked images; missing-image behavior; temporary independent consumer
with and without Logout, Header layout and exact destinations; invalid-input
and non-HTML render probes; independent correctness/privacy review. One-off
probes/screenshots stay outside the repository. Update VALIDATION with actual
observations and limitations. No NCUAS/NPM/Authentik changes, real authentication
exercise, consumer update, root pin, release, push, CI workflow, or durable test.

## 0.5.0 acceptance and delivery — 2026-10-06

After direct preview iteration the Human confirmed the current candidate and
requested publication ("可以餒！就先這樣。可以發佈了。"). This accepts the
0.5.0 engineering and visual follow-ups below, including copyable display
mathematics with original-sized Copy/Copied! feedback. State: ACCEPTED;
automated-test stabilization is not assigned. Delivery endpoint: checkpoint
develop, promote via PR to main, tag/release v0.5.0, observe existing CI/Pages,
verify public routes and synchronize the durable child checkout. Existing
historical v0.3.0 stays unchanged. No consumer changes or root pins.
Earlier CONVERGING/pending statements below are historical candidate receipts
superseded by this scope-bound acceptance, not additional active candidates.

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

Copyable display mathematics follow-up (2026-10-06): add a shared HTML
component around native standalone display math. A render filter captures
the same Pandoc Math source used for display, without delimiters. A nearby
keyboard-accessible Copy LaTeX button reports clipboard success; clipboard
denial reveals selectable source, never false success. Inline math and
non-HTML outputs remain native. Inspect actual clipboard content and
light/dark desktop/mobile preview. Local candidate only; no durable tests
or publication. Askr owns the wrapper and copy interaction, not math layout.
Human visual refinement: visible button label is Copy; accessible name
remains Copy LaTeX. The subsequent request restores the original .8rem type
and .25rem/.5rem padding, superseding the compact-size candidate.
Human success-feedback refinement: successful copy changes the button to
green-outline Copied! for two seconds, then transitions back to Copy.
Repeated clicks restart the feedback duration. Errors retain the manual-copy
disclosure; reduced-motion preference disables transitions. Observe both
success and automatic restoration in the local preview.

Marked-text follow-up (2026-10-06): retain native mark semantics and the
existing mark background token; inherit paragraph text color and use a muted
amber dark fill. Inspect Prose in light/dark desktop and mobile. Deliver local
preview only; no tests, release or consumer changes.

Callout preview follow-up (2026-10-06): compare headered icon/no-icon native
callouts, normalize shell/header block padding and center icon/title/disclosure
glyph. Preserve titleless padding, nested content and native collapse. Inspect
actual default/minimal, expanded/collapsed, long-title and desktop/mobile
light/dark render geometry; deliver local preview, no tests or release.
The same Human follow-up requests separate unordered/ordered list displays,
each with a hierarchical Structure example in components/prose.qmd. Inspect
their actual three-level list markup and mobile containment, without changing
native list behavior or introducing scientific results. The ordered specimen
uses native numeric/alphabetic/numeric markers at successive levels, as
requested. A further callout follow-up removes native iconless-header negative
bottom margin so the shared icon-derived row also produces equal outer insets.

Human preview follow-up (2026-10-06): refine tab-pane padding and label-to-pane
gap, refine header spacing, and repair Areas disclosure placement. Owner is
the same Askr Lead; affected paths are qdk.scss, token documentation and this
receipt. Preserve label size, native selection/collapse, consumer interfaces
and other candidate behavior. Observe desktop/mobile light/dark spacing and
actual Areas/Pages open/close/outside-click behavior in the rendered browser.
Inspect every header control (Pages, Search, version, theme and Areas), including
its position and resulting disclosure. Header-height self-reference and the
native Pages minimum-height override are implementation defects in this scope.
No test writes, consumer/root-pin change or release is assigned by this
follow-up. Deliver an updated local preview for Human review. Only this visual
delta invalidates the prior spacing/header observation; other source receipts
remain bound to their original identity.

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

## Adaptive Areas and smooth-scroll repair — local candidate

Human-assigned scope: remove the Gallery RequireJS/Zenscroll conflict while
retaining native CSS smooth scrolling; show desktop Areas inline only when
the site title, navigation and actual controls fit. Otherwise use the same
Bootstrap Areas disclosure, without changing the Pages sidebar breakpoint.
Long titles truncate only when necessary, retaining their accessible name.
Recalculate after viewport, font and header-content changes; clear open state,
overlay and hidden focus when changing presentation.

Owner: Askr Lead; primary writer: this local task in the registered child
checkout. Semantic state: CONVERGING; delivery endpoint: LOCAL CANDIDATE and
preview. No release, PR mutation, root pins, consumer or infrastructure edits,
or durable tests are assigned. Record changes in an English CHANGELOG with an
Unreleased section and a factual 0.6.0 summary; future PR/Release summaries
derive from it, not a second release-notes authority.

Observe executed Figures output (RequireJS remains, no mismatch, working
navigation, diagram and viewer). Use temporary consumers with generic long
titles/Areas, with/without version selector and Logout. Inspect desktop,
tablet, phone, light/dark and the actual fit boundary; operate every header
control, Escape, keyboard, link selection and resizing while Areas is open.
Rendered browser geometry/state and console are the observation authority;
source/build success alone does not establish these outcomes. Record findings
in VALIDATION; no private consumer payload enters the repository.

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
