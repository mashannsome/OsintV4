from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest, DeleteContactsRequest
from telethon.tl.types import InputPhoneContact
from colorama import Fore, Style
import time

api_id = 30687090
api_hash = "88b84f6d22ef565ba8615a6f4d1cb504"


def telegram_scan(phone):
    print(Fore.CYAN + "\n[+] Checking Telegram account..." + Style.RESET_ALL)

    try:
        with TelegramClient("session", api_id, api_hash) as client:

            contact = InputPhoneContact(
                client_id=0,
                phone=phone,
                first_name="Temp",
                last_name="OSINT"
            )

            result = client(ImportContactsRequest([contact]))

            if result.users:
                user = result.users[0]

                data = {
                    "status": "FOUND",
                    "id": user.id,
                    "name": user.first_name,
                    "username": user.username,
                    "bot": user.bot
                }

                print(Fore.GREEN + "\n===== TELEGRAM FOUND =====")
                for k, v in data.items():
                    print(f"{k:<10}: {v}")
                print("==========================\n")

                # hapus kontak
                client(DeleteContactsRequest(result.users))

                time.sleep(2)
                return data

            else:
                print(Fore.RED + "\nTidak ditemukan akun Telegram atau privasi disembunyikan\n")
                return {"status": "NOT FOUND"}

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return {"status": "ERROR"}
