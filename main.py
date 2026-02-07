from core.ui import header, menu
from modules.phone_osint import scan as phone_scan
from modules.username_osint import scan as username_scan
from modules.telegram_osint import telegram_lookup
from external.run_maigret import run as maigret_run
from external.run_holehe import run as holehe_run
from modules.inspector import run as inspector_run
from core.reporter import save as save_report

header("OSINT V5 ULTIMATE PRO")
menu()

c = input("Select: ")

if c == "1":
    phone = input("Phone: ")
    result = phone_scan(phone)
    print(result)

elif c == "2":
    username = input("Username: ")
    result = username_scan(username)
    print(result)

elif c == "3":
    phone = input("Phone Telegram: +62xxx ")
    result = telegram_lookup(phone)
    print(result)

elif c == "4":
    maigret_run()

elif c == "5":
    holehe_run()

elif c == "6":
    data = input("Masukkan data hasil scan untuk report: ")
    save_report(data)
    print("Report saved di folder reports")

elif c == "0":
    print("Exit...")

else:
    print("Menu tidak tersedia")
