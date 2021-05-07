import requests
import json

def contest_finder():
    """Tells the contest to get the rating changes for"""

    while(True):
        url = "https://codeforces.com/api/contest.list?gym=false"

        response = requests.get(url)

        data = response.json()

        list = []

        for contest in data['result']:
            if contest["phase"] == "FINISHED":
                break
            if(contest["durationSeconds"] < 12500):
                list.append(contest['id'])

        if(len(list) == 0):
            time.sleep(7200)
            continue

        list.sort()

        # print("Contest for this time is " + str(list[0]))

        return list[0]
