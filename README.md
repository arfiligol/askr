# Askr

See [CHANGELOG](CHANGELOG.md) for published package changes. PR and GitHub
Release summaries use the same entries.

Askr is the reading page: measure, type, citations, callouts, and Cards. Quiet
Quartz remains the name of the visual theme. `0.13.2` is the current release,
rendered with Quarto 1.10.18. Stable Quarto `>=1.9.38 <1.11` is supported. The
public format is `askr-html`. The 0.10.0 release adds an optional Header language
selector; the control is absent unless configured and does not change existing
defaults. Version 0.12.0 adds the CSS-only native Card component; see the
[Cards guide](components/cards.qmd) and [Validation](VALIDATION.md). Version
0.12.1 supports native site announcements with theme-aware appearance and
accessible dismissal, corrects their mobile Pages layout, and unifies Header
control transitions; see [Announcements](usage/announcements.qmd).
Version 0.13.0 adds a trusted-local-HTML Chart viewer and dedicated bilingual
Image/Chart demonstrations, and unifies text Copy feedback across code, math
and Mermaid. See [Chart viewer](usage/chart-viewer.qmd) and
[Components](components.qmd).
Version 0.13.1 removes the extra space above native code and Mermaid source
while retaining the shared Copy control.
Version 0.13.2 styles filename-labeled code blocks inside one shared frame;
see [Code component](components/code.qmd). It documents Safari clipboard limits
on HTTP previews without changing Copy behavior, and native footer links to
bilingual License pages and third-party notices; see
[Header and footer links](usage/header-footer.qmd).

## Install

Install release tag `v0.13.2`. Quarto's GitHub installer accepts
branch and tag names, not commit SHA modifiers.

```bash
quarto add arfiligol/askr@v0.13.2 --no-prompt
```

```yaml
format:
  askr-html:
    toc: true
    code-copy: true
```

The GitHub installation lives at `_extensions/arfiligol/askr`. It bundles local
Source Sans 3 body text, Schibsted Grotesk title/navigation UI, IBM Plex Mono code,
Lucide icons, the Askr MIT license, and third-party notices. Source Sans 3 is the
intentional version-pinned Source Sans Pro successor adaptation in this
Quartz-on-Quarto candidate.
No CDN, Quartz runtime, Python runtime, analytics, or consumer data is added.

Askr maps Quartz's typography, tokens, rhythm, links, code,
and callout shell onto Quarto's native navbar/sidebar/TOC and runtime. It does
not introduce Quartz's additional callout families or aliases: that would need
a separate public authoring syntax contract.

Display formulas, including labelled equations and tight-list math, include a compact Copy control for their original LaTeX
without dollar delimiters. Successful copies briefly show Copied!; if clipboard
access is unavailable, the selectable source is revealed. Inline math stays
native. Formula display and copy source are derived from the same authored math.

Askr's image viewer is enabled by default through Quarto's `lightbox` settings.
Images and `askr-image-view` buttons open a floating zoom/pan/Fit viewer;
`mode="inline"` provides those controls directly in the article. Native exclusions
and page-level disablement remain available. Protected sites can configure
`askr.logout.href` for an optional Header link; Askr does not manage sessions.
See [Image viewer](usage/image-viewer.qmd) and
[Protected docs and logout](usage/protected-docs.qmd). The public Gallery
leaves Logout disabled.

Native Mermaid blocks can opt into the same floating viewer, with source
disclosure and Copy from the authored block. See the
[Mermaid viewer guide](usage/image-viewer.qmd#mermaid-viewer).

The optional Header language selector was introduced in 0.10.0. Configure
`askr.languages` to add it; it follows supplied links in the current tab and
does not infer destinations or translate content. Existing navbar language
links are preserved; remove duplicates from the native navbar after configuring
Askr. See [Language selector](usage/languages.qmd).

The Gallery includes an English site and a Traditional Chinese edition at
[`/zh-TW/`](https://arfiligol.github.io/askr/zh-TW/). They are separate Quarto
websites with independent navigation and search, connected at their homepages
by the language selector. Run `quarto render` from the repository root to build
both sites. The ignored copies under `zh-TW/_extensions/askr/`,
`zh-TW/components/images/` and `zh-TW/components/references.bib` are generated
build inputs, not vendored sources; maintain the extension and shared assets in
the root `_extensions/askr/` and `components/` directories.

The documentation version menu lists the current 0.13.2 site, the actual
published 0.13.1, 0.13.0, 0.12.1, 0.12.0, 0.11.0, 0.10.0 and 0.9.0 snapshots,
and the frozen 0.3.0 snapshot.
Archived documentation is historical and unmaintained. Before a future release
replaces the site root, preserve the then-current published site under its
versioned path; the build generates selector manifests for each archive's
runtime.

Askr is intended as a reusable design system for direct SCQ-repository
adoption. The theme Sass variables `$grid-sidebar-width` and `$grid-margin-width`
are 264px, `$grid-body-width` and `$grid-docked-body-width` are 630px, and
`$grid-column-gutter-width` is 26px. The root font size is 18px. The normal 630px
measure applies to docked, floating and absent sidebars. Site option
`askr.reading-width: wide` selects a 780px base with the same responsive factors.
Native width escapes and reader mode remain available.

## Scientific reading options

Configure these options at site level in `_quarto.yml`:

```yaml
askr:
  reading-width: wide # normal (default) or wide
  math-copy: true     # true (default) or false
  page-facts:
    - {key: node-role, label: Role}
    - {key: reader-task, label: Reader task}
```

Page facts use flat scalar front matter, for example `node-role: Concept` and
`reader-task: "Compare the response of the coupled modes."`. Only set values
appear, in configured order, below the description; native author/date metadata
stays available. Long values wrap. Labels and values are rendered as text.

| Interface | Effect |
| --- | --- |
| `.askr-symbol-table` | Narrow term column, wide meaning column; fixed wrapping layout on phones |
| `.askr-table-compact` | Tighter table padding |
| `.askr-table-numeric` | Tabular numerals throughout the table |
| `askr-math-copy: false` | Flat page-level Copy opt-out; a page value overrides the site setting |
| `.no-math-copy` | Per-equation opt-out on a wrapping div or native equation attributes |
| `.askr-wide-figure` | Natural-size figure or Mermaid drawing in an accessible horizontal scroll region |

Table classes work on wrapping divs, including captionless pipe tables.
Every table receives a keyboard-focusable labelled scroll region. Copy source
lives in a data attribute; only a denied clipboard request creates selectable
source. See [Tables](components/tables.qmd), [Mathematics](components/mathematics.qmd)
and [Figures](usage/figures.qmd) for usage. The native fenced-div pattern is
documented in [Cards](components/cards.qmd). To migrate existing course cards,
rename their wrappers and title to the classes in that guide, preserve content,
heading level and destinations, then remove only the local course-card CSS
rules. Keep unrelated consumer styles.

The normal width, enabled math Copy, installation format, footer credit and
supported Quarto range retain their defaults. Override `$qdk-border` for Askr
borders and `$qdk-muted-text` for muted text; the former `$border-color` and
`$toc-color` sources now keep their native Quarto roles. Invalid
`askr.reading-width` values or malformed page-fact configuration
raise render errors. For system color preference, set
`format.askr-html.respect-user-color-scheme: true`; for the existing RequireJS
compatibility setup, set `format.askr-html.smooth-scroll: false`.

## Customize and update

Keep consumer overrides outside the installed extension and make their final
token values explicit. A working pattern appears in
[examples/consumer-override.yml](examples/consumer-override.yml) and
[examples/styles.scss](examples/styles.scss); render the consumer to verify it.
For updates, install a newly reviewed version tag and commit the consumer's
updated `_extensions` copy. Do not rely on a moving branch or edit the installed
copy.

## Gallery and credits

The published gallery is [https://arfiligol.github.io/askr/](https://arfiligol.github.io/askr/).
A merge from `develop` into `main` renders and publishes it. Render the source
gallery locally with `quarto render .`; it demonstrates
article/navigation/TOC/mobile reading, native callouts, tables, code, formulas,
and real saved notebook output. See [credits.qmd](credits.qmd),
[THIRD_PARTY.md](THIRD_PARTY.md), and [ASSET_MANIFEST.md](ASSET_MANIFEST.md).
The Gallery footer links to rendered License and third-party notices pages
using Quarto's native links. See [Header and footer links](usage/header-footer.qmd)
for the authoring guide.

## Maintainer planning and delivery

When an external Pro proposal is supplied, assign one primary receiving Askr
Lead per package and treat it as design input. Small fixes do not need Pro.
Before the Lead updates the existing [execution plan](PLAN.md), verify the
repository, branch, full commit SHA, relevant source and working-tree changes,
package contracts, dependencies, and available capabilities. Use Plan Mode when
substantial planning is needed; if unavailable, keep intake read-only until it
is switched. Keep scope, owners, inputs, outputs, dependencies, authorized
checks, failure handling, and Human decisions in the existing plan and
[validation record](VALIDATION.md), not a parallel governance document.

The original Git owner completes coherent work or an independently deliverable
stage using existing checks, stages only exact paths, commits and pushes to
`develop`, then reads back the remote branch and full SHA. Report the repository,
branch, full SHA, paths, result, and anything pending; do not create empty
commits or include another writer's work. Main promotion, merge, release, tag,
deployment, root-pin changes, and resuming paused product work remain separately
authorized. A remote push does not make source readable in ChatGPT; share only
relevant source through an authorized excerpt or attachment.
