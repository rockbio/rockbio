#!/bin/bash

service rabbitmq-server start
sleep 5
pwd
cp configs/settings.py /usr/local/lib/python3.10/dist-packages/pynnotator/

export USE_DOCKER=yes
#cp rockbio/local_settings.docker.py rockbio/local_settings.py

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"#
python3 manage.py migrate

#hack to load the genes and diseases only once
if [ ! -f data/omim/loaded.txt ]; then
    python3 manage.py populate
    touch data/omim/loaded.txt
fi


export C_FORCE_ROOT='true'
# Start server
# echo "Starting annotator"
python3 manage.py celery &
# celery -A rockbio beat &
# celery -A rockbio worker -l debug -c 4 &

# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000