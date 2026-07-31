# Custom Modifications (gpunkt.org)

Every behavior in this repo that deviates from stock Quartz v4.5.1. Read this before editing any
of the files listed below, and before starting the v4→v5 migration (each item here needs to be
re-verified or re-ported during that migration).

**Sister project**: [[ale.ms|/Users/alemsabic/Desktop/ale.ms]] has already migrated to Quartz v5
and documented the same categories of custom behavior in its own `CUSTOM-MODIFICATIONS.md`. Where
noted below, ale.ms's version has diverged (evolved further, or become obsolete under v5) — check
there before assuming gpunkt.org's version is still the target shape post-migration.

## Footnote Highlighting

**Files**: `quartz/components/scripts/footnotes.inline.ts` (whole file, 66 lines),
`quartz/components/Body.tsx:2-19` (wires the script into `Body.afterDOMLoaded`).

On every SPA `nav` event, `highlightFootnote()` reads `window.location.hash`. If it starts with
`#user-content-fn-`, it adds a `.footnote-highlighted` class to the matching `<li>` (clearing any
previous highlight first) — a manual re-implementation of CSS `:target` styling, needed because
`:target` doesn't reliably re-fire across Quartz's client-side navigation. It also listens for
`hashchange` and for clicks on `a[href^="#user-content-fn-"]` (10ms `setTimeout` to let the browser
scroll first), registered via `window.addCleanup` for correct SPA teardown. The same handler also
renames the "Footnotes" `<h2>` to German "Fußnoten", and injects a "Quellen" `<h2>` into the
`#refs.references.csl-bib-body` bibliography block if one isn't already present. Styling for
`.footnote-highlighted` lives in `quartz/styles/custom.scss` (paired 1:1 with the `:target`
selector, ~lines 505-513 and ~640).

**Why**: book-style highlight-on-click footnote UX, plus German section headings for a
German-language dictionary site.

## Popover Behavior (Citations plugin fork)

**File**: `quartz/plugins/transformers/citations.ts:44-83`.

A full local fork of the `Citations` transformer plugin (wraps `rehype-citation`). After running
`rehypeCitation`, a second `unist-util-visit` pass walks the HTML AST and sets
`data-no-popover: true` on (a) any `<a href="#bib...">` (bibliography backlinks) and (b) any `<a>`
whose parent is a `<sup>` (footnote reference markers) — suppressing Quartz's default hover-preview
popover on same-page anchors, since previewing "the bottom of the current page" is meaningless. The
same pass also HTML-entity-decodes the `data-tooltip` attribute (`&amp;`, `&quot;`, etc. → literal
characters) so citation tooltip text renders correctly. The plugin's `Options` interface adds
`showTooltips` / `tooltipAttribute`, passed straight through to `rehype-citation`.

**Why**: same-page anchor popovers are useless; `showTooltips`/tooltip-decoding power the
hover-tooltips on `(Author, Year)` citation spans.

**Diverges from ale.ms**: ale.ms splits this into two separate local-plugin forks by concern
(`sup > a` suppression lives in its GFM/footnotes fork; tooltip handling lives in its citations
fork; bib-link popover suppression is left to stock upstream). Don't assume a 1:1 file mapping when
porting this during migration.

## Short Title Support

**Files**: `quartz/util/fileTrie.ts:4-9` (`FileTrieData.shortTitle`), `:31-38` (`displayName`
getter), `quartz/util/ctx.ts:18-23` (`BuildTimeTrieData.shortTitle`), `:35-50`
(`trieFromAllFiles()` extraction), `quartz/plugins/emitters/contentIndex.tsx:12-23`
(`ContentDetails.shortTitle`), `:96-122` (emit loop, reads `file.data.frontmatter?.shortTitle`).

Adds an optional `shortTitle` frontmatter field threaded through three build-time data structures.
`fileTrie.ts`'s `displayName` getter resolves
`displayNameOverride ?? (shortTitle ?? title) ?? fileSegmentHint ?? slugSegment`, falling back
cleanly when absent — powers server-rendered Explorer/Breadcrumbs. `ctx.ts` extracts it when
building the trie from all files. `contentIndex.tsx` threads it into the client-fetched
`contentIndex.json`.

**Why**: per inline comment, "for Zotero sources" — long imported bibliographic titles (e.g. a full
German book title) get a compact nav display like "Ahrens (2017)", while the full title still shows
in the page's own H1.

**⚠️ Known gap vs. ale.ms — check before/during migration**: ale.ms's version of this feature
touches **6 places, not 3** — beyond the three above, it also required matching `shortTitle`
fallback logic in a client-side `FileTrieNode` rebuild (`explorer.inline.ts`), a homepage
"phone-book" site index, and `RecentNotes.tsx`. ale.ms found this gap late (fixed in `RecentNotes`
as of 2026-07-31) — any component that independently reads `allFiles` and rebuilds its own list
needs the identical fallback, or short titles silently fail to appear there. gpunkt.org doesn't
currently have those extra components, but if the migration adds an Explorer sidebar rebuild, a
homepage index, or a "recent notes" list (all likely, since ale.ms's are being ported per the
sister-project plan), re-check each one for this exact bug.

## German Locale (Citations plugin config)

**File**: `quartz.config.ts:18` (`configuration.locale: "de-DE"`), `:94-102` (Citations plugin
invocation).

The `Citations` plugin is configured with
`lang: "https://raw.githubusercontent.com/citation-style-language/locales/master/locales-de-DE.xml"`
— a hardcoded URL pointing directly at the German CSL locale XML, rather than letting the plugin
derive it. Also sets `csl: "apa"`, `showTooltips: true`, `tooltipAttribute: "data-tooltip"`,
`linkCitations: false`, `suppressBibliography: false`.

**Why**: produces German-formatted citations/bibliography (German connectives, date/name ordering)
matching the site's German content.

**⚠️ Obsolete under v5 — do not re-add during migration**: ale.ms's `CUSTOM-MODIFICATIONS.md`
documents this exact manual locale-URL construction as "the old v4-era hack," now obsolete —
`@quartz-community/citations` under v5 auto-derives the correct CSL locale from
`configuration.locale: de-DE` alone. When gpunkt.org migrates, this hardcoded `lang:` URL should be
deleted, not carried forward.

## Zotero Styling

**File**: `quartz/styles/custom.scss` — three blocks:
- Dictionary-entry footnotes (~lines 444-518): compact spacing, orange (`#ee683d`, light) /
  neon-green (`#39ff14`, dark) footnote markers and superscript links, `.footnote-highlighted` /
  `:target` background highlight, hidden backrefs. Scoped to `article.dictionary-entry`.
- Global bibliography (~lines 520-556): `.csl-entry` hanging indent, popover suppression on
  `sup a`, hidden backrefs.
- Citation span + tooltip system (~lines 640-731): dotted underline, `cursor: help`, opacity fade,
  plus a pure-CSS `[data-tooltip]` tooltip via `content: attr(data-tooltip)` on `::after`
  (`:hover`-triggered, no JS), themed via a `[saved-theme="..."]` attribute selector. Comment
  credits the rehype-citation demo project as the source pattern.

**Why**: book-like typographic treatment for dictionary-entry content (no `↩` backlinks, colored
footnote markers, hanging-indent bibliography), plus zero-JS citation tooltips.

**Diverges from ale.ms**: ale.ms's Zotero styling covers substantially more surface — 8 highlight
color classes (`mark.hltr-*`, light/dark variants), a full `article.literature-note` design system
(lettered highlight numbering, `Abb. N` figure captions), and a skeuomorphic 3D book-cover effect
for Zotero book covers. **None of that exists in gpunkt.org** (`grep -E "hltr|literature-note|book-cover" quartz/styles/custom.scss` returns nothing). gpunkt.org's content model (a dictionary) apparently doesn't use Zotero "literature notes" the way ale.ms's Zettelkasten does — confirm with the gpunkt-woerter content repo before assuming this feature gap needs closing during migration; it may be correctly out of scope for this site.
