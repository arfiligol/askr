# Candidate validation receipt

## 0.5.0 publication authorization — 2026-10-06

The Human accepted the iterated candidate and requested publication. Release
metadata, install instructions and current manifest now name 0.5.0. The final
101-page non-executing render completed on Quarto 1.10.18; the known figure
specimen warning about absent light/dark cell output persists in this mode.
The existing Pages workflow performs its normal render; its CI/deployment and
public-route observations are delivery receipts, not inferred from this build.
No automated tests were added and no root/consumer revision was changed.

## 0.5.0 engineering candidate — 2026-10-06

### Human preview spacing/navigation follow-up

Copyable display mathematics: focused non-executing Mathematics render completed.
The final Human refinement restores .8rem type and .25rem/.5rem padding,
keeping the short Copy label. Actual rendered type/padding were 13.6px and
4.25px/8.5px at the current desktop scale. A real click was observed as
Copied! with is-copied styling, then returned to Copy with empty live status
after its two-second timer. Green-outline feedback uses the existing tertiary
token; reduced-motion disables color transitions. This supersedes compact
button sizing measurements below.
Two standalone display formulas have Copy LaTeX buttons. The
later Human refinement changes visible labels to Copy and reduces type and
padding. Actual rendered buttons measured approximately 39 × 21px; clicking
the compact button still produced Copied. Accessible names remain Copy LaTeX.
Inline formula remains native. Real button clicks produced Copied only after
the browser clipboard write resolved. Captured short source is
`\omega_r = 2\pi f`, with no dollar delimiters; the long source retains its
TeX commands. The automation clipboard read returned empty, so external
paste destination content is not independently verified and should be tried
by the Human. Clipboard-denial disclosure is implemented but was not forced
in this browser observation. At 1440 × 900 and 390 × 844 the page rendered;
mobile light/dark keeps long mathematics in its local horizontal scroll area.
No console errors/warnings observed. Source review identified textarea's
leading-LF parsing behavior; the transport now supplies its own sacrificial
LF and encodes CR. Screenshots remain outside the repository. No tests added.

Marked-text follow-up: native mark kept a black foreground in both themes.
Askr now inherits paragraph foreground and changes only the existing dark
mark token to #e5c76b33. Actual Prose at 1440 × 900 and 390 × 844 showed
dark foreground #d4d4d4 on rgba(229,199,107,.2), against canvas #161618.
Light mode retained its yellow fill and inherited #4e4e4e foreground.
Theme switching was operated; no console errors/warnings were recorded.
Screenshots were kept outside the repository. This is local candidate
evidence, not publication or arbitrary-browser coverage.

Additional Human follow-up: icon/no-icon callout comparison found native
minimal-shell block padding and disclosure utility padding causing unequal
insets, plus a legacy -3px chevron translation. Headered shells now have no
second block inset, all title margins are zero, and headers share a minimum
row size derived from existing icon and padding tokens. Disclosure utilities
are neutralized while native collapse ownership is unchanged. Titleless
body padding remains outside this selector.

At 1440 × 900 the icon warning and iconless minimal caution headers both
measured 59px with 18px upper/lower padding; at 390 × 844 both measured 46px
with 12.8px padding. Expanded/collapsed states were operated, and their
icon/title/button centers coincided apart from subpixel rounding. Multi-line
title observation exposed the remaining native -1px title margin, which is
now zeroed for all appearances. Both light/dark render observations are scoped
to these gallery callouts, not a guarantee for arbitrary consumer content.

The next Human screenshot exposed a separate native simple/iconless header
negative bottom margin (-3.24px at 1440px). It reduced the collapsed outer
shell to 57.77px despite the shared 59px header, compared with 61px for the
icon warning. The appearance-specific header margin reset now gives both
collapsed shells 61px at 1440 × 900, and 48px at 390 × 844 (46px header,
12.8px upper/lower padding). The mobile dark canvas was observed as #161618;
both title centers exactly matched their row centers. Native collapse was
operated, and the long-title margin computed as zero. Independent read-only
review found no concrete defects in this final delta; SCSS identity:
`5ad8994400bb9cf9bfbe76bb5bcbbc153eee1021481f751045a5a6a407aa9521`.

The Prose gallery now separates Unordered list and Ordered list, each with
a Structure example. Actual markup includes ul/ul/ul and ol/ol/ol hierarchies;
mobile document width remained 390px. Definition lists retain their own
section. These are native structural specimens, not scientific run outputs.
The subsequent alternating-marker request uses native authored markers:
the actual ordered DOM computed decimal → lower-alpha → decimal, with types
1 → a → 1. This does not impose an automatic depth rule on consumer lists.
Prose source identity after this change:
`e260609c9bf6d147d6b40058eb9b73aecb2da38049c4fae46550836b5789ead6`.

The Human subsequently requested tighter tabset padding, coherent header
padding, repair of Areas expansion and inspection of all header controls.
This local visual delta follows candidate `dbc3d3c2fc47e1ae16a535560cfb9ba02fece764`;
it is not accepted or published. Prior implementation receipts below retain
their original scope and identity, except header/tabset spacing now superseded
by these observations. No durable tests were added.

Browser inspection exposed an invalid self-reference in `$qdk-nav-height`,
making the computed CSS variable empty. At 390 × 844 the header shrank to its
31.62px controls and menu positioning lost its height reference. The default
is now the documented 3.4rem. Pages also inherited native `min-height: 100%`,
making its 844px panel extend below the viewport from its 54px top; resetting
that minimum fixes the panel while native collapse still owns open/close.

Actual Quarto 1.10.18 non-executing render and browser operations covered
390 × 844, 900 × 900 and 1440 × 900. Tab-pane padding is now .65rem/.8rem
(10.4px/12.8px mobile, 11.7px/14.4px desktop), label-to-pane gap .5rem
(8px/9px), and .9rem labels/.35rem label block padding remain unchanged.
`--qdk-tab-content-padding` is a documented Sass-derived consumer token.

At 390px all five header controls (Pages, Search, version, theme and Areas)
shared y=11.39px and height=31.62px inside the 54.40px header, giving equal
upper/lower breathing room. The Areas panel settled at x=134px/y=54.40px,
width=256px, extending to the viewport bottom. At 900px it settled at
x=612px/y=61.20px, width=288px, with all five area links visible below the
header. Pages settled at top=54px/bottom=844px instead of overflowing.
At 1440px the header measured 61.20px and brand/search/theme controls and
navigation text were visually centered, without extra native navbar padding.

Operated both themes, Areas open/button-close/backdrop-close, Pages opening,
Areas/Pages mutual closing, version disclosure opening/Escape, Search
opening/Cancel, and native theme toggle. In the observed dark mobile view both
menus remained correctly placed. Native Home switched paired tabsets to
Palace after the existing next-frame native group bridge. No mobile document
overflow was observed at 390px. Temporary screenshots remain outside the repo.
Non-executing figures still have the previously disclosed missing cell outputs;
this does not claim scientific figure execution. Independent read-only delta
review found no requirement-backed defect or private-context leakage. Reviewed
SCSS SHA-256: `1ed3c70bd57080cd0802992d50a7a5e54eae399a5d9f352cc02411c2e463b7b8`.
The gallery was refreshed without execution so navigation shares the corrected
styles. Desktop dark version/Search opening and Escape/Cancel closing were
also operated; screenshot and geometry remained within the viewport.

Scope: PLAN's active 0.5.0 package, based on develop
`efab6e77ba91a9d7b71dd2816a4e191769683e89`. Semantic state is CONVERGING;
Human acceptance, promotion, tag and deployed-site observation are pending.
These are observed technical results, not agent-created acceptance thresholds.

### Inputs and actual operations

Quarto 1.10.18 rendered the 101-page gallery with `quarto render --no-execute`.
The paired tabsets in `components/figures.qmd` were operated in an actual
browser at 1440 × 900 and 390 × 844, in light and dark modes. This package
did not execute notebooks or scientific models. The figures page reports
missing light/dark cell outputs under this non-executing render; no fresh
scientific-output or full-gallery figure-completeness claim is made.

An independent temporary website installed the candidate extension into
`_extensions/arfiligol/askr`, with its own navigation, paired native backend
tabsets, callouts, code, table, styles and external version manifest. It was
rendered separately, then served at both a site root and a repository prefix.
Its authored previous-version home is a routing specimen, not a fabricated
historical release. Temporary inputs and screenshots remain outside this repo.

### Grouped-tab state and keyboard behavior

Mouse selection, ArrowLeft/ArrowRight and Home/End were operated in native
tabs. Both groups settled on the same visible Palace/AEDT panels, active
classes, `aria-selected` values and tab stops: active true/0, inactive false/-1.
Reload restored the native persisted selection, and navigation away followed
by browser Back restored matching content and attributes. Native Bootstrap
keyboard activation does not invoke Quarto's click-only group synchronizer;
the candidate routes that activation through the native click handler on the
next animation frame. The immediate pre-frame state is not a second maintained
selection state. Quarto continues to own group storage and panel selection.

Gallery labels measured 16.2px at desktop and 14.4px at mobile, preserving
0.9rem. Selected/unselected weights are 600/400; prose-link emphasis no longer
leaks into the inactive controls. Default label block padding remains .35rem.
Screenshots showed paired groups in both themes without horizontal document
overflow at the observed mobile width.

### Version paths and disclosure focus

For the independent consumer, manifest `/` resolved to the deployment site
root rather than origin root. The prefix route `/askr/nested/components.html`
produced `/askr/previous/nested/components.html`; a root deployment produced
`/previous/nested/components.html`. Query and fragment were preserved in
corresponding-page links. Clicking the missing corresponding page received
an actual 404 and navigated to the selected version home, `/askr/previous/`
or `/previous/`. At the previous home, the disclosure identified the previous
version and linked back to the current site home. No product path is hardcoded.

Enter and Space opened the disclosure. Tab moved to its ordinary links;
Shift-Tab returned to the trigger. Escape closed it and restored trigger
focus. Tab out of the final link and clicking a tab outside closed the
disclosure without moving focus back from the outside control. The links
are not listbox options; current version uses `aria-current`.

The gallery's custom 404 route was source-reviewed and rendered. Its automatic
Pages-hosted error-document behavior still needs the authorized public-site
observation after release; the temporary static server does not emulate Pages.

### Token authority and independent consumer

Consumer Sass body width of 680px produced a 680px main at 1440px and 748px
at 1920px (the existing 1.1 responsive scale), while the public base stayed
680px. At 390px the main fitted 338px and document width stayed 390px.
Removing duplicate extension grid metadata made the Sass default authoritative.
Quoted font-family lists compiled and computed as Source Sans 3, rather than
an invalid unquoted family falling back to Times.

Consumer tabs used .85rem labels/.3rem block padding: 15.3px/5.4px at desktop,
13.6px/4.8px at mobile. Callout radius computed as the consumer's 8px. Table
cell padding computed as .35rem/.7rem: 6.3px/12.6px at desktop and 5.6px/11.2px
at mobile. Specific selectors were necessary to beat Quarto/Bootstrap cell
padding. Default table padding and 1px header rule preserve the previously
effective native values, and the header's existing muted color is retained.

Consumer canvas and theme-color matched after native toggles: light #f3f5f7,
dark #20252b. Stylesheet-load handling prevents the meta value from retaining
the old palette while the alternate sheet loads. Search frame corners and
dark copy-control declarations now consume their published component tokens;
these two additional fixes were identified by independent source review.

### Quarto compatibility evidence

Candidate range: stable releases `>=1.9.38 <1.11`; CI baseline remains 1.10.18.
Actually rendered and operated: stable 1.9.38 and 1.10.18, plus diagnostic
prerelease 1.10.16. Isolated official macOS archives were used without changing
the installed Quarto. SHA-256 matched the official release API:

- 1.9.38: `47089a5020cfb41981ba0d4b46e110edfa608722aea45ef248e14efba6d6b18a`
- 1.10.16: `3413aaa38f65862ea3af16ef7a0ce41539d89cc9386becdd9f2a3adcf77ada0e`

At 1.9.38 and 1.10.16, three-page independent consumers rendered successfully.
Browser observations covered grouped-keyboard selection, restored ARIA/tab
stops after reload, disclosure, desktop/mobile widths and token overrides,
and light/dark canvas/theme-color agreement. Browser Back was also operated
on 1.10.16. These observations do not cover every intervening patch.

Official source comparisons found native `tabsets.js`, `panel-tabset.lua` and
Bootstrap 5.3.1 identical at inspected 1.9.38/1.10.0/1.10.18 boundaries.
Relevant intervening changes included 1.10.4 secondary-sidebar logo handling,
1.10.15 URL query/fragment matching, 1.10.16 Sass default parsing and 1.10.17
Pandoc/Sass updates. The 1.10.18 render exercises the later compiler baseline.
1.11 changes theme/navigation controls and is excluded pending investigation.
No standing CI matrix, adapter framework or prerelease-support promise is added.
Sources: [native tabs](https://github.com/quarto-dev/quarto-cli/blob/v1.10.18/src/resources/formats/html/tabsets/tabsets.js),
[tabset markup](https://github.com/quarto-dev/quarto-cli/blob/v1.10.18/src/resources/filters/customnodes/panel-tabset.lua),
[1.10 changes](https://github.com/quarto-dev/quarto-cli/blob/v1.10.18/news/changelog-1.10.md),
[1.11 changes](https://github.com/quarto-dev/quarto-cli/blob/v1.11.5/news/changelog-1.11.md).

### Review and limits

Independent read-only review covered the reusable implementation, public
interfaces and privacy boundaries. It identified copy-control/search-token
inconsistencies; owner observations additionally identified font quoting,
grid precedence, site-root and table specificity issues. All have been corrected.
Final independent delta review found no remaining requirement-backed defects.
It reviewed source/receipt correctness and privacy, not a duplicate browser run.
Reviewed implementation SHA-256 identities: `theme-color.html`
`e834378e207b2f0df667d9d4e9042e17e3fc4fd88bac17336ec6aa690fec3417`,
`qdk.scss` `334de632781e7cb1b76a3467b2e6f95b64d788d9d791d99cbcce670970b54b82`,
`qdk-dark.scss` `81ce9e5e4f1627f8843835d77b6dbc8a176f05248d0e8353ac656317861069c7`.
Owner source/diff inspection and scoped non-executing renders also completed.
No durable tests, consumer revisions, root pins, historical snapshot mutations,
infrastructure changes or new logout feature are part of this package.

## 0.4.2 grouped-tabset update — 2026-10-06

Quarto 1.10.18 rendered `components/figures.qmd` without execution. Native
grouped tabsets were inspected at 1440 × 900 and 390 × 844: labels measured
16.2px and 14.4px respectively (0.9rem); label vertical padding is .35rem.
First/last pane block margins are zero, avoiding duplicated paragraph spacing.
Both groups' visible content follows a Palace/AEDT selection. The native group
runtime leaves the second group's ARIA selection attributes inconsistent with
its active classes; that pre-existing runtime issue is not modified here.
No durable tests or consumer dependency updates were assigned. The Human
requested publication of this visual candidate; no stabilization is claimed.

Date: 2026-09-23. Semantic state: **CONVERGING**. These observations are
technical evidence, not Human acceptance thresholds or visual acceptance.

## Toolchain and scope

- Quarto `1.10.18` rendered the local gallery.
- A temporary, isolated Python 3.13 virtual environment supplied Jupyter only
  for local gallery validation; it is not a repository or extension dependency.
- `notebooks/simple-output.ipynb` was executed by `jupyter nbconvert --execute
  --inplace`; its saved output is `Saved notebook output: [3, 5, 8] -> 16`.
- No durable tests, CI configuration, release artifacts, or deployment files
  were added.

## Commands and factual results

```bash
PATH=/tmp/qdk-render-venv/bin:$PATH quarto render .
```

Succeeded: all gallery pages rendered, including executed
`notebook-output.qmd`; `_site/index.html` contains
`#mobile-callout-inspection-target` and the rendered output contains the saved
notebook result.

The Human-selected Quartz-on-Quarto revision also rendered successfully with
the same command: compiled light/dark styles contain the Quartz token values,
and the gallery ships local Schibsted Grotesk 400/700 alongside Source Sans 3
body and IBM Plex Mono code faces.

After browser review identified Quarto default-callout specificity leakage, the
candidate was rerendered with `.callout.callout-style-*` shell overrides:
compiled CSS confirms the uniform 1px semantic-alpha border, 6.3% semantic
shell fill, transparent header, 5px radius, 1rem horizontal shell padding, and
Quartz warning `#db8942`. A browser surface was unavailable to this worker for
a replacement screenshot; owner browser review remains the visual receipt.

The gallery's native titleless/iconless simple callout now renders as
`title=""` plus Quarto's `no-icon` DOM class, with no title container; Askr
explicitly hides that native no-icon container. Dark navigation surfaces now
resolve through `--qdk-canvas` and `--qdk-border`; clean-consumer installation
and Sass override rendering were rerun successfully.

Nested final children now receive an explicit `1rem` bottom margin through a
type/appearance-specific selector. Collapsible Quarto headers use `.75rem`
block padding while ordinary headers retain `1rem`; title, icon, and chevron
are direct flex items with `align-self: center`. These are authored geometry
values verified in compiled CSS and DOM; browser-computed light/dark geometry
remains an owner-side visual receipt.

The dark-theme code correction was rerendered in `qdk-dark.scss` only. Quarto
switches theme stylesheets without changing the body class, so its compiled
dark-only selectors are intentionally unprefixed: `div.sourceCode` and source
`pre` resolve to `#1f1f22` with a `#393639` border and `#d4d4d4` plain text.
Pandoc comments, keywords/operators, strings/numbers, functions, and
builtins/types resolve respectively to `#8b949e`, `#ff7b72`, `#a5d6ff`,
`#d2a8ff`, and `#79c0ff`. The light stylesheet has no corresponding rules, so
the light code palette remains unchanged. Browser-computed values and
copy-control icon pixels remain owner-side visual inspection evidence.

The common code-shell rule now assigns the visible border and 5px radius to
`div.sourceCode` (with `pre` retained as a standalone fallback). For Quarto's
normal nested structure, `div.sourceCode > pre.sourceCode` and its direct
`code.sourceCode` are explicitly transparent with zero border/radius/shadow;
the dark layer applies `#393639` only to that outer wrapper. Gallery and clean
consumer rendering were rerun after this correction.

The common stylesheet also clears Quarto's automatic H2 border and bottom
padding (including heading pseudo-elements) without depending on the active
theme. Explicit `hr` elements instead render as a 1px top border using
`--qdk-border`; `components.qmd` demonstrates the opt-in native Markdown
sequence of a heading, blank line, and `---`. Browser-computed confirmation in
both stylesheet modes remains owner-side visual evidence.

The divider hierarchy was rerendered with explicit theme tokens. Light content
and layout dividers are respectively `rgba(43, 43, 43, .18)` and
`rgba(43, 43, 43, .08)`; dark values are `rgba(212, 212, 212, .24)` and
`rgba(212, 212, 212, .10)`. The manual `hr` uses the content token at 1px with
`opacity: 1`; mobile/offcanvas inline-end boundaries stay transparent. The
desktop docked sidebar no longer draws a layout-token seam, so the side
columns share the article canvas.

The native article-grid defaults now compile from `$grid-sidebar-width` and
`$grid-margin-width` at 264px, `$grid-body-width` and `$grid-docked-body-width`
at 630px, and `$grid-column-gutter-width` at 26px. `$sidebar-border` is
false, so the desktop docked sidebar does not draw a layout seam. Quarto's
docked formula still widens the body by 200px and leaves spare space in a
right-hand flexible column, so one `qdk.scss` rule restates the desktop docked
grid from those variables: outer flexible tracks, 264px side columns, 26px
gutters, and a 630px measure. `#quarto-document-content`
is a 630px-or-less box with `justify-self: center` and auto inline margins, so
it fills that track and stays centered between the side columns. Navbar rules
center the native container and tools as flex items at desktop width; below
992px the collapse keeps Bootstrap's hidden menu instead of a forced flex row.
Links use a 1.25 line-height with `.25rem` block padding. Article list rhythm
is scoped to `#quarto-document-content`, with the navbar list explicitly reset
to zero block margin so Quarto navigation cannot inherit article spacing.
Desktop links are `.9rem`/400 (active 600) against the `.98rem`/700 brand;
mobile links are `.85rem`. The theme toggle is a 28px control that shows a
sun in the light scheme and a moon in the dark scheme, both painted with
`currentColor`. The callout disclosure is a centered chevron in the same
color as its title. Post-change browser center/contrast measurements remain
owner-side visual evidence.

```bash
quarto add <temporary-qdk-extension.zip> --no-prompt
quarto render .
```

Succeeded in a fresh temporary consumer using
`examples/consumer-override.yml`: its compiled stylesheet contains
`--qdk-link: #2D5E85`; the installed extension contains `licenses/Askr-MIT.txt`
and `assets/fonts/SourceSans3VF-Upright.ttf.woff2`. The Quartz revision
additionally confirmed `assets/fonts/SchibstedGrotesk-Regular.woff2` and
`licenses/Schibsted-Grotesk-OFL.txt`. Its rendered CSS resolves
those local files relative to the installed extension; no CDN is involved.

Asset SHA-256 values and immutable source URLs/revisions are recorded in
`ASSET_MANIFEST.md` and `THIRD_PARTY.md`. Quarto output contains both native
light/dark stylesheet alternatives and the color-scheme toggle script.
The gallery now enables Quarto overlay search (`search.location: navbar`,
`search.type: overlay`) and the theme styles that control. An earlier gallery
receipt left search disabled and rendered no search control or `search.json`.

## Pending manual inspection

The consolidated visual review order is Callout, Header, Layout, Divider,
Typography, Code, then final light/dark system behavior. This current pass
addresses Callout geometry/rhythm only; the remaining entries must be reviewed
as a system after their respective candidate changes settle.

Browser inspection remains required for actual desktop/mobile visual behavior,
keyboard focus traversal, collapse/copy interaction, and clipping/overflow.
Contrast has not been measured; no acceptance threshold is asserted. The
loopback preview is `http://127.0.0.1:4568/` (Quarto preview service); a
2026-09-23 loopback `curl -I` returned `HTTP/1.1 200 OK` with the gallery title.

Quartz's full additional callout aliases remain an explicit limitation: the
candidate faithfully styles Quarto's five native types, nesting, and collapse;
adding the other Quartz authoring names requires a separate public syntax
transformer contract.
