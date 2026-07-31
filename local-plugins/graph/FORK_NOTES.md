# Fork notes: graph

Forked from `quartz-community/graph` @ `411971434ab698c495dfc42870eb02d3bc539b3a`
(same commit ale.ms's own fork used).

## Patch

`src/i18n/locales/de-DE.ts`: German heading renamed "Graphansicht" → "Graph" — shorter, same
meaning, matching ale.ms's own homepage design (the always-expanded homepage Graph's `<h3>` needs
to read well at large hero-scale font sizes). No `options`-based override exists for this
(confirmed against the upstream package's `optionSchema`, which only exposes
`localGraph`/`globalGraph`), so forking was the only way to change it.

## Re-syncing with upstream

Re-clone at a newer commit and re-apply the one-line locale string change to
`src/i18n/locales/de-DE.ts`.
