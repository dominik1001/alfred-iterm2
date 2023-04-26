#!/usr/bin/env bash

set -Eeuo pipefail

query="$1"

cd $HOME/Library/ApplicationSupport/iTerm2/Scripts/alfred2/alfred2/
x=$(python3 switch_to_tab.py "$query")
