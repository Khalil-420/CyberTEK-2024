#!/usr/bin/env bash

/usr/local/bin/python3 -m gunicorn -b 0.0.0.0:8000 main:app &