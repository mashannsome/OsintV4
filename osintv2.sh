#!/bin/bash

green='\033[1;32m'
red='\033[1;31m'
cyan='\033[1;36m'
nc='\033[0m'

clear
cat banner.txt
echo ""

echo -e "${cyan}Modules Available:${nc}"
ls modules | nl
echo ""
echo "0. Exit"
echo ""

read -p "Pilih menu: " menu

if [ "$menu" == "0" ]; then
  exit
fi

file=$(ls modules | sed -n "${menu}p")

if [ -f "modules/$file" ]; then
  python3 modules/$file
else
  echo -e "${red}Module tidak ditemukan${nc}"
fi
