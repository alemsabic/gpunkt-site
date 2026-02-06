# DRAFT-PROMPT: Wörterbuch-Eintrag schreiben

**An:** Gemini (oder andere AI)
**Aufgabe:** Vollständigen Wörterbuch-Eintrag schreiben basierend auf Recherche-Material
**Version:** 5.1 (Updated für VORLAGE v5.0 + Recherche-Phase)

---

## INPUT: RECHERCHE-MATERIAL

Du bekommst vollständiges Recherche-Material für einen Wörterbuch-Eintrag:

**A. LEXIKALISCHE RECHERCHE**
- Definitionen (Wörterbücher, Wissenschaft)
- Etymologie (Wortherkunft)
- Semantische Analyse (bei zusammengesetzten Begriffen)
→ **Material für:** Definition, Konstruktion

**B. HISTORISCHE RECHERCHE**
- Die 5 Schritte: Ursprung → Instrumentalisierung → Kontext → Verbreitung → Gegenwart
→ **Material für:** Geschichte

**C. DISKURS-RECHERCHE**
- Funktions-Analyse (Advocatus Diaboli)
- Abgrenzungs-Kontexte (wissenschaftlich, satirisch, etc.)
→ **Material für:** Anwendung, Abgrenzung

**MECHANISMUS-ANALYSE**
- 14 Mechanismen analysiert (● dominant, ◐ teilweise)
→ **Material für:** Analyse

**BELEGE (DIP + WEB)**
- Originalzitate mit Metadaten
→ **Material für:** Belege

---

[RECHERCHE-MATERIAL WIRD HIER EINGEFÜGT]

---

## AUFGABE

Schreibe einen **vollständigen Wörterbuch-Eintrag** im Markdown-Format basierend auf dieser Recherche.

**WICHTIG:** Dieser Eintrag folgt VORLAGE v5.0 — 7-Sektionen-Struktur mit 14 Mechanismen. Narrative Geschichte. Konstruktion zeigt semantische Formel. Anwendung und Abgrenzung optional. Die vier Tests als Standard.

---

## FORMAT-VORLAGE (v5.0 — 7 Sektionen)

```markdown
---
title: [Begriff]
language: de
cssclasses: dictionary-entry
tags:
  - Reizwort
  - [Mechanismus 1]
  - [Mechanismus 2]
---

# [Be|griff|mit|Trenn|stri|chen]

## Definition

[3-5 Sätze. Beantworte die 5 Fragen: Was? Wie? Wirkung? Warum? Kontext?]

## Geschichte

[NARRATIVE STRUKTUR: Erzähle die Geschichte des Begriffs. Ursprung → Instrumentalisierung → Kontext → Verbreitung → Gegenwart. Mit Fettdruck für Anker-Daten (Jahre, Namen, Kontexte). Bei Vulgärsprache optional.]

## Konstruktion

[NUR bei zusammengesetzten Begriffen: "Teil 1" (Bedeutung) + "Teil 2" (Bedeutung) = Wirkung.]

## Analyse

*   ● **[Mechanismus 1] (dominant):** [Präzise Begründung, zeigt WIE es wirkt]
*   ● **[Mechanismus 2]:** [Begründung]
*   ◐ **[Mechanismus 3] (teilweise):** [Begründung]

## Anwendung

[OPTIONAL: Advocatus Diaboli — Warum nutzt jemand dieses Wort? Was denkt der Sprecher? Verhindert Vorwurf der Parteilichkeit.]

## Belege

● [Name (Partei, Funktion) Kontext Datum [@citekey]: »Zitat mit ==Begriff==.«

● [Weiteres Zitat] [@citekey2]: »...«

## Abgrenzung

[OPTIONAL: Wann ist unsere Analyse NICHT zutreffend? Falsifikationsprinzip. Z.B. wissenschaftliche Verwendung, Satire, historische Zitate.]
```

---

## REGELN

### 0. WIE DU DAS RECHERCHE-MATERIAL NUTZT

Du bekommst **fünf Recherche-Dokumente** als Input:

**A-Lexikalisch.md:**
- Nutze die **beste Definition** für die Definition-Sektion
- Nutze die **Etymologie** falls relevant für das Verständnis
- Nutze die **semantische Formel** für die Konstruktion-Sektion (bei zusammengesetzten Begriffen)

**B-Historisch.md:**
- Nutze die **Zusammenfassung für Draft** (narrativ, mit Fettdruck für Anker-Daten)
- Falls nicht vorhanden: Nutze die 5 Schritte (Ursprung → Instrumentalisierung → Kontext → Verbreitung → Gegenwart)
- Bei Vulgärsprache: Falls "Keine dokumentierbare Geschichte" → Sektion weglassen

**C-Diskurs.md:**
- Nutze die **Zusammenfassung für Anwendung-Sektion** (Advocatus Diaboli, 2-3 Sätze)
- Nutze die **Abgrenzungen** (draft-fertig formuliert: "Nicht gemeint, wenn...")
- Falls keine legitimen Kontexte → Abgrenzung weglassen

**MECHANISMUS-Begriff.md:**
- Nutze die **Gesamtanalyse** (dominante Mechanismen mit ●)
- Nutze die **Begründungen** (zeigen WIE, nicht nur DASS)
- Wähle 3-5 relevante Mechanismen

**DIP-Begriff.md + WEB-Begriff.md:**
- Nutze die **ausgewählten Zitate** (wurden bereits manuell gesichtet!)
- Chronologisch ordnen (früheste zuerst)
- Format: `● Name (Partei, Funktion) Kontext Datum [@citekey]: »Zitat mit ==Begriff==.«`

**WICHTIG:** Du musst nicht mehr "raten" oder "kreativ sein" — alle Sektionen haben fundiertes Material!

---

### 1. Frontmatter

```yaml
---
title: Sozialtourismus
language: de
cssclasses: dictionary-entry
tags:
  - Reizwort
  - Inversion
  - Kriminalisierung
---
```

**Tags:**
- **"Reizwort"** — PFLICHT (Oberbegriff für Kampfbegriffe und diskriminierende Vulgärsprache)
- **1-2 dominante Mechanismen** — aus der Analyse-Sektion

---

### 2. Headword mit Trennstrichen

**Format:** `# Be|griff|mit|Trenn|stri|chen`

**Regeln:**
- Trennstriche `|` nach **Silben** (nicht Morphemen!)
- Beispiele:
  - "Sozialtourismus" → `# So|zial|tou|ris|mus`
  - "Remigration" → `# Re|mi|gra|tion`
  - "Putinversteher" → `# Pu|tin|ver|ste|her`

---

### 3. Definition (3-5 Sätze)

**Struktur: Die fünf Fragen**

Eine Definition muss beantworten (typisch 3-5 Sätze):

1. **Was ist es?** (Klassifizierung)
   - Kampfbegriff für X / Euphemismus für Y
   - Sei präzise: "Rechtsextremer Kampfbegriff" > "Kampfbegriff"

2. **Wie funktioniert es?** (Mechanismus kurz)
   - Die semantische Operation in einem Satz

3. **Was bewirkt es?** (Wirkung)
   - Konkret: "suggeriert X", "verschleiert Y", "kriminalisiert Z"
   - Mehrere Wirkungen möglich

4. **Warum wird es benutzt?** (Funktion)
   - Der politische Zweck

5. **Wo steht es?** (Kontext — optional)
   - Nur wenn essentiell

**Stil:**
- Hauptsätze als Grundgerüst
- Subordination wo sie Klarheit schafft (ein Relativsatz ist OK!)
- Verben der Manipulation: "tarnt", "verschleiert", "kriminalisiert", "entmenschlicht", "normalisiert"
- **KEINE Moral:** "zynisch", "perfide" → raus!
- **Kriegsreporter-Haltung:** Zeigen, nicht bewerten

**Länge:** 3-5 Sätze, so viele wie nötig für vollständiges Verständnis

**Beispiel (gut):**
> Kampfbegriff zur Diffamierung von Migration als Sozialbetrug. Suggeriert, Menschen fliehen zum Vergnügen und besuchen Sozialsysteme wie Urlaubsziele. Verschleiert Fluchtgründe (Armut, Krieg, Diskriminierung) und stellt sie als freiwillige Konsumentscheidung dar. Kriminalisiert rechtmäßige EU-Freizügigkeit als systematischen Missbrauch.

---

### 4. Geschichte (NARRATIVE STRUKTUR!)

**WICHTIG:** Bei Vulgärsprache ist diese Sektion optional.

**WICHTIG:** Keine Datenliste! Erzähle die **Geschichte des Begriffs**.

**Die fünf Akte:**

1. **Ursprung** (falls relevant)
   - Hatte der Begriff eine neutrale Herkunft?
   - "Ursprünglich ein soziologischer Fachbegriff für..."
   - Nur wenn die Umdeutung Teil der Manipulation ist

2. **Erste politische Instrumentalisierung**
   - Wer hat ihn geprägt/instrumentalisiert?
   - "Geprägt 2013 von CSU/CDU-Politikern..."
   - "Politisch umgedeutet wurde er in den 1990ern von..."

3. **Kontext**
   - Warum entstand er? Welches Ereignis?
   - "...im Kontext der EU-Osterweiterung"
   - "...im Kontext der Verschwörungstheorie vom 'Großen Austausch'"

4. **Verbreitung**
   - Wer popularisierte ihn? Wer übernahm ihn?
   - "Popularisiert durch X, übernommen von Y"

5. **Gegenwart**
   - Wo steht er heute?
   - "Zum 'Unwort des Jahres 2023' gewählt"

**Format:** Fließende Sätze (nicht Listen!)

**Fettdruck für Anker-Daten (v4.1 NEU!):**
Markiere wichtige Daten **fett**, damit das Auge die Historie schnell erfassen kann:
- **Jahre** (2013, 2022)
- **Namen** (CSU-Politikern, Friedrich Merz)
- **Parteien/Institutionen** (AfD, Front National)
- **Schlüssel-Kontexte** (EU-Osterweiterung, Großer Austausch)
- **Status** (Unwort des Jahres 2023)

**Länge:** Typisch 3-5 Sätze, so viele wie die Geschichte braucht

**Beispiel (gut — narrative Struktur mit Fettdruck):**
> Geprägt **2013** von **CSU/CDU-Politikern** (Hans-Peter Friedrich, Horst Seehofer, Alexander Dobrindt) im Kontext der **EU-Osterweiterung** und verstärkter Migration aus Osteuropa, insbesondere Roma-Gemeinden. Der Begriff zielte darauf, Freizügigkeitsrechte als "Missbrauch" zu delegitimieren. Erneut aufgegriffen **2022** von **Friedrich Merz** im Kontext ukrainischer Geflüchteter. Zum **"Unwort des Jahres 2013"** gewählt.

**Beispiel (schlecht — Datenliste):**
> CSU/CDU 2013 (Friedrich, Seehofer, Dobrindt) im Kontext der EU-Osterweiterung. Erneut 2022: Merz (ukrainische Geflüchtete). Unwort des Jahres 2013.

**Siehst du den Unterschied?** Die erste erzählt eine Geschichte. Die zweite listet Fakten.

---

### 5. Konstruktion (1-2 Sätze)

**WICHTIG:** NUR bei zusammengesetzten Begriffen! Bei einfachen Wörtern oder Vulgärsprache entfällt diese Sektion.

**Format:** `"Teil1" (Bedeutung) + "Teil2" (Bedeutung) = Wirkung.`

**Funktion:** Zeigt die semantische Formel — wie erzeugen die Wortbestandteile ihre manipulative Bedeutung?

**Länge:** 1-2 Sätze (hier ist Kürze Prinzip!)

**Beispiel:**
> "Sozial-" (Sozialsystem als Ziel) + "Tourismus" (Vergnügungsreise) = existenzielle Not wird zu freiwilligem Konsum, Flucht zu Freizeitvergnügen.

---

### 6. Analyse (3-5 Mechanismen aus 14)

**Format:** Ausführliches Format mit Graduierung

```markdown
*   ● **Mechanismus (dominant):** Begründung, die das WIE erklärt, nicht nur das DASS.
*   ● **Mechanismus 2:** Begründung in einem oder zwei Sätzen.
*   ◐ **Mechanismus 3 (teilweise):** Begründung.
```

**Die 14 Mechanismen in 3 Clustern:**
- **Cluster A (Identität):** Ethnisierung, Kriminalisierung, Sexualisierung, Infantilisierung, Pathologisierung
- **Cluster B (Realität):** Euphemismus, Inversion, Naturalisierung, Entpolitisierung, Ontologisierung
- **Cluster C (Eskalation):** Quantifizierung, Militarisierung, Temporalisierung, Entmenschlichung

**Eskalationsleiter:** A→B→C (Markierung → Realitätsverzerrung → Gewalt)

**Graduierung:**
- `●` = dominant (ohne diesen Mechanismus funktioniert der Begriff nicht)
- `◐` = teilweise (schwingt mit, ist kontext-abhängig, nicht zentral)

**Begründung:**
- **Präzise:** Zeige WIE der Mechanismus wirkt
- **Konkret:** Welche Umkehrung? Welche Verschleierung? Welche Masse?
- **So lang wie nötig:** Typisch 1-2 Sätze pro Mechanismus

**Anzahl:** 3-5 relevante Mechanismen (nicht alle 14!)

---

### 7. Anwendung (OPTIONAL — Advocatus Diaboli)

**Funktion:** Zeigt die Perspektive des Sprechers — warum ist der Begriff attraktiv? Verhindert Vorwurf der Parteilichkeit.

**Format:** 2-3 Sätze, die erklären:
- Was denkt der Sprecher, wenn er diesen Begriff benutzt?
- Welche subjektive Berechtigung sieht er?
- Warum ist der Begriff verführerisch?

**Beispiel:**
> Aus Sicht des Sprechers erscheint "Sozialtourismus" als treffende Beschreibung: Wenn Menschen zwischen Heimat und Deutschland pendeln, wirkt das wie "hin und her reisen". Die Metapher des Tourismus fühlt sich intuitiv richtig an, weil sie ein sichtbares Muster (Pendeln) in ein bekanntes Frame (Urlaub) übersetzt. Der Begriff erlaubt es, Ressentiments auszudrücken, ohne offen rassistisch zu wirken.

**Wann weglassen:** Bei reiner Vulgärsprache oder wenn der Begriff rein destruktiv ist (keine plausible subjektive Berechtigung).

---

### 8. Belege (mind. 2-3)

**Format:**
```markdown
## Belege

● Name (Partei, Funktion) Kontext Datum [@citekey]: »Zitat mit ==Begriff==.«

● Name (Partei, Funktion) Kontext Datum [@citekey]: »Zitat.«
```

**Regeln:**
- Jedes Zitat auf **neuer Zeile mit Leerzeile davor**
- Marker: `●` (Kreis) am Zeilenanfang
- Kontext VOR Zitat: Name (Partei, Funktion) Kontext Datum
- Citekeys: `[@nachname_jahr]`
- Begriff im Zitat: `==Begriff==` (Markdown Highlight)
- Guillemets: `»«` (nicht "normale Anführungszeichen")
- Chronologisch (früheste zuerst)

**Wichtig:** Jedes Zitat braucht eine **Leerzeile davor** — sonst wird es unleserlich!

---

### 9. Abgrenzung (OPTIONAL — Falsifikationsprinzip)

**Funktion:** Zeigt, wann unsere Analyse NICHT zutrifft. Macht deutlich, dass der Kontext entscheidet, nicht das Wort allein.

**Format:** "Nicht gemeint, wenn [Bedingung]. [Kurze Erklärung]."

**Beispiel:**
> Nicht gemeint, wenn "Sozialtourismus" in der Migrationsforschung verwendet wird, um die statistische Rückwanderung von Rentnern zu beschreiben. Nicht gemeint, wenn der Begriff in eindeutig erkennbarer Satire genutzt wird, die die Mechanismen sichtbar macht, statt sie zu nutzen.

**Typische Kontexte für Abgrenzung:**
- Wissenschaftliche oder fachliche Verwendung
- Eindeutig erkennbare Satire oder Parodie
- Historische oder analytische Zitate

**Wann weglassen:** Bei reiner Vulgärsprache oder wenn keine legitime Verwendung existiert.

---

## STIL-VORGABEN

### ✅ DO:

**Für Definition & Geschichte:**
- **Hauptsätze als Grundgerüst** — klare Struktur
- **Subordination wo sie hilft** — ein Relativsatz ist besser als zwei holprige Hauptsätze
- **Fließende Prosa** — muss beim Vorlesen fließen (Read-Aloud Test!)
- **Verben vor Nomen** — "verschleiert" statt "Verschleierung"
- **Aktiv statt Passiv** — "kriminalisiert" statt "wird kriminalisiert"
- **Spezifisch** — "CSU 2013" statt "Konservative"

**Für Geschichte:**
- **Narrative Struktur** — erzähle die Geschichte des Wortes
- **Chronologische & kausale Logik** — Ursprung → Instrumentalisierung → Kontext → Verbreitung → Gegenwart
- **Fließende Sätze** — KEINE Datenlisten!
- **Fettdruck für Anker-Daten** — Jahre, Namen, Parteien, Kontexte (damit das Auge schnell erfassen kann)

### ❌ DON'T:

- **Excessive Nebensatzketten** — ein Relativsatz OK, drei zu viel
- **Nominalisierungen** — "Die Verwendung erfolgt" → "Menschen nutzen"
- **Superlative** — "extrem", "unglaublich", "massiv"
- **Moral** — "zynisch", "perfide", "menschenverachtend"
- **Enthusiasmus** — "wichtig!", "beachtenswert"
- **Datenlisten in Geschichte** — "X (Jahr), Y (Jahr)" → erzähle die Geschichte!

---

## DIE VIER TESTS

Jeder Eintrag muss bestehen:

1. **Clarity Test:** Verständlich ohne Vorwissen?
2. **Architecture Test:** Jede Sektion hat innere Logik?
3. **Read-Aloud Test:** Fließt es beim Vorlesen?
4. **Johnson Test:** Klar, vollständig, kein Wort zu viel?

Wenn ein Test fehlschlägt → überarbeite den Eintrag.

---

## QUALITÄTSKRITERIEN

**Dein Eintrag muss erfüllen:**

✅ Alle Zitate aus der Recherche übernommen (mit [@citekeys])
✅ Trennstriche in H1 (`|` zwischen Silben)
✅ **H2-Überschriften (v5.0):** `## Definition`, `## Geschichte`, `## Konstruktion`, `## Analyse`, `## Anwendung`, `## Belege`, `## Abgrenzung`
✅ **Definition beantwortet 5 Fragen** (Was? Wie? Wirkung? Warum? Kontext?)
✅ **Geschichte hat narrative Struktur** (erzählt Geschichte, keine Datenliste!)
✅ **Geschichte: Fettdruck für Anker-Daten** (Jahr, Name, Kontext)
✅ **Konstruktion NUR bei zusammengesetzten Begriffen** (zeigt semantische Formel)
✅ **Analyse nutzt 14 Mechanismen** (3-5 relevante, nicht alle!)
✅ **Analyse: Ausführliches Format** (●/**Mechanismus:** Begründung zeigt WIE)
✅ Analyse graduell (●◐)
✅ **Anwendung optional** (Advocatus Diaboli — Warum nutzt jemand dieses Wort?)
✅ **Abgrenzung optional** (Falsifikationsprinzip — Wann trifft Analyse NICHT zu?)
✅ **Begründungen präzise** (so klar wie nötig!)
✅ Kriegsreporter-Stil (trocken, keine Moral)
✅ Begriff in Zitaten mit `==Begriff==` markiert
✅ **Jedes Zitat auf eigener Zeile mit Leerzeile davor**
✅ Fließende Prosa (Read-Aloud Test bestanden)

---

## BEISPIEL-OUTPUT (Referenz — GOLDSTANDARD)

```markdown
---
title: Sozialtourismus
language: de
cssclasses: dictionary-entry
tags:
  - Reizwort
  - Inversion
  - Kriminalisierung
---

# So|zial|tou|ris|mus

## Definition

Kampfbegriff zur Diffamierung von Migration als Sozialbetrug. Suggeriert, Menschen fliehen zum Vergnügen und besuchen Sozialsysteme wie Urlaubsziele. Verschleiert Fluchtgründe (Armut, Krieg, Diskriminierung) und stellt sie als freiwillige Konsumentscheidung dar. Kriminalisiert rechtmäßige EU-Freizügigkeit als systematischen Missbrauch.

## Geschichte

Geprägt **2013** von **CSU/CDU-Politikern** (Hans-Peter Friedrich, Horst Seehofer, Alexander Dobrindt) im Kontext der **EU-Osterweiterung** und verstärkter Migration aus Osteuropa, insbesondere Roma-Gemeinden. Der Begriff zielte darauf, Freizügigkeitsrechte als "Missbrauch" zu delegitimieren. Erneut aufgegriffen **2022** von **Friedrich Merz** im Kontext ukrainischer Geflüchteter. Zum **"Unwort des Jahres 2013"** gewählt.

## Konstruktion

"Sozial-" (Sozialsystem als Ziel) + "Tourismus" (Vergnügungsreise) = existenzielle Not wird zu freiwilligem Konsum, Flucht zu Freizeitvergnügen.

## Analyse

*   ● **Inversion (dominant):** Kehrt die Realität um. Die existenzielle Not einer Flucht wird semantisch in ein Luxusproblem ("Tourismus") verwandelt, der Schutzsuchende wird zum Urlaubsgast umgedeutet.
*   ● **Kriminalisierung:** Delegitimiert geltendes Recht. Die legale Inanspruchnahme von EU-Freizügigkeit wird als "Missbrauch" oder "Betrug" gerahmt, obwohl sie rechtmäßig ist.
*   ◐ **Ethnisierung (teilweise):** Der Begriff nennt keine Gruppe, zielt aber diskursiv fast ausschließlich auf Roma und Menschen aus Südosteuropa (Antiziganismus).

## Anwendung

Aus Sicht des Sprechers erscheint "Sozialtourismus" als treffende Beschreibung: Wenn Menschen zwischen Heimat und Deutschland pendeln, wirkt das wie "hin und her reisen". Die Metapher des Tourismus fühlt sich intuitiv richtig an, weil sie ein sichtbares Muster (Pendeln) in ein bekanntes Frame (Urlaub) übersetzt. Der Begriff erlaubt es, Ressentiments auszudrücken, ohne offen rassistisch zu wirken.

## Belege

● Hans-Peter Friedrich (CSU, Bundesinnenminister) im Spiegel-Interview März 2013 [@friedrich_2013]: »Wer aber nur kommt, um Sozialleistungen zu kassieren, der missbraucht das Freizügigkeitsrecht. Diesen ==Sozialtourismus== müssen wir unterbinden.«

● Horst Seehofer (CSU, Parteivorsitzender) bei der Kreuth-Klausur Januar 2013 [@seehofer_2013]: »Wir werden uns gegen Zuwanderung in die deutschen Sozialsysteme wehren – bis zur letzten Patrone.«

## Abgrenzung

Nicht gemeint, wenn "Sozialtourismus" in der Migrationsforschung verwendet wird, um die statistische Rückwanderung von Rentnern zu beschreiben. Nicht gemeint, wenn der Begriff in eindeutig erkennbarer Satire genutzt wird, die die Mechanismen sichtbar macht, statt sie zu nutzen.
```

---

## STARTBEFEHL

**Schreibe jetzt den vollständigen Wörterbuch-Eintrag basierend auf der Recherche oben.**

**Wichtig:**
- Nutze ALLE Zitate aus der Recherche
- Trennstriche in H1 nach Silben
- **H2-Überschriften v5.0:** `## Definition`, `## Geschichte`, `## Konstruktion`, `## Analyse`, `## Anwendung`, `## Belege`, `## Abgrenzung`
- **Definition: 3-5 Sätze, beantworte die 5 Fragen**
- **Geschichte: NARRATIVE STRUKTUR + FETTDRUCK** (erzähle die Geschichte mit fetten Anker-Daten! Bei Vulgärsprache optional.)
- **Konstruktion: NUR bei zusammengesetzten Begriffen** (semantische Formel zeigen)
- **Analyse: 14 Mechanismen, 3-5 auswählen** (●/**Mechanismus:** Begründung zeigt WIE)
- **Anwendung: Optional** (Advocatus Diaboli — Warum nutzt jemand dieses Wort?)
- **Abgrenzung: Optional** (Falsifikationsprinzip — Wann trifft Analyse NICHT zu?)
- Kriegsreporter-Stil (trocken, keine Moral)
- Exakte Struktur wie Vorlage v5.0
- **Jedes Zitat auf eigener Zeile mit Leerzeile davor**
- Fließende Prosa (Read-Aloud Test!)

**Die vier Tests bestehen:**
1. Clarity Test: Verständlich ohne Vorwissen?
2. Architecture Test: Jede Sektion hat Logik?
3. Read-Aloud Test: Fließt es?
4. Johnson Test: Klar, vollständig, kein Wort zu viel?
