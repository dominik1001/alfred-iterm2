#!/usr/bin/env bash

set -Eeuo pipefail

query="$1"

cd $HOME/Library/ApplicationSupport/iTerm2/Scripts/alfred2/alfred2/
x=$(python3 get_tabs.py | grep -i "$query")

items=""
while IFS= read -r app; do
  item="{\"uid\":\""$app"\", \"title\":\""$app"\", \"arg\":\""$app"\", \"valid\": true}"
  if [[ $items == "" ]]; then
    items="$item"
  else
    items="$items,$item"
  fi
done <<<"$x"

echo -e "{ \"items\": [$items]}"
