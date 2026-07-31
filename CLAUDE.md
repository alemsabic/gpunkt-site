# Claude Code Instructions - Quartz Repository (gpunkt.org)

## Sister Project

This project and **ale.ms** (`/Users/alemsabic/Desktop/ale.ms`) are both Quartz-based sites
maintained by the same person, kept in close alignment on purpose — both now on Quartz v5, both
using this same `CLAUDE.md` / `CUSTOM-MODIFICATIONS.md` / `upgrade.md` structure. gpunkt.org's own
v4→v5 migration (replayed from ale.ms's `upgrade.md`) is complete — see "Project status" below.
When you land an improvement in one project's tooling, config conventions, or reusable component
(not content), consider whether it should be ported to the other.

---

## ⚠️ Important: Two-Repository Architecture

This repository handles **PRESENTATION ONLY** (Quartz static site generator).

**Content is managed separately**:

- Content Repository: https://github.com/alemsabic/gpunkt-woerter
- Auto-syncs to this repo's `content/` folder via a GitHub Action in the content repo, on every
  push to its `main` branch.
- **DO NOT edit files in `content/` directly** — changes will be overwritten by the next sync.
- **That workflow hardcodes the target branch** (currently checks out this repo's `v5` branch to
  sync into, updated from `v4` during this repo's own v4→v5 cutover). If this repo's production
  branch ever changes again, that workflow file must be updated in the _same_ session — it fails
  silently (green checkmark, no error) if left pointing at a branch nothing serves anymore.

### Repository Focus

- ✅ Design, styling, layout, Quartz configuration, UI components
- ❌ Content (managed in the separate repo above)

---

## Project status

Running **Quartz v5.0.0** — the v4→v5 migration (replayed from ale.ms's `upgrade.md`, every custom
v4 behavior re-ported as a `local-plugins/` fork) is complete and live: `v5` is this repo's
deployed branch (Cloudflare Pages production branch and GitHub default branch). `v4` still exists
as a branch but is no longer built or served. Full migration history, every gotcha found (including
some new to this repo, not in ale.ms's own runbook — e.g. `note-properties` being this ecosystem's
only frontmatter parser, not an optional feature) lives in **`upgrade.md`** — read it for
archaeology on _why_ something is built the way it is, not for what's true today.

**`CUSTOM-MODIFICATIONS.md` still describes v4-era file paths in places** (e.g. `quartz/plugins/
transformers/citations.ts`, `quartz/components/scripts/footnotes.inline.ts`) and needs a pass to
update every entry to its real v5 `local-plugins/*` location — same cleanup ale.ms did right after
its own cutover. Cross-reference against `upgrade.md`'s Phase E notes for the current path of each
behavior in the meantime.

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
  `quartz/util/ctx.ts`, `quartz/plugins/transformers/citations.ts`,
  `quartz/components/scripts/footnotes.inline.ts`, `quartz/plugins/emitters/contentIndex.tsx`.
  Run `find_references` / `get_blast_radius` on the symbol you're about to touch before editing it.
- **When locating where a symbol, component, or type is defined or used anywhere under `quartz/`**,
  instead of grepping across dozens of files by hand. Use `search_symbols` / `find_references`.
- **Before deleting or renaming any exported symbol in `quartz/`** — run `check_delete_safe` first.
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
  npm run build` inside that plugin's own directory, then kill and restart the dev server.

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
  this repo's `v5` branch to sync content into — updated in the same session as this cutover. If
  this repo's production branch ever changes again, that workflow must be updated too, in the same
  session — it fails silently (green checkmark, no error) if left pointing at a branch nothing
  serves anymore.

---

## Custom Modifications

**See `CUSTOM-MODIFICATIONS.md` at the repo root** for every behavior that deviates from stock
Quartz — footnote highlighting, citation-popover suppression, `shortTitle` support, German-locale
citations, and Zotero/dictionary-entry styling (still describes v4-era paths in places — see
"Project status" above). Read it before editing any `local-plugins/*` fork or `quartz/util/
fileTrie.ts` / `quartz/util/ctx.ts`.

---

## Notes

- Site rebuilds automatically in dev mode (`--serve`) when files change.
- Custom styling goes in `quartz/styles/custom.scss`.
- Git safety: never `git add -A` / `git add .` in this repo — stage specific files only.
