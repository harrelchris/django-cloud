#!/usr/bin/env bash

set -e

source .venv/bin/activate

source .env

python -m gunicorn
