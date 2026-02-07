import os

def run(username):
    print("\n[+] Running Maigret...\n")
    os.system(f"python3 external/maigret/maigret.py {username}")
