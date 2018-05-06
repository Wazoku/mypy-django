#!/usr/bin/env bash

# This script sets up a development environment for checking for errors while
# editing type stubs in this project. mypy, pycodestyle, and
# python-language-server will be installed. Editors like Vim with ALE can then
# run these tools automatically.

set -eu

if ! [ -d ve ]; then
    python3.6 -m venv ve
fi

source ve/bin/activate

pip install pip==9.0.3
pip install -r test-requirements.txt
