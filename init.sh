#!/usr/bin/env bash

FLASK_APP=app.py 

flask db init

flask db migrate -m "new tables"

flask db upgrade
