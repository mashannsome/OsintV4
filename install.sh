#!/data/data/com.termux/files/usr/bin/bash
pkg update -y
pkg install python git -y
pip install -r requirements.txt
chmod +x osintv5.sh
pip install maigret
pip install holehe

echo "[+] Install selesai"
