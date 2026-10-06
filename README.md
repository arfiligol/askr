# Askr

See [CHANGELOG](CHANGELOG.md) for published changes and the current Unreleased
candidate. PR and GitHub Release summaries use the same entries.

Askr is the reading page: measure, type, citations, and callouts. Quiet Quartz
remains the name of the visual theme. `0.6.1` is the current release, rendered
with Quarto 1.10.18. Stable Quarto `>=1.9.38 <1.11` is supported. The public
format is `askr-html`. Publication of the optional Logout and native image
viewer was authorized on 2026-10-06 for consumer testing. Those new scopes
remain CONVERGING; publication is not authentication verification or
automated-test stabilization.

## Install

Install the reviewed release tag `v0.6.1`. Quarto's GitHub installer accepts
branch and tag names, not commit SHA modifiers.

```bash
quarto add arfiligol/askr@v0.6.1
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

Standalone display formulas include a Copy button for their original LaTeX
without dollar delimiters. Successful copies briefly show Copied!; if clipboard
access is unavailable, the selectable source is revealed. Inline math stays
native. Formula display and copy source are derived from the same authored math.

Native Quarto Lightbox is enabled by default. Image and optional
`askr-image-view` button entries keep viewing in the article; native exclusions
and page-level disablement remain available. Protected sites can configure
`askr.logout.href` for an optional Header link; Askr does not manage sessions.
See [Image viewer](usage/image-viewer.qmd) and
[Protected docs and logout](usage/protected-docs.qmd). The public Gallery
leaves Logout disabled.

Askr is intended as a reusable design system for direct SCQ-repository
adoption. The theme Sass variables `$grid-sidebar-width` and `$grid-margin-width`
are 264px, `$grid-body-width` and `$grid-docked-body-width` are 630px, and
`$grid-column-gutter-width` is 26px. The root font size is 18px. One docked
track rule in `qdk.scss` uses those variables so the 630px measure stays centered between equal side
columns; consumers retain Quarto's responsive layout, navigation, and runtime
ownership.

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
