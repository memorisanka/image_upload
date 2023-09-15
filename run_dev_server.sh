#!/bin/sh

export PYTHONDONTWRITEBYTECODE=TRUE
export PYTHONUNBUFFERED=TRUE

#./docker/check_psql.sh

python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000