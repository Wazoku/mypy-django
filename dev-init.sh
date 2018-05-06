#!/usr/bin/env bash

set -eu

# This script sets up a development environment for checking for errors while
# editing type stubs in this project. mypy, pycodestyle, and
# python-language-server will be installed. Editors like Vim with ALE can then
# run these tools automatically.

if ! [ -d ve ]; then
    python3.6 -m venv ve
fi

ve/bin/pip install -q pip==9.0.3
ve/bin/pip install -qr test-requirements.txt
