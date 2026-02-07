# WORKFLOW: Hybrid-Recherche → Eintrag

**Projekt:** gpunkt.org - Dokumentarisches Wörterbuch politischer Reizwörter
**Qualität:** Recherche (A-C) + Belege (DIP/Web) + Mechanismus-Analyse → Draft
**Version:** 2.0 (Feb 2026)

---

## 📊 ÜBERSICHT (ASCII-Diagramm)

```
┌─────────────────────────────────────────────────────────────────┐
│              PHASE 0: RECHERCHE (MATERIAL SAMMELN)              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ A. LEXIKALISCH│  │ B. HISTORISCH│  │ C. DISKURS   │          │
│  │ Definition,  │  │ Geschichte   │  │ Anwendung,   │          │
│  │ Etymologie,  │  │ (5 Schritte) │  │ Abgrenzung   │          │
│  │ Konstruktion │  │              │  │              │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                 │                 │                  │
│         ▼                 ▼                 ▼                  │
│  A-Lexikalisch.md  B-Historisch.md  C-Diskurs.md               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PHASE 1: BELEGE (ZITATE SAMMELN)               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌────────────────────┐         ┌─────────────────────┐         │
│  │ 1A. BUNDESTAG      │         │ 1B. WEB-RECHERCHE   │         │
│  │ bundestag_         │         │ 1-WEB-RECHERCHE-    │         │
│  │ recherche.py       │         │ PROMPT.md + Gemini  │         │
│  └────────┬───────────┘         └──────────┬──────────┘         │
│           │                                │                    │
│           ▼                                ▼                    │
│  Recherche/[Begriff]/          Recherche/[Begriff]/             │
│  DIP-*.md                      WEB-Recherche.md                 │
│  + BibTeX                      + BibTeX                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│           PHASE 1.5: ZITAT-KRITERIEN (VOR SICHTUNG!)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  → Lies 1.5-ZITAT-KRITERIEN.md                                  │
│  → Verstehe die 6 Auswahlkriterien                              │
│  → Prominenz, Primär/Sekundär, Affirmativ/Kritisch, Zeit        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              PHASE 2: MANUELLE SICHTUNG (KRITISCH!)             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  → Öffne DIP-Begriff.md + WEB-Begriff.md                        │
│  → Wähle die BESTEN 4-6 Zitate (nach 1.5-Kriterien!)            │
│  → Triple-Verification durchführen                              │
│  → Kopiere BibTeX-Einträge → imports/to_zotero.bib              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 3: ZOTERO-IMPORT                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Zotero → File → Import → to_zotero.bib                      │
│  2. Zotero → Better BibTeX → Export → bibliography.bib          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              PHASE 4: MECHANISMUS-ANALYSE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Input: DIP-Begriff.md + WEB-Begriff.md (ausgewählte Zitate)    │
│  Tool:  2-MECHANISMUS-ANALYSE-PROMPT.md + Gemini                │
│  Output: MECHANISMUS-Begriff.md                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 5: DRAFT SCHREIBEN                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Input: A-C (Recherche) + DIP/WEB (Belege) + Mechanismus        │
│  Tool:  3-DRAFT-PROMPT.md + Gemini                              │
│  Output: Draft-Begriff.md (ALLE Sektionen haben Material!)      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                PHASE 6: FINALISIERUNG (MIT CLAUDE)              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  6A. Draft-Begriff.md → Begriff.md (überarbeiten mit Claude)    │
│  6B. (Optional) 4-EDITOR-WORKFLOW.md (3-Phasen-Editing)         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 7: VERIFICATION                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  python3 wort-fabrik/verify_citations.py                        │
│  → Prüft: Alle [@citekeys] in bibliography.bib?                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 8: PUBLISH                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  git add Begriff.md bibliography.bib                            │
│  git commit -m "feat: add Begriff"                              │
│  git push                                                       │
│  → Auto-Deploy → gpunkt.org                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 DETAILLIERTE SCHRITTE

### PHASE 0: RECHERCHE (MATERIAL SAMMELN)

**Ziel:** Sammle Material für ALLE Sektionen des Eintrags (nicht nur Zitate!)

**Problem gelöst:** Wir können nicht erwarten, dass die KI sich Definition, Geschichte, Anwendung und Abgrenzung "aus den Fingern zieht". Diese Phase liefert **fundiertes Material** für jede Sektion.

---

#### 0A. Lexikalische Recherche

**Tool:** `0-RECHERCHE/A-LEXIKALISCHE-RECHERCHE.md` + Gemini

**Recherchiert:**
- **Wörterbücher:** Duden, DWDS, Wahrig, Grimm
- **Wissenschaftliche Definitionen:** Google Scholar
- **Etymologie:** Wortherkunft, ursprüngliche Bedeutung
- **Semantische Analyse:** Wie ist das Wort konstruiert?

**Command:**
```bash
# Begriff in Prompt einsetzen und ausführen
sed "s/\[BEGRIFF HIER EINSETZEN\]/Begriff/g" \
  wort-fabrik/0-RECHERCHE/A-LEXIKALISCHE-RECHERCHE.md | \
  gemini --model gemini-2.5-pro > wort-fabrik/Recherche/Begriff/A-Lexikalisch.md
```

**Output:** `Recherche/Begriff/A-Lexikalisch.md`

**Liefert Material für:**
- Definition-Sektion (beste Definitionen)
- Konstruktion-Sektion (semantische Formel)

---

#### 0B. Historische Recherche

**Tool:** `0-RECHERCHE/B-HISTORISCHE-RECHERCHE.md` + Gemini

**Recherchiert (die 5 Schritte):**
1. **Ursprung:** Wann und wo tauchte der Begriff erstmals auf?
2. **Erste Prägung:** Wer hat ihn politisch geprägt/instrumentalisiert?
3. **Kontext:** Welches Ereignis/welche Krise?
4. **Verbreitung:** Wie wurde er Mainstream?
5. **Gegenwart:** Wo steht er heute?

**Command:**
```bash
# Begriff in Prompt einsetzen und ausführen
sed "s/\[BEGRIFF HIER EINSETZEN\]/Begriff/g" \
  wort-fabrik/0-RECHERCHE/B-HISTORISCHE-RECHERCHE.md | \
  gemini --model gemini-2.5-pro > wort-fabrik/Recherche/Begriff/B-Historisch.md
```

**Output:** `Recherche/Begriff/B-Historisch.md`

**Liefert Material für:**
- Geschichte-Sektion (chronologische Biographie mit Namen, Daten, Ereignissen)

**Hinweis:** Bei Vulgärsprache oft optional (keine dokumentierbare Geschichte).

---

#### 0C. Diskurs-Recherche

**Tool:** `0-RECHERCHE/C-DISKURS-RECHERCHE.md` + Gemini

**Recherchiert:**
- **Diskurs-Analyse:** Wer nutzt den Begriff? Welche Narrative?
- **Funktions-Analyse:** Warum ist er attraktiv? (Advocatus Diaboli)
- **Abgrenzungs-Kontexte:** Wann ist er legitim/neutral? (Wissenschaft, Satire)

**Command:**
```bash
# Begriff in Prompt einsetzen und ausführen
sed "s/\[BEGRIFF HIER EINSETZEN\]/Begriff/g" \
  wort-fabrik/0-RECHERCHE/C-DISKURS-RECHERCHE.md | \
  gemini --model gemini-2.5-pro > wort-fabrik/Recherche/Begriff/C-Diskurs.md
```

**Output:** `Recherche/Begriff/C-Diskurs.md`

**Liefert Material für:**
- Anwendung-Sektion (Sprecher-Perspektive, Verführungskraft)
- Abgrenzung-Sektion (Kontext-Abhängigkeit, legitime Verwendungen)

---

**WICHTIG:** Diese drei Recherchen können **parallel** ausgeführt werden (verschiedene Tabs/Terminals). Sie sind unabhängig voneinander und liefern jeweils Material für unterschiedliche Sektionen.

---

### PHASE 1: BELEGE (ZITATE SAMMELN)

**Ziel:** Sammle Zitate aus Bundestag + Web-Quellen

---

#### 1A. Bundestag-Recherche

**Tool:** `bundestag_recherche.py`

**Syntax:**
```bash
python3 bundestag_recherche.py "Begriff" "Start-Datum" "End-Datum" "Max-Protokolle"
```

**Parameter (Positionsparameter, keine Flags!):**
1. `"Begriff"` - Suchbegriff (z.B. "Sozialtourismus")
2. `"Start-Datum"` - Start-Datum (z.B. "2013-01-01")
3. `"End-Datum"` - End-Datum (z.B. "2015-12-31") - optional
4. `"Max-Protokolle"` - Maximale Anzahl Protokolle (z.B. 200) - optional

**⚠️ WICHTIG:** Das Script kann **NICHT nach Sprecher/Partei filtern**! Es findet ALLE Verwendungen im Zeitraum. Filterung nach Personen muss **manuell** bei der Sichtung passieren.

**Beispiele:**
```bash
# Suche "Sozialtourismus" von 2013 bis 2015 (ALLE Sprecher)
python3 bundestag_recherche.py "Sozialtourismus" "2013-01-01" "2015-12-31"

# Suche ab 2024 (ohne End-Datum)
python3 bundestag_recherche.py "Sozialtourismus" "2024-01-01"

# Mit max. 100 Protokollen
python3 bundestag_recherche.py "Sozialtourismus" "2013-01-01" "2015-12-31" 100
```

**Output:** `Recherche/[Begriff]/DIP-*.md` (pro Suche eine Datei)

**Beispiele:**
- `Recherche/Sozialtourismus/DIP-Seehofer-2013-2015.md`
- `Recherche/Sozialtourismus/DIP-AfD-2017-2026.md`

**Enthält:**
- Bundestag-Zitate (aus Plenarprotokollen)
- Sprecher (Name, Rolle, Fraktion)
- Seitenzahlen + Bereiche
- BibTeX-Einträge (mit Citekeys: `nachname_jahr`)

**Qualität:** 95/100 (XML-strukturiert, Primärquelle)

---

#### 1B. Web-Recherche

**Tool:** `1-WEB-RECHERCHE-PROMPT.md` + Gemini

**Command:**
```bash
# 1. Prompt vorbereiten (Begriff einsetzen)
sed "s/\[BEGRIFF HIER EINSETZEN\]/Begriff/g" wort-fabrik/1-WEB-RECHERCHE-PROMPT.md | \
  gemini --model gemini-2.5-pro > wort-fabrik/Recherche/Begriff/WEB-Recherche.md
```

**Input:**
- `1-WEB-RECHERCHE-PROMPT.md` (mit `[BEGRIFF HIER EINSETZEN]`)

**Output:** `Recherche/[Begriff]/WEB-Recherche.md`

**Enthält:**
- Web-Zitate (Pressemitteilungen, Interviews, Talkshows)
- 2-Phasen-Prozess (sammeln → auswählen)
- 3-5 beste Zitate
- BibTeX-Einträge (mit Citekeys: `nachname_jahr`)

**Qualität:** 90/100 (Primärquellen, verifizierbar)

---

### PHASE 1.5: ZITAT-KRITERIEN (VOR SICHTUNG!)

**Ziel:** Klare Auswahlkriterien verstehen, bevor du Zitate sichtest

**⚠️ KRITISCH:** Ohne Kriterien wählt man nach "Bauchgefühl" oder "Brisanz" - das führt zu schlechten Zitaten!

**Schritte:**

1. **Lies die Kriterien-Datei:**
   ```bash
   open wort-fabrik/1.5-ZITAT-KRITERIEN.md
   ```

2. **Verstehe die 6 Kriterien:**
   - **Prominenz** (Minister > Abgeordnete)
   - **Art der Verwendung** (Affirmativ vs. Kritisch - BALANCE!)
   - **Klarheit** (Begriff im Zentrum, nicht beiläufig)
   - **Primär- vs. Sekundärzitat** (Direktes Zitat > "X sagte...")
   - **Zeitliche Spreizung** (Etablierung → Höhepunkt → Gegenwart)
   - **Verifizierbarkeit** (PDF funktioniert, Kontext stimmt)

3. **Merke:** Mindestens 1-2 **affirmative** Zitate (sonst fehlt Etablierungsgeschichte!)

**Output:** Klares Verständnis, wonach du suchst

**Siehe:** `1.5-ZITAT-KRITERIEN.md` (ausführlich)

---

### PHASE 2: MANUELLE SICHTUNG (KRITISCH!)

**Ziel:** Wähle die BESTEN 4-6 Zitate aus DIP + Web (nach Phase 1.5 Kriterien!)

**⚠️ TRIPLE-VERIFICATION PFLICHT!**

**Schritte:**

1. **Öffne alle Recherche-Dateien:**
   ```bash
   open wort-fabrik/Recherche/Begriff/DIP-*.md
   open wort-fabrik/Recherche/Begriff/WEB-Recherche.md
   ```

2. **Wähle die besten 4-6 Zitate (nach 1.5-Kriterien!):**
   - ✅ Prominenz (siehe 1.5-ZITAT-KRITERIEN.md)
   - ✅ Primärzitate bevorzugen (nicht "X sagte...")
   - ✅ Balance: Min. 1-2 affirmativ + Rest kritisch
   - ✅ Zeitliche Spreizung (2013 → 2026)

3. **Triple-Verification durchführen:**
   - [ ] **Prüfung 1:** Link öffnen → Zitat im Original finden (Wort-für-Wort)
   - [ ] **Prüfung 2:** Kontext prüfen (korrekt kontextualisiert? Nicht aus Zusammenhang gerissen?)
   - [ ] **Prüfung 3:** Metadaten prüfen (Name, Funktion, Datum korrekt?)
   - **Bei JEGLICHEM Zweifel:** Quelle NICHT verwenden!

4. **BibTeX-Einträge kopieren:**
   ```bash
   # Öffne to_zotero.bib
   open wort-fabrik/imports/to_zotero.bib

   # Kopiere BibTeX-Einträge der ausgewählten Zitate:
   # - Aus DIP-Begriff.md (```bibtex ... ```)
   # - Aus WEB-Begriff.md (```bibtex ... ```)
   # - Füge Trennlinie ein:

   % ========================================
   % From: DIP-Begriff.md + WEB-Begriff.md (JJJJ-MM-TT)
   % ========================================

   @misc{merz_2022, ...}
   @misc{seehofer_2013, ...}
   ```

**Lieber 3 perfekte Zitate als 6 unsichere!**

---

### PHASE 3: ZOTERO-IMPORT

**Ziel:** BibTeX → Zotero → bibliography.bib

**Schritte:**

1. **Zotero öffnen**

2. **Import:**
   - File → Import
   - Wähle: `wort-fabrik/imports/to_zotero.bib`
   - Importiere alle Einträge

3. **Export (überschreibt bibliography.bib):**
   - Better BibTeX → Export Library
   - Format: Better BibTeX
   - Ziel: `bibliography.bib` (Hauptordner)
   - ✅ Keep updated (automatisch)

4. **Cleanup:**
   ```bash
   # to_zotero.bib leeren (für nächsten Begriff)
   > wort-fabrik/imports/to_zotero.bib
   ```

**Warum Zotero?**
- Normalisiert BibTeX-Einträge
- Validiert Metadaten
- Automatisches Export-Update

---

### PHASE 4: MECHANISMUS-ANALYSE

**Ziel:** Analysiere ALLE ausgewählten Zitate (aus DIP + Web)

**Tool:** `2-MECHANISMUS-ANALYSE-PROMPT.md` + Gemini

**Input vorbereiten:**

1. **Kopiere ausgewählte Zitate** aus DIP + Web in eine Datei:
   ```bash
   # Temporäre Datei für Input
   cat > /tmp/mechanismus-input.md <<EOF

   **Zitat 1: [aus DIP oder Web]**
   ...

   **Zitat 2: [aus DIP oder Web]**
   ...

   EOF
   ```

2. **Mechanismus-Analyse ausführen:**
   ```bash
   # Prompt mit Begriff ersetzen + Input anhängen
   (sed "s/\[BEGRIFF HIER EINSETZEN\]/Begriff/g" wort-fabrik/2-MECHANISMUS-ANALYSE-PROMPT.md; \
    cat /tmp/mechanismus-input.md) | \
     gemini --model gemini-2.5-pro > wort-fabrik/Recherche/MECHANISMUS-Begriff.md
   ```

**Output:** `Recherche/[Begriff]/MECHANISMUS-[Begriff].md`

**Enthält:**
- Mechanismus-Analyse für JEDES Zitat (●◐○)
- Gesamtanalyse (dominante Mechanismen)
- Fazit (1-2 Sätze)

**Qualität:** 90/100 (präzise Begründungen, Cluster-Logik)

---

### PHASE 5: DRAFT SCHREIBEN

**Ziel:** First Draft basierend auf ALLEN Recherche-Materialien

**Tool:** `3-DRAFT-PROMPT.md` + Gemini

**Input:**
- `Recherche/[Begriff]/A-Lexikalisch.md` (Definition, Etymologie, Konstruktion)
- `Recherche/[Begriff]/B-Historisch.md` (Geschichte)
- `Recherche/[Begriff]/C-Diskurs.md` (Anwendung, Abgrenzung)
- `Recherche/[Begriff]/DIP-*.md` + `WEB-Recherche.md` (Zitate - ausgewählte)
- `Recherche/[Begriff]/MECHANISMUS-[Begriff].md` (Mechanismen-Analyse)

**Command:**
```bash
# Draft-Prompt mit ALLEN Recherche-Dokumenten füttern
(cat wort-fabrik/3-DRAFT-PROMPT.md; \
 echo ""; echo "---"; echo ""; \
 echo "# RECHERCHE-MATERIAL"; echo ""; \
 cat wort-fabrik/Recherche/Begriff/A-Lexikalisch.md; echo ""; \
 cat wort-fabrik/Recherche/Begriff/B-Historisch.md; echo ""; \
 cat wort-fabrik/Recherche/Begriff/C-Diskurs.md; echo ""; \
 cat wort-fabrik/Recherche/Begriff/MECHANISMUS-Begriff.md) | \
  gemini --model gemini-2.5-pro > wort-fabrik/Drafts/Draft-Begriff.md
```

**Output:** `Drafts/Draft-Begriff.md`

**Enthält:**
- Vollständiger Wörterbuch-Eintrag (VORLAGE v5.0)
- **7 Sektionen mit Material:** Definition (aus A), Geschichte (aus B), Konstruktion (aus A), Analyse (aus Mechanismus), Anwendung (aus C), Belege (aus DIP/WEB), Abgrenzung (aus C)
- Alle Zitate mit [@citekeys]
- Trennstriche in H1 (`# Be|griff`)

**Qualität:** 85/100 (First Draft mit vollständigem Material, braucht Überarbeitung)

**WICHTIG:** Der Draft hat jetzt **fundiertes Material für ALLE Sektionen** statt "aus den Fingern gezogen"!

---

### PHASE 6: FINALISIERUNG (MIT CLAUDE)

**Ziel:** Draft → Final Draft (publikationsreif)

---

#### 6A. Überarbeitung mit Claude

**Input:** `Drafts/Draft-Begriff.md`

**Überarbeitung (v5.0-Struktur):**
- Stil (Kriegsreporter-Haltung, Hauptsätze)
- Trennstriche in H1 korrekt? (`# Be|griff`)
- **7 Sektionen vorhanden?** (Definition, Geschichte, Konstruktion, Analyse, Anwendung, Belege, Abgrenzung)
- Definition beantwortet 5 Fragen?
- Geschichte hat narrative Struktur (keine Datenliste)?
- Konstruktion NUR bei zusammengesetzten Begriffen?
- Analyse nutzt 14 Mechanismen (3-5 ausgewählt)?
- Anwendung zeigt Advocatus Diaboli (optional)?
- Abgrenzung zeigt Falsifikation (optional)?
- Jedes Zitat auf eigener Zeile?
- Fließende Prosa (Read-Aloud Test)?

**Output:** `Begriff.md` (Hauptordner)

---

#### 6B. (Optional) Editor-Workflow

**Tool:** `4-EDITOR-WORKFLOW.md` (3-Phasen-Editing)

**Wann nutzen:**
- Wenn Draft stark überarbeitet werden muss
- Wenn höchste Qualität gefordert (Goldstandard)

**Prozess:**
1. Phase 1: ANALYSE (ohne Änderungen)
2. Phase 2: EDITIEREN (strukturell + sprachlich)
3. Phase 3: QUALITY CHECK (Score ≥ 9.0/10)

**Command:**
```bash
# Claude mit Editor-Workflow füttern
cat wort-fabrik/4-EDITOR-WORKFLOW.md Begriff.md | claude
```

**Output:** Publikationsreifer Text (≥ 9.0/10)

---

### PHASE 7: VERIFICATION

**Ziel:** Prüfe, ob alle [@citekeys] in bibliography.bib vorhanden sind

**Tool:** `verify_citations.py`

**Command:**
```bash
python3 wort-fabrik/verify_citations.py
```

**Was passiert:**
- Scannt alle `.md`-Dateien im Hauptordner
- Findet alle `[@citekey]`-Referenzen
- Vergleicht mit `bibliography.bib`
- Zeigt fehlende Citekeys

**Bei fehlenden Citekeys:**
```bash
# Generiert Stubs in to_zotero.bib
python3 wort-fabrik/verify_citations.py --fix

# Dann: Zotero-Import wiederholen (Phase 3)
```

**Erfolg:**
```
✅ Alle Quellen sind in bibliography.bib vorhanden.
```

---

### PHASE 8: PUBLISH

**Ziel:** Commit & Push → Auto-Deploy → gpunkt.org

**Commands:**
```bash
# 1. Status prüfen
git status

# 2. Dateien hinzufügen
git add Begriff.md bibliography.bib

# 3. Commit
git commit -m "feat: add Begriff

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# 4. Push
git push
```

**Was passiert:**
- GitHub Actions triggert Auto-Deploy
- Sync: `WÖRTER/` → `gpunkt-site/content/`
- Site wird neu gebaut
- Live auf gpunkt.org

**Verify:**
```
https://gpunkt.org/Begriff
```

---

## ⚠️ CRITICAL RULES

### 1. Triple-Verification (PFLICHT!)

**Für JEDES Zitat:**
- [ ] Original-Quelle geöffnet (Link funktioniert)
- [ ] Zitat Wort-für-Wort im Original gefunden
- [ ] Kontext stimmt (nicht aus Zusammenhang gerissen)
- [ ] Metadaten korrekt (Name, Funktion, Datum, Anlass)

**Bei JEGLICHEM Zweifel:** Quelle NICHT verwenden!

**Warum:** Falsche Zuschreibung = Rufschädigung + rechtliche Konsequenzen

---

### 2. BibTeX Citekey Standard

**Format:** `autor_jahr` (lowercase, Unterstrich)

**Beispiele:**
- ✅ `merkel_2010`
- ✅ `höcke_2018`
- ✅ `weidel_2025`
- ❌ `Merkel2010`
- ❌ `merkel-2010`

**Konflikte:** `merkel_2010a`, `merkel_2010b`, etc.

---

### 3. Keine Sekundärquellen

**VERBOTEN:**
- ❌ "Correctiv berichtet, dass X sagte..."
- ❌ "Zeitung A über Zeitung B"
- ❌ Indirekte Rede ("Er sagte, dass...")

**ERLAUBT:**
- ✅ Bundestag-Protokolle (Primärquelle)
- ✅ Original-Videos (mit Zeitstempel)
- ✅ Qualitätsmedien (FAZ, SZ, ARD) **nur mit »wörtlicher Rede«**

---

## 📁 DATEI-STRUKTUR

```
WÖRTER/
  Begriff.md                          # Finaler Eintrag
  bibliography.bib                    # Zotero-Export (automatisch)

  wort-fabrik/
    # === RECHERCHE-PROMPTS (Phase 0) ===
    0-RECHERCHE/
      A-LEXIKALISCHE-RECHERCHE.md     # Definition + Etymologie
      B-HISTORISCHE-RECHERCHE.md      # Geschichte (5 Schritte)
      C-DISKURS-RECHERCHE.md          # Anwendung + Abgrenzung

    # === PROMPTS (nummeriert) ===
    1-WEB-RECHERCHE-PROMPT.md         # Web-Recherche (NUR Zitate)
    2-MECHANISMUS-ANALYSE-PROMPT.md   # Mechanismus-Analyse (NUR Analyse)
    3-DRAFT-PROMPT.md                 # Draft schreiben
    4-EDITOR/                         # 3-Phasen-Editing (optional)
      A-ANALYSE.md
      B-EDITING.md
      C-QUALITY-CHECK.md
      WORKFLOW.md

    # === SCRIPTS ===
    bundestag_recherche.py            # DIP-API (Bundestag)
    verify_citations.py               # Citekey-Checker

    # === TEMPLATES ===
    VORLAGE.md                        # Eintrag-Template (v5.0)
    WERKZEUGKASTEN.md                 # 14 Mechanismen (v4.1)

    # === DOKUMENTATION ===
    WORKFLOW.md                       # Diese Datei
    CLAUDE.md                         # Quick-Start + Status

    # === ORDNER ===
    Recherche/                        # Research Outputs
      [Begriff]/                      # Pro Begriff ein Ordner (z.B. Sozialtourismus/)
        A-Lexikalisch.md              # Phase 0A: Definition, Etymologie
        B-Historisch.md               # Phase 0B: Geschichte (5 Schritte)
        C-Diskurs.md                  # Phase 0C: Anwendung, Abgrenzung
        WEB-Recherche.md              # Phase 1b: Web-Zitate
        DIP-*.md                      # Phase 1a: Bundestag-Zitate (mehrere Dateien)
        MECHANISMUS-[Begriff].md      # Phase 4: Mechanismus-Analyse

    Drafts/                           # First Drafts
      Draft-Begriff.md                # Gemini First Draft

    imports/                          # Zotero Import
      to_zotero.bib                   # Temporär (vor Import)

  Anhang/                             # Öffentliche Dokumentation
    KURZANLEITUNG.md                  # Wie sind Einträge aufgebaut?
    WERKZEUGKASTEN-LESER.md           # Transparenz-Dokument
```

---

## 🎯 QUALITÄTSSICHERUNG

**Jeder Eintrag muss bestehen:**

1. **Clarity Test:** Verständlich ohne Vorwissen?
2. **Architecture Test:** Jede Sektion hat innere Logik?
3. **Read-Aloud Test:** Fließt es beim Vorlesen?
4. **Johnson Test:** Klar, vollständig, kein Wort zu viel?

**Durchschnitt ≥ 9.0/10** (bei Editor-Workflow)

---

## 📊 QUALITÄTS-BENCHMARKS

| Quelle | Qualität | Stärke | Schwäche |
|--------|----------|--------|----------|
| A: Lexikalische Recherche | 95/100 | Wörterbücher, Wissenschaft, fundiert | - |
| B: Historische Recherche | 90/100 | Chronologie, Namen, Daten | Zeitaufwendig |
| C: Diskurs-Recherche | 85/100 | Kontext, Funktion, Abgrenzung | Interpretation nötig |
| DIP (Bundestag) | 95/100 | Primärquelle, 100% verifiziert | Nur Plenarprotokolle |
| Web-Recherche | 90/100 | Pressemitteilungen, Interviews | Sekundärquellen-Risiko |
| Mechanismus-Analyse | 90/100 | Präzise Begründungen | Braucht gute Zitate als Input |
| First Draft (mit A-C) | 85/100 | Vollständig, Material für ALLE Sektionen | Braucht Überarbeitung |
| Final Draft (Claude) | 90/100 | Publikationsreif | - |
| Final Draft (Editor) | 95/100 | Goldstandard | Zeitaufwendig |

---

**Letzte Aktualisierung:** 2026-02-06 (v2.0 - Recherche-Phase hinzugefügt)
**Nächste Review:** Nach erstem Testbegriff mit vollständigem Workflow
