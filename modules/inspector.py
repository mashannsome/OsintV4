import requests


def run(target):
    print("\n===== INSPECTOR RESULT =====\n")

    try:
        url = f"http://ip-api.com/json/{target}"
        data = requests.get(url, timeout=10).json()

        for k, v in data.items():
            print(f"{k:<15}: {v}")

        return data

    except Exception as e:
        print("Error:", e)
        return None
