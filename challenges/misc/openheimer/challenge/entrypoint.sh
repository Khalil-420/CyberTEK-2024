#!/bin/sh

while true; do
    socat TCP-LISTEN:1337,reuseaddr,fork SYSTEM:'/bin/sh openheimer.sh'
done