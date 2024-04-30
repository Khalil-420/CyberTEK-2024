#!/bin/bash
socat TCP-LISTEN:8001,fork,reuseaddr EXEC:"python3 chall.py",pty,stderr