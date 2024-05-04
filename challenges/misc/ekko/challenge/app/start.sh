#!/bin/bash
/usr/local/bin/python3 -m gunicorn --workers 3 --bind 0.0.0.0:1337 app:app