#!/bin/bash

echo "Installing OsintV3..."

pkg update -y
pkg install python git -y

pip install requests

mkdir reports

chmod +x osintv2.sh

echo "Install selesai"
echo "Run: bash osintv2.sh"
