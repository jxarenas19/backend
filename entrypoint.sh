#!/usr/bin/env bash

cd /usr/src/app/kmodels
python manage.py db upgrade
cd /usr/src/app/
flask run