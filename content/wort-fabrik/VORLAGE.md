# VORLAGE: Wörterbuch-Einträge

**Projekt:** gpunkt.org (Reizwörterbuch)
**Version:** 5.0 (06.02.2026)
**Umfang:** Politische Reizwörter + Diskriminierende Vulgärsprache

---

## PHILOSOPHIE: Die Pflicht des Lexikographen

Ein Wörterbuch ist niemals neutral. Jede Definition ist ein politischer Akt. Jede Etymologie eine Entlarvung oder Rechtfertigung. Wenn wir "Remigration" definieren, kontrollieren wir, wie es verstanden wird. Wenn wir "Sozialtourismus" zu seinen Urhebern zurückverfolgen, entlarven wir seine Absicht.

**Unser Standard ist nicht Kürze. Unser Standard ist Präzision, die dem Verstehen dient.**

### Die vier Tests

Jeder Eintrag muss diese Tests bestehen:

1. **Clarity Test:** Kann jemand ohne Vorwissen den Begriff nach einmaligem Lesen vollständig verstehen?
2. **Architecture Test:** Hat jede Sektion eine innere Logik?
3. **Read-Aloud Test:** Fließt der Text beim Vorlesen?
4. **Johnson Test:** Ist dies so klar und vollständig wie möglich, mit keinem Wort mehr als nötig?

Wenn ein Test fehlschlägt → iterieren.

---

## 1. TEMPLATE v5.0

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

Politisches Reizwort zur Diffamierung von Migration als Sozialbetrug. Suggeriert, Menschen fliehen zum Vergnügen und besuchen Sozialsysteme wie Urlaubsziele. Verschleiert Fluchtgründe (Armut, Krieg, Diskriminierung) und stellt sie als freiwillige Konsumentscheidung dar. Kriminalisiert rechtmäßige EU-Freizügigkeit als systematischen Missbrauch.

## Geschichte

Geprägt **2013** von **CSU/CDU-Politikern** (Hans-Peter Friedrich, Horst Seehofer, Alexander Dobrindt) im Kontext der **EU-Osterweiterung** und verstärkter Migration aus Osteuropa, insbesondere Roma-Gemeinden. Der Begriff zielte darauf, Freizügigkeitsrechte als "Missbrauch" zu delegitimieren. Erneut aufgegriffen **2022** von **Friedrich Merz** im Kontext ukrainischer Geflüchteter. Zum **"Unwort des Jahres 2013"** gewählt.

## Konstruktion

"Sozial-" (Sozialsystem als Ziel) + "Tourismus" (Vergnügungsreise) = existenzielle Not wird zu freiwilligem Konsum, Flucht zu Freizeitvergnügen.

## Analyse

*   ● **Inversion (dominant):** Kehrt die Realität um. Migranten, die aus Not kommen, werden als "Touristen" dargestellt – als würden sie zum Vergnügen reisen.
*   ● **Euphemismus:** Verschleierung durch Verharmlosung. Das Wort "Tourismus" klingt positiv und leicht, verdeckt aber die harte Realität von Armutsmigration und lässt harte Abwehrmaßnahmen als "Ordnungspolitik" erscheinen.
*   ● **Kriminalisierung:** Macht aus Rechtsausübung (EU-Freizügigkeit) einen Betrug. Legale Migration wird als "Missbrauch" geframed.
*   ◐ **Ethnisierung:** Richtet sich primär gegen Osteuropäer und Roma, nicht gegen "westliche" EU-Bürger.
*   ◐ **Quantifizierung:** Oft im Kontext von "Massenmigration" genutzt. Suggeriert eine Flut, die das System "überlastet".

## Anwendung

Aus Sicht des Sprechers bietet der Begriff eine rationale Erklärung für wahrgenommene Ungerechtigkeit: Warum sollten "die" bekommen, wofür "wir" arbeiten? Er ermöglicht es, Hilfsbereitschaft als "Naivität" darzustellen und Ausgrenzung als Verteidigung des Eigenen zu rationalisieren.

## Belege

● **Hans-Peter Friedrich** (CSU, Bundesinnenminister) im Spiegel-Interview März 2013 [@friedrich_2013]: »Wer aber nur kommt, um Sozialleistungen zu kassieren, der missbraucht das Freizügigkeitsrecht. Diesen ==Sozialtourismus== müssen wir unterbinden.«

● **Horst Seehofer** (CSU, Parteivorsitzender) bei der Kreuth-Klausur Januar 2013 [@seehofer_2013]: »Wir werden uns gegen Zuwanderung in die deutschen Sozialsysteme wehren – bis zur letzten Patrone.«

## Abgrenzung

Nicht gemeint, wenn ==Sozialtourismus== in der Tourismuswissenschaft genutzt wird, um Reisen mit sozialen Zielen zu beschreiben (z.B. Bildungsreisen, Austauschprogramme). Die Analyse bezieht sich auf die politische Verwendung im Migrations-Diskurs.
```

---

## 2. KOMPONENTEN IM DETAIL

### 2.1 Frontmatter

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
- **"Reizwort"** — Oberbegriff (PFLICHT bei allen Einträgen)
- **Oder spezifischer:** "Rechtsextremer Kampfbegriff", "Diskriminierendes Reizwort", "Politisches Reizwort"
- **Dominante Mechanismen** — 1-3 Mechanismen aus [Werkzeugkasten](WERKZEUGKASTEN.md)
- **Zusätzlich (optional)** — "Vulgärsprache", "Jugendsprache", "Unwort"

---

### 2.2 Headword mit Trennstrichen

```markdown
# So|zial|tou|ris|mus
```

**Format:** H1 mit Trennstrichen `|` zwischen Silben

**Funktion:**
- **Visuelles "Stolpern"** — verlangsamt das Lesen
- **Sichtbarmachung der Konstruktion** — zeigt, wie das Wort gebaut ist

**Regeln:**
- Trennstriche nach **Silben**, nicht nach Morphemen
  - Falsch: `Sozial|tourismus` (Morpheme)
  - Richtig: `So|zial|tou|ris|mus` (Silben)

---

### 2.3 Definition

Eine Definition muss fünf Fragen beantworten (typisch 3-5 Sätze):

1. **Was ist es?** (Klassifizierung)
   - "Rechtsextremer Kampfbegriff für X" / "Politisches Reizwort für Y" / "Diskriminierendes Reizwort für Z"
   - Sei präzise: "Rechtsextremer Kampfbegriff" > "Kampfbegriff"

2. **Wie funktioniert es?** (Mechanismus kurz)
   - Die semantische Operation in einem Satz
   - "Suggeriert, Menschen fliehen zum Vergnügen..."

3. **Was bewirkt es?** (Wirkung)
   - Konkret: "suggeriert X", "verschleiert Y", "kriminalisiert Z"
   - "Verschleiert Fluchtgründe... Kriminalisiert rechtmäßige EU-Freizügigkeit..."

4. **Warum wird es benutzt?** (Funktion)
   - Der politische oder soziale Zweck
   - "...als systematischen Missbrauch"

5. **Wo steht es im Diskurs?** (Kontext — optional)
   - Nur wenn für Verständnis essentiell

#### Stil: Was wirkt

**Do:**
- **Verben der Manipulation:** "tarnt", "verschleiert", "suggeriert", "kriminalisiert", "entmenschlicht"
- **Konkrete Sprache:** "Massendeportationen" statt "problematische Maßnahmen"
- **Hauptsätze als Grundgerüst:** klare Aussagen
- **Subordination wo sie Klarheit schafft:** Ein gut platzierter Relativsatz ist besser als zwei holprige Hauptsätze

**Don't:**
- **Moral-Vokabular:** "zynisch", "perfide" → zeigen, nicht bewerten
- **Superlative:** "extrem", "massiv" → schwächen die Aussage
- **Vage Formulierungen:** "problematisch" → nichts sagend
- **Akademisches Geschwurbel:** "diskursive Strategie der hegemonialen Bedeutungsproduktion" → Deutsch sprechen!

#### Länge

**3-5 Sätze** — so viele wie nötig, um die fünf Fragen zu beantworten.

---

### 2.4 Geschichte (bei politischen Begriffen)

**[Optional bei Vulgärsprache]**

Die Geschichte erzählt die **Biographie des Begriffs** — wie wurde aus einem neutralen Begriff (oder aus dem Nichts) ein Reizwort/Kampfbegriff?

#### Die fünf Akte:

1. **Ursprung (falls relevant)**
   - Hatte der Begriff eine neutrale/akademische Herkunft?
   - "Ursprünglich ein soziologischer Fachbegriff für..."
   - Nur wenn die Umdeutung Teil der Manipulation ist

2. **Erste politische Prägung/Instrumentalisierung**
   - Wer hat den Begriff geprägt oder politisch instrumentalisiert?
   - Name (Institution/Partei) + Jahr
   - "Geprägt 2013 von CSU/CDU-Politikern..."

3. **Kontext: Warum entstand er?**
   - In welchem politischen/sozialen Zusammenhang?
   - "...im Kontext der EU-Osterweiterung"

4. **Verbreitung: Wie wurde er Mainstream?**
   - Wer hat ihn popularisiert? Wer hat ihn übernommen?
   - "Popularisiert durch X beim Treffen Y"

5. **Gegenwart: Wo steht er heute?**
   - "Zum 'Unwort des Jahres 2023' gewählt"

#### Scanbarkeit: Fettdruck für Anker-Daten

**Fett markieren:**
- **Jahre** (2013, 2022)
- **Namen** (CSU-Politikern, Friedrich Merz)
- **Parteien/Institutionen** (AfD, Front National)
- **Schlüssel-Kontexte** (EU-Osterweiterung)
- **Status** (Unwort des Jahres)

#### Länge

**3-5 Sätze** — so viele wie die Geschichte braucht.

---

### 2.5 Konstruktion

**[Nur bei zusammengesetzten Begriffen - bei einfachen Wörtern weglassen]**

Die semantische Formel — wie erzeugen die Wortbestandteile eine manipulative Bedeutung?

**Format:**
```markdown
"Bestandteil 1" (Bedeutung) + "Bestandteil 2" (Bedeutung) = Wirkung
```

**Beispiele:**

> "Sozial-" (Sozialsystem als Ziel) + "Tourismus" (Vergnügungsreise) = existenzielle Not wird zu freiwilligem Konsum.

> "Re-" (zurück) + "Migration" (Wanderung) = suggeriert freiwillige Rückkehr, verschleiert Zwang und Selektion.

#### Länge

**1-2 Sätze** — dies ist die einzige Sektion, wo **Kürze Prinzip** ist.

---

### 2.6 Analyse (PFLICHT)

Die 14 Mechanismen sind in drei Clustern organisiert, die eine **Eskalationsleiter** bilden (A→B→C):

**A: Identitäts-Konstruktion** (Wer ist der Feind?)
Ethnisierung, Kriminalisierung, Sexualisierung, Infantilisierung, Pathologisierung

**B: Realitäts-Verzerrung** (Wie wird Wahrheit manipuliert?)
Euphemismus, Inversion, Naturalisierung, Entpolitisierung, Ontologisierung

**C: Eskalation & Dehumanisierung** (Wie wird Gewalt vorbereitet?)
Quantifizierung, Militarisierung, Temporalisierung, Entmenschlichung

#### Graduierung

- **●** = dominant (ohne diesen Mechanismus funktioniert der Begriff nicht)
- **◐** = teilweise (schwingt mit, ist kontext-abhängig, nicht zentral)

#### Format

```markdown
*   ● **Mechanismus (dominant):** Begründung, die das WIE erklärt, nicht nur das DASS.
*   ● **Mechanismus 2:** Begründung.
*   ◐ **Mechanismus 3:** Begründung.
```

#### Begründung: Präzise, nicht knapp

Die Begründung muss **zeigen, WIE der Mechanismus wirkt**.

**Typisch:** 1-2 Sätze pro Mechanismus.

**Beispiel:**
```markdown
*   ● **Inversion (dominant):** Kehrt die Realität um. Migranten, die aus Not kommen,
    werden als "Touristen" dargestellt – als würden sie zum Vergnügen reisen.
*   ● **Kriminalisierung:** Delegitimiert geltendes Recht. Legale EU-Freizügigkeit
    wird als "Missbrauch" geframed.
```

#### Anzahl der Mechanismen

**3-5 Mechanismen** aus dem [Werkzeugkasten](WERKZEUGKASTEN.md).

- Von stark (●) zu teilweise (◐) geordnet
- Die ersten 2-3 sollten die dominanten sein

---

### 2.7 Anwendung

**[Optional - vor allem bei politisch eingesetzten Begriffen]**

Warum ist der Begriff so attraktiv für den Sprecher? Zeigt die **Perspektive des Anwenders** - die subjektive Berechtigung und Verführungskraft des Begriffs.

**Format:** 2-3 Sätze, Advocatus Diaboli

**Beispiel:**

> Aus Sicht des Sprechers bietet der Begriff eine rationale Erklärung für wahrgenommene Ungerechtigkeit: Warum sollten "die" bekommen, wofür "wir" arbeiten? Er ermöglicht es, Hilfsbereitschaft als "Naivität" darzustellen und Ausgrenzung als Verteidigung zu rationalisieren.

---

### 2.8 Belege

#### Bei politischen Begriffen: Originalzitate mit Quellennachweis

**Format:**
```markdown
● **Name** (Partei, Funktion) bei Anlass Datum [@citekey]: »Zitat mit ==Begriff==.«
```

**Regeln:**

1. **NUR Primärquellen** - Original-Zitate von Personen, die den Begriff verwenden
2. **Vollständige Sätze** - Nicht kürzen mit [...], es sei denn unumgänglich
3. **Chronologisch** - Früheste Verwendung zuerst
4. **Anzahl** - Mind. 2 Zitate, typisch 3-4
5. **Begriff highlighten** - `==Begriff==` im Zitat
6. **Kontext VOR Zitat** - Name, Funktion, Anlass, Datum, dann Zitat

**Beispiel:**
```markdown
● **Björn Höcke** (AfD Thüringen, Vorsitzender) in seinem Buch "Nie zweimal in
denselben Fluss" 2018 [@höcke_2018]: »Neben dem Schutz unserer nationalen und
europäischen Außengrenzen wird ein großangelegtes ==Remigrationsprojekt==
notwendig sein.«
```

#### Bei Vulgärsprache: Authentische Verwendungsbeispiele

**Format:**
```markdown
● »Beispielsatz mit ==Begriff==.«
```

**Regeln:**

1. **Authentische Verwendung** - Zeige, wie der Begriff wirklich benutzt wird
2. **Keine Quellennachweise nötig** - Bei Vulgärsprache ist Authentizität wichtiger
3. **Zeige Wirkung** - Der Kontext sollte klar machen, WARUM der Begriff verletzend ist
4. **Anzahl** - Mind. 2 Beispiele

---

### 2.9 Abgrenzung

**[Optional - empfohlen bei Begriffen mit legitimen Verwendungen]**

Wann trifft unsere Analyse NICHT zu? Zeigt, dass der **Kontext entscheidet**, nicht das Wort allein.

**Format:** "Nicht gemeint, wenn [Bedingung]. [Kurze Erklärung]."

**Beispiele:**

> Nicht gemeint, wenn ==Remigration== in der Migrationsforschung genutzt wird, um die statistische Rückwanderung von Rentnern zu beschreiben. Die Analyse bezieht sich auf die politische Verwendung im rechtsextremen Diskurs.

> Nicht gemeint, wenn der Begriff in satirischem oder parodistischem Kontext verwendet wird, um die Mechanismen sichtbar zu machen (nicht zu nutzen).

**Typische Kontexte für Abgrenzung:**
- Wissenschaftliche oder fachliche Verwendung
- Eindeutig erkennbare Satire oder Parodie
- Historische oder analytische Zitate

---

## 3. CHECKLISTE

**STRUKTUR ✓**
- [ ] Frontmatter (title, language, cssclasses, tags)
- [ ] Headword (H1) mit Trennstrichen `|`
- [ ] **Definition** (3-5 Sätze: Was? Wie? Wirkung? Funktion?)
- [ ] **Geschichte** (H2, bei politischen Begriffen - narrative Struktur!)
- [ ] **Konstruktion** (H2, bei zusammengesetzten Begriffen - Formel!)
- [ ] **Analyse** (H2, PFLICHT - 3-5 Mechanismen, graduiert)
- [ ] **Anwendung** (H2, optional - Advocatus Diaboli)
- [ ] **Belege** (H2 - mind. 2 Zitate/Beispiele)
- [ ] **Abgrenzung** (H2, optional - Kontext-Abhängigkeit zeigen)

**INHALT ✓**
- [ ] Definition präzise & vollständig (5 Fragen beantwortet?)
- [ ] Trennstriche nach Silben (nicht Morphemen!)
- [ ] **Geschichte erzählt die Biographie** des Begriffs
- [ ] **Geschichte: Fettdruck** für Anker-Daten (Jahr, Name, Kontext)
- [ ] Konstruktion erklärt Wortbestandteile (Formel: A + B = C)
- [ ] Analyse: 3-5 relevante Mechanismen aus [Werkzeugkasten](WERKZEUGKASTEN.md)
- [ ] Analyse: Begründung zeigt WIE (nicht nur DASS)
- [ ] Graduierung: `●` (dominant), `◐` (teilweise)
- [ ] Anwendung zeigt Sprecher-Perspektive (Advocatus Diaboli)
- [ ] Belege authentisch, chronologisch
- [ ] Begriff mit `==Begriff==` hervorgehoben
- [ ] **Politisch:** Primärquellen mit [@citekey]
- [ ] **Vulgär:** Verwendungsbeispiele
- [ ] Abgrenzung zeigt legitime Verwendungen (wenn vorhanden)

**STIL ✓**
- [ ] Fließende Prosa (Read-Aloud Test bestanden?)
- [ ] Verben der Manipulation ("tarnt", "verschleiert", "kriminalisiert")
- [ ] Keine Moral ("zynisch", "perfide" → raus!)
- [ ] Keine Superlative ("extrem", "massiv")

**TESTS ✓**
- [ ] **Clarity Test:** Verständlich für jemanden ohne Vorwissen?
- [ ] **Architecture Test:** Jede Sektion hat innere Logik?
- [ ] **Read-Aloud Test:** Fließt es beim Vorlesen?
- [ ] **Johnson Test:** So klar wie möglich, kein Wort mehr als nötig?

---

## 4. HÄUFIGE FEHLER

### Struktur
❌ Trennstriche fehlen in H1
❌ Konstruktion fehlt bei zusammengesetzten Begriffen
❌ Analyse fehlt (PFLICHT!)
❌ Anwendung bei politischen Begriffen fehlt (optional, aber empfohlen)
❌ Abgrenzung fehlt bei Begriffen mit legitimen Verwendungen

### Inhalt
❌ Definition zu kurz ("Reizwort für X." — Wirkung/Funktion fehlt!)
❌ **Geschichte als Datenliste** statt narrative Struktur
❌ **Geschichte ohne Fettdruck** für Anker-Daten
❌ **Analyse: Begründungen zu knapp** (zeigt DASS, nicht WIE)
❌ Begriff in Zitaten nicht mit `==Begriff==` markiert
❌ **Politisch:** Sekundärquellen (nur Original!)
❌ **Politisch:** Fehlende [@citekeys]

### Stil
❌ Moral in Definition ("zynisch", "perfide")
❌ Superlative ("unglaublich", "extrem")
❌ Telegraphischer Stil
❌ Prosa fließt nicht

---

## 5. WORKFLOW

**Schritt 1: Recherche**
- **Politisch:** [1-WEB-RECHERCHE-PROMPT.md](1-WEB-RECHERCHE-PROMPT.md) nutzen
- **Vulgär:** Kulturelle Recherche (Etymologie, Verwendung)

**Schritt 2: Template kopieren**
- Aus Abschnitt 1

**Schritt 3: Schreiben**
- **Definition:** 3-5 Sätze, beantworte die 5 Fragen
- **Trennstriche:** In H1 einfügen (nach Silben!)
- **Geschichte:** Erzähle die Geschichte (nicht Listen!), Fettdruck für Anker-Daten
- **Konstruktion:** Formel A + B = C (wenn zusammengesetzt)
- **Analyse:** 3-5 Mechanismen aus [Werkzeugkasten](WERKZEUGKASTEN.md), präzise Begründungen
- **Anwendung:** Advocatus Diaboli - warum verfängt das?
- **Belege:** Zitate eintragen (jedes auf eigener Zeile!), Begriff mit `==Begriff==`
- **Abgrenzung:** Legitime Verwendungen zeigen (wenn vorhanden)

**Schritt 4: Die vier Tests**
1. Clarity Test: Verständlich ohne Vorwissen?
2. Architecture Test: Jede Sektion hat Logik?
3. Read-Aloud Test: Fließt es?
4. Johnson Test: Klar, vollständig, kein Wort zu viel?

**Wenn ein Test fehlschlägt → überarbeiten.**

**Schritt 5: Checkliste durchgehen**

**Schritt 6: Citations verifizieren** (nur politisch)
```bash
python3 wort-fabrik/verify_citations.py
```

---

## 6. DIE PHILOSOPHIE HINTER DEN REGELN

### Warum keine "Max X Sätze" Regeln?

**Prinzip:** Klarheit > Kürze. Architektur > Arbiträre Limits.

**Ergebnis:** Fließende, präzise Prosa, die reveals statt nur describes.

### Warum "Hauptsätze, aber Subordination erlaubt"?

Ein gut platzierter Relativsatz ist besser als zwei holprige Hauptsätze.

**Prinzip:** Fluss > Dogma. Read-Aloud Test ist der Maßstab.

### Warum "Narrative Struktur" für Geschichte?

Ein Wörterbuch dokumentiert nicht nur Fakten, sondern offenbart Macht. Die Geschichte eines Kampfbegriffs zeigt die Absicht dahinter.

### Warum "Anwendung" (Advocatus Diaboli)?

Verhindert den Vorwurf der Parteilichkeit. Zeigt: Wir verstehen, warum Menschen diese Begriffe nutzen - aber wir zeigen auch, was sie bewirken.

### Warum "Abgrenzung"?

Zeigt Differenzierung. Nicht jede Verwendung eines Begriffs ist manipulativ. Kontext entscheidet.

### Die vier Tests: Warum?

Diese Tests ersetzen arbiträre Regeln mit **Prinzipien**.

---

**Ende der Vorlage v5.0**

*Lexikographie ist ein politischer Akt. Jede Definition ist eine Entscheidung. Handle entsprechend.*
