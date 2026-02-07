import requests

print("Checking update...")

try:
    r = requests.get("https://raw.githubusercontent.com/USERNAME/OsintV4/main/version.txt")
    latest = r.text.strip()
    print("Latest version:", latest)
except:
    print("Tidak bisa cek update")
