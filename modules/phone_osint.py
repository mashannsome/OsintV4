from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest
from telethon.tl.types import InputPhoneContact
from colorama import Fore
from datetime import datetime
import os

api_id = 30687090
api_hash = "88b84f6d22ef565ba8615a6f4d1cb504"

operator_prefix = {
    "0811":"Telkomsel","0812":"Telkomsel","0813":"Telkomsel",
    "0821":"Telkomsel","0822":"Telkomsel","0852":"Telkomsel","0853":"Telkomsel",
    "0817":"XL","0818":"XL","0819":"XL","0859":"XL","0877":"XL","0878":"XL",
    "0831":"Axis","0832":"Axis","0833":"Axis","0838":"Axis",
    "0855":"Indosat","0856":"Indosat","0857":"Indosat","0858":"Indosat",
    "0881":"Smartfren","0882":"Smartfren","0883":"Smartfren","0884":"Smartfren",
    "0885":"Smartfren","0886":"Smartfren","0887":"Smartfren","0888":"Smartfren"
}

def detect_operator(phone):
    local = phone.replace("+62","0")
    return operator_prefix.get(local[:4], "Tidak diketahui")


def telegram_lookup(phone):
    try:
        with TelegramClient("session", api_id, api_hash) as client:
            contact = InputPhoneContact(0, phone, "Temp", "OSINT")
            result = client(ImportContactsRequest([contact]))

            if result.users:
                user = result.users[0]
                client(DeleteContactsRequest(id=[user.id]))

                return {
                    "Telegram":"FOUND",
                    "Username": user.username or "None",
                    "Name": user.first_name or ""
                }
            else:
                return {"Telegram":"NOT FOUND"}
    except:
        return {"Telegram":"ERROR"}


def whatsapp_possible(phone):
    if len(phone) >= 10 and phone.startswith("+62"):
        return "Likely"
    return "Unknown"


def risk_score(data):
    score = 0

    if data.get("Operator") != "Tidak diketahui":
        score += 30
    if data.get("Telegram") == "FOUND":
        score += 40
    if data.get("WhatsApp Possible") == "Likely":
        score += 20
    if data.get("Country") == "Indonesia":
        score += 10

    if score >= 70:
        return "Low"
    elif score >= 40:
        return "Medium"
    else:
        return "High"


def scan(phone):

    print(Fore.CYAN + "\n========== PHONE INTELLIGENCE ULTRA ==========\n")

    hasil = {}

    # format nomor
    if phone.startswith("0"):
        phone = "+62" + phone[1:]
    elif phone.startswith("62"):
        phone = "+" + phone

    hasil["Phone"] = phone

    # country
    hasil["Country"] = "Indonesia" if phone.startswith("+62") else "Unknown"

    # operator
    hasil["Operator"] = detect_operator(phone)

    # telegram
    hasil.update(telegram_lookup(phone))

    # whatsapp heuristic
    hasil["WhatsApp Possible"] = whatsapp_possible(phone)

    # risk score
    hasil["Risk Score"] = risk_score(hasil)

    # OUTPUT
    print(Fore.GREEN + "\n========== HASIL ==========\n")
    for k,v in hasil.items():
        print(f"{k:<18}: {v}")

    # SAVE REPORT
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    txt_file = f"reports/phone_{phone}_{timestamp}.txt"
    html_file = f"reports/phone_{phone}_{timestamp}.html"

    with open(txt_file,"w") as f:
        for k,v in hasil.items():
            f.write(f"{k}: {v}\n")

    with open(html_file,"w") as f:
        f.write("<html><body><h2>Phone Intelligence Report</h2><table border='1'>")
        for k,v in hasil.items():
            f.write(f"<tr><td>{k}</td><td>{v}</td></tr>")
        f.write("</table></body></html>")

    print(Fore.CYAN + f"\nReport TXT  : {txt_file}")
    print(Fore.CYAN + f"Report HTML : {html_file}")

    return hasil
