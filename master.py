import requests

response = requests.get('https://codeforces.com/api/contest.ratingChanges?contestId=1506')

data = response.json()

print(data["status"])

for user in data["result"]:
    if(user["handle"] == "lukesfather" or user["handle"] == "MananDahiya"):
        print(user["rank"])
