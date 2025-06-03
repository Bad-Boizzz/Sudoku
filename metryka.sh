#!/usr/bin/env bash
AUTHOR="dheczko"

echo
echo "==== Metryki Git dla autora: $AUTHOR ===="
echo

echo "1) Liczba commitów:"
git rev-list --all --count --author="$AUTHOR"
echo

echo "2) Liczba lokalnych gałęzi utworzonych przez $AUTHOR (pierwszy commit od niego):"
created=$(git for-each-ref --format="%(refname:short)" refs/heads \
  | while read BR; do
      first=$(git log --reverse --pretty="%an" "$BR" | head -n1)
      if [ "$first" = "$AUTHOR" ]; then
        echo "$BR"
      fi
    done | wc -l)
echo "   $created"
echo "   (lista gałęzi):"
git for-each-ref --format="%(refname:short)" refs/heads \
  | while read BR; do
      first=$(git log --reverse --pretty="%an" "$BR" | head -n1)
      if [ "$first" = "$AUTHOR" ]; then
        echo "   - $BR"
      fi
    done
echo

echo "3) Ostatni commit i gałęzie zawierające go:"
last_hash=$(git log --all --author="$AUTHOR" -n1 --pretty=format:"%H")
if [ -n "$last_hash" ]; then
  echo "   Last commit hash: $last_hash"
  echo "   Gałęzie zawierające ten commit:"
  git branch --contains "$last_hash"
else
  echo "   Brak commitów od $AUTHOR lub commit został usunięty."
fi
echo

echo "4) Liczba merge-commitów autorowanych przez $AUTHOR:"
git log --all --merges --author="$AUTHOR" --pretty=oneline | wc -l
echo

echo "5) Liczba dni aktywności (unikalne daty commitów):"
git log --all --author="$AUTHOR" --date=short --pretty=format:"%ad" \
  | sort -u | wc -l
echo

echo "============================================"
