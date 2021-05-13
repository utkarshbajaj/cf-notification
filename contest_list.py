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
                list.append(contest)

        if(len(list) == 0):
            print("Sleeping for one day")
            time.sleep(oneday)
            continue

        list.sort(key = lambda x: x['startTimeSeconds'])

        # for contest in list:
        #     print(contest)

        return list[0]['id']

if(__name__ == "__main__"):
    ans = contest_finder()
