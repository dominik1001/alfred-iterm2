#!/usr/bin/env bash

set -Eeuo pipefail

#PATH="$PATH:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

query="$1"

cd $HOME/Library/ApplicationSupport/iTerm2/Scripts/alfred2/alfred2/
x=$(python3 alfred2.py | grep -i "$query")

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
