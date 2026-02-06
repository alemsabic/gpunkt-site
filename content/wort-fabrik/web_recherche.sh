#!/bin/bash

# web_recherche.sh - Web-Recherche für einen Begriff
# Usage: ./web_recherche.sh "Begriff"

set -e  # Exit on error

# Check argument
if [ -z "$1" ]; then
  echo "❌ Fehler: Kein Begriff angegeben"
  echo ""
  echo "Usage: ./web_recherche.sh \"Begriff\""
  echo "Beispiel: ./web_recherche.sh \"Remigration\""
  exit 1
fi

BEGRIFF="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RECHERCHE_DIR="$SCRIPT_DIR/Recherche"
MODEL="gemini-3-pro-preview"

# Create directory if needed
mkdir -p "$RECHERCHE_DIR"

# Output file
OUTPUT_FILE="$RECHERCHE_DIR/WEB-$BEGRIFF.md"

echo ""
echo "🌐 Web-Recherche für: '$BEGRIFF'"
echo "ℹ️  Model: $MODEL"
echo "💾 Output: $OUTPUT_FILE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Replace [BEGRIFF HIER EINSETZEN] and pipe to gemini
sed "s/\[BEGRIFF HIER EINSETZEN\]/$BEGRIFF/g" "$SCRIPT_DIR/WEB-RECHERCHE-PROMPT.md" | \
  gemini --model "$MODEL" > "$OUTPUT_FILE"

if [ ! -s "$OUTPUT_FILE" ]; then
  echo "❌ Fehler: Output ist leer"
  exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Web-Recherche abgeschlossen!"
echo ""
echo "📄 Output: $OUTPUT_FILE"
echo "📊 Zeilen: $(wc -l < "$OUTPUT_FILE")"
echo ""
echo "🔍 Nächste Schritte:"
echo "   1. Öffnen: open \"$OUTPUT_FILE\""
echo "   2. Triple-Verification durchführen"
echo "   3. Beste 3-5 Zitate markieren"
echo ""
