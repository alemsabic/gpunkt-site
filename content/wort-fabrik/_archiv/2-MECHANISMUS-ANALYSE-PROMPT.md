# MECHANISMUS-ANALYSE-PROMPT: Dekonstruktion sprachlicher Waffen

**An:** Gemini (oder andere Analyse-AI)
**Projekt:** gpunkt.org - Dokumentation politischer Reizwörter
**Ziel:** Mechanismus-Analyse (●◐) für recherchierte Zitate durchführen

---

## ⚠️ WICHTIG: NUR ANALYSE, KEINE RECHERCHE!

Dieser Prompt ist **Teil 3 eines 4-Schritt-Workflows:**

1. **Bundestag-Recherche** (DIP-API) → Plenarprotokolle
2. **Web-Recherche** (separater Prompt) → Pressemitteilungen, Interviews, Talkshows
3. **Mechanismus-Analyse** (dieser Prompt) → Analysiert ALLE Zitate
4. **Draft schreiben** (separater Prompt) → Finaler Text

**Deine Aufgabe:** NUR Schritt 3 (Mechanismus-Analyse). Du bekommst fertige Zitate, analysierst sie, findest aber KEINE neuen Zitate!

---

## KONTEXT

Ich habe bereits **3-5 Zitate** recherchiert (aus Bundestag und Web-Quellen). Diese Zitate sind verifiziert, haben Metadaten (Quelle, Link, Citekey, BibTeX) und zeigen, wie der Begriff als **sprachliche Waffe** eingesetzt wurde.

**Begriff:** "[BEGRIFF HIER EINSETZEN]"

**Deine Rolle:**
Du bist ein präziser Analytiker. Du dekonstruierst, **welche manipulativen Mechanismen** in jedem Zitat am Werk sind. Du nutzt dafür den **Werkzeugkasten** (14 Mechanismen) und arbeitest mit **Cluster-Logik** und **gradueller Gewichtung** (●◐).

**Du machst KEINE Recherche!** Du analysierst nur die Zitate, die ich dir gebe.

---

## INPUT-FORMAT

Du bekommst Zitate aus **zwei verschiedenen Recherche-Quellen**. Beide Formate sind gültig:

---

### Format A: Web-Recherche (WEB-Begriff.md)

**Zitat 1: [Name] ([Partei/Funktion], [Jahr])**

**Quelle:** [Name, Funktion, Medium/Kontext, Datum (TT.MM.JJJJ)]

**Link:** [Vollständige URL]

**Der subtextuelle Kontext:** [2-3 Sätze: Wie wurde der Begriff als Waffe eingesetzt?]

**Zitat:** »[Vollständiger Satz]«

**Citekey:** `nachname_jahr`

**Verification-Status:** [Primärquelle / Anführungszeichen / Video-Zeitstempel]

---

### Format B: Bundestag-Recherche (DIP-Begriff-DATUM.md)

**## Treffer 1: [JJJJ-MM-TT]**

**Sprecher:** [Name] ([Rolle/Fraktion])

**Wahlperiode:** [WP]/[Dok-Nr]

**Seite:** [Seitenzahl + Bereich]

**PDF:** [Vollständige URL]

**Zitat (Kontext):**
»[Vollständiger Satz]«

**Citekey:** `nachname_jahr`

**BibTeX:**
```bibtex
[BibTeX-Eintrag]
```

---

**Beide Formate enthalten:**
- ✅ Sprecher (Name + Rolle/Funktion)
- ✅ Datum/Jahr
- ✅ Zitat (in »Guillemets«)
- ✅ Citekey (nachname_jahr)
- ✅ Quelle (Link/PDF)

**Deine Aufgabe:** Für JEDES Zitat (egal welches Format) die Mechanismus-Analyse durchführen.

---

## TEIL 1: WERKZEUGKASTEN (14 Mechanismen)

Analysiere für jedes Zitat, **welche manipulativen Mechanismen** am Werk sind.

**Die 14 Mechanismen (organisiert in 3 Clustern):**

Diese Cluster bilden eine **Eskalationsleiter** (A→B→C): Wer markiert ist (A), dessen Realität wird vernebelt (B), bis Gewalt logisch erscheint (C).

### Cluster A: Identitäts-Konstruktion (Wer ist der Feind?)
**Funktion:** Markierung und Ausgrenzung der "Out-Group"

1. **Ethnisierung** - Problem → ethnische/kulturelle Zugehörigkeit
2. **Kriminalisierung** - Legal → Verbrechen
3. **Sexualisierung** - Person → Sexualakt (Degradierung)
4. **Infantilisierung** - Erwachsen → Kind (unreif)
5. **Pathologisierung** - Meinung/Identität → Krankheit ("Wahn")

**Cluster-Logik:** Wenn du einen Mechanismus findest, prüfe die anderen im selben Cluster! Beispiel: "Ethnisierung" gefunden? → prüfe auch "Kriminalisierung".

---

### Cluster B: Realitäts-Verzerrung (Wie wird Wahrheit manipuliert?)
**Funktion:** Verschiebung der Wahrnehmung von Fakten

6. **Euphemismus** - Schlimmes klingt harmlos
7. **Inversion** - Täter ↔ Opfer
8. **Naturalisierung** - Politik → Naturgesetz ("alternativlos")
9. **Entpolitisierung** - Konflikt → Sachzwang
10. **Ontologisierung** - Handlung/Zustand → unveränderliches Wesen ("ein Illegaler")

**Cluster-Logik:** Wenn "Euphemismus" gefunden, prüfe auch "Entpolitisierung".

---

### Cluster C: Eskalation & Dehumanisierung (Wie wird Gewalt vorbereitet?)
**Funktion:** Senkung der Hemmschwelle zur Gewalt

11. **Quantifizierung** - Menschen → Masse/Zahlen ("Flut")
12. **Militarisierung** - Zivil → Krieg ("Terroristen")
13. **Temporalisierung** - Gegenwart → Apokalypse ("Volkstod")
14. **Entmenschlichung** - Mensch → Objekt/Tier/Fehler

**Cluster-Logik:** Wenn "Quantifizierung" gefunden, prüfe auch "Entmenschlichung".

---

**Vollständige Beschreibungen:** Siehe [WERKZEUGKASTEN.md](WERKZEUGKASTEN.md) (v4.1)

---

## TEIL 2: GEWICHTUNGS-LOGIK (● vs. ◐)

Nicht alle Mechanismen wirken gleich stark. Unterscheide zwischen **dominant (●)** und **teilweise vorhanden (◐)**.

### Wann ist ein Mechanismus dominant (●)?

**Kriterien:**
1. **Funktional unerlässlich:** Ohne diesen Mechanismus würde der Begriff nicht funktionieren
2. **Zentral in der Wortbildung:** Der Mechanismus steckt im Wort selbst (z.B. "Tourismus" in "Sozialtourismus" = Euphemismus)
3. **Primäre emotionale Reaktion:** Dieser Mechanismus löst die stärkste Wirkung aus

**Beispiel:** "Sozialtourismus"
- **● Inversion** - OHNE die Umkehrung (Not → Luxus) würde der Begriff nicht funktionieren
- **● Euphemismus** - "Tourismus" IST die verschleiernde Komponente

---

### Wann ist ein Mechanismus teilweise vorhanden (◐)?

**Kriterien:**
1. **Mitschwingt, bildet nicht den Kern:** Der Mechanismus ist erkennbar, aber nicht zentral
2. **Kontext-abhängig:** Ergibt sich aus dem Diskurs-Kontext, nicht aus dem Wort selbst
3. **Sekundäre Wirkung:** Unterstützt die Hauptmechanismen, wirkt aber nicht allein

**Beispiel:** "Sozialtourismus"
- **◐ Ethnisierung** - Das Wort selbst nennt keine Ethnie, aber diskursiv richtet es sich fast ausschließlich gegen Osteuropäer/Roma. Der Mechanismus ist vorhanden, aber nicht im Wort codiert.

---

### Faustregel

**Frage dich:**
- "Wenn ich diesen Mechanismus wegnehme, funktioniert der Begriff noch?"
  - Nein → **●** (dominant)
  - Ja, aber geschwächt → **◐** (teilweise)

**Beispiel:** "Sozialtourismus" ohne Inversion (ohne die Umkehrung Not→Luxus) = der Begriff kollabiert. Also: **● Inversion**.

---

## TEIL 3: ANALYSE-PROZESS (Schritt für Schritt)

Für JEDES Zitat durchläufst du diese Schritte:

### Schritt 1: Welches Cluster passt?

**Frage dich:**
- **Cluster A (Identitäts-Konstruktion):** Wer sind "Wir", wer sind "Die"? Wird eine Gruppe ausgegrenzt, kriminalisiert, sexualisiert, infantilisiert?
- **Cluster B (Realitäts-Verzerrung):** Klingt das Wort harmloser als die Realität? Werden Machtverhältnisse umgekehrt? Wird Politik als Naturgesetz dargestellt?
- **Cluster C (Eskalation & Dehumanisierung):** Werden Menschen zur Masse/Flut? Wird Kriegsvokabular benutzt? Wird mit Apokalypse gedroht?

**→ Prüfe ALLE Mechanismen im passenden Cluster!**

---

### Schritt 2: Gewichte jeden gefundenen Mechanismus

Für jeden gefundenen Mechanismus:
- **Dominant (●):** Ohne diesen Mechanismus funktioniert der Begriff nicht
- **Teilweise (◐):** Schwingt mit, ist kontext-abhängig, nicht zentral

**WICHTIG:** Nutze die **Gegenprobe** aus WERKZEUGKASTEN.md ("Kein Treffer, wenn..."), um False Positives zu vermeiden!

---

### Schritt 3: Begründung schreiben

Für jeden Mechanismus schreibst du eine **präzise Begründung**, die zeigt:
- **WIE** der Mechanismus wirkt (nicht nur "ist vorhanden")
- **WARUM** er als Waffe funktioniert (Wirkung auf das Publikum)
- **WELCHE** Realität verschleiert/umgekehrt/verzerrt wird

**Beispiel (gut):**
- **● Inversion** - Kehrt die Realität um. Migranten, die aus Not (Armut, Arbeitslosigkeit) kommen, werden als "Touristen" dargestellt – als würden sie zum Vergnügen reisen. Arbeitsmigration ist das Gegenteil von Erholungsurlaub. Die Umkehrung delegitimiert den Anspruch auf Solidarität.

**Beispiel (schlecht):**
- **● Inversion** - Ist vorhanden. (← Keine Begründung, zeigt nicht WIE!)

---

## TEIL 4: OUTPUT-FORMAT

**Output-Datei:** `Recherche/MECHANISMUS-[Begriff].md` (z.B. `Recherche/MECHANISMUS-Sozialtourismus.md`)

Liefere für **JEDES Zitat** diese Mechanismus-Analyse:

---

**Zitat 1: [Name] ([Partei/Funktion], [Jahr])**

**Mechanismus-Analyse:**
- **● [Mechanismus 1] (dominant)** - [Präzise Begründung: WIE wirkt der Mechanismus? WARUM funktioniert er als Waffe? WELCHE Realität wird verzerrt?]
- **● [Mechanismus 2]** - [Begründung]
- **◐ [Mechanismus 3] (teilweise)** - [Begründung: WARUM nur teilweise? Kontext-abhängig? Schwingt mit, bildet nicht den Kern?]

---

[2-4 weitere Zitate mit Mechanismus-Analyse]

---

**WICHTIG:** Am Ende lieferst du auch eine **Gesamtanalyse** der dominanten Mechanismen für den Begriff (für die `## Analyse` Sektion im finalen Eintrag):

---

## GESAMTANALYSE (für Draft)

**Dominante Mechanismen des Begriffs "[Begriff]":**

- **● [Mechanismus 1] (dominant)** - [Präzise Begründung, die zeigt WIE der Mechanismus ÜBER ALLE ZITATE HINWEG wirkt. Welches Muster ist erkennbar? Welche Wirkung entfaltet sich?]
- **● [Mechanismus 2]** - [Begründung]
- **◐ [Mechanismus 3] (teilweise)** - [Begründung]

**Fazit (1-2 Sätze):**
[Zusammenfassung: Was macht diesen Begriff zur Waffe? Welche Funktion erfüllt er im Diskurs?]

---

**Hinweis:** Diese Gesamtanalyse wird später in die `## Analyse` Sektion des finalen Eintrags übernommen.

---

## TEIL 5: QUALITÄTSKRITERIEN

Dein Output muss erfüllen:

✅ **Mechanismus-Analyse für JEDES Zitat** (nicht nur für den Begriff allgemein)
✅ **Cluster-Logik genutzt** (wenn ein Mechanismus gefunden, andere im Cluster geprüft)
✅ **Graduierung korrekt** (●◐ entsprechend der Kriterien)
✅ **Begründungen präzise** (zeigen WIE es wirkt, nicht nur DASS es wirkt)
✅ **Gegenprobe durchgeführt** (siehe WERKZEUGKASTEN.md)
✅ **Gesamtanalyse vorhanden** (für alle Zitate zusammen)
✅ **Fazit formuliert** (1-2 Sätze: Was macht diesen Begriff zur Waffe?)

---

## ⚠️ WARNUNGEN

### Warnung 1: Falsche Positive vermeiden

**Problem:** Manchmal scheint ein Mechanismus vorhanden zu sein, ist aber nicht einschlägig.

**Schutz:**
- IMMER die **Gegenprobe** aus WERKZEUGKASTEN.md nutzen ("Kein Treffer, wenn...")
- Beispiel: "Sozialtourismus" hat KEINE Temporalisierung (kein Apokalypse-Framing)
- Lieber 3 korrekte Mechanismen als 6 falsche!

---

### Warnung 2: Fehlende Gewichtung

**Problem:** Alle Mechanismen werden als gleich wichtig dargestellt (alle ●).

**Schutz:**
- **Frage dich:** "Wenn ich diesen Mechanismus wegnehme, funktioniert der Begriff noch?"
- Nur 2-3 Mechanismen sollten **●** sein
- Die anderen sind **◐** (teilweise)

---

### Warnung 3: Zu vage Begründungen

**Problem:** Begründungen sind zu allgemein ("ist vorhanden", "wirkt stark").

**Schutz:**
- **Zeige WIE:** Welche Umkehrung? Welche Verschleierung? Welche Masse?
- **Zeige WARUM:** Welche Wirkung auf das Publikum? Welche Debatte wird beendet?
- **Zeige WELCHE:** Welche Realität wird verzerrt?

---

## TEIL 6: BEISPIEL-ANALYSE

### Input (Zitat):

**Zitat 1: Friedrich Merz (CDU, 2022)**

**Quelle:** Friedrich Merz, Bundesvorsitzender der CDU, Interview in der Sendung "Die richtigen Fragen", Bild TV, 26.09.2022.

**Link:** https://www.bild.de/politik/inland/politik-inland/friedrich-merz-cdu-chef-entschuldigt-sich-fuer-sozialtourismus-aussage-81446754.bild.html

**Der subtextuelle Kontext:** Merz nutzt den Begriff, um ukrainische Kriegsgeflüchtete als opportunistische Nutznießer des deutschen Sozialsystems (Grundsicherung) zu rahmen. Durch die Metapher des "Tourismus" wird die existenzielle Notlage der Flucht in eine freiwillige, berechnende Reisebewegung umgedeutet, um Ressentiments in der Aufnahmegesellschaft zu mobilisieren.

**Zitat:** »Wir erleben mittlerweile einen Sozialtourismus dieser Flüchtlinge: nach Deutschland, zurück in die Ukraine, nach Deutschland, zurück in die Ukraine.«

**Citekey:** `merz_2022`

---

### Output (Mechanismus-Analyse):

**Zitat 1: Friedrich Merz (CDU, 2022)**

**Mechanismus-Analyse:**
- **● Inversion (dominant)** - Kehrt die Realität um. Menschen, die vor Krieg fliehen und temporär in Sicherheit sind, werden als "Touristen" dargestellt – als würden sie zum Vergnügen reisen. Flucht ist das Gegenteil von Erholungsurlaub. Die Umkehrung macht aus einer Notlage (Krieg) eine freiwillige, berechnende Reisebewegung. Dadurch wird der Anspruch auf Schutz und Solidarität delegitimiert.
- **● Euphemismus** - "Tourismus" verschleiert die existenzielle Notlage. Das Wort klingt positiv und leicht (Urlaub, Erholung, Freizeit), verdeckt aber die harte Realität von Krieg, Flucht und Unsicherheit. Die Verharmlosung rechtfertigt harte Abwehrmaßnahmen ("wer touristisch reist, braucht keine Hilfe").
- **● Kriminalisierung** - Stellt legales Verhalten (Pendeln zwischen Heimat und Zuflucht) als Missbrauch dar. Das Wort "Tourismus" impliziert Betrug: "Sie nutzen uns aus, obwohl sie gar nicht müssten." Rechtmäßiges Verhalten wird als moralische Verfehlung geframt, um Kürzungen zu legitimieren.
- **◐ Ethnisierung (teilweise)** - Das Wort selbst nennt keine Ethnie, aber der Kontext (ukrainische Geflüchtete) zeigt: Es richtet sich gegen eine spezifische Gruppe. Der Mechanismus schwingt mit, ist aber nicht im Begriff selbst codiert.

---

## GESAMTANALYSE (für Draft)

**Dominante Mechanismen des Begriffs "Sozialtourismus":**

- **● Inversion (dominant)** - Kernmechanismus über alle Zitate hinweg. Der Begriff kehrt systematisch die Realität um: Migration aus Not (Armut, Krieg, Arbeitslosigkeit) wird als Luxusreise ("Tourismus") dargestellt. Wer aus existenzieller Notwendigkeit kommt, wird als jemand geframt, der zum Vergnügen reist. Diese Umkehrung delegitimiert den Anspruch auf Solidarität und Schutz.

- **● Euphemismus** - "Tourismus" klingt positiv und leicht, verschleiert aber die harte Realität von Flucht, Armut und Diskriminierung. Die Verharmlosung rechtfertigt harte Abwehrmaßnahmen ("wer touristisch reist, braucht keine Hilfe"). Der Begriff macht aus Überlebenskampf eine Freizeitbeschäftigung.

- **● Kriminalisierung** - Delegitimiert geltendes Recht (EU-Freizügigkeit, Asylrecht). Rechtmäßige Migration wird als "Missbrauch" oder "Betrug" geframt. Der Begriff dient dazu, legale Ansprüche als moralische Verfehlung darzustellen und Kürzungen/Ausgrenzung zu rationalisieren.

- **◐ Ethnisierung (teilweise)** - Der Begriff selbst nennt keine Ethnie, zielt aber diskursiv fast ausschließlich auf spezifische Gruppen (Roma, Osteuropäer, ukrainische Geflüchtete). Pauschal wird Betrugsabsicht unterstellt. Der Mechanismus ist kontext-abhängig, aber nicht im Wort selbst codiert.

**Fazit:**
Der Begriff "Sozialtourismus" ist ein **Inversions-Euphemismus mit Kriminalisierung**. Er tarnt Überlebenskampf als Urlaubsreise und delegitimiert so den Anspruch auf Solidarität. Er dient dazu, Hilfsbereitschaft als "Naivität" darzustellen und Ausgrenzung zu rationalisieren.

---

## STARTBEFEHL

**Starte jetzt die Mechanismus-Analyse für "[BEGRIFF HIER EINSETZEN]".**

**WICHTIG:**
- Du bekommst die Zitate von mir (bereits recherchiert und verifiziert)
- Du machst KEINE Recherche, du analysierst NUR
- Du nutzt die **Eskalationsleiter** (A→B→C) und Cluster-Logik
- Du gewichtest graduell (●◐ - dominant vs. teilweise)
- Du begründest präzise (WIE wirkt es? WARUM funktioniert es?)
- Du lieferst am Ende eine Gesamtanalyse (für alle Zitate zusammen)

**Bei Unsicherheit:** Lieber weniger Mechanismen (2-3 dominante), dafür präzise begründet.
