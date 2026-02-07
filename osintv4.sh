#!/bin/bash

green='\033[1;32m'
cyan='\033[1;36m'
red='\033[1;31m'
nc='\033[0m'

clear
cat banner.txt
echo ""
echo -e "${cyan}1.${nc} Phone OSINT"
echo -e "${cyan}2.${nc} Username OSINT"
echo -e "${cyan}3.${nc} Inspector"
echo -e "${cyan}4.${nc} Check Update"
echo -e "${cyan}0.${nc} Exit"
echo ""

read -p "Select menu: " menu

case $menu in
1) python3 modules/phone_osint.py ;;
2) python3 modules/username_osint.py ;;
3) python3 modules/inspector.py ;;
4) python3 modules/updater.py ;;
0) exit ;;
*) echo -e "${red}Invalid menu${nc}" ;;
esac
