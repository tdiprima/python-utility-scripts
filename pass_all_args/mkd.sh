#!/bin/bash
pythonFile="mkd.py"

dirPath="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
dirPath="$dirPath/$pythonFile"

python3 "$dirPath" "$@"
