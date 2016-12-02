#!/usr/bin/env bash

# Prepare db schema
python manage.py migrate --noinput

# Prepare log files and start outputting logs to STDOUT
mkdir /logs/
touch /logs/gunicorn.log
touch /logs/access.log
tail -n 0 -f /logs/*.log &

# Start Gunicorn processes
exec gunicorn dooz.wsgi:application \
    --name dooz \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/logs/gunicorn.log \
    --access-logfile=/logs/access.log \
    --timeout 3000 \
    --reload
