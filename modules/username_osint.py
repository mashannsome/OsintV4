import requests
import concurrent.futures
import os
from datetime import datetime

# daftar situs (bisa ditambah lagi)
sites = {
    "Telegram": f"https://t.me/{username}",
    "Instagram": f"https://www.instagram.com/{username}",
    "GitHub": f"https://github.com/{username}",
    "Twitter/X": f"https://twitter.com/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "Pinterest": f"https://www.pinterest.com/{username}",
    "Medium": f"https://medium.com/@{username}",
    "Facebook": f"https://www.facebook.com/{username}",
    "YouTube": f"https://www.youtube.com/@{username}",
    "SoundCloud": f"https://soundcloud.com/{username}",
    "Vimeo": f"https://vimeo.com/{username}",
    "DeviantArt": f"https://www.deviantart.com/{username}",
    "GitLab": f"https://gitlab.com/{username}",
    "Bitbucket": f"https://bitbucket.org/{username}",
    "Kaggle": f"https://www.kaggle.com/{username}",
    "Replit": f"https://replit.com/@{username}",
    "BuyMeACoffee": f"https://www.buymeacoffee.com/{username}",
    "ProductHunt": f"https://www.producthunt.com/@{username}",
    "Linktree": f"https://linktr.ee/{username}"
}

results = []

def check(site, url):
    try:
        r = requests.get(url, timeout=7)
        if r.status_code == 200:
            status = "FOUND"
        else:
            status = "NOT FOUND"
    except:
        status = "ERROR"

    output = f"{site:<15} : {status} : {url}"
    print(output)
    results.append((site, status, url))

print("\nScanning username...\n")

# multi-thread agar cepat
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for site, url in sites.items():
        executor.submit(check, site, url)

# simpan report
os.makedirs("reports", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_html = f"reports/username_{username}_{timestamp}.html"

with open(file_html, "w") as f:
    f.write("<html><body>")
    f.write(f"<h2>Username OSINT Report: {username}</h2>")
    f.write("<table border='1' cellpadding='5'>")
    f.write("<tr><th>Site</th><th>Status</th><th>URL</th></tr>")

    for site, status, url in results:
        f.write(f"<tr><td>{site}</td><td>{status}</td><td>{url}</td></tr>")

    f.write("</table></body></html>")

print("\nReport saved:", file_html)
