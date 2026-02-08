# Prompt: DIP → KONTEXT-MATERIAL

**Aufgabe:** Wähle die besten 8-10 Zitate aus `DIP-[Begriff].md` und formatiere sie als KONTEXT-MATERIAL für `3-DRAFT-THIS.md`.

**Input:** `DIP-[Begriff].md` (Output von `1-SCAN.py`)

**Output:** Ein KONTEXT-MATERIAL-Block zum direkten Einfügen in `3-DRAFT-THIS.md`.

---

## DIE 8 AUSWAHLKRITERIEN

**Grundsatz: Zitat-Qualität > Prominenz** — lieber ein gehaltvolles Zitat eines Hinterbänklers als ein banales Zitat eines Ministers.

---

### 1. Zitat-Qualität / Aussagekraft (Gewicht: Sehr hoch)

**Gut (verwenden):**
- Argumentativ: Erklärt warum der Begriff problematisch/richtig ist
- Konkret: Nennt Fakten, Zahlen, spezifische Beispiele
- Positionierung: Klare politische Einordnung erkennbar

**Schlecht (streichen):**
- Banal: "Das Thema wird diskutiert" / "Wir sollten darüber reden"
- Leer: Keine Argumentation, nur Behauptung
- Wiederholung: Sagt nur, was schon alle gesagt haben

✅ Gut: »Der Begriff ist zynisch, weil er verschleiert, dass 80% der EU-Zuwanderer arbeiten und Steuern zahlen« *(Argumentation + Zahl)*

❌ Banal: »Wir müssen über Sozialtourismus diskutieren« *(keine Position)*

---

### 2. Prominenz des Sprechers (Gewicht: Hoch, aber nachrangig!)

Rangfolge bei gleicher Qualität:
1. Bundeskanzler/Bundespräsident
2. Minister (Bundesregierung)
3. Staatssekretäre
4. Fraktionsvorsitzende
5. Bekannte Abgeordnete (langjährig, Ex-Minister)
6. Reguläre Abgeordnete

---

### 3. Art der Verwendung (Gewicht: Sehr hoch)

**Affirmativ** (Sprecher nutzt Begriff selbst → zeigt Etablierung):
- "Wir müssen X verhindern"
- "Das ist X"

**Kritisch** (Sprecher lehnt Begriff ab → zeigt Gegenwehr):
- "Der Begriff X ist falsch"
- "Das Unwort X stigmatisiert"

**PFLICHT: Mindestens 2-3 affirmative Zitate** — sonst fehlt die Etablierungsgeschichte.

---

### 4. Primär- vs. Sekundärzitat (Gewicht: Hoch)

**Primärzitat (bevorzugen):** Sprecher verwendet Begriff selbst, direkte Rede.

**Sekundärzitat (vermeiden):** "Merz sagte, es sei X" / indirekte Rede.

---

### 5. Klarheit der Verwendung (Gewicht: Mittel)

Begriff steht im Zentrum — nicht beiläufig, nicht verschachtelt.

✅ Gut: »Aber sie darf nicht zu einer Art „X" mit massiver Armutseinwanderung führen«

❌ Schlecht: »...und dann wurde auch das Thema X kurz angesprochen, wobei...«

---

### 6. Zitat-Länge: Kontext bevorzugen (Gewicht: Mittel)

Lieber **2-4 Sätze** mit Kontext als 1 Satz isoliert. Beim Schreiben kürzen wir — beim Sichten nicht.

✅ Gut: »Die Niederlassungsfreiheit müssen wir bewahren. Aber sie darf nicht zu einer Art „X" führen.« *(Kontext erkennbar)*

❌ Zu kurz: »Das ist X.« *(Wovon spricht er? Affirmativ oder sarkastisch?)*

---

### 7. Zeitliche Spreizung (Gewicht: Mittel)

Entwicklung des Begriffs zeigen:
- 1× Frühe Phase (Etablierung)
- 2-3× Hochphase
- 1× Aktuelle Verwendung

---

### 8. Kontext-Integrität (Gewicht: Sehr hoch)

Zitat darf nicht aus dem Zusammenhang gerissen sein.

❌ Problematisch: Sprecher sagt "Das ist KEIN X!" → Zitat zeigt "Das ist [...] X!"

---

## HÄUFIGE FEHLER

- ❌ Nur kritische Zitate → Etablierungsgeschichte fehlt
- ❌ Alle aus einem Jahr → keine zeitliche Entwicklung
- ❌ Sekundärzitate ("X sagte...") bevorzugt
- ❌ Banales Minister-Zitat statt gutem Hinterbänkler-Zitat

---

## OUTPUT-FORMAT (exakt einhalten!)

```markdown
## KONTEXT-MATERIAL (Bundestag-Recherche)

*[X] Zitate aus [Jahr]–[Jahr]. Faktische Grundlage für Phasen B und C. Belege-Sektion NICHT ausfüllen.*

### Affirmativ (Begriff wird verwendet)

1. **[Vorname Nachname]** ([Funktion/Partei], [JJJJ-MM-TT]): »[Zitat exakt wie in DIP-Datei]«
   `[citekey]` · BT [WP]/[Nr]

2. ...

### Kritisch / Metasprachlich

1. **[Vorname Nachname]** ([Funktion/Partei], [JJJJ-MM-TT]): »[Zitat exakt wie in DIP-Datei]«
   `[citekey]` · BT [WP]/[Nr]

2. ...

### BibTeX (für Zotero-Import)

```bibtex
[BibTeX-Einträge aller ausgewählten Zitate — exakt aus DIP-Datei kopieren]
```
```

---

## REGELN

- **Keine Begründungen** — nur Fakten, kein Meta-Kommentar
- **Zitate exakt** aus DIP-Datei (nicht kürzen, nicht paraphrasieren)
- **Citekeys + BibTeX** exakt aus DIP-Datei übernehmen
- **BibTeX-Format:** `note = {Plenarprotokoll WP/Nr}` — keine Seitenzahlen

---

## STARTE HIER

**Begriff:** [BEGRIFF EINSETZEN]

**Material:** [DIP-[Begriff].md einfügen]
