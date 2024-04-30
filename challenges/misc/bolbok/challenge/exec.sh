#! /usr/bin/env bash

cd "$(mkdir /home/bolbok && dirname -- "/home/bolbok/ ${BASH_SOURCE[0]}")" || exit

PATH="/usr/bolbok/cmds/" exec /bin/rbash --norc --noprofile 2>&1