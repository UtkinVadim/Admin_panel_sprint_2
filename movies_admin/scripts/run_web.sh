#!/bin/sh

python manage.py collectstatic --no-input

echo "Waiting for postgres..."

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py migrate

gunicorn config.asgi:application --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker