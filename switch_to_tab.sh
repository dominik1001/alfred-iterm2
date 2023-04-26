#!/usr/bin/env bash

set -Eeuo pipefail

#PATH="$PATH:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

query="$1"

cd $HOME/Library/ApplicationSupport/iTerm2/Scripts/alfred2/alfred2/
x=$(python3 switch_to_tab.py "$query")
