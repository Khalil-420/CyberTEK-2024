#!/bin/sh

BLUE='\e[32m'
BLINK='\e[7m'
NC='\033[0m'

banner="
       _)        |             |  __ )  
   __|  |   __|  |   _ \    _\` |  __ \  
 \__ \  |  (     |  (   |  (   |  |   | 
 ____/ _| \___| _| \___/  \__,_| ____/             
"

echo "$banner"
echo "${BLUE}${BLINK}[*] Salve! welcome to keydb client 😸😸.${NC}"
keydb-server >/dev/null 2>&1
/home/ctf/setkeys.sh > /dev/null 2>&1
/home/ctf/challenge/siclodb