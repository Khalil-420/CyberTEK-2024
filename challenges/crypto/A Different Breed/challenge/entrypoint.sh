#!/bin/bash
socat TCP-LISTEN:1337,fork,reuseaddr EXEC:"python3 chall.py",pty,stderr