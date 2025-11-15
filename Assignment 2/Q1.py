import json
import requests

print("Yahya Shamim")
print("24k-0020")

# Load configurable endpoint
try:
    with open("apifetch.txt", "r") as file:
        url = file.read().strip()
except FileNotFoundError:
    print("file not found")
    exit()

#Robust error handling
try:
    response = requests.get(url)

    if response.status_code != 200:
        print(f"HTTP Error {response.status_code}")
        print(response.text)
        exit()

    data = response.json()

except requests.exceptions.RequestException as e:
    print("Network error:", e)
    exit()

#API status first
if data.get("status") != "success":
    print("API returned error:")
    print("Reason:", data.get("reason", "Unknown reason"))
    exit()

# Match display
for match in data.get("data", []):
    name = match.get("name", "Unknown match")
    status = match.get("status", "No status")
    venue = match.get("venue", "Unknown venue")
    date = match.get("date", "Unknown date")

    print(f"\n{name} -> {status} -> {venue} -> {date}")

    # nested score details
    if "score" in match and match["score"]:
        print("\nScore details:")
        for score in match["score"]:
            print("inning:", score.get("inning"))
            print("runs:", score.get("r"))
            print("wickets:", score.get("w"))
            print("overs:", score.get("o"))
            print()
    else:
        print("Score not avlbl for match.")
