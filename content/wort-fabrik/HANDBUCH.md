# HANDBUCH: Einen Begriff von Null bis online

**Projekt:** gpunkt.org — Dokumentarisches Wörterbuch politischer Reizwörter

---

## WAS DU BRAUCHST

- Terminal (für Scan und Verify)
- KI-Chat (Claude oder Gemini, für Schritte 2–4)
- Zotero (für Schritt "Quellen sichern")
- Texteditor (Obsidian oder beliebig)

---

## SCHRITT 1: SCAN (Terminal, ~10 min passiv)

**Was:** Bundestag-Protokolle nach dem Begriff durchsuchen.

```bash
cd /Users/alemsabic/Desktop/MEMEX/WÖRTER
python3 wort-fabrik/1-SCAN.py "Begriff"
```

**Output:** `wort-fabrik/Recherche/Begriff/DIP-Begriff.md`

→ Scan läuft im Hintergrund. Weiter mit Schritt 2.

---

## SCHRITT 2: SICHTEN (KI-Chat, ~3 min)

**Was:** Die besten 8-10 Zitate aus dem Scan auswählen lassen.

**So geht's:**
1. `wort-fabrik/2-SICHTEN.md` öffnen — **komplett kopieren**
2. Neuen KI-Chat öffnen (Claude oder Gemini)
3. Inhalt von `2-SICHTEN.md` einfügen
4. Danach `DIP-Begriff.md` einfügen (den kompletten Inhalt)
5. Sende ab

**Output:** Ein Block, der so aussieht:
```
## KONTEXT-MATERIAL (Bundestag-Recherche)
### Affirmativ ...
### Kritisch ...
### BibTeX ...
```

6. Diesen Block **kopieren** → für Schritt 3 bereithalten

---

## SCHRITT 3: DRAFT (KI-Chat, ~5 min)

**Was:** Den vollständigen Wörterbuch-Eintrag schreiben lassen.

**So geht's:**
1. `wort-fabrik/3-DRAFT-THIS.md` öffnen — **komplett kopieren**
2. Neuen KI-Chat öffnen
3. Inhalt von `3-DRAFT-THIS.md` einfügen
4. Ganz oben bei `**Begriff:** [HIER EINSETZEN]` → Begriff eintragen
5. Unter der Linie `---` nach dem Begriff → **KONTEXT-MATERIAL** aus Schritt 2 einfügen
6. Sende ab

**Output:** Vollständiger Wörterbuch-Eintrag mit allen Sektionen.
Die Belege-Sektion enthält noch Platzhalter — das ist gewollt.

7. Output **speichern** als `wort-fabrik/Drafts/Begriff-draft.md`

---

## SCHRITT 4: BELEGE EINSETZEN (manuell, ~5-8 min)

**Was:** Die Platzhalter in der Belege-Sektion mit echten Zitaten füllen.

**So geht's:**
1. `Begriff-draft.md` öffnen
2. Im KONTEXT-MATERIAL (aus Schritt 2) die besten 3-4 Zitate aussuchen
3. Die `[BELEG X: AUSSTEHEND]`-Platzhalter ersetzen durch:
```
● **Name** (Funktion, Datum) [@citekey]: »Zitat«
```
4. Datei speichern als `Begriff.md` im Root (`/Users/alemsabic/Desktop/MEMEX/WÖRTER/`)

---

## SCHRITT 4b: EDIT (KI-Chat, optional, ~10-15 min)

**Was:** Den Eintrag auf Goldstandard polieren.

**So geht's:**
1. `wort-fabrik/4-EDIT-THIS.md` öffnen — **komplett kopieren**
2. Neuen KI-Chat öffnen
3. Inhalt von `4-EDIT-THIS.md` einfügen
4. Danach `Begriff.md` einfügen
5. Sende ab
6. Output überschreibt `Begriff.md`

**Wann nötig:** Nur wenn Draft grobe Schwächen hat oder Goldstandard-Qualität gefordert ist.

---

## SCHRITT 5: QUELLEN SICHERN (Zotero, ~3 min)

**Was:** BibTeX-Einträge in Zotero importieren → `bibliography.bib` aktualisieren.
**Warum:** Pandoc braucht `bibliography.bib` für die [@citekey]-Darstellung auf gpunkt.org.

**So geht's:**
1. Im KONTEXT-MATERIAL (aus Schritt 2) den **BibTeX-Block** kopieren
2. Datei öffnen: `wort-fabrik/imports/to_zotero.bib`
3. BibTeX einfügen (mit Kommentar-Zeile):
```
% === Begriff (Datum) ===
@misc{citekey1, ...}
@misc{citekey2, ...}
```
4. Zotero öffnen → **File → Import** → `to_zotero.bib` auswählen
5. Zotero: **Better BibTeX → Export Library** → Ziel: `bibliography.bib` im Root
   - ✅ "Keep updated" muss aktiviert sein
6. `to_zotero.bib` leeren für nächsten Begriff:
```bash
> wort-fabrik/imports/to_zotero.bib
```

---

## SCHRITT 6: VERIFY (Terminal, ~1 min)

**Was:** Prüfen ob alle Citekeys im Eintrag auch in `bibliography.bib` vorhanden sind.

```bash
python3 wort-fabrik/5-VERIFY.py
```

**Erfolg:**
```
✅ Alle Quellen sind in bibliography.bib vorhanden.
```

**Fehler:**
```bash
python3 wort-fabrik/5-VERIFY.py --fix
# → generiert Stubs → Schritt 5 wiederholen
```

---

## SCHRITT 7: PUBLISH (Terminal, ~1 min)

```bash
git add Begriff.md bibliography.bib
git commit -m "feat: add Begriff

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
git push
```

→ GitHub Actions → auto-deploy → gpunkt.org/Begriff (ca. 2 min)

---

## ZUSAMMENFASSUNG

```
TERMINAL         python3 1-SCAN.py "Begriff"
                        ↓ (läuft im Hintergrund)
KI-CHAT          2-SICHTEN.md + DIP-Begriff.md
                        ↓
                 → KONTEXT-MATERIAL kopieren
                        ↓
KI-CHAT          3-DRAFT-THIS.md + Begriff + KONTEXT-MATERIAL
                        ↓
                 → Draft speichern
                        ↓
MANUELL          Belege-Platzhalter füllen → Begriff.md
                        ↓  (optional: 4-EDIT-THIS.md)
ZOTERO           BibTeX aus KONTEXT-MATERIAL → to_zotero.bib → Import
                        ↓
TERMINAL         python3 5-VERIFY.py
                        ↓
TERMINAL         git push → gpunkt.org
```

**Aktive Zeit: ~20 min. Ziel: unter 30 min pro Begriff.**

---

*Letzte Aktualisierung: 2026-02-08 (v5.0 — idiotensicher)*
