#!/usr/bin/env bash

set -eu

./dev-init.sh

source ve/bin/activate

mypy test
