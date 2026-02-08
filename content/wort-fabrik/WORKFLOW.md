# WORKFLOW: Begriff → gpunkt.org

**Projekt:** gpunkt.org — Dokumentarisches Wörterbuch politischer Reizwörter
**Version:** 3.0 (Feb 2026)

---

## PIPELINE-ÜBERSICHT

```
┌─────────────────────────────────────────────────────┐
│  STEP 1: SCAN                                       │
│  1-SCAN.py "Begriff"                   │
│  → Recherche/[Begriff]/DIP-[Begriff].md             │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  STEP 2: SICHTEN                                    │
│  2-SICHTEN.md + DIP-[Begriff].md      │
│  → KONTEXT-MATERIAL Block                           │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  STEP 3: DRAFT                                      │
│  3-DRAFT-THIS.md (KONTEXT-MATERIAL eingefügt)         │
│  → Drafts/[Begriff]-draft.md                        │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  STEP 4: EDIT (optional)                            │
│  4-EDIT-THIS.md + draft                               │
│  → [Begriff].md (final)                             │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  STEP 5: ZOTERO-IMPORT                              │
│  BibTeX aus KONTEXT-MATERIAL → to_zotero.bib        │
│  → Zotero Import → bibliography.bib                │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  STEP 6: VERIFY                                     │
│  python3 verify_citations.py                        │
│  → Alle [@citekeys] in bibliography.bib?            │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  STEP 7: PUBLISH                                    │
│  git add [Begriff].md bibliography.bib              │
│  git push → auto-deploy → gpunkt.org               │
└─────────────────────────────────────────────────────┘
```

---

## STEP 1: SCAN

**Tool:** `1-SCAN.py`

```bash
python3 1-SCAN.py "Begriff"
# Optional: Startjahr angeben
python3 1-SCAN.py "Begriff" 2010
```

**Was passiert:**
- Scannt ALLE ~4600 BT-Plenarprotokolle seit 2000 (ein Durchgang)
- Findet Protokolle, die den Begriff enthalten
- XML-Parsing nur für Treffer (effizient)
- Max. 5 Treffer pro Jahr (verhindert Dominanz einzelner Jahre)
- Deduplizierung (gleicher Sprecher + Datum = ein Eintrag)

**Output:** `Recherche/[Begriff]/DIP-[Begriff].md`
- Alle Treffer chronologisch, nach Jahr gruppiert
- BibTeX pro Treffer (Format: `note = {Plenarprotokoll WP/Nr}`)
- Alle BibTeX am Ende zusammengefasst

---

## STEP 2: SICHTEN

**Tool:** `2-SICHTEN.md`

**Was tun:**
1. `2-SICHTEN.md` öffnen
2. `DIP-[Begriff].md` als Material einfügen
3. AI wählt 8-10 beste Zitate nach Kriterien
4. Output = KONTEXT-MATERIAL Block

**Kriterien** (Priorität):
1. Zitat-Qualität vor Prominenz
2. Primärzitate bevorzugen
3. Balance: min. 2-3 affirmativ + Rest kritisch
4. Zeitliche Spreizung über alle Jahre
5. Begriff im Zentrum, nicht beiläufig

**Output-Format:**
```markdown
## KONTEXT-MATERIAL (Bundestag-Recherche)
### Affirmativ ...
### Kritisch / Metasprachlich ...
### BibTeX ...
```

**→ Diesen Block in 3-DRAFT-THIS.md einfügen (unter "Begriff: [X]")**

**Referenz:** `REF-Kriterien.md` für detaillierte Auswahlkriterien

---

## STEP 3: DRAFT

**Tool:** `3-DRAFT-THIS.md`

**Was tun:**
1. Begriff oben einsetzen
2. KONTEXT-MATERIAL Block einfügen (aus Step 2)
3. AI arbeitet alle 5 Phasen durch (A-E)
4. Phase E = fertiger Wörterbucheintrag

**WICHTIG:** Die **Belege-Sektion bleibt Placeholder** — AI füllt sie NICHT aus.
Die Zitate kommen aus dem KONTEXT-MATERIAL, nicht aus dem Gedächtnis der AI.

**Output:** `Drafts/[Begriff]-draft.md`

---

## STEP 4: EDIT (optional)

**Tool:** `4-EDIT-THIS.md`

**Wann nutzen:**
- Wenn Draft stark überarbeitet werden muss
- Wenn höchste Qualität gefordert (Goldstandard)

**Prozess:**
1. ANALYSE (ohne Änderungen — versteht den Text)
2. EDITIEREN (strukturell + sprachlich)
3. QUALITY CHECK (Score ≥ 9.0/10)

**Output:** `[Begriff].md` (publikationsreif)

---

## STEP 5: ZOTERO-IMPORT

**Warum Zotero?**
- Normalisiert BibTeX-Einträge
- Validiert Metadaten
- `bibliography.bib` bleibt sauber und vollständig
- Pandoc braucht `bibliography.bib` für [@citekey] Rendering auf gpunkt.org

**Was tun:**

1. BibTeX-Einträge aus KONTEXT-MATERIAL → `imports/to_zotero.bib` kopieren:
```
% ========================================
% From: [Begriff] ([Datum])
% ========================================

@misc{schaeuble_2014, ...}
@misc{scholz_2025, ...}
```

2. Zotero öffnen → File → Import → `imports/to_zotero.bib`

3. Zotero → Better BibTeX → Export Library → `bibliography.bib` (Hauptordner)
   - ✅ Keep updated (automatisch)

4. `to_zotero.bib` leeren für nächsten Begriff:
```bash
> wort-fabrik/imports/to_zotero.bib
```

---

## STEP 6: VERIFY

**Tool:** `verify_citations.py`

```bash
python3 wort-fabrik/verify_citations.py
```

**Was passiert:**
- Scannt alle `.md`-Dateien im Hauptordner
- Findet alle `[@citekey]`-Referenzen
- Vergleicht mit `bibliography.bib`
- Zeigt fehlende Citekeys

**Erfolg:**
```
✅ Alle Quellen sind in bibliography.bib vorhanden.
```

**Bei fehlenden Citekeys:**
- Zurück zu Step 5 (BibTeX fehlt in Zotero)

---

## STEP 7: PUBLISH

```bash
git add [Begriff].md bibliography.bib
git commit -m "feat: add [Begriff]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
git push
```

→ GitHub Actions → auto-deploy → gpunkt.org/[Begriff]

---

## DATEIEN IM ÜBERBLICK

```
wort-fabrik/
│
├── 1-SCAN.py     ← STEP 1: Bundestag-Scan
├── 2-SICHTEN.md ← STEP 2: Zitate sichten
├── 3-DRAFT-THIS.md              ← STEP 3: Eintrag schreiben
├── 4-EDIT-THIS.md               ← STEP 4: Polishing (optional)
├── verify_citations.py        ← STEP 6: Citekey-Check
│
├── REF-Kriterien.md           ← Referenz: Zitat-Auswahlkriterien
├── REF-Werkzeugkasten.md      ← Referenz: 14 Mechanismen
│
├── WORKFLOW.md                ← Diese Datei
├── Queue.md                   ← 100 Begriff-Kandidaten
│
├── Recherche/[Begriff]/       ← DIP-Outputs pro Begriff
├── Drafts/                    ← Entwürfe
└── imports/to_zotero.bib      ← Temporärer BibTeX-Sammler
```

---

## CRITICAL RULES

### BibTeX Format
- **Citekey:** `autor_jahr` (lowercase, Unterstrich: `schaeuble_2014`)
- **Note-Field:** `note = {Plenarprotokoll WP/Nr}` — KEINE Seitenzahlen
- **Grund:** XML-Struktur änderte sich 2022, Seiten nicht konsistent verfügbar

### Keine Sekundärquellen
- ✅ Bundestag-Protokolle, Original-Videos, Qualitätsmedien mit wörtlicher Rede
- ❌ "Correctiv berichtet, dass X sagte...", indirekte Rede

### Belege = Placeholder im Draft
- AI füllt Belege-Sektion NICHT aus
- Belege werden manuell aus KONTEXT-MATERIAL ausgewählt
- Dann per Zotero in bibliography.bib (Step 5)

---

*Letzte Aktualisierung: 2026-02-08 (v3.0 — vereinfachte 4-Schritt-Pipeline)*
