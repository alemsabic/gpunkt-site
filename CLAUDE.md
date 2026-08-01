# Claude Code Instructions - Quartz Repository (gpunkt.org)

## ⚙️ How this file is maintained

This file holds **only durably-true facts about the current state of the project** — config,
architecture, conventions, policies. It is read at the start of every session, so keep it lean and
current, not a historical record.

**Does NOT belong here** (put it elsewhere, or delete it once it's done its job):

- Session-by-session update logs → belongs in git commit messages.
- In-progress migration/project status → belongs in `upgrade.md` while active; once finished,
  replace with a one-line pointer here, don't keep the play-by-play.
- Resolved TODOs, closed bugs, decisions already made → delete once resolved, don't leave a
  checked-off trail. Git history has the trail if anyone needs it.
- One-time debugging narratives → belongs in a commit message or `upgrade.md`. If the _outcome_ is
  a rule that must survive future refactors, that rule belongs in **`CUSTOM-MODIFICATIONS.md`**,
  stated plainly, not narrated.

**Does belong here**: what's true right now (config, file structure, deployment setup), policies
that apply to every session, and pointers to where the detailed, change-prone stuff actually lives.

---

## Sister Project

This project and **ale.ms** (`/Users/alemsabic/Desktop/ale.ms`) are both Quartz v5 sites maintained
by the same person, kept in close alignment on purpose — both follow this same `CLAUDE.md` /
`CUSTOM-MODIFICATIONS.md` / `upgrade.md` structure. When you land an improvement in one project's
tooling, config conventions, or reusable component (not content), consider whether it should be
ported to the other.

---

## ⚠️ Important: Two-Repository Architecture

This repository handles **PRESENTATION ONLY** (Quartz static site generator).

**Content is managed separately**:

- Content Repository: https://github.com/alemsabic/gpunkt-woerter
- Auto-syncs to this repo's `content/` folder via a GitHub Action in the content repo, on every
  push to its `main` branch.
- **DO NOT edit files in `content/` directly** — changes will be overwritten by the next sync.
- **That workflow hardcodes the target branch** (currently `v5`). If this repo's production branch
  ever changes again, that workflow file must be updated in the _same_ session — it fails silently
  (green checkmark, no error) if left pointing at a branch nothing serves anymore.
- **`QUARTZ_REPO_TOKEN` secret (lives in `gpunkt-woerter`, not here):** authenticates that workflow's
  checkout of this repo. It expired silently between 2026-02-23 and 2026-07-31 (two pushes failed,
  content never reached `content/`, no error surfaced anywhere but the Actions tab). Reset
  2026-08-01 using the on-call `gh` session's own token as a stopgap — that token carries far more
  scope (`delete_repo`, `admin:public_key`, ...) than a content-sync job needs. **TODO, no deadline:**
  replace with a fine-grained PAT scoped to `gpunkt-woerter` → `gpunkt-site`, `Contents: Read and
  write` only. Same issue applies to ale.ms's content repo (`alems-notizen`) — see that repo's
  `CLAUDE.md`.

### Repository Focus

- ✅ Design, styling, layout, Quartz configuration, UI components
- ❌ Content (managed in the separate repo above)

---

## Project status

Running **Quartz v5.0.0** — the v4→v5 migration is complete and live: `v5` is this repo's deployed
branch (Cloudflare Pages production branch and GitHub default branch). `v4` still exists as a branch
but is no longer built or served. Full migration history and every gotcha found lives in
**`upgrade.md`** — read it for archaeology on _why_ something is built the way it is, not for what's
true today (that's this file, plus `CUSTOM-MODIFICATIONS.md`).

---

## Doc Exploration Policy (jDocMunch)

This project registers the `jdocmunch` MCP server (project-scoped, `.mcp.json`) for token-efficient
navigation of real documentation sets — e.g. the upstream [Quartz docs](https://github.com/jackyzha0/quartz)
or any other sizeable third-party docs needed while working on this repo. It indexes doc-like files
(Markdown, RST, HTML, OpenAPI specs, etc.) by section instead of requiring full-file reads.

**When to use it**:

- Before exploring an external documentation set (Quartz's own docs, a plugin's docs, a new
  dependency) — `index_repo` (GitHub) or `index_local` (on disk) first, then `search_sections` /
  `get_toc` to find the relevant part.
- To pull specific content once located — use `get_section` (or `get_sections` for several) with
  the section ID, rather than opening the whole file.

**Not for**: this repo's own `CLAUDE.md`, `CUSTOM-MODIFICATIONS.md`, or `README.md` — those are
kept small deliberately and should just be `Read` directly.

This is a manual convention, not an enforced hook. Use judgment: reach for jDocMunch specifically
when indexing genuine external documentation, not this repo's own short files.

---

## Code Exploration Policy (jCodeMunch)

This project also registers the `jcodemunch` MCP server (project-scoped, `.mcp.json`) alongside
jDocMunch. Where jDocMunch indexes _documentation_ (prose, by section), jCodeMunch indexes _source
code_ (TypeScript/JS, by symbol — functions, classes, components, byte-accurate) via tree-sitter.

**Reach for jCodeMunch (not raw `Read`/grep) in these situations**:

- **Before editing any file `CUSTOM-MODIFICATIONS.md` calls out** — `quartz/util/fileTrie.ts`,
  `quartz/util/ctx.ts`, and any file inside `local-plugins/citations/`, `local-plugins/site-scripts/`,
  `local-plugins/content-index/`, or `local-plugins/site-index/`. Run `find_references` /
  `get_blast_radius` on the symbol you're about to touch before editing it.
- **When locating where a symbol, component, or type is defined or used anywhere under `quartz/` or
  `local-plugins/`**, instead of grepping across dozens of files by hand. Use `search_symbols` /
  `find_references`.
- **Before deleting or renaming any exported symbol** in `quartz/` or a `local-plugins/*` fork — run
  `check_delete_safe` first.
- **When exploring an unfamiliar part of the Quartz internals for the first time** — `index_local`
  the relevant directory, then query it rather than opening whole files cold.

**Not for**: this repo's own `CLAUDE.md`/`CUSTOM-MODIFICATIONS.md`/`README` (small, just `Read`
them); the `content/` folder (Markdown content, not code, out of scope per the two-repo
architecture above); trivial edits where the exact file and line are already known and no
ripple-effect risk exists.

---

## Project Overview

- **Name**: gpunkt.org
- **Type**: Static site generator using Quartz v5.0.0
- **Live Site**: https://gpunkt.org

### Key Commands

- **Dev server**: `npx quartz build --serve` (http://localhost:8080)
- **Build**: `npx quartz plugin install --from-config && npx quartz build` (the `--from-config`
  flag matters — see this file's Deployment section and `upgrade.md`'s Phase H for why)
- **Check types**: `npm run check`
- **Format code**: `npm run format`
- **`local-plugins/*` source edits need a rebuild + full server restart, not just a save.** Each
  fork ships from its own `dist/` (built via `tsup`), and a running `--serve` process loads that
  `dist/` once at startup — it never rebuilds or hot-reloads it. `quartz/styles/custom.scss` is the
  exception: it hot-reloads live. After editing any `local-plugins/*/src/**`, run `npm install &&
npm run build` inside that plugin's own directory, then kill and restart the dev server. Every
  `local-plugins/*` package must have its own `.gitignore` listing `dist/` (see
  `CUSTOM-MODIFICATIONS.md`'s Graph entry) — without one, the plugin installer treats a stale
  `dist/` as permanently pre-built and silently stops rebuilding it, even after `src/` changes.

---

## Deployment

**Platform**: Cloudflare Pages

- **Repository**: https://github.com/alemsabic/gpunkt-site
- **Branch**: `v5` — Cloudflare Pages production branch and this repo's GitHub default branch.
  `v4` is the pre-migration branch, kept but no longer deployed.
- **Build Command**: `npx quartz plugin install --from-config && npx quartz build` — the
  `--from-config` flag is required, not optional. Bare `npx quartz plugin install` restores local
  plugins from `quartz.lock.json`'s frozen `resolved` field, an **absolute, install-machine-specific
  path** that doesn't exist on Cloudflare's build machine — every `local-plugins/*`-sourced
  component silently fails to build without this flag (confirmed via the actual Cloudflare build
  log during this repo's own cutover — see `upgrade.md`'s Phase H).
- **Output Directory**: `public`
- **Deploy Time**: 1-2 minutes after push
- The content-sync workflow in `gpunkt-woerter` (`.github/workflows/sync-to-quartz.yml`) checks out
  this repo's `v5` branch to sync content into. If this repo's production branch ever changes again,
  that workflow must be updated too, in the same session (see Two-Repository Architecture above).

---

## Custom Modifications

**See `CUSTOM-MODIFICATIONS.md` at the repo root** for every behavior that deviates from stock
Quartz — footnote highlighting, citation-popover suppression, `shortTitle` support, German-locale
citations, and Zotero/dictionary-entry styling.

**Read it before**: editing any `local-plugins/*` fork, editing `quartz/util/fileTrie.ts` or
`quartz/util/ctx.ts`, touching `quartz/styles/custom.scss`, or doing any future Quartz version
upgrade. Every entry exists because it was lost or broken at least once already.

---

## Notes

- Site rebuilds automatically in dev mode (`--serve`) when files change.
- Custom styling goes in `quartz/styles/custom.scss`.
- Git safety: never `git add -A` / `git add .` in this repo — stage specific files only.
