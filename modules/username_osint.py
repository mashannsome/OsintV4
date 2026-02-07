import requests
import time
from datetime import datetime

username = input("Masukkan username: ")

sites = {
    "Instagram": f"https://www.instagram.com/{username}",
    "GitHub": f"https://github.com/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Twitter": f"https://twitter.com/{username}",
    "Pinterest": f"https://www.pinterest.com/{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "Medium": f"https://medium.com/@{username}"
}

results = []
total = len(sites)
count = 0

print("\nScanning...\n")

for site, url in sites.items():
    try:
        r = requests.get(url, timeout=5)
        status = "FOUND" if r.status_code == 200 else "NOT FOUND"
    except:
        status = "ERROR"

    result = f"{site} : {status} : {url}"
    print(result)
    results.append(result)

    count += 1
    progress = int((count/total)*30)
    bar = "[" + "#"*progress + "-"*(30-progress) + "]"
    print(bar)
    time.sleep(0.3)

# Save HTML report
filename = f"reports/username_{username}.html"

with open(filename, "w") as f:
    f.write("<html><body><h2>OSINT Report</h2><ul>")
    for r in results:
        f.write(f"<li>{r}</li>")
    f.write("</ul></body></html>")

print("\nReport saved:", filename)
