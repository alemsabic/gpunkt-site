#!/usr/bin/env python3
"""
DIP Discovery v2 - Strukturiertes XML-Parsing + automatischer BibTeX-Export

Verbesserungen gegenüber v1:
- Nutzt XML-Struktur statt \n\n-Heuristik
- 100% korrekte Sprecher-Zuordnung
- Automatischer BibTeX-Export (Citekey-Standard: nachname_jahr)
- Extrahiert Seiten-Nummern aus XML
- Erkennt Rollen (Minister, Abgeordneter, etc.)
"""

import sys
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import re
from datetime import datetime

API_KEY = "OSOegLs.PR2lwJ1dwCeje9vTj7FPOt3hvpYKtwKkhw"
BASE_URL = "https://search.dip.bundestag.de/api/v1/plenarprotokoll"

def generate_citekey(nachname, jahr):
    """Generiert Citekey im Standard-Format: nachname_jahr (lowercase)"""
    nachname_clean = nachname.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    nachname_clean = re.sub(r'[^a-z]', '', nachname_clean)
    return f"{nachname_clean}_{jahr}"

def extract_text_from_rede(rede_elem):
    """Extrahiert vollständigen Text aus <rede>-Element"""
    texts = []
    for p in rede_elem.findall('.//p'):
        if p.get('klasse') in ['J', 'J_1', 'O']:  # Haupttext-Absätze
            text = ''.join(p.itertext())
            # Bereinige Whitespace: Zeilenumbrüche durch Leerzeichen ersetzen
            text = ' '.join(text.split())
            texts.append(text.strip())
    return ' '.join(texts)

def extract_page_mapping(root):
    """Extrahiert Mapping rede_id → (Seitenzahl, Seitenbereich) aus Inhaltsverzeichnis"""
    page_map = {}
    for ivz_eintrag in root.findall('.//ivz-eintrag'):
        xref = ivz_eintrag.find('.//xref[@ref-type="rede"]')
        if xref is not None:
            rid = xref.get('rid')
            seite_elem = xref.find('.//seite')
            bereich_elem = xref.find('.//seitenbereich')

            if seite_elem is not None and rid:
                seite = seite_elem.text
                bereich = bereich_elem.text if bereich_elem is not None else ""
                page_map[rid] = (seite, bereich)
    return page_map

def parse_xml_protocol(xml_url, term):
    """Parst XML-Protokoll und findet Reden mit Begriff"""
    try:
        with urllib.request.urlopen(xml_url) as response:
            xml_data = response.read()

        root = ET.fromstring(xml_data)

        # Extrahiere Seitenzahlen-Mapping aus Inhaltsverzeichnis
        page_map = extract_page_mapping(root)

        results = []

        # Finde alle <rede>-Elemente
        for rede in root.findall('.//rede'):
            rede_id = rede.get('id')

            # Hole Seitenzahl + Bereich aus Mapping
            page_info = page_map.get(rede_id, (None, None))
            seite, bereich = page_info

            # Finde <redner> innerhalb der Rede
            redner_elem = rede.find('.//redner')
            if redner_elem is None:
                continue

            # Extrahiere Sprecher-Daten
            name_elem = redner_elem.find('name')
            vorname = name_elem.find('vorname').text if name_elem.find('vorname') is not None else ""
            nachname = name_elem.find('nachname').text if name_elem.find('nachname') is not None else "Unbekannt"

            # Fraktion (falls vorhanden)
            fraktion_elem = name_elem.find('fraktion')
            fraktion = fraktion_elem.text if fraktion_elem is not None else ""

            # Rolle (falls vorhanden, z.B. Minister) - bereinige Whitespace
            rolle_elem = name_elem.find('rolle/rolle_lang')
            rolle = ' '.join(rolle_elem.text.split()) if rolle_elem is not None else ""

            # Extrahiere Redetext
            redetext = extract_text_from_rede(rede)

            # Prüfe, ob Begriff im Text vorkommt
            if term.lower() in redetext.lower():
                # Finde Kontext (Satz mit Begriff)
                sentences = redetext.split('.')
                context_sentence = ""
                for sentence in sentences:
                    if term.lower() in sentence.lower():
                        context_sentence = sentence.strip()
                        break

                results.append({
                    'vorname': vorname,
                    'nachname': nachname,
                    'fraktion': fraktion,
                    'rolle': rolle,
                    'rede_id': rede_id,
                    'seite': seite,
                    'bereich': bereich,
                    'redetext': redetext[:1000],  # Erste 1000 Zeichen
                    'context': context_sentence
                })

        return results

    except Exception as e:
        print(f"❌ Fehler beim XML-Parsing: {e}")
        return []

def generate_bibtex(nachname, vorname, jahr, monat, tag, wp, dok_nr, pdf_url, citekey, rolle="", seite=None, bereich=None):
    """Generiert BibTeX-Eintrag im Standard-Format"""
    # Titel basierend auf Rolle
    if rolle:
        titel = f"Rede im Deutschen Bundestag als {rolle}"
    else:
        titel = "Rede im Deutschen Bundestag"

    # Note: Seitenzahl + Bereich (falls vorhanden)
    if seite and bereich:
        note = f"Seite {seite}{bereich}"
    elif seite:
        note = f"Seite {seite}"
    else:
        note = "Seite XXXX % TODO: Seitenzahl manuell ergänzen"

    bibtex = f"""@misc{{{citekey},
  title = {{{titel}}},
  author = {{{nachname}, {vorname}}},
  year = {{{jahr}}},
  month = {{{monat}}},
  day = {{{tag}}},
  howpublished = {{Plenarprotokoll {wp}/{dok_nr}, Deutscher Bundestag}},
  url = {{{pdf_url}}},
  note = {{{note}}}
}}"""
    return bibtex

def search_dip_discovery_v2(term, start_date=None, end_date=None, max_protocols=100):
    """Hauptfunktion: Sucht Begriff in Bundestags-Protokollen (strukturiert)"""
    print(f"# DIP-Discovery v2: {term}")
    print(f"ℹ️  Strukturiertes XML-Parsing + BibTeX-Export + Pagination")
    print("")

    params = {
        "f.zuordnung": "BT",
        "f.dokumentart": "Plenarprotokoll",
        "format": "json",
        "apikey": API_KEY,
        "limit": 50  # Pro Seite
    }

    if start_date:
        params["f.datum.start"] = start_date
    if end_date:
        params["f.datum.end"] = end_date

    found_total = 0
    bibtex_entries = []
    cursor = None
    protocols_checked = 0

    try:
        # Pagination-Loop
        while protocols_checked < max_protocols:
            # Cursor für Pagination
            if cursor:
                params["cursor"] = cursor

            query_string = urllib.parse.urlencode(params)
            url = BASE_URL + "?" + query_string

            with urllib.request.urlopen(urllib.request.Request(url)) as response:
                data = json.loads(response.read().decode('utf-8'))
                documents = data.get("documents", [])
                cursor = data.get("cursor")  # Nächste Seite
                num_found = data.get("numFound", 0)

                if not documents:
                    print("ℹ️  Keine weiteren Protokolle gefunden.")
                    break

                protocols_checked += len(documents)
                print(f"🔍 Durchsuche Protokolle {protocols_checked - len(documents) + 1}-{protocols_checked} von {num_found} gesamt...")

                for doc in documents:
                    # Prüfe, ob XML verfügbar
                    fundstelle = doc.get("fundstelle", {})
                    xml_url = fundstelle.get("xml_url")

                    if not xml_url:
                        continue

                    # Parse XML
                    results = parse_xml_protocol(xml_url, term)

                    if results:
                        datum = doc.get("datum", "Unbekannt")
                        pdf_url = fundstelle.get("pdf_url", "Keine URL")
                        wp = str(doc.get("wahlperiode", "?"))
                        dok_nr = str(doc.get("dokumentnummer", "?")).replace(f"{wp}/", "")

                        # Datum parsen für BibTeX
                        try:
                            dt = datetime.strptime(datum, "%Y-%m-%d")
                            jahr = dt.year
                            monat = dt.month
                            tag = dt.day
                        except:
                            jahr, monat, tag = "XXXX", "XX", "XX"

                        for result in results:
                            found_total += 1

                            vorname = result['vorname']
                            nachname = result['nachname']
                            fraktion = result['fraktion']
                            rolle = result['rolle']
                            context = result['context']
                            seite = result.get('seite')
                            bereich = result.get('bereich')

                            # Generiere Citekey
                            citekey = generate_citekey(nachname, jahr)

                            # Sprecher-String
                            sprecher = f"{vorname} {nachname}"
                            if rolle:
                                sprecher += f" ({rolle})"
                            elif fraktion:
                                sprecher += f" ({fraktion})"

                            # Seiten-String
                            seiten_str = f"{seite}{bereich}" if seite and bereich else (seite if seite else "Unbekannt")

                            print(f"## Treffer {found_total}: {datum}")
                            print(f"**Sprecher:** {sprecher}")
                            print(f"**Wahlperiode:** {wp}/{dok_nr}")
                            print(f"**Seite:** {seiten_str}")
                            print(f"**PDF:** {pdf_url}")
                            print("")
                            print(f"**Zitat (Kontext):**")
                            print(f"»{context}«")
                            print("")
                            print(f"**Citekey:** `{citekey}`")
                            print("")

                            # Generiere BibTeX
                            bibtex = generate_bibtex(
                                nachname, vorname, jahr, monat, tag,
                                wp, dok_nr, pdf_url, citekey, rolle, seite, bereich
                            )
                            bibtex_entries.append(bibtex)

                            print("**BibTeX:**")
                            print("```bibtex")
                            print(bibtex)
                            print("```")
                            print("")
                            print("---")
                            print("")

                # Prüfe, ob weitere Seiten verfügbar
                if not cursor:
                    print("ℹ️  Alle verfügbaren Protokolle durchsucht.")
                    break

        # Zusammenfassung
        print("")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"✅ {found_total} Treffer gefunden in {protocols_checked} Protokollen")
        print("")

        if bibtex_entries:
            print("📚 **Alle BibTeX-Einträge:**")
            print("```bibtex")
            for entry in bibtex_entries:
                print(entry)
                print("")
            print("```")

    except Exception as e:
        print(f"❌ Fehler: {e}")

if __name__ == "__main__":
    import os

    term = sys.argv[1] if len(sys.argv) > 1 else "Sozialtourismus"
    start_date = sys.argv[2] if len(sys.argv) > 2 else "2013-01-01"
    end_date = sys.argv[3] if len(sys.argv) > 3 else None
    max_protocols = int(sys.argv[4]) if len(sys.argv) > 4 else 200  # Default: 200 Protokolle

    # Output-Datei automatisch generieren
    script_dir = os.path.dirname(os.path.abspath(__file__))
    recherche_dir = os.path.join(script_dir, "Recherche")
    os.makedirs(recherche_dir, exist_ok=True)

    date_suffix = f"-{start_date}"
    if end_date:
        date_suffix += f"-{end_date}"

    output_file = os.path.join(recherche_dir, f"DIP-{term}{date_suffix}.md")

    date_range = f"{start_date} bis {end_date}" if end_date else f"ab {start_date}"
    print(f"🔍 Starte Suche nach '{term}' {date_range} (max. {max_protocols} Protokolle)")
    print(f"💾 Output: {output_file}")
    print("")

    # Redirect stdout to file
    original_stdout = sys.stdout
    with open(output_file, 'w', encoding='utf-8') as f:
        sys.stdout = f
        search_dip_discovery_v2(term, start_date, end_date, max_protocols)

    sys.stdout = original_stdout
    print(f"✅ Recherche gespeichert: {output_file}")
