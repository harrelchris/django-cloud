#!/usr/bin/env bash

set -e

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

if [ ! -f ".env" ]; then
    cp dev.env .env
fi

source .env

set +e
dropdb $POSTGRES_DB
dropuser $POSTGRES_USER
set -e

createuser $POSTGRES_USER
createdb $POSTGRES_DB --owner=$POSTGRES_USER

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput --username user --email user@email.com
