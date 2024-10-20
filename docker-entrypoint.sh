#!/bin/sh
set -e
cd /src/

python manage.py migrate
python manage.py collectstatic --noinput

# Start supervisord
/usr/bin/supervisord -n -c /etc/supervisor/conf.d/supervisord.conf

