#!/bin/bash

while true; do
    socat TCP-LISTEN:13337,reuseaddr,fork SYSTEM:'sh openheimer.sh'
done