#!/bin/bash

BLUE='\e[32m'
BLINK='\e[7m'
NC='\033[0m'

banner="
       _)        |             |  __ )  
   __|  |   __|  |   _ \    _\` |  __ \  
 \__ \  |  (     |  (   |  (   |  |   | 
 ____/ _| \___| _| \___/  \__,_| ____/             
"

echo -e "$banner"
echo -e "${BLUE}${BLINK}[*] salve! welc to keydb 😸😸.${NC}"
keydb-server >/dev/null 2>&1
/home/ctf/challenge/setkeys.sh > /dev/null 2>&1
/home/ctf/challenge/siclodb