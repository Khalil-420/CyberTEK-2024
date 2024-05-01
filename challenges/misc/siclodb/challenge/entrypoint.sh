#!/bin/bash

while true; do
    socat TCP-LISTEN:1499,reuseaddr,fork SYSTEM:'sh keydb.sh'
done