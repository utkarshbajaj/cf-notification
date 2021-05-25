import requests
import json
import time

from master import SendUpdates

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

        for contest in list:
            print(contest)

        contestId = list[0]['id'];
        # contestId = 1525
        start = time.time();

        cont_url = 'https://codeforces.com/api/contest.ratingChanges?contestId=' + str(contestId)

        while True:
            response = requests.get(url)
            data = response.json()

            end = time.time()
            elapsed = end - start

            if(elapsed > 3 * oneday):
                break

            if(data['status'] == "FAILED" or len(data['result']) == 0):
                print("Trying again!")
                time.sleep(600)
                continue

            elif(data['status'] == 'OK'):
                break


        if elapsed > 3 * oneday:
            print("ERROR! Contest was faulty")
            continue



        send_updates = SendUpdates()

        send_updates.sendto(cont_url)

        print("Going to next contest now!")
        time.sleep(10);






if(__name__ == "__main__"):
    ans = contest_finder()
