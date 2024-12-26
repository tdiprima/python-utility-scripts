#!/bin/bash
pythonFile="directory_creator.py"

dirPath="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
dirPath="$dirPath/$pythonFile"

python3 "$dirPath" "$@"
