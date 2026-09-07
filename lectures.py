import requests, sys

ALIAS = "nuigalwayweb"
VENUE = "9167eab0dc78437c93c76b57"

def room_link(name: str) -> str | None:
    r = requests.get(f"https://api.mapsindoors.com/{ALIAS}/api/locations",
                     params={"q": name, "take": 10}, timeout=10)
    r.raise_for_status()

    loc = r.json()[0]
    print(loc)
    if loc != None:
        return f"https://clients.mapsindoors.com/{ALIAS}/{VENUE}/details/{loc['id']}"
    return None

print(room_link(sys.argv[1]))
