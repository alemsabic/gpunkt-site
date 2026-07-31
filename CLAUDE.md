# Claude Code Instructions - Quartz Repository (gpunkt.org)

## Sister Project

This project and **ale.ms** (`/Users/alemsabic/Desktop/ale.ms`) are both Quartz-based sites
maintained by the same person, kept in close alignment on purpose. ale.ms has already migrated to
Quartz v5 and carries a more mature MCP/doc setup (`jdocmunch` + `jcodemunch`, this same
`CLAUDE.md` / `CUSTOM-MODIFICATIONS.md` / `upgrade.md` structure) — gpunkt.org's is being brought
to parity. When you land an improvement in one project's tooling, config conventions, or reusable
component (not content), consider whether it should be ported to the other. gpunkt.org's own
v4→v5 migration is planned separately (see "Project status" below) and will draw directly on
ale.ms's `upgrade.md`.

---

## ⚠️ Important: Two-Repository Architecture

This repository handles **PRESENTATION ONLY** (Quartz static site generator).

**Content is managed separately**:

- Content Repository: https://github.com/alemsabic/gpunkt-woerter
- Auto-syncs to this repo's `content/` folder via a GitHub Action in the content repo, on every
  push to its `main` branch.
- **DO NOT edit files in `content/` directly** — changes will be overwritten by the next sync.
- If that content-repo workflow hardcodes a target branch (as ale.ms's sister workflow does — see
  ale.ms's `CLAUDE.md`), and this repo's production branch ever changes, the workflow must be
  updated in the same session — it fails silently otherwise.

### Repository Focus

- ✅ Design, styling, layout, Quartz configuration, UI components
- ❌ Content (managed in the separate repo above)

---

## Project status

Running **Quartz v4.5.1**. Still on the pre-migration architecture (`quartz.config.ts` +
`quartz.layout.ts`, no `local-plugins/` fork directory, no `quartz.lock.json`). A v4→v5 migration
mirroring ale.ms's is planned as a separate effort, informed directly by ale.ms's `upgrade.md`
(which has a "Phase I" checklist of gotchas to carry over so they don't need rediscovering) and by
this repo's own `CUSTOM-MODIFICATIONS.md` (documents what must be re-verified or re-ported).
Explicitly gated on the user being present and giving the go-ahead — don't start it unattended.

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
- **Type**: Static site generator using Quartz v4.5.1
- **Live Site**: https://gpunkt.org

### Key Commands

- **Dev server**: `npx quartz build --serve` (http://localhost:8080)
- **Build**: `npx quartz build`
- **Check types**: `npm run check`
- **Format code**: `npm run format`
- **Tests**: `npm run test` (Node.js test runner, files live next to source as `*.test.ts`)

---

## Deployment

**Platform**: Cloudflare Pages

- **Repository**: https://github.com/alemsabic/gpunkt-site
- **Branch**: `v4` — current production branch.
- **Build Command**: `npx quartz build`
- **Output Directory**: `public`
- **Deploy Time**: 1-2 minutes after push

---

## Custom Modifications

**See `CUSTOM-MODIFICATIONS.md` at the repo root** for every behavior that deviates from stock
Quartz — footnote highlighting, citation-popover suppression, `shortTitle` support, German-locale
citations, and Zotero/dictionary-entry styling. Read it before editing any of the files it lists,
or before starting the v4→v5 migration.

---

## Notes

- Site rebuilds automatically in dev mode (`--serve`) when files change.
- Custom styling goes in `quartz/styles/custom.scss`.
- Git safety: never `git add -A` / `git add .` in this repo — stage specific files only.
