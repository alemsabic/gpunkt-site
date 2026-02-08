#!/usr/bin/env python3
"""
DIP Discovery v3 - Hybrid-Suche: JSON-Text-Scan + XML-Parsing nur für Treffer

Verbesserungen gegenüber v2:
- Einmaliger Durchlauf über ALLE verfügbaren BT-Protokolle (kein manueller Datumsbereich)
- Nutzt /plenarprotokoll-text für schnellen Text-Scan (kein XML für Nicht-Treffer)
- XML-Parsing nur für Protokolle, die den Begriff tatsächlich enthalten
- Max. 5 Treffer pro Jahr (verhindert Dominanz einzelner "heißer" Jahre)
- Deduplizierung (gleicher Sprecher + Datum = ein Eintrag)
- Seitenanzeige entfernt (irrelevant seit einheitlichem BibTeX-Format)
- Ein Output-File: DIP-[Begriff].md

USAGE:
    python3 bundestag_recherche.py "Begriff"
    python3 bundestag_recherche.py "Begriff" 2010  # optional: Startjahr

BEISPIELE:
    python3 bundestag_recherche.py "Sozialtourismus"
    python3 bundestag_recherche.py "Remigration" 2018
"""

import sys
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import re
from datetime import datetime

API_KEY = "OSOegLs.PR2lwJ1dwCeje9vTj7FPOt3hvpYKtwKkhw"
BASE_URL = "https://search.dip.bundestag.de/api/v1"
MAX_PER_YEAR = 5  # Maximal 5 Treffer pro Jahr


def generate_citekey(nachname, jahr):
    """Generiert Citekey: nachname_jahr (lowercase, keine Umlaute)"""
    nachname_clean = nachname.lower()
    nachname_clean = nachname_clean.replace('ä', 'ae').replace('ö', 'oe')
    nachname_clean = nachname_clean.replace('ü', 'ue').replace('ß', 'ss')
    nachname_clean = re.sub(r'[^a-z]', '', nachname_clean)
    return f"{nachname_clean}_{jahr}"


def extract_context_around_paragraph(rede_elem, target_p, term):
    """Extrahiert Ziel-Absatz + ggf. nächsten kurzen Absatz als Kontext."""
    paragraphs = []
    found = False

    for p in rede_elem.findall('.//p'):
        if p.get('klasse') not in ['J', 'J_1', 'O']:
            continue
        text = ' '.join(''.join(p.itertext()).split()).strip()
        if p == target_p:
            found = True
            paragraphs.append(text)
        elif found and len(paragraphs) == 1:
            if len(text) < 300:
                paragraphs.append(text)
            break

    context = '  '.join(paragraphs)
    if context and not context.endswith(('.', '!', '?', '»', '"')):
        context += '.'
    return context


def parse_xml_for_term(xml_url, term):
    """
    Parst XML-Protokoll und gibt alle Reden zurück, die den Begriff enthalten.
    Gibt strukturierte Daten mit Sprecher, Rolle, Kontext zurück.
    """
    try:
        with urllib.request.urlopen(xml_url, timeout=30) as response:
            xml_data = response.read()
        root = ET.fromstring(xml_data)
        results = []

        for rede in root.findall('.//rede'):
            redner_elem = rede.find('.//redner')
            if redner_elem is None:
                continue

            name_elem = redner_elem.find('name')
            if name_elem is None:
                continue

            vorname_e = name_elem.find('vorname')
            nachname_e = name_elem.find('nachname')
            fraktion_e = name_elem.find('fraktion')
            rolle_e = name_elem.find('rolle/rolle_lang')

            vorname = vorname_e.text if vorname_e is not None else ""
            nachname = nachname_e.text if nachname_e is not None else "Unbekannt"
            fraktion = fraktion_e.text if fraktion_e is not None else ""
            rolle = ' '.join(rolle_e.text.split()) if rolle_e is not None else ""

            # Suche Begriff in Absätzen
            for p in rede.findall('.//p'):
                if p.get('klasse') not in ['J', 'J_1', 'O']:
                    continue
                text = ''.join(p.itertext())
                if term.lower() in text.lower():
                    context = extract_context_around_paragraph(rede, p, term)
                    results.append({
                        'vorname': vorname,
                        'nachname': nachname,
                        'fraktion': fraktion,
                        'rolle': rolle,
                        'context': context,
                    })
                    break  # Nur ersten Treffer pro Rede

        return results

    except Exception as e:
        print(f"  ⚠️  XML-Fehler: {e}", file=sys.stderr)
        return []


def generate_bibtex(nachname, vorname, jahr, monat, tag, wp, dok_nr, pdf_url, citekey, rolle=""):
    """Generiert BibTeX-Eintrag (einheitliches Format, keine Seitenzahlen)."""
    titel = f"Rede im Deutschen Bundestag als {rolle}" if rolle else "Rede im Deutschen Bundestag"
    note = f"Plenarprotokoll {wp}/{dok_nr}"
    return f"""@misc{{{citekey},
  title = {{{titel}}},
  author = {{{nachname}, {vorname}}},
  year = {{{jahr}}},
  month = {{{monat}}},
  day = {{{tag}}},
  howpublished = {{Plenarprotokoll {wp}/{dok_nr}, Deutscher Bundestag}},
  url = {{{pdf_url}}},
  note = {{{note}}}
}}"""


def scan_all_protocols(term, start_year=2000):
    """
    Schritt 1: Scannt alle BT-Plenarprotokolle via plenarprotokoll-text.
    Gibt Liste der Protokolle zurück, die den Begriff enthalten.
    """
    print(f"🔍 Scanne alle BT-Protokolle ab {start_year} nach »{term}«...", file=sys.stderr)

    matching = []
    cursor = None
    checked = 0
    start_date = f"{start_year}-01-01"

    params = {
        "f.zuordnung": "BT",
        "f.datum.start": start_date,
        "format": "json",
        "apikey": API_KEY,
        "limit": 50,
    }

    while True:
        if cursor:
            params["cursor"] = cursor

        query = urllib.parse.urlencode(params)
        url = f"{BASE_URL}/plenarprotokoll-text?{query}"

        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            print(f"  ❌ API-Fehler: {e}", file=sys.stderr)
            break

        documents = data.get("documents", [])
        cursor = data.get("cursor")
        total = data.get("numFound", 0)

        if not documents:
            break

        checked += len(documents)
        print(f"  📄 {checked}/{total} Protokolle gescannt, {len(matching)} Treffer...", file=sys.stderr)

        for doc in documents:
            text = doc.get("text", "")
            if term.lower() in text.lower():
                fundstelle = doc.get("fundstelle", {})
                xml_url = fundstelle.get("xml_url")
                if xml_url:
                    matching.append({
                        "datum": doc.get("datum", ""),
                        "xml_url": xml_url,
                        "pdf_url": fundstelle.get("pdf_url", ""),
                        "wahlperiode": str(doc.get("wahlperiode", "?")),
                        "dokumentnummer": str(doc.get("dokumentnummer", "?")).split("/")[-1],
                    })

        if not cursor:
            break

    print(f"  ✅ Scan abgeschlossen: {len(matching)} Protokolle mit »{term}«", file=sys.stderr)
    return sorted(matching, key=lambda x: x["datum"])


def extract_quotes(term, matching_protocols):
    """
    Schritt 2: XML-Parsing nur für Treffer-Protokolle.
    Gibt alle Zitate zurück, dedupliziert und pro Jahr gecappt.
    """
    print(f"\n📖 Extrahiere Zitate aus {len(matching_protocols)} Protokollen...", file=sys.stderr)

    all_quotes = []
    seen = set()  # Deduplizierung: (nachname, datum)
    year_counts = {}  # Per-Jahr-Zähler

    for proto in matching_protocols:
        datum = proto["datum"]
        try:
            dt = datetime.strptime(datum, "%Y-%m-%d")
            jahr = dt.year
            monat = dt.month
            tag = dt.day
        except Exception:
            continue

        # Per-Jahr-Cap prüfen
        if year_counts.get(jahr, 0) >= MAX_PER_YEAR:
            continue

        results = parse_xml_for_term(proto["xml_url"], term)

        for r in results:
            nachname = r["nachname"]
            key = (nachname.lower(), datum)
            if key in seen:
                continue
            seen.add(key)

            citekey = generate_citekey(nachname, jahr)
            wp = proto["wahlperiode"]
            dok_nr = proto["dokumentnummer"]

            sprecher_info = r["rolle"] if r["rolle"] else r["fraktion"]

            all_quotes.append({
                "datum": datum,
                "jahr": jahr,
                "monat": monat,
                "tag": tag,
                "vorname": r["vorname"],
                "nachname": nachname,
                "fraktion": r["fraktion"],
                "rolle": r["rolle"],
                "sprecher_info": sprecher_info,
                "context": r["context"],
                "citekey": citekey,
                "wp": wp,
                "dok_nr": dok_nr,
                "pdf_url": proto["pdf_url"],
            })

            year_counts[jahr] = year_counts.get(jahr, 0) + 1

            if year_counts[jahr] >= MAX_PER_YEAR:
                break  # Nächstes Protokoll

    return sorted(all_quotes, key=lambda x: x["datum"])


def write_output(term, quotes):
    """Schreibt strukturierten Output für AI-Sichtung."""
    lines = []
    lines.append(f"# DIP-Recherche: {term}")
    lines.append(f"**Durchsucht:** Alle BT-Plenarprotokolle")
    lines.append(f"**Treffer:** {len(quotes)} Zitate")
    lines.append(f"**Max. pro Jahr:** {MAX_PER_YEAR}")
    lines.append("")
    lines.append("---")
    lines.append("")

    current_year = None
    for i, q in enumerate(quotes, 1):
        if q["jahr"] != current_year:
            current_year = q["jahr"]
            lines.append(f"## {current_year}")
            lines.append("")

        sprecher = f"{q['vorname']} {q['nachname']}"
        if q["sprecher_info"]:
            sprecher += f" ({q['sprecher_info']})"

        lines.append(f"### Treffer {i}: {q['datum']}")
        lines.append(f"**Sprecher:** {sprecher}")
        lines.append(f"**Protokoll:** {q['wp']}/{q['dok_nr']}")
        lines.append(f"**PDF:** {q['pdf_url']}")
        lines.append("")
        lines.append(f"»{q['context']}«")
        lines.append("")
        lines.append(f"**Citekey:** `{q['citekey']}`")
        lines.append("")
        lines.append("```bibtex")
        lines.append(generate_bibtex(
            q["nachname"], q["vorname"], q["jahr"], q["monat"], q["tag"],
            q["wp"], q["dok_nr"], q["pdf_url"], q["citekey"], q["rolle"]
        ))
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Alle BibTeX am Ende
    lines.append("## Alle BibTeX-Einträge")
    lines.append("")
    lines.append("```bibtex")
    for q in quotes:
        lines.append(generate_bibtex(
            q["nachname"], q["vorname"], q["jahr"], q["monat"], q["tag"],
            q["wp"], q["dok_nr"], q["pdf_url"], q["citekey"], q["rolle"]
        ))
        lines.append("")
    lines.append("```")

    return "\n".join(lines)


if __name__ == "__main__":
    import os

    if len(sys.argv) < 2:
        print("Usage: python3 bundestag_recherche.py \"Begriff\" [Startjahr]")
        sys.exit(1)

    term = sys.argv[1]
    start_year = int(sys.argv[2]) if len(sys.argv) > 2 else 2000

    # Output-Datei
    script_dir = os.path.dirname(os.path.abspath(__file__))
    recherche_dir = os.path.join(script_dir, "Recherche", term)
    os.makedirs(recherche_dir, exist_ok=True)
    output_file = os.path.join(recherche_dir, f"DIP-{term}.md")

    print(f"🚀 DIP-Recherche v3: »{term}« (ab {start_year})", file=sys.stderr)
    print(f"💾 Output: {output_file}", file=sys.stderr)
    print("", file=sys.stderr)

    # Schritt 1: Alle Protokolle scannen
    matching = scan_all_protocols(term, start_year)

    if not matching:
        print(f"⚠️  Keine Treffer für »{term}«", file=sys.stderr)
        sys.exit(0)

    # Schritt 2: Zitate extrahieren
    quotes = extract_quotes(term, matching)

    # Output schreiben
    output = write_output(term, quotes)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\n✅ Fertig: {len(quotes)} Zitate → {output_file}", file=sys.stderr)
