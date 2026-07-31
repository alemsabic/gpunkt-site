# Quartz v4 → v5 Migration Runbook (gpunkt.org)

Status: **Migration complete (2026-07-31). All phases A–H done: `v5` is live in production on both
Cloudflare Pages (`production_branch: v5`) and GitHub (default branch `v5`), confirmed by fetching
`https://gpunkt.org` directly. `v4` still exists as a branch (not deleted) but is no longer deployed
or the GitHub default.** This was Phase I of ale.ms's migration
(`/Users/alemsabic/Desktop/ale.ms/upgrade.md`) — a replay on the sister project, informed by a
read-only recon pass and by every gotcha ale.ms already hit and solved.

**Remaining housekeeping, not blocking**: `CUSTOM-MODIFICATIONS.md` still describes v4-era file
paths in places (flagged in `CLAUDE.md`'s Project status) — needs a pass to update every entry to
its real `local-plugins/*` v5 location, mirroring what ale.ms did right after its own cutover.

## New findings from this repo's own Phase G (not in ale.ms's runbook)

Found via real-browser comparison against the live `https://gpunkt.org`, not just build-success
checks — same methodology ale.ms used to catch 9 real bugs on its own Phase G:

1. **`RecentNotes` never showed dates on gpunkt.org's actual v4** — unlike ale.ms's own
   `RecentNotes.tsx`. Confirmed by reading `git show v4:quartz/components/RecentNotes.tsx`
   directly: no `Date`/`getDate` import, no `<p class="meta">` block. The recon pass's summary
   ("PageList.tsx/RecentNotes.tsx do still show a date column") was wrong for RecentNotes
   specifically — don't trust a recon summary over the actual source when the two disagree.
   Fixed in `local-plugins/recent-notes` by removing the date-display block (date-based sorting
   is unaffected).
2. **`@quartz-community/note-properties` is not an optional bonus feature in this scaffold — it's
   load-bearing.** It registers `remarkFrontmatter` itself; this v5 ecosystem has no separate
   `FrontMatter` plugin, so disabling it breaks title/tags/aliases extraction entirely (silently
   killed all tag-page generation when tried). Its *component* (a visible Properties panel v4
   never had) is excluded on content pages via `layout.byPageType.content.exclude`, but the
   plugin itself must stay `enabled: true`.
3. **Tag casing is lowercased site-wide, unavoidably, and this is not a bug.** v4's own
   `quartz/util/path.ts` `sluggify()` never lowercased; v5 community's equivalent
   (`@quartz-community/utils`'s `slugifyPath()`) does (`.toLowerCase()` in its source, confirmed by
   reading the compiled `dist`). This is used ecosystem-wide for every slug (file paths *and*
   tags), consistent with the already-accepted "v5 lowercases all URLs" fact from ale.ms's
   `upgrade.md`. Not worth fighting by forking every consumer plugin — accept it, same as the
   overall URL-casing convention.
4. **`tag-page`'s `prefixTags: true` option must also be added to its `package.json`'s
   `optionSchema`**, not just passed in `quartz.config.yaml` — passing an option absent from the
   schema silently disabled the *entire* plugin (zero tag pages generated, no error message).
   Same category of gotcha as the npm-scope exclude-matching bug, different mechanism: config
   options are apparently validated strictly against the declared schema.

**Read `/Users/alemsabic/Desktop/ale.ms/upgrade.md` for the full narrative/rationale behind each fix
referenced below by name.** This file does not repeat those narratives — it states the gpunkt.org-
specific facts, decisions, and phase-by-phase steps, and points at the ale.ms section to read for
the "why" and the exact technique.

## Guiding principle

This migration preserves gpunkt.org's **current v4 behavior exactly** — visuals, labels, markup,
CSS tokens, all of it. Only the underlying mechanism changes (v5's community-plugin architecture +
local-plugin forks, instead of direct edits inside a monolithic `quartz/`). Nowhere in this plan
does "port to v5" mean "adopt ale.ms's version of the same feature" — the two projects' implementations
differ in places (ContentHeader labels, badge system, im-Fokus, date-column presence) and that's
staying as-is. Any future alignment between the two projects' designs is a separate, later
conversation — out of scope here.

## Recon findings this plan is built on (2026-07-31 pass)

- Still Quartz v4.5.1 (`quartz.config.ts` + `quartz.layout.ts`, no `local-plugins/`, no
  `quartz.lock.json`) — same starting point ale.ms had.
- Deployment: Cloudflare Pages dashboard-configured (not in-repo), repo `alemsabic/gpunkt-site`,
  production branch `v4`, build command `npx quartz build`, output `public`. The 4 GitHub Actions
  workflow files in `.github/workflows/` are all stock-template leftovers gated on
  `github.repository == 'jackyzha0/quartz'` — they never run here and aren't part of the real deploy
  path; ignore them, don't try to "migrate" them.
- Content sync (from `gpunkt-woerter`) lives entirely in that other repo — its hardcoded-target-
  branch risk (same pattern as ale.ms's `alems-notizen` workflow) can't be verified from here. Check
  it directly in `gpunkt-woerter` before Phase H's production-branch flip.
- Has its own `CLAUDE.md` and `CUSTOM-MODIFICATIONS.md` (4 documented entries: footnote highlighting,
  citations-fork popover behavior, shortTitle support, German-locale citations config). No prior
  `upgrade.md`/runbook existed before this file.
- Three uncommitted WIP changes on `v4` (font pairing Archivo/Inter → Inter Tight/Spectral, darker
  `darkgray` tokens light+dark, README subtitle drop) — treat as the pre-migration baseline, same as
  ale.ms's own Phase A did with its own pending WIP. **Commit these as Phase A**, don't carry them
  uncommitted across the branch cut.
- The plan file this was cross-checked against
  (`/Users/alemsabic/.claude/plans/ja-recherchier-das-mal-compressed-sutherland.md`) has no
  additional gpunkt.org-specific detail beyond what's captured here and in ale.ms's `upgrade.md`.

## Known gotchas to apply from the start (don't rediscover)

All of these bit ale.ms during its own migration and are fully diagnosed in its `upgrade.md`. Apply
the fix directly; the section pointer is where to read the full story if the "why" matters.

1. **`git checkout -b v5 upstream/v5` wipes the working tree** of anything tracked only on `v4`
   (`CLAUDE.md`, this file) — restore with `git checkout v4 -- CLAUDE.md upgrade.md` right after.
   Untracked `.mcp.json` survives automatically. (ale.ms Phase B)
2. **`baseUrl`**: pass bare `gpunkt.org` (no scheme) to `quartz create`, matching v5 convention.
   (ale.ms Phase C)
3. **`article-title` vs `content-meta`**: `article-title` renders the H1, `content-meta` does not —
   only `content-meta` needs excluding on content pages once gpunkt.org's own ContentHeader fork
   covers that job. Don't exclude `article-title`. (ale.ms Phase D/E)
4. **`fileTrie.ts` / `ctx.ts`** are still core files in v5 (not externalized) — direct-edit for
   `shortTitle`, same as v4. `content-index` genuinely is a separate plugin and needs the local-fork
   treatment. gpunkt.org's shortTitle support is confirmed to span only these 3 files already (no
   `RecentNotes`/`explorer.inline.ts` involvement, unlike ale.ms which had a broader gap) — smaller
   surface to port here. (ale.ms Phase E, "shortTitle support")
5. **Footnote-ref popover fix belongs in the `github-flavored-markdown` fork**, not in a `citations`
   fork — `citations` itself doesn't need forking, upstream already handles bib-backlink popover
   suppression once `configuration.locale: de-DE` is set (which also makes gpunkt.org's hardcoded CSL
   locale URL obsolete — drop it, per gpunkt.org's own `CUSTOM-MODIFICATIONS.md`). (ale.ms Phase E)
6. **No plugin owns `afterDOMLoaded` aggregation** — a small component-only local plugin
   (`site-scripts`, scaffolded from `quartz-community/plugin-template`) carrying the footnote script
   (and gpunkt.org's own `Fußnoten`/`Quellen` heading-relabel logic, which rides in the same file
   today) as a static `afterDOMLoaded` property is sufficient, placed anywhere in the layout. (ale.ms
   Phase E, "Global scripts")
7. **New local plugins need proper npm semver deps** (`@quartz-community/types`/`utils` as `^x.y.z`,
   not a git-ref), or the installed copy has no `dist/` and the build fails on an unresolvable import.
   (ale.ms Phase E, the `site-components`/`site-scripts` package.json bug)
8. **`quartz-fonts` community plugin ships its own hardcoded font fallbacks in a competing CSS
   `@layer`** that wins the cascade over `configuration.theme.typography` unless given matching
   explicit `options`. Disable it outright (nothing here depends on its Obsidian-theme bridging) —
   don't rediscover this via a wrong-font screenshot. (ale.ms Phase G addendum, "quartz-fonts plugin
   conflict")
9. **Local-plugin `dist/` is gitignored** — a fresh checkout (including Cloudflare's build machine)
   has none until something builds it. Bare `npx quartz plugin install` restores from
   `quartz.lock.json`'s frozen **install-machine-absolute** `resolved` path and silently fails on any
   other machine. **Always use `npx quartz plugin install --from-config`**, everywhere, including the
   Cloudflare Pages build command — apply this from Phase B onward, don't wait to discover it via a
   broken preview deploy the way ale.ms did. (ale.ms Phase H, the full root-cause trace)
10. **SCSS-only or otherwise non-`.ts`/`.tsx` changes to an already-linked local plugin need a manual
    `cd local-plugins/<name> && npm install && npm run build`** — `quartz plugin install
    --from-config` no-ops if the plugin is already linked, even with `--latest`. (ale.ms Phase E,
    custom.scss gotcha; also already gpunkt.org's own documented "Bases/Canvas" gotcha per project
    memory)

## gpunkt.org-specific reconciliation notes (preserve behavior, change only the mechanism)

- **Heading badges + im-Fokus**: two new local plugins (new, not forks — same treatment as
  `site-scripts`), one new transformer per current file (`headingbadges.ts`, `imfokus.ts`), same
  regex/logic unchanged.
- **TableOfContents badge duplication**: gpunkt.org's current behavior has the *same* `BADGE_RE`
  logic implemented twice on purpose (AST transformer for the heading itself, separate JSX render in
  the TOC because TOC entries are plain text) — replay this as two separate patches: the transformer
  fork above, and a fork of `quartz-community/table-of-contents` adding the same `renderTocText`
  logic. Do not attempt to unify them into a shared util — that would be a behavior-preserving-but-
  architecture-changing move outside this migration's scope.
- **Footnote-heading relabeling** (`Fußnoten`/`Quellen`) stays bundled in the same `site-scripts`
  local plugin as the footnote-highlight script (gotcha 6 above) — it rides the same DOM lifecycle
  event today, keep it that way.
- **ContentHeader.tsx**: new local plugin (`site-components`-style package), preserving gpunkt.org's
  exact current markup — `Stand:` label (not `Datum:`), edit-link as a standalone `<a class="edit-
  link">` sibling after the `<dl>` (not a `<dd>` inside it, not configurable text), `var(--dark)` CSS
  tokens (matching the Phase-A-committed WIP color pass). One **packaging-necessity** detail, not a
  design choice: gpunkt.org's v4 `ContentHeader.tsx` currently imports `getDate`/`formatDate` from
  the core `./Date.tsx`; once ContentHeader becomes its own local-plugin package outside `quartz/`,
  it can no longer reach into core the same way — inline a local `formatDate`/`getDate` (same
  `DD.MM.YYYY` output) directly in the new plugin, exactly the mechanical reason ale.ms's own
  ContentHeader fork did the same thing.
- **Date.tsx / Head.tsx**: still-core files in v5, direct-edit identically to how they're customized
  today (hardcoded `DD.MM.YYYY` ignoring locale; conditional `" - "` separator). Confirmed byte-
  identical pattern to what ale.ms had, so this is a pure mechanical copy.
- **`PageList.tsx` / date column — do NOT apply ale.ms's date-removal patch.** gpunkt.org keeps its
  date column in list pages (unlike ale.ms, which removed it) — this means the stock `tag-page`/
  `folder-page` plugins' bundled 3-column `listPage.scss` grid (`fit-content(8em) 3fr 1fr`) is
  probably *already correct* for gpunkt.org's 3-item layout (date + desc + tags) and likely needs
  **no fork at all** for this specific concern. Verify this by comparing real rendered output against
  the current gpunkt.org site rather than blind-applying ale.ms's `1fr auto` fix, which was only
  needed because ale.ms's list items shrank to 2 columns after removing the date.
- **`ProfileImage.tsx`**: confirmed orphaned/unused in current source (registered in
  `components/index.ts` but not referenced in `quartz.layout.ts`, stale "NE KONTAM Logo" alt text
  from a pre-gpunkt era). Don't port — dead code, matches a leftover ale.ms found and dropped too.
- **`EditOnGitHub.tsx` equivalent**: ale.ms found this component dead-code in its own v4 (never in
  `quartz.layout.ts`, ContentHeader's own inline link makes it redundant) — check whether gpunkt.org
  has the same standalone component and the same redundancy before deciding whether it needs porting.
- **Open items to verify during Phase E** (recon found no evidence either way — confirm rather than
  assume): does gpunkt.org have a `Tagline` component, a custom `Footer.tsx` (personal links), a
  `tooltips.inline.ts`, or a `RecentNotes` "index-only" rendering rule? None were flagged in
  `CUSTOM-MODIFICATIONS.md` or found during the undocumented-customization scan — treat as "probably
  stock/absent" but confirm by reading the actual v4 source for each before assuming there's nothing
  to port.
- **i18n**: same methodology as ale.ms Phase E — diff gpunkt.org's `de-DE.ts` (if any exists; not yet
  located during recon) against v5 stock plugin locale defaults, port only the deliberate
  customizations, not what's already Quartz's own standard German translation.
- **custom.scss**: full wholesale port, same verification method as ale.ms (spot-check real rendered
  DOM against the most distinctive selectors, confirm `cssclasses` frontmatter still flows through).
  gpunkt.org has none of ale.ms's `hltr-*`/`literature-note`/book-cover system — don't port CSS that
  doesn't correspond to any gpunkt.org content convention.

## Phases (mirroring ale.ms's A→I structure)

### Phase A — Prep on v4 (not started)

- Commit the 3 pending WIP changes (font pairing, contrast colors, README) as a clean baseline commit.
- Create this file (done).
- Sanity-check `CLAUDE.md` for any other drift before branching (mirroring the stale-doc corrections
  ale.ms made in its own Phase A).

### Phase B — Branch to v5 (not started)

```
git remote add upstream https://github.com/jackyzha0/quartz.git
git fetch upstream v5
git checkout -b v5 upstream/v5
npm i
git push -u origin v5
```

Apply gotcha 1 immediately after checkout. Confirm `v4` stays untouched and pushed before proceeding.

### Phase C — Scaffold + import content (not started)

```
git archive v4 -- content | tar -x -C <scratch>/gpunkt-v4-content-backup
npx quartz create --template default --source <scratch>/gpunkt-v4-content-backup/content \
  --strategy copy --baseUrl gpunkt.org --links shortest
```

Verify `npx quartz build` succeeds against the scaffold + real content before moving to Phase D.

### Phase D — Rebuild config (not started)

Translate `quartz.config.ts`/`quartz.layout.ts` into `quartz.config.yaml`. Apply gotcha 3
(`article-title` stays enabled, only `content-meta` excluded once ContentHeader is ported). Defer
Tagline/ContentHeader/Footer/footnote-popover/shortTitle/inline-scripts/i18n to Phase E, same
sequencing ale.ms used.

### Phase E — Port custom plugins (not started)

Work through, in this order (matches dependency order ale.ms found worked well):

1. shortTitle (`fileTrie.ts`/`ctx.ts` direct edits + `content-index` local fork) — gotcha 4.
2. Footnote-popover fix in `github-flavored-markdown` fork — gotcha 5.
3. `site-scripts` local plugin: footnote-highlight + heading-relabel script — gotchas 6, and the
   "footnote-heading relabeling" reconciliation note above.
4. Date.tsx/Head.tsx direct edits.
5. Heading-badges + im-Fokus new local plugins, TableOfContents badge fork — reconciliation notes
   above.
6. ContentHeader new local plugin — reconciliation notes above (packaging-necessity `formatDate`
   inlining).
7. Verify-then-decide on `PageList.tsx`/date-column, `Tagline`, `Footer`, `tooltips.inline.ts`,
   `RecentNotes` index-only, `EditOnGitHub` equivalent, i18n — the open items listed above.
8. `custom.scss` wholesale port + verification.
9. Static assets.

### Phase F — Bases + Canvas (not started)

Same as ale.ms: confirm `bases-page`/`canvas-page` are enabled by default in the scaffold, smoke-test
with real or temporary test content, don't leave test fixtures in `content/`.

### Phase G — Local verification (not started)

Real `npx quartz build --serve` + actual browser inspection, page by page, against the live `v4`
gpunkt.org site as the reference — not just build-success checks. Apply gotcha 8 (`quartz-fonts`)
proactively rather than waiting to spot a wrong font. Keep the same verification rigor ale.ms used —
it found 9 real bugs this way that static checks missed.

### Phase H — CI/CD + deploy cutover ✅ (2026-07-31)

- **Gotcha 9 applied from the start, confirmed necessary by real evidence**: fetched the first v5
  preview build's log directly via the Cloudflare API (`wrangler`'s existing OAuth session on this
  machine, same technique ale.ms used) — confirmed the bare `npx quartz build` build command (the
  project's setting at the time) failed to instantiate all 13 local plugins
  (`Unknown file extension ".ts"` / components failing to load), exactly the predicted failure.
  Updated the Cloudflare Pages project's build command via the API to
  `npx quartz plugin install --from-config && npx quartz build`.
- **Preview deploy verified working**: pushed an empty commit to force a fresh build against the
  corrected setting. Build log confirmed all 13 local plugins installed + built successfully, 143
  files emitted. Fetched the deployed preview URL in a real browser (index page + a content page)
  — renders identically to the local dev build. Production branch (`v4`) untouched throughout;
  Cloudflare Pages builds preview deployments automatically for every push to a connected branch,
  so this required no separate "enable preview" step.
- **Content-sync workflow updated**: `gpunkt-woerter`'s `.github/workflows/sync-to-quartz.yml`
  hardcoded `ref: v4` (checks out this repo's branch to sync content into) — confirmed via `gh api`,
  then changed to `ref: v5` and pushed to `gpunkt-woerter`'s `main`, in the same session as the
  production branch flip below.
- **Production cutover done**: Cloudflare Pages `production_branch` flipped from `v4` to `v5` via
  the API. Pushed an empty commit to force a fresh build in the (now) Production environment —
  confirmed via `wrangler pages deployment list` (`Environment: Production`, `Branch: v5`,
  `Status: Active`). Confirmed live: `curl https://gpunkt.org/` returns 200 with the expected
  content, and a real-browser screenshot of `https://gpunkt.org` matches the verified local/preview
  build exactly. `v4` branch left in place (not deleted), just no longer deployed.
- `CLAUDE.md` updated to reflect v5 as the current/live version (mirrors ale.ms's own
  end-of-migration `CLAUDE.md` rewrite) — see this file's own top status line and the "Remaining
  housekeeping" note above for what's left (`CUSTOM-MODIFICATIONS.md`'s stale v4 paths).

### Phase I — n/a for this repo

(Phase I was "replay on gpunkt.org" in ale.ms's runbook — this file *is* that replay; there's no
further sister project beyond this one.)

## Update discipline

Update this file as each phase actually executes — commands run, gotchas hit, deviations from this
plan, final config — same discipline ale.ms's `upgrade.md` followed. This is what made this plan
possible to write without re-discovering anything; keep that true for whoever picks this up next.
