# Askr release plan

## Current candidate — UI stability follow-up after v0.13.3

Semantic state: CONVERGING. Delivery state: CANDIDATE. The Human interrupted
the v0.13.4 release work; release and publication remain PAUSED. The authorized
endpoint is the `develop` candidate checkpoint and bilingual preview, after
Lead UI results are reviewed. No release is authorized.

Keep the accepted Page List density. Serialize the mobile Areas and Pages
disclosures so the last user intent wins; Escape and backdrop closure must
restore focus. Add keyboard support to the callout control. Initialize language
and Logout controls after DOM readiness. Seed the version selector from the
same local versions manifest; runtime external configuration remains
authoritative, and theme version metadata must not be used to infer selector
versions. Add native cross-document main-content fades with a 120ms duration,
enabled by default, disabled by `askr.page-transitions: false`, and suppressed
for reduced motion. Navigation remains native full-page navigation; this is
not an SPA.

Copy errors must be classified and communicated, with a manual source path
available. Preserve code-only compatibility copying without a broad fallback.

✅ Lead UI review and candidate behavior checks are recorded in
[Validation](VALIDATION.md#current-ui-stability-candidate), including the final
bilingual render after the window-capture, breakpoint, and focus fixes. ⏳ Lead:
deliver the authorized `develop` candidate checkpoint and record its full
remote SHA in the private receipt. Human visual review remains pending. The
v0.13.4 release and publication remain paused.

## Askr v0.13.3 — Page List current-page highlight — 2026-10-28

Semantic state: ACCEPTED. Delivery state: CANDIDATE. The Human authorized
publication of the accepted Page List highlight.

This release highlights the current Quarto Page List item with a theme-aware
row tint and semibold label. The highlight follows Quarto's native active-page
state. The release also preserves the published v0.13.2 Gallery under
`/v0.13.2/` and updates the bilingual version guides.

✅ The actual published v0.13.2 site was copied from `gh-pages` commit
`ccac30acfab164ff2f8ba4db9be7efef7d5beb1a` into `v0.13.2/`: 244 files,
26,612,518 bytes. The source-tree SHA-256 manifest is
`7bd39706a24f6385ec9dd0704e4929970bb6279e37a3940d5a1d4636c2001b67`.
See [Validation](VALIDATION.md) for the exact paths and pending checks.

✅ The default full-site render passed for 111 English and 32 Traditional
Chinese inputs. Archive bytes match the published source exactly. Light/dark
Page List review and the existing mobile row check passed; see [Validation](VALIDATION.md).

⏳ Lead: complete main CI, install the released tag in a fresh Quarto consumer,
and publish the release.

## Askr v0.13.2 — filename code frames and release docs — 2026-10-28

Semantic state: ACCEPTED. Delivery state: PUBLISHED.

This release added the single-frame Quarto filename style and its bilingual
example; native footer guidance and bilingual HTML License pages; and Safari
HTTP-preview clipboard guidance. The Copy implementation and clipboard payload
were unchanged. The typography preview was excluded. Existing documentation
changes were `0beff39` (footer and License) and `85708df` (Safari clipboard note).

✅ Root preserved the actual published v0.13.1 site at `/v0.13.1/` from deployed
`gh-pages` commit `bff50282f12d71dfb9ebaa34f8c6979160230452`: 241 files,
26,374,137 bytes, with hashes verified. Existing browser QA at 390px and 841px
confirmed actual Copy/paste, callout collapse, and one filename/source frame;
see [Validation](VALIDATION.md).

✅ The bilingual 111-page English and 32-page Traditional Chinese gallery
render, main Publish run, Pages deployment, fresh v0.13.2 install and consumer
render completed successfully. See [Validation](VALIDATION.md).

## Askr v0.13.1 — Copy source spacing hotfix — 2026-10-27

Remove the shared Copy control's extra top padding from native code blocks,
including displayed Mermaid source. Keep the text Copy button, success/reset
behavior and existing source content. Preserve the actual published v0.13.0 site as a
historical snapshot before replacing the root site.

✅ The actual published v0.13.0 site is preserved as a 241-file snapshot; the
manifest, build resources and bilingual version guides retain it under `/v0.13.0/`.
The Human authorized this hotfix release. ✅ Lead review, exact-candidate
release render, archive identity, source spacing and Copy placement checks are
complete. ⏳ Lead: complete promotion, main CI, tag installation and public-site
review.

## Askr v0.13.0 — viewers and shared Copy release candidate — 2026-10-27

Give static images and interactive HTML charts separate Component pages in
English and Traditional Chinese. Move the image-viewer examples out of Figures
while keeping the existing `#image-viewer` section as a link to the new page.
The image viewer retains Askr zoom, pan and Fit. The chart viewer embeds trusted
local HTML with its own chart controls and offers an inline frame or a
button-only floating entry through `askr-chart-view`.
The floating toolbar contains Open source and Close; chart operations stay
inside the exported chart.
The Components sidebar groups both viewer pages under a native top-level
Viewers section (檢視器 in Traditional Chinese). The section collapses by
default and opens for the current page; page URLs remain unchanged.

The chart frame follows the Askr theme; the embedded chart retains its authored
colors. Inline and floating frames have independent state. The public demo is
a self-contained Plotly 3.1.0 sine curve with a retained MIT license and pinned
rebuild script. Plotly is bundled only in that Gallery HTML, not the extension.

✅ 2026-10-26: non-executing English/Traditional Chinese renders, desktop/mobile
interaction, chart controls, independent frame state, keyboard closing, failure
recovery and static-image state continuity were checked. See [Validation](VALIDATION.md).
✅ The light/dark visual review is complete.
✅ The simplified floating toolbar and keyboard return behavior were rechecked.
✅ The native bilingual Viewers sidebar grouping and current-page identification
were checked. The Human authorized this scope and the shared text Copy controls
for the v0.13.0 release on 2026-10-27.

Copy uses one text button on code, display math and Mermaid source: `Copy`
changes to `Copied!` with a green outline, then returns after about two seconds.
Retain Quarto code-copy availability and existing math exclusions. The source
worker integrated the previously authored Copy changes, and the Lead verified
the combined exact release candidate before promotion.

✅ The v0.12.1 snapshot preserves the actual published Pages tree; the current
selector and version guides now describe v0.13.0 with that archive retained.
✅ 2026-10-27: the exact combined release tree passed the default bilingual
render, real clipboard checks, Copy feedback/reset and archive identity checks.
⏳ Lead: complete promotion, main CI, tag installation and public-site verification.
The release remains pending; consumer adoption stays with consumer owners.

## Native announcement support — v0.12.1 release candidate — 2026-10-26

Use Quarto's existing `website.announcement` as Askr's supported site-wide
notice. Askr owns its wrapping, semantic colors and accessible close control;
authors keep the native content, icon, type, position and dismissal settings.
For persistent development-version warnings, the guide recommends a warning
notice with dismissal disabled. The Gallery demonstrates the same notice in
English and Traditional Chinese using public example text.

The mobile overlap came from the Pages control occupying the top of the header
while an above-navbar announcement occupied that same space. The implementation
keeps Pages aligned with the navbar after wrapping, dismissal and viewport
changes, while the native header controls article, sidebar and anchor offsets.
Header controls share 150ms ease-in-out color, background, border and shadow
transitions; reduced-motion preferences disable these transitions.

✅ 2026-10-26: local implementation, Lead browser checks and the full bilingual
release render are complete;
see [Validation](VALIDATION.md#native-announcement-support--v0121-release-candidate--2026-10-26).
The Human authorized release of this scope as v0.12.1 on 2026-10-26. Retain
the actual published v0.12.0 documentation as a versioned snapshot.
⏳ Lead: complete promotion, main CI, GitHub Release, Pages deployment and a
fresh tag installation before marking publication complete. Consumer adoption
remains with each consumer owner.

## Native Card component — v0.12.0 release candidate — 2026-10-25

The Human authorized the v0.12.0 release endpoint for the Card component. The
candidate interface uses `.askr-card`,
`.askr-card-body`, and `.askr-card-title`. Its heading link is the primary
navigation; the shell has no click handler, and links in the body retain their
own native destinations. `.unlisted` excludes the real heading from the page
table of contents without changing its author-chosen level.

The English and Traditional Chinese guides provide the exact authoring source,
the class mapping and CSS migration note, and two vertical Gallery examples
linked to existing Usage pages. Their short and long CJK titles make wrapping
visible; the cards contain no scientific examples or results. Inputs
are the requested linked-heading behavior, existing theme tokens, and those
Usage pages. The stylesheet implementation must use existing tokens and remain
CSS-only; its rules are a dependency owned separately from this documentation
package. Existing course-card migration renames only the outer, body, and title
classes, preserves heading text, level, link target, and description content,
then removes only local CSS scoped to the old course-card classes.

Scope includes the Card rules in `_extensions/askr/qdk.scss` under its separate
stylesheet owner, plus the two Cards pages, their navigation entries, links
from the component overviews and README, and this package documentation. This
documentation work package does not edit the stylesheet. Do not change
consumer repositories, root pins, JavaScript, or dependencies. Semantic state:
CONVERGING. Delivery state: CANDIDATE; the Human-authorized endpoint includes
the exact-path `develop` checkpoint, main PR, v0.12.0 tag/release, Pages
publication, and installation handoff. The separate shared Copy follow-up
remains Unreleased and is not part of v0.12.0.

The Lead completed the Card-only renders and Chromium review and the full
bilingual site render recorded in `VALIDATION.md`. Before completing the
release, the Lead still owns main PR/CI, v0.12.0 installation validation, Pages
publication, and deployment/readback. Add no new tests and execute no notebooks
or scientific content.

If the markup cannot retain native heading and link behavior, return the issue
for direction instead of adding JavaScript or making the full card clickable.
Visual acceptance and completed publication remain separate outcomes.

## Shared text-copy feedback — included in v0.13.0 release scope

This local follow-up applies one text-copy interaction to displayed-math
source, Mermaid source and native code blocks. Keep the text button labelled
`Copy`; after a successful copy, change that same button to `Copied!` with a
green outline for about two seconds, then restore `Copy`. Use the same success
state and animation across all three surfaces. Replace the native code-copy
icon and tooltip while retaining Quarto's `code-copy` availability setting.

The source worker owns runtime integration; the Lead reviews the combined
candidate and verifies clipboard payload, success/reset and readable controls
in light/dark desktop/mobile layouts. The Human authorized delivery with the
v0.13.0 viewers release on 2026-10-27. Earlier review outcomes remain in
`VALIDATION.md`; publication is recorded only after the release checks pass.

## Previous: Askr 0.11.0 Mermaid viewer — published 2026-10-21

The Mermaid viewer and the v0.10.0 site snapshot shipped in the published
[v0.11.0 GitHub Release](https://github.com/arfiligol/askr/releases/tag/v0.11.0).
The tag and release remain unchanged. The viewer uses one opt-in wrapper around
a native Mermaid cell and the existing Askr modal; its source and browser
observations are recorded in `VALIDATION.md` and the
[Mermaid viewer guide](usage/image-viewer.qmd#mermaid-viewer). The current
shared-copy follow-up does not amend that published package.

## Previous: Documentation version archive correction — 2026-10-21

At the time of the docs-only archive correction, 0.10.0 was the current
published site. The correction kept the actual published 0.9.0 site as
`v0.9.0/`, retained the frozen 0.3.0 snapshot and left the extension runtime,
installed version and public options unchanged. The `v0.9.0/` source snapshot
comes from the actual Pages tree at
`32b83b78756c09dbcf7fd378996cd1170cfdbc48`; the full root render publishes
that directory and generates compatible selector manifests. The 0.9.0
manifest uses one root relative to its own site directory for current-version
matching and fixed homepage links for navigation; the frozen 0.3.0 manifest
uses its `/askr/` origin prefix and fixed version-home links. Both HTML
snapshots remain unchanged. The published 0.11.0 package preserved the actual
0.10.0 site under `/v0.10.0/` before replacing the current root; it did not
add a second 0.10.0 entry.

Historical sites are unmaintained. The docs-only archive correction shipped
with v0.11.0; see `VALIDATION.md` for its render, browser and Pages receipt.
The Lead retains Git, Pages and publication delivery authority.
Semantic state: CONVERGING; delivery state: PUBLISHED.

## Published: Askr 0.10.0 bilingual release — 2026-10-21

The Human authorized publication of Askr 0.10.0 and its later LCDH adoption.
This package adds the optional Header language selector and an actual bilingual
Gallery. English remains at the existing site root; a separate Traditional
Chinese Quarto website is built under `/zh-TW/`, with its own navigation and
search. Each site's `askr.languages.current` is explicit, and both selector
entries link to the two site homepages.

The root Quarto project excludes `zh-TW/` from its own render. On a full site
render, its post-render helper stages the current Askr extension and shared
image/bibliography assets into ignored generated paths, then renders the child
website into `_site/zh-TW/`. The three executable examples shared by both sites
live once in `_includes/`; translated documents include those same cells
instead of owning copies of executable code.

Implement the site-level `askr.languages` option in Askr's Header. Its
`current` code must match exactly one entry in `items`; provide at least two
entries, each with a unique nonempty scalar `code`, nonempty scalar `label`,
and an HTTPS absolute URL or domain-root `/path` `href`. Reject
protocol-relative and whitespace-containing destinations, and escape every
configured string.

Place a square language icon beside the existing Header tools. Give it the
accessible name and tooltip `Language: <current label>`; keep it available on
narrow screens independently of Areas and reserve its measured width in the
Header layout. The menu uses Askr's light/dark tokens. Each normal link uses its
configured `href` in the current tab, with `lang`, `hreflang`, and a visible
current marker plus `aria-current`. Omit the control when the option is absent;
JavaScript-disabled output contains no dead button. Askr does not infer
destinations, persist language choices, translate content, or alter search.
Existing author-provided navbar language links remain in place; guidance tells
authors to remove duplicates after configuring Askr.

Askr owns the extension, Usage docs and bilingual Gallery build. The public
Gallery is configured for its own English and Traditional Chinese homepages;
consumer repositories, root pins and the frozen `v0.3.0/` remain outside this
package. `v0.3.0/` remains the historical English snapshot.

The corrected full root/child render passed with 106 English and 27 Traditional
Chinese pages, and all three shared cells executed in both. The 27 Chinese pages
have no broken static links; the English and Chinese search indexes contain 211
and 89 entries. The Lead also observed desktop language navigation, four
separate page sidebars, Chinese-only search results and the Figures viewer.
Detailed observations are in `VALIDATION.md`. The 0.10.0 release, Pages
deployment and installation handoff are complete.

Semantic state: CONVERGING. Delivery state: published as `v0.10.0`; the later
documentation archive correction is a separate package.

## Historical work packets

## Historical local-candidate packet — Optional Header language selector — 2026-10-21

The earlier local-candidate packet preceded the Human's publication
authorization and the bilingual Gallery assignment. Its feature contract and
temporary-consumer observations remain historical context; its local-only
endpoint and publication restrictions are superseded by the current package
above.

## 0.9.0 dense scientific reading — 2026-10-21

Ship the Human-assigned P0 reading improvements: accessible scrolling tables,
consistent normal/wide measure, compiled border tokens and contrast, compact
search-clean equation copy, native semantic blocks, flat page facts, and natural
wide figures. Askr Lead owns `quarto-design-kit/**`; consumers, root pins and the
frozen `v0.3.0/` remain outside this package. Runtime assets stay local.

Required observations are Quarto renders, a light/dark compiled public-token
audit and actual browser reading/keyboard/copy/layout behavior, including scoped
temporary probes outside the repository. Record results in `VALIDATION.md`.
No durable tests, new gallery fixtures, CI workflows, scientific execution or
optional SVG/Mermaid image-viewer extension are assigned.

Delivery endpoint: develop checkpoint, reviewed main promotion, `v0.9.0` release,
existing Pages publication, public observation and durable-child synchronization.
The Lead retains Git/publication authority. Semantic state: CONVERGING;
implementation and publication do not imply Human acceptance or stabilization.

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
