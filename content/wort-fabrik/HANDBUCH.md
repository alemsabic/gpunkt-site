# HANDBUCH: Begriff → gpunkt.org

**Projekt:** gpunkt.org — Dokumentarisches Wörterbuch politischer Reizwörter
**Version:** 4.0 (Feb 2026)

---

## PIPELINE-ÜBERSICHT

```
┌─────────────────────────────────────────────────────┐
│  SCHRITT 1: SCAN                                    │
│  python3 1-SCAN.py "Begriff"                        │
│  → Recherche/[Begriff]/DIP-[Begriff].md             │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  SCHRITT 2: SICHTEN (AI-Prompt)                     │
│  2-SICHTEN.md + DIP-[Begriff].md                    │
│  → KONTEXT-MATERIAL Block                           │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  SCHRITT 3: DRAFT (AI-Prompt)                       │
│  3-DRAFT-THIS.md (KONTEXT-MATERIAL eingefügt)       │
│  → Drafts/[Begriff]-draft.md                        │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  SCHRITT 4: EDIT (AI-Prompt, optional)              │
│  4-EDIT-THIS.md + Draft                             │
│  → [Begriff].md (final)                             │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  [MANUELL] ZOTERO-IMPORT                            │
│  BibTeX aus KONTEXT-MATERIAL → to_zotero.bib        │
│  → Zotero Import → bibliography.bib aktualisiert    │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  SCHRITT 5: VERIFY                                  │
│  python3 5-VERIFY.py                                │
│  → Alle [@citekeys] in bibliography.bib?            │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│  [MANUELL] PUBLISH                                  │
│  git add [Begriff].md bibliography.bib              │
│  git push → auto-deploy → gpunkt.org               │
└─────────────────────────────────────────────────────┘
```

---

## SCHRITT 1: SCAN

**Tool:** `1-SCAN.py`

```bash
python3 wort-fabrik/1-SCAN.py "Begriff"
# Optional: Startjahr angeben
python3 wort-fabrik/1-SCAN.py "Begriff" 2010
```

**Was passiert:**
- Scannt alle ~4600 BT-Plenarprotokolle seit 2000 (ein Durchgang)
- Findet Protokolle mit dem Begriff via JSON-Text-Scan
- XML-Parsing nur für Treffer (effizient)
- Max. 5 Treffer pro Jahr (verhindert Dominanz einzelner Jahre)
- Deduplizierung (gleicher Sprecher + Datum = ein Eintrag)

**Output:** `Recherche/[Begriff]/DIP-[Begriff].md`
- Alle Treffer chronologisch, nach Jahr gruppiert
- BibTeX pro Treffer (Format: `note = {Plenarprotokoll WP/Nr}`)
- Alle BibTeX am Ende zusammengefasst

---

## SCHRITT 2: SICHTEN

**Tool:** `2-SICHTEN.md`

**Was tun:**
1. `2-SICHTEN.md` öffnen
2. `DIP-[Begriff].md` als Material einfügen
3. AI wählt 8-10 beste Zitate nach 8 Kriterien aus
4. Output = KONTEXT-MATERIAL Block

**→ Diesen Block in `3-DRAFT-THIS.md` einfügen (unter "Begriff: [X]")**

**Die 8 Kriterien** (vollständig in `2-SICHTEN.md` eingebettet):
1. Zitat-Qualität vor Prominenz
2. Prominenz-Rangfolge
3. Balance Affirmativ/Kritisch (min. 2-3 affirmativ!)
4. Primärzitate bevorzugen
5. Klarheit (Begriff im Zentrum)
6. Zitat-Länge (lieber zu lang)
7. Zeitliche Spreizung
8. Kontext-Integrität

---

## SCHRITT 3: DRAFT

**Tool:** `3-DRAFT-THIS.md`

**Was tun:**
1. Begriff oben einsetzen
2. KONTEXT-MATERIAL Block einfügen (aus Schritt 2)
3. AI arbeitet alle 5 Phasen durch (A: Lexikalisch, B: Historisch, C: Diskurs, D: Mechanismen, E: Schreiben)
4. Phase E = fertiger Wörterbucheintrag nach VORLAGE v5.0

**WICHTIG:** Die **Belege-Sektion bleibt Placeholder** — AI füllt sie NICHT aus.
Belege werden manuell aus dem KONTEXT-MATERIAL ausgewählt.

**Output:** `Drafts/[Begriff]-draft.md`

---

## SCHRITT 4: EDIT (optional)

**Tool:** `4-EDIT-THIS.md`

**Wann nutzen:**
- Wenn Draft stark überarbeitet werden muss
- Wenn höchste Qualität gefordert (Goldstandard)

**Prozess:**
1. ANALYSE (ohne Änderungen — versteht den Text)
2. EDITIEREN (strukturell + sprachlich)
3. QUALITY CHECK (Score ≥ 9.0/10)

**Output:** `[Begriff].md` (publikationsreif, direkt im Root)

---

## MANUELL: ZOTERO-IMPORT

**Warum Zotero?**
- Normalisiert BibTeX-Einträge
- `bibliography.bib` bleibt sauber und vollständig
- Pandoc braucht `bibliography.bib` für [@citekey]-Rendering auf gpunkt.org

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

3. Better BibTeX → Export Library → `bibliography.bib` (Hauptordner)
   - ✅ "Keep updated" aktivieren (automatisches Re-Export)

4. `to_zotero.bib` für nächsten Begriff leeren:
```bash
> wort-fabrik/imports/to_zotero.bib
```

---

## SCHRITT 5: VERIFY

**Tool:** `5-VERIFY.py`

```bash
python3 wort-fabrik/5-VERIFY.py
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
```bash
python3 wort-fabrik/5-VERIFY.py --fix
```
Generiert Stubs in `to_zotero.bib` → dann Zotero-Import wiederholen.

---

## MANUELL: PUBLISH

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
├── 1-SCAN.py              ← Schritt 1: Bundestag-Scan
├── 2-SICHTEN.md           ← Schritt 2: Zitate sichten → KONTEXT-MATERIAL
├── 3-DRAFT-THIS.md        ← Schritt 3: Eintrag schreiben (Phasen A–E)
├── 4-EDIT-THIS.md         ← Schritt 4: Polishing (optional)
├── 5-VERIFY.py            ← Schritt 5: Citekey-Check
│
├── HANDBUCH.md            ← Diese Datei
├── Queue.md               ← 100 Begriff-Kandidaten
│
├── Recherche/[Begriff]/   ← DIP-Outputs pro Begriff
├── Drafts/                ← Entwürfe
└── imports/to_zotero.bib  ← Temporärer BibTeX-Sammler
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
- Dann per Zotero in `bibliography.bib` (vor Schritt 5!)

---

*Letzte Aktualisierung: 2026-02-08 (v4.0)*
