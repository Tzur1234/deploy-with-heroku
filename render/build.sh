#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

pip install django

pip install -r ./requirements/production.txt


python manage.py migrate

# exec /usr/local/bin/gunicorn config.wsgi --bind 0.0.0.0:80 --chdir=/app
