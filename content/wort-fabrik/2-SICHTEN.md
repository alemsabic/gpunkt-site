# Prompt: DIP → KONTEXT-MATERIAL

**Aufgabe:** Wähle die besten 8-10 Zitate aus `DIP-[Begriff].md` und formatiere sie als KONTEXT-MATERIAL für `3-DRAFT-THIS.md`.

**Input:** `DIP-[Begriff].md` (Output von `1-SCAN.py`)

**Output:** Ein KONTEXT-MATERIAL-Block zum direkten Einfügen in `3-DRAFT-THIS.md`.

---

## AUSWAHLKRITERIEN (Priorität von oben nach unten)

1. **Zitat-Qualität** vor Prominenz — argumentativ > banal, auch wenn Hinterbänkler
2. **Primärzitat** bevorzugen — Sprecher nutzt Begriff selbst (nicht: "X sagte...")
3. **Balance** — min. 2-3 affirmative Verwendungen, Rest kritisch/metasprachlich
4. **Zeitliche Spreizung** — chronologisch verteilt über alle verfügbaren Jahre
5. **Klarheit** — Begriff im Zentrum, Kontext erkennbar, nicht beiläufig

**Faustregel:** Lieber 10 als 6 — beim Schreiben kürzen wir, nicht beim Sichten.

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
- **Citekeys** aus DIP-Datei übernehmen
- **BibTeX** aus DIP-Datei übernehmen (Format: `note = {Plenarprotokoll WP/Nr}`)

---

## BEISPIEL-OUTPUT

```markdown
## KONTEXT-MATERIAL (Bundestag-Recherche)

*9 Zitate aus 2014–2025. Faktische Grundlage für Phasen B und C. Belege-Sektion NICHT ausfüllen.*

### Affirmativ (Begriff wird verwendet)

1. **Wolfgang Schäuble** (Finanzminister/CDU, 2014-04-08): »Die Niederlassungsfreiheit in Europa müssen wir bewahren. Aber sie darf natürlich nicht zu einer Art „Sozialtourismus" mit massiver Armutseinwanderung führen.«
   `schaeuble_2014` · BT 18/28

2. **Olaf Scholz** (Bundeskanzler/SPD, 2025-01-30): »[Zitat]«
   `scholz_2025` · BT 21/XX

### Kritisch / Metasprachlich

1. **[Name]** ([Funktion], [JJJJ-MM-TT]): »[Zitat]«
   `[citekey]` · BT [WP]/[Nr]

### BibTeX (für Zotero-Import)

```bibtex
@misc{schaeuble_2014,
  title = {Rede im Deutschen Bundestag als Bundesminister der Finanzen},
  author = {Schäuble, Wolfgang},
  year = {2014},
  month = {4},
  day = {8},
  howpublished = {Plenarprotokoll 18/28, Deutscher Bundestag},
  url = {https://dserver.bundestag.de/btp/18/18028.pdf},
  note = {Plenarprotokoll 18/28}
}
```
```

---

## STARTE HIER

**Begriff:** [BEGRIFF EINSETZEN]

**Material:** [DIP-[Begriff].md einfügen]
