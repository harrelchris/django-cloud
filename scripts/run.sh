#!/usr/bin/env bash

set -e

source .venv/bin/activate

python manage.py runserver
