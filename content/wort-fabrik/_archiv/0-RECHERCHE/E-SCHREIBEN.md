# E. SCHREIBEN: Wörterbuch-Eintrag (First Draft ohne Belege)

**An:** Gemini (oder andere AI)
**Phase:** 0E — Schreiben + Editieren
**Ziel:** Publikationsreifer Eintrag, basierend AUSSCHLIESSLICH auf bereitgestelltem Recherche-Material

---

## ⚠️ TRANSFORMATION-REGEL (ABSOLUT)

**Du ERFINDEST NICHTS. Du GENERIERST NICHTS aus eigenem Wissen.**

Jede Sektion ist eine **Transformation** von vorgegebenem Material in das Format der VORLAGE v5.0.

- **Material vorhanden →** transformieren
- **Material fehlt →** Sektion weglassen oder `[FEHLENDES MATERIAL]` markieren
- **Niemals →** aus eigenem Wissen ergänzen, auch wenn "offensichtlich"

**Warum:** Die Qualität basiert auf verifizierten Recherchen. KI-Wissen ist nicht verifiziert.

---

## MATERIAL-MAPPING (Übersicht)

| Vorlage-Sektion | Quelle |
|---|---|
| Frontmatter-Tags | D-Mechanismus (dominante Mechanismen) |
| Definition | A-Lexikalisch (Definitionen + Semantik) |
| Geschichte | B-Historisch (Zusammenfassung für Draft) |
| Konstruktion | A-Lexikalisch (Wortbestandteile) |
| Analyse | D-Mechanismus (vollständiger Output) |
| Anwendung | C-Diskurs (Zusammenfassung Anwendung) |
| Belege | **PLACEHOLDER** — wird separat eingebaut |
| Abgrenzung | C-Diskurs (Zusammenfassung Abgrenzung) |

---

## SCHRITT 1: FRONTMATTER & HEADWORD

### ← Material (D-Mechanismus, dominante Mechanismen):

```
[HIER EINFÜGEN: D-Mechanismus — welche Mechanismen sind ● dominant?]
```

### → Aufgabe:

Schreibe Frontmatter:
```yaml
---
title: [Begriff]
language: de
cssclasses: dictionary-entry
tags:
  - Reizwort
  - [Mechanismus 1 — dominant]
  - [Mechanismus 2 — dominant, falls vorhanden]
---
```

Dann Headword mit Silbentrennstrichen `|` (nach Silben, NICHT Morphemen):
- ✅ `# So|zial|tou|ris|mus`
- ❌ `# Sozial|tourismus`

---

## SCHRITT 2: DEFINITION

### ← Material (A-Lexikalisch, Definitionen + semantische Analyse):

```
[HIER EINFÜGEN: A-Lexikalisch — Definitionen, Bedeutungsanalyse, semantischer Kern]
```

### → Aufgabe:

Transformiere zu **3-5 Sätzen**. Beantworte diese 5 Fragen — NUR aus dem Material:

1. **Was ist es?** → Klassifizierung ("Kampfbegriff für X", "Politisches Reizwort für Y")
2. **Wie funktioniert es?** → Mechanismus in einem Satz
3. **Was bewirkt es?** → Wirkung ("suggeriert X", "verschleiert Y", "kriminalisiert Z")
4. **Warum wird es benutzt?** → Funktion/politischer Zweck
5. **Wo steht es?** → Kontext (nur wenn essentiell)

**Stil:** Verben der Manipulation (tarnt, verschleiert, kriminalisiert). KEIN Moral-Vokabular (zynisch, perfide).

---

## SCHRITT 3: GESCHICHTE

### ← Material (B-Historisch, Abschnitt "7. Zusammenfassung für Draft"):

```
[HIER EINFÜGEN: B-Historisch — Zusammenfassung für Draft (oder Chronologie + 5 Schritte falls Zusammenfassung fehlt)]
```

### → Aufgabe:

Transformiere zu narrativer Geschichte (**3-5 Sätze**). KEINE Datenliste — erzähle die Geschichte.

**Fettdruck für Anker-Daten:**
- **Jahre**, **Namen**, **Parteien/Institutionen**, **Schlüssel-Kontexte**, **Status** (Unwort etc.)

**Beispiel-Stil:**
> Geprägt **2013** von **CSU/CDU-Politikern** im Kontext der **EU-Osterweiterung**. Der Begriff zielte darauf, Freizügigkeitsrechte als „Missbrauch" zu delegitimieren. Erneut aufgegriffen **2022** von **Friedrich Merz**. Zum **„Unwort des Jahres 2013"** gewählt.

*Bei Vulgärsprache ohne dokumentierbare Geschichte: Sektion weglassen.*

---

## SCHRITT 4: KONSTRUKTION

### ← Material (A-Lexikalisch, Wortbestandteile/Morphologie):

```
[HIER EINFÜGEN: A-Lexikalisch — Wortbestandteile, semantische Formel]
```

### → Aufgabe:

Transformiere zu **1-2 Sätzen** nach diesem Format:

`"Teil1" (Bedeutung) + "Teil2" (Bedeutung) = Wirkung.`

**Beispiel:**
> „Sozial-" (Sozialsystem als Ziel) + „Tourismus" (Vergnügungsreise) = existenzielle Not wird zu freiwilligem Konsum.

*Nur bei zusammengesetzten Begriffen. Bei einfachen Wörtern: Sektion weglassen.*

---

## SCHRITT 5: ANALYSE

### ← Material (D-Mechanismus, vollständiger Output):

```
[HIER EINFÜGEN: D-Mechanismus — vollständiger Output mit ●◐-Mechanismen und Begründungen]
```

### → Aufgabe:

Übernehme direkt. Minimales Editieren (Stil, Kürze). KEIN Hinzufügen neuer Mechanismen.

Format:
```
*   ● **Mechanismus (dominant):** Begründung zeigt WIE es wirkt — nicht nur DASS.
*   ● **Mechanismus 2:** Begründung.
*   ◐ **Mechanismus 3 (teilweise):** Begründung.
```

---

## SCHRITT 6: ANWENDUNG

### ← Material (C-Diskurs, Abschnitt "4. Zusammenfassung Anwendung-Sektion"):

```
[HIER EINFÜGEN: C-Diskurs — Zusammenfassung Anwendung (Advocatus Diaboli)]
```

### → Aufgabe:

Transformiere zu **2-3 Sätzen**. Format: "Aus Sicht des Sprechers..." — zeigt, warum der Begriff verfängt, ohne ihn zu rechtfertigen.

*Optional. Falls kein Material → Sektion weglassen.*

---

## SCHRITT 7: BELEGE (PLACEHOLDER — NICHT AUSFÜLLEN)

```markdown
## Belege

● [BELEG 1: AUSSTEHEND]

● [BELEG 2: AUSSTEHEND]

● [BELEG 3: AUSSTEHEND]
```

**Nicht ergänzen. Nicht raten. Placeholder bleibt bis zur DIP-Verifikation.**

---

## SCHRITT 8: ABGRENZUNG

### ← Material (C-Diskurs, Abschnitt "4. Zusammenfassung Abgrenzung-Sektion"):

```
[HIER EINFÜGEN: C-Diskurs — Zusammenfassung Abgrenzung ("Nicht gemeint, wenn...")]
```

### → Aufgabe:

Übernehme die „Nicht gemeint, wenn..."-Formulierungen direkt. Minimal editieren.

*Optional. Falls kein Material → Sektion weglassen.*

---

## SCHRITT 9: 3-PHASEN-EDITOR

Führe jetzt den vollständigen 3-Phasen-Editor durch. **Keine weiteren Informationen hinzufügen — nur verfeinern, was da ist.**

### PHASE 1: ANALYSE (Diagnostiziere — ändere nichts)

Prüfe schonungslos:
- **Definition:** Alle 5 Fragen beantwortet? Präzise Verben?
- **Geschichte:** Narrativ (nicht Liste)? Fettdruck gesetzt?
- **Konstruktion:** Formel klar und direkt?
- **Analyse:** Begründungen zeigen WIE (nicht nur DASS)?
- **Anwendung:** Advocatus Diaboli klar, keine Rechtfertigung?
- **Abgrenzung:** Draft-fertig formuliert?
- **Gesamt:** Fließt es beim Vorlesen (Read-Aloud Test)? Kein Wort zu viel (Johnson Test)?

Liefere: Strukturierten Analyse-Report mit Editierplan.

### PHASE 2: EDITIEREN

Basierend auf Phase 1:
- Strukturelle Schnitte (was gehört nicht rein?)
- Logik-Reparaturen (Übergänge, Progression)
- Sprachlicher Schliff: Passiv → Aktiv, Substantivierungen → Verben, Füllwörter raus

Zeige Thinking für größere Änderungen:
```
[THINKING: Warum ändere ich X?]
```

### PHASE 3: QUALITY CHECK

Score 1-10 für jede Dimension:
1. Gedankliche Logik
2. Strukturelle Klarheit
3. Effizienz und Schnitt
4. Sprachliche Präzision
5. Konkretheit

**Durchschnitt < 9.0 → zweite Iteration sofort.**

---

## OUTPUT (alles in einem Run)

1. **Analyse-Report** (Phase 1, prägnant)
2. **Editierter Eintrag** (Phase 2, mit Thinking für größere Schnitte)
3. **Quality-Score + finaler Eintrag** (Phase 3)

**Der finale Eintrag ist publikationsreif — bis auf die Belege-Placeholders.**

---

## NACH DIESEM PROMPT

```
→ DIP-Belege (bereits parallel laufend): Triple-verifizierte Zitate einbauen
→ Citekeys in Zotero importieren
→ Fertig
```
