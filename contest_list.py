import requests
import json
import time

oneday = 86400

def contest_finder():
    """Tells the contest to get the rating changes for"""

    url = "https://codeforces.com/api/contest.list?gym=false"

    while(True):
        response = requests.get(url)

        data = response.json()

        list = []

        for contest in data['result']:
            if contest["phase"] == "FINISHED":
                break
            if(contest["durationSeconds"] < 12500 and abs(contest['relativeTimeSeconds']) < 2 * oneday):
                list.append(contest['id'])

        if(len(list) == 0):
            print("Sleeping for one day")
            time.sleep(oneday)
            continue

        list.sort()

        # print("Contest for this time is " + str(list[0]))

        return list[0]

if(__name__ == "__main__"):
    contest_finder()
