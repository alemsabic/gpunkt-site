# Fork notes: recent-notes

Forked from `quartz-community/recent-notes` @ `2c36e87f151431b7fb05a486705adfa790126622`
(same commit ale.ms's own fork used).

## Patch

`src/components/RecentNotes.tsx`: baked in two things v4's config-driven options can't express in
v5's YAML:

1. Index-only rendering (`if (fileData.slug !== "index") return null`) — v4 only showed this on
   the index page via a `ConditionalRender` wrapper. Baked directly into the component rather than
   a `quartz.ts` `ConditionalRender` override, since `loadQuartzLayout()`'s per-pageType override
   merge is shallow (whole-array replace, not append) — fragile against future `afterBody` changes.
2. `.filter((p) => p.slug !== "index")` — v4's `filter: (f) => f.slug !== "index"` option is a JS
   callback, not expressible in YAML.

Unlike ale.ms's own fork of this same plugin, this fork does **not** remove the per-item date
display — gpunkt.org keeps dates in its recent-notes list (matching its overall keep-the-date-column
stance, see the `tag-page`/`folder-page` `PageList.tsx` forks) — only the date-format string was
patched there, not removed. `showTags: false` is set via config options (v4 behavior), unrelated to
the date question.

## Re-syncing with upstream

Re-clone at a newer commit, diff `src/components/RecentNotes.tsx` against this file, and re-apply
the two filter/return additions above.
