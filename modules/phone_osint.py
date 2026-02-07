import requests
from datetime import datetime
import os
from colorama import Fore, Style, init

init(autoreset=True)

numverify_key = ("b82a9f21278d466c5251a0f384ce432b")
abstract_key = ("0a60a9ca70bc4b7e8f898e132c42d9a2")

def scan(phone):

    phone = phone.replace("+","").replace(" ","")

    print(Fore.CYAN + "\n========== PHONE OSINT ELITE ==========\n")

    hasil = {}

    # API 1 Numverify
    if numverify_key:
        try:
            url = f"https://api.apilayer.com/number_verification/validate?number={phone}"
            headers = {"apikey": numverify_key}

            res = requests.get(url, headers=headers, timeout=10)
            data = res.json()

            print("DEBUG Numverify:", data)

            if data.get("valid"):
                hasil = {
                    "Valid": data.get("valid"),
                    "Nomor": data.get("international_format"),
                    "Negara": data.get("country_name"),
                    "Kode Negara": data.get("country_code"),
                    "Lokasi": data.get("location") or "Tidak tersedia",
                    "Operator": data.get("carrier") or "Tidak tersedia",
                    "Tipe Line": data.get("line_type") or "Tidak tersedia",
                    "Sumber": "Numverify"
                }

        except Exception as e:
            print("Numverify error:", e)

    # API 2 Abstract
    if not hasil and abstract_key:
        try:
            url = f"https://phonevalidation.abstractapi.com/v1/?api_key={abstract_key}&phone={phone}"
            data = requests.get(url, timeout=10).json()

            print("DEBUG Abstract:", data)

            if data.get("valid"):
                hasil = {
                    "Valid": data.get("valid"),
                    "Nomor": data.get("format", {}).get("international"),
                    "Negara": data.get("country", {}).get("name"),
                    "Kode Negara": data.get("country", {}).get("code"),
                    "Lokasi": data.get("location") or "Tidak tersedia",
                    "Operator": data.get("carrier") or "Tidak tersedia",
                    "Tipe Line": data.get("type") or "Tidak tersedia",
                    "Sumber": "AbstractAPI"
                }

        except Exception as e:
            print("Abstract error:", e)

    if not hasil:
        print(Fore.RED + "\nGagal mendapatkan data dari semua API\n")
        return None

    print(Fore.GREEN + "\n========== HASIL ==========\n")

    for k, v in hasil.items():
        print(Fore.YELLOW + f"{k:<15}: " + Fore.WHITE + f"{v}")

    return hasil
