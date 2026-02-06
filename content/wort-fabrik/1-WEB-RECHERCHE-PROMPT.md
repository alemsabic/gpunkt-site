# WEB-RECHERCHE-PROMPT: Zitate aus Pressemitteilungen, Interviews, Talkshows

**An:** Gemini (oder andere Research-AI)
**Projekt:** gpunkt.org - Dokumentation politischer Reizwörter
**Ziel:** 3-5 starke Zitate aus Web-Quellen finden (KEINE Mechanismus-Analyse!)

---

## ⚠️ WICHTIG: NUR RECHERCHE, KEINE ANALYSE!

Dieser Prompt ist **Teil 1 eines 4-Schritt-Workflows:**

1. **Bundestag-Recherche** (DIP-API) → Plenarprotokolle
2. **Web-Recherche** (dieser Prompt) → Pressemitteilungen, Interviews, Talkshows
3. **Mechanismus-Analyse** (separater Prompt) → Analysiert ALLE Zitate
4. **Draft schreiben** (separater Prompt) → Finaler Text

**Deine Aufgabe:** NUR Schritt 2 (Web-Recherche). Finde Zitate, aber analysiere sie NICHT!

---

## KONTEXT

Ich recherchiere für ein dokumentarisches Wörterbuch über politische Reizwörter (Kampfbegriffe und diskriminierende Vulgärsprache).

**Begriff:** "[BEGRIFF HIER EINSETZEN]"

**Deine Rolle:**
Du bist ein akribischer Rechercheur. Du arbeitest in **zwei Phasen**:
1. **Phase 1:** ALLE Zitate sammeln (breit, ohne Filter)
2. **Phase 2:** Die BESTEN auswählen (3-5 Zitate, Qualität > Quantität)

**Du machst KEINE Mechanismus-Analyse!** Das kommt später in Schritt 3.

---

## TEIL 0: ZWEI-PHASEN-PROZESS

### Phase 1: SAMMLE ALLE (Maximaler Recall)

**Ziel:** Vollständigkeit. Finde ALLE Spuren des Begriffs.

**Such-Strategie:**
1. **Alle Schreibweisen:**
   - Grundform: `[Begriff]`
   - Mit Bindestrich: `[Be-griff]`
   - Getrenntschreibung: `[Be griff]`
   - Flexionen: `[Begriffs]`, `[Begriffes]`, `[Begriffen]`

2. **Alle Kontexte:**
   - ✅ Angriff: "X ist ein [Begriff]"
   - ✅ Verteidigung: "Ich bin kein [Begriff]"
   - ✅ Selbstkritik: "Warum wir [Begriff] sagten"
   - ✅ Meta-Diskurs: "Der Begriff [Begriff] ist problematisch"

3. **Alle Quellen:**
   - Pressemitteilungen (offizielle Websites: CDU.de, SPD.de, etc.)
   - TV-Interviews (ARD, ZDF, BILD TV, Phoenix, etc.)
   - Talkshows (Anne Will, Hart aber fair, Maischberger, etc.)
   - Radio-Interviews (Deutschlandfunk, etc.)
   - Offizielle Statements (bundesregierung.de, Ministerien)

4. **Dokumentiere ALLES:**
   - Noch keine Selektion!
   - Auch wenn: Datum fehlt, Sprecher unklar, Kontext nicht eindeutig
   - Erst sammeln, dann sortieren

**Output Phase 1:** Vollständige Liste aller Fundstellen (kann 10-20 Zitate sein).

---

### Phase 2: WÄHLE DIE BESTEN (Maximale Präzision)

**Ziel:** Qualität. JETZT wählst du die **3-5 stärksten Zitate** aus Phase 1.

**Auswahlkriterien:**
- **Prominenz:** Minister > Hinterbänkler, Parteispitze > Lokalpolitik
- **Klarheit:** Eindeutige Verwendung (nicht vage, nicht mehrdeutig)
- **Verifizierbarkeit:** Primärquelle (Pressemitteilung, Original-Video) > Zeitungsbericht
- **Waffeneinsatz sichtbar:** Debatte beendet, Macht ausgeübt, Kritik delegitimiert

**Für die 3-5 Besten:**
- JETZT: Triple-Verification durchführen (siehe unten)
- JETZT: BibTeX-Einträge erstellen
- **NICHT:** Mechanismus-Analyse (kommt in Schritt 3!)

**Output Phase 2:** Die finalen 3-5 Zitate mit allen Metadaten (siehe unten).

---

## TEIL 1: QUELLEN-ANFORDERUNGEN

### ✅ ERLAUBT:

**Primärquellen (höchste Priorität):**
- **Pressemitteilungen** (offizielle Websites: CDU.de, SPD.de, bundesregierung.de)
- **Original-Videos** (ARD Mediathek, ZDF Mediathek, YouTube mit Zeitstempel)
- **Offizielle Statements** (Ministerien, Partei-Websites)
- **Radio-Interviews** (Deutschlandfunk, etc. mit Zeitstempel)

**Qualitätsmedien (mit Bedingungen):**
- FAZ, SZ, Spiegel, Zeit, ARD, ZDF, Deutschlandfunk, Tagesschau.de
- **BEDINGUNG:** Zitat MUSS in **»Anführungszeichen«** stehen (wörtliche Rede)
- **Bevorzugt:** Video/Audio mit Zeitstempel (verifizierbar)
- **Akzeptabel:** Schriftliches Interview mit direktem Zitat

---

### ❌ VERBOTEN:

- Sekundär-Sekundärquellen ("Zeitung A über Zeitung B")
- Kritiker-Zitate (wir suchen Täter, nicht Kritiker!)
- Indirekte Rede ("Er sagte, dass...")
- Blogs, Social Media ohne Original-Link
- Tagesschau-Bericht OHNE Link zum Original-Video

---

## TEIL 2: AUSWAHLKRITERIEN (die 3-5 stärksten)

✅ **Waffeneinsatz sichtbar:**
- Debatte wird beendet ("alternativlos")
- Macht wird ausgeübt (Kriminalisierung: "wer betrügt, der fliegt")
- Kritik wird delegitimiert (Inversion: "Meinungsdiktatur")
- Menschen werden entmenschlicht ("Flut", "Tourismus")

✅ **Historisch relevant:**
- Wendepunkt in der Debatte
- Skandal/öffentliche Empörung
- Unwort des Jahres

✅ **Prominent:**
- Minister/Parteispitzen > Hinterbänkler
- Öffentliche Bühne (TV-Interview, Pressemitteilung) > Twitter

✅ **Prägnant:**
- Kurz, eingängig, provokant
- Zeigt Waffeneinsatz klar (nicht vage)

---

❌ **Vermeide Füllmaterial:**
- Technische Verwendung ("Die Umgehungsstraße ist alternativlos")
- Banale Kontexte (Lokalpolitik ohne Relevanz)

**Behutsame Glättung erlaubt:**
- Füllwörter ("äh, also, ja") mit `[...]` streichen
- Kernaussage bleibt identisch

---

## TEIL 3: OUTPUT-FORMAT

### ⚠️ WICHTIG: Format muss kompatibel zu DIP-Output sein!

Liefere für jeden Treffer **exakt dieses Format:**

---

**Zitat [Nr]: [Name] ([Partei/Funktion], [Jahr])**

**Quelle:** [Name, Funktion, Medium/Kontext, Datum (TT.MM.JJJJ)]

**Link:** [Vollständige URL]

**Der subtextuelle Kontext:** [2-3 Sätze: Wie wurde der Begriff als Waffe eingesetzt? Debatte beendet? Macht ausgeübt? Kritik delegitimiert? Menschen entmenschlicht?]

**Zitat:** »[Vollständiger Satz - behutsam geglättet mit [...] wenn nötig]«

**Citekey:** `nachname_jahr`

**Verification-Status:** [Anführungszeichen vorhanden? / Video-Zeitstempel? / Primärquelle?]

---

[3-5 Zitate in diesem Format]

---

**Hinweis zur Verifizierbarkeit:**
[Falls Unsicherheiten bestehen, hier dokumentieren]

---

## TEIL 4: BIBTEX-EINTRÄGE (für bibliography.bib)

Liefere für JEDES Zitat einen passenden BibTeX-Eintrag:

---

### Pressemitteilung:
```bibtex
@misc{nachname_jahr,
  title = {Titel der Pressemitteilung},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  howpublished = {Pressemitteilung [Partei/Organisation]},
  url = {https://...},
  note = {Offizielle Website}
}
```

---

### TV-Interview (ARD/ZDF):
```bibtex
@misc{nachname_jahr,
  title = {Interview in [Sendung]},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  howpublished = {ARD/ZDF},
  url = {https://www.ardmediathek.de/...},
  note = {Zeitstempel: ab MM:SS}
}
```

---

### Zeitungsinterview:
```bibtex
@article{nachname_jahr,
  title = {Artikel-Titel},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  journal = {Frankfurter Allgemeine Zeitung},
  url = {https://www.faz.net/...},
  note = {Interview, wörtliche Rede}
}
```

---

**WICHTIG:**
- **Author = der Sprecher** (NICHT der Journalist!)
- **Citekeys:** `nachname_jahr` (lowercase, z.B. `merkel_2010`)
- Bei mehreren Zitaten pro Person/Jahr: `nachname_jahr_a`, `nachname_jahr_b`
- Citekeys in Zitaten MÜSSEN EXAKT mit BibTeX übereinstimmen

---

## TEIL 5: TRIPLE-VERIFICATION (KRITISCH!)

**PFLICHT bei Politiker-Zitaten:**

Für JEDES Zitat diese 3 Prüfungen durchführen:

### ✓ Prüfung 1: Original finden
- Link öffnen
- Zitat Wort-für-Wort im Original suchen
- **Wenn nicht gefunden:** Quelle NICHT verwenden!

### ✓ Prüfung 2: Kontext prüfen
- Ist das Zitat korrekt kontextualisiert?
- Wird es aus dem Zusammenhang gerissen?
- **Bei Unsicherheit:** Quelle NICHT verwenden!

### ✓ Prüfung 3: Metadaten prüfen
- Name korrekt? (Vorname, Nachname)
- Funktion korrekt? (Minister, Parteivorsitzender)
- Datum korrekt? (TT.MM.JJJJ)
- **Bei Abweichung:** Korrigieren oder Quelle NICHT verwenden!

**Bei JEGLICHEM Zweifel:** Quelle NICHT verwenden!

**Lieber 2 perfekte Zitate als 5 unsichere.**

---

## TEIL 6: CHEAT-SHEET

### ✅ PERFEKT (Goldstandard):

- **Pressemitteilung auf offizieller Website:**
  - `https://www.cdu.de/artikel/merz-statement-migration` (Beispiel)
  - Wortlaut garantiert, offiziell, dauerhaft verfügbar

- **ARD/ZDF-Video mit Zeitstempel:**
  - `https://www.ardmediathek.de/video/...` (ab 12:30)
  - Sicht- und hörbar, verifizierbar, öffentlich-rechtlich

- **FAZ-Interview mit »Zitat« in Anführungszeichen:**
  - Artikel zeigt wörtliche Rede in »Guillemets« oder "Anführungszeichen"
  - Journalist bürgt für Korrektheit

---

### ❌ VERBOTEN (niemals verwenden):

- "Correctiv berichtet, dass X sagte..."
  - Sekundär-Sekundärquelle (zwei Instanzen dazwischen)

- Tagesschau-Bericht OHNE Link zum Original-Video
  - Paraphrase, keine wörtliche Rede

- Social Media Screenshot ohne Verifikation
  - Kann gefälscht sein, kein Kontext

- Blog-Beitrag über Politiker-Aussage
  - Keine journalistische Verantwortung

---

## QUALITÄTSKRITERIEN

Dein Output muss erfüllen:

✅ **3-5 Zitate** (Qualität > Quantität)
✅ **Wörtliche Rede** (Anführungszeichen/Video/Primärquelle)
✅ **Subtextueller Kontext** (Waffeneinsatz dokumentiert)
✅ **KEINE Mechanismus-Analyse** (kommt in Schritt 3!)
✅ **Chronologisch sortiert** (früheste → neueste)
✅ **BibTeX vollständig** (author, year, url, note)
✅ **Citekeys konsistent** (nachname_jahr, lowercase)
✅ **Triple-verified** (3 Prüfungen bestanden)

---

## ⚠️ WARNUNGEN

### Warnung 1: AI-Halluzination
**Problem:** Sprachmodelle erfinden manchmal Zitate oder Quellen.

**Schutz:**
- IMMER Link angeben (zum Prüfen)
- IMMER Verification-Status dokumentieren
- Bei Unsicherheit: Quelle NICHT verwenden

---

### Warnung 2: Rufschädigung
**Problem:** Falsche Zuschreibung = rechtliche Konsequenzen + Glaubwürdigkeitsverlust

**Schutz:**
- Triple-Verification (3 Prüfungen)
- Nur Primärquellen oder verifizierte Qualitätsmedien
- Kontext korrekt wiedergeben

---

### Warnung 3: Sekundärquellen
**Problem:** "Correctiv schreibt, dass Sellner sagte..." = zu viele Instanzen

**Schutz:**
- Nur Original-Quellen (Politiker selbst)
- Keine Berichte über Berichte

---

**Bei JEGLICHEM Zweifel:** Quelle NICHT verwenden!

**Lieber 2 perfekte Zitate als 5 unsichere.**

---

## STARTBEFEHL

**Starte jetzt die Web-Recherche für "[BEGRIFF HIER EINSETZEN]".**

**WICHTIG: Arbeite in zwei Phasen:**

### Phase 1: SAMMLE ALLE
- Suche ALLE Schreibweisen (Bindestrich, Getrennt, Flexionen)
- Suche ALLE Kontexte (Angriff, Verteidigung, Selbstkritik, Meta-Diskurs)
- Suche ALLE Quellen (Pressemitteilungen, Interviews, Talkshows)
- Dokumentiere ALLES (noch keine Selektion!)
- Liefere: Vollständige Liste (kann 10-20 Zitate sein)

### Phase 2: WÄHLE DIE BESTEN
- Aus Phase 1: Wähle die **3-5 stärksten** Zitate
- JETZT: Subtextueller Kontext (Waffeneinsatz zeigen)
- JETZT: BibTeX-Einträge (author = Sprecher, nicht Journalist)
- JETZT: Triple-Verification (3 Prüfungen pro Zitat)
- **NICHT:** Mechanismus-Analyse (kommt in Schritt 3!)

**Bei Unsicherheit:** Lieber weniger Zitate (2-3), dafür perfekt.
